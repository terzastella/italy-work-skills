---
name: aspettativa-lavoro
description: Explain unpaid leave with contribution effects. Use when asked aspettativa, unpaid leave Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Aspettativa (Unpaid Leave)

Time off unpaid, done right: types, contributions gap, return rights.

## When to use

- "aspettativa", "unpaid leave Italy".
- Do not use for parental/maternity tracks (see `maternita-congedi`).

## Workflow

1. Type: consensual (employer agrees) vs legal cases (mandates, serious family reasons per CCNL/law).
2. Effects: no pay, no contributions (gap!), seniority rules vary — stated plainly.
3. Request: written with dates + reason; employer reply terms where due.
4. Output: path + effects + voluntary-contribution option note.

## Rules

- Contribution gap stressed first: the hidden cost of aspettativa.
- CCNL specifics cited, never generic durations as law.
- Refusal: legitimate reasons listed, appeal paths + referral.

## Examples

See `examples/aspettativa-cases.md`. Effects in `references/effetti.md`.

## Edge cases

- Study leave (diritto allo studio/150 ore) → separate paid track, routed.
- Public employees → different rules flagged, not mixed.
- Return denied/delayed → rights + referral, documented everything.
