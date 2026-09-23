# bollette-energia cases

## Offer switch check

Input: 2.700 kWh/y, current €720/y, new offer 0,21 €/kWh + €60/y fixed [sample data].

Output:
```text
New total: 2.700 × 0,21 + 60 = €627 + taxes/accise (recomputed from bill lines)
Saving ≈ €90/y before taxes. Verify on ARERA comparator.
Verdict: switch worth it IF fixed fees confirmed. No endorsement.
```
