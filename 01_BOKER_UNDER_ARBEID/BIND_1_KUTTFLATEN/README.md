# BIND I: KUTTFLATEN (THE CUT SURFACE)

*Fra samlingen som overlevde brente jords taktikk. De tekniske bladene er skåret ut; kun den litterære stammen står igjen.*

---

### *Menneskets møte med friksjon, HOLD og ansvar*

```text
========================================================================================
HOVEDVERKET // BIND I AV TRILOGIEN:
  Verk              : KUTTFLATEN: Menneskets møte med friksjon, HOLD og ansvar
  Forfatter         : Torjusen, Marius Egerhei (ORCID: 0009-0006-0431-6637)
  Lokus             : BOKKANDIDATER/BIND_1_KUTTFLATEN/
  Format            : Norsk Standard Bokformat (155 x 230 mm)
  Sidetall / Omfang : 389 sider / 8 205 linjer
  Master-PDF        : kuttflaten_bok.pdf (6.1 MB)
  Kildemanuskript   : KUTTFLATEN_MASTER_MANUSKRIPT.md
  Målgruppe         : Allmenn sakprosa, filosofer, ledere, samfunnsvitere
========================================================================================
```

---

## 1. Verkets Kjerne og Formål

*Kuttflaten* er Bind I i den store trilogien **Hovedverket**. Boken etablerer det etiske, somatiske og samfunnsmessige grunnlaget for realiseringsarkitekturen:

* **Det somatiske ansvaret:** Hvorfor all abstraksjon til syvende og sist må møte en fysisk kuttflate i menneskekroppen eller i naturen for å være sann.
* **Friksjonens nødvendighet:** Et oppgjør med den moderne illusjonen om friksjonsfrihet. Friksjon er ikke et tap, men selve forutsetningen for grep, retning og etisk tyngde.
* **HOLD som sivilisasjonsprinsipp:** Evnen til å stanse, holde tilbake og kreve vitnesbyrd før en handling realiseres.

---

## 2. Filkatalog

| Fil | Størrelse / Omfang | Beskrivelse |
|---|---|---|
| [`kuttflaten_bok.pdf`](kuttflaten_bok.pdf) | 389 s / 6.1 MB | Komplett, trykkeklar PDF i standard bokformat (155 x 230 mm). |
| [`KUTTFLATEN_MASTER_MANUSKRIPT.md`](KUTTFLATEN_MASTER_MANUSKRIPT.md) | 8 205 linjer / 494 KB | Det samlede, kanoniske Markdown-manuskriptet. |
| [`kuttflaten_bok.tex`](kuttflaten_bok.tex) | 545 KB | LaTeX-kildekode for profesjonell typografisk setting. |
| [`BAKSIDETEKST_BLURB_KUTTFLATEN.md`](BAKSIDETEKST_BLURB_KUTTFLATEN.md) | 2.6 KB | Forlagstekst, baksidetekst og vaskeseddel. |
| [`build_kuttflaten_bok.py`](build_kuttflaten_bok.py) | 11 KB | Python-kompileringsskript for generering av LaTeX og PDF. |
| [`assemble_bind1_clean.py`](assemble_bind1_clean.py) | 6.5 KB | Deterministisk sammenstillingsskript fra kildetekster. |

---

## 3. Kompilering og Bygging

For å rekompilere boken deterministisk fra terminalen:
```bash
cd BOKKANDIDATER/BIND_1_KUTTFLATEN
python3 build_kuttflaten_bok.py
xelatex -interaction=nonstopmode kuttflaten_bok.tex
```
