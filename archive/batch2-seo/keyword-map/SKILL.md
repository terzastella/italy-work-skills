---
name: keyword-map
description: Map keywords to pages without cannibalization. Use when asked keywords, keyword map, keyword mapping, avoid cannibalization.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[keyword list]"
user-invocable: true
disable-model-invocation: false
---

# Keyword Map

Every keyword gets 1 page: no two pages competing with each other.

## When to use

- "keywords", "keyword map", "cannibalization", "content architecture".
- Do not use for snippets (see `meta-tags`).

## Workflow

1. Take keyword list + existing pages (URLs or titles).
2. Group by intent (same question = same group).
3. Table: Group | Primary keyword | Secondary | Page (exists/to create).
4. Flag conflicts: 2 pages on the same intent → merge or canonical.

## Output format

```text
Group A (intent: quote):
- primary: showcase site quote | page: /quote (exists)
- secondary: site cost, showcase site price
Conflicts: /prices and /quote same intent → merge into /quote
```

## Rules

- 1 intent = 1 page, no silent exceptions.
- Long-tail merged into primary, never 100-word pages.
- Keywords without clear volume/intent → motivated `discard` list.

## Examples

See `examples/map-cases.md`. Intent types in `references/intent.md`.

## Edge cases

- Zero existing pages → map from scratch with priority (first 5 groups).
- E-commerce variants → 1 category page + filters, not 1 page per variant.
- Competitor brand keywords → advise against direct targeting, propose honest comparison.
