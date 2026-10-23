# Begrepsforklaring: Fine–Wilf-teoremet og elimineringsmekanismen for spøkelsesmønstre

**Forfatter:** Marius Egerhei Torjusen (ORCID: `0009-0002-9877-5664`)  
**Kanonisk Lokus:** `RADIKAL_DESTILLERING/INTERKOGNITIV_MAPPE/19_BEGREPSFORKLARING_FINE_WILF_OG_SPOKELSESMONSTRE.md`  
**Epistemisk Demarkasjon (`AGENTS.md`):** `L0 Matematisk Teorem (Fine & Wilf, 1965)` $\land$ `L1 Deterministisk Portlogikk` (`INSPIRED_BY != IMPLEMENTS != PROVES`)

---

## 1. Innledning: Når rytmer lurer sansene (Mønstre og spøkelser)

### Hva er et spøkelsesmønster, og hvorfor trengs en observasjonshorisont?
Et **spøkelsesmønster** (også kalt et fantommål, falskt ekko eller *jammer ghost*) er en kombinatorisk illusjon der to uavhengige, overlappende perioder danner en midlertidig sekvens som ser ut til å følge en streng og felles lovmessighet. For å skille en slik forbigående organisatorisk luftspeiling fra en reell fysisk periode, kreves det en matematisk definert **observasjonshorisont** — et minste antall sammenhengende målinger som må gjennomføres før signalbehandlingssystemet kan avdekke en uunngåelig motstrid og felle en sikker dom.

I arbeidet med bølgefenomener, digital signalbehandling og mønstergjenkjenning støter man ofte på situasjoner der to uavhengige rytmer samhandler. Tenk deg to mekaniske ståltannhjul som roterer ved siden av hverandre. Det første hjulet har $p = 5$ tenner, mens det andre har $q = 8$ tenner. Dersom vi betrakter tennenes kontaktpunkter som diskrete klokkepulser eller impulsintervaller ($\text{PRI}_1 = 5$ og $\text{PRI}_2 = 8$), vil tannhjulene i korte tidsintervaller gli inn i det som fremstår som en perfekt, synkronisert takt. Denne mekaniske glidningen og fasemotsetningen speiler nøyaktig den fasetvetydigheten som oppstår i digitale signalbehandlingssystemer.

I radar- og sonarsystemer, programvaredefinert radio (SDR) og avanserte kommunikasjonsnettverk oppstår et tilsvarende fenomen. Når to ulike tidsintervaller overlapper i et for kort observasjonsvindu, dannes det et spøkelsesmønster. Dette er en strukturert datastrøm som fremstår som fullstendig periodisk og lovmessig for observatøren, men som i den fysiske virkeligheten bare er et resultat av kildenes kombinatoriske overlapp.

For å bygge et presist rammeverk rundt dette fenomenet, definerer vi tre helt sentrale begreper:

* **Periode ($p, q$):** Antallet diskrete steg, tegn eller klokkepulser et mønster bruker på å gjenta seg selv eksakt.
* **Periodelåsing:** Tilstanden som inntreffer når to overlappende rytmer over tilstrekkelig lang tid tvinges til å kollapse inn i sin felles underliggende grunnrytme, gitt ved største felles divisor, $\gcd(p, q)$.
* **Observasjonsvindu ($L$):** Antallet sammenhengende målepunkter, tegn eller tidssteg som analyseres i en sammenhengende dataserie.

Dette bringer oss fra den mekaniske intuisjonen om roterende tannhjul over til den matematiske formelen som definerer den absolutt knivskarpe grensen for hvor lenge en slik illusjon kan opprettholdes.

---

## 2. Den matematiske kjernen: Fine–Wilf-teoremet (1965)

I 1965 beviste matematikerne Nathan Jacob Fine og Herbert Wilf den eksakte teoretiske grensen for hvor lenge to ulike perioder, $p$ og $q$, kan opprettholde en falsk illusjon om felles synkronitet uten å kollapse til sin felles grunnrytme.

Teoremet etablerer en absolutt observasjonshorisont $L^*$, uttrykt ved følgende formel:

$$\boxed{L^* = p + q - \gcd(p, q)}$$

For å bryte ned formelen og gjøre variabelkomponentene intuitive for en ny student, benytter vi følgende oversikt:

| Variabel / Symbol | Pedagogisk forklaring & Betydning for Observatøren |
| :--- | :--- |
| **$p$** | Lengden på den første perioden eller rytmen som undersøkes (f.eks. $p = 5$ klokkepulser). |
| **$q$** | Lengden på den andre perioden eller rytmen som undersøkes (f.eks. $q = 8$ klokkepulser). |
| **$\gcd(p, q)$** | Største felles divisor (*Greatest Common Divisor*) for $p$ og $q$. Dette er den største felles underliggende grunnrytmen begge periodene deler. Dersom $p$ og $q$ er innbyrdes primiske, er $\gcd(p, q) = 1$. |
| **$L^*$** | Den absolutte observasjonshorisonten. Dette er det minste antall sammenhengende observasjoner som kreves for at systemet matematisk garantert skal avsløre en falsk periodisitet eller tvinge frem en absolutt periodelåsing. |

### Hvorfor $\gcd(p, q) = 1$ gir den lengste illusjonen

Største felles divisor, $\gcd(p, q)$, uttrykker systemets felles underliggende struktur. Dersom to perioder deler en stor felles divisor (f.eks. $p = 6$ og $q = 9 \implies \gcd(6, 9) = 3$), har signalene sterk felles takt, og horisonten nås raskt ($L^* = 6 + 9 - 3 = 12$).

Når $p$ og $q$ er innbyrdes primiske ($\gcd(p, q) = 1$), finnes det ingen felles underliggende takt utover det enkelte elementet. Dette representerer observatørens verste scenario (*worst-case scenario*): Jo mindre felles grunnrytme periodene har, desto lenger kan illusjonen opprettholdes. Det er nettopp ved $\gcd(p, q) = 1$ at spøkelsesmønsteret oppnår sin maksimale varighet før det kollapser.

### Observasjonsvinduets to tilstander

1. **Under horisonten ($L < L^*$):** Systemet befinner seg i et tvetydig område. To helt uavhengige perioder kan produsere en sekvens som ser 100 % lovmessig ut. Tvetydigheten kan ikke oppklares matematisk innenfor dette vinduet.
2. **Ved eller over horisonten ($L \ge L^*$):** Illusjonen kollapser ubønnhørlig. Dersom sekvensen oppfyller periodisiteten helt til $L^*$, tvinges signalet til å være strikt periodisk med periode $\gcd(p, q)$. Dersom signalet ikke deler denne grunnrytmen, oppstår det en uunngåelig kollisjon (kontradiksjon) ved det eksakte steget $L^*$.

Dette bringer oss fra den teoretiske formelen over til et klassisk, konkret eksempel der vi trinn for trinn skal bevise teoremets virkemåte.

---

## 3. Dypdykk i spøkelsesordet: Eksempelet med $p = 5$ og $q = 8$

La oss undersøke hva som skjer når vi velger to innbyrdes primiske perioder: $p = 5$ og $q = 8$. Siden største felles divisor for $5$ og $8$ er $\gcd(5, 8) = 1$, beregner vi den eksakte observasjonshorisonten $L^*$:

$$L^* = 5 + 8 - \gcd(5, 8) = 5 + 8 - 1 = 12$$

Dette regnestykket forteller oss at det er mulig å konstruere et «spøkelsesord» av lengde $L = L^* - 1 = 11$ tegn som oppfyller både en 5-takt og en 8-takt samtidig, uten at det oppstår en eneste konflikt i løpet av de 11 første posisjonene.

### Visning av spøkelsesordet ($L = 11$)

Det klassiske Sturmiske spøkelsesordet over alfabetet $\{\text{A}, \text{B}\}$ av lengde 11 har følgende struktur:

```text
Indeks:    1   2   3   4   5   6   7   8   9  10  11
Bokstav:   A   B   A   A   B   A   B   A   A   B   A
```

### Verifisering av dobbeltperiodisitet

Vi kan kontrollere at denne sekvensen tilfredsstiller begge periodene for alle gyldige indekser i vinduet:

* **Verifisering av periode $p = 5$ ($a_i = a_{i+5}$ for $i \in \{1, \dots, 6\}$):**
  * $i = 1$: $a_1 = \text{A}$ og $a_6 = \text{A} \implies \text{A} = \text{A}$ (Stemmer)
  * $i = 2$: $a_2 = \text{B}$ og $a_7 = \text{B} \implies \text{B} = \text{B}$ (Stemmer)
  * $i = 3$: $a_3 = \text{A}$ og $a_8 = \text{A} \implies \text{A} = \text{A}$ (Stemmer)
  * $i = 4$: $a_4 = \text{A}$ og $a_9 = \text{A} \implies \text{A} = \text{A}$ (Stemmer)
  * $i = 5$: $a_5 = \text{B}$ og $a_{10} = \text{B} \implies \text{B} = \text{B}$ (Stemmer)
  * $i = 6$: $a_6 = \text{A}$ og $a_{11} = \text{A} \implies \text{A} = \text{A}$ (Stemmer)
* **Verifisering av periode $q = 8$ ($a_i = a_{i+8}$ for $i \in \{1, 2, 3\}$):**
  * $i = 1$: $a_1 = \text{A}$ og $a_9 = \text{A} \implies \text{A} = \text{A}$ (Stemmer)
  * $i = 2$: $a_2 = \text{B}$ og $a_{10} = \text{B} \implies \text{B} = \text{B}$ (Stemmer)
  * $i = 3$: $a_3 = \text{A}$ og $a_{11} = \text{A} \implies \text{A} = \text{A}$ (Stemmer)

Gjennom 11 tegn fremstår datastrømmen som fullstendig harmonisk og dobbeltperiodisk. Et uforberedt målesystem ville konkludert med at mønsteret var bekreftet.

### Det 12. steget (Kollapsen)

Hva skjer dersom utvidelsen av observasjonsvinduet når horisonten ved posisjon 12 ($L = 12$)? Da tvinges systemet til å bestemme verdien for tegn $a_{12}$:

1. **Krav fra periode $p = 5$:**
   $$a_{12} = a_{12-5} = a_7 = \text{B}$$
2. **Krav fra periode $q = 8$:**
   $$a_{12} = a_{12-8} = a_4 = \text{A}$$

Dette leder uunngåelig til en direkte matematisk motstrid (kontradiksjon):

$$a_7 = a_{12} = a_4 \implies \text{B} = \text{A}$$

> **Nøkkelinnsikt: Den knivskarpe kollisjonen**  
> Spøkelsesordet kollapser diskret og uunngåelig ved det eksakte steget $L^* = 12$. Illusjonen som overlevde plettfritt gjennom 11 steg, brister umiddelbart fordi posisjon 12 krever at tegnet må være identisk med både posisjon 7 ($\text{B}$) og posisjon 4 ($\text{A}$). Siden $\text{A} \neq \text{B}$, sprekker kamuflasjen momentant.

Denne kombinatoriske kollisjonen er ikke bare et teoretisk tankeeksperiment; den danner det direkte fundamentet for praktisk ingeniørkunst og robust signalbehandling.

---

## 4. Anvendelse i signalbehandling: Staggered-PRF radar og SDR

I avanserte radar-, sonar- og programvaredefinerte radiosystemer (SDR) benyttes en teknikk som kalles *Staggered Pulse Repetition Frequency (PRF)*. For å unngå blindsoner i avstand og Doppler-hastighet, sender transceiveren ut pulsrekker med to eller flere innbyrdes primiske pulsintervaller – for eksempel $\text{PRI}_1 = p = 5$ og $\text{PRI}_2 = q = 8$ klokkepulser.

Når radarsignalet treffer terreng, støy eller falske sendere (jammere), kan det oppstå flerveis-spøkelsesekko (*multipath clutter / jammer ghosts*). Et slikt spøkelsesekko kan returnere sekvensen `ABAABABAABA` ($L = 11$).

For å forhindre at systemet utløser falsk alarm, bygges signalbehandlingsfilteret ($\Pi_{\mathcal{K}}$) opp med en streng *fail-closed* arkitektur. Så lenge observasjonslengden er under horisonten ($L < 12$), holdes filterporten låst ved $0{,}00\text{ V DC}$ (`GATE::HOLD`). Dette sikrer at uverifiserte kandidatsignaler nektes adgang før den teoretiske bevisgrensen er passert, slik at falske ekko ikke forurenser målsporingen.

Når observasjonsvinduet når $L \ge 12$, skiller systemet operasjonelt mellom kollisjon og koherens:

| Observasjonslengde ($L$) | Tilstand / Mønster | Matematisk status | Port-beslutning & Spenning |
| :--- | :--- | :--- | :--- |
| **Sub-horisont ($L < 12$)**<br/>($L = 11$) | Sub-horisont spøkelsesord (`ABAABABAABA`) | Tvetydighet: Spøkelsesord ubekreftet. Kan være en kombinatorisk luftspeiling. | `GATE::HOLD`<br/>($0{,}00\text{ V DC}$) |
| **Horisont ($L \ge 12$)**<br/>(Kontradiksjon) | Flerveis-kollisjon ved horisont ($a_{12}: \text{B} \neq \text{A}$) | Kontradiksjon avdekket: Spøkelsesmål isolert og avvist. | `GATE::KILL`<br/>($0{,}00\text{ V DC}$) |
| **Horisont ($L \ge 12$)**<br/>(Koherens) | Koherent pulsrekke bekreftet uten kontradiksjon | Ekte periode identifisert: Verifisert fysisk mål. | `GATE::OPEN`<br/>($24{,}00\text{ V DC}$) |

Dersom datastrømmen stopper ved $L = 11$, har ikke systemet nok informasjon til å bekrefte målet, og porten holdes i trygg stase (`GATE::HOLD` ved $0{,}00\text{ V DC}$). Ved $L = 12$ vil enten kontradiksjonen avdekkes slik at spøkelset forkastes (`GATE::KILL` ved $0{,}00\text{ V DC}$), eller en koherent, ekte periode bekreftes slik at porten åpnes for videre sporing (`GATE::OPEN` ved $24{,}00\text{ V DC}$).

Dermed utgjør den matematiske observasjonsterskelen det absolutte skillet mellom empirisk sannhet og systemisk bedrag i digital signalbehandling.

---

## 5. Oppsummering og pedagogiske sjekkpunkter

For å oppsummere den kognitive kjernen i Fine–Wilf-teoremet før videre studier eller eksamen, kan vi feste oss ved tre hovedinnsikter:

1. **Observasjonshorisontens ubønnhørlighet ($L^*$):**
   Man må aldri konkludere med at to overlappende rytmer er synkrone eller tilhører et ekte mål før observasjonsvinduet tilfredsstiller $L \ge p + q - \gcd(p, q)$. Alt som observeres før denne grensen kan være en digital eller kombinatorisk luftspeiling.
2. **Fellen ved korte vinduer ($L < L^*$):**
   Korte dataserier har en naturlig tilbøyelighet til å skape *apofeni* — opplevelsen av mønster og mening i ufullstendige data. Spøkelsesordet `ABAABABAABA` viser at perfekt orden over 11 steg kan være ren kombinatorisk kamuflasje.
3. **Den knivskarpe faseovergangen:**
   Overgangen fra tilsynelatende frihet ($L = 11$) til absolutt matematisk lås skjer ikke gradvis, men i ett enkelt diskret steg ved $L^* = 12$, der kravene fra de to periodene kolliderer direkte.

### Avsluttende sammendragstabell

| Matematisk begrep | Fysisk / Signalteknisk manifestasjon | Operasjonell konsekvens i portstyring |
| :--- | :--- | :--- |
| **Under-horisont ($L < L^*$)** | Sub-horisont spøkelsesekko eller ufullstendig sekvens. | `GATE::HOLD` ($0{,}00\text{ V DC}$) – Signalet låses i avventende, *fail-closed* tilstand. |
| **Horisontsnitt ($L^* = p + q - \gcd(p, q)$)** | Eksakt Fine–Wilf-kollisjonspunkt (posisjon 12). | Avdekking av kontradiksjon ($\text{B} \neq \text{A}$) eller bekreftelse av ekte grunnrytme. |
| **Periodelåsing ($\gcd(p, q)$)** | Sammenfall til felles underliggende grunnrytme. | `GATE::OPEN` ($24{,}00\text{ V DC}$) ved verifisert mål, eller `GATE::KILL` ($0{,}00\text{ V DC}$) ved avvist spøkelse. |
