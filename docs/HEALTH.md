# Health snapshot — generated, do not hand-edit

Date: 2026-09-28. Regenerate with `python scripts/build-health.py`.

Gates green: 11/11.

| Gate | Status | Summary |
|---|---|---|
| validate | green | [OK] templates\skill-starter |
| security | green | OK: no obvious secrets/PII/personal paths. |
| indexes | green | INDEX CHECK OK |
| catalog | green | OK: 278 skills classified, 19 themes. |
| golden | green | eval: 63/63 fixtures green |
| oracles | green | oracles: 5/5 independent checks green |
| invariants | green | invariants: 10/10 hold |
| behavior | green | behavior: OK (245 guided, 36 delicate) |
| freshness | green | freshness: 0 missing, 0 stale (254 skills, 269 refs) |
| vendors | green | hashes: 257 vendor files byte-identical to snapshot. |
| risk-matrix | green | risk matrix: OK (254 skills) |

Green here means the deterministic gates pass. It does not mean
normative content is current (see freshness column) or that every
skill was agent-tested (see `docs/COMPATIBILITY.md`).
