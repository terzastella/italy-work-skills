---
name: camera-commercio
description: Guide registro imprese filings with documents checklist. Use when asked camera di commercio, registro imprese, visura filing Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[filing]"
user-invocable: true
disable-model-invocation: false
---

# Camera di Commercio Practices

Registro imprese filings without rejections: which pratica, which documents, which fees.

## When to use

- "camera di commercio", "registro imprese", "ComUnica filing", "iscrivere impresa".
- Do not use for reading a visura (see `visura-leggimi`).

## Workflow

1. Identify pratica: iscrizione, variazione (sede, attività, cariche), cancellazione, deposito bilanci.
2. Documents + fees + channel (ComUnica/Starweb, digital signature required).
3. Timelines: statutory terms + what late filing costs.
4. Output checklist + "file via" pointer + professional referral for complex cases.

## Rules

- Digital signature mandatory for filings: stated upfront.
- Fees with year; chambers vary slightly — verify local CCIAA.
- Bilanci deposit: deadlines + sanctions for late filing flagged.

## Examples

See `examples/camera-cases.md`. Pratiche map in `references/pratiche.md`.

## Edge cases

- Artigiani/albi → albo registration first, then registro.
- Foreign companies (branch) → separate track, referral.
- Rejected pratica → read the motivo, fix once, resubmit (no stubborn loops).
