# Agentinstrukser – G26 WinchPump

## Prosjekt

**Navn:** KI-basert kapasitetsvarsling for Motive Offshore
**Emne:** LOG650, Høgskolen i Molde
**Gruppe:** G26 WinchPump
**Medlemmer:** Tord Haakon Johnsen Hovden og David Johan Lunde
**Veiledere:** Bård-Inge Pettersen, Per Kristian Rekdal
**Innleveringsfrist:** 31. mai 2026
**Muntlig eksamen:** 1. juni 2026

## Språk og tone

- Svar alltid på **norsk**
- Vær kortfattet og presis – unngå unødvendig utfylling
- Bruk faglige termer der det er naturlig (supply/demand, kapasitetsgap, gap-deteksjon, varslingslogikk osv.)
- Bruk norsk i rapporttekst, statusfiler og planfiler
- Behold norske bokstaver **æ, ø og å** i både kode, Markdown og genererte tabeller når filene skal leses av mennesker

## Encoding

- Lagre alle tekstfiler som **ren UTF-8 uten BOM**
- Hvis PowerShell viser feil tegn, anta at filen ikke er ødelagt før filinnholdet er kontrollert direkte med Read-verktøyet
- Vær ekstra oppmerksom på `status.md`, `rapport.md` og genererte `.md`-tabeller – disse blir lett stygge ved feil encoding

## Mappestruktur

```
000 templates/     – Maler fra høgskolen (ikke rediger)
001 info/          – Generell prosjektinfo
002 meetings/      – Møtereferater
003 references/    – Litteratur og kilder
004 data/          – Rådata og rensede data (KONFIDENSIELT – ikke commit)
005 report/        – Rapportkapitler
011 fase 1 - proposal/
012 fase 2 - plan/ – Prosjektstyringsplan, WBS, milepæler, status
013 fase 3 - review/
014 fase 4 - report/
```

## Viktige filer

| Fil | Formål |
|-----|--------|
| `012 fase 2 - plan/prosjektstyringsplan.md` | Planbaseline – omfang, risiko, ressurser |
| `012 fase 2 - plan/wbs.json` | Arbeidsnedbrytningsstruktur |
| `012 fase 2 - plan/milestones.json` | Milepælsplan |
| `012 fase 2 - plan/status.md` | Løpende prosjektstatus med checkbokser |
| `005 report/Prosjektrapport.md` | Selve rapporten – skrives her |
| `000 templates/` | Høgskolens maler (les, ikke rediger) |

## Regler

- **Aldri commit eller push** uten at Tord eksplisitt ber om det
- **Aldri rediger filer i `000 templates/`**
- **Aldri legg til datafiler** fra `004 data/` i git – de er konfidensielle (Motive Offshore)
- Ikke opprett nye filer med mindre det er nødvendig – foretrekk å redigere eksisterende
- Ikke legg til kommentarer, docstrings eller forklaringer i kode med mindre det er bedt om

## Rapportstruktur

Rapporten skrives i `005 report/Prosjektrapport.md`.

| Kapittel | Tittel | Merknad |
|----------|--------|---------|
| Forside | Egenerklæring, personvern, publiseringsavtale | |
| – | Sammendrag (norsk) | |
| – | Abstract (engelsk) | |
| 1.0 | Innledning | Skrives **sist** |
| 1.1 | Problemstilling | |
| 1.2 | Delproblemer | Valgfri |
| 1.3 | Avgrensinger | |
| 1.4 | Antagelser | |
| 2.0 | Litteratur | |
| 3.0 | Teori | |
| 4.0 | Casebeskrivelse | Motive Offshore |
| 5.0 | Metode og data | |
| 5.1 | Metode | |
| 5.2 | Data | |
| 6.0 | Modellering | gap-deteksjonslogikk + varslingslogikk |
| 7.0 | Analyse | EDA, uke-til-uke-analyse, gap-analyse |
| 8.0 | Resultat | Kun presentasjon, ingen diskusjon |
| 9.0 | Diskusjon | |
| 10.0 | Konklusjon | |
| 11.0 | Bibliografi | APA 7 |
| 12.0 | Vedlegg | KI-erklæring, kravmatrise, kode |

## Rapportskriving

- Skriv innhold fortløpende i rapporten underveis i prosjektet, ikke vent til alt analysearbeid er ferdig.
- I `Prosjektrapport.md` skal inline matematikk skrives med `$...$`, ikke `\(...\)`, siden Markdown-visningen støtter dollar-notasjon best.
- Skill tydelig mellom:
  - `Casebeskrivelse`: beskriver Motive Offshore, dataøkosystemet og historiske fakta.
  - `Metode og data`: beskriver metodevalg, datagrunnlag, datakvalitet og CSV-eksportoppsett.
  - `Analyse/Resultat`: brukes først når faktisk gap-analyse og valideringsresultater er gjort.
- Beskrivende figurer for historisk supply/demand-utvikling skal inn i casekapitlet, ikke i analysekapitlet.
- Datatabeller som dokumenterer datasettet skal inn i datakapitlet.
- Når noe bare er en antagelse, skriv det eksplisitt som antagelse og ikke som verifisert fakta.

## Figurer i rapporten

- Bruk HTML for bilder i `Prosjektrapport.md`, ikke vanlig Markdown-bildeformat, når bredde og sentrering skal styres.
- Standard for rapportfigurer i dette prosjektet:
  - sentrert figur
  - `width="80%"`
  - kort figurtekst under figuren
- Figurtekst skal være sentrert, liten skrift og kursiv.
- Foretrukket mønster:

```html
<div align="center">
  <img src="..." alt="..." width="80%">
  <p align="center"><small><i>Figur X Kort figurtekst.</i></small></p>
</div>
```

## Tabeller i rapporten

- Tabeller kan limes inn direkte som Markdown-tabeller når de er små og lesbare.
- Tabeller skal ha en kort introduksjonssetning i brødteksten før de settes inn.
- Bruk tabellnummer i teksten, for eksempel `Tabell 4.1`.
- Tabeller som trenger tabelltekst kan få samme stil som figurtekster: sentrert, liten skrift og kursiv under tabellen.

## Kode og analyse

- Analysearbeid i `006 analysis/` organiseres etter aktiviteter i prosjektplanen (3.1, 3.2, 3.3 osv.).
- Ett felles `uv`-prosjekt brukes for hele `006 analysis/`.
- Skript, figurer og resultatfiler skal ligge i samme aktivitetsmappe.
- Filnavn i analyseartefakter skal være korte, ryddige og prefikset med `fig_` for figurer og `tab_` for tabeller.

## Praktiske preferanser

- Når noe er fullført i prosjektet, oppdater både planfiler (`milestones.json`, `wbs.json`) og `status.md`.
- Nye arbeidssteg bør legges inn i planen før aktiviteten lukkes.

## Rapportsjekkliste

Bruk denne som en siste kontroll før kapitler ferdigstilles.

- [ ] **Innledning** – kort (1–2 s.), aktualiserer tema, problemstilling er «hvordan»/«hvorfor», avgrensinger er begrunnet. Skrives sist.
- [ ] **Litteratur** – kun bidrag siste 5 år, alle påstander har referanse, ingen synsing.
- [ ] **Teori** – plasserer problemstillingen i fagfeltet, danner grunnlag for metodevalg.
- [ ] **Casebeskrivelse** – beskriver Motive Offshore, dataøkosystemet og 75 %-terskelen. Kun relevant info.
- [ ] **Metode og data** – så nøyaktig at prosessen kan gjentas. KI-bruk dokumentert (kap. 8).
- [ ] **Modellering** – gap-deteksjonslogikk og varslingslogikk forklart og én-til-én med problemstillingen.
- [ ] **Analyse** – EDA, uke-til-uke-sammenligning og gap-analyse dokumentert.
- [ ] **Resultat** – kun presentasjon, ingen diskusjon. Tekst før hver tabell/figur.
- [ ] **Diskusjon** – funn kommentert mot litteratur og problemstilling, begrensninger nevnt.
- [ ] **Konklusjon** – gjentar problemstillingen, oppsummerer hovedfunn, foreslår videre forskning.
- [ ] **Bibliografi** – APA 7 gjennomgående, alle siterte kilder med, KI-referanser inkludert.
- [ ] **Vedlegg** – signert KI-erklæring (obligatorisk), taushetserklæring, kravmatrise.
- [ ] **Sluttsjekk** – begge har lest gjennom, ingen påstander uten referanse, figurer reproduserbare.

## Konvensjoner

- Dokumentasjon skrives i **Markdown**
- Strukturerte data lagres som **JSON**
- Filnavn bruker **små bokstaver og underscore** (f.eks. `status.md`, `wbs.json`)
- Referanser følger **APA 7**-format

## Kontekst som alltid er relevant

- Data hentes fra **Power BI** (aggregert fra Salesforce og Asset Voice)
- Kun prosjekter med **≥75 % vinnersannsynlighet** inkluderes i etterspørselsanalysen
- Kun **Tier 2-utstyrskategorier** inngår i modellen
- Modellen varsler om gap – foreslår ikke løsninger
- Systemet bruker **regelbasert gap-deteksjon** (ikke SARIMA) – uke-til-uke-sammenligning av supply/demand
