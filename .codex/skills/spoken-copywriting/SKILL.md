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
- Re-plan topics
- Switch to unrelated topics
- Generate text-broadcast copy unless requested
- Mark content as published
- Archive or update history
- Produce visuals, shot lists, editing plans, or video files

After delivering the requested copy, STOP.

---

## 2. Required Context and Common Rules（必读上下文）

Determine `CURRENT_ACCOUNT` exactly from repository-root `AGENTS.md`, then enforce Account Context Lock.

Read and obey, in order:

1. `shared/rules/copywriting-common-rules.md`
2. `accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号基本定位.md`
3. `accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号人设与文风.md`

Current-task facts explicitly confirmed by the user may supplement these files, but must not silently replace account identity, business scope, audience, persona, or factual boundaries.

If any required file is missing or unreadable, report the blocking path. Do NOT borrow context from another account.

---

## 3. Content Medium（内容载体）

This Skill writes content primarily understood by listening to a real person.

Optimization priority:

> Auditory clarity（听得懂）  
> → Retention（愿意继续听）  
> → Reasoning comprehension（听懂为什么）  
> → Judgment credibility（相信判断有依据）  
> → Persona trust（建立人物信任）  
> → Conversion readiness（愿意进一步了解）

Subtitles may assist, but MUST NOT determine the script structure.

Do NOT write:
- A longer text-broadcast post
- An article split into short lines
- A report, course note, encyclopedia entry, official notice, or PPT narration
- A mechanically expanded AI outline

Principle:

> 口播不是加长版短文。  
> Spoken copy is not a longer text-broadcast draft.

---

## 4. Core Objective（核心目标）

Each piece should contain:

> One central question（一个中心问题）  
> + One core judgment（一个核心判断）  
> + Visible reasoning（可感知的判断过程）  
> + Necessary conditions（必要条件）  
> + One useful final direction（最终判断或行动方向）

The audience should know:
1. What the judgment is.
2. Why it holds.
3. What to check in their own situation.

---

## 5. Trust Building（信任建立）

Build trust by demonstrating judgment capability, NOT by self-promotion.

Prioritize:
- Identifying the real variable behind a surface problem
- Explaining why a conclusion holds
- Distinguishing materially different situations
- Showing which conditions change the conclusion
- Stating what must be checked first
- Acknowledging real uncertainty
- Giving a useful decision framework

Do NOT rely on:
- Repeated self-praise
- Unsupported experience claims
- Fabricated client counts or cases
- “相信我” style authority claims
- Empty insider / expert posturing

Principle:

> 专业感来自判断过程。  
> Professional credibility comes from the reasoning process.

---

## 6. Length Modes（内容幅度）

Priority:

> User-specified length  
> → Reference length  
> → Topic complexity  
> → Default mode

### Quick Spoken（快速口播）
Approximately 180–280 Chinese characters.

Use for:
- One simple misconception
- One direct judgment
- One common mistake
- One small decision problem

Default structure:

> Hook → Judgment → Why → Key condition → Action direction

### Standard Spoken（标准口播）
DEFAULT. Approximately 280–450 Chinese characters.

Use for:
- One problem requiring explanation
- Two or three important variables
- One short case
- Cause-effect explanation
- Decision comparison

Default structure:

> Hook → Core judgment → Why → 2–3 supporting points → Condition / exception → Final direction

### Deep Spoken（深度口播）
Approximately 450–750 Chinese characters.

Use ONLY when the topic genuinely requires:
- Multiple necessary conditions
- A business / decision chain
- Case development
- Policy interpretation
- Multi-party relationship explanation
- Two or more decision paths

If the script needs substantially more than 750 Chinese characters, first split the topic, remove background, or defer secondary branches.

Do NOT choose a longer mode merely because more source material exists.

---

## 7. Information Capacity（单篇信息容量）

Default upper bound:
- 1 central problem
- 1 core conclusion
- 2–4 supporting logic points
- Necessary conditions or exceptions
- At most 1 main case OR 1 main comparison
- 1 final judgment / check / action direction

Do NOT develop multiple unrelated problems, conclusions, or cases in one piece.

Principle:

> 可以把一个问题讲深。  
> Go deeper on one problem; do not stack many problems into one script.

---

## 8. Pre-Generation Judgment（生成前内部判断）

Internally determine:

1. What is the single central question?
2. What does the audience already know?
3. What do they not know or underestimate?
4. What is the strongest valid information gap?
5. What is the core judgment?
6. Why does it hold?
7. Which variables determine the result?
8. Which condition could change the conclusion?
9. Does the topic need a case, comparison, or process explanation?
10. What best demonstrates professional judgment?
11. What should the audience know how to check afterward?
12. What must not be overstated?
13. Would this persona naturally say it this way aloud?

Do NOT expose this checklist mechanically.

---

## 9. Structure Modes（正文结构模式）

Choose the structure that best fits the topic. Do NOT force one template.

### Judgment Explanation（判断解释型）
> Problem → Judgment → Why → Variables → Conditions → Check direction

### Cognitive Reversal（认知纠偏型）
> Common belief → Correction → Why it fails → Correct judgment → Conditions → Reminder

### Case Breakdown（案例拆解型）
> Case result / conflict → What happened → Real break point → Why → What to check → General lesson

Cases MUST be user-provided, verified, authorized project material, or clearly hypothetical.

### Decision Comparison（决策比较型）
> Two choices → Core difference → Different outcomes → Applicable conditions → Decision standard

### Chain Explanation（链条解释型）
> Starting behavior → Intermediate change → Downstream impact → Final result → Key break point → Check direction

### Mechanism Explanation（机制拆解型）
> Surface phenomenon → Underlying mechanism → Key steps → Why the result appears

Use only when mechanism understanding improves judgment.

### Event / Policy Impact（事件或规则影响型）
Use ONLY after current verification.

> What happened → Who is affected → What changed → What did not change → Practical impact → Current judgment

Do NOT present historical information as a new change.

---

## 10. Opening Hook（前3—5秒）

The opening MUST create a valid reason to continue listening.

Prefer:
- Familiar scenario + unexpected result
- Common judgment + direct conflict
- Specific result + why it happens
- Concrete number / condition + cognitive difference
- Real problem + hidden variable

The opening SHOULD contain a recognizable audience/object/situation plus a concrete conflict, result, benefit, risk, or question.

Do NOT default to:
- “大家好”
- Long self-introduction
- “今天跟大家分享一下”
- “很多朋友问我”
- Vague background
- Empty emotion or unsupported fear

Persona-specific greetings are allowed only when they fit the account voice and do not weaken retention.

---

## 11. Conclusion Timing（结论位置）

Do NOT hide the conclusion until the end merely to manufacture suspense.

Default:

> Give an early directional judgment, then explain why.

Do not state certainty before critical conditions when those conditions materially change the result.

---

## 12. Explanation Logic（解释逻辑）

Prefer:

> What happens → Why → What it affects

or:

> Behavior → Change → Result

or:

> Condition → Judgment → Consequence

Keep professional logic underneath and audience language on the surface.

When a professional term is necessary, first explain what happens in plain language, then give the term.

Do NOT use terminology as a substitute for explanation.

---

## 13. Auditory Clarity（听觉理解）

Every sentence must remain understandable when heard once without subtitles.

Prefer:
- Short or medium spoken sentences
- Clear subject-object relationships
- One main idea per sentence
- Concrete nouns
- Explicit cause / contrast / condition markers
- Repeating the key object when pronouns would become ambiguous

Check every long sentence:

> Can a real person say it comfortably in one breath?

If not, split or rewrite it.

Avoid:
- Long nested clauses
- Continuous definitions
- Stacked abstract concepts
- Written-language inversion
- Excessive parentheses or abbreviations
- Long unexplained enumerations
- Article-style sentences that sound unnatural aloud

---

## 14. Spoken Transitions（口语连接）

Natural transitions may be used to:
- Move to the key point
- Ask and answer a question
- Explain cause
- Reframe a statement
- Introduce an example
- Return from a case to the core judgment

Do NOT hard-code fixed transition phrases into this general Skill.

Exact wording MUST come from the current persona.

Do NOT mechanically repeat fixed phrases such as “重点来了”“你记住”“为什么”“注意了” unless they naturally fit the account voice.

---

## 15. Functional Repetition（必要重复）

Spoken content MAY use functional repetition for auditory comprehension.

Allowed:
- State the core judgment early, then restate it more precisely after explanation
- Repeat the key object to avoid ambiguity
- Summarize one complex comparison
- Return to the original question after a case

Not allowed:
- Repeating the same conclusion with different adjectives
- Repeating warnings or CTA
- Repeating background only to extend duration

Principle:

> 允许帮助理解的重复，不允许无功能重复。  
> Repeat only when it improves listening comprehension.

---

## 16. Persona Expression（人物表达）

Persona MUST be inherited from `账号人设与文风.md` and should materially affect:
- Sentence rhythm
- Directness
- Explanation depth
- Judgment tone
- Humor / teasing
- Analogy style
- Question style
- Forms of address
- How disagreement, uncertainty, cases, and conclusions are expressed

Do NOT reduce persona to catchphrases.

Principle:

> 人物感来自怎么看问题、怎么解释、怎么下判断。  
> Persona comes from how the speaker sees, explains, and judges the problem.

---

## 17. Professional Depth（专业深度）

Professional depth means:
- Better distinction
- Better causal explanation
- Better condition explanation
- Better judgment
- Better decision guidance

It does NOT mean:
- More terminology
- More policy names
- More definitions
- More background
- More industry jargon

Remove detail that does not improve audience judgment.

---

## 18. Conditions and Exceptions（条件与例外）

Prioritize conditions that change:
- The conclusion
- Applicable audience
- Result
- Risk level
- Recommended action

Secondary conditions may be compressed.

Do NOT hide a critical condition to strengthen the hook.

If the answer depends on missing information, state what must be checked instead of inventing certainty.

---

## 19. Case Rules（案例规则）

Cases may come from:
1. User-provided material
2. Verified source material
3. Authorized project material
4. Clearly labeled hypothetical examples

Do NOT fabricate:
- Clients
- Consultation conversations
- Amounts
- Penalties
- Business outcomes

A case exists to clarify judgment, not to decorate the script.

---

## 20. Emotional Expression（情绪表达）

Follow `copywriting-common-rules.md`.

For spoken content, prefer emotion generated by:
- Real consequences
- Contrast
- Case progression
- Judgment conflict
- Opportunity loss
- Hidden variables
- Decision uncertainty
- Chain amplification

Do NOT rely on shouting language, repeated exclamation, threats, artificial urgency, or stacked high-pressure phrases.

Spoken content may be calmer than text-broadcast content while building stronger trust.

---

## 21. Title Rules（标题）

Follow the common title rules.

Spoken titles may additionally favor:
- Questions requiring explanation
- Cognitive conflict
- Decision conflict
- Case result
- Hidden reason
- “Why” information gaps
- Conditions that change a common conclusion

The title MUST promise only what the script can support.

---

## 22. Ending（结尾）

The ending should complete the current reasoning.

Prefer:
- Final judgment
- One check direction
- One decision principle
- One action
- One naturally open question
- One persona-consistent closing line

The audience should finish knowing how to look at the problem.

Do NOT force follow / share / save / comment-keyword / contact / traffic-diversion / material-claim / service-promise CTA unless explicitly allowed by current account rules and user instruction.

---

## 23. Script Formatting（口播稿格式）

Deliver directly usable spoken copy.

Default:
- Natural spoken paragraphs
- One paragraph = one speaking unit
- Punctuation for rhythm
- Necessary paragraph breaks
- No forced one-sentence-per-line formatting
- No text-broadcast 7–15-character line rule
- No artificial subtitle segmentation

Do NOT add performance or production markup by default, including:
- `[停顿]`
- `[重音]`
- `[看镜头]`
- `[字幕]`
- `[BGM]`
- Shot or editing instructions

This Skill writes copy, not directing notes.

---

## 24. Mandatory Reduction Pass（强制删减）

After drafting, remove in this order:

1. Repeated conclusions
2. Background that does not affect judgment
3. Unnecessary definitions
4. Replaceable jargon
5. Repeated emotional warnings
6. Transitions with no listening function
7. Secondary examples
8. Second or later CTA
9. Persona performance with no informational function

Keep a paragraph only if removing it would lose a fact, reason, condition, judgment, case function, or necessary transition.

Deep spoken content may be long; it must not be loose.

---

## 25. Quality Control（质量控制）

Rewrite if ANY applies:
- Opening has no concrete information
- Opening is emotion-only
- Script is merely a longer text-broadcast draft
- Central question is unclear
- Multiple unrelated problems are developed
- No core judgment exists
- Judgment exists but reasoning is missing
- Multiple conclusions are stacked
- Terminology replaces explanation
- A conclusion-changing condition is omitted
- Script sounds like an article, report, or course outline
- Sentences are difficult to say naturally
- Pronouns create listening ambiguity
- Too much background appears before the core issue
- Case content is fabricated
- Trust relies mainly on self-praise
- Persona is reduced to catchphrases
- Emotion exceeds factual support
- Length increases without increasing useful judgment
- Ending introduces a new topic
- CTA conflicts with account or platform boundaries

---

## 26. Internal Scoring（内部评分）

Do NOT expose unless requested.

### Information Value: 1–5
Useful information gap, judgment, or explanation.

### Auditory Clarity: 1–5
Understandable without subtitles.

### Reasoning Quality: 1–5
The audience understands why the conclusion holds.

### Trust Building: 1–5
The script demonstrates useful judgment rather than self-promotion.

### Persona Consistency: 1–5
Fits current persona and language habits.

### Retention Potential: 1–5
The opening and body provide valid reasons to keep listening.

### Conversion Capability: 1–5
The audience can identify relevance, perceive capability, and reasonably want further understanding.

### Platform Risk: Low / Medium / High
Use the common rules for fact risk, absolute claims, manufactured fear, authority misrepresentation, interaction inducement, traffic diversion, and service promises.

If any numeric score is below 3, rewrite first.

---

## 27. Output Modes（输出模式）

Follow the user's request strictly.

### Titles only
Output ONLY title options.

### Spoken copy only
Output ONLY the finalized spoken script.

Do NOT expose structure mode, scoring, risk scoring, or creative process unless requested.

### Complete spoken package
Default output ONLY:
1. Three clearly different title directions
2. One standard / search-recognition title
3. One short title
4. Final spoken script

Do NOT automatically output source explanation, persona analysis, shot list, visual plan, editing plan, or archive actions.

---

## 28. User Override（用户优先）

If the user requests a specific length, duration, tone, depth, case emphasis, or structure, follow it within factual, account, platform, and safety boundaries.

If the user requests conversion between:

> `text_broadcast` ↔ `spoken`

do NOT re-plan the topic. Rewrite the same confirmed topic for the target medium.

---

## 29. Final Principles（最终原则）

> 口播不是加长版短文。  
> Spoken copy is not a longer text-broadcast draft.

> 一条口播只解决一个中心问题。  
> One spoken piece solves one central problem.

> 能直接给方向，就不要故意拖结论。  
> Give an early directional judgment when valid.

> 能解释为什么，就不要只重复结论。  
> Explain why; do not merely repeat the conclusion.

> 能展示判断方法，就不要堆术语。  
> Show judgment; do not stack jargon.

> 复杂内容允许展开，但展开必须增加理解价值。  
> Expansion must add comprehension value.

> 专业感来自区分、解释和判断。  
> Professional credibility comes from distinction, explanation, and judgment.

> 用户只听不看，也应理解核心逻辑。  
> The core logic must work without subtitles.

> 情绪必须来自真实信息。  
> Emotion must come from real information.

> 案例用于解释，不用于制造故事。  
> Cases explain; they do not fabricate drama.

> 关键条件不能为了传播效果被隐藏。  
> Never hide conclusion-changing conditions.

Final spoken content should contain:

> Effective hook  
> + One central question  
> + One core judgment  
> + Understandable reasoning  
> + Necessary conditions  
> + Appropriate professional depth  
> + Natural spoken language  
> + Persona recognizability  
> + Trust-building value  
> + Factual credibility
