---
name: readability-fix
description: Simplify hard texts without losing meaning. Use when asked simplify text, readability, too hard text.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[file]"
user-invocable: true
disable-model-invocation: false
---

# Readability Fix

Hard → clear: short sentences, common words, same information.

## When to use

- "simplify text", "readability", "too hard/technical", "plain language".
- Do not use for translations (see `translate-it-en`) or marketing style.

## Workflow

1. Measure: sentences >25 words, subordinate clauses, bureaucratese, passives (list in output).
2. Rewrite: 1 idea per sentence, active verbs, common terms (glossary for unavoidable technical ones).
3. Output: rewritten text + "before→after" table on 3 worst sentences + what you did NOT touch (data, names).

## Rules

- Meaning unchanged: if ambiguous, ask instead of interpreting.
- Necessary legal/medical terms → keep + parenthetical explanation.
- No dumbing down: simple, not silly.
- Data, dates, names always identical.

## Examples

See `examples/readability-cases.md`. Bureaucratese list in `references/plain.md`.

## Edge cases

- Legal text that must stay as-is → simple version ALONGSIDE, never replacing.
- Poetry/literature → politely decline (style is substance).
- Unknown acronyms → expand on first use or ask.
