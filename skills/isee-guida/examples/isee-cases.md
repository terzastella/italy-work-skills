# isee-guida cases

## Good: family of 4, first DSU

Input: 2 employees + 2 minors, 1 home, 2 accounts [sample data].

Output: documents list (CUs, 31/12 balances + giacenza media per account,
property papers, car plates) + filing routes (INPS online/CAF/patronato) +
`classic mistake avoided: bring 31/12 balances, not current ones.`
No ISEE number computed here.

## Bad: number computed

Input: "calcolami l'ISEE" with household data [sample data].

Output: no number. `Never compute a final ISEE number: method + checklist, INPS calculates.`

## Bad: current balances

Input: user brings this month's statements [sample data].

Output: `Balances at 31/12 of year-2 + giacenza media — current ones are the classic mistake, stated first.`
