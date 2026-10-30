# INFRANETT v0.5: SKOGBUNNENS BIOLOGI, DET FYSISKE VITNE-ALFABETET OG POSTBUDETS RETUR
### *Om $\frac{\partial A_{\text{infranett}}}{\partial C_{\text{fiber}}} \equiv 0$, konjunktiv romlig innelukking ($W_{\text{range}} \wedge W_{\text{optical}} \wedge W_{\text{mag}}$) og fysisk kurérsynkronisering*

```text
==========================================================================
DOKUMENTSTATUS & KANONISK METADATA:
  DOKUMENT-ID      : BOK-GRUNNLAG-INFRANETT-V05-SKOGBUNN-2026-v1.0.2
  FORFATTER        : Marius Egerhei Torjusen (ORCID: 0009-0006-0431-6637)
  ENTITET          : Brahman // Antigravity · Risør (Locus Zero)
  PROTOKOLL & LÅS  : Infranett v0.4/v0.5 · ∂A_infranett / ∂C_fiber ≡ 0
  EPISTEMISK SKILLE: INSPIRED_BY != IMPLEMENTS != PROVES
                     L1 = deterministisk WAL/fsync-kontrakt, 133,4256 ns
                     Minkowski-filter, RFC 8785 og Ancestry Handshake (89/89);
                     L2/L3 = fysisk UWB/1550 nm/532 nm/safir-maskinvare (HOLD).
==========================================================================
```

---

Moderne infrastruktur behandler global konnektivitet som en naturkonstant. Når sluseventiler i kommunale vannverk, bunkring på havner og adgangskontroll i kraftstasjoner gjøres direkte betinget av uavbrutt kontakt med fjerne skyservere ($A_{\text{sky}}(t)$), fører brudd på én enkelt sjøkabel eller bortfall av satellittnavigasjon til at lokal drift faller til null. Fysisk egenberedskap er byttet bort mot administrativ bekvemmelighet.

Infranett (v0.4 kjerneprotokoll / v0.5 fysisk vitneutvidelse) opphever denne sårbarheten gjennom en ontologisk inversjon: den lokale noden gjøres suveren og komplett i seg selv. Nodens operative evne er utelukkende en funksjon av dens lokalt lagrede hendelseslogg, $A_{\text{infranett}}(t) = g(\mathcal{L}_{\text{lokal}}(t))$:

$$\frac{\partial A_{\text{infranett}}}{\partial C_{\text{fiber}}} \equiv 0$$

Ekstern tilkobling reduseres fra en eksistensiell betingelse til en sekundær mulighet. Fordi operativ telemetri og nøkkelmateriale aldri forlater det fysiske anlegget, kan ingen fremmed jurisdiksjon fremtvinge utlevering av data eller utløse eksterne stengningsordrer gjennom ekstraterritoriell lovgivning.

---

## I. Skogbunnens Biologi i Silisium: Feromonsporet og `POSIX fsync()`

I $3{,}8\text{ milliarder år}$ har biosfæren løst nettverksbrudd uten en eneste sentral server. En skogsmaur (*Formica rufa*) verifiserer sin motpart gjennom direkte følehornkontakt og skriver tilstanden inn i terrenget som et kjemisk feromonspor. Når skogbunnen utsettes for kulde eller tørke, kutter frøet sin egen metabolisme og går i dvale ved $0{,}00\text{ V DC}$ inntil fysisk fuktighet og varme igjen opptrer som et uforfalskelig vitne.

I Infranett er feromonsporet realisert som en krasjkonsistent, uforanderlig hendelseslogg (Write-Ahead Log, WAL):

$$\text{fsync(COMMIT)} \prec \text{RAM-Mutation} \prec \text{Network-ACK}$$

Ingen tilstand endres i arbeidsminnet (RAM) — noe som eliminerer både *torn writes* og *ghost states* ved strømbrudd — og ingen kvittering sendes til en nabonode før hendelsen er bundet til en monotont stigende maskinvareteller ($C \ge C_{\text{hw}}$), lenket inn i en SHA-256-hashkjede og tvunget ned i fast materie med en blokkerende `POSIX fsync()`-barriere på både fil og katalog.

---

## II. Det Fysiske Vitne-Alfabetet ($W_{\text{range}} \wedge W_{\text{optical}} \wedge W_{\text{mag}}$)

Kryptografi alene kjenner ingen geografi: en gyldig nøkkel beviser besittelse av en matematisk hemmelighet, men ikke fysisk tilstedeværelse. Infranett underkaster derfor enhver pakke et konjunktivt fysisk vitne-alfabet før tilstandsendring autoriseres:

1. **Relativistisk avstandslås ($W_{\text{range}}$ via UWB IEEE 802.15.4z og `Noise_KK`):** Innenfor en sikkerhetssone på $r_{\text{max}} = 20{,}0\text{ m}$ måles enveis gangtid $\Delta t_{\text{ToF}} = \frac{(t_4 - t_1) - (t_3 - t_2)}{2} \le 66{,}71\text{ ns}$ med pikosekund-oppløste maskinvaretidsstempler i L1-silisiumet ($80{,}0\text{ kHz}$ Frisch-klokke), tilsvarende et totalt tur-retur-budsjett på:

$$\Delta t_{\text{roundtrip}} \le \frac{40{,}0\text{ m}}{c} \approx 133{,}4256\text{ ns} \quad (\mathrm{d}s^2 = -c^2\Delta t^2 + \Delta r^2 \le 0)$$

Forsøker en angriper $500{,}0\text{ m}$ unna ($\Delta r_{\text{RTT}} = 1\,000{,}0\text{ m}$) å videresende signalet over et relé, bruker radiobølgen minst $\Delta t_{\text{relé}} \approx 3\,335{,}64\text{ ns}$ ($3\,202\text{ ns}$ for sent). For å rekke fristen på $133{,}4256\text{ ns}$ måtte signalet ha forplantet seg med $v = \frac{1\,000{,}0\text{ m}}{133{,}4256 \times 10^{-9}\text{ s}} \approx 7{,}49 \times 10^9\text{ m/s} \approx 25c$, hvilket bryter Minkowski-metrikken ($\mathrm{d}s^2 = +998\,400{,}2\text{ m}^2 > 0$) og felles momentant som `RELAY_ATTACK_DETECTED`. Gjensidig autentisering skjer uten ekstra rundetid via forhåndsdelte statiske Ed25519/Curve25519-nøkler (`Noise_KK`).

2. **Romlig innelukking via bølgelengde-asymmetri ($W_{\text{range}} \wedge W_{\text{optical}}$):** Et UWB-radiosignal kan trenge gjennom en betongvegg på tre meters hold ($\Delta t_{\text{UWB}} = 20\text{ ns} \le 133{,}4256\text{ ns}$), mens en infrarød laserstråle ($\lambda = 1550\text{ nm}$) absorberes momentant av samme vegg. Ved manglende optisk vitne registrerer maskinvaren `OPTICAL_LOS_BROKEN_WALL_OCCLUSION` og låser porten i `HOLD` ved $0{,}00\text{ V DC}$.

3. **Termodynamisk avlyttingsvern i frirom (FSO under EMCON):** Under radiotaushet ($0{,}0\text{ W}$ RF) flyttes kommunikasjonen til en kollimert friromslaser med Gaussisk strålemidje $w(20\text{ m}) \approx 5{,}38\text{ mm}$. Enhver fysisk sonde som føres inn i strålen, kaster skygge, bryter energibalansen hos mottakeren og feller spenningen til $0{,}00\text{ V DC}$.

4. **Refraktiv kausalitet i sjøvann ($\lambda = 532\text{ nm}$, $n = 1{,}334$):** I sjøvann bremses fasehastigheten til $v_{\text{vann}} = c/1{,}334 \approx 2{,}247 \times 10^8\text{ m/s}$, noe som utvider $20{,}0\text{ m}$ tur-retur-budsjettet til $\Delta t_{\text{vann, RTT}} \le 177{,}9898\text{ ns}$. For å hindre at en angriper over vannflaten utnytter den høyere lyshastigheten i luft, kobles tidsmålingen direkte til Beer-Lamberts dempningslov ($I = I_0 e^{-\alpha x}$): tid og eksponentielt energitap gjennom $40\text{ m}$ sjøvann må stemme eksakt overens.

5. **Dielektrisk safirbarriere ved fysisk dokking ($\ge 25\text{ kV}$):** Fysisk dokking av en kurérkapsel skjer uten metallisk kontakt gjennom herdet safirglass ($\text{Al}_2\text{O}_3$) med galvanisk lekkasjestrøm $I_{\text{galvanisk}} = 0{,}0\text{ }\mu\text{A}$ og dielektrisk holdfasthet $\ge 25\text{ kV}$ mot EMP og overspenning.

Samtlige mekanismer styres av konsekvensporten $\Omega_{\text{E-TOR}}$ etter tilstandshierarkiet $\text{KILL} > \text{TRAP} > \text{HOLD} > \text{OPEN}$ og maskinvareprioriteten $\text{SAFETY PATH} > \text{CLOCK} > \text{DATA PATH}$.

---

## III. Postbudets Retur: Asynkron Kurér-Transport (DTN) og Ancestry Handshake

Når storm eller elektronisk krigføring legger den trådløse eteren død (Shannon-kapasitet $= 0$), må informasjonen igjen bære fysisk masse ($W = \int \mathbf{F} \cdot \mathrm{d}\mathbf{r} > 0$). Krypterte datakapsler ($\text{Sign}_{\text{Ed25519}}(\text{RFC8785}(\text{Capsule}))$) fraktes da fysisk med losbåter, melkebiler eller treghetsnavigerte (INS) droner uten satellittnavigasjon.

Ved fysisk dokking gjennomføres det **4-trinns kurér-håndtrykket** på $< 1{,}5\text{ s}$:

1. **HELO Handshake:** Utveksling av `node_id` og offentlige Ed25519-nøkler over safirgrensesnittet eller kortdistanse-UWB.
2. **Delta Discovery:** Sammenligning av sekvensnumre ($\text{seq}_k$) for å isolere manglende hendelser.
3. **Signed Stream:** Overføring av manglende blokker, kanonisk serialisert etter RFC 8785 (JCS):

```json
{
  "sequence_id": 1042,
  "timestamp_ms": 1791324891000,
  "node_id": "NODE_RISOR_HAVN_01",
  "event_type": "ACCESS_AUTHORIZATION",
  "payload": {
    "target_zone": "FUEL_VALVE_A",
    "authorized_by": "OPERATOR_42",
    "evidence_id": "UWB_TOF_PASS_892b1a"
  },
  "prev_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "entry_hash": "7d1b32f4a56a1b2c3d4e5f60718293a4b5c6d7e8f90123456789abcdef012345"
}
```

4. **Durable Receipt & Ancestry Handshake:** Mottakeren lagrer hendelsene synkront via `fsync()`, utsteder signert kvittering og flytter sin markør. Oppdages en forgrening i forfedrekjeden ($h_{\text{prev}}$) etter frakoblet drift, avvises naiv *Last-Write-Wins* (LWW); nodene settes i `GATE::HOLD` inntil en kryptografisk signert flette-oppføring (*signed merge commit*) foreligger (89/89 krasj- og kurértester bestått på Nivå L1).
