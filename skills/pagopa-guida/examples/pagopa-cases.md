# pagopa-guida cases

## Good: TARI notice via IO app

Input: €280 TARI notice with IUV, Rome [sample data].

Output: IO app steps + `pay the notice amount only` + receipt saved as file
+ `deadline from notice (year-stated); late paths differ per tax — flagged.`

## Bad: amount rounded up

Input: "arrotondo a cifra tonda per fare prima" [sample data].

Output: `Pay the notice amount only — rounded payments break reconciliation. Receipt saved as file, stated bluntly.`
