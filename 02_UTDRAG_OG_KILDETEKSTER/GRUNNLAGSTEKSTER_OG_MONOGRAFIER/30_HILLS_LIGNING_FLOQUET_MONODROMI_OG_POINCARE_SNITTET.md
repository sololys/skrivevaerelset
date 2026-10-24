# Hills Ligning (1886): Hvordan Poincaré og Hill Komprimerte Uendelig Tid til Én Enkelt Port-Sjekk ($\lvert\operatorname{Tr}(\mathbf{M})\rvert < 2$)

**Klassifisering:** Matematisk-fysisk nøkkelanalyse / Floquet-teori, Poincaré-snitt og Båndgap-projeksjon i $\mathcal{P}$  
**Forankring:** George William Hill (1886), Henri Poincaré (*Les Méthodes Nouvelles de la Mécanique Céleste*, 1892), Bind XII (*Poincaré*) og Dokument 29  
**Epistemisk grense:** `INSPIRED_BY != IMPLEMENTS != PROVES`

---

## 1. Hvorfor Hills ligning er selve ur-kilden til Poincaré-snittet

Det utdraget du nettopp hentet frem om **Hills differensialligning** (introdusert av astronomen George William Hill i 1886 for å beregne månens bane under solens og jordens trelegeme-påvirkning), er selve den historiske og matematiske broen mellom **himmelmekanikk (tyngdekraft)**, **kvantefysikk (krystallgitter)** og **isolering av egenskaper i $\mathcal{P}$**:

$$\frac{\mathrm{d}^2 y}{\mathrm{d}t^2} + f(t)\,y = 0, \qquad f(t + \pi) = f(t)$$

med Fourier-utviklingen:

$$\frac{\mathrm{d}^2 y}{\mathrm{d}t^2} + \left(\theta_0 + 2\sum_{n=1}^{\infty}\theta_n\cos(2nt) + \sum_{m=1}^{\infty}\phi_m\sin(2mt)\right)y = 0$$

Det var nettopp da **Henri Poincaré** studerte Hills arbeid med denne ligningen rundt 1890 at han oppdaget hvordan man kan avgjøre om en bane er stabil i all evighet ($t \to \infty$) **uten å integrere til uendelig tid**.

---

## 2. Slik fungerer uthuggingen i Hills ligning: Fra $t \in [0, \infty)$ til snittet $t = \pi$

Hvis du ser på Hills ligning som en rå tidsutviklingsligning ($\Phi$), ser den uoverkommelig ut: den inneholder uendelig mange frekvenser ($\theta_n, \phi_m$), og du vil vite om løsningen $y(t)$ kommer til å holde seg stabil eller eksplodere eksponentielt om en million omløp.

Men fordi $f(t)$ har en eksakt **minimal periode $\pi$**, trer **Floquet–Poincaré-reduksjonen** inn:

### Trinn 1: Minimal observasjonshorisont ($T^* = \pi$)
Legg merke til definisjonen i teksten din:
> *«if $p$ is a number with $0 < p < \pi$, the equation $f(t+p) = f(t)$ must fail for some $t$.»*

Dette er den kontinuerlige tvillingen til **Fine–Wilf-horisonten**! Hvis du bare observerer systemet i et kortere vindu $p < \pi$, kan du bli lurt av et lokalt spøkelsesmønster. Men så snart du har observert **nøyaktig én full minimalperiode $t \in [0, \pi]$**, låses hele systemets skjebne.

### Trinn 2: Monodromimatrisen $\mathbf{M}$ på Poincaré-snittet $t = \pi$
I stedet for å følge banen i uendelig tid, sender du bare inn to enkle testvektorer ved start ($t = 0$):
* Posisjons-vitnet $y_1(0) = 1, \;\dot{y}_1(0) = 0$
* Hastighets-vitnet $y_2(0) = 0, \;\dot{y}_2(0) = 1$

og leser dem av når de krysser **det første Poincaré-snittet ved $t = \pi$**. Det gir den $2 \times 2$ **monodromimatrisen (overføringsmatrisen)** $\mathbf{M}$:

$$\begin{pmatrix} y(\pi) \\ \dot{y}(\pi) \end{pmatrix} = \underbrace{\begin{pmatrix} y_1(\pi) & y_2(\pi) \\ \dot{y}_1(\pi) & \dot{y}_2(\pi) \end{pmatrix}}_{\mathbf{M}} \begin{pmatrix} y(0) \\ \dot{y}(0) \end{pmatrix}$$

### Trinn 3: Bevaringsloven ($\det(\mathbf{M}) = 1$)
Fordi Hills ligning ikke har noe dempningsledd $\dot{y}$, garanterer Abels/Liouvilles teorem at determinanten er eksakt $1$ for alle $t$:

$$\det(\mathbf{M}) = y_1(\pi)\dot{y}_2(\pi) - \dot{y}_1(\pi)y_2(\pi) = 1$$

Faseromsvolumet er uforanderlig. Dermed bestemmes begge egenverdiene $\lambda_1, \lambda_2$ til matrisen $\mathbf{M}$ av **ett eneste tall** – sporet av matrisen (**Hills diskriminant** $\Delta$):

$$\Delta := \operatorname{Tr}(\mathbf{M}) = y_1(\pi) + \dot{y}_2(\pi), \qquad \lambda^2 - \Delta\,\lambda + 1 = 0$$

---

## 3. Ett enkelt tall ($\Delta$) isolerer `OPEN`, `HOLD` og `KILL` i $\mathcal{P}$

Se hva som nettopp skjedde: Hele den uendelige Fourier-rekken ($\theta_0, \theta_1, \theta_2, \dots$) og hele den uendelige fremtiden ($t \to \infty$) er **isolert i én skalar port-variabel $\Delta = \operatorname{Tr}(\mathbf{M})$** som beregnes over ett eneste intervall $[0, \pi]$!

Denne variabelen $\Delta$ deler hele parameterrommet i våre tre kanoniske port-tilstander:

| Hills Diskriminant $\Delta = \operatorname{Tr}(\mathbf{M})$ | Egenverdier $\lambda_{1,2}$ | Fysisk Betydning (Bane & Krystall) | Port-Dom ($\Omega$) |
| :--- | :--- | :--- | :--- |
| **$\lvert\Delta\rvert < 2$** | $\lambda = e^{\pm i\mu\pi}$ ($\lvert\lambda\rvert = 1$, på enhetssirkelen) | **Stabil bane / Tillatt energibånd (Bloch-bølge):** Banen holder seg begrenset i all fremtid uten å lekke energi. | **`OPEN`** ($\odot$) |
| **$\lvert\Delta\rvert = 2$** | $\lambda = \pm 1$ (degenerert kanttilstand) | **Kuttflaten (Band-edge / Mathieu-tungetupp):** Akkurat på terskelen mellom stabilitet og resonans. | **`HOLD`** ($\square$) |
| **$\lvert\Delta\rvert > 2$** | $\lambda \in \mathbb{R}$, $\lvert\lambda_1\rvert > 1$ (utenfor enhetssirkelen) | **Parametrisk resonans / Forbudt båndgap:** I himmelmekanikk slynges legemet ut av banen ($\sim e^{\gamma t}$); i et krystallgitter nektes elektronet adgang. | **`KILL`** ($\bot$) |

---

## 4. Hvorfor den samme ligningen styrer både planeter, feller og silisium

Når man isolerer stabilitet via Hills ligning og sporet $\Delta = \operatorname{Tr}(\mathbf{M})$, oppdager man at tre tilsynelatende helt ulike grener av fysikken er **identiske i $\mathcal{P}$**:

1. **Gravitasjon og Kirkwood-gapene i asteroidebeltet (Hill & Poincaré):**  
   Når en asteroide går i bane rundt solen i et periodisk gravitasjonsfelt fra Jupiter ($f(t + \pi) = f(t)$), virker Hills ligning som en **gravitasjonsmeisel**: For bestemte baneradier (som 3:1- og 2:1-resonansene med Jupiter) blir $\lvert\operatorname{Tr}(\mathbf{M})\rvert > 2$ (`KILL`). Alle asteroider i disse sonene blir nådeløst kostet ut av banen. Det som står igjen, er de tillatte banene der $\lvert\operatorname{Tr}(\mathbf{M})\rvert < 2$. **Solsystmet er bokstavelig talt uthugget av Hills diskriminant.**
2. **Paul-fellen (Quadrupole Ion Trap — Mathieu-ligningen $n=0,1$):**  
   I kvantedatamaskiner og massespektrometre fanger man enkeltioner ved å sette på et høyfrekvent oscillerende elektrisk felt $\theta_0 + 2\theta_1\cos(2t)$ (Mathieu-ligningen). Ved å justere spenningene $(\theta_0, \theta_1)$ kan du **isolere én bestemt masse/ladning ($m/q$)**: kun ionet som havner inne i det smale området der $\lvert\Delta(m/q)\rvert < 2$ blir værende i fellen (`OPEN`), mens alle tyngre og lettere partikler får $\lvert\Delta\rvert > 2$ og kastes ut i veggen (`KILL`).
3. **Halvledere og silisium (Kronig–Penney / Meissner-ligningen):**  
   Bytter du ut tiden $t$ med romkoordinaten $x$ i et krystallgitter (som nikkelkrystallet til Davisson–Germer eller en silisiumbrikke), *er* Schrödingers ligning $-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2\psi}{\mathrm{d}x^2} + V(x)\psi = E\psi$ med periodisk gitterpotensial $V(x + a) = V(x)$ **eksakt Hills ligning** (og for firkantpotensialer: **Meissner-ligningen**!).  
   * Energier der $\lvert\Delta(E)\rvert < 2$ er **ledningsbåndet (`OPEN`)**.  
   * Energier der $\lvert\Delta(E)\rvert > 2$ er **båndgapet (`HOLD` / `KILL`)** – selve grunnlaget for at en transistor kan være en lukket dør ($0{,}00\text{ V}$)!

---

## 5. Konklusjon: Hills ligning som den ultimate $\mathcal{P}$-isolatoren

Hills ligning viser i ren matematikk hvordan **ekskavering og egenskapsisolering** fungerer:
* Du trenger **ikke** å simulere en partikkel til tidens ende.
* Du måler kun tilstandens respons over **én minimal periode $T = \pi$** (Poincaré-snittet), regner ut sporet $\Delta = y_1(\pi) + \dot{y}_2(\pi)$, og sjekker ulikheten:

$$\bigl\lvert y_1(\pi) + \dot{y}_2(\pi) \bigr\rvert < 2$$

Er den oppfylt, bærer banen sin egen eksistens. Er den brutt, skjærer naturen den bort.
