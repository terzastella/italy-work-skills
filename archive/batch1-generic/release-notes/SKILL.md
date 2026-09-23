---
name: release-notes
description: Write narrative release notes from changelog and diff for GitHub releases. Use when asked release notes, version announcement.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Bash
argument-hint: "<version>"
user-invocable: true
disable-model-invocation: false
---

# Release Notes

Human-readable release notes: what changes for the user, how to upgrade, what breaks.

## When to use

- "release notes", "version announcement", "github release".
- Do not use for technical CHANGELOG entries (see `changelog-gen`).

## Workflow

1. Read the version's CHANGELOG entry + `git diff --stat` of the range.
2. Fixed structure: Title → In short (3 points) → New → Fixes → Breaking → Upgrade.
3. Max 40 lines.
4. Show finished text, do not publish releases without confirmation.

## Output format

```markdown
# 0.3.0 — 20 new skills

In short: automatic changelog, IT code review, Excel budgets.

## New
- ...

## Fixes
- ...

## Breaking
- None. / or list with migration.

## Upgrade
`python scripts/install.py --all`
```

## Rules

- User language, not commits: "Excel budgets with formulas" not "feat(xlsx)".
- Breaking section always present, even if it says "None".
- Never promise future dates or features not in the diff.

## Examples

See `examples/release-cases.md`.

## Edge cases

- Version without changes → advise against releasing, propose accumulating.
- Real breaking change → highlight on top + migration command, never bury it.
