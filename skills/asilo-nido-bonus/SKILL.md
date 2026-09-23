---
name: asilo-nido-bonus
description: Explain nursery bonus with ISEE bands and application. Use when asked bonus nido, asilo nido bonus, nursery bonus Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[household]"
user-invocable: true
disable-model-invocation: false
---

# Asilo Nido Bonus

Nursery money mapped: ISEE bands, monthly amounts, application path.

## When to use

- "bonus nido", "asilo nido bonus", "nursery bonus Italy".
- Do not use for school choice itself.

## Workflow

1. ISEE link (see `isee-guida`): bands set monthly amount (year-stated tables).
2. Public vs private nursery paths differ: explain both.
3. Apply: INPS online/patronato + payment receipts uploaded monthly.
4. Output: band estimate + steps + deadlines.

## Rules

- Amounts with year; tables move — verify current INPS circular.
- Receipts uploaded monthly or money stops: stressed.
- Home-care alternative (supporto domiciliare) mentioned where due.

## Examples

See `examples/nido-cases.md`. Bands in `references/fasce.md`.

## Edge cases

- Mid-year ISEE change → amount recalculated, timing explained.
- Disabled children: higher support flagged + patronato.
- Late application → arrears limits stated plainly.
