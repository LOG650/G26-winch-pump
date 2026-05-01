# Avviksanalyse: Begrenset Power BI-eksportrettighet

**Dato:** 2026-04-30
**Identifisert av:** David (under første datafangst)
**Eier:** Begge
**Risikoreferanse:** R10 i `risk.json`
**Status:** Realisert, håndtert via kontingens

## Sammendrag

Prosjektet planla å bruke Power BI sin innebygde *Analyser i Excel* eller *Eksporter data* for å hente supply/demand-tabellen som CSV-fil. Ved første datafangst 2026-04-30 ble det oppdaget at prosjektgruppens Power BI-bruker ikke har rettigheter til disse funksjonene. Direkte tabelluttrekk er dermed ikke mulig innenfor prosjektets ressursrammer. Avviket er realisert og håndtert ved at gruppen har innført manuell skjermavlesning av PNG-skjermbilder med transkribering til CSV i Python.

## Identifisert avvik

Plandokumentene fra fase 2 (`prosjektsstyringsplan.md`, `core.json`) beskriver datakilden som *"ukentlige CSV-eksporter fra Power BI"*. Faktisk gjennomføring viser:

- *Analyser i Excel* er sperret for prosjektgruppens bruker.
- *Eksporter data* under enkeltvisualer er begrenset til formater som ikke gir maskinleselig tabelldata.
- *Eksporter underliggende data* krever Build-rettighet på datasettet, som ikke er tildelt.
- Tilgjengelige eksportformater begrenser seg til PowerPoint og PDF.

## Årsak

Tilgangsmodellen til Motive Offshores Power BI tildeler eksportrettigheter selektivt av datasikkerhetshensyn. Prosjektgruppens bruker har leserettighet på rapporten, men ikke Build-rettighet på datasettet. Dette er en reell sikkerhetspolicy hos Motive og kan ikke endres innenfor prosjektets tidsramme uten en formell tilgangsutvidelsesprosess.

## Konsekvens

- Direkte CSV-eksport er ikke farbar i prosjektperioden.
- Datafangst må gjennomføres manuelt med ny metodikk.
- Alle plandokumenter som beskriver *"CSV-eksport"* som datakilde må oppdateres eller suppleres med endringsnotat.
- Risiko for økt arbeidsmengde per snapshot og lavere datafangstfrekvens.
- Risiko for transkriberingsfeil i datakvaliteten.

## Tiltak (kontingens)

Følgende tiltak er implementert:

1. **Datafangst via skjermavlesning.** Hver datafangst gjennomføres ved at prosjektgruppen tar PNG-skjermbilder av Power BI-rapportens to relevante sider (*Supply/ Demand – Calendar* og *Supply vs Demand – Overview*) med fastsatt filtersett. Bildene lagres lokalt i `004 data/<dato>_motive_baseline/raw/`.
2. **Transkribering til CSV i Python.** Skript i `006 analysis/3.1 datainnhenting/_transcribe_*.py` (gitignored, inneholder rådata inline) leser av tallene fra skjermbildene og produserer lang-form CSV i `004 data/<dato>_motive_baseline/clean/`.
3. **Sumsjekk mot Power BI.** Hvert transkribert datasett verifiseres automatisk mot Power BIs egne Tier 1-gruppesummer og Totalt-rad via `verify_tier1_sums.py`. Avvik over $\pm 2$ unit-uker per gruppe per uke flagges som transkriberingsfeil.
4. **Avrundingsdokumentasjon.** Power BIs avrundingsstøy på opp til $\pm 2$ mellom celleverdier og Tier 1-summer dokumentert i kapittel 5.2.5 i sluttrapporten.
5. **Risiko R10 lagt til registeret.** Sannsynlighet 5 (realisert), konsekvens 3, nivå 15. Status: *Realisert (håndtert via skjermavlesning)*.

## Vurderte alternativer

| Alternativ | Vurdering |
|---|---|
| Tilgangseskalering hos Motive | Krever formell prosess som ikke ble vurdert gjennomførbar i prosjektperioden. Anbefales som forberedelse til produksjonsbruk. |
| PDF-eksport av rapportside | Selektérbar tekst i PDF kan parses programmatisk. Forkastet fordi det krever full rapportgenerering per datafangst og gir mindre granulær kontroll enn skjermbilder. |
| Skjermavlesning (valgt) | Manuell men kontrollert. Sumsjekk sikrer transkriberingskvalitet. |

## Påvirkning på øvrig plan

| Område | Påvirkning |
|---|---|
| Datafangstfrekvens | Uendret, fortsatt ukentlig |
| Datakvalitet | Akseptabel; sumsjekk validerer hver fangst |
| WBS 3.1 | Beskrivelse og deliverables oppdatert i `wbs.json` |
| Kapittel 5.2 i rapport | Datafangstmetoden beskrives presist i 5.2.3 |
| `core.json`, `requirements.json` | Oppdatert til å reflektere ny metode |
| `prosjektsstyringsplan.md` | Beholdt urørt som historisk leveranse; denne avviksanalysen dokumenterer endringen |
| Milepæl M4 | Indirekte forsinket (se `avviksanalyse-2026-05-01.md`) |

## Verifikasjon

Baseline-snapshot 2026-04-30 er fanget og transkribert med 0 transkriberingsfeil og 2 celler innen avrundingstoleranse. Datafangstmetoden er bekreftet fungerende, og sumsjekken validerer kvaliteten. Ingen reduksjon av prosjektets leveranseevne forventes.
