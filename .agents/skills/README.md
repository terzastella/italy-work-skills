# .agents/skills — Codex / Cursor / Copilot / Gemini standard

This folder is the **universal standard** read by Codex CLI/IDE, Cursor,
Copilot and other https://agentskills.io-compatible agents.

## Usage

Real skills live in `../../skills/`. Do not duplicate them here by hand, use the script:

```bash
python ../../scripts/install.py --all --agent codex
python ../../scripts/install.py --skill invoice-it --agent codex
```

The script copies `skills/<name>/` to:
- current repo: `.agents/skills/<name>/`
- or user level: `~/.agents/skills/<name>/`

## Codex: invocation + openai.yaml

Codex activates skills in 2 ways:
- explicit: `/skills` or `$skill-name`
- implicit: when the `description` matches the task

For reusable distribution (2+ skills or skill+app), package as a Codex Plugin.
Inline `openai.yaml` example for UI and policy (no such file in this repo):

```yaml
interface:
  display_name: "Smart Commit"
  short_description: "Conventional commits from git diff"
policy:
  allow_implicit_invocation: true
dependencies:
  tools: []
```

See https://developers.openai.com/codex/skills
