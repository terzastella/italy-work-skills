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

- Missing header → reported for every skill (rollout complete: 254/254).
- Older than 12 months → STALE, must be re-verified or renewed.
- This check is CI-blocking — a stale source fails the build until renewed.

## Rollout

- Done (2026-09-28): full rollout — 254/254 skills, 269 refs
  (pilot trio, fisco, lavoro, salute, casa+diritto, impresa+PA,
  soldi+famiglia+tutele, trasporti+scuola+scrittura+tooling).
  Stamp tool: `python scripts/check-freshness.py --stamp <skills...>`
  (stamps headers + bumps versions, one theme per change).
- Enforcement: `check-freshness.py --check` is CI-blocking. A date older
  than 12 months fails the build until renewed — stale content cannot
  silently ship.
- `last-verified` never replaces the year next to each figure — both stay.
