# BAMKS-D: Blockchain-Assisted Multi-Keyword Search with Dynamic Revocation & Attribute-Based Access Control

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Ethereum Sepolia](https://img.shields.io/badge/blockchain-Ethereum%20Sepolia-orange.svg)](https://sepolia.etherscan.io/)
[![IPFS Pinata](https://img.shields.io/badge/storage-IPFS%20%7C%20Pinata-teal.svg)](https://pinata.cloud/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**BAMKS-D** is a research prototype evaluating dynamic file-level operations and on-chain revocation mapping built upon the foundational scheme of Cheng et al. (*Internet of Things*, Elsevier, vol. 36, 2026). It integrates **Attribute-Based Access Control (CP-ABE)**, **Multi-Keyword Searchable Inverted Indexing**, and **Instant Single-Document Revocation** anchored on Ethereum Sepolia with decentralized IPFS storage.

---

## 🌟 Key Contributions & Features

1. **Atomic Single-Document Addition ($O(m)$)**:
   - Eliminates monolithic collection re-indexing when appending new records.
   - Computes tokens only for the $m$ keywords of the new document ($0.67 \pm 0.18$\,ms at $L=5,000$ files), achieving a **12.11$\times$ speedup** over Cheng et al. Section 5.10 index update and **3,527.7$\times$** over naive full re-encryption.

2. **Instant On-Chain Document Revocation ($O(1)$)**:
   - Implements direct EVM mapping storage (`mapping(uint256 => bool) deletedDocRegistry`).
   - Constant-time lookup via `keccak256(abi.encode(docId, slotNumber))` with zero array traversal.

3. **Public Verifiability via Ethereum Blockchain**:
   - Smart contracts on Ethereum Sepolia (`BAMKS_Registry.sol`) record document roots and enforce that revoked documents are rejected from search result sets.

4. **Decentralized Storage (IPFS / Pinata)**:
   - Large encrypted payloads (clinical records, telemetry streams, summaries) are stored off-chain on IPFS, with content hashes anchored immutably on-chain.

5. **Interactive Web Dashboard**:
   - Web application (`app.py`, `index.html`) demonstrating real-time clinical identity switching, file encryption, keyword search, IPFS uploads, and smart contract verification.

---

## 🏗️ System Architecture

```text
+-----------------------------------------------------------------------------------+
|                           Attribute Authority (AA)                                |
|                Generates Global Parameters & Distributes User Keys                 |
+-----------------------------------------------------------------------------------+
             |                                                  |
             v                                                  v
+-------------------------+                           +-------------------------+
|     Data Owner (DO)     |                           |     Data User (DU)      |
|  - Encrypts File (AES)  |                           |  - Generates Trapdoor   |
|  - Simulates CP-ABE     |                           |  - Submits Query        |
|  - Generates Index      |                           |  - Decrypts Result      |
+-------------------------+                           +-------------------------+
             |                                                  ^
             | (Encrypted Payload -> IPFS)                      |
             | (Keyword Index -> Cloud)                         |
             v                                                  |
+-----------------------------------------------------------------------------------+
|                          Cloud Service Provider (CSP)                             |
|               Stores Encrypted Indices & Executes Trapdoor Search Matches         |
+-----------------------------------------------------------------------------------+
                                         ^
                                         | Verification & Commitment Proofs
                                         v
+-----------------------------------------------------------------------------------+
|                           Ethereum Blockchain (Sepolia)                           |
|            BAMKS_Registry.sol: Verifies Index State, Roots & Revocations           |
+-----------------------------------------------------------------------------------+
```

---

## 🔗 Live Ethereum Sepolia Deployment & Verified Transactions

The `BAMKS_Registry.sol` smart contract is live and verified on the public Ethereum Sepolia Testnet:

- **Contract Address:** [`0xfDC8615Bf6483c3B0f39c330F55A56Cb0f08C8D3`](https://sepolia.etherscan.io/address/0xfDC8615Bf6483c3B0f39c330F55A56Cb0f08C8D3)
- **Deployment Tx Hash:** [`0x1f058bde75b20c2d1ce513897d77d70f47a2951cbcc83d9bc45a573116bf0dbf`](https://sepolia.etherscan.io/tx/0x1f058bde75b20c2d1ce513897d77d70f47a2951cbcc83d9bc45a573116bf0dbf)
- **Deployment Block:** #11975268 (Gas Used: 6,889,229)
- **Registration Tx Hash (`registerDocument`):** [`0x363d3e8867adb49a2657b798ebb26990a5d0011ec5ddaf7de267ff191dc40ad7`](https://sepolia.etherscan.io/tx/0x363d3e8867adb49a2657b798ebb26990a5d0011ec5ddaf7de267ff191dc40ad7)
  - Confirmed in Block #11975277 | Gas Used: 792,245 | Latency: 35.22 s
- **Deletion Tx Hash (`deleteDocument`):** [`0x008330a08b3ad8926b19de8dc0a1b386b95712dc55077e33df2a36685c876e8d`](https://sepolia.etherscan.io/tx/0x008330a08b3ad8926b19de8dc0a1b386b95712dc55077e33df2a36685c876e8d)
  - Confirmed in Block #11975278 | Gas Used: 242,834 | Latency: 21.83 s
- **Network:** Ethereum Sepolia (Chain ID: `11155111`)

---

## 📂 Repository Structure

```
BAMKS/
├── contracts/
│   ├── BAMKS_Registry.sol         # Solidity smart contract with EVM modExp & RVSC
│   └── build/                     # Compiled ABI & EVM bytecode
├── src/
│   ├── bamks_system.py            # BAMKS core setup, encryption, trapdoor, search
│   ├── crypto_utils.py            # 256-bit prime fields, KDF, hash functions
│   ├── dynamic_extension.py       # Dynamic single-doc update & revocation
│   └── ipfs_storage.py            # Pinata IPFS decentralized integration client
├── diagrams/                      # System architecture, charts & benchmark results
├── sample_inputs/                 # Clinical records suite (.txt, .json, .csv, .md)
├── app.py                         # Flask web application & REST API
├── deploy_sepolia.py              # Ethereum Sepolia smart contract deployment script
├── test_demo.py                   # Full end-to-end cryptographic demo & benchmarks
├── test_correctness_and_security.py # Cryptographic correctness & security test suite
├── proof_of_o1_complexity.py      # Benchmark proving O(1) EVM storage mapping complexity
├── generate_scalability_graph.py  # Multi-N fair scalability plotting
├── index.html                     # Soft, minimal dashboard frontend
├── requirements.txt               # Python package dependencies
├── .env.example                   # Environment variable template
└── README.md                      # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10 or higher (Tested on Python 3.11.9, 13th Gen Intel Core i5-13420H, 16 GB RAM)
- Git

### 2. Clone Repository
```bash
git clone https://github.com/Prashant8991/BAMKS.git
cd BAMKS
```

### 3. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 4. Configuration
Create your `.env` file by copying `.env.example`:
```bash
cp .env.example .env
```
Configure your `.env` parameters:
- `SEPOLIA_RPC_URL`: Ethereum Sepolia node endpoint
- `SEPOLIA_PRIVATE_KEY`: Testnet wallet private key (never use mainnet funds)
- `SEPOLIA_CONTRACT_ADDRESS`: `0xfDC8615Bf6483c3B0f39c330F55A56Cb0f08C8D3`
- `PINATA_API_KEY` & `PINATA_API_SECRET` / `PINATA_JWT`: Pinata IPFS credentials

---

## 🧪 Running Experiments & Benchmarks

### Run the Interactive Web Dashboard
```bash
python app.py
```
Open your browser at `http://localhost:5000` to interact with:
- Clinical identity switching (Cardiology, Oncology, Neurology, General Ward)
- Single-record & multi-file batch upload (`sample_inputs/`)
- Real-time document encryption and IPFS upload
- Multi-keyword search queries
- Dynamic attribute revocation simulation

### Run Cryptographic Demonstration
```bash
python test_demo.py
```

### Run Correctness Test Suite
```bash
python test_correctness_and_security.py
```

### Run Fair Multi-N Scalability Benchmark
```bash
python generate_scalability_graph.py
```

### Verify O(1) EVM Storage Deletion Complexity
```bash
python proof_of_o1_complexity.py
```

---

## ⚖️ Prototype Scope & Limitations

This implementation is an academic research prototype focused on dynamic file update mechanics and EVM state revocation:
- **Algebraic Simulation:** Field arithmetic is evaluated in $(\mathbb{Z}_P^*, \cdot)$ using $P = 2^{256} - 2^{32} - 977$. Bilinear pairings are simulated via exponentiation.
- **Search Function:** The demonstration search script utilizes group parameters directly to evaluate inverted index mechanics.
- **Access Patterns:** As with standard inverted index architectures, search access patterns and keyword frequencies are visible to the CSP.
- **Policy Enforcement:** Access structure satisfaction is demonstrated through attribute set matching.
- **Dataset:** 8 synthetic clinical records authored to demonstrate multi-format EHR workflows.

---

## 👥 Authors & Contributors

- **Prashant Singh** ([@Prashant8991](https://github.com/Prashant8991)) — Cryptographic Engine, Dynamic Algorithms, Dashboard & Evaluation
- **Adak Rushikesh** ([@rushikeshadak6-git](https://github.com/rushikeshadak6-git)) — Solidity Smart Contracts, Blockchain Layer & EVM Benchmarks
