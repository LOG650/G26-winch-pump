# 3.5 Validering og testing

**WBS-aktivitet:** 3.5
**Eier:** Begge
**Status:** Pågår – 50 syntetiske tester implementert og passerer
**Milepæl:** M6 – varslingssystem testet og validert mot kjente gap (2026-05-10)

## Formål

Teste systemet mot kjente gap, verifisere korrekt varsling og teste edge cases.

## Filer

| Fil | Formål |
|-----|--------|
| `conftest.py` | Setter opp `sys.path` slik at testene kan importere `gap_alerting` og `gap_detection` |
| `test_evaluate_alert.py` | Enhetstester for `evaluate_alert`, `severity_cross`, `magnitude_class` (38 tester) |
| `test_thread_lifecycle.py` | Integrasjonstester for varslingstrad-livssyklus, ruting, mønsterdeteksjon (12 tester) |

## Kjøring

```
uv run pytest "3.5 validering/" -v
```

## Dekning

Testsuiten dekker akseptansekriteriet ved å validere:

- **Tabell 6.4 (G-regel):** alle endringstyper med ulike magnitudeklasser, ikke-strukturell vs. strukturell
- **Tabell 6.5 (severity-regel):** alle severity-overganger (skjult nytt gap, forverring, løst, forbedring, innen samme sone)
- **Trad-livssyklus:** ny → påminnelse → eskalert → løst, med reminder_count-inkrementering
- **Ruting (6.7):** asset type → primærmottaker, ukjent type → default
- **Mønsterdeteksjon:** sammenhengende uker for samme asset i digest
- **Edge cases:** identiske snapshots uten aktive trader (0 varsler), eksklusjonshåndtering

Alle **50 tester passerer** på ~1,6 sekunder.

## Akseptansekriterier

Systemet identifiserer gap korrekt (✓ G-regel og severity-regel verifisert), sender varsling til riktig mottaker (✓ ruting verifisert) og håndterer edge cases (✓ identiske snapshots, eksklusjon, suppression, mønsterdeteksjon verifisert).

## Videre arbeid

- Integrasjonstest med faktiske snap 1↔2 og snap 2↔3 (når snap 3 foreligger) – validerer kjernemodulen mot ekte data
- Negativ test for transkriberingsfeil (sumcheck > ±2 → flagget)
