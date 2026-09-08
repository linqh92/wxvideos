# Handoff Packet Schema

Handoff Packet 只用于在 ChatGPT 项目中把用户已采用的选题传递到独立的短文或口播对话。它是临时交接文件，不是 Repo 资产、事实源、状态记录、索引或发布归档。

## 使用边界

- 仅在用户明确采用选题并要求进入短文或口播阶段后生成。
- 文案确认、Repo 执行、视觉规划、发布归档和视觉阶段结束均不使用 Handoff；文案确认后的交付按 `shared/schemas/confirmed-copy-delivery-schema.md` 执行。
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
from_stage: "topic_planning"
to_stage: "text_broadcast_copywriting | spoken_copywriting"
approval_status: "confirmed_by_user"
confirmed_at: "YYYY-MM-DDTHH:MM:SS+08:00"
repo_sync_status: "not_synced | synced"
content_format: "text_broadcast | spoken"
topic_id: "string | null"
---
```

约束：

- `content_id` 按 `content-identity-schema.md` 创建并复用；
- `account_id` 必须与当前账号及 `content_id` 一致；
- `from_stage` 必须是刚完成并已确认的 `topic_planning`；
- `to_stage` 必须是用户明确要求的 `text_broadcast_copywriting` 或 `spoken_copywriting`；
- `approval_status` 只有在用户明确确认后才能写为 `confirmed_by_user`；
- `repo_sync_status` 只描述当前已采用选题及允许记录是否已进入 Repo；
- `content_format` 必须与 `to_stage` 一致：进入短文使用 `text_broadcast`，进入口播使用 `spoken`。

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

## 有效性检查

以下任一情况出现时不得继续下一阶段，应先向用户报告：

- 缺少必填字段或完整确认成果；
- `account_id` 与 `content_id` 或当前账号不一致；
- `approval_status` 不是 `confirmed_by_user`；
- `to_stage` 与当前请求不一致；
- 来源无法定位且缺失会影响事实或结论；
- 多个 Handoff 对同一阶段给出互相冲突的确认结果，且用户未指定最新版本。
