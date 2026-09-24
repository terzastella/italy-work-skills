---
name: carta-identita-cie
description: Guide CIE issuance with costs and validity. Use when asked carta identità, CIE, ID card Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[case]"
user-invocable: true
disable-model-invocation: false
---

# Carta Identità / CIE

ID cards without second trips: booking, costs, validity, minors.

## When to use

- "carta identità", "CIE", "ID card Italy".
- Do not use for passports (see `passaporto-procedura`).

## Workflow

1. First issue vs renewal vs replacement (lost/stolen/damaged) vs minors.
2. Booking: comune agenda + photo specs + fees (year-stated).
3. Validity by age band (year-stated) + expiry-on-birthday rule explained.
4. Output checklist + pickup timing note.

## Rules

- Fees/validity with year; amounts move.
- Paper ID still valid until expiry: no panic renewals needed.
- Minors: parental presence/consent rules stated.

## Examples

See `examples/cie-cases.md`. Validity table in `references/validita.md`.

## Edge cases

- Lost abroad → consulate + denuncia track, flag timelines.
- Urgent travel with expired CIE → passport path may be faster (see passaporto-procedura).
- AIRE members → consulate issuance, longer waits flagged.
