---
name: changelog-gen
description: Generate CHANGELOG entries from commit lists in Keep-a-Changelog format. Use when asked changelog, version entry, release notes from commits.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Bash
argument-hint: "<version>"
user-invocable: true
disable-model-invocation: false
---

# Changelog Gen

Turns a commit list into a sectioned CHANGELOG entry.

## When to use

- "changelog", "version entry", "notes from commits", "keep a changelog".
- Do not use for narrative release notes (see `release-notes`).

## Workflow

1. Get commits: `git log <previous-tag>..HEAD --oneline` or user-provided list.
2. Classify each commit: Added, Changed, Fixed, Removed, Security. Ignore pure `chore` unless user-facing.
3. Output a paste-ready entry (format below).
4. Do not write to CHANGELOG without confirmation: show the entry first.

## Output format

```markdown
## [0.3.0] - 2026-09-23

### Added
- `json-clean` skill with validation and auto-fix

### Fixed
- Installer also copies `assets/` subfolders
```

## Rules

- One line per user-visible change. No internal commits (`wip`, `fix typo` merged).
- Versions `MAJOR.MINOR.PATCH`, date `YYYY-MM-DD`.
- Never invent existing version numbers: check CHANGELOG head first.

## Examples

See `examples/changelog-cases.md`. Section reference in `references/sections.md`.

## Edge cases

- No commits in range → "No changes between <a> and <b>." stop.
- Only `wip`/test commits → entry with `Other` section only + commit-quality warning.
- No CHANGELOG exists → propose creating a minimal one, do not create it alone.
