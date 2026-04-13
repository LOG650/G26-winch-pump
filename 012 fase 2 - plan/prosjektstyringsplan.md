# Prosjektstyringsplan

**Prosjekt:** KI-basert kapasitetsvarsling for Motive Offshore
**Dato:** 2026-03-09
**Utarbeidet av:** David Johan Lunde og Tord Haakon Johnsen Hovden
**Autorisert av:** Faglærer LOG650

---

## Innhold

1. [Sammendrag](#sammendrag)
2. [Behov](#behov)
3. [Sponsor](#sponsor)
4. [Kunde](#kunde)
5. [Forretningscase](#forretningscase)
6. [Omfang](#omfang)
7. [Fremdrift](#fremdrift)
8. [Budsjett](#budsjett)
9. [Risiko](#risiko)
10. [Interessenter](#interessenter)
11. [Ressurser](#ressurser)
12. [Kommunikasjon](#kommunikasjon)
13. [Kvalitet](#kvalitet)
14. [Endringskontrollprosess](#endringskontrollprosess)

---

## Sammendrag

Dette dokumentet utgjør prosjektstyringsplanen for LOG650-prosjektet om KI-basert kapasitetsvarsling for Motive Offshore. Det dokumenterer planbaselines for omfang, fremdrift, budsjett og risiko, og gir tilleggsinformasjon for å støtte prosjektteamet i vellykket gjennomføring.

Prosjektet støtter følgende mål: automatisere overvåkning av kapasitetsgap i Motive Offshores utleiefloåte ved hjelp av kunstig intelligens, slik at manuelle ressurser frigjøres og fremtidige gap oppdages 3–6 måneder i forveien.

Dette er et levende dokument og skal oppdateres av prosjektgruppen ved behov gjennom prosjektets løpetid.

---

## Behov

Motive Offshore benytter i dag Power BI som visualiseringslag over data fra Salesforce (kommersiell etterspørsel) og Asset Voice (operasjonell flåtestatus). Systemet gir gode deskriptive oversikter, men krever daglig manuell overvåkning for å oppdage fremtidige kapasitetsgap. Ansatte kan relativt enkelt følge opp situasjonen de nærmeste ukene, men å identifisere gap 3–6 måneder frem i tid krever betydelig manuell innsats.

Prosjektet svarer på dette behovet ved å utvikle en KI-modell som kontinuerlig analyserer data og automatisk sender varsel når fremtidige kapasitetsgap identifiseres – uten at brukeren trenger å sjekke systemet selv.

---

## Sponsor

Faglærer ved LOG650 er sponsor for prosjektet, ansvarlig for faglig rammeverk og godkjenning av prosjektplanen. Motive AS (del av Motive Offshore Group), Stavanger, er samarbeidspartner og bidrar med reelle data.

---

## Kunde

Motive Offshore representerer sluttbrukerne av løsningen. Prosjektets nøkkelbrukere er kapasitets- og salgsansvarlige som i dag manuelt overvåker kapasitetssituasjonen i Power BI.

---

## Forretningscase

### Alternativer

Følgende alternativer ble vurdert:

- **Status quo:** Fortsette med manuell daglig overvåkning i Power BI. Forkastet fordi det er ressurskrevende og gir liten fremtidshorisont.
- **KI-modell med automatisk varsling (valgt alternativ):** Bygge en modell som analyserer data fra Power BI og sender automatiske e-postvarsler ved identifiserte gap 3–6 måneder frem. God balanse mellom nytte og gjennomførbarhet innen prosjektets rammer.
- **Full systemintegrasjon mot live API:** Direkte kobling mot Salesforce- og Asset Voice-API for sanntidsanalyse. Forkastet – for teknisk krevende og utenfor prosjektets omfang.

### Forutsetninger

- Tilgang til reelle data fra Motive Offshore via Power BI opprettholdes gjennom hele prosjektet.
- Data fra Power BI er tilstrekkelig aggregert og strukturert for modellbruk.
- Vinnersannsynlighet på 75 % er en representativ terskel for inkludering i etterspørselsanalysen.

### Gevinster

- Redusert manuell overvåkningstid for kapasitetsansvarlige
- Tidligere identifikasjon av kapasitetsgap gir lengre ledetid og større handlingsrom
- Bedre grunnlag for ressursplanlegging og forhandlinger

### Kostnader

Prosjektet er et studentprosjekt uten direkte monetære kostnader. Ressurskostnader består av tid brukt av de to gruppemedlemmene, estimert til ca. 200–250 arbeidstimer totalt over semesteret.

### Analyse

Det valgte alternativet gir en klar nyttegevinst i form av redusert manuell innsats og bedre fremtidssikt, uten vesentlige kostnader utover studentenes arbeidstid. Prosjektet er derfor godt begrunnet.

---

## Omfang

### Mål

Prosjektmålet er å utvikle en KI-modell som automatisk identifiserer og varsler om fremtidige kapasitetsgap i Motive Offshores utleiefloåte 3–6 måneder frem i tid, basert på data hentet fra Power BI.

**Forutsetninger på prosjektnivå:**
- Data fra Power BI er tilgjengelig og oppdatert
- Motive Offshore bidrar med domenekompetanse ved behov
- Prosjektet gjennomføres innenfor rammene av emnet LOG650

**Begrensninger på prosjektnivå:**
- Kun prosjekter med vinnersannsynlighet ≥75 % inkluderes
- Kun Tier 2-utstyrskategorier inngår i modellen
- Systemet varsler om gap, men foreslår ikke løsninger eller alternative ressurser
- Direkte teknisk integrasjon mot live Salesforce- og Asset Voice-API er ikke en del av prosjektet

### Krav

Kravene er identifisert innen funksjonalitet, dataintegrasjon og varsling:

| ID | Krav | Eier |
|----|------|------|
| K1 | Modellen skal analysere etterspørselsdata fra Salesforce (via Power BI) med ≥75 % vinnersannsynlighet | Gruppen |
| K2 | Modellen skal analysere tilbudsdata fra Asset Voice (via Power BI) per Tier 2-utstyrskategori | Gruppen |
| K3 | Modellen skal identifisere kapasitetsgap 3–6 måneder frem i tid | Gruppen |
| K4 | Systemet skal automatisk sende e-postvarsel ved identifisert kapasitetsgap | Gruppen |
| K5 | Varselet skal inneholde utstyrskategori, tidsperiode og gapstørrelse | Gruppen |
| K6 | Modellen skal valideres mot historiske kapasitetsgap fra Power BI | Gruppen |

### Løsning

Løsningen som utvikles er en KI-modell som:
1. Henter data fra Power BI (aggregert fra Salesforce og Asset Voice)
2. Beregner forventet etterspørsel per utstyrskategori basert på prosjekter med ≥75 % vinnersannsynlighet
3. Sammenligner med tilgjengelig flåtekapasitet per uke
4. Identifiserer gap i horisonten 3–6 måneder frem
5. Sender automatisk e-postvarsel når gap oppdages

### Arbeidsnedbrytningsstruktur (WBS)

| WBS-ID | Leveranse | Eier |
|--------|-----------|------|
| 1.0 | Prosjektledelse og planlegging | Begge |
| 1.1 | Prosjektstyringsplan | Begge |
| 2.0 | Datainnhenting og forberedelse | Begge |
| 2.1 | Datauttrekk fra Power BI | Begge |
| 2.2 | Dataklargjøring og strukturering | Begge |
| 3.0 | Modellutvikling | Begge |
| 3.1 | Etterspørselsmodell (Salesforce-data) | Begge |
| 3.2 | Tilbudsmodell (Asset Voice-data) | Begge |
| 3.3 | Gap-deteksjonslogikk | Begge |
| 4.0 | Varslingssystem | Begge |
| 4.1 | E-postvarsling ved gap | Begge |
| 5.0 | Validering og testing | Begge |
| 5.1 | Validering mot historiske kapasitetsgap | Begge |
| 5.2 | Brukertesting med Motive Offshore | Begge |
| 6.0 | Rapportering og presentasjon | Begge |
| 6.1 | Skriftlig rapport | Begge |
| 6.2 | Presentasjon for sensor og faglærer | Begge |

---

## Fremdrift

### Milepæler

| Milepæl | Planlagt dato |
|---------|--------------|
| Prosjektstyringsplan godkjent | 2026-03-20 |
| Datainnhenting fullført | 2026-03-31 |
| Etterspørsels- og tilbudsmodell ferdig | 2026-04-15 |
| Gap-deteksjon og varsling implementert | 2026-04-30 |
| Validering fullført | 2026-05-10 |
| Skriftlig rapport levert | 2026-05-20 |
| Presentasjon gjennomført | 2026-05-28 |

### Gantt-oversikt

```
Mars 2026:      [Planlegging & datainnhenting         ]
April 2026:              [Modellutvikling & varsling   ]
Mai 2026:                              [Validering & rapport & presentasjon]
```

### Kritisk linje

Datainnhenting → Modellutvikling → Validering → Rapport → Presentasjon

Forsinkelse i datainnhenting vil direkte påvirke alle påfølgende leveranser og sluttdatoen.

---

## Budsjett

Prosjektet er et studentprosjekt uten direkte monetære kostnader. Ressursene er begrenset til studentenes arbeidstid.

| Ressurstype | Estimert innsats |
|-------------|-----------------|
| David Johan Lunde | ~125 timer |
| Tord Haakon Johnsen Hovden | ~125 timer |
| **Totalt** | **~250 timer** |

---

## Risiko

### Prosess for risikostyring

Risikoregisteret er utarbeidet av prosjektgruppen. Risikoer er identifisert ved gjennomgang av prosjektets avhengigheter og kritiske aktiviteter. Risikoregisteret gjennomgås ved hvert ukentlige arbeidsmøte.

### Risikoregister

| ID | Risiko | Sannsynlighet | Konsekvens | Tiltak | Beredskap | Eier |
|----|--------|--------------|------------|--------|-----------|------|
| R1 | Begrenset datatilgang fra Motive Offshore | Middels | Høy | Etablere tidlig kontakt og avklare datatilgang i fase 1 | Bruke anonymiserte eller syntetiske data ved behov | Begge |
| R2 | Data fra Power BI er ufullstendig eller dårlig strukturert | Middels | Høy | Kartlegge datastruktur tidlig og avklare med Motive | Manuell datarensing og tilpasning | Begge |
| R3 | KI-modellen gir for mange falske positiver | Middels | Middels | Terskeljustering basert på historiske data | Presentere resultater som indikatorer, ikke absolutter | Begge |
| R4 | Tidsmangel grunnet andre emner og forpliktelser | Middels | Middels | Ukentlige arbeidsmøter og klar oppgavefordeling | Prioritere kjernekomponenter (gap-deteksjon) fremfor nice-to-have | Begge |
| R5 | Vinnersannsynlighet på 75 % gir urepresentativt datagrunnlag | Lav | Middels | Validere terskel mot historiske gap | Justere terskel dersom validering tilsier det | Begge |

---

## Interessenter

| Interessent | Rolle | Hovedbehov | Prioritering | Kommunikasjon |
|------------|-------|-----------|-------------|---------------|
| Faglærer LOG650 | Sponsor / sensor | Akademisk kvalitet, metodekrav | Omfang, rapport | Innleveringer og presentasjon |
| Motive Offshore (kontaktperson) | Kunde / datapartner | Praktisk nytte, datakvalitet | Løsningens anvendbarhet | E-post og møter ved behov |
| David Johan Lunde | Prosjektmedlem | Faglig læring, god karakter | Fremdrift, kvalitet | Ukentlige arbeidsmøter |
| Tord Haakon Johnsen Hovden | Prosjektmedlem | Faglig læring, god karakter | Fremdrift, kvalitet | Ukentlige arbeidsmøter |

---

## Ressurser

### Prosjektteam

| Navn | Rolle | Ansvar |
|------|-------|--------|
| David Johan Lunde | Prosjektmedlem | Datainnhenting, modellutvikling, rapportering |
| Tord Haakon Johnsen Hovden | Prosjektmedlem | Datainnhenting, modellutvikling, rapportering |

Begge gruppemedlemmer har delt ansvar for alle leveranser. Oppgaver fordeles løpende basert på kompetanse og tilgjengelighet.

### Kritiske ressurser

- **Datatilgang fra Motive Offshore:** Nødvendig for modellutvikling og validering. Avklares tidlig i prosjektet.
- **Power BI-eksport:** Praktisk metode for datahenting som ikke krever direkte API-integrasjon.

---

## Kommunikasjon

### Ukentlige arbeidsmøter

- **Formål:** Koordinere arbeid, følge opp fremdrift og håndtere risikoer og saker
- **Deltakere:** David Johan Lunde og Tord Haakon Johnsen Hovden
- **Frekvens:** Ukentlig, fast avtalt tidspunkt
- **Varighet:** Maks 1 time

### Kommunikasjon med Motive Offshore

- **Formål:** Datainnhenting, avklaringer, brukertesting
- **Kanal:** E-post og videomøter ved behov
- **Frekvens:** Ved behov, estimert 2–3 ganger totalt

### Innleveringer til faglærer

- **Kanal:** Læringsplattform (Canvas eller tilsvarende)
- **Frekvens:** Per fasekrav i emnet LOG650

---

## Kvalitet

De fire kvalitetsprinsippene som ligger til grunn for prosjektet:

1. **Planlegging:** Kvalitet bygges inn i arbeidet, ikke inspiseres inn i etterkant.
2. **Gevinst:** Høy metodisk kvalitet reduserer risiko for feil og gir bedre validering.
3. **Kontinuerlig forbedring:** Erfaringer fra datainnhenting og modellutvikling brukes løpende til å forbedre arbeidet.
4. **Egnet for formålet:** Alle leveranser skal faktisk kunne brukes av Motive Offshore og oppfylle emnetkravene i LOG650.

### Fagfellevurdering

Begge gruppemedlemmer gjennomgår hverandres arbeid (kode, analyse, rapport) før ferdigstillelse. Gjennomganger gjennomføres ved naturlige sjekkpunkter: etter datainnhenting, etter modellutvikling og etter rapportutkast.

### Validering

Modellen valideres mot historiske kapasitetsgap fra Power BI for å dokumentere treffsikkerhet. Valideringsresultatene dokumenteres i rapporten.

---

## Endringskontrollprosess

Etter at prosjektstyringsplanen er godkjent, skal alle vesentlige endringer i omfang, fremdrift eller tilnærming dokumenteres og avklares med faglærer dersom de påvirker leveranser eller frister.

**Prosess:**
1. Endringsbehov identifiseres og beskrives skriftlig av gruppemedlem
2. Begge gruppemedlemmer vurderer konsekvenser for omfang, fremdrift og kvalitet
3. Ved behov kontaktes faglærer for avklaring
4. Godkjent endring dokumenteres og prosjektstyringsplanen oppdateres

---

*Dokument opprettet: 2026-03-09*
*Neste revisjon: ved behov*
