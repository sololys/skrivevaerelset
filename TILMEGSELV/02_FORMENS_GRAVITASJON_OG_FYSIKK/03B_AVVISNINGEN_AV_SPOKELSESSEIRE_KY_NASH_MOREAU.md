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

## 2. Eksergetisk Skjerming: Det Kryogene Leidenfrost-Plastronet

I arktiske farvann og dypvannskorridorer utsettes autonome plattformer for ekstreme termiske gradienter, hydrodynamisk motstand og aktiv sonardeteksjon. Passivt panser løser ikke disse utfordringene. Overlevelse krever at termisk dissipasjon, motstandsreduksjon og akustisk kamuflasje forenes i ett aktivt termodynamisk skjold.

Fartøyet *HMS Leidenfrost* benytter flytende ammoniakk ($\text{NH}_3$ ved $-33{,}34\,^\circ\text{C}$) for å etablere og opprettholde en kontinuerlig gasshinne – et damp-plastron – rundt hele skroget. Ved å operere i et stabilt filmkokingsregime isoleres det faste skroget fra det omsluttende sjøvannet. Dette gir to målbare fysiske effekter: et **hydrodynamisk friksjonskutt**, der dampfasens lave skjærviskositet frikobler skroget fra grensesjiktets viskøse skjærkrefter og reduserer den hydrodynamiske hudfriksjonen med en faktor på åtte hundre ($800\times$) sammenlignet med direkte væskekontakt, og **akustisk usynlighet**, der den brå endringen i akustisk impedans over gass–væske-grensen absorberer og sprer aktive sonarpulser samtidig som indre mekanisk støy dempes, slik at fartøyet blir tilnærmet usynlig for passive sonarpaneler.

Denne tilstanden hviler på en knivsegg. Dersom den lokale varmefluksen faller under Leidenfrost-punktet, bryter filmkokingen sammen til overgangskoking. Da kollapser gasshinnen, og skroget utsettes for ødeleggende kavitasjon. Systemet overvåker derfor stabilitetsmarginen $M_{\text{stab}}$ i sanntid:

$$M_{\text{stab}} = \frac{\delta - \delta_{\text{crit}}}{\delta}$$

Her er $\delta$ den faktiske tykkelsen på dampfilmen, mens $\delta_{\text{crit}}$ markerer den kritiske grensen for kollaps. Overvåkningen utføres av kontrollrammeverket KORA gjennom to adskilte tidsvinduer: i **FPGA- og programvarevinduet** evaluerer en prosesseringssyklus på $4{,}0\text{ ns}$ klokket ved $500\text{ MHz}$ kontrollbarrierefunksjoner (CBF) og termodynamisk stabilitet, mens **silisium-giljotinen** utgjør en direkte maskinvarelås i silisium med responstid på $2{,}0\text{ ns}$ som opererer helt uavhengig av operativsystemet.

Hvis et miljøsjokk eller termisk tap driver $M_{\text{stab}} \to 0$, utløser $2{,}0\text{ ns}$-giljotinen en momentan kortslutning til $0{,}00\text{ V DC}$. Dette kutter strømmen til pilotkretsene og utløser en mekanisk nødavstengning (ESD) under $50\text{ bar}$ trykk. Fjærbelastede ventiler i Super Duplex 2507-stål og grad 2-titan stenger det kryogene systemet fullstendig på $38{,}4\text{ ms}$. Dette gir en sikkerhetsmargin mot den hydrodynamiske grensen for kavitasjonsbrudd, som ligger på $< 45{,}0\text{ ms}$. Fartøyet låses i sikker stasis før sjokkbølgene rekker å treffe skroget.

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
