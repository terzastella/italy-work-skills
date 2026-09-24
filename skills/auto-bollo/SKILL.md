---
name: auto-bollo
description: Explain car tax by region with deadlines and exemptions. Use when asked bollo auto, car tax Italy, superbollo.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[vehicle/region]"
user-invocable: true
disable-model-invocation: false
---

# Bollo Auto

Car tax without fines: regional amount, deadlines, exemptions.

## When to use

- "bollo auto", "car tax Italy", "superbollo".
- Do not use for fines already issued (payment paths only).

## Workflow

1. Ask: region of residence, vehicle (kW, Euro class, age), first registration vs renewal.
2. Amount: regional tariff on kW + superbollo over threshold (year-stated) + exemptions (historic/disabled/EV where due).
3. Deadlines: month-after-expiry rule + regional calendars; ravvedimento if late.
4. Output: amount math + pay-by date + pay channels (ACI/online/banks).

## Rules

- Region always: amounts and deadlines are regional.
- Superbollo threshold with year; EV/historic exemptions flagged, never assumed.
- Missed years: prescription overview brief + pay-what-is-due guidance, professional flag if messy.

## Examples

See `examples/bollo-cases.md`. Regional notes in `references/regioni.md`.

## Edge cases

- Sold/scrapped car → radiazione/PRA timing decides who pays; flag the gap months.
- Company car fringe use → different track mention, referral.
- Moved regions → new-region rules from move date, verify.
