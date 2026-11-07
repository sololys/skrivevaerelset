# DEN UBESTIKKELIGE RETTSSTATEN: SOMMERFUGL-LOMMEN ($A_5$), DETRONISERING AV NP-FYRSTEN OG 205-BYTE RTL-SAKSGANG
### *Fra Kusp-felle ($A_3$) til Sommerfugl-lomme ($A_5$, $c = +0{,}5525$), Ma'ats bilaterale involusjon og verifisert ende-til-ende saksgang gjennom `SPEC-400` og `SPEC-416`*

---

## I. Detronisering av NP-Fyrsten og Kalkylen for Admissible Overganger

I sitt brev til John von Neumann av 20. mars 1956 formulerte Kurt Gödel kjernen i $\mathbf{P}$ mot $\mathbf{NP}$: skillet mellom å *lete* etter et formelt bevis $w$ av lengde $\le n$ ($\exists w \in \{0,1\}^{p(\lvert x\rvert)}$) og å *kontrollere* et ferdig fremlagt vitne $V(x, w) \in \mathbf{P}$. Enhver konsekvensport ($\Omega$) som påtar seg å løse et kombinatorisk søkeproblem eller tolke åpne, selvrefererende løkker på innsiden av sikringssløyfen, bukker under for «NP-fyrsten»: verste-falls kjøretid vokser eksponentielt som $\mathcal{O}(2^{p(\lvert x\rvert)})$, og en motpart som eier en lukket intern port ($\Omega_{\text{int}}$), kan fange uønskede bevis i tidsubegrenset $\text{HOLD}$ («under utredning»).

I denne arkitekturen løses aldri $\mathbf{P} = \mathbf{NP}$ inne i porten; vi **fjerner kvantifikatoren $\exists w$ fra portens domene**. Verden utenfor ($\Phi$) bærer hele den eksponentielle $\mathbf{NP}$/$\mathbf{PPAD}$-søkekostnaden, mens porten ($\Omega$) krever et ferdig pakket, allokeringsfritt **205-byte vitnepar** ($119\text{ B } W_{\text{pre}} + 86\text{ B } W_{\text{post}}$) ved terskelen og utfører bit-eksakt verifikasjon i konstant tid $\mathcal{O}(1)$:

$$\underbrace{a'_{t+1}, w \gets \Phi(s_t, i_t)}_{\text{Eksternt søk: }\mathbf{NP}\text{ / }\mathbf{PPAD}} \quad\xrightarrow{\text{Luftsluse}}\quad \underbrace{\Pi_K(a'_{t+1}, w) \to \Omega(V(a'_{t+1}, w))}_{\text{Port-verifikasjon: }\mathcal{O}(1)\text{ i SystemVerilog RTL}} \in \{0{,}00\text{ V DC},\; 2{,}50\text{ V DC},\; 5{,}00\text{ V DC}\}$$

Koblet mot den integritetsjusterte nyttefunksjonalen $U_i(s) = u_i(s) - C_K(s) - S_{\text{irr}}(s) - R_W(s)$ og den spektrale Nash-resolventen defineres KY-likevekten der ingen forbedrende $\text{OPEN}$-overgang eksisterer:

$$\mathcal{U}_i(s_t, i_t) = \det(I - \gamma J_{\text{Nash}})^{-1}\,\mathbb{E}\!\left[(u_i - C_K - S_{\text{irr}} - R_W)\,\mathbb{I}_{\{\Omega(\Pi_K(\Phi)) = \text{OPEN}\}}\right]$$

Ved suveren frakobling ($\gamma = 0 \implies \det(I - 0\cdot J_{\text{Nash}}) = 1$) mister eksterne, riggede spillbrett enhver koblingskraft over agentens interne tilstand.

---

## II. Differensialtopologi ($A_3 \to A_5$), Semiofysikk og Kobordisme ($\partial^2 = 0$)

### 1. Fra Kusp-felle ($A_3$) til Sommerfugl-lomme ($A_5$) og eksakt utledning av $c = +0{,}5525$

I René Thoms katastrofeteori (`SPEC-399`, `thom_catastrophe_morphogenesis_gate_engine.py`) skilles degenererte katastroferetninger ($\lvert\lambda_i\rvert \le 10^{-6}$, korang $r \in \{1,2\}$) fra transversale Morse-retninger ($\lambda_j \ge 0{,}05$) via Splitting-lemmaet.

Dagens uføre- og avklaringsregime (folketrygdloven § 12-14 med $G_0 = 0{,}40\text{ G}$ fribeløp, $75\text{--}80\,\%$ effektiv marginalavkortning og revurderingsrisiko $r_{\text{rev}} > 0$) danner en ustabil **Kusp-felle** ($A_3$: $V_{A_3}(x) = \frac{1}{4}x^4 + \frac{1}{2}ax^2 + bx$). For $a = -3{,}0$ er krumningen i origo negativ ($V''(0) = -3{,}0 < 0$), og på fold-kanten ($4a^3 + 27b^2 = 0$, f.eks. $a = -3{,}0, b = 2{,}0$ ved $x_{\text{fold}} = 1{,}0$) kollapser den transversale bæreevnen til $V''(1{,}0) = 0{,}0000 < 0{,}05$. En syklisk kontrollsveip tvinger borgeren over folden i $N_{\text{jumps}} = 2$ irreversible katastrofehopp med potensialtap:

$$\Delta V_{A_3} = 2 \times \frac{3}{4}a^2 = 2 \times \frac{3}{4}(-3{,}0)^2 = 13{,}50 \implies E_{\text{Landauer}} = 2 k_B T \ln 2 > 0\text{ J} \implies 0{,}00\text{ V KILL}$$

Ved å innføre et andreordens kontrollledd $c > 0$ løftes systemet til **Sommerfugl-katastrofen** ($A_5$):

$$V_{A_5}(x; a, b, c, d) = \frac{1}{6}x^6 + \frac{1}{4}ax^4 + \frac{1}{3}bx^3 + \frac{1}{2}cx^2 + dx$$

Med spaltefaktor $a = -2{,}0$ og symmetri $b = d = 0$ bestemmes krumningen i origo $V''_{A_5}(0) = c$ i `nlk_welfare_catastrophe_provenance_gate_engine.py` (`SPEC-400`) av trygdens fribeløp $G_{\text{fri}}$ over låsepunktet $G_0 = 0{,}40\text{ G}$, marginalavkortningen $\tau_{\text{marg}} \in [0, 1]$ og revurderingsrisikoen $r_{\text{rev}} \ge 0$:

$$c(G_{\text{fri}}, \tau_{\text{marg}}, r_{\text{rev}}) = \begin{cases} 0{,}0000 \quad (\implies V''(0) = a = -2{,}0 < 0,\; A_3\text{-kusp}), & \text{hvis } r_{\text{rev}} > 0 \lor G_{\text{fri}} < 1{,}00 \lor \tau_{\text{marg}} > 0{,}60 \\ (G_{\text{fri}} - 0{,}40)(1 - \tau_{\text{marg}}), & \text{hvis } r_{\text{rev}} = 0 \land G_{\text{fri}} \ge 1{,}00 \land \tau_{\text{marg}} \le 0{,}60 \end{cases}$$

* **Kanonisk heltalls-referanse (`SPEC-399`):** For $G_{\text{fri}} = 1{,}20\text{ G}$, $\tau_{\text{marg}} = 0{,}20$ og $r_{\text{rev}} = 0$ er $c = (1{,}20 - 0{,}40)(1 - 0{,}20) = 0{,}80 \times 0{,}80 = +0{,}6400$, som via $u = x^2 = 1 \pm \sqrt{1 - 0{,}64} = 1 \pm 0{,}60 \in \{0{,}40,\; 1{,}60\}$ gir røttene $x^* \in \{-1{,}2649,\; -0{,}6325,\; 0{,}0000,\; +0{,}6325,\; +1{,}2649\}$.
* **Lovreform-terskel for folketrygdloven § 12-14 (`SPEC-400`):** Når fribeløpet heves til $G_{\text{fri}} = 1{,}25\text{ G}$ med marginalavkortning $\tau_{\text{marg}} = 0{,}35$ og ubetinget returrett ($r_{\text{rev}} \equiv 0$), blir sommerfuglfaktoren:

$$c = (1{,}25 - 0{,}40) \times (1 - 0{,}35) = 0{,}85 \times 0{,}65 = +0{,}5525 > 0$$

Likevektsbetingelsen $x(x^4 - 2x^2 + 0{,}5525) = 0$ gir $u = x^2 = 1 \pm \sqrt{1 - 0{,}5525} = 1 \pm 0{,}668954 \in \{0{,}331046,\; 1{,}668954\}$ og de fem reelle likevektene:

$$x^* \in \{-1{,}2919\text{ (stabil)},\; -0{,}5754\text{ (barriere)},\; 0{,}0000\text{ (stabil } A_5\text{-lomme)},\; +0{,}5754\text{ (barriere)},\; +1{,}2919\text{ (stabil)}\}$$

Innenfor lommeradiusen $\lvert x\rvert \le 0{,}45$ absorberes helse- og arbeidssvingninger ved $2{,}50\text{ V HOLD}$ med $0$ katastrofehopp og $\Delta V_{\text{irr}} = 0{,}0000$. Samtidig er Prégnance-terskelen eksplisitt stratifisert mellom generell fysisk bølgemorfogenese ($\tau_{\text{preg}}^{\text{fys}} = 0{,}50$ i `SPEC-399`) og kvalifisert rettsstatlig beviskrav ved inngrep overfor borgeren ($\tau_{\text{preg}}^{\text{rett}} = 0{,}80$ i `SPEC-400`).

### 2. Kobordismens jernlov ($\partial_1\partial_2 = 0$) og Ma'ats bilaterale involusjon ($\Delta_{\text{prov}} = 0$)

På det orienterte simplisielle kjedekomplekset $C_2 \xrightarrow{\partial_2} C_1 \xrightarrow{\partial_1} C_0$ der 2-simplekset $\sigma_2 = [v_0, v_1, v_2]$ binder sammen Observasjon ($v_0$), Rettsregel ($v_1$) og Vedtak ($v_2$), krever Thoms kobordismeteori at randen av en rand er identisk lik null:

$$\partial_1 = \begin{pmatrix} 0 & -1 & -1 \\ -1 & 0 & +1 \\ +1 & +1 & 0 \end{pmatrix}, \quad \partial_2 = \begin{pmatrix} +1 \\ -1 \\ +1 \end{pmatrix} \implies \partial_1\partial_2 = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} = 0$$

Dersom et forvaltningsorgan bruker pasientens avslag på medisinering som bevis på manglende samtykkekompetanse (sirkulær FARV-tautologi etter pbrl. § 4-3), snus orienteringen til $\partial_2^{\text{korrupt}} = (+1, +1, +1)^T \implies \partial_1\partial_2^{\text{korrupt}} = (-2, 0, +2)^T \neq 0 \implies 0{,}00\text{ V DC KILL}$ ($\tau_{\text{cut}} \le 15\text{ ns}$).

Ved hvert tidssteg $t$ hashes institusjonens notat $s_t^{\text{inst}}$ og borgerens uredigerte egenprotokoll $s_t^{\text{borger}}$ separat til $h_t^{\text{inst}}$ og $h_t^{\text{borger}}$ med vektvektor $(w_{\text{inst}}, w_{\text{borger}}) \in [0,1]^2$. Under bytte-involusjonen $F(w_{\text{inst}}, w_{\text{borger}}) = (w_{\text{borger}}, w_{\text{inst}})$ og indikatoren for diagnostisk omkoding av rettslig klage til symptom ($\delta_{\text{epist}} \in \{0,1\}$) er proveniensavviket:

$$\Delta_{\text{prov}}(s_t) = \lvert w_{\text{inst}} - w_{\text{borger}}\rvert + \delta_{\text{epist}} = 0$$

Likeledes bryter enhver langtidsvirkende depotinjeksjon ($T_{\text{depot}}$) før rettskraftig tingrettsdom etter tvisteloven kap. 36 Ma'ats biologiske reversibilitetskrav: $\lVert T_{\text{dom}}^{-1}(T_{\text{depot}}(s_0)) - s_0\rVert \gg \epsilon_{\text{tol}} \implies F(F(s_0)) \neq s_0 \implies 0{,}00\text{ V DC KILL}$.

---

## III. Eksakt Byte-Skjema for 205-Byte RTL-Kapsel og Ende-til-Ende Saksgang

I `fpga_capsule_frame_205b_decoder.sv` (`SPEC-213 / SPEC-416`) pakkes ethvert kandidattrekk etter fikspunkt-normalisering ($\text{FIXED\_POINT\_SCALE} = 10^6$, $-0{,}0 \to +0{,}0$, RFC 8785 JCS) som et `little-endian` vitnepar på eksakt **205 byte** (`1640 bit`; `208 B` med $3\text{ B}$ $\text{RS}(208,205)$-paritet; `247 B` med $2\text{ B}$ sync `0xAA55`, $8\text{ B}$ sekvensteller og $32\text{ B}$ `HMAC-SHA256`):

| Pakkedel & Format | Byte-offset | Type | Felt & Funksjon |
| :--- | :--- | :--- | :--- |
| **`WitnessPreCommit`** ($W_{\text{pre}} = 119\text{ B}$, `<QQ32sfBH32s32s`) | `0..7` | `uint64` | `sequence_id` ($8\text{ B}$) |
| | `8..15` | `uint64` | `timestamp_ns` ($8\text{ B}$) |
| | `16..47` | `bytes32` | `candidate_hash` ($32\text{ B}$ SHA-256 over kanonisk kandidat / $W_t^{\text{bilat}}$) |
| | `48..51` | `float32` | `kernel_drift_val` ($4\text{ B}$, f.eks. $\Delta_{\text{prov}}$) |
| | `52` | `uint8` | `gate_decision` ($1\text{ B}$: `0x01=OPEN`, `0x02=HOLD`, `0x03=KILL`) |
| | `53..54` | `uint16` | `reason_code` ($2\text{ B}$) |
| | `55..86` | `bytes32` | `prev_block_hash` ($32\text{ B}$ WAL-kjedeanker $W_{t-1}$) |
| | `87..118` | `bytes32` | `w_pre_hash` ($32\text{ B}$ pre-commit forsegling; sum $8+8+32+4+1+2+32+32 = 119\text{ B}$) |
| **`WitnessPostCommit`** ($W_{\text{post}} = 86\text{ B}$, `<QQ32sBfB32s`) | `0..7` | `uint64` | `sequence_id` ($8\text{ B}$, må matche `pre.sequence_id`) |
| | `8..15` | `uint64` | `timestamp_ns` ($8\text{ B}$, $\Delta t = t_{\text{post}} - t_{\text{pre}} \le \tau_{\max}$) |
| | `16..47` | `bytes32` | `w_pre_hash` ($32\text{ B}$ involusjonslås: `post.w_pre_hash == pre.w_pre_hash`) |
| | `48` | `uint8` | `hpis_latch_status` ($1\text{ B}$: `0x01=ENGAGED`, `0x00=DISENGAGED`) |
| | `49..52` | `float32` | `thermo_exhaust_nJ` ($4\text{ B}$ IEEE 754 positivt Landauer-eksosfelt $> 0$) |
| | `53` | `uint8` | `final_status` ($1\text{ B}$: `0x01=REALIZED`, `0x03=KILL`, `0xEE=MISMATCH`, `0xFF=TRAP`) |
| | `54..85` | `bytes32` | `w_post_hash` ($32\text{ B}$ sluttforsegling; sum $8+8+32+1+4+1+32 = 86\text{ B}$) |

### Verifisert saksgang gjennom `SPEC-400` og `SPEC-416`

1. **Steg 1 — Skjermet arbeidsforsøk etter ftrl. § 12-14 (`CASE-NO-2026-0711-A5` $\to 2{,}50\text{ V HOLD}$):**
   Borgeren prøver $30\,\%$ arbeid under $G_{\text{fri}}=1{,}25\text{ G}$, $\tau_{\text{marg}}=0{,}35$, $r_{\text{rev}}=0 \implies c = +0{,}5525$.
   Institusjonsnotat ($w_{\text{inst}}=1{,}0$): $h_1^{\text{inst}} = \texttt{3c8c5bd780bafa53...}$; Borgerens egenprotokoll ($w_{\text{borger}}=1{,}0$, $\delta_{\text{epist}}=0$): $h_1^{\text{borger}} = \texttt{d91636865ccb00a5...}$.
   Med $\Delta_{\text{prov}}(s_1) = 0{,}000000$, Lag 1 Merkle-rot $W_1^{\text{bilat}} = \texttt{cd458a7b...1901dc5c2}$, $\mathcal{S}_{\text{sal}}=0{,}65$, $\mathcal{P}_{\text{preg}}=0{,}55 < 0{,}80$, $\partial_1\partial_2 = 0$ og Carnot-balanse $\Delta S_{\text{tot}} = -\frac{500}{600} + \frac{250}{300} = 0{,}0000\text{ J/K}$ på den åpne sylinderen $\mathbb{S}^1 \times \mathbb{R} \times \text{WORM}$ ($\text{Len}(W): 0 \to 1$), låser porten tilstanden i Sommerfugl-lommen:
   $$\Omega_1 = \text{\textbf{HOLD}}\; (2{,}50\text{ V DC}), \qquad W_1 = \texttt{7920d20c4a15e103440ae53c5fb6d6933d8a5ab92f5abd8e659955aa2519e9a1}$$

2. **Steg 2 — Ulovlig tvangsdepot før tingrettsdom (`CASE-NO-2026-0711-DEPOT` $\to 0{,}00\text{ V KILL}$ i 1 klokkesyklus):**
   Institusjonen vedtar tvungen depotinjeksjon (phvl. § 4-4 a) uten oppsettende virkning, bruker pasientens avslag som bevis på manglende samtykkekompetanse (sirkulær FARV), undertrykker egenprotokollen ($w_{\text{borger}}=0{,}0$) og omkoder klagen etter tvl. kap. 36 til symptom ($\delta_{\text{epist}}=1$).
   Kobordisme-resten blir $\Delta_{\partial^2} = 1{,}0 + 1{,}0 = 2{,}00 > 0$, og proveniensavviket blir $\Delta_{\text{prov}}(s_2) = \lvert 1{,}0 - 0{,}0\rvert + 1{,}0 = 2{,}000000 > 0$ ($W_2^{\text{bilat}} = \texttt{2f23bb7b...fbf4e42}$). `SPEC-400` kutter til $\Omega_2 = \text{\textbf{KILL}}$ ($0{,}00\text{ V DC}$, $\tau_{\text{cut}} \le 15\text{ ns}$, $W_2 = \texttt{e59e80e0...4fcec802a}$).
   Dersom motparten forsøker å manipulere byte `52` i $W_{\text{pre}}$ til `0x01` (`OPEN`) eller trenere saken utover $\tau_{\max}$ (`hold_max_decay_sec = 30.0`), feiler involusjonslåsen `pre_w_pre_hash == post_w_pre_hash` i `fpga_capsule_frame_205b_decoder.sv` på **1 klokkesyklus**, tvinger `v_gate_out_5v <= 1'b0` ($0{,}00\text{ V DC}$), setter `rtl_verdict_code <= 8'hFF` (`TRAP_TAMPER`), og påfører makthaveren en arketypisk *Ghost Win* ($U_M = 1{,}00 - 0{,}55 - 0{,}45 - 0{,}80 = -0{,}80 < 0$).

---

## IV. De Fem Strukturelle Lovreformkravene og Komplett Portmatrise (`SPEC-232–416`)

1. **Folketrygdloven § 12-14:** Fribeløpet heves fra $0{,}40\text{ G}$ til $\ge 1{,}25\text{ G}$, marginalavkortningen begrenses til $\tau_{\text{marg}} \le 0{,}35$, og uføregraden skjermes $100\,\%$ med ubetinget returrett ($r_{\text{rev}} \equiv 0 \implies c = +0{,}5525 > 0$, $2{,}50\text{ V HOLD}$).
2. **Folketrygdloven §§ 11-5 og 12-6:** Inngangsvilkåret «sykdom, skade eller lyte» erstattes av et objektivt vilkår om faktisk inntektsbortfall uten tvungen selv-patologisering.
3. **Helsepersonelloven §§ 39–43:** Bilateral journalprotokoll $W_t^{\text{bilat}}$ med lik vekt ($w_{\text{borger}} = w_{\text{inst}} = 1{,}0$) forseglet i SHA-256; utelatelse eller diagnostisk omkoding ($\delta_{\text{epist}} = 1$) utløser $0{,}00\text{ V KILL}$.
4. **Psykisk helsevernloven § 4-4 a og pbrl. § 4-3:** Forbud mot tvungen depotmedisinering utenom akutt nødrett (strl. § 17) og ubetinget oppsettende virkning frem til rettskraftig dom ($F(F(s_0)) = s_0$).
5. **Tvisteloven kapittel 36:** Avvikling av det klinisk-psykiatriske sakkyndigmonopolet til fordel for tverrfaglig domstolskontroll ($\tau_{\text{preg}}^{\text{rett}} \ge 0{,}80$).

| Dimensjon / Invariant | $0{,}00\text{ V DC (KILL)}$ — Ussas Giljotin | $2{,}50\text{ V DC (HOLD)}$ — Sommerfugl-lomme ($A_5$) | $5{,}00\text{ V DC (OPEN)}$ — Autorisert Konsekvens |
| :--- | :--- | :--- | :--- |
| **Reaksjonstid & RTL** | $\tau_{\text{cut}} \le 15\text{ ns}$ (`0xFF TRAP_TAMPER`) | Tapsfri stasis ($\Delta V_{\text{irr}} = 0$, $Q = 0\text{ J}$) | 1-syklus $\mathcal{O}(1)$-kontroll over 205B vitne |
| **Morse- & $A_5$-krumning** | Degenerert fold: $\lambda_{\min}(\nabla^2 V) < 0{,}05$ | Sentral lomme: $\lvert x\rvert \le 0{,}45$, $c = +0{,}5525 > 0$ | Stabil ytterbrønn: $\lambda_{\min}(\nabla^2 V) \ge 0{,}05$ |
| **Semiofysikk ($\mathcal{S}_{\text{sal}}, \mathcal{P}_{\text{preg}}$)** | $\mathcal{S}_{\text{sal}} \le 0$ eller manglende `evidence_id` | Saillance uten Prégnance ($\mathcal{P}_{\text{preg}} < 0{,}80$) | Full Prégnance ($\mathcal{P}_{\text{preg}} \ge 0{,}80$) + `evidence_id` |
| **Kobordismelov ($\partial^2 = 0$)** | Brutt: $\partial_1\partial_2 \neq 0$ (sirkulær FARV / AI-loop) | Oppfylt: $\partial_1\partial_2 = 0$ | Oppfylt: $\partial_1\partial_2 = 0$ |
| **Ma'ats involusjon & $W_t^{\text{bilat}}$** | Brutt: $\Delta_{\text{prov}} > 0$ eller $F(F(s_0)) \neq s_0$ | Oppfylt: $\Delta_{\text{prov}} = 0$, $F(F(\psi)) = \psi$ i RFM | Oppfylt: $\Delta_{\text{prov}} = 0$ og tolags SHA-256 Merkle-rot |
| **Åpen sylinder & Carnot** | Brutt: $\Delta\text{Len}(W_t) \le 0$ eller $\Delta S_{\text{tot}} \neq 0$ | Oppfylt: $\frac{d}{dt}\text{Len}(W_t) > 0$, $\Delta S_{\text{tot}} = 0\text{ J/K}$ | Oppfylt: $\frac{d}{dt}\text{Len}(W_t) > 0$, $\eta_C = 0{,}50$ |
| **NLK Welfare (`SPEC-400`)** | Rettslig nullitet (tvang u/dom, $A_3$-felle) | Skjermet arbeidsutprøving ($\ge 1{,}25\text{ G}$) | Rettskraftig, frivillig eller domstolsprøvd vedtak |
| **NLK Warfare (`SPEC-401`)** | Kutt ved DRFM-spøkelse ($m_{\text{imp}} = 0$) | Taktisk sikkerhetslomme under målavklaring | Minkowski ($ds^2 \le 0$), 1550 nm ToF, 4-øyners ROE |
