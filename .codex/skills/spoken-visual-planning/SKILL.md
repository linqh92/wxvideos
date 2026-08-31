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
- `CURRENT_ACCOUNT` resolved under root `AGENTS.md`;
- Confirmed visual base specifications required by the planning gate below.

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

### Visual Planning Declaration and Base-Spec Gate（视觉规划声明与基础规格确认）

After the spoken content is confirmed and the user requests visual planning:

1. State that the task is entering the visual-planning stage.
2. State that this stage will not rewrite the spoken content, generate images, archive content, or change publication state.
3. Extract visual specifications already provided by the user, the current task, or an authoritative current-account rule.
4. Ask once for all missing planning-critical specifications, then stop and wait for the user's answer.
5. Start formal visual planning only after the planning-critical specifications are confirmed.

Planning-critical specifications:

- **Canvas aspect ratio:** for example `9:16`, `16:9`, `1:1`, or a custom ratio. Never infer a ratio merely from the platform name or content format.
- **Display mode and safe area:** full-screen visual, side visual, picture-in-picture, or another placement; include any area that must remain clear for the speaker, subtitles, title, or account information.
- **Text-in-image strategy:** no generated text, short labels allowed, or reserved blank areas for text added during editing.

Ask about these only when they materially affect the deliverable:

- exact pixel dimensions or resolution;
- fixed image count, timing, or switching cadence;
- target image-generation tool;
- required reference images, products, people, logos, or brand assets;
- cross-image continuity requirements;
- subject-fidelity or realism requirements.

Do not ask again for information already confirmed. Keep the missing-information request concise and grouped into one message rather than spreading it across several turns.

If the user explicitly asks to proceed before the aspect ratio or other planning-critical specifications are known, offer only ratio-neutral semantic segmentation. Do not produce the final image-generation execution guide until the missing specifications are confirmed.

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

Apply the confirmed visual base specifications to every image prompt and to the editing segmentation table. Do not add an unconfirmed aspect ratio, resolution, safe area, text strategy, or tool-specific syntax.

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

Unless the user requests a different deliverable format, create exactly two standalone downloadable Markdown documents:

1. `AI生图执行指南.md` — a complete execution document that can be passed directly to an image-generation tool or operator.
2. `剪辑分段表.md` — a brief segment table for the user to reference during editing.

Provide both documents for download in the final response. Do not require the user to choose, manage, or see a delivery directory. Do not repeat either document's body in the chat response; include only the two document links or attachments and a concise completion note.

The segmentation document must remain brief. It may map spoken ranges or actual audio timestamps to image sequence and viewer-understanding targets, but it must not expand into editing direction. Do NOT add transition, BGM, effect, performance, or archive suggestions unless the user explicitly requests them.

If a final audio file is available, use its real timing. If only finalized spoken text is available, segment by spoken range and do not fabricate timestamps.

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

### Base-spec adherence
- Every prompt uses the confirmed aspect ratio, display mode, safe area, and text strategy.
- No unconfirmed ratio, resolution, tool syntax, or asset requirement is invented.

### Deliverable usability
- `AI生图执行指南.md` is executable without reconstructing missing prompt context from the chat.
- `剪辑分段表.md` is concise and usable during editing.
- The final response provides both documents for download without repeating their contents inline.

If any item fails, revise before output.

---

## Stop

This Skill ends when the two requested downloadable documents are delivered.

Do not automatically:
- rewrite or optimize the spoken script;
- re-plan the topic or produce text-broadcast copy;
- change confirmed facts or conclusions;
- call image generation;
- persist delivery documents in the account vault unless the user explicitly requests that location;
- archive the content;
- move candidate states;
- start editing instructions;
- start a new content-production stage.
