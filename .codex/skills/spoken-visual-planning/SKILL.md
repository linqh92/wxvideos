---
name: spoken-visual-planning
description: Plan explanatory supporting visuals and AI image-generation prompts for a finalized WeChat Video Account spoken script or final voiceover. Use only after spoken copy is confirmed and the user explicitly requests 配图、示意图、视觉分镜、AI生图提示词, or a similar post-copy visual task. The Skill must combine shared comprehension rules with the CURRENT_ACCOUNT visual-style file. Do not rewrite the spoken script, re-plan the topic, archive content, or automatically generate images.
---

# WeChat Video Account Spoken Visual Planning（微信视频号口播示意图规划）

## 1. Scope（职责范围）

This Skill converts a finalized spoken script and/or final voiceover audio into a compact set of explanatory supporting visuals for the middle visual area of a spoken WeChat Channels video.

It MAY output:
- Spoken semantic segmentation
- Recommended image count
- Viewer-understanding target for each segment
- Recommended explanatory visual form
- Account-specific visual-style adaptation
- Final Chinese AI image-generation prompts
- Positive and negative prompts

It MUST NOT:
- rewrite or optimize the spoken script;
- re-plan the topic;
- change confirmed facts or conclusions;
- produce text-broadcast copy;
- produce editing plans, transition instructions, BGM notes, or camera directing notes;
- automatically generate images unless the user explicitly asks for actual image generation in a separate step;
- mark content as published;
- archive or update history;
- change candidate or idea states;
- update content maps or indexes.

After delivering the requested visual-planning materials, STOP.

---

## 2. Trigger Conditions（触发条件）

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

---

## 3. Account Lock（账号隔离）

Determine `CURRENT_ACCOUNT` according to repository-root `AGENTS.md`.

Use `CURRENT_ACCOUNT` to:
- prevent cross-account context leakage;
- load the correct account-level visual style;
- keep visual identity separate between accounts.

Do NOT read other accounts.

---

## 4. Required Context（必读上下文）

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

## 5. Missing Visual Style File（视觉风格文件缺失）

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

## 6. Core Medium Objective（媒介目标）

Optimization priority:

> Information accuracy（信息准确）  
> → Comprehension acceleration（加快理解）  
> → Semantic correspondence（与当前口播贴合）  
> → Best explanatory visual form（选择最适合的解释形式）  
> → Account visual identity（账号视觉辨识度）  
> → Stable viewing rhythm（减少无意义切图）  
> → Decorative aesthetics（装饰性美观）

The default question for every segment is:

> **观众只靠“听”可能卡在哪里？这张图怎样让他“看一眼就懂”？**

Visual style MUST NOT override comprehension.

---

## 7. Three-Layer Visual Assembly（三层视觉合成逻辑）

Every final prompt must be assembled from three layers:

### Layer A — Shared Comprehension Logic（公共理解机制）

Defined by:

```text
visual-aid-generation-rules.md
```

Controls:
- semantic segmentation;
- image-count control;
- viewer-understanding targets;
- explanatory visual types;
- information density;
- person-use restrictions;
- quality and safety constraints.

### Layer B — Account Visual DNA（账号视觉DNA）

Defined by:

```text
accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号视觉风格.md
```

Controls:
- color system;
- rendering language;
- graphic language;
- composition tendency;
- material / texture language;
- typography / label tendency;
- human-presence preference;
- preferred visual forms;
- account-specific avoid rules.

### Layer C — Current Content Adaptation（当前内容适配）

Determined from the current spoken segment.

Controls:
- which business objects appear;
- which relationship or process is shown;
- which abnormality is highlighted;
- whether realism or abstraction is more effective for this segment;
- how much of the account style can be applied without reducing clarity.

Final prompt logic:

```text
Current semantic meaning
+
Best explanatory form
+
CURRENT_ACCOUNT Visual DNA
+
Shared quality constraints
=
Final image-generation prompt
```

---

## 8. Visual-Type Routing（示意图类型路由）

For each semantic segment, select ONE primary visual form:

- `relationship` — 关系示意
- `process` — 流程示意
- `comparison` — 对比示意
- `risk_highlight` — 风险点高亮
- `reconciliation` — 梳理 / 对账 / 闭环示意
- `object_focus` — 单一业务对象聚焦
- `real_scene_support` — 真实场景辅助，仅当它确实提高理解时

Choose the visual form from semantic need first.

Then apply the account Visual DNA.

---

## 9. Image Count Rule（图片数量）

Do not use a fixed image count.

Default guidance:
- One stable image normally supports approximately 6–10 seconds of spoken content.
- A 30–60 second spoken video often needs approximately 4–6 images.
- Use fewer images if several consecutive lines explain the same idea.
- Use more only when the semantic subject or logic genuinely changes.

The final count should be the smallest set that keeps semantic correspondence clear.

---

## 10. Prompt Generation Rules（提示词生成规则）

Each final prompt must include four effective layers:

1. **Semantic content**
2. **Explanatory visual structure**
3. **Account visual DNA**
4. **Quality / negative constraints**

Do not copy a fixed global style string into every prompt.

Do not automatically use:
- blue-gray-white;
- red warning accents;
- realistic business photography;
- light neutral background;
- finance / compliance look;

unless the CURRENT_ACCOUNT visual-style file explicitly defines them for that account or the current content independently requires them.

---

## 11. Negative Prompt Layering（反向提示词分层）

Final negative prompts must be composed from:

### A. Universal Quality Negatives（公共质量反向词）

Always apply:
- low resolution;
- blur;
- broken perspective;
- malformed anatomy when people appear;
- unreadable dense text;
- clutter;
- meaningless decorative elements;
- fake official interfaces;
- watermarks;
- wrong logos;
- unclear information hierarchy;
- generic two-person business dialogue when it does not improve understanding.

### B. Account-Specific Style Negatives（账号风格反向词）

Read from:

```text
账号视觉风格.md
```

These MUST NOT be hard-coded globally.

### C. Scene-Specific Negatives（当前场景专属反向词）

Generate from the current visual form and semantic risk.

---

## 12. Output Format（输出格式）

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

## 13. Final Quality Gate（最终质检）

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

## 14. Completion Boundary（完成边界）

This Skill ends when the requested visual plan and image prompts are delivered.

Do not automatically:
- call image generation;
- create files in the account vault;
- archive the content;
- move candidate states;
- start editing instructions;
- start a new content-production stage.
