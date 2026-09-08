#!/usr/bin/env python3
"""Create stable content IDs and validate ChatGPT-project Handoff Markdown."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import secrets
from pathlib import Path


ACCOUNT_IDS = {"gzminge", "gzxzcs", "qycslc", "gzcktxpp", "tsxbj", "gzlxcs"}
FROM_STAGES = {
    "topic_planning",
    "text_broadcast_copywriting",
    "spoken_copywriting",
    "spoken_visual_planning",
}
TO_STAGES = {
    "text_broadcast_copywriting",
    "spoken_copywriting",
    "spoken_visual_planning",
    "repo_sync",
    "publish_archive",
    "none",
}
SYNC_STATUSES = {"not_synced", "synced", "not_applicable"}
CONTENT_FORMATS = {"text_broadcast", "spoken", "null"}
CONTENT_ID_RE = re.compile(
    r"^wxv-(gzminge|gzxzcs|qycslc|gzcktxpp|tsxbj|gzlxcs)-(\d{8})-([0-9a-f]{8})$"
)
REQUIRED_FIELDS = {
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
}
REQUIRED_SECTIONS = {
    "用户确认原话",
    "已确认成果",
    "关键事实与改变结论的条件",
    "来源引用",
    "用户要求与保留项",
    "允许调整",
    "禁止动作",
    "待执行仓库动作",
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


def validate_handoff(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    errors: list[str] = []

    missing = sorted(REQUIRED_FIELDS - set(meta))
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

    if meta.get("handoff_version") != "1.0":
        errors.append("handoff_version must be 1.0")
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
    if meta.get("from_stage") == "spoken_visual_planning" and meta.get("repo_sync_status") != "not_applicable":
        errors.append("visual-stage Handoff must use repo_sync_status=not_applicable")

    confirmed_at = meta.get("confirmed_at", "")
    try:
        dt.datetime.fromisoformat(confirmed_at)
    except ValueError:
        errors.append("confirmed_at must be an ISO-8601 timestamp")

    headings = set(re.findall(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))
    missing_sections = sorted(REQUIRED_SECTIONS - headings)
    if missing_sections:
        errors.append(f"missing sections: {', '.join(missing_sections)}")

    expected_name = f"Handoff｜{content_id}｜{meta.get('from_stage', '')}-to-{meta.get('to_stage', '')}.md"
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
