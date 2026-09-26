---
name: impresa-familiare
description: Explain family businesses with coadiuvanti rules. Use when asked impresa familiare, family business Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Impresa Familiare

Family firms decoded: coadiuvanti shares, contributions, exit splits.

## When to use

- "impresa familiare", "family business Italy".
- Do not use for SRLs with family shareholders (different track).

## Workflow

1. Setup: titolare + familiari coadiuvanti (degrees listed by law) with written act.
2. Money: profit shares (49% cap to family, year-stated logic) + INPS positions each.
3. Exit/death: share liquidation rules + succession interplay (see successioni-info).
4. Output: setup map + shares math + professional referral.

## Rules

- Shares math on user figures only.
- Fake coadiuvanti (ghost workers) flagged as fraud risk, plainly.
- Azienda coniugale confusion: distinguished, not mixed.

## Examples

See `examples/familiare-cases.md`. Share logic in `references/quote.md`.

## Edge cases

- Divorce with family firm → share/division complexity flagged + lawyer now.
- Minor coadiuvante → special rules + protections noted.
- No written act → proof problems later, fix now.
