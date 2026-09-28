---
name: imposta-bollo
description: Explain stamp duty with thresholds and virtual payment. Use when asked imposta di bollo, marca da bollo, stamp duty Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write Bash
argument-hint: "[document]"
user-invocable: true
disable-model-invocation: false
---

# Imposta di Bollo

Stamp duty decoded: €2 over threshold, virtual vs physical, who pays.

## When to use

- "imposta di bollo", "marca da bollo", "stamp duty Italy".
- Do not use for e-invoice specifics (see `fattura-elettronica-it`).

## Workflow

1. Rule with the bundled script (preferred, reproducible): €2 on invoices/receipts over threshold
   without VAT (threshold and amount are explicit year-stated inputs) — who affixes/pays:
   `python skills/imposta-bollo/scripts/bollo.py --importo 500 --soglia 77.47 --bollo 2 --year 2026`
2. E-invoices: virtual bollo via SdI flow (quarterly payment path).
3. Bank statements/investment docs: periodic duty notes (year-stated).
4. Output: duty check + payment path.

## Rules

- Threshold + amount with year; they move rarely but verify.
- Occasional receipts (see collaborazioni-occasionali): bollo line included.
- Never advise skipping: €2 omissions compound, stated plainly.

## Scripts

- `scripts/bollo.py` — threshold check (threshold and amount are inputs).
  Fixtures with expected outputs in `examples/fixtures/`. Omissions compound.

## Examples

See `examples/bollo-cases.md`. Threshold table in `references/soglie.md`.

## Edge cases

- Exempt subjects (ONLUS/ETS where due) → flag + verify case.
- Lost marca on paper → re-buy + attach, annulment rules noted.
- Foreign docs used in Italy → bollo upon use cases flagged.
