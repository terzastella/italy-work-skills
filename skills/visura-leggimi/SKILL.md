---
name: visura-leggimi
description: Read Italian visura camerale sections and what they mean. Use when asked visura camerale, read visura, company check Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[visura data]"
user-invocable: true
disable-model-invocation: false
---

# Visura Leggimi

Chamber extracts decoded: what each section says about a company.

## When to use

- "visura camerale", "read visura", "company check Italy".
- Do not use for credit decisions (information reading only).

## Workflow

1. Take visura content (user-provided). Identify type: ordinaria vs storica.
2. Walk sections (see `references/sezioni.md`): anagrafica, attività/ATECO, cariche, soci/capitale, unità locali, procedure.
3. Flag: active procedures, recent changes, mismatches with what user was told.
4. Close with: source (registro imprese, date) + "for decisions, verify with professional".

## Rules

- Read only what is in the document: never enrich with web guesses as facts.
- Dates matter: visura snapshot date always stated.
- Red flags described neutrally (procedure = fact, not accusation).

## Examples

See `examples/visura-cases.md`.

## Edge cases

- Historical visura → timeline of changes, focus on recent 2 years.
- Foreign company → Italian visura may not exist; point to home-country registers.
- Mismatch with invoice data → list differences, suggest verification before paying.
