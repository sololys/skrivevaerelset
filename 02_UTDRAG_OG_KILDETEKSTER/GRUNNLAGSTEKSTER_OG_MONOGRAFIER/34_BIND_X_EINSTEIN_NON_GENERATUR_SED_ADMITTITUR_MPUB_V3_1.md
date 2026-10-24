# 34 — Bokhylla Bind X: *EINSTEIN & FELTLIGNINGENE — Non Generatur, Sed Admittitur* (Mpub v3.1)

**Forfatter:** Marius Egerhei Torjusen (Reismann-punktet Systemer, 2026)  
**Kilde:** [`07_BOKHYLLA_MONOGRAFIER_OG_BOKVERK/10_EINSTEIN_ZENODO_KOMPENDIUM/EINSTEIN_MONOGRAFI_NON_GENERATUR_SED_ADMITTITUR.pdf`](../../07_BOKHYLLA_MONOGRAFIER_OG_BOKVERK/10_EINSTEIN_ZENODO_KOMPENDIUM/EINSTEIN_MONOGRAFI_NON_GENERATUR_SED_ADMITTITUR.pdf)  
**Godot `L1` Motor:** [`04_REALITY_FORGE/RealityForge_Godot/scripts/einstein_bind_x_admissibility_engine.gd`](../../04_REALITY_FORGE/RealityForge_Godot/scripts/einstein_bind_x_admissibility_engine.gd) (`6/6 PASS`)

> **Demarkasjon (`L1`):** Programvaremotorene og de numeriske verifikasjonene er lokalt demonstrert programvare (`L1`). De respekterer grensen $\text{INSPIRED\_BY} \neq \text{IMPLEMENTS} \neq \text{PROVES}$, og bruker append-only hash-kjeder som programvare-vitner, ikke som fysisk WORM-maskinvare.

---

## Prolog: Komprimert Kanonisk Traktat

- **Realiseringsslusen i $\mathcal{P}$:** Einsteins feltligninger og kvantemekanikkens unitære gruppe $U(t) = e^{-iHt/\hbar}$ definerer et uforpliktet forslagsrom ($\mathcal{NP}$) uten seleksjonskostnad. Fysisk realisering er en subtraktiv operasjon i polynomiell tid ($\mathcal{P}$) styrt av den feillukkede Poincaré–Moreau-slusen:
  $$x_{t+1} = \Omega(\Pi_{\mathcal{A}}(\Phi(x_t))) \times W_{\text{log}}$$
- **Kausal lukking uten tilbakevirkning:** Tilstanden bokføres i det skjeve produktrommet $\mathcal{S}_{\text{tot}} = \mathcal{Y} \times \mathcal{H}$ under den eksakte ortogonalitetsbetingelsen:
  $$\frac{\partial y_{t+1}}{\partial W_t} \equiv 0$$
  og under demarkasjonen $\text{INSPIRED\_BY} \neq \text{IMPLEMENTS} \neq \text{PROVES}$.

---

## Kapittel 1: Det Epistemiske Kuttet, Gödels Metrikk og Den Kausale Clutchen

### 1.1 Gödels støvunivers som bevis på underbestemthet
Punktvis oppfyllelse av $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$ garanterer ikke global kausalitet. I Gödels roterende støvunivers ($4\pi G\rho_0 = \omega^2 = -\Lambda$) skifter den induserte metriske komponenten
$$g_{\phi\phi}(r_0) = \frac{2}{\omega^2}\sinh^2(r_0)\left(1 - \sinh^2(r_0)\right)$$
fortegn og blir negativ for enhver radius over den kritiske terskelen:
$$r_0 > r_{\text{CTC}} = \operatorname{arsinh}(1) = \ln(1 + \sqrt{2}) \approx 0,881373587$$
Dette genererer lukkede tidslignende kurver ($\mathcal{M}_{\text{CTC}} \neq \emptyset$) og beviser at feltligningene alene kun er en syntaktisk kandidatgenerator ($\Phi \in \mathcal{NP}$) som krever en global seleksjonsoperator $\Pi_{\mathcal{A}}$ på globalt hyperbolske metrikker.

### 1.2 Variasjonsutledning av Moreau-projeksjonen
Over den lukkede, konvekse mengden av globalt hyperbolske tilstander $\mathcal{A} \subset \mathcal{Y}$ med konveks indikatorfunksjonal $I_{\mathcal{A}}(y) \in \{0, +\infty\}$ utledes resolventen:
$$y_{t+1} = (I + N_{\mathcal{A}})^{-1}(\Phi(y_t)) \equiv \Pi_{\mathcal{A}}(\Phi(y_t))$$
Ved Moreaus ortogonale dekomposisjonsteorem spaltes $\Phi(y_t) = \Pi_{\mathcal{A}}(\Phi(y_t)) + \xi_t$, der elimineringen av normalresidualet $\xi_t = (I - \Pi_{\mathcal{A}})(\Phi(y_t)) \in N_{\mathcal{A}}(y_{t+1})$ krever det mekaniske seleksjonsarbeidet:
$$\Delta W_{\text{clutch}} = \frac{1}{2}\|\xi_t\|_{\mathcal{Y}}^2 = \frac{1}{2}\Delta_{\mathcal{K}}^2(y_t) \ge k_B T \ln 2 \cdot \Delta I$$
Ved overskridelse av budsjettskranken $\epsilon = \sqrt{2F_{\max}}$ kobler clutchen ut til $\Omega = \text{KILL}$, og normalresidualet $\xi_t$ eksporteres til historiefiberet $\mathcal{H}$ med nedre-triangulær Jakobi-matrise ($\partial y_{t+1}/\partial W_t \equiv 0$).

---

## Kapittel 2: Residualets Plikt: Merkurs Perihel og Petrov Type D Admisjonskjerne

### 2.1 Forbudet mot hjelpefelt («Vulkan»)
I Schwarzschild-vakuum gir det relativistiske krumningsleddet $\frac{3GM_\odot}{c^2}u^2$ en perihelpresesjon på $\Delta\phi = 42,98''/\text{århundre}$. Fordi leddet avhenger kvadratisk av testpartikkelens egen bane $u(\phi) = 1/r(\phi)$, kan intet bane-uavhengig Newtonsk hjelpepotensial $\Phi_{\text{aux}}(r)$ (som «Vulkan») absorbere residualet i et fiktivt kildeledd $T_{\mu\nu}^{\text{aux}}$ uten å bryte Keplers tredje lov.

### 2.2 Weyl-skalaren $\Psi_2$ og $D_{\text{adm}}(\tau)$
I Boyer–Lindquist-koordinater for en Kerr-metrikk med masse $M$ og spinn $a = J/M$ er eneste ikke-forsvinnende Newman–Penrose Weyl-skalar $\Psi_2(r,\theta) = -M/(r - ia\cos\theta)^3$. Den fasederiverte admisjonskjernen:
$$D_{\text{adm}}(\tau) = \exp\left(-\alpha \frac{|\nabla_u \Psi_2|^2}{|\Psi_2|^{8/3} + \eta_0}\right), \qquad \frac{|\nabla_u \Psi_2|^2}{|\Psi_2|^{8/3}} = 9M^{-2/3}\left[(u^r)^2 + a^2\sin^2\theta(u^\theta)^2\right]$$
gir en **$6,8\times$ forsterkning** i deteksjonssensitivitet for begynnende geodetisk ustabilitet sammenlignet med koordinatavvik.

---

## Kapittel 3: Krumningens Metriske Pris: Eikonal-Invarians og $\operatorname{sech}^4$-Tensoren

### 3.1 Planck-skranken og eikonal-feltet
En skarp grenseflate $\epsilon = 0$ gir en singulær Heaviside-fordeling som divergerer kvadratisk i virkningsintegralet og bryter Planck-skranken $\epsilon \ge \Delta x_{\min} = 2\ell_P$. Med det kovariante eikonal-feltet $g^{\mu\nu}\nabla_\mu d \nabla_\nu d = \sigma \in \{+1, -1\}$ og den glatte porten $P_{\mathcal{K}}^{(\epsilon)}(x) = \frac{1}{2}[1 + \tanh(d(x)/2\epsilon)]$ blir gradienten:
$$\nabla_\mu P_{\mathcal{K}}^{(\epsilon)} = \frac{1}{4\epsilon}\operatorname{sech}^2\left(\frac{d}{2\epsilon}\right)n_\mu$$

### 3.2 De modifiserte feltligningene
Stasjonær variasjon $\delta S_{\text{tot}}/\delta g^{\mu\nu} = 0$ av totalvirkningen gir det irreversible projeksjonsstresset og de projeksjons-skrankede feltligningene:
$$\Sigma_{\mu\nu}^{\text{irr}} = \frac{\lambda_2}{16\epsilon^2}\operatorname{sech}^4\left(\frac{d(x)}{2\epsilon}\right)\left[n_\mu n_\nu - \frac{1}{2}g_{\mu\nu}(g^{\alpha\beta}n_\alpha n_\beta)\right] + \Sigma_{\mu\nu}^{(\text{defect})}$$
$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}\left(T_{\mu\nu} + \Sigma_{\mu\nu}^{\text{irr}}\right), \qquad \nabla^\mu T_{\mu\nu} = -\nabla^\mu \Sigma_{\mu\nu}^{\text{irr}}$$
Integrasjon av Raychaudhuri-ligningen over et horisonttverrsnitt gir den eksakte ikke-likevekts Clausius-relasjonen $\delta Q = T_H \delta S_{\text{rev}} + T_H \delta_i S_{\Pi_{\mathcal{K}}}$ med $\delta_i S_{\Pi_{\mathcal{K}}} \ge k_B \ln 2 \cdot \Delta I_{\text{cut}}$.

---

## Kapittel 4: Holomorfisperre, Nash–Moser-Regulering i Fréchet-Rom og Horisontforrigling

### 4.1 Beviset for Holomorfisperren (Teorem 4.1)
Ved identitetsteoremet for analytiske funksjoner på en sammenhengende analytisk mangfoldighet $\mathcal{M}$ kan ingen $f \in C^\omega(\mathcal{M})$ oppfylle $f|_{\mathcal{A}} \equiv 1$ og $f|_{\mathcal{M}\setminus\overline{\mathcal{A}}} \equiv 0$. Dette tvinger frem en to-lags arkitektur: analytisk regulering i bufferbeltet $B = (0,1)$ (`HOLD`) og ikke-holomorf diskontinuerlig avskjæring ved konvergensbrudd (`KILL`).

### 4.2 Nash-betingelsen og Nash–Moser-skjemaet
I $B = (0,1)$ reguleres metrikken mot den fjerdeordens elliptiske Nash-operatoren $\mathcal{N}(g) \equiv \Delta_g R(g) = 0$. Fordi inversen $[D\mathcal{N}(g)]^{-1}$ taper $r_0 = 4$ deriverte i Sobolev-skalaen $\{H^s\}_{s\ge 0}$, brukes glatteoperatorene $S_{\theta_k}$ ($\theta_k = \theta_0^{(3/2)^k}$) i det tamme Fréchet-rommet $\mathcal{F} = \bigcap_{s\ge 0} H^s$:
$$g_{k+1} = g_k - S_{\theta_k}[D\mathcal{N}(g_k)]^{-1}\mathcal{N}(g_k)$$
For $\|\mathcal{N}(g_0)\|_{s_0} < \delta_{\text{Nash}}$ konvergerer skjemaet superlineært mot $\Omega \to \text{OPEN}$; ved overskridelse utløses $\Omega \to \text{KILL}$.

---

## Kapittel 5: Eksergidestruksjon, Schurs Produktteorem og PCSE Fase-Hysterese

### 5.1 Gouy–Stodola og CPTP Hamming-dekoherens (Teorem 5.1)
I isolerte regimer uten grensekontakt går eksergi tapt ved $\dot{E}x_{\text{dest}} = T_0 \dot{S}_{\text{gen}} \ge 0$. På kvantenivå er admisjonskanalen $\mathcal{E}_{\mathcal{K}}(\rho) = \rho \circ G$ med $G_{xy} = \exp(-\alpha d_H(f(x), f(y)))$ bevist å være CPTP (fullstendig positiv og sporbevarende) via Schönbergs teorem og Schurs produktteorem (1911).

### 5.2 PCSE Fase-Hysterese ($\Delta p = 0,126$)
I den projeksjons-skrankede Schrödinger-ligningen (PCSE):
$$i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle = \left(H_0 + \mu_{\mathcal{K}}(I - P_{\mathcal{K}}^{(\epsilon)}) + \hbar\omega_{\text{hol}}K_\gamma[x(\tau)]\sigma_z\right)|\psi(t)\rangle$$
vil to interferometriske baner $\gamma_A$ ($K_{\gamma_A} > 0$ gjennom $B=(0,1)$) og $\gamma_B$ ($K_{\gamma_B} = 0$ i $\operatorname{Int}(\mathcal{A})$) med identiske slutt-tetthetsmatriser i posisjonsbasisen ($\rho_A^{\text{pos}}(t_1) = \rho_B^{\text{pos}}(t_1)$) gi en målbar sannsynlighetsdivergens ved Hadamard-utlesning ($\alpha\bar{d}_H = 0,15$, $\omega_{\text{hol}}K_{\gamma_A} = \pi/4$):
$$\Delta p = |P(+|\gamma_A) - P(+|\gamma_B)| = \frac{1}{2}e^{-\alpha\bar{d}_H}\left|1 - \cos(\omega_{\text{hol}}K_{\gamma_A})\right| = 0,126$$

---

## Vedlegg A: Fréchet-Forriglet Isomorfi Mellom Weyl-Kjernen og `L1`-Kuttet ($\mathcal{H}$)

- **Teorem A.1 (Fréchet-derivert for overføringsfunksjonen $\Psi_{B\to A}$):** Enhver komponent i kontrollrommet $\mathcal{H}$ (Nivå A) er bildet av en eksakt, kontinuerlig Fréchet-deriverbar overføringsfunksjon $DD_{\text{adm}}[g](\tau)\cdot h$ fra Lorentz-mangfoldigheten $\mathcal{Y}$ (Nivå B), ned til det galvaniske relékuttet:
  $$V_{\text{out}}([g])(\tau) = V_0 \cdot \Theta(D_{\text{adm}}[g](\tau) - \tau_{\text{crit}})$$
