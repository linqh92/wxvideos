---
name: publish-archive
description: 将用户确认已发布并明确要求同步、录入或归档的内容写入当前账号历史库；结构化 Repo 内容文档优先通过确定性脚本执行。
---

# 微信视频号发布归档

## Trigger

以下任一入口成立时使用：

1. 用户明确引用有效 Repo 内容文档，并在当前可写 Codex 任务中要求“检查”“同步”或“录入”；文档必须包含 `publication_status: published_by_user`、`publish_date` 和 `requested_repo_action: archive_published_content`；
2. 用户通过其他输入明确确认内容已实际发布或更新完成，并明确要求归档、写入知识库或保存到历史内容。

只引用或查看 Repo 内容文档时保持只读。用户只说“已发布”时准备可唯一识别的归档预览。实际发布标题、正文或日期不能唯一确定时先询问；不得猜测或覆盖现有记录。

## Structured Repo Document

`delivery_version: "1.1"`、`document_type: "repo_content"` 且包含 `Repo 操作载荷` 的文件使用 `shared/schemas/repo-operation-schema.md` 定义的确定性入口。

- 用户要求“检查”时，运行 `shared/scripts/wxv-ops.py check --input <path>`，只返回计划，不写入。
- 用户要求“同步”或“录入”时，该指令授权当前 Repo 文档指定的动作；运行 `shared/scripts/wxv-ops.py sync-published --input <path> --apply`。
- 使用当前环境已经配置的 Python 运行时。脚本内部完成预检、幂等写入和执行后核验。
- `completed`、`already_synced` 或 `verified` 按脚本结果直接报告；`invalid_document`、`conflict`、`partial_failure` 按错误项停止或进入针对性处理。

脚本成功时不重新解释正文或重复执行文件写入。旧版 Repo 内容文档和其他非结构化归档入口继续使用下述规则。

## Exceptions

结构化 1.1 Repo 文档正常执行只读取根 `AGENTS.md` 与本 Skill，然后把输入路径交给脚本。脚本已经包含账号、身份、事件、历史、索引和候选的固定校验；`shared/schemas/repo-operation-schema.md` 仅在解释接口或处理格式错误时读取。

以下情况读取 [manual-archive.md](references/manual-archive.md)，并只加载该文件指向的相关规则：

- `delivery_version: "1.0"` 的 Repo 内容文档；
- 非结构化发布输入；
- 脚本返回 `invalid_document`、`conflict` 或 `partial_failure`。

脚本成功时不加载人工归档 reference。语义延展、关联内容判断和灵感回流只在用户明确要求的单独任务中执行。

## Stop

完成允许的归档、索引同步和候选终态更新后立即停止。不得自动生成下一批选题、文案或灵感，也不得自动重建内容地图、缺口分析、重复检查、月度复盘或其他派生资产。
