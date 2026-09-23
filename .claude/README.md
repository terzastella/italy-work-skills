# Claude Code adapter

Real skills live in `../skills/`. This folder is install documentation only.

## Install

```bash
# All skills, user level
python scripts/install.py --all --agent claude

# Single skill
python scripts/install.py --skill smart-commit --agent claude

# Destinations:
#  personal: ~/.claude/skills/<name>/
#  project:  .claude/skills/<name>/  (generated, not committed - see .gitignore)
```

## Plugin marketplace

This repo also exposes a Claude Code plugin (`.claude-plugin/plugin.json`).
For official Anthropic skills:

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

## Supported fields

`name`, `description`, `license`, `metadata`, `compatibility`, `allowed-tools`.
See `docs/COMPATIBILITY.md`.
