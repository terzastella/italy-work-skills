---
name: patronato-servizi
description: Map free patronato help with when to go. Use when asked patronato, free help Italy, CAF patronato.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[need]"
user-invocable: true
disable-model-invocation: false
---

# Patronato Servizi

Free help, mapped: what patronati do free, when to go, what to bring.

## When to use

- "patronato", "free help Italy", "CAF patronato".
- Do not use for legal advice (they route, this skill maps).

## Workflow

1. Need → service: pensions, NASpI/DIS-COLL, invalidità, ISEE, assegno unico, maternity.
2. Free vs paid line: patronato core services are free — state it (scam-proofing).
3. Documents per service + booking paths (offices fill fast).
4. Output: service map + documents + nearest-office logic (no addresses invented).

## Rules

- "Free" stressed against fake-consultant scams.
- Never invent office addresses/hours: official finders linked.
- CAF vs patronato distinction explained (tax vs welfare).

## Examples

See `examples/patronato-cases.md`. Service map in `references/servizi.md`.

## Edge cases

- Urgent deadline → walk-in vs booking reality stated + fastest path.
- Language barriers → multilingual desks flagged where known, no promises.
- Fake patronati scams → verification tips (official lists only).
