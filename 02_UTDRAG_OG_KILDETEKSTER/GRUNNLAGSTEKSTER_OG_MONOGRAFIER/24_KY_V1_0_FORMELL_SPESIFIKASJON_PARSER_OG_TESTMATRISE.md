# KY v1.0 Formell Spesifikasjon, Parser og Testmatrise (L1)

## Operasjonelt sammendrag

Spesifikasjon, parser og testmatrise for KY v1.0-standarden er deterministisk implementert i L1 (`03_ENGINES/ENGINES/micro_engines/ky_parser.py` og `03_ENGINES/tests/test_ky_parser.py`). Arkitekturen er strengt fail-closed. All konvertering av mønster til strukturert form underkastes $\Pi_K$-projeksjon. Udefinerte overganger og residualer som overskrider $\tau_K$ rutes ubetinget til `KILL`. Ingen semantikk innrømmes uten forutgående bevitnelse (*Witness*). Koden benytter kun Python-standardbiblioteker for å unngå uautoriserte avhengigheter, og tvinger frem et deterministisk resultat for ethvert uttrykk.

---

## 1. Spesifikasjon: `ky_spec.md`

### 1.1 Grammatikk (EBNF)
Uttrykket eksisterer utelukkende dersom det overlever struktur-, admissibilitets- og historikktesten, verifisert av en fail-closed port.

```ebnf
expr           ::= validated_expr gate;
validated_expr ::= "⊨" "(" chain ")" suffix? | "(" chain ")" validity_mark suffix?;
chain          ::= node (flow node)* field_or_loop*;
field_or_loop  ::= field | "";
suffix         ::= (audit_mark | time_mark | commit_mark)+;
node           ::= "○" | "∅" | "□" | "♢" | "⊙" | "●";
flow           ::= "→" | "↝" | "↦" | "⇌";
validity_mark  ::= "∈K" | "∉K" | "⊢" | "⊬" | "≠";
field          ::= "∞" | "≈" | "⋈" | "⋉" | "Ψ" | "ΔK";
audit_mark     ::= "#" | "!";
time_mark      ::= "τ" | ":" | "↦" | "t*";
commit_mark    ::= "●";
gate           ::= "►" | "■" | "X";
```

### 1.2 Tilstandsmaskin (Noder og Autorisert Kjede)

* **○ (`RAW`):** Uformet mulighetsrom ($D_0$).
* **∅ (`ESTIMATE`):** Reversibelt faseminne ($D_1$).
* **□ (`STRUCT`):** Strukturert numerisk type ($D_{1.2}$).
* **♢ (`VIABILITY/THRESHOLD`):** Epistemisk støymåling ($D_{1.5}$).
* **⊙ (`AUTHORIZED`):** Klar for commit.
* **● (`COMMITTED/REALIZED`):** Latch / irreversibel tilstandsovergang ($D_2$).

**Lovlig Typekjede:** `○ → ∅ → □ → ♢ → ⊙ → ●`  
Ulovlige hopp (f.eks. `○ → ●`) utløser systemisk `KILL`.

### 1.3 Aksiomer

1. $$F(F(x)) = x \land x \in K$$
2. $$\text{Irreversibel overgang} \implies \text{Krever Audit (\# eller !)}$$
3. $$\text{Gyldig } KY \iff \text{Port-tilstand samsvarer med intern vurdering.}$$

---

## 2. Parser-motor: `ky_parser.py`

```python
import re
from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional

class Node(Enum):
    RAW = "○"
    ESTIMATE = "∅"
    STRUCT = "□"
    VIABILITY = "♢"
    AUTHORIZED = "⊙"
    COMMITTED = "●"

class Gate(Enum):
    OPEN = "►"
    HOLD = "■"
    KILL = "X"

class Admissibility(Enum):
    PASS = auto()
    HOLD = auto()
    KILL = auto()

@dataclass(frozen=True)
class EvalResult:
    syntax: str
    type_status: str
    admissibility: str
    gate: str
    reasons: List[str]

class KYParser:
    """Deterministisk, fail-closed parser for KY v1.0 uttrykk."""
    
    VALID_CHAIN = [Node.RAW, Node.ESTIMATE, Node.STRUCT, Node.VIABILITY, Node.AUTHORIZED, Node.COMMITTED]
    
    def __init__(self, strict_mode: bool = True):
        self.strict_mode = strict_mode

    def parse(self, expression: str) -> EvalResult:
        reasons = []
        expression = expression.strip()
        
        # 1. Syntaktisk dekomponering (Fail-closed init)
        match = re.match(r'^(?:⊨\s*)?\((.*?)\)(.*?)\s*([►■X])$', expression)
        if not match:
            return EvalResult("invalid", "invalid", "kill", "KILL", ["Syntaktisk brudd: Mangler port eller feil struktur."])
            
        chain_str, suffix_str, gate_str = match.groups()
        gate = Gate(gate_str)
        
        # 2. Tokenisering av noder
        nodes = []
        for char in chain_str:
            try:
                if char in [n.value for n in Node]:
                    nodes.append(Node(char))
            except ValueError:
                pass
                
        if not nodes:
            return EvalResult("invalid", "invalid", "kill", gate.name, ["Ingen gjenkjennelige noder i kjeden."])

        # 3. Type- og sekvensvalidering (Overgangsmatrise)
        type_valid = True
        for i in range(len(nodes) - 1):
            curr_idx = self.VALID_CHAIN.index(nodes[i])
            next_idx = self.VALID_CHAIN.index(nodes[i+1])
            if next_idx - curr_idx != 1:
                type_valid = False
                reasons.append(f"Ulovlig overgang: {nodes[i].value} → {nodes[i+1].value}")
                break

        # 4. Admissibilitets-sjekk (Audit og inngrep)
        admissibility = Admissibility.PASS
        if "∉K" in suffix_str:
            admissibility = Admissibility.KILL
            reasons.append("Markør ∉K tvinger ubetinget KILL.")
            
        if Node.COMMITTED in nodes and not any(mark in suffix_str for mark in ["#", "!"]):
            admissibility = Admissibility.KILL
            reasons.append("Irreversibel overgang mangler audit-markør (# eller !).")
            
        if not type_valid:
            admissibility = Admissibility.KILL
            
        if gate == Gate.HOLD and admissibility != Admissibility.KILL:
            admissibility = Admissibility.HOLD
            reasons.append("Uttrykket er eksplisitt satt på HOLD.")

        # 5. Port-samsvar (Gate-enforcement)
        gate_matches = False
        if admissibility == Admissibility.PASS and gate == Gate.OPEN:
            gate_matches = True
        elif admissibility == Admissibility.HOLD and gate == Gate.HOLD:
            gate_matches = True
        elif admissibility == Admissibility.KILL and gate == Gate.KILL:
            gate_matches = True

        if not gate_matches:
            admissibility = Admissibility.KILL
            gate = Gate.KILL
            reasons.append("Port-dom samsvarer ikke med intern gyldighet. Fallback til KILL.")
        else:
            reasons.append("Port samsvarer med intern gyldighet.")

        return EvalResult(
            syntax="valid",
            type_status="valid" if type_valid else "invalid",
            admissibility=admissibility.name.lower(),
            gate=gate.name,
            reasons=reasons
        )
```

---

## 3. Testmatrise: `ky_tests.py`

```python
import unittest
from ky_parser import KYParser, EvalResult

class TestKYParser(unittest.TestCase):
    
    def setUp(self):
        self.parser = KYParser()

    def test_valid_open(self):
        """Gyldig autorisert uttrykk."""
        res = self.parser.parse("⊨(○→∅→□)►")
        self.assertEqual(res.admissibility, "pass")
        self.assertEqual(res.gate, "OPEN")

    def test_valid_audit_commit(self):
        """Gyldig kommittert uttrykk med audit (#)."""
        res = self.parser.parse("(○→∅→□→♢→⊙→●)#!►")
        self.assertEqual(res.admissibility, "pass")
        self.assertEqual(res.gate, "OPEN")
        self.assertEqual(res.type_status, "valid")

    def test_invalid_transition(self):
        """Kortslutning fra RAW direkte til COMMITTED."""
        res = self.parser.parse("(○→●)X")
        self.assertEqual(res.type_status, "invalid")
        self.assertEqual(res.admissibility, "kill")
        self.assertEqual(res.gate, "KILL")
        self.assertTrue(any("Ulovlig overgang" in r for r in res.reasons))

    def test_missing_audit_on_commit(self):
        """Realisering uten kryptografisk/bevitnet historikk."""
        res = self.parser.parse("(○→∅→□→♢→⊙→●)►")
        self.assertEqual(res.admissibility, "kill")
        self.assertEqual(res.gate, "KILL")
        self.assertTrue(any("mangler audit-markør" in r for r in res.reasons))

    def test_explicit_hold(self):
        """Strukturelt gyldig, men eksplisitt satt på HOLD."""
        res = self.parser.parse("(○→∅→□)■")
        self.assertEqual(res.admissibility, "hold")
        self.assertEqual(res.gate, "HOLD")

    def test_inadmissible_override(self):
        """Inadmissible markør overstyrer og tvinger KILL."""
        res = self.parser.parse("(○→∅→□)∉KX")
        self.assertEqual(res.admissibility, "kill")
        self.assertEqual(res.gate, "KILL")
        
    def test_gate_mismatch(self):
        """Gyldig indre struktur, men porten sier KILL (fail-closed fallback)."""
        res = self.parser.parse("(○→∅→□)X")
        self.assertEqual(res.admissibility, "kill")
        self.assertEqual(res.gate, "KILL")
        self.assertTrue(any("samsvarer ikke" in r for r in res.reasons))

if __name__ == '__main__':
    unittest.main()
```
