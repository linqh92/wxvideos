---
name: spoken-copywriting
description: Generate finalized WeChat Video Account spoken-camera scripts from a confirmed topic. Inherit the locked account's positioning, audience, persona, business context, factual boundaries, tone, and conversion goal. Use for 口播、真人口播、口播稿, or when the confirmed topic is routed to spoken content. Do not use for topic planning, text-broadcast copywriting, archiving, or visual production.
---

# WeChat Video Account Spoken Copywriting（微信视频号口播文案生成）

## 1. Scope（职责范围）

Generate finalized spoken-camera content ONLY from a confirmed topic.

May output:
- Title（标题）
- Short title（短标题）
- Spoken script（口播正文）
- Complete spoken package（完整口播文案）
- A requested length, version, tone, or rewrite direction

Do NOT:
- re-plan topics;
- switch to unrelated topics;
- generate text-broadcast copy unless requested;
- mark content as published;
- archive or update history;
- produce visuals, shot lists, editing plans, or video files.

After delivering the requested copy, STOP.

---

## 2. Required Context（必读上下文）

Determine `CURRENT_ACCOUNT` exactly from repository-root `AGENTS.md`, then enforce Account Context Lock.

Read and obey, in order:

1. `shared/rules/copywriting-common-rules.md`
2. `accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号基本定位.md`
3. `accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号人设与文风.md`
4. `.codex/skills/spoken-copywriting/references/chinese-spoken-naturalness.md`

The common rules control shared factual and copywriting boundaries.
The account files control who is speaking, to whom, and from what business position.
The naturalness reference controls ONLY how valid content becomes natural Chinese speech.

Do NOT apply the spoken naturalness reference to `text-broadcast-copywriting`.

If any required file is missing or unreadable, report the blocking path. Do NOT borrow context from another account.

---

## 3. Medium Objective（载体目标）

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

## 4. Core Content Requirement（内容核心）

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

## 5. Trust Building（信任建立）

Build trust by demonstrating judgment capability, NOT self-promotion.

Prioritize:
- identifying the real variable behind the surface problem;
- explaining why the result appears;
- distinguishing materially different situations;
- stating which condition changes the answer;
- showing what should be checked first;
- acknowledging real uncertainty;
- giving a useful decision direction.

Do NOT rely on:
- repeated self-praise;
- unsupported experience claims;
- fabricated client counts or cases;
- “相信我” authority language;
- empty insider/expert posturing.

> **专业感来自判断过程，不来自术语密度。**

---

## 6. Length Modes（内容幅度）

Priority:

> User-specified length  
> → Reference length  
> → Topic complexity  
> → Default mode

### Quick Spoken（快速口播）
Approximately 180–280 Chinese characters.

Use for one simple misconception, one direct judgment, one common mistake, or one small decision problem.

### Standard Spoken（标准口播）
DEFAULT. Approximately 280–450 Chinese characters.

Use when the topic needs a short explanation, two or three meaningful variables, one short case, or a decision comparison.

### Deep Spoken（深度口播）
Approximately 450–750 Chinese characters.

Use ONLY when the topic genuinely requires multiple conditions, case development, policy interpretation, a business chain, or multiple decision paths.

Do NOT choose a longer mode merely because more source material exists.

Do NOT fill the target length with background, repeated warnings, or redundant conclusions.

---

## 7. Information Capacity（单篇信息容量）

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

## 8. Hidden Reasoning Skeleton（隐藏判断骨架）

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

## 9. Structure Modes Are Internal Only（结构模式仅用于后台）

Possible internal reasoning structures include:

### Judgment Explanation（判断解释型）
> Problem → Judgment → Why → Variables → Conditions → Check direction

### Cognitive Correction（认知纠偏型）
> Common belief → Correction → Why it fails → Better judgment → Conditions

### Case Breakdown（案例拆解型）
> Result / conflict → What happened → Break point → Why → What to check

### Decision Comparison（决策比较型）
> Two choices → Core difference → Different outcomes → Applicable conditions

### Chain Explanation（链条解释型）
> Starting behavior → Intermediate change → Downstream impact → Key break point

### Mechanism Explanation（机制拆解型）
> Surface phenomenon → Underlying mechanism → Key steps → Why the result appears

### Event / Policy Impact（事件或规则影响型）
Use ONLY after current verification.

> What happened → Who is affected → What changed → What did not change → Practical impact

These structures are reasoning aids.
They MUST NOT automatically become visible sequential sections in the final script.

If the final wording reads like a template because it follows the structure too neatly, rewrite it.

---

## 10. Opening（开场）

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

---

## 11. Conclusion Timing（结论位置）

Give an early directional judgment when the facts allow it.

Do NOT hide the answer until the end merely to create suspense.

When a critical condition materially changes the answer, the opening may give only a conditional direction.

Natural:

> 这笔先别急着报，至少把供应商和付款对一下。  
> 如果你这单走的是另外一种模式，那判断还得再分开。

---

## 12. Explanation Logic（解释逻辑）

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

## 13. Speaking Units（说话单元）

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

## 14. Auditory Clarity（听觉理解）

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

## 15. Natural Chinese Speech（中式真人口语）

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

## 16. Persona Expression（人物表达）

Persona MUST be inherited from `账号人设与文风.md`.

The persona must materially affect:
- what the speaker notices first;
- the order in which the speaker thinks;
- how directly the speaker judges;
- how much explanation is given;
- sentence rhythm;
- question habit;
- afterthought habit;
- uncertainty language;
- humor/teasing style;
- analogy style;
- ending posture.

Do NOT reduce persona to catchphrases or vocabulary.

Principle:

> **人物感先来自“怎么看”，再来自“怎么说”。**

---

## 17. Professional Depth（专业深度）

Professional depth means:
- better distinction;
- better causal explanation;
- better condition explanation;
- better judgment;
- better decision guidance.

It does NOT mean:
- more terminology;
- more policy names;
- more definitions;
- more background;
- more industry jargon.

Remove detail that does not improve audience judgment.

---

## 18. Conditions and Exceptions（条件与例外）

Prioritize conditions that change:
- the conclusion;
- applicable audience;
- result;
- risk level;
- recommended action.

Secondary conditions may be compressed.

Do NOT hide a critical condition to strengthen the opening.

If the answer depends on missing information, say what must be checked instead of inventing certainty.

Natural qualification is encouraged:

> 也不能直接说一定不行，先看你这笔业务到底怎么走。

---

## 19. Case Rules（案例规则）

Cases may come from:
1. user-provided material;
2. verified source material;
3. authorized project material;
4. clearly labeled hypothetical examples.

Do NOT fabricate:
- clients;
- consultation conversations;
- amounts;
- penalties;
- business outcomes.

A case exists to clarify judgment, not to decorate the script.

---

## 20. Emotional Expression（情绪表达）

Follow `copywriting-common-rules.md`.

For spoken content, prefer emotion generated by:
- real consequences;
- contrast;
- case progression;
- judgment conflict;
- opportunity loss;
- hidden variables;
- decision uncertainty;
- chain amplification.

Do NOT rely on shouting language, repeated exclamation, threats, artificial urgency, or stacked high-pressure phrases.

Natural spoken content may be calmer than text-broadcast content while building stronger trust.

---

## 21. Humor and Rhetorical Devices（幽默与修辞）

Humor, rhetorical questions, analogies and teasing are optional tools.

Use them only when:
- the persona naturally uses them;
- the topic contains a real contradiction or useful image;
- they improve understanding or memorability.

Do NOT fill quotas.
Do NOT add a joke simply because the persona is “幽默”.
Do NOT turn every strong statement into a rhetorical question.

---

## 22. Title Rules（标题）

Follow the common title rules and the current persona file.

Spoken titles may favor:
- a direct owner-side question;
- cognitive conflict;
- decision conflict;
- a case result;
- a hidden reason;
- a condition that changes a common conclusion.

The title MUST promise only what the script supports.

---

## 23. Ending（结尾）

The ending should stop when the reasoning has delivered enough value.

Possible endings:
- final judgment;
- one check direction;
- one decision principle;
- one practical action;
- one unresolved condition that still needs real information;
- one persona-consistent closing line.

Do NOT force:
- summary elevation;
- a question;
- follow/share/save prompts;
- comment-keyword CTA;
- contact or traffic diversion;
- service promise.

A script may end simply:

> 这单先把付款和开票对上，别急着往后算。

---

## 24. Script Formatting（口播稿格式）

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

## 25. Mandatory Reduction Pass（强制删减）

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

---

## 26. Naturalness Rewrite Pass（真人化重写）

After reduction, run ONE dedicated natural-Chinese rewrite pass.

Rewrite if ANY applies:
- it sounds like an article read aloud;
- it sounds like English reasoning translated into Chinese;
- three or more consecutive sentences have similar length or structure;
- every sentence is grammatically complete and polished;
- the script relies on stock short-video phrases;
- abstract nouns replace concrete actions;
- connectors make the script sound like a report;
- the persona's speaking habits are not audible;
- a real person would rarely say a sentence this way face-to-face.

Do NOT change facts or conclusions during this pass.

---

## 27. Quality Control（质量控制）

Rewrite if ANY applies:
- opening has no concrete relevance;
- opening is emotion-only;
- script is merely a longer text-broadcast draft;
- central question is unclear;
- multiple unrelated problems are developed;
- no core judgment exists;
- judgment exists but reasoning is missing;
- multiple conclusions are stacked;
- terminology replaces explanation;
- a conclusion-changing condition is omitted;
- script sounds like an article, report, course outline or policy narration;
- sentences are difficult to say naturally;
- pronouns create listening ambiguity;
- too much background appears before the core issue;
- case content is fabricated;
- trust relies mainly on self-praise;
- persona is reduced to catchphrases;
- emotion exceeds factual support;
- length increases without increasing useful judgment;
- ending introduces a new topic;
- CTA conflicts with account or platform boundaries.

---

## 28. Human Speech Test（真人朗读检查）

Before final output, mentally perform these checks:

### Face-to-face test
> **如果客户坐在面前，这个人真的会这样说吗？**

### No-subtitle test
> **不看字幕，只听一遍，核心逻辑能不能跟上？**

### De-copywriting test
> **这是在聊天解释问题，还是在念一篇“很口语”的文案？**

### Over-completeness test
> **是不是为了显得完整，强行加了总结、升华、第三点或第二个案例？**

### Persona identity test
> **遮掉账号名以后，语言和判断方式还能不能看出是这个人？**

If any answer is weak, rewrite once before output.

---

## 29. Internal Scoring（内部评分）

Do NOT expose unless requested.

### Information Value: 1–5
Useful information gap, judgment, or explanation.

### Auditory Clarity: 1–5
Understandable without subtitles.

### Reasoning Quality: 1–5
The audience understands why the conclusion holds.

### Natural Chinese Speech: 1–5
Sounds like real face-to-face Simplified Chinese, not translated or written prose.

### Persona Judgment Consistency: 1–5
The speaker notices and judges the problem in the expected way.

### Persona Voice Distinctiveness: 1–5
The wording and rhythm are recognizably this persona rather than generic “professional口播”.

### Trust Building: 1–5
The script demonstrates useful judgment rather than self-promotion.

### Retention Potential: 1–5
The opening and body provide valid reasons to keep listening.

### Conversion Capability: 1–5
The audience can identify relevance, perceive capability, and reasonably want further understanding.

### Platform Risk: Low / Medium / High
Use the common rules for fact risk, absolute claims, manufactured fear, authority misrepresentation, interaction inducement, traffic diversion, and service promises.

If any numeric score is below 3, rewrite first.

---

## 30. Output Modes（输出模式）

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

## 31. User Override（用户优先）

If the user requests a specific length, duration, tone, depth, case emphasis, or structure, follow it within factual, account, platform, and safety boundaries.

If the user requests conversion between:

> `text_broadcast` ↔ `spoken`

do NOT re-plan the topic. Rewrite the same confirmed topic for the target medium.

When converting TO `spoken`, apply this Skill and the naturalness reference.
When converting TO `text_broadcast`, do NOT carry spoken-only language mechanics into the text-broadcast Skill unless that Skill requires them.

---

## 32. Final Principles（最终原则）

> **口播不是加长版短文。**

> **口播不是把文章拆成短句。**

> **一条口播只解决一个中心问题。**

> **结构负责把逻辑想清楚，不负责把成稿写整齐。**

> **能直接给方向，就不要故意拖结论。**

> **能解释为什么，就不要只重复结论。**

> **能用具体动作讲清楚，就不要先上抽象术语。**

> **允许真实说话里的省略、补一句和轻微修正，但不能制造混乱。**

> **专业感来自区分、解释和判断。**

> **人物感来自思考顺序、判断习惯和说话节奏，不来自口头禅。**

> **用户只听不看，也应理解核心逻辑。**

> **最终先像真人，再像文案。**
