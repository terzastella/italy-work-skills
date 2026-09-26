# fattura-pa cases

## Good: comune service invoice

Input: cleaning service €5.000, CIG given, IPA given, split payment [sample data].

Output: draft with PA blocks + `Net €5.000 | VAT 22% €1.100 (split: paid by PA) | Due to you €5.000`
+ `Transmit via certified channel only after checks.`

## Bad: CIG invented

Input: CIG unknown, "mettine uno plausibile" [sample data].

Output: `Never invent CIG/CUP — from the call documents or [TODO]. Wrong codes reject the invoice.`
