---
name: riscatto-laurea
description: Explain degree buyback costs and convenience check. Use when asked riscatto laurea, degree buyback Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write Bash
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Riscatto Laurea

Buy back degree years: cost methods, convenience test, application path.

## When to use

- "riscatto laurea", "degree buyback Italy".
- Do not use for pension math itself (see `pensione-guida`).

## Workflow

1. Requirements: degree completed, uncovered years (no contributions overlapping).
2. Cost methods with the bundled script (preferred, reproducible): years × year-stated tariff
   (ordinary income-based vs agevolato flat — tariff is the input, method table in `references/metodi.md`):
   `python skills/riscatto-laurea/scripts/riscatto.py --anni 5 --tariffa 6000 --year 2026`
3. Convenience test: years needed for target path vs cost vs tax deduction benefit.
4. Output: method comparison + documents + INPS/patronato route. No purchase advice as fact.

## Rules

- Costs with year and method; flat-rate windows are temporary — verify live.
- Deductibility note (from income) with current rules cited.
- Inoccupati periods: separate favorable track flagged.

## Scripts

- `scripts/riscatto.py` — cost math (tariff is a year-stated input).
  Fixtures with expected outputs in `examples/fixtures/`. Method choice with numbers, never advice as fact.

## Examples

See `examples/riscatto-cases.md`. Method table in `references/metodi.md`.

## Edge cases

- Laurea abroad → recognition first, then buyback eligibility.
- Near-retirement buyback → payoff-time math shown, honest about short horizon.
- Coexisting riscatti (military, etc.) → each evaluated separately, patronato.
