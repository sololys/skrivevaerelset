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

I en verden der nevrale modeller og autonome agenter opererer i friksjonsfrie, asynkrone løkker, er den største faren **semantisk utglidning** (*semantic banding*): forestillingen om at en fysisk handling kan fullføres fordi en algoritme har generert en sannsynlighet over en statistisk terskelverdi. Vår arkitektur etablerer derfor en absolutt, fysisk sperre der **$0{,}00\text{ V DC}$ er naturens standardtilstand**: ingenting får lov til å påvirke den fysiske verden uten eksplisitt autorisasjon, tilstanden `HOLD` konverteres aldri til `OPEN` utelukkende fordi tid passerer, og dersom en sensor feiler, en nettverkspakke forsinkes eller en bølgefunksjon er i uavklart fase, holdes styrespenningen nede på $0{,}00\text{ V DC}$.

---

## 2. To-Trinns Galvanisk Skranke: Elektronisk `CAUSAL_HOLD` mot Mekanisk `KILL`

For å forhindre at ekstern signalstøy tvinger en menneskelig operatør ut i kulden og dermed snur det termodynamiske utmattelsesforholdet ($\eta_{\text{defense}} = 1{,}25 \times 10^9$) mot forsvaret, opererer sperren i to strengt adskilte trinn. Ved ytre nettverksstøy, forsinkede datapakker eller forsøk på radiofrekvent manipulasjon (DRFM) utenfor den kausale lyskeglen, avvises pulsen direkte i den ytre faststoff-luftslusen til en elektrisk kostnad av kun $8{,}0\,\mu\text{J}$, eller styresignalet legges i reversibel elektronisk ventetilstand (**`CAUSAL_HOLD`** ved $0{,}00\text{ V DC}$) uten å løse ut mekaniske fjærlåser. Dersom en kommando derimot allerede har passert luftslusen og et reelt integritetsbrudd eller en fysisk asymmetri oppstår inne i selve prosesskjernen, utløses **Uzzahs Interlock**: en galvanisk kortslutningssperre kutter drivspenningen til jord på under $15\text{ ns}$ og trekker kontaktbroen mekanisk åpen med stålfjærer (**`GATE :: KILL`**). Denne indre mekaniske låsen kan aldri gjenåpnes av programvaren; kun **Level 01 Supreme Human Authority** kan fysisk tilbakestille bryteren ute ved anlegget (`RESET_BY_L01`).

---

## 3. Den Kausale Diamanten (Alexandrov-skranken)

For nærfelt-interaksjoner ($r \le 20{,}0\text{ m}$) i luft ($n \approx 1{,}00029$) definerer lysets hastighet $c$ en ufravikelig tidsgrense tur-retur:

$$\tau_{\text{ToF}} = \frac{2 \cdot 20\text{ m}}{c / n_{\text{air}}} \approx 133{,}425\text{ ns}$$

Et signal med $\tau_{\text{ToF}} \le 133{,}425\text{ ns}$ befinner seg innenfor det tidlignende Minkowski-regimet ($ds^2 \le 0$), der fysisk tilstedeværelse er kausalt mulig. Et signal med $\tau_{\text{ToF}} > 133{,}425\text{ ns}$ – eksempelvis videresendt fra $500\text{ meters}$ avstand – faller i det romlignende regimet ($ds^2 > 0$). Dette kausalitetsbruddet fanges momentant opp av tids-til-digital-omformeren (TDC), som forkaster pakken til en kostnad av $8{,}0\,\mu\text{J}$ og holder porten lukket på $0{,}00\text{ V DC}$.

---

## 4. Append-Only SHA-256 Kausal Historikk

Enhver tilstandsovergang – enten det er en elektronisk stase i `HOLD`, et mekanisk nødkutt i `KILL` eller en verifisert realisering til $5{,}00\text{ V DC}$ (`OPEN`) – forsegles i en append-only SHA-256-hashkjede (`L1`):

$$\text{Hash}_t = \text{SHA-256}(\text{EventID} \,\|\, \text{Timestamp} \,\|\, \text{Hash}_{t-1} \,\|\, \text{Payload})$$

Historikken kan aldri overskrives, bare forlenges gjennom nye epoker. Sannheten om kuttet forblir intakt for revisjon.

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
