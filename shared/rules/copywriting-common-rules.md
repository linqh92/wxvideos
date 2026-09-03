# Copywriting Common Rules（文案生成通用规则）

This file defines shared rules for all copywriting media. Medium-specific Skills MUST inherit these rules and only add format-specific execution constraints.

All copywriting also follows `shared/rules/acquisition-and-fact-framing.md`. That file controls information-role classification, source boundaries, verification decisions, and acquisition preservation.

Do NOT duplicate these rules inside individual Skills unless a short reference is required for clarity.

---

## 1. Required Account Context（必读账号上下文）

Account selection, isolation, and switching follow repository-root `AGENTS.md`; this file does not redefine Account Context Lock.

After the root rules have uniquely determined `CURRENT_ACCOUNT`, read:

1. `accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号基本定位.md`
2. `accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号人设与文风.md`

If a required file is missing or unreadable, report the blocking path. Do NOT infer missing account information from another account.

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

> Legal / platform / business boundaries
> → Information-role fidelity
> → Acquisition strength
> → Reliable professional judgment
> → Effective information gap
> → Real impact
> → Audience comprehension
> → Persona consistency
> → Conversion readiness

Use the strongest acquisition expression permitted by the information's role and source. Keep determinative facts and professional conclusions accurate, and keep conclusion-changing conditions visible.

Default information order when the facts support a decision:

> Strongest valid information / hook
> → Direct or directional conclusion
> → Audience result / benefit / loss
> → Reason or core mechanism
> → 1–3 conclusion-changing conditions as needed
> → Final judgment or one useful action

This is a decision sequence, not a mandatory visible template. Use only the parts the topic and medium genuinely need. Conditions define the boundary of a conclusion; they MUST NOT replace or bury the conclusion.

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

### Explicit Conclusion Mechanism（明确结论机制）

Before drafting, internally determine:

1. What exact question is the topic asking?
2. Is the available information sufficient for a reliable conclusion?
3. What is the default conclusion under the stated facts?
4. Which conditions would materially change that conclusion?
5. What practical result matters most to the audience?

When information is sufficient, answer the decision directly: will / will not, can / cannot, should / should not, affects / does not affect, higher / lower risk, worthwhile / not worthwhile, or which option better fits the stated situation.

When one universal answer would be inaccurate but meaningful branches are known, give branch conclusions:

> Condition A → Conclusion 1
> Condition B → Conclusion 2

Do NOT retreat to “视情况而定 / 需要综合判断” when a usable branch judgment can be given.

When decisive information is genuinely missing, state only:
- which decisive information is missing;
- why it prevents a reliable conclusion;
- what the user must provide or verify next.

Do NOT stack non-decisive conditions merely to appear professional.

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
Use when facts are incomplete, the conclusion is highly uncertain, the topic is sensitive, an authoritative source cannot be verified, a critical applicability condition is unknown, or the account/user requires restraint.

Requirements:
- Preserve specific impacts
- State important conditions
- Avoid worst-case amplification
- Avoid stacked pressure language

### Level 2 | Standard Distribution（常规传播型）
DEFAULT.

Requirements:
- Lead with the strongest valid result, conclusion, benefit, risk, or cognitive conflict appropriate to the medium
- Give a direct answer when the facts permit one
- State what the conclusion means for the audience
- Provide at least one information gap
- Explain one meaningful impact or judgment chain
- Place conditions after the main direction when possible, but state conclusion-changing conditions in time

### Level 3 | Aggressive Test（进攻测试型）
Use ONLY when:
- The user explicitly requests stronger distribution intensity
- Account positioning permits it
- Facts and outcomes are sufficiently verified

Requirements:
- Put the strongest valid information first
- Reduce setup
- Give the supported conclusion directly rather than weakening it by default
- Focus on 1–2 strongest valid pressure / benefit points
- Preserve every critical condition
- Remove cautionary buffer language that does not change the judgment
- Never increase intensity by inventing facts

If all Level 3 conditions are met, do not silently downgrade the draft because of generic model caution. Level 3 still does not permit absolute claims, hidden conditions, unsupported urgency, or exaggerated causality.

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

For every core point, internally ask:

> So what does this mean for the target audience?

If a sentence only explains a policy, definition, term, process, compliance principle, or industry background, continue translating it until the practical consequence is clear. Prefer concrete effects on money, cost, qualification, time, progress, risk, choice, operating result, whether action is needed, or what to do next.

Keep a technical explanation only when it supports the conclusion, changes the audience's judgment, or explains a necessary condition.

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

Humor, rhetorical questions, analogies, and teasing are optional. Use them only when they fit the persona and improve understanding or memorability; do not fill quotas or turn every strong statement into a rhetorical question.

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

### Trust and professional credibility（信任与专业感）

Build trust by demonstrating useful judgment: identify the real variable, explain why the result appears, distinguish materially different situations, preserve conclusion-changing conditions, acknowledge uncertainty, and give a useful check or decision direction.

Do NOT rely on self-praise, unsupported experience claims, fabricated client counts, empty expert posturing, terminology density, or authority language such as “相信我”.

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
- “需要结合实际情况 / 需要综合判断 / 视具体情况而定” without an immediate judgment standard or branch conclusion
- “建议关注 / 需要重视 / 规范经营 / 做好风险防范” without a concrete object, consequence, condition, or action
- Analysis that never answers the decision question asked by the topic

Do not use professional caution as a substitute for judgment. If deleting a formally correct sentence does not reduce the user's ability to decide, understand a result, or act, delete it.

Do NOT hard-code account-specific catchphrases, forms of address, title patterns, humor methods, recommended words, banned words, or CTA patterns here.

---

## 12. Title Baseline（标题基础规则）

Before generating titles, internally extract:
- Clearest supported conclusion
- Largest real benefit / loss
- Strongest cognitive conflict
- Most valuable number
- Most consequential wrong assumption
- Largest information gap
- Most concrete behavior / scenario or conclusion-changing condition
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
- Default to generic “注意事项 / 需要注意什么 / 如何处理” phrasing when a supported result, conflict, benefit, loss, or judgment is available

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
- One branch conclusion or decision standard
- One concrete audience result
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

First classify every material claim under `shared/rules/acquisition-and-fact-framing.md` as a determinative fact, discussion claim, hypothetical scenario, or professional conclusion.

From user material, references, cases, or competitor content, extract:
- Facts
- Scenarios
- Data
- Judgment logic
- Expression methods
- Acquisition devices such as numeric contrast, audience callout, loss, suspense, and service-relevant CTA

Do not mechanically copy a reference or perform superficial synonym replacement. When the user explicitly asks to follow a reference or preserve its acquisition points, retain or reconstruct its high-value hook functions and any wording that remains appropriate for the current account, topic, and information role.

Whenever a determinative fact or professional conclusion is time-sensitive, verify a currently valid authoritative source when tools are available and the workflow permits it.

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

If it cannot be confirmed, do not state it as a determinative fact or use it as the basis for a professional conclusion. Preserve it as a discussion claim when it satisfies the shared discussion-role rules, or convert it into a clearly hypothetical scenario when the source and meaning permit that treatment.

Cases and specific numeric scenarios may come from user-provided material, verified sources, authorized project material, or clearly labeled hypothetical examples. A user-provided anonymous claim with an adjacent hearsay or discussion cue may remain a discussion hook without official case verification. Do not add invented identifying details, present it as officially confirmed, or generalize its result into a universal rule.

Prioritize conditions that change the conclusion, applicable audience, result, risk level, or recommended action. Secondary conditions may be compressed, but conclusion-changing conditions must not be hidden for impact.

Do NOT:
- Present local / partial situations as universal
- Present possibility as certainty
- Package historical information as current change
- Present a generated hypothetical risk as if it already happened
- Present speculation as an official conclusion
- Invent a precise case and disguise it with hearsay language

---

## 15. Strong Expression Boundaries（强表达边界）

Strong expression is the default when:
- the information role is clear;
- the source is permitted for that role;
- determinative facts and professional conclusions are reliable;
- the audience / object scope is accurate;
- critical conditions are preserved;
- the intensity fits account positioning and platform boundaries.

Discussion claims may use strong numbers, results, losses, risk language, and audience callouts when the discussion framing remains clear and the body supplies an independent professional judgment. Hypothetical scenarios may use strong calculated outcomes when their assumptions are visible.

Do not use the following as the authorial conclusion, factual endorsement, or promise:
- Absolute or universal judgments
- Inevitable outcomes
- False urgency
- Fabricated authority endorsements
- Fabricated insider information
- Unconditional promises
- Guaranteed outcomes
- Nonexistent risks or benefits

Principle:

> 合规边界内，优先把目标客户最关心的冲突和结果说到位。
> Within the compliance boundary, foreground the strongest customer-relevant conflict and result.

> 讨论内容标明讨论身份，专业结论保持可靠。
> Frame discussion as discussion and keep professional conclusions reliable.

---

## 16. Core Internal Check（生成前核心检查）

Before writing, internally confirm:

1. Who is the current account/persona?
2. Who is the audience?
3. What is the content objective?
4. What exact decision question must the piece answer?
5. What role does each key claim play: determinative fact, discussion claim, hypothetical scenario, or professional conclusion?
6. Does the source permit that role and level of specificity?
7. Is the information sufficient for a direct conclusion, a branch conclusion, or only a precise information gap?
8. What is the strongest usable outcome / benefit / conflict?
9. What does it concretely mean for the audience?
10. Why does it happen?
11. Which condition determines whether the conclusion holds?
12. Which emotional driver fits best?
13. Why might the audience naturally share, act, or learn more?
14. Would this persona naturally say it this way?
15. Is the current intensity appropriate for the information role and source?
16. Is any acquisition-relevant number, result, audience callout, or supported conclusion being weakened without a role-based reason?

If there is no valid information gap or role-appropriate impact, do NOT use emotion to fake distribution intensity.

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
- A discussion claim is misclassified as a determinative case
- An adjacent discussion cue is ignored
- A result-first hook is weakened into a generic question only because the anonymous discussion claim lacks an official case source
- Reference-provided numbers, losses, audience callouts, suspense, or service-relevant CTA are removed without a role-based reason
- A generated precise case is disguised as a discussion claim
- The same conclusion is repeated without new function
- Background is added only to appear professional
- CTA conflicts with account or platform boundaries
- The audience still cannot answer the topic's central question after consuming the piece
- Conditions are listed without a direct or branch conclusion
- “需要综合判断” or equivalent wording replaces an available judgment
- Policy, terminology, or process is explained without an audience result
- A risk is stated without the condition that makes it relevant
- “需要注意 / 建议关注” appears without what, why, consequence, or next action
- The strongest valid information appears late without a medium-specific reason
- A conclusion that can be stated clearly is deliberately weakened
- The information role permits stronger directness, but generic caution reduces the draft to vague language
- The ending stops at a generic compliance reminder instead of a judgment, result, decision standard, or useful action

Final audience-decision check:

1. Can the target audience answer in one sentence: “所以这件事到底会怎样？”
2. Did the audience receive an answer, or only a list of considerations?
3. Is there a supported conclusion that could be stated earlier?

If the answer is weak, rewrite before output.

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

> 能下结论时直接回答；不能一刀切时给分支结论。
> Answer directly when possible; give branch conclusions when one universal answer would be inaccurate.

> 条件负责限定结论，不负责掩盖结论。
> Conditions define the conclusion's boundary; they do not hide it.

> 用户最终需要的是可靠判断，不是一份正确但没有答案的注意事项。
> The audience needs a reliable judgment, not a correct-looking list with no answer.

> 专业逻辑留在底层，受众语言放在表层。  
> Keep professional logic underneath; present audience language on the surface.

> 分享动力来自内容价值，不来自强制转发。  
> Sharing motivation must come from content value, not forced forwarding.

> 结尾服从账号定位和转化目标。  
> The ending must obey account positioning and conversion objectives.
