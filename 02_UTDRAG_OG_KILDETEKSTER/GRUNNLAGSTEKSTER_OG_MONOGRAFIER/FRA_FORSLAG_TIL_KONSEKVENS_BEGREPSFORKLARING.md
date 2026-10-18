![Realiseringsgrammatikk og Epistemisk Styring: Fra Forslag til Konsekvens](../../morandi/Formell_arkitektur_for_cyber-fysiske_systemer.png)

# BEGREPSFORKLARING: FRA FORSLAG TIL KONSEKVENS
### *Hvorfor maskiner ikke må utføre handling uten kontroll ($\Phi(x_t) \neq x_{t+1}$)*

---

## 1. Kjerneaksiomet: Generert Kandidat $\neq$ Realisert Konsekvens

Et datagenerert forslag er ikke det samme som en utført, uomstøtelig handling i den fysiske hverdagen.

$$\boxed{\mathbf{\text{Generert dynamikk er aldri det samme som realisert konsekvens } (\text{Kandidat } \Phi \neq \text{Konsekvens } x_{t+1})}}$$

En modell eller algoritme kan generere millioner av kandidater ($\Phi$) i et virtuelt modelleringsrom fordi beregning i minnet er reversibel og nesten kostnadsfri ($Q \approx 0.00\text{ J}$). I det øyeblikket en handling utføres i den fysiske verden, gjelder termodynamikkens lover: sletting av ulovlige tilstander og fysisk aktuering krever energi, skaper varme og kan ikke gjøres ugjort.

* **Generert Kandidat ($\Phi$ i $\Pi_K^{\text{math}}$):**
  * *Eksistensrom:* Virtuelt programvarerom (simuleringer, hypoteser og beregnede felt).
  * *Irreversibilitet:* Tapsfri matematisk glatting ($Q = 0.00\text{ J}$ i modelleringsrommet); kan fritt angres, endres eller slettes i minnet.
  * *Skadepotensial:* $0.00\text{ J}$ direkte fysisk påvirkning på omverdenen.
* **Realisert Konsekvens ($x_{t+1}$ i $\Pi_K^{\text{phys}}$):**
  * *Eksistensrom:* Fysisk virkelighet og romtid (reelle aktuatorer, maskinvare og fysiske omgivelser).
  * *Irreversibilitet:* Irreversibel fysisk tilstandssletting ($Q \ge k_B T \ln 2 \cdot \Delta I_{\text{phys}}$ under Landauer-grensen); umulig å gjøre ugjort når linjen først er krysset.
  * *Skadepotensial:* Reell fysisk kraft, energidissipasjon, varme og uomstøtelig materiell konsekvens.

Som i fysikkens **Casimir-kutt** oppstår ikke struktur og virkelighet ved å legge til mer algoritmisk kompleksitet (*addisjon*), men ved å sette ufravikelige grensebetingelser som kutter vekk og forbyr ulovlige tilstander (*subtraksjon*). Trygghet bygges ikke ved å stole på maskinens fantasi, men ved at porten nekter uverifiserte kandidater adgang.

---

## 2. Mennesket ved Snittflaten (*Kreativ-Core*)

I tradisjonelle datasystemer reduseres mennesket ofte til en passiv bruker eller datakilde. I en feillukket (*fail-closed*) arkitektur er mennesket **subjektet ved snittflaten** — den kroppsliggjorte personen som faktisk må bære og leve med følgene når maskinen utfører et fysisk kutt i hverdagen:

> **«The one who feels the cut must not be erased from the architecture of the cut.»**  
> *(Den som kjenner kuttet på kroppen, må aldri viskes ut av kuttets arkitektur.)*

* **Medisinsk dosering vs. injeksjon:** Å beregne en medisinmengde på en skjerm er en kandidat ($\Phi$). Å føre nålen inn i pasientens arm og trykke inn stempelet er kuttet ($x_{t+1}$).
* **Flybaneberegning vs. fysisk rorutslag:** Å regne ut en rute gjennom en storm er en virtuell hypotese ($\Phi$). Å vri på rorflatene i luften er kuttet som bærer menneskelige konsekvenser ($x_{t+1}$).
* **Sensorrespons vs. kranbevegelse:** Å simulere et løft i programvaren er trygt ($\Phi$). Å sende driftsspenning til motoren som løfter fem tonn stål over et arbeidsområde, er snittflaten mot virkeligheten ($x_{t+1}$).

---

## 3. De Tre Kontrolltilstandene: Hierarkiet $\mathrm{KILL} \succ \mathrm{HOLD} \succ \mathrm{OPEN}$

For å hindre at uverifiserte forslag slipper ut i den fysiske verden, styres utgangsporten $\Omega$ av et strengt subsumpsjonsprinsipp der avslag alltid trumfer avventing, som igjen trumfer åpning:

$$\boxed{\mathrm{KILL} \;\succ\; \mathrm{HOLD} \;\succ\; \mathrm{OPEN}}$$

* **`KILL` ($0.00\text{ V DC}$ — Galvanisk kutt):** Vern mot falsk konsekvens. Ingen uautorisert eskalering tillates. Linjespenningen klemmes til null og aktuatorer deaktiveres momentant.
* **`HOLD` ($0.00\text{ V DC}$ — Trykkbevaring / *Pressure Preservation*):** Overgangssluse i trygg dvale (*stasis*). Bevarer det epistemiske potensialet uten forhastet utladning mens sjekker og bevitnelse utføres.
* **`OPEN` ($5.00\text{ V DC}$ — Strukturell forløsning):** Gis utelukkende når samtlige sikkerhetsskranker og vitnesbyrd er 100 % bekreftet ($\Delta_K \equiv 0$).

1. **Enkeltvetoets makt:** Dersom ni kontrollmoduler melder `OPEN`, men én sikkerhetssensor melder `KILL`, kollapser den samlede tilstanden umiddelbart til `KILL` ($0.00\text{ V DC}$).
2. **Ingen flertallsavgjørelser:** Sikkerhet i kritiske systemer kan aldri stemmes over.
3. **Fail-Closed design:** Dersom strømmen går, en kabel ryker eller en modul slutter å svare, faller systemet automatisk tilbake til `KILL` ($0.00\text{ V DC}$).

│ — [ Blad skåret ut ved bokryggen ] —

---

## 4. Hvorfor Trenger Vi en `HOLD`-Sone? (Holomorf Obstruksjon og Phronesis-Båndbredden)

**Teorem A (Det holomorfe obstruksjonsteoremet):** Identitetsteoremet i kompleks analyse fastslår at dersom en glatt, analytisk funksjon $G(z)$ tar en konstant verdi (f.eks. $1$ for «godkjent») på et åpent område, tvinges funksjonen til å være konstant ($1$) over hele det sammenhengende domenet. En trinnløs binærbryter fra $0$ til $1$ kan derfor ikke være analytisk dersom den skal bevare sin regulerende evne. Systemet må innføre et ikke-analytisk polynomisk overgangslag ($\Delta_\epsilon$, f.eks. $g_4(s) = 3t^2 - 2t^3$) — systemets **`HOLD`-sone**.

```text
   [ KANDIDAT-FELT Φ ]  ───►  ( HOLD-sone / Sluse Δ_ε : 0.00V )  ───►  [ FYSISK HANDLING Ω : 5.00V ]
  (Kontinuerlig tenkning)          (Trykkbevaring & Veto)                 (Diskret commit i romtid)
```

### Risør-varselet og Phronesis-båndbredden $[\gamma_{\min}, \gamma_{\max}]$
For at et system skal kunne utøve dømmekraft i `HOLD`-slusen, må den epistemiske friksjonen $\gamma$ ligge innenfor **Phronesis-båndbredden $[\gamma_{\min}, \gamma_{\max}]$**:

1. **Under-friksjon ($\gamma < \gamma_{\min}$ — *Degenerate Stability Regime*, DSR):** Når friksjonen faller mot null ($\gamma \to 0$), flates beslutningslandskapet ut ($\frac{d\mathcal{E}}{dt} = 0$). Når det ikke koster noe å velge, fremstår alle tilstander som like gyldige, og ingen er nødvendige (*Risør-varselet* $\implies \mathrm{KILL}$).
2. **Over-friksjon ($\gamma > \gamma_{\max}$):** Runaway-dissipasjon og støyindusert krakelering river systemet i stykker av egen motstand ($\implies \mathrm{KILL}$).
3. **Nominal Phronesis ($\gamma \in [\gamma_{\min}, \gamma_{\max}]$):** Den eneste levedyktige korridoren der motstanden er passe stor til å skille lovlig bane fra støy.

---

## 5. Dobbel Bevitnelse: Konseptet $\text{Witness}^2$ ($W^2$)

For handlinger med uomstøtelige fysiske konsekvenser er post-hoc logging etter at skaden har skjedd verdiløst. Hele transaksjonskonteksten må forsegles kryptografisk **før** grensen til den fysiske verden krysses (*pre-commit*):

$$\boxed{\mathbf{W^2 = \langle W_{\text{machine}}, W_{\text{human}} \rangle}}$$

```text
                   +---------------------------------------+
                   |         WITNESS² (W²) BEVIS           |
                   +---------------------------------------+
                   |                                       |
                   |  [ W_machine ]        [ W_human ]     |
                   |  Formell, logisk      Etisk hensikt,  |
                   |  og fysikalsk         autorisasjon    |
                   |  konsistens           og ansvar       |
                   |                                       |
                   +-------------------+-------------------+
                                       |
                                       v
                     Skranker innfridd & Pre-commit låst
                                       |
                                       v
                              [ OPEN 5.00V DC ]
```

1. **$W_{\text{machine}}$ (Det maskinelle vitnet):** Attesterer formell, matematisk, logisk og fysikalsk konsistens, forseglet i en append-only SHA-256-forfedrekjede med RFC 8785 kanonisk JSON (og fysisk WORM-media der maskinvarelås er verifisert).
2. **$W_{\text{human}}$ (Det suverene menneskelige vitnet):** Attesterer etisk forankring, teleologisk hensikt og suveren autorisasjon fra mennesket ved snittflaten.

**Ufravikelig Systemregel:** Maskinen kan aldri autorisere sin egen hensikt:
`standalone_commit_authority = NONE │ physical_authority = NONE │ write_enabled = False`
Mangler $W_{\text{human}}$, forblir porten låst i stasis (`HOLD` / $0.00\text{ V DC}$).

---

## 6. Sjekkliste for Systemintegritet og Dømmekraft

* **Skill alltid kandidat fra konsekvens:** $\Phi(x_t) \neq x_{t+1}$.
* **Beskytt subjektet ved snittflaten:** Den som kjenner kuttet på kroppen, skal aldri viskes ut av kuttets arkitektur.
* **Håndhev subsumpsjonshierarkiet:** $\mathrm{KILL} \succ \mathrm{HOLD} \succ \mathrm{OPEN}$ — ett enkelt veto klemmer spenningen til $0.00\text{ V DC}$.
* **Bevar Phronesis-båndbredden $[\gamma_{\min}, \gamma_{\max}]$:** Hold systemet i `HOLD`-slusen ($\Delta_\epsilon$) med reell motstand så dømmekraften ikke kollapser i friksjonsløs DSR.
* **Krev dobbelt vitnesbyrd før grensen:** $W^2 = \langle W_{\text{machine}}, W_{\text{human}} \rangle$ må være låst *før* $5.00\text{ V DC}$ slippes gjennom porten.
