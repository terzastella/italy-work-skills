# bollette-energia cases

## Good: offer switch check

Input: 2.700 kWh/y, current €720/y, new offer 0,21 €/kWh + €60/y fixed [sample data].

Output:
```text
New total: 2.700 × 0,21 + 60 = €627 + taxes/accise (recomputed from bill lines)
Saving ≈ €90/y before taxes. Verify on ARERA comparator.
Verdict: switch worth it IF fixed fees confirmed. No endorsement.

## Bad: headline-price trap

Input: "offerta a 0,15 €/kWh, conviene?" with no fixed fees [sample data].

Output: no verdict. `Fixed fees + taxes recomputed from bill lines first — headline price alone decides nothing.`
```
