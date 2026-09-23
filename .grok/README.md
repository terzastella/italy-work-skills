# Grok adapter

Real skills live in `../skills/`. Grok already reads Claude Code
and `.agents/skills/` with zero extra configuration.

## Install

```bash
python scripts/install.py --all --agent grok
python scripts/install.py --skill smart-commit --agent grok

# Destinations:
#  ~/.grok/skills/<name>/
#  ./.grok/skills/<name>/  (project, walked up to repo root)
# Grok also reads: ~/.claude/skills/, .agents/skills/, ~/.agents/skills/
```

## Slash commands

Every `user-invocable: true` skill appears as `/<skill-name>`.
E.g. `/smart-commit`, `/doc-polish-it`.

Extra Grok-supported fields in this repo:
`argument-hint`, `user-invocable`, `disable-model-invocation`, `metadata`.

Docs: https://docs.x.ai/build/features/skills-plugins-marketplaces.md
