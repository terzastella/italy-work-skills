# Changelog

## 1.1 (Batch 1-IT, 27 active + 35 archived)

- 18 Italy skills: tax (fattura-elettronica-it, regime-forfettario, scadenze-fiscali,
  corrispettivi-it), formal (pec-bozza, sollecito-pagamento, verbale-riunione-it,
  preventivo-it, nota-spese), jobs (cv-europass, lettera-presentazione,
  colloquio-prep-it, dimissioni-procedura), calls/PA (bandi-pmi, domanda-bando,
  spid-cie-guida, privacy-informativa, visura-leggimi).
- Each with `fonti.md` (official links + 2026-09-23 check date) and professional disclaimer.
- Deferred: contratto-base-check, ferie-permessi.
- Indexes: `skills.json` 1.1.0 (27 entries), `plugin.json` 1.1.0.

## 1.0-it (restart Italia, 9 active + 35 archived)

- Pivot: Italian Work Skills Hub. Active `skills/`: hello-agent, skill-creator-it,
  invoice-it, email-formale-it, xlsx-budget-it, translate-it-en,
  press-release-it, doc-polish-it, case-study.
- 35 generic skills moved to `archive/` (frozen, not installed). Backup zip kept.
- Indexes rebuilt: `catalog/skills.json` 1.0.0, `plugin.json` 1.0.0, short `llms.txt`.
- README rewritten with Italy claim (only file in Italian).
- Registry v2 with Italy categories (Fisco, Formali, Lavoro, Bandi-PA, Tutele).

## History (0.x, pre-restart)

- Full English: all 44 skills + templates + scripts + docs in English.
  Only `README.md` stays in Italian. Folder names frozen (`-it` = Italian origin
  or Italy-specific domain). Metadata `lang: "en"`.
- `catalog/skills.json` v0.4.0, `plugin.json` 0.3.0.

## 0.4.0-local (44/200)

- Batch 2 SEO & content: 20 skills (audit, meta, headlines, calendar, keywords,
  gap, outlines, social, newsletter, landing, product, faq, cases, press,
  video, podcast, infographics, cta, readability, reuse), with references+examples
- Name registry with category seats, `docs/BATCHES.md` updated

## 0.3.0-local (24/200)

- Batch 1 transversal foundations: 20 skills (git/release, code quality, docs,
  documents/data, writing, research, tooling), each with references+examples
- Name registry `catalog/_registry.md`, journal `docs/BATCHES.md`
- Indexes: `catalog/skills.json` 24 entries, `llms.txt`, `plugin.json` 0.2.0

## 0.2.0-local

- Local hygiene: badges, `CONTRIBUTING.md`, `SECURITY.md`, roadmap without GitHub
- Depth: `smart-commit` + `doc-polish-it` + `hello-agent` with references/examples/assets
- New: `skill-creator-it`
- Local trust: extended `validate.py` + `scripts/security-check.py`

## 0.1.0

- Scaffold: 3 starter skills, universal installer, `.agents/.claude/.grok/.github` adapters
- Catalog: `catalog/skills.json`, `vendors-manifest.json`, `llms.txt`
