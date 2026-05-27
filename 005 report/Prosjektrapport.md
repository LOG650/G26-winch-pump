

**Tittel (norsk og/eller engelsk)** 

Forfatter(e)

Totalt antall sider inkludert forsiden:      

Molde, Innleveringsdato

**Obligatorisk egenerklæring/gruppeerklæring** 

Den enkelte student er selv ansvarlig for å sette seg inn i hva som er lovlige hjelpemidler, retningslinjer for bruk av disse og regler om kildebruk. Erklæringen skal bevisstgjøre studentene på deres ansvar og hvilke konsekvenser fusk kan medføre. Manglende erklæring fritar ikke studentene fra sitt ansvar.

| *Du/dere fyller ut erklæringen ved å klikke i ruten til høyre for den enkelte del 1-6:* |  |  |
| :---- | :---- | :---- |
| **1\.** | **Jeg/vi erklærer herved at min/vår besvarelse er mitt/vårt eget arbeid, og at jeg/vi ikke har brukt andre kilder eller har mottatt annen hjelp enn det som er nevnt i besvarelsen.**  |  ☐ |
| **2\.** | **Jeg/vi erklærer videre at denne besvarelsen:**  ikke har vært brukt til annen eksamen ved annen avdeling/universitet/høgskole innenlands eller utenlands.  ikke refererer til andres arbeid uten at det er oppgitt. ikke refererer til eget tidligere arbeid uten at det er oppgitt.  har alle referansene oppgitt i litteraturlisten.  ikke er en kopi, duplikat eller avskrift av andres arbeid eller besvarelse.  |  ☐ |
| **3\.** | **Jeg/vi er kjent med at brudd på ovennevnte er å betrakte som fusk og kan medføre annullering av eksamen og utestengelse fra universiteter og høgskoler i Norge, jf. [Universitets- og høgskoleloven](http://www.lovdata.no/all/nl-20050401-015.html) §§4-7 og 4-8 og [Forskrift om eksamen](http://kvalitet.himolde.no/KS_UNL114) §§14 og 15\.**  |  ☐ |
| **4\.** | **Jeg/vi er kjent med at alle innleverte oppgaver kan bli plagiatkontrollert i URKUND, se [Retningslinjer for elektronisk innlevering og publisering av studiepoenggivende studentoppgaver](http://kvalitet.himolde.no/KS_UNL221)** |  ☐ |
| **5\.** | **Jeg/vi er kjent med at høgskolen vil behandle alle saker hvor det forligger mistanke om fusk etter høgskolens [retningslinjer for behandling av saker om fusk](http://kvalitet.himolde.no/KS_UNL409)** |  ☐ |
| **6\.** | **Jeg/vi har satt oss inn i regler og retningslinjer i bruk av [kilder og referanser på biblioteket sine nettsider](http://www.himolde.no/biblioteket/Sider/Veiledning/Kilder-og-referanser.aspx)** |  ☐ |

**Personvern**

**Personopplysningsloven**  
Forskningsprosjekt som innebærer behandling av personopplysninger iht. Personopplysningsloven skal meldes til Norsk senter for forskningsdata, NSD, for vurdering.

**Har oppgaven vært vurdert av NSD?**					☐**ja	 ☐nei**  
\- Hvis ja:   
**Referansenummer:      **  
\- Hvis nei:   
**Jeg/vi erklærer at oppgaven ikke omfattes av Personopplysningsloven:** ☐	

**Helseforskningsloven**  
Dersom prosjektet faller inn under Helseforskningsloven, skal det også søkes om forhåndsgodkjenning fra Regionale komiteer for medisinsk og helsefaglig forskningsetikk, REK, i din region.

**Har oppgaven vært til behandling hos REK?**				☐**ja	 ☐nei**  
\- Hvis ja:   
**Referansenummer:      **

**Publiseringsavtale**

**Studiepoeng:      **			  
**Veileder:      **  
			  
**Fullmakt til elektronisk publisering av oppgaven**  
Forfatter(ne) har opphavsrett til oppgaven. Det betyr blant annet enerett til å gjøre verket tilgjengelig for allmennheten (Åndsverkloven. §2).  
Alle oppgaver som fyller kriteriene vil bli registrert og publisert i Brage HiM med forfatter(ne)s godkjennelse.  
Oppgaver som er unntatt offentlighet eller båndlagt vil ikke bli publisert.

**Jeg/vi gir herved Høgskolen i Molde en vederlagsfri rett til å**   
**gjøre oppgaven tilgjengelig for elektronisk publisering:** 		☐**ja	 ☐nei**

**Er oppgaven båndlagt (konfidensiell)?					☐ja	 ☐nei**  
**(**Båndleggingsavtale må fylles ut)  
\- Hvis ja:   
**Kan oppgaven publiseres når båndleggingsperioden er over?		☐ja	 ☐nei**  
			  
**Dato:      **

**Antall ord:** Marker denne setningen, og skriv inn antall ord dersom det er et krav at antall ord skal oppgis. Hvis det ikke er et krav at antall ord skal oppgis slettes hele dette avsnittet, og i begge tilfeller slettes denne setning. 

**Forfattererklæring**: Marker denne setningen, og skriv inn forfattererklæring dersom det er et krav til oppgaven. Hvis det ikke er krav om forfattererklæring slettes hele dette avsnitt, og i begge tilfeller slettes denne setning. 

**Sammendrag**

Denne rapporten utvikler og demonstrerer et regelbasert varslingssystem som identifiserer kapasitetsgap i Motive Offshore Groups utleieflåte før de utløser dyre hasteløsninger som luftfrakt, fremleie eller nyanskaffelse. Systemet leser ukentlige Power BI-eksporter av flåtekapasitet og kontraktsetterspørsel som har passert Motives 75 %-vinnersannsynlighetsterskel, kombinerer en gap-verdi-regel med en regel basert på Power BIs egen prosentbaserte fargekode, og utløser strukturerte varsler som rutes til ansvarlig asset type-koordinator via daglige digest-e-poster. Pipelinen er bygget i Python, validert mot 50 syntetiske scenarier (alle passerer), og kjørt ende-til-ende på tre reelle snapshots fra Motive Norway-flåten (2026-05-07, 2026-05-14, 2026-05-21) som genererte 31 varsler fordelt på fem koordinatorer over to delta-par. Det viktigste empiriske funnet er at fem av ti varslingstråder som ble åpnet i første delta-par, lukkes automatisk i andre syklus – det første empiriske beviset på at livssyklusen *ny → påminnelse → løst* fungerer på reelle data. Studien viser at en bevisst regelbasert tilnærming, der probabilistisk usikkerhet allerede er innbakt i 75 %-filteret, kan flytte beslutningssyklusen fra en *pull*-modell der oppdagelse av kapasitetsgap er avhengig av at riktig person sjekker dashbordet til riktig tid, til en *push*-modell der digesten leveres til ansvarlig koordinator hver mandag.

**Nøkkelord:** kapasitetsstyring, regelbasert varslingssystem, supply chain, salgspipeline, offshore-utleie, beslutningsstøtte.

**Abstract**

This thesis develops and demonstrates a rule-based alerting system that identifies capacity gaps in Motive Offshore Group's rental fleet before they trigger costly emergency measures such as air freight, sub-leasing or unplanned procurement. The system reads weekly Power BI exports of fleet supply and contract demand that has passed Motive's 75 % win-probability threshold, combines a gap-value rule with a rule based on Power BI's own percentage-based colour key, and emits structured alerts routed to the responsible asset-type coordinator via daily digest emails. The pipeline is implemented in Python, validated against 50 synthetic scenarios (all passing), and executed end-to-end on three real snapshots from the Motive Norway fleet (2026-05-07, 2026-05-14, 2026-05-21), producing 31 alerts across five coordinators over two delta pairs. The principal empirical finding is that five of ten alert threads opened in the first delta pair are closed automatically in the second cycle – the first empirical evidence that the *new → reminder → resolved* lifecycle operates on real data. The study shows that a deliberately rule-based approach, in which probabilistic uncertainty is already embedded in the 75 % filter, can shift the decision cycle from a *pull* model dependent on the right person checking the dashboard at the right time, to a *push* model in which the digest is delivered to the responsible coordinator every Monday.

**Keywords:** capacity management, rule-based alerting, supply chain, sales pipeline, offshore rental, decision support.

Innhold

[**1.0 Innledning	9**](#innledning)

[1.1 Problemstilling	9](#problemstilling)

[1.2 Delproblemer	9](#delproblemer)

[1.3 Avgrensinger	10](#avgrensinger)

[1.4 Antagelser	10](#antagelser)

[**2.0 Litteratur	11**](#litteratur)

[2.1 Datadrevet kapasitetsstyring i supply chain	11](#2.1-datadrevet-kapasitetsstyring-i-supply-chain)

[2.2 Kapasitetsplanlegging og ressursutnyttelse	12](#2.2-kapasitetsplanlegging-og-ressursutnyttelse)

[2.3 Sales pipeline og vinnersannsynlighet som datagrunnlag	12](#2.3-sales-pipeline-og-vinnersannsynlighet-som-datagrunnlag)

[2.4 Automatiserte varslingssystemer	13](#2.4-automatiserte-varslingssystemer)

[**3.0 Teori	13**](#teori)

[3.1 Kapasitetsstyring og ressursbalanse	14](#3.1-kapasitetsstyring-og-ressursbalanse)

[3.2 Tilgjengelighet og kapasitetsgap	14](#3.2-tilgjengelighet-og-kapasitetsgap)

[3.3 Regelbasert varslingslogikk	15](#3.3-regelbasert-varslingslogikk)

[**4.0 Casebeskrivelse	16**](#casebeskrivelse)

[4.1 Motive Offshore Group	16](#4.1-motive-offshore-group)

[4.2 Utleieflåten og utstyrsklasser	16](#4.2-utleieflåten-og-utstyrsklasser)

[4.3 Salgs- og bookingprosessen	17](#4.3-salgs--og-bookingprosessen)

[4.4 Hvordan kapasitetsgap blir oversett, konsekvenser og påvirkende faktorer	17](#4.4-hvordan-kapasitetsgap-blir-oversett)

[4.5 Datagrunnlag	18](#4.5-datagrunnlag)

[**5.0 Metode og data	19**](#metode-og-data)

[5.1 Metode	19](#metode)

[5.1.1 Validitet, reliabilitet og etiske hensyn	19](#5.1.1-validitet-reliabilitet-og-etiske-hensyn)

[5.2 Data	20](#data)

[5.2.1 Datakilder og filtrering	20](#5.2.1-datakilder-og-filtrering)

[5.2.2 Datafangst	21](#5.2.2-datafangst)

[5.2.3 Datasett og kvalitet	22](#5.2.3-datasett-og-kvalitet)

[**6.0 Modellering	23**](#modellering)

[6.1 Oversikt over modellen	23](#6.1-oversikt-over-modellen)

[6.2 Inndata og forhåndsfiltrering	24](#6.2-inndata-og-forhåndsfiltrering)

[6.3 Statisk gap-deteksjon	24](#6.3-statisk-gap-deteksjon)

[6.4 Uke-til-uke-deltadeteksjon	26](#6.4-uke-til-uke-deltadeteksjon)

[6.5 Suppression og eksklusjon	27](#6.5-suppression-og-eksklusjon)

[6.6 Varselsutløsing og ruting	29](#6.6-varselsutløsing-og-ruting)

[**7.0 Analyse	31**](#analyse)

[7.1 Distribusjon av gap-verdier	31](#7.1-distribusjon-av-gap-verdier)

[7.2 Gap-utviklingen over kalenderhorisonten	32](#7.2-gap-utviklingen-over-kalenderhorisonten)

[7.3 Sammenligning på tvers av asset types	33](#7.3-sammenligning-på-tvers-av-asset-types)

[7.4 De mest utsatte utstyrsenhetene	34](#7.4-de-mest-utsatte-utstyrsenhetene)

[7.5 Front-lastet underskudd og inaktive utstyrsenheter	35](#7.5-front-lastet-underskudd-og-inaktive-utstyrsenheter)

[7.6 Uke-til-uke-analyse	36](#7.6-uke-til-uke-analyse)

[7.6.1 Andre delta-par 2026-05-14 ↔ 2026-05-21	38](#7.6.1-andre-delta-par)

[7.6.2 Varslingstråder over to delta-par	39](#7.6.2-varslingstråder-over-to-delta-par)

[**8.0 Resultat	41**](#resultat)

[8.1 Statisk gap-deteksjon på baseline-snapshot	41](#8.1-statisk-gap-deteksjon-på-baseline-snapshot)

[8.2 Uke-til-uke-deltadeteksjon	42](#8.2-uke-til-uke-deltadeteksjon)

[8.3 Krysstabulering: endringstype × magnitudeklasse	43](#8.3-krysstabulering)

[8.4 Varselsutløsing og prioritering	45](#8.4-varselsutløsing-og-prioritering)

[8.4.1 Demonstrasjon av SMTP-leveranse	47](#8.4.1-demonstrasjon-av-smtp-leveranse)

[8.5 Validering mot syntetiske scenarier	49](#8.5-validering-mot-syntetiske-scenarier)

[**9.0 Diskusjon	51**](#diskusjon)

[9.1 Drøfting mot problemstillingen og delproblemene	51](#9.1-drøfting-mot-problemstillingen-og-delproblemene)

[9.2 Sammenligning mot litteraturen	52](#9.2-sammenligning-mot-litteraturen)

[9.3 Modellens robusthet og begrensninger	53](#9.3-modellens-robusthet-og-begrensninger)

[9.4 Datafangstmetodens påvirkning på resultatene	54](#9.4-datafangstmetodens-påvirkning-på-resultatene)

[9.5 Praktisk betydning og generaliserbarhet	55](#9.5-praktisk-betydning-og-generaliserbarhet)

[9.6 Forslag til videre forskning	57](#9.6-forslag-til-videre-forskning)

[**10.0 Konklusjon	58**](#konklusjon)

[**11.0 Bibliografi	59**](#bibliografi)

[**12.0 Vedlegg	60**](#vedlegg)

[Vedlegg A: KI-bruk-erklæring	60](#vedlegg-a-ki-bruk-erklæring)

[Vedlegg B: Konfidensialitet	60](#vedlegg-b-konfidensialitet)

[Vedlegg C: Kravmatrise	60](#vedlegg-c-kravmatrise)

[Vedlegg D: Komplette SMTP-digester fra demo 2026-05-23	60](#vedlegg-d-komplette-smtp-digester)

[Vedlegg E: Full valideringsscenario-tabell	62](#vedlegg-e-full-valideringsscenario-tabell)

[Vedlegg F: Varselsobjekt-skjema	63](#vedlegg-f-varselsobjekt-skjema)

# **1. Innledning**

Effektiv kapasitetsstyring er avgjørende i kapitalintensive bransjer der spesialisert utstyr utgjør kjerneressursen. Innen offshore marine- og løfteutstyrsutleie må selskaper kontinuerlig balansere tilgjengelig flåte mot innkommende prosjektetterspørsel som er balansegang som direkte påvirker både lønnsomhet og kundetilfredshet. Når investeringssyklusene i olje, gass og fornybar energi svinger, blir evnen til å reagere proaktivt på endringer i salgspipelinen en kritisk suksessfaktor.

Dette prosjektet faller innenfor datadrevet kapasitetsstyring og kapasitetsplanlegging, hvor prosjektet knytter salgsdata fra CRM-systemer sammen med flåtens tilgjengelighetsdata for å forbedre denne balansen. Ved å overvåke når salgsmuligheter når en høy vinnersannsynlighet, og automatisk identifisere potensielle kapasitetsgap i den relevante bookingperioden, søker vi å utvikle et regelbasert varslingssystem som kan gi bedre beslutningsstøtte enn dagens manuelle prosesser. Rapporten er skrevet i samarbeid med Motive Offshore Group, et internasjonalt selskap som leier ut offshore-utstyr på tvers av fem regioner.

Studiens betydning er først og fremst operasjonell og økonomisk: i dagens manuelle prosess oppdages kapasitetsgap ofte tett opp mot leveransedato, og marginen forsvinner i hastetiltak som luftfrakt, fremleie fra ekstern leverandør eller nyanskaffelse av utstyr (jf. 4.4). Tidligere deteksjon, allerede når en kontrakt passerer 75 %-terskelen i Salesforce, gir selger og koordinator handlingsrom til å gjennomføre planlagte tiltak fremfor reaktive hasteløsninger, og er den direkte motivasjonen for varslingssystemet som utvikles i denne rapporten.

## **1.1 Problemstilling**

“Hvordan kan et Python-basert varslingssystem bruke ukentlige Power BI-eksporter til å identifisere negative kapasitetsverdier og endringer i Asset Calendar, og automatisk varsle selgere og prosjektkoordinatorer om kapasitetsgap i Motive Offshores utleieflåte?”

## **1.2 Delproblemer**

For å svare på hovedproblemstillingen er prosjektet delt inn i følgende delproblemer:

1. Hvordan kan data fra Salesforce, Asset Voice og Power BI struktureres for å identifisere kapasitetsgap per asset og tidsperiode?  
2. Hvordan kan regelbasert logikk brukes til å oppdage negative verdier, forverrede verdier og endringer fra én uke til neste?  
3. Hvordan kan et automatisk varsel utformes slik at selger eller prosjektkoordinator får tydelig informasjon om assets, periode og gap?  
4. I hvilken grad gir systemet tidligere og tydeligere varsling enn dagens manuelle kontrollprosess?

## **1.3 Avgrensinger**

Prosjektet er avgrenset på følgende områder for å sikre en målrettet analyse:

* Varslingssystemet begrenses til utleieutstyr (rentals) og dekker ikke engineering- eller inspeksjonstjenester, da disse har andre bookingmønstre og kapasitetsstrukturer som krever egne tilnærminger.  
* Systemet bygger på CSV-eksporter fra Power BI, ikke direkte integrasjon mot Salesforce og Asset Voice. Dette fordi direkte API-tilgang faller utenfor prosjektets omfang og krever IT-godkjenninger som ikke er tilgjengelig i prosjektperioden.  
* Terskelverdien er satt til 75 prosent vinnersannsynlighet, i tråd med Motives eksisterende pipeline-klassifisering der dette stadiet representerer en meget sterk mulighet. Analysen undersøker ikke alternative terskelverdier.  
* Prosjektet fokuserer på gapdeteksjon og varsling, ikke på å foreslå løsninger for hvordan kapasitetsgapene skal håndteres. Selve håndteringen, som for eksempel omallokering av utstyr mellom regioner eller innleie fra tredjeparter, er operasjonelle beslutninger som ligger hos Motive.  
* Modellen tar ikke hensyn til vedlikeholdsplanlegging eller transporttid mellom regioner, da disse variablene ikke er tilgjengelig i datagrunnlaget fra Power BI.

## **1.4 Antagelser**

For å kunne gjennomføre analysen og modelleringen er følgende forutsetninger lagt til grunn:

* Det antas at dataene i Salesforce gjenspeiler den faktiske statusen på salgsmulighetene, altså at selgerne oppdaterer vinnersannsynligheten løpende og korrekt. Dersom dette ikke er tilfellet, vil varslingssystemet enten trigge for sent eller ikke i det hele tatt, noe som reduserer systemets praktiske verdi.  
* Det antas at flåtedataene fra Asset Voice er oppdaterte med tanke på tilgjengelighet og status. Utstyr som er registrert som tilgjengelig antas å faktisk være klart for utleie. I praksis kan det oppstå forsinkelser i statusoppdateringer, noe som betyr at systemet kan undervurdere antall konflikter.  
* Det antas at vinnersannsynligheten på 75 prosent er en pålitelig indikator på at en kontrakt er nær avslutning, i tråd med Motives interne retningslinjer for pipeline-klassifisering. Dette gjør at systemet kan fokusere ressursene på de mest sannsynlige kontraktene i stedet for å varsle på alle muligheter i pipelinen.  
* Det antas at endringer i etterspørsel og tilgjengelig kapasitet blir fanget opp i Power BI ved neste ukentlige oppdatering.

# **2. Litteratur**

Dette kapittelet tar for seg relevant forskning og faglitteratur som danner grunnlaget for rapportens problemstilling. Litteraturen brukes til å forklare hvordan datadrevet kapasitetsstyring, kapasitetsplanlegging, sales pipeline-data og automatiserte varslingssystemer kan knyttes sammen i en praktisk beslutningsstøttemodell. Kapittelet viser dermed hvordan tidligere forskning støtter valget av metode og gir et faglig grunnlag for videre teori, modellering og analyse.

## **2.1 Datadrevet kapasitetsstyring i supply chain**

Datadrevet kapasitetsstyring handler om å bruke oppdaterte og strukturerte data som grunnlag for bedre planlegging og raskere beslutninger i supply chain. Xu et al. (2023) viser at big data analytics kan forbedre supply chain planning gjennom bedre nøyaktighet, kortere responstid og økt fleksibilitet. De peker også på at en viktig effekt av slike datadrevne løsninger er prosessoptimalisering og automatisering. Dette er relevant for denne rapporten fordi Power BI allerede samler supply/demand-data fra Salesforce og Asset Voice, men verdien oppstår først når dataene brukes aktivt til å oppdage kapasitetsgap. Koot et al. (2021) viser på samme måte at IoT og big data analytics kan støtte beslutningstaking i supply chain ved å koble operative data til mer systematisk overvåking og beslutningsstøtte. Denne rapporten bygger videre på denne litteraturen ved å utvikle et regelbasert system som ikke bare visualiserer kapasitet, men automatisk identifiserer nye eller forverrede gap og varsler ansvarlig selger. Dermed plasserer prosjektet seg innen datadrevet kapasitetsstyring, med fokus på praktisk bruk av eksisterende data fremfor avansert prediksjonsmodellering. 

## **2.2 Kapasitetsplanlegging og ressursutnyttelse**

Kapasitetsplanlegging handler i stor grad om å sikre at riktige ressurser er tilgjengelige når etterspørselen oppstår. I maritim logistikk blir dette ekstra krevende fordi ressursene ofte er kostbare, geografisk spredt og bundet opp i prosjekter over tid. Wang og Zhen (2025) viser hvordan usikker etterspørsel påvirker beslutninger om flåteplassering og kapasitetsallokering i maritim logistikk. Dette er relevant for Motive Offshore, siden selskapet må vurdere om tilgjengelig utstyr i riktig region er tilstrekkelig til å dekke fremtidige kontrakter. Dersom kapasitetsgap oppdages for sent, kan konsekvensen bli dyre hasteløsninger, som flyfrakt, fremleie eller omdisponering fra andre lokasjoner.

Et lignende poeng kommer frem i forskning på leasingstrategier for fergekapasitet, der etterspørsels-usikkerhet påvirker hvordan kapasitet bør planlegges og utnyttes over tid (Cheng et al., 2025). Selv om studien gjelder ferger, er den overførbar til denne rapporten fordi begge kontekster handler om kapitalintensive ressurser som må disponeres før behovet faktisk oppstår. Sonnleitner et al. (2025) trekker også frem at prognoser ofte fungerer som grunnlag for senere planleggings- og optimaliseringsbeslutninger i transportlogistikk. Denne rapporten bygger videre på denne tankegangen, men med et mer avgrenset formål: modellen skal ikke optimalisere hele flåteallokeringen, men varsle når forventet etterspørsel overstiger tilgjengelig kapasitet. Dermed brukes kapasitetsplanlegging som beslutningsstøtte, ikke som en fullt automatisk styringsmodell.

## **2.3 Sales pipeline og vinnersannsynlighet som datagrunnlag**

Sales pipeline-data kan brukes som mer enn bare en oversikt over mulige salg. I B2B-markeder kan slike data også fungere som et tidlig signal om hvilke fremtidige behov bedriften bør forberede seg på. González-Flores et al. (2025) viser hvordan maskinlæring og CRM-data kan brukes til lead scoring, der målet er å prioritere de salgsmulighetene som har høyest sannsynlighet for å konvertere til faktiske kunder. Studien peker på at dette kan hjelpe salgsorganisasjoner med å bruke tid og ressurser mer effektivt, fordi de får bedre grunnlag for å vurdere hvilke leads som bør følges opp først.

Dette er relevant for denne rapporten fordi Motive Offshore allerede bruker vinnersannsynlighet i Salesforce som en del av sin salgsprosess. Når en kontrakt når 75 % sannsynlighet, kan dette tolkes som et sterkt signal om kommende etterspørsel, ikke bare som en salgsindikator. Rapporten bygger videre på denne tankegangen ved å koble salgsdata til kapasitetsdata fra utleieflåten. I stedet for at vinnersannsynligheten kun brukes til å prioritere salgsarbeid, brukes den her som en trigger for å undersøke om fremtidig etterspørsel kan skape kapasitetsgap. Dermed blir sales pipeline-data en del av beslutningsstøtten for kapasitetsplanlegging, ikke bare et verktøy for salgsoppfølging.

## **2.4 Automatiserte varslingssystemer**

Et varslingssystem har størst verdi når det gjør data om til et beslutningsgrunnlag som brukerne kan handle på. Koot et al. (2021) viser i sin litteraturgjennomgang at IoT og big data analytics kan støtte beslutningstaking i supply chain ved å koble data fra fysiske objekter og operasjonelle prosesser inn i planleggingsarbeidet. Dette er relevant for denne rapporten fordi Motive Offshore har data fra både Salesforce og Asset Voice, men utfordringen ligger i å bruke disse dataene mer proaktivt. I stedet for at selgere og prosjektkoordinatorer manuelt må kontrollere kapasitet, kan et automatisert system gjøre analysen tidligere og mer systematisk.

Sonnleitner et al. (2025) peker på at prognoser i transportlogistikk ofte brukes som input til videre planlegging og optimalisering, altså at prediksjoner først får praktisk verdi når de kobles til beslutninger. Denne rapporten bygger på samme tankegang, men med et mer avgrenset formål. Målet er ikke å automatisere alle beslutninger om flåteallokering, men å varsle når forventet etterspørsel overstiger tilgjengelig kapasitet. Varslingssystemet fungerer derfor som beslutningsstøtte: det gir brukerne tidligere informasjon om mulige kapasitetsgap, slik at de kan vurdere tiltak før problemet blir akutt.

# **3. Teori**

Dette kapittelet presenterer det teoretiske rammeverket for metodevalg og modellering. Tidligere forskning er behandlet i litteraturkapittelet, mens den konkrete modellen beskrives i kapittel 6.

## **3.1 Kapasitetsstyring og ressursbalanse**

Kapasitetsstyring handler om å balansere tilgjengelige ressurser mot etterspørsel innenfor en gitt tidsperiode, og er en sentral disiplin i operations management og supply chain-faget (Rajani & Heggde, 2020). For lav kapasitet gir forsinkelser, tapte inntekter og dyre hastetiltak; for høy kapasitet gir lav ressursutnyttelse og økte kostnader (Cheng et al., 2025; Wang & Zhen, 2025).

I et utleiebasert system uttrykkes ressursbalansen som forholdet mellom tilgjengelig kapasitet og etterspørsel:

$$G_{r,a,t} = S_{r,a,t} - D_{r,a,t}$$

der $G_{r,a,t}$ er kapasitetsbalansen, $S_{r,a,t}$ er tilgjengelig kapasitet, og $D_{r,a,t}$ er etterspørsel for region $r$, utstyrsklasse $a$ og tidsperiode $t$. Dersom $G_{r,a,t} < 0$, overstiger etterspørselen tilgjengelig kapasitet og det oppstår et kapasitetsgap.

## **3.2 Tilgjengelighet og kapasitetsgap**

Tilgjengelighet beskriver hvor mye kapasitet som faktisk kan brukes i en bestemt periode. I et utleiebasert system er ikke alt utstyr tilgjengelig samtidig fordi enkelte enheter allerede kan være leid ut, reservert eller bundet til andre oppdrag, og kapasitetsvurderingen må ta hensyn til både eksisterende forpliktelser og nye behov (Oliveira et al., 2017). Et kapasitetsgap oppstår når

$$S_{r,a,t} < D_{r,a,t}.$$

Slike gap er særlig viktige å oppdage tidlig fordi tiltak som omdisponering, innleie eller nyanskaffelse krever planleggingstid (Koot et al., 2021; Xu et al., 2023). Dersom et gap først oppdages nær leveransedato, svekkes servicenivået fordi virksomheten må bruke hastetiltak for å levere som planlagt – og det er nettopp denne avveiingen mellom kapasitet, gap og servicenivå som motiverer behovet for tidlig deteksjon.

## **3.3 Regelbasert varslingslogikk**

Regelbasert varslingslogikk innebærer at systemet bruker faste betingelser for å avgjøre når et varsel skal utløses. I stedet for å predikere fremtidig etterspørsel kontrollerer systemet om bestemte forhold er oppfylt i datagrunnlaget. En slik tilnærming, der varsler utløses ved at observerte verdier krysser forhåndsdefinerte terskler, omtales i nyere supply chain-litteratur som en *baseline probabilistic alert system* og brukes typisk som referansemodell for mer avanserte IoT- og prognosebaserte varslingssystemer (Alaoua & Karim, 2025). Til forskjell fra prediktive prognosemodeller (Sonnleitner et al., 2025) tar regelbaserte løsninger utgangspunkt i det som faktisk står i datagrunnlaget, og er hensiktsmessige når underliggende usikkerhet allerede er reflektert i et eksisterende sannsynlighetsfilter – som 75 %-terskelen i Motives pipeline.

Formålet er å oppdage kapasitetsgap basert på oppdaterte data, slik at organisasjonen får tidlig varsel før gapene materialiserer seg som operative problemer (Qi et al., 2022). Et varsel utløses når tilgjengelig kapasitet ikke dekker etterspørselen og behovet samtidig vurderes som relevant nok til å kreve oppfølging:

$$A_{r,a,t} = 1 \text{ hvis } G_{r,a,t} < 0 \text{ og } p_j \geq 0{,}75$$

der $A_{r,a,t} = 1$ markerer at et varsel utløses og $p_j$ er vinnersannsynligheten for kontrakt $j$. Samlet gir teorien et grunnlag for metode- og modellkapittelet: kapasitetsstyring forklarer hvorfor supply og demand må sammenlignes, kapasitetsgap forklarer hva systemet skal oppdage, og regelbasert varslingslogikk forklarer hvorfor løsningen kan bygges som en kontrollmodell fremfor en prediksjonsmodell.

# **4. Casebeskrivelse**

Dette kapittelet beskriver Motive Offshore Group som case, med vekt på utleieflåten, dataøkosystemet rundt Salesforce, Asset Voice og Power BI, og hvordan kapasitetsgap oppstår og blir oversett i dagens manuelle prosess. Hensikten er å gi den operasjonelle konteksten som gjør problemstillingen relevant.

## **4.1 Motive Offshore Group**

Motive Offshore Group er et internasjonalt selskap som leier ut spesialisert offshore-utstyr til aktører innen olje, gass og fornybar energi. Selskapet opererer i fem regioner og tilbyr utleieutstyr som winches, pumper og løfteutstyr til marine operasjoner. Virksomheten er kapitalintensiv – den enkelte enhet representerer en stor investering, og flåtens utnyttelsesgrad er direkte bestemmende for selskapets inntjening.

Motives kunder er typisk operatører og entreprenørselskaper innen offshoresektoren som har behov for spesialisert utstyr over en avgrenset prosjektperiode. Kontrakter inngås som regel måneder i forveien, og etterspørselen varierer med aktivitetsnivået i olje, gass og fornybar energi. Svingninger i disse investeringssyklusene fører til perioder med høy etterspørsel og kapasitetspress, men også til perioder med lav utnyttelse.

## **4.2 Utleieflåten og utstyrsklasser**

Flåten er organisert etter utstyrsklasse og region. Hver utstyrsklasse består av et antall enheter, og tilgjengeligheten til disse enhetene varierer fra uke til uke avhengig av eksisterende bookinger, sertifikatstatus og annet. En enhet som allerede er leid ut, reservert for vedlikehold eller under sertifisering, er ikke tilgjengelig for nye kontrakter.

Kapasitet måles som antall tilgjengelige enheter per utstyrsklasse per region per uke. Fordi utstyr er geografisk plassert i én av de fem regionene, og ikke kan flyttes fritt uten ekstra kostnad og planleggingstid, er tilgjengeligheten regionsspesifikk. Et kapasitetsgap i én region kan derfor ikke uten videre dekkes av ledig kapasitet i en annen. Region *Motive Norway*, som er datagrunnlaget i denne rapporten, tilsvarer i praksis ett fysisk verksted lokalisert i Stavanger.

## **4.3 Salgs- og bookingprosessen**

Motive Offshore bruker Salesforce som CRM-system for å følge opp salgsmuligheter. Hver salgsmulighet er knyttet til en ønsket utstyrsklasse, region og tidsperiode, og tildeles en vinnersannsynlighet som oppdateres av selger i takt med kontraktsprosessen. Internt bruker Motive 75 prosent vinnersannsynlighet som terskel for at en kontrakt vurderes som svært sannsynlig.

Flåtens tilgjengelighet styres i Asset Voice, som er Motives system for flåteforvaltning. Asset Voice holder oversikt over hvilke enheter som er tilgjengelige, leid ut, under sertifisering eller avsatt til vedlikehold. De to datasettene – etterspørsel fra Salesforce og tilbud fra Asset Voice – samles i et Power BI-dashbord som presenterer en aggregert supply/demand-oversikt per utstyrsklasse, region og uke. Negative verdier i dette dashbordet betyr at etterspørselen overstiger tilgjengelig kapasitet, altså at det foreligger et kapasitetsgap.

I dag skjer overvåkingen av kapasitetsgap manuelt. Selgere og prosjektkoordinatorer må selv sjekke Power BI-dashbordet og vurdere om en salgsmulighet som nærmer seg kontraktsinngåelse vil skape konflikt med eksisterende bookinger. Det finnes ingen automatisk varsling, og oppdagelsen av et gap er derfor avhengig av at riktig person sjekker dataene til riktig tid.

## **4.4 Hvordan kapasitetsgap blir oversett, konsekvenser og påvirkende faktorer**

Selv om Power BI-dashbordet gjør det mulig å oppdage kapasitetsgap manuelt, viser den daglige driften at ressursprioritering kan føre til at gap fremover i tid ikke blir fulgt opp i tide. Når en selger oppdaterer en kontrakt til 75 prosent vinnersannsynlighet, kontrollerer hen typisk dashbordet for den aktuelle leveranseperioden, og resultatet er enten **tilstrekkelig kapasitet** (ingen tiltak nødvendig) eller et **kapasitetsgap** flere måneder frem i tid – som selgeren noterer seg, men utsetter beslutning om fordi det vurderes som tid nok til å finne en løsning senere. Mellom kontraktsoppdatering og leveranse jobber selgerne videre med andre kunder med kortere tidshorisont (typisk én til fire uker) som har høyere prioritet fordi tiden til å reagere er kortere. Konsekvensen er at det første gapet kan forbli urørt i flere måneder uten at noen aktivt tar ansvar for å løse det, og når leveransedatoen for den opprinnelige kontrakten nærmer seg, er handlingsrommet vesentlig redusert.

Når et kapasitetsgap først oppdages tett opp mot leveransedato, finnes i hovedsak tre mulige tiltak: **bygge nytt utstyr** (produksjonstid ~4 måneder, sjelden mulig sent), **sende utstyr fra annen lokasjon** (krever ofte luftfrakt som er flere ganger dyrere enn sjøtransport) eller **fremleie fra ekstern leverandør** (innleiekostnader reduserer marginen). I tilfeller hvor gapet kunne vært oppdaget tre til seks måneder tidligere, dekkes en ellers unngåelig kostnad av Motive selv – kunden aksepterer normalt ikke ekstra fraktkostnader eller innleiepåslag som ikke var avtalt på forhånd. Tidlig og automatisk varsling gir derfor selgeren tid til å gjennomføre planlagte tiltak fremfor reaktive hasteløsninger, og er den direkte motivasjonen for varslingssystemet som utvikles i denne rapporten.

Fire faktorer er særlig relevante for hvorvidt kapasitetsgap oppstår og om de oppdages i tide: **salgsmulighetenes fremdrift** (når en kontrakt passerer 75 % vinnersannsynlighet, er behovet meget sannsynlig), **eksisterende bookinger** (utstyr leid ut eller reservert reduserer tilgjengelig kapasitet), **geografi** (utstyr er regionslokalisert og kan ikke omdisponeres uten planleggingstid) og **oppdateringsfrekvens** (Power BI oppdateres ukentlig, så endringer i Salesforce eller Asset Voice fanges først opp ved neste snapshot).

## **4.5 Datagrunnlag**

Datagrunnlaget for prosjektet er ukentlige snapshots fra Motive Offshores Power BI-rapport *Supply vs Demand*, som aggregerer etterspørsel fra Salesforce og tilgjengelighet fra Asset Voice; full beskrivelse av datakilder, filterprofil, datafangstmetode og datasettets omfang følger i kapittel 5.2.

# **5. Metode og data**

Dette kapittelet redegjør for det metodiske rammeverket prosjektet bygger på, og dokumenterer datagrunnlaget som ligger til grunn for modellering og analyse. Hensikten er at beskrivelsen skal være presis nok til at en uavhengig leser kan reprodusere både datafangsten og analysen.

## **5.1 Metode**

Prosjektet følger et kvantitativt, anvendt forskningsdesign med en casebasert tilnærming. Motive Offshore brukes som case fordi prosjektet undersøker et konkret kapasitetsproblem i én virksomhet. Analysen bygger på strukturerte Power BI-eksporter med numeriske kapasitetsverdier, etterspørsel og endringer over tid.

Prosjektet har et pragmatisk forskningsperspektiv, der metodevalget er styrt av hva som best svarer på problemstillingen. Formålet er ikke å utvikle en generell statistisk modell, men å undersøke hvordan eksisterende data fra Salesforce, Asset Voice og Power BI kan brukes til å oppdage kapasitetsgap og varsle ansvarlige personer tidligere enn dagens manuelle prosess.

Metoden består av tre hovedtrinn. Først kartlegges og klargjøres CSV-eksporter fra Power BI slik at dataene kan behandles i Python. Deretter utvikles regelbasert logikk som identifiserer negative kapasitetsverdier, forverrede verdier og endringer fra én uke til neste. Til slutt genereres varsel dersom systemet finner et kapasitetsgap som krever oppfølging.

Analysemetoden er regelbasert kvantitativ analyse. Systemet bruker ikke regresjon, maskinlæring eller tidsserieprognoser, men kontrollerer om definerte betingelser er oppfylt i datagrunnlaget. Denne tilnærmingen passer fordi prosjektet handler om å oppdage og varsle kapasitetsgap, ikke å optimalisere flåteallokering eller predikere etterspørsel.

Implementeringen gjennomføres i Python. KI-verktøy brukes som støtte til kodeforslag, feilsøking og dokumentasjon, men ikke som selvstendig analysemodell. Alle metodiske valg og vurderinger gjøres av prosjektgruppen.

Metodiske begrensninger er hovedsakelig knyttet til datakvalitet og oppdateringsfrekvens. Systemet forutsetter at dataene i Salesforce, Asset Voice og Power BI er korrekte og oppdaterte. Prosjektet identifiserer og varsler kapasitetsgap, men vurderer ikke hvilke tiltak Motive Offshore bør gjennomføre for å løse gapet.

### **5.1.1 Validitet, reliabilitet og etiske hensyn**

**Validitet.** Modellen måler det den manuelle prosessen i 4.4 faktisk reagerer på: både den avrundede gap-verdien $G_{r,a,t}$ og fargeklassen `severity_band` som Power BIs *Colour Key* tildeler hver celle. Konstruktvaliditeten styrkes av at fargeklassen kodes direkte fra Power BI-rapporten selgere og koordinatorer bruker i dag, slik at terskelen modellen utløser på er identisk med terskelen brukeren visuelt reagerer på. Eksternvaliditet er avgrenset til Motive Norway-flåten innenfor 75 %+-vinduet; generaliserbarhet til andre verksteder og bransjer drøftes i 9.5.

**Reliabilitet.** Datafangsten skjer via manuell transkripsjon av PNG-bilder (5.2.2), noe som introduserer risiko for avlesningsfeil. Reliabiliteten sikres ved automatisk sumsjekk mot Power BIs egne asset type- og `Totalt`-rader med en toleranse på $\pm 2$ unit-uker per uke (5.2.3), som reflekterer den strukturelle avrundingsstøyen Power BI selv produserer. Snapshots som overstiger toleransen avvises og kontrolleres mot kildebildet før godkjenning. Modellens regelbaserte og deterministiske natur (6.1) gjør at den samme inndatamengden alltid produserer samme varselsmengde, slik at reliabiliteten i analyse-leddet er full.

**Etiske hensyn.** Datagrunnlaget inneholder kommersielt sensitiv informasjon om Motives kunder, kontrakter og flåteutnyttelse. Prosjektgruppen fikk tilgang til Power BI-rapporten gjennom Motive Offshore med en muntlig forståelse om at tallene er konfidensielle. Det er ikke inngått skriftlig taushetserklæring, men prosjektgruppen behandler dataene som konfidensielle: hele datakatalogen `004 data/` er ekskludert fra versjonskontroll for å hindre utilsiktet eksponering. Rapporten gjengir aggregerte tall og anonymiserte asset type-navn, ikke kundenavn eller kontrakts-id-er. KI-verktøy (Anthropic Claude) er brukt som støtte til kodeforslag, feilsøking og språkvask, men ikke som selvstendig analysemodell eller til behandling av rådata utover offentlig dokumentert API-bruk – jf. KI-bruk-erklæringen i Vedlegg A.

## **5.2 Data**

### **5.2.1 Datakilder og filtrering**

Datagrunnlaget for prosjektet er hentet fra Motive Offshores Power BI-rapport *Supply vs Demand*. Rapporten aggregerer flåtens tilgjengelighet fra Asset Voice og etterspørsel fra Salesforce til en samlet supply/demand-oversikt per utstyrskategori, region og uke. Som primær datakilde brukes rapportsiden **Supply/ Demand – Calendar**, som viser ukentlig kapasitetsbalanse per Tier 2-utstyrsenhet over de neste 8 månedene. Hver celle viser supply minus demand som heltall, der negative verdier representerer kapasitetsgap.

I tillegg til tallverdien er hver celle bakgrunns-fargekodet i én av fem klasser fra Power BI-rapportens egen *Colour Key*. Fargen koder ikke gap-verdien direkte, men **forholdet mellom gap og demand** – det vil si hvor stor andel av etterspørselen som mangler eller overdekkes. Klassene er gjengitt i Tabell 5.1.

<div align="center">
  <img src="../004 data/fargekode.png" alt="Power BI Colour Key for Supply vs Demand" width="40%">
  <p align="center"><small><i>Figur 5.1 Power BI-rapportens Colour Key for Supply/ Demand – Calendar, gjengitt fra rapportgrensesnittet.</i></small></p>
</div>

| Farge | Tilstand | Prosent av demand | Operasjonell tolkning |
|-------|----------|--------------------|------------------------|
| Grønn | Supply > Demand | $\geq 25\,\%$ overdekning | God margin, ingen handling |
| Gul | Supply > Demand | $10\,\%-25\,\%$ overdekning | Komfortabel, men begrenset margin |
| Rød | Supply > Demand | $0\,\%-10\,\%$ overdekning | Tett – nær balanse, sårbart for små forstyrrelser |
| Lilla | Demand > Supply | $0\,\%-50\,\%$ underdekning | Reelt gap som må håndteres |
| Svart | Demand > Supply | $\geq 50\,\%$ underdekning | Alvorlig underdekning – kritisk |

<p align="center"><small><i>Tabell 5.1 Fargekoder fra Power BI Colour Key med tilhørende prosent-intervaller og operasjonell tolkning.</i></small></p>

Skillet mellom gap-verdi og farge er operasjonelt betydningsfullt fordi **samme gap-verdi kan tilsvare ulik farge avhengig av underliggende demand**. For eksempel vil $G = -2$ med demand $= 10$ gi 20 % underdekning (lilla), mens $G = -2$ med demand $= 3$ gir 67 % underdekning (svart). Det er fargen, ikke gap-verdien alene, som selgere og prosjektkoordinatorer reagerer på i den daglige bruken av dashbordet. Datasettet i dette prosjektet fanger derfor begge attributtene per celle, lagret som `gap_value` (heltall) og `severity_band` (kategorisk) i den transkriberte CSV-en. Skjemaet er dokumentert i `006 analysis/3.1 datainnhenting/tab_kolonner.md`.

For å sikre at uttrekkene reflekterer den delen av virksomheten som ett enkelt verksted faktisk kan disponere, låses både supply- og demand-siden til samme juridiske enhet via filterprofilen i Tabell 5.2. Datasettet i denne rapporten er hentet for verkstedet Motive Norway (juridisk enhet Motive AS), men de samme filtrene kan byttes synkront for ethvert annet verksted i konsernet – modellen er lokasjons-agnostisk.

| Felt | Verdi | Funksjon |
|------|-------|----------|
| Asset Custodian (Supply) | Motive AS | Juridisk enhet som forvalter flåten |
| Project Owner Demand | Motive AS | Juridisk enhet som eier prosjektet |
| Region | Motive Norway | Fysisk verkstedslokasjon |
| Opp. Probability (%) | 75–100 | Nedre terskel for synlig etterspørsel |

<p align="center"><small><i>Tabell 5.2 Filterinnstillinger i Power BI ved datafangst.</i></small></p>

Filteret **Project Owner Demand** er det som låser etterspørselen til prosjekter som det valgte verkstedet selv eier. Uten dette filteret ville datasettet vise global demand mot norsk flåte alene, noe som blåser opp gap-verdiene og produserer varsler en lokal selger ikke har handlingsrom til å løse. Med filteret på plass varsles selgeren først når det aktuelle verkstedets egen flåte ikke dekker egne prosjekter – tiltak som omdisponering fra et annet verksted blir et bevisst valg, ikke noe som skjuler gapet automatisk.

### **5.2.2 Datafangst**

På uttrekkstidspunktet hadde prosjektgruppens Power BI-bruker ikke tilstrekkelige rettigheter til å bruke *Analyser i Excel* eller *Eksporter data* i rapporten, og direkte tabelluttrekk var derfor ikke mulig. Som arbeidsmetode i prosjektperioden ble det valgt å fange dataene gjennom **manuell skjermavlesning av PNG-skjermbilder** av Power BI-tabellene, og transkribere disse til CSV i Python.

Hvert snapshot dekker hele kalenderen fra inneværende uke og frem til siste uke som vises i Power BI, fordelt over 4–8 skjermbilder for å dekke hele Tier 2-listen vannrett og hele datointervallet loddrett. Råbildene lagres lokalt under `004 data/raw/snapshots/<YYYY-MM-DD>/` og transkriberes til lang-form CSV i `004 data/clean/snapshots/`. Hele datakatalogen er ekskludert fra versjonskontroll i tråd med den muntlige konfidensialitetsavtalen med Motive Offshore (jf. 5.1.1).

Hvert transkribert CSV verifiseres automatisk mot `Totalt`-raden og asset type-summene i Power BI før det godkjennes som datagrunnlag. Avvik på mer enn ±2 unit-uker per asset type per uke flagges som mistanke om transkriberingsfeil og kontrolleres manuelt mot kildebildet. For å fange uke-til-uke-endringene som er kjernen i gap-deteksjonen, tas nye snapshots ukentlig (mandager) gjennom resten av prosjektperioden.

### **5.2.3 Datasett og kvalitet**

Analysegrunnlaget består av en serie ukentlige snapshots av samme Calendar-tabell, hver fanget på en mandag med identisk filterprofil. Tabell 5.3 oppsummerer snapshot-serien.

| Snapshot | Dato | Periode dekket | Antall uker | Antall Tier 2-enheter | Antall rader |
|----------|------|----------------|-------------|-----------------------|--------------|
| $t_0$ (baseline) | 2026-05-07 | 2026-05-11 til 2026-12-28 | 34 | 24 | 816 |
| $t_1$ | 2026-05-14 | 2026-05-18 til 2026-12-28 | 33 | 24 | 792 |
| $t_2$ | 2026-05-21 | 2026-05-25 til 2026-12-28 | 32 | 26 | 832 |

<p align="center"><small><i>Tabell 5.3 Snapshot-serien som inngår i analysegrunnlaget. Hver rad i Calendar er én Tier 2-utstyrsenhet × én uke.</i></small></p>

Tre snapshots gir to delta-par til den dynamiske endringsdeteksjonen i kap 6.4. Antall uker per snapshot avtar med én for hvert påfølgende snapshot fordi Power BI-kalenderen viser en fast endhorisont (28.12.2026) og dermed forskyves bakover etter hvert som inneværende uke flyttes framover. Vurdering av om snapshot-serien er tilstrekkelig som valideringsgrunnlag diskuteres i kap 9.3.

Baseline-snapshotet 2026-05-07 dekket 24 unike Tier 2-utstyrsenheter fordelt på åtte asset types (Winch, Under rollers, Tensioner, Spoolers, RDS, LMA machines, HPUS og Cable Pulling machine) – det vil si den delen av Motive-konsernets fulle Tier 2-katalog som var fysisk lokalisert ved verkstedet Motive Norway på datafangstdatoen. I snapshot $t_2$ (2026-05-21) dukket det opp to nye Tier 2-rader: *60Te Turntable* under en ny asset type *Turntables*, og *Electric – 54kW Electric HPU* under HPUS, sannsynligvis flyttet inn fra et annet verksted i Motive-konsernet mellom $t_1$ og $t_2$. Asset types som Storage reels, HLS, Generators og Cranes finnes hos andre verksteder og inngår ikke i denne lokale flåten. Den dynamiske endringsdeteksjonen i kap 6.4 sammenligner kun celler som finnes i begge snapshots i et delta-par, og de to nye Tier 2-radene inngår derfor først som baseline for et eventuelt snapshot $t_3$.

For datakvalitet finnes 34 uker × 8 asset types = 272 verifiserbare celler i baseline-snapshotet, og alle 272 matcher eksakt mot Power BIs egne asset type-summer. Power BI viser cellene som **avrundede heltall**, men aggregerer asset type-summer fra **underliggende desimalverdier** – en delvis tilgjengelig enhet (f.eks. utleid tre av sju dager = 0,43) vises som 0 men teller som 0,43 i aggregatet, slik at sum av viste celler kan avvike fra Power BIs asset type-sum med ±1 til 2 unit-uker. Slike tilfeller flagges automatisk av sumsjekken og kontrolleres mot kildebildet før datasettet godkjennes. Siden gap-deteksjonen skal reagere på det selgere og prosjektkoordinatorer faktisk ser i dashbordet, brukes leaf-verdiene som hoveddatasett.

# **6. Modellering**

Dette kapittelet beskriver den konkrete modellen som utvikles for å oppdage kapasitetsgap og utløse varsler. Modellen bygger på det teoretiske rammeverket fra kapittel 3 og operasjonaliserer dette mot datagrunnlaget beskrevet i kapittel 5.2. Beskrivelsen er utformet slik at modellen kan implementeres uten ytterligere klargjøringer, og hvert designvalg forankres i den eksplorative dataanalysen i kapittel 7.

## **6.1 Oversikt over modellen**

Modellen behandler hvert ukentlige snapshot fra Power BI gjennom en sekvensiell pipeline med fem trinn: forhåndsfiltering, statisk gap-deteksjon, dynamisk endringsdeteksjon, suppression-regler og varselsutløsing (Figur 6.1). To deteksjonsmekanismer arbeider på det samme filtrerte datasettet:

* **Statisk tilstandsdeteksjon** identifiserer aktive gap i ett enkelt snapshot. For hver celle $(r, a, t)$ – kombinasjonen av region $r$, asset $a$ og uke $t$ – registrerer modellen om gap-verdien $G_{r,a,t}$ er negativ, og klassifiserer hvor alvorlig underskuddet er.
* **Dynamisk endringsdeteksjon** sammenligner samme celle mellom to påfølgende snapshots $s_{i-1}$ og $s_i$, og kategoriserer endringen som *ny*, *forverret*, *forbedret*, *uendret* eller *løst*. Det er denne mekanismen som fanger opp at en kontrakt har blitt oppdatert til 75 prosent vinnersannsynlighet i Salesforce, slik problemstillingen i kapittel 1.1 beskriver.

En celle kan trigge varsel både fordi den er i en alvorlig statisk tilstand og fordi den nylig har endret seg. Suppression-reglene i 6.5 hindrer at strukturelt vedvarende underskudd støyer ut endringsdrevne varsler, og varselsformat og ruting beskrives i 6.6.

Modellen er **regelbasert og deterministisk** – ingen maskinlæring eller prognoser. Hvert utløst varsel kan tilbakeføres til en spesifikk regel, celle og to snapshots, i tråd med begrunnelsen i 3.4.

<div align="center">
  <img src="../006 analysis/3.3 gap-deteksjon/fig_modell_arkitektur.png" alt="Modellens arkitektur" width="60%">
  <p align="center"><small><i>Figur 6.1 Modellens arkitektur. Hvert ukentlige snapshot behandles sekvensielt fra inndata til varselsutløsing. De to deteksjonsreglene opererer på samme filtrerte datasett, men med ulik tidshorisont: statisk deteksjon på ett snapshot, dynamisk deteksjon på to påfølgende snapshots.</i></small></p>
</div>

## **6.2 Inndata og forhåndsfiltrering**

Modellen leser ett eller to snapshots i lang-form CSV med kolonnestruktur som beskrevet i 5.2.1. Hver rad er entydig identifisert av kombinasjonen $(s, r, a, t)$ – snapshot-dato $s$, region $r$, asset_tier2 $a$ og uke $t$ – med tilhørende heltallsverdi $G_{r,a,t}^{(s)}$. For statisk gap-deteksjon (6.3) brukes ett snapshot. For dynamisk endringsdeteksjon (6.4) parres rader fra to snapshots på $(r, a, t)$, slik at hver celle får både forrige og nåværende verdi: $G_{r,a,t}^{(s_{i-1})}$ og $G_{r,a,t}^{(s_i)}$.

Før reglene evalueres, anvendes to forhåndsfiltreringer på hvert snapshot:

* **Eksklusjonsliste:** Et statisk konfigurert sett med assets fjernes fra videre prosessering. Innhold og begrunnelse er gitt i 6.5.
* **Sumsjekk mot Power BI:** Hvert snapshot verifiseres mot Power BIs egne asset type-summer som ble registrert i samme datafangst. Avvik som overstiger en toleranse på $\pm 2$ unit-uker per asset type per uke flagges som transkriberingsfeil, og snapshotet avvises automatisk fra videre prosessering. Toleransen reflekterer den strukturelle avrundingsstøyen dokumentert i 5.2.3: Power BI viser avrundede heltall i celler men aggregerer asset type-summer fra underliggende desimalverdier, slik at sum av celler kan avvike fra asset type-summen med opptil $\pm 2$ uten at det skyldes transkriberingsfeil.

Ved parring av to snapshots i 6.4 oppstår to spesialtilfeller, fordi Power BI-kalenderen alltid viser et fast antall uker fremover fra uttrekksdatoen og dermed forskyver seg mellom påfølgende snapshots:

* En celle i $s_i$ uten motpart i $s_{i-1}$ tilsvarer at kalenderhorisonten har skjøvet seg fremover, og uken ikke var synlig i forrige snapshot. Cellen behandles som *ny* dersom $G_{r,a,t}^{(s_i)} < 0$, ellers ignoreres den.
* En celle i $s_{i-1}$ uten motpart i $s_i$ tilsvarer at uken har passert mellom de to datofangstene og ikke lenger er synlig i kalenderen. Cellen ignoreres uavhengig av tidligere verdi, ettersom den ikke lenger er handlingsrelevant.

Etter forhåndsfiltrering er datasettet klart for de to deteksjonsreglene som beskrives i 6.3 og 6.4.

## **6.3 Statisk gap-deteksjon**

Den grunnleggende regelen for statisk gap-deteksjon er definert i kapittel 3.3 og operasjonaliseres i modellen som:

$$A_{r,a,t}^{(s)} = 1 \quad \text{hvis} \quad G_{r,a,t}^{(s)} < 0$$

der $A_{r,a,t}^{(s)} = 1$ markerer at cellen har et aktivt gap i snapshot $s$. Vinnersannsynlighetsbetingelsen $p_j \geq 0{,}75$ fra teorikapittelet er allerede pålagt i Power BI-filteret som beskrevet i 5.2.2, og inngår derfor ikke som en separat regel i selve kodebasen.

Binær deteksjon skiller ikke mellom marginale celleunderskudd og alvorlige flåtegap. EDA i kapittel 7 viser at alle 77 negative celler i baselinen ligger i intervallet $[-2, -1]$, men modellen beholder tre magnitudeklasser slik at prioriteringen reflekterer alvorlighetsgrad når framtidige snapshots inneholder mer ekstreme verdier. Klassene er oppsummert i Tabell 6.1.

| Magnitudeklasse | Intervall | Beskrivelse | Antall celler | Andel av 77 negative |
|-----------------|-----------|-------------|---------------|----------------------|
| Mildt gap | $-2 \leq G_{r,a,t} \leq -1$ | Marginalt underskudd, sannsynligvis håndterbart innenfor eksisterende fleksibilitet | 77 | 100,0 % |
| Moderat gap | $-5 \leq G_{r,a,t} \leq -3$ | Tydelig underskudd som krever aktiv oppfølging | 0 | 0,0 % |
| Kritisk gap | $G_{r,a,t} \leq -6$ | Stort underskudd som typisk krever omdisponering, fremleie eller hasteanskaffelse | 0 | 0,0 % |

<p align="center"><small><i>Tabell 6.1 Magnitudeklasser med fordeling fra Calendar-datasettet, baseline-snapshot 2026-05-07.</i></small></p>

Klassegrensene følger naturlige brudd i en bredere distribusjon enn baselinen alene representerer, og revideres når flere snapshots gir bredere empirisk verdiområde.

Som komplement til magnitudeklassen registrerer modellen Power BI-rapportens egen fargeklassifisering `severity_band` (5.2.1), som koder det prosentvise forholdet mellom gap og demand. De to klassifikasjonene er ortogonale: en celle med $G = -1$ er alltid *mildt*, men kan være *lilla* eller *svart* avhengig av demand. Skillet er operasjonelt fordi den manuelle varslingen modellen automatiserer bygger på fargen, ikke på gap-verdien. Korrespondansen er oppsummert i Tabell 6.2.

| Magnitudeklasse | Typisk fargebånd | Hvorfor de ikke alltid samsvarer |
|-----------------|------------------|-----------------------------------|
| Mildt ($-2 \leq G \leq -1$) | Lilla eller svart | Et lite gap kan dekke størsteparten av en liten demand og dermed bli svart |
| Moderat ($-5 \leq G \leq -3$) | Vanligvis svart | Et moderat absolutt gap er nesten alltid en stor prosent av demand |
| Kritisk ($G \leq -6$) | Svart | Et stort absolutt gap dekker per definisjon mer enn 50 % i de fleste tilfeller |

<p align="center"><small><i>Tabell 6.2 Forventet sammenheng mellom magnitudeklasse og severity-fargebånd. Modellen lagrer begge attributtene per detektert gap-celle.</i></small></p>

Resultatet av den statiske regelen for et snapshot $s$ er en samling tripletter $(r, a, t)$ som tilfredsstiller $A_{r,a,t}^{(s)} = 1$, hver merket med både magnitudeklasse og `severity_band`. Denne samlingen utgjør grunnlaget for delta-detektoren i 6.4 og for varselsutløsingen i 6.6. Strukturelt vedvarende underskudd, som typisk havner i kritisk-klassen eller har vedvarende svart fargebånd, skilles ut og styres separat gjennom suppression-reglene i 6.5.

## **6.4 Uke-til-uke-deltadeteksjon**

For hver celle $(r, a, t)$ som finnes i begge påfølgende snapshots, klassifiserer modellen endringen i én av fem kategorier basert på fortegnet og forholdet mellom $G_{r,a,t}^{(s_{i-1})}$ og $G_{r,a,t}^{(s_i)}$. Denne klassifiseringen er sentral for problemstillingen: det er endringene mellom snapshots – særlig nye og forverrede gap – som indikerer at en kontrakt har blitt oppdatert i Salesforce og dermed bumpet over 75 %-terskelen mellom de to datofangstene. Definisjonene av endringstypene er gitt i Tabell 6.3.

| Endringstype | Forrige verdi | Nåværende verdi | Tolkning |
|--------------|---------------|-----------------|----------|
| Nytt gap | $G^{(s_{i-1})} \geq 0$ | $G^{(s_i)} < 0$ | Cellen var i balanse eller hadde overskudd, men er nå falt under null. Typisk fordi en ny kontrakt har nådd 75 %-terskelen og dermed inngår i etterspørselen. |
| Forverret gap | $G^{(s_{i-1})} < 0$ | $G^{(s_i)} < G^{(s_{i-1})}$ | Cellen hadde allerede gap, men underskuddet har blitt større. Skyldes ofte at en ny kontrakt er bumpet, eller at en eksisterende reservasjon er trukket. |
| Forbedret gap | $G^{(s_{i-1})} < 0$ | $G^{(s_{i-1})} < G^{(s_i)} < 0$ | Underskuddet har blitt mindre, men cellen har fortsatt et gap. Skyldes typisk at en reservasjon er økt eller at en kontrakt har falt under 75 %-terskelen. |
| Uendret gap | $G^{(s_{i-1})} < 0$ | $G^{(s_i)} = G^{(s_{i-1})}$ | Cellen har samme negative verdi som før. Ingen ny handling utløses, men cellen rapporteres som eksisterende gap. |
| Løst gap | $G^{(s_{i-1})} < 0$ | $G^{(s_i)} \geq 0$ | Tidligere gap er eliminert. Brukes til å avslutte aktive varslingstråder for cellen. |

<p align="center"><small><i>Tabell 6.3 Klassifisering av cellevise endringer mellom påfølgende snapshots $s_{i-1}$ og $s_i$ for celler som finnes i begge.</i></small></p>

Figur 6.2 visualiserer de fem kategoriene som regioner i $(G^{(s_{i-1})}, G^{(s_i)})$-fasen. Kombinasjonen av aksene og diagonalen $y = x$ deler planet inn i seks regioner, der fem av dem tilsvarer endringstypene i Tabell 6.3 og den siste (begge $\geq 0$) ikke gir handlingsrelevans. Kravet om at modellen skal skille mellom nye, eksisterende og forverrede gap dekkes direkte av kategoriene *nytt*, *uendret* og *forverret*; *forbedret* og *løst* er supplerende kategorier som gir varslingstråder en naturlig avslutning.

<div align="center">
  <img src="../006 analysis/3.3 gap-deteksjon/fig_endringstype_fase.png" alt="Endringstype som regioner i (G_prev, G_curr)-fasen" width="65%">
  <p align="center"><small><i>Figur 6.2 Klassifisering av cellevise endringer som regioner i $(G^{(s_{i-1})}, G^{(s_i)})$-fasen. Diagonalen $y = x$ representerer uendret gap-verdi. Eksempelpunktene viser typiske celler i hver kategori.</i></small></p>
</div>

Hver detektert endring kombineres med magnitudeklassen til den nåværende verdien fra 6.3. En forverring innen samme klasse gir lav prioritet, mens en endring som krysser en klassegrense gir høy prioritet. Selve prioriteringslogikken beskrives i 6.6.

Parallelt klassifiserer modellen også **endringen i `severity_band`** mellom de to snapshotene som *verre farge*, *bedre farge* eller *samme farge*. Fordi fargen kodes fra det prosentvise forholdet mellom gap og demand, kan en celle skifte farge selv når gap-verdien er identisk – og fange forverringer som ikke krysser $G = 0$-terskelen. Modellen utløser derfor varsel både på $G$-endringer (Tabell 6.3) og på severity-overganger mellom overdekning og underdekning.

## **6.5 Suppression og eksklusjon**

EDA i kapittel 7 viser at syv utstyrsenheter har sammenhengende negative gap-verdier i de første 9–13 ukene av kalenderhorisonten – såkalt *front-lastet underskudd* (jf. 7.5). Slike sekvenser representerer vedvarende underdimensjonering, ikke kontraktsdrevne endringer. Hvis statisk deteksjon utløser varsel hver uke disse er i gap, drukner de kontraktsdrevne varslene i støy. Modellen anvender derfor en *suppression-regel* for strukturelle assets og en *eksklusjonsliste* for inaktive enheter.

Et asset markeres som strukturelt når $G_{r,a,t}^{(s)} < 0$ for alle observerte $(t, s)$ i et evalueringsvindu på $K = 4$ påfølgende snapshots, slik at kortvarige nedgangsperioder ikke feilaktig klassifiseres som strukturelle. Innenfor prosjektets tre snapshots kan kriteriet ikke eksercerases (jf. 9.3); de syv front-lastede enhetene i Tabell 7.3 er naturlige kandidater for **manuell strukturell-markering** når Motive-koordinatoren bekrefter underdimensjoneringen.

Suppression-regelen styrer hvordan hver detektert endring fra 6.3 og 6.4 håndteres avhengig av om asset er strukturelt eller ikke (Tabell 6.4).

| Endringstype | Krysser magnitudeklasse | Ikke-strukturelt asset | Strukturelt asset |
|--------------|-------------------------|------------------------|-------------------|
| Nytt gap | (n/a) | Varsel | Varsel |
| Forverret | Ja | Varsel | Varsel |
| Forverret | Nei | Varsel (lav prioritet) | Loggføres, ikke varsel |
| Uendret | (n/a) | Loggføres, ikke varsel | Loggføres, ikke varsel |
| Forbedret | (n/a) | Loggføres, ikke varsel | Loggføres, ikke varsel |
| Løst | (n/a) | Varsel (positiv) | Varsel (positiv) |

<p align="center"><small><i>Tabell 6.4 Suppression-regelens utløsingsmatrise basert på endring i $G_{r,a,t}$. Strukturelle assets utløser varsel kun ved meningsfulle tilstandsendringer – klassebytte eller løst gap – og ikke ved variasjon innenfor samme magnitudeklasse.</i></small></p>

Reglene i Tabell 6.4 fanger alle endringer som krysser $G = 0$-grensen eller endrer magnitudeklasse. Den fanger derimot **ikke** endringer hvor $G$ forblir på samme side av nullinjen (begge $\geq 0$ eller begge $< 0$ uten klassebytte) men den underliggende etterspørselen har vokst eller falt slik at det prosentvise gapet har krysset et fargebånd (jf. 5.2.1). Det empiriske eksempelet i 7.6 viser at det første snapshot-paret inneholder tre slike "skjulte" endringer som ikke blir fanget av tabellen over. Modellen anvender derfor en supplerende regel basert på `severity_band`, som evalueres når Tabell 6.4 ikke har utløst varsel for cellen. Severity-båndene ordnes fra alvorlig til komfortabel som svart, lilla, rød, gul, grønn, og en *overgang* defineres som flytting fra ett bånd til et annet mellom to snapshots. Reglene er gitt i Tabell 6.5.

| Severity-overgang | Tolkning | Ikke-strukturelt asset | Strukturelt asset |
|-------------------|----------|------------------------|-------------------|
| Overdekning (grønn/gul/rød) → underdekning (lilla/svart) | Skjult nytt gap: demand har vokst inn i underdekningssone | Varsel | Varsel |
| Lilla → svart | Skjult forverring: mildt gap eskalert til alvorlig | Varsel | Varsel |
| Underdekning → overdekning | Skjult løst gap: demand falt ut av underdekning | Varsel (positiv) | Varsel (positiv) |
| Svart → lilla | Skjult forbedring: alvorlig gap nedjustert til mildt | Loggføres, ikke varsel | Loggføres, ikke varsel |
| Innen samme over- eller underdekningssone (f.eks. grønn → gul) | Marginal endring uten operasjonell handling | Loggføres, ikke varsel | Loggføres, ikke varsel |

<p align="center"><small><i>Tabell 6.5 Supplerende utløsingsregler basert på endring i `severity_band` for celler der Tabell 6.4 ikke har utløst varsel. Reglene utløser varsel når demand-endringer krysser et fargebånd som markerer overgang mellom overdekning og underdekning, eller mellom mild og alvorlig underdekning.</i></small></p>

For celler hvor både $G$ og `severity_band` har endret seg, dominerer Tabell 6.4. Tabell 6.5 utvider dermed deteksjonsrommet uten å konkurrere med $G$-regelen. Strukturelle gap rapporteres i en separat månedlig oversikt til vedlikeholds-/kapasitetsutvidelsesteamet, slik at kortsiktig handling og langsiktig planlegging håndteres i hver sin kanal.

**Eksklusjonslisten** fjerner assets som ikke skal evalueres i det hele tatt. EDA i kapittel 7 identifiserer én slik enhet: *Diesel – 63kW Diesel HPU Zone II* har $G = 0$ i alle 34 ukene av baselinen, hvilket tyder på at den er inaktiv eller registrert med null kapasitet i Asset Voice. Den initielle listen er et forslag basert på baseline og krever bekreftelse fra Motive før produksjonsbruk.

## **6.6 Varselsutløsing og ruting**

Etter forhåndsfiltrering (6.2), statisk deteksjon (6.3), delta-deteksjon (6.4) og suppression (6.5), avgjør siste trinn om varsel skal sendes og til hvem. Utløsingsmatrisene i 6.5 bestemmer *om*; rutingen kombinerer endringstype og magnitudeklasse til en prioritet og kobler varselet til en mottaker.

Et nytt gap eller en forverring som krysser en klassegrense gir høy prioritet; en forverring innen samme klasse gir lav prioritet; et løst gap genererer informasjonsvarsel. Kritisk magnitudeklasse løfter prioriteten ett nivå.

Hvert utløste varsel rutes til en mottaker basert på en konfigurerbar mapping. For dette prosjektet brukes et oppsett der hver asset type har én primærmottaker og det generelle salgsteamet som standardmottaker for asset types uten dedikert koordinator:

```yaml
# recipients.yaml
Winch:                  winch-koordinator@motive-offshore.no
Under rollers:          underrollers-koordinator@motive-offshore.no
Tensioner:              tensioner-koordinator@motive-offshore.no
Spoolers:               spoolers-koordinator@motive-offshore.no
RDS:                    rds-koordinator@motive-offshore.no
LMA machines:           lma-koordinator@motive-offshore.no
HPUS:                   hpus-koordinator@motive-offshore.no
Cable Pulling machine:  cable-koordinator@motive-offshore.no
default:                salg@motive-offshore.no
cc:                     salg@motive-offshore.no
```

Asset type som rutingsnøkkel er pragmatisk: Power BI-tabellen oppgir ikke kontrakts-id, så modellen kan ikke route per kontrakt eller selger. Per-kontrakt-ruting ville krevd Salesforce-integrasjon (utenfor omfanget, jf. 1.3) og er omtalt som produksjonsanbefaling i 9.6.

Hvert utløst varsel produseres som et strukturert objekt med 17 felt (fullt skjema i Vedlegg F) og videreføres til varslingsmodulen `gap_alerting.py` (8.4). Varslene aggregeres til **én digest-e-post per mottaker per snapshot**, gruppert etter endringstype og med mønster-deteksjon som slår sammen sammenhengende uker for samme asset. Aktive (ulukkede) gap genererer en **ukentlig påminnelse** inntil cellen blir *løst* eller *forbedret*.

# **7. Analyse**

Dette kapittelet presenterer den eksplorative dataanalysen utført på baseline-snapshotet 2026-05-07. Resultatene legges frem objektivt; vurdering av hva de betyr er forbeholdt diskusjonskapittelet. Den dynamiske uke-til-uke-analysen presenteres i 7.6 og bygger på sammenligning mellom påfølgende snapshots.

## **7.1 Distribusjon av gap-verdier**

Calendar-datasettet inneholder 816 celler fordelt over 24 utstyrsenheter og 34 uker. Tabell 7.1 viser fordelingen etter fortegn på gap-verdien $G_{r,a,t}$, og Figur 7.1 viser den fulle distribusjonen.

| Tilstand | Antall celler | Andel |
|----------|---------------|-------|
| Negativ verdi (gap) | 77 | 9,4 % |
| Null verdi (balanse) | 260 | 31,9 % |
| Positiv verdi (overskudd) | 479 | 58,7 % |

<p align="center"><small><i>Tabell 7.1 Fordeling av cellene i Calendar-datasettet etter fortegn på gap-verdien.</i></small></p>

<div align="center">
  <img src="../006 analysis/3.2 eda/fig_gap_distribusjon.png" alt="Distribusjon av gap-verdier" width="80%">
  <p align="center"><small><i>Figur 7.1 Distribusjon av gap-verdiene i Calendar-datasettet, fargekodet etter negativ, balansert og positiv tilstand.</i></small></p>
</div>

Distribusjonen er lett venstreforskjøvet for negative verdier og bredere på overskuddssiden. For de negative cellene er median $-1$, 25-prosentilen $-1$ og 5-prosentilen $-2$. Verdiområdet for hele datasettet er $[-2, +7]$.

## **7.2 Gap-utviklingen over kalenderhorisonten**

Figur 7.2 viser sum av $G_{r,a,t}$ aggregert per uke over hele 34-ukers-horisonten.

<div align="center">
  <img src="../006 analysis/3.2 eda/fig_total_gap_per_uke.png" alt="Totalt gap per uke" width="85%">
  <p align="center"><small><i>Figur 7.2 Totalt synlig gap per uke i baseline-snapshotet.</i></small></p>
</div>

Samlet ukentlig gap er positivt gjennom hele horisonten og øker fra $+10$ unit-uker i uken 2026-05-11 til $+34$ i uken 2026-12-28. Trendkurven er svakt stigende og monoton fra og med oktober 2026; de første 9 ukene har lokal flatlinje i intervallet $+9$ til $+13$ fordi syv enheter har strukturelt underskudd i denne tidlige perioden (jf. 7.5). At baseline-snapshotet i sin helhet ligger over null betyr at Motive Norway-flåten samlet sett dekker den 75 %+-eksponerte etterspørselen som er synlig per snapshot-datoen.

## **7.3 Sammenligning på tvers av asset types**

Figur 7.3 dekomponerer det ukentlige gapet etter asset type.

<div align="center">
  <img src="../006 analysis/3.2 eda/fig_per_asset_type_uker.png" alt="Gap per asset type over uker" width="85%">
  <p align="center"><small><i>Figur 7.3 Ukentlig sum av gap-verdi per asset type.</i></small></p>
</div>

Tensioner, RDS og Cable Pulling machine er de asset typene som har vedvarende negative ukessummer i Motive Norway-flåten. Tensioner går så lavt som $-3$ per uke, RDS ned til $-2$ og Cable Pulling machine ned til $-2$. Disse tre asset typene står til sammen for hele det negative bidraget på asset type-nivå (kumulativt $-25$, $-23$ og $-6$ unit-uker over de 34 ukene). Winch, Spoolers, LMA machines, Under rollers og HPUS har positiv ukessum i alle 34 ukene (sum henholdsvis $+308$, $+199$, $+34$, $+34$ og $+307$); HPUS som asset type er altså samlet i overskudd, selv om enkeltenheten *158KW Electric HPU* har negative leaf-celler i tidlig periode (jf. 7.5).

## **7.4 De mest utsatte utstyrsenhetene**

Tabell 7.2 lister de syv enhetene med negativt kumulativt gap over 34 uker, og Figur 7.4 viser samme sortering som heatmap mot ukene.

| Asset type | Asset (Tier 2) | Kumulativt gap |
|--------|---------------|----------------|
| Winch | Hydraulic – Wide\|35Te Wide Drum Winch | −19 |
| Tensioner | Horizontal – 2 track – 15Te Horizontal Tensioner | −16 |
| RDS | 500Te RDS | −14 |
| Tensioner | Horizontal – 4 track – 50Te Tensioner – 4 Track | −9 |
| RDS | 150Te RDS | −9 |
| HPUS | Electric – 158KW Electric HPU | −9 |
| Cable Pulling machine | 2Te Linear Cable Engine | −6 |

<p align="center"><small><i>Tabell 7.2 Utstyrsenhetene med negativt kumulativt gap over snapshot-perioden 2026-05-11 til 2026-12-28.</i></small></p>

<div align="center">
  <img src="../006 analysis/3.2 eda/fig_gap_heatmap_topp30.png" alt="Heatmap utstyrsenheter" width="95%">
  <p align="center"><small><i>Figur 7.4 Heatmap av gap-verdi per uke for de 24 utstyrsenhetene i Motive Norway-baselinen.</i></small></p>
</div>

To av de syv enhetene tilhører Tensioner-gruppen og to tilhører RDS, mens Winch, HPUS og Cable Pulling machine bidrar med én enhet hver. Verste enkeltasset er *Hydraulic – Wide|35Te Wide Drum Winch* med kumulativt gap $-19$, etterfulgt av *Horizontal – 2 track – 15Te Horizontal Tensioner* med $-16$ og *500Te RDS* med $-14$. Alle syv enhetene har sitt negative bidrag konsentrert i de første 9–14 ukene av kalenderhorisonten og stabiliserer seg deretter på $G = 0$ (jf. 7.5).

## **7.5 Front-lastet underskudd og inaktive utstyrsenheter**

Ingen utstyrsenhet i baselinen har $G < 0$ i alle 34 ukene, og ingen tilfredsstiller dermed strukturell-kriteriet i 6.5. Syv enheter har derimot sammenhengende negative gap-verdier i de første 9–13 ukene før de stabiliserer seg på 0 eller overskudd – omtalt som **front-lastet underskudd**. De syv enhetene utgjør 29 % av Calendar-datasettet og er listet i Tabell 7.3.

| Asset type | Asset (Tier 2) | Neg uker av 34 | Min | Snitt-neg | Sum |
|--------|---------------|----------------|-----|-----------|-----|
| RDS | 500Te RDS | 14 | −1 | −1,00 | −14 |
| Tensioner | Horizontal – 2 track – 15Te Horizontal Tensioner | 13 | −2 | −1,23 | −16 |
| Winch | Hydraulic – Wide\|35Te Wide Drum Winch | 10 | −2 | −1,90 | −19 |
| Tensioner | Horizontal – 4 track – 50Te Tensioner – 4 Track | 9 | −1 | −1,00 | −9 |
| RDS | 150Te RDS | 9 | −1 | −1,00 | −9 |
| HPUS | Electric – 158KW Electric HPU | 9 | −1 | −1,00 | −9 |
| Cable Pulling machine | 2Te Linear Cable Engine | 3 | −2 | −2,00 | −6 |

<p align="center"><small><i>Tabell 7.3 Utstyrsenheter med front-lastet underskudd (sammenhengende negative gap-verdier i tidlig kalenderperiode) i baseline-snapshotet 2026-05-07.</i></small></p>

Én utstyrsenhet har $G_{r,a,t} = 0$ i alle 34 uker (Tabell 7.4).

| Asset type | Asset (Tier 2) |
|--------|---------------|
| HPUS | Diesel – 63kW Diesel HPU Zone II |

<p align="center"><small><i>Tabell 7.4 Utstyrsenheter med gap-verdi 0 i alle 34 uker av baseline-snapshotet 2026-05-07.</i></small></p>

## **7.6 Uke-til-uke-analyse**

Den dynamiske endringsdeteksjonen beskrevet i 6.4 er kjørt på det første snapshot-paret 2026-05-07 ↔ 2026-05-14. Modellen sammenligner de 792 cellene som finnes i begge snapshots (33 uker × 24 utstyrsenheter) og klassifiserer hver celle både etter endring i $G_{r,a,t}$ (Tabell 6.3) og etter endring i `severity_band` (5.2.1). Tabell 7.5 viser fordelingen mellom de seks endringskategoriene.

| Endringstype | Antall celler | Andel |
|--------------|---------------|-------|
| Nytt gap | 7 | 0,9 % |
| Forverret gap | 0 | 0,0 % |
| Forbedret gap | 0 | 0,0 % |
| Løst gap | 0 | 0,0 % |
| Uendret gap (negativt) | 70 | 8,8 % |
| Positiv endring (ikke-negativt begge snapshots) | 37 | 4,7 % |
| Stabil (uendret ikke-negativt) | 678 | 85,6 % |

<p align="center"><small><i>Tabell 7.5 Fordeling av cellevise endringer mellom snapshot 2026-05-07 og 2026-05-14.</i></small></p>

I dette første delta-paret er det kun kategorien *nytt gap* som utløser nye varsler basert på $G$-regelen. De syv nye gap-cellene fordeler seg på tre utstyrsenheter, og fem av dem opptrer i fem sammenhengende uker for samme enhet:

- *500Te RDS* har fått ny etterspørsel i ukene 2026-08-17 til og med 2026-09-14, alle med $G$ som faller fra 0 til $-1$ og fargen som skifter fra grønn til svart. Det sammenhengende mønsteret over fem uker er det tydeligste signalet i datasettet på at en ny kontrakt har passert 75 %-terskelen i Salesforce mellom de to datafangstene.
- *Electric – 158KW Electric HPU* (uke 2026-07-13) og *Electric – 55kW Electric HPU* (uke 2026-07-20) viser hvert sitt enkeltstående nye gap.

Severity-deltaen flagger i tillegg ti celler som *verre farge* og to som *bedre farge*. Tre av de ti er $G$-uendret eller forbedret, men har skiftet fargebånd – usynlige for en ren $G$-detektor. Severity-regelen utløser også to positive informasjonsvarsler ved lilla → grønn. Fordelingen er i Tabell 7.6.

| Severity-endring | Antall celler |
|------------------|---------------|
| Verre farge | 10 |
| Bedre farge | 2 |
| Samme farge | 780 |

<p align="center"><small><i>Tabell 7.6 Endring i severity_band mellom snapshot 2026-05-07 og 2026-05-14. Tre av de ti «verre farge»-cellene fanges kun gjennom severity-dimensjonen (G-regelen utløser ikke varsel), og illustrerer empirisk hvorfor `severity_band` er fanget som eget attributt jf. 5.2.1.</i></small></p>

Fordelingen av endringer over kalenderhorisonten og over asset types er vist i Figur 7.5 og 7.7. Endringene konsentreres i juli–september, det vil si i det tidsvinduet som har høyest tetthet av eksisterende negative celler i baselinen, og fordeler seg på asset types RDS og HPUS. Ingen endringer i kategoriene *forverret*, *forbedret* eller *løst* observeres i dette første delta-paret – en konsekvens av at perioden mellom snapshotene kun er én uke, og at de fleste underdekninger i baselinen ligger på $G \in \{-1, -2\}$ uten rom for ytterligere forverring innenfor magnitudeklassen *mildt*.

<div align="center">
  <img src="../006 analysis/3.3 gap-deteksjon/fig_endringer_per_uke_delta1.png" alt="Endringer per uke - delta-par 1" width="80%">
  <p align="center"><small><i>Figur 7.5 Fordeling av cellevise endringer over kalenderhorisonten for delta-par 1 (2026-05-07 ↔ 2026-05-14). Stabile celler er ekskludert for lesbarhet.</i></small></p>
</div>

<div align="center">
  <img src="../006 analysis/3.3 gap-deteksjon/fig_endringer_per_asset_type_delta1.png" alt="Endringer per asset type - delta-par 1" width="80%">
  <p align="center"><small><i>Figur 7.6 Fordeling av cellevise endringer per asset type for delta-par 1. RDS og HPUS dominerer endringsvolumet i det første delta-paret.</i></small></p>
</div>

### **7.6.1 Andre delta-par 2026-05-14 ↔ 2026-05-21**

Med snapshot $t_2$ (2026-05-21) tilgjengelig kjøres delta-detektoren også på det andre snapshot-paret. Sammenligningen omfatter de 768 cellene som finnes i begge snapshots (32 uker × 24 utstyrsenheter); de to nye Tier 2-radene i $t_2$ (jf. 5.2.3) inngår ikke i delta-deteksjonen siden de mangler en motpart i $t_1$. Tabell 7.7 viser fordelingen.

| Endringstype | Antall celler | Andel |
|--------------|---------------|-------|
| Nytt gap | 4 | 0,5 % |
| Forverret gap | 0 | 0,0 % |
| Forbedret gap | 2 | 0,3 % |
| Løst gap | 8 | 1,0 % |
| Uendret gap (negativt) | 60 | 7,8 % |
| Positiv endring (ikke-negativt begge snapshots) | 15 | 2,0 % |
| Stabil (uendret ikke-negativt) | 679 | 88,4 % |

<p align="center"><small><i>Tabell 7.7 Fordeling av cellevise endringer mellom snapshot 2026-05-14 og 2026-05-21.</i></small></p>

Alle fire dynamiske kategorier er nå aktivert. De åtte *løste* gapene fordeler seg på *2Te Linear Cable Engine* (3), *500Te RDS* (3) og *158KW Electric HPU* (1). De fire *nye* gapene rammer fire ulike enhet-/uke-kombinasjoner. Mønsteret er konsistent med at kalenderen forskyves én uke framover: tidlige gap glir ut av synshorisonten, mens nye dukker opp ved overgangen «for tett på» → «innenfor 75 %-vinduet». Severity-fordelingen er i Tabell 7.8.

| Severity-endring | Antall celler |
|------------------|---------------|
| Verre farge | 4 |
| Bedre farge | 11 |
| Samme farge | 753 |

<p align="center"><small><i>Tabell 7.8 Endring i severity_band mellom snapshot 2026-05-14 og 2026-05-21.</i></small></p>

Fordelingen av endringene over kalenderhorisonten og per asset type for delta-par 2 er vist i Figur 7.7 og 7.9. Endringene grupperer seg igjen i sommer- og tidlig høstmåneder – i tråd med at det er denne perioden som har høyest tetthet av eksisterende negative og lilla celler i baselinen og dermed flest celler som er innenfor «én klassebytte» fra et nytt eller løst gap.

<div align="center">
  <img src="../006 analysis/3.3 gap-deteksjon/fig_endringer_per_uke_delta2.png" alt="Endringer per uke - delta-par 2" width="80%">
  <p align="center"><small><i>Figur 7.7 Fordeling av cellevise endringer over kalenderhorisonten for delta-par 2 (2026-05-14 ↔ 2026-05-21). Stabile celler er ekskludert for lesbarhet.</i></small></p>
</div>

<div align="center">
  <img src="../006 analysis/3.3 gap-deteksjon/fig_endringer_per_asset_type_delta2.png" alt="Endringer per asset type - delta-par 2" width="80%">
  <p align="center"><small><i>Figur 7.8 Fordeling av cellevise endringer per asset type for delta-par 2. Cable Pulling machine og RDS er mest aktive – Cable bidrar med både to nye gap og tre løste gap, RDS med tre løste gap.</i></small></p>
</div>

### **7.6.2 Varslingstråder over to delta-par**

Varslingsmodulen `gap_alerting.py` (kap 6.6) holder en persistent tråd-tilstand i `active_alerts.json` på tvers av snapshots. Etter første delta-par var det 10 aktive tråder; etter andre delta-par er antallet 9. Netto endring $-1$ skjuler en større bevegelse: fem tråder lukkes (fire ved *løst gap* mot $G$-regelen og én via *positiv endring* der severity går fra lilla til grønn), og fire nye tråder åpnes (de fire *nye gap*-cellene i Tabell 7.7). Fem av de ti opprinnelige trådene fortsetter inn i tredje syklus med en ukentlig påminnelse (`reminder_count = 1`). Tabell 7.9 sporer de ti opprinnelige trådene gjennom de to delta-parene.

| Tråd-ID | Åpnet ved | Status etter delta-par 1 | Status etter delta-par 2 |
|---------|-----------|--------------------------|--------------------------|
| 500Te RDS @ 2026-08-17 | NYTT_GAP | aktiv | påminnelse |
| 500Te RDS @ 2026-08-24 | NYTT_GAP | aktiv | påminnelse |
| 500Te RDS @ 2026-08-31 | NYTT_GAP | aktiv | **lukket (løst)** |
| 500Te RDS @ 2026-09-07 | NYTT_GAP | aktiv | **lukket (løst)** |
| 500Te RDS @ 2026-09-14 | NYTT_GAP | aktiv | **lukket (løst)** |
| 158KW HPU @ 2026-07-13 | NYTT_GAP | aktiv | **lukket (løst)** |
| 55kW HPU @ 2026-07-20 | NYTT_GAP | aktiv | påminnelse |
| 75Te Spooler @ 2026-06-22 | SKJULT_NYTT_GAP | aktiv | påminnelse |
| 11kW HPU @ 2026-10-12 | SKJULT_NYTT_GAP | aktiv | påminnelse |
| 30kW HPU @ 2026-07-13 | SKJULT_NYTT_GAP | aktiv | **lukket (positiv)** |

<p align="center"><small><i>Tabell 7.9 Livssyklus for de ti trådene som ble åpnet i delta-par 1 (sju via G-regelen og tre via severity-regelen). Etter delta-par 2 er fem tråder lukket og fem fortsetter til neste snapshot. I tillegg åpnes fire nye tråder i delta-par 2 (de fire NYTT_GAP-cellene fra Tabell 7.7), slik at trådtilstanden går fra 10 til 9.</i></small></p>

Tabellen viser at trådmodellen håndterer både *gradvis avklaring* (RDS-mønsteret som smelter bort uke for uke) og *engangsavklaring* (158KW HPU, 30kW HPU). Tråder som krever vedvarende oppfølging overlever til ny påminnelse, konsistent med kravet i 6.6. Den underliggende mekanikken dekkes i 8.4.

# **8. Resultat**

Dette kapittelet presenterer resultatene fra modellkjøringen på baseline-snapshotet 2026-05-07 og det første snapshot-paret (baseline mot 2026-05-14). Resultatene legges frem objektivt; vurdering og tolkning gis i kapittel 9. Hvert delresultat kobles direkte til problemstillingen og delproblemene fra kapittel 1.

## **8.1 Statisk gap-deteksjon på baseline-snapshot**

Den statiske gap-deteksjonsregelen $A_{r,a,t}^{(s)} = 1$ hvis $G_{r,a,t}^{(s)} < 0$ utløser **77 celler** i baseline-snapshot 2026-05-07, av totalt 816 celler i Calendar-datasettet (9,4 %). Fordelingen etter magnitudeklasse er gitt i Tabell 8.1.

| Magnitudeklasse | Intervall | Antall utløste celler | Andel av 77 negative celler |
|-----------------|-----------|-----------------------|------------------------------|
| Mildt gap | $-2 \leq G \leq -1$ | 77 | 100,0 % |
| Moderat gap | $-5 \leq G \leq -3$ | 0 | 0,0 % |
| Kritisk gap | $G \leq -6$ | 0 | 0,0 % |

<p align="center"><small><i>Tabell 8.1 Fordeling av utløste statiske gap-celler i baseline-snapshotet etter magnitudeklasse.</i></small></p>

Fordelt på asset type bidrar RDS, Tensioner og HPUS med flest negative celler (henholdsvis 23, 22 og 19 av 77), Winch og Cable Pulling machine med 10 og 3, mens Spoolers, LMA machines og Under rollers har ingen.

## **8.2 Uke-til-uke-deltadeteksjon**

Klassifiseringen av cellevise endringer mellom snapshot 2026-05-07 og 2026-05-14 er presentert i Tabell 7.5 og bygges ikke om her. Severity-deltaen er gitt i Tabell 7.6. Av de 792 sammenlignede cellene utløser delta-detektoren 7 *nye gap* via $G$-regelen og ytterligere 5 varsler via severity-regelen, med ingen *forverrede*, *forbedrede* eller *løste* gap i dette første delta-paret. Fordelingen over kalenderhorisonten og per asset type er visualisert i Figur 7.5 og 7.7.

For det andre delta-paret 2026-05-14 ↔ 2026-05-21 (Tabell 7.7) utløser deltadetektoren 4 *nye gap* og 8 *løste gap* via $G$-regelen, samt 2 *forbedrede gap*. Severity-deltaen flagger 4 *verre farge*-celler og 11 *bedre farge*-celler (Tabell 7.8). I motsetning til første delta-par er nå alle de fire dynamiske kategoriene aktivert, noe som gir den første empiriske observasjonen av en hel livssyklus i datasettet – fra åpning til løsning. Tabell 8.2 oppsummerer regel-utløsingene for begge delta-parene.

| Regel | Delta-par 1 (792 celler) | Delta-par 2 (768 celler) |
|-------|---------------------------|---------------------------|
| $G$-regel: nytt gap | 7 | 4 |
| $G$-regel: forverret gap | 0 | 0 |
| $G$-regel: forbedret gap | 0 | 2 |
| $G$-regel: løst gap | 0 | 8 |
| Severity-regel: skjult nytt gap | 3 | 0 |
| Severity-regel: skjult forverring | 0 | 0 |
| Severity-regel: skjult løst gap | 2 | 2 |
| **Totalt gap-åpnende varsler (G + severity)** | **10** | **4** |
| **Totalt informasjons-/lukke-varsler (G + severity)** | **2** | **12** |

<p align="center"><small><i>Tabell 8.2 Sammenligning av regel-utløste varsler over de to delta-parene. Det første delta-paret er dominert av åpning av nye underskudd, mens det andre delta-paret kombinerer fire nye åpninger med ti lukke-/informasjonsvarsler – konsistent med at kalenderen forskyves én uke framover og at tidlige gap «glir ut» av synshorisonten.</i></small></p>

## **8.3 Krysstabulering: endringstype × magnitudeklasse**

Tabell 8.3 viser hvilken magnitudeklasse hver utløste endring faller i for snapshot-paret 2026-05-07 ↔ 2026-05-14. Samtlige syv $G$-baserte *nye gap* har $G^{(s_i)} \in \{-1, -2\}$ og faller i klassen *mildt*. Kategoriene *forverret innen klasse* og *forverret krysser klasse* har null observasjoner i dette delta-paret.

| | Mildt ($-2 \leq G \leq -1$) | Moderat ($-5 \leq G \leq -3$) | Kritisk ($G \leq -6$) | Totalt |
|---|---|---|---|---|
| Nytt gap (G-regel) | 7 | 0 | 0 | 7 |
| Forverret (innen klasse) | 0 | 0 | 0 | 0 |
| Forverret (krysser klasse) | 0 | 0 | 0 | 0 |
| Skjult nytt gap (severity-regel) | 3 | 0 | 0 | 3 |
| Skjult forverring (severity-regel) | 0 | 0 | 0 | 0 |
| **Totalt utløste gap-åpnende varsler** | **10** | **0** | **0** | **10** |

<p align="center"><small><i>Tabell 8.3 Fordeling av utløste gap-åpnende varsler etter regel og magnitudeklasse for delta-par 1. Magnitudeklassen er bestemt av $G^{(s_i)}$ for $G$-regelen og av $G^{(s_i)}$-ekvivalenten ved skjult gap (også her havner alle i mildt). Informasjonsvarsler (LØST og SKJULT_LOST_GAP) er ikke inkludert.</i></small></p>

Tabell 8.3b viser den tilsvarende fordelingen for delta-paret 2026-05-14 ↔ 2026-05-21. Mønsteret er det samme – samtlige fire $G$-baserte *nye gap* faller i klassen *mildt* ($G^{(s_2)} \in \{-1, -2\}$). Etter to delta-par er det fremdeles ikke registrert en eneste *forverret* observasjon, hverken innen-klasse eller klassebyttende, og heller ingen $G^{(s_i)} \leq -3$.

| | Mildt ($-2 \leq G \leq -1$) | Moderat ($-5 \leq G \leq -3$) | Kritisk ($G \leq -6$) | Totalt |
|---|---|---|---|---|
| Nytt gap (G-regel) | 4 | 0 | 0 | 4 |
| Forverret (innen klasse) | 0 | 0 | 0 | 0 |
| Forverret (krysser klasse) | 0 | 0 | 0 | 0 |
| Skjult nytt gap (severity-regel) | 0 | 0 | 0 | 0 |
| Skjult forverring (severity-regel) | 0 | 0 | 0 | 0 |
| **Totalt utløste gap-åpnende varsler** | **4** | **0** | **0** | **4** |

<p align="center"><small><i>Tabell 8.3b Fordeling av utløste gap-åpnende varsler etter regel og magnitudeklasse for delta-par 2. Informasjonsvarsler (8 LØST, 2 FORBEDRET og 2 SKJULT_LOST_GAP) er ikke inkludert.</i></small></p>

## **8.4 Varselsutløsing og prioritering**

Suppression-regelen (6.5) videreførte samtlige utløste varsler i begge snapshot-parene fordi suppression-listen er tom – ingen enheter tilfredsstiller $K = 4$-kriteriet etter kun tre snapshots, og koordinator har ikke manuelt markert front-lastede enheter (Tabell 7.3) som strukturelle.

Modulen `gap_alerting.py` (006 analysis/3.4 varsling/) anvender utløsingsmatrisene i 6.5 og rutingen i 6.6 på begge snapshot-parene. For delta-par 1 (2026-05-07 ↔ 2026-05-14) filtreres 33 av 792 celler bort av eksklusjonslisten (én utstyrsenhet × 33 uker, *Diesel – 63kW Diesel HPU Zone II*); av de gjenværende 759 cellene utløser modellen 12 varsler – 7 via $G$-regelen (Tabell 6.4) og 5 via severity-regelen (Tabell 6.5).

| Mottaker (Asset type) | Lav prioritet | Middels prioritet | Høy prioritet | Informasjon | Totalt |
|---|---|---|---|---|---|
| RDS-koordinator | 0 | 5 | 0 | 0 | 5 |
| HPUS-koordinator | 0 | 4 | 0 | 2 | 6 |
| Spoolers-koordinator | 0 | 1 | 0 | 0 | 1 |
| **Sum** | **0** | **10** | **0** | **2** | **12** |

<p align="center"><small><i>Tabell 8.4 Utløste varsler fordelt på mottaker (asset type-koordinator) og prioritet for snapshot-paret 2026-05-07 ↔ 2026-05-14. Lav og høy prioritet er 0 fordi alle observerte gap-verdier ligger i magnitudeklasse «mildt» (jf. 6.3) og ingen forverring krysser klassegrense.</i></small></p>

Varslene aggregeres til tre digest-e-poster, én per primærmottaker. Mønsterdeteksjonen for sammenhengende uker grupperer de fem RDS-varslene i én linje i RDS-digesten – Power BI-cellene viser fem etterfølgende uker (2026-08-17 til 2026-09-14) med samme overgang $G : 0 \to -1$ og farge grønn → svart, som tolkes som én ny kontrakt og ikke fem uavhengige hendelser.

For delta-par 2 (2026-05-14 ↔ 2026-05-21) filtreres 32 av 768 celler bort av samme eksklusjonsregel. På de gjenværende 736 cellene utløser modellen 14 nye/lukkende varsler fra regelmatrisen (Tabell 8.2) og henter i tillegg 5 påminnelser fra den persistente trådtilstanden generert i delta-par 1 (jf. 7.6.2). Resultatet er 19 utstedte varsler fordelt på fem digest-e-poster – to flere mottakere enn i forrige syklus, fordi *Cable Pulling machine* og *Tensioner* nå har egne varsler. Tabell 8.4b oppsummerer fordelingen per mottaker og prioritet.

| Mottaker (Asset type) | Middels prioritet (ny) | Informasjon (løst, skjult løst, påminnelse) | Totalt |
|---|---|---|---|
| RDS-koordinator | 0 | 5 (3 lost + 2 påminnelse) | 5 |
| HPUS-koordinator | 1 | 6 (1 lost + 2 påminnelse + 2 SKJULT_LOST_GAP + 1 LØST_TRAD) | 7 |
| Cable Pulling-koordinator | 2 | 3 (3 lost-informasjon) | 5 |
| Tensioner-koordinator | 1 | 0 | 1 |
| Spoolers-koordinator | 0 | 1 (påminnelse) | 1 |
| **Sum** | **4** | **15** | **19** |

<p align="center"><small><i>Tabell 8.4b Utløste varsler for snapshot-paret 2026-05-14 ↔ 2026-05-21 fordelt på mottaker og prioritet. Antall mottakere øker fra 3 til 5 i denne syklusen fordi *Cable Pulling machine* og *Tensioner* også har endringer som krever oppfølging.</i></small></p>

Trådhåndteringen mellom de to delta-parene er hovedmekanismen som gjør den ukentlige påminnelseslogikken (Tabell 6.5) operasjonell på tvers av snapshots. Etter delta-par 1 stod 10 tråder i `active_alerts.json`; etter delta-par 2 er antallet 9. Tabell 8.4c viser den underliggende balansen.

| Trådhendelse | Antall | Beskrivelse |
|---|---|---|
| Aktive tråder før delta-par 2 | 10 | Bæres med fra slutten av delta-par 1 |
| Lukket ved $G$-regel (LØST) | 4 | 500Te RDS × 3 + 158KW HPU × 1 |
| Lukket ved severity-regel (POSITIV_ENDRING + BEDRE_FARGE) | 1 | 30kW HPU @ 2026-07-13 |
| Påminnelse generert (`reminder_count` økes med 1) | 5 | 500Te RDS × 2 + 55kW HPU + 11kW HPU + 75Te Spooler |
| Nye tråder åpnet (NYTT_GAP) | 4 | 2Te Linear Cable × 2 + 55kW HPU + 4-track 50Te |
| **Aktive tråder etter delta-par 2** | **9** | $10 - 5 + 4 = 9$ |

<p align="center"><small><i>Tabell 8.4c Tilstandsendring i `active_alerts.json` over snapshot-paret 2026-05-14 ↔ 2026-05-21.</i></small></p>

At fem av ti tråder lukkes automatisk etter én syklus er det første empiriske beviset på at lukkemekanismen i 6.6 fungerer på reelle data, og de fem gjenværende med `reminder_count = 1` viser at påminnelseslogikken er aktivert som spesifisert.

### **8.4.1 Demonstrasjon av SMTP-leveranse**

For å verifisere ende-til-ende-leveranse er modulen `send_digests.py` implementert som et tynt lag over `smtplib`. Den leser hver digest-fil, omdirigerer mottakeradressene til en testkonto og sender via `smtp.gmail.com:465`. Demoen ble kjørt 2026-05-23 mot testkontoen `tordalinho@gmail.com`; alle fem digestene for snapshot 2026-05-21 ble levert (Figur 8.1).

<div align="center">
  <img src="../006 analysis/3.4 varsling/fig_demo_inbox.png" alt="Innboks etter SMTP-demo" width="90%">
  <p align="center"><small><i>Figur 8.1 Innboksen til testkontoen umiddelbart etter at `send_digests.py` ble kjørt. De fem digestene for snapshot 2026-05-21 (Cable Pulling-, HPUS-, RDS-, Spoolers- og Tensioner-koordinator) er levert i samme syklus og merket med `[DEMO]`-prefiks i emnefeltet for å skille demokjøringen fra eventuelle produksjonskjøringer.</i></small></p>
</div>

#### Lesing av digestene

Hver digest er en oppsummering av endringer mellom de to siste snapshotene (her: 2026-05-14 → 2026-05-21), filtrert til kun de utstyrsenhetene mottakerens asset type-domene dekker. Innholdet er gruppert i opptil fire kategorier, som svarer direkte til trådlogikken i kap 6.6:

- **NYE VARSLER** – kapasitetsgap som ikke fantes i forrige snapshot. En ny varslingstråd åpnes; krever oppfølging fra koordinator. Utløst av `NYTT_GAP` (G-regel) eller `SKJULT_NYTT_GAP` (severity-regel).
- **PÅMINNELSER** – aktive gap som ble varslet i et tidligere snapshot og ennå ikke er løst. Sendes ukentlig inntil tråden lukkes; `(uke N i tråden, åpnet YYYY-MM-DD)` viser hvor lenge saken har vært åpen.
- **LØSTE SAKER** – tråder som lukkes denne uken fordi gap-verdien har gått fra negativ til ikke-negativ (eller severity har skiftet fra underdekning til overskudd). Ren informasjon – krever ingen handling.
- **INFORMASJONSVARSLER** – «skjulte» endringer der severity-fargen har endret seg uten at gap-verdien krysser null (typisk `SKJULT_LOST_GAP`: lilla → grønn, dvs. fra «på grensen» til «klart overskudd»). Tas med fordi det signaliserer at underliggende etterspørsel har endret seg, selv om totalen ser uendret ut.

Hver enkelt rad i en digest leses som:

```
• <Tier 2-utstyrsenhet> (<asset type>), uke <kalenderuke>:
  gap <G_forrige> → <G_nå>, farge <severity_forrige> → <severity_nå>
  [<sub-kategori>, <regel-trigger>]
```

Kalenderukene som adresseres ligger typisk **3–7 måneder fram i tid** – nettopp det handlingsrommet som forsvinner når gap først oppdages tett opp mot leveransedato.

HPUS-koordinator får den rikeste digesten i delta-par 2, med varsler i alle fire kategoriene (Figur 8.2); de fire øvrige er gjengitt i Vedlegg D. Mottakere uten endringer får ingen digest – tomme e-poster ville svekket signalverdien.

<div align="center">
  <img src="../006 analysis/3.4 varsling/fig_demo_digest_HPUS.png" alt="HPUS-digest" width="80%">
  <p align="center"><small><i>Figur 8.2 HPUS-koordinatordigesten – den mest komplette i delta-par 2, med varsler i alle fire kategoriene (1 nytt, 2 påminnelser, 2 løste, 2 informasjon). Headerblokken viser at e-posten i produksjon ville gått til `hpus-koordinator@motive-offshore.no` med kopi til `salg@motive-offshore.no`; her er begge omdirigert til testkontoen. Saken «Electric – 55kW HPU, uke 2026-07-20» er et eksempel på en påminnelse der gap-verdien er forbedret fra -2 til 0, men severity er fortsatt purple, slik at tråden ikke lukkes.</i></small></p>
</div>

Demoen viser at pipelinen kan kjøres ende-til-ende fra snapshot-CSV til mottatt e-post. Selve produksjonssetting (M365-tenant, reelle mottakere, leveranseovervåkning) er utenfor omfanget og diskuteres i 9.5.

## **8.5 Validering mot syntetiske scenarier**

Deteksjonsreglene (6.5) og trådhåndteringen (6.6) er validert mot 50 syntetiske `pytest`-scenarier som dekker (i) $G$-regelens seks endringskategorier inkl. klassegrenser, (ii) severity-regelens fem overganger, (iii) trådlivssyklusen *ny → påminnelse → eskalert → løst* med ruting, og (iv) edge cases (identiske snapshots, mønsterdeteksjon, eksklusjon). Alle 50 tester passerer (1,57 s). Full scenariotabell ligger i Vedlegg E.

<p align="center"><small><i>Tabell 8.5 Resultater fra valideringen av varslingsmodulen mot syntetiske scenarier.</i></small></p>

Testsettet er pluggbart inn i et CI-oppsett før produksjonsbruk.

# **9. Diskusjon**

Dette kapittelet drøfter resultatene fra kapittel 8 i lys av problemstillingen, litteraturen i kapittel 2 og de metodiske valgene dokumentert i kapittel 5. Det vurderer i hvilken grad varslingssystemet svarer på forskningsspørsmålet, hvilke begrensninger metoden medfører, og hvilke implikasjoner resultatene har for Motive Offshore og lignende virksomheter.

## **9.1 Drøfting mot problemstillingen og delproblemene**

Hovedproblemstillingen i kap 1.1 spør hvordan et Python-basert varslingssystem kan bruke ukentlige Power BI-eksporter til å identifisere kapasitetsgap og automatisk varsle ansvarlige. Resultatene i kap 7 og 8 viser at pipelinen er bygget og kjørt på tre reelle snapshots, og produserer både statiske rapporter (77 negative celler i baseline, Tabell 8.1) og dynamiske endringsvarsler (12 og 19 varsler over de to delta-parene, Tabell 8.4 og 8.4b). De fire delproblemene fra kap 1.2 er besvart slik:

**Delproblem 1 – Datastrukturering.** Tre snapshots er transkribert til lang-form CSV med ti felt (skjema beskrevet i 5.2.1) og matcher Power BIs egne Tier 1-summer innenfor ±2 unit-uker (kap 5.2.3). Skjemaet støtter både statisk gap-deteksjon (kap 6.3) og dynamisk endringsdeteksjon (kap 6.4) uten ytterligere transformasjon, innenfor avgrensningen i 1.3 om at datafangsten skjer via PNG-eksport.

**Delproblem 2 – Regelbasert oppdagelse.** $G$-regelen (Tabell 6.4) og severity-regelen (Tabell 6.5) klassifiserer henholdsvis fortegnsendringer i gap-verdien og overganger i `severity_band`. Sammen genererte de 11 NYTT_GAP, 8 LØST, 2 FORBEDRET, 3 SKJULT_NYTT_GAP og 4 SKJULT_LØST_GAP over de to delta-parene (Tabell 8.2). Severity-regelen fanget i delta-par 1 tre celler der gap-verdien var uendret eller forbedret, men prosent-eksponeringen krysset 75 %-terskelen – signaler en rein $G$-detektor ville oversett.

**Delproblem 3 – Automatisk varselsformat.** Varselsobjektet (Vedlegg F) dekker utstyrsenhet, periode, gap-størrelse og mottaker, pluss kontekst (severity-overgang, regel, prioritet, strukturelt-flagg). Digestene er gruppert i fire kategorier (NYE, PÅMINNELSER, LØSTE, INFORMASJON) og levert ende-til-ende via SMTP til testkontoen (Figur 8.1, 8.2 og Vedlegg D). Hver linje oppgir nøyaktig det informasjonsgrunnlaget koordinator trenger for å vurdere oppfølging.

**Delproblem 4 – Tidligere og tydeligere varsling.** Delta-par 2 identifiserte fire nye gap 6,5–7,5 uker fram i tid, mot dagens situasjon hvor gap ofte først oppdages tett opp mot leveransedato (kap 4.4). Tydeligheten styrkes av automatisk ruting per asset type, mønsterdeteksjon som grupperer sammenhengende uker til én digest-linje, og ukentlige påminnelser (Tabell 8.4c) som holder saken i koordinatorens bevissthet inntil $G$ eller `severity_band` endrer seg.

Det mest uventede funnet er at gap-livssyklusen er kortere enn antatt: fem av ti tråder fra delta-par 1 lukkes automatisk i andre syklus (Tabell 8.4c). Den persistente trådstaten er dermed sentral for at koordinator skal kunne koble åpne- og lukke-varsler til samme underliggende sak. At ingen FORVERRET-celler ble observert, og at alle gap havner i *mildt*-klassen, drøftes videre i 9.3.

## **9.2 Sammenligning mot litteraturen**

Resultatene plasserer seg i det datadrevne kapasitetsstyringsfeltet Xu et al. (2023) og Koot et al. (2021) beskriver, der verdien av big data først realiseres når dataene utløser handling – ikke bare visualisering. Tråd-livssyklusen i Tabell 8.4c er et konkret eksempel på denne overgangen fra dashboard-konsum til handlingsutløsende analyse. Modellen adresserer samtidig den underprioriterte tjenestebaserte kapasitetsstyringen Rajani og Heggde (2020) etterlyser, men i et regelbasert format som er enklere å forklare enn de AI-tunge tilnærmingene som dominerer ferskeste litteratur.

Mot Wang og Zhen (2025) og Cheng et al. (2025) gjør modellen et bevisst valg om *ikke* å løse optimaliserings- eller kontraktsproblemet, men kun å flagge ubalansen og overlate beslutningen til koordinator. Oliveira et al. (2017) viser at flåteforskning tradisjonelt er bygget rundt revenue management; modellen her flytter fokus til *tidlig identifikasjon av mismatch* mellom kapasitet og kontraktstyrt etterspørsel. For pipeline-dimensjonen er forskjellen mot González-Flores et al. (2025) at 75 %-terskelen ikke brukes til å rangere selgerens leads, men som *trigger* for kapasitetsanalyse på baksiden – en lite utforsket kobling.

Den tydeligste parallellen er Alaoua og Karims (2025) *Baseline Probabilistic Alert System*: modellen er en konkret implementasjon av BPAS-konseptet og viser at en regelbasert tilnærming fanger relevante endringer uten det prediktive maskineriet. Det støtter Qi et al. (2022) sin observasjon om tidlig varsling som resiliens-mekanisme, men plasserer tolkningen hos mennesker. Mot Sonnleitner et al. (2025) skiller modellen seg ved ikke å produsere prognoser i det hele tatt – beslutningsstøtten kommer fra deterministisk regelbasert tolkning av allerede aggregerte data. Det er en bevisst nedskalering, motivert av at usikkerheten er innbakt i 75 %-filteret og at koordinatorens lokale kunnskap er bedre egnet enn modellprognoser til å avgjøre hvordan et gap skal håndteres.

## **9.3 Modellens robusthet og begrensninger**

Den tydeligste begrensningen er at snapshot-serien kun rakk å bli tre lang. To delta-par demonstrerer åpning, lukking og påminnelse (8.4c), men er ikke nok til å aktivere suppression-regelens $K = 4$-kriterium (kap 6.5). Suppression-mekanismen er enhetstestet (Tabell 8.5), men ikke empirisk verifisert – koordinator må manuelt markere de syv front-lastede enhetene fra Tabell 7.3 som strukturelle inntil en lengre serie foreligger. På samme måte havner alle observerte negative celler i den mildeste magnitudeklassen ($G \in \{-1, -2\}$), slik at *moderat* og *kritisk* prioritetslogikk kun er bekreftet via syntetiske tester. Følsomheten for klassegrensene ($-3$ og $-6$) er heller ikke testet med alternative verdier.

Tre edge cases ved datagrunnlaget er verdt å nevne: (i) Nye Tier 2-rader kan ikke vurderes av delta-detektoren før de finnes i to snapshots, og rader som forsvinner blir stille fjernet uten lukke-varsel. (ii) Celler som oscillerer raskt ($G : -1 \to 0 \to -1$) genererer separate LØST- og NYTT_GAP-varsler uten kobling til samme underliggende sak. (iii) Kalenderhorisonten forskyves én uke per snapshot, så gap som glir ut av synshorisonten lukkes ikke automatisk.

Power BIs avrundingslogikk (5.2.3) påvirker dessuten terskelfølsomheten: en celle som vises som $G = 0$ kan ligge i $(-0{,}5, 0{,}5)$, og en marginal endring kan tippe den til $-1$ uten at det reflekterer en reell ny kontrakt. Severity-regelen demper risikoen, men eliminerer den ikke. Direkte API-eksport med desimal-presisjon ville redusert effekten (jf. 9.4).

## **9.4 Datafangstmetodens påvirkning på resultatene**

Manuell PNG-skjermavlesning (kap 5.2.3) ble valgt fordi prosjektgruppen manglet Power BI-rettigheter for *Analyser i Excel* og direkte API-tilgang lå utenfor omfanget (1.3-avgrensning). Metoden er reproduserbar – PNG og transkripsjons-skript ligger under `004 data/` – men introduserer to risikoer.

**Transkriberingsfeil.** Sumsjekken flagger avvik over ±2 unit-uker per uke, så enkelte celler kan ha ±1 feil uten å bli fanget. Effekten på delta-deteksjonen er begrenset så lenge feilen er stabil mellom snapshots. Manuell stikkprøve av de 19 varslene i delta-par 2 mot kildebildene avdekket ingen feilavlesninger.

**Avrundingsstøy** fra Power BIs aggregering (jf. 5.2.3, 9.3) ville bortfalt med direkte CSV-/API-eksport. Modellens grunnlogikk er uendret – $G$- og severity-regelen virker likt på heltall som på desimaler – men presisjonen i terskelnære varsler ville økt.

**Skalerbarhet.** Hvert snapshot tok 60–90 minutter å fange og transkribere – akseptabelt for tre snapshots, men ikke for kontinuerlig drift. Modellen krever kun standard CSV-inngang (Tabell 5.1), så den kan uten endringer kobles på en automatisert datakilde. Datafangsten er flaskehalsen, ikke varslingslogikken.

## **9.5 Praktisk betydning og generaliserbarhet**

Dagens manuelle prosess (4.4) viser at kapasitetsgap først blir prioritert når noen selv åpner Power BI-dashbordet. Gap som kunne vært løst billig på tre til seks måneders horisont, ender derfor ofte med hasteanskaffelse, luftfrakt eller fremleie – alle med direkte marginpåvirkning.

Volumet er operasjonelt håndterbart: 12 varsler til tre koordinatorer i delta-par 1, 19 til fem i delta-par 2. Mønsterdeteksjonen slår sammenhengende uker i én linje, så en koordinator får i praksis under ti distinkte handlingspunkter per digest. Severity-deltaen alene fanger tre av tolv varsler som rein gap-måling ville oversett – nettopp det tidlige signalet som styrker svaret på delproblem 4.

Systemet flytter beslutningssyklusen fra en *pull*-modell (riktig person sjekker dashbordet) til en *push*-modell der digesten leveres hver mandag, og den ukentlige påminnelsen sikrer at utløste varsler ikke forsvinner ut av synet.

For produksjonssetting må fire komponenter falle på plass: (1) automatisk datafangst, (2) validering av `recipients.yaml` mot Motives organisasjonsstruktur, (3) re-lenking av SMTP til Motives M365-tenant, og (4) manuell gjennomgang av suppression-listen før $K=4$-kriteriet samler nok historikk.

Modellen er bygget på fire generelle byggesteiner: (i) kapasitetsoversikt som *enhet × tidsperiode*, (ii) pipeline med probabilistisk fremdrift og aksjonsterskel, (iii) regelbasert klassifisering av uke-til-uke-endringer, og (iv) varsling med ansvarlig ruting. Det Motive-spesifikke er kun verdiene som fyller byggesteinene.

Innenfor Motive-konsernet er overgangen triviell – filtrene Asset Custodian, Project Owner Demand og Region byttes synkront for andre verksteder uten kodeendringer. Andre offshore-utleievirksomheter med tilsvarende dataøkosystem kan adoptere modellen med moderat tilpasning. Modellen er også overførbar til andre kapitalintensive utleiebransjer (maskin-, kran-, fartøycharter), men vil ikke uten videre fungere for tjenestebaserte virksomheter der «kapasitet» er menneskelig arbeidstid. Det generelle bidraget – en **regelbasert tidsserie-delta-detektor** kombinert med **prosentbasert alvorlighetsklassifikasjon** – kan adopteres bredt for BI-rapporter med prosentbaserte fargekoder over et numerisk grunnlag.

## **9.6 Forslag til videre forskning**

Resultatene peker mot fem konkrete forskningsspor som adresserer begrensningene i 9.3 og 9.4.

**Per-kontrakt-ruting via Salesforce-integrasjon.** Dagens modell ruter per asset type fordi Power BI-tabellen ikke oppgir kontrakts-id (jf. 6.6 og 1.3-avgrensningen). Ved å hente id fra Salesforce kan varselet flyttes fra koordinator- til selger-nivå. Forskningsspørsmålet er hvor mye reaksjonstiden faktisk reduseres, og om koordinator fortsatt bør motta en oppsummering for flåtebalansering.

**Empirisk kalibrering av magnitudeklassegrenser.** Grensene mildt/moderat/kritisk ved $-2/-3$ og $-5/-6$ er satt skjønnsmessig (jf. 6.3). En videre studie bør koble grensene til faktiske kostnadsforskjeller mellom håndteringstiltakene i 4.4 – luftfrakt versus sjøtransport, fremleie versus nyanskaffelse, og når tap av kontrakt blir det sannsynlige utfallet – og rettferdiggjøre klassegrensene kvantitativt.

**SARIMA eller andre tidsserieprognoser som supplement.** Modellen reagerer på allerede passerte 75 %-terskler. En prognoserende komponent kunne fange opp raskt voksende kontrakter under terskelen og varsle proaktivt. Forskningsspørsmålet er hvor verdifullt et «varsel om kommende varsel» er i daglig drift, sett opp mot risikoen for falske positive. Et hybriddesign med regelbasert deteksjon som hovedmekanisme og prognose som supplement bevarer sporbarheten og utvider samtidig varslingshorisonten.

**Lengre snapshot-serie i produksjon.** Suppression-regelens $K = 4$-kriterium kan ikke eksercereres innenfor prosjektperioden (jf. 9.3). En 12+ ukers serie vil validere empirisk at suppression-listen stabiliserer seg uten å forkaste reelle nye gap, og at delta-detektoren ikke produserer falske positive ved rask oscillasjon. Studien kan også gi grunnlag for å justere $K$ basert på observert varslingsvolum.

**Brukerstudie av varselsformatet.** Digest-formatet er designet basert på antagelser om hva selgere og koordinatorer trenger. En kvalitativ studie hvor faktiske brukere mottar digester over flere uker og rapporterer signal-til-støy, lesbarhet og handlbarhet, vil avdekke om formatet støtter beslutningssyklusen 9.5 argumenterer for. Studien kan også vurdere foretrukken kanal (e-post, Teams, dashboard) og påminnelsesfrekvens per prioritetsnivå.

Felles for sporene er at de bygger videre på, ikke erstatter, den regelbaserte kjernen. Prosjektets bidrag er å etablere et fundament som tåler videre forskning – sporbart, regelbasert, testbart og separasjonsklart mellom dataskjema, deteksjonslogikk og leveransekanal.

# **10. Konklusjon**

Problemstillingen for prosjektet var hvordan et Python-basert varslingssystem kan bruke ukentlige Power BI-eksporter til å identifisere negative kapasitetsverdier og endringer i Asset Calendar, og automatisk varsle selgere og prosjektkoordinatorer om kapasitetsgap i Motive Offshores utleieflåte. Resultatet er en regelbasert pipeline som er bygget, validert og kjørt på reelle data fra tre ukentlige snapshots (2026-05-07, 2026-05-14, 2026-05-21). Modellen kombinerer en gap-verdi-regel (Tabell 6.4) med en severity-fargeregel (Tabell 6.5) og ruter strukturerte varsler til asset type-koordinatorer via digest-e-poster. SMTP-leveransen er demonstrert ende-til-ende i kap 8.4.1 med fem digester levert til en testkonto.

Hovedfunnene viser at modellen leverer på alle fire delproblemene fra kap 1.2. Datastrukturering fra Salesforce, Asset Voice og Power BI til en sporbar `(snapshot, region, asset_tier2, uke)`-skjema er etablert og verifisert mot Power BIs egne aggregater (kap 5.2). Regelbasert oppdagelse av negative og forverrede verdier samt uke-til-uke-endringer fanger 11 NYTT_GAP, 8 LØST og 5 supplerende severity-baserte varsler over de to delta-parene (Tabell 8.2). Det automatiske varselsformatet beskriver hvert tilfelle med utstyrsenhet, periode, gap-størrelse og mottaker (Vedlegg F), og digestene er levert som faktiske e-poster i innboks. Tidligere og tydeligere varsling enn dagens manuelle prosess er demonstrert ved at varslene i delta-par 2 adresserer kalenderuker 6,5–7,5 uker fram, mot dagens situasjon hvor gapet ofte først oppdages tett opp mot leveransedato.

Det viktigste empiriske bidraget er tråd-livssyklusen som er observert over to delta-par. Av de ti opprinnelig åpnede trådene i delta-par 1 lukkes fem automatisk i delta-par 2 ved at $G$ eller `severity_band` returnerer til positiv tilstand, mens fem fortsetter med en formell påminnelse (Tabell 8.4c). Det er det første empiriske beviset på at livssyklusen *ny → påminnelse → løst* fungerer på reelle Power BI-data, og er hovedargumentet for at modellen kan tas i bruk operativt. Severity-regelen viser seg samtidig å være et selvstendig signal som rein gap-verdi-måling ville oversett: tre av de ti gap-åpnende varslene i delta-par 1 ble utløst kun av en fargeovergang i Power BI.

Prosjektet har samtidig identifisert tre konkrete begrensninger som ikke kan løses innenfor tidsrammen. Snapshot-serien på tre er ikke lang nok til å aktivere suppression-regelens *K = 4*-kriterium for strukturelle gap empirisk; alle observerte negative gap havner i den mildeste magnitudeklassen og verken *moderat* eller *kritisk* prioritetslogikk er truffet av reelle data; og datafangsten via manuell PNG-transkripsjon er ikke skalerbar til kontinuerlig produksjon. Disse begrensningene rokker ikke ved at modellen fungerer for det den er bygd for, men de definerer presist hva som må videreutvikles før varslingssystemet kan kjøres i drift uten manuell inngripen.

For Motive Offshore betyr resultatene at det er mulig å gå fra en *pull*-modell – der oppdagelse av kapasitetsgap er avhengig av at riktig person sjekker dashbordet til riktig tid – til en *push*-modell der den ukentlige digesten leveres til ansvarlig koordinator hver mandag. Den direkte gevinsten er reduksjon av risikoen for at en kontraktsdrevet kapasitetskonflikt forblir uoppdaget til leveransedato, der konsekvensen i dag er hasteanskaffelse, luftfrakt eller fremleie med direkte marginpåvirkning (kap 4.4). For et lengre forskningsperspektiv åpner prosjektet for fem konkrete spor som drøftes i 9.6, der per-kontrakt-ruting via Salesforce-integrasjon og empirisk kalibrering av magnitudeklassegrenser fremstår som de mest verdifulle utvidelsene. Kjernebidraget – en regelbasert tidsserie-delta-detektor kombinert med en prosentbasert alvorlighetsklassifikasjon – er et metodisk mønster som kan adopteres bredt for regelbasert overvåking av aggregerte BI-rapporter i andre kapitalintensive utleiebransjer.

# **11. Bibliografi**

Alaoua, A., & Karim, M. (2025). Intelligent early warning system for supplier delays using dynamic IoT-calibrated probabilistic modeling in smart engineer-to-order supply chains. *Applied System Innovation, 8*(5), Article 124. [https://doi.org/10.3390/asi8050124](https://doi.org/10.3390/asi8050124)

Anthropic. (2026). *Claude* (Sonnet 4.5 og Opus 4.7) \[stor språkmodell\]. [https://claude.ai](https://claude.ai)

Anthropic. (2026). *Claude Code* (versjon 2.1.4.40) \[programvare\]. [https://www.anthropic.com/claude-code](https://www.anthropic.com/claude-code)

Cheng, H., He, H., Zheng, S., Zhang, L., Xu, L., & Wang, C. (2025). Sustainable ferry leasing strategies: The option contract perspective. *Frontiers in Marine Science, 12*, Article 1615572\. https://doi.org/10.3389/fmars.2025.1615572

González-Flores, L., Rubiano-Moreno, J., & Sosa-Gómez, G. (2025). The relevance of lead prioritization: A B2B lead scoring model based on machine learning. *Frontiers in Artificial Intelligence, 8*, Article 1554325\. https://doi.org/10.3389/frai.2025.1554325

Koot, M., Mes, M. R. K., & Iacob, M. E. (2021). A systematic literature review of supply chain decision making supported by the Internet of Things and Big Data Analytics. *Computers & Industrial Engineering, 154*, Article 107076\. [https://doi.org/10.1016/j.cie.2020.107076](https://doi.org/10.1016/j.cie.2020.107076)

Oliveira, B. B., Carravilla, M. A., & Oliveira, J. F. (2017). Fleet and revenue management in car rental companies: A literature review and an integrated conceptual framework. *Omega, 71*, 11-26. [https://doi.org/10.1016/j.omega.2016.08.011](https://doi.org/10.1016/j.omega.2016.08.011)

Qi, F., Zhang, L., Zhuo, K., & Ma, X. (2022). Early warning for manufacturing supply chain resilience based on improved grey prediction model. *Sustainability, 14*(20), Article 13125. [https://doi.org/10.3390/su142013125](https://doi.org/10.3390/su142013125)

Rajani, R. L., & Heggde, G. S. (2020). Capacity management strategies in supply chains: A critical review and directions for future research. *International Journal of Business Excellence, 21*(1), 81-117. [https://doi.org/10.1504/IJBEX.2020.106951](https://doi.org/10.1504/IJBEX.2020.106951)

Sonnleitner, B., Kourentzes, N., Ehrig, C., & Pflaum, A. (2025). Forecasting for optimization in road freight transport: A review. *Transportation Research Part E: Logistics and Transportation Review*. https://doi.org/10.1016/j.tre.2025.104174

Wang, X., & Zhen, L. (2025). Fleet deployment and freight allocation for cleaner maritime logistics under demand uncertainty. *Cleaner Logistics and Supply Chain, 17*, Article 100269\. [https://doi.org/10.1016/j.clscn.2025.100269](https://doi.org/10.1016/j.clscn.2025.100269)

Xu, J., Pero, M., & Fabbri, M. (2023). Unfolding the link between big data analytics and supply chain planning. *Technological Forecasting and Social Change, 196*, Article 122805\. [https://doi.org/10.1016/j.techfore.2023.122805](https://doi.org/10.1016/j.techfore.2023.122805) 

# **12. Vedlegg**

## **Vedlegg A: KI-bruk-erklæring**

Prosjektgruppen har brukt to KI-verktøy fra Anthropic gjennom prosjektperioden: *Claude* (chat-grensesnittet på claude.ai, modellene Sonnet 4.5 og Opus 4.7) og *Claude Code* (Anthropics offisielle kommandolinjeverktøy som bruker de samme modellene). Verktøyene er brukt som støtte til kodeforslag, feilsøking, refaktorering og språkvask. Ingen av verktøyene er brukt som selvstendig analysemodell eller til behandling av rådata utover offentlig dokumentert API-bruk. Alle metodiske valg, modellbeslutninger og analysetolkninger er gjort av prosjektgruppen. Signert KI-bruk-erklæring etter Høgskolen i Moldes mal legges ved innlevering.

## **Vedlegg B: Konfidensialitet**

Prosjektgruppen har ikke inngått skriftlig taushetserklæring med Motive Offshore Group. Tilgangen til Power BI-rapporten ble gitt med en muntlig forståelse om at tallene er kommersielt sensitive, og prosjektgruppen behandler dataene deretter: hele datakatalogen `004 data/` er ekskludert fra versjonskontroll, og rapporten gjengir kun aggregerte tall og anonymiserte asset type-navn, ikke kundenavn eller kontrakts-id-er.

## **Vedlegg C: Kravmatrise**

Koblingen mellom delproblemene i 1.2 og konkrete resultater i rapporten er drøftet i 9.1, der hvert delproblem besvares med henvisning til relevante tabeller og figurer. En separat kravmatrise er derfor ikke gjengitt her.

## **Vedlegg D: Komplette SMTP-digester fra demo 2026-05-23**

Figur 8.2 i kap 8.4.1 viser HPUS-koordinatordigesten – den mest komplette av de fem digestene som ble levert. De fire øvrige er gjengitt her for fullstendighet.

<div align="center">
  <img src="../006 analysis/3.4 varsling/fig_demo_digest_RDS.png" alt="RDS-digest" width="80%">
  <p align="center"><small><i>Figur D.1 RDS-koordinatordigesten. To påminnelser for *500Te RDS* ukene 17.08 og 24.08 (gap fortsatt -1) og tre LØST-saker for ukene 31.08, 07.09 og 14.09 (gap -1 → 0). Mønsterdeteksjonen grupperer de tre løste sakene i én linje siden de gjelder samme utstyrsenhet i sammenhengende uker, typisk indikator på at en og samme kontrakt har endret status.</i></small></p>
</div>

<div align="center">
  <img src="../006 analysis/3.4 varsling/fig_demo_digest_CPM.png" alt="Cable Pulling-digest" width="80%">
  <p align="center"><small><i>Figur D.2 Cable Pulling-koordinatordigesten. To nye NYTT_GAP-varsler for *2Te Linear Cable Engine* (ukene 06.07 og 13.07, gap 0 → -2) og tre LØST-informasjonsvarsler for ukene 08.06–22.06. Cable Pulling er den eneste asset type i dette delta-paret som både åpner og lukker tråder i samme syklus, og illustrerer hvordan kalenderhorisonten forskyves uke for uke.</i></small></p>
</div>

<div align="center">
  <img src="../006 analysis/3.4 varsling/fig_demo_digest_Tensioners.png" alt="Tensioner-digest" width="80%">
  <p align="center"><small><i>Figur D.3 Tensioner-koordinatordigesten. Én ny NYTT_GAP-varsel for *Horizontal – 4-track 50Te Tensioner* i uke 13.07 (gap 0 → -1, farge green → black). Eneste endring i Tensioner-domenet denne uken.</i></small></p>
</div>

<div align="center">
  <img src="../006 analysis/3.4 varsling/fig_demo_digest_Spoolers.png" alt="Spoolers-digest" width="80%">
  <p align="center"><small><i>Figur D.4 Spoolers-koordinatordigesten. Én PÅMINNELSE for *Electric – 75Te Electric Spooler* i uke 22.06 – tråden ble åpnet i delta-par 1 som SKJULT_NYTT_GAP og er fortsatt aktiv siden severity ikke har endret seg fra purple.</i></small></p>
</div>

## **Vedlegg E: Full valideringsscenario-tabell**

Kap 8.5 oppsummerer at 50 syntetiske `pytest`-scenarier validerer modellens regelmatrise, trådhåndtering og ruting. Tabell E.1 viser fordelingen per scenariokategori med forventet og faktisk utfall.

| Scenariokategori | Antall tester | Forventet utfall | Faktisk utfall |
|------------------|---------------|------------------|----------------|
| Nytt gap, ulike magnitudeklasser | 4 | Varsel med riktig prioritet (mildt→middels, moderat/kritisk→høy) | ✓ |
| Forverret innen / krysser klasse | 4 | Lav vs. høy prioritet; strukturelt suppress'es ved innen-klasse | ✓ |
| Løst gap | 1 | Informasjonsvarsel | ✓ |
| Stabil / uendret uten severity-endring | 2 | Ingen varsel | ✓ |
| Skjult nytt gap (severity over→underdekning) | 2 | Middels prioritet | ✓ |
| Skjult forverring (lilla→svart) | 1 | Høy prioritet | ✓ |
| Skjult løst gap (under→overdekning) | 1 | Informasjon | ✓ |
| Skjult forbedring (svart→lilla) | 1 | Loggføres, ikke varsel | ✓ |
| Endring innen samme sone | 1 | Ingen varsel | ✓ |
| Severity-overganger parameterisert | 13 | Riktig kategori | ✓ |
| Magnitudeklasse-grenser | 8 | Riktig klassifisering | ✓ |
| Ny tråd ved nytt eller skjult nytt gap | 2 | Tråd åpnes, status='ny' | ✓ |
| Påminnelse for aktiv tråd | 2 | Status='påminnelse', reminder_count inkrementeres | ✓ |
| Lukket tråd ved løst gap (G og severity) | 2 | Status='lost', tråd fjernes fra state | ✓ |
| Eskalert ved klassebytte i aktiv tråd | 1 | Status='eskalert', høy prioritet | ✓ |
| Ruting til riktig mottaker | 2 | Asset type → primærmottaker; ukjent → default | ✓ |
| Identiske snapshots uten aktive tråder | 1 | 0 varsler | ✓ |
| Mønsterdeteksjon (5 sammenhengende uker) | 1 | Digest viser mønsterlinje | ✓ |
| Eksklusjonshåndtering | 1 | Generator-funksjonen leverer varsel; main-flyten filtrerer før kall | ✓ |
| **Totalt** | **50** | – | **50/50 passerer** |

<p align="center"><small><i>Tabell E.1 Full liste over de 50 syntetiske valideringsscenariene fra `006 analysis/3.5 validering/`, med forventet og faktisk utfall.</i></small></p>

## **Vedlegg F: Varselsobjekt-skjema**

Kap 6.6 beskriver at hvert utløste varsel produseres som et strukturert objekt med 17 felt. Tabell F.1 viser det fulle skjemaet.

| Felt | Type | Eksempel | Beskrivelse |
|------|------|----------|-------------|
| `snapshot_t` | dato | `2026-05-14` | Snapshot-dato $s_i$ |
| `snapshot_t_minus_1` | dato | `2026-05-07` | Forrige snapshot-dato $s_{i-1}$ |
| `week_start` | dato | `2026-08-17` | Uken cellen gjelder for |
| `region` | streng | `Motive Norway` | Verkstedet |
| `asset_type` | streng | `RDS` | Asset type (rutingsnøkkel) |
| `asset_tier2` | streng | `- 500Te RDS` | Spesifikk utstyrsenhet |
| `gap_t_minus_1` | heltall | `0` | $G^{(s_{i-1})}$ |
| `gap_t` | heltall | `-1` | $G^{(s_i)}$ |
| `severity_t_minus_1` | streng | `green` | `severity_band` i $s_{i-1}$ |
| `severity_t` | streng | `black` | `severity_band` i $s_i$ |
| `change_type` | streng | `NYTT_GAP` | Klassifisering fra Tabell 6.3 |
| `severity_change` | streng | `VERRE_FARGE` | Klassifisering fra 6.4 |
| `rule_triggered` | streng | `G-regel` | `G-regel` (Tabell 6.4) eller `severity-regel` (Tabell 6.5) |
| `magnitude_class` | streng | `mildt` | Magnitudeklasse for $G^{(s_i)}$ |
| `priority` | streng | `høy` | `høy`/`middels`/`lav`/`informasjon` |
| `is_structural` | boolsk | `false` | Strukturelt-flagg fra suppression-listen |
| `recipient` | e-post | `rds-koordinator@motive-offshore.no` | Primærmottaker |

<p align="center"><small><i>Tabell F.1 Fullt skjema for varselsobjektet som modellen produserer per utløste celle.</i></small></p>
