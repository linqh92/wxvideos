---
name: spoken-visual-planning
description: Plan a search cover, a recommendation-feed opening cover, and a standalone readable PPT document from confirmed spoken content and its approved source material. Use only for explicit PPT视觉、PPT配图、视觉分镜、PPT执行指南 or AI生图提示词 requests after the spoken script is confirmed. Confirm the complete deck content and direction before producing the execution guide and video segmentation table.
---

# Spoken Visual Planning

## Job

Act as the senior designer and information editor for one confirmed spoken topic. Build two coordinated expressions from the same facts:

- the spoken track explains the topic through natural, selective conversation;
- the document track preserves a complete, structured account that remains useful when read without the speaker.

口播像课堂上的现场讲解，负责用真实交流带观众抓住重点；PPT 像课后可分享的资料，负责把背景、关系、条件、过程、判断与行动信息组织完整。两者共享事实和结论，各自按使用场景形成内容。

## Page Responsibilities

Treat the three page types as different design jobs.

| Page type | Communication job | Design focus |
| --- | --- | --- |
| `COVER-01` — native 3:4 search cover | Attract relevant attention in search results, account grids and content lists | Immediate topic recognition, typographic hierarchy, editorial composition and distinctive design character |
| `IMG-01` — native 16:9 recommendation-feed opening cover | Create a reason to stay when the video opens in the recommendation feed | Fast theme recognition, tension, pacing and a strong first-frame composition |
| `IMG-02+` — native 16:9 content pages | Support the live explanation and preserve the complete document for later reading | Information architecture, relationships, evidence, reading order and page-to-page continuity |

搜索封面与推荐流封面承担入口设计。主题文字是第一识别对象，图像、图形、空间和背景共同建立气质与记忆点。吸引力来自内容价值与编辑设计。信息可视化属于内容页的职责。

## Trigger and Boundary

Use this Skill only when a confirmed spoken script or final audio exists and the user explicitly requests PPT pages, visual storyboarding, supporting visuals, a PPT execution guide or image prompts. Account locking and stage routing follow the root `AGENTS.md`.

The confirmed spoken track remains intact. This stage creates separate PPT copy and page structure from the same approved facts and professional conclusions.

This stage ends with the execution guide and segmentation table. Image generation, editable PPT production, video editing, publishing and archiving are separate stages.

## Required Context

After resolving `CURRENT_ACCOUNT`, read:

1. `shared/rules/acquisition-and-fact-framing.md` for claim identity, verification and acquisition framing;
2. `accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号基本定位.md` for business, audience and communication goals;
3. `accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号人设与文风.md` for the speaker's professional relationship and credibility;
4. `accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号视觉风格.md` for confirmed brand assets and visual fact boundaries;
5. the confirmed spoken script or final audio;
6. source material already approved for the current topic, when available;
7. `references/visual-aid-generation-rules.md` for document architecture, execution choices and delivery details.

When the user references an incoming Handoff, validate it with `shared/schemas/handoff-packet-schema.md`. Its `account_id` establishes the account candidate, which must still pass the root account lock; its confirmed spoken copy is the sole prior-stage working result. Do not load `spoken-copywriting`, `topic-planning`, recommendation memory, planning indexes, history searches, rejected drafts or the earlier chat. Only load source paths explicitly listed in the Handoff when they are necessary to preserve a fact or conclusion.

Use only facts supported by the confirmed script, approved source material or verified official sources. Surface a material information gap during content confirmation when it prevents the document track from standing on its own.

Account context explains who is speaking, who should care and what trust means in this situation. The designer derives the visual system from the current topic rather than mechanically mapping age, gender, seniority or personality to a style.

## Workflow

### Phase 1 — Content Architecture and Direction

#### 1. Establish the shared content baseline

Read the spoken track and its approved sources as one evidence set. Identify the confirmed topic, audience, case or scenario, decisive facts, relationships, conditions, professional conclusion and useful next action.

Keep the spoken track conversational. Write the document track for independent reading. The PPT may reorganize, label, group and clarify the confirmed material while preserving its factual role and conclusion-changing conditions.

#### 2. Build the standalone deck narrative

Choose the information chain that makes this particular topic complete. Depending on the material, this may include context, actors, data, sequence, comparison, causality, decision conditions, result, evidence, method or action guidance. These are design considerations rather than a page template.

Give every content page one clear document responsibility. Mark its use as:

- `video_and_share`: shown during the spoken video and retained in the shared deck;
- `share_only`: useful for the complete document and not required in the video sequence.

The deck should remain coherent when `share_only` pages are included and the video should remain coherent when they are omitted.

#### 3. Design the two entry covers

Develop `COVER-01` and `IMG-01` independently from their communication jobs. Select the strongest confirmed topic value, then shape the title, supporting line, typography, composition, imagery and atmosphere for the relevant entry context.

Use editorial judgment to make the text hierarchy the first carrier of meaning. Supporting visuals should strengthen recognition, tension or tone without turning either cover into a content diagram.

#### 4. Define the content-page system

Set the visual foundation and continuity language for the deck. Decide how type, space, color, imagery, diagrams, tables, cards, timelines, process structures or other forms can express the actual information. Each page selects the form that best fits its responsibility.

#### 5. Present the confirmation package

State the chosen direction, page-count rationale, deck narrative and continuity system. Then present:

`本次建议整理为 1 张3:4搜索封面 + 1 张16:9推荐流/PPT封面 + X 张16:9内容页。`

| Page | Confirmation content |
| --- | --- |
| `COVER-01` | 搜索场景、主标题、辅助文案、主题价值与封面概念 |
| `IMG-01` | 推荐流开场场景、主标题、辅助文案、停留理由与封面概念 |
| `IMG-02+` | 页面用途、页面职责、完整PPT文案、信息关系与构图概念 |

The confirmation package contains the complete visible PPT copy, page order, page use, visual direction and page concepts. Stop after presenting it and wait for explicit user confirmation.

### Phase 2 — Page Resolution and Execution Guide

#### 1. Resolve each composition

Complete each confirmed page at its native ratio. Covers are judged as entry designs. Content pages are judged as document pages with a clear reading path, complete information and an intelligible relationship between text and visuals.

Build hierarchy through the whole composition. Page density, visual weight, whitespace and form follow the amount and shape of the information. Cross-page unity comes from the selected visual system; individual layouts respond to their page responsibilities.

#### 2. Choose the execution method

Select the production method page by page:

- a full-page image prompt when the composition and copy load suit direct generation;
- generated visual material combined with an editable typesetting layer when text accuracy, density or future editing matters;
- native layout elements when type, tables, diagrams or structured relationships are the primary content.

The execution guide records the chosen method and enough detail for another designer or production agent to build the page faithfully.

#### 3. Distill image prompts

Write prompts only for the visual assets or full-page images used by the chosen execution method. Describe the selected visual result, composition, atmosphere, relationships and relevant visible copy in affirmative, self-contained language.

The confirmed `Page Copy` section is the text source of truth. Include exact Chinese text inside an image prompt when that text belongs in the generated asset. Keep editable typesetting copy in the page specification and describe the space it occupies in the composition.

#### 4. Review the complete system

Check the two entry covers in their own contexts, the standalone readability of the full deck, the spoken-video sequence, factual consistency, page-to-page continuity and the executability of every page specification.

## Quality Review

- **Search cover**: a relevant viewer can recognize the topic value quickly in search, profile or list contexts; typography and composition carry the attention decision.
- **Recommendation-feed cover**: the opening frame establishes the subject and a credible reason to continue watching.
- **Standalone document**: a reader can understand the topic, important relationships, decisive conditions, conclusion and useful action without hearing the spoken track.
- **Video sequence**: pages marked `video_and_share` support the spoken pacing and remain readable at viewing size.
- **Information integrity**: every claim keeps its confirmed role, source scope and conclusion-changing conditions.
- **Execution clarity**: page copy, hierarchy, layout, production method and any required image prompts form one coherent instruction set.

Actual generated-image quality requires image evidence. Apply the reference's image-feedback method when samples are available or the user authorizes a generation test.

## Output

After confirmation, create and deliver two Markdown files as shared files in the ChatGPT project. These visual-stage files remain outside the Repo and must not be written to an account attachment directory, added to GitHub, indexed or included in a later repository sync.

1. `<角色><内容简称>PPT设计执行指南.md`: use the current account's public short role name and a 2–5 Chinese-character content name.
2. `剪辑分段表.md`: map only pages used in the spoken video to spoken ranges or verified audio times.

The execution guide contains the final page system and one section per page:

- page ID, ratio, role and use;
- complete `Page Copy`;
- information hierarchy and composition;
- selected production method;
- image prompt blocks required by that method.

Use `COVER-01` for the native 3:4 search cover, `IMG-01` for the native 16:9 recommendation-feed/PPT cover, and `IMG-02+` for native 16:9 content pages.

The segmentation table starts from `IMG-01`, includes only `video_and_share` pages and covers the full spoken sequence in order. Use actual timestamps for final audio and spoken start/end phrases when only the script exists.

Both documents describe the final deliverable. Design exploration, internal scoring and process notes stay outside them.

## Stop

End after delivering the two ChatGPT-project documents. Do not generate a Repo Handoff or `pending_repo_actions` for visual files. Continue to image generation, PPT production, editing, publishing or archiving only through the corresponding user-requested stage and a separate conversation when one exists.
