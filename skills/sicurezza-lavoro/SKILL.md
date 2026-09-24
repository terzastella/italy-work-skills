---
name: sicurezza-lavoro
description: Map workplace safety duties with DVR and training. Use when asked sicurezza lavoro, DVR, RSPP Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[company]"
user-invocable: true
disable-model-invocation: false
---

# Sicurezza sul Lavoro (Map Only)

Safety duties mapped: DVR, RSPP, training, medical — consultant executes.

## When to use

- "sicurezza lavoro", "DVR", "RSPP Italy".
- Do not use for writing DVRs or risk assessments (RSPP referral, always).

## Workflow

1. Size/activity: duties scale (DVR always, with standard-procedure option for small firms).
2. Roles: datore/RSPP (internal/external), medico competente, RLS, addetti (antincendio/primo soccorso).
3. Training: general + specific hours + updates (year-stated), records kept.
4. Output: duty map + missing-items list + RSPP referral.

## Rules

- Never write risk assessments here: map + referral only.
- Sanctions exist and bite: stated generally, no scare tactics.
- Subcontracts: client duties (DUVRI) mentioned when relevant.

## Examples

See `examples/sicurezza-cases.md`. Duty map in `references/mappa.md`.

## Edge cases

- Zero employees (solo + occasional) → reduced duties, stated precisely.
- Smart workers at home → safety information duties flagged.
- Accident occurred → emergency + INAIL + lawyer now, no checklists first.
