# 33 — Reality Forge: `PExcavationPhysicsEngine` i Godot 4.3 (`L1`)

> **Bevisnivå (`L1`):** Lokalt demonstrert programvare og deterministisk konsekvensport-simulering i Godot Engine `v4.3.stable.official.77dcf97d8`. Merk grensen `INSPIRED_BY != IMPLEMENTS != PROVES`: en append-only hash-kjede i programvare er en deterministisk vitnelogg i minnet, ikke fysisk WORM-maskinvare.

---

## 1. Fra de 11 fysikkligningene til én spillbar konsekvensmotor

I dokumentet [32_DE_11_FYSIKKLIGNINGENE_FRA_BBGKY_KAOS_TIL_KUTTFLATE_I_P.md](./32_DE_11_FYSIKKLIGNINGENE_FRA_BBGKY_KAOS_TIL_KUTTFLATE_I_P.md) (samt [30_HILLS_LIGNING](./30_HILLS_LIGNING_FLOQUET_MONODROMI_OG_POINCARE_SNITTET.md) og [31_GAUSS_BOKSEN](./31_GAUSS_BOKSEN_KUTTFLATEN_OG_ASYMMETRIEN_MELLOM_FLUKS_OG_FELT.md)) viste vi hvordan fysikkens sentrale ligninger blir beregnbare i polynomisk tid ($\mathcal{P}$) når vi hugger over det eksponentielle korrelasjonsrommet ($\Phi \in \mathcal{NP}$) med en strukturert meisel ($\Pi_K$) og betaler den termodynamiske port-tollen ($\Delta_K$) ved realisering ($\Omega$).

Denne arkitekturen er nå implementert direkte i **Reality Forge** som en ny Godot-kjerne:

- **Implementasjon:** [`04_REALITY_FORGE/RealityForge_Godot/scripts/p_excavation_physics_engine.gd`](../../04_REALITY_FORGE/RealityForge_Godot/scripts/p_excavation_physics_engine.gd) (`class_name PExcavationPhysicsEngine`)
- **Headless Test-suite:** [`04_REALITY_FORGE/RealityForge_Godot/tests/test_p_excavation_physics_engine.gd`](../../04_REALITY_FORGE/RealityForge_Godot/tests/test_p_excavation_physics_engine.gd)

---

## 2. De 5 spillmekaniske fysikk-modulene i `PExcavationPhysicsEngine`

### Modul 1: `evaluate_bbgky_boltzmann_cut` (Statistisk kutt & Landauer-toll)
- **Spillmekanikk:** Hvis en sverm eller gass-sky forsøkes løst som en ulukket BBGKY-kjede ($s < N$ uten *Stosszahlansatz*), nekter motoren å gjette på den manglende korrelasjonen $f_{s+1}$ og fryser tilstanden i `GATE::HOLD` (`0.00V`).
- Når spilleren/kontrolleren aktiverer **Stosszahlansatz-meiselen** ($f_2 \approx f_1 f_1$) med et gyldig `evidence_id`, lukkes hierarkiet i $\mathcal{P}$, entropitollen $\Delta E_{\text{Landauer}} = N_{\text{bits}} k_B T \ln 2$ trekkes fra termobudsjettet, og porten låser til `GATE::OPEN` (`5.00V`).

### Modul 2: `evaluate_gauss_ampere_cut_surface` (Kuttflate-revisjon vs. Symmetri-meisel)
- **Forover (`FIELD_TO_ENCLOSED`):** Summerer fluks-paneler $\Phi_E = \sum \mathbf{E}_i \cdot \Delta\mathbf{A}_i$ og sløyfe-segmenter $\oint \mathbf{B}\cdot\mathrm{d}\mathbf{l}$ i $O(n)$ og avslører umiddelbart innelukket ladning $Q_{\text{enc}}$ og strøm $I_{\text{enc}}$.
- **Baklengs (`ENCLOSED_TO_FIELD`):** Hvis noen forsøker å rekonstruere det indre feltet fra totalfluksen *uten* en gyldig symmetri-meisel (`SPHERICAL`, `CYLINDRICAL`, `PLANAR`), blokkeres rekonstruksjonen i `GATE::HOLD` (`0.00V`) fordi spøkelsesfeltet $\nabla \times \mathbf{C}$ er underbestemt.

### Modul 3: `evaluate_hill_bessel_resonance_gate` (Floquet-monodromi & Sylinder-port)
- **Hill–Floquet:** Sjekker sporet av monodromimatrisen $\mathrm{Tr}(M) = M_{11} + M_{22}$ over én periode $\pi$. Dersom $|\mathrm{Tr}(M)| > 2$, oppstår parametrisk resonans og motoren utløser momentant `GATE::KILL` (`0.00V`) før amplituden eksploderer. På randen $|\mathrm{Tr}(M)| = 2$ holdes tilstanden i `GATE::HOLD`.
- **Bessel-bølgeleder:** Avviser Neumann-singulariteten $Y_\nu(r)$ i origo med `GATE::KILL`, og krever at det radielle bølgetallet $k R$ treffer et av de diskrete Bessel-nullpunktene $j_{0,n} \in \{2.4048, 5.5201, 8.6537, \dots\}$ for å åpne `GATE::OPEN`.

### Modul 4: `evaluate_fluid_shock_and_port_toll` (Bernoulli, Borda–Carnot, Darcy–Weisbach & Burgers Cole–Hopf)
- Kombinerer den tapsfrie Bernoulli-energien langs en strømlinje med:
  1. **Borda–Carnot port-toll** ved brå tverrsnittsutvidelse: $\Delta p_{\text{BC}} = \frac{1}{2}\rho(v_1 - v_2)^2$.
  2. **Darcy–Weisbach vegg-toll** langs rørveggen: $\Delta p_{\text{DW}} = f_D \frac{L}{D} \frac{\rho v_2^2}{2}$.
  3. **Cole–Hopf-transformasjonen** for Burgers' sjokkfront: $u = -2\nu \frac{\partial_x \phi}{\phi}$. Forsøk på viskositetsløs sjokk-propagering ($\nu \le 0$) gir flertydig gradient-katastrofe og utløser `GATE::KILL`.

### Modul 5: `evaluate_dirac_aps_involution` (Dirac i $\mathcal{C}\ell_{3,0}$ uten matrise-spøkelser)
- Representerer spinoren/rotoren direkte i den jevne delen av det fysiske rommets algebra $\mathcal{C}\ell_{3,0}^+$ (`Vector4(s, B_23, B_31, B_12)`).
- Verifiserer at 3D-volumelementet $i = \mathbf{e}_1\mathbf{e}_2\mathbf{e}_3$ gir $i^2 = -1$, at dobbel Clifford-involusjon oppfyller fikspunktkravet $F(F(\Psi)) = \Psi$, og projiserer den lokale spinn-aksen $\mathbf{s}_3 = R \mathbf{e}_3 \tilde{R}$ direkte i 3D-rommet.

---

## 3. Verifikasjon (Godot 4.3 Headless)

```bash
/home/sololyset/.local/bin/godot --headless --path /home/sololyset/04_REALITY_FORGE/RealityForge_Godot -s tests/test_p_excavation_physics_engine.gd
```

Resultat: **`7/7` tester bestått** (inkludert verifikasjon av Reality Forge-invariantene: `HOLD` går aldri over til `OPEN` av at tid går, `OPEN` krever ikke-tomt `evidence_id`, `KILL` kutter til `0.00V`, og `reset_to_hold()` er strengt append-only).
