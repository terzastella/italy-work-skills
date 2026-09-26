# nota-credito cases

## Good: wrong amount, same month

Input: invoice 15/2026 €1.000, correct €900 [sample data].

Output: TD04 draft referencing 15/2026 + `−€100 + VAT effect` + transmit-after-check note.

## Bad: silent correction

Input: "correggo la fattura e la rimando uguale" [sample data].

Output: `Issued invoices are not edited in place — credit note with reference, never silent resends.`
