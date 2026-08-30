---
name: manager-skill
description: "Reconcile and maintain the state of a long-running reading, thinking, writing, or speaking project. Use when Codex should start or resume a project, record its task type and bounded Zotero source entrance, report or update progress, register completed artifacts, preserve active research lines and author decisions, repair stale indexes or status files, or coordinate handoffs among RWS skills. Do not use it to locate or interpret source contents, develop arguments, draft or revise prose, or adapt material for oral delivery."
---

# Project State Manager

## Purpose

Keep the project recoverable across conversations without taking over the intellectual work performed by `reading-skill`, `thinking-skill`, `writing-skill`, `speaking-skill`, or the writer.

Maintain four kinds of state:

1. completed and current artifacts;
2. current phase and next eligible actions;
3. active research lines, including branches not used in the present article;
4. unresolved source checks, author decisions, and cross-skill handoffs.

Do not create a log of every skill invocation or conversation. Record only changes that would matter when the project is resumed.

## Protect boundaries

This skill may:

- inspect project files and reconcile their declared state with actual artifacts;
- create or update the canonical project-state file;
- update root and subdirectory indexes;
- register a research line with its provenance, status, inputs, and next responsible skill;
- record that an artifact is complete, superseded, awaiting review, or blocked;
- preserve a short dated state history;
- identify broken links, stale descriptions, orphaned artifacts, and contradictory status fields.

This skill must not:

- reconstruct or evaluate a source;
- decide what the writer should believe;
- promote a model suggestion into an author judgment;
- build or repair an argument map;
- draft, review, or revise continuous prose;
- adapt material for oral delivery or conduct speaking rehearsal;
- mark a source check complete without evidence from `reading-skill`;
- mark a substantive direction confirmed without the writer's decision.

Route source questions to `reading-skill`, unchosen relations or claims to `thinking-skill`, prose work to `writing-skill`, and oral adaptation or rehearsal to `speaking-skill`.

## Record the source entrance

Treat the Zotero entrance and the RWS project as two layers of one reusable workflow. Record the entrance; do not perform source discovery or extraction yourself.

- Use `1-文科学习 → 00-学习导航` as the default navigation root for learning about a thinker, work, or field.
- Use `1-文科学习 → 03-写作专题` as the default navigation root for an already concrete article, review, or writing topic.
- Let the writer's explicit collection choice override these defaults.
- Treat both collections as entrances to the same downstream reading → thinking → writing process, not as separate workflows.
- Resolve and record the single prepared task collection under that navigation root. A navigation root may organize lifecycle and topic branches and may contain no direct items; follow only the uniquely supported branch identified by the writer's task, prepared-item membership, or an explicit choice.
- Once the task collection is resolved, restrict source selection to items directly in that collection. Do not continue into its child collections, crawl sibling branches, broaden the content scope to the whole library, or merge both navigation roots.
- When a learning project becomes a concrete writing project, preserve its established source identities and artifacts. Update the recorded entrance or add the writing entrance without restarting the project or moving Zotero items.

Hand the recorded scope to `reading-skill`. Let `reading-skill` resolve bibliographic items and readable attachments, and let the relevant file-format workflow extract content.

## Locate the canonical state

Before updating a project:

1. inspect the project root and its indexes, reading records, processed notes, writing briefs, and draft indexes;
2. reuse an existing canonical status file when one clearly serves this role;
3. otherwise create `00-项目状态.md` at the smallest root that contains the whole reading-to-writing project;
4. read [references/project-state.md](references/project-state.md) before creating or substantially restructuring that file.

Do not treat file existence as proof that intellectual or source work is complete. Inspect the artifact and preserve its stated limits.

## Reconcile from evidence

Compare declared state with actual artifacts:

- update stale phases such as “未开始” when completed notes exist;
- register files that exist but are absent from indexes;
- flag index entries whose targets are missing;
- distinguish a rhetorically complete draft from a source-verified publication version;
- preserve unresolved checks already recorded in notes or revision memos;
- prefer the newest writer-confirmed decision over an older placeholder while retaining meaningful superseded decisions.

Make the smallest edits needed to restore consistency. Do not rewrite content artifacts merely to make status files look tidy.

## Maintain research lines

A research line is a question or extension that should remain recoverable even when it is not part of the active article.

For each line, record:

- stable ID and concise title;
- provenance: `writer_confirmed`, `source_derived`, `model_suggested`, or `open`;
- present formulation without strengthening it;
- related artifacts;
- status: `active`, `parked`, `needs_reading`, `needs_thinking`, `integrated`, or `closed`;
- next responsible skill or writer decision.

Keep a line separate from the current article when its relation to that article has not been confirmed.

## Process a handoff

Accept compact handoff packets from the content skills.

- From reading: artifact, stable source identity and access limits, actual coverage, established claims, open checks, possible research lines.
- From thinking: artifact, writer-confirmed decisions, competing or parked lines, source checks, writing readiness.
- From writing: active version, revision layer, applied and deferred findings, source checks, author decisions, next movement.
- From speaking: speaking artifact, audience, occasion, target and estimated duration, deliberate compressions, author checks, rehearsal focus.

Update state only from the packet and inspected artifacts. If the packet conflicts with the files, report the conflict rather than silently choosing one.

## Return results

Return:

- the updated state file and indexes;
- the current phase;
- newly registered or changed research lines;
- unresolved integrity problems;
- the next action and responsible skill.

Do not add substantive advice merely because the state makes an interesting question visible.
