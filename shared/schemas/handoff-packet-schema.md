# Handoff Packet Schema

Handoff Packet 用于在 ChatGPT 项目中的独立阶段对话之间传递已经确认的工作成果。它是临时交接文件，不是 Repo 资产、事实源、状态记录、索引或发布归档。

## 使用边界

- 仅在用户明确确认当前阶段成果后生成。
- 用户只确认时，先询问是否需要 Handoff；用户确认并明确要求进入下一阶段时，直接生成 Handoff 后停止当前阶段。
- Handoff 保留在 ChatGPT 项目中，由用户在新对话通过 `@` 明确引用；不得写入仓库。
- 新对话以最新明确引用且校验有效的 Handoff 作为唯一上一阶段工作成果，不重新加载上一阶段 Skill、检索历史、未采用方案或聊天记忆。
- Handoff 只传身份、确认结果、改变结论的条件、必要来源、用户原始反馈和权限，不复制 AGENTS、Skill、完整历史或无关上下文。

## 文件名

```text
Handoff｜{content_id}｜{from_stage}-to-{to_stage}.md
```

同一阶段重新确认后生成新文件时保留同一 `content_id`，并更新 `confirmed_at`。新对话只使用用户明确引用的最新文件。

## 必填 Frontmatter

```yaml
---
handoff_version: "1.0"
content_id: "wxv-{account_id}-{YYYYMMDD}-{8hex}"
account_id: "{CURRENT_ACCOUNT}"
from_stage: "topic_planning | text_broadcast_copywriting | spoken_copywriting | spoken_visual_planning"
to_stage: "text_broadcast_copywriting | spoken_copywriting | spoken_visual_planning | repo_sync | publish_archive | none"
approval_status: "confirmed_by_user"
confirmed_at: "YYYY-MM-DDTHH:MM:SS+08:00"
repo_sync_status: "not_synced | synced | not_applicable"
content_format: "text_broadcast | spoken | null"
topic_id: "string | null"
---
```

约束：

- `content_id` 按 `content-identity-schema.md` 创建并复用；
- `account_id` 必须与当前账号及 `content_id` 一致；
- `from_stage` 必须是刚完成并已确认的阶段；
- `to_stage` 必须来自用户明确要求，用户未指定下一阶段时使用 `none`；
- `approval_status` 只有在用户明确确认后才能写为 `confirmed_by_user`；
- `repo_sync_status` 只描述当前确认结果是否已进入 Repo；视觉阶段及视觉文件使用 `not_applicable`；
- `content_format` 从文案阶段开始必填；选题尚未确定载体时可为 `null`。

## 正文结构

```markdown
# Handoff｜{content_id}

## 用户确认原话

> 保留触发确认或阶段转换的用户原话。

## 已确认成果

完整放入下一阶段实际需要的确认内容，不依赖上一对话才能理解。

## 关键事实与改变结论的条件

- 只保留已确认且会影响表达、专业结论或视觉信息架构的事实和条件。

## 来源引用

- Repo 路径、候选 ID、推荐批次或实际使用的外部来源；没有则写“无”。

## 用户要求与保留项

- 必须保留的标题、表达、结构、语气、数据或其他明确决定。

## 允许调整

- 下一阶段为完成自身职责可以改变的内容。

## 禁止动作

- 不得回到上一阶段重新选题或推翻已确认结果；
- 不得执行 `to_stage` 之后的阶段；
- 不得把 Handoff 写入 Repo。

## 待执行仓库动作

- pending_repo_actions: []
```

`pending_repo_actions` 只记录当前环境因只读而未执行、且项目规则本来允许持久化的动作，例如推荐反馈记录或用户明确要求的同步。它不是执行授权；后续具有写入能力的环境仍须按当前 Skill、账号锁和写入规则重新校验。

## 阶段最小交接内容

### 选题 → 文案

必须包含已采用选题、目标客户与场景、客户决策问题、核心答案、改变结论的条件、建议或用户指定载体、必要来源和明确反馈。不带入其余候选与整批查重过程。

### 口播文案 → 视觉规划

必须包含最终标题、完整确认口播、关键事实与条件、已批准来源、用户要求和不可改动项。不带入未采用文案、文案 Skill、历史索引或选题检索过程。

### 内容 → Repo 同步或发布归档

必须包含最终确认内容、实际载体、必要身份和待执行动作。发布归档还必须由用户另行确认内容已经实际发布，并明确要求归档；Handoff 本身不能满足这两个条件。

## 有效性检查

以下任一情况出现时不得继续下一阶段，应先向用户报告：

- 缺少必填字段或完整确认成果；
- `account_id` 与 `content_id` 或当前账号不一致；
- `approval_status` 不是 `confirmed_by_user`；
- `to_stage` 与当前请求不一致；
- 来源无法定位且缺失会影响事实或结论；
- 多个 Handoff 对同一阶段给出互相冲突的确认结果，且用户未指定最新版本。
