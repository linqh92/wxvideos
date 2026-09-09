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
| `content_id` | 否 | 候选对应内容完成发布归档后填写；格式引用 `content-identity-schema.md` |
| `business_line` | 否 | 业务方向 |
| `theme` | 否 | 主题 |
| `audience` | 否 | 目标客户 |
| `pain_scene` | 否 | 经营场景与核心痛点 |
| `content_goal` | 否 | 内容目的 |
| `service` | 否 | 可承接服务 |
| `recommended_format` | 否 | 推荐内容载体：`text_broadcast`、`spoken` 或 `either` |
| `created` | 否 | 来源文件创建日期 |

模板、无状态清单和未补全的占位条目不得写入索引。

候选池是个人跨账号维护时的备查资源，用于保存待核验、可推荐、已发布和已放弃的方向；状态不决定推荐顺序或再次推荐资格。推荐批次和用户反馈独立保存在 `topic-recommendation-log-schema.md` 定义的事实记录中，不加入本索引；重建本索引不得删除或重建推荐记录。新候选正文保留需求依据、客户决策问题、核心答案及关键条件；这些正文信息不强制进入索引，旧卡不猜测补填。

`recommended_format` 只是选题阶段的推荐载体，不代表实际生成或发布载体。候选 Markdown 使用中文值“短文字幕”“口播”“均可”，JSONL 使用稳定枚举。旧候选允许缺失该字段，不得批量回填或猜测。

候选为 `待核验` 或 `可推荐` 时通常没有 `content_id`。对应内容发布归档后，候选 Markdown 使用字段 `内容ID`，Index 使用 `content_id`，状态使用 `已发布`；直接给题或参考重写且没有对应候选时不创建候选卡。
