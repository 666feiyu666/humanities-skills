# Reading cards

## Function

A reading card is a reusable semantic unit distilled from source-grounded reading and dialogue. It does not replace the chronological Q&A record. A session preserves how understanding developed; a card preserves one result worth finding and using again.

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

If the center is missing or materially ambiguous, ask one focused construction question. Useful prompts include:

- for a knowledge card: “你最希望这张卡片解释清楚的关系是什么？”
- for a question card: “这个问题对你来说真正没有解决的部分是什么？”

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
# 标题：这个知识单元解释了什么

## 逻辑骨架

问题或条件

→ 关键区分或关系

→ 结论、作用或后果

## 简要展开

用连贯文字解释逻辑骨架。说明概念之间为什么形成这种关系，
而不是把骨架重复成更长的列表。

## 我的经验与实践推演

只在已有真实经验、例子或写作者确认的推演时使用。

## 来源与理解边界

- 来源与位置：
- 实际阅读范围：
- 阅读基础：原书 / 部分原文 / 网络重建
- 相关讨论记录：
- 尚待核查：

## 关联与尚待展开
```

Use only sections that carry information. The logic chain, brief expansion, and source boundary are normally essential. The experience section is optional; never invent personal experience. Faithfully preserve experience or practical reasoning already supplied or confirmed by the writer, but hand off to `thinking-skill` when that reasoning still needs to be developed or tested. A model-proposed extension remains an interpretation or open question until the writer confirms it.

## Question card

A question card preserves an open problem as a productive entrance, not as a failed knowledge card. Supply enough context that the writer can understand later why the question mattered and what has already been tried.

Suggested form:

```markdown
# 核心问题

## 问题如何产生

说明触发问题的段落、概念冲突、经验或讨论节点。

## 当前已能确认

区分原文明确支持的内容、合理解释和写作者的判断。

## 仍不确定或存在分歧

不要为了显得完整而提前作答。

## 下一步需要回到哪里

- 需要重读的章节或段落：
- 需要补充的来源：
- 可以继续追问的具体问题：

## 来源与关联

- 来源与位置：
- 实际阅读范围：
- 相关讨论记录：
- 相关知识卡片：
- 状态：开放 / 部分解决 / 已解决
```

When later reading resolves the question, update its status and link the answer or resulting knowledge card. Do not silently rewrite the original question into a claim.

## Shared provenance

Use compact markers whenever a statement could later be mistaken for the source:

- `[原文]`
- `[概括]`
- `[二手重建]`
- `[解释]`
- `[我的想法]`
- `[待核查]`

Locators may be pages, ebook locations, chapter and section names, or stable paragraph identifiers. Never fabricate a locator. When a claim comes from web research, cite the actual page and do not replace its locator with an inferred book page.

For `partial_source` and `web_reconstruction`, retain actual visible coverage, an evidence ledger when multiple web sources matter, coverage gaps, and claims that require checking against the original.

For a Zotero-located source, use the bibliographic item key and attachment key as the stable local identity when useful. Record filename, content type, link mode, extraction method, and locator limits only when they affect recovery or verification. Do not preserve an absolute Zotero storage path as the durable identifier.

## Updating

Edit the active card when the writer asks to revise it; do not create `v2`, `final`, or date-suffixed duplicates for ordinary changes. In a Git-managed project, let Git preserve routine history. Keep an inline correction or superseded interpretation only when the change itself matters to understanding.

Question cards and knowledge cards may link to each other, but do not force a one-to-one conversion. A useful question can remain a durable entrance after an answer exists.

## Handoff block

End with a small handoff block only when useful:

```markdown
## 交给 thinking-skill 的材料

- 触动点：
- 可继续追问：
- 可用引文：
- 尚需回原书核查：
```

Keep this block source-facing. Do not preselect a central claim or arrange an article on the writer's behalf.
