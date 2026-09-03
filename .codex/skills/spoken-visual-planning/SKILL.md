---
name: spoken-visual-planning
description: Plan one acquisition-focused 3:4 WeChat Channels cover, one retention-focused 16:9 PPT cover, complete professional 16:9 detail pages, and AI image-generation prompts from a finalized spoken script or voiceover. Use after spoken copy is confirmed and the user explicitly requests PPT视觉、PPT配图、视觉分镜或AI生图提示词. Apply CURRENT_ACCOUNT visual DNA, require cover-copy and page-copy confirmation, and do not rewrite the script, generate images, or archive content.
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
Video cover: one fixed 3:4 image for WeChat Channels list and search display
PPT cover: one independent fixed 16:9 opening cover as the first in-video PPT image
Detail pages: fixed 16:9 landscape, one complete full-frame PPT information page per image
Safe area: no special subtitle, speaker, title, or account-information band
Visible copy: concise Chinese cover and PPT copy determined during planning
Tool mode: tool-neutral unless the user names a generation tool
```

The `3:4` video cover is additional and never counts toward the `16:9` PPT-page count. The independent `16:9` PPT cover is always the first in-video page and must be included in the spoken-range or audio-timestamp mapping. Use normal professional margins. Do not ask the user to choose these ratios, safe area, display placement, or whether text should appear. Ask about exact resolution, fixed page count, target tool, reference assets, logos, or fidelity only when the user explicitly makes them relevant.

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
→ 3:4 Video Cover Copy + 16:9 PPT Cover Copy + Detail-Page Copy
→ User Confirmation
→ Video-Cover Visual Design + PPT-Cover Visual Design + Detail-Page Visual Design
→ One Video-Cover Prompt + One PPT-Cover Prompt + One Prompt per Detail Page
→ Cover-to-deck Visual Consistency QA
→ AI生图执行指南.md + 剪辑分段表.md
```

#### Phase 1 — PPT Page Copy Confirmation

If the user specifies a total `16:9` page count, follow it exactly, reserve its first page for the PPT cover, and use the remaining pages for detail. If the user specifies a detail-page count, follow that count and add the independent PPT cover. Otherwise choose `3–6` detail pages according to content complexity and use the minimum count that preserves the full logic without overload.

Before listing pages, state `本次建议整理为 1 张3:4视频号封面 + 1 张16:9 PPT封面 + X 张16:9内容页。`

Present the cover first:

```markdown
# COVER｜视频号3:4封面

## 封面主标题

辅助钩子：

获客角度：

视觉建议：
```

Then present the independent PPT cover:

```markdown
# P1｜PPT封面

## 主标题

辅助钩子：

停留理由：

视觉建议：
```

Then use this format for every detail page, beginning with `P2`:

```markdown
# P2｜页面名称

## 标题

内容：

视觉建议：
```

The `3:4` video cover must extract the current content's strongest source-supported pain point, conclusion, benefit, risk, or cognitive contrast. Its job is to win visual attention from the target user in WeChat Channels list/search results without using misleading clickbait or inventing claims.

The `16:9` PPT cover must directly support target-viewer retention in the natural-feed viewing path. It must connect to the spoken opening, make the relevant viewer recognize that the topic concerns them, surface the core change, risk, benefit, or conflict, and provide a reason to keep watching. Keep it lower-density and visually stronger than every detail page. Do not use it to explain a process, calculation, comparison, checklist, or multi-part solution.

At this stage, `视觉建议` is conceptual only. Do not write final image prompts. After presenting both covers and all detail-page copy, stop and wait for explicit confirmation of the video-cover wording and acquisition angle, PPT-cover wording and retention angle, page count, titles, sequence, wording, and conceptual visual direction. If the user requests changes, remain in Phase 1.

Before presenting any visible title for confirmation, normalize it for image typography:

- remove sentence-style pause punctuation that does not carry meaning, especially `，`, `。`, `；`, and duplicate punctuation;
- express the intended pause through line breaking, spacing, or hierarchy instead of a comma;
- preserve punctuation only when it materially changes meaning, such as a necessary question mark, contrast marker, or semantic colon;
- never change business facts, numbers, terms, or conclusions while cleaning punctuation;
- treat the normalized and user-confirmed title as the exact visible literal used in all later prompts.

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

Follow `references/visual-aid-generation-rules.md` for page segmentation, page functions, page count, controlled semantic density, semantic-structure selection, three-layer visual richness, prompt construction, negative-constraint hierarchy, cross-page rhythm, and QA.

Treat the reference's safe margins, minimum legibility, typography-ratio, and overload-handling rules as execution constraints for every account. Treat other whitespace and element-scale guidance as readability guardrails rather than fixed canvas quotas. Account Visual DNA may change density and stylistic expression, but it must not reduce minimum margins or legibility. Express the intended spatial result inside positive layout instructions, not only inside `Avoid` clauses.

Each page must have one primary viewer-understanding target, one main title hierarchy, one primary semantic structure, only necessary supporting semantic details, one clear reading path, and meaningful progression from adjacent pages. The primary semantic structure may contain multiple coordinated components when all of them explain the same business meaning. Internally complete:

> After seeing this page, the viewer should immediately understand: ________.

The answer must be a business understanding outcome, not merely an object to draw.

If confirmed copy would force undersized text, more modules than the universal density limit, or inadequate whitespace, resolve it during Phase 1 by consolidating wording or increasing the page count with user confirmation. Never preserve a crowded page by shrinking the type or filling the canvas.

Create one independent cover prompt with stable ID `COVER-01`. The cover is not a PPT content page. It must:

- use a fixed `3:4` canvas;
- target WeChat Channels list/search discovery;
- communicate the strongest acquisition-relevant core point from the confirmed content;
- remain readable at thumbnail size;
- use one dominant Chinese headline and at most one short supporting hook;
- create stronger visual contrast than an inner page while preserving the same CURRENT_ACCOUNT colors, typography character, graphic language, and finish;
- avoid misleading urgency, unsupported promises, fabricated results, and unrelated decorative imagery.

Create one independent `16:9` PPT-cover prompt with stable ID `IMG-01`. It is the first in-video PPT image and must:

- connect directly to the spoken opening;
- make the target viewer recognize immediate relevance without requiring prior context;
- foreground one source-supported change, risk, benefit, or conflict and imply a reason to continue watching;
- use one dominant Chinese headline, at most one short supporting hook, and one primary visual focus;
- remain lower-density but visually stronger than every detail page through hierarchy, contrast, scale, and composition rather than added elements;
- avoid process diagrams, calculations, comparisons, checklists, multiple cards, or detailed solutions;
- use a native `16:9` composition and never be a crop or mechanical reuse of the `3:4` video cover;
- preserve the same CURRENT_ACCOUNT colors, typography character, graphic language, and finish as the detail pages.

Use complete detail-page archetypes such as conclusion, comparison, status dashboard, checklist, decision split, or short timeline. Do not let a detail archetype replace the independent PPT cover. Do not default to realistic export-business objects, chain-diagnosis diagrams, semi-realistic document piles, multi-arrow relationship structures, standalone illustrations, or generic flowcharts. Use such elements only when the confirmed page meaning genuinely requires them and keep them subordinate to the PPT hierarchy.

One PPT page must map to one independent image-generation prompt. Every prompt must explicitly include only generation-relevant information:

1. Slide Role;
2. Viewer Understanding Target;
3. Exact Required Chinese Copy;
4. Primary Semantic Structure;
5. Supporting Semantic Details;
6. Background Structure;
7. Composition and Reading Path;
8. Visual Hierarchy and Scale;
9. Concrete visual specifications compiled from CURRENT_ACCOUNT Visual DNA;
10. Spatial and Typography Readability;
11. Fixed 16:9 Complete-Page Finish;
12. Page-Specific Negative Constraints.

The cover prompt must explicitly include:

1. Exact Required Chinese Cover Copy;
2. Dominant Attention Device;
3. Native 3:4 Composition and Thumbnail Reading Order;
4. Background Structure;
5. Concrete color, typography, graphic, material, and finish specifications compiled from CURRENT_ACCOUNT Visual DNA;
6. Spatial and Typography Readability;
7. Complete-Cover Finish and Cover-to-Deck Continuity;
8. Cover-Specific Negative Constraints.

The `IMG-01` PPT-cover prompt must explicitly include:

1. Exact Required Chinese PPT-Cover Copy;
2. Primary Visual Conflict or Focus;
3. Composition Strategy and First-Glance Reading Order;
4. Background Structure;
5. Concrete color, typography, graphic, material, and finish specifications compiled from CURRENT_ACCOUNT Visual DNA;
6. Stronger-Than-Detail Visual Hierarchy and Spatial Readability;
7. Fixed Native 16:9 Complete-Page Finish;
8. PPT-Cover-Specific Negative Constraints.

Build prompts in this priority order:

```text
Viewer Understanding Target
→ Exact Business Meaning / Required Copy
→ Best Primary Semantic Structure
→ Three-Layer Composition and Visual Richness
→ CURRENT_ACCOUNT Visual DNA
→ Spatial and Typography Readability
→ Complete-Page Finish
→ Page-Specific Negative Constraints
```

Positive instructions must describe what to build more specifically than negatives describe what to avoid. Translate abstract terms such as `premium`, `professional`, or `rich` into executable composition, hierarchy, scale, spatial, material, depth, and visual-layer behavior.

Write copy-ready positive prompts and negative constraints in English unless the user explicitly requests another prompt language. Keep required visible wording as exact Chinese literals. Do not translate, transliterate, paraphrase, silently correct, or add wording. Default to Simplified Chinese unless explicitly overridden.

### Single-Execution Prompt Purity（单次执行提示词纯度）

`AI生图执行指南.md` is a single-execution generation document. Assume the image tool has no knowledge of the account, creator, persona, content workflow, marketing plan, or previous chat.

The guide itself must resolve all account-style references into concrete instructions. Do not require the generation tool to infer any visual rule from an account name, role, external file, previous prompt, or prior page.

In every copy-ready `Final Cover Prompt` and `Final Image Prompt`:

- never mention the account ID, account name, creator name, persona, speaker role, `CURRENT_ACCOUNT`, `Visual DNA`, or phrases such as `apply the account style`;
- compile account style into concrete executable visual instructions: exact colors and their roles, typography character, alignment, layout, graphic language, materials, depth, icon treatment, whitespace, and finish;
- exclude target-audience descriptions, search intent, acquisition strategy, retention strategy, spoken-opening commentary, page-planning rationale, and other business context unless it directly changes a visible object, relationship, label, hierarchy, or composition;
- do not refer to information located elsewhere in the guide or prior conversation; each final prompt must be independently executable when copied by itself;
- include no editing metadata, content-state information, publishing advice, account-management wording, or process commentary;
- after drafting, remove every sentence that does not change pixels, visible text, spatial relationships, semantic graphics, or generation constraints.

Planning rationale may remain concise in `Rule Logic` or `中文语义` only when it helps an operator verify semantic accuracy. It must not leak into the copy-ready final prompt.

Keep prompts tool-neutral until the target image-generation tool is confirmed. If the tool has no separate negative-prompt field, include the same constraints as a concise English `Avoid:` clause.

Visible Chinese copy is decided and confirmed during Phase 1. For either cover, prefer one dominant headline and zero or one short supporting hook. For detail pages, prefer one title and `1–3` short supporting strings. List every visible string verbatim in the prompt. The image model must not translate, paraphrase, or invent page copy, policies, tax rates, numbers, English labels, or small print.

Treat the current account's `账号视觉风格.md` as its Account Visual DNA. It controls account-specific rendering, color, background, material, UI/card/icon language, typography tendency, composition, whitespace, human presence, and avoid rules. It must not alter facts or reduce comprehension. Do not copy a global style string or silently default all accounts to one business/PPT look.

---

## AI Execution Document Architecture（AI执行文档结构）

`AI生图执行指南.md` must be optimized for AI-tool comprehension and execution stability. Use this order:

1. `Purpose / 目的`
2. `Execution Objective / 执行目标`
3. `Confirmed Page Structure / 已确认页面语义`
4. `Unified Visual System / 统一视觉系统`
5. `3:4 Video Cover Execution / 3:4视频封面执行`
6. `16:9 PPT Cover Execution / 16:9 PPT封面执行`
7. One execution section per 16:9 detail slide
8. `Visual Continuity and Quality Check / 视觉连续性与质量检查`
9. `Final Core Rules / 最终核心规则`

This is not an ordinary bilingual translation:

- English is the authoritative execution layer for priority, composition, layout behavior, hierarchy, required copy, style application, and prohibitions.
- Chinese is the semantic interpretation layer for business meaning, page intent, and the relationship the viewer must understand.
- Do not translate every English sentence into Chinese line by line.
- Keep exact visible Simplified Chinese copy as quoted literals inside the English image prompt.
- Final prompts are self-contained single-execution instructions and contain no account, creator, persona, audience-profile, workflow, or campaign metadata.

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

The same document must include one `COVER-01` section with the final `3:4` WeChat Channels cover prompt and one `IMG-01` section with the independent `16:9` PPT-cover prompt. `COVER-01` is additional to the confirmed PPT-page count and must not be placed in `剪辑分段表.md`; `IMG-01` is the first in-video PPT page and must be mapped there.

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
- Every `16:9` image is a complete, professionally designed PPT page.
- The deck begins with an independent `IMG-01` PPT cover, followed by readable detail-page progression and a resolved conclusion.
- No page defaults to realistic export objects, chain-diagnosis diagrams, semi-realistic documents, or multi-relationship structures.
- Hierarchy, alignment, whitespace, and component finish are aesthetically resolved.
- Each page uses one primary semantic structure with enough visual authority, supported by an intentional background structure and useful semantic details unless an ultra-minimal treatment is justified.
- No page can be reasonably satisfied by a title plus one floating card or icon, a tiny module on a mostly empty canvas, a stock SaaS template, or a generic three-column presentation layout.

### PPT cover quality
- Exactly one independent `16:9` PPT cover is included as `IMG-01`.
- `IMG-01` connects directly to the spoken opening and gives the target viewer an immediate reason to remain in the natural-feed viewing path.
- The relevant viewer can recognize within one glance that the topic concerns them and see one core change, risk, benefit, or conflict.
- `IMG-01` is visually stronger and less information-dense than every detail page.
- Its visual strength comes from hierarchy, contrast, scale, and composition rather than more modules or decoration.
- It contains one dominant headline, at most one supporting hook, and one primary visual focus.
- It contains no process, calculation, comparison, checklist, multi-card explanation, or detailed solution.
- It is a native `16:9` composition, not a crop or mechanical reuse of `COVER-01`.

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
- Positive instructions operationally define composition, hierarchy, scale, spatial relationships, semantic support, depth, and finish before concise negative constraints.
- Generic adjectives such as `premium`, `professional`, or `rich` never substitute for concrete design behavior.
- Every final prompt is independently executable with no assumed account, creator, persona, audience-profile, workflow, or prior-chat context.
- No account ID, account name, creator name, persona, speaker identity, `CURRENT_ACCOUNT`, `Visual DNA`, or unresolved style reference appears in a final prompt.
- Account style is compiled into concrete colors, typography, alignment, composition, graphic language, material, depth, spacing, and finish.
- Every sentence in a final prompt changes visible output or constrains generation.
- Display titles contain no unnecessary sentence-style commas or other pause punctuation.

### Cross-page consistency
- `COVER-01` uses `3:4`; `IMG-01` and every detail page use `16:9`.
- Background, color roles, UI/card/icon language, material, and rendering language are consistent.
- Title, body, label, and emphasis systems are consistent.
- Pages have sufficient whitespace, clear focal points, and professional page margins.
- Pages satisfy the universal safe-margin, spatial-readability, typography-ratio, line-count, and overload-handling constraints in the shared reference.
- Positive prompts explicitly define intentional breathing room and allow semantically dominant elements to become appropriately large; they do not rely on negative prompts alone.
- Consecutive pages do not mechanically repeat the same card arrangement or internal layout unless repetition is semantically justified.
- Cross-page continuity comes from Account Visual DNA, typography character, color logic, graphic language, and finish rather than identical templates.
- Icons, business relationships, process direction, comparison objects, and risk mapping are accurate.
- No policy, system, number, or document is fabricated.
- The `3:4` acquisition cover, `16:9` PPT cover, and `16:9` detail pages may use different composition roles while remaining one visual system.
- Adjacent pages do not repeat the same idea in different compositions.

### Deliverable usability
- `AI生图执行指南.md` is executable without reconstructing missing prompt context from the chat.
- `AI生图执行指南.md` contains no spoken segment, spoken excerpt, audio timestamp, or editing metadata.
- `剪辑分段表.md` is concise and usable during editing.
- `COVER-01` does not appear in the spoken-range or audio-timestamp mapping.
- `IMG-01` appears as the first in-video PPT mapping and aligns with the spoken opening.
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
