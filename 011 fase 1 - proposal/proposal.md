# Proposal LOG650

**Gruppemedlemmer:** David Johan Lunde og Tord Haakon Johnsen Hovden


**Område:** Kapasitetsplanlegging


**Bedrift (valgbart):** Motive AS (del av Motive Offshore Group), Stavanger


**Problemstilling:**

Hvordan kan et automatisert varslingssystem basert på data fra Power BI oppdage kapasitetsgap i Motive Offshores utleieflåte og varsle ansvarlig selger i tide?


**Data:**

Prosjektet har fått tilgang til reelle data fra Motive Offshore via Power BI. Følgende datatyper vil benyttes:

- **Power BI (supply/demand-tabell):** Ukentlig eksport som CSV med aggregerte gap-verdier per utstyrsklasse og uke, inkludert informasjon om kontrakter og ansvarlige selgere. Data er hentet fra Salesforce (salgsmuligheter og vinnersannsynlighet) og Asset Voice (flåteoversikt og tilgjengelighet), som begge er aggregert i Power BI.
- **Historiske kapasitetsgap:** Reelle tilfeller der etterspørsel har oversteget tilbud, hentet fra Power BI, for å validere varslingssystemet


**Beslutningsvariabler:**

- Varslingsterskel for vinnersannsynlighet: fast satt til 75 %
- Utstyrskategorier som overvåkes (Tier 2-nivå, f.eks. Winch, Cranes, Tensioner)
- Tidspunkt og kanal for automatisk varsling (e-post)
- Terskelverdi for hva som regnes som et kapasitetsgap (negativ supply/demand-verdi)


**Målfunksjon:**

Målet er å minimere antallet uoppdagede kapasitetsgap, der et gap defineres som en periode der etterspørsel fra prosjekter med ≥75 % vinnersannsynlighet overstiger tilgjengelig flåtekapasitet for en gitt utstyrskategori. Systemet skal ukentlig sammenligne supply/demand-data og automatisk varsle ansvarlig selger ved nye eller forverrede gap, slik at tiltak kan iverksettes i god tid.


**Avgrensninger:**

- Kun prosjekter med vinnersannsynlighet på 75 % eller høyere inkluderes i analysen
- Kun Tier 2-utstyrskategorier inngår i systemet
- Systemet dekker alle Motive Offshores kontorer og verksteder globalt, da enheter sendes mellom lokasjoner
- Systemet varsler om gap, men foreslår ikke løsninger, omallokering av utstyr eller alternative ressurser
- Prosjektet benytter reelle data fra Motive Offshore hentet via Power BI
- Direkte teknisk integrasjon mot live Salesforce- og Asset Voice-API er ikke en del av prosjektet – data hentes fra Power BI, der begge systemer allerede er aggregert. I et ferdig produkt vil systemet kunne kobles mot Power BI via REST API for automatisk datahenting
- SARIMA-baserte etterspørselsprognoser inngår ikke i løsningen; gap-deteksjonen er regelbasert med uke-til-uke-sammenligning av supply/demand-data
