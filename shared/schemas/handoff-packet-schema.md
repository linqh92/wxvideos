# Handoff Packet Schema

Handoff Packet 只用于在 ChatGPT 项目中把用户已采用的选题传递到独立的短文或口播对话。它是临时交接文件，不是 Repo 资产、事实源、状态记录、索引或发布归档。

## 使用边界

- 仅在用户明确采用选题并要求进入短文或口播阶段后生成。
- 一份 Handoff 只交接一条独立内容：一个 `topic_id`、一个 `content_id` 和一个 `to_stage`。同一轮采用多个独立选题时必须逐题生成，不得合并到一份 Handoff 或一个下游文案对话。
- 文案确认、Repo 执行、视觉规划、发布归档和视觉阶段结束均不使用 Handoff；文案确认后的交付按 `shared/schemas/confirmed-copy-delivery-schema.md` 执行。
- Handoff 保留在 ChatGPT 项目中，由用户在新对话通过 `@` 明确引用；不得写入仓库。
- 新对话以最新明确引用且校验有效的 Handoff 作为唯一上一阶段工作成果，不重新加载上一阶段 Skill、检索历史、未采用方案或聊天记忆。
- Handoff 只传身份、确认结果、改变结论的条件、必要来源、用户原始反馈和权限，不复制 AGENTS、Skill、完整历史或无关上下文。

## 文件名

```text
选题交接｜{account_id}｜{topic_short_name}｜{YYYYMMDD-HHmmss}.md
```

- `选题交接` 是固定前缀，用户可先输入 `@选题交接` 缩小范围，再按账号或题目短名选择；
- `topic_short_name` 从已采用题目中提取 4～20 个汉字、字母、数字或连字符，只保留能识别主题的核心词，不使用“选题1”“新选题”等泛称；
- 同一轮生成多份 Handoff 时，`topic_short_name` 必须能彼此区分；核心词相同时加入客户、动作或关键条件，避免同一确认时间产生重名文件；
- 文件名时间必须由 `confirmed_at` 转为 `YYYYMMDD-HHmmss`，用于区分同一内容的重新确认版本并按名称识别新旧；
- 完整 `content_id` 保留在 Frontmatter，不再占用文件名的主要搜索位置。

同一阶段重新确认后生成新文件时保留同一 `content_id`，更新 `confirmed_at` 并生成带新时间的文件名。新对话只使用用户明确引用的最新文件。旧版 `Handoff｜{content_id}｜{from_stage}-to-{to_stage}.md` 可继续读取和校验，但新生成文件必须使用上述易搜索命名。

## 必填 Frontmatter

```yaml
---
handoff_version: "1.1"
content_id: "wxv-{account_id}-{YYYYMMDD}-{8hex}"
account_id: "{CURRENT_ACCOUNT}"
topic_short_name: "4～20 个可搜索字符"
from_stage: "topic_planning"
to_stage: "text_broadcast_copywriting | spoken_copywriting"
approval_status: "confirmed_by_user"
confirmed_at: "YYYY-MM-DDTHH:MM:SS+08:00"
repo_sync_status: "not_synced | synced"
content_format: "text_broadcast | spoken"
topic_id: "string | null"
topic_origin: "project_recommendation"
recommendation_batch_id: "uuid"
topic_feedback_status: "synced | pending"
feedback_event_id: "uuid"
---
```

约束：

- `content_id` 按 `content-identity-schema.md` 创建并复用；
- `account_id` 必须与当前账号及 `content_id` 一致；
- `topic_short_name` 必须与已采用选题一致，并符合文件名字符与长度规则；
- `from_stage` 必须是刚完成并已确认的 `topic_planning`；
- `to_stage` 必须是用户明确要求的 `text_broadcast_copywriting` 或 `spoken_copywriting`；
- `approval_status` 只有在用户明确确认后才能写为 `confirmed_by_user`；
- `repo_sync_status` 只描述当前已采用选题及允许记录是否已进入 Repo；
- `content_format` 必须与 `to_stage` 一致：进入短文使用 `text_broadcast`，进入口播使用 `spoken`。
- `recommendation_batch_id`、`topic_id` 和 `feedback_event_id` 必须定位本次推荐批次、被选题目与本次 `selected` 反馈；重试时复用，不得重新生成；
- 多选拆分时，各 Handoff 可以共享 `recommendation_batch_id`，但 `topic_id`、`content_id` 和 `feedback_event_id` 必须分别唯一；一条 selected feedback 只能对应当前 Handoff 的一个 `topic_id`；
- `topic_feedback_status` 表示 recommendation 与 selected feedback 是否均已写入 Repo；任一尚未写入时使用 `pending`。

## 正文结构

```markdown
# 选题交接｜{topic_short_name}

## 用户确认原话

> 保留触发确认或阶段转换的用户原话。

## 已确认成果

完整放入下一阶段实际需要的确认内容，不依赖上一对话才能理解。

## 选题来源与反馈

- recommendation_batch_id: <uuid>
- topic_id: <被选择题目的 ID>
- feedback_event_id: <本次 selected 反馈事件 ID>
- feedback_signal: selected
- feedback_scope: topic
- user_text: <用户选择原话>
- scope_description: <被选择的具体题目>
- occurred_at: <带时区的 ISO 时间>
- topic_feedback_status: synced | pending

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

`pending_repo_actions` 只记录当前环境因只读而未执行、且项目规则本来允许持久化的动作。若推荐批次或 selected feedback 尚未写入，必须按 `shared/schemas/topic-recommendation-log-schema.md` 携带稳定 `action_id`、明确目标路径和完整事件 payload；原 recommendation 事件未入库时与 feedback 事件一起携带，不能只留下摘要或一个无法解析的批次引用。它不是执行授权；文案阶段必须原样继承到 Repo 内容文档，后续具有写入能力的 Codex 仍须按当前 Skill、账号锁、事件 ID 和写入规则重新校验。

同一轮多选且 recommendation 尚未入库时，每份 Handoff 可以携带相同的 recommendation action 和稳定事件 ID，保证任一内容都能独立进入 Codex；每份 Handoff 只能再携带本选题自己的 selected feedback action。后续执行依靠事件 ID 幂等去重，不把共享推荐事件重新编号。

ChatGPT“对话”模式通过 GitHub 集成读取仓库时，不得为生成 Handoff 先尝试写入。该环境直接使用 `repo_sync_status: not_synced`、`topic_feedback_status: pending` 和完整 `pending_repo_actions`；这属于正常交接路径，不输出 `403` 或“写入失败”提示。

## 阶段最小交接内容

### 选题 → 文案

必须包含已采用选题、目标客户与场景、客户决策问题、核心答案、改变结论的条件、建议或用户指定载体、必要来源，以及本次选择反馈的批次 ID、题目 ID、事件 ID、原话、范围和同步状态。不带入其余候选与整批查重过程；只有尚未落库的完整 recommendation 事件可以作为不参与创作的待执行 payload 携带其余实际推荐项。

多选时分别生成的每份 Handoff 仍只把当前被采用题目放入“已确认成果”和创作上下文；共享 recommendation payload 中出现的其余推荐项只用于 Repo 补写，不得被文案阶段当作第二个选题。

## 有效性检查

以下任一情况出现时不得继续下一阶段，应先向用户报告：

- 缺少必填字段或完整确认成果；
- `account_id` 与 `content_id` 或当前账号不一致；
- `approval_status` 不是 `confirmed_by_user`；
- `to_stage` 与当前请求不一致；
- 来源无法定位且缺失会影响事实或结论；
- 多个 Handoff 对同一阶段给出互相冲突的确认结果，且用户未指定最新版本。
