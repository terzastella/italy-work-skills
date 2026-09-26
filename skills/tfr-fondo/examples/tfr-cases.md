# tfr-fondo cases

## Good: new hire choice (script)

Input: first job, €20.000 accrued projection, inflation 2,0% (2025, given), 6 months to decide [sample data].

Run: `python skills/tfr-fondo/scripts/rivalutazione.py --accantonato 20000 --inflazione 2.0 --year 2025`

Output: tasso 3,0% → rivalutazione €600 + fund side mechanics + silence-assent deadline + `no fund names, no "join X" — math only. Decide with numbers, revisit yearly.`

## Good: high-inflation year

Input: €10.000 stock, inflation 5,0% (2025, given) [sample data].

Output: tasso 5,25% → €525. `Formula fixed, inflation is the variable — always year-stated.`

## Bad: fund recommendation

Input: "which fund should I join?" [sample data].

Output: no names. `Mechanics + math only — the choice needs a licensed advisor, stated plainly.`
