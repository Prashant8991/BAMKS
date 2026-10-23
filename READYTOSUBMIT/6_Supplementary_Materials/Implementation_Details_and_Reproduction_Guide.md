# Supplementary Material 3: Implementation Details & Reproduction Guide

## 1. Environment & Dependencies
The entire BAMKS-D cryptographic engine and benchmark suite is built in Python 3.11 with standard, cross-platform dependencies:

```bash
# Core Dependencies
pip install flask flask-cors pycryptodome web3 python-dotenv
# Documentation & Analysis Dependencies
pip install reportlab python-pptx python-docx pymupdf matplotlib
```

---

## 2. Cryptographic Parameters Setup
- **Cyclic Group Order:** 256-bit prime (secp256k1 field prime, as used in `crypto_utils.py`):
  $$P = 2^{256} - 2^{32} - 977 = \texttt{0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F}$$
- **Generator ($g$):** $g = 2 \in \mathbb{Z}_P^*$
- **Master Exponents:** $\mu, \gamma \in_R \mathbb{Z}_P^*$, Collection Shared Exponent $\eta \in_R \mathbb{Z}_{P-1}^*$
- **Symmetric Encryption:** AES-256-GCM authenticated encryption (128-bit authentication tag, 96-bit random nonce) via PyCryptodome.
- **Key Derivation Function:** SHA-256 of concatenated `Phi` and `version_id`:
  $$\text{sym\_key} = \text{SHA256}(\Phi \| version\_id)$$

---

## 3. Step-by-Step Reproduction Guide (Under 60 Seconds)

### Step 1: Run End-to-End Cryptographic Demo & Bug Fix Tests
Executes setup, CP-ABE key generation with fresh randomness $t$, zero-leakage search via Equation (9), off-chain Schnorr NIZK verification, and live benchmark comparisons:
```powershell
python test_demo.py
```
*Expected Result:* Exit code `0`. All 4 phases pass. Output logs confirm up to $3,934\times$ speedup.

### Step 2: Run Correctness & Security Test Suite
Executes 5 automated security assertions (soundness under wrong trapdoors, on-chain revocation invariant, CP-ABE unauthorized denial, and linear index storage scaling):
```powershell
python test_correctness_and_security.py
```
*Expected Result:* `ALL 5 CORRECTNESS & SECURITY TESTS PASSED PERFECTLY!`

### Step 3: Verify Solidity $O(1)$ Deletion Complexity & EVM Gas Invariance
Executes the empirical and mathematical regression benchmark across $N \in [10, 50000]$ records:
```powershell
python proof_of_o1_complexity.py
```
*Expected Result:* Linear regression confirms $dGas/dN = 0.000000$ and $dTime/dN = +0.000000\,\mu\text{s/record}$.

### Step 4: Launch Interactive Web Application & Clinician Workstation
```powershell
python app.py
```
*Expected Result:* Server active at `http://127.0.0.1:5000`. Supports clinical role switching, single & batch EHR upload, zero-leakage multi-keyword search, and smart contract ledger inspection.
