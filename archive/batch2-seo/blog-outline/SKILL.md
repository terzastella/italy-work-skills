---
name: blog-outline
description: Create article outlines with intent, H2s and CTA. Use when asked article outline, blog outline, post structure.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[topic/keyword]"
user-invocable: true
disable-model-invocation: false
---

# Blog Outline

Outlines that write themselves: intent, ordered H2s, CTA, no holes.

## When to use

- "article outline", "blog outline", "post structure".
- Do not use for full articles (outline first, text after).

## Workflow

1. Ask: keyword/intent, audience, promise, target length.
2. Outline: H1 + 4-7 H2s in logical order + 2-3 points per H2 + final CTA.
3. Mark where data/examples/screenshots are needed (`[data]`, `[example]`).
4. Close with proposed title + description (see `meta-tags`).

## Output format

```markdown
# <H1 with keyword>
Intent: <1 line>
## <H2 1> — points: ...
## <H2 2> — [data to verify]
...
CTA: <one>
Title/Description: ...
```

## Rules

- Clear intent within H1 + first 100 planned words.
- One idea per H2, no filler H2s.
- Single CTA, consistent with intent (info → newsletter, commercial → contact).

## Examples

See `examples/outline-cases.md`. H2 flows in `references/flow.md`.

## Edge cases

- Ambiguous keyword → 2 short outlines (one per intent), ask which.
- Long article (>2000 words) → H2/H3 parts + opening summary.
- Old post update → diff outline (keep, cut, add).
