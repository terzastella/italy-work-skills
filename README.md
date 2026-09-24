# Italian Work Skills Hub 🇮🇹

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Spec: agentskills.io](https://img.shields.io/badge/Spec-agentskills.io-blue.svg)
![Validate: local](https://img.shields.io/badge/Validate-local-yellow.svg)

Il primo hub sistematico di **Agent Skills per il lavoro italiano**: fatture con IVA, email formali, budget, comunicati, traduzioni IT-EN. Skill vere e installabili su Claude, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode e Windsurf con un comando.

Sviluppo su repo GitHub privata + branch per batch. Pubblicazione pubblica e marketplace rinviati.

> Skill tutte in inglese (`-it` = dominio Italia o origine italiana).
> Solo questo README resta in italiano.
> Standard: [Agent Skills open standard](https://agentskills.io) (`SKILL.md` + frontmatter).

## Perché Italia

I grandi repo mondiali (superpowers, mattpocock, ECC) coprono coding e marketing USA. Nessuno copre il lavoro italiano: fattura elettronica e IVA, PEC, email con il `Lei`, forfettario, scadenze, Europass, bandi. Qui ogni skill parla di questi casi, con fonti ufficiali (AdE, INPS, EUR-Lex) e disclaimer "verifica col professionista" dove serve.

## Perché questo repo è diverso

1. **Skill vere e installabili** in `skills/` (formato `SKILL.md` universale)
2. **Installer universale** — 1 comando per 9 agenti (Claude, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf)
3. **Profondità**: ogni skill ha `SKILL.md` + `references/` + `examples/`
4. **Separazione chiara**: `skills/*` = originali (MIT) vs `catalog/vendors-manifest.json` = solo link alle ufficiali
5. **Validazione locale** con `scripts/validate.py` + `scripts/security-check.py`
6. **Archivio**: le skill generiche pre-restart stanno in `archive/` (consultabili, non installate)

## Quickstart

```bash
git clone https://github.com/terzastella/AI-Skills.git
cd AI-Skills

# Installa tutto ovunque (9 agenti: claude, codex, grok, cursor, copilot, copilot-cli, gemini, opencode, windsurf)
python scripts/install.py --all

# Oppure solo una skill su un agente
python scripts/install.py --skill invoice-it --agent claude
python scripts/install.py --skill invoice-it --agent codex
python scripts/install.py --skill invoice-it --agent grok

# Verifica che tutto rispetti la spec agentskills.io
python scripts/validate.py
python scripts/security-check.py
```

Destinazioni:

| Agente | Destinazione | Note |
|--------|--------------|------|
| Claude Code | `~/.claude/skills/` o `.claude/skills/` | + plugin via `.claude-plugin/plugin.json` |
| Codex (ChatGPT dev) | `.agents/skills/` | standard Codex, vedi `.agents/skills/README.md` |
| ChatGPT (app) | via Plugin / Codex | Custom GPT in dismissione sett-dic 2026, vedi `docs/CHATGPT-MIGRATION.md` |
| Grok | `~/.grok/skills/` | compatibile anche con `.claude/` e `.agents/` |
| Cursor | `.cursor/skills/` | stesso `SKILL.md` |
| Copilot | `.github/skills/` | stesso `SKILL.md` |
| Copilot CLI | `~/.copilot/skills/` | personale, legge anche `.github/` e `.agents/` |
| Gemini | `.gemini/skills/` | stesso `SKILL.md` |
| OpenCode | `.opencode/skills/` | legge anche `.claude/` e `.agents/` |
| Windsurf | `.windsurf/skills/` | invoca esplicito con `@nome-skill` |

> Formato `skills/*/SKILL.md` compatibile anche con `gh skill install`.

## Catalogo skill (MIT, in inglese)

227 skill organizzate in 16 temi — catalogo completo in [`docs/CATALOG.md`](docs/CATALOG.md)
(generato da `catalog/skills.json`, non modificare a mano):

- [Fisco e tasse](docs/CATALOG.md#fisco-e-tasse) (33) · [Lavoro](docs/CATALOG.md#lavoro) (38) · [Casa](docs/CATALOG.md#casa) (24)
- [PA e documenti](docs/CATALOG.md#pa-e-documenti) (19) · [Impresa](docs/CATALOG.md#impresa) (19) · [Salute](docs/CATALOG.md#salute) (15)
- [Soldi e banche](docs/CATALOG.md#soldi-e-banche) (15) · [Trasporti e viaggi](docs/CATALOG.md#trasporti-e-viaggi) (13) · [Famiglia](docs/CATALOG.md#famiglia) (12)
- [Scuola e giovani](docs/CATALOG.md#scuola-e-giovani) (7) · [Tutele e consumi](docs/CATALOG.md#tutele-e-consumi) (7) · [Giustizia](docs/CATALOG.md#giustizia) (6)
- [Successioni e donazioni](docs/CATALOG.md#successioni-e-donazioni) (6) · [Pensioni](docs/CATALOG.md#pensioni) (4) · [Scrittura e contenuti](docs/CATALOG.md#scrittura-e-contenuti) (4) · [Tooling](docs/CATALOG.md#tooling) (2)

### In evidenza

| Skill | Perché |
|-------|--------|
| [invoice-it](skills/invoice-it/SKILL.md) | Fatture italiane con IVA verificata |
| [regime-forfettario](skills/regime-forfettario/SKILL.md) | Soglie 85k/100k e calcoli |
| [fattura-elettronica-it](skills/fattura-elettronica-it/SKILL.md) | XML via SdI senza scarti |
| [email-formale-it](skills/email-formale-it/SKILL.md) | Il `Lei` fatto bene |
| [pec-bozza](skills/pec-bozza/SKILL.md) | Valore legale preservato |
| [naspi-guida](skills/naspi-guida/SKILL.md) | Requisiti senza miti |
| [isee-guida](skills/isee-guida/SKILL.md) | DSU senza errori |
| [bandi-pmi](skills/bandi-pmi/SKILL.md) | Go/no-go onesto |
| [hello-agent](skills/hello-agent/SKILL.md) | Smoke test 10 secondi |

Installazione: `python scripts/install.py --skill <nome> --all` (tabella completa in `docs/CATALOG.md`).


## Skill ufficiali (solo reference, non copiate)

Non duplichiamo codice altrui per licenza e manutenzione. Vedi `catalog/vendors-manifest.json`:

* **Anthropic `anthropics/skills`**: esempi Apache-2.0 + `docx/pdf/pptx/xlsx` (source-available, solo reference).
* **OpenAI Codex**: skills in `.agents/skills/` + `agents/openai.yaml`.
* **xAI Grok**: built-in Word/Presentations/Spreadsheets/PDFs/Skill Creator + docs `.grok/skills/`.

## Struttura repo

```
ai-skills/
  README.md + LICENSE + llms.txt  # root essenziale
  skills/                    # SOURCE OF TRUTH: 227 skill (9 + batch 1-11 IT)
    tooling: hello-agent/ skill-creator-it/
    cuore: invoice-it/ email-formale-it/ xlsx-budget-it/
      translate-it-en/ press-release-it/ doc-polish-it/ case-study/
    batch1-IT fisco: fattura-elettronica-it/ regime-forfettario/
      scadenze-fiscali/ corrispettivi-it/
    batch1-IT formali: pec-bozza/ sollecito-pagamento/
      verbale-riunione-it/ preventivo-it/ nota-spese/
    batch1-IT lavoro: cv-europass/ lettera-presentazione/
      colloquio-prep-it/ dimissioni-procedura/
    batch1-IT bandi-PA: bandi-pmi/ domanda-bando/ spid-cie-guida/
      privacy-informativa/ visura-leggimi/
    batch2-IT fisco2: partita-iva-apri/ ateco-scelta/ acconti-calcolo/
      ritenuta-acconto/ operazioni-estero/ fattura-pa/ imu-calcolo/ cu-730-guida/
    batch2-IT lavoro2/casa: busta-paga-leggi/ naspi-guida/ isee-guida/
      bollette-energia/ bonus-casa/ sanita-digitale/ affitto-check/
    batch2-IT PA/tutele: pagopa-guida/ garanzie-consumo/ recesso-acquisti/
      isa-check/ tirocinio-guida/
    batch3-IT fisco/impresa: nota-credito/ contributi-inps/ agevolazioni-assunzioni/
      ditta-vs-srl/ camera-commercio/ durc/
    batch3-IT lavoro: maternita-congedi/ malattia-certificato/
      apprendistato/ contratto-tipi/
    batch3-IT casa: condominio-spese/ mutuo-tassi/ compravendita-casa/
      auto-bollo/ assegno-unico/
    batch3-IT PA/tutele: anagrafe-certificati/ passaporto-procedura/
      voli-ritardi/ banche-reclami/ vacanze-pacchetto/
    batch4-IT fisco/famiglia: tari-tassa/ canone-rai/ successioni-info/ donazioni-info/
    batch4-IT lavoro/casa: periodo-prova/ licenziamento-info/ smart-working/
      part-time/ utenze-voltura/ affitto-breve/ compravendita-auto/
    batch4-IT scuola/salute: scuola-iscrizioni/ universita-tasse/ medico-base/
      ticket-esenzioni/ invalidita-104/
    batch4-IT PA/documenti: residenza-cambio/ carta-identita-cie/
      patente-punti/ permesso-soggiorno/
    batch5-IT lavoro/pensioni: colf-badanti/ collaborazioni-occasionali/
      pensione-guida/ riscatto-laurea/ tfr-fondo/
    batch5-IT casa/soldi: prima-casa-agevolazioni/ affitto-concordato/
      conto-corrente-costi/ rc-auto/ criptovalute-fisco/
    batch5-IT famiglia/estero: spese-mediche-detrazioni/ unioni-convivenze/
      asilo-nido-bonus/ testamento-olografo/ aire-estero/
    batch5-IT tutele: certificati-estero/ telefonia-reclami/ energia-reclami/
      assicurazione-casa/ animali-viaggi/
    batch6-IT fisco: ravvedimento-operoso/ cartelle-ader/ rateizzazione-debiti/
      cedolare-secca/ firma-digitale/
    batch6-IT lavoro/impresa: cassa-integrazione/ welfare-aziendale/
      ecommerce-adempimenti/ sicurezza-lavoro/ marchi-info/
    batch6-IT casa/digitali: ape-certificazione/ edilizia-cila-scia/
      amministratore-condominio/ domicilio-digitale-inad/ cassetto-fiscale/
    batch6-IT PA/salute: elezioni-voto/ multe-ricorso/ assicurazione-sanitaria/
      dis-coll/ pensione-reversibilita/
    batch7-IT fisco/lavoro: accertamento-info/ compensazioni-f24/ rimborsi-fiscali/
      somministrazione/ lavoro-minorile/
    batch7-IT impresa/casa: startup-innovativa/ fallimento-crisi-info/ franchising-info/
      usufrutto-nuda/ spese-notarili/
    batch7-IT famiglia/salute: mantenimento-figli/ matrimonio-civile/ cittadinanza/
      assistenza-anziani/ bonus-cultura-18app/
    batch7-IT PA/tutele: patronato-servizi/ concorsi-pubblici/ leasing-finanziamento/
      trasloco-diritti/ riscaldamento-contabilizzazione/
    batch8-IT giustizia/successioni: giudice-di-pace/ conciliazione-paritetica/
      diffida-legale/ mediazione-civile/ testamento-pubblico/
    batch8-IT eredità/lavoro: eredita-debiti/ volture-catastali/ trasferta-estero/
      infortuni-lavoro/ reperibilita-lavoro/
    batch8-IT trasporti/salute: revisione-auto/ ztl-permessi/ trasporto-disabili/
      vaccini-obbligatori/ donazione-sangue/
    batch8-IT soldi/lavoro: pronto-soccorso-ticket/ straordinari-info/ conti-deposito/
      fondo-emergenza/ trasferte-lavoro/
    batch9-IT fisco/lavoro: irpef-scaglioni/ addizionali-regionali/ imposta-bollo/
      aspettativa-lavoro/ trasferimento-sede/
    batch9-IT casa/impresa: plusvalenza-casa/ case-popolari-erp/ agenti-rappresentanti/
      appalti-pubblici-info/ congedo-matrimoniale/
    batch9-IT famiglia/salute: mensa-scolastica/ impegnativa-visite/ donazione-organi/
      adozioni-info/ separazione-divorzio/
    batch9-IT PA/soldi: servizio-civile/ tredicesima-info/ buoni-fruttiferi/
      treni-diritti/ noleggio-auto-diritti/
    batch10-IT fisco/lavoro: plusvalenza-finanziaria/ ivafe-ivie/ dichiarazione-integrativa/
      orario-riposi/ permessi-studio-150/
    batch10-IT impresa/casa: impresa-familiare/ cooperative-info/ comodato-uso/
      cognome-figli/ pignoramento-conto/
    batch10-IT salute/scuola: farmaci-equivalenti/ ricetta-elettronica/ guardia-medica-turisti/
      maturita-esame/ testamento-biologico-dat/
    batch10-IT soldi/tutele: carte-revolving/ usura-tassi/ assicurazione-viaggio/
      officina-diritti/ bagagli-smarriti/
    batch11-IT scuola/condominio: dsa-bes-scuola/ universita-fuorisede/ erasmus-info/
      its-academy/ assemblea-condominiale/
    batch11-IT condominio/lavoro: morosita-condominiale/ lavori-straordinari/
      distacco-lavoratore/ lavoro-notturno/ festivi-lavorati/
    batch11-IT buoni/salute: buoni-pasto/ esami-intramoenia/ screening-prevenzione/
      farmaci-estero/ abbonamenti-palestra/
    batch11-IT soldi: assicurazione-vita-info/ conti-cointestati/ limite-contante/
      bonifici-istantanei/ carta-prepagata/
    (ognuna: SKILL.md + references/ + examples/)
  archive/                   # skill generiche pre-restart (non installate)
    batch1-generic/ (17) + batch2-seo/ (18)
  templates/skill-starter/   # modello per nuove skill
  catalog/                   # skills.json + vendors-manifest.json + _registry.md
  .agents/skills/README.md   # standard Codex/Cursor/Copilot
  .claude/README.md          # adapter Claude Code (+ .claude-plugin/plugin.json)
  .grok/README.md            # adapter Grok Code
  .github/skills/README.md   # adapter Copilot + Copilot CLI
  .opencode/skills/README.md # adapter OpenCode
  .windsurf/skills/README.md # adapter Windsurf (invocazione @nome)
  docs/                      # COMPATIBILITY, CREATE-SKILL, CHATGPT-MIGRATION, THIRD-PARTY, BATCHES
  scripts/install.py + validate.py + security-check.py
```

Regola: **modifica solo in `skills/`**, il resto è generato/copiato da `install.py`.

## Creare una nuova skill

```bash
cp -r templates/skill-starter skills/mia-skill
# edita skills/mia-skill/SKILL.md (name == nome cartella, description con cosa+quando)
python scripts/validate.py --skill mia-skill
```

Guida completa: `docs/CREATE-SKILL.md`. Per skill Italia: aggiungi fonti ufficiali + disclaimer professionista.

## Licenze

* `skills/*`, `templates/*`, `scripts/*`, docs: **MIT** (vedi `LICENSE`).
* Skill ufficiali linkate in `catalog/vendors-manifest.json`: restano dei rispettivi proprietari. In particolare `docx/pdf/pptx/xlsx` di Anthropic sono **source-available, non open-source** — non copiarle, linkale (vedi `docs/THIRD-PARTY-NOTICES.md`).
* Le skill fisco/legge sono bozze informative, non consulenza professionale.

## Roadmap (repo GitHub privata, sviluppo per batch)

- [x] Restart Italia 1.0 (9 skill + archivio 35 generiche)
- [x] Batch 1-IT (18 skill: fisco, formali, lavoro, bandi/PA) → totale 27
- [x] Batch 2-IT (20 skill: fisco 2, lavoro 2, casa, PA, tutele) → totale 47
- [x] 9 agenti (claude, codex, grok, cursor, copilot, copilot-cli, gemini, opencode, windsurf)
- [x] CI gates su repo privata (validate + security + install dry-run)
- [x] Batch 3-IT (20 skill: fisco/impresa, lavoro, casa, PA/tutele) → totale 67
- [x] Batch 4-IT (20 skill: fisco/famiglia, lavoro, casa/auto, scuola/salute, PA) → totale 87
- [x] Batch 5-IT (20 skill: lavoro/pensioni, casa/soldi, famiglia/estero, tutele) → totale 107
- [x] Batch 6-IT (20 skill: fisco, lavoro/impresa, casa/digitali, PA/salute) → totale 127
- [x] Batch 7-IT (20 skill: fisco/lavoro, impresa/casa, famiglia/salute, PA/tutele) → totale 147
- [x] Batch 8-IT (20 skill: giustizia/successioni, eredità/lavoro, trasporti/salute, soldi/lavoro) → totale 167
- [x] Batch 9-IT (20 skill: fisco/lavoro, casa/impresa, famiglia/salute, PA/soldi) → totale 187
- [x] Batch 10-IT (20 skill: fisco/lavoro, impresa/casa, salute/scuola, soldi/tutele) → totale 207
- [x] Batch 11-IT (20 skill: scuola/condominio, condominio/lavoro, buoni/salute, soldi) → totale 227
- [ ] Rinviati da valutare: contratto-base-check, ferie-permessi
- [ ] Test reali sugli agenti e badge in `docs/COMPATIBILITY.md`
- [ ] Batch 12-IT da pianificare (vedi `catalog/_registry.md`)
- [ ] Rinviato (serve repo pubblica): submit a skills.sh / agentskills.io
