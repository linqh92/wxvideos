# Content Identity Schema

本文件定义内容从“选题已采用”开始跨阶段复用的稳定身份。`content_id` 是关联键，不是内容状态，也不代替候选、推荐、发布或归档状态。

## 创建时点

- 用户明确采用某个选题时创建；仅推荐、浏览、跳过或待确认时不创建。
- 用户直接提供题目并进入文案阶段时，最迟在该文案首次被用户明确确认为最终版本时创建。
- 已有有效 `content_id` 时必须复用，不得因新对话、新阶段、修改标题或重新生成 Handoff、Repo 内容文档、视觉规划输入而更换。
- 旧内容不自动回填；只有明确迁移或维护任务才批量补建。

## 格式

```text
wxv-{account_id}-{YYYYMMDD}-{8hex}
```

示例：

```text
wxv-gzminge-20260909-a1b2c3d4
```

约束：

- `account_id` 必须等于根 `AGENTS.md` 中已经锁定的 `CURRENT_ACCOUNT`；
- 日期使用首次创建该 ID 的本地日期；
- `8hex` 使用 8 位小写十六进制随机值；
- 完整值匹配 `^wxv-(gzminge|gzxzcs|qycslc|gzcktxpp|tsxbj|gzlxcs)-\d{8}-[0-9a-f]{8}$`；
- 同一 Repo 内不得存在两个不同内容共用同一 `content_id`。

具有脚本执行能力的环境优先使用 `shared/scripts/content-handoff.py new-id --account <account_id>` 生成，避免手工格式错误；只读 Chat 环境可以按同一格式创建，并通过选题 Handoff、Repo 内容文档或视觉规划输入继续传递。

## 生命周期

```text
已采用选题
→ 已确认文案
→ 可选视觉规划
→ 实际发布
→ 发布归档与后续复盘
```

上述各阶段始终引用同一 `content_id`。内容载体改变、文案修订、视觉方案形成或发布标题调整都不生成新 ID；只有用户明确将其拆成另一条独立内容时才创建新 ID。

## 关联字段

- `account_id`：必填，必须与 ID 中账号一致；
- `topic_id`：已有正式候选或可追溯题目 ID 时填写；直接题目可为 `null`；
- `content_format`：进入文案阶段后使用 `text_broadcast` 或 `spoken`；
- `source_refs`：只记录实际使用且可重新定位的 Repo 路径或外部来源；
- `content_id` 不得承载确认状态、同步状态或发布状态。

## 冲突处理

发现同一内容存在多个 ID，或同一 ID 指向不同账号、不同独立内容时，停止写入并报告冲突。未经用户确认，不合并、不覆盖、不猜测保留哪一个。
