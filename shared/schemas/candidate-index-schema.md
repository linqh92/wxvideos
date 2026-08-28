# Candidate Index Schema

每个账号的候选索引位于：

```text
accounts/<account_id>/内容库/03-选题规划/_candidate-index.jsonl
```

候选卡可以保存在 `待发布选题.md` 或业务选题池中。每行对应一张含明确状态的候选卡。

| 字段 | 必需 | 说明 |
| --- | --- | --- |
| `path` | 是 | 相对仓库根目录的来源文件路径和标题锚点 |
| `title` | 是 | 候选标题 |
| `status` | 是 | 取值引用 `content-state-machine.md` |
| `business_line` | 否 | 业务方向 |
| `theme` | 否 | 主题 |
| `audience` | 否 | 目标客户 |
| `pain_scene` | 否 | 经营场景与核心痛点 |
| `content_goal` | 否 | 内容目的 |
| `service` | 否 | 可承接服务 |
| `created` | 否 | 来源文件创建日期 |

模板、无状态清单和未补全的占位条目不得写入索引。

