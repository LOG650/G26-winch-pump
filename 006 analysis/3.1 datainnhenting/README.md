# 3.1 Datainnhenting og klargjøring

**WBS-aktivitet:** 3.1
**Eier:** David
**Status:** Pågår

## Formål

Eksportere relevante datasett fra Power BI som CSV/Excel og rense/strukturere for analyse.

## Leveranser

- Skript som leser rå data fra `004 data/raw/` og skriver renset utgave til `004 data/clean/`
- `tab_kolonner.md` – datadokumentasjon (kolonner, typer, mangler)

## Filer

| Fil | Formål |
|-----|--------|
| `clean_supply.py` | Rensing av supply-data |
| `clean_demand.py` | Rensing av demand-data |
| `tab_kolonner.md` | Skjema for renset datasett |

## Datafangst via skjermbilder

"Analyser i Excel" og "Eksporter data" er sperret av rettighetspolicy hos Motive.
Datafangst skjer derfor ved **manuell skjermavlesning** av Power BI-kalendervisningen.

### Mappestruktur

```
004 data/raw/snapshots/<YYYY-MM-DD>/   ← PNG-bilder per snapshot-dato
004 data/clean/snapshots/              ← transkribert CSV per snapshot
```

### Skjema

Se [`tab_kolonner.md`](tab_kolonner.md) for kolonnedefinisjoner og eksempelrader.

### Snapshot-kadens

| t | Dato | Formål |
|---|------|--------|
| t₀ | 2026-04-30 | Baseline (i dag) |
| t₁ | 2026-05-04 | Første uke-til-uke-sammenligning |
| t₂ | 2026-05-11 | |
| t₃ | 2026-05-18 | |
| t₄ | 2026-05-25 | Siste før innlevering 2026-05-31 |

## Notat

Selve datafilene ligger i `004 data/` og skal **ikke** committes til git.
