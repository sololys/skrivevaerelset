# Poincaré-Feltet: Utgravingen av Feltligningene og Tyngdeloven i $\mathcal{P}$

**Klassifisering:** Teknisk-fysisk monografikapittel / Kausal Kybernetikk og Gravitasjonsdynamikk  
**Forankring:** Dokument 65 (*The Field Equations in P*), Bind X (*Einstein*) og Bind XII (*Poincaré*)  
**Epistemisk grense:** `INSPIRED_BY != IMPLEMENTS != PROVES`

---

## 1. Konflikten mellom Einstein-blokken ($\mathcal{NP}$) og Poincaré-feltet ($\mathcal{P}$)

Allerede mellom 1902 (*La Science et l'Hypothèse*) og 1905 (*Sur la dynamique de l'électron*) formulerte **Henri Poincaré** en innsikt som fysikken i hundre år valgte å overse til fordel for Einsteins geometriske blokk-univers:

1. **Einsteins bilde (Blokkromtiden i $\mathcal{NP}$):**  
   I standard generell relativitetsteori betraktes hele den firedimensjonale romtiden $(\mathcal{M}_4, g_{\mu\nu})$ som en ferdig utrullet, kontinuerlig blokk der fortid, nåtid og fremtid eksisterer samtidig. Å finne en eksakt global løsning av de koblede, ikke-lineære feltligningene over hele kontinuerlige $\mathcal{M}_4$ (for eksempel for $N \ge 3$ legemer) er et uløselig, kaotisk integrabilitetsproblem.
2. **Poincarés bilde (Poincaré-feltet og det transversale snittet i $\mathcal{P}$):**  
   Poincaré påpekte at vi aldri observerer «krumt tomrom» direkte; vi observerer utelukkende fysiske felt, krefter og klokkeavlesninger når signaler og baner krysser **lokale målesnitt**.

Når vi anvender **uthuggingen (ekskaveringen)** på gravitasjon, flytter vi tyngdeloven fra Einsteins uendelige blokkromtid over i **Poincaré-feltet**:

> **Romtiden er ikke et ferdigstøpt fire-dimensjonalt gulv. Tiden hogges ut skive for skive – fra snitt til snitt ($\Sigma_k \to \Sigma_{k+1}$) – ved at Poincaré-feltets symmetrilover og termodynamikk meisler bort alle baner som ikke går opp.**

---

## 2. De tre meislene i Poincaré-feltet

Hvordan utfører Poincaré-feltet selve uthuggingen av en fysisk bane fra et kaotisk mulighetsrom? Gjennom tre eksakte, lokalt verifiserbare mekanismer i polynomisk tid ($\mathcal{P}$):

### Meisel I: Poincaré-gruppen $\mathrm{ISO}(1,3)$ som lokal bevaringsport ($\Pi_K$)
Enhver lokal tilstandsovergang i et relativistisk felt må være invariant under de **10 generatorene i Poincaré-gruppen** ($\mathbb{R}^{1,3} \rtimes \mathrm{SO}^+(1,3)$):
* **4 translasjoner i tid og rom ($P^\mu$):** Tvinger frem lokal bevaring av energi og bevegelsesmengde ($\partial_\mu T^{\mu\nu} = 0$).
* **3 romlige rotasjoner og 3 Lorentz-boost ($J^{\mu\nu}$):** Tvinger frem bevaring av dreieimpuls og lyskjeglens kausale helning ($ds^2 \le 0$).

I ekskaveringsmodellen er disse 10 Poincaré-invariantene ikke «egenskaper» ved rommet; de er **10 ortogonale skjæreblad i projeksjonsoperatoren $\Pi_K$**. Enhver virtuell fluktuasjon eller kandidatbane i $\Phi$ som bryter én av de 10 Poincaré-låsene, har et residual $\Delta_K > 0$ og hogges umiddelbart bort (`KILL`).

### Meisel II: Det transversale Poincaré-snittet ($\Sigma_k$)
I stedet for å integrere blindt gjennom et uendelig kontinuum der numerisk og fysisk støy (som i trelegemeproblemet) vokser eksponentielt med Lyapunov-eksponenten $e^{\lambda t}$, reduserer Poincaré-feltet den kontinuerlige flyten $\Phi_{\Delta t}$ til en diskret **Poincaré-avbildning** på tvers av et transversalt snitt $\Sigma_k$:

$$x_{k+1} = \mathcal{P}_{\Sigma}(x_k) := \Omega\!\left(\Pi_{\Sigma_k}\!\left(\Phi_{\Delta t}(x_k)\right)\right)$$

Hver gang et legeme eller en bølgefront krysser snittet $\Sigma_k$, utføres en polynomisk verifikasjon av **snitt-residualet**:

$$\Delta_{\Sigma}(x_k) = \bigl\lVert m_k - R(x_k) \bigr\rVert_{\Sigma_k}$$

der $m_k$ er det fysiske vitnet (den målte tilstanden på snittet) og $R(x_k)$ er den projiserte modellen:
* **$\Delta_{\Sigma} \le \epsilon_{\text{drift}} \implies \mathbf{OPEN}$:** Banen innrømmes videre til neste seksjon $\Sigma_{k+1}$.
* **$\Delta_{\Sigma} > \epsilon_{\text{drift}} \implies \mathbf{HOLD / KILL}$:** Det akkumulerte avviket mellom kart og terreng kuttes på snittet *før* feilen får lov til å forplante seg som fiktiv virkelighet.

### Meisel III: Fra sirkel til heliks (Ikke-lukking og Landauer-skatt)
I klassisk himmelmekanikk ser en planetbane ut som en lukket ellipse som vender tilbake til nøyaktig samme punkt: $x(T) = x(0)$.

Men i **Poincaré-feltet** (formulert over det løftede skjevproduktet $\mathcal{S}_{\text{tot}} = \mathcal{X}_{\text{phys}} \times \mathcal{H}_{\text{hist}}$) gjelder **Loven om Ikke-Lukking (*Non-Closing Dynamics*)**:

$$(x_{k+1}, h_{k+1}) \neq (x_k, h_k)$$

Hvorfor? Fordi hver gang banen passerer gjennom porten på Poincaré-snittet $\Sigma_k$ og de urealiserte, kaotiske nabobanene slettes, må systemet betale **Landauer-skatten** ($E_{\min} = k_B T \ln 2$ per slettet frihetsgrad) og skrive et nytt, irreversibelt ledd inn i historiefiberen $h_{k+1} = H(h_k \parallel x_{k+1})$.

Det som i et flatt 3D-projeksjonsbilde ser ut som en evig, repetitiv sirkel ($x(T) \approx x(0)$), er i det fulle Poincaré-feltet en **strengt stigende heliks (spiral)**. Man krysser aldri det samme snittet i samme epoke to ganger.

---

## 3. Feltligningene skrevet i Poincaré-feltet

Når vi samler disse tre meislene, får feltligningene for tyngdekraften en form som skiller skarpt mellom det som **foreslås ($\Phi$)** og det som **innrømmes ($\mathcal{P}$)**:

1. **Kandidat-propagering mellom snittene ($\Phi$):**  
   Mellom $\Sigma_k$ og $\Sigma_{k+1}$ brer gravitasjons- og materiefeltet seg ut som en Lorentz-invariant bølge i Poincaré-rommet:
   $$\Box h_{\mu\nu} = -\frac{16\pi G}{c^4}\,\tau_{\mu\nu}(h, T)$$
   der $\Box = \eta^{\alpha\beta}\partial_\alpha\partial_\beta$ er den flate d'Alembert-operatoren og $\tau_{\mu\nu}$ inkluderer feltets egenenergi.
2. **Ekskavering ved Poincaré-snittet ($\Pi_{\Sigma_k}$):**  
   Ved snittet $\Sigma_k$ projiseres kandidatfeltet ned på den admissibilitetsmengden $\mathcal{A}$ som tilfredsstiller ADM-tvangsligningene ($\mathcal{H}_{\text{ADM}} = 0$, $\mathcal{M}_i = 0$) og kausalitet:
   $$h_{\mu\nu}^{(k+1)} = \Pi_{\mathcal{A}}\!\left(h_{\mu\nu}'\right), \qquad \Delta_K = \bigl\lVert h_{\mu\nu}' - h_{\mu\nu}^{(k+1)} \bigr\rVert$$
3. **Termodynamisk oppgjør ved porten ($\Omega$):**  
   Den bortmeislede resten $\Delta_K$ (de kaotiske og uadmissible banene som ble skåret vekk ved snittet) betales som irreversibel horisont- og strålingsentropi:
   $$\Delta Q_{\Sigma_k} = \int_{\Sigma_k} \Sigma_{\mu\nu}^{\text{irr}}\, u^\mu \mathrm{d}\Sigma^\nu \;\ge\; N_{\text{erased}} \cdot k_B T \ln 2$$

---

## 4. Sammenfatning: Hva tyngdekraften er i Poincaré-feltet

I dette bildet trenger vi ikke lenger å behandle rommet som et mystisk, elastisk gummilaken som bøyer seg av seg selv:

* **Poincaré-feltet** er spenningsfeltet i et flatt referanserom der materie og energi kontinuerlig foreslår nye konfigurasjoner ($\Phi$).
* **Poincaré-snittet ($\Sigma_k$)** er den lokale domstolen i klassen $\mathcal{P}$ som med jevne mellomrom krever at energiregnskapet, dreieimpulsen og lyskjeglen går opp uten rest.
* **Tyngdekraften (Law of Gravity)** er rett og slett den **uthuggede rennen i faserommet** – den eneste sammenhengende rekken av Poincaré-snitt $\Sigma_0 \to \Sigma_1 \to \Sigma_2 \to \dots$ der et legeme kan bevege seg fremover uten å bryte Poincaré-invariantene og uten å pådra seg ubetalt projeksjonsrest ($\Delta_K = 0$).

Det som ikke passer gjennom snittet, blir til varme.  
Det som passerer gjennom snittet, blir til bane og tid.
