---
name: content-gap
description: Find topics competitors cover and you do not. Use when asked content gap, what is missing, competitor topics, what to write.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[niche/url]"
user-invocable: true
disable-model-invocation: false
---

# Content Gap

Write what is missing: data shows the hole, you fill it first.

## When to use

- "content gap", "what is missing", "competitors cover", "what to write".
- Do not use for calendars (see `content-calendar`) or keywords (see `keyword-map`).

## Workflow

1. List your content (titles/URLs) + 2-3 competitors and theirs.
2. Compare by theme: covered by them / by you / by nobody.
3. Output: gap table + top-5 priorities with reason (likely traffic, ease, intent).
4. Per gap: recommended format + angle different from competitors.

## Output format

```text
Covered by them, not you: <n> themes
Top gaps:
1. <theme> — why: <reason>. Format: <guide/checklist>.
2. ...
Already covered well: <short list, do not touch>
```

## Rules

- Priority = strong intent × low effort, never volume alone.
- Mandatory different angle: do not copy, outperform (more data, more examples).
- Gaps without clear intent → `ignore` list, not priorities.

## Examples

See `examples/gap-cases.md`. Comparison method in `references/method.md`.

## Edge cases

- Zero competitor data → gaps from client questions/FAQ instead of competitors.
- Saturated niche → micro-gaps (sub-topics, local cases, updates).
- Giant competitor → attack long-tail, not the head keyword.
