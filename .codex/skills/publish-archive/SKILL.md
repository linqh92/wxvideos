---
name: publish-archive
description: 将用户确认已发布并明确要求同步、录入或归档的内容写入当前账号历史库，增量更新 History Index，并把存在的对应候选标记为已发布。
---

# 微信视频号发布归档

## Trigger

以下任一入口成立时使用：

1. 用户明确引用有效 Repo 内容文档，并在当前可写 Codex 任务中要求“同步”或“录入”；文档必须包含 `publication_status: published_by_user`、`publish_date` 和 `requested_repo_action: archive_published_content`；
2. 用户通过其他输入明确确认内容已实际发布或更新完成，并明确要求归档、写入知识库或保存到历史内容。

只引用或查看 Repo 内容文档时保持只读。用户只说“已发布”时准备可唯一识别的归档预览。实际发布标题、正文或日期不能唯一确定时先询问；不得猜测或覆盖现有记录。

## Required Input

- 实际发布标题、正文和发布日期；
- 实际发布载体；
- 已存在的稳定 `content_id`；迁移前形成且尚未建立 ID 的内容，须先唯一确认账号与内容，再为其新建 ID，不得借用另一条内容的 ID；
- Repo 内容文档入口所需的发布回填字段与当前“同步/录入”指令，或其他入口中的实际发布确认与明确归档指令；
- 根 `AGENTS.md` 已唯一确定的 `CURRENT_ACCOUNT`。

## Required Context

账号选择、隔离、阶段边界和项目级写入权限服从根 `AGENTS.md`。状态含义与转换引用：

```text
shared/schemas/content-state-machine.md
```

归档前完整读取并严格遵循：

```text
accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/历史内容归档规范.md
```

该文件是当前账号历史路径、文件名、Frontmatter、正文结构和完成检查的事实来源。

用户明确引用 Repo 内容文档时，先按 `shared/schemas/confirmed-copy-delivery-schema.md` 和 `shared/schemas/content-identity-schema.md` 校验账号、内容身份、唯一标题、最终正文、`publication_status`、`publish_date` 与 `requested_repo_action`。当前任务中的“同步”或“录入”指令授权执行该文档指定的发布归档动作。视觉规划输入、PPT 文件、视觉执行指南和剪辑分段表不属于归档输入，也不得写入 Repo。

Repo 内容文档包含未完成 `pending_repo_actions` 时，读取 `shared/schemas/topic-recommendation-log-schema.md` 与 `shared/rules/topic-memory-reading.md`，按其中的事件幂等、缓存和反馈摘要规则执行。

## Unique Logic

归档前唯一确认实际发布内容的 `content_format`，只允许：

```text
text_broadcast
spoken
```

来源优先级为：用户明确确认的发布载体 > 本次生成阶段的 `CONTENT_FORMAT`。`recommended_format` 只是选题建议，不得直接代替实际发布载体。无法判断时先询问，不得根据篇幅、候选建议或旧内容形式猜测。

1. Repo 内容文档存在 `pending_repo_actions` 时，先核验目标账号、月份、事件 ID 和原日志，以稳定 ID 幂等补写 recommendation 与 selected feedback 事件，再增量同步本账号推荐检索缓存；同一事件已存在时跳过。
2. 检查目标目录中的同名和疑似重复笔记；存在冲突时停止并报告。
3. 只写实际使用的 `content_id`、标题、正文、实际发布日期和实际 `content_format`，不保存 Handoff、备选标题、草稿过程、视觉文件或未发布信息。历史库中已经存在的旧归档不强制回填 ID。
4. 历史 Markdown 写入成功后，以 `path` 为键 append/update `01-历史内容/_history-index.jsonl` 的单条记录，不全库扫描。
5. 找到对应候选时，无论当前为 `待核验` 还是 `可推荐`，将候选 Markdown 和 `_candidate-index.jsonl` 更新为 `已发布` 并写入同一 `content_id`；没有对应候选时不创建候选卡。只有本 Skill 可以执行该发布转换。
6. 内容地图、内容缺口、重复检查、月度复盘和统计仅在用户明确要求时通过 `shared/scripts/rebuild-derived-assets.ps1` 更新。

### 灵感回流

保留原有内容资产回流机制：从已发布内容提取 1～2 个不重复的后续问题，每个问题建立一篇 `历史延展` 灵感；真实评论、咨询或交付反馈存在时可分别建立灵感并关联历史内容。

新灵感使用公共状态机的初始状态，并以单条 append/update 方式同步 `_idea-index.jsonl`。

## Output

补写 Repo 内容文档携带的待执行推荐与反馈事件，写入一篇符合当前账号归档规范的正式历史 Markdown，增量更新对应 History Index；存在对应候选时同步更新候选 Markdown 与 Candidate Index，并按既有回流机制新增 1～2 条不重复后续灵感。

## Stop

完成允许的归档、索引同步、候选终态更新和灵感回流后立即停止。不得自动生成下一批选题或文案，也不得自动重建内容地图、缺口分析、重复检查、月度复盘或其他派生资产。
