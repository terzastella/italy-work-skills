---
name: anagrafe-certificati
description: Get Italian registry certificates via ANPR online. Use when asked certificato anagrafe, ANPR, stato famiglia, residenza certificate.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[certificate]"
user-invocable: true
disable-model-invocation: false
---

# Anagrafe Certificati (ANPR)

Certificates in minutes, not queues: ANPR online with SPID/CIE.

## When to use

- "certificato anagrafe", "ANPR", "stato famiglia", "residenza certificate".
- Do not use for legalizations/apostille (different track, flag it).

## Workflow

1. Identify certificate: residenza, stato famiglia, nascita, matrimonio, esistenza in vita.
2. Route: ANPR online (SPID/CIE, free, immediate) vs counter (when online fails).
3. Autocertificazione note: PA and public-service managers MUST accept self-declarations
   instead of certificates (DPR 445/2000) — say it first, saves the trip.
4. Output: steps + link + autocertificazione template pointer when applicable.

## Rules

- Autocertificazione-first: many requests do not need certificates at all.
- Never handle anyone's SPID/CIE credentials.
- Marca da bollo cases flagged (€16 where due) with year check.

## Examples

See `examples/anagrafe-cases.md`. Certificate map in `references/mappa.md`.

## Edge cases

- AIRE registered abroad → consulate/ANPR paths, flag differences.
- Urgent + portal down → counter fallback + autocertificazione interim.
- Legalization for abroad → apostille/prefettura track, referral.
