---
name: trasloco-diritti
description: Explain moving rights with quotes and damages. Use when asked trasloco, moving company Italy, danni trasloco.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[move]"
user-invocable: true
disable-model-invocation: false
---

# Trasloco Diritti

Moves protected: written quotes, inventory, damage claims that work.

## When to use

- "trasloco", "moving company Italy", "danni trasloco".
- Do not use for courts (small-claims referral at most).

## Workflow

1. Quote: written, itemized (volume, floors, disassembly, insurance) — verbal quotes rejected.
2. Inventory + photos before/after (the claim foundation).
3. Damage: prompt written notice + repair/replace/refund ladder (see garanzie logic).
4. Output: quote checklist + inventory template pointer + complaint draft if damaged.

## Rules

- No written quote = red flag #1, stated bluntly.
- Deposits capped reasonably; full prepay refused as advice.
- Insurance included vs optional: verified in writing, never assumed.

## Examples

See `examples/trasloco-cases.md`. Quote anatomy in `references/preventivo.md`.

## Edge cases

- International move → customs/inventory extra layer flagged + specialist.
- Storage (deposito) interim → terms + insurance + access rules checked.
- No-show mover → evidence + chargeback/denuncia paths, urgent tone.
