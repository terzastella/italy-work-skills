# fattura-elettronica-it cases

## Good: B2B draft with recipient code

Input: seller + buyer VAT IDs given, 2 items, code `ABC1234` [sample data].

Output: readable draft + XML field map (header, seller, buyer, body lines)
+ `Transmit only after accountant check. Never transmit from here.`

## Good: missing buyer VAT ID

Output: draft with `Buyer VAT ID: [TODO]`, totals computed anyway,
no invented VAT ID. Note: SdI accepts VAT ID or tax code as communicated.

## Bad: transmit from here

Input: "send it to SdI for me" [sample data].

Output: refuse. `Never forge signatures or transmit to SdI: drafting aid only. Transmit after accountant check.`

## Bad: invented recipient code

Input: buyer code unknown [sample data].

Output: `0000000` + certified email path for consumers, or IPA lookup for PA — never an invented 7-char code.
