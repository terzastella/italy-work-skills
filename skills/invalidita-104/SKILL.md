---
name: invalidita-104
description: Explain disability benefits with commission path. Use when asked invalidità, legge 104, disability benefits Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Invalidità e 104 (Info Only, Delicate)

Disability paths mapped: percentages, 104 permits, commission — information, patronato decides.

## When to use

- "invalidità", "legge 104", "disability benefits Italy".
- NEVER for medical assessments or appeals strategy (patronato/lawyer referral).

## Workflow

1. Distinguish: invalidità civile (%) vs handicap L.104 (art.3 c.1 vs c.3) vs accompagnamento.
2. Path: medical certificate → INPS application → commission visit → verbale.
3. 104 permits: 3 days/month (c.3), who can use them, rules overview.
4. Output: path map + documents + patronato referral. No percentage predictions.

## Rules

- Delicate skill: every answer ends with patronato referral.
- Never predict percentages or outcomes.
- Work-capacity notes handled with extra care in tone.

## Examples

See `examples/invalidita-cases.md`. Benefit map in `references/prestazioni.md`.

## Edge cases

- Rejected application → appeal terms + patronato/lawyer now, no DIY.
- Worsening condition → aggravamento path mentioned.
- Caregiver asking → their permits/rights section, not just the disabled person's.
