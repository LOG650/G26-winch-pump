# 006 analysis

Analysearbeid for G26 WinchPump. Felles `uv`-prosjekt med én undermappe per WBS-aktivitet i fase 3.

## Struktur

| Mappe | WBS | Innhold |
|-------|-----|---------|
| `3.1 datainnhenting/` | 3.1 | Rensing av rådata fra Power BI-eksport |
| `3.2 eda/` | 3.2 | Eksplorativ dataanalyse, figurer, tabeller |
| `3.3 gap-deteksjon/` | 3.3 | Regelbasert uke-til-uke gap-deteksjon |
| `3.4 varsling/` | 3.4 | E-postvarsling med 75 %-terskel og påminnelse |
| `3.5 validering/` | 3.5 | Testing mot kjente gap og edge cases |

Detaljer for hver aktivitet ligger i undermappenes egen `README.md`.

## Komme i gang

```bash
cd "006 analysis"
uv sync
```

Kjøre et skript:

```bash
uv run python "3.2 eda/eda_supply_demand.py"
```

## Avhengigheter

- `pandas` – datamanipulering
- `matplotlib` – figurer
- `openpyxl` – lese Excel-eksporter fra Power BI
- `python-dotenv` – SMTP-credentials i 3.4 (`.env`-fil committes ikke)

Legg til nye avhengigheter med `uv add <pakke>`.

## Filnavn-konvensjoner

- `fig_*.png` – figurer brukt i rapporten
- `tab_*.md` – tabeller brukt i rapporten
- Skript, figurer og resultatfiler ligger **sammen** i samme aktivitetsmappe (jf. AGENTS.md)

## Data

Datafiler ligger i `../004 data/` og er **konfidensielle** (Motive Offshore). De skal aldri committes – `.gitignore` blokkerer `*.csv`, `*.xlsx`, `*.parquet` som ekstra sikkerhetsnett.
