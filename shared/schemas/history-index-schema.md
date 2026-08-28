# History Index Schema

每个账号的历史索引位于：

```text
accounts/<account_id>/内容库/01-历史内容/_history-index.jsonl
```

每行对应一篇正式历史 Markdown。字段：

| 字段 | 必需 | 说明 |
| --- | --- | --- |
| `path` | 是 | 相对仓库根目录的 Markdown 路径 |
| `title` | 是 | 标题；缺失时从文件名推导 |
| `publish_date` | 是 | 发布日期；缺失时从文件名推导 |
| `business_line` | 否 | 业务方向 |
| `theme` | 否 | 主题 |
| `content_type` | 否 | 内容类型 |
| `audience` | 否 | 目标受众 |
| `pain_scene` | 否 | 客户痛点或经营场景 |
| `content_goal` | 否 | 内容目标 |
| `status` | 是 | 正式历史统一写为 `published` |
| `series` | 否 | 系列 |
| `region` | 否 | 地域 |

索引只保存检索元数据，不保存正文。Markdown 永远是最终事实来源。

