---
name: tfr-fondo
description: Compare TFR in company vs pension funds. Use when asked TFR, fondo pensione, severance Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# TFR vs Fondi

Severance choice with numbers: TFR revaluation vs fund returns + tax perks.

## When to use

- "TFR", "fondo pensione", "severance Italy", "destinazione TFR".
- Do not use for investment advice (comparison math only).

## Workflow

1. Mechanics + revaluation math with the bundled script (preferred, reproducible):
   TFR accrues yearly, revalues at 1.5% + 75% of year-stated inflation:
   `python skills/tfr-fondo/scripts/rivalutazione.py --accantonato 20000 --inflazione 2.0 --year 2025`
2. Fund alternative: contributions, employer match where due, separate taxation at exit.
3. Compare on: horizon, risk, tax at payout, advance (anticipazioni) rules.
4. Silence-assent rule for new hires stated plainly (opt-out window).

## Rules

- No fund recommendations, no "join X": mechanics + math only.
- Tax-at-exit differences shown with year-stated rules.
- Advance rules (casa/salute %) stated generally, fund specifics referred.

## Scripts

- `scripts/rivalutazione.py` — revaluation math (inflation is a year-stated input).
  Fixtures with expected outputs in `examples/fixtures/`. Mechanics only, never recommendations.

## Examples

See `examples/tfr-cases.md`. Comparison in `references/confronto.md`.

## Edge cases

- Small firms (<50): TFR stays in company vs Fondo Tesoreria INPS — explain split.
- Already chosen years ago → revocability limits stated, no regret engineering.
- Public employees (TFS): different animal entirely — redirect, do not mix.
