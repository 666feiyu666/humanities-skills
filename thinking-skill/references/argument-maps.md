# Argument maps

## Purpose

Turn fragments or visual thought maps into a writer-confirmed representation of what is being asked, claimed, supported, contested, and left open. The map prepares writing but is not a draft.

Use this workflow only when the supplied material already has a recognisable structure or the exploratory route has produced one. Do not impose a map on a writer who is still discovering what might matter.

## Reconstruct image inputs

For PNG, JPG, PDF, screenshots, or exported mind maps:

1. inspect the artifact at original or sufficient detail;
2. record the root node, branches, sub-branches, arrows, grouping, and visible labels;
3. note cropped, obscured, unreadable, or connector-free regions;
4. distinguish an explicit arrow from proximity or layout;
5. preserve empty nodes and question placeholders;
6. label any inferred hierarchy or relation as inferred.

Do not redraw or “complete” the map before the writer can inspect the reconstruction.

## Classify nodes

Use only roles that help the current inquiry:

- `material`: passage, event, note, example, or experience;
- `question`: issue the writer is trying to answer;
- `judgment`: position the writer currently holds;
- `reason`: consideration offered for a judgment;
- `evidence`: material supporting a reason or claim;
- `warrant`: why the evidence bears on the claim;
- `definition`: meaning assigned to a term;
- `distinction`: separation of two terms or cases;
- `objection`: pressure against a claim;
- `qualification`: limit or condition;
- `implication`: what follows if a claim is accepted;
- `transition`: why a new branch becomes necessary;
- `source_check`: statement requiring `reading-skill`;
- `author_decision`: choice only the writer can make;
- `open_question`: intentionally unresolved branch.

Tag ownership when ambiguity matters: source, writer, model, or external commentator.

## Classify edges

Prefer explicit edge labels:

- supports;
- exemplifies;
- defines;
- distinguishes;
- causes;
- motivates;
- qualifies;
- contradicts;
- rebuts;
- implies;
- reframes;
- follows in sequence;
- opens the next question;
- relation not yet established.

A shared topic word does not establish an argumentative edge.

## Diagnose structure

Look for:

- claims without reasons;
- material without an identified use;
- reasons without evidence or warrant;
- parallel branches that may be competing centers;
- a conclusion that introduces a new question rather than follows from the map;
- shifts between source reconstruction and writer extension;
- a personal example carrying an unjustified general claim;
- unresolved source checks hidden inside a conceptual bridge;
- a branch that belongs to a different article.

Name the highest-consequence issue first.

## Ask Socratically

Ask one question per round when possible. Favor questions such as:

- What made the initial judgment plausible?
- Which event or distinction changed it?
- Is this branch a reason for the main claim or a second center?
- What relation does this arrow assert?
- Why does this example support the judgment?
- Is this a source claim, your extension, or a comparison?
- Does the objection narrow the claim or defeat it?
- Is the final question the conclusion of this piece or the opening of another?

Do not ask the writer to complete a form. Let each answer update the map.

## Refine through successive rounds

For each round:

1. restate the writer-confirmed portion that is currently in play;
2. identify the one ambiguity or relation whose answer would most change the map;
3. offer a provisional relation type or structural test;
4. ask one focused question;
5. update only the answered branch;
6. record the decision or correction before moving to another branch.

When the writer corrects a reconstruction, lead with the correction and revise its downstream consequences. Do not defend the earlier reading or continue questioning from a superseded map.

When source evidence is needed to settle a concept or attribution, isolate the check and return it to `reading-skill`; after verification, resume from the same structural question.

Stop when the writer says the structure is clear enough, asks for consolidation, or signals that the next question goes beyond the intended scope. Clarity is local to the requested task; it does not require every branch to be filled.

## Preserve versions

Keep three layers distinct:

1. **Faithful reconstruction**: only what the supplied artifact establishes.
2. **Proposed revision**: model-suggested nodes or relations.
3. **Confirmed map**: relations and judgments accepted by the writer.

When revising a saved map, append a dated decision or mark a path as superseded rather than silently rewriting the history of thought.

At closure, save these layers in a processed Markdown note following `processed-notes.md`. The final note should make the writer's corrections and decisions recoverable without requiring the original dialogue.

## Map format

Use a Markdown tree or list by default:

```markdown
# 论证图

- 核心问题：
  - 材料：
  - 暂定判断：
    - 理由一：
      - 证据：
      - 推论桥梁：
    - 限定：
    - 异议：
  - 下一问题：
```

Use Mermaid when relations become easier to inspect visually. Quote labels containing punctuation. Keep the map editable and pair it with a short decision ledger.

## Writing-readiness gate

A map is ready to hand to `writing-skill` for the requested scope when:

- one governing question is selected;
- the central judgment is chosen or explicitly provisional;
- the main reasons or movements are connected;
- evidence is attached or missing support is visibly marked;
- consequential qualifications and objections have a status;
- source checks are isolated;
- branches reserved for another piece are identified;
- the writer has confirmed the direction.

“Ready” does not mean exhaustive or certain. It means the remaining uncertainty can stay visible without forcing the drafter to choose the writer's position.
