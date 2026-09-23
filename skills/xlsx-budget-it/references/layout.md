# xlsx-budget-it sheet layout

`Income` sheet: `Date | Item | Amount`
`Expenses` sheet: `Date | Category | Item | Amount`
`Summary` sheet:
- `Total income =SUM(Income!C:C)`
- `Total expenses =SUM(Expenses!D:D)`
- `Balance =Income-Expenses`
- Per-category table: `=SUMIF(Expenses!B:B, "Housing", Expenses!D:D)` etc.
- `% category =Category/TotalExpenses`

Default categories (max 8): Housing, Food, Transport, Health, Leisure, Other.
Row 1 always header. No hand-written totals.
