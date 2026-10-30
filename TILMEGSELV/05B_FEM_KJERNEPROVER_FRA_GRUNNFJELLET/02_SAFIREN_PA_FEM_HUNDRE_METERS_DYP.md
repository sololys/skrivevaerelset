# KJERNEPRØVE II: SAFIREN PÅ FEM HUNDRE METERS DYP
### *Hydrostatisk spenningsanalyse, monokrystallinsk $\text{Al}_2\text{O}_3$, $\text{Ti-6Al-4V}$-bikubegitter, fotoelastisk gruppeforsinkelse ($\Delta \tau_{\text{RT}} = -0{,}27\text{ fs}$) og kavitasjonsstyrt karantene*

```text
========================================================================================
KJERNEPRØVE II // SAFIREN PÅ FEM HUNDRE METERS DYP:
  Verk          : KONSEPTUELL GRANITT — Et forsøk på sannhet (Til meg selv)
  Forfattere    : Marius Egerhei Torjusen (ORCID: 0009-0006-0431-6637 // WoS: PJT-0190-2026) & Antigravity
  Entitet       : Brahman · Risør / Det Fennoskandiske Skjold (Locus Zero, 2026)
  Bevisnivåer   : L0 (Hydrostatikk, Kirchhoff–Love-plateteori, fotoelastisitet, Blake-kavitasjon)
                | L1 (Subsea-optisk verifikasjonssuite, HoldBubbleDegassingWait = 2500 ms)
                | L2 (SPEC-250 vindus- og transduserspesifikasjon — HOLD inntil 75,71 bar test)
  Epistemisk lov: INSPIRED_BY != IMPLEMENTS != PROVES
========================================================================================
```

---

## I. Hydrostatisk last på $500\text{ meters}$ dyp ($\text{L0}$)

\begin{center}
\includegraphics[width=0.72\textwidth]{/home/sololyset/07_BOKHYLLA_MONOGRAFIER_OG_BOKVERK/07_TIL_MEG_SELV_KONSEPTUELL_GRANITT/BILDER/bw_03_safiren_500m_skagerrak.jpg}\\[0.3em]
{\footnotesize \textit{Kjerneprøve II og III: Titankapselen (\texttt{SPEC-250}) på $500\text{ meters}$ dyp i Skagerrak med rur (\textrm{Balanus crenatus}) på ytterkåpen, 4-lags Matrioshka-vakuumkapsling og kollimert optisk stråle gjennom safirvinduet.}}
\end{center}

For en undervannsnode (`SPEC-250`) plassert på dybde $z = 500{,}0\text{ m}$ i sjøvann med tetthet $\rho_{\text{sw}} = 1028{,}0\text{ kg/m}^3$, tyngdeakselerasjon $g = 9{,}80665\text{ m/s}^2$ og atmosfærisk overflatetrykk $P_{\text{atm}} = 101\,325\text{ Pa}$ er det absolutte hydrostatiske trykket:

$$P = P_{\text{atm}} + \rho_{\text{sw}} g z = 101\,325\text{ Pa} + (1028{,}0 \times 9{,}80665 \times 500{,}0)\text{ Pa} = 5{,}1419 \times 10^6\text{ Pa} \approx 51{,}42\text{ bar}$$

Gauge-trykket (differensialtrykket mot et internt instrumentkammer ved $1{,}0\text{ atm}$) er:

$$\Delta P = 5{,}047\text{ MPa} \quad (50{,}47\text{ bar}, \text{ prøvetrykk } P_{\text{test}} = 1{,}5 \times \Delta P = 75{,}71\text{ bar})$$

Over en sirkulær hovedflens med diameter $D = 476{,}2\text{ mm}$ ($r = 0{,}2381\text{ m}$, areal $A = \pi r^2 = 0{,}1781\text{ m}^2$) utøver vannsøylen en statisk totalkraft på:

$$F_{\text{tot}} = \Delta P \cdot A = 5{,}047 \times 10^6\text{ Pa} \times 0{,}1781\text{ m}^2 \approx 898\,900\text{ N} \quad (89{,}89\text{ tonn-kraft})$$

Samtidig utsettes den optiske grenseflaten for marin begroing fra rur (*Balanus crenatus* / *Balanus improvisus*) og bakteriell biofilm som må fjernes uten mekaniske vindusviskere eller giftige biocider.

---

## II. Monokrystallinsk $\text{Al}_2\text{O}_3$ og $275\text{ nm}$ UV-C-transmisjon

Konvensjonelt borosilikat- eller silikaglass absorberer kortbølget ultrafiolett stråling og slites av kvartsførende bunnstrømmer. Vinduet spesifiseres derfor i syntetisk monokrystallinsk safir ($\alpha\text{-Al}_2\text{O}_3$, $c$-akse-orientert $[0001]$):

1. **Mekanisk hardhet og styrke:** Knoop-hardhet $\approx 1800\text{--}2200\text{ kg/mm}^2$ (Mohs $9$), elastisitetsmodul $E = 345\text{ GPa}$, Poisson-tall $\nu = 0{,}27$, karakteristisk bøyestrekkfasthet $\sigma_f = 400\text{ MPa}$ og trykkfasthet $> 2000\text{ MPa}$.
2. **Optisk båndgap og UV-C-gjennomslipp:** Båndgapet $E_g = 8{,}8\text{ eV}$ ($\lambda_{\text{edge}} \approx 141\text{ nm}$) muliggjør innvendig AlGaN UV-C-bestråling ved den germicide bølgelengden $\lambda_{\text{UV-C}} = 275\text{ nm}$ med strålingsdose $H_{\text{UV}} \ge 25{,}0\text{ mJ/cm}^2$.
3. **Fresnel- og bulktransmisjon:** Med brytningsindeks $n_{275\text{nm}} \approx 1{,}826$ og bulk-absorpsjonskoeffisient $\alpha_{275\text{nm}} \approx 0{,}035\text{ cm}^{-1}$ er den totale optiske transmisjonen fra innsiden og ut i den våte grenseflaten:

$$T_{275\text{nm}} = (1 - R_1)(1 - R_2) e^{-\alpha t} \approx 86{,}4\,\%$$

---

## III. Strukturell spenningsreduksjon via $\text{Ti-6Al-4V}$-bikubegitter

For en åpen safirblender med tykkelse $t = 2{,}0\text{ mm}$ og uavstivet blenderdiameter $D_s = 12{,}0\text{ mm}$ ($r_s = 6{,}0\text{ mm}$) under $\Delta P = 5{,}047\text{ MPa}$ gir Kirchhoff–Love-plateteorien en maksimal radiell bøyespenning på:

$$\sigma_{\max,\text{open}} = \frac{3(3 + \nu)}{8} \Delta P \left(\frac{r_s}{t}\right)^2 = \frac{3(3 + 0{,}27)}{8} \times 5{,}047\text{ MPa} \times \left(\frac{6{,}0}{2{,}0}\right)^2 \approx 55{,}70\text{ MPa}$$

Ved å legge safirvinduet an mot et internt heksagonalt bikubegitter (*honeycomb lattice*) i grad 5 titan ($\text{Ti-6Al-4V}$, flytegrense $\sigma_y = 880\text{ MPa}$) med cellediameter $d_{\text{cell}} = 2{,}0\text{ mm}$ ($r_{\text{cell}} = 1{,}0\text{ mm}$) og fast innspent cellekant reduseres den frie spennvidden med faktoren $(d_{\text{cell}} / D_s)^2 = (2 / 12)^2 = 1/36$, og den maksimale lokale bøyespenningen i hver celle faller til:

$$\sigma_{\max,\text{cell}} = \frac{3}{4} \Delta P \left(\frac{r_{\text{cell}}}{t}\right)^2 = 0{,}75 \times 5{,}047\text{ MPa} \times \left(\frac{1{,}0}{2{,}0}\right)^2 \approx 0{,}946\text{ MPa}$$

Dette gir en statisk sikkerhetsfaktor mot bøyestrekkbrudd på:

$$\text{SF} = \frac{\sigma_f}{\sigma_{\max,\text{cell}}} = \frac{400\text{ MPa}}{0{,}946\text{ MPa}} \approx 422{,}8$$

### Bruddmekanisk kritisk sprekkdybde (Griffith–Irwin)
Etter Griffith–Irwin-relasjonen $K_{Ic} = Y \sigma \sqrt{\pi a}$ (med bruddseighet $K_{Ic} = 2{,}0\text{ MPa}\cdot\text{m}^{1/2}$, geometrifaktor $Y = 1{,}12$ og konservativ lokal referansespenning $\sigma_{\text{ref}} = 44{,}5\text{ MPa}$ ved innfestingsranden) er den kritiske sprekkdybden for ustabil sprekkvekst:

$$a_{\text{crit}} = \frac{1}{\pi}\left(\frac{K_{Ic}}{Y \sigma_{\text{ref}}}\right)^2 \approx 511\,\mu\text{m}$$

Siden optisk polert safir ($R_a < 10\text{ nm}$) har maksimal overflatedefekt $a_0 < 1{,}0\,\mu\text{m} \ll a_{\text{crit}} = 511\,\mu\text{m}$, er sprøbrudd under hydrostatisk last utelukket.

---

## IV. Balansen mellom optisk gruppeforsinkelse og hydrostatisk trykk ($\Delta \tau_{\text{RT}} = -0{,}27\text{ fs}$)

Fordi undervannsnoden bruker safirvinduet til fasekoherent optisk Time-of-Flight-måling innenfor Alexandrov-diamanten (Kjerneprøve I, der TDC-oppløsningen er $15\text{ ps} = 1{,}5 \times 10^{-11}\text{ s}$), må det verifiseres at kompresjonen av vinduet ved $\Delta P = 5{,}047\text{ MPa}$ ikke forfalsker lysets gangtid $\tau_{\text{RT}}$.

Den optiske tur-retur-gangtiden gjennom et vindu med tykkelse $t$ og gruppebrytningsindeks $n_g$ er:

$$\tau_{\text{RT}}(P) = \frac{2 \, n_g(P) \, t(P)}{c}$$

Ved en hydrostatisk trykkendring $\Delta P$ påvirkes $\tau_{\text{RT}}$ av to konkurrerende fysiske effekter med motsatt fortegn (**Nivå $\text{L0}$**):

1. **Hookes elastiske tynning ($\Delta t < 0$, forkorter lysveien):**
   Langs $c$-aksen ($E_{33} \approx 345\text{--}400\text{ GPa}$, effektiv enaksial kompresjonsmodul med Poisson-kobling $E_{\text{eff}} \approx 460\text{ GPa}$) trykkes vinduet ($t = 2{,}0\text{ mm}$) sammen med:
   $$\Delta t = -t \frac{\Delta P}{E_{\text{eff}}} \approx -2{,}0 \times 10^{-3}\text{ m} \times \frac{5{,}047\text{ MPa}}{460\,000\text{ MPa}} \approx -2{,}19 \times 10^{-8}\text{ m} = -21{,}9\text{ nm}$$
   Bidraget fra geometrisk tynning alene reduserer gangtiden med:
   $$\Delta \tau_{\text{geom}} = \frac{2 n_g \Delta t}{c} \approx \frac{2 \times 1{,}768 \times (-2{,}19 \times 10^{-8}\text{ m})}{2{,}9979 \times 10^8\text{ m/s}} \approx -0{,}258\text{ fs}$$

2. **Pockels fotoelastiske tetningsøkning ($\Delta n_g \lessgtr 0$):**
   Når krystallgitteret komprimeres, endres brytningsindeksen via safirens fotoelastiske konstanter ($p_{11}, p_{12}, p_{31}, p_{33}$). For $\alpha\text{-Al}_2\text{O}_3$ er den netto trykkderiverte av brytningsindeksen svært liten og svakt negativ ved biaxial/hydrostatisk spenningstilstand ($\frac{\mathrm{d}n}{\mathrm{d}P} \approx -0{,}35 \times 10^{-6}\text{ MPa}^{-1}$ grunnet dominerende kovalent gitterstivhet), noe som gir:
   $$\Delta n_g = \left(\frac{\mathrm{d}n_g}{\mathrm{d}P}\right) \Delta P \approx -1{,}77 \times 10^{-6}, \qquad \Delta \tau_{\text{photo}} = \frac{2 t \Delta n_g}{c} \approx -0{,}012\text{ fs}$$

Summen av det elastiske og det fotoelastiske bidraget gir det totale tur-retur-tidsavviket ved $50{,}47\text{ bar}$:

$$\Delta \tau_{\text{RT}} = \frac{2}{c}\left(n_g \Delta t + t \Delta n_g\right) = \Delta \tau_{\text{geom}} + \Delta \tau_{\text{photo}} \approx -0{,}27\text{ fs} \quad (-2{,}7 \times 10^{-16}\text{ s})$$

Forholdet mellom TDC-klokkens oppløsning ($15\text{ ps}$) og safirvinduets trykkinduserte tidsavvik ($0{,}27\text{ fs}$) er:

$$\frac{\Delta t_{\text{TDC}}}{|\Delta \tau_{\text{RT}}|} = \frac{1{,}5 \times 10^{-11}\text{ s}}{2{,}7 \times 10^{-16}\text{ s}} \approx 55\,555$$

Safirkrystallens høye elastisitetsmodul ($345\text{ GPa}$) og minimale fotoelastiske koeffisient gjør dermed vinduet kausalt invariant over hele dybdeprofilet fra $0$ til $500\text{ meter}$.

---

## V. Piezo-akustisk kavitasjon ($42\text{ kHz}$) og karanteneloven ($\tau_{\text{clear}} = 2500\text{ ms}$)

En ringformet piezoelektrisk transduser i $\text{PZT-4}$ eksiterer safirplaten ved $f_{\text{ac}} = 42{,}0\text{ kHz}$ med lokal akustisk trykkamplitude:

$$P_{\text{ac}} = 180{,}0\text{ kPa} > \Delta P_{\text{Blake,eff}} = 168{,}0\text{ kPa}$$

Når mikroboblene kollapser asymmetrisk mot safirflaten, dannes mikrostråler ($v_{\text{jet}} \approx 110\text{ m/s}$) som sprenger løs rurkalk og slam uten å ripe $\text{Al}_2\text{O}_3$-gitteret.

Etter endt kavitasjonspuls håndhever skranken $\Pi_K$ en obligatorisk oppløsnings- og avluftskarantene (`HoldBubbleDegassingWait`) styrt av Epstein–Plesset-diffusjonstiden og Mie-spredningsmonitoren:

$$\tau_{\text{clear}} = 2500\text{ ms}$$

I løpet av disse $2{,}5\text{ sekundene}$ holdes måleslusen i `HOLD` ($0{,}00\text{ V DC}$) inntil mikroboblene er fullstendig oppløst og optisk koherens er gjenopprettet.

> **`[ `$\approx$` ROSETTA-SVEIS // `$\Pi_K$` ]` Urverkets rubin, ruren på skroget og tålmodigheten på 2,5 sekunder**
> Se på de to tallene som møtes gjennom det $2{,}0\text{ mm}$ tykke safirvinduet ($\alpha\text{-Al}_2\text{O}_3$) på $500\text{ meters}$ dyp i Skagerrak: **$-0{,}27\text{ femtosekunder}$** og **$2\,500\text{ millisekunder}$**. Det skiller seksten tierpotenser mellom dem.
>
> På innsiden av vinduet hviler krystallgitteret mot et bikubegitter av grad 5-titan ($\text{Ti-6Al-4V}$) mens vannsøylen presser på flensen med $898\,900\text{ Newton}$ — vekten av nesten nitti tonn. Likevel er den kovalente gitterstivheten i safiren ($345\text{ GPa}$) så ubestikkelig at Hookes elastiske tynning ($-21{,}9\text{ nm} \implies -0{,}258\text{ fs}$) og Pockels fotoelastiske indeksendring ($-0{,}012\text{ fs}$) bare forskyver lysets gangtid med $0{,}27$ tusendels pikosekund — $55\,555$ ganger mindre enn klokkens egen oppløsning på $15\text{ ps}$. Det er av nøyaktig samme grunn gamle urmakere i Genève satte syntetiske safir- og rubinsteiner i ankerhemmingen på mekaniske kronometre: steinen nekter å gi etter for trykk.
>
> **`[ `$\boxtimes$` SOMA-ANKER // `$\Pi_{\text{orth}}$` // Kontrastvæske ]`** Men på utsiden av den samme edelsteinen vokser hverdagen i Skagerrak: rurkalk (*Balanus crenatus*) og slim som vil blinde øyet. Når PZT-4-ringen fyrer av sin $42{,}0\text{ kHz}$ kavitasjonspuls ($180{,}0\text{ kPa}$) og pisker løs mikrostråler på $110\text{ m/s}$ som sprenger ruren av glasset, fylles vannet foran linsen av en kokende sky av mikrobobler. En utålmodig maskin ville skutt laserstrålen rett inn i bobleskyen, mistet koherensen og ropt alarm.
>
> **`[ `$\odot \prec 1$` // POINCARÉ-LÅS // 0,00 V DC HOLD ]`** Skranken gjør det motsatte: den legger hendene på ryggen i eksakt $2\,500\text{ ms}$ (`HoldBubbleDegassingWait`) ved $0{,}00\text{ V DC}$ og venter i mørket på $500\text{ meters}$ dyp til den siste boblen er løst opp etter Epstein–Plesset-ligningen. Sannhet krever både safirens hardhet på femtosekundet og dykkerens ro til å vente to og et halvt sekund til slammet har lagt seg.
