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
from_stage: "spoken_copywriting"
to_stage: "spoken_visual_planning"
approval_status: "confirmed_by_user"
confirmed_at: "2026-09-09T10:30:00+08:00"
repo_sync_status: "not_synced"
content_format: "spoken"
topic_id: "null"
---

# Handoff｜{content_id}

## 用户确认原话
> 确认

## 已确认成果
完整口播。

## 关键事实与改变结论的条件
- 条件一。

## 来源引用
- 无。

## 用户要求与保留项
- 保留结论。

## 允许调整
- 视觉结构。

## 禁止动作
- 不重写口播。

## 待执行仓库动作
- pending_repo_actions: []
'''


def main() -> None:
    content_id = MODULE.create_content_id("gzminge", "2026-09-09", "a1b2c3d4")
    assert content_id == "wxv-gzminge-20260909-a1b2c3d4"

    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / f"Handoff｜{content_id}｜spoken_copywriting-to-spoken_visual_planning.md"
        path.write_text(valid_packet(content_id), encoding="utf-8")
        result = MODULE.validate_handoff(path)
        assert result["valid"], result["errors"]

        broken = path.with_name(f"Handoff｜{content_id}｜spoken_copywriting-to-repo_sync.md")
        broken.write_text(valid_packet(content_id).replace('account_id: "gzminge"', 'account_id: "gzxzcs"'), encoding="utf-8")
        result = MODULE.validate_handoff(broken)
        assert not result["valid"]
        assert any("account_id does not match" in error for error in result["errors"])

    print("CONTENT HANDOFF TESTS PASSED")


if __name__ == "__main__":
    main()
