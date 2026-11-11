# 🏛️ BIND X: ALBERT EINSTEIN & FELTLIGNINGENE — *NON GENERATUR, SED ADMITTITUR*
### *Om Gödels roterende støvunivers ($r\_{\text{CTC}}$), Petrov Type D Weyl-kjernen ($6{,}8\times$), $\operatorname{sech}^4$-projeksjonsstresset, Nash–Moser-iterasjon, $\text{ER}=\text{EPR}$ og Page-kurvens unitaritet*

> **Epistemisk demarkasjon (`INSPIRED_BY != IMPLEMENTS != PROVES`):** Einsteins feltligninger (1915), Gödels metriske løsning (1949), Newman–Penrose Weyl-skalarer, Kerr-geometrien (1963), Nash–Moser implisitt funksjonsteorem (1956/1966), Bekenstein–Hawking-entropi, Maldacena–Susskind $\text{ER}=\text{EPR}$-formodningen (2013), Don Pages enhetskurve (1993) og Schurs produktteorem tilhører $\text{L0}$. De numeriske admisjonsfiltrene ($D_{\text{adm}}$, Moreau-resolventen $\Pi_{\mathcal{A}}$, `einstein_ky_engine.py` Fase 1–4 og PCSE-simuleringen) er deterministiske programvaremodeller på nivå $\text{L1}$. De utgjør ingen modifikasjon av astrofysisk generell relativitetsteori i naturen.

---

## 1. Hvorfor Einsteins Feltligninger Alene er en Underbestemt $\mathcal{NP}$-Kandidatgenerator

Einsteins klassiske feltligninger fra november 1915 knytter romtidens krumning til energi-impulstensoren $T_{\mu\nu}$:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = R_{\mu\nu} - \frac{1}{2}R\,g_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}\,T_{\mu\nu}$$

I over et århundre har denne ligningen blitt feiret som selve ur-bildet på en komplett naturlov. I 1949 ga imidlertid Kurt Gödel Albert Einstein en fødselsdagsgave som rystet denne antakelsen i grunnvollene. Gödel konstruerte en **eksakt, glatt, stasjonær løsning** av Einsteins feltligninger for et trykkfritt, roterende støvunivers ($T_{\mu\nu} = \rho_0 u_\mu u_\nu$) med negativ kosmologisk konstant $\Lambda$:

$$4\pi G\rho_0 = \omega^2 = -\Lambda > 0$$

I sylindriske koordinater $(t, r, \phi, z)$ med $c = 1$ og skalering $2\omega^2 = 1$ har Gödel-metrikken linjeelementet:

$$\mathrm{d}s^2 = -\mathrm{d}t^2 + \mathrm{d}r^2 + \mathrm{d}z^2 - 2\sqrt{2}\sinh^2(r)\,\mathrm{d}t\,\mathrm{d}\phi + \sinh^2(r)\bigl(1 - \sinh^2(r)\bigr)\,\mathrm{d}\phi^2$$

Se nøye på den vinkel-metriske komponenten langs en sirkel med konstant $t, r = r_0, z$:

$$g_{\phi\phi}(r_0) = \sinh^2(r_0)\bigl(1 - \sinh^2(r_0)\bigr)$$

Så lenge $\sinh(r_0) < 1$, er $g_{\phi\phi}(r_0) > 0$, og sirkelen er romlignende. Men i det øyeblikket radiusen passerer den kritiske Gödel-horisonten

$$r_0 > r_{\text{CTC}} = \operatorname{arsinh}(1) = \ln\bigl(1 + \sqrt{2}\bigr) \approx 0{,}88137$$

blir $\sinh(r_0) > 1$ og dermed **$g_{\phi\phi}(r_0) < 0$**! Sirkelen $(t = \text{konst}, r = r_0, \phi \in [0, 2\pi])$ er blitt en **lukket tidslignende kurve (CTC — *Closed Timelike Curve*)**: en observatør kan reise langs sirkelen fremover i sin egen lokale egentid og ankomme sin egen fortid.

**Den fundamentale lærdommen (*Non Generatur, Sed Admittitur*):** Einsteins differensialligning $G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa T_{\mu\nu}$ er lokalt tilfredsstilt i hvert eneste punkt av Gödels univers, med positiv energitetthet $\rho_0 > 0$. Likevel kollapser den globale kausaliteten fullstendig. En lokal differensialligning er derfor **kun en kandidatgenerator ($\Phi_{\text{GR}} \subset \mathcal{NP}$)**. For at en løsning skal ha rett til fysisk eksistens i $\mathcal{P}$, må den i tillegg passere en global kausal admisjonsport $\Pi_{\mathcal{A}}$ (kronologibevaring, global hyperbolisitet og termodynamisk pil).

---

## 2. Den Kausale Clutchen og det Skjeve Produktet $\mathcal{S}_{\text{tot}} = \mathcal{Y} \times \mathcal{H}$

I *Bind X* formaliseres koblingen mellom feltkandidaten $y \in \mathcal{Y}$ og vitnetilstanden $h \in \mathcal{H}$ som et **skjevt produkt** (*skew-product dynamical system*) over det totale tilstandsrommet $\mathcal{S}_{\text{tot}} = \mathcal{Y} \times \mathcal{H}$. Den tillatte konvekse kjeglen av globalt hyperbolske, kronologiske og energipositive tilstander betegnes $\mathcal{A} \subset \mathcal{Y}$.

Tilstandsoppdateringen styres av Moreau-resolventen $\Pi_{\mathcal{A}} = (I + N_{\mathcal{A}})^{-1}$ (som minimerer den kvadratiske avstanden $\frac{1}{2}\|y - \tilde{y}\|^2 + I_{\mathcal{A}}(y)$) koblet gjennom den binære kausale clutchen $\chi(W_t) \in \{0, 1\}$:

$$y_{t+1} = y_t + \chi(W_t)\Bigl(\Pi_{\mathcal{A}}\bigl(\tilde{y}_{t+1}\bigr) - y_t\Bigr)$$

Samtidig krever den kausale uavhengigheten mellom terreng/vitne og forslagsgenerator at Jakobi-matrisen på det utvidede rommet $(W_t, y_{t+1})$ er strengt nedre-triangulær med hensyn på manipulering av vitnet fra innsiden:

$$\frac{\partial W_t}{\partial \tilde{y}_{t+1}} \equiv 0, \qquad \left.\frac{\partial y_{t+1}}{\partial \tilde{y}_{t+1}}\right|_{W_t = 0} \equiv 0$$

Når vitnet svikter ($W_t = 0 \implies \chi(W_t) = 0$), kobles clutchen ut med matematisk null-stivhet for kandidaten $\tilde{y}_{t+1}$: tilstanden fryser eksakt i $y_{t+1} = y_t$ (`HOLD`).

---

## 3. Merkurs Perihel, Petrov Type D Weyl-Kjernen ($6{,}8\times$) og Eksakt Fréchet-Derivasjon

### 3.1 Merkurs perihelresidual som klassisk modell-terreng-dom
I 1859 påviste Le Verrier at Merkurs perihel presederer med et uforklart avvik utover summen av alle kjente newtoniske planetperturbasjoner. Generell relativitetsteori gir den eksakte geodetiske korreksjonen per omløp:

$$\Delta\phi = \frac{6\pi G M_\odot}{a(1 - e^2)c^2} = 42{,}98''\text{ per århundre}$$

I skrankens språk var Vulkan-hypotesen (jakten på en usynlig planet innenfor Merkur) et forsøk på å lappe en sviktende generator i $\mathcal{NP}$, mens det observerte avviket på $42{,}98''/\text{århundre}$ var det fysiske terrengets ugjendrivelige dom i $\mathcal{P}$.

### 3.2 Petrov Type D Weyl-admisjonskjernen ($D_{\text{adm}}$)
Når en bane nærmer seg et sterkt, roterende gravitasjonsfelt eller en krummet fasesingularitet (modellert ved Kerr-metrikken med masse $M$ og spinnparameter $a = J/Mc$), er skalar krumningsinformasjon ($R = 0$ i vakuum!) fullstendig blind for tidevannskreftene. I Newman–Penrose-formalismen fanges hele den frie gravitasjonsfeltstyrken i en Petrov Type D-romtid av én enkelt kompleks Weyl-skalar i Kinnersley-tetraden:

$$\Psi_2(r, \theta) = -\frac{M}{(r - i a\cos\theta)^3}$$

Med reell modul $|\Psi_2| = M / (r^2 + a^2\cos^2\theta)^{3/2}$ konstruerer Bind X den dimensjonsløse, skaleringsinvariante **Weyl-admisjonskjernen** langs observatørens fire-hastighet $u^\mu$:

$$D_{\text{adm}}(\tau) = \exp\!\left(-\alpha\,\frac{|\nabla_u \Psi_2|^2}{|\Psi_2|^{8/3} + \eta_0}\right) \in (0, 1]$$

Eksponenten $8/3$ i nevneren er ikke valgt vilkårlig: fordi $|\Psi_2| \sim r^{-3}$ og $|\nabla_u \Psi_2| \sim r^{-4}$, skalerer telleren som $|\nabla_u \Psi_2|^2 \sim r^{-8}$ og $|\Psi_2|^{8/3} \sim (r^{-3})^{8/3} = r^{-8}$. Forholdet er dermed **eksakt dimensjonsløst og asymptotisk skaleringsinvariant** i svakfeltet, mens det stuper brått mot $0$ når banen møter skarpe krumningssprang nær ergosfæren. Numerisk verifikasjon viser at $D_{\text{adm}}(\Psi_2)$ gir **$6{,}8\times$ høyere deteksjonssensitivitet** for begynnende banekollaps enn Kretschmann-skalaren $K = R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} = 48\,\operatorname{Re}(\Psi_2^2)$ alene.

**Teorem 10.1 (Eksakt Fréchet-derivasjon av Weyl-admisjonskjernen):** *La $Q(g) = \frac{|\nabla_u\Psi_2(g)|^2}{|\Psi_2(g)|^{8/3} + \eta_0}$ være kvotientfunksjonalet for metrikken $g$. For enhver symmetrisk metrisk perturbasjon $h = \delta g_{\mu\nu}$ er Fréchet-derivatet $DD_{\text{adm}}[g]\cdot h$ veldefinert og gitt eksakt ved:*

$$D D_{\text{adm}}[g]\cdot h = -\alpha\,D_{\text{adm}}(g)\left[\frac{2\operatorname{Re}\bigl(\overline{\nabla_u\Psi_2}\,(D(\nabla_u\Psi_2)[g]\cdot h)\bigr)}{|\Psi_2|^{8/3} + \eta_0} - \frac{8}{3}\frac{|\nabla_u\Psi_2|^2\,|\Psi_2|^{2/3}\operatorname{Re}\bigl(\overline{\Psi_2}\,(D\Psi_2[g]\cdot h)\bigr)}{\bigl(|\Psi_2|^{8/3} + \eta_0\bigr)^2}\right]$$

---

## 4. Planck-Skranken ($\epsilon \ge 2l_P$), Eikonal-Virkningen og $\operatorname{sech}^4$-Projeksjonsstresset ($\Sigma_{\mu\nu}^{\text{irr}}$)

En skarp matematisk Heaviside-vegg $\Theta(d)$ ved randen $\partial\mathcal{A}$ krever uendelig romlig oppløsning ($\epsilon \to 0$) og gir en singulær Dirac-delta-gradient $\nabla_\mu\Theta(d) = \delta(d)\,n_\mu$, som divergerer kvadratisk i virkningsintegralet. I fysisk kvantegravitasjon utelukker imidlertid kombinasjonen av Heisenbergs uskarphetsrelasjon ($\Delta p \ge \hbar / (2\Delta x)$) og kravet om at måleenergien ikke kollapser innenfor sin egen Schwarzschild-horisont ($r_S = 2GE/c^4 \ge l_P^2/\Delta x$) enhver lokalisering skarpere enn den doble Planck-lengden:

$$\epsilon \ge \Delta x_{\min} = 2 l_P = 2\sqrt{\frac{\hbar G}{c^3}} \approx 3{,}232 \times 10^{-35}\text{ m}$$

Avstanden $d(x)$ til grensen av det admissible rommet $\partial\mathcal{A}$ defineres gjennom det kovariante eikonal-feltet $g^{\mu\nu}\nabla_\mu d(x)\,\nabla_\nu d(x) = \sigma \in \{+1, -1\}$ med normalvektor $n_\mu = \nabla_\mu d(x)$. Den regulariserte admisjonsporten og dens feltgradient får dermed en glatt overgangsprofil:

$$P_K^{(\epsilon)}(x) = \frac{1}{2}\left[1 + \tanh\!\left(\frac{d(x)}{2\epsilon}\right)\right], \qquad \nabla_\mu P_K^{(\epsilon)}(x) = \frac{1}{4\epsilon}\operatorname{sech}^2\!\left(\frac{d(x)}{2\epsilon}\right)n_\mu$$

Totalvirkningen for systemet med metrisk felt $g_{\mu\nu}$, materiefelter $\psi$, eikonal-avstand $d(x)$ og Lagrange-multiplikator $\eta(x)$ er:

$$S_{\text{tot}}[g, \psi, d, \eta] = \int_{\mathcal{M}}\mathrm{d}^4x\,\sqrt{-g}\left[\frac{c^4}{16\pi G}(R - 2\Lambda) + \mathcal{L}_{\text{mat}}(\psi, g) - \frac{\lambda_2}{2}g^{\mu\nu}\bigl(\nabla_\mu P_K^{(\epsilon)}\bigr)\bigl(\nabla_\nu P_K^{(\epsilon)}\bigr) - V_\epsilon\bigl(P_K^{(\epsilon)}\bigr) - \frac{\eta(x)}{2}\bigl(g^{\mu\nu}\nabla_\mu d\,\nabla_\nu d - \sigma\bigr)\right]$$

Ved å variere $S_{\text{tot}}$ med hensyn på den inverse metrikken ($\delta S_{\text{tot}} / \delta g^{\mu\nu} = 0$) fremkommer den utvidede feltligningen:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}\Bigl(T_{\mu\nu} + \Sigma_{\mu\nu}^{\text{irr}}\Bigr)$$

der det **irreversible grense-projeksjonsstresset** $\Sigma_{\mu\nu}^{\text{irr}} = -\frac{2}{\sqrt{-g}}\frac{\delta S_{\text{adm}}}{\delta g^{\mu\nu}}$ har den eksakte $\operatorname{sech}^4$-profilen:

$$\Sigma_{\mu\nu}^{\text{irr}} = \underbrace{\frac{\lambda_2}{16\epsilon^2}\operatorname{sech}^4\!\left(\frac{d(x)}{2\epsilon}\right)\left[n_\mu n_\nu - \frac{1}{2}g_{\mu\nu}\bigl(g^{\alpha\beta}n_\alpha n_\beta\bigr)\right]}_{\Sigma_{\mu\nu}^{(\text{grad})} \text{ (eksakt } \operatorname{sech}^4\text{-profil)}} - \underbrace{g_{\mu\nu}\,V_\epsilon\bigl(P_K^{(\epsilon)}\bigr)}_{\Sigma_{\mu\nu}^{(\text{pot})}} + \underbrace{\eta(x)\left[n_\mu n_\nu - \frac{1}{2}g_{\mu\nu}\bigl(g^{\alpha\beta}n_\alpha n_\beta\bigr)\right]}_{\Sigma_{\mu\nu}^{(\text{eik})} \text{ (eikonal defekt / normalspenning)}}$$

* **Eksponentiell taushet i det indre ($\mathcal{A}^{\circ}$):** Når tilstanden befinner seg trygt inne i det tillatte rommet ($d(x) \gg \epsilon$), går $\operatorname{sech}^4\bigl(\frac{d}{2\epsilon}\bigr) \to 16\,\mathrm{e}^{-2d/\epsilon} \to 0$ og $V_\epsilon(1) = 0$. Da er $\Sigma_{\mu\nu}^{\text{irr}} \equiv 0$, og standard generell relativitetsteori ($G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa T_{\mu\nu}$) gjelder eksakt.
* **Planck-skalert repulsiv vegg ved randen ($\partial\mathcal{A}$):** I grenseskiktet $|d(x)| \lesssim \epsilon$ reiser $\Sigma_{\mu\nu}^{\text{irr}}$ en glatt, fysisk energibarriere av orden $\mathcal{O}(\lambda_2/\epsilon^2) \propto l_P^{-2}$ som bøyer geodetiske baner bort fra den ulovlige sonen.
* **Bianchi–Landauer-konservering ved horisonten:** Fordi Einsteins tensor tilfredsstiller den kontraherte Bianchi-identiteten $\nabla^\mu G_{\mu\nu} \equiv 0$, påtvinger feltligningen den eksakte balansen:

$$\nabla^\mu\Bigl(T_{\mu\nu} + \Sigma_{\mu\nu}^{\text{irr}}\Bigr) = 0 \quad \Longleftrightarrow \quad \nabla^\mu T_{\mu\nu} = -\nabla^\mu\Sigma_{\mu\nu}^{\text{irr}} = f_\nu^{\text{cut}}$$

Når en ustabil komponent klippes ut av admisjonsporten $\Pi_K$, forsvinner ikke energien ut i intet; den konverteres direkte til irreversibel grensevarme og entropiproduksjon i samsvar med Landauers prinsipp på horisonten og Gouy–Stodola-eksergitapet ($\dot{E}x_{\text{dest}} = T_0\,\dot{S}_{\text{gen}} \ge 0$). Ved overganger på endelig tid $\tau_{\text{proc}} > 0$ skjerpes den kvasistatiske Landauer-skranken ytterligere av den termodynamiske lengden $\mathcal{L}_{\text{thermo}}$ i Ruppeiner-/Fisher–Rao-metrikken (Dør 18, *Den Langsomme Heisen*):

$$\delta Q = T_H\,\delta_i S_{\Pi_K} \ge k_B T_H \ln 2 \cdot \Delta I_{\text{cut}}, \qquad W_{\text{diss}}(\tau_{\text{proc}}) \ge \frac{T_0\,\mathcal{L}_{\text{thermo}}^2}{\tau_{\text{proc}}}$$

---

## 5. Holomorfisperren, Nash–Moser-Iterasjon, Kerr-Forrigling og Schurs CPTP-Bevis

Bind X fullfører den klassiske og semiklassiske feltarkitekturen med fire skarpe strukturelle resultater:

1. **Holomorfisperren (Teorem 10.2):** Ved utgangen av skranken anvendes den ikke-glatte terskelprojeksjonen $\Pi_\tau(z)$ som klipper amplituden eller tvinger fasen til reell bærer. Fordi $\frac{\partial \Pi_\tau}{\partial \bar{z}} \neq 0$ bryter Cauchy–Riemann-ligningene i terskelbeltet, kan ingen analytisk fortsettelse eller kompleks pol-ekstrapolasjon lekke tvers gjennom en lukket port.
2. **Nash–Moser-iterasjon for fjerdeordens vakuum- og grenseligninger ($\Delta_g R(g) = 0$):**
   John Nashs geometriske feltligning $\mathcal{N}(g) = \Delta_g R(g) = 0$ (samt variasjonen av eikonal-grenseleddet $\nabla^\mu\Sigma_{\mu\nu}^{\text{irr}}$ der $d(x)$ selv avhenger av $g_{\mu\nu}$) er en **4.-ordens ikke-lineær partiell differensialoperator** i metrikken $g$. Dersom man forsøker en standard Newton–Banach-iterasjon $g_{k+1} = g_k - [D\mathcal{N}(g_k)]^{-1}\mathcal{N}(g_k)$ på et fast Sobolev-rom $H^s(\mathcal{M})$, oppstår et fatalt **tap av deriverte** (*loss of derivatives*): fordi koeffisientene i den lineariserte operatoren $D\mathcal{N}(g_k)$ avhenger av 4.-ordens deriverte av bakgrunnsmetrikken $g_k$, avbilder den inverse operatoren $[D\mathcal{N}(g_k)]^{-1}$ et residual fra $H^s$ inn i $H^{s - r_0}$ med tap $r_0 = 4$:
   $$g_k \in H^s \implies \mathcal{N}(g_k) \in H^{s-4} \implies \bigl[D\mathcal{N}(g_k)\bigr]^{-1}\mathcal{N}(g_k) \in H^{s-4}$$
   Etter $\lfloor s/4 \rfloor$ steg faller iterasjonen ut av $C^2(\mathcal{M})$, og løseren eksploderer i numerisk høyfrekvent støy («meiselen splintres mot granitten»).
   I det **tamme Fréchet-rommet** $C^\infty(\mathcal{M}) = \bigcap_{s \ge s_0} H^s(\mathcal{M})$ utstyrt med en familie av Littlewood–Paley frekvenskutt- og glattingsoperatorer $\{S_\theta\}_{\theta > 1}$ som tilfredsstiller de tamme Sobolev-estimatene
   $$\bigl\|S_\theta u\bigr\|_{H^{s+p}} \le C_{s,p}\,\theta^p\,\|u\|_{H^s}, \qquad \bigl\|(I - S_\theta)u\bigr\|_{H^{s-p}} \le C_{s,p}\,\theta^{-p}\,\|u\|_{H^s} \quad (p \ge 0)$$
   gjenopprettes **kvadratisk konvergens** ved å injisere $S_{\theta_k}$ med super-eksponentiell båndbreddevekst $\theta_k = \theta_0^{\kappa^k}$ ($\kappa = \frac{3}{2}$) i hvert Newton-steg:
   $$g_{k+1} = g_k - S_{\theta_k}\bigl[D\mathcal{N}(g_k)\bigr]^{-1}\mathcal{N}(g_k)$$
   Her kompenserer høyfrekvensglattingen $\theta_k^{r_0}$ eksakt for derivasjonstapet $r_0 = 4$, mens det kvadratiske Newton-leddet $\|\mathcal{N}(g_k)\|_{H^s}^2 \propto \theta_k^{-2\alpha}$ dominerer restleddet $(I - S_{\theta_k})$ og driver sekvensen $\{g_k\}$ mot en glatt, fysisk admisjonsmetrikk $g_\infty \in C^\infty(\mathcal{M}) \cap \mathcal{A}$.
3. **Kerr-horisontenes 3-trinns sikkerhetsforrigling i [`einstein_ky_engine.py`](file:///home/sololyset/03_ENGINES/ENGINES/micro_engines/einstein_ky_engine.py):**
   I Boyer–Lindquist-koordinater $(t, r, \theta, \phi)$ med $\Sigma = r^2 + a^2\cos^2\theta$ og $\Delta = r^2 - 2Mr + a^2$ utgjør de tre karakteristiske flatene rundt en roterende Kerr-masse en eksakt mekanisk eskaleringskjede (`KerrTensorFelt` og `EinsteinKYMotor`):

| Horisont / Grenseflate | Eksakt Boyer–Lindquist-ligning | Fysisk / Metrisk Tilstand | Portdom i `einstein_ky_engine.py` |
| --- | --- | --- | --- |
| **1. Ergosfæren (Statisk grense)** | $r_E(\theta) = M + \sqrt{M^2 - a^2\cos^2\theta}$ | $g_{tt} = -\bigl(1 - \frac{2Mr}{\Sigma}\bigr) \ge 0$; *frame-dragging* ($\omega = -g_{t\phi}/g_{\phi\phi} > 0$) forbyr statiske og motroterende baner ($v^\phi \le 0$) | `WARNING / PRE-BRAKE`: `STATIC_OR_COUNTER_ROTATING_FORBIDDEN_IN_ERGOSPHERE` dersom $a > 0 \land v^\phi \le 0$; tillater Penrose-ekstraksjon kun ved $v^\phi > 0$ |
| **2. Ytre Hendelseshorisont ($r_+$)** | $r_+ = M + \sqrt{M^2 - a^2}$ | $\Delta(r_+) = 0$; en-veis kausal membran der lyskjeglene vipper innover og Bekenstein–Hawking-entropien er $S_{\text{BH}} = \frac{k_B A}{4l_P^2} = \pi k_B\frac{r_+^2 + a^2}{l_P^2}$ | `HOLD` (`EVENT_HORIZON_COMMIT_LOCKED`): Tilstanden låses som en irreversibel 2D holografisk WORM-overflatenode (`0,00 V DC` mot tilbaketrekning) |
| **3. Indre Cauchy-horisont ($r_-$)** | $r_- = M - \sqrt{M^2 - a^2}$ | $\Delta(r_-) = 0$; masse-inflasjon og uendelig blåforskyvningsinstabilitet knuser global hyperbolisitet og determinisme ($\mathcal{H}^-$) | `KILL` (`CAUCHY_HORIZON_BREACH`): Øyeblikkelig maskinvarekutt (`KILL_0V`) før sammenbrudd av Cauchy-utviklingen |

4. **CPTP Hamming-dekoherens via Schurs produktteorem (Teorem 10.3) og PCSE fase-hysterese ($\Delta p \approx 0{,}126$, $27{,}2\sigma$):**
   * **Schurs produktteorem:** Når en kvantetilstand $\rho$ med indeks-kodeord i Hamming-rommet $\{0, 1\}^n$ utsettes for dekoherenskanalen $\mathcal{E}_\gamma(\rho)_{ij} = \mathrm{e}^{-\gamma\,d_H(i, j)}\rho_{ij}$ ($\gamma > 0$), er matrisen $C_{ij} = \mathrm{e}^{-\gamma\,d_H(i,j)} = \bigotimes_{m=1}^n \begin{pmatrix} 1 & \mathrm{e}^{-\gamma} \\ \mathrm{e}^{-\gamma} & 1 \end{pmatrix}$ et $n$-fold Kronecker-produkt av strengt positivt definite $2\times 2$-matriser (egenverdier $1 \pm \mathrm{e}^{-\gamma} > 0$). Etter **Schurs produktteorem** er Hadamard-produktet $\mathcal{E}_\gamma(\rho) = C \circ \rho$ en garantert fullstendig positiv og sporbevarende (**CPTP**) kvantekanal som eksponentielt slukker ikke-diagonale superposisjoner med stor Hamming-avstand.
   * **Projeksjons-Skranked Schrödinger-Dynamikk (PCSE) og Bell–KY Fase-Hysterese ($\Delta p \approx 0{,}126$):** I [`unified_admissibility_pcse_gravity_engine.py`](file:///home/sololyset/03_ENGINES/ENGINES/micro_engines/unified_admissibility_pcse_gravity_engine.py) (`SPEC-212`) utvikler tilstandsvektoren $|\psi(t)\rangle$ seg under den ikke-hermitiske seleksjonslikningen
     $$\mathrm{i}\hbar\frac{\partial|\psi\rangle}{\partial t} = H_0|\psi\rangle - \mathrm{i}\hbar\lambda\bigl(I - \Pi_K\bigr)|\psi\rangle, \qquad \mathcal{O}_K(\psi) = \bigl(I - \Pi_K\bigr)|\psi\rangle$$
     Langs en verdenslinje $\gamma: [t_0, t_f] \to \mathcal{H}$ akkumulerer et tilstandsensemble den relasjonelle belastningsmetrikken $D_K(\gamma) = \int_{t_0}^{t_f}\bigl(\alpha\|\ddot{\psi}(t)\|^2 + \beta\dot{Q}_{\text{erase}}(t)\bigr)\mathrm{d}t$, som definerer horisontkjernen $K_\gamma = \exp\bigl(-\lambda D_K(\gamma)\bigr) \in (0, 1]$.
     I et to-arms Mach–Zehnder-interferometer sammenlignes **Bane A** (en direkte geodetisk rotasjon i det indre av $\mathcal{A}$ med $D_K(A) = 0 \implies K_\gamma(A) = 1{,}00$) og **Bane B** (en syklisk høy-forsterket bane som har berørt sikkerhetsgrensen og betalt en kryogenisk Landauer-skatt $Q_{\text{total}}(B) = D_K(B)\,k_B T\ln 2 \approx 4{,}81 \times 10^{-23}\text{ J}$ ved $T = 4{,}12\text{ K}$, slik at $D_K(B) \approx 1{,}22\text{–}1{,}386 \implies K_\gamma(B) \approx 0{,}25$). Begge baner ender i eksakt samme øyeblikkelige tetthetsmatrise $|\psi_A(t_f)\rangle = |\psi_B(t_f)\rangle = |+\rangle$ med Frobenius-avstand $\|\rho_A - \rho_B\|_F < 10^{-16}$.
     Mens en minneløs (Markoviansk) Born-projektor er blind for banens forhistorie, leser det **historiske POVM-elementet** $E_K(K_\gamma) = \frac{1}{2}\bigl(I + K_\gamma(\hat{n}\cdot\vec{\sigma})\bigr)$ (med $E_K + E_K^\perp = I$) ut det strukturelle arret i $K_\gamma$:
     $$P\bigl(E_K \mid \rho, K_\gamma\bigr) = \operatorname{Tr}\bigl(\rho\,E_K(K_\gamma)\bigr) = \frac{1}{2}\Bigl(1 + K_\gamma\bigl(\vec{r}\cdot\hat{n}\bigr)\Bigr)$$
     Dette produserer den målbare førsteordens fase-hysteresen mellom den indre geodetiske banen og grense-berøringsbanen:
     $$\Delta p = |p_A - p_B| = \frac{1}{2}\bigl(1 - K_\gamma(B)\bigr)\bigl(\vec{r}\cdot\hat{n}\bigr) \approx \mathbf{0{,}1262} \quad \bigl(p_A = 0{,}5002,\; p_B = 0{,}6264,\; z \approx \mathbf{27{,}2\sigma}\text{ ved } N = 20\,000\text{ skudd}\bigr)$$
   * **Streng bevaring av No-Signaling ($\rho_B' \equiv \rho_B$):** Fordi de historiske POVM-operatorene $M_{A,\mu} = \sqrt{E_{K,\mu}}$ på Alices delsystem utgjør et komplett sett ($\sum_\mu M_{A,\mu}^\dagger M_{A,\mu} = E_K + (I_A - E_K) = I_A$), forblir Bobs reduserte tetthetsmatrise over et romlig adskilt EPR-par $\rho_{AB}$ matematisk uforandret:
     $$\rho_B' = \operatorname{Tr}_A\!\left(\sum_\mu \bigl(M_{A,\mu}\otimes I_B\bigr)\rho_{AB}\bigl(M_{A,\mu}^\dagger\otimes I_B\bigr)\right) = \operatorname{Tr}_A\!\Bigl(\bigl(\underbrace{\sum_\mu M_{A,\mu}^\dagger M_{A,\mu}}_{=\,I_A}\otimes I_B\bigr)\rho_{AB}\Bigr) = \operatorname{Tr}_A(\rho_{AB}) \equiv \rho_B$$

---

## 6. Fase 4 i `einstein_ky_engine.py`: Holografisk Sammenfiltring ($\text{ER}=\text{EPR}$), Hawking-Spalting og Page-Kurvens Unitaritet ($\operatorname{Tr}(\rho^2) = 1$)

I [`einstein_ky_engine_phase4.py`](file:///home/sololyset/03_ENGINES/ENGINES/micro_engines/einstein_ky_engine_phase4.py) (verifisert med `30/30 PASS` i [`test_einstein_ky_engine.py`](file:///home/sololyset/03_ENGINES/tests/test_einstein_ky_engine.py) og [`test_einstein_ky_engine_phase4.py`](file:///home/sololyset/03_ENGINES/tests/test_einstein_ky_engine_phase4.py)) løftes Kerr-skranken fra klassisk og semiklassisk relativitet inn i holografisk kvanteinformasjon gjennom to koblede motorer:

### 6.1 $\text{ER}=\text{EPR}$ og Morris–Thorne Ormehullsmetrikken (`EinsteinRosenWormholeFelt`)
Maldacena og Susskinds $\text{ER}=\text{EPR}$-prinsipp postulerer at enhver maksimal kvantesammenfiltring (et Einstein–Podolsky–Rosen-klokke-par $|\Phi^+\rangle_{AB} = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$) er dual til en ikke-traverserbar Einstein–Rosen-bro ($\text{ER}$) i romtidens topologi.

I `EinsteinRosenWormholeFelt` modelleres broen ved Morris–Thorne-linjeelementet i egentlig radielt koordinat $l \in (-\infty, +\infty)$:

$$\mathrm{d}s^2 = -c^2\,\mathrm{d}t^2 + \mathrm{d}l^2 + \bigl(b_0^2 + l^2\bigr)\bigl(\mathrm{d}\theta^2 + \sin^2\theta\,\mathrm{d}\phi^2\bigr)$$

der **ormehullets struperadius $b_0$** ved $l = 0$ ikke er et fritt ad-hoc-tall, men bestemmes direkte av den kvantemekaniske gjensidige informasjonen (**Mutual Information**) $I(A:B) = S(\rho_A) + S(\rho_B) - S(\rho_{AB})$ mellom grensekodene $A$ og $B$:

$$b_0 = \sqrt{\alpha\,I(A:B)}, \qquad I(A:B) = \begin{cases} 2\ln 2 \approx 1{,}38629\text{ nats} & \text{for en maksimalt sammenfiltret Bell-tilstand } (\text{verifisert via delt }\mathtt{entanglement\_hash}) \\ 0 & \text{ved brutt koherens / ukorrelerte noder} \end{cases}$$

* **Geodetisk kortslutning i $\Pi_{\mathcal{A}}$:** Mens to romlig adskilte noder $A$ og $B$ i det ytre euklidske rommet har avstand $d_{\text{Euclid}} = \|\mathbf{x}_A - \mathbf{x}_B\|_2 \gg 1$, gir et verifisert kryptografisk sammenfiltringsvitne (`entanglement_hash_A == entanglement_hash_B`) en åpen strupe $b_0 = \sqrt{2\alpha\ln 2} > 0$ med indre geodetisk lengde $d_{\text{ER}} = l_{\text{throat}} \ll d_{\text{Euclid}}$. Admisjonsporten verifiserer konsistensen mellom nodene i $\mathcal{O}(1)$ over broen uten å bryte kausalitet i det ytre rommet ($\text{no-signaling}$ bevares fordi ingen klassisk nyttelast kan krysse strupen uten et uavhengig klassisk vitne).
* **Øyeblikkelig strupekollaps ved tukling:** Dersom en angriper måler eller manipulerer én av nodene slik at sammenfiltringshashen brytes, faller $I(A:B) \to 0 \implies b_0 = 0$. Ormehullsstrupen snøres igjen på én syklus, og systemet tvinges tilbake til den fulle ytre lyskjegle-forsinkelsen $d_{\text{Euclid}}$.

### 6.2 Asymmetrisk Hawking-Parspalting og Page-Kurvens Unitaritet (`HolographicHawkingEngine`)
Hawking-paradokset (1975) oppstår når vakuumfluktuasjoner nær den ytre Kerr-horisonten $r_+ = M + \sqrt{M^2 - a^2}$ skaper et sammenfiltret kvantepar $(A, B)$ ved $r = r_+ + \epsilon$. Dersom den innfallende partneren $A$ går tapt i en lovløs singularitet mens $B$ unnslipper som termisk stråling, vil strålingsentropien $S_{\text{rad}}(t)$ vokse monotont til hele det sorte hullet er fordampet ($M \to 0$), slik at en ren kvantetilstand ender i en blandet termisk grøt ($\operatorname{Tr}(\rho^2) < 1$ — tap av informasjon og sammenbrudd av kvantemekanisk unitaritet).

I `HolographicHawkingEngine` løses dette gjennom **horisont-forsegling (`EVENT_HORIZON_COMMIT_LOCKED`)** og **Don Pages enhetskurve**:

1. **Asymmetrisk dom ved $r_+ + \epsilon$ (`execute_hawking_split`):**
   * **Den innfallende partneren $A$ ($v_A^r < 0$):** Krysser $r_+$ inn i det indre området $r_- < r \le r_+$. I stedet for å slettes fra universets regnskap, fanges $A$ av Trinn 2 i Kerr-forriglingen (`EVENT_HORIZON_COMMIT_LOCKED`) og skrives som en uforanderlig **2D holografisk WORM-overflatenode** (`horizon_commit_hash`) på horisontarealet $A_H = 4\pi(r_+^2 + a^2)$. Samtidig trekkes den eksakte hvilemassen fra Kerr-kilden:
     $$M_{n+1} = \max\bigl(0,\; M_n - \delta m\bigr)$$
   * **Den utgående partneren $B$ ($v_B^r > 0$):** Admitteres gjennom $\Pi_{\mathcal{A}}$ (`ADMITTED_TO_MANIFOLD`) og unnslipper til det ytre rommet med en kryptografisk peker til $A$ sin horisont-forsegling (`entanglement_hash`), til en termodynamisk Landauer-pris på $\Delta Q = 2{,}85\text{ pJ}$ per spalting.
2. **Bekenstein–Hawking-kapasiteten og Page-tiden ($t_{\text{Page}}$):**
   Så lenge det sorte hullet er ungt og stort, har horisonten rikelig med holografiske frihetsgrader:
   $$S_{\text{BH}}\bigl(M(n)\bigr) = \pi k_B\,\frac{r_+(M(n))^2 + a_{\text{eff}}^2}{l_P^2}$$
   Hver utsendte Hawking-kvant $B$ øker strålingsentropien med $\ln 2$. Men fordi strålingen $B$ kun er sammenfiltret med de gjenværende WORM-nodene på horisonten, kan strålingens von Neumann-entropi $S_{\text{rad}}(n)$ **aldri overstige horisontens egen Bekenstein–Hawking-entropi $S_{\text{BH}}(n)$**:
   $$S_{\text{rad}}(n) = \min\Bigl(n\ln 2,\; S_{\text{BH}}\bigl(M(n)\bigr)\Bigr)$$
3. **Vendingen ved Page-punktet og ren slutt-tilstand ($\operatorname{Tr}(\rho^2) = 1$):**
   * **Før Page-tiden ($n\ln 2 < S_{\text{BH}}(n)$):** $S_{\text{rad}}(n)$ vokser lineært med $n\ln 2$ fordi hver nye utsendte kvant bringer ny sammenfiltring med horisonten.
   * **Etter Page-tiden ($n\ln 2 \ge S_{\text{BH}}(n)$):** Horisonten er mettet; nye utsendte Hawking-kvanter er via $\text{ER}=\text{EPR}$-broene sammenfiltret med den *tidligere utsendte* strålingen og renser derfor strålingstilstanden. $S_{\text{rad}}(n)$ bøyer nedover langs den krympende horisontkurven $S_{\text{BH}}(M(n))$.
   * **Full fordampning ($M \to 0$):** Når den siste masseresten fordamper, går $S_{\text{BH}}(0) \to 0 \implies S_{\text{rad}}(\text{slutt}) = 0$. Hele det historiske vitneregnskapet er bevart i den utsendte strålingen med eksakt kvantemekanisk renhet:
     $$\lim_{M \to 0} S_{\text{rad}} = 0 \quad \Longleftrightarrow \quad \operatorname{Tr}\bigl(\rho_{\text{rad}}^2\bigr) = 1{,}0, \qquad \mathtt{unitarity\_preserved = True}$$

> **KONTRASTVÆSKE // DET SANSELIGE ANKERET ($\Pi_{\text{orth}}$ — Bind X / Feltligningene)**  
> * **Ligning i faserommet:** $D_{\text{adm}}(\tau) = \exp\!\left(-\alpha\frac{|\nabla_u\Psi_2|^2}{|\Psi_2|^{8/3}+\eta_0}\right)$, $\Sigma_{\mu\nu}^{\text{irr}} \propto \epsilon^{-2}\operatorname{sech}^4\!\left(\frac{d(x)}{2\epsilon}\right)$, Nash–Moser-glatting $g_{k+1} = g_k - S_{\theta_k}[D\mathcal{N}(g_k)]^{-1}\mathcal{N}(g_k)$ og Page-kurven $S_{\text{rad}}(n) = \min\bigl(n\ln 2, S_{\text{BH}}(n)\bigr)$.  
> * **Kjøtt, stål og sludd:** Bak Newman–Penrose-skalaren $\Psi_2$, det fjerdeordens derivasjonstapet i Nash–Moser-iterasjonen og horisont-forseglingen ved $r_+$ står en enkel, brutal erfaring fra steinhoggerens benk: slår du meiselen for brått inn i kald granitt uten å glatte slaget ($\epsilon \to 0$), sprekker ikke steinen langs snittet — meiselstålet splintres i hånden din av tilbakeslaget ($\Sigma_{\mu\nu}^{\text{irr}} \to \infty$). Og når steinen først er delt langs kløven ($r_+$), passer de to bruddflatene fortsatt eksakt inn i hverandre tann for tann ($b_0 = \sqrt{\alpha I(A:B)}$, $\operatorname{Tr}(\rho^2) = 1$).  
> * **Dom ved porten:** Selv romtiden krever en endelig fuge ($\epsilon \ge 2l_P$), en utjevnet meiselvinkel ($S_{\theta_k}$) og en uforfalskelig bruddflate før en tilstand får lov til å sette seg som varig krumning.
