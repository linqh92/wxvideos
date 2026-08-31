---
name: idea-intake
description: 将用户提供的文字、图片文字、同行内容或反馈，按当前账号既有格式独立录入灵感库，并增量更新 Idea Index。仅在用户要求保存或录入灵感时使用。
---

# 灵感录入

## Trigger

用户明确要求保存或录入原始灵感、竞品内容、用户想法、图片文字或客户反馈时使用。

本 Skill 只做采集，不做选题分析、候选入池、文案生成、官方核验、历史扫描或归档。

## Required Input

- 用户提供的原始文字、图片文字或明确备注；
- 根 `AGENTS.md` 已唯一确定的 `CURRENT_ACCOUNT`。

用户文字原样写入，不改写或总结。用户提供图片时只提取可读文字，不保存、嵌入、链接或归档图片本身；无法完整识别时，只记录可读部分并标记“文字识别不完整”，不得猜测补写。用户同时提供文字和图片时，分别保存用户原文和图片文字提取；数据表现、链接或备注仅在用户材料中出现时记录。

## Required Context

账号选择、隔离和写入边界统一服从根 `AGENTS.md`。本 Skill 只读写：

```text
accounts/{CURRENT_ACCOUNT}/内容库/03-选题规划/灵感库/**
```

状态和索引字段分别引用：

```text
shared/schemas/content-state-machine.md
shared/schemas/idea-index-schema.md
```

## Unique Logic

1. 每条灵感建立一篇独立笔记，保存至 `accounts/{CURRENT_ACCOUNT}/内容库/03-选题规划/灵感库/YYYY/YYYY-MM/`。
2. 文件名使用 `YYYY-MM-DD｜简短名称.md`；名称描述可识别场景，不直接照搬竞品标题。无法判断时使用“待分析灵感”加序号。
3. Frontmatter 记录 `title`、`aliases`、`tags`、`source_type`、`status`、`created`、`updated`；初始状态使用公共状态机定义。
4. 只保存本次提供的原文、图片文字提取结果和明确备注；不得补充目标客户、主题、业务线、服务关联、结论或选题建议。
5. `选题灵感收集.md` 只作索引和模板说明，不保存多条灵感正文。
6. 笔记成功写入后，以 `path` 为键 append/update `灵感库/_idea-index.jsonl` 的单条记录；Index 只抄录 Markdown 已有元数据，不得成为唯一事实源。

## Output

按当前账号现有格式写入一篇灵感笔记，并增量同步 Idea Index。笔记模板：

~~~markdown
---
title: "灵感｜简短名称"
aliases: []
tags:
  - "视频号/灵感"
source_type: "用户录入"
status: "待分析"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
---

# 灵感｜简短名称

## 原始材料

### 用户文字

### 图片文字提取

### 数据表现或备注

## 处理备注

- 材料形式：文字 / 图片文字提取 / 图文混合
- 文字识别：完整 / 不完整 / 不适用
~~~

## Stop

完成一条独立灵感笔记及对应索引更新后立即停止。不得自动改变灵感状态；只有用户后续明确要求选题或分析灵感时，才可进入 `topic-planning`。
