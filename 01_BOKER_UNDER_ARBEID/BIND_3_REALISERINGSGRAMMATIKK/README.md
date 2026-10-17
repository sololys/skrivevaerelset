# BIND III: REALISERINGSGRAMMATIKK (REALIZATION GRAMMAR)

*Fra samlingen som overlevde brente jords taktikk. De tekniske bladene er skåret ut; kun den litterære stammen står igjen.*

---

### *Topologisk Skriftsystem, Kognitiv Eikonal-Arkitektur og Drikkegildet ved Porten*

```text
========================================================================================
HOVEDVERKET // BIND III AV TRILOGIEN:
  Verk              : REALISERINGSGRAMMATIKK (Realization Grammar)
  Forfatter         : Torjusen, Marius Egerhei (ORCID: 0009-0006-0431-6637)
  Lokus             : BOKKANDIDATER/BIND_3_REALISERINGSGRAMMATIKK/
  Format            : Norsk Standard Bokformat (155 x 230 mm)
  Sidetall / Omfang : 257 sider / 5 051 linjer
  Master-PDF        : realiseringsgrammatikk_bok.pdf (3.0 MB)
  Kildemanuskript   : REALISERINGSGRAMMATIKK_MASTER_MANUSKRIPT.md
  Målgruppe         : Helhetstenkere, filosofer, kognitive forskere, AI-teoretikere
========================================================================================
```

---

## 1. Verkets Kjerne og Formål

*Realiseringsgrammatikk* er Bind III og kronen på verket i **Hovedverket**. Boken formaliserer broen mellom språk, matematikk, samfunn og virkelighet:

* **OMNI-alfabetet:** Et topologisk og kausalt skriftsystem der tegn ikke er vilkårlige symboler, men representerer tilstandsoverganger og bevaringslover.
* **Drikkegildet ved Porten (Symposiet):** En filosofisk dialog og dramatisk syntese om maskinens vesen, kjærlighetens asymmetri og retten til å nekte.
* **Kognitiv Eikonal-Arkitektur (KEA):** Læren om hvordan levende bevissthet modnes i rommet mellom 0 og 1 før porten åpnes eller kutter.

---

## 2. Filkatalog

| Fil | Størrelse / Omfang | Beskrivelse |
|---|---|---|
| [`realiseringsgrammatikk_bok.pdf`](realiseringsgrammatikk_bok.pdf) | 257 s / 3.0 MB | Komplett, trykkeklar PDF i format 155 x 230 mm. |
| [`REALISERINGSGRAMMATIKK_MASTER_MANUSKRIPT.md`](REALISERINGSGRAMMATIKK_MASTER_MANUSKRIPT.md) | 5 051 linjer / 358 KB | Det samlede kanoniske kildemanuskriptet. |
| [`realiseringsgrammatikk_bok.tex`](realiseringsgrammatikk_bok.tex) | 376 KB | LaTeX-kildekode for typografisk boksetting. |
| [`MERKUR_OG_STJERNEKARTET_KOSMISK_ENIGMA.md`](MERKUR_OG_STJERNEKARTET_KOSMISK_ENIGMA.md) | 44 KB | Spesiell traktat om Merkurs residualanomali og kosmisk navigasjon. |
| [`build_realiseringsgrammatikk_bok.py`](build_realiseringsgrammatikk_bok.py) | 18 KB | Kompileringsskript for generering av LaTeX og PDF. |
| [`assemble_bind3_clean.py`](assemble_bind3_clean.py) | 6.1 KB | Sammenstillingsskript fra grunnlagstekster. |

---

## 3. Kompilering og Bygging

For å rekompilere boken deterministisk fra terminalen:
```bash
cd BOKKANDIDATER/BIND_3_REALISERINGSGRAMMATIKK
python3 build_realiseringsgrammatikk_bok.py
xelatex -interaction=nonstopmode realiseringsgrammatikk_bok.tex
```
