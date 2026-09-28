---
name: sanita-digitale
description: Guide FSE, IO app and health bookings in Italy. Use when asked fascicolo sanitario, IO app, CUP booking, tessera sanitaria.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write
argument-hint: "[need]"
user-invocable: true
disable-model-invocation: false
---

# Sanità Digitale

Health services online: FSE records, IO app, CUP bookings, card status.

## When to use

- "fascicolo sanitario", "IO app", "CUP booking", "tessera sanitaria".
- Do not use for medical advice (admin paths only).

## Workflow

1. Identify need: records access (FSE, regional), booking (CUP online/phone), card (expiry/replacement), IO app services.
2. Access path per need: SPID/CIE required level + where (region portal vs national).
3. Regional variance note: health is regional — always name the region.
4. Close with office fallback (ASL counter) when digital fails.

## Rules

- Never handle health data content: admin navigation only.
- Region always asked first: Lombardy versus Sicily procedures (portals year-stated).
- No medical interpretation of records, ever.

## Examples

See `examples/sanita-cases.md`. Access map in `references/accessi.md`.

## Edge cases

- Expired health card → replacement path + temporary coverage note.
- Minors/elderly → delegation paths.
- Urgent care → 112/118 first, never app guidance for emergencies.
