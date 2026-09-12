"""Rebuild account idea indexes from Markdown source files."""

from __future__ import annotations

import argparse

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


def rebuild_idea_index(account_id: str) -> int:
    idea_root = REPO_ROOT / "accounts" / account_id / "内容库" / "03-选题规划" / "灵感库"
    if not idea_root.exists():
        raise FileNotFoundError(f"Idea root not found: {idea_root}")

    rows: list[dict[str, str]] = []
    files = sorted(
        (
            path
            for path in idea_root.rglob("*.md")
            if path.is_file() and not path.name.casefold().startswith("00-")
        ),
        key=lambda path: culture_sort_key(str(path.resolve())),
    )
    for path in files:
        metadata = get_frontmatter(path)
        title = get_metadata_value(metadata, ("title",)) or get_title_from_filename(path)
        rows.append(
            {
                "path": get_repository_relative_path(path),
                "title": title,
                "created": get_metadata_value(metadata, ("created", "date")),
                "status": get_metadata_value(metadata, ("status",)),
                "business_line": get_metadata_value(metadata, ("business_line",)),
                "audience": get_metadata_value(metadata, ("audience",)),
                "pain_scene": get_metadata_value(metadata, ("pain_scene",)),
                "source": get_metadata_value(metadata, ("source", "source_type")),
            }
        )

    output = idea_root / "_idea-index.jsonl"
    write_json_lines(output, rows)
    print(
        f"{account_id} idea_index={len(rows)} "
        f"path={get_repository_relative_path(output)}"
    )
    return len(rows)


def main() -> int:
    configure_console()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--account-id")
    args = parser.parse_args()
    for account_id in get_target_account_ids(args.account_id):
        rebuild_idea_index(account_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
