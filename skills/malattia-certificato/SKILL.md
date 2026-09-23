---
name: malattia-certificato
description: Explain sick-leave certificates with visit windows. Use when asked malattia, certificato medico, sick leave Italy, reperibilità.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Malattia e Certificato

Sick leave done right: telematic certificate, availability windows, pay effects.

## When to use

- "malattia", "certificato medico", "sick leave Italy", "reperibilità".
- Do not use for medical advice or disputes.

## Workflow

1. Certificate: doctor sends telematically to INPS; worker informs employer promptly.
2. Reperibilità windows (current hours + year) + what happens on missed visit.
3. Pay: carenza rules overview + CCNL integrations vary — flag to check contract.
4. Close with INPS/contract verification note.

## Rules

- Hours and carenza with year; rules change — verify current.
- Public vs private differences flagged, not merged.
- No diagnosis handling: admin procedure only.

## Examples

See `examples/malattia-cases.md`. Windows table in `references/fasce.md`.

## Edge cases

- Hospitalization → different certificate flow, flag it.
- Abroad sickness → specific notification duties, referral.
- Repeated short leaves → control-visit likelihood + honest behavior note.
