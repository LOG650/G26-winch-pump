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

## Filteroppsett (Power BI)

Alle snapshots bruker følgende filtre i Power BI. Begge sider av regnestykket
er låst til samme verksted (Motive Norway), slik at gap-verdiene reflekterer
flåten som lokalt selger faktisk kan disponere:

| Filter | Verdi | Kommentar |
|--------|-------|-----------|
| Asset Custodian (Supply) | `Motive AS` | Juridisk enhet som forvalter flåten |
| Project Owner Demand | `Motive AS` | Juridisk enhet som eier prosjektet |
| Region | `Motive Norway` | Fysisk verkstedslokasjon |
| Opp. Probability (%) | `75` | Nedre terskel for synlig etterspørsel |

Modellen er lokasjons-agnostisk: de tre første filtrene byttes synkront for å
kjøre samme analyse for et annet verksted (Motive UK, Motive USA, ...).

Gjeldende baseline er **2026-05-07** med fullt filtersett.

## Datafangst via skjermbilder

"Analyser i Excel" og "Eksporter data" er sperret av rettighetspolicy hos Motive.
Datafangst skjer derfor ved **manuell skjermavlesning** av Power BI-kalendervisningen.

For hver celle fanges **to attributter**:

- `gap_value` – heltallet som vises i cellen (supply minus demand, avrundet)
- `severity_band` – cellens bakgrunnsfarge fra Power BI Colour Key, som koder
  prosent-gap relativt til demand (`green`/`yellow`/`red`/`purple`/`black`)

Fargen er ikke redundant med gap-verdien: samme `gap_value = -2` kan være
lilla (lite reelt underskudd) eller svart (over halvparten av en liten demand)
avhengig av underliggende etterspørsel. Begge attributter må derfor
transkriberes per celle. Se fargenøkkelen i [`tab_kolonner.md`](tab_kolonner.md#fargenøkkel-for-severity_band)
og bildet `004 data/fargekode.png`.

### Mappestruktur

```
004 data/<YYYY-MM-DD>_motive_no/raw/    ← PNG-bilder per snapshot-dato
004 data/<YYYY-MM-DD>_motive_no/clean/  ← transkribert CSV per snapshot
```

### Skjema

Se [`tab_kolonner.md`](tab_kolonner.md) for kolonnedefinisjoner og eksempelrader.

### Snapshot-kadens

| t | Dato | Status | Formål |
|---|------|--------|--------|
| t₀ | 2026-05-07 | ✅ Ferdig | Baseline – lokalt verksted (Motive Norway) på begge sider, fullt filtersett |
| t₁ | 2026-05-14 | ✅ Ferdig | Første uke-til-uke-sammenligning (snap1 ↔ snap2) |
| t₂ | 2026-05-21 | Planlagt (torsdag) | Andre delta-par (snap2 ↔ snap3) – demonstrerer ukentlig varslingstråd over flere snapshots, jf. 3.4-akseptansekriterium |

**Begrenset til tre snapshots.** Et fjerde snapshot (2026-05-28) ble vurdert,
men marginal verdi gjør at innsatsen heller plasseres på WBS 3.4–3.6 i
sluttspurten. To delta-par er tilstrekkelig for å demonstrere modellens
fem endringstyper og varslingstrådens livssyklus; lengre snapshot-serier i
produksjon adresseres som videre arbeid i kap 9 av rapporten.

## Notat

Selve datafilene ligger i `004 data/` og skal **ikke** committes til git.
