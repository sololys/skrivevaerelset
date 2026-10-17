# HOVEDVERKET: DEN STORE BOKEN (OMNIBUS)

*Fra samlingen som overlevde brente jords taktikk. De tekniske bladene er skåret ut; kun den litterære stammen står igjen.*

---

### *Det Samlede Ettbinds Praktverket (Bind I, Bind II og Bind III i Én Bok)*

```text
========================================================================================
HOVEDVERKET // OMNIBUS MASTER-UTGAVE:
  Verk              : HOVEDVERKET (Den Store Boken - Omnibus)
  Forfatter         : Torjusen, Marius Egerhei (ORCID: 0009-0006-0431-6637)
  Lokus             : BOKKANDIDATER/HOVEDVERKET_OMNIBUS_EN_BOK/
  Format            : Monumentalt Praktformat (170 x 240 mm / Royal Octavo)
  Sidetall / Omfang : 651 sider / over 25 000 linjer
  Master-PDF        : HOVEDVERKET_DEN_STORE_BOKEN_OMNIBUS.pdf (13.3 MB)
  Kildemanuskript   : HOVEDVERKET_OMNIBUS_MASTER_MANUSKRIPT.md (1.22 MB)
  Innhold           : Komplett samling av Bind I, Bind II og Bind III med felles apparat
========================================================================================
```

---

## 1. Verkets Kjerne og Formål

*Hovedverket (Omnibus)* samler hele Marius Egerhei Torjusens trilogi i ett sammenhengende, monumentalt praktverk på 651 sider:

1. **Del I: Kuttflaten** — Det somatiske ansvaret, friksjonens epistemologi og menneskets forankring (389 s i originalbind).
2. **Del II: Codex Geocybernetica** — Litisk kybernetikk, de 44 leksikonmodulene og de 7 syntetiske kapslene (179 s A4 i originalbind).
3. **Del III: Realiseringsgrammatikk** — OMNI-alfabetet, Drikkegildet ved Porten og Kognitiv Eikonal-Arkitektur (257 s i originalbind).

Omnibus-utgaven er designet for permanent forvaring, akademiske biblioteker og bibliofile samlinger som ønsker hele tenkningen samlet mellom to permer.

---

## 2. Filkatalog

| Fil | Størrelse / Omfang | Beskrivelse |
|---|---|---|
| [`HOVEDVERKET_DEN_STORE_BOKEN_OMNIBUS.pdf`](HOVEDVERKET_DEN_STORE_BOKEN_OMNIBUS.pdf) | 651 s / 13.3 MB | Komplett, trykkeklar master-PDF for hele ettbindsverket. |
| [`HOVEDVERKET_OMNIBUS_MASTER_MANUSKRIPT.md`](HOVEDVERKET_OMNIBUS_MASTER_MANUSKRIPT.md) | 1.22 MB / 25k+ linjer | Det samlede, monolittiske Markdown-kildemanuskriptet. |
| [`HOVEDVERKET_DEN_STORE_BOKEN_OMNIBUS.tex`](HOVEDVERKET_DEN_STORE_BOKEN_OMNIBUS.tex) | 1.38 MB | Komplett LaTeX-kildekode for profesjonell boksetting. |
| [`build_hovedverket_omnibus.py`](build_hovedverket_omnibus.py) | 26 KB | Kompileringsskript for generering av LaTeX og PDF. |
| [`assemble_hovedverket_omnibus.py`](assemble_hovedverket_omnibus.py) | 8.2 KB | Skript som trekker sammen Bind 1, 2 og 3 til én omnibus. |

---

## 3. Kompilering og Bygging

For å rekompilere hele Omnibus-verket deterministisk:
```bash
cd BOKKANDIDATER/HOVEDVERKET_OMNIBUS_EN_BOK
python3 assemble_hovedverket_omnibus.py
python3 build_hovedverket_omnibus.py
xelatex -interaction=nonstopmode HOVEDVERKET_DEN_STORE_BOKEN_OMNIBUS.tex
```
