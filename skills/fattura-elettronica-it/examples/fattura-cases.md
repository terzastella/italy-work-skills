# fattura-elettronica-it cases

## B2B draft with recipient code

Input: seller + buyer VAT IDs given, 2 items, code `ABC1234` [sample data].

Output: readable draft + XML field map (header, seller, buyer, body lines)
+ `Transmit only after accountant check. Never transmit from here.`

## Missing buyer VAT ID

Output: draft with `Buyer VAT ID: [TODO]`, totals computed anyway,
no invented VAT ID. Note: SdI accepts VAT ID or tax code as communicated.
