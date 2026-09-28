---
name: assistenza-anziani
description: Map elder care from home help to RSA with benefits. Use when asked assistenza anziani, elder care Italy, RSA.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Assistenza Anziani

Elder care mapped: home help, ADI, RSA, cash benefits — information, patronato/ASL decide.

## When to use

- "assistenza anziani", "elder care Italy", "RSA".
- Do not use for medical advice.

## Workflow

1. Need level: home help (badante/ADI) vs residential (RSA/RSA aperta).
2. Money: accompagnamento (100% invalidity + need, via invalidità path) · regional contributions (year-stated).
3. Access: GP/ASL assessment + waiting lists reality (ranges, never promises).
4. Output: options map + first steps + patronato/ASL referral.

## Rules

- No medical content, admin paths only.
- Regional variance huge: region asked first, always.
- Caregiver burnout: respite options mentioned with humanity.

## Examples

See `examples/anziani-cases.md`. Options map in `references/mappa.md`.

## Edge cases

- Urgent discharge from hospital → dimissioni protette path, fast action.
- Dementia/Alzheimer: dedicated tracks flagged + associations mentioned.
- Family disagreements → mediation paths, no sides taken.
