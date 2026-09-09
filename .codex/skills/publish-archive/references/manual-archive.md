# Manual Archive Exceptions

本文件只用于 `delivery_version: "1.0"` 的 Repo 内容文档、非结构化发布输入，以及 `wxv-ops.py` 返回需要人工处理的错误。

## Required Input

- 根 `AGENTS.md` 已唯一确定的 `CURRENT_ACCOUNT`；
- 实际发布标题、正文、发布日期和载体；
- 已有稳定 `content_id`；迁移前内容缺少 ID 时，先唯一确认账号与内容再建立 ID；
- 实际发布确认与明确归档指令；
- Repo 内容文档存在时，保留其中的选题来源、事件 ID 和完整 `pending_repo_actions`。

无法唯一确定标题、正文、发布日期、载体、账号或内容身份时停止并询问，不得猜测、借用另一条内容的 ID 或覆盖已有事实。

## Required Context

按具体错误读取最小必要规则：

1. `shared/schemas/content-state-machine.md`；
2. 当前账号 `内容库/00-首页与维护规则/历史内容归档规范.md`；
3. Repo 文档入口读取 `shared/schemas/confirmed-copy-delivery-schema.md` 与 `shared/schemas/content-identity-schema.md`；
4. 存在待执行推荐事件时读取 `shared/schemas/topic-recommendation-log-schema.md` 与 `shared/rules/topic-memory-reading.md`。

视觉规划输入、PPT 文件、视觉执行指南和剪辑分段表不属于归档输入。

## Execution

实际 `content_format` 只允许 `text_broadcast` 或 `spoken`。来源优先级为：用户明确确认的发布载体、Repo 内容文档字段、本次生成阶段的 `CONTENT_FORMAT`。`recommended_format` 不能代替实际发布载体。

1. 按事件 ID 幂等补写允许的 recommendation 与 selected feedback；同一事件已经存在时跳过。`selected` 只记录选择事实，不建立长期偏好摘要。
2. 检查目标目录中的同名、相同 `content_id` 和疑似重复笔记；冲突时停止。
3. 历史 Markdown 只保存实际使用的标题、正文、发布日期、载体、归档元数据和稳定 `content_id`。
4. 历史写入成功后，以 `path` 为键增量维护 `_history-index.jsonl`。
5. 能唯一定位现有候选时，将候选 Markdown 与 `_candidate-index.jsonl` 更新为 `已发布` 并写入同一 `content_id`；没有对应候选时不创建候选卡。
6. 推荐事件写入成功后增量同步推荐检索缓存。

没有明确、可靠的延展题或关联内容时，使用当前账号归档规范允许的占位文本。后续问题提炼、关联内容判断与灵感回流属于单独的按需或批量任务。

内容地图、内容缺口、重复检查、月度复盘和统计只在用户明确要求时更新。Git 提交与推送服从根 `AGENTS.md` 的单独授权规则。

