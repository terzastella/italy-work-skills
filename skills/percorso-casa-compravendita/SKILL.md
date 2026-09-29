---
name: percorso-casa-compravendita
description: Guided home-buying path, offer to taxes. Use when asked comprare casa passo passo, buy home path Italy, mutuo to IMU.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Percorso: Casa Compravendita (Offer to Taxes)

Buy a home in order: budget, mortgage, deed, costs, running taxes.
Rules and figures verified for the year in course (year-stated everywhere).

## When to use

- Whole-journey home-buying requests ("voglio comprare casa, da dove parto?").
- Do not use for single questions (route to the specific skill instead).

## Workflow (tappe + handoff)

1. **Budget** (see `mutuo-tassi` + `xlsx-budget-it`): affordable instalment from income
   (script for the budget math). Handoff: budget ceiling.
2. **Purchase** (see `compravendita-casa`): proposta, preliminare (caparra confirmatoria
   vs penitenziale), rogito. Info-only on clauses, notary decides.
3. **Notary costs** (see `spese-notarili`): imposte + onorario estimate, first-home
   breaks (see `prima-casa-agevolazioni`) where due. Handoff: cost picture.
4. **IMU check** (see `imu-calcolo` + script): seconda casa or luxury? Run the math
   with comune rate (explicit input). Main home: exempt, stated.
5. **TARI + utilities** (see `tari-tassa`, `utenze-voltura`): running costs + meter moves.
   Close: notary + accountant check before signing anything.

## Rules

- No purchase verdicts ("buy/don't buy"): map + math only.
- Caparra types never confused: confirmatoria vs penitenziale stated plainly.
- Amounts with year; municipal rates explicit inputs, never memory.
- Rogito clauses are notary territory: info-only here.

## Examples

Two end-to-end runs in `examples/percorso-cases.md`. Stage detail in `references/tappe.md`.

## Edge cases

- Prima casa benefits lost on resale timing → flag early (see `prima-casa-agevolazioni`).
- Co-buyers with shares → split math per share first.
- Auction purchase (asta) → different track flagged + specialist referral.
