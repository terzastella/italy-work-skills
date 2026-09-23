# Copilot (IDE) / Copilot CLI / Cursor adapter

Real skills live in `../../skills/`, same `SKILL.md` format.

```bash
# Copilot project skills (repo)
python ../../scripts/install.py --skill invoice-it --agent copilot
# copies to .github/skills/<name>/

# Copilot CLI personal skills (all projects)
python ../../scripts/install.py --skill invoice-it --agent copilot-cli
# copies to ~/.copilot/skills/<name>/

# Cursor
python ../../scripts/install.py --skill invoice-it --agent cursor
# copies to .cursor/skills/<name>/
```

Copilot CLI also reads `.claude/skills/` and `.agents/skills/`, so repo installs
are shared. No content changes required.

Docs: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot
