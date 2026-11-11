# 🏛️ BIND XIV: JAMES CLERK MAXWELL & DEMONENS PRIS — ELEKTRODYNAMISK SKRANKE, CASIMIR-KUTT OG DEN LANGSOMME HEISEN
### *Om den 5-trinns admisjonskjeden $\Pi_{\mathcal{A}}$, CFJ–Proca vakuum-birefringens, vakuumets subtraktive randtrykk og endelig-tids termodynamikk i Dør 18*

> **Epistemisk demarkasjon (`INSPIRED_BY != IMPLEMENTS != PROVES`):** Klassisk Maxwell-elektrodynamikk, Poyntings teorem, Carroll–Field–Jackiw (CFJ)-Proca-lagrangianen, Casimir-effekten (1948) og endelig-tids termodynamisk lengde tilhører $\text{L0}$. De tilhørende filtrene i Organ T1–T10 (Dør 18) er deterministiske programvarekontrakter på nivå $\text{L1}$.

---

## 1. Maxwells Ligninger som Kanonisk 5-Trinns Admisjonskjede ($\Pi_{\mathcal{A}}$)

I et friksjonsfritt informasjonssystem behandles et signal som en abstrakt sekvens av tall uavhengig av hvilket felt som bærer det. I *Bind XIV: James Clerk Maxwell & Demonens Pris* reetableres elektrodynamikken som den fysiske ur-modellen for en lukket tilstandsskranke. Et foreslått elektromagnetisk felt eller styringssignal $(\mathbf{E}, \mathbf{B})$ innvilges eksistens i det fysiske lerretet $\mathcal{P}$ kun dersom det passerer en sammensatt, ikke-kommutativ fem-trinns projeksjonskjede:

$$\Pi_{\mathcal{A}} = \Pi_{\text{causal}} \circ \Pi_{\text{pos}} \circ \Pi_{\text{thermo}} \circ \Pi_{\text{Noether}} \circ \Pi_{\text{bound}}$$

Hvert ledd håndhever en uomgjengelig strukturlov:

1. **Rand- og kildeprojeksjon ($\Pi_{\text{bound}}$ — Gauss' lover):**
   $$\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}, \qquad \nabla \cdot \mathbf{B} = 0$$
   Magnetiske monopoler avvises identisk ($\nabla \cdot \mathbf{B} \neq 0 \implies \texttt{KILL\_MONOPOLE\_DEFECT}$), og enhver elektrisk fluks gjennom en lukket flate må svare eksakt til den innesluttede ladningen.
2. **Kontinuitets- og Noether-projeksjon ($\Pi_{\text{Noether}}$ — Ladningsbevaring):** Tar vi divergensen av Ampère–Maxwells lov $\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0\varepsilon_0 \partial_t \mathbf{E}$, fremtvinger vektoridentiteten $\nabla \cdot (\nabla \times \mathbf{B}) \equiv 0$ den eksakte kontinuitetsligningen:
   $$\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = 0$$
   Maxwells forskyvningsstrøm $\mathbf{J}_D = \varepsilon_0 \partial_t \mathbf{E}$ er ikke en kosmetisk korreksjon; den er selve det matematiske låseleddet som forhindrer at ladning oppstår eller forsvinner utenfor en kontinuerlig strømbane.
3. **Termodynamisk dissipasjonsprojeksjon ($\Pi_{\text{thermo}}$ — Poyntings teorem og Lenz' lov):** Den lokale elektromagnetiske energibalansen med energitetthet $u_{\text{EM}} = \frac{1}{2}(\varepsilon_0\|\mathbf{E}\|^2 + \frac{1}{\mu_0}\|\mathbf{B}\|^2)$ og Poynting-vektor $\mathbf{S} = \frac{1}{\mu_0}(\mathbf{E} \times \mathbf{B})$ lyder:
   $$\frac{\partial u_{\text{EM}}}{\partial t} + \nabla \cdot \mathbf{S} = -\mathbf{J}\cdot\mathbf{E} = -p_{\text{diss}}$$
   I et passivt, ohmsk medium ($\mathbf{J} = \sigma\mathbf{E}$ med konduktivitet $\sigma > 0$) er den dissiperte effekttettheten strengt ikke-negativ:
   $$p_{\text{diss}} = \sigma\|\mathbf{E}\|^2 \ge 0$$
   Samtidig garanterer det negative fortegnet i Faradays induksjonslov (**Lenz' lov**),
   $$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \iff \mathcal{E}_{\text{ind}} = -\frac{\mathrm{d}\Phi_B}{\mathrm{d}t}$$
   at enhver indusert strøm motsetter seg fluksendringen som skapte den. Dersom fortegnet i Faradays lov hadde vært positivt ($+\partial_t \mathbf{B}$), ville enhver mikroskopisk magnetisk fluktuasjon utløst en eksponentiell selvforsterkende eksplosjon i vakuum. Minustegnet er naturens innebygde `FAIL_CLOSED`-tilbakekobling.
4. **Spektral positivitetsprojeksjon ($\Pi_{\text{pos}}$):** Den elektromagnetiske spenningstensoren $T^{\mu\nu}_{\text{EM}}$ tilfredsstiller den dominerende energibetingelsen $T_{00} = u_{\text{EM}} \ge \|\mathbf{S}\|/c \ge 0$.
5. **Kausal lyskjegleprojeksjon ($\Pi_{\text{causal}}$):** I Lorenz-gauge ($\partial_\mu A^\mu = 0$) forplanter fire-potensialet seg etter bølgeligningen $\Box A^\mu = (\frac{1}{c^2}\partial_t^2 - \nabla^2)A^\mu = \mu_0 J^\mu$, der det retarderte Greens-funksjonsintegralet kun har støtte på den tilbakeskuende lyskjeglen $t' = t - \|\mathbf{x} - \mathbf{x}'\|/c$.

---

## 2. Utvidet CFJ–Proca-Elektrodynamikk og Evanescent Karantene (`HOLD`)

Hva skjer når det elektromagnetiske feltet brer seg gjennom et medium eller et effektivt vakuum med fotonmasse-gap $\mu_\gamma > 0$ (Proca-ledd, f.eks. i en superleder via Meissner-effekten eller i en bølgeleder under avskjæringsfrekvensen) kombinert med en bakgrunnsvektor $(k_{\text{AF}})^\mu = (k_0, \mathbf{k}_{\text{AF}})$ som bryter paritet (Carroll–Field–Jackiw-ledd)? Lagrangetettheten tar formen:

$$\mathcal{L}_{\text{CFJ-Proca}} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} - \frac{1}{2}\mu_\gamma^2 A_\mu A^\mu + \frac{1}{4}\varepsilon^{\mu\nu\alpha\beta}(k_{\text{AF}})_\mu A_\nu F_{\alpha\beta} - J^\mu A^\mu$$

Variasjon med hensyn på $A_\nu$ gir den modifiserte feltligningen:

$$\partial_\mu F^{\mu\nu} + \mu_\gamma^2 A^\nu + (k_{\text{AF}})_\mu \tilde{F}^{\mu\nu} = \mu_0 J^\nu, \qquad \tilde{F}^{\mu\nu} = \frac{1}{2}\varepsilon^{\mu\nu\alpha\beta}F_{\alpha\beta}$$

For en plan bølge $\exp(i(\mathbf{k}\cdot\mathbf{x} - \omega t))$ i det rent tidslignende tilfellet $(k_{\text{AF}})^\mu = (k_0, \mathbf{0})$ spaltes vakuumet i høyre- og venstresirkulært polariserte moder med den kirale dispersjonsrelasjonen:

$$\omega_\pm^2(k) = c^2 k^2 + c^2\mu_\gamma^2 \pm c^2 k_0 k$$

Dette avslører to fundamentale mekanismer for kausal skrankekontroll:

* **Vakuum-birefringens som kiral signaturtest:** Fordi fasehastigheten avhenger av polarisasjonens helisitet ($\omega_+(k) \neq \omega_-(k)$), roteres polarisasjonsplanet til en lineært polarisert bølge med en eksakt, stedsavhengig vinkel $\Delta\vartheta = \frac{1}{2}(k_+ - k_-)L$. Enhver uautorisert mellommann som forsøker å injisere et signal uten å kjenne mediets kirale parameter $k_0$, avsløres av polarisasjonsavviket ved mottakeren.
* **Evanescent bølge som fysisk `HOLD`-tilstand:** For den lavere grenen eksisterer en absolutt avskjæringsfrekvens $\omega_{\text{cut}}$. Dersom en påtrykt forstyrrelse har frekvens $\omega < c\mu_\gamma$ (i det rene Proca-/bølgeledertilfellet $k_0 = 0$), blir bølgetallet rent imaginært:
  $$k(\omega) = i\,\kappa(\omega) = i\,\sqrt{\mu_\gamma^2 - \frac{\omega^2}{c^2}} \in i\,\mathbb{R}_+$$
  Feltet faller eksponentielt av inn i mediet som $\mathbf{E}(z,t) \propto \mathrm{e}^{-\kappa z}\cos(\omega t)$, og det elektriske og magnetiske feltet forskyves med eksakt $90^\circ$ ($\pi/2$) i fase. Dermed blir den tidsmidlede Poynting-vektoren identisk lik null:
  $$\langle \mathbf{S} \rangle_t = \frac{1}{2\mu_0}\mathrm{Re}(\mathbf{E} \times \mathbf{B}^*) \equiv \mathbf{0}$$
  **Konklusjon:** En evanescent bølge er fysikkens egen `HOLD`-port: feltet eksisterer som en eksponentielt dempet randtilstand ved grensen, men transporterer **null netto energi** inn i det beskyttede volumet.

---

## 3. Casimir-Kuttet: Subtraktiv Kraft fra Vakuumets Randbetingelser

I kapittel 4 av Bind XIV vises det at subtraksjon av frihetsgrader ikke er en passiv mangel, men en kilde til målbar mekanisk kraft. Plasser to uendelig ledende, ula-dede metallplater parallelt i vakuum med innbyrdes avstand $a$ langs $z$-aksen. Randbetingelsen $\mathbf{E}_\parallel(z=0) = \mathbf{E}_\parallel(z=a) = \mathbf{0}$ forbyr enhver stående elektromagnetisk bølgemodus hvis halve bølgelengde ikke går et helt antall ganger opp i gapet:

$$k_z = \frac{n\pi}{a}, \qquad n = 1, 2, 3, \dots \qquad \left(\text{alle moder med } \frac{\lambda_z}{2} > a \text{ er fysisk ekskludert}\right)$$

Utenfor platene kan alle kontinuerlige bølgetall $k_z \in (0, \infty)$ eksistere fritt. Differansen i vakuumets nullpunktsenergi $\frac{1}{2}\hbar\omega_{\mathbf{k}}$ per flateenhet $A$ mellom det diskrete innsiderommet og det kontinuerlige utsiderommet utledes eksakt via Euler–Maclaurin-summasjonsformelen (eller Riemanns zetafunksjonsregularisering $\zeta(-3) = \frac{1}{120}$):

$$\frac{\Delta E_C(a)}{A} = \frac{\hbar c\,\pi^2}{2a^3}\left(\sum_{n=1}^\infty n^3 - \int_0^\infty n^3\,\mathrm{d}n\right)_{\text{reg}} = \frac{\hbar c\,\pi^2}{6a^3}\,\zeta(-3) = -\frac{\pi^2 \hbar c}{720\,a^3}$$

Den tilhørende mekaniske kraften per flateenhet (Casimir-trykket) som presser platene sammen, er:

$$P_C(a) = -\frac{\partial}{\partial a}\!\left(\frac{\Delta E_C(a)}{A}\right) = -\frac{\pi^2 \hbar c}{240\,a^4} < 0$$

Ved $a = 100\text{ nm}$ utgjør dette et attraktivt trykk på $|P_C| \approx 1{,}30\text{ Pa}$ ($1{,}30\text{ N/m}^2$) alene fra fraværet av ulovlige bølgemoder mellom platene. Dette er *minuskatalysens fysiske ur-bevis*: ved å sette to strenge grenser som ekskluderer bølgelengder større enn gapet, skaper selve eksklusjonen et bindende strukturtrykk som holder arkitekturen sammen.

---

## 4. Maxwells Demon og «Den Langsomme Heisen» i Dør 18

I 1867 foreslo Maxwell sitt berømte tankeeksperiment: En tilsynelatende masseløs «demon» vokter en luke mellom to gasskamre, måler molekylenes hastighet og slipper kun raske molekyler én vei og langsomme den andre, slik at en temperaturforskjell oppstår uten tilført arbeid ($\Delta S_{\text{tot}} < 0$).

Gjennom Szilard (1929), Landauer (1961) og Bennett (1982) ble demonens regnskap avslørt: Demonen må lagre måleresultatet i et fysisk minne med endelig kapasitet. For å fortsette syklusen må minnet nullstilles, hvilket tvinger frem en irreversibel entropiproduksjon $\Delta S_{\text{erase}} \ge k_B \ln 2$ og varmeavgivelsen $Q_{\text{erase}} \ge k_B T \ln 2$ per bit.

I industriell sanntidsstyring oppstår imidlertid en enda strengere skranke enn den kvasistatiske Landauer-grensen. Landauer-grensen $k_B T \ln 2$ gjelder kun når tilstandsovergangen utføres uendelig langsomt ($\tau_{\text{proc}} \to \infty$). Når et kontrollsystem tvinger en fysisk prosess langs en tilstandsbane $\lambda(t)$ fra $\lambda(0) = \lambda_A$ til $\lambda(\tau_{\text{proc}}) = \lambda_B$ på en **endelig tid** $\tau_{\text{proc}} > 0$, fastslår endelig-tids termodynamikk (Salamon & Berry 1983; Crooks 2007) at det minimalt dissiperte ekstraarbeidet vokser omvendt proporsjonalt med prosesstiden:

$$W_{\text{diss}}(\tau_{\text{proc}}) = W_{\text{applied}} - \Delta F \ge \frac{T_0\,\mathcal{L}_{\text{thermo}}^2}{\tau_{\text{proc}}}$$

der $\mathcal{L}_{\text{thermo}}$ er den termodynamiske lengden i Ruppeiner-/Fisher–Rao-metrikken $g_{ij}(\lambda) = \frac{\partial^2 S}{\partial \lambda^i \partial \lambda^j}$:

$$\mathcal{L}_{\text{thermo}} = \int_0^{\tau_{\text{proc}}} \sqrt{g_{ij}\bigl(\lambda(t)\bigr)\,\dot{\lambda}^i(t)\,\dot{\lambda}^j(t)}\,\mathrm{d}t$$

**Doktrinen om Den Langsomme Heisen (Organ T1–T10 i Dør 18):**
Dersom en algoritmisk kontroller forsøker å presse en fysisk tilstandsovergang gjennom på $\tau_{\text{proc}} \to 0$ (en øyeblikkelig «heis» i tilstandsrommet), divergerer den dissiperte effekten som $\dot{Q}_{\text{diss}} \ge T_0\mathcal{L}_{\text{thermo}}^2 / \tau_{\text{proc}}^2 \to \infty$. Systemets kjølekapasitet $\dot{Q}_{\text{cool,max}}$ overskrides, hvilket fører til termisk runaway. Derfor håndhever Dør 18 den eksakte fartsbegrenseren i tilstandsrommet:

$$\bigl\|\dot{\lambda}(t)\bigr\|_g = \sqrt{g_{ij}(\lambda)\,\dot{\lambda}^i\dot{\lambda}^j} \le \sqrt{\frac{\dot{Q}_{\text{cool,max}}}{T_0}} \implies \tau_{\text{proc}} \ge \mathcal{L}_{\text{thermo}}\sqrt{\frac{T_0}{\dot{Q}_{\text{cool,max}}}}$$

Enhver kommando som krever en raskere tilstandsendring enn hva den termodynamiske metrikken $g_{ij}(\lambda)$ og kjølebudsjettet $\dot{Q}_{\text{cool,max}}$ tillater, bremses ned til «Den Langsomme Heisen» eller felles momentant med `KILL_FINITE_TIME_THERMO_EXCEEDED`.

---

## 5. De Fem Termodynamiske Konstitusjonsprinsippene, `SPEC-250-THERMO` og Organ T1–T10 i Dør 18

I stedet for å anta at informasjon er en vektløs, friksjonsfri abstraksjon i skyen, slår arkitekturen fast at **informasjon er fysisk bundet**. Virkeligheten genereres ikke fritt i minnet, men innvilges lokalt gjennom et ufravikelig termodynamisk oppgjør (*«Reality is not generated. Reality is admitted»*). Dette håndheves i kjørbar kode gjennom fem konstitusjonelle prinsipper:

1. **Landauer-skatten ($Q \ge k_B T \ln 2$):** Å sjonglere kontrafaktiske hypoteser i det reversible fasedomenet ($\Phi$) koster i praksis ingenting så lenge involusjonen $F(F(s)) = s$ er verifisert ($\Delta I_{\text{erase}} = 0$). Men idet en kandidat overføres til en irreversibel fysisk handling ($\Omega$), må systemet slette de alternative banene fra tilstandsrommet. Ved $+4{,}0\,^\circ\text{C}$ ($T = 277{,}15\text{ K}$) koster slettingen av én enkelt bit nøyaktig $2{,}6523 \times 10^{-21}\text{ J}$ ($10{,}865\text{ aJ}$ for en 4096-bits blokk). Påstander om å gjennomføre informasjonskollaps uten å betale denne slettevarmen avvises feillukket med `KILL_LANDAUER_LIMIT_VIOLATION`.
2. **Kostnad før konsekvens (TERMO-laget):** For å forhindre at systemet tømmer ubetalt energetisk gjeld over på omgivelsene, integreres TERMO-laget som en obligatorisk kontrollflate i realiseringskjeden:
   $$\Phi \longrightarrow \Pi_K \longrightarrow \text{IDC} \longrightarrow \text{TERMO} \longrightarrow \Omega \longrightarrow W$$
   Ingen konsekvensport kan åpnes ($\Omega_{\text{TERMO}} = \text{OPEN}$) før den termodynamiske bæreevnen ($Q_{\text{total}} \le Q_{\max}$, $P_{\text{peak}} \le P_{\max}$, $T_{\text{node}} < T_{\max}$) er eksplisitt verifisert på forhånd. Termodynamisk kapasitet kan aldri bevilges eller bokføres *post-factum*.
3. **Maxwell-integrabilitet (Schwarz' teorem):** Målte responser og telemetri fra sensorer kan ikke opptre som en gyldig fysisk tilstand dersom de motstrider hverandre. Kryssderivatene av tilstandspotensialet må tilfredsstille ulikheten:
   $$\left| \frac{\partial^2 \Psi}{\partial x \partial y} - \frac{\partial^2 \Psi}{\partial y \partial x} \right| \le \epsilon_{\text{Maxwell}}$$
   slik at lokale målinger beviselig kan integreres til et felles potensial. Dersom kryssderivatene divergerer, avsløres målingene som telemetriforfalskning eller ustabilt sensorbrudd, og Organ T2 kapper kretsen med `KILL_MAXWELL_INTEGRABILITY_FAILED`.
4. **Lukkede kaskadekretser (OrgelKraft™ & $\Delta R = 0$):** For at et industrielt eller kjemisk anlegg skal følge termodynamikken, må det opprette eksakt rasjonal massebalanse ($\Delta R = 0$). Avfall og spillvarme fra én prosess-sløyfe utgjør drivkraften for den neste, slik at netto ukompensert restpost over syklusen holdes eksakt lukket.
5. **Feillukket stans ved null spenning (`0,00 V DC`):** Dersom det oppstår støy, manglende kjølereservoar eller et brudd på bevaringslovene, nekter maskinen å fortsette på gjetninger. Drivspenningen kalles umiddelbart ned til **$0{,}00\text{ V DC}$** (`GATE :: KILL` eller `HOLD`), og den fysiske kretsen kobles fra.

### 5.1 Kildekoden for `SPEC-250-THERMO` ($\Pi_{K,\text{thermo}}$ i `spec250_gate.rs`)

I `03_ENGINES/spec250_gate.rs` er flyttall (`f32`/`f64`) bannlyst for å forhindre avrundingslekkasje. Regnskapet føres i heltalls **attojoule** ($\text{aJ} = 10^{-18}\text{ J}$, `u128`) og **mikrojoule** ($\mu\text{J} = 10^{-6}\text{ J}$, `i128`):

```rust
// Fra 03_ENGINES/spec250_gate.rs (DEL 6: SPEC-250-THERMO)
pub const LANDAUER_PER_BIT_AJ: u128 = 3;      // Eksakt 2.6523e-21 J = 0.00265 aJ (tak-avrundet i aJ)
pub const LANDAUER_4096_BITS_AJ: u128 = 11;   // 4096 bits * 2.6523e-21 J ≈ 10.865 aJ

pub const W_UWB_TOF_PROBE_UJ: i128 = 1;            // 80 nJ rundet opp til 1 uJ
pub const W_OPTICAL_532_PULSE_UJ: i128 = 4;        // 4.00 uJ (100 mW optisk @ 25% eff i 10 us)
pub const W_CRYPTO_SIGN_UJ: i128 = 43;             // 42.50 uJ (TRNG + Ed25519 sign)
pub const W_CRYPTO_VERIFY_ONLY_UJ: i128 = 13;      // 12.50 uJ (Ed25519 verify uten eNVM fsync)
pub const W_ENVM_WAL_FSYNC_UJ: i128 = 130;         // 130.00 uJ (4096 bit FRAM/MRAM forsegling)
pub const W_SPEC250_MOSFET_OPEN_UJ: i128 = 250;    // 250.20 uJ (5.00 V gate-ladning og hold)
pub const W_EARLY_REJECT_TDC_UJ: i128 = 8;         // 8.15 uJ (TDC-avbrudd ved ds² > 0)
```

Ved et romlignende relé-angrep ($\mathrm{d}s^2 > 0$) kapper mottakernoden sekvensen i TDC-porten etter kun $8\;\mu\text{J}$ (`W_EARLY_REJECT_TDC_UJ`), før signatursjekk, før WAL-forsegling og før MOSFET-ladning, slik at angriperen brenner hele sitt eksterne energibudsjett mot en uendret dør på `0,00 V DC`.

### 5.2 De Ti Kontrollorganene (Organ T1–T10) i Dør 18 (`door18_heis_baereevne`)

I `03_ENGINES/door18_heis_baereevne/` evalueres enhver kandidat med oppstrøms frigivelse fra Dør 15 ($\Pi_K$) og Dør 17 (KY-Nash) gjennom ti spesialiserte bæreorganer under subsumsjonsloven $\texttt{KILL} > \texttt{HOLD} > \texttt{OPEN}$ (`27/27 PASS` i `test_baereevne.py`):

| Organ | Kontraktmodul | Fysisk invariant og kontrolloppdrag | Feillukket dom (`KILL` / `HOLD`) |
| :--- | :--- | :--- | :--- |
| **T1 (`18.01`)** | `t01_energy_budget.py` | **Landauer-skatt & Toppeffekt:** $E_{\text{op}} \le E_{\max}$, $P_{\text{peak}} \le P_{\max}$ og $E_{\text{op}} \ge k_B T \ln(2)\,\Delta I_{\text{erase}}$. | `KILL_LANDAUER_LIMIT_VIOLATION`<br>`KILL_PEAK_POWER_EXCEEDED` |
| **T2 (`18.02`)** | `t02_thermal_budget.py` | **Varme & Maxwell-integrabilitet:** $T_{\text{node}} < T_{\max}$, margin $M_T = T_{\max} - T_{\text{node}}$ og $\lvert\partial_x\partial_y\Psi - \partial_y\partial_x\Psi\rvert \le \epsilon_{\text{Maxwell}}$. | `KILL_MAXWELL_INTEGRABILITY_FAILED`<br>`KILL_THERMAL_LIMIT_EXCEEDED`<br>`HOLD_THERMAL_MARGIN_LOW` |
| **T3 (`18.03`)** | `t03_latency_budget.py` | **Relativistisk kausalitet & Latens:** Minkowski-intervall $\mathrm{d}s^2 = -(c\Delta t)^2 + d^2 \le 0$ ($\tau_{\text{transit}} \ge d/c$). | `KILL_SUPERLUMINAL_CAUSALITY_VIOLATION`<br>`KILL_LATENCY_BUDGET_EXCEEDED` |
| **T4 (`18.04`)** | `t04_memory_budget.py` | **Endelig tilstandsminne:** Forhindrer at Maxwells demon lagrer uendelig historikk uten sletting ($M_{\text{used}} + \Delta M \le M_{\max}$). | `KILL_MEMORY_CAPACITY_EXCEEDED` |
| **T5 (`18.05`)** | `t05_bandwidth_budget.py` | **Shannon–Hartley & DPI:** Sjekker kanalens båndbredde og *Data Processing Inequality* ($\text{gain} \le 1{,}0$). | `KILL_SIGNAL_INTEGRITY_GAIN_VIOLATION`<br>`KILL_BANDWIDTH_EXCEEDED` |
| **T6 (`18.06`)** | `t06_material_wear.py` | **Litisk/mekanisk utmatting:** Akkumulert slitasje $W_{\text{wear}} + \Delta W \le W_{\max}$ og $\dot{W} \le \dot{W}_{\max}$. | `KILL_MATERIAL_FATIGUE_EXCEEDED`<br>`KILL_ACCELERATED_DEGRADATION` |
| **T7 (`18.07`)** | `t07_dissipation.py` | **2. hovedsetning, Involusjon & IDC:** Krever $\Delta S_{\text{irr}} \ge 0$ og eksplisitt $\text{IDC} = (D_i, R_i, C_i(t), U_{\text{irrev}})$ i $D_2$; fritak i $D_0/D_1$ ved $F(F(s))=s$. | `KILL_SECOND_LAW_ENTROPY_VIOLATION`<br>`KILL_UNDECLARED_IRREVERSIBILITY_BOUNDARY`<br>`OPEN_REVERSIBLE_INVOLUTION_EXEMPT` |
| **T8 (`18.08`)** | `t08_reserve_margin.py` | **Kompositt sikkerhetsreserve:** $R_{\text{comp}} = \min(R_E, R_Q, R_\tau, R_M, R_B, R_W)$ og global supragrense $C_{\text{supra}} = \min_i C_i(t)$. | `KILL_RESERVE_FULLY_EXHAUSTED`<br>`HOLD_RESERVE_MARGIN_THIN` |
| **T9 (`18.09`)** | `t09_resource_witness.py` | **Kryptografisk ressursvitne ($W_{18}$):** Append-only SHA-256-kjede som låser observasjonene fra T1–T8 før T10 feller dom. | `KILL_WITNESS_CHAIN_TAMPERED` |
| **T10 (`18.10`)**| `t10_carrying_gate.py` | **Bæreevnesporten ($\Omega_{18}$):** Subsumsjonsmotor (`KILL > HOLD > OPEN`). Krever at samtlige T1–T9 returnerer `OPEN` før `can_carry = True`. | `KILL_BUDGET_EXCEEDED:...`<br>`DOOR_18_CARRYING_CAPACITY_V1_REALIZED` |

---

## 6. Strålens Syv Dimensjoner i *Konseptuell Granitt*: Fra Nullgeodet ($k_\mu k^\mu = 0$) til Rue Lhomond (`07.11.1867–2026`)

I arkitekturen til *Konseptuell granitt* og de tilhørende spesifikasjonene opptrer **«stråler»** (og *stråling*) aldri som en uforpliktende metafor, men som selve den kausale, termodynamiske og geometriske prøvesteinen mellom mulighetsrommet ($\Phi \subset \mathbf{NP}$) og den fysiske virkeligheten ($\Omega \subset \mathcal{P}$).

På tvers av verket manifesterer strålene seg langs syv skarpe dimensjoner:

### 6.1 Den Eikonale Strålen: Nullgeodeten som Rettslig Skranke

I den geometrisk-optiske grensen av Maxwells ligninger ($F_{\mu\nu} = f_{\mu\nu}\mathrm{e}^{\mathrm{i}S/\lambda}$) defineres en **stråle** av det kovariante hovedsymbolet og nullbetingelsen for eikonalfasen $S$:

$$H(x, k) = \frac{1}{2} g^{\mu\nu}(x) k_\mu k_\nu = 0 \iff k_\mu k^\mu = 0$$

De karakteristiske strålene følger affint parametriserte **nullgeodeter** ($\frac{\mathrm{d}x^\mu}{\mathrm{d}\sigma} = k^\mu, \; k^\nu \nabla_\nu k^\mu = 0$). I realiseringsgrammatikken fungerer dette som den elektrodynamiske kodifiseringen av selve *lovhjemmelen*:

* **Metrikken ($g^{\mu\nu}$)** er rettsgrunnlaget og maskinvarens fysiske skranker.
* **De karakteristiske strålene** er de *eneste* lovlige banene for realisering i romtiden.
* Enhver kandidatvektor $k_\mu$ som bryter lyskjeglebetingelsen ($R_{\text{null}} > \varepsilon_{\text{tol}}$) eller transversalitetskravet ($k_\mu a^\mu \neq 0$), avsløres som «maskinell fiksjon» og kuttes umiddelbart med $\mathrm{KILL}$ ($0{,}00\text{ V DC}$).

### 6.2 Den Frikoblede Strålen: Nærfelt vs. Irreversibelt Strålingsfelt ($\text{Rev}^1 \to \text{Rev}^2$)

Når en ladning $q$ beveger seg, splitter Liénard–Wiechert-feltene det elektriske feltet i to fundamentalt ulike bidrag:

$$\mathbf{E}(\mathbf{x}, t) = \mathbf{E}_{\text{velocity}}(\mathbf{x}, t) + \mathbf{E}_{\text{radiation}}(\mathbf{x}, t)$$

* **Hastighetsfeltet / Nærfeltet ($\propto R^{-2}$):** Er bundet til ladningen og bærer ingen netto energi til uendelig ($\text{Rev}^1$).
* **Akselerasjonsfeltet / Strålingsfeltet ($\propto R^{-1}$):** Avhenger lineært av akselerasjonen $\ddot{\mathbf{z}}(t_r)$ og løsriver seg fra kilden som **irreversibel elektromagnetisk stråling** ($\text{Rev}^2$). Som det heter på kaien i Risør når Super Duplex-kontaktoren slår inn med en liten lysbue: ingen JSON-pakke med `undo()` kan noen gang samle inn igjen fotonene som har forlatt gnistgapet.

### 6.3 Den Evanescente Strålen: Fysikkens Egen $\mathrm{HOLD}$-Port

I utvidet CFJ–Proca-elektrodynamikk og Klein–Gordon-seleksjon ($\lvert\mathbf{k}\rvert^2 = \frac{\omega^2}{c^2} - m_{\text{eff}}^2$) oppstår tre stråleregimer:

* **Propagerende stråle ($\omega > c m_{\text{eff}} \implies \mathrm{OPEN}$):** Bølgetallet $k$ er reelt, og strålen bærer autorisert energi gjennom porten.
* **Kiral dreining ($\omega_+(k) \neq \omega_-(k)$):** Vakuum-birefringens roterer polarisasjonsplanet med $\Delta\vartheta = \frac{1}{2}(k_+ - k_-)L$ og avslører enhver uautorisert mellommann som ikke kjenner mediets kirale signatur.
* **Evanescent bølge ($\omega < c m_{\text{eff}} \implies \mathrm{HOLD}$):** Bølgetallet blir rent imaginært ($k = \mathrm{i}\kappa$). Feltet faller eksponentielt av inn i mediet ($\mathrm{e}^{-\kappa z}$), det elektriske og magnetiske feltet er $90^\circ$ ute av fase, og den tidsmidlede Poynting-fluksen er eksakt null ($\langle \mathbf{S} \rangle_t \equiv \mathbf{0}$). Strålen lyser opp grenseflaten som en «evanescent fotnote» uten å lekke én joule uautorisert kraft inn i $\Omega$.

### 6.4 Vokter- og Målestrålene: Laser, Radar, Safir og Kavitasjon

I *Infranett v0.5* og dypvannsnoden *SPEC-250* brukes fysiske stråler som ubøyelige dørvakter ($\Pi_K$ og $\Pi_{\text{orth}}$):

* **Den optiske vaktstrålen ($\lambda = 1550\text{ nm}$ og $532\text{ nm}$):** Mens et UWB-radiosignal kan trenge gjennom en betongvegg på tre meters hold innenfor Alexandrov-fristen ($\tau_{\text{ToF}} \le 133{,}4256\text{ ns}$), stanses den infrarøde laserstrålen momentant av veggen (`OPTICAL_LOS_BROKEN_WALL_OCCLUSION` $\implies 0{,}00\text{ V HOLD}$). Under radiotaushet (EMCON) har friromslaseren en strålemidje på kun $w(20\text{ m}) \approx 5{,}38\text{ mm}$; enhver fysisk sonde som stikkes inn i strålen, kaster skygge og kutter kretsen.
* **Safirvinduet og kavitasjonsstrålene på 500 m dyp:** Gjennom det $2{,}0\text{ mm}$ tykke monokrystallinske $\alpha\text{-Al}_2\text{O}_3$-vinduet under $898\,900\text{ N}$ vanntrykk endres lysstrålens gangtid med kun $\Delta\tau_{\text{RT}} = -0{,}27\text{ fs}$ ($55\,555$ ganger mindre enn TDC-oppløsningen på $15\text{ ps}$). Når rur (*Balanus crenatus*) begroer utsiden, vaskes vinduet av $275\text{ nm}$ UV-C-stråling ($86{,}4\,\%$ transmisjon) og $42\text{ kHz}$ akustisk kavitasjon som pisker løs **mikrostråler** ($v_{\text{jet}} \approx 110\text{ m/s}$), etterfulgt av $2\,500\text{ ms}$ disiplinert boblekarantene ved $0{,}00\text{ V DC}$ før laserstrålen får skyte igjen.
* **77 GHz kuvøse-stråle og Stokes-polarisasjon:** Over det premature spedbarnet måler 77 GHz-strålen brystkassens løft på $0{,}05\text{ mm}$ uten berøring og nekter å tegne en falsk kurve ved støy. I militær og maritim målavklaring (`SPEC-401`) avsløres DRFM-spøkelsessignaler fordi de bryter Noether-symmetrien i **Stokes-vektoren** $\vec{S} = [I, Q, U, V]^\top$: et ekte stålskrog kan ikke vippe polarisasjonsvinkelen $\psi = \frac{1}{2}\mathrm{atan2}(S_2, S_1)$ raskere enn $\dot{\psi}_{\max} = 45^\circ/\text{s}$.

### 6.5 Kjernefysiske Stråler i Grunnfjellet: Spallasjon, Radiolyse og $^{57}\text{Fe}$

I *OrgelKraft* (Kjerneprøve V) er hele prosesskjeden bygget rundt tre typer stråler i grunnfjellet:

1. **Spallasjonsstrålen som eksternt vitne ($W = 1$):** Den underkritiske thorium-smeltesaltkjernen ($k_{\text{eff}} = 0{,}960 < 1{,}000$, forsterkning $M_{\text{sub}} = 25{,}0\times$) eier ingen evne til å opprettholde kjedereaksjonen alene. Den er 100 % avhengig av en kontinuerlig, ekstern protonstråle mot blymålet. Kuttes strømmen til $0{,}00\text{ V DC}$, slokner strålen på mikrosekunder ($W = 0$), bølgetallet blir imaginært ($k = \mathrm{i}\kappa$), og kjernen dør momentant.
2. **MeV-gammastråling til kjemisk arbeid (Radiolyse):** I stedet for å gå til spille som varme, brukes gammastrålingen fra kjernen i Pipe 2 til radiolytisk vannsplitting som produserer eksakt $0{,}3588\text{ kg H}_2/\text{døgn}$, som deretter møter $3{,}9317\text{ kg CO}_2$ over Invar-36-membranen ($293{,}0\text{ mV}$, $0{,}0\text{ W}$) og danner $2{,}6816\text{ kg}$ eddiksyre med $\Delta R = 0$.
3. **Den rekylfrie $14{,}4\text{ keV}$ gammastrålen i $^{57}_{26}\text{Fe}$ (Mössbauer-låsen):** En frittflyvende kjerne som sender ut et gammafoton, sklir bakover i rekyl ($E_R = E_\gamma^2 / 2Mc^2$) og mister resonansen. Men når $^{57}\text{Fe}$-kjernen er boltet fast i grunnfjellets krystallgitter, tar hele krystallens masse imot rekylen ($f_{\text{LM}} = \exp(-\langle x^2 \rangle k_\gamma^2) \ge 1 - 10^{-12}$).

### 6.6 Advarselen fra Rue Lhomond: Boken som Fortsatt Stråler

I Kapittel 2.1.6 står verkets sterkeste historiske påminnelse om hvorfor stråling aldri må forveksles med en ufarlig tanke i $\Phi$: **Marie Skłodowska-Curie** (født `07.11.1867` – på nøyaktig samme 7. november-meridian som Lise Meitner, C. V. Raman, Albert Camus og forfatteren selv).

Da hun isolerte radium ($^{226}_{88}\text{Ra} \to \,^{222}_{86}\text{Rn} + \alpha$, $T_{1/2} = 1\,600\text{ år}$), bar hun de selvlysende reagensrørene i frakkelommen og hadde dem på nattbordet fordi det blågrønne skjæret så ut som et vakkert, uforpliktende lys i $\text{Rev}^1$. Men hver alfapartikkel og gammastråle var en irreversibel $\text{Rev}^2$-hendelse i $D_2$ uten blyskjerming ($\neg\Pi_K$). Hennes originale laboratorienotatbøker fra 1898 i Paris er derfor vitenskapshistoriens mest bokstavelige fysiske **WORM-logg ($D_3$)**: tanken og fingeravtrykket hennes er brent så dypt inn i papiret at boken fortsatt **stråler** og puster ut radon-222 hundre år etter hennes død, innlåst i blyskrin som kun kan åpnes mot en fysisk signert Level 01-ansvarsfraskrivelse.

### 6.7 Den Syvende Strålen langs 7. November-Meridianen: Raman-Skiftet ($\Delta\nu_{\text{Raman}}$) og Meitners Spaltning

Langs den samme **7. november-meridianen** (`07.11.1867 → 07.11.1878 → 07.11.1888 → 07.11.1913 → 07.11.1989 → 07.11.2026`) lukkes strålens syvende dimensjon av **Lise Meitner** (`07.11.1878`) og **Sir C. V. Raman** (`07.11.1888`):

* **Raman-strålen som materiens uforfalskelige vitnesignatur ($\hbar\omega_{\text{ut}} = \hbar\omega_{\text{inn}} \mp \hbar\Omega_{\text{gitter}}$):** Mens elastisk Rayleigh-spredning returnerer lyset uendret ($\Delta E = 0$, $\text{Rev}^1$), tvinger uelastisk **Raman-spredning** fotonet til å veksle et eksakt kvantum vibrasjonsenergi $\hbar\Omega_{\text{gitter}}$ (et optisk fonon) med selve krystallgitteret ($\text{Rev}^2$). Strålen som kommer ut, bærer molekylets indre bindingsstyrke som et frekvensskift $\Delta\nu_{\text{Raman}}$ ingen ekstern angriper kan forfalske uten å endre selve atombindingene i steinen.
* **Meitners fisjonsstråle og hvorfor kjernen må holdes underkritisk ($\Delta m \cdot c^2 \approx 200\text{ MeV}$):** Da Lise Meitner i desember 1938 beregnet væskedråpemodellen for kjernefisjon, viste hun at et enkelt termisk nøytron kan få en ustabil tung kjerne til å briste langs sin egen sadelflate ($A_3$-fold). Nettopp derfor forbyr `OrgelKraft` enhver superkritisk kjedereaksjon og låser reaktoren til det underkritiske beltet ($k_{\text{eff}} = 0{,}960 < 1{,}000$) og protaktinium-233s naturgitte `HOLD`-sluse ($t_{1/2} = 26{,}97\text{ døgn}$).

> **`[⊙ ≺ 1 // POINCARÉ-LÅS // STRÅLENS KONSTITUSJONELLE LOV]`**  
> **I $\Phi$ er strålen et vektløst lys; i $\Pi_K$ er den en nullgeodetisk lov og en $133{,}43\text{ ns}$ kausal grense; og i $D_2/D_3$ er den et irreversibelt spor i materien som krever bly, safir, vakuum og et våkent menneske ved bryteren.**


