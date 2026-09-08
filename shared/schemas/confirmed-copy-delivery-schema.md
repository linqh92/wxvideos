# Confirmed Copy Delivery Schema

本文件定义文案阶段被用户最终确认后的交付文件。最终文案文件用于承载已经确定的内容，不是 Handoff，也不延续文案对话中的推理、草稿或淘汰方案。

## 完成门槛

- 用户必须明确确认最终正文；仍在修改、比较或局部确认时不得生成最终文件。
- Repo 内容文档必须有且只有一个最终标题。存在多个标题方案但用户尚未选定时，先提醒用户选择，或取得用户明确授权后代选；不得把沉默视为选择。
- 口播完整方案包含三个主标题方案。用户只确认口播正文、没有明确选择主标题时，将正文标记为“已确认，标题待确认”，主动提醒后停止，不生成最终文件。
- 常规搜索标题和短标题是派生用途标题，不自动代替用户应选择的最终主标题；只有用户明确指定时才可作为最终标题。
- 标题确认后，创建或复用 `shared/schemas/content-identity-schema.md` 定义的稳定 `content_id`。后续改标题或修订同一内容时仍复用该 ID。

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

该文件供用户切换到具有仓库能力的 Codex 任务后通过 `@` 引用。它是已确认内容的 Repo 执行输入，不表示内容已经写入 Repo、实际发布或获得归档授权。Codex 仍须读取最新根 `AGENTS.md`，并按用户在该任务中的明确指令判断允许的写入目标和动作。

必填 Frontmatter：

```yaml
---
delivery_version: "1.0"
document_type: "repo_content"
content_id: "wxv-{account_id}-{YYYYMMDD}-{8hex}"
account_id: "{CURRENT_ACCOUNT}"
content_format: "text_broadcast | spoken"
approval_status: "confirmed_by_user"
confirmed_at: "YYYY-MM-DDTHH:MM:SS+08:00"
final_title: "用户最终选择的标题"
topic_id: "string | null"
repo_sync_status: "not_synced"
---
```

正文只保留 Repo 执行所需的正式信息：

```markdown
# {最终标题}

## 最终正文

<用户确认的完整短文或口播正文>

## 关键事实与改变结论的条件

- <仅保留会影响内容可靠性或适用范围的事实和条件>

## 来源引用

- <实际使用且可重新定位的来源；没有则写“无”>

## 用户确认与保留项

- 用户确认原话：<原话>
- 必须保留：<没有则写“无”>

## 待执行仓库动作

- pending_repo_actions: []
```

`pending_repo_actions` 只记录用户已经明确要求、但当前只读环境无法执行的动作。仅生成这份文件本身不产生 Repo 写入授权，也不得预设尚不存在的仓库存储位置。

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

不得带入其余标题方案、未采用正文、修改过程、文案 Skill、选题检索过程、历史索引、Repo 操作说明或 `pending_repo_actions`。

## 更新与冲突

- 同一内容重新确认标题或正文时，重生成对应文件并保留原 `content_id`，以最新 `confirmed_at` 为准。
- 两份口播文件的 `content_id`、`account_id`、`final_title`、最终正文和关键事实必须一致。
- 文件间存在冲突，或标题、正文、账号任一项无法唯一确定时，不得进入 Repo 执行或视觉规划，应先让用户确认。
