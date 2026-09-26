# visura-leggimi cases

## Good: supplier check before paying

Input: visura ordinaria dated 01/09/2026, active, matching VAT [sample data].

Output: sections summary + `no open procedures, 1 address change in 2025`
+ `snapshot 01/09/2026 — for credit decisions verify with professional.`

## Mismatch found

Output: `Invoice VAT X vs visura VAT Y — do not pay, verify first.`
Neutral facts, no accusations.

## Bad: pay anyway

Input: "pago lo stesso, tanto è urgente" despite mismatch [sample data].

Output: `Mismatch = stop. Urgency never overrides verification — do not pay, verify first, stated bluntly.`
