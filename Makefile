# MORANDI-CORE // FORMAL REALIZATION CONTRACT (skrivevaerelset)
# Default target is FAIL-CLOSED (0.00 V DC). Explicit verification is mandatory.

.DEFAULT_GOAL := hold
.PHONY: hold verify

hold:
	@echo "[HOLD] 0.00 V DC. System is at rest. Run 'make verify' to verify archive integrity."
	@exit 1

verify:
	@python3 -B 05_BYGGEVERKTOY_OG_ARKIV/verify_public_surface.py
