# Kortetiltak for Prosjektrapport.md

**Status:** Forberedt 2026-05-18, klar for sluttspurten
**Mål:** Redusere rapporten med 100–150 linjer (~12–17 %) uten å miste substans
**Når:** Etter snapshot 3 er transkribert og analysert (~22.05)

## Utgangspunkt

Rapporten er **867 linjer** ved utgangspunkt. Tyngdepunkter:

| Kap | Linjer (omtrent) |
|---|---|
| 6 Modellering | ~155 |
| 7 Analyse | ~140 |
| 8 Resultat | ~110 |
| 9 Diskusjon | ~90 |
| 5 Metode og data | ~82 |
| 4 Casebeskrivelse | ~55 |

## Tiltak gruppert etter innsats

### 🔧 Lavthengende rydding (5–10 min)

- [ ] Fjern draftnotat "Metode og data (kan splittes i to)" (kap 5-tittel, linje 291)
- [ ] Fjern instruksjonsavsnitt "Litt avhengig av omfanget..." (linje 293)
- [ ] Reduser kap 4.7 (Datagrunnlag, ~10 linjer) til én setning som peker fram mot 5.2 – innholdet dupliseres allerede der

### 🔄 Sammenslåinger uten innholdsoffer (~30 min totalt)

| Slå sammen | Til | Spart |
|---|---|---|
| Kap 3.1 + 3.2 | "Kapasitet og gap" – bruker samme G/S/D-formel | ~15 linjer |
| Kap 3.3 + 3.4 | "Kapasitetsutnyttelse og beslutningslogikk" – varslingsregel bygger på utnyttelse | ~10 linjer |
| Kap 4.5 + 4.6 | Integrer i 4.4 som siste avsnitt | ~20 linjer |
| Kap 5.2.1 + 5.2.2 | "Datakilder og filtrering" – filtre er egenskap ved datakilde | ~5 linjer |
| Kap 5.2.4 + 5.2.5 | "Datasett og kvalitet" | ~5 linjer |
| Kap 6.5 + 6.6 | "Suppression og eksklusjon" – begge filter-mekanismer | ~10 linjer |
| Kap 9.5 + 9.6 | "Praktisk betydning og generaliserbarhet" | ~10 linjer |

**Sum: ~75 linjer (~9 %)**

### ⚠️ Innhold som krever beslutning

- [ ] **Kap 7 vs 8 overlapp.** Skolen krever begge (Analyse med tolkning, Resultat kun presentasjon). I dag dupliserer kap 8 tabeller fra kap 7. Mulighet: kap 8 reduseres til **referanser** ("Resultatene er presentert i Tabell 7.5 og 7.6; her oppsummeres koblingen til delproblemene"). **Potensielt 40–60 linjer spart**, men risiko for brudd med malens formelle krav.
- [ ] **recipients.yaml-utdrag i kap 6 (linje 514).** Vurder å flytte til vedlegg (kap 12). **~15 linjer spart.**
- [ ] **Kap 9 placeholder-blokker.** Skriv kun de som faktisk fyller en drøftingsfunksjon, slett resten.

### 🚫 Hva som ikke skal røres

- Kap 5.2.1 (fargenøkkelen) – kritisk for forståelse av datasettet
- Kap 6.3–6.4 (modellbeskrivelsen) – kjerne i hele rapporten
- Kap 7.6 (uke-til-uke-analysen) – eneste empiriske validering av modellverdi
- Tabell 5.2 (filterinnstillinger) og Tabell 5.3 (snapshot-serien) – nødvendige for reproduserbarhet
- Tabell/figur-numre etter renummerering – kontroller alle tekstreferanser etter sammenslåing

## Anbefalt rekkefølge i sluttspurten

1. **Rydding** (5 min): draftnotater + kap 4.7
2. **Kap 3-restrukturering** (15 min): slå sammen 3.1+3.2, 3.3+3.4
3. **Kap 4-restrukturering** (15 min): kollaps 4.5+4.6 inn i 4.4
4. **Kap 5+6 underseksjoner** (20 min)
5. **Kap 7/8-vurdering** (30 min): krever beslutning – diskuter før kutt
6. **Kap 9 placeholders** (15 min): fjern eller fyll

**Estimert total innsats: ~1,5 timer**
**Forventet kutt: 100–150 linjer (~12–17 %)**

## Sjekkliste etter kutt

- [ ] Alle tabell- og figurnumre renummeret konsistent
- [ ] Alle interne kryssreferanser oppdatert (Tabell X.Y, Figur X.Y, kap X.Y)
- [ ] Innholdsfortegnelse (hvis det finnes) regenerert
- [ ] Lest gjennom hele rapporten for å sjekke at sammenslåtte avsnitt flyter naturlig
- [ ] Rapportsjekkliste i AGENTS.md gått gjennom
