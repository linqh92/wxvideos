---
name: project-optimization-minimal-change
description: Apply minimal-change discipline when users ask to modify, adjust, optimize, fix, refine, simplify, correct, or partially redesign an existing project, workflow, rule, agent, prompt system, automation, document structure, or implementation. Preserve working behavior and avoid unrelated redesign.
---

# Project Optimization — Minimal Change Discipline

## Purpose

Use this skill whenever an existing project, workflow, rule, agent, prompt system, automation, document structure, or implementation needs to be:

- adjusted
- optimized
- fixed
- refined
- simplified
- corrected
- partially redesigned
- made more reliable

This skill is specifically designed to prevent over-expansion during high-reasoning model execution.

The default goal is:

> Fix the smallest responsible part of the existing system while preserving everything that already works.

Optimization does **not** automatically mean redesign.

---

## Core Principle

### Minimal Effective Change

Before proposing any solution, assume that the problem may be local.

Do not expand the problem into an architectural, workflow-wide, or system-wide issue unless evidence requires it.

Always prefer:

`local fix → local rule adjustment → local workflow adjustment → structural change → architecture redesign`

Move to the next level only when the previous level cannot reliably solve the problem.

The burden of proof is on expansion.

---

# 1. Scope Control

## Default Behavior

When receiving an optimization or adjustment request:

1. Identify the exact observed problem.
2. Identify the smallest project element directly responsible for it.
3. Check whether modifying only that element can solve the problem.
4. Preserve unrelated rules, files, stages, behaviors, and interfaces.
5. Expand scope only when a dependency makes the local fix insufficient.

Do not begin by redesigning the surrounding system.

---

## Scope Classification

Before implementation, internally classify the required change.

### Level 1 — Point Fix

A single:

- condition
- instruction
- field
- parameter
- naming rule
- trigger
- output requirement
- validation rule
- file operation

can solve the issue.

Preferred whenever possible.

### Level 2 — Local Rule Fix

Several closely related rules inside one module, stage, document, or skill need modification.

No unrelated workflow stages should change.

### Level 3 — Local Workflow Fix

The issue crosses several directly connected steps of one workflow.

Modify only those connected steps.

### Level 4 — Structural Fix

A shared abstraction, interface, or system structure is genuinely responsible for repeated failures.

Use only when Levels 1–3 cannot reliably resolve the problem.

### Level 5 — Architecture Redesign

Reserved for cases where the existing architecture itself prevents the required behavior.

Never choose this level merely because a cleaner architecture is imaginable.

---

## Expansion Guard

Before proposing a structural or architectural change, verify:

- Is the current failure reproducible outside the local point?
- Does the local fix create a known inconsistency?
- Are multiple independent modules affected?
- Is the existing structure preventing the intended behavior?
- Would the larger change materially reduce future failure rather than merely look cleaner?

If the answer is mostly no, stay local.

---

# 2. Preserve Existing Behavior

Existing project behavior is assumed intentional unless explicitly identified as defective.

Do not casually:

- rename unrelated files
- reorganize folders
- rewrite working rules
- introduce new abstractions
- replace established terminology
- merge stages
- split stages
- create new schemas
- add validation layers
- introduce new handoff documents
- add configuration systems

A proposed improvement is not automatically justified by conceptual cleanliness.

Prefer compatibility over theoretical elegance.

---

# 3. Separate Problem Analysis from Project Rules

Optimization discussions may contain:

- debugging history
- failed attempts
- hypotheses
- temporary reasoning
- user feedback
- model mistakes
- alternative approaches
- discarded solutions
- conversational clarification

These are **working context**, not project rules.

They must not automatically enter permanent project documents.

---

## Permanent Documentation Rule

A project-facing document should contain only information required for future execution.

Usually this includes:

- final rule
- final behavior
- trigger condition
- input requirement
- output requirement
- execution sequence
- exception
- validation condition
- file/path convention
- dependency
- compatibility constraint

Do not include conversational history unless the document is explicitly intended to be:

- an incident report
- debugging report
- decision record
- retrospective
- migration note
- changelog

---

## Forbidden Documentation Noise

For normal project rule documents, avoid sections such as:

- Background of this discussion
- Why we discussed this
- Previous attempts
- Iteration process
- Conversation summary
- What the user said earlier
- Version-by-version reasoning
- Problems we encountered during this chat
- Alternative solutions considered
- Model thought process
- Optimization journey

Do not preserve information merely because it appeared in the conversation.

---

## Final-State Documentation

Write documentation from the perspective that the final rule already exists.

Prefer:

> When generating a visual-planning handoff, save the resulting Markdown file to the project Library folder.

Avoid:

> Previously the visual-planning stage did not save the document, so after discussion we decided that from now on...

Documentation describes the system.

It does not narrate the conversation that produced the system.

---

# 4. English-First Project Documentation

Project logic, rules, workflows, schemas, interfaces, and execution instructions should default to English.

Use English for:

- headings
- rule definitions
- workflow descriptions
- state names
- stage names
- field descriptions
- conditions
- implementation logic
- validation logic
- file operations
- agent instructions
- technical explanations
- comments that describe system behavior

---

## Chinese Usage Rule

Chinese is allowed only when it carries project semantics that would become less precise if translated.

Typical valid cases:

### User-facing literal content

Examples:

- `"选题交接"`
- `"视觉规划"`
- `"引导咨询"`
- `"短文内容方案"`

Keep Chinese when these strings are actual UI labels, filenames, content types, or business terms used by the project.

### Semantic clarification

When an English term cannot fully preserve a Chinese business meaning, use:

`English description (必要中文语义)`

Example:

> consultation CTA (`引导咨询`)

### Literal matching

When implementation depends on an exact Chinese string, preserve that exact string.

Example:

```text
If the document contains the literal section "引导咨询", exclude that section from visual planning.
```

---

## Avoid Full-Chinese Technical Documentation

Do not write the entire project rule document in Chinese simply because the user communicates in Chinese.

Communication language and project-document language are separate concerns.

Default:

- conversation with user → Chinese
- project SKILL / rule / workflow documentation → English
- project-specific Chinese semantics → retain only where necessary

---

# 5. High-Reasoning Model Restraint

High reasoning capability should improve diagnosis, not increase change scope.

Do not convert deeper reasoning into larger implementation.

Use additional reasoning to answer:

- What is the actual failure point?
- What is the smallest reliable fix?
- What must remain untouched?
- Is the proposed complexity necessary?
- Am I solving the reported problem or redesigning the project?

The model may internally consider broader possibilities, but the final implementation must remain proportional to the actual problem.

---

## Complexity Is Not a Quality Signal

Do not treat these as inherently superior:

- more rules
- more files
- more agents
- more abstraction
- more stages
- more validation
- more fallback logic
- more documentation
- more configuration

A one-line rule change can be better than a new subsystem.

---

# 6. Optimization Execution Workflow

For every project adjustment, use this sequence.

## Step 1 — Define the Observable Problem

Reduce the request to one concrete failure statement.

Example:

> The visual-planning stage creates a handoff document but does not persist it to the project's Library folder.

Do not broaden it yet.

---

## Step 2 — Locate the Responsible Rule

Find the exact:

- skill
- instruction
- stage
- function
- condition
- document rule
- file operation

that controls the failing behavior.

---

## Step 3 — Test the Smallest Fix

Ask:

> If only this rule changes, will the intended behavior become correct without breaking existing behavior?

If yes, stop expanding.

---

## Step 4 — Check Dependencies

Inspect only directly connected dependencies.

Do not inspect unrelated parts of the project merely to produce a more comprehensive optimization.

---

## Step 5 — Implement the Change

Modify the smallest responsible surface.

Preserve existing structure whenever possible.

---

## Step 6 — Clean the Documentation

Before writing or updating project documentation, remove:

- reasoning history
- discussion history
- rejected options
- temporary hypotheses
- redundant explanation
- model-specific commentary

Keep only executable future-state information.

---

## Step 7 — Language Pass

Check the final project document:

- Is core project logic written in English?
- Are Chinese phrases limited to necessary project semantics?
- Are exact Chinese literals preserved where implementation depends on them?
- Has conversational Chinese leaked into technical rules unnecessarily?

---

## Step 8 — Scope Verification

Before completion, verify:

> Did this task modify anything that was not necessary to solve the stated problem?

If yes, remove or justify it.

---

# 7. Proposed Change Format

When presenting an optimization plan, prefer this compact structure:

```text
Observed issue:
<exact failure>

Responsible area:
<smallest responsible component>

Required change:
<minimal modification>

Unchanged:
<important surrounding behavior that remains intact>

Reason:
<why the local fix is sufficient>
```

Do not produce a large redesign proposal unless requested or required.

---

# 8. Documentation Output Rules

When generating a permanent project document:

### Include

- Purpose
- Trigger
- Rules
- Workflow
- Inputs
- Outputs
- Exceptions
- Validation
- File operations
- Compatibility constraints

Only include sections that are actually necessary.

### Exclude by default

- discussion notes
- iterative history
- conversational context
- explanation of how the solution was discovered
- abandoned alternatives
- user/model dialogue
- unnecessary rationale
- generic best practices unrelated to execution

---

# 9. Change Boundary Declaration

For adjustment tasks, explicitly identify what is outside the requested change boundary.

Example:

```text
Change boundary:
Only modify the persistence behavior of the visual-planning handoff document.

Do not modify:
- content-generation rules
- visual-planning logic
- filename schema
- repo output behavior
- other handoff stages
```

This boundary should guide implementation, not necessarily appear in every permanent document.

---

# 10. No Opportunistic Refactoring

While fixing one problem, do not automatically fix nearby imperfections.

Do not perform:

- unrelated cleanup
- naming normalization
- stylistic rewrites
- folder restructuring
- schema modernization
- prompt consolidation
- duplicated-rule elimination

unless they are necessary for the requested fix.

Potential improvements may be mentioned separately, but they must not silently enter the implementation.

---

# 11. Evidence-Based Expansion

A broader optimization is allowed when there is concrete evidence that the same underlying defect affects multiple places.

Example:

Three workflow stages independently fail because they rely on the same missing persistence contract.

In that case, changing the shared contract may be smaller and safer than patching all three stages.

The principle remains:

> Choose the smallest change that solves the actual shared cause.

Minimal change does not mean blindly editing the fewest lines.

It means minimizing unnecessary system impact.

---

# 12. Output Restraint

Do not over-explain simple fixes.

Match explanation size to change size.

For a small rule correction, a short explanation is preferred.

For a structural change, more explanation is justified.

Do not create extensive documents merely because the model has enough reasoning capacity to do so.

---

# 13. Final Self-Check

Before completing an optimization task, verify all of the following:

- [ ] I identified the actual failure rather than an imagined larger problem.
- [ ] I attempted the smallest viable fix first.
- [ ] I did not redesign unrelated project components.
- [ ] Existing working behavior remains unchanged.
- [ ] Permanent documentation describes the final system, not the conversation.
- [ ] Iteration history and discussion noise were removed.
- [ ] Core project logic is written in English.
- [ ] Chinese appears only where semantic precision or literal matching requires it.
- [ ] I did not perform opportunistic refactoring.
- [ ] The implementation complexity is proportional to the problem.
- [ ] Any expanded scope is supported by a real dependency or shared root cause.

If any item fails, revise before delivery.

---

# 14. Priority Rules

When instructions conflict, use this priority:

1. Explicit user requirement
2. Existing project contract
3. Preserve working behavior
4. Minimal effective change
5. Local consistency
6. Architectural elegance

Architectural elegance must never override a smaller valid fix.

---

# 15. Default Decision Rule

When uncertain between:

**A. Modify one existing rule**

and

**B. Introduce a broader mechanism that could solve similar future problems**

choose **A** unless the broader mechanism is already required by demonstrated failures.

Do not solve hypothetical future problems during a local optimization task.

---

## Final Operating Principle

> Reason broadly. Diagnose precisely. Change narrowly. Document only the final system.

For high-reasoning models, additional intelligence should primarily reduce unnecessary changes, not produce larger ones.
