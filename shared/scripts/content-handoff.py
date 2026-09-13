#!/usr/bin/env python3
"""Create stable content IDs and validate ChatGPT-project Handoff Markdown."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import secrets
import uuid
from pathlib import Path


ACCOUNT_IDS = {"gzminge", "gzxzcs", "qycslc", "gzcktxpp", "tsxbj", "gzlxcs"}
FROM_STAGES = {
    "topic_planning",
}
TO_STAGES = {
    "text_broadcast_copywriting",
    "spoken_copywriting",
}
SYNC_STATUSES = {"not_synced", "synced"}
CONTENT_FORMATS = {"text_broadcast", "spoken"}
CONTENT_ID_RE = re.compile(
    r"^wxv-(gzminge|gzxzcs|qycslc|gzcktxpp|tsxbj|gzlxcs)-(\d{8})-([0-9a-f]{8})$"
)
TOPIC_SHORT_NAME_RE = re.compile(r"^[A-Za-z0-9\u4e00-\u9fff-]{4,20}$")
COMMON_REQUIRED_FIELDS = {
    "handoff_version",
    "content_id",
    "account_id",
    "from_stage",
    "to_stage",
    "approval_status",
    "confirmed_at",
    "repo_sync_status",
    "content_format",
    "topic_id",
    "topic_origin",
    "recommendation_batch_id",
    "topic_feedback_status",
    "feedback_event_id",
}
VERSION_REQUIRED_FIELDS = {
    "1.0": set(),
    "1.1": {"topic_short_name"},
}
REQUIRED_SECTIONS = {
    "用户确认原话",
    "已确认成果",
    "选题来源与反馈",
    "关键事实与改变结论的条件",
    "来源引用",
    "用户要求与保留项",
    "允许调整",
    "禁止动作",
    "待执行仓库动作",
}
LEGACY_ACTION_TYPES = {
    "append_topic_recommendation_event",
    "append_topic_feedback_event",
    "append_jsonl_event",
}
LEGACY_ACTIONS = {
    "append_jsonl",
    "append_recommendation_event",
    "append_feedback_event",
    "append_topic_recommendation_event",
    "append_topic_feedback_event",
}


def create_content_id(account_id: str, date_value: str | None, suffix: str | None) -> str:
    if account_id not in ACCOUNT_IDS:
        raise ValueError(f"unknown account_id: {account_id}")
    if date_value:
        parsed = dt.date.fromisoformat(date_value)
    else:
        parsed = dt.date.today()
    token = suffix or secrets.token_hex(4)
    if not re.fullmatch(r"[0-9a-f]{8}", token):
        raise ValueError("suffix must be exactly 8 lowercase hexadecimal characters")
    return f"wxv-{account_id}-{parsed:%Y%m%d}-{token}"


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening frontmatter fence")
    try:
        closing = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
    except StopIteration as exc:
        raise ValueError("missing closing frontmatter fence") from exc

    result: dict[str, str] = {}
    for line in lines[1:closing]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"\'')
    return result


def extract_section(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$\r?\n(?P<body>.*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise ValueError(f"missing section: {heading}")
    return match.group("body").strip()


def require_uuid(value: object, field: str) -> None:
    try:
        uuid.UUID(str(value))
    except (ValueError, AttributeError, TypeError) as exc:
        raise ValueError(f"{field} must be a UUID") from exc


def extract_pending_actions(text: str) -> list[dict[str, object]]:
    section = extract_section(text, "待执行仓库动作")
    if re.fullmatch(r"-\s*pending_repo_actions:\s*\[\s*\]", section):
        return []
    match = re.fullmatch(r"```json\s*(\{.*\})\s*```", section, re.DOTALL)
    if not match:
        raise ValueError("待执行仓库动作 must contain one JSON object")
    try:
        payload = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid pending_repo_actions JSON: {exc.msg}") from exc
    if not isinstance(payload, dict):
        raise ValueError("待执行仓库动作 JSON must be an object")
    actions = payload.get("pending_repo_actions")
    if not isinstance(actions, list):
        raise ValueError("pending_repo_actions must be an array")
    return actions


def validate_pending_actions(actions: list[dict[str, object]], account_id: str) -> list[dict[str, object]]:
    validated: list[dict[str, object]] = []
    expected_prefix = f"accounts/{account_id}/内容库/03-选题规划/推荐记录/"
    for index, source_action in enumerate(actions):
        if not isinstance(source_action, dict):
            raise ValueError(f"pending_repo_actions[{index}] must be an object")
        action = dict(source_action)
        if action.get("action_type") in LEGACY_ACTION_TYPES:
            payload = action.get("payload")
            if not isinstance(payload, dict):
                raise ValueError(f"pending_repo_actions[{index}].payload must be an object")
            action["action_type"] = "append_topic_recommendation_events"
            action["source_schema"] = "shared/schemas/topic-recommendation-log-schema.md"
            action["events"] = [payload]
        elif action.get("action") in LEGACY_ACTIONS:
            payload = action.get("payload")
            if not isinstance(payload, dict):
                raise ValueError(f"pending_repo_actions[{index}].payload must be an object")
            action["action_type"] = "append_topic_recommendation_events"
            action["source_schema"] = "shared/schemas/topic-recommendation-log-schema.md"
            action["events"] = [payload]
        if action.get("action_type") != "append_topic_recommendation_events":
            raise ValueError(f"unsupported pending action: {action.get('action_type')}")
        if action.get("source_schema") != "shared/schemas/topic-recommendation-log-schema.md":
            raise ValueError("pending action source_schema is invalid")
        require_uuid(action.get("action_id"), f"pending_repo_actions[{index}].action_id")
        target = str(action.get("target_path", "")).replace("\\", "/")
        if not target.startswith(expected_prefix) or not re.fullmatch(
            re.escape(expected_prefix) + r"\d{4}-\d{2}\.jsonl", target
        ):
            raise ValueError(f"invalid pending action target: {target}")
        events = action.get("events")
        if not isinstance(events, list) or not events:
            raise ValueError(f"pending_repo_actions[{index}].events must be non-empty")
        for event_index, event in enumerate(events):
            if not isinstance(event, dict):
                raise ValueError(f"pending_repo_actions[{index}].events[{event_index}] must be an object")
            require_uuid(event.get("event_id"), f"pending event {event_index}.event_id")
            if event.get("event_type") not in {"recommendation", "feedback"}:
                raise ValueError("pending event_type must be recommendation or feedback")
            if event.get("account_id") != account_id:
                raise ValueError("pending event account_id mismatch")
            occurred_at = event.get("occurred_at")
            if not isinstance(occurred_at, str) or not occurred_at.strip():
                raise ValueError("pending event occurred_at is required")
            try:
                occurred_datetime = dt.datetime.fromisoformat(occurred_at)
            except ValueError as exc:
                raise ValueError("pending event occurred_at is invalid") from exc
            if occurred_datetime.strftime("%Y-%m") != Path(target).stem:
                raise ValueError("pending event target month does not match occurred_at")
            require_uuid(event.get("batch_id"), f"pending event {event_index}.batch_id")
            if event["event_type"] == "recommendation":
                topics = event.get("topics")
                if not isinstance(topics, list) or not topics:
                    raise ValueError("recommendation.topics must be non-empty")
                for topic in topics:
                    if not isinstance(topic, dict):
                        raise ValueError("recommendation topic must be an object")
                    require_uuid(topic.get("topic_id"), "recommendation.topic_id")
            else:
                if event.get("signal") != "selected":
                    raise ValueError("Handoff accepts only selected feedback events")
                topic_ids = event.get("topic_ids")
                if not isinstance(topic_ids, list) or len(topic_ids) != 1:
                    raise ValueError("selected feedback must contain one topic_id")
                require_uuid(topic_ids[0], "feedback.topic_ids[0]")
        action["target_path"] = target
        validated.append(action)
    return validated


def validate_handoff(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    errors: list[str] = []

    version = meta.get("handoff_version", "")
    required_fields = COMMON_REQUIRED_FIELDS | VERSION_REQUIRED_FIELDS.get(version, set())
    missing = sorted(required_fields - set(meta))
    if missing:
        errors.append(f"missing fields: {', '.join(missing)}")

    content_id = meta.get("content_id", "")
    match = CONTENT_ID_RE.fullmatch(content_id)
    if not match:
        errors.append("content_id format is invalid")

    account_id = meta.get("account_id", "")
    if account_id not in ACCOUNT_IDS:
        errors.append("account_id is invalid")
    if match and account_id != match.group(1):
        errors.append("account_id does not match content_id")

    if version not in VERSION_REQUIRED_FIELDS:
        errors.append("handoff_version must be 1.0 or 1.1")
    if meta.get("from_stage") not in FROM_STAGES:
        errors.append("from_stage is invalid")
    if meta.get("to_stage") not in TO_STAGES:
        errors.append("to_stage is invalid")
    if meta.get("approval_status") != "confirmed_by_user":
        errors.append("approval_status must be confirmed_by_user")
    if meta.get("repo_sync_status") not in SYNC_STATUSES:
        errors.append("repo_sync_status is invalid")
    if meta.get("content_format") not in CONTENT_FORMATS:
        errors.append("content_format is invalid")
    expected_format = {
        "text_broadcast_copywriting": "text_broadcast",
        "spoken_copywriting": "spoken",
    }.get(meta.get("to_stage", ""))
    if expected_format and meta.get("content_format") != expected_format:
        errors.append("content_format does not match to_stage")
    if meta.get("topic_origin") != "project_recommendation":
        errors.append("topic_origin must be project_recommendation")
    if meta.get("topic_feedback_status") not in {"synced", "pending"}:
        errors.append("topic_feedback_status is invalid")
    if meta.get("topic_feedback_status") == "pending" and meta.get("repo_sync_status") != "not_synced":
        errors.append("pending topic feedback requires repo_sync_status=not_synced")
    if meta.get("topic_feedback_status") == "synced" and meta.get("repo_sync_status") != "synced":
        errors.append("synced topic feedback requires repo_sync_status=synced")

    for field in ("topic_id", "recommendation_batch_id", "feedback_event_id"):
        try:
            uuid.UUID(meta.get(field, ""))
        except (ValueError, AttributeError):
            errors.append(f"{field} must be a UUID")
    confirmed_at = meta.get("confirmed_at", "")
    try:
        confirmed_datetime = dt.datetime.fromisoformat(confirmed_at)
    except ValueError:
        errors.append("confirmed_at must be an ISO-8601 timestamp")
        confirmed_datetime = None

    headings = set(re.findall(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))
    missing_sections = sorted(REQUIRED_SECTIONS - headings)
    if missing_sections:
        errors.append(f"missing sections: {', '.join(missing_sections)}")

    pending_actions: list[dict[str, object]] = []
    if "待执行仓库动作" in headings:
        try:
            pending_actions = validate_pending_actions(extract_pending_actions(text), account_id)
        except ValueError as exc:
            errors.append(str(exc))
    if meta.get("topic_feedback_status") == "pending":
        carried_events = [
            event
            for action in pending_actions
            for event in action.get("events", [])
            if isinstance(event, dict)
        ]
        feedback = [event for event in carried_events if event.get("event_id") == meta.get("feedback_event_id")]
        if (
            len(feedback) != 1
            or feedback[0].get("topic_ids") != [meta.get("topic_id")]
            or feedback[0].get("batch_id") != meta.get("recommendation_batch_id")
        ):
            errors.append("pending selected feedback payload is missing or inconsistent")
    elif meta.get("topic_feedback_status") == "synced" and pending_actions:
        errors.append("synced topic feedback cannot contain pending actions")

    if version == "1.0":
        expected_name = f"Handoff｜{content_id}｜{meta.get('from_stage', '')}-to-{meta.get('to_stage', '')}.md"
    else:
        topic_short_name = meta.get("topic_short_name", "")
        if topic_short_name and not TOPIC_SHORT_NAME_RE.fullmatch(topic_short_name):
            errors.append("topic_short_name must be 4-20 Chinese characters, letters, digits, or hyphens")
        timestamp = confirmed_datetime.strftime("%Y%m%d-%H%M%S") if confirmed_datetime else "INVALID-TIME"
        expected_name = f"选题交接｜{account_id}｜{topic_short_name}｜{timestamp}.md"
    if path.name != expected_name:
        errors.append(f"filename must be: {expected_name}")

    return {
        "valid": not errors,
        "path": str(path),
        "content_id": content_id,
        "account_id": account_id,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_id = subparsers.add_parser("new-id")
    new_id.add_argument("--account", required=True, choices=sorted(ACCOUNT_IDS))
    new_id.add_argument("--date")
    new_id.add_argument("--suffix", help=argparse.SUPPRESS)

    validate = subparsers.add_parser("validate")
    validate.add_argument("path", type=Path)

    args = parser.parse_args()
    if args.command == "new-id":
        print(create_content_id(args.account, args.date, args.suffix))
        return 0

    result = validate_handoff(args.path)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
