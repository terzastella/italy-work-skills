---
name: headline-it
description: Create clickable headlines without clickbait. Use when asked headline, title, article title, post title.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[topic]"
user-invocable: true
disable-model-invocation: false
---

# Headlines

10 headlines to choose from, each with a different angle and reason.

## When to use

- "headline", "title", "article/post/video title".
- Do not use for SEO meta titles (see `meta-tags`).

## Workflow

1. Ask: topic, audience, promise (what the reader gets).
2. Generate 10 headlines: 3 direct, 3 with numbers, 2 questions, 2 emotional angles.
3. Mark the 2 recommended + why. Max 70 chars each.

## Output format

```text
1. [direct] <headline> (62)
...
Recommended: 3 and 7 (why: keyword + number + clear promise)
```

## Rules

- Keepable promise: no "shocking" if it is a basic guide.
- Real numbers or `[n]` placeholders: never invented realistic numbers.
- Clean language: no pointless anglicisms.

## Examples

See `examples/headline-cases.md`. Patterns in `references/patterns.md`.

## Edge cases

- Boring topic → benefit angle ("how to save 2 hours"), not sensationalism.
- Existing title to improve → 5 variants + what changes in each.
- Social length → ≤40-char versions on request.
