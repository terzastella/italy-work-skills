---
name: bonus-casa
description: Explain Italian home bonuses with requirements and papers. Use when asked bonus casa, ristrutturazione detrazione, ecobonus, bonus mobili.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[works planned]"
user-invocable: true
disable-model-invocation: false
---

# Bonus Casa

Home bonuses without traps: rates, caps, papers, talking-fiscal-credit rules.

## When to use

- "bonus casa", "ristrutturazione detrazione", "ecobonus", "bonus mobili", "superbonus".
- Do not use for tax filing (information + papers only).

## Workflow

1. Classify works: ordinary renovation vs energy vs furniture vs seismic.
2. Per class: current rate + cap + years (with YEAR — rates change; verify AdE guide).
3. Papers: bonifico parlante, fatture, asseverazioni/comunicazioni where due.
4. Output: eligible path + papers checklist + professional referral (tecnico/commercialista).

## Rules

- Rates always with year ("50% 2026" style): rules move every budget law.
- Bonifico parlante details exact (causale, codes): the classic killer.
- Superbonus legacy: explain current state briefly, no nostalgia planning.

## Examples

See `examples/bonus-cases.md`. Rate table in `references/aliquote.md`.

## Edge cases

- Works already done without papers → recovery options honest assessment, no miracles.
- Cessione credito/sconto: current availability check, rules tightened over years.
- Condominium works → assembly + millesimi + administrator path flagged.
