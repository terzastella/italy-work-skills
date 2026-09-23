---
name: content-calendar
description: Create monthly editorial calendars with channels and formats. Use when asked editorial calendar, content plan, what to publish.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[month/theme]"
user-invocable: true
disable-model-invocation: false
---

# Content Calendar

A month of content in a table: date, channel, format, theme, CTA.

## When to use

- "editorial calendar", "content plan", "what to publish".
- Do not use for single pieces (see `blog-outline`, `social-post-it`).

## Workflow

1. Ask: month, channels (blog/social/newsletter), sustainable real frequency, themes.
2. Table with 4 columns: Date | Channel | Format+Theme | CTA.
3. Balance: 40% value, 30% product, 20% social proof, 10% behind the scenes.
4. Close with weekly load (piece count) + warning if unsustainable.

## Output format

```text
Week 1:
Mon — blog — guide [theme] → CTA: newsletter
Wed — social — 3-point carousel → CTA: comment
...
Load: 6 pieces/week. Sustainable? <yes/no + proposed cut>
```

## Rules

- Honest frequency: 2/week kept beats 7 abandoned.
- Every piece has a CTA, never purposeless content.
- Real dates of the asked month.

## Examples

See `examples/calendar-cases.md`. Format mix in `references/mix.md`.

## Edge cases

- Single channel → vertical calendar with fixed weekly columns.
- Zero themes → propose 4 sector pillars before the calendar.
- Team of 1 → max 3 pieces/week, systematic reuse (see `repurpose-content`).
