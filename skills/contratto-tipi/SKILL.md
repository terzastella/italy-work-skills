---
name: contratto-tipi
description: Compare Italian work contract types without legal advice. Use when asked contratto tipi, co.co.co vs subordinato, P.IVA vs dipendente.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write
argument-hint: "[offer]"
user-invocable: true
disable-model-invocation: false
---

# Contratto Tipi (Info Only)

Subordinato vs co.co.co vs P.IVA: what changes in protections, pay, risk — no legal verdicts.

## When to use

- "contratto tipi", "co.co.co vs subordinato", "P.IVA vs dipendente".
- Do not use for signing decisions or disputes (professional referral).

## Workflow

1. Take the offer facts (hours, direction, pay, duration).
2. Compare dimensions: subordination signs, protections (malattia/ferie/TFR/NASpI),
   contributions, notice, exit.
3. Flag mismatch patterns (false autonomous) descriptively + referral.
4. Output comparison + questions to ask before signing.

## Rules

- Bogus self-employment: describe legal test factors, never declare fraud.
- No "sign/don't sign" verdicts: information + questions + referral.
- CCNL-specific numbers only with source. Thresholds year-stated where cited (see `regime-forfettario` 85k/100k gates).

## Examples

See `examples/contratti-cases.md`. Dimensions in `references/dimensioni.md`.

## Edge cases

- Co.co.co offered for employee-like role → mismatch list + union referral.
- P.IVA imposed by employer → forfettario exclusion risk (see regime-forfettario).
- Fixed-term chains → renewal limits flagged generally, CCNL specifics referred.
