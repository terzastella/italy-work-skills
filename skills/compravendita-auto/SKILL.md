---
name: compravendita-auto
description: Guide car sales with PRA transfer and checks. Use when asked comprare auto usata, passaggio auto, car sale Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[deal]"
user-invocable: true
disable-model-invocation: false
---

# Compravendita Auto

Used-car deals without surprises: checks, PRA transfer, costs.

## When to use

- "comprare auto usata", "passaggio auto", "car sale Italy".
- Do not use for new-car dealer warranties (different track).

## Workflow

1. Checks before money: visura PRA (fermo amministrativo, ipoteche), revisione validity,
   km coherence, tagliandi.
2. Transfer: atto + PRA registration (60 days), IPT + fees (province-based, year-stated).
3. Payment: traced means only (no big cash), passaggio contestuale.
4. Output: checks status + cost math + appointment checklist.

## Rules

- Fermo amministrativo check is mandatory, never skipped.
- IPT varies by province/kW: ranges + year, verify current.
- Never pay before checks: order is fixed (checks → atto → pay → PRA).

## Examples

See `examples/auto-cases.md`. Check list in `references/checklist.md`.

## Edge cases

- Seller with reservation (riserva di proprietà) → flag + notary/ACI guidance.
- Foreign plates → re-registration path, referral.
- Inherited car → heir transfer track with documents.
