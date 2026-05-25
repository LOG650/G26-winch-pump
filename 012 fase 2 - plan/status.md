# Prosjektstatus

**Prosjekt:** G26 WinchPump – KI-basert kapasitetsvarsling for Motive Offshore
**Dato:** 2026-05-24
**Utarbeidet av:** David Johan Lunde og Tord Haakon Johnsen Hovden

---

## Milepæler

| ID | Ferdig | Milepæl | Planlagt dato | Faktisk dato |
|----|--------|---------|--------------|--------------|
| M1 | [x] | Godkjent prosjektbeskrivelse (proposal) | 2026-02-23 | 2026-02-23 |
| M2 | [x] | Data mottatt og klargjort | 2026-03-10 | 2026-03-10 |
| M3 | [x] | Godkjent prosjektstyringsplan | 2026-03-16 | 2026-03-16 |
| M4 | [x] | Første fungerende gap-deteksjonsscript | 2026-04-18 | 2026-05-14 |
| M5 | [x] | Varslingslogikk implementert (e-postvarsling) | 2026-05-02 | 2026-05-23 *(SMTP-demo)* |
| M6 | [x] | Varslingssystem testet og validert mot kjente gap | 2026-05-10 | 2026-05-23 *(50 syntetiske tester + 2 delta-par på reelle data)* |
| M7 | [x] | Førsteutkast rapport ferdig | 2026-05-16 | 2026-05-24 *(alle kapitler skrevet; sammendrag/abstract/forside gjenstår som finpuss)* |
| M8 | [ ] | Sluttrapport innlevert | 2026-05-31 | – |

---

## WBS-status

### 1.0 Initiering

- [x] 1.1 Prosjektbeskrivelse (proposal) — Begge
- [x] 1.2 Litteratursøk (innledende) — Tord
- [x] 1.3 Datatilgang avklart — David

### 2.0 Planlegging

- [x] 2.1 Prosjektstyringsplan — Tord
- [x] 2.2 Kravspesifikasjon — Begge
- [x] 2.3 Forskningsplan — Begge
- [x] 2.4 WBS og Gantt-plan — Tord

### 3.0 Gjennomføring

- [x] 3.1 Datainnhenting og klargjøring — David *(snapshot 1, 2 og 3 ferdig transkribert: 2026-05-07, 2026-05-14, 2026-05-21)*
- [x] 3.2 Eksplorativ dataanalyse (EDA) — Tord
- [x] 3.3 Gap-deteksjonslogikk — Begge *(begge delta-par kjørt: snap1↔snap2 gav 7 NYTT_GAP + 5 severity-varsler, snap2↔snap3 gav 4 NYTT_GAP + 8 LØST + 7 severity-/påminnelse-varsler)*
- [x] 3.4 Varslingslogikk — Begge *(kjernemodul + thread-tracking ferdig; SMTP-leveranse demonstrert ende-til-ende 2026-05-23 med 5 digester levert til testkonto)*
- [x] 3.5 Validering og testing — Begge *(50 pytest-tester passerer; reelle data over 2 delta-par viser 5 av 10 tråder lukkes automatisk i andre syklus)*
- [x] 3.6 Rapportskriving (løpende) — Begge *(alle kapitler 1–10 skrevet; bibliografi og vedlegg D/F/G på plass; sammendrag og forside-erklæringer gjenstår)*

### 4.0 Avslutning

- [ ] 4.1 Sluttrapport — Begge *(kortetiltak gjennomført 2026-05-24; sluttsjekk og endelig innlevering gjenstår)*
- [ ] 4.2 KI-bruk-dokumentasjon — Begge *(Vedlegg A venter på mal fra skolen)*
- [ ] 4.3 Muntlig presentasjon — Begge

---

## Rapportstatus

### Forside og erklæringer

- [ ] Egenerklæring/gruppeerklæring signert
- [ ] Personvern (NSD/REK vurdert)
- [ ] Publiseringsavtale fylt ut
- [ ] Sammendrag (norsk)
- [ ] Abstract (engelsk)

### Kapitler

- [x] 1.0 Innledning
  - [x] 1.1 Problemstilling
  - [x] 1.2 Delproblemer
  - [x] 1.3 Avgrensinger
  - [x] 1.4 Antagelser
- [x] 2.0 Litteratur
- [x] 3.0 Teori
- [x] 4.0 Casebeskrivelse (Motive Offshore)
- [x] 5.0 Metode og data
  - [x] 5.1 Metode
  - [x] 5.2 Data
- [x] 6.0 Modellering
- [x] 7.0 Analyse
- [x] 8.0 Resultat
- [x] 9.0 Diskusjon
- [x] 10.0 Konklusjon
- [x] 11.0 Bibliografi (APA 7) — 10 referanser
- [ ] 12.0 Vedlegg
  - [ ] Vedlegg A: KI-bruk-erklæring *(venter på mal)*
  - [ ] Vedlegg B: Taushetserklæring *(signeres ved innlevering)*
  - [ ] Vedlegg C: Kravmatrise *(skrives før innlevering)*
  - [x] Vedlegg D: Komplette SMTP-digester
  - [x] Vedlegg F: Full valideringsscenario-tabell
  - [x] Vedlegg G: Varselsobjekt-skjema

### Ferdigstilling

- [x] Førsteutkast (alle kapitler dekket) — ferdig 2026-05-24 *(7 dager etter planlagt 2026-05-16)*
- [ ] Tilbakemeldinger fra veiledere innarbeidet *(peer review fra halvveis i prosjektet legges inn senere)*
- [ ] KI-bruk dokumentert og erklæring signert
- [ ] Sluttsjekk per AGENTS.md-sjekkliste
- [ ] Endelig innlevering — innen 2026-05-31

---

## Gjenstående arbeid (per 2026-05-24, 7 dager til frist)

| Oppgave | Estimat |
|---|---|
| Sammendrag (norsk) + Abstract (engelsk) | 1–2 t |
| Vedlegg C: Kravmatrise | 30–60 min |
| Vedlegg A: KI-bruk-erklæring | 30 min når mal foreligger |
| Vedlegg B: Taushetserklæring + forside-erklæringer (signering) | 1 t |
| Innarbeiding av peer review | 1–2 t |
| Sluttsjekk per AGENTS.md-sjekkliste | 1 t |
| **Sum** | **5–8 t** |

---

*Neste revisjon: ved neste arbeidsmøte eller ved statusendring*
