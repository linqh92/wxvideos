# Spoken Visual Aid Generation Rules（口播示意图与AI生图公共规则）

## 1. Role of This File（本文件职责）

This file defines the **shared comprehension and visual-explanation mechanism** for all accounts.

It MUST define:
- how spoken content is segmented;
- what makes a visual worth switching;
- how to define viewer-understanding targets;
- how to select explanatory visual forms;
- how to control information density;
- when people should or should not appear;
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

## 2. Visual Role（视觉角色）

For spoken WeChat Channels content, the middle visual is an **explanatory aid**, not a character-performance scene.

The visual should compensate for the limitations of listening-only comprehension.

The objective is:

> **让目标用户在听口播的同时，通过“看”更快理解业务关系、风险点、流程、差异和结论。**

The image should reduce cognitive load.

It should not merely make the screen look less empty.

---

## 3. Communication Priority（传播优先级）

Use this priority:

1. Information accuracy
2. Viewer understands faster
3. Image matches the current spoken topic
4. Best explanatory visual form
5. Account visual identity
6. Stable image-switch rhythm
7. Decorative aesthetics

The account visual style is important, but it is subordinate to comprehension.

Do not optimize first for:
- actor emotion;
- office atmosphere;
- cinematic storytelling;
- decorative realism;
- generic business photography.

---

## 4. Semantic Segmentation（语义分段）

Read the complete spoken content before planning any image.

Segment by semantic meaning, not by subtitle line.

A new visual segment is justified when one of these changes:
- core question;
- business object;
- cause / consequence relation;
- normal / abnormal state;
- process stage;
- risk point;
- verification focus;
- conclusion / action direction.

Merge adjacent spoken lines when they explain the same underlying meaning.

### Viewer understanding target

For each segment, complete this sentence internally:

> **观众看到这张图以后，应该立即明白：________。**

This sentence must express an understanding outcome.

Bad:

> 展示财务人员看电脑。

Good:

> 观众应立即明白：供应商货款来自老板个人账户，而不是公司账户。

---

## 5. Image Count Control（图片数量控制）

Do not create one image per sentence.

Default guidance:
- one image ≈ 6–10 seconds;
- 30–60 second spoken content often ≈ 4–6 images;
- short transitions may be shorter;
- continuous explanation may stay on one image longer.

The count is not a quota.

Choose the minimum number that keeps the visual meaning aligned with the spoken content.

### Merge when
- same business object;
- same risk point;
- same logical relationship;
- only wording changes;
- one visual can explain all included lines.

### Split when
- topic changes;
- object changes;
- logic changes;
- a key abnormal point is introduced;
- problem turns into consequence;
- discovery turns into verification;
- explanation turns into conclusion.

---

## 6. Visual Form Library（示意图形式库）

### 6.1 Relationship Demonstration（关系示意）

Use when the core content is about who / what is connected to whom / what.

Examples:
- company account → supplier;
- personal account → supplier;
- buyer ↔ supplier;
- invoice ↔ payment ↔ declaration;
- goods flow ↔ money flow.

Preferred structure:
- clearly separated objects;
- arrows or directional relationships;
- one abnormal link;
- one highlighted node;
- minimal labels.

Style expression must come from the CURRENT_ACCOUNT visual-style file.

### 6.2 Process Demonstration（流程示意）

Use when the spoken content explains a chain.

Examples:
- payment path;
- reimbursement path;
- transaction loop;
- audit verification;
- declaration → review → result;
- document matching.

Preferred structure:
- left-to-right or top-to-bottom;
- 3–5 visible steps;
- one highlighted break point;
- strong order;
- minimal text.

Avoid information overload.

Do not require a PPT-like flowchart style.

### 6.3 Comparison Demonstration（对比示意）

Use when the viewer needs to compare two states.

Examples:
- normal vs abnormal;
- company payment vs personal payment;
- closed loop vs broken loop;
- documents match vs documents mismatch.

Preferred structure:
- split screen;
- left / right;
- before / after;
- parallel objects;
- clear contrast.

Do not globally prescribe the comparison colors.

Use the account visual-style file.

### 6.4 Risk Highlight（风险点高亮）

Use when one abnormal point carries most of the meaning.

Examples:
- one wrong payer;
- one missing link;
- one unmatched amount;
- one document that does not correspond to the transaction.

Preferred structure:
- one focal object;
- one clear marker;
- reduced surrounding clutter;
- visible contrast between normal context and abnormal point.

The warning color or marking style must come from the account visual-style file.

Do not globally force red.

### 6.5 Reconciliation / Closure（梳理与闭环）

Use when the content is about sorting, matching, checking, or closing the business logic.

Examples:
- reconcile payment;
- match documents;
- connect transaction evidence;
- verify business loop.

Preferred structure:
- grouped documents / objects;
- connected checkpoints;
- aligned rows;
- check / match indicators;
- previously broken logic becoming organized.

The visual feeling should communicate “logic being sorted”, not merely “a person working”.

### 6.6 Object Focus（业务对象聚焦）

Use when one concrete object is enough.

Examples:
- one payment record;
- one invoice;
- one declaration document;
- one account relationship;
- one warning row.

The object should dominate the image.

Avoid unnecessary people.

### 6.7 Real Scene Support（真实场景辅助）

Use only when a real scene genuinely improves comprehension.

Examples:
- container loading when the content is about actual goods flow;
- warehouse / port when the point depends on physical export movement;
- desk documents when the point is “materials appear complete”.

If a person appears:
- keep the person secondary;
- do not make facial expression the main information carrier;
- avoid dialogue composition.

Whether the scene is photographic, illustrative, 3D, collage, or hybrid must come from the account visual-style file.

---

## 7. Human Presence Rule（人物使用规则）

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

## 8. Account Visual DNA Injection（账号视觉DNA注入）

After choosing the best explanatory visual form, read:

```text
accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号视觉风格.md
```

Inject the account Visual DNA into:
- rendering;
- color;
- material / texture;
- graphic language;
- composition tendency;
- human-presence tendency;
- information density;
- label style;
- account-specific negative style constraints.

Do not let Visual DNA change the factual relationship being explained.

Do not let Visual DNA force a less understandable visual form.

---

## 9. Information Density（信息密度）

One image should explain one main point.

Default visible complexity:
- 1 main relationship, OR
- 1 main process, OR
- 1 comparison, OR
- 1 highlighted abnormality.

Avoid combining:
- multiple unrelated risks;
- multiple different timelines;
- several independent diagrams;
- too many labels;
- too many business documents.

The viewer should understand the key idea within roughly one second.

The exact graphic density may vary by account, but comprehension remains the upper bound.

---

## 10. Prompt Construction（提示词结构）

Every positive prompt must explicitly define:

1. Business theme
2. Core objects
3. Relationship / process / comparison
4. Key point to highlight
5. Visual form
6. Composition
7. CURRENT_ACCOUNT visual-style injection
8. Output quality

### Standard Chinese Prompt Template

```text
[业务主题]。

画面重点不是人物交流，而是清晰示意“[唯一核心信息]”。

画面包含：
[核心对象1]、
[核心对象2]、
[必要对象3]。

重点表现：
[对象之间的关系 / 流程 / 对比 / 风险点]，
突出[异常点 / 关键节点 / 断点 / 需要梳理的内容]。

采用[关系示意 / 流程示意 / 对比示意 / 风险点高亮 / 梳理闭环 / 单一对象聚焦 / 真实场景辅助]的视觉形式。
构图清晰，重点信息一眼可懂，避免依赖大量文字阅读。

视觉风格严格遵循当前账号《账号视觉风格.md》：
[从 CURRENT_ACCOUNT 视觉风格文件动态注入 Rendering / Color / Graphic Language / Composition / Human Presence / Information Density 等有效参数]。

高分辨率，
画面比例按当前任务或账号视觉规范执行，
适合微信视频号口播中段示意图。
```

Do not insert a global fixed style string.

---

## 11. Negative Prompt Architecture（反向提示词架构）

Every final prompt must contain three negative layers.

### 11.1 Universal Quality Negatives（公共质量反向词）

Always apply:

```text
低清晰度，模糊，虚焦，错误透视，
人物出现时的人体畸形、手部错误、五官崩坏、比例失衡，
背景杂乱，元素无意义堆砌，画面信息过载，
满屏小字，密集不可读文字，大段中文说明，
伪造官方银行系统界面，伪造税务系统界面，伪造海关或政府系统界面，
随机水印，错误Logo，表意不清，信息层级混乱，
不必要的双人商务对话，人物抢占信息主体。
```

These are quality / communication constraints.

### 11.2 Account-Specific Style Negatives（账号风格反向词）

Read from:

```text
账号视觉风格.md
```

These are NOT global rules.

### 11.3 Scene-Specific Negatives（场景专属反向词）

Generate from the selected visual form.

#### Account / payment relationship
- avoid full-screen phone UI;
- avoid dense bank statement text;
- avoid random people talking;
- avoid unrelated office scene.

#### Process
- avoid excessive arrows;
- avoid information overload;
- avoid abstract flow that cannot be understood quickly.

#### Comparison
- avoid asymmetric comparison objects;
- avoid too much explanatory text.

#### Risk highlight
- avoid warning decoration overwhelming the core object;
- avoid panic acting replacing the actual risk point.

#### Reconciliation
- avoid ordinary office posing;
- avoid messy paper piles replacing the logical closure.

---

## 12. Text-in-Image Rules（图片文字）

Do not depend on long Chinese text.

Prefer:
- short labels;
- arrows;
- grouping;
- simplified business objects;
- check / cross;
- broken link;
- warning marker;
- highlight;
- simplified document identity.

Avoid:
- full Chinese paragraphs;
- full bank statements;
- full invoices;
- full official notices;
- dense tax forms;
- policy text reproduced inside the image.

If exact Chinese text is important, add it later in the editing layer.

---

## 13. Official-Looking Interface Risk（伪官方界面风险）

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

## 14. Mandatory Self-Check（强制自检）

### Comprehension test

> 如果不看字幕，这张图能不能帮助观众更快理解当前口播？

If no, redesign.

### Person-removal test

> 把人物去掉以后，信息是否反而更清楚？

If yes, remove or weaken the person.

### One-second test

> 观众一秒内能不能找到这张图的重点？

If no, simplify.

### Duplication test

> 相邻两张图是否只是换了构图，但表达同一个意思？

If yes, merge.

### Account differentiation test

> 当前 Prompt 是否真的体现了 CURRENT_ACCOUNT 的视觉DNA？

If no, re-read the account visual-style file.

### Style-over-comprehension test

> 为了账号风格，是否牺牲了信息理解效率？

If yes, preserve the explanatory structure and weaken the style constraint.

---

## 15. Completion Standard（完成标准）

A qualified visual plan should make the spoken video feel:

> **声音在解释，画面同步把逻辑演示出来；不同账号共享理解机制，但拥有不同视觉语言。**

That is the target standard.
