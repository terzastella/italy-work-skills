# csv-clean cases

## Semicolon CSV

Input (`clients.csv`, Latin-1, `;`):
```text
Name;City;Spent
John ;Boston;120.50
John ;Boston;120.50

Ann;Chicago;80
```

Report:
```text
File: clients.csv | Rows: 5 → 3 | Columns: 3
Encoding: Latin-1 → UTF-8
Header: ok
Removed: 1 duplicate, 1 empty row
Trimmed: 2 cells | Types: Spent → number
Output: clients.clean.csv (original untouched)
```

## Ambiguous dates (blocked)

Input with mixed `01/02/03`: no fixes, output
`Rows 4,7,9: ambiguous date, specify format (DD/MM/YY or MM/DD/YY).`
