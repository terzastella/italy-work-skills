---
name: irpef-scaglioni
description: Explain IRPEF brackets with marginal vs average math. Use when asked IRPEF scaglioni, income tax brackets Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[income]"
user-invocable: true
disable-model-invocation: false
---

# IRPEF Scaglioni

Brackets decoded: marginal vs average, with worked math — never fear the jump.

## When to use

- "IRPEF scaglioni", "income tax brackets Italy", "se aumento lo stipendio pago di più?".
- Do not use for full return filing (method + math only, see `cu-730-guida`).
- Do not use for flat-rate regimes (see `regime-forfettario`).

## Workflow

1. Take the user's gross income figure. Never assume one.
2. Load the dated bracket table for the tax year (`examples/scaglioni-2025.json`
   pattern — table year must equal the requested year, verified live).
3. Run the slice math (preferred, reproducible):
   `python skills/irpef-scaglioni/scripts/irpef.py --reddito 35000 --scaglioni skills/irpef-scaglioni/examples/scaglioni-2025.json --year 2025`
4. Show: slice table + total tax + average rate + marginal rate side by side.
5. Kill the classic fear with numbers: only the slice above the threshold pays
   the higher rate — earning more never nets less. Prove it, don't assert it.
6. Detrazioni note: tax credits lower the bill after brackets (separate step, not in the script).

## Rules

- Brackets/rates always with year; reforms move them — verify live, never timeless tables.
- The script refuses mismatched table/request years: that error is a feature, surface it.
- Math shown step by step on user figures only, never assumed incomes.
- Forfettari: different world (see `regime-forfettario`), do not mix.
- Tassazione separata (arrears, TFR): separate track flagged, not merged into slices.

## Scripts

- `scripts/irpef.py` — slice math from an explicit dated table.
  Fixtures with expected outputs in `examples/fixtures/`. Run:
  `python skills/irpef-scaglioni/scripts/irpef.py --help`

## Examples

Good and bad cases in `examples/irpef-cases.md`. Bracket tables live next to
the cases (`examples/scaglioni-YYYY.json`), dated and year-checked.

## Edge cases

- Arrears/tassazione separata → separate track flagged, not merged.
- Foreign income slices → quadro RW interplay mentioned + referral.
- 730 vs Redditi path → routed (see `cu-730-guida`), not computed here.
- Zero/negative input → refused with error, never computed.
- Year without a table → stop and verify live, never reuse last year's table silently.
