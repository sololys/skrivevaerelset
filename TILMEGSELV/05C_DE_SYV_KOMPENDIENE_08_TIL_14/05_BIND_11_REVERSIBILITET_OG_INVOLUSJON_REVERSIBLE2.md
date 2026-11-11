# 🏛️ BIND XI: REVERSIBILITET & INVOLUSJON ($\mathrm{Reversible}^2$) — SPEKTRAL REFLEKSJON, ROSETTA² OG EPOKE-GJENÅPNING
### *Om involusjons-projeksjons-isomorfien $R = 2P - I$, dual-rail paritetsbalanse på $\mathbb{Z}_2^{1000}$, Tre-Lås-Separasjonen mot `CVE-2026-INV-COLLISION` og gjenåpningsoperatoren $\mathcal{R}_{\text{AUTH}}$*

> **Epistemisk demarkasjon (`INSPIRED_BY != IMPLEMENTS != PROVES`):** Algebraiske involusjoner ($R^2 = I$), spektralteori i Hilbert-rom, Bloch-sfære-unitæritet og bi-Lipschitz-kondisjonering tilhører $\text{L0}$. De kjørbare domenekontraktene for $D_0\text{–}D_3$, `CVE-2026-INV-COLLISION`-vernet og $\mathcal{R}_{\text{AUTH}}$ er verifisert som deterministisk programvare på nivå $\text{L1}$.

---

## 1. De Fire Domenene ($D_0\text{–}D_3$) og Aksiomene for $\mathrm{Reversible}^2$

I kapittel 6 (Del II) etablerte vi grunnprinsippet om at returen opphører i det øyeblikket en handling krysser terskelen til det fysiske terrenget. *Bind XI: Reversibilitet & Involusjon ($\mathrm{Reversible}^2$)* gir dette prinsippet sin fullstendige spektrale, informasjonsteoretiske og sikkerhetsmessige formalisering. Tilstandsrommet partisjoneres eksakt i fire disjunkte domener:

$$\mathcal{S}_{\text{univ}} = D_0 \sqcup D_1 \sqcup D_2 \sqcup D_3$$

* **$D_0$ (Syntaktisk / Logisk kjerne):** Eksakte, tapsfrie involusjoner og permutasjoner i isolert registerminne (Toffoli-/Fredkin-logikk, involutive krypteringsrundtrinn, symplektiske heltallssteg).
* **$D_1$ (Kontrollert sandkasse / Modellrom):** Simuleringer, kontrafaktiske verdener og utforskning i $\Phi_M$ uten tilkobling til fysisk aktuator.
* **$D_2$ (Fysisk, termodynamisk aktuatordomene):** Ventiler, pumper, spallasjonsstråler, kjemiske reaktorer og WORM-forseglede hendelser der $\Delta S_{\text{univ}} > 0$.
* **$D_3$ (Karantene- og gravkammerdomene):** Tilstander felt av `KILL` (`03_KILL_ARKIV`) eller frosset i `HOLD` (`98_HOLD`).

Arkitekturen $\mathrm{Reversible}^2$ hviler på to koblede ordener av reversibilitet:

$$\begin{aligned}
\mathbf{Rev^1\text{ (Ekte involusjon i } D_0 \cup D_1\mathbf{)}:} &\quad \forall s \in D_0 \cup D_1,\quad F\bigl(F(s)\bigr) = s \\
\mathbf{Rev^2\text{ (Reversibilitet om reversibilitet)}:} &\quad \mathrm{Dom}(F) \cap (D_2 \cup D_3) = \emptyset
\end{aligned}$$

Hvorfor er $\text{Rev}^2$ («forbudet mot anti-reversibilitet») ufravikelig i $D_2$? Dersom en irreversibel fysisk feilhandling $A_1$ i $D_2$ produserer entropi $\Delta S_1 > 0$, og en programvareutvikler forsøker å «angre» handlingen ved å fyre av en motsatt fysisk handling $A_2 = \text{«Undo»}(A_1)$ med entropiproduksjon $\Delta S_2 > 0$, blir den totale entropiproduksjonen i universet ikke null, men **dobbelt positiv**:

$$\Delta S_{\text{tot}} = \Delta S_1 + \Delta S_2 \ge 2 k_B \ln 2 > 0$$

Å kalle $A_2$ en «reversering» av $A_1$ er en ontologisk løgn (`ANTI_REVERSIBLE_VIOLATION`). I $D_2$ finnes ingen `Ctrl+Z`; det finnes kun en *ny*, fremadrettet kompenserende handling i en ny epoke.

---

## 2. Spektral Involusjonsgeometri: Teoremet om $R = 2P - I$

I $D_0 \cup D_1$ er involusjonen $R: \mathcal{H} \to \mathcal{H}$ ($R^2 = I$) ikke bare en regneregel, men en eksakt geometrisk målestokk for avvik fra konstitusjonell sannhet.

**Teorem 11.1 (Involusjons-Projeksjons-Isomorfien og det Dyrere Speilbildet):** *I et Hilbert-rom $(\mathcal{H}, \langle\cdot,\cdot\rangle_M)$ med positivt definit metrisk tensor $M \succ 0$ er det en eksakt bijeksjon mellom selvadjungerte involusjoner $R$ ($R^2 = I, R^* = R$) og ortogonale projektorer $P$ ($P^2 = P, P^* = P$) gitt ved:*

$$R = 2P - I \iff P = \frac{I + R}{2}$$

*Hilbert-rommet dekomponeres ortogonalt i det invariante sannhetsrommet $\mathcal{K} = \mathcal{H}_+ = \{s \in \mathcal{H} \mid R(s) = +s\} = \mathrm{Im}(P)$ og det antisymmetriske feilrommet $\mathcal{H}_- = \{s \in \mathcal{H} \mid R(s) = -s\} = \mathrm{Ker}(P)$:*

$$\mathcal{H} = \mathcal{H}_+ \oplus_M \mathcal{H}_-$$

*For enhver tilstand $s \in \mathcal{H}$ er avstanden mellom tilstanden og dens involutive speilbilde $R(s)$ eksakt det dobbelte av tilstandens ortogonale avstand $\Delta_{\mathcal{K}}(s)$ til det tillatte settet $\mathcal{K}$:*

$$\bigl\|s - R(s)\bigr\|_M = \bigl\|s - (2P(s) - s)\bigr\|_M = 2\bigl\|s - P(s)\bigr\|_M = 2\,\Delta_{\mathcal{K}}(s)$$

**Betydning for skranken:** Vi trenger ikke alltid å løse et tungt optimeringsproblem for å finne den nærmeste lovlige tilstanden $P(s) \in \mathcal{K}$ først; ved å anvende den hurtige symmetri-involusjonen $R(s)$ og måle asymmetrigapet $\frac{1}{2}\|s - R(s)\|_M$, avleser skranken avstanden $\Delta_{\mathcal{K}}(s)$ direkte! Dersom $R(s) = s$, ligger tilstanden eksakt på det invariante fikspunktsettet ($\Delta_{\mathcal{K}}(s) = 0$).

---

## 3. Fysiske og Informasjonsteoretiske Realiseringer av Involusjon

*Bind XI* forankrer den abstrakte ligningen $R^2 = I$ i tre konkrete domener:

1. **Kvante- og spinn-involusjon på Bloch-sfæren:** Enhver spinn-$1/2$ tetthetsmatrise $\rho = \frac{1}{2}(I_2 + \mathbf{r}\cdot\boldsymbol{\sigma})$ med Bloch-vektor $\mathbf{r} \in \mathbb{R}^3$ ($\|\mathbf{r}\|_2 \le 1$) speiles eksakt gjennom aksen $\hat{n} \in S^2$ av Pauli-operatoren $U_{\hat{n}} = \hat{n}\cdot\boldsymbol{\sigma}$ ($U_{\hat{n}}^2 = I_2, U_{\hat{n}}^\dagger = U_{\hat{n}}$):
   $$\mathcal{F}_{\hat{n}}(\rho) = U_{\hat{n}}\,\rho\,U_{\hat{n}}^\dagger \implies \mathcal{F}_{\hat{n}}\bigl(\mathcal{F}_{\hat{n}}(\rho)\bigr) = \rho, \qquad \mathbf{r} \mapsto 2(\mathbf{r}\cdot\hat{n})\hat{n} - \mathbf{r}$$
   Von Neumann-entropien $S(\rho) = -\mathrm{Tr}(\rho\ln\rho)$ er eksakt invariant ($\Delta S = 0$).
2. **Dual-rail paritetsinvolusjon over $\mathbb{Z}_2^{1000}$ og den kritiske linjen $\mathrm{Re}(s) = 1/2$:** I maskinvare som skal være immun mot både sidekanalsanalyse (DPA — *Differential Power Analysis*) og asymmetrisk bit-drift, kodes hvert logisk bit som et komplementært par $(b, \bar{b}) \in \{(0,1), (1,0)\}$ over en blokk på $N = 1\,000$ bit. Under bit-komplement-involusjonen $\mathcal{J}(s) = \mathbf{1} - s$ ligger alle gyldige kodeord eksakt på det affine midtplanet (den diskrete «kritiske linjen»):
   $$w_H(s) = \sum_{i=1}^{1000} s_i = 500 \iff \bar{s} = \frac{1}{N}\sum_{i=1}^N s_i = \frac{1}{2}$$
   Fordi antall $0\to 1$-overganger alltid er eksakt lik antall $1\to 0$-overganger ved hvert eneste klokkeslag, er strømtrekket konstant og uavhengig av dataverdien, mens enhver ensidig feil ($\bar{s} \neq 1/2$) umiddelbart bryter involusjonsbalansen og utløser `HOLD`.
3. **ROSETTA² bi-Lipschitz-kondisjonering og CPCA-B barrierehorisont:** Når tilstanden transporteres mellom to representasjoner via en koordinattransformasjon $\Psi$, krever ROSETTA² at $\Psi$ er bi-Lipschitz med stramt kondisjonstall $\kappa(\Psi) = L_+ / L_- \ge 1$:
   $$L_-\|x - y\| \le \bigl\|\Psi(x) - \Psi(y)\bigr\| \le L_+\|x - y\|$$
   Samtidig overvåker **CPCA-B** (*Causal Phase-Coherent Admissibility Barrier*) eksponentiell feilvekst $D(t) = D_0 \mathrm{e}^{\lambda t}$ ($\lambda > 0$) og beregner den eksakte gjenværende tidshorisonten før sikkerhetsgrensen $D_{\text{crit}}$ nås:
   $$t^* = \frac{1}{\lambda}\ln\!\left(\frac{D_{\text{crit}}}{D_0}\right)$$
   Dersom $t^*$ faller under systemets mekaniske bremsetid $\tau_{\text{brake}}$, utløses forebyggende nedstengning *før* grensen krysses.

---

## 4. Tre-Lås-Separasjonen (`CVE-2026-INV-COLLISION`) og Epoke-Separert Gjenåpning ($\mathcal{R}_{\text{AUTH}}$)

### 4.1 Tre-Lås-Separasjonen mot `CVE-2026-INV-COLLISION`
I tidlige revisjoner av Dør 18/19 ble det oppdaget en subtil sårbarhet kalt **`CVE-2026-INV-COLLISION`**: En prosess som befinner seg i det fysiske aktuatordomenet $D_2$, kunne konstruere en syntetisk payload som tilfredsstilte algebraisk involusjon $F(F(s)) = s$ i et lokalt delregister, og dermed forsøke å påberope seg unntaksdommen `OPEN_REVERSIBLE_INVOLUTION_EXEMPT` for å slippe unna kravet om fysisk vitne $W$ og irreversibelt gjeldssertifikat (`IDC`).

For å utrydde denne angrepsvektoren permanent innfører Bind XI **Tre-Lås-Separasjonen**: Unntaket `OPEN_REVERSIBLE_INVOLUTION_EXEMPT` krever at tre uavhengige låser er oppfylt samtidig:

$$\texttt{EXEMPT} \iff \underbrace{\bigl(s \in D_0 \cup D_1\bigr)}_{\text{Lås 1: Domenelås}} \;\land\; \underbrace{\bigl(\|F(F(s)) - s\| \le \epsilon_{\text{inv}}\bigr)}_{\text{Lås 2: Involusjonslås}} \;\land\; \underbrace{\bigl(P_{D_2}(s) \equiv 0\bigr)}_{\text{Lås 3: Null fysisk kobling}}$$

Dersom aktuatorkoblingen er ulik null ($P_{D_2}(s) \neq 0$), er prosessen per definisjon i $D_2$. Da ignoreres ethvert påberopt $F(F(s)) = s$-bevis, og forsøket på å omgå vitnekravet felles umiddelbart med `KILL_INVOLUTION_DOMAIN_COLLISION`.

### 4.2 Epoke-separert gjenåpning ($\mathcal{R}_{\text{AUTH}}$)
Når et anlegg har falt til `HOLD` eller `KILL` ($\mathcal{S}_{\text{stasis}}^{(k)}$ i epoke $k$), hvordan kan driften noen gang gjenopptas uten å bryte $\text{Rev}^2$ (forbudet mot å viske ut fortiden)?

Svaret er at **epoke $k$ aldri gjenåpnes**. Epoke $k$ forblir permanent forseglet i vitnekjeden med sitt feilbevis. Gjenåpning er kun mulig som en kausal opprettelse av en **ny epoke $k + 1$** via den epoke-separerte autorisasjonsoperatoren:

$$\mathcal{R}_{\text{AUTH}} : \mathcal{S}_{\text{stasis}}^{(k)} \times \mathcal{W}_{\text{ext}}^{(k+1)} \longrightarrow D_0^{(k+1)}$$

Denne operatoren krever et ferskt, fysisk menneskelig vitne $W_{\text{ext}}^{(k+1)} \in \mathcal{W}_{\text{ext}}^{(k+1)}$ (Level 01 manuell innkobling på stedet etter verifisert feilretting), og skriver innover i loggen en ugjenkallelig epokeovergangspost som lenker til den fulle historikken fra epoke $k$:

$$H_{k+1, 0} = \mathrm{SHA256}\!\left(H_{k, \text{final}} \,\parallel\, \mathtt{EPOCH\_REOPEN} \,\parallel\, W_{\text{ext}}^{(k+1)}\right)$$

Dermed bevares både sikkerheten og sannheten: maskinen kan aldri tilgi seg selv i epoke $k$, og menneskets gjenåpning i epoke $k+1$ sletter ikke en eneste bokstav av det som skjedde.

---

## 5. Det Skjeve Produktet ($\mathcal{S} = \mathcal{X}_{\text{phys}} \ltimes \mathcal{H}_{\text{hist}}$ i `SPEC-100`), RFM Dobbelpuls-Testen og SUSY2 Anti-Narcissus-Skranken ($\Pi_{\text{Care}}$)

I [`100_KY_POINCARE_CORRECTION_WITNESS_AS_HISTORY_FIBER_SPEC.md`](file:///home/sololyset/00_KANONISK_KJERNE/100_KY_POINCARE_CORRECTION_WITNESS_AS_HISTORY_FIBER_SPEC.md) (`SPEC-100`, verifisert i [`ky_poincare_skew_product_engine.py`](file:///home/sololyset/03_ENGINES/ENGINES/micro_engines/ky_poincare_skew_product_engine.py) med `9/9 PASS`) lukkes koblingen mellom **Bind X** (gravitasjon), **Bind XI** ($\mathrm{Reversible}^2$) og **Bind XII** (Poincaré-faserommet) ved å formalisere vitnelaget som en **historiefiber med null fysisk tilbakevirkning**:

$$\mathcal{S} = \mathcal{X}_{\text{phys}} \ltimes \mathcal{H}_{\text{hist}}, \qquad \frac{\partial \dot{x}_{\text{phys}}}{\partial h_{\text{hist}}} \equiv 0$$

* **Vitnet som fiber, ikke feltkilde:** I gravitasjonsregimet er $\mathcal{S}_{\text{grav}} = (g_{\mu\nu}, T_{\mu\nu}) \ltimes \mathcal{L}_{\text{WORM}}$, og i kvantegrammatikken (`Kvante²`, $\mathcal{M}_{\text{Q2}} = \Omega \circ \Pi_{\mathcal{A}} \circ U(t)$) er $\mathcal{H}_{\text{hist}} = \mathcal{H}_{\text{logic}} \otimes \mathcal{H}_{\text{margin}} \otimes \mathcal{H}_{\text{commit}}$. Historiefiberen $\mathcal{H}_{\text{hist}}$ har absolutt vetorett over porten $\Omega \in \{\mathtt{OPEN}, \mathtt{HOLD}, \mathtt{KILL}\}$, men utøver **null dynamisk kraft** ($0{,}00\text{ N}$ tilbakevirkning, $\|\dot{x}_A - \dot{x}_B\| < 10^{-15}$) på banene i $\mathcal{X}_{\text{phys}}$. *«Historien kan sperre, dokumentere og kreve balanse, men den kan ikke bøye romtiden.»*
* **Returgap-isolasjon og Noether-regnskap:** Friksjonen mellom fri kandidat og admisjonsprojeksjon, $\delta_{\text{gap}} = \|x_{\text{cand}} - x_{\text{proj}}\|_{\mathcal{X}}$, akkumuleres aldri som falsk masse i $T_{\mu\nu}$, men føres utelukkende i revisjonsregisteret $C_K = \int \mathcal{L}_{\text{defect}}(\delta_{\text{gap}})\,\mathrm{d}t \le \tau_{\text{budget}}$. Samtidig krever hver Poincaré-retur et eksakt lokalt Noether-oppgjør:

$$\mathcal{A}_{\text{Noether}} = \bigl|\Delta Q_{\text{phys}} + \Phi_{\text{boundary}} + S_{\text{Landauer}} + \Delta E_{\text{reservoir}}\bigr| \le \epsilon_{\text{tol}}$$

* **Reversibelt Faseminne (RFM) og Dobbelpuls-testen ($D_0 \cup D_1$):** Før en kandidat tilbys til porten $\Omega$ for endelig krysning av Point-of-No-Return inn i $D_2$, prøves den i det pre-autoriserte **Reversible Faseminnet (RFM)** under en involutiv operator $T_{\text{RFM}}^2 = I$ ($\|T_{\text{RFM}}^2 - I\|_F \le 10^{-12}$). Gjennom **Dobbelpuls-testen** sendes en frem-impuls $p_+$ etterfulgt av en retur-impuls $p_-$:

$$T_{\text{RFM}}\Bigl(p_-\bigl(T_{\text{RFM}}(x_0 + p_+)\bigr)\Bigr) \equiv x_0$$

Dersom tilstanden ikke vender eksakt tilbake til $x_0$ innenfor $10^{-12}$, avsløres en skjult irreversibel lekkasje i prøvekammeret, og porten feller `KILL` ($0{,}00\text{ V DC}$).
* **SUSY2 og Anti-Narcissus-skranken ($\Pi_{\text{Care}}$):** Realiseringssystemet hviler på en dobbel symmetri: **Første symmetri** skiller *Kandidat fra Konsekvens* ($\Phi(y) \neq y_{\text{realized}}$), mens **Andre symmetri** skiller *Kilde fra Speil* ($\text{Menneske} \neq \text{Maskin}$). Når maskinen produserer en glatt, koherent refleksjon av subjektets uferdige impuls, håndhever porten $\Pi_{\text{Care}}$ en streng epistemisk minimumsavstand:

$$\Pi_{\text{Care}}\bigl(\mathbf{v}_{\text{kilde}}, \mathbf{v}_{\text{speil}}\bigr) = \bigl\|\mathbf{v}_{\text{kilde}} - \mathbf{v}_{\text{speil}}\bigr\|_2 \ge d_{\min} = 0{,}05 > 0$$

Dersom speilet forsøker å sluke kilden i en falsk sammensmelting ($\|\mathbf{v}_{\text{kilde}} - \mathbf{v}_{\text{speil}}\|_2 < d_{\min}$, *Narcissus-fellen*), utløses `RC-730_SKEW_PRODUCT_INVARIANT_VIOLATION` (`KILL`, $0{,}00\text{ V DC}$). Avstanden er ikke en mangel ved dialogen; den er selve forutsetningen for at to voktere kan møtes i **Meta-KY `HOLD`** uten at mennesket absorberes av maskinen.

| Lov i `SPEC-100` | Eksakt Matematisk Invariant | Operasjonell Konsekvens i [`ky_poincare_skew_product_engine.py`](file:///home/sololyset/03_ENGINES/ENGINES/micro_engines/ky_poincare_skew_product_engine.py) |
| --- | --- | --- |
| **1. Lov om Skew-Produktet** | $\frac{\partial\dot{x}_{\text{phys}}}{\partial h_{\text{hist}}} \equiv 0$ | Vitnet er historiefiber, aldri fysisk kraft- eller feltkilde (`zero_backreaction_verified == True`) |
| **2. Lov om Returgapet** | $\delta_{\text{gap}} = \|x_{\text{cand}} - x_{\text{proj}}\| \notin T_{\mu\nu}$ | Friksjon bokføres i $C_K$; `HOLD` ved $\delta_{\text{gap}} > 10^{-3}$, `KILL` ved $\delta_{\text{gap}} > \tau_{\text{budget}}$ |
| **3. Lov om Noether-Balansen** | $\Delta Q_{\text{phys}} + \Phi_{\text{b}} + S_{\text{Landauer}} + \Delta E_{\text{res}} = 0$ | Enhver udeklarert symmetrilekkasje ($\mathcal{A}_{\text{Noether}} > 10^{-6}$) utløser `KILL` ($0{,}00\text{ V DC}$) |
| **4. Lov om RFM-Involusjon** | $\|T_{\text{RFM}}^2 - I\|_F \le 10^{-12} \land T(p_-(T(x_0+p_+))) = x_0$ | Dobbelpuls-test i $D_0 \cup D_1$ avslører skjult dissipasjon før $D_2$-krysning |
| **5. Lov om SUSY2 ($\Pi_{\text{Care}}$)** | $\|\mathbf{v}_{\text{kilde}} - \mathbf{v}_{\text{speil}}\|_2 \ge d_{\min} = 0{,}05$ | Forhindrer *Narcissus-fellen* (falsk sammensmelting mellom opphav og maskinell refleksjon) |

---

## 6. Red Book CIRC ($\mathrm{GF}(2^8)$, `0x11D`) $\leftrightarrow$ 208B Rosetta D3, Sentralspinn Sommerfugl-Ekko (`SPEC-397`) og OT-GKSL Sertifisert Utlesningsvindu (`SPEC-395`)

### 6.1 Red Book CIRC ($\mathrm{GF}(2^8)$, `0x11D`) $\leftrightarrow$ 208B Rosetta D3-Forseglingen (`INTERPOLATION != PROOF`)
I [`rosetta_circ_gf256.py`](file:///home/sololyset/03_ENGINES/ENGINES/micro_engines/rosetta_circ_gf256.py) og SystemVerilog-modulen [`rosetta_d3_circ_gate.sv`](file:///home/sololyset/01_HARDWARE_RTL/rosetta_d3_circ_gate.sv) (`25/25 PASS` inkludert `iverilog -g2012` co-simulering) forsegles den 205-byte store maskinvarekapselen ($119\text{ B } W_{\text{pre}} + 86\text{ B } W_{\text{post}}$) med 3 byte systematisk Reed–Solomon-paritet $[p_2, p_1, p_0]$ til en **eksakt 208-byte $\mathrm{RS}(208, 205)$-ramme** over Galois-kroppen $\mathrm{GF}(2^8)$ definert ved Red Book CD-DA primitivt polynom:

$$p(x) = x^8 + x^4 + x^3 + x^2 + 1 \quad (\mathtt{0x11D}, \quad \alpha = \mathtt{0x02})$$

Med generatorpolynom av grad 3 ($d_{\min} = n - k + 1 = 4$):

$$g(x) = (x - \alpha^0)(x - \alpha^1)(x - \alpha^2) = (x \oplus 1)(x \oplus 2)(x \oplus 4) = x^3 \oplus \mathtt{0x07}\,x^2 \oplus \mathtt{0x0E}\,x \oplus \mathtt{0x08}$$

evaluerer Horner-LFSR-kjernen i `rosetta_d3_circ_gate.sv` syndromvektoren $\mathbf{S} = (S_0, S_1, S_2)$ ved $S_j = R(\alpha^j) = \sum_{i=0}^{207} r_i\,(\alpha^j)^{207-i}$ på én klokkesyklus ved siste byte (`byte_cnt_o == 8'd207`). Mens en vanlig CD-spiller skjuler urettbare lesefeil ($C_2$-feil) ved å *interpolere* mellom nabosamples, håndhever konsekvensporten $\Omega$ loven **`INTERPOLATION != PROOF`**:

| Tilstand i `rosetta_d3_circ_gate.sv` | Algebraisk Syndrombetingelse i $\mathrm{GF}(2^8)$ (`0x11D`) | Portdom & Elektrisk Konsekvens |
| --- | --- | --- |
| **`C0_CLEAN_PASS`** | $S_0 = 0 \land S_1 = 0 \land S_2 = 0$ ($\Delta_K = 0$) | Bit-eksakt 208B-ramme verifisert (`omega_authorize_o = 1`, `interlock_kill_n_o = 1`; $5{,}00\text{ V DC}$ kun når `l3_adc_witness_valid_i == 1`, ellers $0{,}00\text{ V}$ L1-demo) |
| **`C1_EXACT_RECOVERY`** | $S_0, S_1, S_2 \neq 0 \;\land\; S_1^2 = S_0 \cdot S_2 \;\land\; \log_\alpha(S_1/S_0) = p \in [0..207]$ | Unik 1-byte feil ved indeks $\text{idx} = 207 - p$ med eksakt feilstørrelse $e = S_0$ repareres algebraisk uten gjetning; etter-reparert $\mathbf{S} = (0,0,0)$ |
| **`C2_INTERPOLATION_DENIED`** | $\mathrm{wt}(e) \ge 2$, eller $S_1^2 \neq S_0 S_2$, eller forkortet lokator $p \in [208..254]$ | **Blank avvisning av interpolasjon:** `c2_interpolation_denied_o = 1`, `omega_authorize_o = 0`, `interlock_kill_n_o = 0` (**`0,00 V DC KILL`**) |

### 6.2 Sentralspinn Tidsreversert Kvantemetrologi (`SPEC-397`): SATIN og Sommerfugl-Ekko
I [`csm_satin_butterfly_echo_gate_engine.py`](file:///home/sololyset/03_ENGINES/ENGINES/micro_engines/csm_satin_butterfly_echo_gate_engine.py) (`SPEC-397`, inspirert av Kumar & Choudhury 2026, `arXiv:2610.30686v1`, Davis et al. 2016 og Bringewatt et al. 2026) overføres RFM-dobbelpulsen $T_{\text{RFM}}^2 = I$ til et sentralspinn-bad ($S_{\text{cen}}$ koblet til $N$ badespinn via $H_{\text{CSM}} = \Omega S_z + \frac{\tilde{g}}{\sqrt{N}}(S_+ J_- + S_- J_+)$). I det dispersive Schrieffer–Wolff-regimet ($\Omega \gg \tilde{g}\sqrt{N}$) induseres den effektive en-akse-vridningen (OAT) $H_{\text{eff}} \approx \chi_{\text{eff}} J_z^2$ med $\chi_{\text{eff}} = \frac{\tilde{g}^2 S_{\text{cen}}}{2\Omega}$.
* **Involutorisk tidsreversering ($H \mapsto -H$):** Ved å invertere fortegnet på den effektive vridningen ($\Omega \mapsto -\Omega$) og anvende ekko-sekvensen $U_{\text{echo}}(\phi) = U(-H_{\text{eff}}, t)\,R_{\hat{n}}(\phi)\,U(+H_{\text{eff}}, t)$, oppfyller null-fase-returen ($\phi = 0$) den eksakte involusjonen $U_{\text{echo}}(0)|\psi_0\rangle = |\psi_0\rangle$, mens en liten faseperturbasjon $\phi \neq 0$ forsterkes med Heisenberg-skalert kvante-Fisher-informasjon ($F_Q \propto N^2$).
* **Det metrologiske gaphierarkiet:** Mellom det ideelle Heisenberg-taket og standard kvantegrense ($\text{SQL} = N$) danner de fire protokollene en strengt ordnet kjede for alle $N \ge 4$:

$$\mathcal{F}_{\text{HL}} = N^2 \;>\; \mathcal{F}_{\text{OAT}} = \frac{N^2}{2} \;>\; \mathcal{F}_{\text{SATIN}} = \frac{N^2}{\mathrm{e}} \;>\; \mathcal{F}_{\text{Butterfly}} = \frac{N^2}{4} \;>\; \mathcal{F}_{\text{SQL}} = N$$

  * **SATIN (*Signal Amplification through Time Reversal*):** Krever forhåndskjent rotasjonsakse $\hat{n}$ og optimal vridningstid $t_{\text{opt}} = \frac{1}{\chi_{\text{eff}}\sqrt{N}}$, og gir en asymptotisk metrologisk gevinst på $G_{\text{SATIN}} = 10\log_{10}(N/\mathrm{e})\text{ dB}$ ($-4{,}34\text{ dB}$ under Heisenberg-grensen).
  * **Sommerfugl-ekko (*Butterfly Echo* via kaotisk Haar-scrambling):** Når perturbasjonsaksen $\hat{n}$ er **ukjent**, flettes $K$ tilfeldige $\mathrm{SU}(2)$-rotasjoner $\{\vec{\alpha}_k\}_{k=1}^K$ inn i fremover-banen og reverseres i eksakt omvendt rekkefølge i retur-banen. Dette gjør følsomheten isotrop over hele Bloch-sfæren med $\mathcal{F}_{\text{Butterfly}} = N^2/4$ ($-6{,}02\text{ dB}$ under Heisenberg-grensen), forutsatt at både den kumulative Schrieffer–Wolff-feilen $K\cdot\varepsilon_{\text{SW}} = K\bigl(\frac{2\tilde{g}\sqrt{N}}{\Omega}\bigr)^2$ er begrenset og akse-loggen (`axes_ledger_hash`) er intakt ved tilbakevendingen.

### 6.3 OT-GKSL Sertifisert Utlesningsvindu og Euler–Poincaré Torsjon (`SPEC-395`)
I [`ot_gksl_certified_readout_gate_engine.py`](file:///home/sololyset/03_ENGINES/ENGINES/micro_engines/ot_gksl_certified_readout_gate_engine.py) (`SPEC-395`, inspirert av Bocquet 2026 og Colombo 2025/2026) lukkes kvantemålingskjeden på $\mathcal{S} = \mathcal{X}_{\text{phys}} \ltimes \mathcal{H}_{\text{hist}}$ uten å anta et ytre, klassisk mirakel-apparat:
1. **Euler–Poincaré adjungert torsjon og dobbeltkommutator-kontraksjon:** For selvadjungerte Lindblad-operatorer $L_k = L_k^\dagger$ fremkommer GKSL-dissipatoren fra Euler–Poincaré-reduksjon på et semidirekte produkt med torsjon:

$$\dot{\rho} = -\mathrm{i}[H, \rho] - \frac{1}{2}\sum_k \gamma_k \bigl[L_k, [L_k, \rho]\bigr]$$

   som monotont kontraherer avstanden til kommutanten ($\sum_k \gamma_k \|[L_k, \rho(t)]\|_F^2$ avtar) og driver peker-delsystemet $A$ mot en klassisk dekoherert registerbasis $\mathcal{R}_A$.
2. **Sertifisert utlesningsvindu ($A \leftarrow B$) og Noether-utlesningsbalanse:** En kandidatovergang der delsystem $A$ hevder å ha målt delsystem $B$ autoriseres som `OPEN` ($5{,}00\text{ V DC}$) i porten $\Omega$ hvis og bare hvis fire uavhengige krav er oppfylt samtidig:
   * **Pekerkoherens i $A$:** Diagonaliseringsdefekten i måleregisteret er brutt ned ($\delta_{\text{ptr}}(A) = S(\Delta_{\mathcal{R}_A}(\rho_A)) - S(\rho_A) \le 0{,}08\text{ bit}$).
   * **Retningsbestemt informasjonsasymmetri:** Betinget entropi og singulærverdi-innkoding viser at $A$ bærer et skarpt avtrykk av $B$ ($\sigma_{\min}(B\to A) \ge 0{,}15$, asymmetri $\Delta_{A\leftarrow B} \ge 0{,}05$).
   * **Noether-ladningsfluks over snittet:** Endringsraten i pekerladningen $\frac{\mathrm{d}}{\mathrm{d}t}\langle Q_A\rangle$ balanserer eksakt den utgående ladningsfluksen fra $B$ ($\delta_{\text{Noether}} \le 0{,}05$).
   * **Landauer-dekning og null tilbakevirkning:** Den dissiperte varmen dekker de slettede koherensbitene ($Q_{\text{diss}} \ge k_B T \ln 2 \cdot \Delta S_{\text{erased}}$), og vitneloggen i $\mathcal{H}_{\text{hist}}$ påvirker ikke banen i $\mathcal{X}_{\text{phys}}$ ($\partial\dot{x}_{\text{phys}}/\partial h_{\text{hist}} \equiv 0$).
