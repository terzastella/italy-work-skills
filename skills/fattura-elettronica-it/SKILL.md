---
name: fattura-elettronica-it
description: Guide Italian e-invoices via SdI with mandatory data and rejections. Use when asked fattura elettronica, SDI invoice, XML invoice, scarto SDI.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[invoice data]"
user-invocable: true
disable-model-invocation: false
---

# Italian E-Invoicing (Fattura Elettronica)

E-invoices via SdI that pass controls: mandatory data, recipient codes, rejections handled.

## When to use

- "fattura elettronica", "SDI invoice", "XML invoice", "scarto SDI".
- Do not use for generic invoices (see `invoice-it`) or tax advice.

## Workflow

1. Collect: seller (denominazione, VAT ID), buyer (VAT ID or tax code), items, rates.
   See `references/dati-obbligatori.md` for the mandatory list (art. 21 DPR 633/72).
2. Recipient code: 7-char SdI code, `0000000` + certified email for consumers, PA code from IPA index.
3. Draft the readable invoice + XML field map (header/transmission, seller, buyer, body).
   Never forge signatures or transmit to SdI: drafting aid only.
4. Rejections: read the SdI receipt code, map to fix in `references/scarti.md`, redraft.

## Rules

- Fattura XML only via SdI since 1/1/2019 (B2B/B2C); simplified invoice only ≤100€ total.
- Buyer section: VAT ID or tax code as communicated (SdI accepts both, per AdE FAQ).
- Never invent VAT IDs, codes, or receipt numbers.
- Informational draft only: verify with accountant before transmitting.

## Examples

See `examples/fattura-cases.md`. Official sources in `references/fonti.md`.

## Edge cases

- Foreign currency: line amounts in Euro, total may be foreign (SdI does not check total).
- PA invoices: follow DM 55/2013 rules + CIG/CUP when required.
- Rejected file: fix and resend within 5 days of the rejection receipt (verify current rule).
