---
name: abbonamenti-palestra
description: Explain gym contracts with withdrawal and freezes. Use when asked abbonamento palestra, gym contract Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[contract]"
user-invocable: true
disable-model-invocation: false
---

# Abbonamenti Palestra

Gym contracts decoded: tacit renewal, freezes, withdrawal that works.

## When to use

- "abbonamento palestra", "gym contract Italy".
- Do not use for distance contracts only (see `recesso-acquisti` for online).

## Workflow

1. Renewal: tacit-renewal clauses read first (the classic trap) + disdetta terms/notice.
2. Freeze (sospensione): injury/move paths with proof requirements.
3. Withdrawal: distance-signed = 14 days (see recesso-acquisti); in-gym = contract terms.
4. Output: situation check + letter draft points + deadlines.

## Rules

- Contract text decides: read it before advising anything.
- Unfair terms flagged generally + consumer association referral.
- No "stop paying and disappear" advice, ever.

## Examples

See `examples/palestra-cases.md`. Renewal logic in `references/rinnovi.md`.

## Edge cases

- Gym closed/moved → service-failure exit paths + chargeback angles.
- Medical stop → certificate + freeze path, stated as first move.
- Aggressive retention calls → written-only rule + evidence kept.
