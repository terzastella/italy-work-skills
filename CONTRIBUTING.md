# Contributing — technical entrypoint

Human version: `docs/CONTRIBUTING.md` (includes the L0–L3 quality gate).
Automation rules: `AGENTS.md`.

## How to propose a skill (in English)

1. Copy the template:
   ```bash
   cp -r templates/skill-starter skills/<skill-name>
   ```
2. Edit `skills/<skill-name>/SKILL.md`:
   - `name` == folder name, hyphen-case, max 64
   - `description` = what it does + when to use it, max 1024, English
   - keep `license: MIT`, `compatibility`, `metadata: {author, version, lang: "en"}`
3. Add depth: `scripts/` for code, `references/` for checklists,
   `assets/` for templates, `examples/` for before/after.
4. Validate and test locally (all must pass):
   ```bash
   python scripts/validate.py
   python scripts/security-check.py
   python scripts/check-indexes.py
   python scripts/build-catalog.py --check
   python scripts/eval-golden.py       # if you touched a skill with scripts/
   python scripts/check-oracles.py     # same
   python scripts/check-invariants.py  # same
   python scripts/eval-behavior.py
   python scripts/check-freshness.py --check
   python scripts/install.py --skill <skill-name> --dest ./tmp-test --all
   Remove-Item ./tmp-test -Recurse -Force
   ```
5. Update indexes: `catalog/skills.json`, `llms.txt`,
   `.claude-plugin/plugin.json`, `docs/COMPATIBILITY.md` table.
   Regenerate: `python scripts/build-catalog.py`, `python scripts/build-plugins.py`,
   `python scripts/build-risk-matrix.py`, `python scripts/build-health.py`
   (never hand-edit `docs/CATALOG.md`, manifests, `docs/RISK-MATRIX.md`,
   `docs/HEALTH.md`; fix the generators instead).

## Rules

- Single source of truth: `skills/`. Never duplicate into `.claude/`, `.grok/`, `.agents/`.
- `vendors/` is read-only: never hand-edit, never add originals there. Updates via
  `scripts/sync-vendors.py` flow (re-copy, verify hashes, bump lock).
- No secrets, tokens, personal absolute paths, PII.
- English everywhere. Sober tone, no emoji.
- Max ~500 lines per `SKILL.md`, details in `references/`.
