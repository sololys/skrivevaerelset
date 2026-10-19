# Infranett v0.5 — `SPEC-250-CLEAN` ($\Pi_{K,\text{clean}}$: $275\text{ nm}$ UV-C + $42\text{ kHz}$ PZT-4 Kavitasjonsrens) og `SPEC-250-MECH` ($\Pi_{K,\text{mech}}$: $500\text{ m}$ Elastostatikk, Bikube-Støttegitter og PZT-SHM for $\text{Al}_2\text{O}_3$ Safirflens)

**Dokument-ID:** `INFRANETT-V05-SPEC250-CLEAN-UVC-PZT-OG-MECH-500M-SPEC`  
**Versjon:** `1.0 (Canonical Biofouling Mitigation & 500m Structural Mechanics Specification)`  
**Dato:** `19. oktober 2026`  
**Forfatter / Entitet:** `Marius Egerhei Torjusen (Brahman)`  
**Epistemisk Status (`AGENTS.md`):**
* **`L0` (Elastostatikk, Bruddmekanikk, Fotoelastisitet & Akustisk Fysikk):** Kirchhoff–Love sirkulær platespenning (fritt opplagt rand $D_s = 12.0\text{ mm}$ vs. fast innspent bikube-celle $d_{\text{cell}} = 2.0\text{ mm}$), Griffith–Irwin kritisk sprekkdybde ($a_{\text{crit}} \approx 511\,\mu\text{m}$), Blake-kavitasjonsterskel ($P_B \ge 180\text{ kPa}$) og fotoelastisk ToF-invarians ($\Delta \tau_{\text{RT}} \approx -0.27\text{ fs}$ ved $50.47\text{ bar}$).
* **`L1` (Deterministisk Fastpunkt Rust- og Python-Kjerne):** Verifisert med heltallsaritmetikk i `spec250_gate.rs` (`#![no_std]`, `#![forbid(unsafe_code)]`, `#![deny(clippy::float_arithmetic)]`, `22/22 PASS`) og `infranett_laser_fso_witness_engine.py` (`15/15 PASS`). `INSPIRED_BY != IMPLEMENTS != PROVES`: Programvareledgere (`WAL`) er append-only SHA-256 hash-kjeder, ikke fysiske WORM-medier.
* **`L2/L3` (`HOLD` — Fysisk Trykktank-, Akustisk- og Biofouling-Validering):** Fysisk DNV-ST-0373 / ASME PVHO-1 trykkprøving ved $75.71\text{ bar}$ ($750\text{ m}$) og langsiktig marin eksponering tilhører fysisk maskinvareverifikasjon (`SPEC-250 HIL`).

---

## Del I: `SPEC-250-CLEAN` ($\Pi_{K,\text{clean}}$: Innvendig $275\text{ nm}$ UV-C + $42.0\text{ kHz}$ PZT-4 Kavitasjonsrens)

### Operasjonelt Sammendrag (Del I)

Renseprotokollen **SPEC-250-CLEAN ($\Pi_{K,\text{clean}}$)** opprettholder det optiske tapet i safir-dokkingvinduet permanent i **Biofouling Nivå 1** ($L_{\text{bio}} \le 2.13\text{ dB}$ over to vinduer, $d_{\text{bio}} \le 0.05\text{ mm}$) uten mekaniske viskere, pakninger eller elektriske gjennomføringer i skroget.

Systemet utnytter to fysiske egenskaper ved monokrystallinsk syntetisk safir ($\text{Al}_2\text{O}_3$, $d = 2.0\text{ mm}$):

1. **Dyp-UV Transparens ($T_{275\text{nm}} > 85\%$):** Mens vanlig kvarts-/borsilikatglass blokkerer eller degraderes av UV-C, tillater $\text{Al}_2\text{O}_3$ innvendig monterte AlGaN UV-C LED-er ($\lambda_{\text{UV}} = 275.0\text{ nm}$) å bestråle den våte ytterflaten direkte fra innsiden av Faraday-buret. Dette induserer tymindimerisering i DNA/RNA hos bakterier, diatomeer og rurlarver (*cypris*) før adhesjon.
2. **Høy Akustisk Impedans ($Z_{\text{Al}_2\text{O}_3} \approx 44.3\text{ MRayl}$):** En ringformet piezoelektrisk PZT-4-transduser, epoksy-bundet til innsiden av safirflensen, eksiterer høyfrekvente Rayleigh-overflatebølger og lokal akustisk kavitasjon ($f_{\text{pzt}} = 42.0\text{ kHz}$, $P_{\text{akustisk}} > P_{\text{Blake}}$) i sjøvannsfilmen. Kollapsende mikro-kavitasjonsbobler vasker bort dødt organisk materiale og silt uten at en eneste kobbertråd krysser skrogveggen ($I_{\text{galvanisk}} = 0.0\text{ }\mu\text{A}$).

For å forhindre optisk og akustisk selv-jamming av det relativistiske ToF-vitnet ($\Delta t_{\text{roundtrip}} \le 133.42\text{ ns}$ / $178.92\text{ ns}$), er renseaktivering og kommunikasjonsautorisasjon strengt gjensidig utelukkende (**gjensidig ortogonal lås** i maskinvare):

$$\text{CLEAN\_ACTIVE} = 1 \implies \Omega_{\text{SPEC-250}} = 0.00\text{ V DC (HOLD)} \quad \land \quad \Omega_{\text{SPEC-250}} = 5.00\text{ V DC} \implies P_{\text{UV}} = P_{\text{PZT}} = 0.00\text{ W}$$

---

### 1. Fysiske Konstanter, Operatorer og Invarianter for $\Pi_{K,\text{clean}}$

| Parameter / Operator | Matematisk Formulering & Rom | Terskel / Invariant | Konsekvens ved Avvik ($\Delta_K$) |
| :--- | :--- | :--- | :--- |
| **Fotonisk DNA-Inaktivering** ($\lambda_{\text{UV}}$) | AlGaN UV-C ved $\lambda_{\text{UV}} = 275.0\text{ nm}$ ($E_{\gamma} = 4.51\text{ eV}$) | Fluens $H_{\text{UV}} = I_{\text{UV}} \cdot \Delta t_{\text{uv}} \ge 25.0\text{ mJ/cm}^2$ ($\text{LD}_{99.9}$) | $H_{\text{UV}} < 15.0\text{ mJ/cm}^2 \implies \text{BIO\_DRIFT\_WARN}$ |
| **Safir UV-Transmisjon** ($T_{275}$) | $\text{Al}_2\text{O}_3$ ($d = 2.0\text{ mm}$, båndgap $E_g \approx 8.8\text{ eV}$) | $T(275\text{ nm}) \approx 86.4\%$ (Ingen solarisering) | $I_{\text{PD,uv\_mon}} < I_{\text{min}} \implies \text{HOLD\_UV\_FAULT}$ |
| **Akustisk Blake-Terskel** ($P_B$) | $P_B = P_0 - P_v + \frac{4}{3}\sigma_{st}\sqrt{\frac{3}{(R_0)^3 (P_0 - P_v + 2\sigma_{st}/R_0)}}$ | $P_{\text{akustisk}} \ge 180\text{ kPa}$ ved $f_{\text{pzt}} = 42.0\text{ kHz}$ | Under terskel $\implies$ Kun akustisk strømning (ingen skjærrens) |
| **Kavitasjons-Utlufting** ($\tau_{\text{clear}}$) | Oppdrift og oppløsning av mikro-bobler ($a_b \sim 20 - 150\text{ }\mu\text{m}$) | $\Delta t_{\text{post\_pzt}} \ge 2500\text{ ms}$ før $532\text{ nm}$ ToF-måling | Måling under $\tau_{\text{clear}} \implies L_{\text{Mie}} \gg 10\text{ dB} \implies \text{HOLD}$ |
| **Tilbake-refleksjon** ($R_{\text{bio}}$) | Intern skråvinkel-innskyting ($\theta_i = 38^\circ$) på $532\text{ nm}$ | Endring i spredt retur $\Delta I_{\text{scatter}} > 12\%$ utløser syklus | Vedvarende $\Delta I_{\text{scatter}} > 40\% \implies \text{HOLD\_FOULED}$ |
| **Termisk Sikring** ($\Delta T_{\text{flange}}$) | PZT + UV-C varmeutvikling mot sjøvannskjølesluk | $T_{\text{safir}} \le 45.0^\circ\text{C}$ ($\Delta T \le 25\text{ K}$) | $T_{\text{safir}} > 45.0^\circ\text{C} \implies \text{KILL\_CLEAN\_PWR}$ ($0.00\text{ V}$) |

---

### 2. Fysisk Konstruksjon og Strålegang (Uten Gjennomføringer)

For å bevare Faraday-buret og den evanescente bikube-bølgelederen ($\omega_{\text{EMP}} < \omega_c \approx 87.86\text{ GHz}$) uendret, er alle rensekomponenter plassert på den **tørre innsiden** av $\text{Al}_2\text{O}_3$-safirvinduet:

```text
   VÅT SIDE (Sjøvann / Jerlov III)       SAFIRVINDU          TØRR SIDE (Innside av Faraday-Bur)
   Biofilm d_bio <= 0.05 mm (Nivå 1)     Al₂O₃ (2.0 mm)      I_galvanisk = 0.0 μA (Ingen hull/pakninger)
                                         ┌──────────┐
                                         │          │ ◄─── [PZT-4 Piezo-Ring (42.0 kHz)]
      Kollapsende                        │          │       Bundet med akustisk epoksy til safir-rand.
      Kavitasjonsbobler (P > P_Blake) ◄──┤  Bikube  │       Sender ultrasoniske skjærbølger gjennom
      River løs silt og død biofilm      │  Kanal   │       krystallgitteret ut i grenseflaten.
                                         │ (d=2 mm) │
      DNA/RNA Tymindimerisering      ◄───┤  ||||||  │ ◄─── [275 nm AlGaN UV-C LED-Matrise]
      (H_UV >= 25 mJ/cm²)                │  ||||||  │       Koplet inn via kvartskollimator /
                                         │  ||||||  │       UV-reflekterende skråspeil (R_275 > 99%).
      532 nm & 1550 nm Kausal-Linje  ◄───┼──┼┼┼┼┼┼──┼────► [DM_532/1550 -> Si-APD & InGaAs TRX]
      (Strengt avstengt under rens)      │          │       Beskyttet av OD6 UV-blokkeringsfilter
                                         └──────────┘       (λ_cut < 350 nm) foran fotodetektorene.
```

#### A. Hvorfor UV-C ($275\text{ nm}$) + PZT ($42\text{ kHz}$) er Nødvendig i Kombinasjon

1. **Alene svikter UV-C mot uorganisk slam (*Silt Shielding*):** I Jerlov Type III-kystvann legger uorganisk leire og kalkpartikler seg på vinduet. Disse skjermer underliggende bakterier mot $275\text{ nm}$-fotoner.
2. **Alene krever kavitasjon høy kontinuerlig energi:** Hvis levende rurlarver (*barnacle cyprids*) først rekker å herde sitt sementprotein på safirflaten, kreves ekstrem akustisk intensitet for å rive dem løs.
3. **Synergi i $\Pi_{K,\text{clean}}$:** Periodisk $275\text{ nm}$ bestråling steriliserer grenseflaten slik at intet biologisk lim dannes, mens en kort $42.0\text{ kHz}$ piezoelektrisk kavitasjonspuls blåser vekk løse døde celler og uorganisk silt. Dermed låses vinduet permanent i **Nivå 1 ($L_{\text{bio}} \le 2.13\text{ dB}$)**.

#### B. Optisk Beskyttelse av Si-APD og InGaAs under UV-C Eksponering

En $275\text{ nm}$ fotonstrøm ($E_{\gamma} = 4.51\text{ eV}$) vil generere kraftig mørkestrøm og potensielt degradere antirefleksbelegget på $\text{Si-APD}$-en dersom den treffer detektoren direkte. Derfor sitter et hardt dielektrisk langpass-filter ($\lambda_{\text{pass}} > 400\text{ nm}$, $\text{OD} > 6$ ved $275\text{ nm}$) foran $\text{DM}_{532/1550}$-stråledeleren, og høyspennings-bias ($V_{\text{bias}} \approx 120\text{ V}$) til $\text{Si-APD}$ kobles fysisk fra under UV-C-pulsen.

#### C. Akustisk-Optisk Interlock (Unngåelse av Selv-Indusert Mie-Blokkering)

En tett kavitasjonssky ($\text{VF}_b = 5 \times 10^{-3}$) gir et Mie-spredningstap på $130.3\text{ dB/m}$ og forårsaker romlignende flerbane-spredning ($ds^2 > 0$). Protokollen håndhever derfor en obligatorisk **Boble-Utluftingsfase (`STATE :: DEGASS_WAIT`, $\tau_{\text{clear}} \ge 2500\text{ ms}$)** etter hver PZT-puls, verifisert ved at intern $532\text{ nm}$ tilbakespredning ($\Delta I_{\text{scatter}}$) faller tilbake til basislinjen før porten gjenåpner for ekstern trafikk.

---

### 3. Deterministisk Tilstandsmaskin for Rensesyklusen

```text
[IDLE_READY: Vindu i Nivå 1 (L_bio <= 2.13 dB)]
  │  • UV-C = 0.00 V, PZT = 0.00 V
  │  • Port klar for D1->D3 ToF-evaluering
  │
  ├─► Trigger: Timer (Δt >= 3600 s) ELLER Optisk Spredning (ΔI_scatter > 12%)
  │   Pre-betingelse: Ingen aktiv ToF-handshake (SPEC250_GATE == 0.00 V DC)
  ▼
[PHASE_1_INTERLOCK_LOCKDOWN]
  │  • Lås SPEC-250 til GATE :: HOLD_MAINTENANCE (0.00 V DC)
  │  • Koble fra Si-APD HV-bias (beskytt mot UV-blending)
  ▼
[PHASE_2_UVC_STERILIZATION (Δt_uv = 15.0 s)]
  │  • Aktiver 275 nm AlGaN LED-matrise (I_uv = 2.0 mW/cm² -> H_uv = 30.0 mJ/cm²)
  │  • Verifiser UV-fotodiode-vitne (W_uv_ok == 1) og T_safir <= 45.0 °C
  ▼
[PHASE_3_PZT_CAVITATION_BURST (Δt_pzt = 2.0 s)]
  │  • Deaktiver UV-C; aktiver 42.0 kHz PZT-ring i pulser (Duty = 20%, P > 180 kPa)
  │  • Mikro-jetstråler fra kollapsende bobler løsner død biofilm og silt
  ▼
[PHASE_4_MIE_DEGASS_WAIT (τ_clear >= 2.5 s)]
  │  • PZT = 0.00 V; vent til kavitasjonsbobler forlater strålebanen (VF_b -> 0)
  │  • Send lav-effekt 532 nm testpuls: Mål intern Fresnel/Mie-refleksjon (I_scatter)
  ├──────────────┬───────────────────────────────────────┐
  │ I_scatter OK │ (L_bio <= 2.13 dB)                    │ I_scatter > Terskel (Etter 3 forsøk)
  ▼              │                                       ▼
[RETURN TO IDLE_READY]                        [GATE :: HOLD_WINDOW_OCCLUDED (0.00 V DC)]
  • Koble inn Si-APD HV-bias                    • Logg kryptografisk vedlikeholdsvitne i WAL
  • Åpne for 532nm / 1550nm ToF                 • Krev fysisk inspeksjon (aldri 5.00 V i blinde)
```

---

## Del II: `SPEC-250-MECH` ($\Pi_{K,\text{mech}}$: Elastostatikk, Bikube-Støttegitter og PZT-SHM ved $500\text{ m}$ Dyp)

### Operasjonelt Sammendrag (Del II)

Den mekaniske konstruksjons- og trykkspesifikasjonen **SPEC-250-MECH ($\Pi_{K,\text{mech}}$)** fastsetter de eksakte elastostatikk-, bruddmekanikk- og piezo-akustiske grensene for innfesting av et monokrystallinsk syntetisk safirvindu ($\text{Al}_2\text{O}_3$, tykkelse $t = 2.00\text{ mm}$, $c$-akse $0^\circ$ orientering) i en Grad 5 titanflens ($\text{Ti-6Al-4V}$) med integrert $\text{PZT-4}$ kavitasjonsring ved $h = 500.0\text{ m}$ dyp i nordisk kystvann ($\rho_{\text{sw}} = 1028.0\text{ kg/m}^3$).

Ved $500.0\text{ m}$ dyp utsettes vinduet for et hydrostatisk differensialtrykk på $\Delta P_{\text{op}} = 5.047\text{ MPa}$ ($50.47\text{ bar}$) og et dimensjonerende prøvetrykk ($1.5\times$ sikkerhetsfaktor, DNV-ST-0373 / ASME PVHO-1) på $\Delta P_{\text{proof}} = 7.571\text{ MPa}$ ($75.71\text{ bar}$). Fordi den evanescente EMP-sperren ($\omega_{\text{EMP}} < \omega_c \approx 87.86\text{ GHz}$) allerede krever en metallisk bikube-bølgeleder ($d_{\text{cell}} = 2.00\text{ mm}$), integreres $\text{Ti-6Al-4V}$ bikube-matrisen som et **strukturelt trykk-støttegitter (*Structural Honeycomb Backing Grid*)** direkte på safirens tørre innside:

1. **Multi-Skala Spenningsreduksjon:** Når bikube-gitteret har full mekanisk kontakt med safirvinduets bakside, reduseres det frie spennet fra den optiske totalblenderen ($D_s = 12.00\text{ mm}$) til enkeltcellen ($d_{\text{cell}} = 2.00\text{ mm}$). Den maksimale bøyespenningen ved $500\text{ m}$ dyp faller da fra $\sigma_{\max,\text{full}} = 55.70\text{ MPa}$ ($\text{SF}_{\text{op}} = 7.18$) til $\sigma_{\max,\text{cell}} = 0.946\text{ MPa}$ ($\text{SF}_{\text{cell}} = 422.8$ mot safirens bøye-bruddstyrke $\sigma_{f,\text{safir}} = 400.0\text{ MPa}$).
2. **Selvforseglende Hydrostatisk Konsekvensport:** Våt-til-tørr-tetningen er konstruert slik at økende vanntrykk $\Delta P_{\text{op}}$ komprimerer safirvinduet hardere mot det primære $\text{Ti-6Al-4V}$ skuldersetet og en sekundær gullbelagt C-ring ($\text{Inconel 718 / Au}$). Ved $500\text{ m}$ dyp endres den optiske faselengden gjennom vinduet med kun $\Delta \tau_{\text{vindu, RT}} = -0.27\text{ fs}$, hvilket holder Minkowski-diamanten $\mathcal{D}(E_1, E_2)$ ($\Delta t_{\text{RT}} \le 133.42\text{ ns}$ / $178.92\text{ ns}$) absolutt invariant.

$$\Phi_{\text{hydro}}(50.47\text{ bar}) \xrightarrow{\text{Al}_2\text{O}_3 \otimes \text{Ti-6Al-4V}} \Pi_{K,\text{mech}}\big(\sigma_{\max} \ll \sigma_{\text{tillatt}} \land I_{\text{galv}} = 0.0\text{ }\mu\text{A}\big) \xrightarrow{\Omega} \text{AKUERISAAVOQ}$$

---

### 4. Materialegenskaper, Konstanter og Grensebetingelser

| Parameter / Konstant | Symbol | $\text{Al}_2\text{O}_3$ Safir ($0^\circ$ $c$-akse) | $\text{Ti-6Al-4V}$ (Grad 5, ELI) | $\text{PZT-4}$ (Hård Piezo-Keram) |
| :--- | :--- | :--- | :--- | :--- |
| **Elastisitetsmodul (Youngs)** | $E$ | $345.0\text{ GPa}$ | $113.8\text{ GPa}$ | $81.3\text{ GPa}$ ($Y_{11}^E$) |
| **Poissons forhold** | $\nu$ | $0.270$ | $0.342$ | $0.330$ |
| **Trykkstyrke (Kompresjon)** | $\sigma_{c,\text{ult}}$ | $2100.0\text{ MPa}$ | $970.0\text{ MPa}$ | $520.0\text{ MPa}$ |
| **Bøye-/Strekkstyrke** | $\sigma_{f,\text{ult}}$ | $400.0\text{ MPa}$ (Weibull $m \approx 12$) | $880.0\text{ MPa}$ ($\sigma_{y,0.2}$) | $76.0\text{ MPa}$ (Dynamisk strekk) |
| **Bruddseighet (Modus I)** | $K_{\text{IC}}$ | $2.50\text{ MPa}\cdot\text{m}^{1/2}$ | $75.0\text{ MPa}\cdot\text{m}^{1/2}$ | $1.10\text{ MPa}\cdot\text{m}^{1/2}$ |
| **Termisk utvidelse (CTE)** | $\alpha_T$ | $5.30 \times 10^{-6}\text{ K}^{-1}$ ($\perp c$) | $8.60 \times 10^{-6}\text{ K}^{-1}$ | $4.00 \times 10^{-6}\text{ K}^{-1}$ |
| **Akustisk impedans** | $Z = \rho c_L$ | $44.3\text{ MRayl}$ ($\rho = 3980\text{ kg/m}^3$) | $27.3\text{ MRayl}$ ($\rho = 4430\text{ kg/m}^3$) | $34.5\text{ MRayl}$ ($\rho = 7500\text{ kg/m}^3$) |
| **DC Resistivitet** | $\rho_{\text{DC}}$ | $> 10^{14}\text{ }\Omega\cdot\text{m}$ (Isolator) | $1.78 \times 10^{-6}\text{ }\Omega\cdot\text{m}$ (Faraday-bur) | Isolert på tørr side |

---

### 5. Eksakt Utledning av Trykk, Spenning og Nedbøyning ved $500\text{ m}$ Dyp

#### A. Hydrostatisk Trykkgrunnlag ved $h = 500.0\text{ m}$

I nordisk kystvann (salinitet $35\text{ PSU}$, $T = 4.0^\circ\text{C}$) er tettheten $\rho_{\text{sw}} = 1028.0\text{ kg/m}^3$ og tyngdeakselerasjonen ved $60^\circ\text{ N}$ (Skagerrak/Norskekysten) $g = 9.819\text{ m/s}^2$:

$$P_{\text{hydro}}(500\text{ m}) = \rho_{\text{sw}} \cdot g \cdot h = 1028.0\text{ kg/m}^3 \cdot 9.819\text{ m/s}^2 \cdot 500.0\text{ m} = 5\,046\,966\text{ Pa} \approx 5.047\text{ MPa}$$

$$\Delta P_{\text{op}} = 5.047\text{ MPa} \text{ (}50.47\text{ bar)}, \qquad \Delta P_{\text{proof}} = 1.5 \cdot \Delta P_{\text{op}} = 7.571\text{ MPa} \text{ (}75.71\text{ bar)}, \qquad \Delta P_{\text{crush}} = 2.5 \cdot \Delta P_{\text{op}} = 12.618\text{ MPa} \text{ (}126.18\text{ bar)}$$

#### B. Kirchhoff–Love Platespenning (To-Nivå Verifikasjon for $t = 2.00\text{ mm}$)

1. **Konservativt Grensetilfelle 1 — Fritt opplagt over hele $D_s = 12.00\text{ mm}$ ($a_s = 6.00\text{ mm}$):**

$$\sigma_{\max,\text{full}} = \frac{3(3 + \nu)}{8} \cdot \Delta P \cdot \left(\frac{a_s}{t}\right)^2 = 11.03625 \cdot \Delta P$$

   * Ved $500\text{ m}$ drift ($\Delta P_{\text{op}} = 5.047\text{ MPa}$): $\sigma_{\max,\text{full}} = 55.70\text{ MPa} \implies \text{SF}_{\text{op}} = 7.18$, $w_{\max,\text{full}} \approx 1.71\,\mu\text{m}$.
   * Ved $750\text{ m}$ prøvetrykk ($\Delta P_{\text{proof}} = 7.571\text{ MPa}$): $\sigma_{\max,\text{full}} = 83.56\text{ MPa} \implies \text{SF}_{\text{proof}} = 4.79$.
2. **Operasjonelt Tilfelle 2 — Støttet av $\text{Ti-6Al-4V}$ Bikube-Bølgeleder ($d_{\text{cell}} = 2.00\text{ mm}$, $a_{\text{cell}} = 1.00\text{ mm}$):**

$$\sigma_{\max,\text{cell}} = \frac{3}{4} \cdot \Delta P_{\text{op}} \cdot \left(\frac{a_{\text{cell}}}{t}\right)^2 = 0.75 \cdot 5.047\text{ MPa} \cdot 0.25 = 0.946\text{ MPa} \implies \text{SF}_{\text{cell}} = 422.8$$

#### C. Flens-Sete Kompresjon, Skjær og Bruddmekanikk ($K_{\text{IC}}$)

* **Effektivt bærende seteareal i $\text{Ti-6Al-4V}$:** $A_{\text{sete}} = 188.62\text{ mm}^2 - 90.48\text{ mm}^2 = 98.14\text{ mm}^2$.
* **Total aksial hydrostatisk kraft ($D_{\text{tetning}} = 19.60\text{ mm}$):** $F_{\text{hydro}}(500\text{ m}) = 5.047\text{ MPa} \cdot 301.72\text{ mm}^2 = 1522.8\text{ N}$.
* **Gjennomsnittlig kompresjonsspenning på setet:** $\sigma_{\text{sete}}(500\text{ m}) = 15.52\text{ MPa} \ll \sigma_{y,\text{Ti}} = 880.0\text{ MPa}$ ($\text{SF} = 56.70$).
* **Kritisk defektstørrelse (Griffith–Irwin):**

$$a_{\text{crit}} = \frac{1}{\pi} \left(\frac{K_{\text{IC}}}{Y \cdot \sigma_{\max,\text{full}}}\right)^2 = \frac{1}{\pi} \left(\frac{2.50}{1.12 \cdot 55.70}\right)^2 \approx 511\text{ }\mu\text{m} \gg a_0 < 2.0\text{ }\mu\text{m}$$

---

### 6. Mekanisk Tverrsnitt og Kraftflyt ved $500\text{ m}$ Dyp ($\Pi_{K,\text{mech}}$)

```text
   VÅT SIDE (500 m dyp: P_op = 5.047 MPa / 50.47 bar)            TØRR SIDE (Faraday-Bur: 0.10 MPa)
   Sjøvann (ρ = 1028 kg/m³, σ_sw ≈ 4.8 S/m)                      I_galvanisk = 0.0 μA (Galvanisk lukket)
 
                        F_hydro = 1522.8 N
                    │    │    │    │    │    │
                    ▼    ▼    ▼    ▼    ▼    ▼
       ┌────────────┬────────────────────────┬────────────┐
       │ Ti-6Al-4V  │  Fluorsilikon-buffer   │ Ti-6Al-4V  │  ◄── Krympeklaring Δr = 50 μm (tar opp CTE)
       │ Holde-ring ├────────────────────────┤ Holde-ring │
       ├────────────┤   Al₂O₃ Safirvindu     ├────────────┤
       │            │  t = 2.00 mm (0° c)    │            │
       │  Primær-   │  D_ytre = 20.00 mm     │  Primær-   │
       │  tetning   │  w_max(cell) < 0.05 μm │  tetning   │
       │ (Au/In718  ├────┬───┬──────┬───┬────┤ (Au/In718  │
       │  C-Ring)   │Sete│PZT│ Sete │PZT│Sete│  C-Ring)   │
       │            │ Ti │-4 │||||||│-4 │ Ti │            │  ◄── PZT-4 i avlastet spor (σ_pre = 18 MPa)
       │            │    └───┤||||||├───┘    │            │      Sender 42 kHz Rayleigh-bølger inn i Al₂O₃
       │            │ Ti-6Al-4V Flens-Skulder│            │
       └────────────┴────────┤||||||├────────┴────────────┘
                             │||||||│                        ◄── Integrert Ti-6Al-4V Bikube-Bølgeleder
                             │||||||│                            (d_cell = 2.0 mm, L = 7.0 mm, >112 dB EMP)
                                ││                               Fungerer som strukturelt trykk-støttegitter!
                                ▼▼
                    532 nm / 1550 nm / 275 nm UV-C
                    Til Dikroisk Speil (DM_532/1550)
```

---

### 7. Oppsummeringstabell: Sikkerhetsfaktorer og Fail-Closed Grenser

| Mekanisk / Fysisk Modus | Belastning ved 500 m ($50.47\text{ bar}$) | Belastning ved Prøvetrykk ($75.71\text{ bar}$) | Materialgrense (Brudd / Flyt) | Sikkerhetsfaktor ($\text{SF}_{500\text{m}}$) | Fail-Closed Sensor & Dom ($\Pi_K$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Safir Bøyespenning (Uten gitterstøtte)** | $55.70\text{ MPa}$ | $83.56\text{ MPa}$ | $400.0\text{ MPa}$ | **$7.18$** | PZT Impedans-skift $\implies \text{KILL}$ |
| **Safir Bøyespenning (Med bikube-støtte)** | $0.95\text{ MPa}$ | $1.42\text{ MPa}$ | $400.0\text{ MPa}$ | **$422.8$** | PZT Impedans-skift $\implies \text{KILL}$ |
| **$\text{Ti-6Al-4V}$ Skulder Kompresjon** | $15.52\text{ MPa}$ | $23.28\text{ MPa}$ | $880.0\text{ MPa}$ | **$56.70$** | Elastisk regime |
| **Safir Skjærspenning ved Setekant** | $6.32\text{ MPa}$ | $9.48\text{ MPa}$ | $250.0\text{ MPa}$ | **$39.56$** | Ingen delaminering |
| **$\text{PZT-4}$ Aksial Forspenning** | $18.00\text{ MPa}$ | $22.50\text{ MPa}$ | $520.0\text{ MPa}$ (Komp.) | **$28.89$** | Overvåket via $f_{\text{res}} \approx 42\text{ kHz}$ |
| **Hulroms-Fukt / Lekkasje ($I_{\text{galv}}$)** | $0.00\text{ nA}$ | $0.00\text{ nA}$ | $> 1.0\text{ nA}$ | **$\infty$ (Isolert)** | $I_{\text{galv}} > 0 \implies \text{KILL}$ ($0.00\text{ V}$) |

---

### 8. Referanseimplementasjon i Rust (`spec250_gate.rs`)

Se [`engines/spec250_gate.rs`](../engines/spec250_gate.rs) for den kjørbare, heltallsbaserte `#![forbid(unsafe_code)]`-implementasjonen av både `SapphireCleanController::step_clean_fsm` (`SPEC-250-CLEAN`) og `evaluate_flange_integrity` (`SPEC-250-MECH`), verifisert med `22/22` enhetstester i `rustc --test`.
