# Windsurf (Cascade) adapter

Real skills live in `../../skills/`, same `SKILL.md` open standard.

## Install

```bash
python ../../scripts/install.py --all --agent windsurf
python ../../scripts/install.py --skill invoice-it --agent windsurf

# Destinations:
#  project: .windsurf/skills/<name>/ (this folder, generated — see .gitignore)
#  user:    ~/.codeium/windsurf/skills/<name>/ (copy manually)
```

Windsurf also discovers `.agents/skills/` (and `.claude/skills/` if Claude
config reading is enabled).

## Important: invoke explicitly

Cascade's automatic skill invocation is unreliable. For guaranteed loading,
invoke with `@<skill-name>` in chat (e.g. `@invoice-it`).

Docs: https://docs.windsurf.com/windsurf/cascade/skills
