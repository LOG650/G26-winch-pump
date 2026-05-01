# 3.2 EDA – Funn og implikasjoner for modelleringen

Eksplorativ dataanalyse av snapshot 2026-04-30 (Calendar: 2 880 celler over 80
utstyrsenheter × 36 uker; Overview: 152 rader over 19 kategorier × 8 måneder).
Genererte figurer og tabeller ligger i samme mappe som dette dokumentet.

## Overordnet bilde

- **58,7 % av cellene i Calendar viser et gap** (gap-verdi < 0)
- **31,5 %** er nøyaktig 0 (balanse)
- **9,8 %** har overskuddskapasitet (gap-verdi > 0)
- **Median gap-verdi: −1**, P5: −6, ekstremverdier ned til −13
- **Reservation-gap (Demand − Reservations) per måned varierer fra 73 til 324 unit-uker**

Distribusjonen er sterkt høyreskeiv (Figur 1): de fleste gap-celler er små
(−1 eller −2), men en lang hale av store underskudd opp mot −13 trekker opp
det operasjonelle inntrykket. **Modellen bør derfor klassifisere gap etter
magnitude** (liten / moderat / kritisk) og ikke bare på fortegn.

## Strukturelle vs kontraktsdrevne gap

EDA avdekker to fundamentalt forskjellige typer gap som modellen må håndtere
ulikt:

### 1. Strukturelle underskudd (8 utstyrsenheter)

Disse har **negativ gap-verdi i alle 36 uker** av snapshotet (Tabell
`tab_strukturelle_gaps.md`):

| Asset | Snitt-gap |
|-------|-----------|
| Horizontal - 2 track - 15Te Horizontal Tensioner | −8,31 |
| Electric - 54kW Electric HPU | −8,14 |
| Hydraulic - Wide\|35Te Wide Drum Winch | −4,67 |
| 400Te RDS | −4,11 |
| Horizontal - 2 track - 20Te Vertical | −1,00 |
| Hydraulic - 60Te Mooring Winch | (alltid −4) |
| Hydraulic - Crane - Palfinger | −1,03 |
| 80Te / 60Te RDS | ca −1,5 / −1 |

For disse assetene er underskuddet en **kapasitetsstrukturell tilstand** – det
finnes for få enheter i flåten til å dekke baseline-etterspørselen. Et varsel
hver eneste uke for slike assets ville være støy: selger og koordinator vet
allerede at flåten er underdimensjonert her, og varsel uten ny informasjon
øker ikke beslutningskvaliteten.

**Implikasjon for kapittel 6 Modellering:** Modellen bør ha en regel som
**suppress'er varsling for assets med konstant negativ verdi over et
sammenligningsvindu**, og i stedet flagge dem som "structural deficit" i en
egen rapport som vedlikeholdsteamet kan vurdere på langsiktig basis.

### 2. Kontraktsdrevne gap (resten)

Det er endringer her – nye gap som dukker opp og eksisterende gap som
forverres mellom snapshots – som er kjernen i varslingsbehovet. Disse kan
kun identifiseres når vi sammenligner to påfølgende snapshots, ikke fra et
enkelt snapshot. Det er derfor uke-til-uke-deltadeteksjonen som først kan
testes etter snapshot 2026-05-04.

## Kandidater for eksklusjon fra modellen (2 assets)

Følgende assets har gap-verdi 0 i alle 36 uker (`tab_zero_gap_assets.md`):

- 200Te Crane loaded Underrollers
- Crane loaded\|250Te Crane Loaded Underrollers - 250Te Crane Loaded Underrollers

Begge er i `Under rollers`-gruppen. Null variasjon over 36 uker tyder på at
disse enten ikke er aktive utleieenheter eller at de aldri kommer i
kapasitetsklem. **Implikasjon:** Modellen kan ekskludere disse fra
varslingslogikken for å redusere støy. Bekreftelse fra Motive bør innhentes
før endelig eksklusjon.

## Topp 10 utstyrsenheter med størst kumulativt underskudd

Tre Tier 1-grupper dominerer "verstingslisten" (Figur `fig_topp10_verste_assets.png`):

- **HPUS:** 4 av topp 10 (54kW, 90KW, 84KW, 37kW)
- **Tensioner:** 2 av topp 10 (15Te Horizontal, 50Te 4-track)
- **Winch:** 2 av topp 10 (35Te Wide Drum, 60Te Mooring)
- **RDS, Cable Pulling:** 1 hver

Verste enkeltasset er **Horizontal - 2 track - 15Te Horizontal Tensioner**
med kumulativt underskudd på 299 unit-uker over 36 uker (snitt −8,3 per uke).

**Implikasjon for varslingsmottakere (3.4):** Hvis vi velger modell A
(per utstyrskategori), vil HPUS-koordinatoren motta klart flest varsler.
Dette bør reflekteres i recipients-konfigurasjonen.

## Blindsone-effekten – kvantifisert

Figur `fig_total_gap_per_uke.png` og `fig_demand_vs_reservations_maanedlig.png`
viser tydelig hovedmotivasjonen for prosjektet:

- **Total ukentlig gap reduseres lineært fra ca −182 i mai 2026 til omtrent 0
  i januar 2027** – en reduksjon på ~180 unit-uker over 8 måneder
- **Synlig 75 %+ demand reduseres fra 884 (mai) til 301 (desember)** – 66 %
  reduksjon
- **Reservation-gap per måned er nokså stabilt 285–324 unit-uker fra
  mai–august**, men faller til 73 i desember

Den nedadgående trenden er **ikke** et tegn på at fremtiden er problemfri –
det er nettopp tegnet på at fremtidens kontrakter ennå ikke er bumpet til
75 %, og at modellen har liten tid på seg fra en kontrakt blir synlig til
leveranse skjer. Hvis vi snitter gradienten i Figur 2, vokser synlige gap
med ~5 unit-uker per uke nedover horisonten – det er størrelsesordenen
varslingssystemet må fange tidlig.

## Per-Tier 1-utvikling

Figur `fig_per_tier1_uker.png` viser at HPUS dominerer det totale gapet i
nær fremtid (helt nede i −59 i mai), mens de andre gruppene ligger
relativt flatt. **HPUS er hovedbidragsyteren til samlet underskudd**, men
også gruppen med flest assets (26 av 80 leaf-rader, 32,5 % av flåten i
Calendar). Per-asset-gjennomsnittet er ikke nødvendigvis verst i HPUS.

## Datakvalitet bekreftet

EDA bekrefter funn fra 5.2.5 i rapporten:
- 0 negative outliers utover det som forklares av rounding (ingen verdier
  utenfor [−13, 6])
- 2 av 36 uker har +2 avvik mot Tier 1-summer (allerede dokumentert som
  rounding støy)
- Ingen manglende uker eller assets i datasettet

## Konkrete implikasjoner for kapittel 6 Modellering

| Designvalg | EDA-grunnlag |
|------------|--------------|
| Magnitude-klassifisering av gap | Halefordeling i Figur 1, P5 = −6 |
| Suppress strukturelle gap fra varsling | 8 assets har konstant negativ gap |
| Eksklusjonsliste for inaktive assets | 2 assets med 0 i hele perioden |
| Per-asset-spesifikk historikk | "Strukturell vs kontraktsdrevet"-skille er nødvendig |
| Uke-til-uke-deltatest = hovedmekanisme | Snapshotspesifikk gap-verdi alene gir ikke nok signal |
| HPUS-koordinator som første mottaker | Dominerer både volum og topp-10-listen |

## Begrensninger og åpne spørsmål

- **Ett snapshot er ikke nok** for å evaluere uke-til-uke-mekanismen.
  Trenger snapshot 2026-05-04 for første ekte deltatest.
- **Strukturelle gaps kan være feilkonfigurert demand i Salesforce**, ikke
  reell flåteunderdimensjonering. Bør verifiseres med Motive før vi
  designer suppression-regelen.
- **EDA dekker kun 75–100 % vinnersannsynlighet.** Vi har ikke synlighet
  i hva som ligger på 50–75 %, og dermed kan vi ikke kvantifisere
  blindsonen presist. Dette er et empirisk gap som først kan måles ved
  uke-til-uke-sammenligning over tid.
