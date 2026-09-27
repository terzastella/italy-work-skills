# Production batches

All skill content in English. Only `README-IT.md` stays in Italian (`README.md` is the English showcase).

## RESTART 2026-09-23 - Italian Work Skills Hub

Generic batches below are archived (`archive/`, 35 skills, frozen).
Active: 254 skills in `skills/` + 24 pinned vendor skills in `vendors/`.

## Local-tests-1 - first real-agent runs ✅ 2026-09-26 (no version bump)

- OpenCode + Ollama `qwen3:8b` (qwen3.6 too slow on this hardware, recorded):
  9 runs, 7 ✅ (hello-agent, invoice-it, frontend-design, tdd, imu-calcolo,
  irpef-scaglioni, acconti-calcolo), 2 model-limit ❌ (implicit trigger miss,
  brainstorming methodology fail). Zero skill-content bugs.
- `opencode.json` (Ollama provider) committed; skills installed to
  `.opencode/skills/` (gitignored). Log: `docs/TEST-PLAN-LOCAL.md`,
  results: `docs/COMPATIBILITY.md` local-track section.
- Lesson logged: agents write outputs into installed skill dirs — check
  `git status` after every agent session. Fixed: `hello-agent` table version 0.1→0.2.

## Matrix-codex-1 - codex + ollama-local ✅ 2026-09-26 (no version bump)

- `codex exec` + provider `ollama-local` (`~/.codex/config.toml`, no login):
  5 cells, 3 ✅ (hello-agent via file-read, frontend-design, brainstorming con
  riserva), 1 grave invention ❌ (invoice-it invented IBAN/SWIFT), 1 harness ❌
  (sandbox blocked all writes on tdd). Claude CLI reinstalled (was broken shim).
- Auto-load does NOT trigger on qwen3:8b — explicit file-read priming required.
- Log: `docs/TEST-PLAN-LOCAL.md` codex section; results: `docs/COMPATIBILITY.md`.

## Matrix-claude-1 - ollama launch claude + qwen3:8b ✅ 2026-09-26 (no version bump)

- `ollama launch claude --model qwen3:8b` accepts piped prompts, no login needed.
  Skills installed to `~/.claude/skills/` (no repo dest for claude); prompts
  need ABSOLUTE skill paths (launched cwd differs).
- 5 cells, 4 ✅ (hello-agent, invoice-it con riserva, frontend-design,
  brainstorming), 1 methodology ❌ (tdd showed test-after, no RED).
  Claude CLI reinstalled earlier (was broken shim) — healthy now.

## Percorsi-1.16 - guided paths ✅ 2026-09-25 (254 active)

5 hub skills (`user-invocable` entry points) orchestrating existing skills with
handoff context, no duplicated questions. Each: SKILL.md + `references/tappe.md` +
`examples/percorso-cases.md` (2 end-to-end Good + 1 Bad) + run protocol in
`tests/percorsi/` + behavior guards.

- Impresa: percorso-apri-partita-iva (idea→ATECO→regime+script→INPS→scadenze→prima fattura)
- Lavoro: percorso-assunzione-domestica (profilo→contratto→paga→contributi→permessi→prima busta),
  percorso-busta-controllo (contratto→netto+script→TFR+script→ferie+script)
- Casa: percorso-casa-compravendita (budget→rogito→notaio→IMU+script→TARI)
- Successioni: percorso-lutto (delicate, sober tone, debts-before-assets, referrals every tappa)

Batch gate: `validate.py` 279 OK (278 entries + template),
`security-check.py` clean, `install.py --all` dry-run ok (254 ours × 9 agents),
`eval-behavior.py` OK (25 guided: 20 golden + 5 percorsi).

## Percorsi-0.2 - guided paths versioned ✅ 2026-09-25 (no version bump)

The 5 `percorso-*` hubs bumped 0.1→0.2 (they already met the Golden bar:
tappe + end-to-end Good/Bad + run protocols + behavior guards).
**Nothing left at 0.1: 254/254 skills at 0.2.** Depth program complete:
Golden-1..11 (219) + Delicate-1 (30) + Percorsi (5).

## Delicate-1 - sensitive wave ✅ 2026-09-25 (no version bump)

All 30 delicate skills to 0.2 with Good/Bad examples, year markers, out-links —
text-only forever (scripts ban enforced by eval-behavior: 0/36 ship code).
Every Bad case is a refused verdict/strategy/prediction. No simulated personal
cases: protocols are procedural info-seeking prompts.
Behavior guards extended to 245 guided (215 + 30). Zero skills left at 0.1
outside the 5 percorsi (guided, versioned separately).

## Golden-12 - flagship XL ✅ 2026-09-25 (no version bump)

10 flagship skills to long guides (100-150 SKILL lines, tappe + multi-turn +
priority edge tables, split references, 0.3): imu-calcolo (tappe, special
cases, payment notes, 5 fixtures), irpef-scaglioni (tappe, detrazioni layer,
5 fixtures), regime-forfettario (gates-first tappe, esclusioni file,
5 fixtures), busta-paga-leggi (section walk, 5 fixtures), scadenze-fiscali
(profile calendars), partita-iva-apri (cost preview), fattura-elettronica-it
(recipient routing), naspi-guida (duties file), colf-badanti (nights file),
successioni-info (debts-first file). Multi-turn protocols extended.
Gate: fixtures 63/63 green.

## Golden-11 - depth wave eleven ✅ 2026-09-25 (no version bump)

19 remaining neutral skills to 0.2 (last neutrals: only 30 delicate + 5 percorsi
left at 0.1): abbonamenti-palestra, cognome-figli, colloquio-prep-it,
doc-polish-it, lettera-presentazione, matrimonio-civile, matrimonio-estero,
patronato-servizi, press-release-it, privacy-informativa, pronto-soccorso-ticket,
ricetta-elettronica, screening-prevenzione, servizi-cimiteriali-funebri,
servizio-civile, skill-creator-it, translate-it-en, universita-estero-laurea,
verbale-riunione-it. Good/Bad + year markers + out-links; toolchain skills
(doc-polish-it, skill-creator-it) get *-cases.md protocols. Text-only wave.
Behavior guards extended to 215 guided.

## Golden-10 - depth wave ten ✅ 2026-09-25 (no version bump)

20 more skills to 0.2 with Good/Bad examples, year markers, out-links:
casa/tutele (ape-certificazione, assicurazione-casa, assicurazione-sanitaria,
assicurazione-viaggio, case-popolari-erp, comodato-uso, diffida-legale),
PA/salute (domicilio-digitale-inad, donazione-organi, donazione-sangue,
edilizia-cila-scia, esami-intramoenia, farmaci-equivalenti, farmaci-estero,
firma-digitale, impegnativa-visite), scuola/lavoro/PA (its-academy,
lavoro-minorile, maturita-esame, pagopa-guida). Text-only wave.
Behavior guards extended to 196 guided.

## Golden-9 - depth wave nine ✅ 2026-09-25 (no version bump)

20 more skills to 0.2 with Good/Bad examples, year markers, out-links:
lavoro/casa (amministratore-condominio, volture-catastali, trasferimento-sede,
trasferta-estero, infortuni-lavoro, concorsi-pubblici, welfare-aziendale,
multiproprieta-diritti, officina-diritti, noleggio-auto-diritti), soldi/PA/
famiglia (carta-prepagata, conti-cointestati, bonus-cultura-18app,
scuola-privata-paritaria, animali-viaggi, aire-estero, certificati-estero,
elezioni-voto, assistenza-anziani, cure-termali). Text-only wave.
Behavior guards extended to 176 guided.

## Golden-8 - depth wave eight ✅ 2026-09-25 (no version bump)

20 more skills to 0.2 with Good/Bad examples, year markers, out-links:
soldi (fondo-emergenza, plusvalenza-finanziaria, leasing-finanziamento),
casa/fisco (affitto-check, compravendita-casa, fattura-proforma,
libri-contabili, isa-check), lavoro (part-time, permessi-studio-150,
lavoro-spettacolo, trasferte-lavoro, reperibilita-lavoro), sindacati
(sciopero-diritti, assemblea-sindacale, rsu-rls, videosorveglianza-lavoro,
stagionali-turismo, smart-working, aspettativa-lavoro).
2 new neutral scripts (fondo, plusvalenza): fixtures 55/55 green.
Behavior guards extended to 156 guided.

## Golden-7 - depth wave seven ✅ 2026-09-25 (no version bump)

20 more skills to 0.2 with Good/Bad examples, year markers, out-links:
auto/trasporti (bonus-casa, canone-rai, auto-bollo, rc-auto,
compravendita-auto, patente-punti, revisione-auto, ztl-permessi,
trasporto-disabili), tutele/scuola/salute (energia-reclami,
telefonia-reclami, vacanze-pacchetto, bagagli-smarriti, erasmus-info,
universita-fuorisede, dsa-bes-scuola, sanita-digitale, medico-base,
guardia-medica-turisti, mensa-scolastica). Text-only wave.
Behavior guards extended to 136 guided.

## Golden-6 - depth wave six ✅ 2026-09-25 (no version bump)

20 more skills to 0.2 with Good/Bad examples, year markers, out-links:
fisco/impresa (cartelle-ader, corrispettivi-it, cu-730-guida, operazioni-estero,
impresa-familiare, limite-contante, visura-leggimi, cassetto-fiscale, durc),
forme/lavoro/servizi (ditta-vs-srl, ecommerce-adempimenti, ateco-scelta,
dis-coll, agevolazioni-assunzioni, lavori-straordinari, sicurezza-lavoro),
trasversali (preventivo-it, sollecito-pagamento, case-study, trasloco-diritti).
Text-only wave. Behavior guards extended to 116 guided.

## Golden-5 - depth wave five ✅ 2026-09-25 (no version bump)

20 more skills to 0.2 with Good/Bad examples, year markers, out-links:
fisco/impresa (nota-credito, nota-spese, fattura-pa, camera-commercio,
startup-innovativa), lavoro (tirocinio-guida, agenti-rappresentanti,
buoni-pasto, distacco-lavoratore), soldi/casa (fido-scoperto, assegni-bancari,
bonifici-istantanei, banche-reclami, morosita-condominiale,
assemblea-condominiale), PA/tutele (anagrafe-certificati, carta-identita-cie,
garanzie-consumo, recesso-acquisti, treni-diritti). Text-only wave (no new
scripts — remaining neutral calculators honestly exhausted).
Behavior guards extended to 105 guided.

## Golden-4 - depth wave four ✅ 2026-09-25 (no version bump)

20 more skills to 0.2 with Good/Bad examples, year markers, out-links:
fisco (contributi-inps, imposta-bollo, rimborsi-fiscali, ivafe-ivie,
addizionali-regionali), lavoro (cassa-integrazione, lavoro-notturno,
festivi-lavorati, somministrazione, usura-tassi), casa/scuola/PA
(prima-casa-agevolazioni, spese-notarili, usufrutto-nuda, affitto-breve,
utenze-voltura, asilo-nido-bonus, scuola-iscrizioni, ticket-esenzioni,
passaporto-procedura, residenza-cambio).
2 new neutral scripts (contributi, bollo): fixtures 51/51 green.
Behavior guards extended to 85 guided.

## Golden-3 - depth wave three ✅ 2026-09-25 (no version bump)

20 more skills to 0.2 with Good/Bad examples, year markers, out-links:
fisco (ravvedimento-operoso, compensazioni-f24, spese-mediche-detrazioni,
plusvalenza-casa, rateizzazione-debiti, dichiarazione-integrativa), lavoro
(straordinari-info, collaborazioni-occasionali, orario-riposi,
congedo-matrimoniale), soldi/casa (condominio-spese, mutuo-tassi,
conti-deposito, carte-revolving, buoni-fruttiferi), tutele/casa/scuola
(riscaldamento-contabilizzazione, voli-ritardi, conciliazione-paritetica,
affitto-concordato, universita-tasse).
12 new neutral scripts (ravvedimento, compensa, detrai19, pluscasa, rateizza,
straord, occasionali, riparto, mutuo, deposito, revolving, bpf): fixtures
48/48 green. Behavior guards extended to 65 guided.

## Golden-2 - depth wave two ✅ 2026-09-25 (no version bump)

20 more skills to 0.2 with Good/Bad examples, year markers, out-links:
fisco (fattura-elettronica-it, ritenuta-acconto, cedolare-secca), math
(tredicesima-info, riscatto-laurea), lavoro (contratto-tipi, periodo-prova,
dimissioni-procedura, malattia-certificato, apprendistato), soldi/casa/PA
(conto-corrente-costi, tari-tassa, bollette-energia, spid-cie-guida,
domanda-bando), info/delicate text-only (maternita-congedi, pensione-guida,
successioni-info, donazioni-info, testamento-olografo — no scripts, ever).
5 new neutral scripts (ritenuta, cedolare, tredicesima, riscatto + eval branches):
fixtures 32/32 green. Behavior guards extended to 45 guided.

## Superpowers-2 - hooks, versions, multi-harness ✅ 2026-09-25 (no version bump)

- `hooks/session-start.md`: Italian-work router + per-harness wiring (text only, no executables).
- `.version-bump.json` + `scripts/bump-version.py` (tested: 1.15.0→1.15.1→reverted).
- `scripts/build-plugins.py`: generates `.codex-plugin/`, `.cursor-plugin/`,
  `gemini-extension.json` from `skills.json` (273 skills each) + CI sync check.
- `GEMINI.md` twin of `AGENTS.md`; cumulative `RELEASE-NOTES.md`
  (absorbs `RELEASE-NOTES-1.15.md`).

## Superpowers-1 - behavior harness ✅ 2026-09-25 (no version bump)

- `tests/` drill-style harness: README + `patterns-ban.txt` + 20 Golden run
  protocols (`input.md` + `expect.md` each).
- `scripts/eval-behavior.py`: static guards — Golden out-links/Good-Bad/year
  markers, delicate scripts-ban + referral + no-affirmative-verdicts (CI step).
  Fixed real gaps on first run (missing Good cases, missing year markers,
  dead link filename `mu-cases.md` was Golden-1).
- Workflow docs reference the new gates (`AGENTS.md`, PR template).

## Fiducia-1 - evals + audits + test plan ✅ 2026-09-25 (no content change)

- `scripts/eval-golden.py`: deterministic runner over all Golden-1 fixtures
  (23/23 green, CI step). No LLM, no network.
- `docs/AUDITS.md`: self-certification sheets for the 36 sensitive skills
  (does / refuses / refers). Scripts ban on delicate verified: 0/36 ship code.
- `docs/TEST-PLAN.md`: 5 skills × 3 agents protocol with install commands
  and per-cell smoke prompts. Account-side execution pending (yours).

## Golden-1 - depth program ✅ 2026-09-25 (20 skills deepened, no version bump)

20 most-used skills deepened in place (`metadata.version` 0.1→0.2): expanded
SKILL.md, split references, good/bad examples, cross-links (no Golden left
without an out-link). 10 neutral stdlib scripts added (math only, rates and
tables are explicit dated inputs, never bundled truth):

- imu-calcolo (`imu.py`, 3 fixtures), irpef-scaglioni (`irpef.py` + dated tables,
  3 fixtures), acconti-calcolo (`acconti.py`, explicit split, 3 fixtures),
  regime-forfettario (`forfettario.py`, 3 fixtures), invoice-it (`totals.py`,
  2 fixtures), busta-paga-leggi (`payslip_check.py`, 3 fixtures),
  ferie-permessi (`ratei.py`, 2 fixtures), tfr-fondo (`rivalutazione.py`, 2 fixtures),
  assegno-unico (`fasce.py` + dated tables, 1 fixture), xlsx-budget-it (`budget.py`, 1 fixture).
- Text-only deep-dives (no script by design): scadenze-fiscali, naspi-guida
  (typos fixed), email-formale-it, pec-bozza, cv-europass, bandi-pmi,
  colf-badanti, partita-iva-apri, isee-guida, hello-agent (`## Rules` added).

Delicate/info-only skills are excluded from scripts, permanently.
Gate: `validate.py` full OK (hardened: frontmatter + sections + references/examples),
every script run against its fixtures with matching outputs, `security-check.py` clean.

## Integrativa 1.15 - deferred closed ✅ 2026-09-25 (249 active)

2 skills (the historic deferred), each `SKILL.md` + `references/` + `examples/`.

- Lavoro: contratto-base-check, ferie-permessi (info-only + referral, no verdicts)

Batch gate: `validate.py` 274 OK (273 entries + template),
`security-check.py` clean, `install.py --all` dry-run ok (249 ours × 9 agents).

## Batch 12-IT - sindacati, impresa, casa, scuola ✅ 2026-09-25 (247 active)

20 skills, each `SKILL.md` + `references/` + `examples/` (fake data always marked).

- Sindacati/lavoro: sciopero-diritti, assemblea-sindacale, rsu-rls, stagionali-turismo, videosorveglianza-lavoro
- Impresa/fisco: libri-contabili, whistleblowing-info, fattura-proforma, irap-info, lavoro-spettacolo
- Casa/famiglia/salute: multiproprieta-diritti, affido-familiare, matrimonio-estero, salute-mentale-info, cure-termali
- Scuola/fine-vita/soldi: scuola-privata-paritaria, universita-estero-laurea, servizi-cimiteriali-funebri, fido-scoperto, assegni-bancari

Delicate (affido-familiare, salute-mentale-info): info-only + referral.
Batch gate: `validate.py` 272 OK (271 entries + template; `CHANGELOG` counts 271 entries),
`security-check.py` clean, `install.py --all` dry-run ok (247 ours × 9 agents).

## Vendor batch ✅ 2026-09-23 (227 ours + 24 vendors)

24 verbatim pinned copies (see `vendors/upstreams.lock.json`): anthropics-skills (10),
mattpocock-skills (6), superpowers (8). Opt-in via `install.py --source vendors`.
Excluded: docx/pdf/pptx/xlsx (source-available); Codex/Grok have no public repos.

Batch gate: `validate.py` zero FAIL (vendor-only structural issues are warnings),
`security-check.py` clean, `install.py --all` + `--all --source vendors` ok,
`sync-vendors.py` pinned and current.

## Vendor resync ✅ 2026-09-26 (superpowers 5bf4e78 → 8ca22db)

CI drift job flagged `obra/superpowers` moved (release v6.4.2, "leaner plans").
Re-copied the 8 pinned trees byte-identical: only `writing-plans/SKILL.md`
reworked upstream + `plan-document-reviewer-prompt.md` deleted upstream
(no dangling refs). Other trees + all frontmatter descriptions unchanged.
`--include-vendors` security hits are pre-existing upstream-doc placeholders.
Lock + manifest + NOTICES bumped; drift check green.

## Batch 11-IT - school, condo, money ✅ 2026-09-23 (227 active)

20 skills, each `SKILL.md` + `references/` + `examples/` (fake data always marked).

- School/condo: dsa-bes-scuola, universita-fuorisede, erasmus-info, its-academy, assemblea-condominiale
- Condo/jobs: morosita-condominiale, lavori-straordinari, distacco-lavoratore, lavoro-notturno, festivi-lavorati
- Vouchers/health: buoni-pasto, esami-intramoenia, screening-prevenzione, farmaci-estero, abbonamenti-palestra
- Money: assicurazione-vita-info, conti-cointestati, limite-contante, bonifici-istantanei, carta-prepagata

Batch gate: `validate.py` 228 OK zero warnings (227 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 227×9 ok.

## Batch 10-IT - money, business, health ✅ 2026-09-23 (207 active)

20 skills, each `SKILL.md` + `references/` + `examples/` (fake data always marked).

- Tax/jobs: plusvalenza-finanziaria, ivafe-ivie, dichiarazione-integrativa, orario-riposi, permessi-studio-150
- Business/home: impresa-familiare, cooperative-info, comodato-uso, cognome-figli, pignoramento-conto
- Health/school: farmaci-equivalenti, ricetta-elettronica, guardia-medica-turisti, maturita-esame, testamento-biologico-dat
- Money/tutele: carte-revolving, usura-tassi, assicurazione-viaggio, officina-diritti, bagagli-smarriti

Delicate (testamento-biologico-dat, pignoramento-conto): info-only + referral.
Batch gate: `validate.py` 208 OK zero warnings (207 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 207×9 ok.

## Batch 9-IT - tax, home, family ✅ 2026-09-23 (187 active)

20 skills, each `SKILL.md` + `references/` + `examples/` (fake data always marked).

- Tax/jobs: irpef-scaglioni, addizionali-regionali, imposta-bollo, aspettativa-lavoro, trasferimento-sede
- Home/business: plusvalenza-casa, case-popolari-erp, agenti-rappresentanti, appalti-pubblici-info, congedo-matrimoniale
- Family/health: mensa-scolastica, impegnativa-visite, donazione-organi, adozioni-info, separazione-divorzio
- PA/money: servizio-civile, tredicesima-info, buoni-fruttiferi, treni-diritti, noleggio-auto-diritti

Delicate (adozioni-info, separazione-divorzio): info-only + referral.
Batch gate: `validate.py` 188 OK zero warnings (187 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 187×9 ok.

## Batch 8-IT - justice, transport, money ✅ 2026-09-23 (167 active)

20 skills, each `SKILL.md` + `references/` + `examples/` (fake data always marked).

- Justice/succession: giudice-di-pace, conciliazione-paritetica, diffida-legale, mediazione-civile, testamento-pubblico
- Debts/jobs: eredita-debiti, volture-catastali, trasferta-estero, infortuni-lavoro, reperibilita-lavoro
- Transport/health: revisione-auto, ztl-permessi, trasporto-disabili, vaccini-obbligatori, donazione-sangue
- Money/jobs: pronto-soccorso-ticket, straordinari-info, conti-deposito, fondo-emergenza, trasferte-lavoro

Delicate (giudice-di-pace, mediazione-civile, eredita-debiti, vaccini-obbligatori): info-only + referral.
Batch gate: `validate.py` 168 OK zero warnings (167 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 167×9 ok.

## Batch 7-IT - audits, business, family ✅ 2026-09-23 (147 active)

20 skills, each `SKILL.md` + `references/` + `examples/` (fake data always marked).

- Tax/jobs: accertamento-info, compensazioni-f24, rimborsi-fiscali, somministrazione, lavoro-minorile
- Business/home: startup-innovativa, fallimento-crisi-info, franchising-info, usufrutto-nuda, spese-notarili
- Family/health: mantenimento-figli, matrimonio-civile, cittadinanza, assistenza-anziani, bonus-cultura-18app
- PA/tutele: patronato-servizi, concorsi-pubblici, leasing-finanziamento, trasloco-diritti, riscaldamento-contabilizzazione

Delicate (mantenimento-figli, fallimento-crisi-info): info-only + referral.
Batch gate: `validate.py` 148 OK zero warnings (147 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 147×9 ok.

## Batch 6-IT - tax ops, business, home ✅ 2026-09-23 (127 active)

20 skills, each `SKILL.md` + `references/` + `examples/` (fake data always marked).

- Tax: ravvedimento-operoso, cartelle-ader, rateizzazione-debiti, cedolare-secca, firma-digitale
- Jobs/business: cassa-integrazione, welfare-aziendale, ecommerce-adempimenti, sicurezza-lavoro, marchi-info
- Home/digital: ape-certificazione, edilizia-cila-scia, amministratore-condominio,
  domicilio-digitale-inad, cassetto-fiscale
- PA/health: elezioni-voto, multe-ricorso, assicurazione-sanitaria, dis-coll, pensione-reversibilita

Delicate (multe-ricorso, pensione-reversibilita, marchi-info): info-only + referral.
Batch gate: `validate.py` 128 OK zero warnings (127 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 127×9 ok.

## Batch 5-IT - pensions, money, family ✅ 2026-09-23 (107 active)

20 skills, each `SKILL.md` + `references/` + `examples/` (fake data always marked).

- Jobs/pensions: colf-badanti, collaborazioni-occasionali, pensione-guida, riscatto-laurea, tfr-fondo
- Home/money: prima-casa-agevolazioni, affitto-concordato, conto-corrente-costi, rc-auto, criptovalute-fisco
- Family/abroad: spese-mediche-detrazioni, unioni-convivenze, asilo-nido-bonus, testamento-olografo, aire-estero
- Tuteles: certificati-estero, telefonia-reclami, energia-reclami, assicurazione-casa, animali-viaggi

Delicate (pensione-guida, testamento-olografo, criptovalute-fisco): info-only + referral.
Batch gate: `validate.py` 108 OK zero warnings (107 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 107×9 ok.

## Batch 4-IT - daily life ✅ 2026-09-23 (87 active)

20 skills, each `SKILL.md` + `references/` + `examples/` (fake data always marked).

- Tax/family: tari-tassa, canone-rai, successioni-info, donazioni-info
- Jobs-4: periodo-prova, licenziamento-info, smart-working, part-time
- Home/car: utenze-voltura, affitto-breve, compravendita-auto
- School/health: scuola-iscrizioni, universita-tasse, medico-base, ticket-esenzioni, invalidita-104
- PA/documents: residenza-cambio, carta-identita-cie, patente-punti, permesso-soggiorno

Delicate (licenziamento-info, invalidita-104, successioni-info): info-only + referral, no tactics.
Batch gate: `validate.py` 88 OK zero warnings (87 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 87×9 ok.

## Batch 3-IT - enterprise, jobs-3, home, PA ✅ 2026-09-23 (67 active)

20 skills, each `SKILL.md` + `references/` + `examples/` (fake data always marked).

- Tax/business: nota-credito, contributi-inps, agevolazioni-assunzioni,
  ditta-vs-srl, camera-commercio, durc
- Jobs-3: maternita-congedi, malattia-certificato, apprendistato, contratto-tipi
- Home: condominio-spese, mutuo-tassi, compravendita-casa, auto-bollo, assegno-unico
- PA/tutele-2: anagrafe-certificati, passaporto-procedura, voli-ritardi,
  banche-reclami, vacanze-pacchetto

Batch gate: `validate.py` 68 OK zero warnings (67 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 67×9 ok.

## Batch 2-IT - second-level Italy ✅ 2026-09-23 (47 active)

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

## Batch 1-IT - Italy work ✅ 2026-09-23 (27 active)

18 skills, each `SKILL.md` + `references/` (incl. `fonti.md` with official links +
check date for tax/law/PA) + `examples/` (fake data always marked).

- Tax: fattura-elettronica-it, regime-forfettario, scadenze-fiscali, corrispettivi-it
- Formal: pec-bozza, sollecito-pagamento, verbale-riunione-it, preventivo-it, nota-spese
- Jobs: cv-europass, lettera-presentazione, colloquio-prep-it, dimissioni-procedura
- Calls/PA: bandi-pmi, domanda-bando, spid-cie-guida, privacy-informativa, visura-leggimi

Deferred: contratto-base-check, ferie-permessi (prudence review later).
Batch gate: `validate.py` 28 OK zero warnings (27 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 27×6 ok.
Maintenance note: tax thresholds/rates change yearly - refresh `fonti.md` dates annually.

## History (pre-restart, archived)

## Batch 1 - transversal foundations ✅ 2026-09-23 (24/200)

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

## Batch 2 - SEO & content ✅ 2026-09-23 (44/200)

20 skills, each `SKILL.md` + `references/` + `examples/`. All names in `catalog/_registry.md`.

- SEO foundations: seo-audit, meta-tags, headline-it, keyword-map, content-gap
- Planning: content-calendar, blog-outline, repurpose-content
- Social/newsletter/media: social-post-it, newsletter-it, video-script-it, podcast-outline
- Pages/product: landing-copy, product-desc-it, faq-gen, cta-optimize
- Trust/media: case-study, press-release-it, infographic-brief, readability-fix

Batch gate: `validate.py` 45 OK zero warnings (44 skills + template),
`security-check.py` clean, `install.py --all --dest ./tmp-test` 44×6 ok.

Batch rules (still valid): never two open batches. Names first in `catalog/_registry.md`,
content in blocks of 5 with intermediate gates, indexes at the end.
