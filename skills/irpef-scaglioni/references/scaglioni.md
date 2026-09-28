# IRPEF brackets (irpef-scaglioni)

last-verified: 2026-09-28

Slice principle: each income slice pays its own rate. Total = sum of slices.
Average rate = total / income. Marginal rate = rate of the top slice.

Dated tables live in `examples/scaglioni-YYYY.json` (e.g. 2025: 23% to 28.000,
25% to 50.000, 43% above). Every table carries its year and a VERIFY LIVE note.

Reforms move brackets — a table is valid only for its year. The script enforces
this: table year must equal the requested year or it errors out.

Detrazioni (tax credits) apply after brackets and are a separate computation,
not part of slice math. Forfettari live in a different world entirely
(see `regime-forfettario`).
