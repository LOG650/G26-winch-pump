# Dataskjema – supply/demand-snapshots

To CSV-er per snapshot:

1. **Calendar** – ukentlig gap-verdi per Tier 2-utstyrsenhet (`*_supply_demand_motive_alle_75pct.csv`)
2. **Overview** – månedlig aggregat per Tier 1-kategori (`*_supply_demand_overview_motive_alle_75pct.csv`)

---

## 1. Calendar – ukentlige gap-verdier

Skjema for renset CSV som genereres fra Power BI-skjermbilder (kalendervisningen
"Supply/ Demand – Calendar"). Én rad per **(snapshot, uke, utstyrsenhet)**.

## Format

- **Filtype:** CSV
- **Skilletegn:** komma (`,`)
- **Encoding:** UTF-8 uten BOM
- **Desimaltegn:** punktum (`.`) – verdiene er heltall, men formatet er pandas-vennlig
- **Datoformat:** ISO 8601 (`YYYY-MM-DD`)

## Kolonner

| Kolonne | Type | Eksempel | Beskrivelse |
|---------|------|----------|-------------|
| `snapshot_date` | dato | `2026-04-30` | Dato skjermbildet ble tatt – fungerer som id for hver "uke-til-uke"-sammenligning |
| `week_start` | dato | `2026-09-07` | Mandag i den uken cellen gjelder for |
| `asset_tier1` | streng | `Winches` | Toppnivågruppen i tabellen (Winches, Under rollers, ...) |
| `asset_tier2` | streng | `Hydraulic - 60Te Mooring Winch` | Spesifikk utstyrsenhet, eksakt slik den står i Power BI |
| `gap_value` | heltall | `-4` | Supply minus demand. Negativ verdi = kapasitetsgap |
| `custodian` | streng | `Motive AS` | Filterverdi: Asset Custodian (Supply) |
| `region` | streng | `Alle` | Filterverdi: Region |
| `probability_threshold` | heltall | `75` | Filterverdi: Opp. Probability (%) – nedre terskel |

## Eksempel (5 rader)

```csv
snapshot_date,week_start,asset_tier1,asset_tier2,gap_value,custodian,region,probability_threshold
2026-04-30,2026-09-07,Winches,Pneumatic - FA5 Air winch,0,Motive AS,Alle,75
2026-04-30,2026-09-14,Winches,Pneumatic - FA5 Air winch,0,Motive AS,Alle,75
2026-04-30,2026-09-21,Winches,Pneumatic - FA5 Air winch,0,Motive AS,Alle,75
2026-04-30,2026-09-28,Winches,Pneumatic - FA5 Air winch,-2,Motive AS,Alle,75
2026-04-30,2026-10-05,Winches,Pneumatic - FA5 Air winch,-2,Motive AS,Alle,75
```

## Datakilde

Power BI-rapport, side **"Supply/ Demand – Calendar"**, hos Motive Offshore.
Eksport via "Analyser i Excel" og "Eksporter data" er sperret av rettighetspolicy.
Datafangst skjer derfor ved **manuell skjermavlesning** av PNG-skjermbilder
i prosjektperioden 2026-04-30 til 2026-05-31.

## Aggregeringsnivå

- **Tidsoppløsning:** uke (mandag-mandag)
- **Utstyrsoppløsning:** Tier 2 (spesifikk utstyrsenhet, ikke individuelle serienumre)
- **Geografisk oppløsning:** aggregert på tvers av alle regioner (`region = "Alle"`)
  for grunnsettet. Region-spesifikke uttrekk gjøres separat dersom relevant.

## Datakvalitet

- Verdier transkriberes fra skjermbilder. Lesefeil kan forekomme.
- `Totalt`-rad og Tier 1-gruppesummer i Power BI brukes som **sum-sjekk** per
  snapshot for å verifisere at transkriberingen er fullstendig
  (`verify_tier1_sums.py`).
- Snapshots som har inkonsistent sum flagges og må kontrolleres manuelt.

### Avrundingsstøy fra Power BI

Power BI viser cellene som **avrundede heltall**, men aggregerer Tier 1-rader
og `Totalt` fra **underliggende desimal-grunndata**. Det betyr at sum av viste
celler kan avvike fra Power BIs egen Tier 1-sum med **typisk ±1–2** per gruppe
per uke. Dette er ikke en transkriberingsfeil, men en konsekvens av at en
delvis tilgjengelig utstyrsenhet (f.eks. utleid 3 av 7 dager = 0.43) lagres
som desimal og avrundes til heltall ved visning.

Forskjeller på 1–2 aksepteres derfor som avrundingsstøy. Større avvik (>2)
flagges som mistanke om transkriberingsfeil. Vi bruker **leaf-verdiene** som
hoveddatasett fordi det er disse selgere og koordinatorer faktisk ser i
Power BI – og som gap-deteksjonen skal reagere på.

## Lange vs. brede tabeller

Datasettet lagres i **lang form** (én rad per uke per asset). Brede tabeller
brukt i rapporten genereres ved behov med `pivot_table` i pandas.

---

## 2. Overview – månedlige aggregater

Skjema for renset CSV som genereres fra "Supply vs Demand – Overview"-siden i
Power BI. Én rad per **(snapshot, måned, Tier 1-kategori)**.

Brukes som overordnet kontroll av datagrunnlaget og for høynivåfigurer i
rapporten – ikke som hoveddatasett for gap-deteksjon.

### Kolonner

| Kolonne | Type | Eksempel | Beskrivelse |
|---------|------|----------|-------------|
| `snapshot_date` | dato | `2026-04-30` | Dato bildene ble tatt |
| `month` | streng | `2026-05` | Måned aggregatet gjelder for (`YYYY-MM`) |
| `asset_tier1` | streng | `Winch` | Tier 1-kategori (Winch, HPUS, Mob-Personnel, ...) |
| `assets_in_fleet` | heltall \| tom | `12` | Antall enheter i flåten. Tom for tjenester (mob/demob) og noen kategorier |
| `assets_red_tag` | heltall \| tom | tom | Antall enheter merket Red Tag (oftest tom) |
| `demand` | heltall | `212` | Total etterspørsel for måneden (unit-uker) |
| `reservations_per_av` | heltall \| tom | `135` | Reservasjoner i Asset Voice. Tom for tjenester |
| `custodian` | streng | `Motive AS` | Filterverdi |
| `region` | streng | `Alle` | Filterverdi |
| `probability_threshold` | heltall | `75` | Filterverdi (Opp. Probability % nedre terskel) |

### Tier 1-kategorier

Overview inneholder 19 kategorier – flere enn Calendar:

- **Med flåte (i Calendar):** Winch, Under rollers, Turntables, Tensioner,
  Storage reels, Spoolers, RDS, LMA machines, HPUS, HLS, Generators, Cranes,
  Cable Pulling machine
- **Uten flåte (kun i Overview):** Mob-Personnel, Mob-Equipment,
  Mob/Demob-Personnel, Mob/Demob-Equipment, Demob-Personnel, Demob-Equipment

De siste seks er **operasjonelle tjenester** (mobilisering/demobilisering),
ikke fysisk utstyr. De er ekskludert fra gap-deteksjonen per
avgrensning i 1.3 i prosjektrapporten.

### Eksempel (3 rader)

```csv
snapshot_date,month,asset_tier1,assets_in_fleet,assets_red_tag,demand,reservations_per_av,custodian,region,probability_threshold
2026-04-30,2026-05,Winch,12,,212,135,Motive AS,Alle,75
2026-04-30,2026-05,Mob-Personnel,,,9,,Motive AS,Alle,75
2026-04-30,2026-05,HPUS,16,,291,241,Motive AS,Alle,75
```

### Datakvalitet

- Sumsjekk per måned mot `Totalt`-raden i Power BI verifiserer at fleet,
  demand og reservations summerer korrekt. **Ingen avrundingsstøy** observert
  her – Overview-tallene er rene heltall (i motsetning til Calendar).
- Tom celle = blank i Power BI (ikke 0). Skiller "ikke målt" fra "0".
