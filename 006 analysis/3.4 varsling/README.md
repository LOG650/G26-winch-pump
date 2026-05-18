# 3.4 Varslingslogikk

**WBS-aktivitet:** 3.4
**Eier:** Begge
**Status:** Pågår – kjernemodul ferdig, påminnelseslogikk venter på snapshot 3
**Milepæl:** M5 – varslingslogikk implementert (2026-05-02)

## Formål

Implementere 75 %-terskel, gap-deteksjon og e-postvarsling med ukentlige påminnelser.

## Filer

| Fil | Formål |
|-----|--------|
| `gap_alerting.py` | Hovedmodul: leser `gap_changes.csv` fra 3.3, anvender Tabell 6.4 (G-regel) og Tabell 6.5 (severity-regel), genererer varselsobjekter og digest-e-poster |
| `recipients.yaml` | Mottakerkonfigurasjon per asset type med CC til salgsteamet |
| `varsler.csv` | Komplett varselsliste (genereres) |
| `digests/` | Digest-e-post per mottaker per snapshot (genereres) |

## Status på leveranser

- [x] Python-modul for varselsgenerering (`gap_alerting.py`)
- [x] Varselsformat – Varselsobjekt-skjema i 6.7 Tabell 6.6, implementert som `@dataclass`
- [x] Recipients-konfig per asset type (`recipients.yaml`)
- [x] Eksklusjons- og suppression-håndtering per 6.5/6.6
- [x] Mønsterdeteksjon for sammenhengende uker
- [x] Digest-format per mottaker
- [ ] Ukentlig påminnelseslogikk – krever tre+ snapshots for å demonstrere varslingstråd som lever over uker (venter på t₂ = 2026-05-21)
- [ ] SMTP-leveranse – modulen produserer digest-filer; faktisk sending krever SMTP-credentials i `.env` og er kun beskrevet i 6.7
- [ ] Dokumentasjon av produksjonsintegrasjon mot Power BI REST API – står som videre arbeid i kap 9

## Kjøring

```
uv run python "3.4 varsling/gap_alerting.py"
```

## Akseptansekriterier

Varsel genereres korrekt ved ≥75 % vinnersannsynlighet og gap (✓ kjernedeteksjon validert mot snap 1↔2); ukentlig påminnelse er foreløpig kun beskrevet i modelltekst og avventer snapshot 3 for empirisk demonstrasjon.

## Notat

SMTP-credentials lastes via `python-dotenv` fra en `.env`-fil som **ikke** skal committes.
