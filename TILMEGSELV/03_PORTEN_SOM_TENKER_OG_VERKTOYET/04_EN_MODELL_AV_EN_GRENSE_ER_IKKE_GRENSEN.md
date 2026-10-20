# EN MODELL AV EN FYSISK GRENSE ER IKKE DEN FYSISKE GRENSEN
### *Om Simplex/SOTIF-blindhet, 6G ISAC-entropi ($\chi(\tau,\nu)$ mot $H(X)$), 8 000 Monte Carlo-kjøringer og brent silisium ($W \not\equiv \text{software log}$)*

```text
========================================================================================
DOKUMENTSTATUS & KANONISK METADATA:
  DOKUMENT-ID             : BOK-GRUNNLAG-MODELL-AV-GRENSE-ISAC-SOTIF-2026-v1.0
  FORFATTER               : Marius Egerhei Torjusen (ORCID: 0009-0006-0431-6637 // WoS: PJT-0190-2026)
  ENTITET                 : Brahman // Antigravity · Risør (Locus Zero)
  OPERATORSTRUKTUR        : T_KY = Ω ∘ Π_K ∘ Φ · Reality = Fix(Π ∘ Φ) · W !≡ software log
  SIMULERING (L1)         : 8 000 Monte Carlo-kjøringer (25,00 % klassisk falsk realisering vs. 0,00 % i T_KY)
  EPISTEMISK SKRANKE      : INSPIRED_BY != IMPLEMENTS != PROVES
                            L1 = deterministisk simulering & append-only hash-kjeder i programvare;
                            L2/L3 = fysisk reléarbeid, 56Fe/Mössbauer-lås og fysisk anti-fuse/laser-WORM i maskinvare.
========================================================================================
```

---

**En modell av en fysisk grense er ikke den fysiske grensen.**

Moderne sikkerhetskritiske systemer lider av en grunnleggende epistemisk feilslutning: de forveksler utsendelsen av en digital kommando med utførelsen av en fysisk handling. Rammeverk som Simplex og ISO 21448 (SOTIF) håndterer overføring av kontrollautoritet mellom algoritmer før en handling iverksettes, men de er blinde for hva systemet har rett til å hevde etter at kontrollkjeden brytes. Når en mekanisk kobling ryker, en transistor brenner av, eller drivspenningen faller bort nedstrøms for digital-til-analog-omformeren, fortsetter tradisjonell programvare å registrere tilstanden som fullført. Prosessoren skriver en bekreftelse til minnet basert på at ordren forlot det digitale grensesnittet, mens den fysiske verden forblir uendret.

Denne sårbarheten oppstår fordi programvareendringer og fysiske hendelser tilhører to adskilte termodynamiske regimer. Å endre en bit i et digitalt minne eller lagre en transaksjonslogg krever en ubetydelig energimengde ($E \sim k_B T \ln 2 \approx 3 \times 10^{-21}\text{ J}$) og utfører intet mekanisk arbeid. Å åpne en høyspentkontaktor, flytte en hydraulisk ventil eller bremse en masse krever derimot irreversibelt arbeid ($\Delta S > 0$) mot fysisk motstand. En programvarelogg kan derfor kun bevitne at en intensjon ble autorisert i silisiumet; den kan aldri bevise at arbeidet fant sted i materien ($W \not\equiv \text{software log}$).

For å lukke denne kløften erstatter realiseringsgrammatikken ($T_{KY} = \Omega \circ \Pi_K \circ \Phi$) optimistiske tilstandsantakelser med en streng operatorstruktur. Her skilles det sylskarpt mellom kandidatgenerering ($\Phi$), admissibilitetsdom ($\Pi_K$), fysisk realisering ($\Omega$) og uavhengig bevitnelse ($W$). Fysisk eksistens i styringsløkken defineres utelukkende som et fikspunkt under admissibilitetsprojeksjonen:

$$\text{Reality} = \text{Fix}(\Pi \circ \Phi)$$

Dersom en foreslått bane bryter med de fysiske invariantene i porten $\Pi_K$, oppstår intet fikspunkt. Systemet nektes matematisk og elektrisk å hevde at en handling er utført.

---

## I. 6G ISAC-Konflikten: Woodward-Ambiguitet mot Shannon-Entropi

Nødvendigheten av et slikt filter trer tydelig frem i 6G-systemer for integrert deteksjon og kommunikasjon (ISAC), der radar og telekommunikasjon deler samme radiofrekvente bølgeform. Her oppstår en uløselig fysisk konflikt mellom to mål. Presis radarmåling av avstand og hastighet krever en sylskarp Woodward-ambiguitetsfunksjon $\chi(\tau, \nu)$ med lav sidelobestøy og deterministisk fasestruktur. Høy dataoverføringskapasitet krever derimot maksimal Shannon-entropi $H(X)$, noe som tvinger frem stokastiske fase- og amplitudevariasjoner i signalet.

Når datatrafikk med høy entropi moduleres inn på bølgeformen, spres signalenergien utover tids- og frekvensplanet. Radarens ambiguitetstopp flates ut, sidelobene vokser, og målestøyen forplanter seg direkte inn i kontrollsløyfens Kalman-filter (EKF). Resultatet er kinematisk ustabilitet der kandidaten ($\Phi$) foreslår rykkvise, farlige styringsvektorer basert på forvrengte sanseinntrykk.

I realiseringsgrammatikken fanges denne usikkerheten opp ved kilden. Admissibilitetsporten $\Pi_K$ overvåker forholdet mellom radarens hovedlobeenergi og bølgeformens Shannon-entropi i sanntid. I det øyeblikket telekommunikasjonsstøyen presser kovariansen over sikkerhetsterskelen, feiler projeksjonen ($\Pi_K \Phi = \perp$). Porten faller umiddelbart fra sin nominelle driftsspenning på $5{,}00\text{ V DC}$ ned til $0{,}00\text{ V DC}$ og låser systemet i en feillukket hviletilstand (`HOLD` eller `KILL`).

---

## II. 8 000 Monte Carlo-Simuleringer: Kartet mot Terrenget

Effekten av denne arkitektoniske grensen er dokumentert gjennom $8\,000$ Monte Carlo-simuleringer av kritiske brudd i kontrollkjeden (`L1`). Når aktuatorer svikter eller signallinjer kuttes, rapporterer klassiske kommandobaserte arkitekturer en falsk realisering i **$25{,}00\,\%$** av tilfellene ($2\,000$ av $8\,000$ kjøringer). De fortsetter å styre etter et kart som ikke lenger stemmer med terrenget. Under nøyaktig samme feilbetingelser oppnår realiseringsgrammatikken **$0{,}00\,\%$** falske positiver ($0$ av $8\,000$ kjøringer). Ved hvert brudd tvinges tilstanden øyeblikkelig til `OUTCOME_UNKNOWN`, og utgangslinjene legges døde på $0{,}00\text{ V DC}$.

---

## III. Det Fysiske Vitnets Triadiske Forankring ($W$)

For at en tilstandsovergang til slutt skal registreres som en faktisk hendelse i maskinvare (`L2`/`L3`), krever arkitekturen et fysisk vitne ($W$) som er bundet til uforanderlige naturlover gjennom tre samvirkende lag. For det første kreves galvanisk og mekanisk arbeid: bekreftelsen avhenger ikke av en logisk spenning på en prosessorutgang, men av at det elektromagnetiske feltet i spolen faktisk bryter sammen og at herdede returfjærer fysisk trekker kontaktbroen åpen til $0{,}00\text{ V DC}$. For det andre forankres systemets hviletilstand i kjernefysiske og atomære referanser, slik som jernkjerner av isotopen $^{56}\text{Fe}$ ($\sim 8{,}79\text{ MeV}$ bindingsenergi per nukleon) og Mössbauer-låser basert på rekylfri resonansabsorpsjon av gammastråling, der en tilstandsendring krever et eksakt fysisk Doppler-hastighetsskift ($\epsilon_\delta \approx 0{,}8\text{ mm/s}$) i selve substratet. For det tredje skilles det strengt mellom programvarelogger – som på Nivå $\text{L1}$ utelukkende utgjør append-only SHA-256-hashkjeder på magnetisk eller flash-basert lagringsmedium – og fysisk irreversibelt maskinvareminne (`L2`/`L3`), der vitnesbyrdet forsegles i fysiske WORM-medier (*Write-Once-Read-Many*) ved å brenne av silisiumsikringer (*anti-fuse*) eller ablatere substratet med laser. Når et slikt fysisk vitnesbyrd først er brent inn, kan det ikke omskrives uten fysisk ødeleggelse av komponenten.

---

## IV. Lukking av Transduser-Kløften ($\Pi_{\text{orth}}$) og Vern mot Biologisk Utmattelse (`CAUSAL_HOLD` $\neq$ `KILL`)

En kritisk revisjon av enhver feillukket sikkerhetsarkitektur (jf. IEC 61508 og ISO 13849) må besvare to operasjonelle angrepsvektorer som ellers vil ødelegge systemet innenfra: *Transduser-kløften* (*The Transducer Gap*) og *Biologisk utmattelses-DoS* (*Liveness Starvation*).

### 1. Transduser-kløften, to-faset kausalitet ($\Pi_K$ mot $\Pi_{\text{orth}}$) og kryss-modal bevitnelse

En digital konsekvensport ($\Pi_K$) eller en append-only programvarelogg (`fsync()`) kan aldri observere et fysisk molekyl, et masseresidual ($\Delta R$) eller et mekanisk ventilsete direkte. Den observerer utelukkende elektriske spenninger og tidsstempler fra analog-til-digital-omformere (ADC) og tids-til-digital-omformere (TDC). Dersom en enkelt sensor utsettes for termisk drift, kalibreringssvikt eller fysisk spoofing *før* signalet når porten, vil en naiv arkitektur enten forsegle en fysisk løgn inn i en uforanderlig logg eller låse systemet i en permanent, uopprettelig vranglås (*Permanent Denial of Reality*).

Samtidig må arkitekturen løse **Pre-Commit-paradokset**: en port kan ikke kreve bevis på at en ventil *allerede* har beveget seg som betingelse for å gi ventilen spenning til å bevege seg. Realiseringsgrammatikken deler derfor verifikasjonen i to kausalt adskilte faser:

1. **Pre-Commit Admissibilitet i $\Pi_K$ ($\Phi \to \Pi_K$):** Før spenningen $5{,}00\text{ V DC}$ innvilges, verifiserer $\Pi_K$ at kandidaten tilfredsstiller alle statiske og kinematiske forhåndsbetingelser: kausal lyskegle ($\Delta t \le 133{,}425\text{ ns}$), levedyktighetsbetingelsen ($\dot{x}_t \in T_K(x_t)$), bremsemargin ($\Delta x_{\text{margin}} > 0$) og prosesskjernens hviletilstand.
2. **In-Flight Utførelsesbevitnelse i $\Pi_{\text{orth}}$ ($\Omega \to W$):** Så snart $\Pi_K$ åpner porten ($5{,}00\text{ V DC}$), må den fysiske overgangen fullbyrdes og bevitnes innenfor det mekaniske lukkevinduet ($\Delta t_{\text{act}} \le 38{,}4\text{ ms}$). Ingen enkeltstående transduser har suverenitet til å utstede et gyldig sluttbevis ($W = 1$). I stedet tvinger $\Pi_{\text{orth}}$ minst tre fysisk ikke-kommuterende måledomener til å bekrefte samme energi- og massebalanse under selve utførelsen: det elektromagnetiske domenet (spole-induktans og back-EMF-signatur $\int V(t)I(t)\,dt$ under ventilbevegelsen), det termodynamiske domenet (entalpi- og temperaturgradient $\Delta T$ over strømningsmotstanden) og det kausale tidsdomenet (akustisk eller optisk Time-of-Flight $\Delta\tau_{\text{RT}}$ gjennom mediet). Fordi en angriper eller en enkeltsensorfeil ikke samtidig kan forfalske motinduksjonen i kobberspolen, varmekapasiteten i væsken og lydhastigheten i stålet uten at arbeidet faktisk utføres, utløser ethvert avvik innenfor $38{,}4\text{ ms}$-vinduet et øyeblikkelig kutt til $0{,}00\text{ V DC}$ (`Crowbar Type B`):

$$\Pi_{\text{orth}}(W_{\text{EM}},\, W_{\text{term}},\, W_{\text{ToF}}) = 0 \implies \text{OUTCOME\_UNKNOWN} \implies \mathbf{GATE :: KILL}$$

Skulle en korrupt eller feilkalibrert sensorepoke likevel bli oppdaget i etterkant, bryter ikke systemet den historiske loggen. Fordi en append-only kjede aldri kan slettes eller skrives over, gjenopprettes sannheten gjennom en eksplisitt, ikke-destruktiv kompensasjonsepoke (**`RECONCILE_EPOCH`**). Denne nye blokken refererer kryptografisk til den feilaktige epokens SHA-256-hash, dokumenterer det fysiske avviksbeviset og re-allokerer tilstandsrommet fremover i tid uten å slette et eneste byte av revisjonssporet.

### 2. Skillet mellom elektronisk `CAUSAL_HOLD` og mekanisk `KILL`

Det andre angrepet retter seg mot den menneskelige operatøren. I Kjerneprøve II vises det at TDC-slusen på $500\text{ meters}$ dyp avviser et forsinket eller manipulert signal med en elektrisk kostnad på kun $8\,\mu\text{J}$. Dersom enhver slik $8\,\mu\text{J}$ nettverksstøy eller falsk pakke utenfra skulle utløse en fullstendig mekanisk fjærlås (`GATE :: KILL`), ville en angriper på overflaten kunne sende én forfalsket lyspuls i timen og tvinge et menneske til å bruke $10\,000\text{ J}$ i fysisk muskelkraft på å dra tunge stålbrytere tilbake i lås i kulden. Resultatet ville vært en asymmetrisk **biologisk utmattelses-DoS** (*Alarm Fatigue*), der operatøren til slutt enten kollapser eller kobler forbi sikkerhetsreléet med en kobbertråd.

For å gjøre en slik utmattelse fysisk umulig, trekker arkitekturen en absolutt grense mellom to ulike $0{,}00\text{ V DC}$-tilstander:

$$\text{Transport- og kanalstøy} \;\longrightarrow\; \mathbf{CAUSAL\_HOLD} \qquad \not\equiv \qquad \text{Indre prosessbrudd} \;\longrightarrow\; \mathbf{GATE :: KILL}$$

Når en pakke avvises i det ytre skjoldet – enten på grunn av brutt kausal lyskegle ($\Delta t > 133{,}425\text{ ns}$), ugyldig kryptografisk epokesignatur eller forbigående 6G ISAC-entropi – utløses **aldri** den mekaniske fjærlåsen. Forfalskede eller forsinkede pakker kastes lydløst i den ytre TDC- og luftslusen (`Enigma-Fasespeil Airlock`) til en kostnad av $8\,\mu\text{J}$, eller systemet går inn i en reversibel, faststoffbasert ventetilstand (**`CAUSAL_HOLD`** ved $0{,}00\text{ V DC}$ på styresignalet) innenfor det lokale tidsvinduet på $400\text{ sykluser}$. Så snart støyen opphører og det ortogonale lokalvitnet ($W = 1$) igjen er stabilt, gjenopptas driften elektronisk uten at en eneste mekanisk lås har sluppet taket.

Den irreversible, mekaniske fjærreturen (**`GATE :: KILL`**), som krever fysisk menneskelig muskelkraft (**`RESET_BY_L01`**) for å spennes opp igjen, er strengt reservert for tilfeller der en kommando *allerede har passert* den ytre kausale slusen, men hvor den indre fysiske prosesskjernen selv bryter en bevaringslov – slik som tap av kjøling, brudd i kammertrykk, svikt i aktuatorens tilbakekobling ($\Omega \neq \text{Fix}(\Pi \circ \Phi)$) eller ikke-null masseresidual ($\Delta R \neq 0$). En ekstern støykilde kan dermed brenne sine egne kondensatorer tomme mot skjoldet uten å flytte et eneste mekanisk relé på innsiden. Menneskets rygg kalles kun ut i stormen når selve jernet, saltet eller trykkammeret krever en fysisk dom.

En digital signatur i en loggfil beviser kun at en maskin hadde til hensikt å handle. Sann sikkerhet oppstår først når arkitekturen nekter å godta koden som vitne, skiller ytre støy fra indre prosessbrudd, og tvinger enhver påstand om virkeligheten til å hente sitt bevis i termodynamisk arbeid, kjernefysisk stabilitet og ortogonal materiell motstand.
