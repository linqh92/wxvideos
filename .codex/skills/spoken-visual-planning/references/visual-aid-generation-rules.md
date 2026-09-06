# Visual Planning and Execution Reference

Use this reference with `spoken-visual-planning`. The Skill owns routing, account context, confirmation and final delivery. `shared/rules/acquisition-and-fact-framing.md` owns claim identity and verification boundaries.

## Dual-Expression Model

Build the spoken track and the document track from one confirmed evidence set.

The spoken track selects what a person should say aloud to make the topic easy to follow. The document track organizes what a reader needs to understand the topic later. Shared facts, relationships and professional conclusions remain consistent even when sentence form, information density and sequence differ.

口播保留真实交流感，PPT 保留完整资料价值。完整指读者能够还原问题、理解关键关系、看清条件并知道结论怎样成立；页面数量与信息密度由内容决定。

## Entry-Cover Design

### Search cover — `COVER-01`

Design for recognition in a compact 3:4 list, search result or account grid. Lead with the confirmed topic value and a typographic hierarchy that remains legible at thumbnail size. Use composition, imagery, color and space to create a distinct editorial presence.

搜索场景首先解决“这条内容是否和我有关、是否值得点开”。标题承担主要信息，辅助文案补充必要对象、结果或条件。

### Recommendation-feed opening cover — `IMG-01`

Design the native 16:9 opening frame around immediate comprehension and a reason to stay. Use timing implied by hierarchy, contrast and composition. The page also serves as the shared deck's title page.

推荐流场景首先解决“我正在看什么、为什么值得继续”。停留理由来自选题冲突、结果、判断价值或信息缺口，并通过专业的编辑设计呈现。

Both covers are entry designs. Their imagery supports topic recognition, tone and memorability. Information visualization begins with the content pages.

## Standalone Document Architecture

Determine completeness from the current subject. Ask what an informed reader would still need after seeing the title and conclusion. Select the dimensions that materially improve understanding.

Useful dimensions include:

- context and scope;
- people, entities or objects involved;
- confirmed numbers, documents or evidence;
- sequence and dependencies;
- comparison, calculation or causal relationship;
- conditions that change the judgment;
- professional conclusion and practical next action.

Convert these dimensions into a deck narrative. A page may establish context, resolve one relationship, document evidence, explain a method or preserve reference detail. Page boundaries follow comprehension and later retrieval.

资料页可以承载口播中简要带过、但独立阅读时需要保留的背景、字段、条件和步骤。补充内容来自已确认材料或完成核验的来源。

## Information Design for Content Pages

Give each page one main document responsibility and decide the reader's first, second and supporting reads. Select a visual form after identifying the information relationship.

- Sequence may use steps, a route, a timeline or spatial progression.
- Comparison may use aligned columns, scales, paired structures or a table.
- Causality may use linked states, input-output structure or annotated evidence.
- Classification may use groups, matrices, fields or nested regions.
- A decisive conclusion may use typographic composition supported by concise evidence.

These are available forms, not presets. Photography, illustration, diagrams, native shapes, tables and editorial typography are chosen by the designer for the page's actual job.

Build continuity through a small set of stable relationships such as type character, color contrast, spacing rhythm, graphic treatment or confirmed brand assets. Let page layouts vary with their content while the deck still feels authored as one work.

## Page Copy and Typesetting

Maintain a `Page Copy` block for every page. It is the approved textual source for final production and includes headings, body text, labels, notes, figures, units and meaningful punctuation.

Write PPT copy for scanning and reference:

- headings state the page's judgment or subject;
- labels make relationships and ownership explicit;
- body text preserves necessary explanation and conditions;
- notes hold secondary qualifications without burying the conclusion;
- tables and diagrams use terms that remain clear outside the spoken context.

中文 PPT 文案以独立阅读为判断场景。标题可以比口播更凝练，说明文字可以比口播更完整；专业结论、数字、条件和事实身份保持一致。

Place copy according to reading order and realistic space. Long or accuracy-sensitive text belongs in an editable typesetting layer. Short display copy may be rendered inside a generated asset when the chosen tool can support the intended result.

## Production-Method Selection

Choose the method that best preserves the design and the content.

### Full-page generation

Use when the page relies on a unified visual scene or composition and contains a manageable amount of display text. The prompt describes the full native canvas, selected composition and visible copy.

### Generated visual plus editable type

Use when the visual benefits from image generation while the copy needs reliable typesetting or later revision. The prompt creates the relevant visual layer, including the space and relationship reserved for type. The guide specifies final copy and layout separately.

### Native page construction

Use when typography, tables, diagrams or structured fields carry most of the meaning. The guide describes layout, hierarchy and styling directly. Image prompts are included for supporting assets used in the design.

A deck may combine these methods while preserving one visual system.

## Prompt Distillation

Turn a resolved visual decision into a self-contained execution prompt. Start with the intended asset and native ratio, then describe the dominant composition, supporting elements, spatial relationships, visual character and any text rendered within the asset.

Write affirmative, outcome-focused instructions. Retain details that change recognition, hierarchy, relationships or visual appearance. Combine repeated style information and resolve alternatives before delivery.

Each prompt carries the context required to produce its own asset. It does not depend on another page ID, an account file or an earlier explanation. Shared appearance is expressed through the relevant visual traits on that asset.

For generated text, list the confirmed Simplified Chinese copy with its position and hierarchy. For editable type, describe the reserved text region, contrast and composition while the exact copy remains in `Page Copy`.

生成画面中的中文只承担已经确定的展示任务。页面资料文字以 `Page Copy` 为准，图像提示词负责其实际生成范围内的文字和视觉结果。

## Execution Guide Format

Use the following structure for each page:

~~~markdown
## IMG-02｜<页面名称>

- Ratio: 16:9
- Role: content page
- Use: video_and_share | share_only
- Production method: full-page generation | generated visual + editable type | native page construction

### Page Copy

<完整页面文案，包括标题、正文、标签、数据与必要备注>

### Information and Composition

<阅读顺序、信息关系、版式、视觉重量、图形或图像职责、页间连续性>

### Image Prompts

```text
<当前执行方式需要的完整、自足提示词；没有生图资产时写 None>
```
~~~

Apply the same structure to `COVER-01` and `IMG-01`, using their distinct entry roles. The document begins with the confirmed deck direction and visual system, followed by pages in final order.

## Video Segmentation

`剪辑分段表.md` maps the spoken sequence to pages marked `video_and_share`. Start with `IMG-01`; the 3:4 search cover stays outside the video timeline. Use verified audio times when audio exists and spoken start/end phrases when planning from a script.

The mapping covers the full spoken track in order. A page may remain on screen across several spoken sentences when that supports comprehension. Pages marked `share_only` remain in the PPT execution guide and outside the video segmentation table.

## Review with Generated Evidence

Text review verifies content architecture and execution clarity. Generated samples provide evidence about composition, legibility and model behavior.

Inspect cover recognition at thumbnail or first-frame size. Inspect content pages at video size and full document-reading size. Classify a problem as content hierarchy, layout choice, prompt ambiguity, text-rendering limitation or model execution variance, then revise the responsible layer.

When the user authorizes a generation test, select pages that represent the actual uncertainty: one entry cover, one information-dense page or one complex relationship page as appropriate. Keep test observations outside the final execution guide.
