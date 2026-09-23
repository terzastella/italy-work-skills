---
name: commit-scope
description: Suggest the conventional-commit scope by analyzing touched files. Use when asked which scope, commit scope, conventional scope.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Bash
argument-hint: ""
user-invocable: true
disable-model-invocation: false
---

# Commit Scope

One scope only, the right one: from diff to the lowercase word in parentheses.

## When to use

- "which scope", "commit scope", "conventional scope".
- Do not use for the whole message (see `smart-commit`).

## Workflow

1. Run `git diff --stat` (staged or not, declare which).
2. Map paths → scope with rules in `references/scope-map.md`.
3. Propose 1 scope + 1 alternative. Max 1 word, lowercase.
4. If mixed areas, scope = dominant area or no scope (explain why).

## Rules

- Scope = folder/module/function, never a sentence.
- If >3 areas touched → no scope + suggest splitting the commit.
- Consistency with previous commits: check `git log --oneline -10` for used scopes.

## Examples

See `examples/scope-cases.md`.

## Edge cases

- Empty diff → no scope, "nothing to commit".
- New module → scope = new module name, flag it as new.
- Repo without convention → propose scope anyway + note "first repo scope".
