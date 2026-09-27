# Methodology — how this hub thinks

The equivalent of other repos' "Philosophy" section, written for our domain:
Italian bureaucratic work, where a wrong number costs money and a wrong
legal move costs more.

## 1. Information where it helps, referral where it matters

Skills explain and compute; they never replace the professional. Two tiers:

- **Operative skills** (invoices, budgets, emails, CVs): produce drafts and
  verified math. The agent acts, the human signs.
- **Info-only skills** (36 audited in `docs/AUDITS.md`): map the procedure,
  list the gates, refuse verdicts and strategies, close with a referral
  (accountant, notary, patronato, lawyer, doctor). Delicate topics never
  ship executable code — permanently.

## 2. Neutral calculators, never bundled truth

The bundled scripts compute pure math from explicit dated inputs: rates, brackets,
tables, thresholds. What they never do:

- Bundle a rate, table, or deadline as timeless truth.
- Decide eligibility, validity, or strategy.
- Reach the network, depend beyond stdlib (except documented cases like openpyxl).

A script that can't show its inputs refuses to run (year mismatch errors,
splits that don't sum to 100). That refusal is a feature.

## 3. English instructions, Italian artifacts

Agents trigger and compose in English; Italian users are served through Italian
outputs, not Italian instructions. Skill bodies, references, and examples are
English; invoice bodies, email bodies, rates, legal wordings stay Italian.
Only the landing pages (`README.md`/`README-IT.md`) may be Italian.

## 4. Progressive disclosure

Metadata (~100 tokens) routes; `SKILL.md` (<5.000 tokens) instructs; `references/`,
`scripts/`, `assets/` load on demand. Long tables and dated figures live in
references, never in the trigger path. Every skill links out (no isles):
related skills, regime hubs (`contratto-tipi`, `busta-paga-leggi`,
`scadenze-fiscali`), and official sources.

## 5. Evidence over claims

- Fiscal figures always carry their year. Examples use marked fake data.
- Worked examples with expected results live next to every script; `eval-golden.py`
  re-runs them deterministically in CI.
- Real-agent installs are recorded dated (`docs/TEST-PLAN.md` →
  `docs/COMPATIBILITY.md`). Untested is declared, never implied.

## 6. Maintenance over mass

Italian rules change yearly; every skill is a yearly liability. We prefer
249 deep skills to 400 shallow ones. New skills need a hole they fill
(see `.github/ISSUE_TEMPLATE/new-skill.md`); duplicates merge into hubs.
