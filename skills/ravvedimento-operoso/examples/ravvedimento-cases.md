# ravvedimento-operoso cases

## Good: 40-day late VAT (script)

Input: €2.000 VAT, 40 days late, no notices [sample data].

Run: `python skills/ravvedimento-operoso/scripts/ravvedimento.py --imposta 2000 --giorni 40 --sanzione-pct 1.5 --tasso-legale 2.0 --year 2026`

Output: sanzione €30 + interessi €4,38 → totale €2.034,38 + F24 codes + `pay now —
each day costs. Verify band % live before paying.`

## Bad: audit already started

Input: avviso di accertamento received, "can I still ravvedere?" [sample data].

Output: stop. `Audit started → different track. Never advise hiding: spontaneous + fast is the whole point — referral now.`
