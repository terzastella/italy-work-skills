# xlsx-budget-it cases

## Good: January budget with data (script)

Input: salary $2000, rent $800, groceries $350, transport $120.

Run: `python skills/xlsx-budget-it/scripts/budget.py --month 2026-01 --income 2000 --spese affitto:800 spesa:350 trasporti:120 --out budget-2026-01`

Output: `budget-2026-01/` (Income.csv + Expenses.csv, open in Excel, add SUM formulas) + summary:
```text
Income: $2000 | Expenses: $1270 | Balance: $730
Housing 63% | Food 28% | Transport 9%
```

## Good: no data

Output: run script with `--income 0` and no `--spese`, then empty template with 2 `[example]` rows + `Delete the example rows and enter your items.`

## Bad: hand-computed totals

Input: any budget request [sample data].

Output: never type totals by hand. `Formulas (or the script), not hand-computed values: every total is computed.`
