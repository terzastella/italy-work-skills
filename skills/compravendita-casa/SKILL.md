---
name: compravendita-casa
description: Guide home buying from proposal to deed with costs. Use when asked comprare casa, rogito, notaio costs Italy, proposta acquisto.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[stage]"
user-invocable: true
disable-model-invocation: false
---

# Compravendita Casa

Buy a home in order: proposal, preliminare, checks, rogito — costs at every step.

## When to use

- "comprare casa", "rogito", "notaio costs", "proposta acquisto".
- Do not use for legal advice (notary referral for the deed).

## Workflow

1. Stage: proposal (proposta, caparra confirmatoria vs penitenziale) → preliminare (compromesso, registration) → urban checks → rogito.
2. Checks list (see `references/verifiche.md`): planimetria/catasto match, abusi, ipoteche, APE.
3. Costs: agency %, notaio (imposta registro vs IVA by case), cadastre/mortgage taxes — ranges with year.
4. Output: stage map + checks status + cost estimate + questions for notaio/agent.

## Rules

- Caparra confirmatoria vs penitenziale difference stated (money consequences differ).
- Never skip urban/catasto conformity: the classic disaster.
- Prima casa benefits noted with conditions (residenza timing), verify current year rules (year-stated).

## Examples

See `examples/casa-cases.md`.

## Edge cases

- Abuso edilizio found → stop-or-sanatoria paths, technician referral, no minimization.
- Auction purchase (asta) → different track entirely, flag + specialist referral.
- New build vs used → garanzie + fideiussione notes for new builds.
