# Telemetry Discrepancy Estimator for Regional Publishers

> Estimate pageview discrepancies between first-party server logs and client analytics. A discrepancy is not proof of ad-blocking or revenue loss.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CLI_SCRIPT](https://img.shields.io/badge/Format-CLI--SCRIPT-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Build an open-source telemetry discrepancy estimator: 1) an optional same-origin pageview beacon that sends only after explicit analytics consent, 2) a Python log analyzer that compares server and client event counts, and 3) guidance for interpreting discrepancies. Differences may result from consent choices, JavaScript failures, sampling, caching, bots, or blockers; the tool cannot identify the cause by itself.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `docs/reverse-proxy-guide.md`
- `examples/sample_access_logs.txt`
- `LICENSE`
- `README.md`
- `reports/loss_analysis.html`
- `src/audit_loss.py`
- `src/beacon_test.js` (Node tests for consent and same-origin safeguards)
- `src/telemetry_beacon.js`
- `src/telemetry_loss_estimator.py`
- `tests/test_audit.py`
- `tests/test_estimator.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/audit_loss.py --help
```

### Interactive Browser Tool
Open `reports/loss_analysis.html` directly in your web browser (Chrome, Edge, Safari) to use the local interactive calculator or dashboard. Operates 100% client-side with zero external network calls.

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "reporting",
  "repository": "ad-blocker-telemetry-loss-estimator",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Consent-Gated Beacon:** Sends a minimal pageview event to a configured same-origin endpoint only when the host page explicitly sets `window.__analyticsConsent = true`. It does not attempt to evade blockers or identify a person.
- **Interpretation:** Do not infer regional ad-blocker penetration from the sample logs. Use consented, account-specific measurements and describe the result as a tracking discrepancy unless the cause is independently established.
- **Privacy Respect:** Script strictly measures aggregated loss metrics without tracking personal identifiers or circumventing client browser privacy settings.

---

## 📚 Primary Documentation & Verifiable References

- [IAB Tech Lab: Ad Blocking Measurement Guidelines](https://iabtechlab.com/) - Industry standards for assessing ad blocking impact and measurement loss.
- [W3C Beacon API Specification](https://www.w3.org/TR/beacon/) - Asynchronous lightweight telemetry standard for web browsers.
- [Brave Software / Privacy Standards](https://brave.com/) - Technical documentation on client-side content filtering mechanics.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
