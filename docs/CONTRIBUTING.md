# Contributing (for humans)

Thank you for helping. You don't need to know our history — just follow
these steps. Technical details for automation live in `AGENTS.md`.

## Add or improve a skill in 5 steps

1. **Copy the template:**
   `cp -r templates/skill-starter skills/my-skill`
2. **Write it in English.** Skill name == folder name (lowercase, hyphens).
   Say what it does and when to use it in the first lines. Keep the main
   file focused; details go in `references/`, examples in `examples/`.
3. **Validate:** `python scripts/validate.py --skill my-skill`
4. **Security scan:** `python scripts/security-check.py`
   (no secrets, no real names or emails, no personal file paths).
5. **Update the lists:** `catalog/skills.json`, `llms.txt`,
   `.claude-plugin/plugin.json`, `docs/COMPATIBILITY.md`, then regenerate
   the catalog with `python scripts/build-catalog.py`.

## Open a pull request

Fill in the template (`.github/PULL_REQUEST_TEMPLATE.md`). Automated checks
run on every PR: file validation, security scan, index coherence, install
dry-run, and example checks. Green on all of them is required.

## Quality gate for new skills (classify first)

Find your level in `docs/RISK-MATRIX.md`, then satisfy its row:

- **L0 informative** — structure, sources, no invented data, examples.
- **L1 operative** — L0 + mandatory inputs, deterministic output, edge cases,
  Good/Bad examples, year markers.
- **L2 calculator** — L1 + neutral script, fixtures with expected outputs,
  hand-computed oracle in `tests/oracles/`, invariants where they apply.
- **L3 delicate** — L1 + info-only + professional referral, never scripts/,
  never verdicts/strategies, `last_verified` from day one.

## Ground rules

- English everywhere in skill content (Italian survives only inside example
  documents: invoice bodies, email bodies, official rates and wordings).
- Every amount states its year. Examples use clearly fake data.
- Sensitive topics (law, health, family, inheritance): information plus a
  professional referral. Never verdicts, never strategies.
- Never edit `vendors/` (pinned third-party copies) or `archive/` (frozen).
- One skill per change when possible; bump its version on every change.

Technical counterpart: `CONTRIBUTING.md` (root) + `AGENTS.md`.
