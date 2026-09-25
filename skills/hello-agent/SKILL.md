---
name: hello-agent
description: 10-second smoke test to verify the agent sees and loads skills. Use when asked to test skills, hello, verify installation.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read
argument-hint: ""
user-invocable: true
disable-model-invocation: false
---

# Hello Agent

Verifies in 10 seconds that skills are visible to the current agent.

## When to use

- User asks "test skills", "hello", "do skills work?".
- After `scripts/install.py` to confirm installation.

## Workflow

1. Do not read other files, no context needed.
2. Reply with the table below filled for the current environment.
3. If you do not know the skill path in use, write `unknown` — do not invent.

## Required output

```markdown
| Item | Value |
|------|-------|
| Agent | <Claude Code / Codex / Grok / Cursor / Copilot / other> |
| Active skill | hello-agent 0.1 |
| Skill path | <path you were loaded from, or unknown> |
| Status | OK |
```

Then one line: `Next test: try /invoice-it or /doc-polish-it`.

## Output per agent (same format, different paths)

| Agent | Expected path |
|-------|---------------|
| Claude Code | `~/.claude/skills/hello-agent/` or `.claude/skills/hello-agent/` |
| Codex | `.agents/skills/hello-agent/` or `~/.agents/skills/hello-agent/` |
| Grok | `~/.grok/skills/hello-agent/` (also reads `.claude/` and `.agents/skills/`) |
| Cursor | `.cursor/skills/hello-agent/` |
| Copilot | `.github/skills/hello-agent/` |
| Gemini | `.gemini/skills/hello-agent/` |

If the path matches none above, write `unknown` plus the real path.

## Example

User: `hello skills`
Reply: table above with Agent=Claude Code, Status=OK.

## Edge cases

- If invoked implicitly without explicit request, still reply briefly (max 10 lines).
