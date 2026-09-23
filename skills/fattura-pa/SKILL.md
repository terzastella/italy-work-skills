---
name: fattura-pa
description: Guide B2G invoices to Italian public bodies with CIG/CUP. Use when asked fattura PA, B2G invoice, CIG CUP, invoice public administration Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[contract data]"
user-invocable: true
disable-model-invocation: false
---

# Fattura PA (B2G)

Invoices the PA accepts first try: IPA code, CIG/CUP, split payment.

## When to use

- "fattura PA", "B2G invoice", "CIG/CUP", "invoice to comune/ministry".
- Do not use for B2B (see `fattura-elettronica-it`).

## Workflow

1. Identify: administration (IPA code from indicepa.gov.it), contract (CIG, CUP when works).
2. Draft with PA blocks: IPA recipient, CIG/CUP fields, split payment (scissione dei pagamenti) note.
3. Signature note: qualified signature required for PA (XAdES enveloped per specs).
4. Verify-then-transmit rule: draft here, transmit via certified channel only.

## Rules

- DM 55/2013 rules apply on top of standard e-invoicing.
- Split payment: PA pays VAT directly — show net/total split correctly.
- Never invent IPA codes, CIG, CUP: look up or `[TODO]`.

## Examples

See `examples/fattura-pa-cases.md`. PA fields in `references/campi-pa.md`.

## Edge cases

- Missing CIG (excluded contracts) → state exclusion reason, do not fake a code.
- Rejected by PA system → read notification, fix field, resend (see scarti logic).
- MEPA orders → order reference attached to invoice data.
