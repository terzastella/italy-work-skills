---
name: infographic-brief
description: Create infographic briefs with data and hierarchy. Use when asked infographic, design brief, data visual.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[topic]"
user-invocable: true
disable-model-invocation: false
---

# Infographic Brief

Briefs a designer executes without calling back: data, hierarchy, final copy.

## When to use

- "infographic", "design/graphic brief", "data visual".
- Do not use for creating the image (brief only).

## Workflow

1. Ask: single message, available data, format (square/stories/A4), brand.
2. Hierarchy: numbered title → 3-5 ordered blocks → source → CTA.
3. Final copy per block (max 15 words), data with source.
4. Ready output to hand to the designer + note on what NOT to include.

## Rules

- 1 message per infographic, never 3.
- Data only as provided/verified with source: never invented percentages.
- Max 5 blocks: beyond that, split into a series.
- Final copy, not "lorem" or vague directions.

## Examples

See `examples/infographic-cases.md`. Layouts in `references/layouts.md`.

## Edge cases

- Zero data → "concept" brief (process, steps) instead of fake numbers.
- Too much data → pick 5, rest behind a "learn more" link.
- Rigid brand → cite existing palette/fonts, no off-brand proposals.
