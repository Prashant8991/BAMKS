# BAMKS-D: Blockchain-Assisted Multi-Keyword Search with Dynamic Revocation & Attribute-Based Encryption

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Ethereum Sepolia](https://img.shields.io/badge/blockchain-Ethereum%20Sepolia-orange.svg)](https://sepolia.etherscan.io/)
[![IPFS Pinata](https://img.shields.io/badge/storage-IPFS%20%7C%20Pinata-teal.svg)](https://pinata.cloud/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**BAMKS-D** is a cryptographic healthcare and enterprise data-sharing framework combining **Ciphertext-Policy Attribute-Based Encryption (CP-ABE)**, **Blockchain-Assisted Multi-Keyword Searchable Encryption (BAMKS)**, and **Dynamic User Revocation** with decentralized IPFS storage.

---

## 🌟 Key Features

1. **Multi-Keyword Searchable Encryption (BAMKS)**:
   - Search across encrypted medical records without revealing plaintexts or search queries to cloud servers.
   - Constant-time $O(1)$ search complexity verification over inverted keyword indices.

2. **Fine-Grained Access Control (CP-ABE)**:
   - Expressive access policies (e.g., `(Role_Doctor AND Dept_Cardiology)`).
   - Only data users holding matching attribute private keys can reconstruct decryption parameters.

3. **Dynamic User & Attribute Revocation**:
   - Immediate revocation of compromised or departing personnel without re-encrypting the entire cloud database.
   - Dynamic parameter updates synchronized through blockchain state.

4. **Public Verifiability via Ethereum Blockchain**:
   - Smart contracts on Ethereum (`BAMKS_Registry.sol` on Sepolia Testnet) record verifiable cryptographic commitments and index state roots, preventing dishonest cloud servers from returning partial or forged search results.

5. **Decentralized Storage (IPFS / Pinata)**:
   - Large encrypted payloads (EHRs, imaging, clinical notes) are stored off-chain on IPFS, with content hashes anchored immutably on-chain.

6. **Interactive Web Dashboard**:
   - Modern web UI (`app.py`, `index.html`) demonstrating real-time identity switching, file encryption, keyword search, IPFS uploads, and smart contract verification.

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
|  - Encrypts Key (CP-ABE)|                           |  - Submits Query        |
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

## 📂 Repository Structure

```
BAMKS/
├── contracts/
│   ├── BAMKS_Registry.sol         # Solidity smart contract for Sepolia
│   └── build/                     # Compiled contract ABI and bytecode
├── src/
│   ├── bamks_system.py            # BAMKS core setup, encryption, trapdoor, search
│   ├── crypto_utils.py            # 256-bit prime fields, KDF, hash functions
│   ├── dynamic_extension.py       # Dynamic single-doc update & revocation
│   └── ipfs_storage.py            # Pinata IPFS integration client
├── diagrams/                      # System architecture, charts & flow diagrams
├── app.py                         # Flask web application & REST API
├── deploy_sepolia.py              # Ethereum Sepolia smart contract deployment script
├── test_demo.py                   # Full end-to-end cryptographic demo test
├── proof_of_o1_complexity.py      # Benchmark proving O(1) search complexity
├── index.html                     # Interactive dashboard frontend
├── requirements.txt               # Python package dependencies
├── .env.example                   # Environment variable template
└── README.md                      # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10 or higher
- Node.js / MetaMask wallet (for Sepolia interaction, optional)
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
Fill in your configuration details inside `.env`:
- `SEPOLIA_RPC_URL`: Ethereum Sepolia node endpoint (default public RPC provided)
- `SEPOLIA_PRIVATE_KEY`: Testnet wallet private key (never use mainnet funds)
- `PINATA_API_KEY` & `PINATA_API_SECRET` / `PINATA_JWT`: Optional Pinata IPFS credentials

---

## 🧪 Running the System

### Run the Interactive Web Dashboard
```bash
python app.py
```
Open your browser at `http://localhost:5000` to interact with:
- Clinical identity switching (Cardiology, Oncology, Neurology, General Ward)
- Real-time document encryption and IPFS upload
- Verifiable multi-keyword search queries
- Dynamic attribute revocation simulation

### Run Cryptographic Demonstration & Test Suite
```bash
python test_demo.py
```

### Verify $O(1)$ Search Complexity
```bash
python proof_of_o1_complexity.py
```

### Deploy / Verify Smart Contract on Sepolia Testnet
```bash
python deploy_sepolia.py
```

---

## 🔐 Security & Safe Practices

- **Never commit `.env` or your private keys**: The repository includes `.gitignore` to prevent secret leaks.
- Always use a dedicated testnet wallet with zero real funds for Sepolia testing.

---

## 👥 Authors & Contributors

- **Prashant Singh** ([@Prashant8991](https://github.com/Prashant8991)) — Cryptographic Engine, CP-ABE, Dynamic Algorithms & REST API
- **Adak Rushikesh** ([@rushikeshadak6-git](https://github.com/rushikeshadak6-git)) — Solidity Smart Contracts, Blockchain Layer & EVM Benchmarks

