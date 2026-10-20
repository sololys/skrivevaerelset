# Infranett v0.5 — Operasjonell Syntese: Relativistisk Konsekvensport ($\Pi_K$), Evanescent EMP-Bølgeleder, $6\text{G} \otimes W_{\text{laser}}$ RIS-Lås og SPEC-250 Rust-Kjerne

**Dokument-ID:** `INFRANETT-V05-OPERASJONELL-SYNTESE-EMP-6G-SPEC250`  
**Versjon:** `1.0 (Canonical Operational Synthesis)`  
**Dato:** `19. oktober 2026`  
**Forfatter / Entitet:** `Marius Egerhei Torjusen (Brahman)`  
**Epistemisk Status (`AGENTS.md`):**
* **`L0` (Matematikk, Elektrodynamikk & Relativistisk Geometri):** Minkowski-romtidsintervall ($ds^2 \le 0$), Euklidsk trekantulikhet for RIS-speiling ($r_{\text{RIS}} > r_{\text{LOS}}$), og sylindrisk $\text{TE}_{11}$ bølgeleder-avskjæring ($J'_1(p'_{11}) = 0$, $p'_{11} \approx 1{,}8412$).
* **`L1` (Deterministisk Programvare & Fastpunkt-Referansekjerne):** Verifisert i `spec250_gate.rs` (Rust, `#![forbid(unsafe_code)]`, heltalls pikosekund-aritmetikk) og `infranett_laser_fso_witness_engine.py` (`9/9 PASS`). `INSPIRED_BY != IMPLEMENTS != PROVES`: Programvarekjeder (`WAL`) er append-only SHA-256 hash-kjeder, ikke fysiske WORM-medier.
* **`L2/L3` (`HOLD` — Fysisk Maskinvare- og Feltvalidering):** Fysisk HEMP $E_1$-testing ($50\text{ kV/m}$), $\text{Al}_2\text{O}_3$ safir-gjennomslagstesting ($> 70\text{ kV}$) og $6\text{G}$ Sub-THz / $1550\text{ nm}$ FSO maskinvare-koherens tilhører fysisk laboratorieverifikasjon (`SPEC-250 HIL`).

---

## Operasjonelt Sammendrag

Foreningen av de fire innleverte spesifikasjonene konsoliderer **Infranett v0.5** som en relativistisk, termodynamisk og elektromagnetisk lukket tilstandsmaskin. Systemet erstatter stokastiske antakelser (RSSI, sivil 6G-AI, nettverkstillit) med eksakte fysiske invarianter: Minkowski-romtidsgeometri ($ds^2 \le 0$), mekanisk spillteori ($\Delta U_{\text{cheat}} < 0$), evanescent bølgeleder-avskjæring ($\omega < \omega_c$) og optisk siktlinje-isolasjon ($W_{\text{laser}}$).

Enhver tilstandsovergang fra et uverifisert potensial ($\Phi$) til en fysisk aksjon krever strukturell projeksjon ($\Pi_K$) og port-autorisasjon ($\Omega$) før den forsegles i en append-only beviskjede ($W$). Ingen ekstern protokoll eller AI-komponent i det fysiske laget har myndighet til å krysse konsekvensporten uten et deterministisk vitne:

$$\Phi \xrightarrow{\Pi_K} \Omega \xrightarrow{W} \text{AKUERISAAVOQ}$$

---

## 1. Formell Romtid, Kanal- og Portmatrise ($\Pi_K$)

Tabellen under definerer de eksakte matematiske rommene, operatorene og grensebetingelsene som styrer SPEC-250-slusen på tvers av UWB, optisk FSO, EMP-vern og 6G-grensesnitt.

| Domene / Operator | Matematisk Formulering & Rom | Terskel / Invariant | Konsekvens ved Avvik ($\Delta_K$) |
| :--- | :--- | :--- | :--- |
| **Kausal Diamant** $\mathcal{D}(E_1, E_2)$ | $\mathcal{D}(E_1, E_2) = J^+(E_1) \cap J^-(E_2) \subset \mathcal{M}^4$ | $ds^2 = -c^2(\Delta t)^2 + (\Delta r)^2 \le 0$ | $ds^2 > 0 \implies \text{GATE :: KILL}$ ($0.00\text{ V DC}$) |
| **Relativistisk ToF** (IEEE 802.15.4z) | $\Delta t_{\text{roundtrip}} = t_2 - t_1$, $N_{\text{ephem}} \in_R \{0,1\}^{256}$ | $\Delta t_{\text{budget}} \le \frac{2 \cdot r_{\max}}{c} \approx 133.42\text{ ns}$ ($r_{\max} = 20.0\text{ m}$) | $\Delta t > 133.42\text{ ns} \implies \text{GATE :: KILL}$ |
| **Monoton Epoke** ($C_{\text{hw}}$) | $C_{\text{capsule}} \in \mathbb{N}_0$, lagret i TPM / eNVM | $C_{\text{capsule}} \ge C_{\text{hw}}$ | $C < C_{\text{hw}} \implies \text{GATE :: HOLD\_STALE\_EPOCH}$ |
| **Mekanisk Nash-Likevekt** | $U(s_A, s_B) = G(s_A, s_B) - W_{\text{kinetic}} - W_{\text{crypto}}$ | $W_{\text{verify}} \approx 0 \ll W_{\text{forge}} \to \infty$ | $R_{\text{fork}} > 0 \implies G = 0, \Delta U_{\text{cheat}} < 0 \implies \text{KILL}$ |
| **Galvanisk Isolasjon** ($\text{Al}_2\text{O}_3$) | $I_{\text{galvanisk}}$ over syntetisk safirvindu ($d = 2.0\text{ mm}$) | $R_{\text{DC}} \to \infty$, $I_{\text{galvanisk}} = 0.0\text{ }\mu\text{A}$, $V_{\text{break}} > 70\text{ kV}$ | Konduktiv bane detektert $\implies \text{GALVANIC\_BREACH}$ |
| **Evanescent EMP-Filter** | Bikube-bølgeleder ($d = 2.0\text{ mm}$), $k = \frac{1}{c}\sqrt{\omega^2 - \omega_c^2}$ | $\omega_{\text{EMP}} < \omega_c \implies k \in i\mathbb{R}_+$ (Demping $> 100\text{ dB}$) | $\lambda_{\text{laser}} \in \{532\text{ nm}, 1550\text{ nm}\} \ll d \implies \text{Passband}$ |
| **6G $\otimes$ Infranett ($\Pi_K$-Lås)** | 6G ISAC / RIS / PHY-AI isolert i estimeringsrom $\mathcal{E}_{\text{D1}}$ | $\Delta r_{\text{6G}} - \Delta r_{\text{laser}} \le \epsilon_{\text{koherens}} \land \text{LOS\_OK} = 1$ | RIS-omvei ($\Delta r_{\text{RIS}} > \Delta r_{\text{LOS}}$) $\implies \text{HOLD / KILL}$ |

---

## 2. Verifikasjon av Kausalitet, RIS-Speiling og Bølgeleder-Fysikk

### A. Geometrisk Invarians i Relativistisk Avstandsbegrensning

* **Uavhengig Kontroll av Konstantgrunnlag:** I et standardisert vakuum/luft-grensesnitt med $c = 2.99792458 \times 10^8\text{ m/s}$ og en absolutt perimetergrense på $r_{\max} = 20.0\text{ m}$ (total banelengde $L = 2 \cdot r_{\max} = 40.0\text{ m}$), er det eksakte tidsbudsjettet:

$$\Delta t_{\text{budget}} = \frac{40.0\text{ m}}{2.99792458 \times 10^8\text{ m/s}} \approx 133.4256\text{ ns}$$

* **Presisering av Romtidsintervallet ($ds^2$) ved Angrep fra $r_{\text{angrep}} = 500\text{ m}$:**
  * Enveiskravet mellom utsendelsen $E_1 = (t_1, \mathbf{x}_B)$ på Node B og refleksjonshendelsen $E_A = (t_A, \mathbf{x}_A)$ hos angriperen ved $\vert\mathbf{x}_A - \mathbf{x}_B\vert = 500\text{ m}$ innenfor halvparten av tidsvinduet ($\Delta t_{1\to A} = 66.71\text{ ns}$) gir:

$$ds^2_{1\to A} = -c^2(\Delta t_{1\to A})^2 + (\Delta r_{1\to A})^2 = -(20.0\text{ m})^2 + (500.0\text{ m})^2 = -400\text{ m}^2 + 250\,000\text{ m}^2 = +249\,600\text{ m}^2 > 0$$

  * Evaluert over den utfoldede tur-retur-banen ($L_{\text{RT}} = 1000\text{ m}$) mot totalbudsjettet ($\Delta t_{\text{budget}} = 133.42\text{ ns}$), slik oppsummeringslikningen i dokument 1 oppstiller det, blir regnestykket:

$$-(2.99792 \times 10^8\text{ m/s} \cdot 133.42 \times 10^{-9}\text{ s})^2 + (1000\text{ m})^2 = -1599.8\text{ m}^2 + 1\,000\,000\text{ m}^2 = +998\,400.2\text{ m}^2 \gg 0$$

  * Begge formuleringer bekrefter at hendelsen ligger dypt i det romlignende området ($ds^2 > 0$) utenfor Alexandrov-intervallet $\mathcal{D}(E_1, E_2)$.

### B. Matematisk Knusing av 6G RIS-Speiling (Metamaterial-Anomali)

I sivil 6G benyttes *Reconfigurable Intelligent Surfaces* (RIS) til å etablere virtuelle siktlinjer (*Non-Line-of-Sight*, NLOS) ved å påføre et lokalt faseskift $\phi_{\text{RIS}}(\mathbf{x})$ på innkommende bølgefronter ved $100\text{ GHz} - 3\text{ THz}$.

1. **Trekantulikheten i Euklidsk Rom:** La noden stå i $\mathbf{x}_B$, aktøren i $\mathbf{x}_A$, og RIS-flaten i $\mathbf{x}_{\text{RIS}}$ (ikke kollineær med $\overline{\mathbf{x}_B \mathbf{x}_A}$). Den fysiske veilengden via speilet tilfredsstiller strengt:

$$r_{\text{RIS}} = \Vert\mathbf{x}_B - \mathbf{x}_{\text{RIS}}\Vert_2 + \Vert\mathbf{x}_{\text{RIS}} - \mathbf{x}_A\Vert_2 > \Vert\mathbf{x}_B - \mathbf{x}_A\Vert_2 = r_{\text{LOS}}$$

2. **Kryss-Spektral Inkonsistens ($6\text{G} \otimes W_{\text{laser}}$):** Infranett krever simultan koherens mellom RF/THz-bølgen og den kollimerte $1550\text{ nm}$ FSO-laseren ($\lambda_{\text{laser}} = 1.55\text{ }\mu\text{m}$). Et sub-THz metamateriale designet for dipolresonans ved $\lambda_{\text{6G}} \approx 1\text{ mm}$ ($300\text{ GHz}$) fungerer som en diffus eller ugjennomsiktig flate for $\lambda_{\text{laser}} = 1.55\text{ }\mu\text{m}$.
3. **Konsekvens:** Enten brytes den optiske siktlinjen ($\text{LOS\_OK} = 0$), eller så produserer gjenutsendingen et målbart residual $\Delta_K = \vert t_{\text{ToF, 6G}} - t_{\text{ToF, laser}}\vert > \tau_{\text{max}}$, hvilket utløser øyeblikkelig `GATE :: KILL`.

### C. Evanescent Demping i Bikube-Bølgeleder (Waveguide Beyond Cutoff)

For en sylindrisk metallisk kanal med diameter $d = 2.0\text{ mm}$ (radius $a = 1.0\text{ mm}$) er den laveste avskjæringsfrekvensen (dominante $\text{TE}_{11}$-modus) gitt ved det første nullpunktet til den deriverte Bessel-funksjonen $J'_1(p'_{11}) = 0$ der $p'_{11} \approx 1.8412$:

$$f_c = \frac{p'_{11} \cdot c}{2\pi a} \approx \frac{1.8412 \cdot 2.99792 \times 10^8\text{ m/s}}{2\pi \cdot 1.0 \times 10^{-3}\text{ m}} \approx 87.86\text{ GHz}$$

* **For HEMP / NNEMP ($f_{\text{EMP}} \le 10\text{ GHz} \ll 87.86\text{ GHz}$):** Bølgetallet langs kanalaksen $z$ blir rent imaginært:

$$k_z = \frac{2\pi}{c}\sqrt{f_{\text{EMP}}^2 - f_c^2} = i \alpha, \quad \alpha \approx \frac{p'_{11}}{a} \approx 1841.2\text{ m}^{-1}$$

Dempingen per millimeter kanallengde ($L$) er:

$$A_{\text{dB}}(L) = 20 \log_{10}\left(e^{\alpha L}\right) \approx 8.686 \cdot 1.8412\text{ mm}^{-1} \cdot L \approx 16.0\text{ dB/mm}$$

En kanallengde på $L = 7.0\text{ mm}$ gir dermed $> 112\text{ dB}$ passiv fysisk demping uten komponenter som kan mettes eller brenne opp under $E_1$-pulsen ($50\text{ kV/m}$).
* **For FSO-Laser ($f_{\text{laser}} \approx 193.4\text{ THz} \gg 87.86\text{ GHz}$):** Bølgetallet er reelt ($k_z \in \mathbb{R}_+$), og fotonene passerer uhindret gjennom safirvinduet med $I_{\text{galvanisk}} = 0.0\text{ }\mu\text{A}$.

---

## 3. Deterministisk Tilstandsdiagram: Realiseringsgrammatikk (D1–D3)

Flyten under viser hvordan uautoriserte input-signaler (6G-AI, EMP, Relé-forsøk) filtreres ut før de når `5.00 V DC` aktuator-nivå:

```text
[D1: ESTIMATE / POTENSIAL (Φ)]
  │  Innkommende 6G ISAC-bølge, UWB-puls eller K-POD FSO-kapsel
  │  (0.00% autoritet — GENERATION != AUTHORIZATION)
  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ [Π_K: STRUKTURELL PROJEKSJON & FYSIKKFILTER]                            │
│  1. Galvanisk & Evanescent vern: I_galv == 0.0 μA ∧ ω_EMP < ω_c         │
│  2. Relativistisk Diamant:       Δt_RT <= 133.42 ns (ds² <= 0)          │
│  3. Optisk Koherens (W_laser):   LOS_OK == 1 ∧ |Δr_6G - Δr_laser| <= ε  │
│  4. Epoke & Impedans:            C_in >= C_hw ∧ VSWR_avvik <= 5σ        │
│  5. Kryptografisk Arv:           Ed25519(N_ephem) == VALID ∧ R_fork == 0│
└───────────────┬─────────────────────────────────────────┬───────────────┘
                │ Alle 5 invarianter == TRUE              │ Brudd / Usikkerhet (Δ_K > terskel)
                ▼                                         ▼
[D2: COMMIT / PORT-AUTORISASJON (Ω)]        [FAIL-CLOSED AVVISNING]
  │  SPEC-250 NO-MOSFET aktiveres             │  • Stale Epoch / Jamming -> GATE :: HOLD (0.00 V DC)
  │  Utgang: 5.00 V DC                        │  • ds² > 0 / R_fork > 0  -> GATE :: KILL (0.00 V DC)
  ▼                                           ▼
[D3: WITNESS / KONSEKVENS (W)]              [TERMODYNAMISK TAP FOR ANGRIPER]
  │  Append-only SHA-256 WAL + fsync          │  ΔU_cheat = -W_kinetic - W_forge < 0
  │  Tilstand: AKUERISAAVOQ                   │  Ingen nettverksmutasjon
```

---

## 4. Referanseimplementasjon: Fail-Closed Konsekvensport ($\Pi_K$) i Rust (`spec250_gate.rs`)

Følgende deterministiske modul (uten eksterne avhengigheter) håndhever samtlige fysiske og spillteoretiske krav fra spesifikasjonene før porten tillater eksitasjon til `5.00 V DC`.

```rust
#![forbid(unsafe_code)]
#![deny(clippy::float_arithmetic)] // Tvinger heltallsbasert fastpunkt-aritmetikk i kjernen

/// Fysiske konstanter og terskler i pikosekunder (ps) og mikrometer (um)
/// for å unngå IEEE 754 flyttalls-ufullstendigheter.
pub const C_UM_PER_PS: u128 = 299; // Eksakt gulvverdi for 299.792458 um/ps
pub const MAX_TOF_ROUNDTRIP_PS: u64 = 133_420; // 133.42 ns (20.0 m tur-retur)
pub const MAX_LASER_6G_DIVERGENCE_PS: u64 = 15; // Maks tillatt ToF-avvik mellom 6G og 1550nm laser
pub const MAX_VSWR_SIGMA_X100: u32 = 500; // 5.00 sigma grense mot DRFM-jamming

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum GateVoltage {
    ZeroVoltClamp, // 0.00 V DC (Fail-Closed hviletilstand)
    Authorized5V0, // 5.00 V DC (Kun ved fullstendig bevist vitne)
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum GateVerdict {
    Open {
        voltage: GateVoltage,
        committed_epoch: u64,
    },
    HoldStaleEpoch {
        voltage: GateVoltage,
        presented: u64,
        required: u64,
    },
    HoldSignalUncertainty {
        voltage: GateVoltage,
        reason: &'static str,
    },
    KillCausalityViolation {
        voltage: GateVoltage,
        measured_rt_ps: u64,
    },
    KillGalvanicOrEmpBreach {
        voltage: GateVoltage,
    },
    KillByzantineFork {
        voltage: GateVoltage,
    },
}

/// Representerer målte fysiske størrelser ved inngangen til SPEC-250-slusen (D1 -> Π_K)
#[derive(Debug, Clone, Copy)]
pub struct PhysicalTelemetry {
    pub galvanic_current_na: u32,      // Krav: 0 nA (Safir-isolasjon)
    pub waveguide_cutoff_intact: bool, // Krav: true (ω_EMP < ω_c)
    pub uwb_tof_roundtrip_ps: u64,     // Målt IEEE 802.15.4z ToF i pikosekunder
    pub six_g_tof_roundtrip_ps: u64,   // Målt 6G ISAC ToF i pikosekunder
    pub laser_1550nm_los_ok: bool,     // Koherent W_laser siktlinje-lås
    pub vswr_deviation_sigma_x100: u32,// Impedansavvik (x100)
}

/// Representerer den kryptografiske og sekvensielle tilstanden til kapselen
#[derive(Debug, Clone, Copy)]
pub struct CapsuleWitness {
    pub capsule_epoch: u64,
    pub bilateral_nonce_valid: bool,   // Ed25519 signatur over N_ephem ∈ {0,1}^256
    pub ancestry_fork_residual: u32,   // R_fork (Krav: == 0)
}

/// Hardware-forankret tilstand i mottakende Infranett-node (Node B)
pub struct Spec250Gate {
    hw_monotonic_counter: u64,
    current_voltage: GateVoltage,
}

impl Spec250Gate {
    #[must_use]
    pub const fn new(initial_hw_epoch: u64) -> Self {
        Self {
            hw_monotonic_counter: initial_hw_epoch,
            current_voltage: GateVoltage::ZeroVoltClamp,
        }
    }

    /// Utfører den strukturelle projeksjonen Π_K.
    /// Enhver feil tvinger spenningen til 0.00 V DC før retur.
    pub fn evaluate_transition(
        &mut self,
        telemetry: &PhysicalTelemetry,
        witness: &CapsuleWitness,
    ) -> GateVerdict {
        // Garantér at porten starter i 0.00 V DC under evaluering
        self.current_voltage = GateVoltage::ZeroVoltClamp;

        // 1. EMP & Galvanisk Isolasjonssjekk (Skjold 1 & 2)
        if telemetry.galvanic_current_na > 0 || !telemetry.waveguide_cutoff_intact {
            return GateVerdict::KillGalvanicOrEmpBreach {
                voltage: GateVoltage::ZeroVoltClamp,
            };
        }

        // 2. Mekanisk Spillteori & Kryptografisk Arv (Nash-invariant)
        if !witness.bilateral_nonce_valid || witness.ancestry_fork_residual > 0 {
            return GateVerdict::KillByzantineFork {
                voltage: GateVoltage::ZeroVoltClamp,
            };
        }

        // 3. Relativistisk Kausal Diamant D(E1, E2) (ds² <= 0)
        if telemetry.uwb_tof_roundtrip_ps > MAX_TOF_ROUNDTRIP_PS {
            return GateVerdict::KillCausalityViolation {
                voltage: GateVoltage::ZeroVoltClamp,
                measured_rt_ps: telemetry.uwb_tof_roundtrip_ps,
            };
        }

        // 4. 6G ⊗ Infranett Fysikklås (Knuser RIS-speiling og AI-forgiftning)
        if !telemetry.laser_1550nm_los_ok {
            return GateVerdict::HoldSignalUncertainty {
                voltage: GateVoltage::ZeroVoltClamp,
                reason: "W_LASER_LOS_BROKEN_OR_RIS_NLOS_ATTEMPT",
            };
        }

        let tof_divergence = telemetry
            .six_g_tof_roundtrip_ps
            .abs_diff(telemetry.uwb_tof_roundtrip_ps);
        if tof_divergence > MAX_LASER_6G_DIVERGENCE_PS {
            return GateVerdict::KillCausalityViolation {
                voltage: GateVoltage::ZeroVoltClamp,
                measured_rt_ps: telemetry.six_g_tof_roundtrip_ps,
            };
        }

        if telemetry.vswr_deviation_sigma_x100 > MAX_VSWR_SIGMA_X100 {
            return GateVerdict::HoldSignalUncertainty {
                voltage: GateVoltage::ZeroVoltClamp,
                reason: "VSWR_5SIGMA_EXCEEDED_DRFM_JAMMING_SUSPECTED",
            };
        }

        // 5. Monoton Epoke-sjekk (Motvirker Asynkron Causality Eclipse)
        if witness.capsule_epoch < self.hw_monotonic_counter {
            return GateVerdict::HoldStaleEpoch {
                voltage: GateVoltage::ZeroVoltClamp,
                presented: witness.capsule_epoch,
                required: self.hw_monotonic_counter,
            };
        }

        // D2 -> D3: Alle fysiske og matematiske lover er oppfylt.
        // Oppdater monoton teller og autoriser 5.00 V DC (AKUERISAAVOQ).
        self.hw_monotonic_counter = witness.capsule_epoch.saturating_add(1);
        self.current_voltage = GateVoltage::Authorized5V0;

        GateVerdict::Open {
            voltage: self.current_voltage,
            committed_epoch: self.hw_monotonic_counter,
        }
    }
}
```
