# ChatGPT / Codex — migration guide

> Review after Dec 2026 (dates below expire 11/12/2026).

> Archived from `.chatgpt/README.md`. There is no standard `.chatgpt/` folder read by ChatGPT.

## 2026 situation

- **Custom GPTs retiring**: no new GPTs from 25/09/2026, execution stops
  11/12/2026 for Enterprise (then Free/Plus/Pro). Migration to **Plugins**.
- **Codex** (CLI/IDE/app) reads `SKILL.md` from `.agents/skills/` — same format as this repo.
- **Codex Plugin** = distribution unit for reusable skills (+ app/MCP).

## How to use this repo's skills

```bash
# 1. Codex (recommended, same SKILL.md)
python scripts/install.py --all --agent codex
# copies to .agents/skills/<name>/ or ~/.agents/skills/

# 2. ChatGPT app: package as Plugin (skill + Codex config)
# inline example below; see .agents/skills/README.md for details
```

## Codex config example (inline, no agents/openai.yaml file in this repo)

```yaml
interface:
  display_name: "Smart Commit"
  short_description: "Conventional commits from git diff"
policy:
  allow_implicit_invocation: true
```

Docs: https://developers.openai.com/codex/skills
