---
name: passaporto-procedura
description: Guide Italian passport requests with agenda and costs. Use when asked passaporto, passport Italy, questura appointment.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[case]"
user-invocable: true
disable-model-invocation: false
---

# Passaporto Procedura

Passport without second trips: agenda prenota, documents, fees, pickup.

## When to use

- "passaporto", "passport Italy", "questura appointment".
- Do not use for visas (destination-country matter).

## Workflow

1. Agenda: prenota via Polizia di Stato portal (SPID/CIE) + available slots reality note.
2. Documents: ID, photos (ICAO specs), old passport, payment receipts (bollettino + marca, year-stated).
3. Fees with year; minors: both parents consent + rules.
4. Output checklist + timeline estimate + pickup/delivery options.

## Rules

- Fees/photos specs with year; amounts move.
- Minors: consent rules stated carefully + referral for conflicts.
- Never promise timelines: questure vary wildly — ranges + status tracking.

## Examples

See `examples/passaporto-cases.md`. Documents in `references/documenti.md`.

## Edge cases

- Urgent travel → emergency title paths (questura evaluates), no guarantees.
- Lost/stolen → denuncia first, then procedure.
- AIRE abroad → consulate track, longer timelines flagged.
