#!/usr/bin/env python3
"""Fail-closed public surface and monograph parity gate for sololys/skrivevaerelset."""

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

EXPECTED_GRANITT_SHA = "e3d49d466212cff631cb793583e779bd4833d5240c7236c6bb3629150cd03668"
GRANITT_PDFS = (
    "KONSEPTUELL_GRANITT_ET_FORSOK_PA_SANNHET.pdf",
    "03_FERDIGE_BOKER_PDF/KONSEPTUELL_GRANITT_ET_FORSOK_PA_SANNHET.pdf",
    "TILMEGSELV/KONSEPTUELL_GRANITT_ET_FORSOK_PA_SANNHET.pdf",
    "TILMEGSELV/TILMEGSELV_MONOGRAFI.pdf",
)
REQUIRED_SURFACE = ("README.md", "index.html", "CITATION.cff", ".zenodo.json")
BIN_EXTS = {".pdf", ".png", ".jpg", ".jpeg", ".webp", ".svg", ".woff", ".woff2", ".ttf", ".otf"}

LEAK_RE = re.compile(
    r"(/home/sololyset|file://|(?i:gemini-core)|pods-sovereign-bioreactors|"
    r"00_KANONISK_KJERNE|00_INTERKOGNITIV|01_CANONICAL_SCHEMAS|01_HARDWARE_RTL|"
    r"02_PROTOCOLS|03_ENGINES|04_REALITY_FORGE(?!_OG_MOTORER)|05_PATENTS|"
    r"06_RESEARCH|07_BOKHYLLA|08_ACTIVE_BIDS|09_SYSTEM|CARBON/)"
)
PUBLIC_SOLOLYS = {
    "sololys",
    "sololys_profile",
    "skrivevaerelset",
    "epistemic-architectures",
    "epistemic-architectures-notes",
    "ky-rox-public-demonstrators",
    "monolitt",
}
MD_LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    self_rel = str(Path(__file__).resolve().relative_to(root))
    errors: list[str] = []

    for req in REQUIRED_SURFACE:
        if not (root / req).is_file():
            errors.append(f"Missing required surface file: {req}")

    for rel_pdf in GRANITT_PDFS:
        p = root / rel_pdf
        if not p.is_file():
            errors.append(f"Missing monograph PDF: {rel_pdf}")
            continue
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        if digest != EXPECTED_GRANITT_SHA:
            errors.append(f"SHA-256 mismatch on {rel_pdf}: got {digest}, expected {EXPECTED_GRANITT_SHA}")

    zj = json.loads((root / ".zenodo.json").read_text(encoding="utf-8"))
    cff = (root / "CITATION.cff").read_text(encoding="utf-8")
    if zj.get("doi") != "10.5281/zenodo.24032522" or 'doi: "10.5281/zenodo.24032522"' not in cff:
        errors.append("DOI mismatch between .zenodo.json and CITATION.cff (expected 10.5281/zenodo.24032522)")
    if zj.get("license") != "CC-BY-ND-4.0" or 'license: "CC-BY-ND-4.0"' not in cff:
        errors.append("License mismatch between .zenodo.json and CITATION.cff (expected CC-BY-ND-4.0)")

    checked_text_files = 0
    checked_links = 0

    for p in sorted(root.rglob("*")):
        if ".git" in p.parts or not p.is_file() or p.suffix.lower() in BIN_EXTS:
            continue
        rel = str(p.relative_to(root))
        if rel == self_rel:
            continue
        checked_text_files += 1
        txt = p.read_text(encoding="utf-8", errors="replace")

        for idx, ln in enumerate(txt.splitlines(), 1):
            m_leak = LEAK_RE.search(ln)
            if m_leak:
                errors.append(f"Path/identity leak {m_leak.group(0)!r} in {rel}:{idx}")
            for um in re.finditer(r"github\.com/sololys/([A-Za-z0-9_.-]+)", ln):
                slug = um.group(1).rstrip(".,;:)")
                if slug not in PUBLIC_SOLOLYS:
                    errors.append(f"Non-public repo URL ({slug}) in {rel}:{idx}")

        if p.suffix.lower() == ".html":
            for idx, ln in enumerate(txt.splitlines(), 1):
                for hm in re.finditer(r'(?:href|src)="([^"]+)"', ln):
                    u = hm.group(1)
                    if u.startswith(("http://", "https://", "mailto:", "#", "data:", "javascript:")):
                        continue
                    checked_links += 1
                    clean = unquote(u.split("#", 1)[0].split("?", 1)[0])
                    if not clean:
                        continue
                    cand = (root / clean.lstrip("/")) if clean.startswith("/") else (p.parent / clean)
                    try:
                        res = cand.resolve()
                        ok = res.exists() and (res == root or root in res.parents)
                    except Exception:
                        ok = False
                    if not ok:
                        errors.append(f"Broken HTML link in {rel}:{idx} -> {u}")

        elif p.suffix.lower() == ".md":
            in_fence = False
            for idx, ln in enumerate(txt.splitlines(), 1):
                if ln.strip().startswith("```"):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                for m in MD_LINK_RE.finditer(ln):
                    target = m.group(3).strip("<>")
                    if target.startswith(("http://", "https://", "mailto:", "#", "javascript:")):
                        continue
                    checked_links += 1
                    clean = unquote(target.split("#", 1)[0].split("?", 1)[0])
                    if not clean:
                        continue
                    cand = (root / clean.lstrip("/")) if clean.startswith("/") else (p.parent / clean)
                    try:
                        res = cand.resolve()
                        ok = res.exists() and (res == root or root in res.parents)
                    except Exception:
                        ok = False
                    if not ok:
                        errors.append(f"Broken Markdown link in {rel}:{idx} -> {target}")

    if errors:
        print(f"[MORANDI_GATE=KILL // 0.00 V DC] {len(errors)} violation(s) detected:")
        for err in errors[:30]:
            print(f"  - {err}")
        return 1

    print(
        f"MORANDI_PUBLIC_SURFACE=PASS "
        f"(text_files={checked_text_files}, local_links={checked_links}, leaks=0, broken_links=0)"
    )
    print(f"KONSEPTUELL_GRANITT_PARITY=PASS (4/4 copies == {EXPECTED_GRANITT_SHA[:16]}...)")
    print(
        "[L1_VERIFIED // HOLD_READY_FOR_W2] L1 software checks passed "
        "(PHYSICAL_AUTHORITY=NONE; W_human required for W2). "
        "Literary archive and monograph integrity verified (0.00 V DC)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
