"""Rebuild account history indexes from Markdown source files."""

from __future__ import annotations

import argparse
import re

from index_common import (
    REPO_ROOT,
    configure_console,
    culture_sort_key,
    get_frontmatter,
    get_metadata_value,
    get_repository_relative_path,
    get_target_account_ids,
    get_title_from_filename,
    write_json_lines,
)


def rebuild_history_index(account_id: str) -> int:
    history_root = REPO_ROOT / "accounts" / account_id / "内容库" / "01-历史内容"
    if not history_root.exists():
        raise FileNotFoundError(f"History root not found: {history_root}")

    rows: list[dict[str, str]] = []
    files = sorted(
        (path for path in history_root.rglob("*.md") if path.is_file()),
        key=lambda path: culture_sort_key(str(path.resolve())),
    )
    for path in files:
        metadata = get_frontmatter(path)
        title = get_metadata_value(metadata, ("title",)) or get_title_from_filename(path)
        publish_date = get_metadata_value(metadata, ("publish_date", "published", "date"))
        if not publish_date:
            match = re.match(r"^(\d{4}-\d{2}-\d{2})", path.stem)
            if match is not None:
                publish_date = match.group(1)

        rows.append(
            {
                "path": get_repository_relative_path(path),
                "content_id": get_metadata_value(metadata, ("content_id",)),
                "title": title,
                "publish_date": publish_date,
                "business_line": get_metadata_value(metadata, ("business_line",)),
                "theme": get_metadata_value(metadata, ("theme",)),
                "content_type": get_metadata_value(metadata, ("content_type",)),
                "content_format": get_metadata_value(metadata, ("content_format",)),
                "audience": get_metadata_value(metadata, ("audience",)),
                "pain_scene": get_metadata_value(metadata, ("pain_scene",)),
                "content_goal": get_metadata_value(metadata, ("content_goal",)),
                "status": "published",
                "series": get_metadata_value(metadata, ("series",)),
                "region": get_metadata_value(metadata, ("region",)),
            }
        )

    output = history_root / "_history-index.jsonl"
    write_json_lines(output, rows)
    print(
        f"{account_id} history_index={len(rows)} "
        f"path={get_repository_relative_path(output)}"
    )
    return len(rows)


def main() -> int:
    configure_console()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--account-id")
    args = parser.parse_args()
    for account_id in get_target_account_ids(args.account_id):
        rebuild_history_index(account_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
