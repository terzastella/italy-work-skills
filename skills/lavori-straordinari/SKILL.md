---
name: lavori-straordinari
description: Guide extraordinary condo works with funds and bids. Use when asked lavori straordinari condominio, facade works Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[works]"
user-invocable: true
disable-model-invocation: false
---

# Lavori Straordinari

Big works done right: majorities, special fund, compared bids.

## When to use

- "lavori straordinari condominio", "facade works Italy".
- Do not use for permits (see `edilizia-cila-scia`).

## Workflow

1. Majority for the work type (innovazioni vs manutenzione, year-stated).
2. Fondo speciale: mandatory advance fund proportion (year-stated), collected before starting.
3. Bids: 2-3 comparable preventivi + capitolato + direttore lavori where due.
4. Bonus links (see `bonus-casa`) + payment tracing. Output: decision pack.

## Rules

- No works without fund: stated as rule, not advice.
- Single-bid awards flagged (competition required in spirit).
- Urgent works (pericolo): fast track with ratifica after — order matters.

## Examples

See `examples/straordinari-cases.md`. Majority + fund in `references/regole.md`.

## Edge cases

- Dissenters refusing to pay → enforcement paths + referral, no self-help.
- Appalto gone wrong → collaudo + reserves + lawyer referral, documented all.
- Superbonus-era leftovers → credit/cession status check first.
