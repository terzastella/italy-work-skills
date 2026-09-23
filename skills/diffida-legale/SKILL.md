---
name: diffida-legale
description: Structure formal warnings with tracked sending. Use when asked diffida, formal warning Italy, lettera di diffida.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Diffida (Formal Warning)

Warnings that count later: facts, request, deadline, tracked sending — no threats.

## When to use

- "diffida", "formal warning Italy", "lettera di diffida".
- Do not use for court filings (lawyer referral).

## Workflow

1. Structure: facts (dated) + legal basis named generally + request + reasonable deadline.
2. Sending: raccomandata A/R or PEC (see `pec-bozza`) — proof of content + delivery.
3. Tone: firm, factual, zero threats/insults (they backfire — stated).
4. Output: draft + sending checklist.

## Rules

- Never threats ("or else..."): requests + deadlines only.
- Facts only as provided; dates/amounts exact.
- Lawyer review recommended before sending in disputes.

## Examples

See `examples/diffida-cases.md`. Structure in `references/struttura.md`.

## Edge cases

- Ongoing negotiation → diffida may harden positions: timing advice, neutral.
- Counterparty unknown address → anagrafe/visura lookup paths first.
- Urgent harm continuing → faster instruments flagged + referral.
