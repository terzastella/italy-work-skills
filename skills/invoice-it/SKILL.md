---
name: invoice-it
description: Prepare Italian invoices with items, VAT and verified totals. Use when asked invoice, bill, quote with totals, fee note.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[client]"
user-invocable: true
disable-model-invocation: false
---

# Italian Invoice

Correct Italian invoices: headers, items, VAT per rate, double-checked totals.

## When to use

- "invoice", "bill", "quote with totals", "fee note" (Italian format).
- Do not use for tax advice (document only).

## Workflow

1. Collect: issuer (name, VAT ID), client, number, date, items (desc, qty, price), VAT rates.
2. Compute: taxable per item → VAT per rate → total. Recompute twice (show the math).
3. Output: document + verification table. Format below.
4. Always mark `DRAFT — verify with accountant` if tax data is incomplete.

## Verification format

```text
Item 1: <desc> — <q> x €<p> = €<tot>
Taxable: €<x> | VAT 22%: €<y> | VAT 10%: €<z> | TOTAL: €<t>
Missing data: <list or "none">
```

## Rules

- Never invent VAT IDs, tax codes, existing invoice numbers: only given data.
- Totals always recomputed and shown, never just the final figure.
- Disclaimer: not tax advice, draft document only.

## Examples

See `examples/invoice-cases.md`. Common rates in `references/vat.md`.

## Edge cases

- Flat-rate scheme → no VAT, correct wording, ask scheme confirmation.
- Foreign currency → total in currency + note, no invented conversion.
- Missing client data → draft with `[TODO]`, no realistic fake names.
