# GOOGLE NOTEBOOKLM — «LAG RAPPORT»-STYRINGSINSTRUKSER
### *Skreddersydde systemprompter for «Konseptuell granitt — Et forsøk på sannhet (Til meg selv)»*

**Kilde som lastes opp i NotebookLM:**
* [`KONSEPTUELL_GRANITT_ET_FORSOK_PA_SANNHET.pdf`](/home/sololyset/07_BOKHYLLA_MONOGRAFIER_OG_BOKVERK/07_TIL_MEG_SELV_KONSEPTUELL_GRANITT/KONSEPTUELL_GRANITT_ET_FORSOK_PA_SANNHET.pdf) (`102 sider`, SHA-256: `16a24bdf7cd5432731276447cadba63a8ab1cb2f30be4119233b25ea34050fac`)
* Eventuelt også [`MASTER_MANUSKRIPT_SAMLET.md`](/home/sololyset/07_BOKHYLLA_MONOGRAFIER_OG_BOKVERK/07_TIL_MEG_SELV_KONSEPTUELL_GRANITT/MASTER_MANUSKRIPT_SAMLET.md) for rå LaTeX-likninger og tabeller.

---

## 1. Hovedprompt for «Lag din egen rapport» (Teknisk & Konstitusjonell Synteserapport)

> *Lim inn denne direkte i feltet **«Lag rapport» $\to$ «Lag din egen» (Create your own)** i Google NotebookLM:*

```text
Skriv en uttømmende, knivskarp fag- og arkitekturrapport på norsk basert på monografien «Konseptuell granitt — Et forsøk på sannhet (Til meg selv)».

STRENGE STIL- OG METODEKRAV:
1. Subtraktiv sakprosa: Unngå blomstrende adjektiver, klisjeer og svevende metaforer. Skriv i en kald, presis og uforhandlingsbar ingeniør- og rettsfilosofisk tone («Kutt ordene inntil bare fjellet står igjen»).
2. Epistemisk disiplin: Bevar skillet INSPIRED_BY != IMPLEMENTS != PROVES og nivåinndelingen L0 (fysiske naturlover), L1 (lokalt verifisert programvare, 7/7 L1_LAW-monolitter med 42/42 PASS, ΔR = 0), og L2/L3 (prospektive maskinvare- og reaktorspesifikasjoner fastholdt i disiplinert HOLD).
3. Eksakte tall og likninger: Gjengi de eksakte terskelverdiene fra kilden uten avrunding eller omskrivning.

STRUKTUR FOR RAPPORTEN:
I. EKSEKUTIV SYNTESE: ABSTRAKSJON BÆRER INGEN VEKT
- Forklar bruddet mellom masseløse kandidathypoteser i silisiumet (Φ) og irreversibel fysisk konsekvens i terrenget (Ω).
- Definer realiseringsgrammatikken R = (Φ, Π_K, Ω, W) og den idempotente projektoren Π_K^2 = Π_K.

II. KAUSAL ORDEN, VITNEDELING OG BELNAP–DUNN-DISSENS
- Gjennomgå den kausale rekkefølgen Durable(I_n) < Execute_n < Durable(R_n) < ACK_n, to-trinns vitnedeling (W_pre^2 vs. R_n), håndtering av IN_DOUBT-krasjvinduet (RECOVERY_HOLD) og bilateralt vitneanker (W_T^bilat).
- Forklar hvorfor sensor- eller modellkonflikt B = (1,1) i Belnap–Dunn 4-verdi-logikk tvinger frem HOLD, og hvorfor d/dt(HOLD) = 0 (tid alene kan aldri oppheve en sperre).

III. HARDWARE-HERDING OG DET MEKANISKE LUFTGAPET (0,00 V DC vs. 5,00 V DC)
- Skillet mellom elektronisk ventetilstand (CAUSAL_HOLD ved 8,0 µJ i TDC) og galvanisk nødfrakobling (GATE :: KILL innen <15 ns med >= 5,0 mm fysisk luftgap og herdede returfjærer).
- Hvordan arkitekturen motstår innsidetrusler (utløserfri/trip-free lås, kalibrert mekanisk skjærsplint F_shear = 1 200 N og 2-av-2 nøkkelvitne W_h = W_h,1 ∧ W_h,2) samt fjær-/ventilsvikt (1-av-2 diversitær serieredundans med eFuse/pyro-sikring).

IV. DE FEM KJERNEPRØVENE FRA GRUNNFJELLET (NAKNE TERSKLER)
Analyser hver av de fem kjerneprøvene med full teknisk presisjon:
1. Kjerneprøve I (Avstanden mellom 0 og 1): 8-trinns intervallgrammatikk, 257:1-loven (ΔQ = 1,5259e-5), Oleiniks entropibetingelse E, Stefan-betingelsen (L_latent > 0), Fichera–Oleinik-randdrift, QLP/KY-Enigma og Alexandrov-lyskjeglen (133,4256 ns over 20 m).
2. Kjerneprøve II (Safiren på 500 m dyp): 50,47 bar overtrykk (898 900 N), monokrystallinsk Al2O3 (E_g = 8,8 eV, 86,4 % transmisjon ved 275 nm UV-C), Ti-6Al-4V-bikubegitter (σ_max,cell = 0,946 MPa, SF = 422,8, a_crit = 511 µm, Δτ_RT = -0,27 fs) og 42 kHz PZT-4-kavitasjon (180 kPa > 168 kPa) med 2500 ms avluftskarantene (HoldBubbleDegassingWait).
3. Kjerneprøve III (Termisk konduktans og Matrioshka-kapsling): Hvorfor eksternt LN2-dampskjold forkastes (36,0 kW/m^2 varmefluks, P = 51,42 bar > P_c = 33,96 bar, og 700–800 bar isokor trykkeksplosjon ved strømbrudd), og hvordan den tørre 4-lags vakuum-Matrioshkaen holder kjernen ved T_0 <= 4,12 K (<15 mW lekkasje).
4. Kjerneprøve IV (Prisen på et sannferdig blunk): Landauer-grensen ved +4,0 °C (2,6523e-21 J), TDC-forkastelse ved 8,0 µJ mot 10 000 J reléangrep på 500 m dyp (termodynamisk utmattelsesforhold η_defense = 1,25e9) og W_forge >= 9,025e17 J.
5. Kjerneprøve V (Orgelet i grunnfjellet): T-POD underkritisk nøytronikk (k_eff = 0,960 -> <0,50 ved passiv fryseplugg-drenering etter Fermis aldersligning og geometrisk buckling B_g^2), Protaktinium-233s 26,97-døgns tidslås, Ludwig–Soret-separasjon (73 130x), K-POD ved 0,998 V DC gjennom 2,7 Å krone-eter-kavitet, eksakt rasjonal massebalanse (ΔR = 0,000000000000 kg over 141,100998 kg) og POD-Mycelin (50,0 W ± 0,5 W) med Ghost Payoff Interlock (12,5 µs).

V. KONKLUSJON: LEVEL 01 OG DEN MENNESKELIGE ARBEIDSPLIKTEN
- Oppsummer hvorfor maskinen har fullmakt til å kutte strømmen, men aldri autoritet til å tilgi seg selv.
```

---

## 2. Prompt for «Kritisk Revisjons- og Stressrapport» (Red-Team / Sikkerhetsrevisjon)

> *Brukes i **«Lag rapport» $\to$ «Lag din egen»** når du vil at NotebookLM skal revidere boken som en streng sikkerhets- og systemrevisor (IEC 61508 SIL-4 / DO-178C):*

```text
Opptre som en uavhengig sikkerhetsrevisor (IEC 61508 SIL-4) og teoretisk fysiker. Lag en teknisk revisjonsrapport av «Konseptuell granitt — Et forsøk på sannhet» som kartlegger:
1. Alle matematiske og fysiske invarianter på Nivå L0 som brukes som forkastelseskriterier i skranken Π_K.
2. Alle programvaremekanismer som er deterministisk verifisert på Nivå L1 (inkludert de 7 L1_LAW-monolittene, 257:1-kvantisering, QLP, KY-Enigma og eksakt rasjonal brøkregning ΔR = 0).
3. Alle prospektive maskinvare- og prosesskomponenter på Nivå L2/L3 som forfatterne eksplisitt holder i disiplinert HOLD inntil fysisk trykkammer- og feltkvalifisering foreligger.
4. En verifikasjonsmatrise (Tabell) som viser feilmodus, deteksjonsmekanisme, reaksjonstid (15 ps TDC, 15 ns crowbar, 12,5 µs Ghost Payoff, 2500 ms kavitasjonskarantene, 26,97 døgn 233Pa-sluse) og fysisk slutt-tilstand.
Hold språket fritt for adjektiver og metaforer.
```

---

## 3. Styringsinstruks for «Audio Overview / Deep Dive» (Tilpass lydoversikt)

> *Lim inn i **«Tilpass» (Customize)** under Audio Overview i NotebookLM:*

```text
Fokuser samtalen på de harde fysiske tallene og mekanismene i boken, ikke på løs filosofi. Forklar konkret:
1. Hvorfor en datamaskin ikke kan lukke et fysisk luftgap på 5 millimeter når spenningen er 0,00 V DC, og hvorfor en mekanisk skjærsplint på 1 200 Newton knuser hvis noen prøver å tvinge spaken mens magnetlåsen holder igjen.
2. De fem kjerneprøvene fra grunnfjellet med eksakte tall: 133,4256 nanosekunder i lyskjeglen, 898 900 Newton (nesten 90 tonn) på safirvinduet i Norskerenna med titan-bikube (sikkerhetsfaktor 422,8), hvorfor flytende nitrogen i et lukket kammer gir 700–800 bar eksplosjonstrykk ved strømbrudd, hvordan 8 mikrojoule i tidsmåleren slår ut et angrep på 10 000 joule (1,25 milliarder til 1), og hvordan OrgelKraft-kaskaden krever eksakt null i restmasse (ΔR = 0 kg) og bruker Protaktinium-233 (26,97 døgn) og 2,7 Ångstrøm krone-eter ved 0,998 volt.
3. Vær tydelig på bokens egen ærlighetskontrakt: forskjellen på L0 (fysikk), L1 (kjørende programvare) og L2/L3 (maskinvare- og reaktordesign i HOLD).
```
