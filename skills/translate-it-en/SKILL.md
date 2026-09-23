---
name: translate-it-en
description: Translate IT-EN texts preserving structure, code and tone. Use when asked translate, English version, Italian version.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[file] [--to en|it]"
user-invocable: true
disable-model-invocation: false
---

# Translate IT-EN

Faithful translations: same structure, same tone, code untouched.

## When to use

- "translate", "English/Italian version", "localize text".
- Do not use for restyling (see `doc-polish-it`).

## Workflow

1. Direction: default IT→EN if text is Italian, EN→IT if English. `--to` forces.
2. Translate prose only: code blocks, paths, technical names, commands stay unchanged.
3. Identical structure: same headings, lists, tables, lines.
4. Close with `Notes: <ambiguous terms + choice made>` (max 3).

## Rules

- Faithfulness > elegance: no additions, no cuts.
- Standard tech terms unchanged (`commit`, `pull request`, `build`).
- Quotes and markdown formatting preserved.
- Never translate secrets/tokens/URLs.

## Examples

See `examples/translate-cases.md`. Tech glossary in `references/glossary.md`.

## Edge cases

- Mixed IT/EN text → translate only source-language parts, flag the rest.
- Puns/idioms → translation + note in parentheses.
- Whole file → frontmatter and file names unchanged.
