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
- Bruk faglige termer der det er naturlig (supply/demand, SARIMA, kapasitetsgap osv.)
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
| `005 report/rapport.md` | Selve rapporten – skrives her |
| `005 report/rapport_mal.md` | Rapportmal med kapitelstruktur og veiledning (les, ikke rediger) |
| `000 templates/` | Høgskolens maler (les, ikke rediger) |

## Regler

- **Aldri commit eller push** uten at Tord eksplisitt ber om det
- **Aldri rediger filer i `000 templates/`**
- **Aldri legg til datafiler** fra `004 data/` i git – de er konfidensielle (Motive Offshore)
- Ikke opprett nye filer med mindre det er nødvendig – foretrekk å redigere eksisterende
- Ikke legg til kommentarer, docstrings eller forklaringer i kode med mindre det er bedt om

## Rapportstruktur

Rapporten skrives i `005 report/rapport.md`. Malen med veiledning ligger i `005 report/rapport_mal.md` – les den, men ikke rediger den.

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
| 6.0 | Modellering | SARIMA + varslingslogikk |
| 7.0 | Analyse | EDA, Box-Jenkins, gap-analyse |
| 8.0 | Resultat | Kun presentasjon, ingen diskusjon |
| 9.0 | Diskusjon | |
| 10.0 | Konklusjon | |
| 11.0 | Bibliografi | APA 7 |
| 12.0 | Vedlegg | KI-erklæring, kravmatrise, kode |

## Rapportsjekkliste

Bruk denne som en siste kontroll før kapitler ferdigstilles.

- [ ] **Innledning** – kort (1–2 s.), aktualiserer tema, problemstilling er «hvordan»/«hvorfor», avgrensinger er begrunnet. Skrives sist.
- [ ] **Litteratur** – kun bidrag siste 5 år, alle påstander har referanse, ingen synsing.
- [ ] **Teori** – plasserer problemstillingen i fagfeltet, danner grunnlag for metodevalg.
- [ ] **Casebeskrivelse** – beskriver Motive Offshore, dataøkosystemet og 75 %-terskelen. Kun relevant info.
- [ ] **Metode og data** – så nøyaktig at prosessen kan gjentas. KI-bruk dokumentert (kap. 8).
- [ ] **Modellering** – SARIMA matematisk definert, varslingslogikk forklart, én-til-én med problemstillingen.
- [ ] **Analyse** – EDA, Box-Jenkins, residualanalyse og sensitivitetsanalyse dokumentert.
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
- Prosjektet bruker **SARIMA/Box-Jenkins** for tidsseriemodellering
