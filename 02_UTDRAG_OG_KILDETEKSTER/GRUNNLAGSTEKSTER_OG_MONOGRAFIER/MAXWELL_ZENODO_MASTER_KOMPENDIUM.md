# MAXWELL & DEMONENS PRIS // ELEKTRODYNAMISK ADMISJON OG DET SUBTRAKTIVE VAKUUMET
## En Monografi om Poynting-Dissipasjon, CFJ–Proca-Birefringens, Casimir-Kuttet og Termodynamisk Bæreevne

**Forfatter:** Marius Egerhei Torjusen (ORCID: `0009-0002-9877-5664`)  
**Arkitektonisk Komposisjon:** Skjevt Produkt ($\mathcal{S}_{\text{tot}} = \mathcal{Y} \times \mathcal{H}$) — Sammenhengende Norsk Hovedverk ($\mathcal{Y}$) + Lukket Teknisk Vitnevedlegg ($\mathcal{H}$)  
**Utgave:** `v3.0-MONOLITT` (0 % kryss-volum-duplisering mot Bind X)  
**Dato:** 23. oktober 2026  

---

## PROLOG // KOMPRIMERT KANONISK TRAKTAT

### I. Fra Fritt Bølgeskjema til Elektromagnetisk Realisering

> **Maxwells Admisjonslov:** En løsning $(\mathbf{E}, \mathbf{B})$ av de frie bølgeligningene i vakuum er kun et matematisk forslag. For at et elektromagnetisk felt skal utøve irreversibelt arbeid og bli til et fysisk faktum, må det passere gjennom den kompositte admisjonskjeden $\Pi_{\mathcal{A}} = \Pi_{\text{causal}} \circ \Pi_{\text{pos}} \circ \Pi_{\text{thermo}} \circ \Pi_{\text{Noether}} \circ \Pi_{\text{bound}}$ og betale Szilard–Landauer-prisen ($Q_{\text{demon}} \ge k_B T \ln 2$ per selektert bit).

I 1865 samlet James Clerk Maxwell elektrisitet, magnetisme og lys i fire sammenkoblede partielle differensialligninger. Seks år senere, i 1871, introduserte han tankeeksperimentet som i mer enn et århundre skulle hjemsøke termodynamikken og informasjonsteorien: **Maxwells demon** – et mikroskopisk vesen som ved å vokte en liten luke mellom to gasskamre tilsynelatende kunne sortere raske og langsomme molekyler uten å utføre mekanisk arbeid, og dermed senke universets entropi i strid med termodynamikkens andre hovedsetning.

Løsningen på demonens paradoks – utarbeidet gjennom Leo Szilard (1929), Léon Brillouin (1951), Rolf Landauer (1961) og Charles Bennett (1982) – er selve hjørnesteinen i dette fjortende bindet: **Demonen er ikke hevet over fysikken.** For å avgjøre om porten skal åpnes (`OPEN`) eller holdes lukket (`HOLD / KILL`), må demonen først måle og lagre tilstanden i et fysisk minne med endelig kapasitet. Når minnet tilbakestilles for neste syklus, krever slettingen av hver eneste forkastet kandidatbit en ufravikelig varmeutvikling:

$$\Delta Q_{\text{gate}} \ge k_B T \ln 2 \cdot \Delta I_{\text{discard}}$$

Seleksjon i en fysisk port er aldri gratis. Demonens regnskap går alltid i pluss for entropien.

### II. Den Fem-Trinns Elektromagnetiske Admisjonskjeden ($\Pi_{\mathcal{A}}$)

En utvidet felt-tilstandsvektor $y_t = (\mathbf{E}_t, \mathbf{B}_t, \mathcal{M}_t)$ som utvikler seg fra den hyperbolske Maxwell-generatoren $\tilde{y}_{t+1} = \Phi_{\text{Maxwell}}(y_t)$, slippes kun frem til fysisk aktuering dersom den oppfyller fem samvirkende projeksjonsbetingelser:
1. **Relativistisk Kausalitet ($\Pi_{\text{causal}}$):** Bølgefrontens støtte må ligge strengt innenfor fremtidig lyskjegle ($\text{supp}(\mathbf{E}_{t+\Delta t}) \subseteq J^+(y_t)$, $v_{\text{front}} \le c = 1/\sqrt{\varepsilon_0\mu_0}$).
2. **Energipositivitet ($\Pi_{\text{pos}}$):** Den lokale energitettheten $u_{\text{EM}} = \frac{1}{2}(\varepsilon\lVert\mathbf{E}\rVert^2 + \mu^{-1}\lVert\mathbf{B}\rVert^2) \ge 0$ er ikke-negativ overalt.
3. **Termodynamisk Poynting-Dissipasjon ($\Pi_{\text{thermo}}$):** I ledende og dispersive medier ($\sigma > 0$) krever Poyntings teorem at tap av feltenergi eksakt balanseres av positiv Joule-varme $p_{\text{diss}} = \mathbf{J}\cdot\mathbf{E} = \sigma\lVert\mathbf{E}\rVert^2 \ge 0$ og entropivekst $\dot{S}_{\text{env}} = p_{\text{diss}}/T \ge 0$.
4. **Global Noether-Bevaring ($\Pi_{\text{Noether}}$):** Kontinuitetsligningen $\partial_t \rho + \nabla\cdot\mathbf{J} = 0$ og den totale fire-impulsen $\nabla_\mu(T_{\text{EM}}^{\mu\nu} + T_{\text{matter}}^{\mu\nu}) = 0$ holdes eksakt lukket over grensesnittet.
5. **Subduksjon ved Ledende Grenseflater ($\Pi_{\text{bound}}$):** Tangentiell elektrisk feltkomponent $\mathbf{n} \times \mathbf{E}_{\parallel}$ og normal magnetisk fluks $\mathbf{n}\cdot\mathbf{B}_{\perp}$ tvinges på plass ved fysiske speil- og kavitetsvegger.

### III. CFJ–Proca Utvidet Elektrodynamikk og Casimir-Kuttet

Når vakuumet underlegges en bakgrunns-anisotropi $k_{\text{AF}}^\mu$ (Carroll–Field–Jackiw, CFJ) og en endelig fotonmasse-skranke $m_\gamma$ (Proca), spaltes vakuumets dispersjonsrelasjon i to chirale polarisasjonsgrener ($\pm$) med vakuum-birefringens og et nedre frekvenskutt $\omega_{\text{cut}}$ under hvilket bølgen blir evanescent (`HOLD`). Og når to ledende grenseflater settes opp med avstand $a$ i det kvantemekaniske vakuumet (**Casimir-kuttet**), skapes en målbar tiltrekkende kraft $F_C / A = -\frac{\pi^2\hbar c}{240 a^4}$ – ikke ved å legge til nye bølgemoder mellom platene, men ved **subtraktiv seleksjon** som forbyr bølgelengder $\lambda > 2a$ å eksistere i kaviteten.

---

# HOVEDVERK ($\mathcal{Y}$) // MONOGRAFI I FEM KAPITLER

---

## KAPITTEL 1 // MAXWELLS LIGNINGER, POYNTINGS TEOREM OG DEMONENS TERMODYNAMISKE PRIS

### 1.1 Forskjellen Mellom En Bølgeligning og En Hendelse
I det tomme rom ($\rho = 0, \mathbf{J} = \mathbf{0}$) er Maxwells ligninger:

$$\nabla\cdot\mathbf{E} = 0, \quad \nabla\cdot\mathbf{B} = 0, \quad \nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}, \quad \nabla\times\mathbf{B} = \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}$$

fullstendig tidsreversible under transformasjonen $(t, \mathbf{E}, \mathbf{B}) \mapsto (-t, \mathbf{E}, -\mathbf{B})$. En retardert sfærisk bølge som stråler utover fra en antenne, og en avansert sfærisk bølge som kommer inn fra uendeligheten og samler seg perfekt i antennen, er begge matematisk gyldige løsninger av $\Box A^\mu = 0$.

Hvorfor ser vi i den fysiske verden bare den retarderte bølgen, og hvorfor etterlater enhver elektromagnetisk måling et irreversibelt spor? Fordi det fysiske universet aldri er et grenseløst, tapsfritt vakuum. Enhver faktisk realisering krysser et materiell- og målegrensesnitt med endelig konduktivitet $\sigma > 0$, der **Poyntings energibalanseligning** trer i kraft:

$$-\frac{\partial}{\partial t}\int_\Omega \frac{1}{2}\left(\varepsilon\lVert\mathbf{E}\rVert^2 + \frac{1}{\mu}\lVert\mathbf{B}\rVert^2\right)dV = \oint_{\partial\Omega} (\mathbf{E}\times\mathbf{H})\cdot d\mathbf{A} + \int_\Omega \mathbf{J}\cdot\mathbf{E}\,dV$$

Det siste leddet på høyre side – det Ohmske arbeidet $\int_\Omega \sigma\lVert\mathbf{E}\rVert^2\,dV \ge 0$ – bryter tidsreverseringssymmetrien og konverterer koherent bølgeenergi til termisk entropi $\Delta S_{\text{irr}} = \int (\sigma\lVert\mathbf{E}\rVert^2 / T)\,dV\,dt > 0$. Uten dette dissipative leddet kan feltet aldri registreres i en detektor, aldri bevege et relé, og aldri bli en bevitnet hendelse.

### 1.2 Faradays Induksjonslov og Lenz’ Motstandsprinsipp som Naturlig Barriere
Michael Faradays oppdagelse i 1831 av elektromagnetisk induksjon, supplert med Heinrich Lenz’ fortegnslov (1834):

$$\mathcal{E}_{\text{ind}} = \oint_{\partial\Sigma} \mathbf{E}\cdot d\boldsymbol{\ell} = -\frac{d}{dt}\iint_\Sigma \mathbf{B}\cdot d\mathbf{A} = -\frac{d\Phi_B}{dt}$$

utgjør naturens egen prototypsluse mot uhemmet tilstandsvekst. Minustegnet i Lenz’ lov er ikke en konvensjon; det er en direkte nødvendighet av energibevaring og Le Chateliers stabilitetsprinsipp. Dersom fortegnet hadde vært positivt ($+d\Phi_B/dt$), ville enhver mikroskopisk fluktuasjon i magnetisk fluks indusere en strøm som forsterket fluksen ytterligere, og vakuumet ville eksplodere i en selvforsterkende runaway-ustabilitet på null tid.

Lenz’ lov forteller oss at **enhver endring av tilstandsfluks vekker en proporsjonal, motrettet elektromotorisk kraft som krever reelt mekanisk arbeid ($\delta W = I\,d\Phi_B$) for å overvinnes.** Motstanden er selve garantien for at verden ikke løper løpsk.

---

## KAPITTEL 2 // UTVIDET ELEKTRODYNAMIKK: PROCA-MASSE, CFJ-ANISOTROPI OG EVANESCENT `HOLD`

### 2.1 Den Utvidede CFJ–Proca-Lagrange-Tettheten
For å undersøke hvordan selve det elektromagnetiske vakuumet fungerer som et frekvens- og polarisasjonsselektivt filter, betrakter vi den utvidede gauge- og Lorentz-modifiserte **Carroll–Field–Jackiw–Proca (CFJ–Proca)** Lagrange-tettheten for fire-potensialet $A^\mu = (\phi/c, \mathbf{A})$ og feltstyrketensoren $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$:

$$\mathcal{L}_{\text{CFJ-Proca}} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} - \frac{1}{2}\mu_\gamma^2 A_\mu A^\mu + \frac{1}{4}\varepsilon^{\mu\nu\alpha\beta}(k_{\text{AF}})_\mu A_\nu F_{\alpha\beta} - J^\mu A_\mu$$

Her representerer:
* $\mu_\gamma = m_\gamma c / \hbar$ den inverse Compton-bølgelengden knyttet til en effektiv Proca-masse (eller plasma-/superleder-gap i et medium),
* $(k_{\text{AF}})^\mu = (k_0, \mathbf{k}_{\text{AF}})$ en aksial bakgrunns-firevektor som bryter paritet ($\mathcal{P}$) og Lorentz-symmetri og påtvinger en foretrukket vakuumrotasjon.

Variasjon av virkningen $\delta\int \mathcal{L}_{\text{CFJ-Proca}}\,d^4x = 0$ gir de modifiserte feltligningene:

$$\partial_\mu F^{\mu\nu} + \mu_\gamma^2 A^\nu + (k_{\text{AF}})_\mu \tilde{F}^{\mu\nu} = \mu_0 J^\nu, \qquad \tilde{F}^{\mu\nu} = \frac{1}{2}\varepsilon^{\mu\nu\alpha\beta}F_{\alpha\beta}$$

### 2.2 Vakuum-Birefringens og Evanescent Avskjæring ($\omega < \omega_{\text{cut}} \implies \text{HOLD}$)
Ved å sette inn en plan bølgeansats $A^\mu(x) \propto \epsilon^\mu e^{-i(\omega t - \mathbf{k}\cdot\mathbf{r})}$ i en kildefri region ($J^\nu = 0$) med rent tidslignende CFJ-vektor $k_{\text{AF}}^\mu = (k_0, \mathbf{0})$, spaltes dispersjonsrelasjonen i to høyre- og venstresirkulært polariserte grener ($\lambda = \pm 1$):

$$\omega_\pm^2(k) = c^2 k^2 + c^2\mu_\gamma^2 \pm c^2 k_0 k$$

Dette har to umiddelbare fysiske konsekvenser for bølgeforplantning gjennom porten:
1. **Kiralt Faseskille (Birefringens):** De to sirkulære polarisasjonene forplanter seg med ulik fase- og gruppehastighet, hvilket roterer polarisasjonsplanet med en vinkel $\Delta\theta = \frac{1}{2}k_0 L$ over en veilengde $L$. En bølge hvis polarisasjonsfase ikke samsvarer med mottakerportens admisjonsvinkel, reflekteres tilbake.
2. **Evanescent Karantene (`HOLD`) under Avskjæringsfrekvensen:** For en gitt frekvens $\omega$ løses bølgetallet $k(\omega)$ fra $\omega^2 - c^2\mu_\gamma^2 \mp c^2 k_0 k - c^2 k^2 = 0$. Når drivfrekvensen synker under den effektive Proca-gapfrekvensen ($\omega < \omega_{\text{cut}}$), blir bølgetallet rent imaginært ($k = i\kappa$ med $\kappa > 0$):

$$\mathbf{E}(z, t) = \mathbf{E}_0 e^{-\kappa z}\cos(\omega t), \qquad \langle \mathbf{S} \rangle_t = \text{Re}(\mathbf{E} \times \mathbf{H}^*) \equiv \mathbf{0}$$

En evanescent bølge transporterer **eksakt null netto aktiv effekt** gjennom barrieren ($\langle\mathbf{S}\rangle_t = \mathbf{0}$); feltet lagrer kun reaktiv energi i grenseflaten ($B = (0,1)$) og venter på at frekvensen og energien skal løftes over terskelen $\omega_{\text{cut}}$ før strålingen slippes ut som en forplantende bølge (`OPEN`).

---

## KAPITTEL 3 // CASIMIR-KUTTET — VAKUUMETS SUBTRAKTIVE TRYKK

### 3.1 Hvorfor Grenser Skaper Kraft Gjennom Fravær
I klassisk tenkning oppstår krefter ved at man *legger til* partikler eller kilder i et rom. Hendrik Casimir beviste i 1948 det stikk motsatte for det kvantemekaniske elektromagnetiske vakuumet: **Selve innføringen av en grenseflate som forbyr bestemte moder å eksistere, frembringer et reelt, målbart mekanisk trykk.**

Betrakt to uendelig utstrakte, perfekt ledende plater plassert parallelt i $xy$-planet ved $z = 0$ og $z = a$. Grensebetingelsen $\mathbf{n} \times \mathbf{E} = \mathbf{0}$ på platene tvinger den transversale bølgevektoren langs $z$-aksen til å være diskret kvantisert:

$$k_z = \frac{n\pi}{a}, \qquad n = 0, 1, 2, \dots$$

mens alle kontinuerlige bølgetall $k_z \in \mathbb{R}$ er tillatt på utsiden av kaviteten ($z < 0$ og $z > a$). Dermed er alle vakuumfluktuasjoner med halvbølgelengde større enn plateavstanden ($\lambda/2 > a$) **subtraktivt ekskludert** fra det indre rommet.

### 3.2 Euler–Maclaurin-Utledning av Casimir-Energitettheten
Nullpunktsenergien per flateenhet mellom platene er gitt ved den regulariserte summen over de tillatte modene $\omega_n(k_\parallel) = c\sqrt{k_\parallel^2 + (n\pi/a)^2}$:

$$\frac{E_{\text{cav}}(a)}{A} = \frac{\hbar}{2}\sum_{n=-\infty}^{\infty}\int \frac{d^2 k_\parallel}{(2\pi)^2}\,c\sqrt{k_\parallel^2 + \left(\frac{n\pi}{a}\right)^2}$$

Ved å trekke fra den frie vakuumenergien i samme volum (der summen $\sum_n$ erstattes av integralet $\int dn$) og anvende **Euler–Maclaurin-summasjonsformelen** (eller analytisk fortsettelse av Riemanns zetafunksjon $\zeta(-3) = \frac{1}{120}$):

$$\frac{\Delta E_C(a)}{A} = -\frac{\pi^2 \hbar c}{720\,a^3}$$

Differentiasjon med hensyn på plateavstanden $a$ gir det attraktive **Casimir-trykket**:

$$P_C(a) = -\frac{\partial}{\partial a}\left(\frac{\Delta E_C(a)}{A}\right) = -\frac{\pi^2 \hbar c}{240\,a^4} < 0$$

Casimir-effekten er det reneste fysiske bildet på *subtraktiv ontologi*: kaviteten holdes sammen og komprimeres ikke av det som er lagt inn mellom veggene, men av tyngden av alt det som grensen $\Pi_{\text{bound}}$ nektet adgang.

---

## KAPITTEL 4 // DEN LANGSOMME HEISEN (DØR 18) — TERMODYNAMISK BÆREEVNE OG KVASI-STATISK ANSVAR

### 4.1 Prisen for Hastverk: Endelig-Tids Termodynamikk og Friksjonstap
I klassisk likevektstermodynamikk utføres det maksimale arbeidet (eller kreves det minimale arbeidet $\Delta W_{\text{min}} = \Delta F$) kun i den **kvasi-statiske grensen** der prosessen tar uendelig lang tid ($\tau_{\text{proc}} \to \infty$). Når et system derimot tvinges til å endre tilstand fra $\lambda_0$ til $\lambda_1$ på en endelig tid $\tau_{\text{proc}}$, sier **endelig-tids termodynamikk** (Sekimoto–Sivak–Crooks) at det irreversible ekstraarbeidet (dissipert som varme $Q_{\text{irr}}$) skalerer omvendt proporsjonalt med prosesstiden langs det termodynamiske lengdeelementet $\mathcal{L}_{\text{thermo}}$:

$$W_{\text{diss}}(\tau_{\text{proc}}) = W(\tau_{\text{proc}}) - \Delta F \ge \frac{\mathcal{L}_{\text{thermo}}^2}{\tau_{\text{proc}}}, \qquad \mathcal{L}_{\text{thermo}} = \int_0^{\tau_{\text{proc}}} \sqrt{g_{ij}(\lambda)\,\dot{\lambda}^i\dot{\lambda}^j}\,dt$$

der $g_{ij}(\lambda)$ er friksjons- eller Fisher–Rao-informasjonsmetrikken på tilstandsrommet.

Jo raskere en overgang tvinges gjennom ($\tau_{\text{proc}} \downarrow 0$), desto voldsommere vokser varmeutviklingen $W_{\text{diss}} \propto 1/\tau_{\text{proc}}$ og det mekaniske stresset i bærestrukturen.

### 4.2 Dør 18 (*Den Langsomme Heisen*) som Fysisk Fartsbegrenser
I en tid der algoritmiske systemer kappløper om maksimal gjennomstrømming og null latens, innfører **Dør 18 (*Den Langsomme Heisen*)** den motsatte konstitusjonelle regelen: **Hastigheten til en tilstandsovergang skal aldri overstige konstruksjonens termiske og strukturelle bæreevne.**

Vi definerer den maksimalt tillatte fasederiverte $\dot{\lambda}_{\max}$ ut fra strukturens kjølekapasitet $\dot{Q}_{\text{cool,max}}$ og mekaniske sikkerhetsmargin $\sigma_{\text{yield}} / \text{SF}$:

$$\big\lVert \dot{\lambda}(t) \big\rVert_{g} \le v_{\text{elevator}} = \sqrt{\frac{\dot{Q}_{\text{cool,max}}}{T_0}} \quad \wedge \quad \sigma_{\text{mech}}\big(\ddot{\lambda}(t)\big) \le \frac{\sigma_{\text{yield}}}{\text{SF}}$$

Hvis en ekstern forespørsel krever en akselerasjon eller løftehastighet som bryter denne grensen, nekter *Den Langsomme Heisen* å spurte. Den bremser bevegelsen ned til det kvasi-statiske sporet der lasten kan bæres trygt hele veien opp uten at vaierne ryker eller motoren brenner opp. Sann styrke ligger ikke i hvor fort man kan rase gjennom rommet uten last, men i hvor tung bør man kan løfte uten å miste grepet.

---

## KAPITTEL 5 // DE TRE LERRETENE — KAUSAL TREGHET OG TERMODYNAMISK SUVERENITET

### 5.1 Treenigheten av Mulighet, Motstand og Spor
Når vi nå ser tilbake på hele buen gjennom disse fem monografiene – fra Einsteins krumme romtid (*Bind X*), via involusjonens dobbeltlov (*Bind XI*), Poincarés tverrsnitt (*Bind XII*) og Gödels ytre vitne (*Bind XIII*) frem til Maxwells og Casimirs elektrodynamiske sluse (*Bind XIV*) – trer det frem en enhetlig naturfilosofi spent ut over **De Tre Lerretene**:

1. **Det Første Lerretet ($\Phi \in \mathcal{Y}_{\text{cand}}$ — Mulighetsfeltet):** Her bølger Maxwells frie potensialer, Schrödingers superposisjoner og Einsteins ufiltrerte metrikker. Det første lerretet er rikt, symmetrisk og reversibelt ($\text{Rev}^1$), men det er ennå vektløst. Det har ingen historie.
2. **Det Andre Lerretet ($\Pi_{\mathcal{A}}, \Omega$ — Kuttflaten og Porten):** Her møter bølgen motstanden: Lenz’ motkraft, Casimir-veggene, kontrollbarrieren, Poincaré-snittet $\Sigma_k$ og det ytre Gödel-vitnet. Her skilles Bøff fra Bløff, og her betales demonens pris $Q \ge k_B T \ln 2$.
3. **Det Tredje Lerretet ($\mathcal{H}$ — Det Uutslettelige Vitnesbyrdet):** Her størkner det som overlevde porten til irreversibel materiell struktur ($D_2/D_3$). På det tredje lerretet finnes ingen angreknapp ($\text{Rev}^2$). Hvert strøk som først er satt i lerretet, blir stående som en bærende del av verdens gulv.

Ingen bølge blir til lys som varmer et rom før den har latt seg stanse og absorbere av en flate.

---

# VEDLEGG ($\mathcal{H}$) // DET LUKKEDE VITNELAGET (ELEKTROMAGNETISK TELEMETRI, L1-HARNESS OG KILDEKATALOG)

*Dette avsluttende vedlegget utgjør historiefiberet $\mathcal{H}$ i det skjeve produktet $\mathcal{S}_{\text{tot}} = \mathcal{Y} \times \mathcal{H}$ ($\partial y_{t+1}/\partial W_t \equiv 0$). Alle konkrete L1-simuleringsterskler, galvaniske reléspesifikasjoner og kildedokument-peker er isolert her.*

### H.1 Demarkasjon mellom Elektrodynamisk Feltteori ($\mathcal{Y}$) og Cyber-Fysisk Instrumentering ($\mathcal{H}$)

Under aksiomet $\text{INSPIRED\_BY} \neq \text{IMPLEMENTS} \neq \text{PROVES}$ gjelder følgende strukturelle samsvar mellom Maxwell-fysikken i $\mathcal{Y}$ og instrumenteringslaget i $\mathcal{H}$:

| Fysisk Lov i Hovedverk ($\mathcal{Y}$) | Matematisk Betingelse | Teknisk L1/L3-Realisering i Vedlegg ($\mathcal{H}$) |
| :--- | :--- | :--- |
| **Kausal Lysgrense ($\Pi_{\text{causal}}$)** | $v_{\text{front}} \le c = (\varepsilon_0\mu_0)^{-1/2}$ | Tidsstempel- og fase-sjekk mot ikke-kausale datapakker |
| **Poynting- og Joule-balanse ($\Pi_{\text{thermo}}$)** | $\sigma\lVert\mathbf{E}\rVert^2 \ge 0$, $\dot{S}_{\text{env}} \ge 0$ | Termisk effekt- og strømsensor ($I^2 R \le P_{\text{max}}$) |
| **Lenz’ Induksjonsmotstand** | $\mathcal{E}_{\text{ind}} = -d\Phi_B/dt$ | Flyback-diode, dI/dt-snubber og induktiv dempning ved kutt |
| **CFJ–Proca Evanescent Gap** | $\omega < \omega_{\text{cut}} \implies \langle\mathbf{S}\rangle_t = \mathbf{0}$ | Lavfrekvent `HOLD`-buffer ($0{,}00\text{ V}$ aktiv utgang) |
| **Dør 18 (*Den Langsomme Heisen*)** | $\lVert\dot{\lambda}\rVert_g \le \sqrt{\dot{Q}_{\text{cool,max}}/T_0}$ | Slew-rate-begrenser og trinnvis ramp-kontroll |

### H.2 Katalog over Konsoliderte Kildedokumenter i Bind XIV (0 % Duplisering mot Bind X)

1. **Arbeidsnotat 01 & 02:** *Electromagnetic Realization under Admissibility Constraints (Maxwell–KY Pipeline $\Pi_{\mathcal{A}}$).*
2. **Traktat 03:** *Faraday's Law of Electromagnetic Induction & Lenz's Law as Passive Stability Interlock.*
3. **Dokument 79:** *Utvidet Elektrodynamikk — Carroll–Field–Jackiw (CFJ) Birefringens og Proca Fotonmasse-Gap.*
4. **Dokument 146:** *Casimir-Kuttet — Vakuumets Subtraktive Trykk ($P_C = -\pi^2\hbar c / 240 a^4$).*
5. **Dokument 100:** *Den Langsomme Heisen — Bæreevne og Termodynamisk Ansvarlighet (Dør 18).*
6. **Traktat 08 & 09:** *The Architecture of Realization & The Three Canvases (Causal Inertia and Thermodynamic Sovereignty).*
*(Merk: Dokument 74 om det relativistiske $\text{sech}^4$-projeksjonsstresset $\Sigma_{\mu\nu}^{\text{irr}}$ i Einsteins feltligninger er kanonisk plassert i Bind X: Kapittel 3).*
