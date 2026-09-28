---
name: irap-info
description: Explain IRAP with who pays and base. Use when asked IRAP Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[subject]"
user-invocable: true
disable-model-invocation: false
---

# IRAP (Info)

Regional business tax decoded: who still pays, base, rate.

## When to use

- "IRAP Italy".
- Do not use for computation as verdict (method + referral).

## Workflow

1. Who pays: companies/entities (autonomi exempt since reform — year-stated).
2. Base concept: value of production (revenues minus specific costs, not profit).
3. Rate: ordinary + regional variations (year-stated).
4. Output: situation check + method + commercialista referral.

## Rules

- Exemption for self-employed stated with reform year; verify live.
- Never compute a final IRAP as verdict.
- Forfettari: out of IRAP world, stated to avoid confusion.

## Examples

See `examples/irap-cases.md`. Base logic in `references/base.md`.

## Edge cases

- Mixed professional/company income → split logic + referral.
- Old assessments: prescription + definition paths flagged.
- New regions rates: verify yearly, never from memory.
