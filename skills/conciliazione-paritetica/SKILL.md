---
name: conciliazione-paritetica
description: Explain joint conciliation with consumer associations. Use when asked conciliazione paritetica, joint conciliation Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[dispute]"
user-invocable: true
disable-model-invocation: false
---

# Conciliazione Paritetica

Joint settlement with the company + consumer association: fast, free-ish, binding if agreed.

## When to use

- "conciliazione paritetica", "joint conciliation Italy".
- Do not use for court paths (see `giudice-di-pace`).

## Workflow

1. Sectors with active protocols (telecom, energy, transport, banks — verify live list).
2. Prior complaint to company first (mandatory order) via association.
3. Hearing: company + association reps, proposal, acceptance = binding deal.
4. Output: eligibility + steps + association contact logic (no invented addresses).

## Rules

- Company-first order mandatory; protocol must exist for the sector.
- Free or near-free: costs stated upfront.
- No outcome promises.

## Examples

See `examples/conciliazione-cases.md`. Protocol map in `references/protocolli.md`.

## Edge cases

- No protocol in sector → Conciliaweb/ARERA/ABF sector paths instead (routed).
- Failed conciliation → court/ADR next steps named, referral.
- Business (not consumer) → different tools, flag + referral.
