#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("content-handoff.py")
SPEC = importlib.util.spec_from_file_location("content_handoff", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


TOPIC_ID = "11111111-1111-4111-8111-111111111111"
BATCH_ID = "22222222-2222-4222-8222-222222222222"
FEEDBACK_EVENT_ID = "33333333-3333-4333-8333-333333333333"
RECOMMENDATION_EVENT_ID = "66666666-6666-4666-8666-666666666666"
ACTION_ID = "77777777-7777-4777-8777-777777777777"
SECOND_ACTION_ID = "88888888-8888-4888-8888-888888888888"


def valid_packet(content_id: str) -> str:
    return f'''---
handoff_version: "1.1"
content_id: "{content_id}"
account_id: "gzminge"
topic_short_name: "出口退税风险判断"
from_stage: "topic_planning"
to_stage: "spoken_copywriting"
approval_status: "confirmed_by_user"
confirmed_at: "2026-09-09T10:30:00+08:00"
repo_sync_status: "synced"
content_format: "spoken"
topic_id: "{TOPIC_ID}"
topic_origin: "project_recommendation"
recommendation_batch_id: "{BATCH_ID}"
topic_feedback_status: "synced"
feedback_event_id: "{FEEDBACK_EVENT_ID}"
---

# 选题交接｜出口退税风险判断

## 用户确认原话
> 确认

## 已确认成果
已选定选题。

## 选题来源与反馈
- recommendation_batch_id: 22222222-2222-4222-8222-222222222222
- topic_id: 11111111-1111-4111-8111-111111111111
- feedback_event_id: 33333333-3333-4333-8333-333333333333
- feedback_signal: selected
- feedback_scope: topic
- user_text: 选择这个题
- scope_description: 已选定选题
- occurred_at: 2026-09-09T10:30:00+08:00
- topic_feedback_status: synced

## 关键事实与改变结论的条件
- 条件一。

## 来源引用
- 无。

## 用户要求与保留项
- 保留结论。

## 允许调整
- 口播表达。

## 禁止动作
- 不重做选题。

## 待执行仓库动作
```json
{{
  "pending_repo_actions": []
}}
```
'''


def recommendation_event() -> dict:
    return {
        "event_id": RECOMMENDATION_EVENT_ID,
        "event_type": "recommendation",
        "occurred_at": "2026-09-09T10:00:00+08:00",
        "account_id": "gzminge",
        "batch_id": BATCH_ID,
        "topics": [{"topic_id": TOPIC_ID}],
    }


def feedback_event() -> dict:
    return {
        "event_id": FEEDBACK_EVENT_ID,
        "event_type": "feedback",
        "occurred_at": "2026-09-09T10:05:00+08:00",
        "account_id": "gzminge",
        "batch_id": BATCH_ID,
        "topic_ids": [TOPIC_ID],
        "signal": "selected",
    }


def pending_packet(content_id: str, actions: list[dict]) -> str:
    payload = json.dumps({"pending_repo_actions": actions}, ensure_ascii=False, indent=2)
    return (
        valid_packet(content_id)
        .replace('repo_sync_status: "synced"', 'repo_sync_status: "not_synced"')
        .replace('topic_feedback_status: "synced"', 'topic_feedback_status: "pending"')
        .replace("- topic_feedback_status: synced", "- topic_feedback_status: pending")
        .replace(
            '```json\n{\n  "pending_repo_actions": []\n}\n```',
            f"```json\n{payload}\n```",
        )
    )


def canonical_actions() -> list[dict]:
    return [
        {
            "action_id": ACTION_ID,
            "action_type": "append_topic_recommendation_events",
            "target_path": "accounts/gzminge/内容库/03-选题规划/推荐记录/2026-09.jsonl",
            "source_schema": "shared/schemas/topic-recommendation-log-schema.md",
            "events": [recommendation_event(), feedback_event()],
        }
    ]


def legacy_actions() -> list[dict]:
    return [
        {
            "action_id": ACTION_ID,
            "action": "append_topic_recommendation_event",
            "target_path": "accounts/gzminge/内容库/03-选题规划/推荐记录/2026-09.jsonl",
            "payload": recommendation_event(),
        },
        {
            "action_id": SECOND_ACTION_ID,
            "action": "append_topic_feedback_event",
            "target_path": "accounts/gzminge/内容库/03-选题规划/推荐记录/2026-09.jsonl",
            "payload": feedback_event(),
        },
    ]


def main() -> None:
    content_id = MODULE.create_content_id("gzminge", "2026-09-09", "a1b2c3d4")
    assert content_id == "wxv-gzminge-20260909-a1b2c3d4"

    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "选题交接｜gzminge｜出口退税风险判断｜20260909-103000.md"
        path.write_text(valid_packet(content_id), encoding="utf-8")
        result = MODULE.validate_handoff(path)
        assert result["valid"], result["errors"]

        pending_path = path.with_name("选题交接｜gzminge｜出口退税风险判断｜20260909-103000.md")
        pending_path.write_text(pending_packet(content_id, canonical_actions()), encoding="utf-8")
        result = MODULE.validate_handoff(pending_path)
        assert result["valid"], result["errors"]

        pending_path.write_text(pending_packet(content_id, legacy_actions()), encoding="utf-8")
        result = MODULE.validate_handoff(pending_path)
        assert result["valid"], result["errors"]

        unknown_actions = canonical_actions()
        unknown_actions[0]["action_type"] = "append_invented_event"
        pending_path.write_text(pending_packet(content_id, unknown_actions), encoding="utf-8")
        result = MODULE.validate_handoff(pending_path)
        assert not result["valid"]
        assert any("unsupported pending action" in error for error in result["errors"])

        mismatched_actions = canonical_actions()
        mismatched_actions[0]["events"][1]["topic_ids"] = ["99999999-9999-4999-8999-999999999999"]
        pending_path.write_text(pending_packet(content_id, mismatched_actions), encoding="utf-8")
        result = MODULE.validate_handoff(pending_path)
        assert not result["valid"]
        assert any("pending selected feedback payload" in error for error in result["errors"])

        path.write_text(valid_packet(content_id), encoding="utf-8")

        second_content_id = MODULE.create_content_id("gzminge", "2026-09-09", "b2c3d4e5")
        second_path = Path(directory) / "选题交接｜gzminge｜成本合规判断｜20260909-103000.md"
        second_path.write_text(
            valid_packet(second_content_id)
            .replace("出口退税风险判断", "成本合规判断")
            .replace("11111111-1111-4111-8111-111111111111", "44444444-4444-4444-8444-444444444444")
            .replace("33333333-3333-4333-8333-333333333333", "55555555-5555-4555-8555-555555555555"),
            encoding="utf-8",
        )
        second_result = MODULE.validate_handoff(second_path)
        assert second_result["valid"], second_result["errors"]

        first_meta = MODULE.parse_frontmatter(path.read_text(encoding="utf-8"))
        second_meta = MODULE.parse_frontmatter(second_path.read_text(encoding="utf-8"))
        assert first_meta["recommendation_batch_id"] == second_meta["recommendation_batch_id"]
        assert first_meta["content_id"] != second_meta["content_id"]
        assert first_meta["topic_id"] != second_meta["topic_id"]
        assert first_meta["feedback_event_id"] != second_meta["feedback_event_id"]

        wrong_name = path.with_name("选题交接｜gzminge｜泛称｜20260909-103000.md")
        wrong_name.write_text(valid_packet(content_id), encoding="utf-8")
        result = MODULE.validate_handoff(wrong_name)
        assert not result["valid"]
        assert any("filename must be" in error for error in result["errors"])

        invalid_short_name = path.with_name("选题交接｜gzminge｜题目含空格｜20260909-103000.md")
        invalid_short_name.write_text(
            valid_packet(content_id).replace('topic_short_name: "出口退税风险判断"', 'topic_short_name: "题目 含空格"'),
            encoding="utf-8",
        )
        result = MODULE.validate_handoff(invalid_short_name)
        assert not result["valid"]
        assert any("topic_short_name must be" in error for error in result["errors"])

        broken = path.with_name("选题交接｜gzxzcs｜出口退税风险判断｜20260909-103000.md")
        broken.write_text(valid_packet(content_id).replace('account_id: "gzminge"', 'account_id: "gzxzcs"'), encoding="utf-8")
        result = MODULE.validate_handoff(broken)
        assert not result["valid"]
        assert any("account_id does not match" in error for error in result["errors"])

        legacy = path.with_name(f"Handoff｜{content_id}｜topic_planning-to-spoken_copywriting.md")
        legacy.write_text(
            valid_packet(content_id)
            .replace('handoff_version: "1.1"', 'handoff_version: "1.0"')
            .replace('topic_short_name: "出口退税风险判断"\n', ''),
            encoding="utf-8",
        )
        result = MODULE.validate_handoff(legacy)
        assert result["valid"], result["errors"]

        legacy_bullet = legacy.with_name(f"Handoff｜{content_id}｜topic_planning-to-spoken_copywriting.md")
        legacy_bullet.write_text(
            legacy.read_text(encoding="utf-8").replace(
                '```json\n{\n  "pending_repo_actions": []\n}\n```',
                "- pending_repo_actions: []",
            ),
            encoding="utf-8",
        )
        result = MODULE.validate_handoff(legacy_bullet)
        assert result["valid"], result["errors"]

        invalid_transition = path.with_name(f"Handoff｜{content_id}｜spoken_copywriting-to-spoken_visual_planning.md")
        invalid_transition.write_text(
            valid_packet(content_id)
            .replace('handoff_version: "1.1"', 'handoff_version: "1.0"')
            .replace('topic_short_name: "出口退税风险判断"\n', '')
            .replace('from_stage: "topic_planning"', 'from_stage: "spoken_copywriting"')
            .replace('to_stage: "spoken_copywriting"', 'to_stage: "spoken_visual_planning"'),
            encoding="utf-8",
        )
        result = MODULE.validate_handoff(invalid_transition)
        assert not result["valid"]
        assert any("from_stage is invalid" in error for error in result["errors"])
        assert any("to_stage is invalid" in error for error in result["errors"])

    print("CONTENT HANDOFF TESTS PASSED")


if __name__ == "__main__":
    main()
