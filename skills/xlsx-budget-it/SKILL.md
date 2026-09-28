---
name: xlsx-budget-it
description: Create monthly Excel budgets with sheets, formulas and summary. Use when asked Excel budget, expense sheet, expense tracker, household budget.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write Bash
argument-hint: "[month]"
user-invocable: true
disable-model-invocation: false
---

# Budget Tracker

Ready monthly budget: income, expenses per category, summary with formulas.

## When to use

- "Excel budget", "expense sheet", "expense tracker", "household/monthly budget".
- Do not use for advanced statistical analysis.

## Workflow

1. Ask (if missing): month, currency, categories (defaults below), known income.
2. Build with the bundled script (preferred, reproducible):
   `python skills/xlsx-budget-it/scripts/budget.py --month 2026-01 --income 2000 --spese affitto:800 spesa:350 trasporti:120 --out budget-2026-01`
   Stdlib only: writes Income.csv + Expenses.csv (open in Excel) and prints the Summary JSON.
2. Fixed 3-sheet structure: `Income` | `Expenses` | `Summary`.
3. Mandatory formulas: `SUM` per category, `=Income-TotalExpenses`, `%` per category.
4. Default categories: Housing, Food, Transport, Health, Leisure, Other. Max 8.
5. Deliver file + 5-line chat summary.

## Rules

- Formulas, not hand-computed values: every total is a formula.
- Header always row 1, one row = one entry with date.
- Formatted currency, no invented cents beyond given data.

## Scripts

- `scripts/budget.py` — CSV builder + summary math (balance, per-category share).
  Fixture with expected output in `examples/fixtures/`. Convert CSVs to .xlsx
  with SUM formulas when openpyxl is available; never hand-compute totals.

## Examples

See `examples/budget-cases.md`. Sheet layout in `references/layout.md`.

## Edge cases

- No data given → empty template with 2 rows marked `[example]`.
- Multiple months → one file per month + `Year` sheet with links, not 12 sheets at once.
- Foreign currency → currency column + rate note, do not convert by fantasy.
- Sizing an emergency fund from the balance → see `fondo-emergenza`.
