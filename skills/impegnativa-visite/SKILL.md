---
name: impegnativa-visite
description: Guide specialist referrals with priority classes. Use when asked impegnativa, specialist referral Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[need]"
user-invocable: true
disable-model-invocation: false
---

# Impegnativa Visite

Referrals decoded: priority classes RA/B/D/P, booking, ticket links.

## When to use

- "impegnativa", "specialist referral Italy".
- Do not use for medical advice.

## Workflow

1. Priority class on referral (U/B/D/P + days, year-stated) decides the wait.
2. Booking: CUP regional paths (see `sanita-digitale`) + recall lists.
3. Ticket link (see `ticket-esenzioni`): exemptions checked before paying.
4. Output: class reading + booking steps + ticket check.

## Rules

- Classes with year; regions implement differently — verify local CUP.
- GP writes the class: wrong class = wrong wait, ask GP to fix.
- No diagnosis, admin navigation only.

## Examples

See `examples/impegnativa-cases.md`. Classes in `references/classi.md`.

## Edge cases

- Expired referral → validity windows vary, re-issue path.
- Intramoenia fast track → costs vs wait trade-off explained neutrally.
- Urgent symptoms → ER first (see pronto-soccorso-ticket), never wait for booking.
