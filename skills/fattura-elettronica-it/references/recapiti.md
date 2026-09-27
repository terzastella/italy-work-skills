# Recipient routing (fattura-elettronica-it)

Wrong recipient = certain rejection. Route BEFORE drafting.

## B2B with SdI code

7-char code from the buyer (cassetto fiscale / IPA for PA). Draft carries it
in the transmission block. Unknown code → `[TODO]`, never invented.

## B2C consumers

`0000000` + buyer's certified email (PEC). No PEC → paper-equivalent paths
flagged, accountant confirms.

## PA (see `fattura-pa`)

IPA code + CIG/CUP where required (DM 55/2013). Split payment noted.
Never improvise CIG/CUP: call documents or `[TODO]`.

## Forfettari issuers

No VAT lines by definition. Bollo €2 line where due (see `imposta-bollo`).
Exemption statement on face, every invoice.
