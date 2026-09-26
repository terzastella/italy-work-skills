---
name: scadenze-fiscali
description: Read Italian tax deadlines and build payment calendars. Use when asked scadenze fiscali, versamenti, acconto saldo, tax deadlines Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[year/profile]"
user-invocable: true
disable-model-invocation: false
---

# Scadenze Fiscali

Tax deadlines read correctly: balance vs advance, extensions, and the golden rule — always re-check AdE.

## When to use

- "scadenze fiscali", "versamenti", "acconto/saldo", "when to pay taxes Italy".
- Do not use for computing amounts owed (method + calendar only).
  Splits: see `acconti-calcolo`; regime math: see `regime-forfettario` — this skill dates them.

## Workflow

1. Ask: profile (forfettario/ordinary/employee), year, what is due (income tax, advance, VAT).
2. Explain the mechanism first: saldo (prior year) + acconti (current year), historic method.
3. Build calendar table with each deadline + what + note (extensions like DL 89/2026 happen).
4. Close with: dates move yearly — verify on agenziaentrate.gov.it before paying.

## Rules

- Never state a deadline without year. Never invent extensions.
- Distinguish statutory deadline vs announced extension, with source + date.
- Forfettario specifics: imposta sostitutiva saldo + 50% first advance (historic method, LM42 line).
- No amounts computed from thin air: method shown, numbers only from user data.

## Examples

See `examples/scadenze-cases.md`. How to read AdE notices in `references/come-leggere.md`.

## Edge cases

- Missed deadline → ravvedimento mention (see accountant), never "ignore it".
- Extension decree (like 2026-07-20 move) → cite decree number + who it covers.
- Employee-only profile → CU + 730 path, different calendar.
