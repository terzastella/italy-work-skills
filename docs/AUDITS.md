# Audits — sensitive skills self-certification

36 skills carry legal, health, family, or financial weight. Each is audited
below: what it DOES, what it REFUSES, and where it REFERS. Rule of the house:

- Info-only + professional referral, always. No validity verdicts, no case
  strategy, no executable legal/medical acts, no diagnosis, no fund names.
- Delicate skills NEVER ship executable `scripts/`. Math-only scripts
  (Golden-1) are banned here permanently.
- Every sensitive answer ends with a referral line. No exceptions.

## Lavoro e previdenza

| Skill | Does | Refuses | Refers to |
|---|---|---|---|
| contratto-base-check | clause map, red-flag list, questions for review | validity verdicts, dispute strategy | union / labor lawyer |
| contratto-tipi | contract type overview | "which contract for me" verdicts | union / accountant |
| licenziamento-info | procedure map, deadlines overview | case strategy, letter drafting as tactic | union / lawyer |
| maternita-congedi | leave types, durations (year-stated) | case-specific entitlement verdicts | patronato / INPS |
| pensione-guida | path overview, requirements map | amount computation, "when retire" verdicts | patronato |
| pensione-reversibilita | eligibility map | amount verdicts | patronato |
| pignoramento-conto | mechanics, urgency ladder | debt strategy | lawyer |
| multe-ricorso | appeal paths overview | appeal drafting as strategy, success odds | judge / lawyer |
| whistleblowing-info | channel order, protections overview | case content strategy | ANAC / specialist |
| salute-mentale-info | access paths, helplines, 118 ladder | diagnosis, therapy, medication talk | CSM / GP / 118 |
| invalidita-104 | benefit map, application paths | medical verdicts | patronato / doctor |

## Fisco e impresa

| Skill | Does | Refuses | Refers to |
|---|---|---|---|
| accertamento-info | audit invites, adhesion paths map | defense strategy | accountant / lawyer |
| criptovalute-fisco | declaration paths map | evasion-adjacent optimization | accountant |
| fallimento-crisi-info | crisis procedure map | turnaround strategy | OCC / lawyer |
| irap-info | who-pays + base method | final computation as verdict | accountant |
| appalti-pubblici-info | tender reading map | bid strategy | tender consultant |
| cooperative-info | form overview | incorporation verdicts | notary / accountant |
| franchising-info | contract reading points | "sign it" verdicts | lawyer |
| marchi-info | registration paths | prior-art verdicts | UIBM attorney |

## Famiglia e successioni

| Skill | Does | Refuses | Refers to |
|---|---|---|---|
| adozioni-info | path overview | suitability predictions, timelines | tribunal / services |
| affido-familiare | types, allowances, paths | suitability/timeline predictions | services / tribunal |
| separazione-divorzio | procedure map | strategy, custody predictions | lawyer |
| mantenimento-figli | computation method overview | amount verdicts | judge / lawyer |
| eredita-debiti | accept/renounce mechanics | estate strategy | notary |
| successioni-info | declaration paths, deadlines | filing as such | CAF / notary |
| donazioni-info | forms overview | tax-optimization schemes | notary |
| testamento-olografo | formal requirements map | clause drafting with effects | notary |
| testamento-pubblico | form overview | content advice | notary |
| testamento-biologico-dat | DAT paths | content advice | doctor / notary |
| unioni-convivenze | regime overview | strategy on disputes | lawyer |
| cittadinanza | path overview | eligibility verdicts | prefettura / lawyer |
| permesso-soggiorno | permit types, renewal paths | case strategy on quotas | patronato / lawyer |

## Giustizia e salute

| Skill | Does | Refuses | Refers to |
|---|---|---|---|
| giudice-di-pace | competence + procedure map | outcome predictions | lawyer |
| mediazione-civile | procedure map | strategy | mediator / lawyer |
| vaccini-obbligatori | obligation map (year-stated) | medical advice | pediatrician / GP |
| assicurazione-vita-info | product mechanics | product picks, returns promises | IVASS / advisor |

## Verification

- `security-check.py` covers all 36 (no PII/secrets patterns).
- `validate.py` enforces structure; content audit is this file + review.
- Scripts ban: `for d in <36 dirs>; do test ! -d skills/$d/scripts` — zero exceptions.
- Re-audit on every content change to a listed skill.
