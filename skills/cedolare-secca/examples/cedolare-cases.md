# cedolare-secca cases

## Good: €12k rent, 35% marginal (script)

Input: €12.000/y, 35% marginal [sample data].

Run: `python skills/cedolare-secca/scripts/cedolare.py --canone 12000 --cedolare 21 --marginale 35`

Output: `21% flat = €2.520 vs IRPEF ≈ €4.200 + addizionali → cedolare wins here.
Marginal asked, not assumed. Option steps included.`

## Bad: marginal assumed

Input: "conviene la cedolare?" with no marginal rate [sample data].

Output: no winner. `Marginal rate asked: never assume 23/25/35/43% — one question first, math after.`

## Bad: commercial use

Input: shop rental asking cedolare [sample data].

Output: `Commercial use excluded — say it when relevant, no math run.`
