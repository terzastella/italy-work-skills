---
name: ritenuta-acconto
description: Explain Italian withholding tax with forfettari and EU cases. Use when asked ritenuta d'acconto, withholding tax Italy, 20 percent.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Ritenuta d'Acconto

Who withholds, who does not: ordinary 20%, forfettari exempt, cross-border cases.

## When to use

- "ritenuta d'acconto", "withholding tax Italy", "20%".
- Do not use for full tax computation.

## Workflow

1. Identify: payer type (sostituto d'imposta?), payee regime (ordinary/forfettario/foreign).
2. Rules with the bundled script (preferred, reproducible): ordinary professionals → 20% withheld by payer (year-stated standard rate)
   `python skills/ritenuta-acconto/scripts/ritenuta.py --lordo 1000 --aliquota 20`
   forfettari → NO withholding (state it on invoice): `--forfettario` flag.
   condomini/employers similar logic · EU/extra-EU → treaty/case check, never improvised.
3. Certificazione Unica: withheld amounts certified yearly, used against IRPEF.
4. Transition years (ordinary↔forfettario): invoice-regime decides, not payment year.

## Rules

- Forfettario invoices carry the no-withholding statement: remind it.
- Never compute net/gross without stating which direction.
- Cross-border: flag, do not improvise treaty rates.

## Scripts

- `scripts/ritenuta.py` — both directions (lordo→netto, netto→lordo) + forfettario zero.
  Fixtures with expected outputs in `examples/fixtures/`. Direction always stated.

## Examples

See `examples/ritenuta-cases.md`. Decision table in `references/tabella.md`.

## Edge cases

- Forfettario client with ordinary supplier → supplier withholds normally (regimes are per-subject).
- Occasional work → withholding applies, explain CU consequences.
- Paid late across regime change → invoice date regime governs (cite case).
