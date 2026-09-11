# Living line-of-argument artifacts

## Purpose

Maintain the writer's current argumentative intent outside the prose so that drafting and revision do not depend on reconstructing it afresh in every turn. The artifact should make changes to central concepts and their relations visible before those changes propagate through the draft.

Use this workflow for a substantial argumentative article or section that is stored in a project, for multi-round drafting, or whenever the writer explicitly requests a living outline or persistent argument context. Do not create one for a short isolated paragraph, purely local language edit, or review comments with no drafting project unless the writer asks for it.

## Location and name

Keep the artifact beside the draft or at the root of the writing project. Use the project's established naming convention. Otherwise prefer `line-of-argument.md` for an English project and `论证线.md` for a Chinese project. If a directory contains several unrelated drafts, first give the piece its own folder or use a filename that unambiguously identifies the draft.

## What it records

Record only the current structure needed to write and review the argument:

- the artifact's review status;
- the governing question or rhetorical action;
- a compact rhetorical situation: the intended reader's starting position, the desired writer-reader relationship, the overall movement the prose should create, and reliable evidence of voice;
- the writer's current central judgment, including its degree of certainty;
- the core concepts and the meanings they have in this piece;
- the claim path, with the relation between adjacent movements stated explicitly;
- each section's or passage's writing job and its relation to what precedes and follows;
- writer-supplied examples, established source material, or other evidence assigned to each movement;
- consequential model proposals, author decisions, and source checks that remain open;
- explicit boundaries that prevent a claim from becoming broader or stronger than intended.

Represent the claim path in the clearest economical form. Arrows are useful only when their labels state real relations such as `explains`, `qualifies`, `contrasts with`, `supports`, or `therefore`; spatial adjacency alone is not a relation. A compact table or nested outline may be clearer when several concepts recur across sections.

Do not turn the artifact into a prose summary, sentence-by-sentence plan, source dump, revision history, task tracker, or archive of rejected branches. Version control or existing project records can preserve history. Keep rejected reasoning only when forgetting the rejection would create a realistic risk of repeating it.

The rhetorical situation is durable orientation, not a paragraph-by-paragraph script. Do not preselect a rhetorical question, connective, anecdote, or cadence for every argument node. Those local choices belong to rhetorical drafting and may change as the prose develops without changing the line of argument.

## Authority and review status

The writer's latest instruction or correction outranks the file. A source can establish facts but does not decide the writer's evaluation. The artifact becomes drafting authority only to the extent that the writer has supplied or reviewed its substantive content.

Use a visible binary status such as:

- `Review draft` / `待审阅`: set whenever Codex creates or changes any content in the artifact;
- `Writer-confirmed` / `已审阅`: set only by the writer after inspecting the current artifact.

Every Codex modification resets the whole artifact's visible status to awaiting review, including an edit that merely incorporates explicit writer comments or makes a low-risk clarification. Codex must not mark the revised artifact reviewed, preserve its reviewed status, or restore that status on the writer's behalf. Stable portions do not need to be reconsidered substantively, but the file as a current version remains unreviewed until the writer personally changes the marker.

Do not label the artifact final. A later correction changes only the affected relations and downstream sections, but the status reset still applies to the artifact as a whole.

## Update cycle

### Establish before prose

Create the artifact from the writer's actual brief, notes, headings, judgments, and established source packets. Distinguish structural elaboration from a model-proposed thesis, reason, premise, evaluation, or conclusion. When a consequential proposal remains open, return the artifact for review and stop before prose unless the writer explicitly asked for immediate drafting or for outline and prose together.

### Consult before substantive work

Before drafting, continuing, or materially revising, read the current artifact together with the writer's latest instruction and the affected prose. Do not rely on memory of an earlier turn when the file exists.

### Update before propagation

When the writer changes a governing question, central judgment, concept, relation, section job, selection of evidence, or argumentative boundary, update the artifact first, reset its status to awaiting review, and trace the consequences through dependent sections. Low-risk structural clarification may be updated directly but triggers the same status reset. Keep a consequential Codex proposal under review until accepted.

Pure copyediting, punctuation repair, and other local changes that preserve the argument do not require an outline update.

### Reconcile after prose

After substantial drafting or revision, reconstruct the realized claim path from the prose independently and compare it with the artifact.

- Repair accidental divergence in the prose.
- If the prose exposes a useful but substantive new path, present it as a proposed update rather than silently rewriting the artifact after the fact.
- Update the artifact directly only for writer-confirmed changes or low-risk clarifications that preserve the confirmed direction, and reset its status to awaiting review after the edit.

The goal is synchronized argumentative state, not mechanical conformity. Productive deviations are allowed; consequential ones become explicit and reviewable.

## Compact starting form

Adapt this form to the piece rather than filling every heading mechanically:

```markdown
# [Working title] — line of argument

> Status: Review draft

## Governing question

...

## Central judgment

...

## Rhetorical situation

- Reader's starting position: ...
- Desired writer-reader relationship: ...
- Overall reader movement: ...
- Reliable voice evidence: ...

## Core concepts and relations

- `Concept A`: meaning in this piece
- `A --qualifies/supports/contrasts with--> B`

## Claim path

1. Movement and what it establishes.
   - Relation to the next movement: ...
   - Available material: ...

## Passage plan

### Passage or section

- Writing job: ...
- Ordered development: ...
- Local conclusion or handoff: ...

## Open for author review

- Consequential proposal, decision, or source check only.

## Boundaries

- Claim not to make, excluded scope, or evidence limit.
```
