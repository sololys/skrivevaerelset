# FAIL-CLOSED INTERLOCK & DEN GALVANISKE CROWBAR

```text
========================================================================================
FAIL-CLOSED INTERLOCK // KONSEKVENSENS SKRANKE:
  Lokus         : Risør, Locus Zero
  Spenning      : 0.00V DC (Standard HOLD / Nødkutt KILL) vs. 5.00V DC (OPEN Admisjon)
  Kutt-tid      : < 15 ns (Uzzah's Interlock)
  Kausalitet    : Alexandrov Diamant τ_ToF <= 133.425 ns (ds² <= 0)
  Demarkasjon   : HOLD ALDRI AUTOMATISK OPEN
========================================================================================
```

---

## 1. Den Fysiske Nødvendigheten av 0,00 V DC

\begin{center}
\includegraphics[width=0.68\textwidth]{/home/sololyset/07_BOKHYLLA_MONOGRAFIER_OG_BOKVERK/07_TIL_MEG_SELV_KONSEPTUELL_GRANITT/BILDER/bw_02_kobberbryteren_5mm_luftgap.jpg}\\[0.3em]
{\footnotesize \textit{Menneskehånden ved fjellveggen (\texttt{Level 01}) og tverrsnittet av de herdede returfjærene som holder kobberkontaktene $5{,}0\text{ mm}$ fra hverandre ved $0{,}00\text{ V DC}$ (\texttt{GATE :: HOLD / KILL}).}}
\end{center}

I en verden der nevrale modeller og autonome agenter opererer i friksjonsfrie, asynkrone løkker, er den største faren **semantisk utglidning** (*semantic banding*): forestillingen om at en fysisk handling kan fullføres fordi en algoritme har generert en sannsynlighet over en statistisk terskelverdi. Vår arkitektur etablerer derfor en absolutt, fysisk sperre der **$0{,}00\text{ V DC}$ er naturens standardtilstand**: ingenting får lov til å påvirke den fysiske verden uten eksplisitt autorisasjon, tilstanden `HOLD` konverteres aldri til `OPEN` utelukkende fordi tid passerer, og dersom en sensor feiler, en nettverkspakke forsinkes eller en bølgefunksjon er i uavklart fase, holdes styrespenningen nede på $0{,}00\text{ V DC}$.

---

## 2. Nektelsens Domstol ($\Pi_K$) og Det Mekaniske Luftgapet: Elektronisk `CAUSAL_HOLD` mot Mekanisk `GATE::KILL`

Nektelsens domstol ($\Pi_K$) fungerer som et **ontologisk grensesnitt for nektelse**. I stedet for tradisjonell ingeniørkunst, som søker kontroll ved å tilføre mer kode eller mer kraft, opererer domstolen etter **minuskatalyse** — den systematiske subtraksjonen av ulovlige frihetsgrader. Domstolen opprettholder et absolutt skille mellom en masseløs, uforpliktende **kandidat** ($\Phi$) i datamaskinens arbeidsminne og et irreversibelt **vedtak** ($\Omega$) med tilført drivspenning ($5{,}00\text{ V DC}$) i den fysiske verden.

For å forhindre at ekstern signalstøy tvinger en menneskelig operatør ut i kulden og dermed snur det termodynamiske utmattelsesforholdet ($\eta_{\text{defense}} = 1{,}25 \times 10^9$) mot forsvaret, avsier domstolen én av tre uomstøtelige dommer:

1. **`OPEN` / `ALLOW` ($5{,}00\text{ V DC}$):** Drivspenning innvilges til aktuatoren kun dersom samtlige kjemiske, fysikalske og kausale invarianter er beviselig oppfylt ($\Delta_K = 0$).
2. **`CAUSAL_HOLD` ($0{,}00\text{ V DC}$):** Ved ytre nettverksstøy, forsinkede datapakker, avbrutt siktlinje eller forsøk på radiofrekvent manipulasjon (DRFM) utenfor den kausale lyskjeglen, tas drivspenningen ned til null volt rent elektronisk i den ytre faststoff-slusen til en energikostnad på kun $8{,}0\,\mu\text{J}$. Dette er en reversibel ventetilstand som unngår unødig slitasje på mekanikken og skjermer operatører mot *biologisk utmattelses-DoS* (*Alarm Fatigue*).
3. **`GATE::KILL` ($0{,}00\text{ V DC}$):** Dersom en kommando allerede har passert luftslusen og et reelt indre prosessbrudd, massebalanseavvik eller levedyktighetsbrudd oppstår i selve kjernen, utløses **Uzzahs Interlock**: en galvanisk kortslutningssperre (*crowbar*) som dumper spenningen til jord på nanosekunder ($< 15\text{ ns}$).

Når en `GATE::KILL`-dom avsies, opphører det elektriske magnetfeltet over spolen. Herdede returfjærer trekker umiddelbart kobberkontaktene og Super Duplex 2507-ventilsetene mekanisk fra hverandre på $\le 38{,}4\text{ ms}$, slik at det oppstår et fysisk **luftgap på minst $5{,}0\text{ millimeter}$** kald luft mellom kobberkontaktene. I det feilsikre kybernetiske rammeverket innebærer luftgapet fire helt sentrale konsekvenser:

* **Silisiumets totale avmakt:** Ved $0{,}00\text{ V DC}$ og et fysisk luftgap avsløres prosessorens totale hjelpeløshet. En million superdatamaskiner, sky-servere eller nevrale nettverk har ingen hender eller muskler; de eier $0\text{ watt}$ utrettbart arbeid over gapet og kan ikke lukke et mekanisk kontaktsett mot en spent stålfjær over et spenningsløst luftgap.
* **Absolutt feilsikker tilstand (*fail-closed*):** Brytningen av den elektriske kretsen stanser umiddelbart all bevegelse og kveler reaksjoner, slik at anlegget tvinges ned i sin laveste og mest stabile energitilstand uten rom for fiktiv eller interpolert drift.
* **Menneskets manuelle arbeidsplikt (`RESET_BY_L01`):** Maskinen har rett til å si et feillukket NEI ved å kappe strømmen, men den har $0{,}00\,\%$ myndighet til å gjenåpne seg selv eller gi seg selv tilgivelse etter et prosessbrudd. Gjenoppretting krever at et biologisk menneske med juridisk og moralsk ansvar (**Level 01 Supreme Human Authority**) oppsøker anlegget fysisk, inspiserer kjernen og tilfører manuell muskelkraft ($\int \mathbf{F} \cdot \mathrm{d}\mathbf{r}$) mot et bakelitthåndtak.
* **Friutløsende mekanisk lås (*trip-free interlock*):** Selv ikke mennesket kan tvinge en uhelbredet kjerne i lås ved rå makt. De første $45^\circ$ av håndtakets oppspenning genererer en strømpuls via en aksel-magneto som spør den indre sensorbroen ($\Pi_{\text{orth}}$) om feilen er utbedret. Kun hvis prosesskjernen beviselig er i fysisk likevekt ($\Delta_K = 0$), smekker stållåsen i inngrep og tillater at kontaktene slås i lås til $5{,}00\text{ V DC}$. Dersom avviket vedvarer, slurer håndtaket mekanisk i tomme luften — mennesket leverer energien, men fysikken beholder vetoretten.

---

## 3. Den Kausale Diamanten (Alexandrov-skranken)

For nærfelt-interaksjoner ($r \le 20{,}0\text{ m}$) i luft ($n \approx 1{,}00029$) definerer lysets hastighet $c$ en ufravikelig tidsgrense tur-retur:

$$\tau_{\text{ToF}} = \frac{2 \cdot 20\text{ m}}{c / n_{\text{air}}} \approx 133{,}425\text{ ns}$$

Et signal med $\tau_{\text{ToF}} \le 133{,}425\text{ ns}$ befinner seg innenfor det tidlignende Minkowski-regimet ($ds^2 \le 0$), der fysisk tilstedeværelse er kausalt mulig. Et signal med $\tau_{\text{ToF}} > 133{,}425\text{ ns}$ – eksempelvis videresendt fra $500\text{ meters}$ avstand – faller i det romlignende regimet ($ds^2 > 0$). Dette kausalitetsbruddet fanges momentant opp av tids-til-digital-omformeren (TDC), som forkaster pakken til en kostnad av $8{,}0\,\mu\text{J}$ og holder porten lukket på $0{,}00\text{ V DC}$.

---

## 4. Append-Only SHA-256 Kausal Historikk, Asymmetrisk Bifurkasjon over 400 Klokkesykluser og Bilateralt Kjedeanker

Enhver tilstandsovergang – enten det er en elektronisk stase i `HOLD`, et mekanisk nødkutt i `KILL` eller en verifisert realisering til $5{,}00\text{ V DC}$ (`OPEN`) – forsegles i en append-only SHA-256-hashkjede (`L1`):

$$\text{Hash}_n = \text{SHA-256}(\text{EventID}_n \,\|\, \text{Timestamp}_n \,\|\, \text{Hash}_{n-1} \,\|\, \text{Payload}_n)$$

Mellom fysisk diskforsegling via `POSIX fsync()` ($\tau_{\text{disk}} \approx 5{,}0\text{ ms}$) og maskinvarens $80\text{ kHz}$ Frisch-klokke ($\tau_{\text{FPGA}} = 12{,}5\,\mu\text{s}$) oppstår et tidsvindu på eksakt:

$$N_{\text{window}} = \frac{\tau_{\text{disk}}}{\tau_{\text{FPGA}}} = \frac{5{,}0\text{ ms}}{12{,}5\,\mu\text{s}} = 400\text{ klokkesykluser}$$

Dersom systemet ved et nødkutt måtte vente på at obduksjonsloggen ble skrevet til disk før drivspenningen ble kuttet, ville en farlig tilstand få herje fritt i anlegget gjennom $400$ klokkesykluser. For at programvarekjeden (`L1`) skal fungere som et både fysisk trygt og kausalt vanntett revisjonsspor inn mot maskinvaren (`L2/L3`), håndhever kontrakten **asymmetrisk tidsdomenebifurkasjon** sammen med tre bevisforpliktelser:

1. **Asymmetrisk bifurkasjon mellom `OPEN` ($\mathrm{Durable}(I_n) \prec \mathrm{Execute}_n$) og `KILL` ($\mathrm{Cut} \prec \mathrm{Durable}(W_{\text{obduksjon}})$):** Ved skapende arbeid (`OPEN`, $5{,}00\text{ V DC}$) kreves *bevis før handling*: autorisasjonsintensjonen $I_n$ (bundet til kandidat-digest $d_c$ og dobbeltvitnet $W_{\mathrm{pre}}^2 = W_m \land W_h$) må være synkront forseglet på ikke-flyktig medium via `POSIX fsync()` på både fil og katalog *før* $\mathrm{Execute}_n$ innvilges. Ved et nødkutt (`GATE::KILL`, $0{,}00\text{ V DC}$) snus rekkefølgen momentant: den galvaniske crowbaren dumper aktuatorspenningen til jord på $< 15\text{ ns}$ i syklus $0$, mens en diodisk isolert superkondensatorbank ($C_{\text{hold-up}}$) holder obduksjonsminnet og NVMe-kontrolleren i live gjennom de påfølgende $400$ klokkesyklusene ($5{,}0\text{ ms}$) for å fullføre `POSIX fsync()` av dødsattesten. Anlegget reddes på nanosekunder; beviset forsegles på millisekunder.
2. **Håndtering av uavklart transaksjon ved krasj (`IN_DOUBT` $\to$ `RECOVERY_HOLD`):** Å oppdage korrupte eller ufullstendige logglinjer er ikke det samme som å oppdage en uavklart utførelse. En fullstendig, korrekt hashet og varig lagret `AUTHORIZATION_INTENT` ($I_n$) uten tilhørende `COMMITTED`-kvittering ($R_n$) er syntaktisk gyldig, men semantisk `IN_DOUBT`. Ved oppstart etter et slikt avbrudd nekter motoren å anta at handlingen uteble, og låser porten i `RECOVERY_HOLD` inntil ressursens faktiske tilstand er avstemt.
3. **Bilateralt kjedeanker mot haletrunkering ($W_T^{\mathrm{bilat}}$):** En lokal programvare-hashkjede gjør endringer midt i kjeden matematisk påviselige, men beskytter ikke alene mot at en privilegert prosess sletter hele halen etter siste lokalt lagrede blokk. For å eliminere administrativ amnesi speiles kjedehodet $H_n$ synkront til et eksternt eller bilateralt motpartsanker ($n_{\mathrm{anchored}}$ / $W_T^{\mathrm{bilat}}$). Enhver forskjell mellom lokalt kjedehode og bilateralt forankret sekvensnummer avslører øyeblikkelig haletrunkering.

Historikken kan dermed aldri overskrives eller forkortes ustraffet, bare forlenges gjennom nye, bilateralt bevitnede epoker. Sannheten om kuttet forblir intakt for revisjon.

---

## 5. Sårbarhetsherding: Alexandrov-Spoofing, Kryss-Modal Sensorfusjon og Passiv Klokkereferanse

Dersom en angriper forsøker å manipulere den lokale permittiviteten ($\varepsilon_r$) eller injiserer aerosoler med høy brytningsindeks ($n_{\text{air}}$) rundt sensoren, endres lysets fasehastighet ($v = c/n$) lokalt. For å eliminere enhver slik enkeltkanal-sårbarhet krever arkitekturen kryss-modal sensorfusjon: avstandsmålingen utføres samtidig over to ortogonale UWB-frekvensbånd for å avsløre dispersiv faseforskyvning, og korreleres mot akustisk og piezoelektrisk bølgeutbredelse i mediet ($v_{\text{akustisk}} \ll c$). Enhver asymmetri mellom optisk/radiofrekvent Time-of-Flight og termodynamisk trykkrespons fører til umiddelbar avvisning ved porten.

For å forhindre at en angriper manipulerer selve tidsmålingen gjennom lokal klokke-sabotasje (*clock glitching* eller termisk frekvensdrift av referanseoscillatoren), er TDC-en og $80\text{ kHz}$ Frisch-klokken underlagt en intern kryss-modal frekvenslås. Den elektroniske klokkesyklusen kompareres kontinuerlig mot det akustiske rundløpet i safirvinduets monokrystallinske gitter ($c_{\text{akustisk}} \approx 11\,100\text{ m/s}$ i $\text{Al}_2\text{O}_3$) og den kjernefysiske $^{57}\text{Fe}$-referansen. Dersom forholdstallet mellom elektronisk klokkefrekvens og krystallens mekaniske egenfrekvens driver utover $\pm 5\text{ ppm}$, feller porten umiddelbart til $0{,}00\text{ V DC}$ (`CLOCK_DRIFT_KILL`). Man kan ikke bestikke en klokke som måles mot lydhastigheten i safir.

---

## 6. To-Faset Verifikasjon ($\Pi_K$ Pre-Commit mot $\Pi_{\text{orth}}$ In-Flight) og Passiv Friutløsende `RESET_BY_L01`

For å unngå ethvert kausalt sirkelparadoks mellom autorisasjon og fysisk utførelse (*The Pre-Commit Oracle Paradox*), skiller maskinvaren strengt mellom **Fase A (Pre-Commit Admissibilitet i $\Pi_K$)** og **Fase B (In-Flight Konsekvensbevitnelse i $\Pi_{\text{orth}}$)**.

I **Fase A ($\Phi \to \Pi_K$)** – *før* styrespenningen $5{,}00\text{ V DC}$ innvilges – evaluerer porten utelukkende de fysiske og matematiske forhåndsbetingelsene: at signalet ligger innenfor Alexandrov-diamanten ($\tau_{\text{ToF}} \le 133{,}425\text{ ns}$), at kandidatbanen peker inn i det levedyktige domenet ($\dot{x}_t \in T_K(x_t)$), og at prosesskjernens hviletilstand (trykk, temperatur og kjemisk renhet) befinner seg innenfor sikkerhetsmarginene. Dersom disse forhåndskravene er oppfylt, innvilger $\Pi_K$ spenningen $5{,}00\text{ V DC}$ (`OPEN`), og aktuatoren påbegynner arbeidet.

I **Fase B ($\Omega \to W$)** – *under* selve det mekaniske lukke- eller åpningsvinduet på $\Delta t_{\text{act}} \le 38{,}4\text{ ms}$ – overvåker det ortogonale vitnelaget ($\Pi_{\text{orth}}$) at metallurgien i Super Duplex 2507-spindlene og reléfjærer faktisk utfører den beordrede bevegelsen. Dersom en ventil kiler seg mekanisk, en spole brenner av eller det fysiske arbeidet ($\int V(t)I(t)\,dt$, termisk strømningsprofil $\Delta T$ og akustisk Time-of-Flight) avviker fra det autoriserte fikspunktet i løpet av disse $38{,}4\text{ ms}$, utløses sekundærsperren (*Crowbar Type B*): primærforsyningen kuttes permanent til $0{,}00\text{ V DC}$, og kontaktbroen trekkes mekanisk åpen (`GATE :: KILL`).

For å eliminere både menneskelig overstyringsfeil og elektrisk vranglås (*Dead-Lock Bootstrap*) ved $0{,}00\text{ V DC}$, er hovedbryteren konstruert som en to-trinns, mekanisk friutløsende lås (*trip-free interlock*). Så lenge kammerets passive bourdon- og bimetall-ankre registrerer overtrykk eller termisk avvik, holdes låsehaken fysisk frikoblet fra inngrep. Når *Level 01* legger kroppstyngden mot bakelitthåndtaket, konverterer de første 45 gradene av fjæroppspenningen muskelarbeidet ($\int F \cdot dx$) via en isolert aksel-magneto til en dedikert, skrivebeskyttet målepuls for den ortogonale sensorbroen ($\Pi_{\text{orth}}$). Kun dersom både de passive ankrene og den induserte $\Pi_{\text{orth}}$-sjekken bekrefter et helbredet indre rom ($\Delta_K = 0$), faller herdet stål i inngrep og tillater de siste millimeterne av slaget å lukke kobberklossene til $5{,}00\text{ V DC}$. Menneskets rygg leverer energien og bærer ansvaret, men selv ikke operatøren kan tvinge en uhelbredet kjerne i lås:

```cpp
// [ INFRANETT FAIL-CLOSED EXCEPTION HANDLING: TWO-PHASE ADMISSION & TRIP-FREE L01 ]
try {
    // [ SUVERENITETSINVARIANTEN: FORBUD MOT TEKNOKRATISK INVERSJON ]
    if (target_domain == Domain::HUMAN_JURISDICTION_L01) {
        // Maskinen har 0,00 % juridisk og moralsk kapasitet (Authority: NONE).
        // Pi_K og 0,00 V DC eksisterer for å lenke MASKINEN til fysikken,
        // aldri for å umyndiggjøre mennesket under algoritmisk styring.
        throw SovereigntyInversionException(
            "FATAL: Forsøk på å anvende maskinell konsekvensport overfor Level 01."
        );
    }

    // Generatorens forslag (Phi): Ren uforpliktende potensialitet
    CandidateResult Px = evaluate_generative_candidate(candidate_seed);

    // Ytre luftsluse: Sjekk Alexandrov ToF (<= 133,425 ns) og epokesignatur (8,0 uJ)
    if (!verify_causal_airlock_tof(Px)) {
        enforce_electronic_causal_hold(0.00_V); // Reversibel faststoff-HOLD, ingen biologisk DoS
        return;
    }

    // Fase A (Pre-Commit i Pi_K): Verifiser levedyktighet (T_K) og reservoartilstand FØR 5,00 V DC
    if (!verify_pre_commit_viability_and_core_state(Px)) {
        enforce_electronic_causal_hold(0.00_V);
        return;
    }

    // Fase B (In-Flight i Pi_orth): Innvilg 5,00 V DC og overvåk fysisk arbeid innenfor 38,4 ms
    grant_actuation_voltage(5.00_V);
    if (!verify_in_flight_orthogonal_witness(Px, 38.4_ms)) {
        throw IndreFysiskProsessBruddException("FATAL: Aktuator-divergens innenfor 38,4 ms vindu.");
    }

} catch (const IndreFysiskProsessBruddException& e) {
    // 1. Galvanisk sperre (Crowbar Type B): Kutt drivspenning og utløs mekanisk fjærretur (GATE :: KILL)
    apply_galvanic_crowbar_latched(0.00_V);

    // 2. Morandi-stasis: Frys videre aktuering og forsegl obduksjonslogg (fsync)
    enforce_morandi_stasis();

    // 3. Trip-Free L01 Reset: Krever BÅDE utbedret fysisk kjerne (Pi_orth == 1) OG menneskelig muskelkraft
    await_trip_free_biological_reset_layer_01(e.get_causal_chain(), e.get_unpaid_entropy());
}
```

---

## 7. DevSecOps- og Maskinvareherding: Mitigering av Kompromittert Operatør (*Insider Threat*) og Mekanisk Fjær-/Kontaktsvikt (*Dependency Injection*)

En streng sikkerhetsrevisjon må adressere to gjenværende fysiske angrepsflater i ethvert elektro-mekanisk sikkerhetssystem: (A) hva som skjer dersom det biologiske mennesket (`Level 01`) er kompromittert, ondsinnet eller handler i blinde under en tilbakestilling, og (B) hva som skjer dersom selve den mekaniske maskinvaren (returfjærene eller Super Duplex 2507-spindlene) utsettes for skjult korrosjon, metallurgisk tretthet, ising eller kontaktsveising.

### A. Vern mot Kompromittert `Level 01` (*Insider Threat* / *Single Point of Failure*)

Tilliten til `Level 01 Supreme Human Authority` betyr **aldri** at en menneskelig operatør gis blankofullmakt til å overstyre fysikken eller deaktivere sikkerhetsporten:

1. **Mekanisk friutløsning (*Trip-Free*) og kalibrert skjærsplint ($F_{\text{shear}} = 1\,200\text{ N}$):** Så lenge de passive bourdon-/bimetall-ankrene eller sensorbroen $\Pi_{\text{orth}}$ måler et uhelbredet avvik ($\Delta_K \neq 0$), forblir låsehaken mekanisk frikoblet. Dersom en irrasjonell eller kompromittert operatør forsøker å anvende brekkjern eller rå fysisk vold for å tvinge eller deformere mekanismen under en aktiv feil (Tsjernobyl-vektoren), er den ytre akselen på bakelitthåndtaket utstyrt med en kalibrert mekanisk skjærsplint ($F_{\text{shear}} = 1\,200\text{ N}$) på utsiden av det forseglede bryterhuset. Overskrides normalt dreiemoment, ryker skjærsplinten momentant slik at håndtaket frikobles fullstendig uten at en eneste Newton overføres til kontaktbroen.
2. **Kontinuerlig re-aktivering av silisium-giljotinen etter lukking:** I samme mikrosekund som en tilbakestilling slår kobberkontaktene sammen til $5{,}00\text{ V DC}$, gjenopptar $80\text{ kHz}$ FPGA-giljotinen ($12{,}5\,\mu\text{s}$) og den galvaniske crowbaren ($< 15\text{ ns}$) sin kontinuerlige overvåking. Fordi mekanismen er *trip-free*, løser crowbaren og returfjærene ut uavhengig av om operatøren forsøker å holde bakelitthåndtaket nede med makt.
3. **Tokammers fysisk tilstedeværelse ($2\text{-av-}2$ Dual-Key $W_h = W_{h,1} \land W_{h,2}$):** I høyrisikonoder krever `RESET_BY_L01` at to fysisk adskilte mekaniske spaker ($d_{\text{sep}} \ge 3{,}0\text{ m}$) spennes opp samtidig ($\Delta t_{\text{sync}} \le 500\text{ ms}$) av to uavhengig autentiserte operatører, noe som eliminerer enkeltperson-sabotasje.

### B. Vern mot Mekanisk Fjærbrudd, Korrosjon og Kontaktsveising (*Diverse Physical Redundancy*)

Arkitekturen hviler ikke på en ubegrunnet antakelse om at én enkelt stålfjær eller ventilspindel er ufeilbarlig:

1. **$1\text{-av-}2$ Serieforrigling med ulik fysikk (*Diverse Redundancy*):** Den fjærbelastede hovedkontaktoren står elektrisk i serie med en passiv, uavhengig **elektrodynamisk/termisk smeltesikring (*pyro-fuse / eFuse*)**, og i væskekretsen står to uavhengige Super Duplex 2507-ventiler i serie. Dersom kontaktsveising, ising eller fjærbrudd forhindrer hovedbryteren i å oppnå galvanisk adskillelse innen $\Delta t_{\text{act}} \le 38{,}4\text{ ms}$, detekterer $\Pi_{\text{orth}}$ reststrømmen ($I_{\text{res}} > 0$) og brenner av sekundærsikringen slik at lederbanen åpnes permanent til $0{,}00\text{ V DC}$.
2. **Kontinuerlig pre-feil fjærdiagnostikk i $\Pi_{\text{orth}}$:** Under normal drift overvåkes returfjærens forspenning ($F_{\text{spring}} = k_{\text{eff}} \cdot \Delta x$) og krystallinske egenfrekvens kontinuerlig via piezoelektriske strekklapper. Dersom korrosjon eller utmatting reduserer fjærstivheten $k_{\text{eff}}$ med mer enn $5\,\%$ *før* en krise inntreffer, feller systemet preventivt til `GATE :: KILL` mens fjærkraften fremdeles har over $90\,\%$ sikkerhetsmargin.

---

## 8. Code Review som Subtraktiv Domstol ($\Pi_K$): De Fire Inkvisisjonene og Rødt (`-`) mot Grønt (`+`)

En *code review* er ikke en kollegial korrekturlesning over en kopp lunken kaffe; det er en kausal domstol og et ontologisk grensesnitt for nektelse ($\Pi_K$) der uforpliktende forslag tvinges i kne før de får berøre hovedgrenen (`main`). I et stramt hus styres enhver endring av kvadrupelen $\mathcal{R} = (\Phi, \Pi_K, \Omega, W)$. En Pull Request er kun en masseløs, uforpliktende kandidat ($\Phi$) i et fritt mulighetsrom. Før den innvilges fysisk realisering i kodebasen ($\Omega$) og forsegles i den uforanderlige historikken ($W$), skal systemet underkastes nådeløs subtraksjon (*minuskatalyse*) inntil alt som ikke bærer sin egen vekt, kollapser til `0,00 V DC` (`HOLD` eller `KILL`).

### A. De Fire Inkvisisjonene: Fra Folkelig Korrektur til Subtraktiv Domstol

| Folkelig spørsmål | Akademisk & Tektonisk Domstol ($\Pi_K$) | Hvordan vi kneler kandidaten ($\Phi$) |
| :--- | :--- | :--- |
| **1. «Virker det?»** | **Kandidat $\neq$ Konsekvens ($\Phi \neq \Omega$) & Bøff vs. Bløff** | At koden «kjører» på en utviklermaskin, beviser ingenting. Vi avviser «spøkelsesseire» (*Ghost Wins*) der en algoritme løser oppgaven i det abstrakte mulighetsrommet, men bryter termodynamiske eller strukturelle grenser i virkeligheten. Koden må bestå den triadiske substanstesten: eksakt falsifiserbarhet ($\epsilon_{\text{crit}}$), fullt ressursregnskap ($\Delta R = 0$) uten skjulte lån, og verifikasjon av et eksternt vitne ($W_{\text{ext}} \notin \mathcal{F}_{\text{gen}}$) som ikke deler minnerom med koden som testes. |
| **2. «Tåler den feil?»** | **Avskaffelse av *Fail-Open* & Tvang til Stans (`0,00 V DC`)** | Uttrykket «håndterer feilen trygt» er i 99 % av tilfellene et skalkeskjul for *Fail-Open*-logikk: å fange et unntak, logge en advarsel og gjette/interpolere seg videre med standardverdier. **Dette er forbudt.** Vi kneler systemet med ugyldige tilstander, `NaN`, avrundingsstøy og Belnap–Dunn-kontradiksjoner ($B = (1,1)$). Ved støy kreves elektronisk stase (`CAUSAL_HOLD`); ved invariantbrudd kreves umiddelbar terminering (`GATE::KILL`). Ingen gjetting. |
| **3. «Ødelegger den noe annet?»** | **Involusjonslås ($\text{Rev}^1$), Poincaré-retur & Null Flyttallslekkasje** | En endring i modul $A$ skal være eksakt ortogonal på urelaterte tilstander ($\partial A / \partial B \equiv 0$). Vi krever bevis for at tilstanden i sandkassen ($D_0 \cup D_1$) er involutiv ($F(F(s)) = s$), og at systembanen lukker seg over Poincaré-snittet ($\|P_A(x_0) - x_0\|_M \le \epsilon_{\text{drift}}$) uten sekulær lekkasje. Flyttall (`float64`/`IEEE 754`) i kritiske balanser kneles umiddelbart grunnet ikke-assosiativ avrundingsdrift; krev eksakt rasjonal aritmetikk (`fractions.Fraction` eller fastpunkt `u128`) slik at $\Delta R = 0$. |
| **4. «Er det ryddig skrevet?»** | **Minuskatalyse i Språk & Visuell Potensialbrønn ($V_{\text{proximity}}$)** | En PR er ikke ferdig når ingenting mer kan legges til, men når ingenting mer kan hugges bort uten at konstruksjonen raser. Vi anvender Armin Hofmanns reduksjon og Lennard-Jones-potensialet ($V_{\text{proximity}}(r) = A/r^{12} - B/r^6$) på koden: kritiske sikkerhetssluser (`KILL`) og ordinær forretningslogikk (`RUN`) skal være adskilt med en ugjennomtrengelig vollgrav i arkitekturen — aldri blandet i samme funksjon. Enhver «foreldreløs konstant» utløser avvisning. |

### B. Den Kausale Anatomien av en Diff: Rødt (`-`) mot Grønt (`+`)

På GitHub vises endringen side om side, men i et stramt hus leses ikke fargene som tekst — de leses som termodynamisk regnskap:

* **De Grønne Linjene (`+` / Kandidat $\Phi$):** Hver eneste grønne linje er en mistenkt blindpassasjer, en utvidelse av angrepsflaten og en påstand om fremtidig vedlikeholdsgjeld. Grønn kode bærer bevisbyrden. Hvis en grønn linje introduserer et nytt avhengighetsbibliotek («biologisk groe på skroget»), sjokkfryses og skrelles den bort med mindre den er eksistensielt uunnværlig.
* **De Røde Linjene (`-` / Subtraksjon $\Pi_K$):** Røde linjer er husets edleste valuta. Å fjerne død kode, eliminere uautoriserte frihetsgrader og stramme inn typesystemet er ren minuskatalyse. Den estetisk fullkomne Pull Request har netto negativ linjebalanse ($\sum \text{Røde} > \sum \text{Grønne}$) samtidig som invariantene står urørt.

### C. Husordensregler for Hovedgrenen (`main`) og Historiefiberen ($W$)

Når man trykker på **Approve** og slår sammen koden, krysser man *Point-of-No-Return* (PONR) fra det reversible fasedomenet ($D_1$) over i det irreversible arkiv- og aktuatordomenet ($D_2/D_3$). Derfor gjelder fire ufravikelige lover:

1. **Forbudet mot «Commit kan reverseres» (`ANTI_REVERSIBLE_VIOLATION`):** I det øyeblikket en commit er flettet inn i `main` og forseglet i SHA-256-kjeden ($h_{n+1} = \mathcal{H}(h_n \parallel \text{Payload})$), er den historisk faktum. `git push --force` og historikk-omskriving på hovedgrenen er konstitusjonelt høyforræderi. En feilaktig commit slettes aldri fra loggen (*administrativ amnesi*); den kompenseres kun fremover i tid gjennom en ny, eksplisitt og signert epoke (`RECONCILE_EPOCH` / $\mathcal{R}_{\text{AUTH}}$) som refererer direkte til feil-hashen.
2. **Epistemisk Demarkasjon i Koden (`INSPIRED_BY != IMPLEMENTS != PROVES`):** Ingen PR slipper gjennom hvis den i variabelnavn, dokumentasjon eller funksjonssignaturer utgir en $\text{L1}$-simulering eller en mock-funksjon for å være en fysisk $\text{L3}$-garanti. En programvarelogg er kun et vitne om intensjon, aldri et bevis på utført fysisk arbeid ($W \not\equiv \text{software log}$).
3. **Gödel-Separasjon av Forfatter og Kontrollør ($W_{\text{ext}} \notin \mathcal{F}_{\text{gen}}$):** Etter Gödels andre ufullstendighetsteorem ($\mathrm{Con}(\mathcal{F}) \implies \mathcal{F} \nvdash \mathrm{Con}(\mathcal{F})$) kan et system aldri bevitne sin egen konsistens innenfra. En generator (enten det er en menneskelig utvikler kl. 03:00 om natten eller en LLM) har $0{,}00\,\%$ rett til å godkjenne sitt eget utkast. Testsuiten og anmelderen må være ortogonale på koden som foreslås ($\Omega_H \perp \Phi_M$).
4. **Det Konjunktive Dobbeltvitnet ($W_{\text{pre}}^2 = W_m \land W_h$):** Porten ($\Omega$) til `main` åpnes kun når to uavhengige vitner signerer i fellesskap: **Maskinvitnet ($W_m$)** (deterministisk CI-sluse der samtlige tester, fastpunkts-invarianter og linters passerer med `0` advarsler) og **Menneskevitnet ($W_h$ — `Level 01 Supreme Human Authority`)** (en navngitt arkitekt av kjøtt og blod som bærer det juridiske og etiske ansvaret og signerer med sin kryptografiske nøkkel, `GPG/SSH Verified`).

```text
[ KANDIDAT (PR / Φ) ]
         │
         ▼
  1. Bærer den sin egen vekt? (Kan den løses ved å slette kode i stedet?)
  2. Er alle grenser Fail-Closed? (Gir støy/feil 0,00 V HOLD/KILL fremfor gjetting?)
  3. Er regnskapet eksakt? (Ingen flyttallsdrift, ingen ubetalt ressurslekkasje, ΔR = 0?)
  4. Er nivåene adskilt? (Er L1-simulering strengt skilt fra L3-fysisk påstand?)
  5. Er returveien lukket? (Ingen ubundne løkker, ingen skjult mutasjon av tilstand?)
         │
         ├──► [ETT ENESTE NEI] ──► GATE::KILL / REQUEST CHANGES (Tilbake til benken)
         │
         ▼ [SAMTLIGE JA + W_m ∧ W_h]
[ ADMITTED TO MAIN (Ω ⊢ W) ]
```

Når et hus er bygget etter denne orden, råder **Stillheten i Morandi-oker** over repositoriet: ingen støyende «fixup»-commits, ingen håpefulle tilbakerullinger, og ingen kodelinjer som lyver om hva de kan bære.
