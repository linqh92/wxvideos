# Chinese Spoken Naturalness（中式真人口语规则）

## 1. Scope（适用范围）

This reference applies ONLY to `spoken-copywriting`.

It controls how a valid content judgment is turned into natural Simplified Chinese that sounds like a real Chinese person speaking to another person.

It MUST NOT be inherited by `text-broadcast-copywriting` unless a future task explicitly changes that Skill.

Its job is NOT to change facts, business conclusions, account identity, topic logic, or add professional content that the topic does not require.

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

Naturalness MUST NOT weaken factual precision, hide a conclusion-changing condition, or broaden a narrow topic into a generic professional explanation.

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

Calibration example:

Written:

> 该方案在现有条件下并不适合继续推进，建议先核实关键参数后再作决定。

Spoken:

> 这个先别往下推。真正卡住你的不是流程，是前面那个关键参数还没确定。参数一变，后面的判断也会跟着变。

The example demonstrates speech transformation only. It is NOT a reusable structure.

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

Natural Chinese speech may mix:

> 短判断 + 正常解释 + 补一句 + 稍长条件句

This description is a listening characteristic, NOT a required four-part sentence pattern.

Example:

> 执照是办下来了。先别急着觉得事情结束了，后面还有几步要接。哪一步没接上，问题就可能从那一步回来。

Do NOT reuse the example's business objects by default.

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

> 这个能做。现在差的是条件，不是再补一堆解释。

> 先把这一项定下来。后面的，等它确定了再判断。

> 这里已经讲清楚了，到这儿就可以停。

Do NOT manufacture grammatical mistakes merely to look conversational.

---

## 6. Afterthought and Self-Repair（补一句与轻微自我修正）

Real speech may refine itself after the first statement.

Use this only when it improves precision or realism.

Natural forms include:

> 这个做法不太稳。准确一点讲，是你现在这个条件下不太稳。

> 也不能直接说一定不行，关键变量还没确定。

> 先看这个数。哦，还有一个前提得一起确认，不然这个判断下不完整。

Do NOT overuse self-correction as a performance trick.

Do NOT turn self-repair into a recurring account catchphrase.

---

## 7. Concrete Chinese Before Abstract Labels（先说具体，再说概念）

Prefer objects, actions, people, time, numbers and visible outcomes before abstract nouns.

Written:

> 当前方案存在执行路径不匹配的问题。

Spoken:

> 你现在按 A 的方式在做，后面的资料却是按 B 准备的，这两边接不上。专业上可以叫路径不匹配，但先把哪里接不上说清楚更重要。

Written:

> 企业应提升资料管理能力。

Spoken:

> 同一件事用到的资料先放到一起，谁负责、做到哪一步、还缺什么，一眼能看出来就行。

The examples show “concrete before abstract”. They do NOT define preferred account content.

---

## 8. Active Human Subjects（优先真人主动句）

Use a clear human, company, department, system or object as the subject when that improves comprehension.

Written:

> 相关资料应予以补充完善。

Spoken:

> 缺哪份就先补哪份，别一上来把整套东西全部重做。

Written:

> 该问题可能导致申请被退回。

Spoken:

> 这一项没满足，审核的时候就可能把申请退回来。

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
> 存在风险 → 容易卡 / 容易出问题 / 还要再确认

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

> 表面上看已经满足了。问题在后面那个条件，它一变，前面的结论就不能直接照搬。

Avoid:

> 当前条件已经满足。此外，需要注意的是后续条件可能发生变化。因此，应进一步进行综合判断。

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

> 这个先别急。  
> 其实吧，关键不在这里。  
> 你看，这两个数字已经对不上了。  
> 那这种情况，就得另外判断。

Do NOT assign quotas such as “three particles per paragraph”.
Do NOT force `啊、呢、吧、你看、说白了` into every script.
Do NOT reuse the same particle pattern merely because it sounded natural in a previous example.

---

## 12. Functional Repetition（功能性重复）

Chinese speech may repeat the same key noun rather than constantly replacing it with pronouns or synonyms.

Useful repetition:

> 这个比例先看基数。基数一变，同样的比例代表的东西就不一样。

Avoid decorative repetition:

> 这很危险，非常危险，真的特别危险。

Repeat for listening clarity, not emotional inflation.

Functional repetition applies to the CURRENT topic's key object. It does NOT justify repeatedly introducing the same professional objects across unrelated topics.

---

## 13. Questions（提问）

Questions are optional.

Use a question when a real speaker would naturally ask it to expose a missing condition or contradiction.

Good:

> 现在看着是符合。可这个条件能不能一直成立？这个才决定后面要不要调整。

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
- a consequence already happening;
- another form that is more natural for the current topic and persona.

There is no fixed preferred order.

Examples:

> 这事看着麻烦，其实先把一个条件搞清楚，结论就出来了。

> 同样是这个结果，换一个前提，处理方式可能完全不一样。

Examples demonstrate opening naturalness only. Do NOT reuse them as universal hooks.

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
- a consultation gap;
- an emotional uplift.

A natural ending may simply stop after:
- the final judgment;
- the first thing to verify;
- a condition that still needs confirmation;
- one practical action;
- the last sentence needed to make the current answer complete.

Examples:

> 所以现在先把这个条件定下来，别急着往后推。

> 这个比例如果后面还会变，现在就不用先下死结论。

> 关键资料没确定之前，这个答案就只能到这里。

Do NOT add another general checklist after the topic is already complete.

---

## 16. Before / After Calibration（改写前后语感标尺）

Use these examples to learn the transformation pattern, NOT to reuse the final wording, business objects, reasoning sequence, or conclusion pattern.

### Example 1｜去报告腔

Before:

> 对于初创企业而言，在经营初期应当充分重视财税合规管理，以避免后续产生不必要的风险。

After:

> 公司刚开始做生意，前面有些东西别随手处理。现在觉得省事，真有业务了，经常还得回来补。

### Example 2｜抽象变具体

Before:

> 企业应关注关键业务信息之间的一致性。

After:

> 同一件事是谁做的、做到哪一步、最后结果是什么，前后得接得上。哪一段突然换了口径，后面解释就会变麻烦。

### Example 3｜允许补一句

Before:

> 某项异常可能影响后续处理结果，企业应及时核查相关业务。

After:

> 这项异常确实可能影响后面的处理。  
> 不是说一出现就一定有问题，先看它到底碰到了哪一步，这个更重要。

### Example 4｜不强行三段式

Before:

> 首先核对基础信息，其次核对执行情况，最后结合结果进行综合判断。

After:

> 先别急着下结论。把最关键的那个条件拿出来，看它现在到底是什么状态。很多时候，这一个地方就已经能决定方向。

### Example 5｜去短句工厂

Avoid:

> 条件有了。数据有了。结果有了。资料齐了。问题还在。

Prefer:

> 看着东西都齐了，可真正决定结果的那个条件还没确定。前面再完整，也替代不了这一项。

Calibration examples MUST stay domain-light where possible.
Do NOT treat any example's nouns, order, or diagnostic method as preferred content for the account.

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

The same applies to professional frameworks:

> current topic  
> + current decisive variable  
> + only the necessary professional reasoning

not from a recurring industry checklist.

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
11. A narrow topic has been expanded into a broad professional checklist.
12. A recurring industry framework appears even though the current conclusion does not require it.
13. A calibration example has leaked into the final wording as a preferred noun set, sentence pattern, or reasoning sequence.
14. The script continues after the useful decision point only to make the content feel more complete.

Final tests:

> **先关掉字幕想象真人说一遍：现实里会这么说吗？**

> **再把行业通用框架拿掉看一遍：这个题本身还成立吗？如果成立，就别把那套框架硬说出来。**

If the answer is weak, rewrite.
