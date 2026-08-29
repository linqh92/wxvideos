# Copywriting Common Rules（文案生成通用规则）

This file defines shared rules for all copywriting media. Medium-specific Skills MUST inherit these rules and only add format-specific execution constraints.

Do NOT duplicate these rules inside individual Skills unless a short reference is required for clarity.

---

## 1. Account Context Lock（账号上下文锁定）

Before writing, determine `CURRENT_ACCOUNT` exactly from repository-root `AGENTS.md` and enforce Account Context Lock.

Read ONLY the locked account's relevant context unless the user explicitly requests cross-account comparison or system maintenance.

Required account files:

1. `accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号基本定位.md`
2. `accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号人设与文风.md`

If `CURRENT_ACCOUNT` cannot be uniquely determined, follow repository-root routing rules. If a required file is missing or unreadable, report the blocking path.

Do NOT infer missing account information from another account.

---

## 2. Account Parameters（账号参数）

Dynamically inherit, when defined:
- Account type
- Content objective
- Business scope
- Target audience
- Audience comprehension level
- Persona identity and experience
- Persona personality
- Relationship with the audience
- Tone and emotional style
- Humor / teasing habits
- Professional depth
- Title style
- Interaction style
- Conversion objective
- Prohibited expressions
- Fact and compliance boundaries

These parameters MUST materially affect wording, explanation depth, emotional intensity, professional language, interaction style, and ending tone.

Do NOT flatten all accounts into one generic style.

Principle:

> 账号定位决定谁在说、对谁说、为什么说、怎么说。  
> Account positioning determines who speaks, to whom, why, and how.

---

## 3. Confirmed Task Context（当前任务上下文）

If the topic was confirmed earlier in the same task, inherit only the necessary confirmed context, including:
- Core topic
- Target audience
- Audience scenario
- Content objective
- Related business / service context
- Verified facts
- Confirmed data
- Confirmed expression boundaries
- Confirmed content medium when applicable

Do NOT silently re-plan the topic.

User-confirmed current-task facts may supplement account files but MUST NOT override account identity or business boundaries unless the user explicitly changes them.

---

## 4. Communication Objective（传播目标）

Every piece should move through as much of this chain as the medium supports:

> Attention（停留）  
> → Specific information hit（被具体信息击中）  
> → Cognitive or emotional shift（认知/情绪变化）  
> → Effective information gap（有效信息差）  
> → Useful judgment（形成判断）  
> → Share / act / learn-more willingness（分享、行动或继续了解）  
> → Trust（建立信任）  
> → Conversion readiness（接近转化目标）

Execution priority:

> Fact accuracy  
> → Account / platform boundaries  
> → Effective information gap  
> → Real impact  
> → Appropriate emotional intensity  
> → Audience comprehension  
> → Persona consistency  
> → Conversion capability

Do NOT sacrifice accuracy or critical conditions for retention.

---

## 5. Known vs. Unknown Information（已知与未知）

Separate:

### Audience already knows
Directly observable, commonly experienced, or already obvious information.

Use mainly for context. It MUST NOT be the main value of the piece.

### Audience does not know or underestimates
Prioritize:
- Overlooked consequences or benefits
- Key validity conditions
- Hidden costs
- Impact accumulation
- Surface vs. real outcome
- Upstream-to-downstream propagation
- Why common practice may fail
- Conditions that invalidate a common judgment

Every piece SHOULD provide at least one effective information gap.

If the topic lacks enough factual support:
- Do NOT fabricate
- Do NOT force high-pressure wording
- State the limitation when necessary
- Recommend adding data, conditions, cases, comparison, or outcome evidence when appropriate

---

## 6. Emotional Drivers（情绪驱动）

Emotion may strengthen communication, but MUST come from real information.

Possible drivers:
- Risk
- Urgency
- Curiosity
- Opportunity
- Loss
- Contrast
- Absurdity
- Identity resonance
- Security
- Gain / benefit
- Decision conflict
- Uncertainty

Choose only what fits the account, topic, and verified facts.

Do NOT assume anxiety or fear is always appropriate.

---

## 7. Sources of Emotion（情绪来源）

Prefer one or two:

### Outcome Impact
What the result affects.

### Accumulation / Amplification
How impact grows with time, frequency, scale, or conditions.

### Cognitive Contrast
Gap between prior belief and actual result.

### Chain Propagation
How one link affects downstream links.

### Opportunity Loss
What may be missed by misunderstanding or delay.

### Decision Conflict
How different choices create different outcomes.

### Uncertainty
When the real problem is inability to judge, explain, or control later.

Emotion MUST NOT exist independently of facts.

---

## 8. Expression Intensity（表达强度）

### Level 1 | Conservative / Steady（稳健型）
Use when facts are incomplete, the topic is sensitive, outcomes are uncertain, or the account/user requires restraint.

Requirements:
- Preserve specific impacts
- State important conditions
- Avoid worst-case amplification
- Avoid stacked pressure language

### Level 2 | Standard Distribution（常规传播型）
DEFAULT.

Requirements:
- Lead with a valid result, benefit, risk, or cognitive conflict appropriate to the medium
- Provide at least one information gap
- Explain one meaningful impact or judgment chain
- State conclusion-changing conditions in time

### Level 3 | Aggressive Test（进攻测试型）
Use ONLY when:
- The user explicitly requests stronger distribution intensity
- Account positioning permits it
- Facts and outcomes are sufficiently verified

Requirements:
- Put the strongest valid information first
- Reduce setup
- Focus on 1–2 strongest valid pressure / benefit points
- Preserve every critical condition
- Never increase intensity by inventing facts

Principle:

> 表达更强，是信息和后果更直接。  
> Stronger expression means more direct information and consequences, not exaggeration.

---

## 9. Audience Language（受众语言）

Use language the target audience naturally understands.

Prioritize:
- Familiar objects
- Real life / business scenarios
- Directly perceivable results
- Judgment methods consistent with the persona

Translate professional logic into:

> Behavior → Change → Result

When a professional concept is necessary:

> Explain what happens first; name the professional term second.

Do NOT hard-code industry terminology inside this common rule file.

---

## 10. Persona Expression（人物表达）

Persona MUST come from the locked account's voice file.

It may affect:
- Directness
- Explanation depth
- Emotional intensity
- Humor / teasing
- Rhetorical questions
- Analogies
- Judgment tone
- Sentence rhythm
- Forms of address
- Interaction style

Persona performance MUST serve information.

Do NOT mechanically create persona through:
- Fixed catchphrases
- Forced jokes
- Repeated forms of address
- Stacked internet slang
- Tone inconsistent with account identity
- Sacrificing accuracy for personality

Principle:

> 人物感来自看问题和说问题的方式。  
> Persona comes from how the person sees and explains the problem.

---

## 11. Language Quality（语言质量）

Rewrite when the draft contains:
- Template-like AI phrasing
- Bureaucratic / official tone
- Textbook-outline feel
- Excessive professionalism
- Stacked abstract concepts
- Mechanical summaries
- Repeated sentence patterns
- Language inconsistent with the persona
- Wording a real person with this persona would not naturally use

Do NOT hard-code account-specific catchphrases, forms of address, title patterns, humor methods, recommended words, banned words, or CTA patterns here.

---

## 12. Title Baseline（标题基础规则）

Before generating titles, internally extract:
- Strongest valid outcome
- Largest information gap
- Strongest cognitive conflict
- Most concrete behavior / scenario
- Most valuable number or condition
- Best-fitting emotional driver

Every title MUST fit:
- Current persona
- Target-audience language
- Strongest valid information point
- Current expression intensity
- Fact and platform boundaries

Do NOT:
- Center a title on jargon merely because the topic contains it
- Remove a conclusion-changing condition for impact
- State only “what the content is about” without a reason to continue

For a complete package, default to three clearly different title directions unless the account defines another system:

1. Outcome Impact（结果影响型）
2. Cognitive Conflict（认知冲突型）
3. Accumulation / Decision（累积或决策型）

### Standard Title（常规标题）
Use for clear topic description and search recognition.

Prefer:
- Clear object / audience
- Clear scenario
- Clear core problem
- Natural keyword inclusion

### Short Title（短标题）
Default:
- Within 16 Chinese characters unless account rules specify otherwise
- Minimal punctuation
- Preserve core conflict, result, or information gap

---

## 13. Ending and Interaction（结尾与互动）

Do NOT force a question, forwarding prompt, or unified CTA.

Choose based on account positioning, topic, and content objective:
- One core judgment
- One action
- One check direction
- One specific question
- One open judgment space
- One persona-consistent closing line
- One natural reason to share

Do NOT add by default:
- Forced forwarding
- Forced saving
- Emotional coercion
- Fabricated material / 资料 claims
- Fabricated benefits
- Contact information
- Unrequested traffic diversion

CTA MUST obey current account and platform boundaries.

---

## 14. Facts and Verification（事实与核验）

From user material, references, cases, or competitor content, extract ONLY:
- Facts
- Scenarios
- Data
- Judgment logic
- Expression methods

Do NOT:
- Copy wording verbatim
- Perform superficial synonym replacement
- Fabricate cases, people, data, results, events, or trends
- Generalize an individual case into a universal rule

Whenever information is time-sensitive or requires deterministic judgment, verify a currently valid authoritative source when tools are available and the workflow permits it.

Includes, but is not limited to:
- Policies
- Laws and regulations
- Platform rules
- Product / processing / eligibility rules
- Prices
- Time limits / deadlines
- Penalties / liabilities
- Local rules
- Industry standards
- Current events
- Statistical data

If it cannot be confirmed, do NOT state it as definite fact.

Do NOT:
- Present local / partial situations as universal
- Present possibility as certainty
- Package historical information as current change
- Present a risk as if it already happened
- Present speculation as an official conclusion

---

## 15. Strong Expression Boundaries（强表达边界）

Strong expression is allowed ONLY when:
- Facts are true
- Audience / object scope is accurate
- Causal relationship is valid
- Critical conditions are preserved
- Outcomes are evidence-supported
- Intensity fits account positioning

Do NOT use without evidence:
- Absolute or universal judgments
- Inevitable outcomes
- False urgency
- Fabricated authority endorsements
- Fabricated insider information
- Unconditional promises
- Guaranteed outcomes
- Nonexistent risks or benefits

Principle:

> 可以把真实影响说重。  
> You may emphasize a real impact strongly.

> 不能把不存在的影响说出来。  
> You may not invent an impact that does not exist.

---

## 16. Core Internal Check（生成前核心检查）

Before writing, internally confirm:

1. Who is the current account/persona?
2. Who is the audience?
3. What is the content objective?
4. What does the audience already know?
5. What new information does this piece add?
6. What is the strongest real outcome / benefit / conflict?
7. Why does it happen?
8. Which condition determines whether the conclusion holds?
9. Which emotional driver fits best?
10. Why might the audience naturally share, act, or learn more?
11. Would this persona naturally say it this way?
12. Is the current intensity fully supported by facts?

If there is no valid information gap or real impact, do NOT use emotion to fake distribution intensity.

---

## 17. Common Quality Control（通用质量控制）

Rewrite if ANY applies:
- No useful information gap
- No specific result, benefit, judgment, or meaningful explanation
- Emotion lacks factual support
- A conclusion-changing condition is omitted
- Professional language is not translated for the audience
- Persona conflicts with account positioning
- Business language or traits from another account appear
- Facts, results, events, or trends are fabricated
- The same conclusion is repeated without new function
- Background is added only to appear professional
- CTA conflicts with account or platform boundaries

Medium-specific Skills MUST add their own format checks.

---

## 18. Common Scoring（通用评分）

Internal by default.

### Information Gap: 1–5
Does the content provide information the audience did not know or underestimated?

### Emotional / Distribution Intensity: 1–5
Does emotion come from real information and create a valid reason to care?

### Share Value: 1–5
Does it have reminder, discussion, explanation, or identity-expression value without forced sharing?

### Account Consistency: 1–5
Does it fit account identity, persona, audience comprehension, and conversion objective?

### Conversion Capability: 1–5
Can the target audience recognize relevance, perceive useful capability, and reasonably want further understanding?

### Platform Risk: Low / Medium / High
Check:
- Fact risk
- Absolute-claim risk
- Manufactured fear
- Authority misrepresentation
- Interaction inducement
- Traffic diversion
- Service / outcome promises

If any numeric score is below 3, rewrite first.

Medium-specific Skills MAY add extra scoring dimensions.

---

## 19. Output Discipline（输出纪律）

Follow the user's requested output strictly.

Do NOT automatically expose:
- Creative process
- Internal reasoning
- Persona parameter checklist
- Scoring
- Risk analysis
- Long source lists
- Unrelated topic ideas
- Visual production plans
- Archive operations

Only disclose a factual limitation when necessary for correctness.

---

## 20. Final Principles（最终原则）

> 每次先读取当前账号，再决定怎么写。  
> Read the current account first, then decide how to write.

> 不在公共规则中写死行业、业务、人群和人物。  
> Do not hard-code industry, business, audience, or persona.

> 不写死固定词语、口头禅和 CTA。  
> Do not hard-code fixed wording, catchphrases, or CTA.

> 每篇至少提供一个有效信息差。  
> Every piece should provide at least one effective information gap.

> 情绪必须来自真实信息。  
> Emotion must come from real information.

> 允许强化真实影响，不制造虚假恐慌。  
> Strengthen real impact; do not manufacture false fear.

> 条件可以分层表达，但不能故意隐瞒。  
> Conditions may be layered, but never intentionally hidden.

> 专业逻辑留在底层，受众语言放在表层。  
> Keep professional logic underneath; present audience language on the surface.

> 分享动力来自内容价值，不来自强制转发。  
> Sharing motivation must come from content value, not forced forwarding.

> 结尾服从账号定位和转化目标。  
> The ending must obey account positioning and conversion objectives.
