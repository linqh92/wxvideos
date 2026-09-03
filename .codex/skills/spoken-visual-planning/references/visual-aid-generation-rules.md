# Spoken PPT Page Planning and Image-Prompt Rules（口播 PPT 页面规划与 AI 生图公共规则）

## 1. Role of This File（本文件职责）

This file defines the **shared 3:4 video-cover, independent 16:9 PPT-cover, 16:9 detail-page planning, confirmation, prompt-construction, and QA mechanism** for all accounts.

It MUST define:
- how finalized spoken content is analyzed;
- how PPT pages are segmented by communication function;
- how to define viewer-understanding targets;
- how to select internal PPT visual modules;
- how to control information density;
- when people should or should not appear;
- how to build one complete image prompt per PPT page;
- how to run cross-page consistency QA;
- universal image-quality constraints;
- universal fact / interface / text constraints.

It MUST NOT define a fixed account visual style.

Do NOT globally hard-code:
- color palette;
- rendering style;
- lighting style;
- background color;
- brand accent color;
- material style;
- illustration vs. photography;
- 2D vs. 3D;
- account-specific layout language.

Those belong to:

```text
accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号视觉风格.md
```

---

## 2. PPT Page Role（PPT 页面角色）

For spoken WeChat Channels content, each output image is a **complete PPT-style information page**, not a standalone explanatory illustration or character-performance scene.

Every visual package contains one independent `3:4` WeChat Channels cover for list/search discovery and one independent `16:9` PPT cover as the first in-video page. The `3:4` cover is not a PPT page and does not count toward the PPT-page total. The `16:9` PPT cover is part of the in-video deck and precedes all detail pages.

The visual should compensate for the limitations of listening-only comprehension.

The objective is:

> **让目标用户在听口播的同时，通过“看”更快理解业务关系、风险点、流程、差异和结论。**

The page should combine concise text and necessary visual modules to reduce cognitive load.

It should not merely make the screen look less empty.

---

## 3. Communication Priority（传播优先级）

Use this priority:

1. Information accuracy
2. Viewer understands faster
3. Image matches the current spoken topic
4. Best PPT information structure
5. Account visual identity
6. Stable page-switch rhythm
7. Decorative aesthetics

The account visual style is important, but it is subordinate to comprehension.

Do not optimize first for:
- actor emotion;
- office atmosphere;
- cinematic storytelling;
- decorative realism;
- generic business photography.

---

## 4. Content Analysis and PPT Page Segmentation（内容分析与 PPT 页面划分）

Read the complete finalized spoken content before planning any page.

Internally extract only what exists:

- topic;
- audience pain point;
- core conclusion;
- case;
- risk;
- cause;
- misconception;
- method;
- action direction;
- CTA.

Do not invent absent items. This analysis is internal and must not become a separate deliverable.

Segment by **page communication function**, not by subtitle line, source paragraph, punctuation, or fixed word count.

Common page functions include:

- capture pain point;
- state conclusion;
- correct misconception;
- show case;
- explain cause;
- expose risk;
- give method;
- compare two states;
- explain process;
- summarize action direction;
- CTA.

Consider a new page when one of these changes materially:

- core question;
- primary business object;
- logical relationship;
- cause → consequence;
- misconception → correct understanding;
- problem → risk;
- risk → solution;
- case → analysis;
- analysis → conclusion;
- conclusion → CTA.

Prefer merging when adjacent content shares the same core point, business object, risk point, causal relationship, or only varies wording, and one page can communicate it clearly without overload.

### Viewer understanding target

For each page, complete this sentence internally:

> **观众看到这一页以后，应该立即明白：________。**

This sentence must express a business understanding outcome, not merely a visual object.

Bad:

> 展示一个税务系统界面。

Good:

> 观众应立即明白：问题不是没有发票，而是付款主体与业务主体对不上。

### Fixed Production Defaults（固定生产默认值）

Use one native `16:9` PPT cover followed by `16:9` detail pages, and add one fixed `3:4` WeChat Channels list/search cover. Treat each `16:9` image as one complete full-frame PPT page. Use normal professional margins and do not reserve a mandatory subtitle, speaker, title, or account-information band.

Visible Chinese cover copy and PPT page copy are determined during copy planning. Do not ask the user to select a separate text-in-image strategy.

Keep prompts tool-neutral unless the user names a generation tool. Ask about resolution, assets, logos, fidelity, or tool-specific requirements only when the user's request makes them relevant.

---

## 5. Page Count and Page Planning（页数与页面规划）

If the user explicitly specifies the page/image count, follow it exactly unless a higher-priority explicit instruction conflicts:

```text
User-Specified Page Count > Automatic Decision
```

If the user specifies a total `16:9` page count, reserve the first page for the PPT cover and use the remainder for detail pages. If the user specifies a detail-page count, add the independent PPT cover to that count. Otherwise choose `3–6` detail pages according to content complexity and use the minimum number that preserves the complete logic without overload.

Do not create one page per sentence. Every page must have:

1. one primary understanding target;
2. one main title hierarchy;
3. one primary semantic structure, which may contain several coordinated components serving the same meaning;
4. only necessary supporting semantic details;
5. one clear visual structure;
6. a meaningful relationship to adjacent pages.

The page sequence must reorganize spoken content for PPT reading and create meaningful information progression rather than preserve source paragraph boundaries.

Before visual prompting, output `本次建议整理为 1 张3:4视频号封面 + 1 张16:9 PPT封面 + X 张16:9内容页。`

Present the cover first:

```markdown
# COVER｜视频号3:4封面

## 封面主标题

辅助钩子：

获客角度：

视觉建议：
```

Then present the PPT cover:

```markdown
# P1｜PPT封面

## 主标题

辅助钩子：

停留理由：

视觉建议：
```

Then present every detail page, beginning with `P2`, in this format:

```markdown
# P2｜页面名称

## 标题

内容：

视觉建议：
```

The `3:4` video cover must use the strongest source-supported core point from an acquisition perspective: a pain point, decisive conclusion, relevant benefit, risk, or cognitive contrast. It must match the target user's likely search intent without misleading clickbait or unsupported promises.

The `16:9` PPT cover must support retention after the video enters the target viewer's natural-feed path. It must connect to the spoken opening, establish immediate relevance, surface one core change, risk, benefit, or conflict, and create a reason to continue watching. It is not a detail page and must not begin explaining the process, calculation, comparison, checklist, or solution.

The visual suggestion remains conceptual at this stage.

### Title punctuation normalization

Before showing cover and page titles for confirmation, optimize them as display typography rather than preserving sentence punctuation mechanically:

- remove non-semantic pause punctuation, especially Chinese commas `，`, full stops `。`, semicolons `；`, and duplicated punctuation;
- create rhythm with line breaks, spacing, weight, or alignment instead of leaving a comma in a display title;
- retain a question mark, colon, dash, or other punctuation only when it carries necessary meaning or defines the title structure;
- preserve every fact, number, term, and conclusion;
- once the user confirms the normalized title, use that exact literal consistently in the execution guide and final prompt.

### Mandatory confirmation gate

After presenting both covers and all detail-page copy, stop. Wait for explicit confirmation of the video-cover headline, supporting hook and acquisition angle; the PPT-cover headline, supporting hook and retention angle; the page count, titles, sequence, wording, and conceptual visual direction. If changes are requested, revise the copy and remain at this stage. Do not generate final image prompts until the user gives unambiguous confirmation.

---

## 6. WeChat Channels Acquisition Cover（视频号获客封面）

The `3:4` cover has a different communication job from the PPT pages. It must win relevant visual attention in WeChat Channels list/search results and make the target user want to open the video.

Requirements:

- stable ID: `COVER-01`;
- fixed `3:4` canvas;
- one dominant Chinese headline;
- zero or one short supporting hook;
- one obvious focal device: contrast, key number, status conflict, or decisive conclusion;
- strong thumbnail readability;
- direct relevance to the target user's search intent;
- no unsupported result promise, misleading urgency, or sensational wording;
- the same account colors, typography character, graphic language, and finish as the content deck;
- stronger emphasis and contrast than an inner slide without becoming a disconnected advertising poster.

Do not create the cover by cropping a `16:9` page. Recompose it specifically for the vertical `3:4` frame.

---

## 7. Complete PPT Page Archetypes（完整PPT页面原型）

Choose the page archetype from the confirmed communication task. Do not begin from card count, an object, illustration, diagram type, or fixed layout template. A page may use several coordinated components when they form one primary semantic structure and explain the same business meaning.

### 7.1 PPT Cover Page（PPT封面）

The first `16:9` page is always the independent PPT cover. Its functional job is to retain the relevant target viewer after the video appears in the natural-feed viewing path. Use one source-supported conflict, pain point, change, risk, benefit, question, or decisive conclusion that connects directly to the spoken opening. Prefer one dominant title, zero or one short supporting hook, one primary visual focus, and a restrained background.

The PPT cover must be visually stronger than every detail page through hierarchy, contrast, scale, and composition, not through higher information density. It must not contain a process diagram, calculation structure, comparison layout, checklist, multi-card explanation, or detailed solution. Build it natively for `16:9`; do not crop or mechanically reuse the `3:4` list/search cover.

### 7.2 Conclusion Page（结论页）

Use one visually dominant conclusion, number, or judgment. It may be integrated with a timing arc, marker, status cue, key-object relationship, or other restrained support when those components clarify the same conclusion. Do not dilute it with several equal cards.

### 7.3 Comparison Page（对比页）

Use two clearly matched states with equal visual weight and obvious differentiation. Avoid long explanations, mismatched structures, or weak contrast.

### 7.4 Process or Timeline Page（流程或时间页）

Use only when order is essential. Keep `3–5` visible stages, one direction, and one highlighted threshold. Do not convert every explanation into a process.

### 7.5 Checklist or Diagnostic Page（检查或诊断页）

Use for concrete actions or multiple checks. Use `2–4` aligned cards or rows only when independent items genuinely need separation; otherwise prefer a visual checkpoint sequence, diagnostic field, or semantic node cluster. Do not imply sequence unless one exists.

### 7.6 Status or Dashboard Page（状态或看板页）

Use a status track, layered state field, verification panel, semantic node cluster, or restrained cards only when they directly explain the confirmed content. Cards are a separation tool, not the default page skeleton. Do not add random charts, fake data, or fabricated interfaces merely to look professional.

### 7.7 Decision Split Page（分支判断页）

Use when the viewer must distinguish two causes, states, or next actions. Keep the split balanced and the branch conclusions immediately readable.

### 7.8 Case Page（案例页）

Use only when the source contains a real case. Present it as a clear information composition, not a dramatic character scene or decorative business photograph.

### Legacy visual forms

Relationship maps, realistic business scenes, object-focused visuals, semi-realistic documents, and multi-arrow structures are not default page archetypes. Use them only when the confirmed meaning cannot be expressed more clearly through the professional PPT archetypes above, and keep them subordinate to the page hierarchy.

### 7.9 Reusable Semantic Composition Vocabulary（可复用语义构图词汇）

Select the smallest useful form that explains the page meaning. Reusable options include:

- editorial infographic composition;
- large-number composition;
- status track;
- decision axis;
- layered state field;
- semantic node cluster;
- split-field comparison;
- visual checkpoint sequence;
- key-object composition;
- reconciliation structure;
- large typographic statement integrated with a visual system;
- structured geometric field.

Allow top-left editorial, top-centered, asymmetric left-weighted, split, large-number-led, visual-right/text-left, visual-left/text-right, or centered-statement compositions when appropriate. Do not force consecutive slides into the same title position or card arrangement unless repetition is semantically useful.

---

## 8. Human Presence Rule（人物使用规则）

Default:

> **If the image communicates better without a person, remove the person.**

Use people only when:
- their action clarifies the process;
- their role is necessary to identify the business relationship;
- the scene would otherwise become too abstract.

People must not become the main narrative device.

Avoid by default:
- 双人对话镜头;
- 老板和财务面对面交流;
- 会议室讨论;
- 握手;
- 多人围桌;
- 争论;
- 审讯式场景;
- 情绪化表演;
- 普通商务肖像;
- “两个人看文件”的万能镜头.

This is a communication rule, not a style rule.

---

## 9. Account Visual DNA Injection（账号视觉DNA注入）

This section is the `CURRENT_ACCOUNT visual-style injection` boundary. It applies account identity after the best semantic structure has been selected and must never redefine shared comprehension or factual rules.

After choosing the best explanatory visual form, read:

```text
accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号视觉风格.md
```

Inject the account Visual DNA into:
- rendering;
- color;
- background;
- material / texture;
- UI and card language;
- icon language;
- typography hierarchy tendency;
- graphic language;
- composition tendency;
- whitespace pattern;
- human-presence tendency;
- information density;
- label style;
- account-specific negative style constraints.

Do not let Visual DNA change the factual relationship being explained.

Do not let Visual DNA force a less understandable visual form.

The account file is an internal source, not something the image-generation tool can resolve. Compile its relevant rules into concrete visual instructions. Never place the account ID, account name, creator name, persona, speaker identity, `CURRENT_ACCOUNT`, `Visual DNA`, or a reference such as `apply the account style` inside a copy-ready final prompt.

Do not hard-code a government-grade SaaS Dashboard style, one blue-gray/orange palette, one background, a no-people rule, a `40% left / 60% right` layout, or white rounded cards for every account. The shared workflow fixes one `3:4` acquisition cover, one `16:9` PPT cover, and `16:9` detail pages; visual identity comes from the current account's authoritative visual-style file.

---

## 10. PPT Information Density（PPT 信息密度）

One PPT page should carry one primary communication task.

A page may contain:

- title and optional subtitle;
- 1–3 short supporting points;
- numbers and labels;
- process, comparison, relationship, or status modules;
- cards, icons, arrows, and a concise conclusion.

Avoid:

- multiple unrelated topics;
- excessive cards or UI stacking;
- long paragraphs and dense small text;
- several complex processes on one page;
- crowded spacing or unclear hierarchy;
- too many business documents or labels.

The viewer should identify the page's main point within roughly one second. Exact density may vary by account, but comprehension remains the upper bound.

### 10.1 Three-Layer Semantic Richness（三级语义视觉层）

Unless an intentionally ultra-minimal page is justified by its communication role, define a controlled three-layer composition:

1. **Background Structure** — low-contrast, non-factual structure such as restrained gradients, structural grids, cropped numerals, soft geometric fields, subtle paths, section framing, abstract business-network traces, understated scale/tick motifs, or page-edge accents.
2. **Primary Semantic Structure** — the dominant business meaning, such as a decisive number, state conflict, comparison, decision split, timeline, diagnostic relationship, reconciliation, or key-object relationship.
3. **Supporting Semantic Details** — normally `2–4` useful markers, status dots, short labels, micro-icons, breakpoint indicators, supporting nodes, restrained highlights, or secondary shape transitions.

Every layer must support the same viewer-understanding target. Background structure must not create new business claims, and supporting details must explain rather than decorate empty space. The layers may remain visually restrained; this is a completeness model, not a requirement to make every layer busy.

### 10.2 Universal Spatial Readability Guardrails（通用空间可读性护栏）

Use spatial restraint as a readability outcome, not a mechanical canvas quota. The safe-margin and minimum-legibility rules below are hard constraints; all other scale and whitespace guidance is a soft guardrail and overload warning. An account may use a calmer or denser composition when its Visual DNA supports it, provided the page remains immediately scannable and does not crowd required copy.

For every `16:9` content page:

- keep an outer safe margin of at least `7%` of the canvas short side;
- compose enough negative space to separate hierarchy and keep the page breathable;
- allow the primary semantic structure to occupy a large, visually dominant region when the page meaning requires it;
- keep clear gaps between distinct semantic groups and align supporting details to the primary structure;
- use only as many non-semantic decorative elements as the account style needs for a resolved finish, without competing with the message.

For the independent `16:9` PPT cover:

- keep the same outer safe-margin floor as other `16:9` pages;
- use one primary visual focus and no explanatory module set;
- create a lower-density but fully composed background field and enough open space for immediate headline recognition;
- allow the headline, core status, number, or semantic shape to become visually dominant when that is the retention device;
- create stronger visual contrast than every detail page without adding unrelated modules.

For every `3:4` acquisition cover:

- keep an outer safe margin of at least `8%` of the canvas short side;
- preserve visibly intentional open space around the reading path;
- make the main headline the dominant first-glance element without crowding the frame or safe margin;
- keep the supporting hook to one short block;
- size the primary non-text visual according to its semantic importance rather than a fixed area cap.

Do not shrink the main visual merely to satisfy an occupied-area percentage. When using scale language, explain the intended hierarchy and relationship: what dominates, what remains secondary, how the eye moves, and how surrounding space is composed. Oversized numerals, cropped semantic shapes, large status fields, relationship paths, and strongly weighted regions are allowed when they are the confirmed meaning and remain readable and intentional.

**中文语义：** 留白是主动组织阅读节奏的空间，不是必须达标的固定面积。主语义结构该大时可以大，但必须有清晰层级、稳定边距和有意设计的周边空间。

### 10.3 Universal Typography Proportion（通用字体比例）

Treat body copy as the `1.0` visual-size baseline. Use perceived cap-height ratios rather than tool-specific point sizes:

- content-page title: `1.8–2.2×` body copy;
- key number or decisive conclusion: `2.0–2.6×` body copy;
- supporting label: `0.75–0.85×` body copy;
- necessary annotation: never below `0.70×` body copy;
- no more than four visible type-size levels on one page.

Keep a content-page title to no more than two balanced lines. Keep each supporting point to no more than two lines. Leave at least one body-line height between the title block and the main information area. Use tabular-width numerals and common baselines when amounts, percentages, dates, or ranges are compared.

For a `3:4` cover, keep the headline to two or three balanced lines and make it the first reading target without allowing it to fill the frame. Use one smaller supporting-hook level and avoid a third explanatory text level.

For the `16:9` PPT cover, keep the headline to no more than two balanced lines and at roughly `1.2–1.4×` the perceived size of a detail-page title. Use zero or one short supporting hook and no third explanatory text level. The cover's hierarchy must remain stronger than detail pages even when the account Visual DNA uses a restrained style.

**中文语义：** 字号层级服务于阅读顺序。标题先被看到，关键数字或结论获得强调，正文保持稳定可读；不得为了塞进更多内容而缩小正文、压缩行距或制造过多字号层级。

### 10.4 Universal Overload Thresholds（通用超载阈值）

For a normal content page, prefer one title plus `1–3` supporting strings. As operational limits:

- keep visible Chinese copy near or below `65` Chinese characters when the meaning permits;
- use no more than four independent information modules;
- use no more than four visible process stages by default;
- when a checklist exceeds five items, split or regroup it instead of reducing type size;
- when any limit conflicts with factual completeness, add or re-plan pages during Phase 1 and obtain confirmation rather than deleting required meaning.

Resolve overload in this order:

1. remove non-informational decoration;
2. consolidate repeated or subordinate expression without changing meaning;
3. reduce the scale and visual weight of supporting elements;
4. increase or re-plan pages with user confirmation.

Never solve overload first by shrinking text, compressing line spacing, removing margins, or enlarging every module to compete for attention.

**中文语义：** 内容要点必须保留，但不要求全部挤在同一页。超过承载上限时，先去装饰、再合并表达、再降低辅助元素权重，最后通过确认后的分页解决。

---

## 11. AI Execution Document and Prompt Structure（AI执行文档与Prompt结构）

The final `AI生图执行指南.md` must follow this order:

1. `Purpose / 目的`
2. `Execution Objective / 执行目标`
3. `Confirmed Page Structure / 已确认页面语义`
4. `Unified Visual System / 统一视觉系统`
5. `3:4 Video Cover Execution / 3:4视频封面执行`
6. `16:9 PPT Cover Execution / 16:9 PPT封面执行`
7. `16:9 Detail Slide Execution Sections / 16:9内容页逐页执行`
8. `Visual Continuity and Quality Check / 视觉连续性与质量检查`
9. `Final Core Rules / 最终核心规则`

This is not an ordinary bilingual translation:

- English defines executable logic, priority, layout behavior, hierarchy, required copy, style application, and prohibitions.
- Chinese explains business semantics, page intent, and what the viewer must understand.
- Chinese must not duplicate every English sentence line by line.
- Exact visible Simplified Chinese copy remains quoted inside the English prompt.

Write global deck rules once. Per-slide prompts should reference the unified system and focus on page-specific composition. Avoid repeated master paragraphs, precise coordinate grids, and identical long negative lists.

The cover section must contain:

```markdown
## COVER-01｜3:4 Video Cover

### Rule Logic
[English acquisition objective, target viewer/search intent, thumbnail hierarchy, and style-continuity rules]

### 中文语义
[核心卖点、目标用户痛点与获客表达意图]

### Final Cover Prompt
[One self-contained English 3:4 prompt containing the exact Chinese cover copy]

### Avoid
[Concise English cover-specific negative constraints]
```

The final cover prompt must define, in this priority order:

1. exact Chinese headline and optional supporting hook;
2. dominant attention device;
3. native `3:4` composition and thumbnail-first reading order;
4. background structure;
5. concrete color, typography, graphic, material, depth, and finish specifications compiled from the account style;
6. spatial readability;
7. complete-cover finish;
8. cover-specific failures to avoid.

### Compact 3:4 Cover Prompt Template

```text
Create one professional 3:4 WeChat Channels video cover for list and search discovery.

Render exactly this Simplified Chinese cover copy and no other visible text:
Main headline: "[exact Chinese headline]"
Supporting hook: "[exact Chinese hook]" or None

Design for small-thumbnail readability. Make the main headline the first focal point,
followed by [key number / status conflict / decisive conclusion / benefit or risk cue].
Use a strong but professional vertical 3:4 composition; do not crop a 16:9 slide.
Composition and reading path: [state the visual center of gravity, direction, alignment,
scale contrast, and relationship between headline, attention device, and supporting hook].
Background structure: [state the low-contrast structural layer that makes the frame feel
complete without adding a business claim]. Preserve the universal safe margin and apply
the universal cover typography hierarchy and line-count limits.

Use these concrete visual specifications compiled for this execution: [exact color roles,
typography character, graphic language, material, depth, spacing, and finish]. Maintain
the same specified visual system as the 16:9 content deck, with slightly stronger
contrast and emphasis for acquisition.

High-resolution, visually distinctive, credible, relevant, uncluttered, and readable
at thumbnail size. Deliver a fully resolved cover with intentional hierarchy, depth,
spatial balance, visual-system consistency, and no visually unfinished region.
```

The PPT-cover section must contain:

```markdown
## IMG-01｜16:9 PPT Cover

### Rule Logic
[English retention objective, target-viewer relevance, spoken-opening connection, visual-strength hierarchy, and style-continuity rules]

### 中文语义
[目标客户为什么会停留，以及第一眼必须识别的核心变化、风险、利益或冲突]

### Final Image Prompt
[One self-contained English 16:9 prompt containing the exact Chinese PPT-cover copy]

### Avoid
[Concise English PPT-cover-specific negative constraints]
```

The final PPT-cover prompt must define, in this priority order:

1. exact Chinese headline and optional supporting hook;
2. primary visual conflict or focus;
3. composition strategy and first-glance reading order;
4. background structure;
5. concrete color, typography, graphic, material, depth, and finish specifications compiled from the account style;
6. stronger-than-detail hierarchy and spatial readability;
7. fixed native `16:9` complete-page finish;
8. PPT-cover-specific failures to avoid.

### Compact 16:9 PPT Cover Prompt Template

```text
Create one independent, professional 16:9 PPT cover as the first in-video page.

Render exactly this Simplified Chinese PPT-cover copy and no other visible text:
Main headline: "[exact Chinese headline]"
Supporting hook: "[exact Chinese hook]" or None

Use one primary visual focus and a native 16:9 composition. Make this cover visually
stronger than every detail page through hierarchy, contrast, scale, and composition,
not through unrelated elements. Composition strategy: [state the visual center of gravity,
direction, dominant shape or field, alignment logic, scale contrast, and first-glance path].
Background structure: [state the low-contrast structural field and how open space is
intentionally composed]. Keep the headline to no more than two balanced lines at roughly
1.2–1.4× the perceived size of detail-page titles.

Use these concrete visual specifications compiled for this execution: [exact color roles,
typography character, graphic language, material, depth, spacing, and finish]. Maintain
the same specified system as the detail pages while giving the PPT cover a stronger
first-glance focal hierarchy.

Do not crop or mechanically reuse the 3:4 video cover. Do not explain a process,
calculation, comparison, checklist, multi-part solution, or detailed conclusion here.
High-resolution, presentation-ready, credible, immediately relevant, and fully resolved
as a complete cover rather than a title plus one floating object.
```

Every detail-slide section, beginning with `IMG-02`, must contain:

```markdown
## IMG-02

### Rule Logic
[Concise English execution rules]

### 中文语义
[Business meaning and page intent]

### Final Image Prompt
[One self-contained English prompt containing exact Chinese literals]

### Avoid
[Concise English page-specific negative constraints]
```

Each final prompt must define, in this priority order:

1. slide role;
2. one viewer-understanding outcome;
3. exact required Chinese copy;
4. primary semantic structure;
5. supporting semantic details;
6. background structure;
7. composition and reading path;
8. visual hierarchy and scale;
9. concrete visual specifications compiled from the account style;
10. spatial and typography readability;
11. fixed `16:9` complete-page finish;
12. page-specific failures to avoid.

### Compact Tool-Neutral English Prompt Template

```text
Create one complete, professional 16:9 PPT slide as part of the same deck.

Slide role: [hook / conclusion / comparison / process / checklist / status / decision / case].
The viewer should immediately understand: [one business outcome].

Render exactly this Simplified Chinese PPT copy and no other visible text:
Title: "[exact Chinese title]"
Supporting copy: "[exact Chinese string]", "[exact Chinese string]"

Primary semantic structure: [the dominant composition that explains the business meaning].
Supporting semantic details: [2–4 useful markers, labels, nodes, highlights, or transitions,
or explicitly justify fewer for an ultra-minimal page].
Background structure: [a low-contrast structural layer with no new factual claim].
Composition and reading path: [visual center of gravity, direction, foreground/middle/background
relationship, dominant shape, secondary structure, alignment logic, and visual rhythm].
Information hierarchy and scale: [title > conclusion > semantic structure > support], with
[key term, number, contrast, status, or relationship] visually dominant when appropriate.
Spatial readability: preserve the safe margins, use enough intentionally composed open space
for immediate scanning, and do not shrink the primary structure to satisfy a fixed area quota.
Typography scale: apply the universal title/body/label ratios and line-count limits.

Use these concrete visual specifications compiled for this execution: [exact color roles,
typography hierarchy, UI/card language, icon style, material, depth, spacing rhythm,
and finish]. Maintain this same specified system across the deck.

High-resolution and presentation-ready. Deliver a fully resolved composition with intentional
hierarchy, depth, spatial balance, visual-system consistency, precise alignment, and complete-page finish.
```

Keep prompts tool-neutral until the user names a generation tool. Do not promise exact cross-slide pixel identity unless a real reference slide, template, or asset is supplied. Do not place spoken excerpts, audio timing, or editing metadata inside the execution guide.

### 11.1 Single-Execution Prompt Purity（单次执行提示词纯度）

Treat every `Final Cover Prompt` and `Final Image Prompt` as a standalone instruction pasted into an image-generation tool with no memory or account context.

The copy-ready prompt must not contain:

- account ID, account name, creator name, persona, speaker identity, or business-role biography;
- `CURRENT_ACCOUNT`, `Visual DNA`, `apply the account style`, or any unresolved reference to another file, page, prompt, chat, or workflow;
- target-audience profiles, search intent, acquisition rationale, retention rationale, spoken-opening explanation, publishing state, or campaign strategy unless one of these directly defines a visible object or composition;
- editing advice, timestamps, spoken excerpts, BGM, transitions, performance notes, or archive instructions;
- internal planning labels that do not change the rendered image.

Compile account style into explicit pixel-affecting instructions: colors and their roles, background treatment, typography character, alignment, composition, scale, graphic language, icon treatment, material, depth, whitespace, and finish.

After drafting each final prompt, apply the pixel-impact test:

> If a sentence does not change visible text, objects, relationships, hierarchy, composition, color, material, depth, legibility, output format, or negative constraints, remove it from the final prompt.

Planning rationale may remain concise in `Rule Logic` and `中文语义` for operator verification, but it must not leak into the copy-ready prompt.

---

## 12. Negative Prompt Architecture（反向提示词架构）

Use three negative layers, but state each shared layer only once and keep the positive composition instructions longer and more operational than the negatives. Deliver all copy-ready negative constraints in English. If the confirmed tool has a separate negative-prompt field, place them there. Otherwise append them to the positive prompt as a concise English `Avoid:` clause.

### 12.1 Universal Quality Negatives（公共质量反向词）

Define once at deck level:

```text
low resolution, blur, malformed layout, clutter, weak information hierarchy,
unreadable or garbled Chinese, invented text or numbers, fabricated official interfaces,
watermarks, incorrect logos, cropped important content, meaningless decorative UI,
compressed margins, undersized body text, too many type-size levels, unfinished slide draft,
title with one floating card, isolated icon composition, stock SaaS template,
mostly empty canvas with a tiny module, generic three-column presentation template,
decorative UI with no semantic relationship.
```

These are quality / communication constraints.

### 12.2 Account-Specific Style Negatives（账号风格反向词）

Read from:

```text
账号视觉风格.md
```

These are NOT global rules.

### 12.3 Scene-Specific Negatives / Page-Specific Negatives（页面专属反向词）

Generate only the failures relevant to the selected page archetype. Do not repeat the complete universal list in every slide.

#### Process page
- avoid excessive arrows;
- avoid too many process nodes;
- avoid unclear sequence;
- avoid information overload;
- avoid abstract flow that cannot be understood quickly.

#### Comparison page
- avoid asymmetric comparison objects;
- avoid inconsistent card hierarchy;
- avoid too much explanatory text.
- avoid weak contrast.

#### Risk page
- avoid warning decoration overwhelming the core object;
- avoid excessive red;
- avoid decorative alarm symbols;
- avoid unclear risk objects.

#### Dashboard / card page
- avoid meaningless data;
- avoid random charts;
- avoid fabricated official interfaces;
- avoid tiny UI text;
- avoid excessive card stacking.

#### 3:4 acquisition cover
- avoid simply cropping a 16:9 slide;
- avoid weak thumbnail contrast;
- avoid long or multi-line supporting copy;
- avoid more than two competing focal points;
- avoid oversized headlines or non-text visuals filling the frame;
- avoid compressed margins and insufficient open space;
- avoid irrelevant decorative imagery;
- avoid sensational clickbait, unsupported promises, and fabricated outcomes;
- avoid breaking the CURRENT_ACCOUNT visual identity.

#### 16:9 PPT cover
- avoid a generic chapter-title or corporate title-slide treatment;
- avoid weak relevance to the target viewer or spoken opening;
- avoid the same visual intensity as or weaker intensity than detail pages;
- avoid process diagrams, calculations, comparisons, checklists, or multi-card explanations;
- avoid more than one primary visual focus;
- avoid adding elements merely to create impact;
- avoid cropping or mechanically reusing the `3:4` video cover;
- avoid unsupported urgency, promises, outcomes, or claims.

---

## 13. PPT Text Handling（PPT页面文字处理）

Visible Chinese copy is determined in the confirmed cover and PPT page copy. It is not a separate user-confirmation setting.

For either cover, prefer one dominant headline and zero or one short supporting hook. For each `16:9` detail page, prefer one title and `1–3` short supporting strings. List every permitted string verbatim in the English prompt.

Prefer:
- one concise title;
- one short conclusion or key number;
- short status labels;
- grouping and alignment;
- consistent cards and icons;
- one clear emphasis treatment.

Avoid:
- full Chinese paragraphs;
- full bank statements;
- full invoices;
- full official notices;
- dense tax forms;
- policy text reproduced inside the image.

If a draft page contains too much text for reliable generation, condense it during the page-copy stage and obtain user confirmation before prompt generation.

When short Chinese labels are generated:

- list every permitted label verbatim in a separate `Required Chinese text` field;
- repeat those exact Chinese literals inside the English prompt;
- instruct the model not to translate, transliterate, paraphrase, or add text;
- default to Simplified Chinese unless the user explicitly requests Traditional Chinese;
- preserve confirmed numbers, capitalization, symbols, and normalized confirmed punctuation exactly;
- add `no English text, no extra characters, no garbled Chinese text, no invented text, no invented numbers` to the English negative constraints.

Never translate, transliterate, paraphrase, or invent page text, policy names, tax rates, numbers, English labels, or unauthorized small print merely to complete the layout.

For titles, “preserve punctuation exactly” applies only after display-title normalization and user confirmation. Do not copy sentence-style commas into a title by habit. A confirmed title should normally express pauses through line breaks or spacing; retain punctuation only when it carries necessary meaning.

---

## 14. Official-Looking Interface Risk（伪官方界面风险）

Do not create fabricated screenshots that appear to be real:
- tax bureau systems;
- banking systems;
- customs systems;
- government portals;
- official notices.

When a system interface is useful, use a neutral schematic representation:
- generic table;
- generic transaction row;
- generic document card;
- generic status indicator.

The image should explain the logic, not impersonate an official system.

---

## 15. Cover and Cross-Page Visual Consistency QA（封面与跨页视觉一致性检查）

After the video-cover prompt, PPT-cover prompt, and all detail-page prompts are drafted, run one complete cover-to-deck QA pass and revise failed prompts before output.

### Canvas

- `COVER-01` uses fixed `3:4`;
- `IMG-01` and every detail page use fixed `16:9`;
- consistent resolution when specified;
- all `16:9` PPT pages keep at least the universal `7%` safe margin;
- `3:4` covers keep at least the universal `8%` safe margin;
- the absence of a mandatory reserved band does not authorize edge-to-edge information filling.

### Acquisition cover

- the cover uses the strongest confirmed acquisition angle;
- the main headline is readable at list/search thumbnail size;
- the composition was designed for `3:4`, not cropped from `16:9`;
- the cover earns attention through relevance, hierarchy, and contrast rather than clickbait;
- the cover remains recognizably part of the same account visual system as the content deck.

### PPT cover

- exactly one independent PPT cover appears as `IMG-01` before every detail page;
- it connects directly to the spoken opening and gives the relevant target viewer a reason to remain in the natural-feed viewing path;
- one glance reveals who the content concerns and one core change, risk, benefit, or conflict;
- it is visually stronger and less information-dense than every detail page;
- its strength comes from hierarchy, contrast, scale, and composition rather than additional modules or decoration;
- it uses one dominant headline, at most one supporting hook, and one primary visual focus;
- it contains no process, calculation, comparison, checklist, multi-card explanation, or detailed solution;
- it is a native `16:9` composition, not a crop or mechanical reuse of `COVER-01`.

### Visual DNA

- consistent background and color roles;
- consistent UI, card, and icon language;
- consistent material and rendering language.

### Typography

- consistent title hierarchy;
- consistent body-text logic;
- consistent label system;
- consistent emphasis behavior.
- title, body, label, and annotation sizes satisfy the universal visual-size ratios;
- titles and supporting points satisfy the universal line-count limits;
- display titles contain no unnecessary sentence-style commas or other pause punctuation;
- no page uses smaller text or tighter line spacing to compensate for overload.

### Layout

- no page is overfilled;
- cards appear only when item separation improves comprehension;
- open space is intentionally composed rather than left as an unfinished void;
- clear primary focal point;
- important elements are not too close to edges;
- no meaningless decoration;
- the primary semantic structure has enough visual authority for the page meaning;
- supporting semantic details reinforce the same meaning;
- scale is judged by hierarchy and readability rather than fixed occupied-area limits;
- the page does not resemble a title with one floating card, an isolated icon, a stock SaaS template, or a mostly empty unfinished canvas.

### Semantic accuracy

- correct icon meaning and business relationships;
- correct process direction;
- valid comparison objects and risk mapping;
- no fabricated policy, system, number, interface, or document.

### Cross-page continuity

- the video cover, PPT cover, and detail pages share account color roles, typography character, graphic language, and finish;
- similar modules remain visually stable;
- adjacent pages are not merely different compositions of the same idea;
- information progression is continuous;
- every page has a distinct primary communication task;
- consecutive pages do not mechanically repeat the same card arrangement, title position, or internal skeleton unless the repeated structure carries meaning;
- the deck intentionally varies page archetypes and visual weight while retaining continuity through Account Visual DNA, typography character, color logic, graphic language, and finish.

### Final-prompt purity

- every copy-ready prompt is independently executable with no assumed account or chat context;
- no account ID, account name, creator name, persona, speaker identity, `CURRENT_ACCOUNT`, `Visual DNA`, or unresolved style reference appears in a final prompt;
- target profiles, search intent, acquisition or retention rationale, workflow commentary, and other non-pixel information remain outside final prompts;
- account style is compiled into concrete colors, typography, layout, graphic language, material, depth, spacing, and finish;
- every sentence in a final prompt changes visible output or constrains generation.

## 16. Mandatory Self-Check（强制自检）

### Comprehension test

> 如果不看字幕，这一页能不能帮助观众更快理解当前口播？

If no, redesign.

### Person-removal test

> 把人物去掉以后，信息是否反而更清楚？

If yes, remove or weaken the person.

### One-second test

> 观众一秒内能不能找到这一页的重点？

If no, simplify.

### Breathing-space, dominance, and scale test

> 页面是否保留安全边距和清晰阅读空间，同时允许真正的核心数字、状态或语义关系获得足够视觉主导性？

If no, rebalance hierarchy, supporting details, and intentionally composed open space; do not solve the problem by mechanically shrinking the primary semantic structure or adding prohibitions.

### Complete-page finish test

> 这一页是否已经形成完整、可直接演示的页面，而不是“标题＋一个小卡片/图标＋大片未设计背景”？

If no, strengthen the background structure, primary semantic structure, supporting semantic details, depth treatment, alignment logic, and spatial balance without adding unsupported facts or unrelated decoration.

### Typography proportion test

> 标题、正文、标签是否符合通用字号比例与行数上限，且没有为了容纳内容而缩小正文或压缩行距？

If no, remove decoration, consolidate subordinate wording, reduce support weight, or return to Phase 1 for confirmed re-pagination.

### Duplication test

> 相邻两页是否只是换了构图，但表达同一个意思？

If yes, merge or revise their page functions.

### Cross-page rhythm test

> 连续页面是否在保持账号视觉统一的同时，使用了与各自语义任务匹配的不同页面原型和视觉重量？

If no, vary the composition archetype, title position, dominant region, or reading direction. Keep repetition only when it communicates a meaningful comparison, sequence, or recurring state.

### Account differentiation test

> 当前 Prompt 是否真的体现了 CURRENT_ACCOUNT 的视觉DNA？

If no, re-read the account visual-style file.

### Style-over-comprehension test

> 为了账号风格，是否牺牲了信息理解效率？

If yes, preserve the explanatory structure and weaken the style constraint.

### Fixed-format test

> 是否包含一张3:4视频号封面、一张独立16:9 PPT封面与全部16:9内容页，并且没有额外设置未经要求的字幕区、人物区或文字策略确认门槛？

If no, restore the fixed production defaults.

### Cover acquisition test

> 封面在视频号列表缩略图状态下，是否能让目标搜索用户立刻看到与自己相关的核心问题或结论？

If no, shorten the copy, strengthen the hierarchy, and redesign the `3:4` composition without changing the confirmed claim.

### PPT cover retention test

> 在没有额外上下文、尚未听完整段口播时，目标客户能否在第一眼确认“这与我有关”，看到一个核心变化、风险、利益或冲突，并获得继续停留的理由？

If no, revise the `IMG-01` wording, spoken-opening connection, and first-glance hierarchy before designing detail pages.

### PPT cover strength test

> `IMG-01` 是否在保持更低信息密度的同时，明显比所有细节页更有视觉冲击力？

If no, strengthen hierarchy, contrast, scale, or composition. Do not add explanatory modules, decoration, or multiple focal points.

### Cover continuity test

> 视频号封面、PPT封面和内容页是否承担不同功能，同时仍然明显属于同一账号、同一内容视觉系统？

If no, restore the account colors, typography character, graphic language, and finish while preserving the distinct acquisition, retention, and explanation roles.

### Prompt-language test

> 可直接复制的正向 Prompt 和反向限制是否为英文，而画面内必须出现的文字是否仍是精确中文原文？

If no, rewrite the prompt semantically in English and restore the exact Chinese literals.

### Chinese-text fidelity test

> 每张图允许生成的中文是否已逐字列明，并且 Prompt 禁止翻译、音译、改写或自行增字？

If no, return to the confirmed page copy and correct the exact visible literals.

### Complete-page prompt test

> 每个 Prompt 是否描述完整 PPT 页面，并明确页面功能、文案、布局、信息层级与视觉模块，而不是只描述一张独立示意图？

If no, rebuild the prompt as a complete PPT page.

### Cross-page QA test

> 全部页面是否已完成画布、视觉 DNA、文字层级、布局、语义准确性和连续性检查？

If no, run the full cross-page QA and revise failed prompts before delivery.

### Downloadable-deliverable test

> 生图执行指南是否只包含生图执行信息，没有“图片用途”、口播分段、口播原文或音频时间；剪辑分段表是否独立承担口播范围与图片编号的映射，并且最终回答没有重复展开文档正文？

If no, revise the documents and delivery response.

`COVER-01` must appear only in `AI生图执行指南.md`; it must not appear in `剪辑分段表.md` because it has no spoken-range mapping.

`IMG-01` is the first in-video PPT page. It must appear in `剪辑分段表.md` and align with the spoken opening or real opening timestamp.

---

## 17. Execution State Machine（执行状态机）

```text
SOURCE
→ ANALYZE
→ PAGE_COUNT
→ VIDEO_COVER_COPY + PPT_COVER_COPY + DETAIL_PAGE_COPY
→ WAIT_FOR_EXPLICIT_CONFIRMATION
→ VIDEO_COVER_PROMPT + PPT_COVER_PROMPT + DETAIL_PAGE_PROMPTS
→ COVER_TO_DECK_QA
→ FINAL_DOCUMENTS
```

The confirmation state must not be skipped.

---

## 18. Completion Standard（完成标准）

A qualified visual plan should make the spoken video feel:

> **3:4视频号封面负责列表与搜索获客，16:9 PPT封面负责自然流开场停留，后续16:9内容页负责解释重点、结构、差异和结论；三者共享账号视觉DNA。**

That is the target standard.
