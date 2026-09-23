---
name: json-clean
description: Validate and fix JSON with line-by-line error report. Use when asked invalid JSON, format JSON, fix JSON, validate JSON.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[file.json]"
user-invocable: true
disable-model-invocation: false
---

# JSON Clean

Broken JSON → valid JSON, with every fix declared.

## When to use

- "invalid JSON", "format JSON", "fix JSON", "validate JSON", "parsing error".
- Do not use for designing schemas from scratch (fix + validate only).

## Workflow

1. Validate and locate: first error with line and reason (`python -m json.tool` or equivalent).
2. Mechanical fixes only: trailing commas, single quotes, comments, BOM.
3. Never "fix" values or structure: dubious data → flag, do not invent.
4. Output: valid JSON + fix report (format below). Original untouched by default.

## Report format

```text
File: <name> | Errors: <n> | Status: VALID
Fixes: line 12 trailing comma removed; line 30 single→double quotes
Doubts: <list or "none"> | Output: <file>
```

## Rules

- One mechanical fix at a time, re-verify after each.
- Never change types (string→number) without confirmation.
- Large files (>1MB) → streaming/sample validation, declare coverage.

## Examples

See `examples/json-cases.md`. Common errors in `references/errors.md`.

## Edge cases

- JSONL/JSON5/YAML mistaken → convert format declaring it, not fake JSON.
- Duplicate keys → flag (last wins in parsing), ask which to keep.
- Broken encoding → like `csv-clean`: compare UTF-8/Latin-1, ask.
