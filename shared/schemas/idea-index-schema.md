# Idea Index Schema

每个账号的灵感索引位于：

```text
accounts/<account_id>/内容库/03-选题规划/灵感库/_idea-index.jsonl
```

| 字段 | 必需 | 说明 |
| --- | --- | --- |
| `path` | 是 | 相对仓库根目录的灵感 Markdown 路径 |
| `title` | 是 | 灵感标题 |
| `created` | 否 | 创建日期 |
| `status` | 是 | 取值引用 `content-state-machine.md` |
| `business_line` | 否 | 分析后才可能存在 |
| `audience` | 否 | 分析后才可能存在 |
| `pain_scene` | 否 | 分析后才可能存在 |
| `source` | 否 | 用户明确提供或正文已有的来源类型 |

Index 不补写 Markdown 中不存在的业务事实。

