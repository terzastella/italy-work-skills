---
name: vacanze-pacchetto
description: Explain package travel rights with assistance and refunds. Use when asked vacanza pacchetto, package travel Italy, tour operator.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[trip/issue]"
user-invocable: true
disable-model-invocation: false
---

# Vacanze Pacchetto

Package holidays protected: organizer duties, assistance, price and refund rules.

## When to use

- "vacanza pacchetto", "package travel Italy", "tour operator".
- Do not use for flight-only issues (see `voli-ritardi`).

## Workflow

1. Confirm package (2+ combined services, single contract) vs separate bookings (different rules!).
2. Rights map: pre-trip info, price changes (8% threshold logic), assistance during, alternatives/refund on failure.
3. Complaint: prompt notice on site + written follow-up + evidence (photos, receipts).
4. Output: rights summary + complaint draft + evidence list.

## Rules

- Package vs DIY first: most "no-right" answers come from wrong classification.
- Price increases capped with passenger exit right — state the mechanism.
- Insolvency: guarantee fund mention + referral, no panic (fund rules year-stated).

## Examples

See `examples/vacanze-cases.md`. Rights map in `references/diritti.md`.

## Edge cases

- Linked bookings (click-through) → package-like protections may apply, flag nuance.
- Force majeure at destination → assistance duties remain, refund logic differs.
- Minors/fragile travelers → assistance priority noted.
