# Release Notes — v1.15.0 (2026-09-25)

**249 original skills + 24 pinned third-party = 273 catalog entries.**
Tag: `v1.15.0` (first tag; SemVer from here: patch = fixes, minor = new skills).

## New: Integrativa 1.15 (deferred closed)

- `contratto-base-check` — guided contract reading, clause map, red flags. Info-only, no validity verdicts.
- `ferie-permessi` — accrual math, fruition deadlines (year-stated), ROL/104 overview.

The two historic deferred skills are closed. No deferred left.

## Previous: v1.14.0 Batch 12-IT (20 skills)

Sindicati/lavoro, impresa/fisco, casa/famiglia/salute, scuola/fine-vita/soldi.
Delicate info-only + referral (affido-familiare, salute-mentale-info).

## Previous: v1.13.0 Vendor batch (24 pinned)

anthropics-skills (10, Apache-2.0), mattpocock-skills (6, MIT), superpowers (8, MIT).
Byte-identical copies pinned in `vendors/upstreams.lock.json`. Opt-in via
`python scripts/install.py --all --source vendors`.

## Install

```bash
python scripts/install.py --all                          # ours only (default)
python scripts/install.py --all --source vendors         # ours + third-party
python scripts/install.py --skill <name> --agent claude  # one skill, one agent
```

9 agents: claude, codex, grok, cursor, copilot, copilot-cli, gemini, opencode, windsurf.

## Gates (all green)

`validate.py` 274 OK · `security-check.py` clean · JSON indexes valid ·
`install.py` dry-run 2739 destinations (249 × 11) · `build-catalog.py --check` clean.

Full history: `CHANGELOG.md`.
