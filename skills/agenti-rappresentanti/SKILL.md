---
name: agenti-rappresentanti
description: Explain sales agents with Enasarco and FIRR. Use when asked agente rappresentante, Enasarco Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Agenti e Rappresentanti

Sales agents decoded: Enasarco, provvigioni, FIRR exit money.

## When to use

- "agente rappresentante", "Enasarco Italy".
- Do not use for generic VAT opening (see `partita-iva-apri`).

## Workflow

1. Contract: monomandatario vs plurimandatario, written terms that matter (zone, exclusivity, provvigioni %).
2. Enasarco: dual contributions (agent + firm shares, year-stated) + pension track.
3. Exit: FIRR accrual (yearly set-aside) + notice/indennità at termination.
4. Output: situation check + questions for the mandante + association referral.

## Rules

- Provvigioni math on user figures only.
- False-agency (subordinato mascherato) patterns flagged + referral.
- Forfettario fit for agents: noted with gates (see regime-forfettario).

## Examples

See `examples/agenti-cases.md`. Money map in `references/soldi.md`.

## Edge cases

- Foreign mandante → applicable law/INPS questions flagged + referral.
- Non-payment of provvigioni → written claims + termini, referral early.
- Pluri vs mono switch → contribution/FIRR effects explained generally.
