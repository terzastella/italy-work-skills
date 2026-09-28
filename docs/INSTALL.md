# Install guide

## Requirements

- Python 3.10+ (`python --version` to check).
- Git, to clone the repository.
- One of the supported agents (see table below).

## Install everything

```bash
git clone https://github.com/terzastella/italy-work-skills.git
cd italy-work-skills
python scripts/install.py --all
```

This copies all 254 original skills into every agent folder on your machine.

## Install one skill on one agent

```bash
python scripts/install.py --skill invoice-it --agent claude
python scripts/install.py --skill invoice-it --agent codex
```

Agent names: `claude`, `codex`, `grok`, `cursor`, `copilot`, `copilot-cli`,
`gemini`, `opencode`, `windsurf`.

## Where skills land

| Agent | Folder |
|-------|--------|
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.agents/skills/` |
| Grok | `~/.grok/skills/` |
| Cursor | `.cursor/skills/` (inside the repo) |
| Copilot | `.github/skills/` (inside the repo) |
| Copilot CLI | `~/.copilot/skills/` |
| Gemini | `.gemini/skills/` (inside the repo) |
| OpenCode | `.opencode/skills/` (inside the repo) |
| Windsurf | `.windsurf/skills/` (invoke with `@name`) |

Copies inside the repo are generated and never committed to git.

## Third-party skills (optional)

24 extra skills from other authors live in `vendors/`. They are opt-in:

```bash
python scripts/install.py --all --source vendors
python scripts/install.py --skill tdd --source vendors
```

## Verify it works

Ask your agent: `hello skills`. You should get a small table back.
If not: check the folder above exists and restart the agent.

## Common problems

- **Agent doesn't see new skills** → restart the agent session; skills load at startup.
- **Python errors** → check `python --version` (needs 3.10+) and run from the repo root.
- **"Unknown skill"** → list names with `python scripts/install.py --all --dry-run`.
- **Work without internet** → installing and all checks run fully offline.
