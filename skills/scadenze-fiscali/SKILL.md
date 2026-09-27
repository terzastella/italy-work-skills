---
name: scadenze-fiscali
description: Read Italian tax deadlines and build payment calendars. Use when asked scadenze fiscali, versamenti, acconto saldo, tax deadlines Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write
argument-hint: "[year/profile]"
user-invocable: true
disable-model-invocation: false
---

# Scadenze Fiscali

Tax deadlines read correctly: balance vs advance, extensions, and the golden rule —
always re-check AdE. Flagship skill: profile calendars, extension discipline, chains.

## When to use

- "scadenze fiscali", "versamenti", "acconto/saldo", "when to pay taxes Italy".
- Do not use for computing amounts owed (method + calendar only).
  Splits: see `acconti-calcolo`; regime math: see `regime-forfettario` — this skill dates them.

## Workflow (tappe with formal in/out)

### Tappa 1 — Profile + year (both or nothing)

Input: profile (forfettario / ordinary / employee), year, what's due
(income tax, advance, VAT, IMU?). Output: routed calendar template
(see `references/calendari-tipo.md`). Wrong profile = wrong calendar:
ask first, never default.

### Tappa 2 — Mechanism before dates

Explain saldo (prior year) + acconti (current year), historic method.
Forfettario specifics: imposta sostitutiva saldo + first advance (LM42 line,
split per current rules — see `acconti-calcolo`).

### Tappa 3 — Build the calendar table

Each row: date | who | what | surcharge? | source. Statutory deadline vs
announced extension distinguished, decree number + AdE notice date cited
(extensions like DL 89/2026 happen — never invented).

### Tappa 4 — Close with verify + links

Dates move yearly — verify on agenziaentrate.gov.it before paying.
Amounts chain: `regime-forfettario` computes, `acconti-calcolo` splits,
this skill dates. Missed deadline → ravvedimento mention (see accountant),
never "ignore it".

## Multi-turn protocol

Turn 1 (profile + year): "chi sei fiscalmente + che anno?" — both or nothing.
Turn 2 (calendar): dated table with sources. Turn 3 (amounts?): route to
regime/acconti skills — this skill never computes owed amounts.

## Rules

- Never state a deadline without year. Never invent extensions.
- Distinguish statutory deadline vs announced extension, with source + date.
- Forfettario specifics: imposta sostitutiva saldo + first advance (historic method, LM42 line).
- No amounts computed from thin air: method shown, numbers only from user data.
- Employee-only profile → CU + 730 path, different calendar (see `cu-730-guida`).

## Examples

Good and bad cases in `examples/scadenze-cases.md`. How to read AdE notices
in `references/come-leggere.md`. Profile calendars in `references/calendari-tipo.md`.

## Edge cases (priority order)

| # | Case | Action |
|---|---|---|
| 1 | Missed deadline | ravvedimento mention (see accountant), never "ignore it" |
| 2 | Extension decree | cite number + who it covers (e.g. 2026-07-20 move) |
| 3 | Employee-only | CU + 730 path, different calendar |
| 4 | Screenshot extension | decree number or it didn't happen (see come-leggere) |
| 5 | IMU/TARI mixed in | route to `imu-calcolo` / `tari-tassa`, never merge calendars |
