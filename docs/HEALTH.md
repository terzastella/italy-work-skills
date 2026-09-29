# Health snapshot — generated, do not hand-edit

Date: 2026-09-29. Regenerate with `python scripts/build-health.py`.

Gates green: 16/16.

| Gate | Status | Summary |
|---|---|---|
| validate | green | [OK] templates\skill-starter |
| security | green | OK: no obvious secrets/PII/personal paths. |
| json | green | JSON OK |
| indexes | green | INDEX CHECK OK |
| catalog | green | OK: 278 skills classified, 19 themes. |
| golden | green | eval: 63/63 fixtures green |
| oracles | green | oracles: 15/15 independent checks green |
| invariants | green | invariants: 19/19 hold |
| behavior | green | behavior: OK (245 guided, 36 delicate) |
| freshness | green | freshness: 0 missing, 0 stale (254 skills, 309 refs) |
| sources | green | sources: 40 /40 pilot skills schema-ok, 0 stale |
| plugins-sync | green | wrote gemini-extension.json: 278 skills, v1.16.0 |
| install-dryrun | green | Done. |
| installer-attack | green | installer-attack-test: SKIP (no symlink rights: [WinError 1314] Il privilegio richiesto non appartiene al client: 'C:\\Users\\tanta\\AppData\\Local\\Temp\\evils |
| vendors-verify | green | hashes: 268 vendor files byte-identical to snapshot. |
| risk-matrix | green | risk matrix: OK (254 skills) |

Green here means the deterministic gates pass. It does not mean
normative content is current (see freshness column) or that every
skill was agent-tested (see `docs/COMPATIBILITY.md`).
