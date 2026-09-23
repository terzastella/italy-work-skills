---
name: git-status-express
description: Explain in 10 lines what is happening in the repo from git status and diff. Use when asked repo status, what did I change, change summary.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Bash
argument-hint: ""
user-invocable: true
disable-model-invocation: false
---

# Git Status Express

A readable snapshot of the repo in 10 seconds: what changed, where, how big.

## When to use

- "repo status", "what did I change", "change summary", "where am I".
- Do not use for committing (see `smart-commit`) or changelog (see `changelog-gen`).

## Workflow

1. Run `git status --short` and `git diff --stat`. If not a git repo, say so and stop.
2. Group by area: code, docs, config, tests, other.
3. Output in fixed format (below), max 15 lines.
4. Close with 1 line "Suggested next step" (commit, test, docs) — one suggestion only.

## Output format

```text
Repo: <name> | Branch: <branch> | Clean/Dirty
Staged: <n> files | Unstaged: <n> files | Untracked: <n> files
Areas touched: <area1> (<n> files), <area2> (<n> files)
Main files: <3 max, with +lines/-lines>
Next step: <one suggestion>
```

## Rules

- Never more than 15 lines. No full `git diff` dumps.
- Binary/large files flagged `[large]`, not analyzed in detail.
- Never run `checkout`, `reset`, `clean` or other destructive commands.

## Examples

See `examples/status-cases.md`.

## Edge cases

- Clean repo → "Clean repo on <branch>, nothing to do." (2 lines, stop).
- Not a git repo → explain `git init` in 1 line, stop.
- Thousands of files (e.g. accidentally committed `node_modules`) → flag likely cause (missing `.gitignore`), do not list.
