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

1. `shared/rules/acquisition-and-fact-framing.md` for information roles, source boundaries, verification decisions, and acquisition preservation;
2. `shared/rules/copywriting-common-rules.md` for account context, audience language, persona, titles, endings, trust, cases, common quality control, and output discipline;
3. `references/chinese-spoken-naturalness.md` for spoken-only Chinese naturalness.

Do not apply the naturalness reference to `text-broadcast-copywriting`. If required account context or either rule file is missing, report the blocking path and do not borrow another account's context.

## Unique Logic

### Medium Objective（载体目标）

This Skill writes content that should work when heard once from a real person.

Optimization priority:

> Legal / platform / business boundaries（合规边界）
> → Information-role fidelity（信息身份准确）
> → Acquisition strength（获客强度）
> → Reliable professional judgment（专业结论可靠）
> → Natural human speech（像真人在说）  
> → Auditory clarity（听得懂）  
> → Retention（愿意继续听）  
> → Reasoning comprehension（听懂为什么）  
> → Judgment credibility（相信判断有依据）  
> → Persona recognizability（听得出是谁）  
> → Conversion readiness（愿意进一步了解）

`Conversion readiness` is an outcome of useful content, credible judgment, and audience relevance. It is NOT a mandatory visible section, consultation gap, CTA, or ending pattern in every script.

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
- the exact central question the audience needs answered;
- whether the facts support a direct conclusion, branch conclusions, or only a precise information gap;
- the default core judgment under the stated facts;
- the reasoning that makes the judgment credible;
- the condition that may change the judgment;
- the practical audience result;
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

Length modes define practical content capacity, NOT a target that should be filled.

#### Quick Spoken（快速口播）

Usually up to approximately 280 Chinese characters.

Use for one simple misconception, one direct judgment, one common mistake, or one small decision problem.

A complete answer may be substantially shorter. Do NOT add secondary conditions, general checks, extra examples, or background merely to approach the upper bound.

#### Standard Spoken（标准口播）

DEFAULT. Usually up to approximately 450 Chinese characters.

Use when the topic needs a short explanation, two or three genuinely conclusion-relevant variables, one short case, or a decision comparison.

A script may stay below the common 280–450 range when the topic is already fully explained.

#### Deep Spoken（深度口播）

Usually up to approximately 750 Chinese characters.

Use ONLY when the topic genuinely requires multiple conclusion-changing conditions, case development, policy interpretation, a business chain, or multiple decision paths.

Do NOT choose a longer mode merely because more source material exists.

Do NOT fill available length with background, repeated warnings, generic professional checks, or redundant conclusions.

---

### Information Capacity（单篇信息容量）

Default upper bound:
- 1 central problem;
- 1 core conclusion;
- only the supporting reasoning elements actually needed;
- necessary conclusion-changing conditions or exceptions;
- at most 1 main case OR 1 main comparison;
- 1 useful final direction when the topic naturally needs one.

Do NOT create “三点 / 四点” merely because a template expects them.

#### Topic-local Reasoning（本题局部推理）

Use the full professional knowledge base internally, but expose only what this specific topic needs.

The final spoken script should contain only:
- facts that affect this topic;
- variables that materially change this topic's conclusion;
- conditions necessary to keep the conclusion accurate;
- reasoning needed to make the judgment understandable and credible;
- practical audience impact that follows from the current topic.

Broader professional frameworks, recurring diagnostic systems, standard checklists, triads, quadrants, “closed-loop” models, or industry-wide verification routines are internal reasoning tools by default.

Do NOT surface them merely:
- to make the answer look complete;
- to demonstrate professionalism;
- because they are commonly used in the industry;
- because they appeared in previous successful scripts;
- because the account often talks about them.

A recurring professional framework may appear ONLY when it directly explains or changes the current topic's conclusion.

Principle:

> **后台可以判断得完整，前台只说这个题真正需要说的话。**

---

### Hidden Reasoning Skeleton（隐藏判断骨架）

Before wording the script, internally determine:

1. What is the single central question?
2. What does the audience already know?
3. What do they not know or underestimate?
4. What is the strongest valid information gap?
5. What is the core judgment?
6. Why does it hold?
7. Which variable or variables materially determine this result?
8. Which condition could actually change the conclusion?
9. What information is necessary for this topic, and what professional knowledge can stay internal?
10. Does the topic genuinely need a case, comparison, mechanism, or branch explanation?
11. What best demonstrates professional judgment without broadening the topic?
12. What must not be overstated?
13. How would this specific persona naturally explain this exact issue face-to-face?
14. Can the audience restate the answer in one sentence after hearing it once?
15. Is the draft giving an answer or expanding into a general checklist?
16. Is a supported conclusion being delayed or weakened without a factual reason?

Do NOT expose this checklist.
Do NOT map checklist order directly into paragraph order.

---

### Structure Modes Are Internal Only（结构模式仅用于后台）

Structure must emerge from the current topic's factual relationship, not from a preselected visible template.

Internally, the topic may require:
- a judgment;
- a correction of a misconception;
- a case;
- a comparison;
- a causal chain;
- a mechanism;
- an event or policy impact;
- or another structure that fits the actual information.

Do NOT select a structure merely to create variety.
Do NOT force every topic through the same sequence of hook, conclusion, reason, conditions, self-check, and CTA.
Do NOT treat internal reasoning order as final speaking order.

If one sentence is enough to establish the judgment, do not create an extra section.
If one condition changes the answer, explain that condition; do not add unrelated conditions for completeness.
If the final wording reads like a reusable template instead of a person explaining this specific topic, rewrite it.

Principle:

> **结构跟着问题走，不跟着 Skill 走。**

---

### Reference Style Calibration（参考内容校准）

Use this only when the user provides or explicitly designates a reference video, audio, transcript, script, competitor example, or style sample.

First extract high-level speaking characteristics that can transfer across topics, such as:
- how quickly useful information begins;
- whether the speaker reveals the conclusion directly or progressively;
- overall information density;
- continuity versus pause / breathing space;
- sentence-length variation;
- conversational versus explanatory feel;
- how professional judgment is demonstrated;
- emotional intensity;
- how naturally the content creates willingness to learn more;
- whether the ending closes on a judgment, action, unresolved condition, or natural continuation.

When the user asks to follow the reference, preserve or reconstruct its acquisition function at equal or stronger usable intensity. High-value elements may include numeric contrast, result or loss, audience callout, risk tension, curiosity, and a service-relevant CTA. Keep the original information role: discussion remains discussion, a hypothesis remains a hypothesis, and a determinative claim remains subject to verification.

Do NOT convert the reference into a universal content template.

Do NOT mechanically copy:
- paragraph count;
- sentence count;
- exact information order;
- a hook formula when it does not fit the current topic or requested reference treatment;
- recurring question form;
- CTA form;
- professional-object combinations;
- checklist items;
- diagnostic framework;
- catchphrases;
- characteristic wording.

Generate from the current topic, current facts, current persona, and current audience after calibration.

Do not weaken an anonymous, user-provided discussion hook into a generic question solely because it contains an unverified amount or result. Preserve the adjacent discussion cue and keep the body conclusion independently reliable.

Principle:

> **学参考内容的说话状态和信息释放方式，不学它的固定骨架。**

---

### Opening（开场）

The opening must create immediate relevance and use the strongest acquisition angle permitted by the information role and source. It does NOT need a stock hook phrase.

Possible forms include:
- direct judgment;
- direct result, benefit, loss, or useful action;
- concrete action;
- one number;
- familiar scene;
- visible contradiction;
- real question;
- consequence already happening;
- another opening that is more natural for this specific topic and persona.

There is no fixed priority among these forms.

Choose the opening that lets this topic enter naturally and usefully. A scene may support the answer, but it must not delay the core direction merely for immersion.

Reduce weak setup such as “很多老板不知道”“这个问题要注意”“今天聊一下” unless a high-value statement immediately makes it useful.

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

When information is sufficient, answer directly. When a critical condition materially changes the answer, give enough direction for the listener to understand the decision and then explain the branch naturally. When decisive information is genuinely missing, name the missing variable and explain why it blocks the conclusion.

Do NOT use “需要结合实际情况 / 需要综合判断 / 视情况而定” as an endpoint when a direct answer, branch conclusion, or concrete decision standard is available.

The conclusion does not have to appear in the same sentence position across different scripts. It only needs to arrive before unnecessary setup or explanation obscures the answer.

---

### Explanation Logic（解释逻辑）

Keep professional logic underneath and audience language on the surface.

Useful internal relations include:

> What happens → Why → What it affects

> Behavior → Change → Result

> Condition → Judgment → Consequence

These are reasoning relations, not required visible sequences.

For every core explanation, internally ask:

> So what does this mean for the listener?

If a policy, term, process, mechanism, or compliance principle does not change the listener's judgment, explain a necessary condition, or lead to a practical result, compress or remove it.

Practical results may include money, cost, qualification, time, progress, risk, choice, operating result, whether action is needed, or what to verify next.

But final Chinese may express these relations without explicit connectors or perfectly complete sentences.

When a professional term is necessary:

> **先说发生了什么，再补专业上叫什么。**

Do NOT use terminology or a familiar industry framework as a substitute for topic-specific explanation.

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

The examples in `references/chinese-spoken-naturalness.md` demonstrate language transformation only. They are NOT content patterns, preferred business objects, or reusable diagnostic sequences.

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
- no translationese disguised as polished Chinese;
- no reuse of calibration examples as account-default expression patterns.

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
5. non-decisive professional framework or checklist content;
6. repeated emotional warnings;
7. connectors with no listening function;
8. secondary examples;
9. second or later CTA;
10. persona performance with no informational function;
11. polished summary sentences that only repeat what the audience already understood.

Keep a unit only if removing it would lose a fact, reason, conclusion-changing condition, judgment, case function, listening clarification, necessary transition, or useful audience result.

After reduction, run one naturalness rewrite pass from `references/chinese-spoken-naturalness.md` without changing facts or conclusions.

If the topic is already complete before reaching the nominal length mode, stop. Do NOT refill removed material with new generic content.

---

### Spoken Quality Control（口播专项质检）

Rewrite if ANY applies:
- opening has no concrete relevance;
- the strongest valid information is delayed without a spoken-naturalness reason;
- a discussion hook is treated as a determinative case despite an adjacent hearsay or discussion cue;
- a result, number, loss, audience callout, or suspense element from a requested reference is removed without a role-based reason;
- a result-first discussion hook is softened into a generic question only because it lacks an official case source;
- a generated precise case is disguised with hearsay language;
- script is merely a longer text-broadcast draft;
- central question is unclear;
- multiple unrelated problems are developed;
- no core judgment exists;
- the shared explicit-conclusion check fails when the script is heard once, leaving only analysis or a list of considerations;
- branch conditions are present but their different conclusions cannot be distinguished by listening;
- policy, terminology, mechanism, or a familiar industry framework dominates the speech while the current topic's practical result remains unclear;
- a supported conclusion is weakened into verbal hedging or delayed until the listener is likely to miss it;
- judgment exists but reasoning is missing;
- multiple conclusions are stacked;
- a narrow question has expanded into a general compliance / diagnostic checklist;
- professional objects or checks appear only because they are common in the account's industry, not because they change this topic's answer;
- script sounds like an article, report, course outline or policy narration;
- sentences are difficult to say naturally;
- pronouns create listening ambiguity;
- too much background appears before the core issue;
- length increases without increasing useful judgment;
- ending introduces a new topic;
- ending adds a CTA or consultation gap that the content does not naturally require;
- ending stops at generic “规范 / 关注 / 重视” language instead of a judgment, result, decision standard, or useful action;
- intensity comes mainly from loud, absolute, threatening, or stock short-video language rather than verified information;
- a supplied reference has been copied as a visible structure instead of being used only for high-level calibration.

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
> **是不是为了显得完整，强行加了总结、升华、第三点、第二个案例，或者一套通用检查框架？**

#### Topic-local test
> **留下来的每个专业点，真的都在回答这一条内容的问题吗？**

#### Framework-leak test
> **有没有把后台常用的专业判断框架，习惯性说到了前台？**

#### Persona identity test
> **遮掉账号名以后，语言和判断方式还能不能看出是这个人？**

#### Audience decision test
> **听完以后，用户能不能用一句话回答“所以这件事到底会怎样”？**

#### Answer-not-checklist test
> **用户得到的是一个答案，还是只得到了一份注意事项？**

#### Conclusion timing test
> **有没有一个可靠结论本可以更早说，却被放到了后半段？**

#### Condition-boundary test
> **条件是在限定结论，还是在掩盖结论？**

#### Intensity-source test
> **表达力度来自真实结果和判断，还是来自情绪词和音量感？**

#### Reference-calibration test
> **如果有参考内容，获客功能是否保留，信息身份是否清楚，表达是否仍然属于当前账号和题目，并避免了与任务无关的机械照搬？**

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

If the user requests a specific length, duration, tone, depth, case emphasis, structure, or reference style, follow it within factual, account, platform, and safety boundaries.

When a reference is supplied, apply `Reference Style Calibration` unless the user explicitly requests another treatment.

If the user requests conversion between:

> `text_broadcast` ↔ `spoken`

do NOT re-plan the topic. Rewrite the same confirmed topic for the target medium.

When converting TO `spoken`, apply this Skill and the naturalness reference.
When converting TO `text_broadcast`, do NOT carry spoken-only language mechanics into the text-broadcast Skill unless that Skill requires them.

---

## Stop

Before delivery, confirm that the listener can follow the logic once, answer “所以到底会怎样” in one sentence, and understand the key boundary or next action when one is actually needed.

The conclusion must be clear without sounding like a slogan; conditions must define the conclusion rather than hide it.

The script may end naturally after the useful decision point. Do not force a consultation gap, CTA, extra checklist, or generic professional closing merely because the content is intended to acquire leads.

After delivering the requested title, spoken script, or complete spoken package, stop. Do not generate visual plans, shot lists, editing instructions, video files, publication-state changes, or archive writes; visual support requires a separate explicit request routed by root `AGENTS.md`.
