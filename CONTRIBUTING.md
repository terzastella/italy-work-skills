# Contributing (local only for now)

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
4. Validate and test locally:
   ```bash
   python scripts/validate.py --skill <skill-name>
   python scripts/security-check.py
   python scripts/install.py --skill <skill-name> --dest ./tmp-test --all
   Remove-Item ./tmp-test -Recurse -Force
   ```
5. Update indexes: `catalog/skills.json`, `llms.txt`,
   `.claude-plugin/plugin.json`, `docs/COMPATIBILITY.md` table.
6. Regenerate the catalog: `python scripts/build-catalog.py` (never edit
   `docs/CATALOG.md` by hand; fix `scripts/build-catalog.py` keywords or
   overrides instead if a skill lands in the wrong theme).

## Rules

- Single source of truth: `skills/`. Never duplicate into `.claude/`, `.grok/`, `.agents/`.
- `vendors/` is read-only: never hand-edit, never add ours there. Updates via
  `scripts/sync-vendors.py` flow (re-copy, verify hashes, bump lock).
- No secrets, tokens, personal absolute paths, PII.
- English everywhere. Sober tone, no emoji.
- Max ~500 lines per `SKILL.md`, details in `references/`.
