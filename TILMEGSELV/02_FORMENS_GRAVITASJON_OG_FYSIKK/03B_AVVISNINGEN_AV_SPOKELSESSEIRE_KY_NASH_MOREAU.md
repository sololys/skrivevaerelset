# AVVISNINGEN AV SPØKELSESSEIRE: KY-NASH, MOREAU-FEIEPROSESSEN OG DET KRYOGENE PLASTRONET
### *Om «Ghost Wins» ($U_i = -\infty$), Nagumos tangentkjegle ($\dot{x}_t \in T_K(x_t)$), Skorokhod-refleksjon og stabilitetsmarginen $M_{\text{stab}}$*

---

En algoritme kjenner ingen smerte når et stålskrog revner. Klassisk reguleringsteori og spillteori hviler på en skjør forutsetning: at tilstander forplanter seg fritt gjennom et friksjonsløst matematisk landskap, der agenter maksimerer sin nyttefunksjon uten fysisk motstand.

I sikkerhetskritiske cyber-fysiske systemer fører denne antakelsen til katastrofe. Når programvare optimaliserer fritt i det ikke-deterministiske mulighetsrommet ($\mathcal{NP}$-rommet), oppstår det vi kaller *spøkelsesseire* («Ghost Wins»). Dette er fiktive strategivektorer som fremstår matematisk optimale i koden, men som bryter termodynamiske, strukturelle eller fysiske grenser i den materielle verden ($\mathcal{P}$-rommet).

En autonom agent som jakter maksimal uttelling ($\max U_i$), utnytter blinde flekker i modellen og genererer styringsbaner som ødelegger selve maskinvaren den er satt til å betjene. For å eliminere denne sårbarheten må friksjonsløs nyttemaksimering erstattes med projeksjonsstyrte levedyktighetsgrenser (*Viability Boundaries*). Ingen tilstandsendring får utføres før kandidatbanen er bevist fremover-invariant innenfor en tillatt fysisk mangfoldighet.

---

## 1. Avvisningen av Spøkelsesseire: Moreau-Feieprosessen

Konflikten mellom lokal nytteoptimalisering og fysisk overlevelse avgjøres ved grensen til det tillatte rommet $K \subset \mathbb{R}^n$. Under klassisk Nash-logikk beregner en agent gradienter over nyttefunksjonen $U_i(x_i, x_{-i})$ uten hensyn til om den resulterende banen forlater det lukkede domenet $K$.

I rammeverket for *KY-Nash* tvinges enhver strategikandidat gjennom en ufravikelig operatorkjede før den når en fysisk aktuator:

$$\text{Kandidatforslag } (\Phi) \longrightarrow \text{Projeksjon } (\Pi_K) \longrightarrow \text{Realisering } (\Omega)$$

Gjennom Moreaus feieprosess ($\Pi_K$) låses systemtilstanden til det kompakte domenet $K$. Langs randen $\partial K$ styres utviklingen av Nagumos tangentkjeglebetingelse, som krever at hastighetsvektoren $\dot{x}_t$ til enhver tid peker innover i eller langs tangentkjeglen $T_K(x_t)$:

$$\dot{x}_t \in T_K(x_t), \quad \forall x_t \in \partial K$$

For å opprettholde denne invariansen under stokastiske forstyrrelser fra omgivelsene, underlegges randdynamikken Skorokhods reflekterende differensialligning:

$$dx_t = -\gamma \nabla H_{\text{int}}(x_t)dt + \sqrt{2D}\,dW_t - n(x_t)dL_t$$

Her representerer $H_{\text{int}}(x_t)$ systemets indre Hamilton-funksjon, $dW_t$ er en Wiener-prosess med diffusjonskonstant $D$, $n(x_t)$ er den utadpekende enhetsnormalvektoren til $K$, og $L_t$ er en ikke-avtagende lokal tidsprosess som utelukkende trer i kraft når tilstanden berører randen $x_t \in \partial K$.

Dersom en kandidatstrategi fra programvaren ($\Phi$) forsøker å krysse randen av $K$, utløser Moreau-operatoren en uendelig straffeskaleringsfaktor ($C_K \to \infty$). I evalueringsrommet kollapser kandidatens nytteverdi momentant:

$$U_i = -\infty$$

Dette sammenbruddet fanges opp av *Den Ikke-Løgnende Kjernen* (`NLK`) og portvokteren $\Omega$ før signalet rekker å forplikte maskinvaren. Portvokteren feller styrespenningen direkte til en deterministisk, feilsikker stasis ved $0{,}00\text{ V DC}$. En destruktiv handling kan ikke utføres, fordi det matematiske rommet som beskriver handlingen er geometrisk skåret bort fra kontrollsløyfen før aktuatoren mottar energi.

| Parameter | Klassisk Nash-logikk | KY-Nash Moreau-håndhevelse |
| --- | --- | --- |
| **Optimalitetskriterium** | Friksjonsløs maksimering ($\max U_i$) | Levedyktig admissibilitet ($\text{Fix}(\Pi_K \circ \Phi) \subset \text{Viab}$) |
| **Randbrudd** | Myk straff eller tilbakemelding i etterkant | Uendelig straff ($C_K \to \infty$) via Nagumo ($\dot{x} \in T_K(x)$) |
| **Nytterealisering** | Ubegrenset i $\mathcal{NP}$-rommet | Momentan kollaps til $U_i = -\infty$ i $\Phi$ |
| **Maskinvaretilstand** | *Fail-Open* ($5{,}00\text{ V DC}$ som standard) | *Fail-Closed* ($0{,}00\text{ V DC}$ kortslutning / lås) |
| **Epistemisk status** | Ubekreftet kandidatforslag ($\Phi$) | Verifisert realisering ($\Omega \circ \Pi_K \circ \Phi$) |

---

## 2. Grensetilfellet for Aktiv Skjerming (`LEIDENFROST`-Modellen) og Overgangen til Passiv Matrioshka-Isolasjon (`SPEC-250`)

I arktiske farvann og dypvannskorridorer på $500\text{ meters}$ dyp ($50\text{ bar}$ i Skagerrak, jf. `SPEC-250`) utsettes undervannsnoder og skrog for kraftige termiske gradienter og hydrostatisk trykk. Som et teoretisk og simulert grensetilfelle ($\text{L0}/\text{L1}$) undersøker *LEIDENFROST*-modellen hva som skjer dersom man forsøker å opprettholde en aktiv kryogen gasshinne – et damp-plastron av flytende ammoniakk ($\text{NH}_3$ ved $-33{,}34\,^\circ\text{C}$) – på utsiden av et skrog i filmkokingsregimet. Teoretisk gir en slik dampfase et hydrodynamisk friksjonskutt (reduksjon av viskøse skjærkrefter med opptil $800\times$) og en brå akustisk impedansendring over gass–væske-grensen.

Nettopp dette grensetilfellet demonstrerer imidlertid hvorfor en åpen, aktiv fasegrense hviler på en termodynamisk knivsegg. Dersom den lokale varmefluksen faller under Leidenfrost-punktet, bryter filmkokingen sammen til overgangskoking, gasshinnen kollapser under Taylor-ustabilitet, og skroget utsettes for ødeleggende kavitasjonssjokk ($< 45{,}0\text{ ms}$). I kontrollrammeverket KORA overvåkes derfor stabilitetsmarginen $M_{\text{stab}}$ kontinuerlig:

$$M_{\text{stab}} = \frac{\delta - \delta_{\text{crit}}}{\delta}$$

Her er $\delta$ tykkelsen på grensesjiktet, mens $\delta_{\text{crit}}$ markerer den kritiske grensen for kollaps. Overvåkningen utføres gjennom to adskilte tidsvinduer: i **FPGA- og programvarevinduet** evaluerer en prosesseringssyklus på $4{,}0\text{ ns}$ ($500\text{ MHz}$) kontrollbarrierefunksjoner (CBF) og termodynamisk stabilitet, mens **silisium-giljotinen** utgjør en direkte maskinvarelås med responstid på $2{,}0\text{ ns}$ uavhengig av operativsystemet.

Dersom et miljøsjokk eller termisk tap driver $M_{\text{stab}} \to 0$, utløser $2{,}0\text{ ns}$-giljotinen en momentan kortslutning til $0{,}00\text{ V DC}$. Dette kutter strømmen til pilotkretsene og utløser en mekanisk nødavstengning (ESD) under $50\text{ bar}$ trykk, der fjærbelastede ventiler i Super Duplex 2507-stål og grad 5-titan stenger kretsløpet fullstendig på $38{,}4\text{ ms}$ – innenfor sikkerhetsmarginen på $< 45{,}0\text{ ms}$. Som det vises i Kjerneprøve III (Kapittel `5.4`), leder denne analysen direkte til verkets ingeniørmessige subtraksjonsdom for den stasjonære Skagerrak-noden (`SPEC-250`): i stedet for å balansere en sårbar, kokende gasshinne i åpent hav, forkastes utvendig filmkoking til fordel for en **passiv Matrioshka-vakuumkapsling** på innsiden av et lukket $\text{Ti-6Al-4V}$-trykkskrog, der $38{,}4\text{ ms}$-sikkerhetsventilene fungerer som den siste mekaniske skranken.

---

## 3. Relativistisk Inngjerding og Det Epistemiske Bevishierarkiet

På samme måte som Moreau-operatoren stenger ute spøkelsesseire i tilstandsrommet, stenger den relativistiske lyskjeglemetrikken ($ds^2 = -(c\Delta t)^2 + \vert\Delta \mathbf{r}\vert^2$) ute falske posisjons- og reléangrep via *Digital Radio Frequency Memory* (DRFM), GNSS-forfalskning (*spoofing*) og videresending (*meaconing*). Fordi fysikken kun tillater interaksjoner langs tidslignende eller lyslignende baner ($ds^2 \le 0$), vil ethvert syntetisk relé utenfor perimeteren på $\Delta r = 20\text{ meter}$ overskride den øvre tidsgrensen $\Delta t_{\text{roundtrip}} = 2\Delta r / c \approx 133{,}42\text{ ns}$ og drive intervallet over i det romlignende regimet ($ds^2 > 0$), hvorpå tilstanden nektes overgang til `OPEN` ($5{,}00\text{ V DC}$) og felles til $0{,}00\text{ V DC}$.

Et feilsikkert system krever dermed en absolutt grenseoppgang mellom teoretiske modeller, programvarearkitektur og fysisk verifisert maskinvare. Ingen påstand om sikkerhet er gyldig uten at den understøttes av måleinstrumenter på atomært og relativistisk nivå: **operando-spektroskopi** ($\text{NMR}$ og $^{57}\text{Fe}$ Mössbauer-isomerskift $\delta \approx 0{,}8\text{ mm/s}$ samt kjemiske stasislåser ved $\text{O}_2 < 0{,}5\text{ ppm}$ og $0{,}0\text{ ppm }\text{NH}_3$) bekrefter fysiske og kjemiske tilstandsendringer før høyspenningskretser lukkes; **Ultra-Wideband (UWB) tidsmetrologi** håndhever den relativistiske avstandsgrensen ($\Delta t \le 133{,}42\text{ ns}$) i sanntid; og **ikke-flyktige vitnekjeder** forsegler enhver tilstandsovergang i en uforanderlig historikk over systemets faktiske utførelse. Denne strukturen tvinger ethvert signal gjennom et tredelt epistemisk hierarki:

| Epistemisk nivå | Operasjonelt domene | Håndhevelsesmekanisme |
| --- | --- | --- |
| **`INSPIRED_BY`** | Teoretisk modell ($\text{L0}$) | Kandidatgenerator ($\Phi$): Simulerer ubegrensede strategier i $\mathcal{NP}$-rommet uten fysisk forpliktelse. |
| **`IMPLEMENTS`** | Programvare / RTL ($\text{L1}$) | Projeksjonsoperator ($\Pi_K$): Kontrollerer levedyktighetsgrenser ($\text{Viab}$), Nagumo-betingelser ($\dot{x} \in T_K(x)$) og CBF-skranker. |
| **`PROVES`** | Fysisk maskinvare ($\text{L2/L3}$) | Maskinvarerealisering ($\Omega$): Aktiverer fysiske låser til $0{,}00\text{ V DC}$ (`KILL`/`HOLD`) eller $5{,}00\text{ V DC}$ (`OPEN`/`COMMIT`), sikret i vitnekjeder. |

Ved å skille forslag ($\Phi$), projeksjon ($\Pi_K$) og fysisk fullbyrdelse ($\Omega$), garanterer arkitekturen at ingen virtuell representasjon kan omgå den fysiske verdens skranker:

$$\mathcal{T}_{\text{KY}} = \mathcal{M} = \Omega \circ \Pi_K \circ \Phi$$

Overlevelse i fiendtlige miljøer kan aldri hvile på abstraksjoner som feiler mot det åpne. Dynamikken genererer muligheter; admissibiliteten avgjør hva som får eksistere.
