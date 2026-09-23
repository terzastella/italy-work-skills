---
name: skill-starter
description: TEMPLATE - replace with what the skill does and when to use it. Use when <trigger>.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Gemini
metadata: {author: your-name, version: "0.1", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[file or argument]"
user-invocable: true
disable-model-invocation: false
---

# Skill Name

Short intro: what it does in 2 lines.

## When to use

- Case 1: ...
- Case 2: ...

Do not use when: ...

## Workflow

1. Read input and context (files, diff, repo).
2. Apply the rules below.
3. Show output in the required format.
4. Ask for confirmation before destructive actions.

## Rules

- Rule 1, concrete and verifiable.
- Rule 2 with good/bad example.

## Examples

### Input
```text
example input
```

### Expected output
```text
example output
```

## Edge cases

- Missing file -> explain what is missing, do not invent.
- Dirty repo / huge diff -> summarize first, then detail.

## References

See `references/` for extended checklists, `scripts/` for automation,
`assets/` for templates. Keep this file under 500 lines,
move details to `references/`.
