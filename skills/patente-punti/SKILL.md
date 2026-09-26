---
name: patente-punti
description: Explain licence points with deductions and recovery. Use when asked patente punti, driving licence points Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Patente a Punti

Points decoded: 20 to start, deductions per offence, how to earn back.

## When to use

- "patente punti", "driving licence points Italy", "decurtazione punti".
- Do not use for fines appeals (different path, flag it).

## Workflow

1. Balance: 20 start + bonus up to 30 after clean years (year-stated rules).
2. Deduction table by offence class (see `references/decurtazioni.md`): phone, speed, belt, alcohol tiers.
3. Zero points → revisione (re-exam) path; courses recover points (who/when).
4. Check saldo via official portal (SPID) — never third-party point checkers with data.

## Rules

- Tables with year; amounts/points move with code updates.
- Alcohol/drug tiers: criminal edge flagged + lawyer referral, no minimization.
- Neopatentati: doubled deductions + limits — always stated for new drivers.

## Examples

See `examples/patente-cases.md`.

## Edge cases

- Foreign licence in Italy → conversion/recognition paths, flag differences.
- Company car offence → driver declaration duty + terms, explain plainly.
- Contested fine → payment vs appeal trade-off with deadlines, no legal strategy beyond basics.
