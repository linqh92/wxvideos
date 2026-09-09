# Repo Operation Schema

本文件定义结构化 `Repo内容文档` 在可写本地工作树中的确定性执行接口。脚本只处理文件中已经确认的数据，不判断文案含义，不生成新内容。

## 操作载荷

`Repo内容文档` 使用 `delivery_version: "1.1"`，并包含一个 `## Repo 操作载荷` 章节。该章节只能放置一个 JSON 对象：

```json
{
  "schema_version": "1.0",
  "action": "archive_published_content",
  "account_id": "gzminge",
  "content_id": "wxv-gzminge-20260909-a1b2c3d4",
  "content_format": "text_broadcast",
  "publish_date": "2026-09-09",
  "final_title": "唯一最终标题",
  "archive_metadata": {
    "business_line": "固定选项或账号允许值",
    "theme": "固定选项或账号允许值",
    "content_type": "固定选项或账号允许值",
    "audience": "固定选项或账号允许值",
    "pain_scene": "一个主要客户场景",
    "content_goal": "知识库可追踪目标",
    "region": "广州",
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

`account_id`、`content_id`、`content_format`、`publish_date` 和 `final_title` 必须与 Frontmatter 完全一致。`pending_repo_actions` 沿用 `confirmed-copy-delivery-schema.md` 定义的完整事件结构。

`extension_topics` 与 `related_content` 只接收已经明确提供且可直接保存的值。常规文案确认时使用空数组；脚本分别写入“待根据发布后咨询问题补充”和“暂无直接关联内容”。语义延展、关联判断与灵感回流属于单独的按需或批量任务。

## 命令

统一入口：

```text
shared/scripts/wxv-ops.py
```

只读检查：

```text
python shared/scripts/wxv-ops.py check --input "<Repo内容文档路径>"
```

执行发布归档：

```text
python shared/scripts/wxv-ops.py sync-published --input "<Repo内容文档路径>" --apply
```

执行后核验：

```text
python shared/scripts/wxv-ops.py verify --input "<Repo内容文档路径>"
```

`--apply` 是写入授权开关。用户只要求查看、检查或引用文件时只能运行 `check`。

## 固定执行范围

`sync-published` 按以下数据边界执行：

- 校验 Repo 文档版本、账号、内容身份、标题、载体、日期和操作载荷；
- 按事件 ID 幂等补写 `pending_repo_actions` 中的推荐与 `selected` 反馈；
- 写入正式历史 Markdown，并按 `path` 增量维护 History Index；
- 能唯一定位现有候选时，将候选 Markdown 与 Candidate Index 更新为 `已发布` 并写入同一 `content_id`；
- 同步本账号推荐检索缓存；
- 使用空延展与空关联数组时写入规范允许的占位文本；
- 不创建候选卡、不生成灵感、不重建内容地图或复盘资产、不执行 Git 提交或推送。

## 结果状态

脚本始终输出 JSON：

- `ready`：检查通过，可以执行；
- `completed`：本次写入完成并通过核验；
- `already_synced`：对应事实已经完整存在，未重复写入；
- `verified`：执行结果完整；
- `invalid_document`：文件格式或必填字段不符合接口；
- `authorization_required`：缺少 `--apply`；
- `conflict`：账号、ID、事件、历史或候选存在冲突；
- `partial_failure`：部分文件已经写入，但缓存或最终核验未完成。

`invalid_document`、`conflict` 和 `partial_failure` 需要根据脚本返回的具体错误处理。未经用户确认不得猜测缺失数据、覆盖冲突文件或更换 `content_id`。

