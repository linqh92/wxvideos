#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


# Load the production script directly so tests exercise its public functions.
SCRIPT_PATH = Path(__file__).with_name("wxv-ops.py")
SPEC = importlib.util.spec_from_file_location("wxv_ops", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


ACCOUNT = "gzminge"
CONTENT_ID = "wxv-gzminge-20260909-a1b2c3d4"
TOPIC_ID = "11111111-1111-4111-8111-111111111111"
BATCH_ID = "22222222-2222-4222-8222-222222222222"
RECOMMENDATION_EVENT_ID = "33333333-3333-4333-8333-333333333333"
FEEDBACK_EVENT_ID = "44444444-4444-4444-8444-444444444444"
ACTION_ID = "55555555-5555-4555-8555-555555555555"


def compact(value: dict) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


# Build one complete recommendation-and-selection fixture.
def recommendation_event() -> dict:
    return {
        "event_id": RECOMMENDATION_EVENT_ID,
        "event_type": "recommendation",
        "occurred_at": "2026-09-09T10:00:00+08:00",
        "account_id": ACCOUNT,
        "batch_id": BATCH_ID,
        "replaces_topic_ids": [],
        "request_summary": "测试推荐",
        "topics": [
            {
                "topic_id": TOPIC_ID,
                "title": "测试选题",
                "audience": "企业老板",
                "decision_question": "如何处理？",
                "core_answer": "按条件处理。",
                "key_conditions": ["条件一"],
                "service": "财税服务",
                "demand_basis": {"type": "用户需求", "detail": "测试"},
                "recommended_format": "text_broadcast",
                "source_refs": [
                    "accounts/gzminge/内容库/03-选题规划/测试选题池.md#测试选题"
                ],
            }
        ],
        "return_reason": "",
    }


def feedback_event() -> dict:
    return {
        "event_id": FEEDBACK_EVENT_ID,
        "event_type": "feedback",
        "occurred_at": "2026-09-09T10:05:00+08:00",
        "account_id": ACCOUNT,
        "batch_id": BATCH_ID,
        "topic_ids": [TOPIC_ID],
        "scope": "topic",
        "signal": "selected",
        "user_text": "选择这个题",
        "scope_description": "测试选题",
    }


def repo_document(payload: dict) -> str:
    return f'''---
delivery_version: "1.1"
document_type: "repo_content"
content_id: "{CONTENT_ID}"
account_id: "{ACCOUNT}"
content_format: "text_broadcast"
approval_status: "confirmed_by_user"
confirmed_at: "2026-09-09T10:10:00+08:00"
publication_status: "published_by_user"
publish_date: "2026-09-09"
requested_repo_action: "archive_published_content"
final_title: "测试：最终标题？"
topic_id: "{TOPIC_ID}"
topic_origin: "project_recommendation"
recommendation_batch_id: "{BATCH_ID}"
topic_feedback_status: "pending"
feedback_event_id: "{FEEDBACK_EVENT_ID}"
repo_sync_status: "not_synced"
---

# 测试：最终标题？

## 最终正文

这是用户确认并已经发布的完整正文。

## Repo 操作载荷

```json
{json.dumps(payload, ensure_ascii=False, indent=2)}
```
'''


def valid_payload() -> dict:
    return {
        "schema_version": "1.0",
        "action": "archive_published_content",
        "account_id": ACCOUNT,
        "content_id": CONTENT_ID,
        "content_format": "text_broadcast",
        "publish_date": "2026-09-09",
        "final_title": "测试：最终标题？",
        "archive_metadata": {
            "business_line": "企业财税合规",
            "theme": "测试主题",
            "content_type": "条件判断",
            "audience": "企业老板",
            "pain_scene": "企业需要判断测试问题。",
            "content_goal": "帮助企业识别测试条件。",
            "region": "广州",
            "platform": "微信视频号",
            "series": "测试系列",
            "source": "用户确认发布内容",
            "summary": "内容说明测试问题、主要判断和适用边界。",
            "audience_description": "需要处理测试问题的企业老板。",
            "pain_scene_description": "企业在测试场景下缺少明确的判断依据。",
            "extension_topics": [],
            "related_content": [],
        },
        "pending_repo_actions": [
            {
                "action_id": ACTION_ID,
                "action_type": "append_topic_recommendation_events",
                "target_path": "accounts/gzminge/内容库/03-选题规划/推荐记录/2026-09.jsonl",
                "source_schema": "shared/schemas/topic-recommendation-log-schema.md",
                "events": [recommendation_event(), feedback_event()],
            }
        ],
    }


# Create an isolated minimal account repository for write-path testing.
def prepare_repo(root: Path) -> Path:
    history = root / "accounts" / ACCOUNT / "内容库" / "01-历史内容"
    planning = root / "accounts" / ACCOUNT / "内容库" / "03-选题规划"
    history.mkdir(parents=True)
    planning.mkdir(parents=True)
    (history / "_history-index.jsonl").write_text("", encoding="utf-8")
    candidate_file = planning / "测试选题池.md"
    candidate_file.write_text(
        "# 测试选题池\n\n### 测试选题\n\n- 状态：可推荐\n- 目标客户：企业老板\n",
        encoding="utf-8",
    )
    candidate = {
        "path": "accounts/gzminge/内容库/03-选题规划/测试选题池.md#测试选题",
        "title": "测试选题",
        "status": "可推荐",
        "business_line": "企业财税合规",
        "theme": "测试主题",
        "audience": "企业老板",
        "pain_scene": "测试场景",
        "content_goal": "测试目标",
        "service": "财税服务",
        "recommended_format": "text_broadcast",
        "created": "2026-09-09",
    }
    (planning / "_candidate-index.jsonl").write_text(compact(candidate) + "\n", encoding="utf-8")
    document = root / f"Repo内容文档｜{CONTENT_ID}｜测试内容.md"
    document.write_text(repo_document(valid_payload()), encoding="utf-8")
    return document


# Cover first sync, idempotent retry, CLI usage, and conflict rejection.
def main() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        document_path = prepare_repo(root)
        document = MODULE.load_repo_document(document_path)
        plan = MODULE.make_plan(root, document)
        assert plan["history_action"] == "create"
        assert len(plan["new_event_ids"]) == 2
        assert plan["candidate_action"] == "mark_published"

        result = MODULE.apply_sync(root, document, plan)
        assert result["status"] == "completed"
        assert result["verified"]
        history_path = root / result["history_path"]
        assert history_path.name == "2026-09-09｜测试：最终标题？.md"
        history_text = history_path.read_text(encoding="utf-8")
        assert "## 可延展选题\n\n- 待根据发布后咨询问题补充" in history_text
        assert "## 关联内容\n\n- 暂无直接关联内容" in history_text
        assert "这是用户确认并已经发布的完整正文。" in history_text

        log = root / "accounts" / ACCOUNT / "内容库" / "03-选题规划" / "推荐记录" / "2026-09.jsonl"
        assert len(log.read_text(encoding="utf-8").splitlines()) == 2
        candidate_text = (
            root / "accounts" / ACCOUNT / "内容库" / "03-选题规划" / "测试选题池.md"
        ).read_text(encoding="utf-8")
        assert "- 状态：已发布" in candidate_text
        assert f"- 内容ID：{CONTENT_ID}" in candidate_text

        second_plan = MODULE.make_plan(root, document)
        assert second_plan["history_action"] == "already_present"
        assert second_plan["new_event_ids"] == []
        assert second_plan["candidate_action"] == "none"
        second = MODULE.apply_sync(root, document, second_plan)
        assert second["status"] == "already_synced"
        assert len(log.read_text(encoding="utf-8").splitlines()) == 2

        verified = MODULE.verify_sync(root, document)
        assert verified["verified"], verified["errors"]

        cli_check = subprocess.run(
            [sys.executable, str(SCRIPT_PATH), "--repo-root", str(root), "check", "--input", str(document_path)],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        assert json.loads(cli_check.stdout)["status"] == "ready"
        cli_sync = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--repo-root",
                str(root),
                "sync-published",
                "--input",
                str(document_path),
                "--apply",
            ],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        assert json.loads(cli_sync.stdout)["status"] == "already_synced"
        assert not (root / ".wxv-ops.lock").exists()

        changed_path = root / f"Repo内容文档｜{CONTENT_ID}｜正文冲突.md"
        changed_path.write_text(
            repo_document(valid_payload()).replace(
                "这是用户确认并已经发布的完整正文。",
                "这是同一内容 ID 下不同的正文。",
            ),
            encoding="utf-8",
        )
        changed_document = MODULE.load_repo_document(changed_path)
        try:
            MODULE.make_plan(root, changed_document)
        except MODULE.OperationError as exc:
            assert exc.status == "conflict"
            assert any("body differs" in error for error in exc.errors)
        else:
            raise AssertionError("same content_id with a different body must fail")

        broken_payload = valid_payload()
        broken_payload["account_id"] = "gzxzcs"
        broken_path = root / f"Repo内容文档｜{CONTENT_ID}｜错误账号.md"
        broken_path.write_text(repo_document(broken_payload), encoding="utf-8")
        try:
            MODULE.load_repo_document(broken_path)
        except MODULE.OperationError as exc:
            assert exc.status == "invalid_document"
        else:
            raise AssertionError("payload mismatch must fail")

    print("WXV OPS TESTS PASSED")


if __name__ == "__main__":
    main()
