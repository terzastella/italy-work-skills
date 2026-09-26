---
name: preventivo-it
description: Write Italian quotes with items, validity and terms. Use when asked preventivo, quote, quotazione, estimate Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[client/work]"
user-invocable: true
disable-model-invocation: false
---

# Preventivo (Italian Quote)

Quotes that get signed: itemized work, validity date, payment terms.

## When to use

- "preventivo", "quote", "quotazione", "estimate" (Italy).
- Do not use for invoices (see `invoice-it`).

## Workflow

1. Ask: client, work items (desc, qty, price), validity days (default 30), payment terms, VAT rate.
2. Structure: header → items table → total (+VAT note) → validity → terms → acceptance line.
3. Show totals math like `invoice-it`. Validity date computed, not vague ("a while").
4. Mark `BOZZA` until all data given.

## Rules

- Validity always dated (default 30 days from issue, year-stated on the document).
- Payment terms explicit (e.g. 30% upfront, balance on delivery) only as agreed/proposed.
- Never invent client data; `[TODO]` placeholders.
- Note: signed quote = contract-ish — suggest review for big amounts.

## Examples

See `examples/preventivo-cases.md`. Clauses in `references/clausole.md`.

## Edge cases

- Client asks discount → revised version numbered (v2), never edit v1 silently.
- Extra work mid-job → change-order draft, not free addition.
- PA quote → MEPA/CIG notes when relevant, flag them.
