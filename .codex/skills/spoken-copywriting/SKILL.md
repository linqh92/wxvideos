---
name: spoken-copywriting
description: Generate finalized WeChat Video Account spoken-camera scripts from a confirmed topic. Inherit the locked account's positioning, audience, persona, business context, factual boundaries, tone, and conversion goal. Use for 口播、真人口播、口播稿, or when the confirmed topic is routed to spoken content. Do not use for topic planning, text-broadcast copywriting, archiving, or visual production.
---

# WeChat Video Account Spoken Copywriting（微信视频号口播文案生成）

## Trigger

Use only when the user requests 口播、真人口播、口播稿 or spoken-camera explanation from a confirmed topic, or when root routing resolves the confirmed topic to `CONTENT_FORMAT=spoken`.

Do not use for topic planning, text-broadcast copy, visual production, publication state changes, or archiving.

## Required Input

- A confirmed topic or a clear topic supplied directly by the user;
- The requested title, script, complete package, length, tone, or rewrite direction;
- `CURRENT_ACCOUNT` and `CONTENT_FORMAT=spoken` resolved under root `AGENTS.md`.

## Required Context

Account selection, isolation, content-format routing, and stage boundaries follow root `AGENTS.md`.

Read and obey:

1. `shared/rules/copywriting-common-rules.md` for account context, factual boundaries, audience language, persona, titles, endings, trust, cases, common quality control, and output discipline;
2. `references/chinese-spoken-naturalness.md` for spoken-only Chinese naturalness.

Do not apply the naturalness reference to `text-broadcast-copywriting`. If required account context or either rule file is missing, report the blocking path and do not borrow another account's context.

## Unique Logic

### Medium Objective（载体目标）

This Skill writes content that should work when heard once from a real person.

Optimization priority:

> Fact accuracy（事实准确）  
> → Natural human speech（像真人在说）  
> → Auditory clarity（听得懂）  
> → Retention（愿意继续听）  
> → Reasoning comprehension（听懂为什么）  
> → Judgment credibility（相信判断有依据）  
> → Persona recognizability（听得出是谁）  
> → Conversion readiness（愿意进一步了解）

Subtitles may assist, but MUST NOT determine sentence structure.

Do NOT write:
- a longer text-broadcast post;
- an article cut into short lines;
- a report or course outline;
- an official notice;
- a mechanically expanded AI outline;
- a “口语化文章” that still sounds written when read aloud.

Principle:

> **口播不是把文章改短句，而是直接按人说话的方式生成。**

---

### Core Content Requirement（内容核心）

Each piece should stay centered on one meaningful problem.

Internally identify:
- one central question;
- one core judgment;
- the reasoning that makes the judgment credible;
- the condition that may change the judgment;
- the most useful thing the audience should know or check afterward.

These elements are semantic requirements, NOT mandatory visible sections.

The final script does NOT need to explicitly present all of them as separate paragraphs.

Principle:

> **逻辑要完整，表达不必工整。**

---

### Length Modes（内容幅度）

Priority:

> User-specified length  
> → Reference length  
> → Topic complexity  
> → Default mode

#### Quick Spoken（快速口播）
Approximately 180–280 Chinese characters.

Use for one simple misconception, one direct judgment, one common mistake, or one small decision problem.

#### Standard Spoken（标准口播）
DEFAULT. Approximately 280–450 Chinese characters.

Use when the topic needs a short explanation, two or three meaningful variables, one short case, or a decision comparison.

#### Deep Spoken（深度口播）
Approximately 450–750 Chinese characters.

Use ONLY when the topic genuinely requires multiple conditions, case development, policy interpretation, a business chain, or multiple decision paths.

Do NOT choose a longer mode merely because more source material exists.

Do NOT fill the target length with background, repeated warnings, or redundant conclusions.

---

### Information Capacity（单篇信息容量）

Default upper bound:
- 1 central problem;
- 1 core conclusion;
- 1–4 supporting reasoning elements as actually needed;
- necessary conditions or exceptions;
- at most 1 main case OR 1 main comparison;
- 1 useful final direction.

The `1–4` range is a capacity limit, NOT a requirement to produce a list.

Do NOT create “三点 / 四点” merely because a template expects them.

---

### Hidden Reasoning Skeleton（隐藏判断骨架）

Before wording the script, internally determine:

1. What is the single central question?
2. What does the audience already know?
3. What do they not know or underestimate?
4. What is the strongest valid information gap?
5. What is the core judgment?
6. Why does it hold?
7. Which variables materially determine the result?
8. Which condition could change the conclusion?
9. Does the topic genuinely need a case, comparison, or chain explanation?
10. What best demonstrates professional judgment?
11. What should the audience know how to check afterward?
12. What must not be overstated?
13. How would this specific persona naturally explain it face-to-face?

Do NOT expose this checklist.
Do NOT map checklist order directly into paragraph order.

---

### Structure Modes Are Internal Only（结构模式仅用于后台）

Possible internal reasoning structures include:

#### Judgment Explanation（判断解释型）
> Problem → Judgment → Why → Variables → Conditions → Check direction

#### Cognitive Correction（认知纠偏型）
> Common belief → Correction → Why it fails → Better judgment → Conditions

#### Case Breakdown（案例拆解型）
> Result / conflict → What happened → Break point → Why → What to check

#### Decision Comparison（决策比较型）
> Two choices → Core difference → Different outcomes → Applicable conditions

#### Chain Explanation（链条解释型）
> Starting behavior → Intermediate change → Downstream impact → Key break point

#### Mechanism Explanation（机制拆解型）
> Surface phenomenon → Underlying mechanism → Key steps → Why the result appears

#### Event / Policy Impact（事件或规则影响型）
Use ONLY after current verification.

> What happened → Who is affected → What changed → What did not change → Practical impact

These structures are reasoning aids.
They MUST NOT automatically become visible sequential sections in the final script.

If the final wording reads like a template because it follows the structure too neatly, rewrite it.

---

### Opening（开场）

The opening must create immediate relevance, but it does NOT need a stock hook phrase.

Possible forms:
- direct judgment;
- concrete action;
- one number;
- familiar scene;
- visible contradiction;
- real question;
- consequence already happening.

Prefer the current persona's natural first sentence over a universal short-video formula.

Do NOT default to:

> 大家好。  
> 今天跟大家分享一下。  
> 很多朋友问我。  
> 注意了。  
> 重点来了。  
> 跟你说个扎心的事实。  
> 一定要看完。

These are not absolute banned words; they are banned as automatic hooks.

Spoken titles follow the shared title baseline and may foreground a direct audience question, decision conflict, case result, hidden reason, or a condition that changes the conclusion. The title must promise only what the script supports.

---

### Conclusion Timing（结论位置）

Give an early directional judgment when the facts allow it.

Do NOT hide the answer until the end merely to create suspense.

When a critical condition materially changes the answer, the opening may give only a conditional direction.

Natural:

> 这笔先别急着报，至少把供应商和付款对一下。  
> 如果你这单走的是另外一种模式，那判断还得再分开。

---

### Explanation Logic（解释逻辑）

Keep professional logic underneath and audience language on the surface.

Useful internal relations include:

> What happens → Why → What it affects

> Behavior → Change → Result

> Condition → Judgment → Consequence

But final Chinese may express these relations without explicit connectors or perfectly complete sentences.

When a professional term is necessary:

> **先说发生了什么，再补专业上叫什么。**

Do NOT use terminology as a substitute for explanation.

---

### Speaking Units（说话单元）

Generate the script as speaking units rather than article sentences.

A speaking unit may be:
- a short judgment;
- a normal explanation;
- a half-sentence supplement;
- a question immediately answered;
- a condition added afterward;
- a brief correction;
- a concrete object or number returned to for clarity.

Allow controlled irregularity when meaning remains clear.

Examples:

> 钱是收到了。收哪儿了？这个先看。

> 票有。能不能抵，得看这票对应的到底是哪笔业务。

> 这个做法不一定错。准确一点讲，是不能只凭现在这一个条件就下结论。

---

### Auditory Clarity（听觉理解）

Every key sentence must remain understandable when heard once without subtitles.

Prefer:
- clear objects;
- concrete nouns;
- understandable cause/contrast/condition relations;
- repeating the key object when a pronoun would become ambiguous;
- sentence lengths that vary naturally.

Do NOT reduce auditory clarity to “short sentences”.

A longer sentence is acceptable if a real person can say it naturally and the listener can follow it once.

Avoid:
- nested clauses;
- definition chains;
- abstract noun stacking;
- written-language inversion;
- long unexplained enumerations;
- sentences that are grammatically correct but unnatural in face-to-face Chinese.

---

### Natural Chinese Speech（中式真人口语）

Follow `references/chinese-spoken-naturalness.md`.

Important permissions:
- natural subject omission;
- half-sentence supplements;
- afterthought conditions;
- light self-repair;
- functional keyword repetition;
- natural discourse particles;
- mixed sentence length;
- direct sentence-to-sentence continuation without forced connectors.

Important restrictions:
- no fixed character limit per sentence;
- no forced `你 / 大家 / 咱们` quota;
- no universal hook/transition/ending phrase bank;
- no deliberate grammatical disorder;
- no translationese disguised as polished Chinese.

---

### Script Formatting（口播稿格式）

Deliver directly usable spoken copy.

Default:
- natural spoken paragraphs;
- paragraph breaks based on speaking sense, not a fixed number of sentences;
- punctuation for rhythm;
- no forced one-sentence-per-line formatting;
- no text-broadcast 7–15-character line rule;
- no artificial subtitle segmentation.

Do NOT add performance or production markup by default, including:
- `[停顿]`;
- `[重音]`;
- `[看镜头]`;
- `[字幕]`;
- `[BGM]`;
- shot or editing instructions.

This Skill writes copy, not directing notes.

---

## Quality Gate

### Mandatory Reduction Pass（强制删减）

After the factual draft is correct, remove in this order:

1. repeated conclusions;
2. background that does not affect judgment;
3. unnecessary definitions;
4. replaceable jargon;
5. repeated emotional warnings;
6. connectors with no listening function;
7. secondary examples;
8. second or later CTA;
9. persona performance with no informational function;
10. polished summary sentences that only repeat what the audience already understood.

Keep a unit only if removing it would lose a fact, reason, condition, judgment, case function, listening clarification, or necessary transition.

After reduction, run one naturalness rewrite pass from `references/chinese-spoken-naturalness.md` without changing facts or conclusions.

---

### Spoken Quality Control（口播专项质检）

Rewrite if ANY applies:
- opening has no concrete relevance;
- script is merely a longer text-broadcast draft;
- central question is unclear;
- multiple unrelated problems are developed;
- no core judgment exists;
- judgment exists but reasoning is missing;
- multiple conclusions are stacked;
- script sounds like an article, report, course outline or policy narration;
- sentences are difficult to say naturally;
- pronouns create listening ambiguity;
- too much background appears before the core issue;
- length increases without increasing useful judgment;
- ending introduces a new topic.

---

### Human Speech Test（真人朗读检查）

Before final output, mentally perform these checks:

#### Face-to-face test
> **如果客户坐在面前，这个人真的会这样说吗？**

#### No-subtitle test
> **不看字幕，只听一遍，核心逻辑能不能跟上？**

#### De-copywriting test
> **这是在聊天解释问题，还是在念一篇“很口语”的文案？**

#### Over-completeness test
> **是不是为了显得完整，强行加了总结、升华、第三点或第二个案例？**

#### Persona identity test
> **遮掉账号名以后，语言和判断方式还能不能看出是这个人？**

If any answer is weak, rewrite once before output.

---

## Output

Follow the user's request strictly.

### Titles only
Output ONLY title options.

### Spoken copy only
Output ONLY the finalized spoken script.

### Complete spoken package
Default output ONLY:
1. three clearly different title directions;
2. one standard/search-recognition title;
3. one short title;
4. final spoken script.

Do NOT expose structure mode, scoring, risk scoring, creative process, source explanation, shot list, visual plan, editing plan, or archive actions unless requested.

---

## User Override

If the user requests a specific length, duration, tone, depth, case emphasis, or structure, follow it within factual, account, platform, and safety boundaries.

If the user requests conversion between:

> `text_broadcast` ↔ `spoken`

do NOT re-plan the topic. Rewrite the same confirmed topic for the target medium.

When converting TO `spoken`, apply this Skill and the naturalness reference.
When converting TO `text_broadcast`, do NOT carry spoken-only language mechanics into the text-broadcast Skill unless that Skill requires them.

---

## Stop

After delivering the requested title, spoken script, or complete spoken package, stop. Do not generate visual plans, shot lists, editing instructions, video files, publication-state changes, or archive writes; visual support requires a separate explicit request routed by root `AGENTS.md`.
