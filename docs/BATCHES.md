# Production batches

All skill content in English. Only `README.md` stays in Italian.

## RESTART 2026-09-23 — Italian Work Skills Hub

Generic batches below are archived (`archive/`, 35 skills, frozen).
Active: 87 skills in `skills/` (9 + Batch 1-IT 18 + Batch 2-IT 20 + Batch 3-IT 20 + Batch 4-IT 20).

## Batch 4-IT — daily life ✅ 2026-09-23 (87 active)

20 skills, each `SKILL.md` + `references/` + `examples/` (fake data always marked).

- Tax/family: tari-tassa, canone-rai, successioni-info, donazioni-info
- Jobs-4: periodo-prova, licenziamento-info, smart-working, part-time
- Home/car: utenze-voltura, affitto-breve, compravendita-auto
- School/health: scuola-iscrizioni, universita-tasse, medico-base, ticket-esenzioni, invalidita-104
- PA/documents: residenza-cambio, carta-identita-cie, patente-punti, permesso-soggiorno

Delicate (licenziamento-info, invalidita-104, successioni-info): info-only + referral, no tactics.
Batch gate: `validate.py` 88 OK zero warnings (87 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 87×9 ok.

## Batch 3-IT — enterprise, jobs-3, home, PA ✅ 2026-09-23 (67 active)

20 skills, each `SKILL.md` + `references/` + `examples/` (fake data always marked).

- Tax/business: nota-credito, contributi-inps, agevolazioni-assunzioni,
  ditta-vs-srl, camera-commercio, durc
- Jobs-3: maternita-congedi, malattia-certificato, apprendistato, contratto-tipi
- Home: condominio-spese, mutuo-tassi, compravendita-casa, auto-bollo, assegno-unico
- PA/tutele-2: anagrafe-certificati, passaporto-procedura, voli-ritardi,
  banche-reclami, vacanze-pacchetto

Batch gate: `validate.py` 68 OK zero warnings (67 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 67×9 ok.

## Batch 2-IT — second-level Italy ✅ 2026-09-23 (47 active)

20 skills, each `SKILL.md` + `references/` (incl. `fonti.md` with official links +
check date for tax/law/PA) + `examples/` (fake data always marked).

- Tax-2: partita-iva-apri, ateco-scelta, acconti-calcolo, ritenuta-acconto,
  operazioni-estero, fattura-pa, imu-calcolo, cu-730-guida
- Jobs-2: busta-paga-leggi, naspi-guida, tirocinio-guida
- Casa: isee-guida, bollette-energia, bonus-casa, sanita-digitale, affitto-check
- PA/tutele: pagopa-guida, garanzie-consumo, recesso-acquisti, isa-check
  (+ tirocinio-guida counted in jobs-2)

Batch gate: `validate.py` 48 OK zero warnings (47 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 47×9 ok.

## Batch 1-IT — Italy work ✅ 2026-09-23 (27 active)

18 skills, each `SKILL.md` + `references/` (incl. `fonti.md` with official links +
check date for tax/law/PA) + `examples/` (fake data always marked).

- Tax: fattura-elettronica-it, regime-forfettario, scadenze-fiscali, corrispettivi-it
- Formal: pec-bozza, sollecito-pagamento, verbale-riunione-it, preventivo-it, nota-spese
- Jobs: cv-europass, lettera-presentazione, colloquio-prep-it, dimissioni-procedura
- Calls/PA: bandi-pmi, domanda-bando, spid-cie-guida, privacy-informativa, visura-leggimi

Deferred: contratto-base-check, ferie-permessi (prudence review later).
Batch gate: `validate.py` 28 OK zero warnings (27 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 27×6 ok.
Maintenance note: tax thresholds/rates change yearly — refresh `fonti.md` dates annually.

## History (pre-restart, archived)

## Batch 1 — transversal foundations ✅ 2026-09-23 (24/200)

20 skills + 4 foundation. Each: `SKILL.md` + `references/` + `examples/`.

- Git & release: git-status-express, changelog-gen, release-notes, commit-scope
- Code quality: code-review-it, systematic-debug, refactor-plan, test-gen-it
- Docs: api-docs-it, readme-gen
- Documents/data: pdf-extract-it, csv-clean, xlsx-budget-it, invoice-it
- Writing: email-formale-it, translate-it-en
- Research/data: web-research, source-cite, json-clean
- Tooling: prompt-pack-it

Batch gate: `validate.py` 25 OK zero warnings (24 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 24×6 ok.

## Batch 2 — SEO & content ✅ 2026-09-23 (44/200)

20 skills, each `SKILL.md` + `references/` + `examples/`. All names in `catalog/_registry.md`.

- SEO foundations: seo-audit, meta-tags, headline-it, keyword-map, content-gap
- Planning: content-calendar, blog-outline, repurpose-content
- Social/newsletter/media: social-post-it, newsletter-it, video-script-it, podcast-outline
- Pages/product: landing-copy, product-desc-it, faq-gen, cta-optimize
- Trust/media: case-study, press-release-it, infographic-brief, readability-fix

Batch gate: `validate.py` 45 OK zero warnings (44 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 44×6 ok.

## Batch 3 (next, to plan)

Candidates by category (15-20 names to approve before writing):
- Cat.9 Data & scripts: log-analyze, rename-batch, backup-check…
- Cat.2 Code quality: tdd-guard, env-check…

Batch rules: never two open batches. Names first in `catalog/_registry.md`,
content in blocks of 5 with intermediate gates, indexes at the end.
