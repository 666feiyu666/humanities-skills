# Argument maps

## Purpose

Turn fragments or visual thought maps into an author-reviewable representation of what is being asked, claimed, supported, contested, and left open. The map develops within writing and can be tested through exploratory passages. Treat it as writer-confirmed only after explicit review.

Use this workflow only when the supplied material already has a recognisable structure or the exploratory route has produced one. Do not impose a map on a writer who is still discovering what might matter.

## Confirm the plan in chat before editing

Read an existing map without immediately completing or improving it. Present the faithful reconstruction and proposed changes in the conversation, discuss consequential choices, and obtain explicit confirmation of the concrete plan for the current scope before creating or modifying a map file. A map's existence or a request to improve it does not settle that plan. This gate also applies to persistent outlines and line-of-argument files, and cannot be bypassed by saving the map inside a closure record.

Keep per-round answers and corrections in the discussion until the edit plan is confirmed. Agreement on one branch is not agreement on unrelated changes. Once the plan is accepted, apply only those changes without asking again; return a new consequential proposal to chat before writing it.

## Reconstruct image inputs

For PNG, JPG, PDF, screenshots, or exported mind maps:

1. inspect the artifact at original or sufficient detail;
2. record the root node, branches, sub-branches, arrows, grouping, and visible labels;
3. note cropped, obscured, unreadable, or connector-free regions;
4. distinguish an explicit arrow from proximity or layout;
5. preserve empty nodes and question placeholders;
6. label any inferred hierarchy or relation as inferred.

Show the reconstruction in chat. Do not redraw or complete the map file until the writer has discussed and explicitly confirmed the concrete plan.

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

Tag ownership when ambiguity matters: source, writer, model, or external commentator. These roles are aids for analysis and discussion; do not turn them into mandatory fields in the outline.

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

Do not ask the writer to complete a form. Let each answer refine the working understanding in chat; it does not automatically trigger a map-file update.

## Refine through successive rounds

For each round:

1. restate the writer-confirmed portion that is currently in play;
2. identify the one ambiguity or relation whose answer would most change the map;
3. offer a provisional relation type or structural test;
4. ask one focused question;
5. reflect the answered branch in the conversation and distinguish it from still-open choices;
6. keep the decision or correction visible in chat; edit the map file only after the concrete plan for the current scope is confirmed.

When the writer corrects a reconstruction, lead with the correction and discuss its downstream consequences. Confirm the resulting edit plan before changing the file. Do not defend the earlier reading or continue questioning from a superseded understanding.

When source evidence is needed to settle a concept or attribution, isolate the check and return it to `reading-skill`; after verification, resume from the same structural question.

Stop when the writer says the structure is clear enough, asks for consolidation, or signals that the next question goes beyond the intended scope. Clarity is local to the requested task; it does not require every branch to be filled.

## Preserve versions

Keep three layers distinct:

1. **Faithful reconstruction**: only what the supplied artifact establishes.
2. **Proposed revision**: model-suggested nodes or relations.
3. **Confirmed map**: relations and judgments accepted by the writer.

Keep the reconstruction, proposed changes, writer corrections, and revision reasons distinct in chat. Once the concrete plan is accepted, update the saved outline to show the current argument without appending a dated decision ledger or superseded paths. Preserve that history in a separate record only when the writer requests one.

If the concrete map plan has not been confirmed in chat, return the proposed changes and open choices in the conversation; do not save an unconfirmed map as part of another note. Follow `processed-notes.md` only for a requested separate inquiry record.

## Map format

Use a concise Markdown outline by default. Show the core question, ordered claims or questions, and why they connect. Group movements when it helps the argument; do not impose a fixed number of parts or steps.

Render headings and steps in the outline language. For example:

```markdown
# Argument map

**Core question:** …

1. **Claim or question developed here.** Reasoning or example that establishes the step.
2. **Next claim or question.** Explain how it follows from, qualifies, or extends the previous step.
```

Use Mermaid when relations become easier to inspect visually. Quote labels containing punctuation. Keep the map editable; discuss revision reasons and alternatives in chat.

## Writing-readiness gate

A map becomes a usable outline for Humanizer (`humanizer` for English prose; `humanizer-zh` for Chinese prose) for the requested scope when:

- one governing question is selected;
- the central judgment is chosen or explicitly provisional;
- the main reasons or movements are connected;
- evidence is available in the established material, or missing support has been identified in the conversation;
- consequential qualifications and objections are reflected in the claims or discussed in chat;
- source checks and branches reserved for another piece are clear in the conversation;
- the writer has supplied or confirmed the direction, or explicitly authorized drafting from a provisional outline. Clarify that status in chat.

“Ready” does not mean exhaustive or certain. It means the remaining uncertainty can stay visible without forcing the drafter to choose the writer's position.
