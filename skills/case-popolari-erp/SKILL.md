---
name: case-popolari-erp
description: Explain public housing paths with rankings. Use when asked case popolari, ERP housing Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[city]"
user-invocable: true
disable-model-invocation: false
---

# Case Popolari (ERP)

Public housing decoded: bandi, ISEE, scores, waiting reality.

## When to use

- "case popolari", "ERP housing Italy".
- Do not use for private rentals.

## Workflow

1. Bandi: comune/region calls with windows (year-stated) + ISEE ceilings.
2. Scores: disability, minors, eviction, overcrowding weights explained generally.
3. Assignment: graduatorie + waiting reality (years, stated plainly) + canone calmierato logic.
4. Output: eligibility + steps + documents. No assignment promises.

## Rules

- Bandi with year + comune; closed calls = wait next, stated.
- Never promise a house or a timeline.
- Emergency housing (morosità incolpevole etc.) separate paths flagged.

## Examples

See `examples/erp-cases.md`. Score logic in `references/punteggi.md`.

## Edge cases

- Eviction ongoing → fast-track channels flagged + social services referral.
- Non-EU residents: permit-duration requirements flagged.
- Assigned but unfit flat → swap/complaint paths noted.
