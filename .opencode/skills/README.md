# OpenCode adapter

Real skills live in `../../skills/`, same `SKILL.md` open standard.
OpenCode discovers them natively — no conversion needed.

## Install

```bash
python ../../scripts/install.py --all --agent opencode
python ../../scripts/install.py --skill invoice-it --agent opencode

# Destinations:
#  project: .opencode/skills/<name>/ (this folder, generated — see .gitignore)
#  user:    ~/.config/opencode/skills/<name>/
```

OpenCode also reads `.claude/skills/` and `.agents/skills/` for compatibility,
so skills installed for Claude/Codex are visible too.
Frontmatter rules are identical (name 1-64 hyphen-case, description 1-1024).

Docs: https://opencode.ai/docs/skills
