# DOKUMENT 43: INNRAMMING AV DE SEKS FØRSTEORDENS BØLGELOVENE — ASYMMETRIEN MELLOM BØLGE ($\mathcal{NP}$) OG LOV I PUNKTET ($\mathcal{P}$)

**Forankring:** Dokument 187 (`SPEC-390`, `DOI: 10.5281/zenodo.23424505`), Det Store Matematiske Kompendium (Dokument 42) og Reality Forge Godot 4.3 (`L1`)  
**Kardinal-aksiom:**
$$\text{INSPIRED\_BY} \neq \text{IMPLEMENTS} \neq \text{PROVES} \qquad \land \qquad \text{ANDREORDENS BØLGE } (\mathcal{NP}) \supsetneq \text{FØRSTEORDENS LOV } (\mathcal{P})$$

---

## 1. Den Innrammede Plakaten: De Seks Førsteordens Bølgelovene

```text
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                        DE SEKS FØRSTEORDENS BØLGELOVENE — FRA BØLGE I NP TIL LOV I PUNKTET (P)                       ║
║                    «Det som er mangfoldighet i NP, blir paradoks når det krever eksistens i P.»                      ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                                                      ║
║  [I] DEN KAUSALE ENVEISBØLGEN (1D FAKTORISERING AV D'ALEMBERT)                                                       ║
║      ∂u/∂t + c ∂u/∂x = 0   ⟹   u(x,t) = f(x - ct)                                                                    ║
║      • Kutter bort baklengs-tid-spøkelset g(x + ct) som overlever i (c⁻² ∂_t² - ∂_x²)u = 0.                          ║
║                                                                                                                      ║
║  [II] DET AKUSTISKE PORT-HAMILTONSKE FRIEDRICHS-SYSTEMET (J^T = -J)                                                  ║
║      (1 / ρ₀c²) ∂p/∂t + ∇·v = 0,          ρ₀ ∂v/∂t + ∇p = 0                                                          ║
║      • Symplektisk energibevaring i første orden: dE/dt = ∫ (p ∂_t p/ρ₀c² + ρ₀ v·∂_t v) dV = -∮ p v·dA.               ║
║                                                                                                                      ║
║  [III] MAXWELLS FØRSTEORDENS VAKUUMBØLGE MED DIVERGENS-LÅS                                                           ║
║      ∂E/∂t - c²(∇ × B) = 0,     ∂B/∂t + (∇ × E) = 0,     ∇·E = 0,     ∇·B = 0                                        ║
║      • Andreordensbølgen □E = 0 tillater longitudinelle spøkelser (E ∥ k); førsteordensloven ∇·E = 0 kutter dem.     ║
║                                                                                                                      ║
║  [IV] WEYLS FØRSTEORDENS KIRALE SPINNERBØLGE (MASSELØS HELISITETSLÅS)                                                ║
║      (1/c) ∂ψ_R/∂t + (σ · ∇)ψ_R = 0,          (1/c) ∂ψ_L/∂t - (σ · ∇)ψ_L = 0                                         ║
║      • Låser spinn-operatoren σ eksakt til bølgens utbredelsesretning k (ĥ = (σ·k)/|k| = ±1).                        ║
║                                                                                                                      ║
║  [V] DIRACS FØRSTEORDENS BØLGE I FYSISK ROMS ALGEBRA Cl_{3,0}(R) (APS)                                               ║
║      ( (1/c) ∂/∂t + ∇ ) Ψ = (mc / ħ) Ψ i σ₃,          i = σ₁ σ₂ σ₃                                                   ║
║      • Kvadratroten av Klein–Gordon-operatoren: garanterer positiv sannsynlighetstetthet ρ = ⟨Ψ Ψ†⟩₀ ≥ 0.            ║
║                                                                                                                      ║
║  [VI] TORJUSENS LÅSTE FØRSTEORDENS TVANGSSYSTEM (ψ₀, ψ) (DOKUMENT 187 / SPEC-390)                                    ║
║      (1)  (1/c²) ∂ψ₀/∂t + ∇·ψ = 0                           [Flukslås:     ∂_μ Ψ^μ = 0]                              ║
║      (2)  m₀ ψ₀ - c (m · ψ) = 0                             [Amplitudelås: m_μ Ψ^μ = 0]                              ║
║      (3)  ∂ψ/∂t + ∇ψ₀ - (c²/ħ)(m × ψ) = 0                   [Kiral rotasjonsflyt]                                    ║
║      (4)  ∇ × ψ + (m/ħ)ψ₀ - (c m₀/ħ)ψ = 0                   [Helisitets- og vortisitetslås]                          ║
║                                                                                                                      ║
║      ──► ANDREORDENS UTFOLDELSE (NP-Forslagsrom Φ):                                                                  ║
║          ( (1/c²)∂_t² - ∇² + (Mc/ħ)² ) ψ₀ = 0,     M² = |m|² - m₀²   (Kryssledd C₁ = 0 og C₂ = 0 kansellerer!)       ║
║                                                                                                                      ║
║      ──► FØRSTEORDENS SKJULT SKRANKE (P-Projeksjon Π_K):                                                             ║
║          ( (m₀/c)∂_t + m · ∇ ) ψ₀ = 0   ⟺   (ω/c)m₀ - k · m = 0      (m^μ ∂_μ Ψ^ν = 0)                               ║
║                                                                                                                      ║
║      ──► TRE-TILSTANDS KONSEKVENSPORT (Ω):                                                                           ║
║          • |m| > |m₀|  (M² > 0, v_g < c)  ⟹  OPEN / ADMIT (krever gyldig evidence_id + Δ_K = 0)                      ║
║          • |m| = |m₀|  (M² = 0, lyskjegle)⟹  HOLD         (marginal hvile ved 0,00 V DC)                             ║
║          • |m| < |m₀|  (M² < 0, takyonisk)⟹  KILL         (momentan avvisning av eksponentiell lekkasje)             ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
```

---

## 2. Det Eksakte Matematiske Beviset for Asymmetrien ($\text{Lov i } \mathcal{P} \subsetneq \text{Bølge i } \mathcal{NP}$)

La en planbølge-kandidat i $\mathbb{R}^{1,3}$ være gitt ved:
$$\psi_0(t,\mathbf{x}) = A_0 \cos(\mathbf{k}\cdot\mathbf{x} - \omega t), \qquad \boldsymbol{\psi}(t,\mathbf{x}) = \mathbf{A}\cos(\mathbf{k}\cdot\mathbf{x} - \omega t) + \mathbf{B}\sin(\mathbf{k}\cdot\mathbf{x} - \omega t)$$

### Steg 1: Hva andreordens Klein–Gordon-bølgen ($\Phi$ i $\mathcal{NP}$) krever
Andreordensligningen $\left(\frac{1}{c^2}\partial_t^2 - \nabla^2 + \frac{M^2 c^2}{\hbar^2}\right)\Psi = 0$ med $M^2 = |\mathbf{m}|^2 - m_0^2$ krever **kun** dispersjonsrelasjonen på masseskallet:
$$\frac{\omega^2}{c^2} - |\mathbf{k}|^2 = \frac{(|\mathbf{m}|^2 - m_0^2)c^2}{\hbar^2}$$
Enhver bølgevektor $\mathbf{k} \in \mathbb{R}^3$ og enhver amplitude $(A_0, \mathbf{A}, \mathbf{B})$ som tilfredsstiller denne ene skalarligningen, slipper gjennom andreordensbølgen!

### Steg 2: Hva det førsteordens tvangssystemet ($\Pi_K$ i $\mathcal{P}$) krever
For at den samme bølgen skal være en faktisk løsning av de fire førsteordensligningene (1)–(4), må **tre uavhengige tvangsresidualer** være eksakt null i hvert punkt:
1. **Amplitudekuttet ($\Delta_K^{(1)}$ fra Ligning 2):**
   $$\Delta_K^{(1)} = \big|m_0 \psi_0 - c\,\mathbf{m}\cdot\boldsymbol{\psi}\big| = 0 \implies m_0 A_0 = c\,\mathbf{m}\cdot\mathbf{A} \;\land\; \mathbf{m}\cdot\mathbf{B} = 0$$
2. **Flukskuttet ($\Delta_K^{(2)}$ fra Ligning 1):**
   $$\Delta_K^{(2)} = \left|\frac{1}{c^2}\frac{\partial \psi_0}{\partial t} + \nabla\cdot\boldsymbol{\psi}\right| = 0 \implies \frac{\omega}{c^2}A_0 = \mathbf{k}\cdot\mathbf{A} \;\land\; \mathbf{k}\cdot\mathbf{B} = 0$$
3. **Banekuttet / Kinematisk Ortogonalitet ($\Delta_K^{(3)}$ fra $\nabla\cdot(\text{Ligning 4}) + \text{Ligning 1}$):**
   $$\Delta_K^{(3)} = \left|\frac{\omega}{c}m_0 - \mathbf{k}\cdot\mathbf{m}\right| = 0$$

> **Teorem (Asymmetrien mellom Bølge og Lov):**  
> Løsningsmengden $\mathcal{S}_{\text{1.orden}}$ av førsteordenslovene (1)–(4) er en **ekte, streng delmengde** av løsningsmengden $\mathcal{S}_{\text{2.orden}}$ av Klein–Gordon-bølgeligningene:
> $$\boxed{\mathcal{S}_{\text{1.orden}} = \Big\{\Psi \in \mathcal{S}_{\text{2.orden}} \;\Big|\; \Delta_K^{(1)}(\Psi) = \Delta_K^{(2)}(\Psi) = \Delta_K^{(3)}(\Psi) = 0\Big\} \subsetneq \mathcal{S}_{\text{2.orden}}}$$
> Derivering ($\text{1. orden} \to \text{2. orden}$) er en **ikke-invertibel glemselsoperator** som sletter fase-, polarisasjons- og retningslåsene. Å gå tilbake fra bølgen i $\mathcal{NP}$ til loven i $\mathcal{P}$ krever projeksjonsslusen $\Pi_K$.

---

## 3. Verifisert Godot 4.3 `L1`-Motor: `FirstOrderWaveLawEngine` (`6/6 PASS`)

* **Motor:** [`first_order_wave_law_engine.gd`](file:///home/sololyset/04_REALITY_FORGE/RealityForge_Godot/scripts/first_order_wave_law_engine.gd)
* **Headless Testsuite:** [`test_first_order_wave_law_engine.gd`](file:///home/sololyset/04_REALITY_FORGE/RealityForge_Godot/tests/test_first_order_wave_law_engine.gd)
