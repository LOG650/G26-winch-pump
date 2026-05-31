# Råbilder – snapshot 2026-05-14

Skjermbilder fra Motive Offshores Power BI-rapport, tatt 2026-05-14. Fanget
visning: **Supply/ Demand – Calendar**.

> **Konfidensielt.** Bildene er ikke i git, kun lokalt.

## Filnavn-konvensjon

```
calendar_motive_no_75pct_rows<R1>-<R2>_weeks<W1>-<W2>.png
```

Eksempel:
```
calendar_motive_no_75pct_rows01-12_weeks01-09.png
calendar_motive_no_75pct_rows13-24_weeks01-09.png
calendar_motive_no_75pct_rows01-12_weeks10-18.png
...
```

## Sjekkliste per snapshot

- [ ] Filtre er satt korrekt:
  - Asset Custodian (Supply) = `Motive AS`
  - Project Owner Demand = `Motive AS`
  - Region = `Motive Norway`
  - Opp. Probability (%) = `75–100`
- [ ] Calendar: alle Tier 2-rader er dekket (sjekk at `Totalt`-raden er med på siste loddrette bilde)
- [ ] Calendar: datointervall fra inneværende uke til så langt Power BI viser
- [ ] **Cellefargene må være tydelig synlige** (ikke skalert ned så lavt at grønn/lilla/svart ikke kan skilles) – fargen transkriberes som `severity_band` per celle
- [ ] Colour Key-boksen til høyre i rapporten er med i minst ett bilde per snapshot, som visuell sjekk på at fargeintervallene ikke er endret
- [ ] Filnavn følger konvensjonene over

## Transkribering

Hver celle leses som **(gap_value, severity_band)** – tallet i cellen og
bakgrunnsfargen (grønn/gul/rød/lilla/svart). Fargen koder prosent-gap og
er ikke utledbar fra gap-verdien alene. Se
[`006 analysis/3.1 datainnhenting/tab_kolonner.md`](../../../006%20analysis/3.1%20datainnhenting/tab_kolonner.md)
for full skjemabeskrivelse.
