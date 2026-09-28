# Spec checklist for new skills

last-verified: 2026-09-28

Copied from the `agentskills.io` standard + repo conventions.

- [ ] Folder `skills/<name>/` with mandatory `SKILL.md`
- [ ] Frontmatter `name`: hyphen-case, max 64, == folder name
- [ ] Frontmatter `description`: what it does + when to use it ("Use when..."), max 1024
- [ ] `license: MIT`, `compatibility`, `metadata: {author, version, lang}`
- [ ] Multi-agent fields untouched: `allowed-tools`, `argument-hint`,
      `user-invocable`, `disable-model-invocation`
- [ ] Body: numbered workflow + verifiable rules + good/bad examples + edge cases
- [ ] Body <500 lines, >20 chars. Details in `references/`, code in `scripts/`
- [ ] No secrets/tokens/PII/absolute paths (check with `scripts/security-check.py`)
- [ ] Every code block with language, paths in backticks
- [ ] Indexes updated: `catalog/skills.json`, `llms.txt`,
      `.claude-plugin/plugin.json`, `README.md`, `docs/COMPATIBILITY.md`
