# sollecito-pagamento cases

## L1 first reminder

Input: invoice 7/2026 €1.220, 20 days overdue, no prior reminders [sample data].

Output (Italian draft):
```text
Oggetto: Promemoria fattura n. 7/2026 — scadenza superata
Egregio...,
Le ricordo la fattura n. 7/2026 del 10/08/2026 di €1.220, scaduta il 10/09/2026.
La invito a provvedere entro 7 giorni. Resto a disposizione, anche per reinviarLe il documento.
Cordiali saluti, ...
```

## L3 with dispute (blocked escalation)

Input: client disputes the amount. Output: no L3 — clarification draft instead:
`Chiedo dettaglio contestazione prima di procedere.`
