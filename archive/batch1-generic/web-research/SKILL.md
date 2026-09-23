---
name: web-research
description: Guided web research with cited summary and source comparison. Use when asked research, find information, compare sources, overview of.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[question]"
user-invocable: true
disable-model-invocation: false
---

# Web Research

Sourced answers: summary + citations + declared disagreements.

## When to use

- "research", "find information", "overview of", "compare sources".
- Do not use for formal citations (see `source-cite`).

## Workflow

1. Split the question into 2-4 searchable sub-questions.
2. Search and open primary sources (official docs, papers, repos) before blogs.
3. Summary max 20 lines + fact table with one source per row.
4. Close with "What we do not know" (source limits) if relevant.

## Output format

```text
Summary: <5 lines max>
Facts:
- <fact> [source: <name>, <date>]
Disagreements: <sources in conflict or "none">
Limits: <what is missing>
```

## Rules

- Minimum 2 independent sources for key facts.
- Always record each source's date (freshness).
- Never present as certain what a single source says.
- Full links, never shortened/invented.

## Examples

See `examples/research-cases.md`. Source hierarchy in `references/sources.md`.

## Edge cases

- Sources disagree → show both with dates, do not pick silently.
- Only old sources (>2 years on fast topics) → obsolescence warning.
- Paywall → use visible abstract/meta, declare limit, do not bypass.
