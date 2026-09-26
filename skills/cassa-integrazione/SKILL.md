---
name: cassa-integrazione
description: Explain wage guarantee funds with worker pay effects. Use when asked cassa integrazione, CIG, furlough Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Cassa Integrazione (CIG)

Furlough decoded: ordinary/extraordinary, what workers get, who files.

## When to use

- "cassa integrazione", "CIG", "furlough Italy".
- Do not use for dismissals (see `licenziamento-info`).

## Workflow

1. Type: ordinaria (temporary crisis) · straordinaria (restructuring) · deroga/fondi (residual) — year-stated.
2. Worker side: % of pay (caps, year-stated), who advances (employer vs direct INPS), timing.
3. Employer side: application + union procedure overview (no DIY on complex cases).
4. Output: situation map + pay math + union/consultant referral.

## Rules

- Caps and % with year; never timeless figures.
- Deroga/fondi rules move: verify current.
- No "you will get X" promises: company filing decides.

## Examples

See `examples/cassa-cases.md`. Types in `references/tipi.md`.

## Edge cases

- Part-time CIG → proportional math flagged.
- CIG + second job → compatibility rules + referral.
- End of CIG → rientro vs mobilità paths listed.
