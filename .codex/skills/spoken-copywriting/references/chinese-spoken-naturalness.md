# Chinese Spoken Naturalness（中式真人口语规则）

## 1. Scope（适用范围）

This reference applies ONLY to `spoken-copywriting`.

It controls how a valid content judgment is turned into natural Simplified Chinese that sounds like a real Chinese person speaking to another person.

It MUST NOT be inherited by `text-broadcast-copywriting` unless a future task explicitly changes that Skill.

Its job is NOT to change facts, business conclusions, account identity, or topic logic.

Its job is to remove:
- translationese;
- official-document tone;
- report tone;
- over-polished AI prose;
- mechanically short sentences;
- template-like short-video speech.

Core principle:

> **先像一个中国人在说话，再像一篇写得漂亮的文案。**

---

## 2. Priority（优先级）

When rules conflict, use this priority:

> Fact accuracy  
> → Critical conditions  
> → Account persona  
> → Audience comprehension  
> → Natural Chinese speech  
> → Rhetorical polish

Naturalness MUST NOT weaken factual precision or hide a conclusion-changing condition.

---

## 3. Generate Speech, Not a Written Draft（直接生成说话，不先写文章）

Do NOT first write a complete article and then shorten sentences.

Build the final wording as a sequence of speaking units.

A speaking unit may be:
- a short judgment;
- a normal explanatory sentence;
- a half-sentence supplement;
- a question immediately answered;
- a condition added after the main judgment;
- a brief correction or qualification;
- a concrete example;
- a return to the main object.

The unit does not need to be grammatically symmetrical with the previous one.

Natural:

> 这笔钱先别急着算利润。票都还没对上，后面怎么算都容易偏。  
> 当然，如果你这单本来就不是这么走的，那要另外看。

Avoid:

> 首先需要判断利润。其次需要核对发票。最后需要结合具体业务情况进行分析。

---

## 4. Sentence Shape（句子形态）

Prefer mixed sentence lengths and mixed grammatical shapes.

Do NOT impose a fixed character limit such as “each sentence must be under 15 characters”.

Avoid 3 or more consecutive sentences that are all:
- equally short;
- equally complete;
- structurally parallel;
- `判断 → 原因` pairs;
- `问题 → 风险 → 建议` pairs.

Natural Chinese speech often mixes:

> 短判断 + 正常解释 + 补一句 + 稍长条件句

Example:

> 执照是办下来了。先别急着觉得事情结束了，后面税务、银行、记账这些还得接上。  
> 哪一步没接，后面都可能回来找你。

---

## 5. Controlled Incompleteness（受控的不完整表达）

When the meaning is already clear, allow natural ellipsis.

Allowed:
- omit a repeated subject;
- omit an object already established by context;
- use a short fragment as a supplement;
- place a condition after the judgment;
- stop after the useful decision point instead of forcing a grand conclusion.

Examples:

> 钱是收到了。收哪儿了？这个才要先看。

> 票有。能不能用，另说。

> 这一步先处理。后面的，等资料对上再判断。

Do NOT manufacture grammatical mistakes merely to look conversational.

---

## 6. Afterthought and Self-Repair（补一句与轻微自我修正）

Real speech may refine itself after the first statement.

Use this only when it improves precision or realism.

Natural forms include:

> 这个做法不太稳。准确一点讲，是你现在这个资料条件下不太稳。

> 也不能说一定有问题，主要还是看这笔业务怎么走的。

> 先看付款。哦，报关方式也得一起看，不然这个判断下不完整。

Do NOT overuse self-correction as a performance trick.

---

## 7. Concrete Chinese Before Abstract Labels（先说具体，再说概念）

Prefer objects, actions, money, people, time and visible outcomes before abstract nouns.

Written:

> 企业存在资金流与业务流不匹配的风险。

Spoken:

> 货是这家公司出的，钱却打到另外一个账户，后面解释的时候就容易卡。  
> 专业上你可以把它理解成资金和业务没对上。

Written:

> 应提升单证管理能力。

Spoken:

> 合同、报关单、发票、收汇别各放各的，先把同一笔业务对到一起。

---

## 8. Active Human Subjects（优先真人主动句）

Use a clear human, company, department, system or object as the subject when that improves comprehension.

Written:

> 相关资料应予以补充完善。

Spoken:

> 缺哪份资料就先补哪份，别一上来把整套文件重新做一遍。

Written:

> 该问题可能导致申报被退回。

Spoken:

> 这块没对上，系统或者审核环节就可能把申报退回来。

Do not force a subject when Chinese naturally omits it.

---

## 9. Remove Translationese（去翻译腔）

Rewrite expressions that are grammatical but do not sound like normal face-to-face Chinese.

High-risk patterns include:
- `对于……而言`;
- `在……的情况下` when a simpler condition works;
- `进行 / 开展 / 予以 / 作出` as empty verbs;
- noun-heavy phrases translated from English logic;
- repeated `这意味着……`;
- repeated `从某种角度来看……`;
- repeated `基于……可以得出……`;
- mechanically complete `如果……那么……` chains;
- long passive constructions with no natural subject.

Prefer:

> 对老板来说 → 老板最关心的是……  
> 进行核对 → 对一下  
> 予以处理 → 先处理  
> 存在风险 → 容易卡 / 容易出问题 / 还要再核对

These are direction examples, NOT a fixed replacement dictionary.

---

## 10. Connect Like a Chinese Speaker（自然承接）

If two sentences can follow directly, do not add a connector merely to show logic.

Reduce mechanical use of:
- 因此;
- 此外;
- 同时;
- 其次;
- 值得注意的是;
- 需要注意的是;
- 综上;
- 总的来说.

Natural:

> 票已经开了。问题是，货到底是不是这家供应商出的？  
> 这个对不上，后面就不是“有票没票”这么简单了。

Avoid:

> 发票已经开具。此外，需要注意的是货物来源是否一致。因此，应进一步核实供应商情况。

---

## 11. Discourse Particles（口语颗粒）

Small spoken markers may be used when they fit the persona and sentence.

Possible functions:
- re-enter the topic;
- hold the floor briefly;
- soften a correction;
- point to an object;
- create a natural pause;
- add a small qualification.

Examples:

> 这个你先别急。  
> 其实吧，关键还在付款。  
> 你看，这两张单子数字就没对上。  
> 那这种情况，就得分开看了。

Do NOT assign quotas such as “three particles per paragraph”.
Do NOT force `啊、呢、吧、你看、说白了` into every script.

---

## 12. Functional Repetition（功能性重复）

Chinese speech may repeat the same key noun rather than constantly replacing it with pronouns or synonyms.

Useful repetition:

> 这笔退税先看供应商。供应商一旦出了异常，你这边就要回头看以前这几笔采购。

Avoid decorative repetition:

> 这很危险，非常危险，真的特别危险。

Repeat for listening clarity, not emotional inflation.

---

## 13. Questions（提问）

Questions are optional.

Use a question when a real speaker would naturally ask it to expose a missing condition or contradiction.

Good:

> 钱已经收了。收公司账户，还是个人账户？这个结果差很多。

Avoid stacking:

> 你知道为什么吗？你知道后果是什么吗？你知道问题出在哪吗？

A strong statement does not need to be converted into a rhetorical question.

---

## 14. Opening Naturalness（自然开场）

A short-video opening still needs relevance, but it does not need a stock “hook phrase”.

Possible opening forms:
- direct judgment;
- concrete action;
- one number;
- familiar scene;
- visible contradiction;
- a real question;
- a consequence already happening.

Examples:

> 公司账户都开始收钱了，这时候还一直零申报，就得先看看业务到底做到哪一步了。

> 货已经出了，票还没来。退税先别急着报，这一段要先对清楚。

Do NOT default to:

> 注意了。  
> 重点来了。  
> 很多人不知道。  
> 你一定要看完。  
> 跟你说个扎心的事实。

These phrases are not forbidden words; they are forbidden as default templates.

---

## 15. Ending Naturalness（自然收尾）

Do not force every script to end with:
- a summary;
- a lesson;
- a slogan;
- a question;
- a CTA;
- an emotional uplift.

A natural ending may simply stop after:
- the final judgment;
- the first thing to check;
- a condition that still needs confirmation;
- one practical action.

Examples:

> 所以这单先把付款和开票对上，别急着往后算。

> 如果你们后面还准备融资，那这个比例现在就要重新看。

> 资料没齐之前，我不会先下“能退还是不能退”的结论。

---

## 16. Before / After Calibration（改写前后语感标尺）

Use these examples to learn the transformation pattern, NOT to reuse the final wording.

### Example 1｜去报告腔

Before:

> 对于初创企业而言，在经营初期应当充分重视财税合规管理，以避免后续产生不必要的风险。

After:

> 公司刚开始做生意，账和税别先放一边。前面随手处理的东西，后面真有业务了，经常还得回来补。

### Example 2｜抽象变具体

Before:

> 企业应关注资金流、票据流与业务流的一致性。

After:

> 谁卖货、谁开票、钱打给谁，这三件事别各走各的。放到同一笔业务里能对得上，后面才好解释。

### Example 3｜允许补一句

Before:

> 供应商异常可能对企业出口退税产生影响，企业应及时核查相关业务。

After:

> 供应商一旦异常，你这边的退税确实可能被带着一起核。  
> 不是说一定有问题，先把跟这家供应商有关的几笔采购找出来，这个最实际。

### Example 4｜不强行三段式

Before:

> 首先核对合同，其次核对发票，最后核对银行流水，并综合判断业务真实性。

After:

> 先别急着下结论。合同拿出来，发票放旁边，再看钱到底怎么走。三样一对，很多问题自己就出来了。

### Example 5｜去短句工厂

Avoid:

> 钱收了。票开了。合同有了。资料齐了。风险还在。

Prefer:

> 钱收了、票也开了，看着资料挺齐。可合同里写的交易方式跟实际走法不一样，这个才是要继续问的地方。

---

## 17. No Phrase Bank Dependency（不依赖固定表达库）

Do NOT maintain a universal library of hooks, transitions, warnings and endings for direct insertion.

A phrase list may be used only as negative examples or calibration samples.

The final wording should be generated from:

> current fact  
> + current speaker  
> + current listener  
> + current speaking situation

not from phrase retrieval.

---

## 18. Naturalness Rewrite Pass（真人化重写）

After the factual draft is correct, run one naturalness rewrite pass.

Rewrite when ANY applies:
1. The sentence is correct but unlikely to be said face-to-face.
2. Three or more sentences have similar length or structure.
3. Every paragraph is complete and polished like a mini article.
4. The script relies on stock short-video phrases.
5. Abstract nouns replace concrete actions.
6. Pronouns make listening ambiguous.
7. Connectors are doing work that sentence order could do naturally.
8. The script sounds translated from English reasoning.
9. The persona disappears if account names are removed.
10. A sentence can be deleted with almost no information loss.

Final test:

> **先关掉字幕想象真人说一遍：现实里会这么说吗？**

If the answer is no, rewrite.
