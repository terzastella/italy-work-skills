---
name: spese-notarili
description: Read notary quotes with taxes vs fees split. Use when asked spese notarili, notary costs Italy, preventivo notaio.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[quote/deed]"
user-invocable: true
disable-model-invocation: false
---

# Spese Notarili

Notary quotes decoded: taxes (pass-through) vs fee (negotiable-ish) vs costs.

## When to use

- "spese notarili", "notary costs Italy", "preventivo notaio".
- Do not use for choosing the notary (comparison criteria only, no endorsements).

## Workflow

1. Split the quote: imposte (registro/ipotecarie/catastali by case) + onorario + spese vive.
2. Explain: taxes go to State (fixed by tables), fee is the real comparison number.
3. Prima-casa vs ordinary vs donation vs company: which tax set applies.
4. Output: quote reading + comparable fee extraction + questions for notaries.

## Rules

- Tax tables year-stated; never compute exact taxes as verdict.
- Fee negotiability stated plainly (ask 2-3 preventivi).
- No notary endorsement, ever.

## Examples

See `examples/notarili-cases.md`. Split logic in `references/scomposizione.md`.

## Edge cases

- Suspiciously low fee → what is excluded (visure? trascrizione?) asked.
- Donation/succession deeds → different tax sets, routed correctly.
- Mortgage deed bundled → two deeds, two cost blocks, separated.
