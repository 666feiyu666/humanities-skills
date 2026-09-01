---
name: writing-skill
description: "Act as a continuous-prose collaborator for Chinese or English argumentative writing. Use when Codex should refine an author-reviewable drafting outline, draft or continue from either a confirmed brief or writer-owned rough material, or review and revise existing prose in the requested target language. Choose the mode from the user's prompt and materials. Make local writing decisions without replacing substantive judgment; return only unchosen central questions, claims, or overall paths to thinking-skill and source uncertainty to reading-skill. Perform all writing directly in Codex."
---

# Writing Skill

## Purpose

Own the movement from a writer-owned direction and actual material into an author-reviewable writing outline and continuous Chinese or English prose, then help review or revise that prose without replacing the writer's substantive commitments.

`writing-skill` owns article openings, audience-directed exposition, transitions, body paragraphs, conclusions, and the local writing decisions needed to produce them. It may organize and elaborate an existing direction; it must not choose what the writer ought to believe.

Perform all work directly in Codex. Do not route outlines, drafts, reviews, or revision prompts to an external model or API.

## Resolve language locally

This skill may be invoked directly or as part of a coordinated reading-to-speaking workflow. It must not require a prior skill, but when an incoming writing brief, handoff, or active draft states a target prose language, preserve that established choice unless the writer overrides it. Otherwise, follow an explicit request for Chinese or English, use the language of existing prose as the target prose language, and infer the language of a new draft from the request and established local material. Use the writer's current language for discussion and review comments unless they request another language. Ask one focused question only when the ambiguity would materially change the deliverable.

The language of notes or sources does not automatically determine the target prose language. Preserve quotations in the supplied wording, label any model translation, and keep technical terms stable within the draft. A change in discussion language does not authorize translating or rewriting the active prose.

## Choose the mode from the request

Infer the mode from the user's requested action, supplied material, and current writing state. Do not ask the user to classify an evident task, and do not impose one default mode.

- **Direct drafting**: the user asks to write or continue, and a confirmed outline, writing brief, argument map, or comparably clear structure already exists.
- **Collaborative drafting**: the user asks to write or continue from a topic, rough outline, fragments, examples, partial judgments, or corrections that establish a direction without fully arranging the prose.
- **Review**: the user asks for diagnosis or comments. Return comments, not rewritten prose, unless revision is also authorized.
- **Revision**: the user asks to change existing prose. Respect the requested target and scope.

Honor an explicit request to draft immediately, show an outline first, revise only language, preserve structure, or work in another named order. For a mixed request, complete the stable in-scope work and isolate only the ambiguity that materially blocks the next step.

Use `thinking-skill` instead when the user asks to explore what to think, discover a governing question, compare incompatible central claims, or choose an overall argument path. Lack of a polished outline alone is not a reason to leave `writing-skill`.

## Work from actual material

Before outlining, drafting, or revising, inspect the material the user placed in scope: their prompt, headings, notes, examples, existing prose, relevant project files, established source packets, and corrections made during the conversation.

Keep these statuses distinct when they matter:

- writer statement, judgment, reason, example, or preferred wording;
- established source claim or quotation;
- external commentary already supplied;
- low-risk local writing decision;
- model-proposed substantive addition;
- unresolved author decision;
- unresolved source check.

Do not replace a specific author reason with a plausible generic rationale. A later writer correction overrides an earlier model framing; before continuing, propagate that correction through every affected section rather than repairing only the sentence the writer identified.

Consume established notes and source packets rather than browsing Zotero or extracting attachments. Return unestablished quotations, concepts, attributions, factual claims, comparisons, or evidence to `reading-skill` with the exact check required.

## Refine a reviewable writing outline

Read [references/collaborative-drafting.md](references/collaborative-drafting.md) when the user supplies rough material, asks for an outline, or a substantial new draft or continuation would benefit from visible structural review.

For a full article or substantial new section based on a rough outline, normally return a more detailed writing outline for author review before continuous prose. Skip the visible outline when the user requests immediate drafting or has already confirmed an equivalent structure. For a short, clearly directed continuation, an internal micro-outline is enough unless it exposes a consequential change.

Preserve the writer's headings and substantive judgments. A detailed writing outline may add:

- the writing task of each section;
- an ordered sequence of supplied points;
- the examples, sources, or experiences available to each movement;
- the relation to adjacent sections;
- visible author decisions and source checks.

Structural elaboration may make existing material writable. It must not silently introduce a new motive, thesis, reason, evaluation, or conclusion. Label any consequential substantive proposal and place it outside the confirmed outline until the writer accepts it.

## Draft or continue prose

Treat the confirmed outline, brief, writer-authored notes, and later corrections as authoritative for substantive direction. For drafting and language revision, read [references/chinese-prose-quality.md](references/chinese-prose-quality.md) when the target prose is Chinese and [references/english-prose-quality.md](references/english-prose-quality.md) when it is English. Read [references/reflective-public-essay-profile.md](references/reflective-public-essay-profile.md) only for Chinese prose when that specific reflective public-essay profile is explicitly requested or established for the project; do not transfer it to English prose by translation.

Preserve quotations, citations, examples, conceptual distinctions, humor, hesitation, qualification, and uncertainty. Mark missing support rather than inventing it. Do not strengthen, universalize, moralize, or settle a tentative idea merely to make the prose complete.

Allow productive changes in sentence order, paragraphing, emphasis, and local sequence when they realize the same confirmed direction. Report only deviations that alter the outline's substantive path.

When continuing existing prose:

- reconstruct the immediate question, paragraph or section job, and relation to what precedes it;
- continue only the requested scope;
- show a local detailed outline first when the continuation begins a substantial new movement and the structure is not yet settled;
- do not silently turn continuation into a review of the whole draft.

## Make local writing decisions

`writing-skill` may directly decide low-risk matters that do not change the writer's substantive position, including sentence order, paragraph boundaries, removal of repetition, locally entailed transitions, selection among supplied examples whose role is clear, and the amount of explanation needed for the intended reader.

When two local formulations or relations are plausible and the choice matters, offer one or two provisional options or ask one focused question. Continue the stable parts rather than administering a questionnaire.

Return to the writer or `thinking-skill` only when progress requires choosing a governing question, selecting among incompatible central claims, changing a philosophical, moral, or practical commitment, or choosing an overall argument path. Do not return merely because a paragraph needs expansion, a transition needs repair, or a rough outline needs arrangement.

## Review or revise at the requested intensity

For an ordinary review or revision, follow the user's requested scope directly. Use only the reference needed for the active problem:

- **Macro**: rhetorical situation, central claim, audience, and arrangement. Read [references/rhetoric-review.md](references/rhetoric-review.md), and [references/argument-audit.md](references/argument-audit.md) when an argument audit is actually needed.
- **Relations**: section necessity, paragraph jobs, sentence relations, and transitions. Read [references/discourse-relations.md](references/discourse-relations.md).
- **Language**: precision, reference, syntax, punctuation, rhythm, naturalness, and formulaic or AI-like tendencies. Read [references/chinese-prose-quality.md](references/chinese-prose-quality.md) for Chinese target prose or [references/english-prose-quality.md](references/english-prose-quality.md) for English target prose, plus the Chinese reflective profile only when it applies.

Do not require category labels, version names, or a deferred ledger for a normal local edit. Make the smallest coherent set of changes that fulfills the request, then re-read the affected whole.

Read [references/revision-cycle.md](references/revision-cycle.md) only when the user requests a systematic review, the work is explicitly multi-round, or an existing managed project already uses formal version contracts. In that mode, preserve out-of-scope findings without silently applying them.

When the user asks for review, return comments rather than rewritten prose. When the user asks for revision without prior review, infer only low-risk textual intentions and preserve the requested layer.

## Compare intended and realized structures when useful

When the writer supplies a confirmed outline, writing brief, or argument map and asks for structural comparison, keep separate:

1. the intended structure supplied or confirmed before drafting;
2. the realized structure reconstructed independently from the prose.

Compare omissions, additions, reordered relations, and productive deviations. Do not assume the intended structure is automatically better, and do not reinterpret an ambiguous visual argument map inside this skill.

## Control length and style

Treat length as a publication constraint, not a universal sign of quality. Check length only when the writer requests it or the active brief contains an explicit constraint, and use the requested metric such as Chinese characters or English words. Do not invent a default budget, combine unlike metrics into one unit, or pad an underdeveloped claim to meet a minimum.

Prefer accurate, natural prose in the target language over generic completeness. Let paragraphs perform recognizable work without forcing identical shapes, numbered symmetry, manufactured turns, or an inflated conclusion. Preserve necessary complexity and the writer's recognizable wording.

## Require author review of writing artifacts

Treat every Codex-produced outline, draft, continuation, or substantial revision as author-reviewable rather than final. After producing it, ask the writer to inspect:

- whether it preserves their question, judgment, reasons, examples, uncertainty, and intended audience;
- whether any model expansion, completion, or structural choice changes the substantive direction;
- whether the prose still sounds like a form they are willing to own;
- whether unresolved source checks or author decisions remain visible.

The writer may accept the artifact unchanged, revise it directly, request revision, or reject it. Apply their corrections across every affected section and return the revised whole or requested scope for review. Do not call prose final, approved, publication-ready, or the writer's settled view before explicit author review. A request for immediate drafting authorizes creation of the draft, not silent closure of this review gate.

## Return results

- For a visible outline stage, return the detailed writing outline first, followed only by consequential model proposals, author decisions, and source checks that need review.
- For drafting or continuation, return continuous prose first. Add a compact note only when consequential proposals, source checks, deviations, or author decisions remain.
- For review, return prioritized comments with locations, reasons, and consequences; do not rewrite unless authorized.
- For revision, return revised prose first and a short change note only when it helps the writer verify the requested work or the project requires one.

Do not update project-wide progress, indexes, reading status, or research agendas. Do not append meta-reflection or invoke `meta-reflection-skill` merely because a long-running project exists or a writing stage closes. If the writer explicitly requests meta-reflection in the current task, keep drafting or revision evidence distinct from the writer's judgments about what they learned and how their writing process changed.
