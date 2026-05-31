# Snapshot 2026-05-14 – Motive Norway (t₁)

Første uke-til-uke-sammenligning mot baseline 2026-05-07. Datasett fra Motive
Offshores Power BI-rapport *Supply vs Demand*, fanget 2026-05-14.

> **Konfidensielt.** Hele `004 data/` er ekskludert fra git.

## Innhold

```
2026-05-14_motive_no/
├── raw/                                                       ← skjermbilder
│   └── README.md                                                (filnavn-konvensjon)
├── clean/
│   └── 2026-05-14_supply_demand_motive_no_75pct.csv           ← Calendar (816 rader forventet)
└── README.md                                                    (denne fila)
```

## Filtre brukt

Identisk med baseline 2026-05-07:

| Filter | Verdi |
|--------|-------|
| Asset Custodian (Supply) | `Motive AS` |
| Project Owner Demand | `Motive AS` |
| Region | `Motive Norway` |
| Opp. Probability (%) | `75–100` |

## Calendar-datasett

- **Periode:** 2026-05-18 til 2026-12-28 (33 uker)
- **Granularitet:** Tier 2-utstyrsenhet × uke
- **Verdier per celle:**
  - `gap_value` = supply minus demand (heltall, slik Power BI viser cellen)
  - `severity_band` = cellens bakgrunnsfarge fra Power BI Colour Key
    (`green`/`yellow`/`red`/`purple`/`black`), som koder prosent-gap

Skjema: se [`006 analysis/3.1 datainnhenting/tab_kolonner.md`](../../006%20analysis/3.1%20datainnhenting/tab_kolonner.md).

## Reproduksjon

CSV-en genereres fra rådata-bilder via skript i `006 analysis/3.1 datainnhenting/`:

- `_transcribe_2026-05-14.py` – Calendar (gitignored, inneholder rådata inline)
- `verify_asset_type_sums.py` – sumsjekk

## Plass i tidsserien

| t | Dato | Status |
|---|------|--------|
| t₀ | 2026-05-07 | Baseline (ferdig) |
| **t₁** | **2026-05-14** | **Dette snapshotet (ferdig)** |
| t₂ | 2026-05-21 | Planlagt – siste i serien (torsdag) |
