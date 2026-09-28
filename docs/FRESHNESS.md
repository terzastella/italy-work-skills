# Source freshness — keeping legal/fiscal content from going stale

Italian rules change yearly. Year markers and official references are not
enough on their own: nobody re-reads 254 skills every January. This file
defines the lightweight mechanism that makes staleness visible.

## Rule

Every file in `skills/*/references/` carries a machine-readable header:

```text
last-verified: YYYY-MM-DD
```

Meaning: on that date a human confirmed the figures, thresholds, and cited
sources against the official source (AdE, INPS, EUR-Lex, ministry pages).

## Check

```bash
python scripts/check-freshness.py           # report only, exit 0
python scripts/check-freshness.py --check   # exit 2 if anything is stale/missing
```

- Missing header → reported (pilot skills only for now; full rollout later).
- Older than 12 months → STALE, must be re-verified or renewed.
- This check is advisory, not a CI gate — a stale source is a maintenance
  debt, not a broken build. Promote to gate once the rollout is complete.

## Rollout

- Done (2026-09-28): pilot trio + full tax cluster — 35 skills, 47 refs
  (`invoice-it`, `imu-calcolo`, `regime-forfettario` + `Fisco e tasse` theme).
  Stamp tool: `python scripts/check-freshness.py --stamp <skills...>`
  (stamps headers + bumps versions, one theme per change).
- Next: lavoro theme, then salute/diritto. Delicate skills get priority
  after tax.
- `last-verified` never replaces the year next to each figure — both stay.
