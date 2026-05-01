# Avviksanalyse: Forskyvning av milepæler M4–M7

**Dato:** 2026-05-01
**Identifisert av:** Begge (under planoppdatering)
**Eier:** Begge
**Status:** Realisert, plandato beholdes for sporbarhet

## Sammendrag

Fire av åtte milepæler i prosjektets opprinnelige plan er forsinket med 9–18 dager sammenlignet med opprinnelig plandato. M8 (sluttrapport innlevert 2026-05-31) holder uendret som ufravikelig endato. Forsinkelsen er hovedsakelig drevet av at datafangstmetoden måtte endres (jf. `avviksanalyse-2026-04-30.md`) og av at den eksplorative dataanalysen ble utvidet i omfang for å forankre modelleringsvalgene empirisk.

## Identifisert avvik

| ID | Milepæl | Plandato | Realistisk dato | Forsinkelse |
|----|---------|----------|-----------------|-------------|
| M1 | Godkjent prosjektbeskrivelse (proposal) | 2026-02-23 | 2026-02-23 | 0 dager |
| M2 | Data mottatt og klargjort | 2026-03-10 | 2026-04-30* | 51 dager |
| M3 | Godkjent prosjektstyringsplan | 2026-03-16 | 2026-03-16 | 0 dager |
| **M4** | **Første fungerende gap-deteksjonsscript** | **2026-04-18** | **~2026-05-06** | **18 dager** |
| **M5** | **Varslingslogikk implementert** | **2026-05-02** | **~2026-05-13** | **11 dager** |
| **M6** | **Varslingssystem testet og validert** | **2026-05-10** | **~2026-05-20** | **10 dager** |
| **M7** | **Førsteutkast rapport ferdig** | **2026-05-16** | **~2026-05-25** | **9 dager** |
| M8 | Sluttrapport innlevert | 2026-05-31 | 2026-05-31 | 0 dager |

\* M2 ble formelt markert oppnådd ved tidlig sample-data, men reell komplett baseline-snapshot ble først fanget 2026-04-30 grunnet R10-avviket.

## Årsak

Forsinkelsen har tre hovedårsaker:

1. **R10-avviket (Power BI-tilgang).** Datafangstmetoden måtte endres fra CSV-eksport til skjermavlesning. Utvikling av transkriberings- og verifikasjonsskript ble nødvendig før selve gap-deteksjonen kunne testes, hvilket utvidet 3.1 i omfang.
2. **Utvidet EDA-omfang.** Den eksplorative dataanalysen (3.2) ble mer detaljert enn opprinnelig planlagt fordi funnene danner empirisk grunnlag for modelleringsvalgene i kapittel 6 (magnitudeklasser, suppression-regler, eksklusjonsliste). Investeringen i EDA forventes å redusere arbeidsmengden i 3.3 og 3.5.
3. **Snapshot-avhengighet for M4.** Akseptansekriteriet for WBS 3.3 – at modellen skal skille mellom *nye*, *eksisterende* og *forverrede* gap – krever to påfølgende snapshots. Andre snapshot er mandag 2026-05-04, hvilket setter en faktisk grense på når M4 kan oppnås.

## Konsekvens

- Buffer fra første utkast (M7) til endato (M8) reduseres fra 15 til 6 dager.
- Validering (3.5) og rapportferdigstilling (3.6) får kortere tid til iterativ forbedring.
- M8 kan fortsatt oppnås, men med mindre fleksibilitet hvis nye avvik oppstår.

## Tiltak

1. **Plandato beholdes urørt** i `milestones.json` for sporbarhet og evaluering. Realistiske datoer dokumenteres kun i denne avviksanalysen og som noter i `status.md`.
2. **Parallell arbeidsflyt.** Rapportskriving (3.6) og kodeutvikling (3.3, 3.4) kjøres parallelt frem til M6 for å gjenvinne tid. Kapittel 6 og 7 i rapporten er allerede ferdige som forberedelse.
3. **Fokusert valideringsplan.** 3.5 begrenses til ett ekte snapshot-par (baseline 2026-04-30 + 2026-05-04) supplert med syntetiske scenarier for edge cases, fremfor en lengre snapshot-serie. Dette er beskrevet eksplisitt i metodikkens begrensninger i kapittel 9.
4. **Tidlig figurproduksjon.** EDA-figurer er ferdig generert og innlemmet i kapittel 7 før M7-fristen, slik at sluttspurten kan fokusere på resultat- og diskusjonskapittelet.
5. **Ukentlig statusvurdering.** Buffer mot M8 vurderes hver fredag for å oppdage ytterligere glidning tidlig.

## Vurderte alternativer

| Alternativ | Vurdering |
|---|---|
| Be veiledere om utsettelse av M8 | Forkastet. M8 = innleveringsfrist for LOG650 og er ufravikelig. |
| Redusere omfang av rapporten | Forkastet. Kapittelstruktur er bestemt av LOG650-kravene. |
| Redusere omfang av valideringen | Valgt delvis. 3.5 fokuserer på ett snapshot-par + syntetiske scenarier. |
| Parallellisere rapport og kode | Valgt. Iverksatt 2026-05-01. |

## Påvirkning på øvrig plan

| Område | Påvirkning |
|---|---|
| WBS 3.5 | Redusert omfang (færre snapshot-par i validering); dokumentert i `wbs.json` deliverables |
| WBS 3.3 | Avhenger av snapshot 2 (2026-05-04); kan ikke akselereres ytterligere |
| WBS 3.6 | Akselerert; kapittel 1–7 ferdig før M7-fristen |
| Kapittel 9 (Diskusjon) | Utvides til å dekke metodisk begrensning fra én snapshot-serie og hva fullstendig validering ville krevd |
| `milestones.json` | Plandato beholdes; ingen oppdatering av datofelter |
| `status.md` | Note per WBS-aktivitet om realistisk fremdrift |

## Status

Avviket er realisert og under håndtering. Tiltak iverksatt 2026-05-01. Buffer mot M8 vurderes ukentlig hver fredag. Videre forskyvning utløser ny avviksanalyse.
