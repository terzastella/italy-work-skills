---
name: pronto-soccorso-ticket
description: Explain ER codes and copay with exemptions. Use when asked pronto soccorso ticket, ER copay Italy, codice bianco.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Pronto Soccorso Ticket

ER triage decoded: color codes, when the ticket applies, who is exempt.

## When to use

- "pronto soccorso ticket", "ER copay Italy", "codice bianco".
- Do not use for medical advice — emergencies call 112/118 first, stated.

## Workflow

1. Codes: red/yellow/green/white logic (urgency, not arrival order).
2. Ticket: white-code non-urgent cases pay (amount year-stated); exemptions apply (see `ticket-esenzioni`).
3. Follow-ups from ER (visits ordered there): ticket rules stated.
4. Output: code map + ticket logic + exemption check.

## Rules

- Emergencies first: 112/118 stated before anything else.
- Amounts with year; regions vary — verify local.
- No diagnosis, ever.

## Examples

See `examples/ps-cases.md`. Code map in `references/codici.md`.

## Edge cases

- Left without being seen → ticket may still apply, stated plainly.
- GP-referred access → different track flagged.
- Tourist ER access → EHIC/payment notes, no one turned away in emergency.
