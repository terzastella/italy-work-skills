---
name: cure-termali
description: Explain thermal cures with SSN tickets. Use when asked cure termali, thermal cures Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[need]"
user-invocable: true
disable-model-invocation: false
---

# Cure Termali

Thermal cures decoded: prescription, ticket, accredited centers.

## When to use

- "cure termali", "thermal cures Italy".
- Do not use for medical advice on efficacy.

## Workflow

1. Prescription: GP/specialist cycle prescription (pathologies list where due).
2. Ticket: yearly cycle coverage + ticket amount (year-stated) + exemptions apply.
3. Centers: accredited list logic (region), booking paths.
4. Output: steps + costs + booking.

## Rules

- No efficacy claims beyond procedure.
- Yearly cycle limits stated (one funded cycle typical, verify).
- Travel/stay costs: user's own, stated plainly.

## Examples

See `examples/termali-cases.md`. Cycle logic in `references/cicli.md`.

## Edge cases

- Exemption holders: ticket waived paths (see ticket-esenzioni).
- Outside region: mobility rules flagged.
- Private-only centers: full-price reality, no SSN illusions.
