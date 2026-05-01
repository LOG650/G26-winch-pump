# 3.3 Gap-deteksjonslogikk

**WBS-aktivitet:** 3.3
**Eier:** Begge
**Status:** Pågår
**Milepæl:** M4 – første fungerende gap-deteksjonsscript (2026-04-18)

## Formål

Regelbasert logikk for identifisering av kapasitetsgap og uke-til-uke-endringer i supply/demand-data.

## Leveranser

- Python-script for gap-deteksjon
- Uke-til-uke-sammenligning av supply/demand-data
- Logg over utløste regler (dato, asset-type, verdier, mottaker)

## Akseptansekriterier

Gap-deteksjon skiller mellom **nye**, **eksisterende** og **forverrede** gap på testdata.

## Notat

Regelbasert tilnærming – ikke SARIMA. Uke-til-uke-sammenligning er kjernen.
