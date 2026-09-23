# pdf-extract-it cases

## Native report with table

Input: `report.pdf` 8 pages, selectable text, table on p. 3.

Output: full markdown text + p. 3 table converted with headers
+ note `Source: report.pdf, pp. 1-8`.

## Partial scan

Input: `contract_scan.pdf`, pp. 1-2 text, 3-5 skewed images.

Output: text pp. 1-2 + `pp. 3-5: scanned, ~70% readable, [unreadable]` where needed
+ warning "request original for legal value".
