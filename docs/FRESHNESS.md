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

- Done (2026-09-28): full rollout — 254/254 skills, 309 refs
  (pilot trio, fisco, lavoro, salute, casa+diritto, impresa+PA,
  soldi+famiglia+tutele, trasporti+scuola+scrittura+tooling).
  Stamp tool: `python scripts/check-freshness.py --stamp <skills...>`
  (stamps headers + bumps versions, one theme per change).
- Enforcement: `check-freshness.py --check` is CI-blocking. A date older
  than 12 months fails the build until renewed — stale content cannot
  silently ship.
## Semantic layer (sources → claims)

Timestamps prove a date, not a review. Rolled-out skills additionally carry
`references/fonti-verificate.md` with a `## Sources (verified YYYY-MM-DD)`
block: every bullet names an official source (URL), and maps it to the
claims that depend on it via `claims:`. That header counts as the file's
freshness date (one date per file, never dual) and `--stamp` never touches
semantic files. `scripts/check-sources.py --check`
is CI-blocking on schema+dates; `--check-links` HEADs every URL (advisory).

Pilot (2026-09-28, all HTTP 200 live): pensione-guida (INPS), successioni-info
(AdE), salute-mentale-info (Ministero Salute), cittadinanza (Interno),
separazione-divorzio (Normattiva L.898/1970), licenziamento-info (Lavoro).
Wave 2 (2026-09-28): 34 casa+diritto skills (AdE guide, Normattiva,
ARERA, ENEA/MASE, Notariato, Bankitalia-ABF, IVASS) — 40 semantic skills
total, 0 dead links. Queued (no verified official URL yet):
case-popolari-erp (regional), riscaldamento-contabilizzazione,
multiproprieta-diritti, conciliazione-paritetica, giudice-di-pace.
Rollout continues theme by theme; link monitoring and impact analysis
build on this inventory.

`last-verified` never replaces the year next to each figure — both stay.
