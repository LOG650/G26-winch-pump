# 3.2 EDA – Funn og implikasjoner for modelleringen

Eksplorativ dataanalyse av baseline-snapshot **2026-05-07** (Motive Norway:
816 celler over 24 Tier 2-utstyrsenheter × 34 uker). Genererte figurer og
tabeller ligger i samme mappe som dette dokumentet.

> **Merknad om scope.** Tidligere EDA brukte et utgått worldwide-snapshot
> (2026-04-30, 80 assets × 36 uker). Da vi snevret inn til ett verksted
> (Motive Norway / Stavanger), endret datagrunnlaget seg fundamentalt – fra
> en flåte med kronisk underdimensjonering til en lokal flåte som stort sett
> har overdekning. Hovedfunnene under reflekterer den nye, mindre, lokale
> scopen.

## Overordnet bilde

- **58,7 % av cellene har positiv gap** (overdekning)
- **31,9 %** er nøyaktig 0 (balanse eller mikro-gap skjult av avrunding)
- **9,4 %** har negativ gap (kapasitetsgap)
- **Median gap-verdi: +1**, P5: −1

Distribusjonen (Figur 1) er sentrert rundt 0 med en kort negativ hale ned
til −2 og en lang positiv hale opp til +7. **Motive Norway-flåten er stort
sett tilstrekkelig dimensjonert** for det som ligger på 75 %+
vinnersannsynlighet i kontraktene som er synlige nå.

## Ingen strukturelle gaps

Et viktig funn: **null utstyrsenheter har negativ gap i alle 34 uker**
(`tab_strukturelle_gaps.md` er tom). Alle 24 leaf-rader har minst én uke
med gap ≥ 0.

Dette står i sterk kontrast til den tidligere worldwide-analysen, der 8
assets hadde konstant negativ gap. På Motive Norway-nivået finnes det
**ingen kapasitetsstrukturelle underskudd** – alle observerte gaps er
midlertidige.

**Implikasjon for modellering:** Suppression-regelen vi planla for
"structural deficit" (varselsstopp for assets som alltid er negative)
har ingen kandidater i dette datasettet. Den kan likevel beholdes i
modellen som forebyggende mekanisme – den vil bare være "stille" på
nåværende baseline.

## Gappene er kontraktsdrevne

Figur `fig_total_gap_per_uke.png` viser at den totale gap-verdien per uke
**vokser fra ca +10 i mai til +34 mot slutten av 2026** – det vil si,
flåten ser mer og mer overdimensjonert ut jo lenger ut i tid vi ser.

Dette er ikke fordi flåten faktisk er overdimensjonert i fremtiden – det
er den klassiske **blindsone-effekten**: kontrakter som vil bumpes til
75 % senere er ikke synlige ennå. Negative gaps konsentreres i de første
~14 ukene fordi det er der kontraktene allerede har passert
sannsynlighetsterskelen.

**Implikasjon:** Hovedmekanismen i varslingssystemet må være
**uke-til-uke-deltadeteksjon**, ikke statisk snapshot-analyse. Det er når
nye kontrakter dukker opp eller eksisterende forverres mellom snapshots
at signalet er informativt.

## Topp 10 utstyrsenheter med størst kumulativt underskudd

Verstinglisten (`tab_topp10_verste_assets.md`) viser at de "verste" gappene
i ny scope er **vesentlig mindre** enn i den tidligere worldwide-analysen:

| Asset | Kumulativt gap (34 uker) |
|---|---|
| Hydraulic - Wide \| 35Te Wide Drum Winch | −19 |
| Horizontal - 2 track - 15Te Horizontal Tensioner | −16 |
| − 500Te RDS | −14 |
| − 150Te RDS | −9 |
| Electric - 158KW Electric HPU | −9 |
| Horizontal - 4 track - 50Te Tensioner | −9 |
| − 2Te Linear Cable Engine | −6 |
| Diesel - 63kW Diesel HPU Zone II | 0 |
| Electric - 11kW Electric HPU | +12 |
| Electric - 90KW Electric HPU | +13 |

De tre nederste har positivt kumulativt gap – de havner i "topp 10" fordi
det er **bare 24 assets totalt** i datasettet, og det ikke finnes flere
med rent negativt bidrag. Snitt-gappet for verste asset (35Te Wide Drum)
er −0,56 per uke; for 15Te Tensioner −0,47. Til sammenligning hadde
15Te Tensioner i worldwide-analysen et snittgap på −8,31.

## Zero-gap assets

Kun **én** asset har gap-verdi 0 i alle 34 uker (`tab_zero_gap_assets.md`):

- **Diesel - 63kW Diesel HPU Zone II** – alltid 0, alltid lilla. Lilla
  fargen indikerer at det underliggende gapet er svakt negativt (skjult
  av avrunding til heltall), men ikke nok til å bli rapportert som
  konkret underskudd.

Dette er en kandidat for **eksklusjon fra varslingslogikken** – ingen
variasjon over horisonten betyr at deltadetektoren aldri kan utløse et
informativt varsel her.

## Severity-bandet – fanget men ikke analysert

Med snapshot 2 (2026-05-14) er `severity_band` (Power BI-fargen per celle)
nå med i skjemaet og retrofittet på baseline. Foreløpige observasjoner:

- Mange "0"-celler bærer lilla farge – Power BI viser at underliggende
  gap er svakt negativt, men avrundes til 0. Dette gjelder spesielt for
  små HPU-er (Diesel Zone II, 11kW, 30kW i mai-juni, 55kW i mai-juli).
- Ingen celler er røde eller gule i baseline-perioden – det binære skillet
  mellom grønn (overdekning) og lilla/svart (underdekning) er det
  operasjonelt meningsfulle.
- `gen_baseline_csv.py` kjører en farge-konsistens-sjekk som flagger
  umulige kombinasjoner (positiv gap_value med lilla/svart farge eller
  motsatt). Den passerer for begge snapshots.

**Implikasjon for kapittel 6 Modellering:** Severity-bandet kan brukes
til å klassifisere alvorlighet (lilla = liten dip, svart = strukturelt
underskudd) uavhengig av selve gap-verdien. Dette gir et mer presist
signal enn å bare bruke gap-verdien.

## HPUS dominerer flåten – fortsatt

11 av 24 leaf-rader (45,8 %) er HPUS (hydrauliske kraftaggregater). Det
totale HPUS-bidraget til ukentlig gap (Figur `fig_per_asset_type_uker.png`)
er likevel moderat siden mange av HPUS-radene er stabile null-gap-typer.
158KW er det største enkeltbidraget med −1 i mai-juli, deretter 0.

**Implikasjon for varslingsmottakere (3.4):** Hvis vi velger modell A
(per utstyrskategori), vil HPUS-koordinatoren fortsatt motta flest
varsler – men volumet vil være lavt sammenlignet med worldwide-bildet.

## Konkrete implikasjoner for kapittel 6 Modellering

| Designvalg | EDA-grunnlag |
|---|---|
| Hovedmekanisme = uke-til-uke-delta | Strukturelle gaps finnes ikke; blindsone-effekten dominerer |
| Severity-klassifisering via `severity_band` | Power BI-fargen koder prosent-gap, ikke gap_value alene |
| Suppression for strukturelle gaps | Beholdes som forebygging, ingen kandidater i nåværende baseline |
| Eksklusjonsliste for inaktive assets | 1 kandidat (Diesel 63kW Zone II) – verifiseres med Motive |
| Tier 2-granularitet | 24 leaf-rader er håndterbart for manuell verifikasjon |
| Avrundingstoleranse ±2 i sumsjekk | Bekreftet: Power BI Totalt aggregerer fra desimal-grunndata |

## Begrensninger og åpne spørsmål

- **Ny baseline er mye mindre enn forventet.** Hele EDA-narrativet i
  tidligere utkast (basert på worldwide-snapshot) er ikke overførbart.
  Lokal scope er det riktige nivået for å vurdere Motive Norways flåte.
- **Severity-fargene er manuelt avlest fra PNG-bilder.** For enkelte
  celler (`Electric - 158KW Electric HPU` baseline-uker 0-8) er fargen
  satt til `black` for konsistens, men visuell avlesning var usikker.
  Bør verifiseres i Power BI ved neste anledning.
- **Sammenligning med snapshot 2 (2026-05-14) er nå mulig** og er
  hovedinngangen til 3.3 gap-deteksjon. Forskjellene mellom snapshots
  vil avsløre om systemet kan fange opp reelle kontraktsendringer.
- **EDA bruker ikke `severity_band`-feltet ennå.** Hvis kapittel 7 skal
  ha figur som viser fargefordeling per asset type eller per uke, må
  `eda_main.py` utvides.
