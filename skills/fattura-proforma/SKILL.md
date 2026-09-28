---
name: fattura-proforma
description: Explain proforma invoices with no tax value. Use when asked fattura proforma, proforma invoice Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Fattura Proforma

Quotes that look like invoices, without tax value: uses and limits.

## When to use

- "fattura proforma", "proforma invoice Italy".
- Do not use for real invoicing (see `fattura-elettronica-it`, `invoice-it`).

## Workflow

1. Uses: quotes, customs values, advance agreements — never tax documents.
2. Marking: "PROFORMA — no valore fiscale" stated on face.
3. Conversion: proforma → real invoice flow when deal closes.
4. Output: draft points + conversion checklist.

## Rules

- Never present proforma as invoice toPA/banks: fraud-adjacent, refused plainly.
- Numbering separate from invoices (no sequence mixing).
- Foreign trade: proforma + packing interplay noted briefly (customs rules year-stated).

## Examples

See `examples/proforma-cases.md`. Uses in `references/usi.md`.

## Edge cases

- Client insists on "fattura proforma via SdI" → impossible by design, explained.
- Proforma paid: convert to invoice now, stated as urgent.
- Public tenders: proforma never valid as invoice, flag + referral.
