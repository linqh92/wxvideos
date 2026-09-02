---
name: spoken-visual-planning
description: Plan one acquisition-focused 3:4 WeChat Channels cover plus complete professional 16:9 PPT content pages and AI image-generation prompts from a finalized spoken script or voiceover. Use after spoken copy is confirmed and the user explicitly requests PPT视觉、PPT配图、视觉分镜或AI生图提示词. Apply CURRENT_ACCOUNT visual DNA, require cover-copy and page-copy confirmation, and do not rewrite the script, generate images, or archive content.
---

# WeChat Video Account Spoken PPT Visual Planning（微信视频号口播 PPT 图片规划）

## Trigger

Use this Skill only when BOTH conditions are satisfied:

1. A finalized or user-confirmed spoken script already exists, or the user provides a final voiceover/audio file.
2. The user explicitly requests a post-copy visual task such as:
   - PPT 图片 / PPT 页面视觉
   - 口播 PPT 配图 / PPT 生图 Prompt
   - 配图 / 示意图 / 中间画面
   - 视觉分镜 / AI 生图提示词
   - 根据口播或音频规划图片

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

### Fixed Production Defaults（固定生产默认值）

After the spoken content is confirmed and the user requests visual planning:

1. State that the task is entering the visual-planning stage.
2. State that this stage will not rewrite the spoken content, generate images, archive content, or change publication state.
3. Apply the following defaults without asking the user to confirm them.

```text
Content pages: fixed 16:9 landscape, one complete full-frame PPT information page per image
Video cover: one fixed 3:4 image for WeChat Channels list and search display
Safe area: no special subtitle, speaker, title, or account-information band
Visible copy: concise Chinese cover and PPT copy determined during planning
Tool mode: tool-neutral unless the user names a generation tool
```

The 3:4 cover is additional and never counts toward the 16:9 content-page count. Use normal professional margins. Do not ask the user to choose these ratios, safe area, display placement, or whether text should appear. Ask about exact resolution, fixed page count, target tool, reference assets, logos, or fidelity only when the user explicitly makes them relevant.

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

### PPT Planning and Prompt Assembly（PPT 规划与提示词合成）

Run this two-phase workflow:

```text
Finalized Spoken Content / Final Voiceover
→ Content Analysis
→ Page Count Decision
→ 3:4 Cover Copy + PPT Page Copy
→ User Confirmation
→ Cover Visual Design + PPT Page Visual Design
→ One Cover Prompt + One Prompt per PPT Page
→ Cover-to-deck Visual Consistency QA
→ AI生图执行指南.md + 剪辑分段表.md
```

#### Phase 1 — PPT Page Copy Confirmation

If the user specifies a page count, follow it exactly. Otherwise choose `3–6` pages according to content complexity and use the minimum count that preserves the full logic without overload.

Before listing pages, state `本次建议整理为 1 张3:4视频封面 + X 页16:9内容PPT。`

Present the cover first:

```markdown
# COVER｜视频号3:4封面

## 封面主标题

辅助钩子：

获客角度：

视觉建议：
```

Then use this format for each content page:

```markdown
# P1｜页面名称

## 标题

内容：

视觉建议：
```

The cover must extract the current content's strongest source-supported pain point, conclusion, benefit, risk, or cognitive contrast. Its job is to win visual attention from the target user in WeChat Channels list/search results without using misleading clickbait or inventing claims.

At this stage, `视觉建议` is conceptual only. Do not write final image prompts. After presenting the cover and all page copy, stop and wait for explicit confirmation of cover wording, acquisition angle, page count, titles, sequence, wording, and conceptual visual direction. If the user requests changes, remain in Phase 1.

#### Phase 2 — Visual Translation

Start only after unambiguous confirmation such as `确认`, `可以`, `没问题`, `继续`, or `下一步`.

Use three authority layers:

1. **Content layer:** finalized spoken content is the only authoritative business-content source. Extract, condense, reorganize, and convert it into PPT-friendly titles, conclusions, labels, or lists without adding policies, data, cases, numbers, facts, or changed conclusions.
2. **Structure layer:** determine page count, order, function, information progression, title hierarchy, density, and reading path. Reorganize for PPT reading rather than mechanically splitting sentences.
3. **Visual layer:** determine layouts, modules, color, graphic language, whitespace, and emphasis without changing the business meaning.

Use this priority:

```text
Spoken facts
> PPT information structure
> Visual presentation
> Decorative aesthetics
```

Read the complete spoken content first. Internally extract only what exists: topic, audience pain point, core conclusion, case, risk, cause, misconception, method, action direction, and CTA. Do not expose this analysis as a separate deliverable.

Follow `references/visual-aid-generation-rules.md` for page segmentation, page functions, page count, information density, page-module routing, prompt construction, three-layer negative constraints, and cross-page QA.

Each page must have one primary viewer-understanding target, one main title hierarchy, one core information module, only necessary support, one clear visual structure, and meaningful progression from adjacent pages. Internally complete:

> After seeing this page, the viewer should immediately understand: ________.

The answer must be a business understanding outcome, not merely an object to draw.

Create one independent cover prompt with stable ID `COVER-01`. The cover is not a PPT content page. It must:

- use a fixed `3:4` canvas;
- target WeChat Channels list/search discovery;
- communicate the strongest acquisition-relevant core point from the confirmed content;
- remain readable at thumbnail size;
- use one dominant Chinese headline and at most one short supporting hook;
- create stronger visual contrast than an inner page while preserving the same CURRENT_ACCOUNT colors, typography character, graphic language, and finish;
- avoid misleading urgency, unsupported promises, fabricated results, and unrelated decorative imagery.

Use complete PPT page archetypes such as opening hook, conclusion, comparison, status dashboard, checklist, decision split, or short timeline. Do not default to realistic export-business objects, chain-diagnosis diagrams, semi-realistic document piles, multi-arrow relationship structures, standalone illustrations, or generic flowcharts. Use such elements only when the confirmed page meaning genuinely requires them and keep them subordinate to the PPT hierarchy.

One PPT page must map to one independent image-generation prompt. Every prompt must explicitly include:

1. Slide Role;
2. Viewer Understanding Target;
3. Exact Required Chinese Copy;
4. PPT Page Archetype;
5. Layout and Reading Order;
6. Information Hierarchy;
7. Key Emphasis;
8. Relevant CURRENT_ACCOUNT Visual DNA;
9. Fixed 16:9 Complete-Page Output;
10. Quality Requirements;
11. Page-Specific Negative Constraints.

The cover prompt must explicitly include:

1. Search/List Acquisition Objective;
2. Target Viewer and Search Intent;
3. Exact Required Chinese Cover Copy;
4. Thumbnail Reading Order;
5. Visual Attention Device;
6. Relevant CURRENT_ACCOUNT Visual DNA;
7. Fixed 3:4 Output;
8. Cover-to-deck Continuity Requirements;
9. Cover-Specific Negative Constraints.

Write copy-ready positive prompts and negative constraints in English unless the user explicitly requests another prompt language. Keep required visible wording as exact Chinese literals. Do not translate, transliterate, paraphrase, silently correct, or add wording. Default to Simplified Chinese unless explicitly overridden.

Keep prompts tool-neutral until the target image-generation tool is confirmed. If the tool has no separate negative-prompt field, include the same constraints as a concise English `Avoid:` clause.

Visible Chinese copy is decided and confirmed during Phase 1. For the cover, prefer one dominant headline and zero or one short supporting hook. For content pages, prefer one title and `1–3` short supporting strings. List every visible string verbatim in the prompt. The image model must not translate, paraphrase, or invent page copy, policies, tax rates, numbers, English labels, or small print.

Treat the current account's `账号视觉风格.md` as its Account Visual DNA. It controls account-specific rendering, color, background, material, UI/card/icon language, typography tendency, composition, whitespace, human presence, and avoid rules. It must not alter facts or reduce comprehension. Do not copy a global style string or silently default all accounts to one business/PPT look.

---

## AI Execution Document Architecture（AI执行文档结构）

`AI生图执行指南.md` must be optimized for AI-tool comprehension and execution stability. Use this order:

1. `Purpose / 目的`
2. `Execution Objective / 执行目标`
3. `Confirmed Page Structure / 已确认页面语义`
4. `Unified Visual System / 统一视觉系统`
5. `3:4 Video Cover Execution / 3:4视频封面执行`
6. One execution section per 16:9 content slide
7. `Visual Continuity and Quality Check / 视觉连续性与质量检查`
8. `Final Core Rules / 最终核心规则`

This is not an ordinary bilingual translation:

- English is the authoritative execution layer for priority, composition, layout behavior, hierarchy, required copy, style application, and prohibitions.
- Chinese is the semantic interpretation layer for business meaning, page intent, and the relationship the viewer must understand.
- Do not translate every English sentence into Chinese line by line.
- Keep exact visible Simplified Chinese copy as quoted literals inside the English image prompt.

Write deck-wide rules once. Do not repeat long master descriptions, precise coordinate grids, or identical negative lists on every slide. Each slide should focus on its page-specific visual task.

---

## Output

Create exactly two standalone downloadable Markdown documents:

1. `AI生图执行指南.md` — a complete execution document that can be passed directly to an image-generation tool or operator.
2. `剪辑分段表.md` — a brief segment table for the user to reference during editing.

Do not replace them with a combined document, page-copy confirmation document, JSON, ordinary chat output, or a plain prompt list.

`AI生图执行指南.md` contains generation-execution information only. For each PPT page/image, include:

- a stable image ID;
- concise English execution rules;
- necessary Chinese semantic interpretation;
- one final English image prompt containing exact Chinese literals;
- concise English negative constraints;
- only the asset, fidelity, or continuity requirements needed for generation.

The same document must include one `COVER-01` section with the final `3:4` WeChat Channels cover prompt. The cover is additional to the confirmed content-page count and must not be placed in `剪辑分段表.md`.

Do not include spoken segments, spoken excerpts, audio timestamps, editing advice, BGM, transitions, performance direction, or publishing advice in `AI生图执行指南.md`. Page intent and Chinese semantic interpretation are allowed only when they improve AI execution.

Provide both documents for download in the final response. Do not require the user to choose, manage, or see a delivery directory. Do not repeat either document's body in the chat response; include only the two document links or attachments and a concise completion note.

The segmentation document must remain brief. It is the only deliverable that maps spoken ranges or actual audio timestamps to PPT image IDs and viewer-understanding targets. It must not expand into editing direction. Do NOT add transitions, BGM, sound effects, animation, camera movement, performance direction, or publishing advice by default.

If a final audio file is available, use its real timing. If only finalized spoken text is available, segment by spoken range and do not fabricate timestamps.

---

## Quality Gate

Before output, verify:

### Content and page structure
- Spoken facts and conclusions are unchanged.
- Confirmed page count, titles, wording, and sequence are unchanged.
- Pages are determined by communication function, not punctuation or source paragraphs.
- Every page has one clear understanding target and a distinct primary communication task.
- Pages have meaningful information progression.
- One complete PPT page maps to one prompt.
- Text and visual modules serve the understanding target rather than decoration.

### Complete PPT quality
- Every 16:9 content image is a complete, professionally designed PPT information page.
- The deck has an effective cover/hook, readable inner-page progression, and a resolved conclusion.
- No page defaults to realistic export objects, chain-diagnosis diagrams, semi-realistic documents, or multi-relationship structures.
- Hierarchy, alignment, whitespace, and component finish are aesthetically resolved.

### Video cover quality
- Exactly one `3:4` cover prompt is included as `COVER-01`.
- The cover uses the strongest confirmed acquisition angle from the current content.
- The main message remains readable at WeChat Channels thumbnail size.
- The cover earns attention through hierarchy, contrast, and relevance rather than clickbait.
- The cover is visually continuous with the account's 16:9 content deck.

### Account differentiation
- Every page explicitly applies CURRENT_ACCOUNT Visual DNA.
- The final prompts actually reflect CURRENT_ACCOUNT Visual DNA.
- The result is not silently falling back to a universal business style.
- Account style does not override comprehension.

### Prompt quality
- English instructions are direct, concise, and ordered by importance.
- Chinese content explains semantics rather than duplicating the English rules.
- Required in-image wording is listed as exact Chinese literals and is not translated or transliterated.
- Deck-wide rules are stated once; slide prompts contain only necessary page-specific differences.
- Each prompt describes a complete PPT page rather than a standalone explanatory illustration.
- Tool-specific syntax appears only when the target tool is confirmed.

### Cross-page consistency
- `COVER-01` uses `3:4`; every content page uses `16:9`.
- Background, color roles, UI/card/icon language, material, and rendering language are consistent.
- Title, body, label, and emphasis systems are consistent.
- Pages have sufficient whitespace, clear focal points, and professional page margins.
- Icons, business relationships, process direction, comparison objects, and risk mapping are accurate.
- No policy, system, number, or document is fabricated.
- The `3:4` acquisition cover and `16:9` content pages may use different composition roles while remaining one visual system.
- Adjacent pages do not repeat the same idea in different compositions.

### Deliverable usability
- `AI生图执行指南.md` is executable without reconstructing missing prompt context from the chat.
- `AI生图执行指南.md` contains no spoken segment, spoken excerpt, audio timestamp, or editing metadata.
- `剪辑分段表.md` is concise and usable during editing.
- `COVER-01` does not appear in the spoken-range or audio-timestamp mapping.
- Spoken-range or audio-timestamp mapping appears only in `剪辑分段表.md`.
- Timestamps are never fabricated when no final audio exists.
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
