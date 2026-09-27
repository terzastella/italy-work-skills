# User guide — start here if you know nothing

## What this is

AI agents (Claude, Codex, Grok, and others) can learn reusable abilities
called **skills**. This repository is a collection of **254 skills for
Italian work life**, plus 24 well-known third-party skills included
as pinned copies. Everything runs **on your own computer** — no data
leaves your PC.

Examples of what the skills cover: Italian invoices with VAT, formal
business emails, payslip reading, tax deadlines, rental contracts,
public grants, health paperwork, school enrollments.

## Try it in 2 minutes

1. Install everything (see `INSTALL.md` for details):
   `python scripts/install.py --all`
2. Ask your agent: `hello skills` — it replies with a small table.
   That table means the skills are visible. Done.

## Three everyday examples you can copy

**An invoice.** "Draft an invoice: consulting 10h x 50 euro, VAT 22%."
You get a draft with verified totals (€610). Fill in names, have your
accountant confirm before sending.

**A payslip check.** "Base 1800 + 150 overtime, stated net 1620. Does it add up?"
You get every line explained and the math recomputed. Gaps become polite
questions for payroll — never accusations.

**Opening a VAT number.** "I want to freelance, expecting 50k. Where do I start?"
You get a step-by-step path: activity, tax regime, social contributions, deadlines,
first invoice — with an accountant review before filing anything.

## What to expect (honest limits)

- **Drafts and math, not verdicts.** Skills explain and compute; they never
  replace an accountant, notary, or lawyer. Sensitive topics (law, health,
  family, inheritance) give information plus a professional referral — always.
- **Figures carry their year.** Italian rules change yearly; every amount
  states which year it belongs to. If a number looks old, ask for the current one.
- **Your data stays yours.** Skills work on figures you provide. Redact names
  and fiscal codes before sharing payslips or contracts.

## Where to go next

- Installing on your agent: `INSTALL.md`
- Questions: `FAQ.md` — words we use: `GLOSSARY.md`
- How skills are built and checked: `METHODOLOGY.md`
- Full list by theme: `CATALOG.md`
