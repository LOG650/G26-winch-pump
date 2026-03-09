# Proposal LOG650

**Gruppemedlemmer:** David Johan Lunde og Tord Haakon Johnsen Hovden


**Område:** Kapasitetsplanlegging


**Bedrift (valgbart):** Motive AS (del av Motive Offshore Group), Stavanger


**Problemstilling:**

Hvordan kan en KI-modell basert på data fra Salesforce og Asset Voice automatisk varsle om fremtidige kapasitetsgap i Motive Offshores utleiefloåte 3–6 måneder frem i tid?


**Data:**

Prosjektet har fått tilgang til reelle data fra Motive Offshore via Salesforce, Asset Voice og Power BI. Følgende datatyper vil benyttes:

- **Salesforce:** Historiske og pågående salgsmuligheter med tilhørende utstyrskrav, prosjektvarighet og vinnersannsynlighet (1 %, 25 %, 50 %, 75 %, 100 %)
- **Asset Voice:** Flåteoversikt per utstyrskategori (Tier 2) med status, sertifikatgyldighet og tilgjengelighet per uke
- **Kalenderdata:** Ukes- og månedsinndeling over en planleggingshorisont på minimum 6 måneder
- **Historiske kapasitetsgap:** Reelle tilfeller der etterspørsel har oversteget tilbud, hentet fra Power BI, for å validere varslingssystemet


**Beslutningsvariabler:**

- Varslingsterskel for vinnersannsynlighet: fast satt til 75 %
- Varslingshorisont: 3–6 måneder frem i tid
- Utstyrskategorier som overvåkes (Tier 2-nivå, f.eks. Winch, Cranes, Tensioner)
- Tidspunkt og kanal for automatisk varsling (e-post)


**Målfunksjon:**

Målet er å minimere antallet uoppdagede kapasitetsgap i planleggingshorisonten på 3–6 måneder, der et gap defineres som en periode der etterspørsel fra prosjekter med ≥75 % vinnersannsynlighet overstiger tilgjengelig flåtekapasitet for en gitt utstyrskategori. I tillegg måles antall dager i forveien et gap identifiseres, da en lengre ledetid gir større handlingsrom for Motive Offshore.


**Avgrensninger:**

- Kun prosjekter med vinnersannsynlighet på 75 % eller høyere inkluderes i analysen
- Kun Tier 2-utstyrskategorier inngår i modellen
- Modellen dekker alle Motive Offshores kontorer og verksteder globalt, da enheter sendes mellom lokasjoner
- Systemet varsler om gap, men foreslår ikke løsninger eller alternative ressurser
- Prosjektet benytter reelle data fra Motive Offshore hentet via Power BI
- Direkte teknisk integrasjon mot live Salesforce- og Asset Voice-API er ikke en del av prosjektet – data hentes fra Power BI, der begge systemer allerede er aggregert. I et ferdig produkt vil KI-modellen kunne kobles mot Power BI via REST API for automatisk datahenting
