# Text surrogates: keep OCR output for reuse

## Purpose

Decide when a source's extracted text should be kept on disk as a reusable "text surrogate", so a later reading session reuses it instead of re-running OCR, and when it should not. A surrogate is the extracted/OCR text file plus the source note that makes it recoverable.

## Decision rule

Keep a text surrogate only when the text cannot be reliably re-derived from the source PDF on demand. The test is recoverability, not "was OCR ever run":

| PDF condition | Extraction | Keep surrogate? |
|---|---|---|
| usable text layer | direct extraction | No — re-extractable at any time; a kept copy would drift from the source |
| scanned, no text layer | Apple Vision OCR | Yes — OCR is costly and not repeatable on demand |
| mixed (some pages have a text layer, some are scanned) | keep the text layer, OCR the missing pages | Yes — a plain re-extraction would silently lose the OCR'd pages |

A mixed PDF is kept even though part of its text could be re-extracted directly, because the whole surrogate is what makes the OCR'd pages recoverable. Do not keep a surrogate for a fully text-layered PDF merely because extraction was easy.

## Location and naming

Place the surrogate in the reading-task material directory, following the established practice:

- `01-阅读记录/<task>/00-材料/<source-stem>-OCR.txt` — the text surrogate. Its header already records the extraction method (direct / OCR / hybrid) and PDF page markers.
- `01-阅读记录/<task>/00-材料/来源说明.md` — the source note that makes the surrogate reusable (identity, extraction record, page mapping, usage limits).

Do not create a domain-level surrogate directory. Cross-task reuse goes through the literature index: `00-索引/文献索引/<work>.md` links to the task's `来源说明.md`, which links to the text surrogate. Do not copy the text into other tasks.

## Source note (来源说明.md)

Reuse the established three-section shape:

1. **Stable source identity** — source origin; Zotero item/attachment key when applicable; filename; edition or translation if established; bibliographic fields that remain unestablished.
2. **Extraction record** — page count and text-layer status; extraction or OCR method and rendering settings; actual coverage; the surrogate's filename; and the PDF-page ↔ printed-page mapping when verified.
3. **Usage limits** — machine-recognized text is for retrieval and first reading only; exact quotations, footnotes, references, proper names, and page numbers must be verified against the PDF image.

This file is the intended home for operational extraction detail, as a deliberate exception to the general source-note relevance rule in `../SKILL.md`. Those details live here to enable reuse, not to be published into a reading record or card.

## Reuse check (Establish the source)

Before extracting, look in the task's `00-材料/` for an existing text surrogate and `来源说明.md` that match the current source (same Zotero attachment key, or same filename when Zotero is not involved):

- match found → reuse it and do not re-OCR. Take its page mapping and coverage as the basis for what can be located, and re-verify against the PDF only what the current question needs.
- no match, and the PDF has a usable text layer → extract directly; do not keep a surrogate.
- no match, and OCR is needed → invoke `ocr-scanned-pdf`, keep the surrogate, and write `来源说明.md`.

## Boundaries

- A text surrogate is machine-recognized text. Never treat it as a verified edition for quotation, page reference, or bibliographic claims; defer exact wording to the source PDF.
- Keeping a surrogate is a mechanical transformation and is exempt from the author-review gate, but it writes into the workspace only at the location and naming above. The writer may request not to keep one.
- Navigation state inside `来源说明.md` (for example a Zotero collection path) is mutable; refresh it on use per the root `AGENTS.md`.
- `ocr-scanned-pdf` only extracts and returns a path. This skill decides whether to keep the result and where.
