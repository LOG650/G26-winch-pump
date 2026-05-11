# Dataskjema – supply/demand-snapshots

Én CSV per snapshot: **Calendar** – ukentlig gap-verdi per Tier 2-utstyrsenhet
(`*_supply_demand_motive_no_75pct.csv`).

## Calendar – ukentlige gap-verdier

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
| `snapshot_date` | dato | `2026-05-07` | Dato skjermbildet ble tatt – fungerer som id for hver "uke-til-uke"-sammenligning |
| `week_start` | dato | `2026-09-07` | Mandag i den uken cellen gjelder for |
| `asset_type` | streng | `Winches` | Asset type / utstyrstype (Winches, Under rollers, ...) |
| `asset_tier2` | streng | `Hydraulic - 60Te Mooring Winch` | Spesifikk utstyrsenhet, eksakt slik den står i Power BI |
| `gap_value` | heltall | `-4` | Supply minus demand. Negativ verdi = kapasitetsgap |
| `custodian` | streng | `Motive AS` | Filterverdi: Asset Custodian (Supply) – juridisk enhet som forvalter utstyret |
| `project_owner_demand` | streng | `Motive AS` | Filterverdi: Project Owner Demand – juridisk enhet som eier prosjektet |
| `region` | streng | `Motive Norway` | Filterverdi: Region – fysisk verksted/lokasjon |
| `probability_threshold` | heltall | `75` | Filterverdi: Opp. Probability (%) – nedre terskel |

## Eksempel (5 rader)

```csv
snapshot_date,week_start,asset_type,asset_tier2,gap_value,custodian,project_owner_demand,region,probability_threshold
2026-05-07,2026-05-11,Winch,Hydraulic - Wide|20Te Wide Drum Winch - 20Te Wide Drum Winch,4,Motive AS,Motive AS,Motive Norway,75
2026-05-07,2026-05-18,Winch,Hydraulic - Wide|20Te Wide Drum Winch - 20Te Wide Drum Winch,4,Motive AS,Motive AS,Motive Norway,75
2026-05-07,2026-05-11,Tensioner,Horizontal - 2 track - 15Te Horizontal Tensioner,-1,Motive AS,Motive AS,Motive Norway,75
2026-05-07,2026-05-11,RDS,- 500Te RDS,-1,Motive AS,Motive AS,Motive Norway,75
2026-05-07,2026-05-11,HPUS,Electric - 90KW Electric HPU,-2,Motive AS,Motive AS,Motive Norway,75
```

## Datakilde

Power BI-rapport, side **"Supply/ Demand – Calendar"**, hos Motive Offshore.
Eksport via "Analyser i Excel" og "Eksporter data" er sperret av rettighetspolicy.
Datafangst skjer derfor ved **manuell skjermavlesning** av PNG-skjermbilder
i prosjektperioden 2026-04-30 til 2026-05-31.

## Aggregeringsnivå

- **Tidsoppløsning:** uke (mandag-mandag)
- **Utstyrsoppløsning:** Tier 2 (spesifikk utstyrsenhet, ikke individuelle serienumre)
- **Geografisk oppløsning:** Datasettet er låst til ett verksted om gangen.
  Supply filtreres på `custodian = "Motive AS"` (juridisk enhet som forvalter
  flåten), demand filtreres på `project_owner_demand = "Motive AS"` (juridisk
  enhet som eier prosjektet) og `region = "Motive Norway"` (fysisk
  verkstedslokasjon). Samme rapport kan kjøres lokalt for andre verksteder
  (Motive UK, Motive USA, ...) ved å bytte alle tre filtrene synkront.

## Datakvalitet

- Verdier transkriberes fra skjermbilder. Lesefeil kan forekomme.
- `Totalt`-rad og asset type-summer i Power BI brukes som **sum-sjekk** per
  snapshot for å verifisere at transkriberingen er fullstendig
  (`verify_asset_type_sums.py`).
- Snapshots som har inkonsistent sum flagges og må kontrolleres manuelt.

### Avrundingsstøy fra Power BI

Power BI viser cellene som **avrundede heltall**, men aggregerer asset type-rader
og `Totalt` fra **underliggende desimal-grunndata**. Det betyr at sum av viste
celler kan avvike fra Power BIs egen asset type-sum med **typisk ±1–2** per asset type
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
