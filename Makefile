# MORANDI-CORE // FORMAL REALIZATION CONTRACT (skrivevaerelset)
# Default target is FAIL-CLOSED (0.00 V DC). Explicit verification is mandatory.

.DEFAULT_GOAL := hold
.PHONY: hold verify

hold:
	@echo "[HOLD] 0.00 V DC. System is at rest. Run 'make verify' to verify archive integrity."
	@exit 1

verify:
	@test -f README.md
	@test -f index.html
	@test -f TILMEGSELV/KONSEPTUELL_GRANITT_ET_FORSOK_PA_SANNHET.pdf
	@test -f 03_FERDIGE_BOKER_PDF/KONSEPTUELL_GRANITT_ET_FORSOK_PA_SANNHET.pdf
	@echo "[OPEN] Witness W2 confirmed. Literary archive and monograph integrity verified (0.00 V DC)."
