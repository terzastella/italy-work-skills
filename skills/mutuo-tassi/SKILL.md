---
name: mutuo-tassi
description: Compare mortgages with TAN/TAEG and total cost. Use when asked mutuo, mortgage Italy, TAN TAEG, surroga.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[offers]"
user-invocable: true
disable-model-invocation: false
---

# Mutuo Tassi

Mortgages compared on total cost: TAN vs TAEG, fees, insurance, fine print.

## When to use

- "mutuo", "mortgage Italy", "TAN/TAEG", "surroga", "tasso fisso/variabile".
- Do not use for financial advice (comparison math only).

## Workflow

1. Take 2+ offers: TAN, TAEG, duration, fees (istruttoria/perizia), insurance (mandatory? cost), spread.
2. Compare on TAEG + total repaid, never TAN alone.
3. Fixed vs variable: explain trade-off plainly + cap/floor notes.
4. Surroga: cost-zero rules + when it pays (remaining years matter).
5. Output table + winner by math + questions for the bank.

## Rules

- TAEG is the comparison number (offers year-stated); TAN alone never decides.
- Insurance costs included in math when mandatory.
- No bank endorsement; no "take it now" pushes.

## Scripts

- `scripts/mutuo.py` — TAEG-based totals + variable shock scenario (rates are inputs).
  Fixtures with expected outputs in `examples/fixtures/`. Compare on TAEG, never TAN alone.

## Examples

See `examples/mutuo-cases.md`. Rate glossary in `references/glossario.md`.

## Edge cases

- Tied insurance (polizza abbinata) → cost it separately, flag tying.
- Early years of variable → payment shock scenarios shown.
- Giovani/first-home perks → state current schemes with year, verify live.
