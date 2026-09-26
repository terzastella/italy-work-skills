---
name: pec-bozza
description: Draft Italian certified emails with legal-value notes. Use when asked PEC draft, certified email, posta certificata, legal email Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[recipient/purpose]"
user-invocable: true
disable-model-invocation: false
---

# PEC Drafts

Certified emails done right: draft + receipts explained, legal value preserved.

## When to use

- "PEC draft", "certified email", "posta certificata", "legal email Italy".
- Do not use for normal email (see `email-formale-it`).

## Workflow

1. Ask: recipient PEC address, purpose, deadline, attachments.
2. Draft in Italian (formal `Lei`) + English notes around it explaining choices.
3. Attach the receipt checklist (see `references/ricevute.md`): acceptance + delivery receipts to keep.
4. Never send anything: output is a draft + send instructions.

## Rules

- Legal value comes from PEC-to-PEC + both receipts: say it every time.
- Ordinary email to PEC has no certified value: flag it if asked.
- Attachments listed with names; deadlines in bold.
- Never invent PEC addresses.

## Examples

See `examples/pec-cases.md`.

## Edge cases

- No PEC mailbox of sender → explain they need one first (AgID-listed providers).
- Urgent + no receipts yet → send + keep polling receipt mailbox, note the gap.
- Dispute coming → suggest lawyer before sending, draft stays neutral and factual.
