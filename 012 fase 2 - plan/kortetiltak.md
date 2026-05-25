# Kortetiltak for Prosjektrapport.md

**Status:** Oppdatert 2026-05-24, klar for gjennomføring
**Mål:** Redusere rapporten med ~155 linjer (~14 %) uten å miste substans
**Utgangspunkt:** Rapporten er **1146 linjer**

## Avklart plan – gjennomføres i rekkefølge

### Gruppe A – Trygge, åpenbare kutt (~21 linjer)

- [x] **A1.** Fjern draftnotat «Metode og data (kan splittes i to)» og instruksjonsavsnitt «Litt avhengig av omfanget...» (linje 291–293) – 3 linjer
- [x] **A2.** Reduser kap 4.7 «Datagrunnlag» (~7 linjer) til 1 setning som peker fram mot 5.2 – innholdet dupliseres helt i 5.2 – ~6 linjer
- [x] **A3.** Fjern mal-instruksjonene i kap 10 (linje 1108–1119) – 12 linjer (kap 10 skrives på nytt etter dette)

### Gruppe B – Sammenslåing av underkapittel (~55 linjer)

- [x] **B1.** Slå sammen kap 4.5 + 4.6 → integrert i 4.4 «Hvordan kapasitetsgap blir oversett, konsekvenser og faktorer» – ~20 linjer
- [x] **B2.** Slå sammen kap 5.2.1 + 5.2.2 → «Datakilder og filtrering» – ~5 linjer
- [x] **B3.** Slå sammen kap 5.2.4 + 5.2.5 → «Datasett og kvalitet» – ~5 linjer
- [x] **B4.** Slå sammen kap 6.5 + 6.6 → «Suppression og eksklusjon» – ~15 linjer
- [x] **B5.** Slå sammen kap 9.5 + 9.6 → «Praktisk betydning og generaliserbarhet» – ~10 linjer

### Gruppe C – Stramming av nylig skrevne avsnitt (~25 linjer)

- [x] **C1.** Stram kap 9.1 – 9.4: fjerne overlapp mellom 9.1 («Forventede og uventede funn») og 9.3 (begrensninger), redusere gjentagelser – ~25 linjer

### Gruppe D – Vedlegg-flytting (~57 linjer i hovedtekst)

- [x] **D1.** Flytt Figur 8.3 (RDS-digest), Figur 8.4 (Cable Pulling-digest), Figur 8.5 (Tensioner-digest) og Figur 8.6 (Spoolers-digest) til Vedlegg D «Komplette SMTP-digester fra demo 2026-05-23». Behold Figur 8.1 (innboks) og Figur 8.2 (HPUS-digest) i hovedteksten – ~20 linjer
- [x] **D2.** Kondenser Tabell 8.6 (valideringsscenarier, 19 rader) til en kort oppsummering i kap 8.6 («50 tester fordelt på X kategorier, alle passerer; full liste i Vedlegg F»). Full tabell flyttes til Vedlegg F – ~15 linjer
- [x] **D3.** Kondenser Tabell 6.6 (varselsobjekt-skjema, 17 rader) til kort liste i kap 6.6 («objektet inneholder kjernefelt X, Y, Z + 8 metadata-felt; fullt skjema i Vedlegg G»). Full tabell flyttes til Vedlegg G – ~22 linjer

## Det som IKKE skal røres

Per beslutning 2026-05-24:

- **Kap 2 Litteratur** – urørt (referanseseksjon)
- **Kap 3 Teori** – urørt (referanseseksjon, nylig oppdatert med Rajani & Heggde, Oliveira, Alaoua & Karim, Qi et al.)
- `recipients.yaml`-utdrag i kap 6.7 – beholdes i hovedteksten (brukers valg)
- Tabell 5.1 (fargenøkkelen) – kritisk for forståelse
- Tabell 5.3 (snapshot-serien) – nødvendig for reproduserbarhet
- Kap 6.3 og 6.4 – kjerna i modellbeskrivelsen
- Kap 7.6 / 7.6.1 / 7.6.2 – eneste empiriske validering av modellverdi
- Tabell 8.7 (delproblem-kobling) – kort og tett kobla til diskusjonen
- Figur 6.2 (endringstype-fase) – forklarer kjerneregelen

## Senere arbeid (etter Kap 10)

- [ ] Vedlegg A: KI-bruk-erklæring (mal ventes fra skolen)
- [ ] Vedlegg B: Taushetserklæring (krever signatur)
- [ ] Vedlegg C: Kravmatrise (kobling mellom WBS-akseptansekriterier og leveranser) – lages etter Kap 10
- [ ] Vurder ytterligere vedleggs-flytting etter ferdig kap 10

## Forventet resultat etter alle tiltak

| Tiltak | Spart |
|---|---|
| Gruppe A | 21 linjer |
| Gruppe B | 55 linjer |
| Gruppe C | 25 linjer |
| Gruppe D | 57 linjer |
| **Sum** | **~158 linjer** |

**Rapport går fra 1146 → ~990 linjer (14 % kutt).** Vedlegget vokser med ~50 linjer kondenserte tabeller og figurer.

## Sjekkliste etter alle kutt

- [ ] Alle tabell- og figurnumre renummerert konsistent (særlig kap 8 etter D1/D2/D3)
- [ ] Alle interne kryssreferanser oppdatert (Tabell X.Y, Figur X.Y, kap X.Y)
- [ ] Innholdsfortegnelse regenerert
- [ ] Lest gjennom hele rapporten for å sjekke at sammenslåtte avsnitt flyter naturlig
- [ ] Rapportsjekkliste i AGENTS.md gått gjennom
- [ ] Sjekke at ingen av de 10 bibliografi-referansene blir foreldreløse etter sammenslåing
