---
name: source-cite
description: Verify quotes and sources with consistent format. Use when asked cite sources, bibliography, references, verify quote.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[text or link]"
user-invocable: true
disable-model-invocation: false
---

# Source Cite

Citations that hold: verifiable, complete, uniformly formatted.

## When to use

- "cite sources", "bibliography", "references", "verify quote/link".
- Do not use for exploratory research (see `web-research`).

## Workflow

1. For each claim needing a source: find the original (not a quote of a quote).
2. Verify link: reachable? Does the content really say so? Date?
3. Format everything in one style (card below). Max 1 style per document.
4. Flag weak sources (authorless blogs, dead links) with `[weak]` tag.

## Card format

```text
[1] Author. Title. Publisher, date. <link>
    Supports: <1 line what it backs>
```

## Rules

- Never cite what you did not verify.
- No "ibid/op.cit.": every entry self-contained.
- If source not found → `[source unverified]`, never an invented link.
- Dates always present.

## Examples

See `examples/cite-cases.md`. Styles in `references/styles.md`.

## Edge cases

- Dead link → look for archive/cache, else mark `[dead link, verified on DD/MM/YYYY]`.
- Offline-only source → full citation without link, `[offline]` tag.
- Quote of a quote → trace to original or mark `[secondary]`.
