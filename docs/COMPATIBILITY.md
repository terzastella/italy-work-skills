# Multi-agent compatibility

One `SKILL.md` for all. Differences only in the loader, not the format.

| Field | Required | Claude | Codex | Grok | Notes |
|-------|----------|--------|-------|------|-------|
| `name` | yes | ✅ | ✅ | ✅ | hyphen-case, == folder name, max 64 |
| `description` | yes | ✅ | ✅ | ✅ | what + when, max 1024, English |
| `license` | no | ✅ | ✅ | ✅ | MIT for ours, see THIRD-PARTY for vendors |
| `compatibility` | no | ✅ | ✅ | ✅ (ignores `model`,`effort`) | max 500 chars |
| `metadata` | no | ✅ | ✅ | ✅ (string map) | `author, version, lang` |
| `allowed-tools` | no | ✅ | ⚠️ experimental | ignored | Claude Code only |
| `argument-hint` | no | ignored | ignored | ✅ slash autocomplete |  |
| `user-invocable` | no | n/a | n/a | ✅ default true | `false` hides slash |
| `disable-model-invocation` | no | n/a | `allow_implicit_invocation` in openai.yaml | ✅ |  |

## Paths per agent

| Agent | Repo | User | Extra |
|-------|------|------|-------|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | plugin `.claude-plugin/` |
| Codex | `$REPO/.agents/skills/` | `~/.agents/skills/` | `/etc/codex/skills`, `agents/openai.yaml` |
| Grok | `./.grok/skills/` | `~/.grok/skills/` | also reads `.claude/`, `.agents/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |  |
| Copilot | `.github/skills/` | — | CLI also reads `.claude/`, `.agents/skills/` |
| Copilot CLI | `.github/skills/` | `~/.copilot/skills/` | same spec, SDK `skillDirectories` |
| Gemini | `.gemini/skills/` | — |  |
| OpenCode | `.opencode/skills/` | `~/.config/opencode/skills/` | also reads `.claude/`, `.agents/skills/`; permissions in `opencode.json` |
| Windsurf | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` | also reads `.agents/skills/`; invoke explicitly with `@skill-name` |

## Test status (update after real tests, 9 active skills)

| Skill | Claude | Codex | Grok | Last test |
|-------|--------|-------|------|-----------|
| hello-agent | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| skill-creator-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| invoice-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| email-formale-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| xlsx-budget-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| translate-it-en | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| press-release-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| doc-polish-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| case-study | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| fattura-elettronica-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| regime-forfettario | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| scadenze-fiscali | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| corrispettivi-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| pec-bozza | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| sollecito-pagamento | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| verbale-riunione-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| preventivo-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| nota-spese | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| cv-europass | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| lettera-presentazione | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| colloquio-prep-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| dimissioni-procedura | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| bandi-pmi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| domanda-bando | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| spid-cie-guida | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| privacy-informativa | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| visura-leggimi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| partita-iva-apri | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| ateco-scelta | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| acconti-calcolo | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| ritenuta-acconto | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| operazioni-estero | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| fattura-pa | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| imu-calcolo | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| cu-730-guida | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| busta-paga-leggi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| naspi-guida | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| isee-guida | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| bollette-energia | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| bonus-casa | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| sanita-digitale | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| affitto-check | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| pagopa-guida | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| garanzie-consumo | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| recesso-acquisti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| isa-check | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| tirocinio-guida | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| nota-credito | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| contributi-inps | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| agevolazioni-assunzioni | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| ditta-vs-srl | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| camera-commercio | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| durc | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| maternita-congedi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| malattia-certificato | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| apprendistato | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| contratto-tipi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| condominio-spese | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| mutuo-tassi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| compravendita-casa | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| auto-bollo | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| assegno-unico | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| anagrafe-certificati | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| passaporto-procedura | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| voli-ritardi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| banche-reclami | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| vacanze-pacchetto | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| tari-tassa | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| canone-rai | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| successioni-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| donazioni-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| patente-punti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| periodo-prova | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| licenziamento-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| smart-working | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| part-time | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| utenze-voltura | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| affitto-breve | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| compravendita-auto | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| scuola-iscrizioni | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| universita-tasse | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| medico-base | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| ticket-esenzioni | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| invalidita-104 | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| residenza-cambio | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| carta-identita-cie | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| permesso-soggiorno | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| colf-badanti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| collaborazioni-occasionali | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| pensione-guida | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| riscatto-laurea | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| tfr-fondo | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| prima-casa-agevolazioni | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| affitto-concordato | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| conto-corrente-costi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| rc-auto | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| criptovalute-fisco | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| spese-mediche-detrazioni | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| unioni-convivenze | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| asilo-nido-bonus | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| testamento-olografo | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| aire-estero | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| certificati-estero | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| telefonia-reclami | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| energia-reclami | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| assicurazione-casa | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| animali-viaggi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| ravvedimento-operoso | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| cartelle-ader | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| rateizzazione-debiti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| cedolare-secca | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| firma-digitale | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| cassa-integrazione | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| welfare-aziendale | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| ecommerce-adempimenti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| sicurezza-lavoro | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| marchi-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| ape-certificazione | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| edilizia-cila-scia | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| amministratore-condominio | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| domicilio-digitale-inad | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| cassetto-fiscale | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| elezioni-voto | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| multe-ricorso | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| assicurazione-sanitaria | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| dis-coll | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| pensione-reversibilita | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| accertamento-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| compensazioni-f24 | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| rimborsi-fiscali | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| somministrazione | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| lavoro-minorile | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| startup-innovativa | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| fallimento-crisi-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| franchising-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| usufrutto-nuda | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| spese-notarili | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| mantenimento-figli | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| matrimonio-civile | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| cittadinanza | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| assistenza-anziani | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| bonus-cultura-18app | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| patronato-servizi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| concorsi-pubblici | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| leasing-finanziamento | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| trasloco-diritti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| riscaldamento-contabilizzazione | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| giudice-di-pace | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| conciliazione-paritetica | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| diffida-legale | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| mediazione-civile | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| testamento-pubblico | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| eredita-debiti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| volture-catastali | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| trasferta-estero | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| infortuni-lavoro | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| reperibilita-lavoro | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| revisione-auto | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| ztl-permessi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| trasporto-disabili | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| vaccini-obbligatori | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| donazione-sangue | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| pronto-soccorso-ticket | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| straordinari-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| conti-deposito | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| fondo-emergenza | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| trasferte-lavoro | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| irpef-scaglioni | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| addizionali-regionali | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| imposta-bollo | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| aspettativa-lavoro | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| trasferimento-sede | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| plusvalenza-casa | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| case-popolari-erp | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| agenti-rappresentanti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| appalti-pubblici-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| congedo-matrimoniale | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| mensa-scolastica | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| impegnativa-visite | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| donazione-organi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| adozioni-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| separazione-divorzio | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| servizio-civile | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| tredicesima-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| buoni-fruttiferi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| treni-diritti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| noleggio-auto-diritti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| plusvalenza-finanziaria | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| ivafe-ivie | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| dichiarazione-integrativa | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| orario-riposi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| permessi-studio-150 | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| impresa-familiare | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| cooperative-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| comodato-uso | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| cognome-figli | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| pignoramento-conto | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| farmaci-equivalenti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| ricetta-elettronica | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| guardia-medica-turisti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| maturita-esame | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| testamento-biologico-dat | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| carte-revolving | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| usura-tassi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| assicurazione-viaggio | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| officina-diritti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| bagagli-smarriti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| dsa-bes-scuola | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| universita-fuorisede | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| erasmus-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| its-academy | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| assemblea-condominiale | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| morosita-condominiale | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| lavori-straordinari | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| distacco-lavoratore | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| lavoro-notturno | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| festivi-lavorati | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| buoni-pasto | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| esami-intramoenia | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| screening-prevenzione | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| farmaci-estero | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| abbonamenti-palestra | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| assicurazione-vita-info | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| conti-cointestati | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| limite-contante | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| bonifici-istantanei | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| carta-prepagata | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| frontend-design (vendor/anthropics) | ⚠️ untested | ⚠️ untested | ⚠️ untested | Apache-2.0 |
| skill-creator (vendor/anthropics) | ⚠️ untested | ⚠️ untested | ⚠️ untested | Apache-2.0 |
| mcp-builder (vendor/anthropics) | ⚠️ untested | ⚠️ untested | ⚠️ untested | Apache-2.0 |
| webapp-testing (vendor/anthropics) | ⚠️ untested | ⚠️ untested | ⚠️ untested | Apache-2.0 |
| claude-api (vendor/anthropics) | ⚠️ untested | ⚠️ untested | ⚠️ untested | Apache-2.0 |
| brand-guidelines (vendor/anthropics) | ⚠️ untested | ⚠️ untested | ⚠️ untested | Apache-2.0 |
| doc-coauthoring (vendor/anthropics) | ⚠️ untested | ⚠️ untested | ⚠️ untested | Apache-2.0 |
| internal-comms (vendor/anthropics) | ⚠️ untested | ⚠️ untested | ⚠️ untested | Apache-2.0 |
| canvas-design (vendor/anthropics) | ⚠️ untested | ⚠️ untested | ⚠️ untested | Apache-2.0 |
| theme-factory (vendor/anthropics) | ⚠️ untested | ⚠️ untested | ⚠️ untested | Apache-2.0 |
| tdd (vendor/pocock) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |
| diagnosing-bugs (vendor/pocock) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |
| code-review (vendor/pocock) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |
| research (vendor/pocock) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |
| to-spec (vendor/pocock) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |
| prototype (vendor/pocock) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |
| brainstorming (vendor/superpowers) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |
| writing-plans (vendor/superpowers) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |
| executing-plans (vendor/superpowers) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |
| systematic-debugging (vendor/superpowers) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |
| test-driven-development (vendor/superpowers) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |
| using-git-worktrees (vendor/superpowers) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |
| requesting-code-review (vendor/superpowers) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |
| verification-before-completion (vendor/superpowers) | ⚠️ untested | ⚠️ untested | ⚠️ untested | MIT |

Archived generic skills (35 in `archive/`) are not tested or installed.

How to test (local only):
1. `python scripts/install.py --skill hello-agent --agent <agent>`
2. Ask the agent `hello skills` and check the reply table
3. Mark ✅ + date + agent version (e.g. `✅ 2026-09-23 claude-code 1.x`)
4. Repeat for `smart-commit` (sample diff) and `doc-polish-it` (sample file)
