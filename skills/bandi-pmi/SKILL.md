---
name: bandi-pmi
description: Read Italian calls for SMEs with go/no-go checklist. Use when asked bandi, contributi, agevolazioni, fondi PMI.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[call text/link]"
user-invocable: true
disable-model-invocation: false
---

# Bandi PMI

Calls read like contracts: eligibility, fundable costs, deadlines, scores — then go/no-go.

## When to use

- "bandi", "contributi", "agevolazioni", "fondi PMI", "call for proposals Italy".
- Do not use for writing the application (see `domanda-bando`).

## Workflow

1. Extract: who is eligible (ATECO, size, region), fundable vs excluded costs,
   aid intensity (%), deadlines, evaluation criteria weights.
2. Go/no-go table: 5 checks (eligible? costs fit? deadline feasible? score realistic? paperwork load?).
3. Output: verdict + what to prepare first + official link + call closing date.
4. Never promise winning: scores and funds are competitive.

## Rules

- Every fact with call article/page number cited.
- Deadlines year-stated (date + time + timezone); "check for extensions" note.
- De minimis cumulation flagged when relevant (ask accountant).
- Expired calls → say expired + find the replacement edition.

## Examples

See `examples/bandi-cases.md`. Reading grid in `references/griglia.md`.

## Edge cases

- Vague call text → list ambiguities + where to ask (info desk, FAQ of the call).
- Regional + national overlap → compare both, pick one (cumulation rules).
- Last-days rush → advise against rushed filings, list minimum viable dossier.
