---
name: text-broadcast-copywriting
description: Generate finalized WeChat Video Account text-broadcast / subtitle copy from a confirmed topic. Inherit the locked account context and shared copywriting rules. Use for 短文字幕、文字播报、打字字幕短视频. Do not use for spoken-camera scripts, topic planning, inspiration intake, publication archiving, or visual production.
---

# WeChat Video Account Text-Broadcast Copywriting（微信视频号短文字幕文案生成）

## Trigger

Use only for `CONTENT_FORMAT=text_broadcast`: generate 短文字幕、文字播报, or 打字字幕 copy from a confirmed topic.

Do not use when the user requests 口播、真人口播、出镜讲, or 口播稿.

## Required Input

- A confirmed topic or a clear topic supplied directly by the user;
- The requested title, body copy, or complete package mode;
- `CURRENT_ACCOUNT` and `CONTENT_FORMAT=text_broadcast` resolved under root `AGENTS.md`.

## Required Context

Account selection, isolation, content-format routing, and stage boundaries follow root `AGENTS.md`.

Before drafting, read and obey:

```text
1. shared/rules/acquisition-and-fact-framing.md
2. shared/rules/copywriting-common-rules.md
```

The shared rules control account and persona inheritance, audience language, business boundaries, information gap, emotion, expression intensity, fact verification, platform boundaries, titles, CTA, common quality control, and scoring.

This file defines only text-broadcast-specific execution constraints. When rules conflict, follow the user's explicit request, current-account rules, and shared rules in that order.

## Unique Logic

### Content Medium（内容载体）

Text-broadcast content is presented through line-by-line text, short subtitles, or a typing effect. The audience receives the information primarily through visual reading, without relying on a real speaker's voice, expression, or performance.

Therefore, the copy MUST:

- optimize information order, sentence length, and line breaks for visual reading;
- communicate one judgment quickly through a single-point, high-density structure;
- establish a clear information gap, impact, result, or cognitive conflict on the first screen;
- preserve final line breaks that can be handed directly to post-production.

Do NOT write a spoken-camera script, long article, official document, training material, consulting report, encyclopedia explanation, or generic AI summary.

---

### First Screen（第一屏）

The first screen supports retention, immediate relevance, and information-gap recognition. It MUST contain no more than 4 lines and prioritize at least one of the following:

- a direct result;
- a direct conclusion;
- a real benefit or loss;
- correction of a common wrong judgment;
- a strong, valid information gap.

When choosing the opening information, prefer this order when it fits the topic:

1. direct result;
2. clear conclusion;
3. cognitive conflict;
4. audience benefit or loss;
5. valuable number;
6. concrete scene conflict;
7. a question with real decision value.

A scene or audience object may appear, but it MUST NOT delay the core conclusion merely for “代入感”. If the first 2–4 lines still contain only background, emotion, questions, setup, or a restatement of the visible situation, the opening fails.

Do NOT use greetings, course-like introductions, or template reminders as the only opening value. Reduce weak hooks such as “很多老板不知道”“这个问题需要注意”“今天来说一下”“最近有人问” unless a high-value conclusion follows immediately.

Non-critical conditions may appear later, but every conclusion-changing condition must remain visible in time.

---

### Single-Point High Density（单点高密度）

Default main-copy flow:

```text
Strongest valid information or cognitive conflict
→ Direct conclusion
→ Audience benefit, loss, or practical result
→ Reason or core mechanism
→ Conclusion-changing condition
→ Final judgment or one action direction
```

Not every piece must display every step. Each sentence must perform at least one function: fact, number, object, behavior, information gap, reason, condition, impact, judgment, audience result, or action direction.

Delete any sentence whose removal does not reduce useful information. Do NOT develop multiple logic threads for completeness or stack familiar observations, background, definitions, transitions, repeated conclusions, or persona performance with no information function.

---

### Main-Copy Modes（正文模式）

Select automatically based on the topic. Do not default to one fixed template:

- **Outcome-First（结果直击型）**: Result → Clear conclusion → Reason → Critical condition → Audience result;
- **Cognitive Correction（认知翻转型）**: Common judgment → Direct correction → Supported conclusion → Critical condition → Practical result;
- **Accumulation Escalation（累积升级型）**: Current situation → Accumulation path → Amplified result → Clear conclusion → Current action;
- **Chain Propagation（链条传导型）**: Starting problem → Intermediate impact → Audience result → Critical break point → Clear conclusion;
- **Numeric Comparison（数字对比型）**: Number or ratio → Direct difference → Clear conclusion → Critical condition → Audience benefit or loss;
- **Decision Comparison（决策比较型）**: Two choices → Core difference → Different results → Clear decision standard;
- **Event Impact（事件影响型）**: Verified event → Affected audience → Change → Practical impact → Current judgment or action.

Do NOT invent a change, trend, or result merely to fit a mode. Events, policies, and platform changes require current verification before use.

---

### Text-Broadcast Length（短文长度）

Priority:

1. user-specified length or reference length;
2. explicit current-account length rules;
3. this Skill's default.

When unspecified, the body defaults to approximately 90–130 Chinese characters. If a rule, professional judgment, or business chain is complex, narrow the angle first and keep only one core judgment. Extend to approximately 160 Chinese characters only when accurate compression is genuinely impossible. Do not default to more than 200 Chinese characters.

Before exceeding the default length, check for repeated known information, excessive background, ineffective setup, too many questions being explained at once, removable connectors, splittable long sentences, or content added merely to appear professional.

---

### Per-Piece Information Limit（单篇信息上限）

- Express only one core conclusion;
- Use at most one core pressure point or benefit point;
- Explicitly develop no more than three judgment conditions;
- Explain at most one professional concept;
- Keep only one result, risk, or action direction;
- Do not repeat the same conclusion in different wording;
- Do not add complete rule background or operating steps merely to appear professional.

When multiple necessary conditions exist, develop only those directly relevant to the current scenario and preserve the others as concise boundaries. Compression MUST NOT hide a condition that changes the conclusion.

---

### Visual Reading and Line Breaks（视觉阅读与换行）

The body MUST preserve final line breaks that can be used directly for text broadcast:

- one core information unit per line;
- 10–16 lines by default;
- preferably 7–15 Chinese characters per line;
- important numbers, results, or judgments may stand alone;
- prefer line breaks at condition, result, or logic changes;
- check whether any sentence longer than 30 Chinese characters can be split;
- preferably 2–4 lines per information block;
- no more than 4 lines on the first screen, with a concrete conflict, result, or judgment established;
- do not stack more than two explanatory information blocks consecutively;
- no more than 3 lines in the ending;
- do not hand a solid paragraph to post-production for later splitting;
- do not break complete meaning merely to create short lines.

Stronger expression may come only from earlier conclusions, more direct results, and reduced setup. Do not increase body length merely to increase intensity.

Use numbering only when parallel information, steps, or checks genuinely become easier to scan. Do not default to a fixed-size list.

## Quality Gate

### Text-Broadcast Quality Control（短文专项质检）

Rewrite if ANY applies:

- the first screen lacks the strongest valid information, or its first 2–4 lines contain only background, emotion, questions, setup, or restated observations;
- a discussion hook is treated as a determinative case despite an adjacent discussion cue;
- a requested reference's strongest number, result, loss, audience callout, or suspense is removed without a role-based reason;
- a result-first discussion hook is softened into a generic question only because it lacks an official case source;
- a generated precise case is disguised with hearsay language;
- the shared explicit-conclusion check fails in visual-only reading, so the audience still cannot answer the topic;
- conditions, policy, or terminology occupy most lines, making the body a list of considerations rather than an answer;
- a supported conclusion is weakened, delayed until the second half, or replaced by a generic reminder;
- multiple core conclusions or logic threads are developed;
- the draft reads like an article, report, training material, or longer spoken script;
- sentences are too long for line-by-line display;
- final line breaks are missing or break complete meaning;
- the default body has fewer than 10 or more than 16 lines without a valid reason;
- line lengths remain too short or too long and damage reading rhythm;
- the first screen exceeds 4 lines before establishing a concrete conflict, result, or judgment;
- the body exceeds 130 Chinese characters before the topic angle has been narrowed;
- rule background, definitions, irrelevant conditions, or a second result reminder are added for completeness;
- numbering, parallel sentence patterns, or repeated conclusions are used mechanically.

After the first draft, run one mandatory reduction pass:

1. remove repeated conclusions;
2. remove rule background and definition-style explanations;
3. remove conditions that do not change the core judgment;
4. remove transition-only sentences;
5. remove the second and later result reminders or CTAs;
6. when the body exceeds 130 Chinese characters, narrow the scope instead of mechanically shortening sentences to force all information in.

## Output

Follow the user's requested output strictly. Do not append unrelated content.

### Titles Only（只要标题）

Output title options only. Do not include reasons, scoring, or risk analysis unless requested.

### Body Copy Only（只要正文）

Output only the body copy with final visual line breaks. By default, do not expose mode names, scoring, risk analysis, or creative explanation. Add one brief note after the body only when a factual risk or verification limitation must be disclosed for correctness.

### Complete Package（要完整文案）

By default, output only:

1. three clearly different title directions;
2. one standard/search-recognition title;
3. one short title;
4. one finalized body with text-broadcast line breaks.

Do NOT output the creative process, internal judgment, persona parameter checklist, long source list, unrelated topics, visual production plan, or archive operations.

## Stop

Before delivery, confirm that an audience reading without sound can quickly obtain one complete judgment and answer “所以这件事到底会怎样” in one sentence. The audience must receive an answer, not merely a list of considerations.

The first screen must contain the strongest valid information. The body must remain single-point and high-density. Conditions must define the conclusion rather than hide it, and line breaks must be directly usable. If the result is merely a spoken script cut into multiple lines, rewrite it.

After delivering the requested titles, body copy, or complete package, stop. Do not re-plan the topic, mark content as published, write to history, update the content map, archive automatically, or produce visual assets.
