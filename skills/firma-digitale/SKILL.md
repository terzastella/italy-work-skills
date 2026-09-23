---
name: firma-digitale
description: Explain digital signatures with types and issuance. Use when asked firma digitale, digital signature Italy, SPID firma.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[need]"
user-invocable: true
disable-model-invocation: false
---

# Firma Digitale

Sign digitally with the right tool: FEA vs qualified, devices, renewals.

## When to use

- "firma digitale", "digital signature Italy".
- Do not use for SPID access (see `spid-cie-guida`).

## Workflow

1. Need: PA filings (qualified), contracts (advanced may do), invoices PA (XAdES per specs).
2. Types: semplice vs avanzata (FEA) vs qualificata — value ladder explained.
3. Issuance: AgID-listed providers, ID verification, devices (token/smartcard/remote).
4. Validity/renewal cycles + what expires breaks (signed docs stay valid — explain).

## Rules

- Never handle anyone's signature credentials/OTPs.
- Provider names as categories (certificatori accreditati), no endorsements.
- Remote vs token trade-offs stated neutrally.

## Examples

See `examples/firma-cases.md`. Type ladder in `references/tipi.md`.

## Edge cases

- Expired mid-procedure → renewal timing + already-signed validity reassurance.
- Company signatory powers → visura/corporate proof note (see visura-leggimi).
- Foreigner needing Italian signature → SPID + provider paths, flag friction.
