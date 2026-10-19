# Infranett v0.5 — Maritim Dual-Lambda Safir-Port ($\Pi_{K,\text{maritim}}$: $532\text{ nm} \leftrightarrow 1550\text{ nm}$) og Radiometrisk Effektbudsjett i Jerlov Type III Kystvann, Biofouling og Mie-Kavitasjon

**Dokument-ID:** `INFRANETT-V05-MARITIM-SAFIR-JERLOV-III-RADIOMETRI-SPEC`  
**Versjon:** `1.0 (Canonical Maritime Optical & Radiometric Specification)`  
**Dato:** `19. oktober 2026`  
**Forfatter / Entitet:** `Marius Egerhei Torjusen (Brahman)`  
**Epistemisk Status (`AGENTS.md`):**
* **`L0` (Optisk Fysikk, Fresnel-Refleksjon, Beer–Lambert & Mie-Ekstinksjon):** Eksakte utledninger for brytningsindeks-tilpasning over $\text{Al}_2\text{O}_3$ safirvindu ($n_s(532) = 1.772$, $n_{\text{sw}}(532) = 1.341 \implies R_{\text{sw}} \approx 1.92\%$), spektral båndgap-isolasjon ($\text{Si-APD}$ $E_g \approx 1.12\text{ eV}$ vs. $\text{InGaAs}$ med $\text{OD} > 6$ langpass), Jerlov Type III attenuasjon ($1.824\text{ dB/m}$) og geometrisk Mie-spredning på kavitasjonsbobler ($Q_{\text{ext}} \approx 2.0$).
* **`L1` (Deterministisk Fastpunkt Rust- og Python-Kjerne):** Verifisert med heltalls millidesibel- ($\text{mdB}$) og pikosekund-aritmetikk i `spec250_gate.rs` (`#![no_std]`, `#![forbid(unsafe_code)]`, `#![deny(clippy::float_arithmetic)]`) og `infranett_laser_fso_witness_engine.py`. `INSPIRED_BY != IMPLEMENTS != PROVES`: Programvareledgere (`WAL`) er append-only SHA-256 hash-kjeder, ikke fysiske WORM-medier.
* **`L2/L3` (`HOLD` — Fysisk Maritim & Optisk HIL-Validering):** Fysisk våt-dokking i trykktank/kystvann, UV-C biofouling-vedlikehold og høyeffekt dazzler-eksponering tilhører fysisk maskinvareverifikasjon (`SPEC-250 Maritim HIL`).

---

## Del I: Maritim Dual-Lambda Safir-Port ($\Pi_{K,\text{maritim}}$: $532\text{ nm} \to 1550\text{ nm}$ Våt-til-Tørr Transduksjon)

### Operasjonelt Sammendrag (Del I)

Port-overgangen mellom en undervanns K-POD-kurer ($\lambda_1 = 532\text{ nm}$, blågrønt transmisjonsvindu i sjøvann) og en overflate-/kainode ($\lambda_2 = 1550\text{ nm}$, atmosfærisk øyesikker FSO) ved en maritim safir-dokkingstasjon realiseres som en galvanisk isolert, to-frekvent optisk konsekvensport ($\Pi_{K,\text{maritim}}$).

Overgangen forbyr enhver elektrisk konduksjon ($I_{\text{galvanisk}} = 0.0\text{ }\mu\text{A}$) og løser den fysiske faseovergangen mellom saltvann ($n_{\text{sw}} \approx 1.338\text{–}1.341$, høy elektrisk ledningsevne $\sigma_{\text{sw}} \approx 4.8\text{ S/m}$) og tørr atmosfære ($n_{\text{air}} \approx 1.0003$) gjennom et syntetisk monokrystallinsk safirvindu ($\text{Al}_2\text{O}_3$, $d = 2.0\text{ mm}$) kombinert med en dikroisk bølgeleder-arkitektur.

Ingen datapakke konverteres direkte fra $532\text{ nm}$ til $1550\text{ nm}$ som en blind analog repeater; transduksjonen krever at den innkommende $532\text{ nm}$-tilstanden passerer den relativistiske kausale diamanten $\mathcal{D}(E_1, E_2)$, består mekanisk spillteoretisk validering ($R_{\text{fork}} = 0$), og autoriseres til $5.00\text{ V DC}$ før den re-emitteres på $1550\text{ nm}$ FSO-bussen.

$$\Phi_{532\text{nm}} \xrightarrow{\text{Al}_2\text{O}_3\text{ Dokking}} \Pi_{K}\big(\mathcal{D}(E_1,E_2) \land \text{Nash}\big) \xrightarrow{\Omega\text{ (5.00 V)}} W_{\text{WAL}} \xrightarrow{\text{Transduksjon}} \text{FSO}_{1550\text{nm}} \implies \text{AKUERISAAVOQ}$$

---

### 1. Fysiske Rom, Konstanter og Optiske Parametere

| Parameter / Operator | Symbol | Sjøvann / Våt Side ($\lambda_1$) | Safir-Barriere ($\text{Al}_2\text{O}_3$) | Atmosfære / Tørr Side ($\lambda_2$) |
| :--- | :--- | :--- | :--- | :--- |
| **Operativ Bølgelengde** | $\lambda$ | $532.0\text{ nm}$ (Nd:YAG $2\omega$) | Transmisjonsbånd: $150 - 5500\text{ nm}$ | $1550.0\text{ nm}$ (InGaAsP C-bånd) |
| **Frekvens** | $\nu = c/\lambda$ | $563.52\text{ THz}$ | — | $193.41\text{ THz}$ |
| **Brytningsindeks (Fase/Gruppe)** | $n(\lambda)$ | $n_{\text{sw}}(532) \approx 1.341$ | $n_s(532) = 1.772$, $n_s(1550) = 1.746$ | $n_{\text{air}}(1550) \approx 1.00027$ |
| **Fysisk Forplantningshastighet** | $v_p = c / n$ | $2.2356 \times 10^8\text{ m/s}$ | $1.6918 \times 10^8\text{ m/s}$ ($532\text{ nm}$) | $2.9971 \times 10^8\text{ m/s}$ |
| **Dempingskoeffisient** | $\alpha$ | $\sim 0.15\text{–}1.824\text{ dB/m}$ (kystvann) | $< 0.001\text{ dB/mm}$ | $\sim 0.2\text{ dB/km}$ (klarvær) |
| **Sjøvannets Ledningsevne** | $\sigma_{\text{sw}}$ | $\approx 4.8\text{ S/m}$ (kortslutter RF/6G) | $\sigma_{\text{Al}_2\text{O}_3} < 10^{-14}\text{ S/m}$ ($R_{\text{DC}} \to \infty$) | $\approx 0\text{ S/m}$ |
| **Fotodetektor-Arkitektur** | $\text{PD}_i$ | Si-APD (Silisium lavinefotodiode) | — | InGaAs PIN / APD |

---

### 2. Fysisk og Optisk Port-Arkitektur (Våt-til-Tørr Grensesnitt)

Ved dokking i maritimt miljø (kai-sluse, ubåtskrog eller autonom bøye) oppstår tre fysiske utfordringer som porten løser deterministisk:

#### A. Brytningsindeks-Matching og Fresnel-Tap ved Våt Dokking

Når K-POD-enheten dokker mot kai-nodens safirvindu under eller i vannlinjen, befinner det seg en tynn film av sjøvann ($d_{\text{film}} \in [0.05, 2.0]\text{ mm}$) mellom K-POD-ens safirvindu ($\text{W}_A$) og kai-nodens safirvindu ($\text{W}_B$).

* **Uten optisk tilpasning:** Overgangen Safir $\to$ Luft $\to$ Safir gir en høy brytningsindekskontrast ($\Delta n = 1.772 - 1.000 = 0.772$), som medfører Fresnel-refleksjonstap per flate på:

$$R_{\text{air}} = \left(\frac{n_s - n_{\text{air}}}{n_s + n_{\text{air}}}\right)^2 = \left(\frac{1.772 - 1.000}{2.772}\right)^2 \approx 7.75\%$$

* **Med sjøvann i dokkingspalten:** Sjøvann ($n_{\text{sw}} = 1.341$) fungerer som en naturlig indeks-matchende væske mellom safirvinduene:

$$R_{\text{sw}}(532\text{ nm}) = \left(\frac{n_s - n_{\text{sw}}}{n_s + n_{\text{sw}}}\right)^2 = \left(\frac{1.772 - 1.341}{1.772 + 1.341}\right)^2 = \left(\frac{0.431}{3.113}\right)^2 \approx 1.92\% \text{ per grenseflate}$$

* **Hvorfor $1550\text{ nm}$ stanses av vannfilmen mens $532\text{ nm}$ passerer:** Vann har en absorpsjonskoeffisient ved $\lambda_2 = 1550\text{ nm}$ på $\alpha_{\text{H}_2\text{O}}(1550) \approx 12.0\text{ cm}^{-1}$ ($\sim 52\text{ dB/cm}$), mens absorpsjonen ved $\lambda_1 = 532\text{ nm}$ er $\alpha_{\text{H}_2\text{O}}(532) \approx 0.00045\text{ cm}^{-1}$. Dersom spalten er fylt med sjøvann eller sjøsprøyt under dokking, kveles $1550\text{ nm}$, mens $532\text{ nm}$ krysser spalten tilnærmet tapsfritt.

#### B. Koaksial Dikroisk Stråledeler Bak Safirvinduet

For at samme fysiske safir-port ($d = 2.0\text{ mm}$ tykkelse, innfelt i en $\text{Ti-6Al-4V}$ titanflens med bikube-bølgeleder) skal kunne håndtere både våt dokking ($532\text{ nm}$) og tørr atmosfærisk siktlinje ($1550\text{ nm}$), benyttes et passivt dikroisk speil ($\text{DM}_{532/1550}$) på innsiden av Faraday-buret:

1. **Refleksjonsbånd ($\lambda_1 = 532\text{ nm}$):** $\text{DM}_{532/1550}$ har dielektrisk belegg med reflektivitet $R(532\text{ nm}) > 99.5\%$ ved $45^\circ$ innfallsvinkel, og styrer den blågrønne strålen direkte til Silisium-APD-mottakeren ($\text{RX}_{532}$) og $532\text{ nm}$ laserdioden ($\text{TX}_{532}$).
2. **Transmisjonsbånd ($\lambda_2 = 1550\text{ nm}$):** $\text{DM}_{532/1550}$ har transmisjon $T(1550\text{ nm}) > 98.5\%$, slik at den infrarøde FSO-strålen passerer rett gjennom langs den optiske hovedaksen til InGaAs-transceiveren ($\text{TRX}_{1550}$).

#### C. Relativistisk ToF-Skalering i Maritimt Medium ($\mathcal{D}_{\text{sw}}(E_1, E_2)$)

Under optisk avstandsbegrensning (*Distance Bounding*) i sjøvann er forplantningshastigheten redusert av brytningsindeksen $n_{\text{sw}} = 1.341$:

$$v_{\text{sw}} = \frac{c}{n_{\text{sw}}} \approx 2.2356 \times 10^8\text{ m/s}$$

* **Ved direkte fysisk safir-mot-safir dokking ($r_{\text{dock}} \le 0.10\text{ m}$):**

$$\Delta t_{\text{budget, dock}} = \frac{2 \cdot 0.10\text{ m}}{v_{\text{sw}}} + \tau_{\text{APD\_turnaround}} \approx 0.895\text{ ns} + \tau_{\text{hw}} \le 2.50\text{ ns}$$

* **Ved sub-overflate nær-sone ($r_{\max} = 20.0\text{ m}$ i vann):**

$$\Delta t_{\text{budget, sw}} = \frac{2 \cdot 20.0\text{ m}}{2.2356 \times 10^8\text{ m/s}} \approx 178.92\text{ ns}$$

*(Merk: Port-kontrolleren velger strengt det strammeste tidsbudsjettet basert på dokking-sensorens våt/kontakt-status; ved fysisk dokking låses $\Delta t_{\text{budget}}$ til dokking-profilen).*

---

### 3. Konstruksjons- og Transduksjonsdiagram ($\Pi_{K,\text{maritim}}$)

```text
  VÅT SIDE (Sjøvann / K-POD)        SAFIR-BARRIERE         TØRR SIDE (Faraday-Bur / Kainode)
  σ_sw ≈ 4.8 S/m (EMP/RF dør)     Al₂O₃ (d = 2.0 mm)      I_galvanisk = 0.0 μA (R_DC -> ∞)
                                  Bikube (d_h = 2 mm)
 ┌──────────────────────────┐         ┌────────┐         ┌───────────────────────────────────┐
 │ K-POD (Node A)           │         │  ||||  │         │  Dikroisk Speil (DM_532/1550)     │
 │                          │ 532 nm  │  ||||  │ 532 nm  │         ╲                         │
 │ [TX/RX 532nm] ───────────┼────────►│  ||||  ├─────────┼────────► ╲ ──► [trx_1550nm FSO]   │
 │ (Blågrønn Laser)         │◄────────┤  ||||  │◄────────┼───────── ╱ ◄── (1550 nm til Kai)  │
 └──────────────────────────┘  ToF    │  ||||  │         │         │                         │
                              Δt_RT   └────────┘         │         ▼ Reflektert 532 nm       │
                                       >112 dB           │  [Si-APD RX_532 / LD TX_532]      │
                                      EMP-Sperre         │         │                         │
                                                         │         ▼ (D1: Kun Kandidat-Bits) │
                                                         │  ┌─────────────────────────────┐  │
                                                         │  │ Π_K: SPEC-250 PORTVAKT      │  │
                                                         │  │ • ds² <= 0 (ToF_532 <= T_m) │  │
                                                         │  │ • Ed25519(N_ephem) == VALID │  │
                                                         │  │ • C_in >= C_hw ∧ R_fork == 0│  │
                                                         │  └──────┬───────────────┬──────┘  │
                                                         │    OPEN │ (5.00 V DC)   │ KILL    │
                                                         │         ▼               ▼ (0.00V) │
                                                         │  [D2/D3: SHA-256 WAL] [JORDING]   │
                                                         │         │                         │
                                                         │         ▼ Autorisert Re-Emisjon   │
                                                         │  [1550 nm Laser-Driver Aktivert]  │
                                                         └───────────────────────────────────┘
```

---

### 4. Sikkerhetsinvarianter for Bølgelengde-Transduksjon ($532\text{ nm} \to 1550\text{ nm}$)

For å forhindre at den optiske overgangen utnyttes som et passivt optisk relé (*Optical Wormhole Attack*), håndheves tre absolutte regler i maskinvare:

1. **Forbud mot Analog / All-Optisk Transduksjon (Ingen OEO-Repeater):**
   * En uautorisert fotonstrøm på $532\text{ nm}$ kan aldri direkte-modulere $1550\text{ nm}$-laseren. Strømmen til $1550\text{ nm}$ laser-driveren styres fysisk av utgangen på SPEC-250 NO-MOSFET-slusen ($V_{\text{gate}} \in \{0.00\text{ V}, 5.00\text{ V}\}$).
   * Så lenge $\Pi_K$ ikke har verifisert hele kapselen, ligger $1550\text{ nm}$ TX-trinnet fysisk klampet til $0.00\text{ V DC}$.
2. **Termodynamisk Kostnad ved Optisk Støy-Injeksjon ($\Delta U_{\text{cheat}} < 0$):**
   * Dersom en fiendtlig undervannsdrone skyter en kraftig $532\text{ nm}$ blendings- eller spoofing-laser mot safirvinduet, absorberes energien uten at noen prosessering eller videresending skjer på $1550\text{ nm}$-siden.
   * Ved fotostrøm over metningsterskelen ($I_{\text{PD, 532}} > I_{\text{sat}}$) eller brudd på ekstremal ToF-grense, forblir porten i `GATE :: HOLD / KILL` ($0.00\text{ V DC}$), og angriperen tapper eget batteri i sjøvann uten nettverksmutasjon ($G = 0$).
3. **Spektral Kryss-Isolasjon (Optisk Bandgap-Sperre):**
   * Silisium-detektoren ($\text{Si-APD}$, båndgap $E_g \approx 1.12\text{ eV}$, avskjæringsbølgelengde $\lambda_c \approx 1100\text{ nm}$) er fysisk blind for $1550\text{ nm}$-fotoner ($E_{\text{foton}} = 0.80\text{ eV} < E_g$).
   * Foran InGaAs-detektoren ($1550\text{ nm}$) sitter et langpass-filter ($\lambda_{\text{pass}} > 1300\text{ nm}$, optisk tetthet $\text{OD} > 6$ ved $532\text{ nm}$). Dette eliminerer enhver mulighet for kryss-bølgelengde injeksjon mellom våt og tørr kanal.

---

## Del II: Radiometrisk Effektbudsjett for $\lambda_1 = 532.0\text{ nm}$ i Jerlov Kystvannstype III, Biofouling og Mie-Kavitasjon

### Operasjonelt Sammendrag (Del II)

Det optiske effektbudsjettet for $\lambda_1 = 532.0\text{ nm}$ undervanns laser-vitne ($W_{\text{laser}}$) i **Infranett v0.5** etablerer den eksakte radiometriske grensen mellom en lovlig kausal hendelse ($\mathcal{D}(E_1, E_2)$) og optisk kanalbrudd under reelle skandinaviske kystforhold (**Jerlov kystvannstype III**), marin begroing (**biofouling** på $\text{Al}_2\text{O}_3$-safirvinduer) og kavitasjons-/propellbobler (**Mie-spredning**).

I henhold til den mekaniske spillteorien i SPEC-250 og feil-lukket realiseringsgrammatikk skilles det strengt mellom **fysisk kanalusikkerhet** og **relativistisk/kryptografisk bedrag**:

1. **Radiometrisk Usikkerhet ($P_{\text{RX}} < P_{\text{sens}}$ eller $P_{\text{RX}} > P_{\text{sat}}$):** Forårsaket av kraftig begroing, bobleskyer eller optisk jamming. Utløser **$\text{GATE :: HOLD}$ ($0.00\text{ V DC}$)** uten permanent svartelisting.
2. **Kausalitets- eller Arvebrudd ($ds^2 > 0$ via flerbane-spredning eller $R_{\text{fork}} > 0$):** Utløser umiddelbar **$\text{GATE :: KILL}$ ($0.00\text{ V DC}$)** og påfører angriperen et irreversibelt termodynamisk tap ($\Delta U_{\text{cheat}} < 0$).

$$\Phi_{532\text{nm}}(P_{\text{TX}}) \xrightarrow{L_{\text{Jerlov-III}} + L_{\text{bio}} + L_{\text{Mie}}} P_{\text{RX}} \in [P_{\text{sens}}, P_{\text{sat}}] \xrightarrow{\Pi_K(ds^2 \le 0)} \Omega\text{ (5.00 V)} \xrightarrow{W} \text{AKUERISAAVOQ}$$

---

### 5. Radiometriske Operatorer, Fysiske Rom og Terskelverdier

For en sender-effekt på $P_{\text{TX}} = 100\text{ mW}$ ($+20.00\text{ dBm}$) ved $\lambda = 532.0\text{ nm}$ (fotonenergi $E_{\gamma} = hc/\lambda \approx 3.734 \times 10^{-19}\text{ J}$) og en Silisium lavinefotodiode ($\text{Si-APD}$) med responsivitet $\mathcal{R}_0 \approx 0.38\text{ A/W}$ og lavineforsterkning $M = 50$ ($\mathcal{R}_{\text{eff}} = M \cdot \mathcal{R}_0 = 19.0\text{ A/W}$):

| Parameter / Operator | Matematisk Definisjon | Eksakt Verdi (532 nm) | Port-Konsekvens ($\Pi_K$) |
| :--- | :--- | :--- | :--- |
| **Sendereffekt** ($P_{\text{TX}}$) | $10 \log_{10}(P_{\text{mW}} / 1\text{ mW})$ | $+20.00\text{ dBm}$ ($100.0\text{ mW}$) | Konstant kilde-eksitasjon |
| **Låsterskel (Sensitivitet)** ($P_{\text{sens}}$) | $I_{\text{PD,min}} = 500\text{ nA} \implies P_{\text{sens}} = \frac{I_{\text{min}}}{\mathcal{R}_{\text{eff}}}$ | $-45.80\text{ dBm}$ ($26.32\text{ nW}$) | $P_{\text{RX}} < -45.80\text{ dBm} \implies \text{HOLD}$ |
| **Metningsgrense (Dazzler)** ($P_{\text{sat}}$) | $I_{\text{PD,max}} = 50\text{ }\mu\text{A} \implies P_{\text{sat}} = \frac{I_{\text{max}}}{\mathcal{R}_{\text{eff}}}$ | $-25.80\text{ dBm}$ ($2.632\text{ }\mu\text{W}$) | $P_{\text{RX}} > -25.80\text{ dBm} \implies \text{HOLD}$ |
| **Tilgjengelig Linkbudsjett** ($\Delta L_{\max}$) | $\Delta L_{\max} = P_{\text{TX}} - P_{\text{sens}}$ | $65.80\text{ dB}$ | Absolutt tak for summen av alle tap |
| **Jerlov Type III Demping** ($c_{\text{III}}$) | $c(\lambda) = a(\lambda) + b(\lambda)$ (absorpsjon + spredning) | $c_{\text{III}}(532) = 0.42\text{ m}^{-1}$ | $\alpha_{\text{III}} = 4.343 \cdot c_{\text{III}} = 1.824\text{ dB/m}$ |
| **Mottakbar Spredningsordre** | Kun ballistiske fotoner ($\Delta t \le \Delta t_{\text{budget}}$) | Flerbane-fotoner med $ds^2 > 0$ | Sen-ankomne fotoner forkastes av TDC |

---

### 6. Matematisk Utledning av de 4 Optiske Tapskomponentene

Det totale optiske tapet $L_{\text{tot}}(r)$ mellom K-POD (Node A) og Kainoden (Node B) over avstanden $r \in [0.002\text{ m}, 20.0\text{ m}]$ er gitt i desibel ved:

$$L_{\text{tot}}(r) = L_{\text{opt/Fresnel}} + L_{\text{geom}}(r) + L_{\text{Jerlov-III}}(r) + L_{\text{bio}}(t_{\text{eksponering}}) + L_{\text{Mie}}(\text{VF}_b, r)$$

#### A. Grensesnitt-, Fresnel- og Dikroiske Tap ($L_{\text{opt/Fresnel}}$)

Strålen krysser to syntetiske $\text{Al}_2\text{O}_3$-safirvinduer ($d = 2.0\text{ mm}$, $n_s = 1.772$), to bikube-bølgeledere (honeycomb $\omega < \omega_c$ med åpent arealforhold $\eta_{\text{hc}} \approx 0.82$), og to dikroiske speil ($\text{DM}_{532/1550}$ med $R_{532} = 0.995$):

1. **Innvendig AR-belagt flate (Luft $\leftrightarrow$ Safir, $\times 2$):** Restrefleksjon $R_{\text{AR}} \approx 0.25\% \implies L_{\text{AR}} = 2 \cdot 0.011\text{ dB} = 0.022\text{ dB}$.
2. **Utvendig Våt Flate (Safir $\leftrightarrow$ Sjøvann $n_{\text{sw}} = 1.341$, $\times 2$):**

$$R_{\text{sw}} = \left(\frac{1.772 - 1.341}{1.772 + 1.341}\right)^2 \approx 0.01918 \implies L_{\text{Fresnel}} = 2 \cdot \left(-10\log_{10}(1 - 0.01918)\right) \approx 0.168\text{ dB}$$

3. **Bikube-bølgeleder skyggetap ($\times 2$):** $L_{\text{hc}} = 2 \cdot (-10\log_{10}(0.82)) \approx 1.724\text{ dB}$.
4. **Dikroisk speil og kollimatoroptikk ($\times 2$):** $L_{\text{DM}} \approx 0.286\text{ dB}$.
* **Sum faste optiske systemtap:** $L_{\text{opt/Fresnel}} = 2.20\text{ dB}$.

#### B. Turbiditet i Jerlov Kystvannstype III ($L_{\text{Jerlov-III}}(r)$)

I nordiske fjorder og havnebassenger (Jerlov Type III, høy konsentrasjon av CDOM/gulstoff og fytoplankton) følger den ballistiske (ikke-spredte) intensiteten Beer–Lamberts lov med total attenuasjonskoeffisient $c_{\text{III}} = a_{\text{III}} + b_{\text{III}} = 0.14\text{ m}^{-1} + 0.28\text{ m}^{-1} = 0.42\text{ m}^{-1}$:

$$L_{\text{Jerlov-III}}(r) = -10 \log_{10}\left(e^{-c_{\text{III}} \cdot r}\right) = (10 \cdot \log_{10} e) \cdot c_{\text{III}} \cdot r \approx 4.3429 \cdot 0.42\text{ m}^{-1} \cdot r = 1.824\text{ dB/m} \cdot r$$

* **Ved direkte dokking ($r = 0.002\text{ m}$):** $L_{\text{Jerlov-III}} = 0.0036\text{ dB} \approx 0.00\text{ dB}$.
* **Ved $20.0\text{ m}$ perimetergrense ($r = 20.0\text{ m}$):** $L_{\text{Jerlov-III}} = 1.824 \cdot 20.0 = 36.48\text{ dB}$.

#### C. Maritim Begroing / Biofouling på Safirvinduet ($L_{\text{bio}}$)

Begroing på optiske vinduer i sjøvann skjer i tre distinkte faser, modellert ved flate-dekningsgrad $f_c \in [0, 1]$ (okklusjon fra rur/kalkrørsormer) og biofilm-tykkelse $d_{\text{bio}}$ (bakteriefilm og kiselalger/diatomeer med klorofyll/fukoxantin-absorpsjon $\mu_{\text{bio}}(532) \approx 4.5\text{ mm}^{-1}$):

$$L_{\text{bio}} = N_{\text{vinduer}} \cdot \left[ -10 \log_{10}(1 - f_c) + 4.3429 \cdot \mu_{\text{bio}} \cdot d_{\text{bio}} \right]$$

1. **Nivå 1 — Primær kondisjonerings- og bakteriefilm (0–14 dager, eller aktiv UV-C/visker):** $d_{\text{bio}} \le 0.05\text{ mm}, f_c = 0.02 \implies L_{\text{bio,1}} \approx 2.13\text{ dB}$ (totalt for 2 vinduer).
2. **Nivå 2 — Moderat mikro-begroing / diatomeer (1–3 måneder uten rens):** $d_{\text{bio}} = 0.25\text{ mm}, f_c = 0.20 \implies L_{\text{bio,2}} = 2 \cdot (0.969\text{ dB} + 4.886\text{ dB}) = 11.71\text{ dB}$.
3. **Nivå 3 — Kritisk makro-begroing / rur (*Barnacle Encrustation*):** $d_{\text{bio}} = 0.60\text{ mm}, f_c = 0.85 \implies L_{\text{bio,3}} = 2 \cdot (8.239\text{ dB} + 11.726\text{ dB}) = 39.93\text{ dB}$.

#### D. Luftbobler og Kavitasjon via Mie-Spredning ($L_{\text{Mie}}$)

Når en K-POD manøvrerer med thrustere nær kai eller skrog, genereres luftbobler med radius $a_b \in [50\text{ }\mu\text{m}, 1.5\text{ mm}]$. Fordi størrelsesparameteren $x = \frac{2\pi a_b n_{\text{sw}}}{\lambda} \gg 1$ ($x \in [800, 23\,000]$), befinner spredningen seg i det geometriske Mie-regimet der ekstinksjonseffektiviteten konvergerer mot $Q_{\text{ext}} \approx 2.0$ (ekstinksjonsparadokset).

For en boble-volumfraksjon $\text{VF}_b = \frac{4}{3}\pi a_b^3 N_b$ (hvor $N_b$ er antall bobler per $\text{m}^3$), er boblenes attenuasjonskoeffisient $\gamma_b$:

$$\gamma_b = N_b \cdot Q_{\text{ext}} \cdot \pi a_b^2 = \frac{3 \cdot \text{VF}_b}{2 \cdot a_b} \implies L_{\text{Mie}}(r) = 4.3429 \cdot \left(\frac{3 \cdot \text{VF}_b}{2 \cdot a_b}\right) \cdot r$$

* **Lett boblesky ($\text{VF}_b = 10^{-5}$, $a_b = 0.5\text{ mm}$):** $\gamma_b = 0.030\text{ m}^{-1} \implies 0.13\text{ dB/m}$ ($2.60\text{ dB}$ over $20\text{ m}$).
* **Tett propell-kavitasjon i dokkingspalte ($\text{VF}_b = 5 \times 10^{-3}$, $a_b = 0.25\text{ mm}$, $r = 0.10\text{ m}$):** $\gamma_b = 30.0\text{ m}^{-1} \implies 130.3\text{ dB/m}$, som over en $0.10\text{ m}$ spalte gir $L_{\text{Mie}} = 13.03\text{ dB}$.
* **Tett propell-kavitasjon over $20.0\text{ m}$ ($\text{VF}_b = 10^{-3}$, $a_b = 0.25\text{ mm}$):** $\gamma_b = 6.0\text{ m}^{-1} \implies 26.06\text{ dB/m}$, som over $20.0\text{ m}$ gir $L_{\text{Mie}} = 521.2\text{ dB}$ (total optisk blokkering).

---

### 7. Eksakt Effektbudsjett-Matrise (dBm) på Tvers av Operasjonelle Regimer

I tabellen under er $P_{\text{TX}} = +20.00\text{ dBm}$, låsterskelen $P_{\text{sens}} = -45.80\text{ dBm}$, og metningsgrensen $P_{\text{sat}} = -25.80\text{ dBm}$ (aktivert med passiv optisk attenuator $\text{VOA}_{\text{dock}} = 30.0\text{ dB}$ ved kontakt-dokking for å hindre at Si-APD-en mettes på $2\text{ mm}$ avstand):

| Parameter / Ledd | Regime 1: Fysisk Safir-Dokking ($r = 0.002\text{ m}$, Moderat Bio + Kavitasjon) | Regime 2: Sub-Overflate Nærsone ($r = 10.0\text{ m}$, Jerlov III + Bio 2 + Bobler) | Regime 3: $20.0\text{ m}$ Perimetergrense ($r = 20.0\text{ m}$, Jerlov III + Bio 1) | Regime 4: Kritisk Svikt ($r = 20.0\text{ m}$, Jerlov III + Bio 2 + Kavitasjon) |
| :--- | :--- | :--- | :--- | :--- |
| **Sendereffekt ($P_{\text{TX}}$)** | $+20.00\text{ dBm}$ | $+20.00\text{ dBm}$ | $+20.00\text{ dBm}$ | $+20.00\text{ dBm}$ |
| **Nær-sone VOA-demping** | $-30.00\text{ dB}$ | $0.00\text{ dB}$ | $0.00\text{ dB}$ | $0.00\text{ dB}$ |
| **Faste Optiske Tap ($L_{\text{opt}}$)** | $-2.20\text{ dB}$ | $-2.20\text{ dB}$ | $-2.20\text{ dB}$ | $-2.20\text{ dB}$ |
| **Geometrisk Divergens ($L_{\text{geom}}$)** | $0.00\text{ dB}$ | $-12.40\text{ dB}$ | $-18.42\text{ dB}$ | $-18.42\text{ dB}$ |
| **Jerlov Type III ($1.824\text{ dB/m}$)** | $0.00\text{ dB}$ | $-18.24\text{ dB}$ | $-36.48\text{ dB}$ | $-36.48\text{ dB}$ |
| **Biofouling-tap ($L_{\text{bio}}$)** | $-11.71\text{ dB}$ (Nivå 2) | $-11.71\text{ dB}$ (Nivå 2) | $-2.13\text{ dB}$ (Nivå 1) | $-11.71\text{ dB}$ (Nivå 2) |
| **Luftbobler / Mie ($L_{\text{Mie}}$)** | $-1.30\text{ dB}$ ($2\text{ mm}$ kav.) | $-1.30\text{ dB}$ (Lett sky) | $-2.60\text{ dB}$ (Lett sky) | $-52.12\text{ dB}$ (Thruster-sky) |
| **Totalt Kanaltap ($L_{\text{tot}}$)** | **$-45.21\text{ dB}$** | **$-45.85\text{ dB}$** | **$-61.83\text{ dB}$** | **$-120.93\text{ dB}$** |
| **Mottatt Effekt ($P_{\text{RX}}$)** | **$-28.00\text{ dBm}$** *(VOA-regulert)* | **$-25.85\text{ dBm}$** | **$-41.83\text{ dBm}$** | **$-100.93\text{ dBm}$** |
| **Linkmargin ($P_{\text{RX}} - P_{\text{sens}}$)** | **$+17.80\text{ dB}$** | **$+19.95\text{ dB}$** | **$+3.97\text{ dB}$** | **$-55.13\text{ dB}$ (UNDERSKUDD)** |
| **Portvaktens Dom ($\Pi_K$)** | **`GATE :: OPEN` ($5.00\text{ V}$)** | **`GATE :: OPEN` ($5.00\text{ V}$)** | **`GATE :: OPEN` ($5.00\text{ V}$)** | **`GATE :: HOLD` ($0.00\text{ V}$)** |

---

### 8. Kausal-Radiometrisk Beslutningstre (Mekanisk Spillteori & ToF)

```text
[INNKOMMENDE 532 nm PULS PÅ SAFIRVINDU]
  │
  ├─► 1. RADIOMETRISK VINDUSKONTROLL (P_RX)
  │     ├─ P_RX < -45.80 dBm (Jerlov III + Biofouling + Kavitasjon > 65.8 dB)
  │     │    └──► [GATE :: HOLD (0.00 V DC)] -> Krev fysisk kontakt-dokking (r -> 2 mm)
  │     │
  │     ├─ P_RX > -25.80 dBm (Fiendtlig Dazzler eller udempet høyeffekt-laser)
  │     │    └──► [GATE :: HOLD (0.00 V DC)] -> APD-metningsvern aktivert
  │     │
  │     └─ P_RX ∈ [-45.80 dBm, -25.80 dBm] (Gyldig fotonstrøm: 500 nA .. 50 μA)
  │          │
  ▼          ▼
  ├─► 2. KAUSAL DIAMANT D(E1, E2) & MIE-SPREDNINGSFILTER
  │     │  (Kan en angriper på r = 100 m bruke en 10 kW laser for å slå gjennom Jerlov III?)
  │     │  • På r = 100 m er L_Jerlov = 182.4 dB, men selv om fotonene når frem:
  │     │  • Δt_fysisk(100 m i sjøvann) = (2 * 100 m) / (2.2356e8 m/s) = 894.61 ns
  │     │  • 894.61 ns > 178.92 ns (ds² > 0: Romlignende intervall!)
  │     │
  │     ├─ Δt_RT > Δt_budget (Flerbane Mie-hale eller fjern-laser)
  │     │    └──► [GATE :: KILL (0.00 V DC)] -> ΔU_cheat = -W_laser_kW - W_crypto < 0
  │     │
  │     └─ Δt_RT <= Δt_budget ∧ R_fork == 0 ∧ C_in >= C_hw
  │          └──► [GATE :: OPEN (5.00 V DC)] -> WAL fsync -> AKUERISAAVOQ
```

> **Spillteoretisk bevis mot «High-Power Laser Spoofing» i grumsete vann:** I et konvensjonelt optisk system som måler mottatt effekt ($P_{\text{RX}}$), kunne en angriper på $r = 100\text{ m}$ kompensert for Jerlov III-dempingen ved å øke sendereffekten $P_{\text{TX}}$. I Infranett v0.5 er effekten $P_{\text{RX}}$ kun en *nødvendig* betingelse for deteksjon, aldri en *tilstrekkelig* betingelse for autorisasjon. Jo mer effekt angriperen pumper inn i sjøvannet fra utsiden av $20\text{ m}$-sonen, desto større blir det termodynamiske tapet $W_{\text{kinetic/optical}}$, mens porten urokkelig avviser pakken ved $\Delta t_{\text{roundtrip}} > 178.92\text{ ns}$ (`GATE :: KILL`).

---

### 9. Referanseimplementasjon i Rust (`spec250_gate.rs`)

Se [`engines/spec250_gate.rs`](../engines/spec250_gate.rs) for den kjørbare, heltallsbaserte `#![forbid(unsafe_code)]`-implementasjonen av både `DualLambdaSapphirePort::process_wet_to_dry_bridge` og `evaluate_subsea_532nm_link` (verifisert med `rustc --test`).
