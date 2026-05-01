# 3.4 Varslingslogikk

**WBS-aktivitet:** 3.4
**Eier:** Begge
**Status:** Ikke startet
**Milepæl:** M5 – varslingslogikk implementert (2026-05-02)

## Formål

Implementere 75 %-terskel, gap-deteksjon og e-postvarsling med ukentlige påminnelser.

## Leveranser

- Python-modul for e-postvarsling
- Varselsformat (utstyrsklasse, tidsperiode, gap-størrelse, mottaker)
- Ukentlig påminnelseslogikk frem til gap er løst
- Dokumentasjon av produksjonsintegrasjon (Power BI REST API)

## Akseptansekriterier

Varsel genereres korrekt ved ≥75 % vinnersannsynlighet og gap; påminnelse sendes ukentlig.

## Notat

SMTP-credentials lastes via `python-dotenv` fra en `.env`-fil som **ikke** skal committes.
