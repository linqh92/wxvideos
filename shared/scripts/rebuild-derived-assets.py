"""Rebuild deterministic derived summaries from account indexes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys

from index_common import (
    REPO_ROOT,
    configure_console,
    convert_groups_to_object,
    get_repository_relative_path,
    get_target_account_ids,
    read_json_lines,
)


def run_rebuild(script_name: str, account_id: str) -> None:
    subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "shared" / "scripts" / script_name),
            "--account-id",
            account_id,
        ],
        check=True,
    )


def rebuild_derived_assets(account_id: str) -> None:
    vault = REPO_ROOT / "accounts" / account_id / "内容库"
    history_index = vault / "01-历史内容" / "_history-index.jsonl"
    idea_index = vault / "03-选题规划" / "灵感库" / "_idea-index.jsonl"
    candidate_index = vault / "03-选题规划" / "_candidate-index.jsonl"

    if not history_index.exists():
        run_rebuild("rebuild-history-index.py", account_id)
    if not idea_index.exists():
        run_rebuild("rebuild-idea-index.py", account_id)
    if not candidate_index.exists():
        run_rebuild("rebuild-candidate-index.py", account_id)

    history = read_json_lines(history_index)
    ideas = read_json_lines(idea_index)
    candidates = read_json_lines(candidate_index)
    history_with_month = []
    for row in history:
        match = re.match(r"^(\d{4}-\d{2})", str(row.get("publish_date", "")))
        history_with_month.append({"publish_month": match.group(1) if match else ""})

    summary = {
        "account_id": account_id,
        "generated_from": [
            get_repository_relative_path(history_index),
            get_repository_relative_path(idea_index),
            get_repository_relative_path(candidate_index),
        ],
        "history_index_sha256": hashlib.sha256(history_index.read_bytes()).hexdigest(),
        "history_count": len(history),
        "idea_count": len(ideas),
        "candidate_count": len(candidates),
        "history_by_month": convert_groups_to_object(history_with_month, "publish_month"),
        "history_by_business_line": convert_groups_to_object(history, "business_line"),
        "history_by_theme": convert_groups_to_object(history, "theme"),
        "history_by_content_type": convert_groups_to_object(history, "content_type"),
        "idea_by_status": convert_groups_to_object(ideas, "status"),
        "candidate_by_status": convert_groups_to_object(candidates, "status"),
        "note": "该 JSON 是可重复生成的机器派生摘要；原内容地图、缺口分析、重复检查和月度复盘 Markdown 保留为人工资产，不在本脚本中覆盖。",
    }

    output = vault / "04-内容复盘" / "_derived-assets-summary.json"
    with output.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(
        f"{account_id} derived_summary=1 "
        f"path={get_repository_relative_path(output)}"
    )


def main() -> int:
    configure_console()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--account-id")
    args = parser.parse_args()
    for account_id in get_target_account_ids(args.account_id):
        rebuild_derived_assets(account_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
