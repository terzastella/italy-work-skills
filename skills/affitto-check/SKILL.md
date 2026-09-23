---
name: affitto-check
description: Read Italian rental contracts with red flags and costs. Use when asked affitto, rental contract Italy, canone, caparra.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[contract data]"
user-invocable: true
disable-model-invocation: false
---

# Affitto Check

Rental contracts read before signing: type, costs, red flags — information, not legal advice.

## When to use

- "affitto", "rental contract Italy", "canone", "caparra", "cedolare".
- Do not use for disputes (lawyer referral).

## Workflow

1. Identify contract type: 4+4, 3+2 (concordato), transitorio, studenti, breve.
2. Checklist (see `references/checklist.md`): deposit (max 3 months), registration duty split,
   cedolare vs IRPEF note, spese split, recesso terms.
3. Red flags: cash-only rent, no registration, deposit >3 months, blank fields.
4. Output: verdict (ok / negotiate X / walk away + why) + questions for the landlord.

## Rules

- Never declare a contract "legal/illegal": flags + professional referral.
- Registration (AdE, 30 days) always mentioned with duty split.
- Amounts/dates only as provided.

## Examples

See `examples/affitto-cases.md`.

## Edge cases

- Unregistered proposal → explain risks plainly, suggest registration.
- Cedolare secca choice → landlord-side note, tenant impact stated.
- Student/short contracts → duration rules + renewal specifics flagged.
