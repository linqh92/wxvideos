---
name: publish-archive
description: 仅在内容已实际发布且用户明确要求归档时，将内容写入当前账号历史库，增量更新 History Index，并把对应候选改为已发布。
---

# 微信视频号发布归档

## Trigger

仅当以下两项同时成立时使用：

1. 用户明确确认内容已实际发布或更新完成；
2. 用户明确要求归档、写入知识库或保存到历史内容。

如果用户只说“已发布”，只准备可唯一识别的归档预览，不写文件。实际发布标题、正文或日期不能唯一确定时先询问；不得猜测或覆盖现有记录。

## Required Input

- 实际发布标题、正文和发布日期；
- 实际发布载体；
- 用户的实际发布确认与明确归档指令；
- 根 `AGENTS.md` 已唯一确定的 `CURRENT_ACCOUNT`。

## Required Context

账号选择、隔离、阶段边界和项目级写入权限服从根 `AGENTS.md`。状态含义与转换引用：

```text
shared/schemas/content-state-machine.md
```

归档前完整读取并严格遵循：

```text
accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/历史内容归档规范.md
```

该文件是当前账号历史路径、文件名、Frontmatter、正文结构和完成检查的事实来源。

## Unique Logic

归档前唯一确认实际发布内容的 `content_format`，只允许：

```text
text_broadcast
spoken
```

来源优先级为：用户明确确认的发布载体 > 本次生成阶段的 `CONTENT_FORMAT`。`recommended_format` 只是选题建议，不得直接代替实际发布载体。无法判断时先询问，不得根据篇幅、候选建议或旧内容形式猜测。

1. 检查目标目录中的同名和疑似重复笔记；存在冲突时停止并报告。
2. 只写实际使用的标题、正文、实际发布日期和实际 `content_format`，不保存备选标题、草稿过程或未发布信息。
3. 历史 Markdown 写入成功后，以 `path` 为键 append/update `01-历史内容/_history-index.jsonl` 的单条记录，不全库扫描。
4. 找到对应候选时，将候选 Markdown 和 `_candidate-index.jsonl` 同步更新为公共状态机中的发布终态。只有本 Skill 可以执行此转换。
5. 不自动重建内容地图、内容缺口、重复检查、月度复盘或统计。用户明确要求时才运行 `shared/scripts/rebuild-derived-assets.ps1`。

### 灵感回流

保留原有内容资产回流机制：从已发布内容提取 1～2 个不重复的后续问题，每个问题建立一篇 `历史延展` 灵感；真实评论、咨询或交付反馈存在时可分别建立灵感并关联历史内容。

新灵感使用公共状态机的初始状态，并以单条 append/update 方式同步 `_idea-index.jsonl`。

## Output

写入一篇符合当前账号归档规范的正式历史 Markdown，增量更新对应 History Index；存在对应候选时同步更新候选 Markdown 与 Candidate Index，并按既有回流机制新增 1～2 条不重复后续灵感。

## Stop

完成允许的归档、索引同步、候选终态更新和灵感回流后立即停止。不得自动生成下一批选题或文案，也不得自动重建内容地图、缺口分析、重复检查、月度复盘或其他派生资产。
