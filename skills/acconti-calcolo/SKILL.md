---
name: acconti-calcolo
description: Compute Italian advance payments with historic method. Use when asked acconto imposte, advance payment, how acconti work Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[prior year tax]"
user-invocable: true
disable-model-invocation: false
---

# Acconti (Advance Payments)

Saldo + acconti without surprises: historic method, thresholds, previsional option.

## When to use

- "acconto imposte", "advance payment", "how acconti work", "quanto acconto pago?".
- Do not use for deadline calendar (see `scadenze-fiscali`).
- Do not use for the final balance math of a regime (see `regime-forfettario`, `irpef-scaglioni`).

## Workflow

1. Take prior-year due tax from the return (e.g. LM42 line for forfettari). Cite the line.
2. Threshold: above 52€ (verify year) → advance due; at/below → none.
3. Split: the instalment split is an explicit input, never assumed — IRPEF-style
   instalments vs single sostitutiva advance differ and rules changed in the past.
   Check AdE for the year, state the split, then compute.
4. Run the math (preferred, reproducible):
   `python skills/acconti-calcolo/scripts/acconti.py --imposta 5820 --split 100 --year 2026`
5. Previsional alternative only if income really drops: show both, flag penalties
   for underpayment, never recommend blindly.
6. Close with payment dates pointer (see `scadenze-fiscali`) + accountant check.

## Rules

- Numbers only from user data or return lines cited.
- The script refuses splits that don't sum to 100: that error is a feature.
- Thresholds with year. Forfettario vs ordinary kept distinct.
- First year (no history) → usually no advance, explain why.
- Mixed incomes → advances per tax type, do not merge.

## Scripts

- `scripts/acconti.py` — storico/previsionale math with explicit split.
  Fixtures with expected outputs in `examples/fixtures/`. Run:
  `python skills/acconti-calcolo/scripts/acconti.py --help`

## Examples

Good and bad cases in `examples/acconti-cases.md`. Method table in `references/metodo.md`.

## Edge cases

- First year (no history) → usually no advance, explain why.
- Sharp income drop → previsional path + risk note + professional referral.
- Mixed incomes → advances per tax type, do not merge.
- Overpaid advance → compensation paths flagged (see `compensazioni-f24`), not computed here.
