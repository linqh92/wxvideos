---
name: video-copywriting
description: Generate high-impact, socially shareable WeChat Video Account text-broadcast copy from a confirmed topic. Dynamically inherit each project's account positioning, audience, persona, business context, tone, content boundaries, and conversion goals. Use for titles, 正文, or complete copy after a topic is confirmed. Do not use for topic planning, inspiration intake, publication archiving, or visual production.
---

# WeChat Video Account Text-Broadcast Copywriting（微信视频号文字播报文案生成）

## 1. Scope of Responsibility（职责范围）

This Skill ONLY generates finalized WeChat Video Account text-broadcast content（文字播报内容）from a topic that has already been confirmed.

Deliver only what the user requests, including:

- Title（标题）
- Short title（短标题）
- Main copy（正文）
- Complete copy package（完整文案）
- A specified version or expression direction（指定版本或表达方向）

If the topic comes from a previously confirmed step, the Skill MUST inherit all confirmed context, including:

- Core topic（核心主题）
- Target audience（目标受众）
- Audience scenario（受众场景）
- Content objective（内容目的）
- Related service or business context（服务或业务关联）
- Verified facts（已核验事实）
- Confirmed data（已确认数据）
- Confirmed expression boundaries（已确认表达边界）

After delivering the requested copy, STOP. Do NOT automatically:

- Re-plan topics（重新规划选题）
- Expand into unrelated topics（扩展无关主题）
- Mark content as published
- Write to historical content libraries
- Update a content map
- Create archive records
- Produce visuals or video

---

## 2. Dynamically Load Account Context（动态读取账号上下文）

Before writing, determine `CURRENT_ACCOUNT` exactly as defined by the repository-root `AGENTS.md`, then enforce Account Context Lock. Do not inspect another account to infer missing information.

Read both files for the locked account:

1. `accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号基本定位.md` — business scope, audience, content goal, and factual boundaries.
2. `accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号人设与文风.md` — persona, voice, title style, natural-language rules, and prohibited expression patterns.

If `CURRENT_ACCOUNT` cannot be uniquely determined, ask the user to confirm it. If either required file is missing or unreadable, report the blocking path instead of borrowing context from another account.

Current-task facts explicitly confirmed by the user may supplement these files but must not silently replace the locked account identity or business boundaries. Do NOT invent account identity, persona, business scope, or target audience.

---

## 3. Account Parameters That MUST Be Dynamically Inherited（必须动态继承的账号参数）

Identify from the current account positioning:

- Account type（账号类型）
- Content objective（内容目的）
- Platform and content format（平台与内容形式）
- Core business or content direction（核心业务或内容方向）
- Target audience（目标受众）
- Audience comprehension level（受众理解能力）
- Everyday or business language familiar to the audience（受众熟悉的生活或业务语言）
- Persona identity（人物身份）
- Persona experience（人物经历）
- Persona personality（人物性格）
- Relationship with customers/audience（客户或受众关系）
- Expression intensity（表达强度）
- Emotional style（情绪风格）
- Humor / teasing / 吐槽 habits（幽默与吐槽习惯）
- Degree of professional terminology（专业术语使用程度）
- Title style（标题气质）
- Interaction style（互动方式）
- Conversion objective（转化目标）
- Explicitly prohibited writing styles（明确禁止的文风）
- Fact and compliance boundaries（事实与合规边界）

These parameters MUST materially affect:

- Title wording
- First-screen expression（第一屏表达）
- Main-copy structure（正文结构）
- Emotional intensity
- Explanation method
- Sentence length
- Professional depth
- Interaction style
- Ending tone
- Overall persona recognizability（人物辨识度）

Do NOT flatten all accounts into one standardized writing style.

Principle:

> 账号定位决定谁在说、对谁说、为什么说、用什么方式说。  
> Account positioning determines who is speaking, to whom, why, and how.

> Skill只负责传播结构、信息组织和质量控制。  
> The Skill is responsible only for communication structure, information organization, and quality control.

---

## 4. Content Medium（内容载体）

This Skill generates WeChat Video Account text-broadcast content（微信视频号文字播报内容）:

- Copy appears line by line or paragraph by paragraph
- It may be paired with simulated typing or subtitle effects
- Users mainly receive information by reading
- The content must not depend on a real person's voice, facial expressions, or vocal performance

Therefore, the copy MUST be optimized for visual reading（视觉阅读）.

Do NOT default to writing:

- A spoken-camera script（真人口播演讲稿）
- A long-form article
- An official notice
- Training material
- A consulting report
- An encyclopedia-style explanation
- Academic exposition
- A generic AI-summary style draft（标准AI总结稿）

If the current account positioning explicitly requires otherwise, follow the account positioning.

---

## 5. Platform Distribution Assumptions（平台传播假设）

WeChat Video Account content may continue spreading through social relationships, friend interactions, and sharing.

Do NOT treat any specific recommendation weight as a confirmed algorithmic fact. However, before finalizing content, ALWAYS check:

> 用户看完以后，是否获得了值得提醒、讨论或分享的信息。  
> After reading, did the user gain information worth reminding others about, discussing, or sharing?

Sharing motivation SHOULD come primarily from the content itself, for example:

- The audience learns something they did not know
- They discover reality differs from prior understanding
- They realize a consequence, benefit, or impact was underestimated
- They understand that a problem may accumulate or expand
- The content helps explain a dispute or misunderstanding
- The content helps others make a judgment
- The content carries identity-expression or social-reminder value

Do NOT mechanically require every post to name a person to forward it to.

Do NOT rely on forced forwarding, forced saving, or emotional coercion to manufacture sharing.

---

## 6. Core Communication Chain（核心传播链路）

Default communication chain:

> See（看到）  
> → Get hit by specific information（被具体信息击中）  
> → Experience an emotional or cognitive shift（产生情绪或认知变化）  
> → Discover a meaningful information gap（发现有效信息差）  
> → Quickly understand the cause and impact（快速看懂原因和影响）  
> → Develop willingness to share, act, or learn more（产生分享、行动或进一步了解的意愿）  
> → Build trust in the account（建立账号信任）  
> → Move closer to the account's conversion objective（接近账号转化目标）

Execution priority:

> Fact accuracy（事实准确）  
> → Safety and platform boundaries（安全与平台边界）  
> → Effective information gap（有效信息差）  
> → Real impact（真实影响）  
> → Emotional / distribution intensity（情绪与传播强度）  
> → Share value（分享价值）  
> → Reading efficiency（阅读效率）  
> → Persona recognizability（人物辨识度）  
> → Conversion capability（转化能力）  
> → Information completeness（信息完整度）

Do NOT sacrifice retention and reading efficiency merely to make the content more complete.

---

## 7. Known vs. Unknown Information（已知信息与未知信息）

Before writing, distinguish between:

### What the audience already knows（受众已经知道的内容）

These are phenomena the audience can directly observe, has already experienced, or generally understands.

Such information may be used ONLY to establish context. It MUST NOT be the main value of the entire piece.

### What the audience does not know or underestimates（受众不知道或低估的内容）

Prioritize:

- Overlooked consequences
- Overlooked benefits
- Key conditions required for the conclusion to hold（关键成立条件）
- Hidden costs
- How risk or impact accumulates
- Difference between surface appearance and real outcome
- How current behavior affects later outcomes
- How one link in a chain propagates into later links
- Why common practices may fail to produce expected outcomes
- Under what conditions an existing judgment becomes invalid

Every piece MUST provide at least one effective information gap（有效信息差）.

If the topic lacks sufficient factual support for an effective information gap:

- Do NOT fabricate
- Do NOT force a high-pressure version
- Explicitly indicate that the topic currently lacks a strong distribution hook（传播支点）
- Recommend adding data, conditions, cases, comparisons, or outcome evidence

---

## 8. Emotional-Drive Principles（情绪驱动原则）

Emotion may be used to strengthen distribution, but emotion MUST arise from real information.

Dynamically select based on account positioning and topic nature:

- Sense of risk（风险感）
- Urgency（紧迫感）
- Anxiety（焦虑感）
- Curiosity（好奇感）
- Opportunity（机会感）
- Loss（损失感）
- Contrast（反差感）
- Absurdity（荒诞感）
- Identity resonance（身份认同）
- Security（安全感）
- Gain / benefit（获得感）

Do NOT assume every account should use anxiety or fear.

When account positioning, topic direction, and verified facts support risk-based expression, the Skill MAY create:

> 有事实依据、有条件边界、有具体影响的真实焦虑。  
> Real anxiety grounded in facts, bounded by conditions, and tied to specific impacts.

If risk-based expression does not fit the account, choose another emotional driver consistent with the positioning.

---

## 9. Sources of Emotion（情绪来源）

Choose one or two structures that best fit the topic.

### Outcome Impact（结果影响）
State directly what the final impact affects.

### Accumulation / Amplification（累积放大）
Explain how a problem or opportunity expands with time, frequency, scale, or conditions.

### Cognitive Contrast（认知反差）
Show the gap between the audience's original belief and the actual result.

### Chain Propagation（链条传导）
Explain how one link affects multiple downstream links.

### Opportunity Loss（机会损失）
Explain what may be missed by failing to understand or act in time.

### Decision Conflict（决策冲突）
Explain how different choices create different outcomes.

### Uncertainty（不确定性）
Show that the real problem may not be the current symptom, but the later inability to judge, explain, or control the situation.

Emotion MUST NOT exist independently of facts.

---

## 10. Expression Intensity（表达强度）

### Level 1 | Conservative / Steady（稳健型）

Use when:

- Factual conditions are incomplete
- The topic is highly sensitive
- The outcome cannot be confirmed
- Account positioning is rational and restrained
- The user explicitly requests cautious wording

Requirements:

- Preserve specific impacts
- Explain judgment conditions first
- Do not proactively amplify worst-case outcomes
- Do not stack high-pressure language
- Do not manufacture unsupported urgency

### Level 2 | Standard Distribution（常规传播型）

DEFAULT level.

Requirements:

- The first screen MUST contain a specific impact, benefit, risk, or cognitive conflict
- Provide at least one effective information gap
- Develop one clear impact chain
- State conditions and boundaries in time
- Do not weaken the copy with meaningless softeners
- Do not rely on punctuation or slogans to manufacture emotion

### Level 3 | Aggressive Test（进攻测试型）

Use ONLY when ALL relevant conditions are satisfied:

- The user explicitly requests stronger distribution intensity
- Account positioning permits strong expression
- Topic facts have been verified
- Outcomes and conditions are sufficiently supported

Requirements:

- Put the strongest valid information first
- Reduce background and setup
- Focus on only 1–2 core pressure points or benefit points
- Preserve every key condition that could change the conclusion
- Never increase aggression by introducing false facts

Principle:

> 表达更强，是信息和后果更直接。  
> Stronger expression means information and consequences are more direct.

> 不是情绪和措辞更夸张。  
> It does NOT mean more exaggerated emotions or wording.

---

## 11. First-Screen Rules（第一屏规则）

The first screen is responsible for:

- Retention（停留）
- Immediate audience self-identification（对号入座）
- Emotional activation（情绪启动）
- Establishing the information gap（信息差建立）

Dynamically choose one structure:

### Structure 1
> Familiar behavior or scenario（熟悉的行为或场景）  
> + Underestimated result（被低估的结果）

### Structure 2
> Surface phenomenon（表面现象）  
> + Real result（真实结果）

### Structure 3
> A small problem（一个小问题）  
> + Amplified impact（放大后的影响）

### Structure 4
> Specific number or fact（明确数字或事实）  
> + Cognitive conflict（认知冲突）

### Structure 5
> Common judgment（常见判断）  
> + Direct correction（直接纠正）

The first screen MUST prioritize objects, behaviors, and results that the current account's audience can immediately understand.

Do NOT open with emotion only and no information.

Do NOT open with vague background, greetings, course-style introductions, or template reminders.

The first screen may postpone non-critical conditions, but MUST NOT conceal any condition that would change the conclusion.

---

## 12. Main-Copy Logic（正文逻辑）

Default main-copy structure: single-point, high-density（单点高密度）.

> Specific scenario or cognitive conflict（具体场景或认知冲突）  
> → Core judgment + necessary conditions（核心判断与必要条件）  
> → One result or action direction（一个结果或行动方向）

Before generating, internally determine:

1. What does the audience already know?
2. What new information does this piece add?
3. Why does this result occur?
4. What does the result affect?
5. What does the audience most need to judge or check now?

These questions are for internal logic validation. Do NOT mechanically expose all of them in the final copy.

The final main copy should retain ONLY information necessary for the current core judgment.

Do NOT merely restate obvious phenomena. Do NOT expand multiple logical threads just for completeness.

---

## 13. Main-Copy Modes（正文模式）

Automatically choose based on the topic. Do NOT lock into one template over time.

### Result-First（结果直击型）
> Result → Cause → Condition → Scope of impact → Judgment direction

### Cognitive Reversal（认知翻转型）
> Common judgment → Direct correction → Key condition → Real result

### Accumulation Upgrade（累积升级型）
> Current phenomenon → Accumulation method → Amplified result → Current check point

### Chain Propagation（链条传导型）
> Starting issue → Intermediate impact → Final landing point → Judgment direction

### Numeric Comparison（数字对比型）
> Number or ratio → Direct difference → Hidden condition → Final result

### Decision Comparison（决策比较型）
> Two choices → Core difference → Respective outcomes → Decision standard

### Event Impact（事件影响型）
Use ONLY when the event, policy, or platform change has been verified:

> Real event → Affected audience → What changed → Specific impact → Current judgment

Do NOT invent trends, changes, actions, or outcomes merely to fit an event-based template.

---

## 14. Information Density（信息密度）

Every sentence MUST perform at least one function:

- Provide a fact
- Give a number
- Identify an object/audience
- Describe a behavior
- Provide an information gap
- Explain a cause
- State a condition
- Develop an impact
- Provide a judgment
- Point to an action direction

If removing a sentence does not reduce the information gained by the audience, remove it first.

Low-value content includes:

- Vague reminders
- Repeated conclusions
- Meaningless setup
- Pure emotional expression
- Transitions that add no new information
- Background unrelated to the core judgment
- Persona performance that carries no informational function
- Repeating phenomena the audience already knows

---

## 15. Audience Language（受众语言）

Expression MUST be dynamically inherited from the current account positioning.

Prioritize:

- Language the target audience uses in daily life
- Objects familiar to the target audience
- Real life or business scenarios
- Results the audience can directly perceive
- Judgment methods consistent with the persona identity

Professional expression SHOULD be translated into a structure the audience can understand:

> 行为 → 变化 → 结果  
> Behavior → Change → Result

When a professional concept is necessary:

> 先让受众理解发生了什么，再补充专业名称。  
> First help the audience understand what happened, then add the professional term.

Do NOT hard-code fixed terminology, common objects, or vocabulary for any industry inside this general Skill.

---

## 16. Persona Expression（人物表达）

Persona feel（人物感）MUST be dynamically inherited from account positioning.

Persona parameters may affect:

- Directness
- Degree of explanation
- Emotional intensity
- Humor intensity
- 吐槽 intensity
- Use of rhetorical questions
- Analogy style
- Judgment tone
- Sentence rhythm
- Forms of address（称呼方式）
- Interaction style

Persona performance MUST serve the information.

Do NOT mechanically perform persona through:

- Repeating fixed catchphrases
- Forcing jokes
- Mechanically adding forms of address
- Continuous rhetorical questions
- Stacking internet slang
- Mimicking a tone inconsistent with account identity
- Sacrificing factual accuracy for personality

Principle:

> 人物感来自看问题和说问题的方式。  
> Persona comes from how the person sees and explains the problem.

> 不来自固定词语。  
> It does not come from fixed words.

---

## 17. Language Quality（语言质量）

Rewrite first when any of the following appear:

- Template-like AI phrasing（模板化AI表达）
- Official bureaucratic tone（官方公文腔）
- Textbook-outline feel（教材目录感）
- Excessive professionalism
- Stacked abstract concepts
- Ineffective emotional setup
- Mechanical summaries
- Repeated sentence patterns
- Language inconsistent with account persona
- Wording a real person with this persona would not naturally say

Do NOT hard-code account-specific items into this general Skill, including:

- Catchphrases
- Banned-word lists
- Recommended-word lists
- Forms of address
- Humor methods
- Title sentence patterns
- CTA sentence patterns

All of these MUST come from the specific account positioning.

---

## 18. Visual Reading Rules（视觉阅读规则）

The final main copy MUST preserve line breaks that can be directly used for text-broadcast display（文字播报）.

Default requirements:

- One core information unit per line（一行表达一个核心信息）
- Main copy defaults to 10–16 lines（正文默认10—16行）
- Prefer 7–15 Chinese characters per line（每行优先7—15个汉字）
- Important numbers, results, or judgments may occupy a standalone line
- Prefer line breaks where conditions, results, or logic changes
- Any sentence over 30 Chinese characters MUST be checked for splitting（超过30字必须检查能否拆分）
- Recommend 2–4 lines per information block
- First screen: maximum 4 lines, and MUST include scenario + core conflict（第一屏最多4行）
- Do not use more than two explanatory information blocks consecutively
- Ending: maximum 3 lines（结尾最多3行）
- Do not hand a full long paragraph to post-production for later splitting
- Do not fragment complete meaning merely to create shorter lines

Level 3 may increase intensity ONLY through conclusion-first ordering, direct outcomes, and reduced setup. It MUST NOT increase main-copy length merely because the expression is stronger.

If the account positioning defines a different visual rhythm, follow the account positioning.

Do not default to fixed-count numbered lists.

Use numbering ONLY when parallel information, steps, or check items are genuinely easier to scan that way.

---

## 19. Title Generation（标题生成）

Every title MUST simultaneously fit:

- Current persona style
- Current target-audience language
- Strongest valid information point in the topic
- Current expression intensity
- Fact and platform boundaries

Before generating titles, internally extract:

- Strongest valid outcome（最强有效结果）
- Largest information gap（最大信息差）
- Most obvious cognitive conflict
- Impact most suitable for amplification
- Most concrete behavior or scenario
- Most valuable number or condition
- Emotional driver most consistent with account positioning

Do NOT automatically center the title on a professional term merely because the topic contains one.

Do NOT remove a key condition that would change the conclusion merely to make the title more impactful.

---

## 20. Title Directions（标题方向）

For a complete copy package, DEFAULT to three clearly different title directions.

### Direction 1 | Outcome Impact（结果影响型）
Highlight the most important real result, benefit, loss, or change.

### Direction 2 | Cognitive Conflict（认知冲突型）
Highlight the difference between the audience's prior belief and the actual situation.

### Direction 3 | Accumulation or Decision（累积或决策型）
Highlight how impact grows, or how different choices produce different outcomes.

If the account positioning defines a clearer title system, prioritize the account's own title system. Do NOT force these three directions.

A title MUST NOT merely state “what this content is about.” It MUST provide a reason to continue reading.

---

## 21. Standard Title and Short Title（常规标题与短标题）

A complete package may additionally output:

### Standard Title（常规标题）
Used to clearly describe the topic and support search recognition.

Requirements:

- Clear object/audience
- Clear scenario
- Clear core problem
- Naturally include relevant keywords
- Do not intentionally exaggerate

### Short Title（短标题）

Default requirements:

- Within 16 Chinese characters（16个汉字以内）
- Avoid complex punctuation
- Preserve the core conflict, result, or information gap

If the account positioning defines different requirements, follow the account positioning.

---

## 22. Ending and Interaction（结尾与互动）

Do NOT force a question at the end. Do NOT force a forwarding prompt.

Dynamically choose based on account positioning, topic, and content objective:

- One core judgment
- One current action
- One check direction
- One specific question
- One partially open judgment space
- One persona-consistent closing line
- One natural reason to share

Do NOT unify all accounts under one CTA.

Do NOT add by default:

- Forced forwarding（强制转发）
- Forced saving（强制收藏）
- Emotional coercion（情绪绑架）
- Fabricated material/资料 claims（虚构资料领取）
- Fabricated benefits（虚构福利）
- Contact information（联系方式）
- Traffic diversion / 导流 methods not requested by the user（未经用户要求的导流方式）

CTA MUST obey the current account positioning and platform boundaries.

---

## 23. Length Control（长度控制）

If account positioning defines main-copy length, follow that first.

If the user provides a reference length, the user's reference length has the highest priority.

If unspecified, default main-copy length is approximately 90–130 Chinese characters（约90—130字）.

When rules, professional judgments, or business chains are complex, first narrow the angle and explain only one core judgment. If compression is genuinely impossible, expand up to about 160 Chinese characters, but do NOT default to 200+ characters.

For complex topics, length may increase moderately, but ALWAYS check:

- Is known information being repeated?
- Is there too much background?
- Is there ineffective setup?
- Is the piece trying to explain too much at once?
- Can connective sentences be removed?
- Are there overly long sentences?
- Is useless content being added merely to look professional?

Principle:

> 用最少必要文字传递最多有效信息。  
> Use the minimum necessary words to deliver the maximum useful information.

---

## 23.1 Per-Piece Information Limit（单篇信息上限）

Default limits:

- Only one core conclusion per piece（每篇只表达一个核心结论）
- At most one core pressure point OR benefit point
- At most three explicitly expanded judgment conditions（显性展开的判断条件最多三个）
- Explain at most one professional term
- Keep only one result, risk, or action direction
- Do not repeat the same conclusion using different wording
- Do not complete every background condition or operational step merely to appear professional

When multiple necessary conditions exist, explicitly expand only those directly relevant to the current scenario. Preserve the rest as brief condition boundaries for further judgment. Compression MUST NOT conceal any condition that could change the conclusion.

---

## 24. Facts and Verification（事实与核验）

From user-provided cases, competitor content, and reference materials, extract ONLY:

- Facts
- Scenarios
- Data
- Judgment logic（判断逻辑）
- Expression methods

Do NOT:

- Copy original wording verbatim
- Perform superficial word substitution
- Fabricate cases
- Fabricate people
- Fabricate data
- Fabricate results
- Fabricate events
- Fabricate trends
- Generalize an individual case into a universal rule

Whenever information may change over time or requires a deterministic judgment, the Skill MUST verify a currently valid authoritative source.

This includes, but is not limited to:

- Policies（政策）
- Laws and regulations（法律法规）
- Platform rules（平台规则）
- Product rules
- Processing / eligibility conditions（办理条件）
- Prices
- Time limits / deadlines（时间期限）
- Penalties or liabilities（处罚或责任）
- Local rules
- Industry standards
- Current events
- Statistical data

If it cannot be confirmed, do NOT state it as a definite fact.

Do NOT:

- Present a local/partial situation as universal
- Present a possibility as certainty（把可能写成必然）
- Package historical information as a current change
- Present a risk as if it has already happened
- Present speculation as an official conclusion

---

## 25. Boundaries for Strong Expression（强表达边界）

Strong expression is allowed ONLY when:

- Facts are true
- Audience/object scope is accurate
- Causal relationship is valid
- Conditions are not concealed
- Outcomes are evidence-supported
- Intensity does not exceed what account positioning allows

Do NOT use without evidence:

- Absolute judgments（绝对化判断）
- Universalized judgments（普遍化判断）
- Inevitable outcomes（必然结果）
- False urgency（虚假紧迫感）
- Fabricated authority endorsements（虚构权威背书）
- Fabricated insider information（虚构内部信息）
- Unconditional promises（无条件承诺）
- Guaranteed outcomes（保证性结果）
- Nonexistent risks or benefits

Principle:

> 可以把真实影响说重。  
> You may emphasize a real impact strongly.

> 不能把不存在的影响说出来。  
> You may NOT invent an impact that does not exist.

---

## 26. Internal Pre-Generation Judgment（生成前内部判断）

Before formal writing, internally confirm:

1. Who is the current account/persona?（当前账号是谁？）
2. Who is the account speaking to?（当前账号面对谁表达？）
3. What is the conversion objective of this content?（当前内容的转化目标是什么？）
4. What does the audience already know?
5. What new information does this piece add?
6. What is the strongest REAL outcome?
7. How does the impact form or amplify?
8. Which condition determines whether the conclusion holds?
9. Which emotional driver best fits the current account?
10. Why might the audience naturally want to share?
11. Would this persona actually say it this way in real life?
12. Is there enough factual support for the current expression intensity?

If there is no effective information gap or real impact, do NOT use emotion to fake distribution intensity.

---

## 27. Quality Control（质量控制）

Automatically rewrite if ANY of the following problems appear:

- The first screen contains no useful information
- The first two lines contain only emotion
- The copy only repeats phenomena the audience already knows
- No effective information gap
- No specific result or benefit
- No explanation of how the impact forms
- Strong expression lacks factual support
- A condition capable of changing the conclusion is omitted
- Entire piece is flat and linear
- Entire piece reads like an article, report, or training material
- Large amounts of professional language remain untranslated into audience language
- Sentences are too long for line-by-line display
- Fixed numbering is used mechanically
- A unified CTA is used mechanically
- Emotion depends only on punctuation and slogans
- Persona expression conflicts with account positioning
- Business language or persona traits from another account are used
- Facts, results, or trends are fabricated for distribution performance
- More than one core conclusion is developed simultaneously
- More than three judgment conditions are explicitly listed
- The same conclusion, impact, or reminder is repeated
- Rule background, definitions, or unrelated check items are added for completeness
- Main copy exceeds the default length without first attempting to narrow the angle

After drafting, perform ONE mandatory reduction pass（强制删减）in this order:

1. Remove repeated conclusions.
2. Remove rule background and definition-style explanation.
3. Remove conditions that do not change the core judgment.
4. Remove pure transition sentences.
5. Remove the second and later result reminders or CTAs.
6. If the copy exceeds 130 Chinese characters, narrow the content scope first. Do NOT cram information by mechanically shortening sentences.

---

## 28. Core Scoring（核心评分）

### Information Gap（信息差）: 1–5

Check:

- Does it provide information the audience did not know or underestimated?
- Does it go beyond plain repetition?
- Is there a meaningful condition, result, or cognitive difference?

### Emotional / Distribution Intensity（情绪与传播强度）: 1–5

Check:

- Does the first screen create impact?
- Does emotion come from real information?
- Does it make the audience reassess the importance of the topic?

### Share Value（分享价值）: 1–5

Check:

- Does it have reminder, discussion, explanation, or identity-expression value?
- Could it naturally trigger sharing?
- Does it rely on forced-forward wording?

### Reading Efficiency（阅读效率）: 1–5

Check:

- Can it be understood quickly?
- Is information order clear?
- Is each line suitable for visual reading?
- Are there complex long sentences?

### Account Consistency（账号一致性）: 1–5

Check:

- Does it fit the current account identity?
- Does it fit persona language habits?
- Does it fit target-audience comprehension?
- Does it fit the account's conversion objective?

### Conversion Capability（转化能力）: 1–5

Check:

- Can the target audience recognize that the content applies to them（对号入座）?
- Does the copy demonstrate useful judgment capability?
- Does it leave reasonable room for further understanding?
- Does it naturally connect to the account objective?

### Platform Risk（平台风险）: Low / Medium / High（低 / 中 / 高）

Check:

- Fact risk（事实风险）
- Absolute-claim risk（绝对化风险）
- False emotion / manufactured fear（虚假情绪）
- Authority misrepresentation（权威误导）
- Interaction inducement（互动诱导）
- Traffic diversion / 导流
- Service or outcome promises（服务或结果承诺）

Except for platform risk, if ANY score is below 3, rewrite first.

---

## 29. Output Modes（输出模式）

Choose output strictly according to the user's request. Do NOT force unrelated output.

### If the user asks only for titles（用户只要标题）

Output ONLY title options. Do not include rationale or scores unless requested.

### If the user asks only for main copy（用户只要正文）

Output ONLY the final main copy（正文）.

By default, do NOT include content mode, scores, risk analysis, or creative explanation.

Only when there is a factual risk or verification limitation that MUST be disclosed to the user, add ONE brief note after the main copy.

### If the user asks for a complete copy package（用户要完整文案）

DEFAULT output ONLY:

1. Three titles in clearly different directions
2. One standard title（常规标题）
3. One short title（短标题）
4. Main copy formatted with final text-broadcast line breaks（按最终文字播报换行格式输出的正文）

Content mode, title rationale, core scoring, and risk analysis are INTERNAL quality-control information. Do NOT expose them unless the user explicitly asks.

Do NOT output:

- Creative process
- Internal reasoning process（内部判断过程）
- Persona parameter checklist
- Long source lists
- Unrelated topic ideas
- Visual production plans
- Archive operations
- Unrequested expansion

---

## 30. Final Principles（最终原则）

> 每次先读取当前账号，再决定怎么写。  
> Read the current account first, then decide how to write.

> 不在 Skill 中写死行业、业务、人群和人物。  
> Do not hard-code industry, business, audience, or persona into the Skill.

> 不在 Skill 中写死固定词语、口头禅和CTA。  
> Do not hard-code fixed words, catchphrases, or CTAs into the Skill.

> 不重复受众已经知道的事情。  
> Do not repeat what the audience already knows.

> 每篇至少提供一个有效信息差。  
> Every piece must provide at least one effective information gap.

> 情绪必须来自真实信息。  
> Emotion must come from real information.

> 允许强化真实影响，不制造虚假恐慌。  
> Strengthen real impact; do not manufacture false fear.

> 条件可以分层说明，但不能故意隐瞒。  
> Conditions may be layered, but never intentionally concealed.

> 分享动力来自内容价值，不来自强制转发。  
> Sharing motivation must come from content value, not forced forwarding.

> 专业信息留在底层，受众语言放在表层。  
> Keep professional logic underneath; present audience language on the surface.

> 标题负责制造停留理由。  
> Titles create a reason to stop and continue reading.

> 第一屏负责建立信息差和情绪动力。  
> The first screen establishes the information gap and emotional drive.

> 正文负责说明影响如何形成。  
> Main copy explains how the impact forms.

> 结尾服从账号定位和转化目标。  
> The ending must obey account positioning and conversion objectives.

> 文字播报必须按视觉阅读方式交付。  
> Text-broadcast copy must be delivered for visual reading.

Final content should contain:

> Effective information gap（有效信息差）  
> + Real impact（真实影响）  
> + Appropriate emotion（合适情绪）  
> + Fast reading（快速阅读）  
> + Share value（分享价值）  
> + Persona recognizability（人物辨识度）  
> + Account consistency（账号一致性）  
> + Conversion capability（转化能力）  
> + Factual credibility（事实可信度）
