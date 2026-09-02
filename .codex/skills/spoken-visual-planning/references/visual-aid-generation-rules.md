# Spoken PPT Page Planning and Image-Prompt Rules（口播 PPT 页面规划与 AI 生图公共规则）

## 1. Role of This File（本文件职责）

This file defines the **shared 3:4 video-cover plus 16:9 PPT-page planning, confirmation, prompt-construction, and QA mechanism** for all accounts.

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

In addition, every visual package contains one independent `3:4` WeChat Channels cover for list/search discovery. The cover is not a PPT content page and does not count toward the content-page total.

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

Use `16:9` landscape for every PPT content image and add one fixed `3:4` WeChat Channels list/search cover. Treat each content image as one complete full-frame PPT page. Use normal professional margins and do not reserve a mandatory subtitle, speaker, title, or account-information band.

Visible Chinese cover copy and PPT page copy are determined during copy planning. Do not ask the user to select a separate text-in-image strategy.

Keep prompts tool-neutral unless the user names a generation tool. Ask about resolution, assets, logos, fidelity, or tool-specific requirements only when the user's request makes them relevant.

---

## 5. Page Count and Page Planning（页数与页面规划）

If the user explicitly specifies the page/image count, follow it exactly unless a higher-priority explicit instruction conflicts:

```text
User-Specified Page Count > Automatic Decision
```

Otherwise choose `3–6` pages according to content complexity and use the minimum number that preserves the complete logic without overload.

Do not create one page per sentence. Every page must have:

1. one primary understanding target;
2. one main title hierarchy;
3. one core information module;
4. only necessary supporting information;
5. one clear visual structure;
6. a meaningful relationship to adjacent pages.

The page sequence must reorganize spoken content for PPT reading and create meaningful information progression rather than preserve source paragraph boundaries.

Before visual prompting, output `本次建议整理为 1 张3:4视频封面 + X 页16:9内容PPT。`

Present the cover first:

```markdown
# COVER｜视频号3:4封面

## 封面主标题

辅助钩子：

获客角度：

视觉建议：
```

Then present every content page in this format:

```markdown
# P1｜页面名称

## 标题

内容：

视觉建议：
```

The cover must use the strongest source-supported core point from an acquisition perspective: a pain point, decisive conclusion, relevant benefit, risk, or cognitive contrast. It must match the target user's likely search intent without misleading clickbait or unsupported promises.

The visual suggestion remains conceptual at this stage.

### Mandatory confirmation gate

After presenting the cover and all PPT page copy, stop. Wait for explicit confirmation of the cover headline, supporting hook, acquisition angle, page count, titles, sequence, wording, and conceptual visual direction. If changes are requested, revise the copy and remain at this stage. Do not generate final image prompts until the user gives unambiguous confirmation.

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

Choose the page archetype from the confirmed communication task. Do not begin from an object, illustration, or diagram type.

### 7.1 Opening Hook Page（内容开场钩子页）

Use for an opening conflict, pain point, question, or decisive conclusion. Prefer one dominant title, one short support statement or number, one strong contrast/status module, and a restrained background. This is the first `16:9` content page, not the `3:4` list/search cover.

### 7.2 Conclusion Page（结论页）

Use one large conclusion, number, or judgment supported by one restrained visual module. Do not dilute the conclusion with several equal cards.

### 7.3 Comparison Page（对比页）

Use two clearly matched states with equal visual weight and obvious differentiation. Avoid long explanations, mismatched structures, or weak contrast.

### 7.4 Process or Timeline Page（流程或时间页）

Use only when order is essential. Keep `3–5` visible stages, one direction, and one highlighted threshold. Do not convert every explanation into a process.

### 7.5 Checklist or Diagnostic Page（检查或诊断页）

Use for concrete actions or multiple checks. Prefer `2–4` aligned cards or rows with consistent hierarchy. Do not imply sequence unless one exists.

### 7.6 Status or Dashboard Page（状态或看板页）

Use neutral cards, status labels, metrics, or review modules only when they directly explain the confirmed content. Do not add random charts, fake data, or fabricated interfaces merely to look professional.

### 7.7 Decision Split Page（分支判断页）

Use when the viewer must distinguish two causes, states, or next actions. Keep the split balanced and the branch conclusions immediately readable.

### 7.8 Case Page（案例页）

Use only when the source contains a real case. Present it as a clear information composition, not a dramatic character scene or decorative business photograph.

### Legacy visual forms

Relationship maps, realistic business scenes, object-focused visuals, semi-realistic documents, and multi-arrow structures are not default page archetypes. Use them only when the confirmed meaning cannot be expressed more clearly through the professional PPT archetypes above, and keep them subordinate to the page hierarchy.

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

Do not hard-code a government-grade SaaS Dashboard style, one blue-gray/orange palette, one background, a no-people rule, a `40% left / 60% right` layout, or white rounded cards for every account. The shared workflow fixes one `3:4` acquisition cover plus `16:9` content pages; visual identity comes from the current account's authoritative visual-style file.

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

---

## 11. AI Execution Document and Prompt Structure（AI执行文档与Prompt结构）

The final `AI生图执行指南.md` must follow this order:

1. `Purpose / 目的`
2. `Execution Objective / 执行目标`
3. `Confirmed Page Structure / 已确认页面语义`
4. `Unified Visual System / 统一视觉系统`
5. `3:4 Video Cover Execution / 3:4视频封面执行`
6. `16:9 Slide Execution Sections / 16:9内容页逐页执行`
7. `Visual Continuity and Quality Check / 视觉连续性与质量检查`
8. `Final Core Rules / 最终核心规则`

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

The final cover prompt must define:

1. target viewer and search intent;
2. acquisition objective;
3. exact Chinese headline and optional supporting hook;
4. thumbnail-first reading order;
5. visual attention device;
6. relevant CURRENT_ACCOUNT Visual DNA;
7. fixed `3:4` output;
8. continuity with the 16:9 content deck;
9. cover-specific quality failures to avoid.

### Compact 3:4 Cover Prompt Template

```text
Create one professional 3:4 WeChat Channels video cover for list and search discovery.

Target viewer and search intent: [who is searching and what problem they want solved].
Acquisition objective: [why this relevant viewer should open the video].

Render exactly this Simplified Chinese cover copy and no other visible text:
Main headline: "[exact Chinese headline]"
Supporting hook: "[exact Chinese hook]" or None

Design for small-thumbnail readability. Make the main headline the first focal point,
followed by [key number / status conflict / decisive conclusion / benefit or risk cue].
Use a strong but professional vertical 3:4 composition; do not crop a 16:9 slide.

Apply the CURRENT_ACCOUNT Visual DNA: [relevant account-specific descriptors].
Use the same color roles, typography character, icon/card language, and finish as the
16:9 content deck, with slightly stronger contrast and emphasis for acquisition.

High-resolution, visually distinctive, credible, relevant, uncluttered, and readable
at thumbnail size. No unsupported promises, misleading urgency, or unrelated imagery.
```

Every slide section must contain:

```markdown
## IMG-01

### Rule Logic
[Concise English execution rules]

### 中文语义
[Business meaning and page intent]

### Final Image Prompt
[One self-contained English prompt containing exact Chinese literals]

### Avoid
[Concise English page-specific negative constraints]
```

Each final prompt must define:

1. slide role;
2. one viewer-understanding outcome;
3. exact required Chinese copy;
4. page archetype;
5. layout and reading order;
6. information hierarchy;
7. key emphasis;
8. relevant CURRENT_ACCOUNT Visual DNA;
9. fixed `16:9` complete-page output;
10. quality requirements and page-specific failures to avoid.

### Compact Tool-Neutral English Prompt Template

```text
Create one complete, professional 16:9 PPT slide as part of the same deck.

Slide role: [hook / conclusion / comparison / process / checklist / status / decision / case].
The viewer should immediately understand: [one business outcome].

Render exactly this Simplified Chinese PPT copy and no other visible text:
Title: "[exact Chinese title]"
Supporting copy: "[exact Chinese string]", "[exact Chinese string]"

Use [page archetype and visual module].
Layout: [clear page-specific grid and reading order].
Information hierarchy: [title > conclusion > support > visual module].
Emphasize: [key term, number, contrast, or status].

Apply the CURRENT_ACCOUNT Visual DNA: [relevant account-specific descriptors].
Maintain the same deck-level color roles, typography hierarchy, UI/card language,
icon style, spacing rhythm, and finish as the other slides.

High-resolution, presentation-ready, sufficient whitespace, precise alignment,
clear focal point, and complete PPT composition.
```

Keep prompts tool-neutral until the user names a generation tool. Do not promise exact cross-slide pixel identity unless a real reference slide, template, or asset is supplied. Do not place spoken excerpts, audio timing, or editing metadata inside the execution guide.

---

## 12. Negative Prompt Architecture（反向提示词架构）

Every final prompt must contain three negative layers. Deliver all copy-ready negative constraints in English. If the confirmed tool has a separate negative-prompt field, place them there. Otherwise append them to the positive prompt as a concise English `Avoid:` clause.

### 12.1 Universal Quality Negatives（公共质量反向词）

Define once at deck level:

```text
low resolution, blur, malformed layout, clutter, weak information hierarchy,
unreadable or garbled Chinese, invented text or numbers, fabricated official interfaces,
watermarks, incorrect logos, cropped important content, meaningless decorative UI,
insufficient whitespace, standalone illustration composition, generic flowchart styling.
```

These are quality / communication constraints.

### 12.2 Account-Specific Style Negatives（账号风格反向词）

Read from:

```text
账号视觉风格.md
```

These are NOT global rules.

### 12.3 Page-Specific Negatives（页面专属反向词）

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
- avoid irrelevant decorative imagery;
- avoid sensational clickbait, unsupported promises, and fabricated outcomes;
- avoid breaking the CURRENT_ACCOUNT visual identity.

---

## 13. PPT Text Handling（PPT页面文字处理）

Visible Chinese copy is determined in the confirmed cover and PPT page copy. It is not a separate user-confirmation setting.

For the `3:4` cover, prefer one dominant headline and zero or one short supporting hook. For each `16:9` content page, prefer one title and `1–3` short supporting strings. List every permitted string verbatim in the English prompt.

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
- preserve confirmed numbers, punctuation, capitalization, and symbols exactly;
- add `no English text, no extra characters, no garbled Chinese text, no invented text, no invented numbers` to the English negative constraints.

Never translate, transliterate, paraphrase, or invent page text, policy names, tax rates, numbers, English labels, or unauthorized small print merely to complete the layout.

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

After the cover prompt and all content-page prompts are drafted, run one complete cover-to-deck QA pass and revise failed prompts before output.

### Canvas

- `COVER-01` uses fixed `3:4`;
- every content page uses fixed `16:9`;
- consistent resolution when specified;
- normal professional page margins without a mandatory reserved band.

### Acquisition cover

- the cover uses the strongest confirmed acquisition angle;
- the main headline is readable at list/search thumbnail size;
- the composition was designed for `3:4`, not cropped from `16:9`;
- the cover earns attention through relevance, hierarchy, and contrast rather than clickbait;
- the cover remains recognizably part of the same account visual system as the content deck.

### Visual DNA

- consistent background and color roles;
- consistent UI, card, and icon language;
- consistent material and rendering language.

### Typography

- consistent title hierarchy;
- consistent body-text logic;
- consistent label system;
- consistent emphasis behavior.

### Layout

- no page is overfilled;
- cards are not crowded;
- sufficient whitespace;
- clear primary focal point;
- important elements are not too close to edges;
- no meaningless decoration.

### Semantic accuracy

- correct icon meaning and business relationships;
- correct process direction;
- valid comparison objects and risk mapping;
- no fabricated policy, system, number, interface, or document.

### Cross-page continuity

- the cover and content pages share account color roles, typography character, graphic language, and finish;
- similar modules remain visually stable;
- adjacent pages are not merely different compositions of the same idea;
- information progression is continuous;
- every page has a distinct primary communication task.

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

### Duplication test

> 相邻两页是否只是换了构图，但表达同一个意思？

If yes, merge or revise their page functions.

### Account differentiation test

> 当前 Prompt 是否真的体现了 CURRENT_ACCOUNT 的视觉DNA？

If no, re-read the account visual-style file.

### Style-over-comprehension test

> 为了账号风格，是否牺牲了信息理解效率？

If yes, preserve the explanatory structure and weaken the style constraint.

### Fixed-format test

> 是否包含一张3:4封面与全部16:9内容PPT，并且没有额外设置未经要求的字幕区、人物区或文字策略确认门槛？

If no, restore the fixed production defaults.

### Cover acquisition test

> 封面在视频号列表缩略图状态下，是否能让目标搜索用户立刻看到与自己相关的核心问题或结论？

If no, shorten the copy, strengthen the hierarchy, and redesign the `3:4` composition without changing the confirmed claim.

### Cover continuity test

> 封面是否比内容页更有注意力强度，同时仍然明显属于同一账号、同一内容视觉系统？

If no, restore the account colors, typography character, graphic language, and finish while keeping stronger cover emphasis.

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

---

## 17. Execution State Machine（执行状态机）

```text
SOURCE
→ ANALYZE
→ PAGE_COUNT
→ COVER_COPY + PAGE_COPY
→ WAIT_FOR_EXPLICIT_CONFIRMATION
→ COVER_PROMPT + PAGE_PROMPTS
→ COVER_TO_DECK_QA
→ FINAL_DOCUMENTS
```

The confirmation state must not be skipped.

---

## 18. Completion Standard（完成标准）

A qualified visual plan should make the spoken video feel:

> **3:4封面在搜索与列表路径中吸引正确的目标用户，16:9专业PPT页面在观看过程中呈现重点、结构、差异和结论；两者共享账号视觉DNA。**

That is the target standard.
