# keyword-map cases

## Site quotes

Input keywords: site quote, site cost, showcase site price, showcase site quote.

Output:
```text
Group A (transactional: quote):
- primary: showcase site quote | page: /quote (exists)
- secondary: site quote, site cost
Conflicts: none
Discarded: none
```

## Real conflict

Input: /prices and /quote on the same intent.
Output: `Conflict: merge into /quote, redirect from /prices.`
