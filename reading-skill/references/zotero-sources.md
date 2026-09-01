# Zotero source acquisition

## Purpose

Use Zotero as a source-discovery and attachment-location adapter for reading. Do not treat it as a fourth reading basis: the basis remains `direct_source`, `partial_source`, or `web_reconstruction` according to what content was actually inspected.

## Resolve the source

1. Invoke `manage-zotero-library` and follow its runtime and safety rules.
2. Resolve the navigation root before resolving source content. Treat `1-文科学习 → 00-学习导航` as the default learning root and `1-文科学习 → 03-写作专题` as the default concrete-writing root, unless the writer names another scope.
3. Resolve one prepared task collection under that root. Navigation roots may contain lifecycle and topic branches and no direct items. Use the writer's task name, collection path, or prepared-item membership to identify a unique branch; do not recursively collect every descendant or inspect unrelated siblings as content.
4. Once resolved, restrict source selection to items directly in the task collection. Do not include items found only in its child collections, another navigation root, or unrelated library locations unless the writer explicitly expands scope.
5. Resolve either a top-level bibliographic item or a standalone attachment intentionally prepared in the task collection. Require a unique match within scope; do not choose silently among editions, translations, similarly titled works, or duplicate attachments.
6. For a bibliographic item, locate its attachments. For a standalone attachment, preserve the attachment key and filename and state that no parent bibliographic record is available; do not invent missing book or chapter metadata.
7. Select an attachment that matches the requested edition, language, and format. If metadata does not settle the choice, inspect the file's title page, copyright page, or internal metadata before making bibliographic claims.
8. Pass the resolved local file to the appropriate PDF, document, ebook, or filesystem extraction workflow. Preserve page, chapter, section, and ebook locator boundaries whenever the format permits.

The two default collections are alternate entrances into one RWS workflow. Do not move or duplicate Zotero memberships when a learning task later becomes a writing task; preserve the stable item identity and state the transition in the reading artifact when it affects source scope. Do not turn that transition into an automatic project-state update or meta-reflection.

Interpret the attachment result conservatively:

- `localPath` means that the locator verified an existing local file at that moment;
- `candidatePath` without `localPath` is an unresolved expectation, not a readable file;
- `contentType`, `filename`, and `linkMode` help select a reader but do not establish the file's textual contents;
- an item or attachment key identifies a Zotero record but does not prove edition, translation, completeness, or scan quality.

## Resolve ambiguity and failure

Stop and report the exact ambiguity when several bibliographic items or plausible attachments remain. Prefer the writer's named edition or language over format convenience.

When no `localPath` is available, do not attempt to read `candidatePath`. Report whether the likely cause is an unsynced stored file, an unavailable linked file, or an unsupported path mapping. Continue with another supplied source or web-assisted reading only when the writer's request permits it.

The current Zotero workflow locates attachments; it does not expose Zotero annotations or guarantee EPUB CFI data. Use a CFI, annotation quotation, or annotation comment only when that data was separately supplied or directly extracted and verified.

## Preserve provenance

For a source likely to enter a reading archive or reading card, preserve only the identifiers needed to recover and verify it:

- source origin: `zotero`;
- bibliographic item key;
- attachment key, filename, content type, and link mode;
- edition or translation established from the record or file;
- extraction method and actual inspected coverage;
- locator system and any mismatch between file pages and printed pages.

Treat an absolute Zotero storage path as task-local operational data. Do not preserve it as the durable source identity, because it is machine-specific. Do not copy an attachment into the reading repository, rename it, or change its collection membership unless the writer explicitly requests that separate operation.

## Keep evidence boundaries

Finding an attachment is not reading it. Opening or extracting a whole file is not evidence that every page was inspected. Record direct coverage at the level actually checked, and record OCR failures, image-only pages, missing chapters, DRM or parser limits, and locator loss.

Use Zotero metadata for discovery and provisional bibliography. For an exact quotation, page reference, edition claim, or translation comparison, verify against the attachment content or another direct bibliographic source.
