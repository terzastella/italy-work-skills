---
name: assicurazione-vita-info
description: Explain life policies with surrender math. Use when asked assicurazione vita, life policy Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[policy]"
user-invocable: true
disable-model-invocation: false
---

# Assicurazione Vita (Info Only)

Life policies decoded: TCM vs vita intera vs unit, surrender math.

## When to use

- "assicurazione vita", "life policy Italy".
- Do not use for investment advice (comparison math only).

## Workflow

1. Types: TCM (term, pays on death in window) · vita intera/miste (savings layer) · unit/index-linked (market risk flagged).
2. Surrender (riscatto): penalties by year + paid-vs-received math shown plainly.
3. Beneficiaries: designation + fuori-asse rules overview (no verdicts on shares).
4. Output: situation map + questions for insurer/advisor.

## Rules

- No product endorsement; no "sign it" pushes.
- Unit-linked risks stated bluntly (capital not guaranteed).
- Succession interplay flagged + notary referral for big estates (rules year-stated).

## Examples

See `examples/vita-cases.md`. Types in `references/tipi.md`.

## Edge cases

- Old dormant policy found → kiss-and-check path (company search + documents).
- Bank-pushed bundle with mortgage → tied-selling check + IVASS angle flagged.
- Lapsed payments → riduzione vs riscatto options explained.
