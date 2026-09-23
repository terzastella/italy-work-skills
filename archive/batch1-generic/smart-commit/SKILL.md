---
name: smart-commit
description: Create conventional commits in English from git diff with pre-commit checklist. Use when asked for commit, commit message, conventional commits, changelog.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Bash
argument-hint: ""
user-invocable: true
disable-model-invocation: false
---

# Smart Commit

Generates conventional commit messages from `git diff --staged` (or `git diff` if nothing staged).

## When to use

- "make the commit", "commit message", "conventional commit", "changelog".
- Do not use for push, rebase, merge — message + checklist only.

## Workflow

1. Run `git status --short` and `git diff --stat` to gauge scope.
2. If nothing staged, use non-staged `git diff` and say so explicitly.
3. If diff > ~200 lines, summarize per file before proposing a message.
4. Propose ONE main message + 2 alternatives. Format:
   `<type>(<scope>): <description>` — max 72 chars on first line.
5. Allowed types: see `references/conventional-types.md` (`feat, fix, docs, refactor, test, chore, build, ci`).
6. Show pre-commit checklist (large files, secrets, TODO). Never commit alone, ask for confirmation.
7. Run or suggest `python skills/smart-commit/scripts/check-diff.py` before proposing.
8. Worked examples: see `examples/diff-cases.md`.

## Rules

- Imperative description, lowercase, no trailing period. English.
- One scope only, lowercase: e.g. `feat(auth): add refresh token rotation`.
- Never include secrets/keys in the message.
- Never `git commit` / `git push` without explicit confirmation.

## Examples

Good:
```text
feat(auth): add refresh token rotation
fix(ui): fix table overflow on mobile
docs(readme): add skills compatibility matrix
```

Bad:
```text
Fix bug. (vague, capital, period)
update stuff (no type, vague)
feat(Auth): Added big stuff. (capitals, past tense, period)
```

## Edge cases

- Empty diff -> "nothing to commit, `git status` clean".
- Binary/large files (>1MB) -> flag, suggest Git LFS or exclusion.
- Possible secrets (see script) -> block proposal, show file:suspicious line.
