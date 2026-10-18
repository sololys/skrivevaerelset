# Research Monograph · Document 187 (Version 2.0) · Canonical Compendium
## Asymmetrien mellom Bølge og Lov: Førsteordens Tvangssystem $(\psi_0, \boldsymbol{\psi})$, Klein–Gordon-Reduksjon, De Tre Aksiomene og Paradoks som Mangfoldighet i $\mathcal{NP}$ (`KY Engine v2.0 // κ27 // SPEC-390`)

> *«Det som er mangfoldighet i $\mathcal{NP}$, blir paradoks når det krever eksistens i $\mathcal{P}$.»*

* **Forfatter:** Marius Egerhei Torjusen (ORCID: [`0009-0006-0431-6637`](https://orcid.org/0009-0006-0431-6637))
* **Institusjon:** ReismannPoint Systems // Brahman Ventures · Lokus Zero, Risør, Norway
* **Zenodo Concept DOI:** [`10.5281/zenodo.23424505`](https://doi.org/10.5281/zenodo.23424505) · **v1.0 DOI:** [`10.5281/zenodo.23424506`](https://doi.org/10.5281/zenodo.23424506)
* **Dato:** 18. oktober 2026 · **Utgave:** Versjon 2.0 (Tospråklig NO/EN Omni-Syntese)
* **Epistemisk Demarkasjon (`AGENTS.md`):** `INSPIRED_BY != IMPLEMENTS != PROVES` · `GENERATION != AUTHORIZATION != WITNESSED CONSEQUENCE`

---

## 1. Grunnmuren: Det låste førsteordenssystemet

Vi betrakter et koblet feltsystem bestående av skalarfeltet $\psi_0(t, \mathbf{x}) \in \mathbb{R}$ og vektorfeltet $\boldsymbol{\psi}(t, \mathbf{x}) \in \mathbb{R}^3$, styrt av en konstant masse-firevektor $m^\mu = (m_0, \mathbf{m})$ med $\mathbf{m} \in \mathbb{R}^3$. Systemets konstitutive førsteordenslover er gitt ved likningene (1)–(4):

$$\frac{1}{c^2}\frac{\partial \psi_0}{\partial t} + \nabla \cdot \boldsymbol{\psi} = 0 \tag{1}$$
$$m_0 \psi_0 - c\,\mathbf{m} \cdot \boldsymbol{\psi} = 0 \tag{2}$$
$$\frac{\partial \boldsymbol{\psi}}{\partial t} + \nabla \psi_0 - \frac{c^2}{\hbar}(\mathbf{m} \times \boldsymbol{\psi}) = \mathbf{0} \tag{3}$$
$$\nabla \times \boldsymbol{\psi} + \frac{\mathbf{m}}{\hbar}\psi_0 - \frac{c m_0}{\hbar}\boldsymbol{\psi} = \mathbf{0} \tag{4}$$

Fra likning (1) og (2) følger $[\psi_0] = c[\boldsymbol{\psi}]$ og $[m_0] = [\mathbf{m}] = \text{kg}$, der $\frac{Mc}{\hbar}$ har enhet av invers lengde ($\text{m}^{-1}$, invers Compton-bølgelengde).

---

## 2. Utfoldelsen: Eksakt utledning av Klein–Gordon-likningene

Ved å derivere (1) og (3) med hensyn på tid og substituere (2) og (4), kansellerer kryssleddene $\mp \frac{1}{\hbar}\mathbf{m} \times \nabla\psi_0$ ($\mathbf{C}_1 = \mathbf{0}$) og de longitudinelle leddene $\pm \frac{c m_0}{\hbar^2}\mathbf{m}\psi_0$ ($\mathbf{C}_2 = \mathbf{0}$) hverandre eksakt, og etterlater de rene andreordens Klein–Gordon-likningene:

$$\left(\frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \nabla^2 + \left(\frac{Mc}{\hbar}\right)^2\right)\psi_0 = 0, \qquad \left(\frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \nabla^2 + \left(\frac{Mc}{\hbar}\right)^2\right)\boldsymbol{\psi} = \mathbf{0}, \qquad M^2 = |\mathbf{m}|^2 - m_0^2.$$

---

## 3. Den skjulte skranken: Hvorfor bølgen ikke er nok

Tar vi divergensen av likning (4) og bruker $\nabla \cdot (\nabla \times \boldsymbol{\psi}) \equiv 0$ sammen med (1), fremtvinges den skjulte integrabilitetsbetingelsen:

$$\left(\frac{m_0}{c}\frac{\partial}{\partial t} + \mathbf{m} \cdot \nabla\right)\psi_0 = 0 \iff m^\mu \partial_\mu \Psi^\nu = 0.$$

| Lov | Kovariant form | Fysisk og geometrisk betydning |
| :--- | :--- | :--- |
| **Ligning (1)** | $\partial_\mu \Psi^\mu = 0$ | **Lorenz-betingelse:** Bevarelse av fire-strøm; låser skalarendring til romlig fluks. |
| **Ligning (2)** | $m_\mu \Psi^\mu = 0$ | **Algebraisk ortogonalitet:** Feltvektoren må ligge i hyperplanet ortogonalt på $m^\mu$. |
| **Integrabilitet** | $m^\mu \partial_\mu \Psi^\nu = 0$ | **Kinematisk ortogonalitet:** For planbølge $k^\mu = (\omega/c, \mathbf{k})$ må $\frac{\omega}{c}m_0 - \mathbf{k}\cdot\mathbf{m} = 0$. |

---

## 4. Speilingen i $\mathcal{P}$ mot $\mathcal{NP}$: Paradoks er Mangfoldighet i $\mathcal{NP}$

1. **Andreordenslikningene som Mulighetsrommet ($\Phi$ — Mangfoldighet i $\mathcal{NP}$):** Fire frakoblede bølgelikninger på hele masseskallets hyperboloide.
2. **Førsteordenssystemet som Projektor ($\Pi_K$ — Kuttet inn i $\mathcal{P}$):**
   * **Amplitudekuttet:** $\Delta_K^{(1)} = |m_0\psi_0 - c\,\mathbf{m}\cdot\boldsymbol{\psi}| = 0$
   * **Flukskuttet:** $\Delta_K^{(2)} = \left|\frac{1}{c^2}\frac{\partial \psi_0}{\partial t} + \nabla\cdot\boldsymbol{\psi}\right| = 0$
   * **Banekuttet:** $\Delta_K^{(3)} = \left|\frac{\omega}{c}m_0 - \mathbf{k} \cdot \mathbf{m}\right| = 0$
3. **Masserelasjonen som Konsekvensport ($\Omega$):**
   * $|\mathbf{m}| > |m_0| \iff M^2 > 0 \implies \texttt{OPEN / ADMIT (5.00 V DC)}$
   * $|\mathbf{m}| = |m_0| \iff M^2 = 0 \implies \texttt{HOLD (0.00 V DC)}$
   * $|\mathbf{m}| < |m_0| \iff M^2 < 0 \implies \texttt{KILL (0.00 V DC)}$

---

## 5. Indeksering til Regnskapsenhet fremfor ZFCs Tomme Mengde ($\emptyset$) (NY I v2.0)

1. **Endelig regnskapsgulv:** Ingen fysisk tilstand er indeksert til den kostnadsfrie tomme mengden ($\emptyset$) i ZFC; grunnenheten for fysisk regnskapsplikt er en bevitnet tilstandsovergang ($W = 1$) betalt ved Landauers gulv ($Q_{\Pi_K} \ge N k_B T \ln 2$) over et positivt spektralgulv ($\lambda_{\min}(G) \ge \varepsilon_G > 0$).
2. **Eliminering av uprojiserte uendeligheter ($\Pi_K^2 = \Pi_K$):** Projektoren kutter ubegrensede symbolrom ned til et endelig, bærende underrom ($N \le 3$) før aktuering.
3. **Rapporterbar identitet mot entropi:** Når det ikke-valgte residualet ($\Delta_K = \Phi - \Pi_K(\Phi)$) avvises som varme, mister de uforenlige frihetsgradene sin rapporterbarhet slik at den overlevende strukturen ($\Pi_K(\Phi)$) forblir invariant, bevitnet og rapporterbar over tid.

---

## 6. 1-Syklus Silisiumrealisering (`E-TOR`) og De Tre Kjerneaksiomene (NY I v2.0)

* **Aksiom I (`HOLD`):** $\partial_t x = 0 \implies \Omega = \text{HOLD}$ ($0.00\text{ V DC}$, $\tau_{\text{dead}}$ dødtid $Q_{\text{high}}\cdot Q_{\text{low}} = 0$).
* **Aksiom II ($\Pi_K$):** $\Pi_K^2 = \Pi_K$ (1-klokkesyklus SystemVerilog RTL i `01_HARDWARE_RTL/etor_pi_k_projection_gate.sv`).
* **Aksiom III (`GRACE`):** Nullpunkts-tilgivelse (`reset()`) til $\Delta S_{\text{debt}} = 0$ med uforanderlig WORM SHA-256 proveniens.
