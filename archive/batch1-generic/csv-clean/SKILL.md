---
name: csv-clean
description: Clean CSVs with a report of everything fixed. Use when asked clean CSV, messy CSV, fix CSV, CSV encoding.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[file.csv]"
user-invocable: true
disable-model-invocation: false
---

# CSV Clean

Messy CSV into clean table, with a report of every fix.

## When to use

- "clean CSV", "messy CSV", "fix CSV", "CSV encoding", "CSV duplicates".
- Do not use for data analysis (cleaning only).

## Workflow

1. Inspect: rows, columns, separator, encoding, header.
2. Fixes in order: encoding → separator → header → whitespace → types → duplicates → empty rows.
3. Show report (format below) + first 5 rows preview. Never overwrite the original without confirmation: default new file `<name>.clean.csv`.

## Report format

```text
File: <name> | Rows: <n> → <m> | Columns: <n>
Encoding: <detected> → UTF-8
Header: <ok / fixed: ...>
Removed: <n> duplicates, <n> empty rows
Trimmed: <n> cells | Types: <e.g. price column → number>
Output: <file> (original untouched)
```

## Rules

- Never delete columns without explicit confirmation.
- Never "fix" ambiguous values: flag row and ask (e.g. dates `01/02/03`).
- Implicit backup: original untouched by default.

## Examples

See `examples/csv-cases.md`. Check list in `references/checks.md`.

## Edge cases

- Ambiguous separator → show 3 raw rows, ask.
- Broken encoding (mojibake) → try UTF-8/Latin-1, show comparison, ask.
- Millions of rows → work on samples + script, not all in chat.
