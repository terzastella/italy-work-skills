---
name: noleggio-auto-diritti
description: Explain car rentals with deposits and damages. Use when asked noleggio auto, car rental Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[rental]"
user-invocable: true
disable-model-invocation: false
---

# Noleggio Auto Diritti

Rentals without surprises: deposits, deductibles, damage disputes.

## When to use

- "noleggio auto", "car rental Italy".
- Do not use for leasing (see `leasing-finanziamento`).

## Workflow

1. Before: deposit size + credit-card hold logic + deductible (franchigia) tiers + extra insurance options.
2. Pickup: photo/video round + fuel level + existing damage on contract.
3. Return: same-condition check + fuel + late-return fees.
4. Disputes: written contest + chargeback paths + evidence list.

## Rules

- Deductible tiers with the contract cited, year-stated; never generic "full coverage" as fact.
- Photos at pickup/return: the claim foundation, stressed first.
- No company endorsement.

## Examples

See `examples/noleggio-cases.md`. Checklist in `references/checklist.md`.

## Edge cases

- Debit card refused → credit-card requirement stated upfront.
- Cross-border use → authorized countries in contract, fines follow driver.
- Young driver surcharges → age rules stated plainly.
