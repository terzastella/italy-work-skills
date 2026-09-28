---
name: nota-spese
description: Build Italian expense reports with receipts and totals. Use when asked nota spese, expense report, rimborsi, trasferta.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[trip/period]"
user-invocable: true
disable-model-invocation: false
---

# Nota Spese

Expense reports that get reimbursed: every euro with receipt, totals checked.

## When to use

- "nota spese", "expense report", "rimborsi", "trasferta".
- Do not use for invoices issued (see `invoice-it`).

## Workflow

1. Ask: period/trip, expenses (date, kind, amount, receipt yes/no), company caps if any.
2. Table: Date | Kind | Amount | Receipt | Notes. Totals by kind + grand total.
3. Flag: missing receipts, over-cap items, foreign currency (no fantasy conversion).
4. Output report + "to fix" list for missing pieces.

## Rules

- No receipt → flagged, never silently accepted (policy decides, not you).
- Kilometric refunds: rate + km stated by user, math shown (ACI tables year-stated where used).
- Per-diem vs actual: follow stated company policy, ask if unknown.

## Examples

See `examples/nota-cases.md`. Categories in `references/categorie.md`.

## Edge cases

- Mixed personal/business → split lines, business only totaled.
- Cash without receipt → flagged `[no receipt]`, propose affidavit note per policy.
- Foreign currency → original + rate + date, converted total marked as such.
