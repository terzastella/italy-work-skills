# nota-spese cases

## Good: Milan trip

Input: train €86 (ticket), hotel €120 (invoice), 2 meals €45 (1 receipt missing) [sample data].

Output:
```text
12/09 train €86 [ok] | 12/09 hotel €120 [ok] | 12/09 dinner €25 [ok] | 13/09 lunch €20 [NO RECEIPT]
Total: €251 | To fix: 1 missing receipt (lunch 13/09)
```
Report + fix list, nothing silently accepted.

## Bad: missing receipt accepted

Input: "tanto sono 20 euro, mettili lo stesso" [sample data].

Output: `Nothing silently accepted — missing receipt stays flagged until fixed, amounts never invented.`
