---
name: fattura-elettronica-it
description: Guide Italian e-invoices via SdI with mandatory data and rejections. Use when asked fattura elettronica, SDI invoice, XML invoice, scarto SDI.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.6", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[invoice data]"
user-invocable: true
disable-model-invocation: false
---

# Italian E-Invoicing (Fattura Elettronica)

E-invoices via SdI that pass controls: mandatory data, recipient codes, rejections handled.
Flagship skill: field map, code routing, rejection clinic — drafting aid only, never transmission.

## When to use

- "fattura elettronica", "SDI invoice", "XML invoice", "scarto SDI".
- Do not use for generic invoices (see `invoice-it`) or tax advice.

## Workflow (tappe with formal in/out)

### Tappa 1 — Parties + items

Input: seller (denominazione, VAT ID), buyer (VAT ID or tax code), items, rates.
Output: completeness check against `references/dati-obbligatori.md`
(art. 21 DPR 633/72). Missing buyer ID → `[TODO]`, never invented.

### Tappa 2 — Recipient routing

7-char SdI code · `0000000` + certified email for consumers ·
PA code from IPA index (see `fattura-pa` for CIG/CUP).
Wrong-channel rejections start here: route first, draft second.

### Tappa 3 — Draft + field map

Readable invoice + XML field map (header/transmission, seller, buyer, body).
Totals verified with `invoice-it` math (see `totals.py` pattern).
Never forge signatures or transmit to SdI: drafting aid only, stated every time.

### Tappa 4 — Rejection clinic

Read the SdI receipt code → map to fix in `references/scarti.md` → redraft.
Fix-and-resend window year-stated (verify current rule, e.g. 5 days).

## Multi-turn protocol

Turn 1 (parties): seller + buyer + code routing. Turn 2 (draft): readable +
field map with totals. Turn 3 (rejection, if any): code → fix → redraft.
Transmission is never a turn: accountant + certified channel only.

## Rules

- Fattura XML only via SdI since 1/1/2019 (B2B/B2C); simplified invoice only ≤100€ total.
- Buyer section: VAT ID or tax code as communicated (SdI accepts both, per AdE FAQ).
- Never invent VAT IDs, codes, or receipt numbers.
- Informational draft only: verify with accountant before transmitting.
- Forfettari: no VAT lines, bollo line where due (see `imposta-bollo`).

## Examples

Good and bad cases in `examples/fattura-cases.md`. Mandatory data in
`references/dati-obbligatori.md`. Rejection map in `references/scarti.md`.
Official sources in `references/fonti.md`. Recipient routing in `references/recapiti.md`.

## Edge cases (priority order)

| # | Case | Action |
|---|---|---|
| 1 | Rejected file | code → fix → redraft within window (verify current rule) |
| 2 | Foreign currency | line amounts in Euro, total may be foreign (SdI does not check total) |
| 3 | PA invoices | DM 55/2013 + CIG/CUP (see `fattura-pa`), never improvised |
| 4 | Forfettario issuer | no VAT, bollo line, exemption statement |
| 5 | Consumer buyer | `0000000` + PEC path, explained |
