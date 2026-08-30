# Project state schema

Use only sections that carry current information. Keep the file concise enough to inspect at the start of a task.

```markdown
# 项目状态

- 项目：
- 任务类型：学习｜明确写作专题
- Zotero 入口：导航根 → 已解析任务 collection；仅任务 collection 当前层级
- 当前阶段：
- 最后更新：
- 当前可继续的位置：

## 产物登记

| 类型 | 文件或来源 | 状态 | 主要限制 |
|---|---|---|---|

## 活跃研究线索

| ID | 线索 | 来源状态 | 当前状态 | 相关材料 | 下一责任方 |
|---|---|---|---|---|---|

## 跨技能队列

### 返回 reading-skill

### 返回 thinking-skill

### 交给 writing-skill

## 作者决定

## 项目完整性问题

## 下一步

## 状态变更

- YYYY-MM-DD：只记录会影响恢复项目的变化。
```

## Status meanings

Artifact status:

- `active`: currently being changed;
- `ready_for_handoff`: sufficient for the next named skill;
- `awaiting_review`: continuous prose exists but has not completed its requested review;
- `needs_source_check`: rhetorically usable but not source-verified;
- `complete_for_scope`: complete only for the stated scope;
- `superseded`: retained for history but no longer current.

Research-line provenance:

- `writer_confirmed`: the writer explicitly formulated or accepted the line;
- `source_derived`: directly motivated by established source material;
- `model_suggested`: proposed by Codex and not yet accepted;
- `open`: provenance or commitment is not yet settled.

Never use a completion label without stating the scope. A reading card may be `complete_for_scope` while the book remains only partially read.

## Index policy

- Keep one canonical link to the current artifact and retain older versions only when they matter.
- For a source managed outside the repository, such as a Zotero attachment, register a stable source identity and its access or coverage limit; do not substitute a machine-specific absolute storage path or copy the source into the project automatically.
- Record one active Zotero navigation root and one resolved task collection by default. Add or change an entrance only when the writer changes the task type or explicitly scopes more than one collection; never infer permission to merge roots, crawl sibling branches, or traverse below the resolved task collection.
- Remove or repair links to nonexistent files.
- Do not list temporary files, caches, or abandoned generated artifacts.
- Keep indexes descriptive; keep decisions and queues in the canonical state file.
- When a status sentence conflicts with the state file, update the status sentence rather than duplicating the entire state.
