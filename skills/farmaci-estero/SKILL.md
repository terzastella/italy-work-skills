---
name: farmaci-estero
description: Explain buying drugs abroad with limits. Use when asked farmaci estero, buy medicine abroad Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Farmaci all'Estero

Drugs across borders: personal quantities, prescriptions, bans.

## When to use

- "farmaci estero", "buy medicine abroad Italy".
- Do not use for medical advice or dosages.

## Workflow

1. Personal use quantities + prescription validity abroad (varies).
2. Controlled substances: strict bans + criminal edge flagged + referral.
3. Online pharmacies: EU-logo verification, no-name sites refused as advice.
4. Output: path map + limits + referral for edge cases.

## Rules

- No drug advice, admin paths only.
- Sketchy-site purchases: refused plainly with reasons.
- Quantities with the personal-use logic, never smuggling tolerance (limits year-stated).

## Examples

See `examples/farmaci-cases.md`. Limits in `references/limiti.md`.

## Edge cases

- Chronic therapy abroad long-term → local prescription transfer path.
- Customs stop → documents ready list + calm procedure.
- Veterinary drugs: separate track flagged, not mixed.
