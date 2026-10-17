# BIND II: CODEX GEOCYBERNETICA (LITISK KYBERNETIKK LEKSIKON)

*Fra samlingen som overlevde brente jords taktikk. De tekniske bladene er skåret ut; kun den litterære stammen står igjen.*

---

### *Fysikk for Metafysikk: Det Litisk-Kybernetiske Leksikon og de 7 Syntetiske Kapslene*

```text
========================================================================================
HOVEDVERKET // BIND II AV TRILOGIEN:
  Verk              : CODEX GEOCYBERNETICA (Litisk Kybernetikk Leksikon)
  Forfatter         : Torjusen, Marius Egerhei (ORCID: 0009-0006-0431-6637)
  Lokus             : BOKKANDIDATER/BIND_2_FYSIKK_FOR_METAFYSIKK/
  Format            : Monumentalt Leksikonformat (To-spalters A4 med plansjer)
  Sidetall / Omfang : 179 sider A4 / 18 371 linjer (44 Moduler)
  Master-PDF        : litisk_kybernetikk_leksikon.pdf (9.6 MB)
  Kildemanuskript   : CODEX_GEOCYBERNETICA_MASTER_MANUSKRIPT.md
  Målgruppe         : Fysikere, kybernetikere, matematikere, systemarkitekter
========================================================================================
```

---

## 1. Verkets Kjerne og Formål

*Codex Geocybernetica* er Bind II i **Hovedverket**. Boken er utformet som et monumentalt leksikon og oppslagsverk over den litiske kybernetikken:

* **44 Leksikonmoduler:** Strukturerte oppslag over termodynamikk, anortositt, symplektiske faserom, Landauer-stasis og kognitiv arkitektur.
* **De 7 Syntetiske Kapslene:** De formelle, ugjennomtrengelige forankringspunktene som binder programvare og teori til det litiske grunnfjellet.
* **Matematisk og fysisk presisjon:** Formler, tensor-kjerner og operasjonelle protokoller for uforfalskbar vitneførsel.

---

## 2. Filkatalog

| Fil | Størrelse / Omfang | Beskrivelse |
|---|---|---|
| [`litisk_kybernetikk_leksikon.pdf`](litisk_kybernetikk_leksikon.pdf) | 179 s A4 / 9.6 MB | Ferdig to-spalters leksikon-PDF med fullt apparat. |
| [`CODEX_GEOCYBERNETICA_MASTER_MANUSKRIPT.md`](CODEX_GEOCYBERNETICA_MASTER_MANUSKRIPT.md) | 18 371 linjer / 459 KB | Det samlede kanoniske kildemanuskriptet. |
| [`litisk_kybernetikk_leksikon.tex`](litisk_kybernetikk_leksikon.tex) | 560 KB | LaTeX-kildekode for to-spalters akademisk praktsetting. |
| [`00_LEKSIKON_MODULINDEKS.md`](00_LEKSIKON_MODULINDEKS.md) | 19 KB | Komplett modulindeks over samtlige 44 leksikonmoduler. |
| [`FYSIKK_FOR_METAFYSIKK_BOK_1.md`](FYSIKK_FOR_METAFYSIKK_BOK_1.md) | 502 KB | Det opprinnelige grunnlagsmanuskriptet (Fysikk for metafysikk). |
| [`build_litisk_kybernetikk_leksikon.py`](build_litisk_kybernetikk_leksikon.py) | 17 KB | Kompileringsskript for generering av leksikon-PDF. |
| [`assemble_bind2_clean.py`](assemble_bind2_clean.py) | 24 KB | Sammenstillingsskript for kildetekster og moduler. |

---

## 3. Kompilering og Bygging

For å rekompilere leksikonet deterministisk fra terminalen:
```bash
cd BOKKANDIDATER/BIND_2_FYSIKK_FOR_METAFYSIKK
python3 build_litisk_kybernetikk_leksikon.py
xelatex -interaction=nonstopmode litisk_kybernetikk_leksikon.tex
```
