# mutuo-tassi cases

## Good: two offers compared (script)

Input: A 3.1% TAEG fixed vs B 2.6% TAN variable, 20y €180k [sample data].

Run: `python skills/mutuo-tassi/scripts/mutuo.py --capitale 180000 --anni 20 --taeg-a 3.1 --tan-b 2.6 --shock 2.0`

Output: A totale €241.754 vs B €231.029 (shock €275.642) + `A costs more
but sleeps better; B wins IF rates stay — your call with numbers, no endorsement.`
+ questions for banks (insurance, fees, cap?).

## Bad: TAN-only comparison

Input: "2,6 vs 3,1, prendo il 2,6" [sample data].

Output: stop. `Compare on TAEG totals + shock scenario — TAN alone decides nothing, stated bluntly.`
