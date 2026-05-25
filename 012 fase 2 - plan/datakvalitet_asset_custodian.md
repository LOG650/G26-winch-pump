# Datakvalitet: Asset Custodian vs. fysisk lokasjon

**Status:** Avdekket 2026-05-24 etter avklaring fra David
**Type:** Tolkningsmessig nyanse i datagrunnlaget
**Beslutning:** Avventer – styres av Tord, ingen endring gjøres uten beskjed
**Påvirker:** Kap 7.4 (Tabell 7.2), 7.5 (Tabell 7.3), 7.6, 8.x, SMTP-demo-figurer

## Situasjonen

Power BI-filteret som brukes i datafangst (`Asset Custodian = Motive AS`, `Project Owner Demand = Motive AS`, `Region = Motive Norway`) treffer prosjekter der **Motive Norway står som organisatorisk eier**, ikke nødvendigvis prosjekter der utstyret faktisk befinner seg fysisk i Motive Norway.

David har avklart at de syv enhetene i Tabell 7.2 / 7.3 alle har samme historikk:

> "Etter de blir sendt til en annen lokasjon har de bare blitt værende, men Motive Norge står som 'eier', så de ligger fortsatt inne. Men egentlig har me ingen prosjekter med disse. Alle de utstyrene med stort gap, som eg sendte screenshot av, e utstyr me ikkje har, men me står som eier av prosjektet, altså Motive Norge har kunden som ska ha feks 500t RDS, men det blir mobilisert og sendt fra en annen lokasjon."

Det betyr at de syv enhetene (35Te Wide Drum Winch, 15Te Horizontal Tensioner, 500Te RDS, 50Te Tensioner 4-track, 150Te RDS, 158KW HPU, 2Te Linear Cable Engine) er utstyr Motive Norway **ikke fysisk eier**, men dekkes opp av andre Motive-lokasjoner i konsernet.

## Konsekvenser for analysen som står i rapporten

| Område | Hvordan det påvirkes |
|---|---|
| Tabell 7.2 (7.4) – «De mest utsatte utstyrsenhetene» | Alle 7 enheter er teknisk «utsatte» fra Power BI-perspektiv, men ikke fra et fysisk-kapasitet-perspektiv |
| Tabell 7.3 (7.5) – «Front-lastet underskudd» | Samme 7 enheter |
| Kap 7.6 / Tabell 7.5 – 7 NYTT_GAP i delta-par 1 | Sannsynligvis alle på disse enhetene |
| Kap 7.6.1 / Tabell 7.7 – 4 NYTT_GAP + 8 LØST i delta-par 2 | ~12 av 19 varsler i delta-par 2 gjelder disse enhetene |
| Tabell 8.5c (tråd-livssyklus) | De 5 lukkede + 5 påminnelser er primært disse enhetene |
| SMTP-demo (Figur 8.1–8.6) | Innholdet i 4 av 5 digester gjelder disse enhetene |

## Alternativ A: Filtrere bort de syv enhetene fra datagrunnlaget

**Hva det innebærer:**
- Justere transkriberings-scriptene for snap1, snap2, snap3 så disse 7 enhetene ekskluderes fra leaf-radene
- Re-kjøre `gap_detection.py` og `gap_alerting.py` for begge delta-par
- Regenerere alle figurer: `fig_endringer_per_uke_delta1.png`, `_delta2.png`, `fig_endringer_per_asset_type_delta1.png`, `_delta2.png`, `fig_endringstype_fase_delta1/2.png`
- Ta ny SMTP-demo (alle 5 digester blir andre, eller kanskje ingen i det hele tatt)
- Oppdatere all tekst og tall i: Tabell 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.1, 8.1b, 8.2, 8.3, 8.3b, 8.4, 8.5, 8.5b, 8.5c
- Oppdatere brødtekst i kap 7.4, 7.5, 7.6, 7.6.1, 7.6.2, 8.1, 8.2, 8.5, 8.5.1, 9.1, 9.2, 9.5

**Estimert arbeidstid:** 6–8 timer

**Risiko:**
- Sannsynligvis null NYTT_GAP og null tråder i analyse – modellen er fortsatt funksjonelt korrekt, men hovedargumentet i 9.5 («5 av 10 tråder lukkes automatisk i andre syklus») kollapser fordi det ikke lenger finnes noen tråder å lukke
- Severity-regelens 3 «skjulte» varsler i delta-par 1 forsvinner trolig også
- SMTP-demoen mister sitt empiriske innhold
- Modellens validering blir avhengig kun av syntetiske tester (Tabell 8.6)

**Konsekvens for rapporten:** Modellbeskrivelsen og teorien står seg, men det empiriske bidraget i kap 7–8 blir betydelig svakere – det ville være en demonstrasjon av at modellen ikke produserer falske varsler, men ingen demonstrasjon av at den fanger reelle endringer.

## Alternativ B: Beholde data som det er, dokumentere som metodologisk innsikt

**Hva det innebærer:**
- Tilføye 1 setning i kap 5.2.2 om at filteret `Asset Custodian = Motive AS` reflekterer organisatorisk eierskap, ikke nødvendigvis fysisk lokasjon
- Tilføye 1 avsnitt i kap 9.4 (eller 9.3) som drøfter dette som datakvalitetsavvik mellom kilden og fysisk realitet, og hvordan eksklusjonslisten i 6.6 er det riktige håndteringsverktøyet
- Tilføye 1 setning i kap 9.5 om at koordinator i produksjon vil legge disse 7 enhetene i eksklusjonslisten basert på lokal kunnskap
- Eventuelt en kort merknad i kap 7.4 eller 7.5

**Estimert arbeidstid:** 30–45 minutter

**Argument for B:**
- Modellen responderer på det Power BI viser, som er det selgere/koordinator faktisk ser i dashbordet. Avviket mellom data og fysisk realitet er et **kildekvalitetsproblem**, ikke et modellproblem
- Avdekkingen er en styrke å demonstrere, ikke en svakhet å skjule: nettopp denne typen avvik er grunnen til at eksklusjonslisten og menneske-i-løkka-modellen er designet inn
- Tidsbruk er minimal og risikoen for å rasere rapportens empiriske bidrag er null
- Kan diskuteres muntlig som tegn på at gruppen har forstått datagrunnlaget i dybden

**Argument mot B:**
- Rapporten kan virke å overdrive modellens funn hvis leseren ikke fanger nyansen om at varslene gjelder utstyr Motive Norway ikke fysisk eier
- En streng leser kan argumentere for at den «riktige» metodikken var å filtrere på fysisk lokasjon fra start

## Anbefaling

**Alternativ B**, med følgende konkrete tilføyinger når beslutningen tas:

1. **Kap 5.2.2** – ny setning etter filterlisten:
   > «Filterkombinasjonen treffer prosjekter der Motive AS står som organisatorisk eier i Salesforce. Dette samsvarer ikke alltid med fysisk lokasjon: enkelte utstyrsenheter som vises som tilgjengelige under Motive Norway-filteret er fysisk plassert ved andre Motive-verksteder og mobiliseres derfra ved leveranse.»

2. **Kap 9.4** – nytt avsnitt etter avrundingsstøy-diskusjonen:
   > «Et beslektet datakvalitetsfunn er at filteret `Asset Custodian = Motive AS` treffer organisatorisk eierskap snarere enn fysisk lokasjon (jf. 5.2.2). De syv enhetene i Tabell 7.3 er alle prosjekter der Motive Norway står som kunde-eier, men der utstyret faktisk mobiliseres fra andre Motive-verksteder. Det betyr at det dynamiske gapsignalet i mange av delta-par-varslene reflekterer en kontraktuell forpliktelse uten en korresponderende fysisk knapphet i Motive Norway. Datatekniks sett er varslene korrekte – de speiler det selgere og koordinatorer ser i Power BI – men koordinator vil i produksjon legge disse enhetene i eksklusjonslisten (kap 6.6) for å unngå unødvendig oppfølging av kapasitet som dekkes andre steder.»

3. **Kap 9.5** – tilføyelse til avsnittet om hva som må falle på plass:
   > «Suppression-listen … bør gjennomgås manuelt av en flåtekoordinator første gang systemet kjøres i produksjon, slik at kjente strukturelle underdimensjoneringer (jf. 7.5) **og enheter som dekkes fra andre verksteder (jf. 9.4)** markeres opp før K=4-kriteriet rekker å samle nok historikk.»

## Når beslutningen tas

Tord vurderer dette opp mot total tidsbruk og kvalitetsmål. Hvis Alternativ B velges, gjøres tilføyingene over på 30–45 minutter. Hvis Alternativ A velges, må det settes av en hel kveldsøkt (6–8 timer) og prosjektplanen for kortetiltak / kap 10 / sammendrag må re-prioriteres.

Ingenting gjøres før Tord gir beskjed.
