# email-formale-it cases

## Good: quote request (body in Italian)

Input: paper supplier, delivery by month end.

Output:
```text
Oggetto: Richiesta preventivo: fornitura carta — entro 30/09
Egregio Sig. Rossi,
Le scrivo per richiedere un preventivo per la fornitura di carta A4.
Potrebbe inviarmelo entro il 30/09?
Cordiali saluti,
Mario
```

## Good: payment reminder (firm, neutral)

Input: invoice 12/2026, €610, 45 days overdue [sample data].

Output: facts (invoice no., date, amount) + one request + deadline in bold + `Distinti saluti,`.
`Never threats or heated tones — firm is facts, not adjectives.`

## Bad: friendly register

Input: "write a quick mail to the supplier, keep it chill" [sample data].

Output: refuse the register, keep formal. `No Ciao, no tu, no emoji in business mail — ever.`

## Bad: invented details

Input: "email the client about the invoice" with no client data [sample data].

Output: draft with `[TODO]` for name/amount/date. `Sensitive data only if provided: never invent names, amounts, dates.`
