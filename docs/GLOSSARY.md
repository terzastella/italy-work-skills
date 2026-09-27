# Glossary — our words in plain language

Internal development words (batch, golden, guided, versions like 0.2) never
appear in user-facing pages. This file translates the few that leak through
automation, so nobody has to ask.

- **Skill** — one folder that teaches an agent one task (`SKILL.md` + examples).
- **Fixture** — a worked example with its expected result attached, used to
  test the small calculators automatically.
- **Calculator (scripts/)** — a tiny local program some skills ship for exact
  math (tax totals, instalments). Rates and tables are always inputs with a
  year, never hidden inside.
- **References** — background reading the agent opens only when needed.
- **Vendors** — third-party skills, copied exactly and never edited here.
- **Archive** — retired skills, kept for reference, never installed.
- **Catalog** — the generated theme list (`CATALOG.md`); a machine writes it,
  humans don't edit it.
- **Info-only** — skills that explain and refer to a professional instead of
  deciding (all legal/health/family matters).
- **Smoke test** — the 10-second `hello skills` check proving skills load.
