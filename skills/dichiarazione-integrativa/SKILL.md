---
name: dichiarazione-integrativa
description: Fix filed returns with integrativa paths. Use when asked dichiarazione integrativa, amend return Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[return/error]"
user-invocable: true
disable-model-invocation: false
---

# Dichiarazione Integrativa

Fix filed returns: in-favor vs against-you, terms, penalties.

## When to use

- "dichiarazione integrativa", "amend return Italy".
- Do not use for first filing.

## Workflow

1. Direction: a favore (claim back: deadlines + refund path) vs sfavore (pay + ravvedimento link, see `ravvedimento-operoso`).
2. Terms per direction (year-stated) + which model/year to amend.
3. Documents: original + corrected figures side by side.
4. Output: path + terms + referral for big amounts.

## Rules

- Terms with year; late = different track, stated plainly.
- Never hide income "hoping": correction beats discovery, stated.
- Avviso bonario received: special definition may beat integrativa — compare.

## Examples

See `examples/integrativa-cases.md`. Term table in `references/termini.md`.

## Edge cases

- Audit already open on those years → integrativa barred, referral now.
- 730 integrativa: CAF/professional path noted.
- Multiple years wrong → year-by-year, oldest first logic explained.
