# Official sources — fattura elettronica (verified 2026-09-23)

- AdE e-invoicing portal: https://www.agenziaentrate.gov.it/portale/fatturazione-elettronica
- AdE technical specs (SdI, v1.9.x, XAdES enveloped XML): https://www.agenziaentrate.gov.it/portale/specifiche-tecniche
- developers.italia.it FatturaPA: https://developers.italia.it/it/fatturapa
- Key rules used: XML via SdI mandatory since 1/1/2019 (B2B/B2C); simplified invoice ≤100€ total (art. 21-bis DPR 633/72);
  buyer = VAT ID or tax code as communicated; PA invoices under DM 55/2013.
- Re-check before transmitting: specs version and receipt codes change.
