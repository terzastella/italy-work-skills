---
name: condominio-spese
description: Read condo statements with millesimi and disputes. Use when asked condominio, spese condominiali, millesimi, assemblea.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[statement]"
user-invocable: true
disable-model-invocation: false
---

# Condominio Spese

Condo money decoded: rendiconto, millesimi, riparti, what to contest and how.

## When to use

- "condominio", "spese condominiali", "millesimi", "assemblea".
- Do not use for legal disputes (lawyer referral).

## Workflow

1. Take rendiconto + millesimi table + delibera challenged (if any).
2. Check: totals vs riparti math, millesimi applied correctly, innovazioni vs manutenzione split,
   morosità handling, fondo cassa.
3. Output: verified math + anomalies + contest path (assemblea impugnazione terms, mediator).
4. Close with administrator questions list.

## Rules

- Math recomputed from given figures only.
- Impugnazione terms stated with year; missed terms = say so plainly.
- No legality verdicts on delibere: anomalies + professional referral.

## Examples

See `examples/condominio-cases.md`. Reading keys in `references/chiavi.md`.

## Edge cases

- Supercondominio/complex structures → separate tables per building, flag it.
- Amministratore unresponsive → registered-letter draft + revoca assembly path.
- Affittuario vs proprietario → who pays what split (spese ordinarie/straordinarie).
