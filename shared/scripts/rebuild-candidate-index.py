"""Rebuild account candidate indexes from Markdown candidate cards."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any, Mapping

from index_common import (
    REPO_ROOT,
    configure_console,
    culture_sort_key,
    get_frontmatter,
    get_mapping_value,
    get_metadata_value,
    get_repository_relative_path,
    get_target_account_ids,
    write_json_lines,
)


ALLOWED_STATUSES = ("待核验", "可推荐", "已发布", "已放弃")
RECOMMENDED_FORMATS = {
    "短文字幕": "text_broadcast",
    "文字播报": "text_broadcast",
    "短文": "text_broadcast",
    "口播": "spoken",
    "真人口播": "spoken",
    "均可": "either",
}


def convert_recommended_format(value: str) -> str:
    return RECOMMENDED_FORMATS.get(value.strip(), "")


def add_candidate_card(
    target: list[dict[str, str]],
    title: str,
    fields: Mapping[str, Any],
    file_path: Path,
    file_metadata: Mapping[str, Any],
) -> None:
    if not title.strip() or title == "简短名称":
        return
    status = get_mapping_value(fields, "状态")
    if status not in ALLOWED_STATUSES:
        return

    pain_scene = "；".join(
        value
        for value in (
            get_mapping_value(fields, "经营场景"),
            get_mapping_value(fields, "核心痛点"),
        )
        if value.strip()
    )
    clean_title = re.sub(r"^选题[｜|：:]\s*", "", title, flags=re.IGNORECASE).strip()
    relative = get_repository_relative_path(file_path)
    content_id = get_mapping_value(fields, "内容ID") or get_mapping_value(
        fields, "content_id"
    )
    content_goal = get_mapping_value(fields, "内容目标") or get_mapping_value(
        fields, "内容目的"
    )
    recommended_format = convert_recommended_format(
        get_mapping_value(fields, "建议载体")
    )
    target.append(
        {
            "path": f"{relative}#{clean_title}",
            "title": clean_title,
            "status": status,
            "content_id": content_id,
            "business_line": get_mapping_value(fields, "业务方向"),
            "theme": get_mapping_value(fields, "主题"),
            "audience": get_mapping_value(fields, "目标客户"),
            "pain_scene": pain_scene,
            "content_goal": content_goal,
            "service": get_mapping_value(fields, "可承接服务"),
            "recommended_format": recommended_format,
            "created": get_metadata_value(file_metadata, ("created", "date")),
        }
    )


def rebuild_candidate_index(account_id: str) -> int:
    planning_root = REPO_ROOT / "accounts" / account_id / "内容库" / "03-选题规划"
    if not planning_root.exists():
        raise FileNotFoundError(f"Candidate root not found: {planning_root}")

    rows: list[dict[str, str]] = []
    files = sorted(
        (
            path
            for path in planning_root.rglob("*.md")
            if path.is_file() and "灵感库" not in path.parts
        ),
        key=lambda path: culture_sort_key(str(path.resolve())),
    )
    for path in files:
        file_metadata = get_frontmatter(path)
        current_title = ""
        fields: dict[str, str] = {}
        in_fence = False

        for line in path.read_text(encoding="utf-8-sig").splitlines():
            if re.match(r"^\s*(~~~|```)", line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue

            heading = re.match(r"^###\s+(.+?)\s*$", line)
            if heading is not None:
                add_candidate_card(rows, current_title, fields, path, file_metadata)
                current_title = heading.group(1).strip()
                fields = {}
                continue
            if re.match(r"^#{1,2}\s+", line):
                add_candidate_card(rows, current_title, fields, path, file_metadata)
                current_title = ""
                fields = {}
                continue
            if current_title.strip():
                field = re.match(r"^-\s*([^：:]+)[：:]\s*(.*)$", line)
                if field is not None:
                    key = field.group(1).strip()
                    existing = next(
                        (name for name in fields if name.casefold() == key.casefold()), None
                    )
                    fields[existing or key] = field.group(2).strip()

        add_candidate_card(rows, current_title, fields, path, file_metadata)

    rows.sort(key=lambda row: culture_sort_key(row["path"]))
    output = planning_root / "_candidate-index.jsonl"
    write_json_lines(output, rows)
    print(
        f"{account_id} candidate_index={len(rows)} "
        f"path={get_repository_relative_path(output)}"
    )
    return len(rows)


def main() -> int:
    configure_console()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--account-id")
    args = parser.parse_args()
    for account_id in get_target_account_ids(args.account_id):
        rebuild_candidate_index(account_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
