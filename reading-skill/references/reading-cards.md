# Reading cards

## Function

A reading card is a reusable semantic unit distilled from source-grounded reading and dialogue. It does not replace the chronological Q&A record. A session preserves how understanding developed; a card preserves one result worth finding and using again.

Choose the card language from the writer's explicit request, the active card, or the current dialogue when creating a new card. Render headings, prompts, status labels, and human-facing provenance markers naturally in that language. Preserve quotations in the source wording actually inspected and label any model translation. The English labels used below name semantic roles rather than mandatory surface wording.

Card creation is selected by the writer, not decided by the skill and not required as a closing ritual. Codex may identify and explain candidates, but the writer decides whether to create no cards, one card, or several cards of different types. One card may draw on several sessions or passages.

Before creating writer-selected cards from a substantive multi-turn dialogue in a declared local project, preserve that dialogue according to [reading-sessions.md](reading-sessions.md) and link the relevant session record from each card.

## Keep the writer in control

At a checkpoint, Codex may offer a compact list of candidates. For each candidate, give only:

- a proposed title;
- a proposed card type;
- one sentence explaining why that type fits the current state of understanding.

Do not draft a full card until the writer accepts or directly requests it. The writer may reject, defer, rename, retype, merge, or split any candidate. A request to save, pause, close, or synthesize the dialogue applies to the session record only and must not be treated as permission to create cards.

When the writer directly requests a named card or card type, treat the artifact choice as confirmed. That request does not authorize Codex to invent the card's substantive center. If the source state cannot support the selected type, explain the limitation and offer a question card or continued dialogue instead.

## Co-construct the content

The writer should exercise agency over what the card means, not only whether the file exists. Card-making therefore begins from a writer-shaped semantic center and uses Codex as a scaffold, source checker, supplementer, and editor.

Before drafting, recover relevant writer contributions already present in the dialogue. These may include a tentative title, the problem as the writer sees it, a proposed logic or distinction, a point of confusion, an example, or an experience. Do not ask the writer to repeat material that already supplies the center.

If the center is missing or materially ambiguous, ask one focused construction question in the dialogue language. Useful prompts are equivalent to:

- for a knowledge card: “What relationship do you most want this card to clarify?”
- for a question card: “What part of this question remains genuinely unresolved for you?”

Do not turn this into a form-filling interview. Once the writer has supplied or confirmed the center, Codex may build a compact working skeleton, test it against the source, point out missing links, offer alternatives, add verified context and locators, and improve readability.

The following remain the writer's responsibility unless already expressed and confirmed:

- the card's substantive center and conceptual priority;
- which interpretation or distinction they want to retain when several remain possible;
- personal experience, motivation, and practical significance;
- acceptance of any model-proposed extension.

The following are appropriate Codex contributions:

- faithful reconstruction of the writer's existing ideas;
- source verification and provenance separation;
- focused questions, counterchecks, and alternative formulations;
- supplemental explanation supported by the reading basis;
- structural and language refinement after the center is established.

Even when the writer asks for a complete draft, use the discussion as their initial construction. If no writer-shaped center exists, pause for one focused contribution rather than producing the card from scratch.

## Propose card types by epistemic function

Use the state of the inquiry, not the surface topic, to choose a form:

- **Knowledge-card candidate**: a source-grounded concept, distinction, relationship, or argumentative movement is stable enough to explain and revisit.
- **Question-card candidate**: a consequential question, ambiguity, disagreement, or missing bridge remains open and may guide later reading.
- **Recommend no card yet**: the exchange is still exploratory, too local, or not useful enough to retrieve independently.

Do not turn uncertainty into a knowledge claim merely to complete a template. The same session may support both a knowledge-card candidate and one or more question-card candidates; only the writer decides which become artifacts.

When a recurring output serves another distinct retrieval function, describe that function and ask the writer whether it should become a named card type. Do not adopt or accumulate permanent types from one-off shapes without the writer's choice.

## Knowledge card

A knowledge card should remain readable after the immediate conversation has been forgotten. Its default movement is:

1. show the logic compactly;
2. explain the logic in connected prose;
3. when real material exists, test or extend it through the writer's experience or practice;
4. preserve enough source context to recover the basis and limits.

Suggested form:

```markdown
# Title: What this knowledge unit explains

## Logical skeleton

Problem or condition

→ Key distinction or relation

→ Conclusion, function, or consequence

## Brief development

Explain the logical skeleton in connected prose. Show why the concepts have this
relation instead of repeating the skeleton as a longer list.

## My experience and practical extension

Use only when real experience, an example, or a writer-confirmed extension exists.

## Sources and limits of understanding

- Source and locator:
- Actual reading coverage:
- Reading basis: direct source / partial source / web reconstruction
- Related session record:
- Still to verify:

## Relations and further questions
```

Use only sections that carry information. The logic chain, brief expansion, and source boundary are normally essential. The experience section is optional; never invent personal experience. Faithfully preserve experience or practical reasoning already supplied or confirmed by the writer, but hand off to `thinking-skill` when that reasoning still needs to be developed or tested. A model-proposed extension remains an interpretation or open question until the writer confirms it.

## Question card

A question card preserves an open problem as a productive entrance, not as a failed knowledge card. Supply enough context that the writer can understand later why the question mattered and what has already been tried.

Suggested form:

```markdown
# Central question

## How the question arose

Identify the passage, conceptual tension, experience, or dialogue point that raised it.

## What is currently established

Separate direct source support, reasonable interpretation, and writer judgment.

## What remains uncertain or disputed

Do not answer prematurely for the sake of completeness.

## Where to return next

- Chapter or passage to reread:
- Additional source needed:
- Specific question to continue:

## Sources and relations

- Source and locator:
- Actual reading coverage:
- Related session record:
- Related knowledge card:
- Status: open / partially resolved / resolved
```

When later reading resolves the question, update its status and link the answer or resulting knowledge card. Do not silently rewrite the original question into a claim.

## Shared provenance

Use localized equivalents of these compact markers whenever a statement could later be mistaken for the source:

- `[quotation]`
- `[source reconstruction]`
- `[secondary reconstruction]`
- `[interpretation]`
- `[my thought]`
- `[needs verification]`

Locators may be pages, ebook locations, chapter and section names, or stable paragraph identifiers. Never fabricate a locator. When a claim comes from web research, cite the actual page and do not replace its locator with an inferred book page.

For `partial_source` and `web_reconstruction`, retain actual visible coverage, an evidence ledger when multiple web sources matter, coverage gaps, and claims that require checking against the original.

For a Zotero-located source, use the bibliographic item key and attachment key as the stable local identity when useful. Record filename, content type, link mode, extraction method, and locator limits only when they affect recovery or verification. Do not preserve an absolute Zotero storage path as the durable identifier.

## Updating

Edit the active card when the writer asks to revise it; do not create `v2`, `final`, or date-suffixed duplicates for ordinary changes. In a Git-managed project, let Git preserve routine history. Keep an inline correction or superseded interpretation only when the change itself matters to understanding.

Question cards and knowledge cards may link to each other, but do not force a one-to-one conversion. A useful question can remain a durable entrance after an answer exists.

## Handoff block

End with a small handoff block only when useful:

```markdown
## Material for thinking-skill

- Point of interest:
- Question to continue:
- Usable quotation:
- Still to verify in the source:
```

Keep this block source-facing. Do not preselect a central claim or arrange an article on the writer's behalf.
