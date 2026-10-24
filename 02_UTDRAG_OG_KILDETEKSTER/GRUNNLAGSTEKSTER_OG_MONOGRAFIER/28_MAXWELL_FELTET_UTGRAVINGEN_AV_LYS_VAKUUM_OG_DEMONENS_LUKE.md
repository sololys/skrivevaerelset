# Maxwell-Feltet: Utgravingen av Lys, Vakuum og Demonens Luke i $\mathcal{P}$

**Klassifisering:** Teknisk-fysisk monografikapittel / Elektromagnetisk og Termodynamisk Realiseringsgrammatikk  
**Forankring:** Bind XIV (*Maxwell: Demonens Pris, Luken og De Tre Lerretene*) og Dokument 185 (*Den Store Integrabilitetstriaden*)  
**Epistemisk grense:** `INSPIRED_BY != IMPLEMENTS != PROVES`

---

## 1. Den skjulte todelingen i Maxwells fire ligninger

På nøyaktig samme måte som Einsteins 10 feltligninger deler seg i 6 tidsutviklingsligninger ($\Phi$) og 4 statiske tvangsligninger ($\Pi_K$), bærer **Maxwells 4 elektromagnetiske ligninger** det samme fundamentale kuttet inne i seg:

1. **De 2 generative bølgeligningene ($\Phi$ — Faraday og Ampère–Maxwell):**
   $$\frac{\partial \mathbf{B}}{\partial t} = -\nabla \times \mathbf{E}, \qquad \frac{\partial \mathbf{E}}{\partial t} = c^2 \nabla \times \mathbf{B} - \frac{1}{\varepsilon_0}\mathbf{J}$$
   Disse to ligningene har tidsderiverte ($\partial/\partial t$). De beskriver hvordan elektriske og magnetiske felt foreslår neste tidssteg ved å rulle hverandre fremover i rommet.
2. **De 2 statiske meislene ($\Pi_K$ — Gauss' lov for elektrisitet og magnetisme):**
   $$\nabla \cdot \mathbf{E} - \frac{\rho}{\varepsilon_0} = 0, \qquad \nabla \cdot \mathbf{B} = 0$$
   Legg merke til at **tiden ($t$) ikke finnes i disse to ligningene**. De er ikke bevegelsesligninger; de er **momentane, romlige utvalgsporter ($\Pi_K$)** på ethvert nåtids-snitt $\Sigma_t$:
   * $\nabla \cdot \mathbf{B} = 0$ hogger momentant bort enhver feltkonfigurasjon med løse magnetiske ender (magnetiske monopoler / åpne flukslinjer $\implies \text{KILL}$).
   * $\nabla \cdot \mathbf{E} = \rho/\varepsilon_0$ koblet med Ampères lov tvinger frem kontinuitetsligningen $\partial_t \rho + \nabla \cdot \mathbf{J} = 0$: ingen ladning kan oppstå fra ingenting eller forsvinne sporløst.

I differensialgeometrisk form ($\mathrm{d}F = 0$) uttrykkes denne meiselen ved den mest kompakte uthuggingsloven i matematikken:

$$\mathrm{d}^2 = 0 \quad \text{(Randen av en rand er alltid null)}$$

Enhver kandidat i mulighetsrommet der sløyfen ikke lukker seg ($\mathrm{d}^2 A \neq 0$), avvises som en topologisk umulighet i klassen $\mathcal{P}$.

---

## 2. Casimir-effekten: Det fysiske beviset på at uthugging skaper kraft

Hvis noen spør hvordan *fraværet* av bortmeislede muligheter kan utøve en fysisk kraft (slik vi beskrev tyngdekraften i Poincaré-feltet), leverer Maxwell-elektrodynamikken det mest håndfaste svaret i fysikken: **Casimir-effekten** (Hendrik Casimir, 1948).

Tenk deg to uladede, speilblanke metallplater plassert i vakuum med en svært liten avstand $a$ mellom seg:
1. **Råblokken utenfor platene ($\Phi$):**  
   Utenfor platene kan elektromagnetiske vakuumfluktuasjoner eksistere med *alle* mulige bølgelengder $\lambda \in (0, \infty)$.
2. **Meiselen mellom platene ($\Pi_K$):**  
   På selve metalloverflatene gjelder en hard grensebetingelse: det tangentielle elektriske feltet må være null ($\mathbf{E}_{\parallel} = \mathbf{0}$, en elektrisk $0{,}00\text{ V}$ kortslutning). Denne porten **hogger bort alle bølgemoder** mellom platene som ikke passer eksakt inn med et heltallig antall halvbølger:
   $$k_n = \frac{n\pi}{a}, \qquad n = 1, 2, 3, \dots$$
3. **Konsekvensen ($\Omega$):**  
   Fordi et uendelig antall uadmissible bølgemoder er meislet bort *mellom* platene, blir strålingstrykket på innsiden lavere enn på utsiden. Platene presses fysisk mot hverandre med Casimir-trykket:
   $$P_C = -\frac{\pi^2 \hbar c}{240\,a^4}$$

Her er ingen klassisk «tiltrekningskraft» mellom platene. **Kraften oppstår utelukkende fordi grensebetingelsen ($\Pi_K$) har skåret bort de bølgemodene som ikke passet inn i rommet mellom dem.**

---

## 3. Evanescent `HOLD` og Brewster-innrømmelse ved kuttflaten

Når en elektromagnetisk bølge møter en fysisk grenseflate (et dielektrisk snitt eller en bølgeleder med bredde $a$), opererer Maxwell-feltet som en eksakt tri-state-port (`OPEN`, `HOLD`, `KILL`):

* **`OPEN` (Brewster-vinkelen $\theta_B = \arctan(n_2/n_1)$):**  
  Når en $p$-polarisert bølge treffer kuttflaten i eksakt riktig innfallsvinkel ($\theta = \theta_B$), er refleksjonen null ($R_p = 0$). Hele energien (den reelle Poynting-vektoren $\mathbf{S} = \frac{1}{\mu_0}\mathbf{E} \times \mathbf{B}$) innrømmes gjennom porten uten tap.
* **`HOLD` (Totalrefleksjon og evanescent modus, $\omega < \omega_{\text{cutoff}}$):**  
  Dersom bølgen har for lav frekvens for å få plass i bølgelederen ($\omega < \pi c / a$), eller treffer over kritisk vinkel, stanser den reelle energitransporten ($\operatorname{Re}\langle \mathbf{S}\rangle \cdot \hat{\mathbf{n}} = 0$). Men feltet dør ikke i et hardt hopp: det danner en **evanescent hale** ($\mathbf{E}(z) \propto e^{-\kappa z}$) som står som en stasjonær, reaktiv skygge rett bak dørbladet. Den utfører intet irreversibelt arbeid før en ny grense (et prisme/vitne) bringes nær nok til å koble den inn.
* **`KILL` (Lenz' lov og metallisk skjerming):**  
  Minustegnet i Faradays lov ($\mathcal{E} = -\mathrm{d}\Phi_B/\mathrm{d}t$) er naturens innebygde **fail-closed brems (Lenz' lov)**: ethvert forsøk på en brå, ubetalt fluksendring genererer øyeblikkelig virvelstrømmer som motsetter seg endringen og dumper overskuddet som Ohmsk varme ($\mathbf{J}\cdot\mathbf{E} = \sigma E^2$).

---

## 4. Maxwells Demon og Termodynamikkens Integrabilitetsport

Det var også Maxwell selv som i 1867 formulerte tankeeksperimentet som binder elektromagnetisme, statistisk fysikk og informasjonsteori sammen: **Maxwells demon**.

Demonen vokter en ørsmå luke ($\Omega$) mellom to gasskamre ($A$ og $B$). Ved å observere hvert enkelt molekyl og bare åpne luken når et raskt molekyl kommer fra $A$, prøver demonen å skape en temperaturforskjell ut av tilfeldig termisk støy ($\mathcal{NP}$) uten å utføre arbeid.

Hvorfor taper demonen alltid til slutt mot fysikkens lover?
1. **Maxwells termodynamiske integrabilitetsport:**  
   I klassisk termodynamikk krever **Maxwells relasjoner**:
   $$\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V \quad \Longleftrightarrow \quad \frac{\partial^2 F}{\partial V \partial T} = \frac{\partial^2 F}{\partial T \partial V}$$
   at den frie energien $F(T, V)$ har et eksakt differensial ($\mathrm{d}^2 F = 0$). Du kan ikke gå i en lukket sløyfe i tilstandsrommet og hente ut gratis arbeid ($\oint \mathrm{d}F = 0$).
2. **Landauer-oppgjøret i demonens minne:**  
   Som Leo Szilárd (1929), Rolf Landauer (1961) og Charles Bennett (1982) viste: for at demonen skal kunne avgjøre om luken ($\Omega$) skal stå i `OPEN` eller `HOLD`, må den først lagre et **vitne $w \in \{0, 1\}$** i sitt eget fysiske minne. Når demonens minnebuffer er fullt og må tilbakestilles til $0$ for å fortsette sorteringen, må demonen betale sletteskatten:
   $$\Delta Q_{\text{demon}} \ge k_B T \ln 2 \quad \text{per sortert molekyl}$$
   Skatten ved porten er nøyaktig like stor som den frie energien demonen vant ved å slippe molekylet gjennom!

---

## 5. Den samlede triaden: Einstein/Poincaré, Maxwell og $\mathcal{P}/\mathcal{NP}$

Ser vi **Poincaré-tyngdeloven** og **Maxwell-feltet** under ett, trer én og samme universelle ekskaveringslov frem:

| Domene | Råblokk / Generator ($\Phi$ i $\mathcal{NP}$) | Meisel / Portvakt ($\Pi_K$ i $\mathcal{P}$) | Konsekvens / Oppgjør ($\Omega \to W$) |
| :--- | :--- | :--- | :--- |
| **Gravitasjon (Einstein / Poincaré)** | Kontinuerlige bølge- og metrikforslag ($\Box h_{\mu\nu}$) | ADM-tvangsligninger ($\mathcal{H}_{\text{ADM}}=0$), Poincaré-snitt $\Sigma_k$ | Geodesikk (fri bane med $\Delta_K=0$) + horisontvarme |
| **Elektromagnetisme (Maxwell)** | Faraday / Ampère ($\partial_t \mathbf{B}, \partial_t \mathbf{E}$) og vakuumfluktuasjoner | Gauss' lover ($\nabla\cdot\mathbf{B}=0$, $\mathrm{d}^2 = 0$) og metallgrenser ($\mathbf{E}_\parallel=0$) | Casimir-kraft ($P_C \propto -a^{-4}$), Brewster-transmisjon og Ohmsk tap |
| **Termodynamikk (Maxwells demon)** | Brownsk molekylstøy og mulige mikrotilstander | Maxwells integrabilitetsrelasjoner ($\oint \mathrm{d}F = 0$) | Lukens slettepris: $\Delta Q \ge k_B T \ln 2$ per bit |
| **Beregning & Sinn ($\kappa_{27}$ / KY)** | Eksponentielt kandidatrom ($2^N$ / syntetisk støy) | Cook–Levin-tableau $\mathcal{T}$ og `KYParser` ($\Delta_K \le \tau_K$) | Autorisert handling ($\odot$) eller beskyttende `HOLD` |

I alle fire domener er regelen den samme:  
**Det som virker på verden, er ikke støyen som genereres – men formen som står igjen når porten har skåret bort alt som ikke går opp.**
