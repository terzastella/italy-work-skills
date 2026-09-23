---
name: trasferta-estero
description: Guide business trips abroad with per-diem and papers. Use when asked trasferta estero, business travel abroad Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[trip]"
user-invocable: true
disable-model-invocation: false
---

# Trasferta Estero

Work trips abroad covered: per-diem vs receipts, documents, insurance.

## When to use

- "trasferta estero", "business travel abroad Italy".
- Do not use for national trips (see `nota-spese`).

## Workflow

1. Regime: diaria forfettaria vs piè di lista (company policy decides, ask).
2. Documents: passport validity, visas, EHIC/private insurance, A1 social-security form for EU.
3. Currency: official-rate conversions with date, receipts kept originals.
4. Output: checklist + cost table + insurance verification.

## Rules

- A1 form for EU postings flagged early (classic miss).
- Insurance never assumed: verify coverage before flying.
- Per-diem tax treatment overview, no personal tax verdicts.

## Examples

See `examples/trasferta-cases.md`. Documents in `references/documenti.md`.

## Edge cases

- Long postings (distacco) → different regime entirely, referral.
- High-risk countries → Farnesina check + company duty of care.
- Mixed business/personal days → split accounting, stated plainly.
