# AGENTS.md

Instructions for AI agents working in this repo.

## Source of truth

- Original skills live only in `skills/<name>/SKILL.md` (+ `references/`, `examples/`,
  `scripts/` for neutral calculators, `assets/` for templates).
- `vendors/` are pinned byte-identical third-party copies. **Never hand-edit.**
- `archive/` is frozen. Never install from it, never list it in indexes.

## Rules

- Skill content in **English only** (Italian survives only as domain artifact:
  invoice bodies, email bodies, rates, legal wording). Only `README-IT.md`/`README.md`
  landing pages may be Italian — check which one this repo uses.
- `SKILL.md`: `name` (hyphen-case) == folder name, max 64 chars. `description`
  states what + when ("Use when..."), max 1024 chars. Body < 500 lines;
  details go to `references/`, code to `scripts/`, templates to `assets/`.
- Frontmatter: `license` (MIT for ours), `compatibility` (environment requirements
  when needed), `metadata: {author, version, lang}`, `allowed-tools`
  (`Read Write`; +`Bash` only when the skill ships a script), `argument-hint`,
  `user-invocable`, `disable-model-invocation`.
- Delicate skills (legal/health/family): info-only + professional referral.
  Never validity verdicts, never strategies, never executable legal acts.
- No secrets, no PII, no absolute personal paths, no real names or emails.
  Fiscal figures always carry their year. Examples use marked fake data.
- Bump `metadata.version` on every skill change. One skill per change when possible.

## Workflow

```bash
cp -r templates/skill-starter skills/my-skill
# edit, then:
python scripts/validate.py --skill my-skill
python scripts/security-check.py
python scripts/check-indexes.py
python scripts/build-catalog.py --check
python scripts/eval-golden.py  # if you touched a skill with scripts/
python scripts/eval-behavior.py  # if you touched Golden skills or delicate ones
```

Update indexes: `catalog/skills.json`, `llms.txt`, `.claude-plugin/plugin.json`,
`docs/COMPATIBILITY.md`, regenerate `docs/CATALOG.md` with
`python scripts/build-catalog.py`. See `docs/CREATE-SKILL.md` and `CONTRIBUTING.md`.
