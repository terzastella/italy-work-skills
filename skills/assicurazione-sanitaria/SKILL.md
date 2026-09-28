---
name: assicurazione-sanitaria
description: Explain integrative health funds with deductibility. Use when asked assicurazione sanitaria, fondo sanitario, health fund Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Assicurazione Sanitaria Integrativa

Beyond SSN: health funds and policies decoded — coverage, costs, tax perks.

## When to use

- "assicurazione sanitaria", "fondo sanitario", "health fund Italy".
- Do not use for medical advice.

## Workflow

1. Types: fondi sanitari (contractual vs voluntary) vs polizze malattia/infortuni.
2. Coverage map (see `references/coperture.md`): visits, dental caps, hospitalization top-ups, check-ups.
3. Tax: contribution deductibility limits (year-stated) + payout treatment.
4. Output: needs-matched comparison points + questions for fund/insurer. No endorsements.

## Rules

- No product names as recommendations; comparison criteria only.
- Waiting periods (carenze) always checked — the classic trap.
- CCNL-linked funds: enrollment may be automatic, flag it.

## Examples

See `examples/sanitaria-cases.md`.

## Edge cases

- Pre-existing conditions → coverage questionnaire honesty + exclusion risks.
- Double coverage (fund + policy) → coordination rules, no double refunds assumed.
- Quitting job with fund → continuation/portability options flagged.
