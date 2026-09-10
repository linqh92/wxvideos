# Confirmed Copy Delivery Schema

本文件定义文案阶段被用户最终确认后的交付文件。最终文案文件用于承载已经确定的内容，不是 Handoff，也不延续文案对话中的推理、草稿或淘汰方案。

## 完成门槛

- 用户必须明确确认最终正文；仍在修改、比较或局部确认时不得生成最终文件。
- Repo 内容文档必须有且只有一个最终标题。存在多个标题方案但用户尚未选定时，先提醒用户选择，或取得用户明确授权后代选；不得把沉默视为选择。
- 口播完整方案包含三个主标题方案。用户只确认口播正文、没有明确选择主标题时，将正文标记为“已确认，标题待确认”，主动提醒后停止，不生成最终文件。
- 常规搜索标题和短标题是派生用途标题，不自动代替用户应选择的最终主标题；只有用户明确指定时才可作为最终标题。
- 标题确认后，创建或复用 `shared/schemas/content-identity-schema.md` 定义的稳定 `content_id`。后续改标题或修订同一内容时仍复用该 ID。
- Repo 内容文档采用个人发布回填约定：最终内容确认后进入制作发布，文档使用 `publication_status: published_by_user`、实际 `publish_date` 和 `requested_repo_action: archive_published_content` 表达后续 Codex 归档意图。用户提供其他发布日期时使用其明确日期；未提供时使用 `confirmed_at` 的本地日期。

## 项目文件交付

凡后续步骤要求在同一 ChatGPT 项目的新对话中通过 `@` 引用的交付文件，必须添加到当前项目来源。仅生成可下载文件或当前对话临时附件不视为完成。添加后确认文件已出现在项目来源中，并可按完整文件名通过 `@` 选择。

当前环境无法直接添加时，交付文件并明确告知用户该文件尚未加入项目来源，提示其手动添加；不得声称已经可以通过 `@` 引用。

## 交付数量

### 短文字幕

最终确认后生成一份文件：

```text
Repo内容文档｜{content_id}｜{内容简称}.md
```

生成后结束短文阶段，不询问或生成 Handoff，也不进入发布归档。

### 口播内容

最终正文和最终标题均确认后，同时生成两份文件：

```text
Repo内容文档｜{content_id}｜{内容简称}.md
视觉规划输入｜{content_id}｜{内容简称}.md
```

无论用户是否立即开始视觉规划，两份文件都生成。生成后结束口播阶段；不得在同一对话加载或执行视觉 Skill。

## Repo 内容文档

该文件供用户完成制作发布后，切换到具有仓库能力的 Codex 任务并通过 `@` 引用。文件记录最终发布内容、发布回填事实和预期归档动作。用户在当前 Codex 任务中明确要求“同步”或“录入”时，构成发布归档指令；仅引用或查看文件时保持只读。Codex 仍须读取最新根 `AGENTS.md`，核验账号、内容身份、日期、重复记录与允许的写入目标。

必填 Frontmatter：

```yaml
---
delivery_version: "1.1"
document_type: "repo_content"
content_id: "wxv-{account_id}-{YYYYMMDD}-{8hex}"
account_id: "{CURRENT_ACCOUNT}"
content_format: "text_broadcast | spoken"
approval_status: "confirmed_by_user"
confirmed_at: "YYYY-MM-DDTHH:MM:SS+08:00"
publication_status: "published_by_user"
publish_date: "YYYY-MM-DD"
requested_repo_action: "archive_published_content"
final_title: "用户最终选择的标题"
topic_id: "string | null"
topic_origin: "project_recommendation | direct_user_input"
recommendation_batch_id: "uuid | null"
topic_feedback_status: "synced | pending | not_applicable"
feedback_event_id: "uuid | null"
repo_sync_status: "not_synced"
---
```

正文只保留 Repo 执行所需的正式信息：

~~~markdown
# {最终标题}

## 选题来源与反馈

- topic_origin: project_recommendation | direct_user_input
- recommendation_batch_id: <uuid 或 null>
- topic_id: <选题 ID 或 null>
- feedback_event_id: <uuid 或 null>
- feedback_signal: selected | not_applicable
- feedback_scope: topic | not_applicable
- user_text: <用户选择该题的原话；直接给题时写“不适用”>
- scope_description: <被选择的具体题目；直接给题时写“不适用”>
- occurred_at: <反馈发生时间；不适用时写 null>
- topic_feedback_status: synced | pending | not_applicable

## 最终正文

<用户确认的完整短文或口播正文>

## 关键事实与改变结论的条件

- <仅保留会影响内容可靠性或适用范围的事实和条件>

## 来源引用

- <实际使用且可重新定位的来源；没有则写“无”>

## 用户确认与保留项

- 用户确认原话：<原话>
- 必须保留：<没有则写“无”>

## 发布回填

- publication_status: published_by_user
- publish_date: YYYY-MM-DD
- requested_repo_action: archive_published_content

## Repo 操作载荷

```json
{
  "schema_version": "1.0",
  "action": "archive_published_content",
  "account_id": "{CURRENT_ACCOUNT}",
  "content_id": "wxv-{account_id}-{YYYYMMDD}-{8hex}",
  "content_format": "text_broadcast | spoken",
  "publish_date": "YYYY-MM-DD",
  "final_title": "用户最终选择的标题",
  "archive_metadata": {
    "business_line": "当前账号固定选项或允许值",
    "theme": "当前账号固定选项或允许值",
    "content_type": "当前账号固定选项或允许值",
    "audience": "当前账号固定选项或允许值",
    "pain_scene": "一个主要客户场景",
    "content_goal": "知识库可追踪目标",
    "region": "当前账号既定地区",
    "platform": "微信视频号",
    "series": "所属系列",
    "source": "用户确认发布内容",
    "summary": "2～4句内容概述",
    "audience_description": "具体客户类型、阶段或业务状态",
    "pain_scene_description": "客户在什么情况下遇到什么困难",
    "extension_topics": [],
    "related_content": []
  },
  "pending_repo_actions": []
}
```
~~~

### 选题反馈继承规则

- 文案来源是选题 Handoff 时，Repo 内容文档必须继承其中的选题来源、推荐批次、`selected` 反馈、用户原话、作用范围、事件 ID 和同步状态。
- Handoff 中尚未执行的 `pending_repo_actions` 必须原样继承到 Repo 内容文档；不得因为文案阶段结束、文件改名或已生成正文而丢弃、概括或重新生成事件 ID。
- 如果原推荐批次和选择反馈均已成功写入 Repo，保留对应 ID 并标记 `topic_feedback_status: synced`，无需重复加入待执行动作。
- 如果任一记录尚未写入，标记 `topic_feedback_status: pending`。待执行动作必须带稳定 `action_id`、明确目标路径和符合 `topic-recommendation-log-schema.md` 的完整事件 payload，使 Codex 能按 `event_id` 幂等补写；原推荐批次尚未入库时，必须同时携带完整 recommendation 事件和 selected feedback 事件，不能只写一个引用不存在批次的反馈。
- 用户直接给题、直接提供参考内容重写且没有经过项目推荐时，使用 `topic_origin: direct_user_input`、`topic_feedback_status: not_applicable`，相关批次和反馈 ID 为 `null`；不得虚构推荐或选择反馈。
- 文案 Skill 只能把这些字段作为 Repo 追踪信息原样转交，不得加载推荐历史、利用未采用选题改写当前内容或把待执行动作当成新的用户授权。

Repo 操作载荷的完整字段、执行命令和结果状态统一引用 `shared/schemas/repo-operation-schema.md`。其中归档分类、内容概述、目标客户描述和痛点场景描述在文案最终确认时根据当前账号规则与最终内容一次性确定；`extension_topics` 和 `related_content` 常规使用空数组。

`pending_repo_actions` 只记录项目规则本来允许、但当前环境无法执行的动作。推荐与反馈事件使用如下自包含结构；没有待执行动作时保留空数组：

```json
{
  "action_id": "uuid",
  "action_type": "append_topic_recommendation_events",
  "target_path": "accounts/{account_id}/内容库/03-选题规划/推荐记录/YYYY-MM.jsonl",
  "source_schema": "shared/schemas/topic-recommendation-log-schema.md",
  "events": [
    {"完整 recommendation 事件": "已经存在时可省略"},
    {"完整 selected feedback 事件": "必填"}
  ]
}
```

Codex 在用户明确要求“同步”或“录入”时，由 `publish-archive` 调用 `shared/scripts/wxv-ops.py sync-published --apply`。脚本按事件 ID 幂等补写待执行推荐与反馈、写入历史事实源并更新索引；存在对应候选时将其更新为 `已发布`，没有对应候选时不创建候选卡。

## 视觉规划输入文档

该文件只供新的 `spoken-visual-planning` 对话通过 `@` 引用，保留在 ChatGPT 项目中，不写入 Repo。它是视觉阶段唯一的上一阶段工作成果。

必填 Frontmatter：

```yaml
---
delivery_version: "1.0"
document_type: "spoken_visual_input"
content_id: "wxv-{account_id}-{YYYYMMDD}-{8hex}"
account_id: "{CURRENT_ACCOUNT}"
content_format: "spoken"
approval_status: "confirmed_by_user"
confirmed_at: "YYYY-MM-DDTHH:MM:SS+08:00"
final_title: "用户最终选择的标题"
topic_id: "string | null"
repo_sync_status: "not_applicable"
---
```

正文结构：

```markdown
# 视觉规划输入｜{最终标题}

## 最终标题

<只保留用户最终选择的一个标题>

## 最终口播正文

<用户确认的完整口播正文>

## 关键事实与改变结论的条件

- <视觉资料必须保持一致的事实和条件>

## 已批准来源

- <视觉规划确实需要的来源；没有则写“无”>

## 不可改动项

- <用户明确要求保留的结论、数据、表述或范围；没有则写“无”>

## 视觉阶段允许调整

- PPT 的信息架构、分页、页面标题、说明文字、视觉形式和剪辑对应关系可按视觉 Skill 调整，但不得改写最终口播正文或改变已确认专业结论。
```

不得带入其余标题方案、未采用正文、修改过程、文案 Skill、选题反馈、推荐批次、选题检索过程、历史索引、Repo 操作说明或 `pending_repo_actions`。

## 更新与冲突

- 同一内容重新确认标题或正文时，重生成对应文件并保留原 `content_id`，以最新 `confirmed_at` 为准。
- 两份口播文件的 `content_id`、`account_id`、`final_title`、最终正文和关键事实必须一致。
- 文件间存在冲突，或标题、正文、账号任一项无法唯一确定时，不得进入 Repo 执行或视觉规划，应先让用户确认。
