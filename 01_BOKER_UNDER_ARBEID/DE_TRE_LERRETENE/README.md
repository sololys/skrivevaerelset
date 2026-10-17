# DE TRE LERRETENE (THE THREE CANVASES)

*Fra samlingen som overlevde brente jords taktikk. De tekniske bladene er skåret ut; kun den litterære stammen står igjen.*

---

### *Et Filosofisk og Kausalt Manifest over Bruddet, Asynkroniteten og Banens Ensomhet*

```text
========================================================================================
MANIFEST & SAKPROSAKANDIDAT:
  Verk              : DE TRE LERRETENE: Bruddet, Asynkroniteten og Banens Ensomhet
  Forfatter         : Torjusen, Marius Egerhei (ORCID: 0009-0006-0431-6637)
  Lokus             : BOKKANDIDATER/DE_TRE_LERRETENE/
  Format            : Kompakt Bokformat (155 x 230 mm)
  Sidetall / Omfang : 22 sider / 3.0 MB PDF
  Master-PDF        : de_tre_lerretene_bok.pdf
  Manuskript        : MANUSKRIPT_DE_TRE_LERRETENE.md / THE_THREE_CANVASES_MASTER_MONOGRAPH.md
========================================================================================
```

---

## 1. Verkets Kjerne og Formål

*De Tre Lerretene* er et kort, kraftfullt filosofisk manifest som danner en estetisk og eksistensiell bro for Hovedverket. Verket analyserer tre fundamentale lerreter i menneskets erkjennelse:

1. **Det Første Lerretet (Bruddet):** Den opprinnelige friksjonen og adskillelsen fra det ubevisste.
2. **Det Andre Lerretet (Asynkroniteten):** Tidsforsinkelsen, radioskyggen og avstanden der tanken må modnes uten ytre bekreftelse.
3. **Det Tredje Lerretet (Banens Ensomhet):** Menneskets uunngåelige alenegang langs sin egen kausale bane før porten åpnes eller kutter.

---

## 2. Filkatalog

| Fil | Størrelse / Omfang | Beskrivelse |
|---|---|---|
| [`de_tre_lerretene_bok.pdf`](de_tre_lerretene_bok.pdf) | 22 s / 3.0 MB | Fullt illustrert, trykkeklar prakt-PDF i format 155 x 230 mm. |
| [`MANUSKRIPT_DE_TRE_LERRETENE.md`](MANUSKRIPT_DE_TRE_LERRETENE.md) | 14 KB | Det norske kildemanuskriptet for manifestet. |
| [`THE_THREE_CANVASES_MASTER_MONOGRAPH.md`](THE_THREE_CANVASES_MASTER_MONOGRAPH.md) | 37 KB | Full engelsk monografiversjon av verket. |
| [`de_tre_lerretene_bok.tex`](de_tre_lerretene_bok.tex) | 18.6 KB | LaTeX-kildekode for typografisk boksetting. |
| [`build_de_tre_lerretene_bok.py`](build_de_tre_lerretene_bok.py) | 12.5 KB | Kompileringsskript for generering av LaTeX og PDF. |

---

## 3. Kompilering og Bygging

For å rekompilere manifestet:
```bash
cd BOKKANDIDATER/DE_TRE_LERRETENE
python3 build_de_tre_lerretene_bok.py
xelatex -interaction=nonstopmode de_tre_lerretene_bok.tex
```
