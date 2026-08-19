# Recursive revision cycle

## Purpose

Give each saved revision one explicit working scope while preserving recursive movement among observation layers. A structural version should not silently become a language pass, and a language version should not conceal a newly exposed structural problem. Classify every finding, apply only the active scope, and carry other findings forward in a deferred revision ledger.

The three observation layers are:

1. **Macro**: rhetorical situation, central claim, argument, audience, and arrangement.
2. **Relations**: section necessity, paragraph jobs, and relations among adjacent units.
3. **Style**: diction, reference, syntax, punctuation, rhythm, and the writer's style profile.

Group macro and relations under a **structure round** for versioning. Treat style as a **language round**. The rounds control what this version edits; they do not forbid diagnosis at another layer.

## Classify every review comment

Use one category label and one status label for each finding:

- `[结构｜宏观]`: governing action, central claim, argument path, audience, section order, opening, or conclusion;
- `[结构｜关系]`: section necessity, paragraph job, evidence-to-claim bridge, adjacent-unit relation, or transition;
- `[语言]`: diction, reference, syntax, punctuation, rhythm, repetition, or voice;
- `[来源核查]`: quotation, attribution, factual basis, concept, comparison, evidence, or scope that must be established by `reading-skill`;
- `[作者决定]`: a substantive position, scope, governing question, or argument choice reserved for the writer.

Mark the status as:

- `[本轮]`: apply in the current version;
- `[递延]`: preserve for a later version;
- `[返回]`: stop at the writing boundary and hand the issue to reading, thinking, or the writer.

Prefer compact combined markers in review comments:

```text
（[本轮｜结构-关系] 本段与上一段重复，合并后保留一个证据链。）
（[递延｜语言] “仍然可能”重复，留到语言修订。）
（[返回｜来源核查] 需要核对引文页码及概念适用范围。）
```

When the reviewer supplies unmarked comments, classify them before editing. Do not ask the reviewer to rewrite them.

## Set the version contract

Name and scope the new version before revision:

- `D00N-结构修订`: activate `[结构｜宏观]` and `[结构｜关系]`;
- `D00N-语言修订`: activate `[语言]`;
- use a mixed or purpose-specific label only with explicit writer authorization.

In a structure round, make only the local wording changes needed to keep moved, split, merged, or newly connected prose grammatical. Record all broader polishing as `[递延｜语言]`.

In a language round, preserve the argument map and paragraph jobs. If accurate wording requires changing a claim, warrant, paragraph role, or order, mark the problem `[递延｜结构-宏观]` or `[递延｜结构-关系]` and return to the relevant structural layer.

At the end of the version, preserve a deferred revision ledger with:

| Location | Category | Finding | Why deferred | Intended round |
|---|---|---|---|---|

Do not silently drop a deferred item when creating the next version. Reclassify it as `[本轮]`, keep it deferred with a reason, or close it because an earlier edit made it obsolete.

## Keep invention and source verification at the boundary

Enter rhetorical revision only when continuous prose exists. The rhetoric professor may identify an invention problem, name competing claims neutrally, ask clarifying questions, and describe the structural consequence of each option. It must not choose the writer's value position, invent support, or turn a tentative thought into a settled claim.

Return to the writer when revision requires:

- choosing among substantive positions;
- changing a philosophical, moral, or practical commitment;
- selecting a new central question;
- accepting a stronger or broader claim than the writer has authorized.

Use `return_to_invention`, state the exact author decision or missing map relation, and hand the task to `thinking-skill`. Do not revise past that point.

Use `return_to_reading` and hand the task to `reading-skill` when revision requires checking or supplying a quotation, attribution, concept, source relation, factual claim, or evidence not established in the provided material. State the exact check rather than a general request for more research.

## Select the entry layer

When the writer names a layer, start there but still detect problems above it. When the writer asks for automatic diagnosis, enter at the highest consequential unresolved layer:

1. Start at **macro** for a split central action, competing claims, missing argument path, unsupported scope, or audience-positioning problem.
2. Start at **relations** only when the governing claim and broad arrangement are stable but section, paragraph, or sentence relations are not.
3. Start at **style** only when argument and relations are stable enough that local editing will not conceal a higher-level problem.

Do not bury a macro problem under relation or style comments. Diagnosing another layer does not authorize editing it in the current version.

## Run one revision loop

Use the same internal loop at every layer:

1. **Diagnose** the text's present effect, independently of the writer's stated intention.
2. **Separate ownership**: distinguish rhetorical problems, missing material, and decisions reserved for the writer.
3. **Confirm the target**: state the version label, active categories, and writer authorization.
4. **Revise within scope**: change only active findings and the minimum dependent wording.
5. **Re-read the resulting whole**: check whether the change solved the problem and add new out-of-scope findings to the deferred ledger.
6. **Choose movement**:
   - `stay`: continue at the current layer;
   - `advance`: move to a more local layer;
   - `return`: move to a higher layer;
   - `return_to_invention`: stop for a substantive author decision;
   - `return_to_reading`: stop for a defined source or evidence check;
   - `exit`: the text satisfies the current publication purpose, with remaining limits recorded.

When `advance` would cross from the active structure round into the language round, close the current version and schedule the deferred language findings for the next version instead of editing them immediately.

Never assume that a completed style pass means the article is finished.

## Macro layer

Read [rhetoric-review.md](rhetoric-review.md) and [argument-audit.md](argument-audit.md). Check:

- exigence, intended readers, constraints, and the judgment the writer hopes to change;
- the question promised by the opening and the claim established by the body;
- title, opening, section sequence, conclusion, and their governing rhetorical action;
- the job of each section and why the next section becomes necessary;
- ethos, pathos, and logos as interacting effects, not independent scores;
- Toulmin claim, data or grounds, warrant, backing, qualifier, and rebuttal;
- the position assigned to writer, reader, and people under discussion.

Return to invention instead of revising when candidate central claims remain in substantive competition.

## Relations layer

Read [discourse-relations.md](discourse-relations.md). Check:

- why each section or paragraph follows the previous one;
- each paragraph's nucleus and the job of its other sentences;
- elaboration, evidence, warrant, cause, reason, result, contrast, concession, condition, counterexample, sequence, reorientation, and closure;
- false cause, missing warrant, decorative contrast, pseudo-concession, unequal comparison, hidden reorientation, excessive connective chaining, and ambiguous reference.

Repair the underlying relation before changing the connective. Return to macro when the relation cannot be repaired without changing the claim, argument path, or scope.

## Style layer

Read [style-profile.md](style-profile.md). Check:

- exact diction and stable concepts;
- sentence subjects, pronoun reference, modifier scope, and negation scope;
- punctuation as an expression of syntax and discourse relation;
- repeated `不是……而是……`, unnecessary colons, overcompressed long sentences, unanswered rhetorical questions, and isolated aphorisms;
- paragraph rhythm, movement between abstraction and lived scenes, and an ending proportionate to what the article established;
- preservation of the writer's humor, hesitation, uncertainty, and recognizable voice.

Return to relations when no accurate local wording can express the supposed relation. Return to macro when the relation problem comes from an unstable claim or structure.

## Preserve invariants

At every layer:

- preserve the writer's ownership of substantive judgment;
- preserve names, titles, quotations, citations, page numbers, supplied examples, and conceptual distinctions;
- distinguish writer claims, source claims, model suggestions, and actual rhetorical effects;
- do not broaden a claim, erase uncertainty, or invent material;
- do not remove necessary warrants, qualifiers, rebuttals, or evidence for fluency or compression;
- do not apply a deferred finding merely because it is easy to fix;
- save revisions as new versions and report the target, changes, movement, and unresolved problems.

## Return a cycle result

For review, return:

- **current layer** and why it is the correct entry point;
- **realized map or relation** appropriate to that layer;
- **strongest achieved effect**;
- **classified findings** with status, locations, reasons, and consequences;
- **author decisions** and missing material;
- **movement**: stay, advance, return, return to invention, return to reading, or exit;
- **next action** stated conditionally when writer judgment is required.

For authorized revision, return:

1. the revised prose;
2. a compact cycle memo containing the version label, active layer, target, applied changes, deferred revision ledger, movement, next layer, and unresolved problems.
