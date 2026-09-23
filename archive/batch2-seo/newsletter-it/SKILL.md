---
name: newsletter-it
description: Write newsletters with fixed structure and CTA. Use when asked newsletter, list email.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[theme/issue]"
user-invocable: true
disable-model-invocation: false
---

# Newsletter

Newsletters that get opened: subject, 3 blocks, 1 CTA.

## When to use

- "newsletter", "list email".
- Do not use for 1-to-1 emails (see `email-formale-it`).

## Workflow

1. Ask: issue theme, 2-3 contents, main CTA, list tone.
2. Structure: Subject ×2 options → 3-line intro → Block1/2/3 (title+4 lines+link) → CTA → Sign+PS.
3. Max 300 body words. Links with UTM placeholder if tracking needed.
4. Paste-ready output + alternative subjects.

## Rules

- 1 main CTA, rest secondary links.
- Subject ≤50 chars, no full caps, no "FREE!!!".
- PS with repeated CTA link (many read only the PS).
- Privacy: no visible addresses, BCC/list, unsubscribe note.

## Examples

See `examples/newsletter-cases.md`. Layout in `references/layout.md`.

## Edge cases

- Cold list → sober subject, no promises, 1-line intro of yourself.
- Too many contents → max 3 blocks, rest "next issue".
- Commercial blast → declare nature + visible unsubscribe.
