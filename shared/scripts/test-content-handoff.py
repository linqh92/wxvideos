#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("content-handoff.py")
SPEC = importlib.util.spec_from_file_location("content_handoff", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def valid_packet(content_id: str) -> str:
    return f'''---
handoff_version: "1.0"
content_id: "{content_id}"
account_id: "gzminge"
from_stage: "topic_planning"
to_stage: "spoken_copywriting"
approval_status: "confirmed_by_user"
confirmed_at: "2026-09-09T10:30:00+08:00"
repo_sync_status: "synced"
content_format: "spoken"
topic_id: "11111111-1111-4111-8111-111111111111"
topic_origin: "project_recommendation"
recommendation_batch_id: "22222222-2222-4222-8222-222222222222"
topic_feedback_status: "synced"
feedback_event_id: "33333333-3333-4333-8333-333333333333"
---

# Handoff｜{content_id}

## 用户确认原话
> 确认

## 已确认成果
已采用选题。

## 选题来源与反馈
- recommendation_batch_id: 22222222-2222-4222-8222-222222222222
- topic_id: 11111111-1111-4111-8111-111111111111
- feedback_event_id: 33333333-3333-4333-8333-333333333333
- feedback_signal: selected
- feedback_scope: topic
- user_text: 选择这个题
- scope_description: 已采用选题
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
- pending_repo_actions: []
'''


def main() -> None:
    content_id = MODULE.create_content_id("gzminge", "2026-09-09", "a1b2c3d4")
    assert content_id == "wxv-gzminge-20260909-a1b2c3d4"

    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / f"Handoff｜{content_id}｜topic_planning-to-spoken_copywriting.md"
        path.write_text(valid_packet(content_id), encoding="utf-8")
        result = MODULE.validate_handoff(path)
        assert result["valid"], result["errors"]

        broken = path.with_name(f"Handoff｜{content_id}｜topic_planning-to-text_broadcast_copywriting.md")
        broken.write_text(valid_packet(content_id).replace('account_id: "gzminge"', 'account_id: "gzxzcs"'), encoding="utf-8")
        result = MODULE.validate_handoff(broken)
        assert not result["valid"]
        assert any("account_id does not match" in error for error in result["errors"])

        legacy = path.with_name(f"Handoff｜{content_id}｜spoken_copywriting-to-spoken_visual_planning.md")
        legacy.write_text(
            valid_packet(content_id)
            .replace('from_stage: "topic_planning"', 'from_stage: "spoken_copywriting"')
            .replace('to_stage: "spoken_copywriting"', 'to_stage: "spoken_visual_planning"'),
            encoding="utf-8",
        )
        result = MODULE.validate_handoff(legacy)
        assert not result["valid"]
        assert any("from_stage is invalid" in error for error in result["errors"])
        assert any("to_stage is invalid" in error for error in result["errors"])

    print("CONTENT HANDOFF TESTS PASSED")


if __name__ == "__main__":
    main()
