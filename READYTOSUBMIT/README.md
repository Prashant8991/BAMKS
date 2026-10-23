# BAMKS-D: Final Review 3 Submission Package
**Course:** BCSE309L — Cryptography and Network Security  
**Institution:** School of Computer Science & Engineering (SCOPE), Vellore Institute of Technology (VIT), Chennai  
**Faculty Guide:** Prof. Karthika V  

### Student Authors
- **Prashant Singh** (Reg. No: 24BYB1042)
- **Adak Rushikesh** (Reg. No: 24BYB1055)

---

## 1. Submission Package Overview

This directory contains the complete and final set of deliverables for **Review 3** for our project:
**"BAMKS-D: Enabling Dynamic File-Level Operations in Blockchain-Assisted Attribute-Based Multi-Keyword Search for Cloud-Edge-IoT"**
*(Resolving the Section 8 Open Research Challenge of Cheng et al., Elsevier Internet of Things, 2026)*

```
READYTOSUBMIT/
├── 1_Presentation_PPT/
│   └── BAMKS_D_Final_Presentation.pptx          # 16-Slide Final Review 3 Presentation (Widescreen 16:9)
├── 2_Research_Paper_Word/
│   ├── IEEE_BAMKS_D_Research_Paper.docx         # Our Complete Research Paper (6,492 Words, Editable Word Document)
│   └── Base_Research_Paper_Cheng_et_al_2026.docx # Foundational Base Paper (Cheng et al., 2026, 23 Pages, Editable Word Document)
├── 3_Research_Paper_PDF/
│   ├── IEEE_BAMKS_D_Research_Paper.pdf          # Our Complete Research Paper (13 Pages, Camera-Ready IEEE Format)
│   └── Cheng_et_al_2026_Base_Research_Paper_BAMKS.pdf # Original Base Research Paper (Elsevier Internet of Things, 23 Pages)
├── 4_Research_Paper_LaTeX/
│   └── IEEE_BAMKS_D_Research_Paper.tex          # Complete LaTeX Source Code (IEEEtran Class)
├── 5_Source_Code/
│   └── BAMKS_D_Complete_Source_Code.zip         # Full Portable Functional Codebase, Smart Contracts & Datasets (5.2 MB)
└── 6_Supplementary_Materials/
    ├── Additional_Experimental_Results.md       # Empirical Benchmark Tables & Speedup Analysis
    ├── Dataset_Details_and_Links.md             # Clinical EHR Corpus Specifications, Schemas & Standards
    ├── Implementation_Details_and_Reproduction_Guide.md # Step-by-Step Reproduction Instructions
    ├── Web3_Sepolia_and_IPFS_Audit_Proof.md     # Verified Ethereum Sepolia Smart Contract & IPFS Proof
    ├── benchmark_fair_results.csv               # Raw Empirical Benchmark Results (CSV)
    └── benchmark_fair_results.json              # Raw Empirical Benchmark Results (JSON)
```

---

## 2. Foundational Base Research Paper Details
- **Title:** *Blockchain-assisted attribute-based multi-keyword search for dynamic encrypted data in cloud-edge-IoT*
- **Authors:** Hanlei Cheng, Sio-Long Lo, Jing Lu
- **Journal:** Elsevier *Internet of Things*, Volume 36, Article 101838, December 2025 / 2026
- **DOI:** [10.1016/j.iot.2025.101838](https://doi.org/10.1016/j.iot.2025.101838)
- **Included Formats:**
  - Editable Microsoft Word: `2_Research_Paper_Word/Base_Research_Paper_Cheng_et_al_2026.docx`
  - Publication PDF: `3_Research_Paper_PDF/Cheng_et_al_2026_Base_Research_Paper_BAMKS.pdf`

---

## 3. Key Experimental & Architectural Results

| Metric | Cheng et al. (Baseline) | BAMKS-D (Proposed) | Improvement / Result |
| :--- | :---: | :---: | :---: |
| **Single-Document Addition** | $O(L \cdot m)$ modular multiplications | Strict $O(m)$ token generation | **5.27× index speedup / 5.46× file speedup** at $L=5,000$ (724× vs. full re-indexing) |
| **Single-Document Revocation** | Re-encrypts entire collection | Strict $O(1)$ EVM state mapping | **Constant 50,111 EVM gas** ($\Delta	ext{Gas} = 0$ across $N \in \{1, 50, 500\}$) |
| **On-Chain Revocation Proof** | Requires re-keying | `deletedDocRegistry` verification | **100% Soundness** (Zero false positives, mathematically proven) |
| **Storage Architecture** | Centralized cloud index | Dual-Layer: Sepolia EVM + Pinata IPFS | Decentralized, verifiable, and economically viable |

---

## 4. Live Ethereum Sepolia Contract & Verified Transactions
- **Contract Name:** `BAMKS_Registry.sol`
- **Verified Contract Address:** [`0x17b09aad051BcD92EcfF3F08d87B1b333287cB1F`](https://sepolia.etherscan.io/address/0x17b09aad051BcD92EcfF3F08d87B1b333287cB1F)
- **Deployment Transaction:** [`0x2ac22e95065d53dbebd14125b11551ff0ccc393d85a22e29adc05e282eb6371b`](https://sepolia.etherscan.io/tx/0x2ac22e95065d53dbebd14125b11551ff0ccc393d85a22e29adc05e282eb6371b) (Block #11975525)
- **Document Registration Tx:** [`0xfdf127c7b1528cd1cd8bce1758ffe5a19260cc1a40f882b8b9f787e4ed591fbe`](https://sepolia.etherscan.io/tx/0xfdf127c7b1528cd1cd8bce1758ffe5a19260cc1a40f882b8b9f787e4ed591fbe) (Block #11975531)
- **Document Deletion Tx:** [`0x496e29a844e72e136220c71cf7a1780d29f7e86b99b9e9fb5db7c662d8c3a6d1`](https://sepolia.etherscan.io/tx/0x496e29a844e72e136220c71cf7a1780d29f7e86b99b9e9fb5db7c662d8c3a6d1) (Block #11975532)

---

## 5. Remote GitHub Repository
All functional project source code, test suites, contracts, and evaluation benchmarks are hosted at:  
**GitHub:** [https://github.com/Prashant8991/BAMKS.git](https://github.com/Prashant8991/BAMKS.git)