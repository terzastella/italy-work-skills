---
name: farmaci-equivalenti
description: Explain generic drugs with substitution rules. Use when asked farmaci equivalenti, generic drugs Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[medicine]"
user-invocable: true
disable-model-invocation: false
---

# Farmaci Equivalenti

Generics decoded: same active ingredient, when substitution applies, ticket links.

## When to use

- "farmaci equivalenti", "generic drugs Italy".
- Do not use for medical advice (pharmacist/doctor decide).

## Workflow

1. Equivalence: same active ingredient + dose + form (transparency lists).
2. Substitution: pharmacist may/must dispense equivalent unless doctor forbids (non sostituibilità note).
3. Ticket link: reference price vs paid difference (see spese-mediche-detrazioni for papers).
4. Output: situation check + questions for doctor/pharmacist.

## Rules

- No drug recommendations, ever.
- Lists with year; products change — verify live.
- Doctor's non-substitution respected, never bypassed.

## Examples

See `examples/equivalenti-cases.md`. Equivalence in `references/equivalenza.md`.

## Edge cases

- Narrow-therapeutic-index drugs: substitution caution flagged + doctor decides.
- Shortages: equivalent switch paths via pharmacist, no DIY changes.
- Pediatric/elderly formulations: pharmacist guidance, not agent advice.
