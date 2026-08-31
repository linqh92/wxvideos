---
name: spoken-visual-planning
description: Plan explanatory supporting visuals and AI image-generation prompts for a finalized WeChat Video Account spoken script or final voiceover. Use only after spoken copy is confirmed and the user explicitly requests 配图、示意图、视觉分镜、AI生图提示词, or a similar post-copy visual task. The Skill must combine shared comprehension rules with the CURRENT_ACCOUNT visual-style file. Do not rewrite the spoken script, re-plan the topic, archive content, or automatically generate images.
---

# WeChat Video Account Spoken Visual Planning（微信视频号口播示意图规划）

## Trigger

Use this Skill only when BOTH conditions are satisfied:

1. A finalized or user-confirmed spoken script already exists, or the user provides a final voiceover/audio file.
2. The user explicitly requests a spoken-video visual-support task such as:
   - 配图
   - 示意图
   - 中间画面
   - 视觉分镜
   - AI 生图提示词
   - 根据口播规划图片
   - 根据音频规划配图
   - 口播辅助视觉

Do NOT automatically invoke this Skill after `spoken-copywriting`.

## Required Input

- A finalized or user-confirmed spoken script, or a final voiceover/audio file;
- The user's requested visual-plan or prompt deliverable;
- `CURRENT_ACCOUNT` resolved under root `AGENTS.md`.

## Required Context

Account selection, isolation, and stage boundaries follow root `AGENTS.md`; this Skill does not redefine them.

Before planning visuals, read and obey in this order:

```text
1. .codex/skills/spoken-visual-planning/references/visual-aid-generation-rules.md
2. accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号视觉风格.md
3. Finalized spoken script and/or final voiceover provided in the current task
```

The shared reference defines **how visuals improve understanding**.

The account visual-style file defines **how this account should look**.

The finalized spoken content defines **what this specific piece needs to explain**.

### Do NOT automatically read

```text
accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号人设与文风.md
accounts/{CURRENT_ACCOUNT}/内容库/01-历史内容/**
accounts/{CURRENT_ACCOUNT}/内容库/02-内容地图/**
accounts/{CURRENT_ACCOUNT}/内容库/03-选题规划/**
accounts/{CURRENT_ACCOUNT}/内容库/04-内容复盘/**
accounts/{CURRENT_ACCOUNT}/内容库/05-内容素材库/**
_history-index.jsonl
_idea-index.jsonl
_candidate-index.jsonl
```

This Skill is content-first and visual-system-aware, not persona-first.

---

## Unique Logic

### Missing Visual Style File（视觉风格文件缺失）

If:

```text
accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号视觉风格.md
```

is missing or unreadable:

1. Do NOT borrow another account's visual style.
2. Do NOT silently fall back to a fixed blue-gray business style.
3. Use only the shared comprehension rules plus the current content's semantic needs.
4. Report the missing path before producing a final account-branded prompt package.
5. If the user explicitly allows a temporary neutral style, use a content-adaptive neutral baseline only for the current task.

A temporary neutral baseline MUST NOT be treated as the account's permanent style.

---

### Planning and Prompt Assembly（规划与提示词合成）

Follow `references/visual-aid-generation-rules.md` for semantic segmentation, visual-switch necessity, viewer-understanding targets, visual-type routing, image-count control, information density, human-presence limits, prompt construction, three-layer negative prompts, and universal quality checks.

Treat the current account's `账号视觉风格.md` as its Account Visual DNA; it controls account-specific rendering, color, graphic language, composition, human presence, and avoid rules.

For every final prompt, combine exactly these sources without changing their authority:

```text
Current spoken semantics
+ best explanatory form from the reference
+ CURRENT_ACCOUNT visual DNA
+ shared quality and scene constraints
= final image-generation prompt
```

Choose semantics and explanatory form before applying account style. Account style must not alter facts or reduce comprehension. Do not copy a global style string or silently default all accounts to the same business look.

---

## Output

Unless the user requests a different structure, output only:

### A. 口播语义分段表

```markdown
| 图序 | 对应口播范围 | 核心信息 | 观看者理解目标 | 推荐视觉形式 | 建议图片数量 |
|---|---|---|---|---|---|
```

### B. 当前账号视觉基准

```markdown
## 当前账号视觉基准
- Rendering:
- Color:
- Graphic language:
- Composition:
- Human presence:
- Account-specific avoid:
```

### C. Final Prompt Blocks

```markdown
## 图X｜[核心主题]

### 对应口播
[对应口播范围]

### 观看者理解目标
[看完应立即理解什么]

### 推荐视觉形式
[relationship / process / comparison / risk_highlight / reconciliation / object_focus / real_scene_support]

### 正向提示词
[完整中文通用AI生图提示词：语义 + 解释结构 + 当前账号视觉DNA]

### 反向提示词
[公共质量反向词 + 当前账号风格反向词 + 当前图专属反向约束]
```

Do NOT add editing suggestions, transition suggestions, BGM suggestions, confirmation checklists, internal scoring, or archive instructions.

---

## Quality Gate

Before output, verify:

### Comprehension
- Each image has one clear understanding target.
- The image helps explain something that audio alone may be slower to process.
- The image is not merely decorative.

### Account differentiation
- The final prompts actually reflect CURRENT_ACCOUNT Visual DNA.
- The result is not silently falling back to a universal business style.
- Account style does not override comprehension.

### Prompt quality
- Core objects are explicit.
- Relationships / process / abnormal point are explicit.
- Visual form is explicit.
- Account visual DNA is explicitly applied.
- Negative prompt includes universal + account + scene layers.

If any item fails, revise before output.

---

## Stop

This Skill ends when the requested visual plan and image prompts are delivered.

Do not automatically:
- rewrite or optimize the spoken script;
- re-plan the topic or produce text-broadcast copy;
- change confirmed facts or conclusions;
- call image generation;
- create files in the account vault;
- archive the content;
- move candidate states;
- start editing instructions;
- start a new content-production stage.
