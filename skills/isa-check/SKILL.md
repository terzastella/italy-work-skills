---
name: isa-check
description: Explain ISA reliability indexes with score reading. Use when asked ISA, indici affidabilità, ISA score, pagella fiscale.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[activity]"
user-invocable: true
disable-model-invocation: false
---

# ISA Check

ISA scores decoded: what the 1-10 number means and which benefits it unlocks.

## When to use

- "ISA", "indici affidabilità", "ISA score", "pagella fiscale".
- Do not use for computing the score (AdE software/data only).

## Workflow

1. Explain: ISA replaces studi di settore; score 1-10 from data coherence indicators.
2. Thresholds: ≥8-9 benefits (fewer controls, faster refunds, no visto for compensations) — current list with year.
3. Reading a score: which indicators drag it (see `references/indicatori.md`), improvement levers that are legitimate.
4. Close with accountant review (data quality decides the score).

## Rules

- Never compute/predict a score: reading only.
- Benefits list with year — regimes change.
- No gaming advice: legitimate data quality only, never figure-tweaking.

## Examples

See `examples/isa-cases.md`.

## Edge cases

- Excluded subjects (forfettari, start cases) → ISA does not apply, say why.
- Low score panic → plan: data review + next-year indicators, no quick fixes.
- Flat-rate + ISA confusion → separate regimes, explain boundary.
