#!/usr/bin/env python3
"""Deterministic repository operations for structured wxvideos documents."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import os
import re
import sys
import unicodedata
import uuid
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ACCOUNT_IDS = {"gzminge", "gzxzcs", "qycslc", "gzcktxpp", "tsxbj", "gzlxcs"}
CONTENT_FORMATS = {"text_broadcast", "spoken"}
CONTENT_ID_RE = re.compile(
    r"^wxv-(gzminge|gzxzcs|qycslc|gzcktxpp|tsxbj|gzlxcs)-(\d{8})-([0-9a-f]{8})$"
)
HISTORY_FIELDS = (
    "business_line",
    "theme",
    "content_type",
    "audience",
    "pain_scene",
    "content_goal",
    "region",
    "platform",
    "series",
    "source",
)
ARCHIVE_TEXT_FIELDS = ("summary", "audience_description", "pain_scene_description")
INVALID_FILENAME_CHARS = str.maketrans(
    {"<": "＜", ">": "＞", ":": "：", '"': "＂", "/": "／", "\\": "＼", "|": "｜", "?": "？", "*": "＊"}
)


# Core document and error models shared by every operation.
class OperationError(Exception):
    def __init__(self, status: str, *errors: str):
        super().__init__("; ".join(errors))
        self.status = status
        self.errors = list(errors)


@dataclass
class RepoDocument:
    path: Path
    text: str
    meta: dict[str, str]
    payload: dict[str, Any]
    final_body: str

    @property
    def account_id(self) -> str:
        return self.meta["account_id"]

    @property
    def content_id(self) -> str:
        return self.meta["content_id"]

    @property
    def final_title(self) -> str:
        return self.meta["final_title"]

    @property
    def publish_date(self) -> str:
        return self.meta["publish_date"]

    @property
    def content_format(self) -> str:
        return self.meta["content_format"]


# Parse and validate the structured Repo content document before any write.
def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].lstrip("\ufeff").strip() != "---":
        raise OperationError("invalid_document", "missing opening frontmatter fence")
    try:
        closing = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise OperationError("invalid_document", "missing closing frontmatter fence") from exc
    result: dict[str, str] = {}
    for line in lines[1:closing]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)", line)
        if not match:
            raise OperationError("invalid_document", f"unsupported frontmatter line: {line}")
        key, raw = match.groups()
        raw = raw.strip()
        if len(raw) >= 2 and raw[0] == raw[-1] == '"':
            try:
                raw = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise OperationError("invalid_document", f"invalid quoted frontmatter value: {key}") from exc
        elif len(raw) >= 2 and raw[0] == raw[-1] == "'":
            raw = raw[1:-1].replace("''", "'")
        result[key] = raw
    return result


def extract_section(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$\r?\n(?P<body>.*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise OperationError("invalid_document", f"missing section: {heading}")
    return match.group("body").strip()


def extract_operation_payload(text: str) -> dict[str, Any]:
    section = extract_section(text, "Repo 操作载荷")
    match = re.fullmatch(r"```json\s*(\{.*\})\s*```", section, re.DOTALL)
    if not match:
        raise OperationError("invalid_document", "Repo 操作载荷 must contain one JSON object")
    try:
        payload = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise OperationError("invalid_document", f"invalid Repo operation JSON: {exc.msg}") from exc
    if not isinstance(payload, dict):
        raise OperationError("invalid_document", "Repo operation payload must be an object")
    return payload


def require_uuid(value: Any, field: str) -> None:
    try:
        uuid.UUID(str(value))
    except (ValueError, AttributeError, TypeError) as exc:
        raise OperationError("invalid_document", f"{field} must be a UUID") from exc


def require_nonempty(mapping: dict[str, Any], names: tuple[str, ...], prefix: str = "") -> None:
    missing = [name for name in names if not isinstance(mapping.get(name), str) or not mapping[name].strip()]
    if missing:
        label = f"{prefix}." if prefix else ""
        raise OperationError("invalid_document", "missing fields: " + ", ".join(label + name for name in missing))


def validate_pending_actions(actions: Any, account_id: str) -> list[dict[str, Any]]:
    if not isinstance(actions, list):
        raise OperationError("invalid_document", "pending_repo_actions must be an array")
    validated: list[dict[str, Any]] = []
    expected_prefix = f"accounts/{account_id}/内容库/03-选题规划/推荐记录/"
    for index, action in enumerate(actions):
        if not isinstance(action, dict):
            raise OperationError("invalid_document", f"pending_repo_actions[{index}] must be an object")
        # Early Repo content documents stored one recommendation or feedback
        # event per action. Normalize that losslessly before applying the
        # current batched-event validation and sync path.
        if action.get("action_type") in {
            "append_topic_recommendation_event",
            "append_topic_feedback_event",
        }:
            payload = action.get("payload")
            if not isinstance(payload, dict):
                raise OperationError("invalid_document", f"pending_repo_actions[{index}].payload must be an object")
            action = dict(action)
            action["action_type"] = "append_topic_recommendation_events"
            action["source_schema"] = "shared/schemas/topic-recommendation-log-schema.md"
            action["events"] = [payload]
        if action.get("action_type") != "append_topic_recommendation_events":
            raise OperationError("invalid_document", f"unsupported pending action: {action.get('action_type')}")
        if action.get("source_schema") != "shared/schemas/topic-recommendation-log-schema.md":
            raise OperationError("invalid_document", "pending action source_schema is invalid")
        require_uuid(action.get("action_id"), f"pending_repo_actions[{index}].action_id")
        target = str(action.get("target_path", "")).replace("\\", "/")
        if not target.startswith(expected_prefix) or not re.fullmatch(
            re.escape(expected_prefix) + r"\d{4}-\d{2}\.jsonl", target
        ):
            raise OperationError("invalid_document", f"invalid pending action target: {target}")
        events = action.get("events")
        if not isinstance(events, list) or not events:
            raise OperationError("invalid_document", f"pending_repo_actions[{index}].events must be non-empty")
        for event_index, event in enumerate(events):
            if not isinstance(event, dict):
                raise OperationError("invalid_document", "pending event must be an object")
            require_uuid(event.get("event_id"), f"pending event {event_index}.event_id")
            if event.get("event_type") not in {"recommendation", "feedback"}:
                raise OperationError("invalid_document", "pending event_type must be recommendation or feedback")
            if event.get("account_id") != account_id:
                raise OperationError("invalid_document", "pending event account_id mismatch")
            if not isinstance(event.get("occurred_at"), str) or not event["occurred_at"].strip():
                raise OperationError("invalid_document", "pending event occurred_at is required")
            try:
                occurred_at = dt.datetime.fromisoformat(event["occurred_at"])
            except ValueError as exc:
                raise OperationError("invalid_document", "pending event occurred_at is invalid") from exc
            if occurred_at.strftime("%Y-%m") != Path(target).stem:
                raise OperationError("invalid_document", "pending event target month does not match occurred_at")
            if event["event_type"] == "recommendation":
                require_uuid(event.get("batch_id"), "recommendation.batch_id")
                topics = event.get("topics")
                if not isinstance(topics, list) or not topics:
                    raise OperationError("invalid_document", "recommendation.topics must be non-empty")
                for topic in topics:
                    if not isinstance(topic, dict):
                        raise OperationError("invalid_document", "recommendation topic must be an object")
                    require_uuid(topic.get("topic_id"), "recommendation.topic_id")
            else:
                if event.get("signal") != "selected":
                    raise OperationError("invalid_document", "Repo sync accepts only selected feedback events")
                require_uuid(event.get("batch_id"), "feedback.batch_id")
                topic_ids = event.get("topic_ids")
                if not isinstance(topic_ids, list) or len(topic_ids) != 1:
                    raise OperationError("invalid_document", "selected feedback must contain one topic_id")
                require_uuid(topic_ids[0], "feedback.topic_ids[0]")
        action = dict(action)
        action["target_path"] = target
        validated.append(action)
    return validated


def load_repo_document(path: Path) -> RepoDocument:
    if not path.is_file():
        raise OperationError("invalid_document", f"input file not found: {path}")
    text = path.read_text(encoding="utf-8-sig")
    meta = parse_frontmatter(text)
    required_meta = (
        "delivery_version",
        "document_type",
        "content_id",
        "account_id",
        "content_format",
        "approval_status",
        "confirmed_at",
        "publication_status",
        "publish_date",
        "requested_repo_action",
        "final_title",
        "topic_origin",
        "topic_feedback_status",
        "repo_sync_status",
    )
    require_nonempty(meta, required_meta)
    if meta["delivery_version"] != "1.1":
        raise OperationError("invalid_document", "delivery_version must be 1.1 for scripted sync")
    if meta["document_type"] != "repo_content":
        raise OperationError("invalid_document", "document_type must be repo_content")
    match = CONTENT_ID_RE.fullmatch(meta["content_id"])
    if not match:
        raise OperationError("invalid_document", "content_id format is invalid")
    if meta["account_id"] not in ACCOUNT_IDS or match.group(1) != meta["account_id"]:
        raise OperationError("invalid_document", "account_id does not match content_id")
    if meta["content_format"] not in CONTENT_FORMATS:
        raise OperationError("invalid_document", "content_format is invalid")
    if meta["approval_status"] != "confirmed_by_user":
        raise OperationError("invalid_document", "approval_status must be confirmed_by_user")
    if meta["publication_status"] != "published_by_user":
        raise OperationError("invalid_document", "publication_status must be published_by_user")
    if meta["requested_repo_action"] != "archive_published_content":
        raise OperationError("invalid_document", "requested_repo_action must be archive_published_content")
    if meta["repo_sync_status"] != "not_synced":
        raise OperationError("invalid_document", "repo_sync_status must be not_synced")
    try:
        dt.date.fromisoformat(meta["publish_date"])
        dt.datetime.fromisoformat(meta["confirmed_at"])
    except ValueError as exc:
        raise OperationError("invalid_document", "publish_date or confirmed_at is invalid") from exc
    if not path.name.startswith(f"Repo内容文档｜{meta['content_id']}｜") or not path.name.endswith(".md"):
        raise OperationError("invalid_document", "filename does not match Repo content document identity")

    payload = extract_operation_payload(text)
    if payload.get("schema_version") != "1.0" or payload.get("action") != "archive_published_content":
        raise OperationError("invalid_document", "unsupported Repo operation payload")
    for field in ("account_id", "content_id", "content_format", "publish_date", "final_title"):
        if payload.get(field) != meta[field]:
            raise OperationError("invalid_document", f"payload {field} does not match frontmatter")
    archive = payload.get("archive_metadata")
    if not isinstance(archive, dict):
        raise OperationError("invalid_document", "archive_metadata must be an object")
    require_nonempty(archive, HISTORY_FIELDS + ARCHIVE_TEXT_FIELDS, "archive_metadata")
    for list_field in ("extension_topics", "related_content"):
        value = archive.get(list_field)
        if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
            raise OperationError("invalid_document", f"archive_metadata.{list_field} must be a string array")
    payload["pending_repo_actions"] = validate_pending_actions(
        payload.get("pending_repo_actions", []), meta["account_id"]
    )
    if meta["topic_origin"] == "project_recommendation":
        for field in ("topic_id", "recommendation_batch_id", "feedback_event_id"):
            require_uuid(meta.get(field), field)
        if meta["topic_feedback_status"] not in {"pending", "synced"}:
            raise OperationError("invalid_document", "project recommendation feedback status is invalid")
        carried_events = [
            event
            for action in payload["pending_repo_actions"]
            for event in action["events"]
        ]
        if meta["topic_feedback_status"] == "pending":
            feedback = [event for event in carried_events if event.get("event_id") == meta["feedback_event_id"]]
            if (
                len(feedback) != 1
                or feedback[0].get("topic_ids") != [meta["topic_id"]]
                or feedback[0].get("batch_id") != meta["recommendation_batch_id"]
            ):
                raise OperationError("invalid_document", "pending selected feedback payload is missing or inconsistent")
        elif carried_events:
            raise OperationError("invalid_document", "synced topic feedback cannot contain pending actions")
    elif meta["topic_origin"] == "direct_user_input":
        if meta["topic_feedback_status"] != "not_applicable":
            raise OperationError("invalid_document", "direct input feedback status must be not_applicable")
        for field in ("topic_id", "recommendation_batch_id", "feedback_event_id"):
            if meta.get(field) not in {"null", ""}:
                raise OperationError("invalid_document", f"direct input {field} must be null")
        if payload["pending_repo_actions"]:
            raise OperationError("invalid_document", "direct input cannot contain pending recommendation actions")
    else:
        raise OperationError("invalid_document", "topic_origin is invalid")
    final_body = extract_section(text, "最终正文")
    if not final_body:
        raise OperationError("invalid_document", "final body is empty")
    return RepoDocument(path=path, text=text, meta=meta, payload=payload, final_body=final_body)


# Repository I/O helpers keep paths scoped, JSONL valid, and writes atomic.
def safe_repo_path(repo_root: Path, relative: str) -> Path:
    relative = relative.replace("\\", "/")
    if relative.startswith("/") or ".." in Path(relative).parts:
        raise OperationError("conflict", f"unsafe repository path: {relative}")
    target = (repo_root / Path(relative)).resolve()
    try:
        target.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise OperationError("conflict", f"path escapes repository: {relative}") from exc
    return target


def read_jsonl(path: Path) -> list[tuple[str, dict[str, Any]]]:
    if not path.exists():
        return []
    rows: list[tuple[str, dict[str, Any]]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise OperationError("conflict", f"invalid JSONL: {path} line {line_number}") from exc
        if not isinstance(value, dict):
            raise OperationError("conflict", f"JSONL row is not an object: {path} line {line_number}")
        rows.append((raw, value))
    return rows


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + f".{os.getpid()}.tmp")
    temp.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temp, path)


@contextmanager
def repository_lock(repo_root: Path):
    path = repo_root / ".wxv-ops.lock"
    try:
        descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise OperationError("conflict", "another wxv repository operation is active or left a stale lock") from exc
    try:
        os.write(descriptor, str(os.getpid()).encode("ascii"))
        os.close(descriptor)
        yield
    finally:
        path.unlink(missing_ok=True)


def compact_json(value: dict[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def canonical_json(value: dict[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def relative_repo_path(repo_root: Path, path: Path) -> str:
    return path.resolve().relative_to(repo_root.resolve()).as_posix()


def normalized_title(value: str) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFKC", value).casefold() if ch.isalnum())


def filename_title(title: str) -> str:
    result = title.translate(INVALID_FILENAME_CHARS).strip().rstrip(".")
    if not result:
        raise OperationError("invalid_document", "final_title cannot produce a valid filename")
    return result


def yaml_scalar(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


# Build the formal history note and resolve its account-scoped destination.
def build_history_text(document: RepoDocument) -> str:
    archive = document.payload["archive_metadata"]
    fields = {
        "content_id": document.content_id,
        "title": document.final_title,
        "status": "已发布",
        "publish_date": document.publish_date,
        **{name: archive[name].strip() for name in HISTORY_FIELDS},
        "content_format": document.content_format,
    }
    ordered = (
        "content_id", "title", "status", "publish_date", "business_line", "theme",
        "content_type", "content_format", "audience", "pain_scene", "content_goal",
        "region", "platform", "series", "source",
    )
    frontmatter = "\n".join(f"{name}: {yaml_scalar(fields[name])}" for name in ordered)
    extensions = archive["extension_topics"] or ["待根据发布后咨询问题补充"]
    related = archive["related_content"] or ["暂无直接关联内容"]
    extension_lines = "\n".join(f"- {item.strip()}" for item in extensions)
    related_lines = "\n".join(f"- {item.strip()}" for item in related)
    return (
        f"---\n{frontmatter}\n---\n\n"
        f"# {document.final_title}\n\n"
        f"## 内容概述\n\n{archive['summary'].strip()}\n\n"
        f"## 目标客户\n\n{archive['audience_description'].strip()}\n\n"
        f"## 目标客户痛点场景\n\n{archive['pain_scene_description'].strip()}\n\n"
        f"## 内容正文\n\n{document.final_body.strip()}\n\n"
        f"## 可延展选题\n\n{extension_lines}\n\n"
        f"## 关联内容\n\n{related_lines}\n"
    )


def history_target(repo_root: Path, document: RepoDocument) -> Path:
    date = dt.date.fromisoformat(document.publish_date)
    relative = (
        f"accounts/{document.account_id}/内容库/01-历史内容/"
        f"{date:%Y}/{date:%Y-%m}/{date:%Y-%m-%d}｜{filename_title(document.final_title)}.md"
    )
    return safe_repo_path(repo_root, relative)


def history_index_path(repo_root: Path, account_id: str) -> Path:
    return safe_repo_path(repo_root, f"accounts/{account_id}/内容库/01-历史内容/_history-index.jsonl")


def candidate_index_path(repo_root: Path, account_id: str) -> Path:
    return safe_repo_path(repo_root, f"accounts/{account_id}/内容库/03-选题规划/_candidate-index.jsonl")


# Detect existing history and content conflicts before applying pending events.
def existing_history(repo_root: Path, document: RepoDocument, target: Path) -> dict[str, Any] | None:
    index = history_index_path(repo_root, document.account_id)
    if not index.is_file():
        raise OperationError("conflict", f"history index missing: {relative_repo_path(repo_root, index)}")
    rows = read_jsonl(index)
    matches = [row for _, row in rows if row.get("content_id") == document.content_id]
    if len(matches) > 1:
        raise OperationError("conflict", f"duplicate history content_id: {document.content_id}")
    target_rel = relative_repo_path(repo_root, target)
    if matches:
        row = matches[0]
        if row.get("path") != target_rel or row.get("title") != document.final_title or row.get("publish_date") != document.publish_date:
            raise OperationError("conflict", f"content_id points to different history content: {document.content_id}")
        if not target.is_file():
            raise OperationError("conflict", f"history index points to missing file: {target_rel}")
        history_text = target.read_text(encoding="utf-8-sig")
        history_meta = parse_frontmatter(history_text)
        expected_meta = {
            "content_id": document.content_id,
            "title": document.final_title,
            "publish_date": document.publish_date,
            "content_format": document.content_format,
            **{name: document.payload["archive_metadata"][name] for name in HISTORY_FIELDS},
        }
        mismatches = [name for name, value in expected_meta.items() if history_meta.get(name) != value]
        if mismatches:
            raise OperationError("conflict", "history file metadata differs: " + ", ".join(mismatches))
        if extract_section(history_text, "内容正文").strip() != document.final_body.strip():
            raise OperationError("conflict", f"history body differs for content_id: {document.content_id}")
        archive = document.payload["archive_metadata"]
        section_checks = {
            "内容概述": archive["summary"],
            "目标客户": archive["audience_description"],
            "目标客户痛点场景": archive["pain_scene_description"],
        }
        section_mismatches = [
            heading
            for heading, expected in section_checks.items()
            if extract_section(history_text, heading).strip() != expected.strip()
        ]
        if section_mismatches:
            raise OperationError("conflict", "history sections differ: " + ", ".join(section_mismatches))
        return row
    normalized = normalized_title(document.final_title)
    title_matches = [row for _, row in rows if normalized_title(str(row.get("title", ""))) == normalized]
    if title_matches:
        raise OperationError("conflict", "an existing history item has the same normalized title")
    if target.exists():
        raise OperationError("conflict", f"target history file already exists: {target_rel}")
    return None


# Prepare and append recommendation and selected-feedback events idempotently.
def collect_pending_events(document: RepoDocument) -> list[tuple[str, dict[str, Any]]]:
    result: list[tuple[str, dict[str, Any]]] = []
    seen: dict[str, str] = {}
    for action in document.payload["pending_repo_actions"]:
        for event in action["events"]:
            packed = canonical_json(event)
            event_id = event["event_id"]
            if event_id in seen and seen[event_id] != packed:
                raise OperationError("conflict", f"conflicting duplicate event in document: {event_id}")
            if event_id not in seen:
                seen[event_id] = packed
                result.append((action["target_path"], event))
    return result


def inspect_event_writes(repo_root: Path, document: RepoDocument) -> list[tuple[Path, dict[str, Any]]]:
    planning = safe_repo_path(
        repo_root, f"accounts/{document.account_id}/内容库/03-选题规划/推荐记录"
    )
    existing: dict[str, str] = {}
    if planning.exists():
        for source in sorted(planning.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9].jsonl")):
            for _, event in read_jsonl(source):
                event_id = str(event.get("event_id", ""))
                if not event_id:
                    raise OperationError("conflict", f"event without event_id: {source}")
                packed = canonical_json(event)
                if event_id in existing and existing[event_id] != packed:
                    raise OperationError("conflict", f"conflicting duplicate event in repository: {event_id}")
                existing[event_id] = packed
    writes: list[tuple[Path, dict[str, Any]]] = []
    for target_rel, event in collect_pending_events(document):
        event_id = event["event_id"]
        packed = canonical_json(event)
        if event_id in existing:
            if existing[event_id] != packed:
                raise OperationError("conflict", f"event_id already exists with different payload: {event_id}")
            continue
        target = safe_repo_path(repo_root, target_rel)
        writes.append((target, event))
        existing[event_id] = packed
    return writes


def apply_event_writes(writes: list[tuple[Path, dict[str, Any]]]) -> list[str]:
    changed: list[str] = []
    grouped: dict[Path, list[dict[str, Any]]] = {}
    for path, event in writes:
        grouped.setdefault(path, []).append(event)
    for path, events in grouped.items():
        current = path.read_text(encoding="utf-8-sig") if path.exists() else ""
        if current and not current.endswith("\n"):
            raise OperationError("conflict", f"JSONL file has an incomplete final line: {path}")
        addition = "".join(compact_json(event) + "\n" for event in events)
        atomic_write(path, current + addition)
        changed.append(str(path))
    return changed


def all_topic_events(repo_root: Path, document: RepoDocument) -> list[dict[str, Any]]:
    events = [event for _, event in collect_pending_events(document)]
    planning = safe_repo_path(
        repo_root, f"accounts/{document.account_id}/内容库/03-选题规划/推荐记录"
    )
    if planning.exists():
        for source in sorted(planning.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9].jsonl")):
            events.extend(row for _, row in read_jsonl(source))
    return events


# Locate and update an existing candidate linked to the selected topic.
def topic_details(repo_root: Path, document: RepoDocument) -> tuple[str | None, list[str]]:
    topic_id = document.meta.get("topic_id", "")
    if not topic_id or topic_id == "null":
        return None, []
    title: str | None = None
    refs: list[str] = []
    for event in all_topic_events(repo_root, document):
        if event.get("event_type") != "recommendation":
            continue
        for topic in event.get("topics", []):
            if topic.get("topic_id") == topic_id:
                candidate_title = str(topic.get("title", "")).strip()
                if title and candidate_title and title != candidate_title:
                    raise OperationError("conflict", f"topic_id has conflicting titles: {topic_id}")
                title = candidate_title or title
                refs.extend(str(ref) for ref in topic.get("source_refs", []) if isinstance(ref, str))
    return title, refs


def locate_candidate(repo_root: Path, document: RepoDocument) -> dict[str, Any] | None:
    index_path = candidate_index_path(repo_root, document.account_id)
    if not index_path.is_file():
        raise OperationError("conflict", f"candidate index missing: {relative_repo_path(repo_root, index_path)}")
    rows = [row for _, row in read_jsonl(index_path)]
    by_content_id = [row for row in rows if row.get("content_id") == document.content_id]
    if len(by_content_id) > 1:
        raise OperationError("conflict", f"duplicate candidate content_id: {document.content_id}")
    if by_content_id:
        return by_content_id[0]
    topic_title, refs = topic_details(repo_root, document)
    explicit_refs = []
    prefix = f"accounts/{document.account_id}/内容库/03-选题规划/"
    for ref in refs:
        normalized = ref.replace("\\", "/")
        if normalized.startswith(prefix) and ".md#" in normalized and "/灵感库/" not in normalized:
            explicit_refs.append(normalized)
    explicit_matches = [row for row in rows if row.get("path") in explicit_refs]
    if len(explicit_matches) > 1:
        raise OperationError("conflict", "multiple candidate references match the selected topic")
    if explicit_matches:
        return explicit_matches[0]
    if topic_title:
        target = normalized_title(topic_title)
        title_matches = [row for row in rows if normalized_title(str(row.get("title", ""))) == target]
        if len(title_matches) > 1:
            raise OperationError("conflict", "multiple candidates have the selected topic title")
        if title_matches:
            return title_matches[0]
    return None


def validate_candidate_state(candidate: dict[str, Any] | None, document: RepoDocument) -> None:
    if not candidate:
        return
    status = candidate.get("status")
    if status not in {"待核验", "可推荐", "已发布"}:
        raise OperationError("conflict", f"candidate cannot transition from status: {status}")
    existing_id = str(candidate.get("content_id", ""))
    if existing_id and existing_id != document.content_id:
        raise OperationError("conflict", "candidate already has a different content_id")


def update_candidate_markdown(repo_root: Path, candidate: dict[str, Any], document: RepoDocument) -> str:
    reference = str(candidate.get("path", ""))
    if "#" not in reference:
        raise OperationError("conflict", "candidate index path has no heading anchor")
    relative, anchor = reference.split("#", 1)
    path = safe_repo_path(repo_root, relative)
    if not path.is_file():
        raise OperationError("conflict", f"candidate file missing: {relative}")
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    start = None
    for index, line in enumerate(lines):
        match = re.fullmatch(r"###\s+(.+?)\s*", line)
        if match and normalized_title(match.group(1)) == normalized_title(anchor):
            if start is not None:
                raise OperationError("conflict", f"duplicate candidate heading: {reference}")
            start = index
    if start is None:
        raise OperationError("conflict", f"candidate heading missing: {reference}")
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if re.match(r"^#{1,3}\s+", lines[index]):
            end = index
            break
    status_indexes = [i for i in range(start + 1, end) if re.match(r"^-\s*状态[：:]", lines[i])]
    id_indexes = [i for i in range(start + 1, end) if re.match(r"^-\s*(内容ID|content_id)[：:]", lines[i])]
    if len(status_indexes) != 1 or len(id_indexes) > 1:
        raise OperationError("conflict", f"candidate card fields are ambiguous: {reference}")
    lines[status_indexes[0]] = "- 状态：已发布"
    if id_indexes:
        lines[id_indexes[0]] = f"- 内容ID：{document.content_id}"
    else:
        lines.insert(status_indexes[0] + 1, f"- 内容ID：{document.content_id}")
    atomic_write(path, "\n".join(lines) + "\n")
    return relative


def update_candidate_index(repo_root: Path, candidate: dict[str, Any], document: RepoDocument) -> str:
    path = candidate_index_path(repo_root, document.account_id)
    target_ref = candidate["path"]
    rows = read_jsonl(path)
    output: list[str] = []
    found = 0
    for raw, row in rows:
        if row.get("path") == target_ref:
            found += 1
            row["status"] = "已发布"
            row["content_id"] = document.content_id
            raw = compact_json(row)
        output.append(raw)
    if found != 1:
        raise OperationError("conflict", f"candidate index row count is {found}: {target_ref}")
    atomic_write(path, "\n".join(output) + "\n")
    return relative_repo_path(repo_root, path)


# Keep machine indexes and the local recommendation cache synchronized.
def upsert_history_index(repo_root: Path, document: RepoDocument, target: Path) -> bool:
    path = history_index_path(repo_root, document.account_id)
    rows = read_jsonl(path)
    target_rel = relative_repo_path(repo_root, target)
    archive = document.payload["archive_metadata"]
    row = {
        "path": target_rel,
        "content_id": document.content_id,
        "title": document.final_title,
        "publish_date": document.publish_date,
        "business_line": archive["business_line"],
        "theme": archive["theme"],
        "content_type": archive["content_type"],
        "content_format": document.content_format,
        "audience": archive["audience"],
        "pain_scene": archive["pain_scene"],
        "content_goal": archive["content_goal"],
        "status": "published",
        "series": archive["series"],
        "region": archive["region"],
    }
    output: list[str] = []
    found = 0
    changed = False
    for raw, existing in rows:
        if existing.get("path") == target_rel:
            found += 1
            if existing.get("content_id") not in {None, "", document.content_id}:
                raise OperationError("conflict", f"history index path has a different content_id: {target_rel}")
            packed = compact_json(row)
            if canonical_json(existing) != canonical_json(row):
                raw = packed
                changed = True
        output.append(raw)
    if found > 1:
        raise OperationError("conflict", f"duplicate history index path: {target_rel}")
    if found == 0:
        output.append(compact_json(row))
        changed = True
    if changed:
        atomic_write(path, "\n".join(output) + "\n")
    return changed


def sync_topic_cache(repo_root: Path, account_id: str) -> int:
    module_path = Path(__file__).with_name("topic-memory.py")
    spec = importlib.util.spec_from_file_location("wxv_topic_memory", module_path)
    if not spec or not spec.loader:
        raise OperationError("partial_failure", "cannot load topic-memory.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    planning = safe_repo_path(repo_root, f"accounts/{account_id}/内容库/03-选题规划")
    database = module.connect(planning)
    try:
        return int(module.sync(database, planning, account_id))
    finally:
        database.close()


# Orchestrate dry-run planning, authorized writes, and post-write verification.
def make_plan(repo_root: Path, document: RepoDocument) -> dict[str, Any]:
    target = history_target(repo_root, document)
    existing = existing_history(repo_root, document, target)
    event_writes = inspect_event_writes(repo_root, document)
    candidate = locate_candidate(repo_root, document)
    validate_candidate_state(candidate, document)
    return {
        "document": str(document.path),
        "account_id": document.account_id,
        "content_id": document.content_id,
        "history_path": relative_repo_path(repo_root, target),
        "history_action": "already_present" if existing else "create",
        "new_event_ids": [event["event_id"] for _, event in event_writes],
        "candidate_path": candidate.get("path") if candidate else None,
        "candidate_action": "mark_published" if candidate and (
            candidate.get("status") != "已发布" or candidate.get("content_id") != document.content_id
        ) else "none",
        "semantic_enrichment": "deferred",
        "_target": target,
        "_existing": existing,
        "_event_writes": event_writes,
        "_candidate": candidate,
    }


def public_plan(plan: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in plan.items() if not key.startswith("_")}


def apply_sync(repo_root: Path, document: RepoDocument, plan: dict[str, Any]) -> dict[str, Any]:
    changed: list[str] = []
    try:
        event_paths = apply_event_writes(plan["_event_writes"])
        changed.extend(relative_repo_path(repo_root, Path(path)) for path in event_paths)
        target: Path = plan["_target"]
        if plan["_existing"] is None:
            atomic_write(target, build_history_text(document))
            changed.append(relative_repo_path(repo_root, target))
        if upsert_history_index(repo_root, document, target):
            changed.append(relative_repo_path(repo_root, history_index_path(repo_root, document.account_id)))
        candidate = plan["_candidate"]
        if candidate and plan["candidate_action"] == "mark_published":
            changed.append(update_candidate_markdown(repo_root, candidate, document))
            changed.append(update_candidate_index(repo_root, candidate, document))
        cache_added = sync_topic_cache(repo_root, document.account_id)
        verification = verify_sync(repo_root, document)
        if not verification["verified"]:
            raise OperationError("partial_failure", *verification["errors"])
    except OperationError as exc:
        if changed and exc.status != "partial_failure":
            raise OperationError(
                "partial_failure",
                "completed paths: " + ", ".join(sorted(set(changed))),
                *exc.errors,
            ) from exc
        raise
    except Exception as exc:
        details = ["completed paths: " + ", ".join(sorted(set(changed)))] if changed else []
        raise OperationError("partial_failure", *details, f"unexpected execution error: {exc}") from exc
    return {
        "status": "already_synced" if not changed else "completed",
        **public_plan(plan),
        "changed_paths": sorted(set(changed)),
        "topic_cache_added_events": cache_added,
        "verified": True,
    }


def verify_sync(repo_root: Path, document: RepoDocument) -> dict[str, Any]:
    errors: list[str] = []
    target = history_target(repo_root, document)
    if not target.is_file():
        errors.append("history file is missing")
    else:
        meta = parse_frontmatter(target.read_text(encoding="utf-8-sig"))
        if meta.get("content_id") != document.content_id:
            errors.append("history file content_id mismatch")
    index_rows = [row for _, row in read_jsonl(history_index_path(repo_root, document.account_id))]
    matching_history = [row for row in index_rows if row.get("content_id") == document.content_id]
    if len(matching_history) != 1:
        errors.append("history index does not contain exactly one matching content_id")
    planned_events = collect_pending_events(document)
    repository_events: dict[str, str] = {}
    log_root = safe_repo_path(
        repo_root, f"accounts/{document.account_id}/内容库/03-选题规划/推荐记录"
    )
    if log_root.exists():
        for source in sorted(log_root.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9].jsonl")):
            for _, event in read_jsonl(source):
                repository_events[str(event.get("event_id", ""))] = canonical_json(event)
    for _, event in planned_events:
        if repository_events.get(event["event_id"]) != canonical_json(event):
            errors.append(f"pending event is not synchronized: {event['event_id']}")
    candidate = locate_candidate(repo_root, document)
    if candidate and (candidate.get("status") != "已发布" or candidate.get("content_id") != document.content_id):
        errors.append("matching candidate is not marked as published")
    return {
        "status": "verified" if not errors else "incomplete",
        "verified": not errors,
        "account_id": document.account_id,
        "content_id": document.content_id,
        "history_path": relative_repo_path(repo_root, target),
        "errors": errors,
    }


# Command-line interface returns stable JSON for Codex or direct local use.
def emit(value: dict[str, Any]) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("check", "verify"):
        command = subparsers.add_parser(name)
        command.add_argument("--input", required=True, type=Path)
    sync = subparsers.add_parser("sync-published")
    sync.add_argument("--input", required=True, type=Path)
    sync.add_argument("--apply", action="store_true", help="required to authorize repository writes")
    args = parser.parse_args()
    repo_root = args.repo_root.resolve()
    try:
        document = load_repo_document(args.input.resolve())
        if args.command == "verify":
            result = verify_sync(repo_root, document)
            emit(result)
            return 0 if result["verified"] else 2
        if args.command == "check":
            plan = make_plan(repo_root, document)
            emit({"status": "ready", **public_plan(plan)})
            return 0
        if not args.apply:
            raise OperationError("authorization_required", "sync-published requires --apply")
        with repository_lock(repo_root):
            plan = make_plan(repo_root, document)
            emit(apply_sync(repo_root, document, plan))
        return 0
    except OperationError as exc:
        emit({"status": exc.status, "errors": exc.errors})
        return 3 if exc.status in {"conflict", "partial_failure"} else 2
    except Exception as exc:
        emit({"status": "partial_failure", "errors": [f"unexpected operation error: {exc}"]})
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
