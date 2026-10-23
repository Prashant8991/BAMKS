# BAMKS-D: Final Review 3 Submission Package
**Course:** BCSE309L — Cryptography and Network Security  
**Institution:** Vellore Institute of Technology (VIT), Chennai  
**Faculty Guide:** Prof. Karthika V  
**Authors:**
- **Prashant Singh** (Reg. No: 24BYB1042)
- **Rushikesh Adak** (Reg. No: 24BYB1055)

---

## 1. Directory Structure

This submission directory contains the complete set of required deliverables for Review 3, organized into standardized folders:

```
submission_materials/
├── Base_Research_Paper_Cheng_et_al/            # ⭐ ORIGINAL BASE RESEARCH PAPER (Requested by Faculty Guide)
│   └── Cheng_et_al_2026_Base_Research_Paper_BAMKS.pdf # Full Elsevier 23-page base research paper
├── 1_Presentation_PPT/
│   ├── BAMKS_D_Final_Presentation.pptx          # 16-slide widescreen presentation
│   └── create_presentation.py                   # Automated PPTX generator
├── 2_Research_Paper_Source/
│   ├── Base_Research_Paper_Cheng_et_al_2026.docx # Editable Word Document of Base Paper (Cheng et al., 2026)
│   ├── IEEE_BAMKS_D_Research_Paper.docx         # Editable Microsoft Word document (Our Work)
│   ├── IEEE_BAMKS_D_Research_Paper.tex          # Complete LaTeX source (IEEEtran class)
│   ├── README.md                                # Folder documentation & source guide
│   └── create_word_paper.py                     # Script to sync and regenerate docx
├── 3_Research_Paper_PDF/
│   ├── IEEE_BAMKS_D_Research_Paper.pdf          # Final IEEE research paper PDF (Our Work, 13 Pages, 4.4 MB)
│   └── create_ieee_pdf.py                       # High-fidelity PDF generator script
├── 4_Source_Code/
│   ├── BAMKS_D_Complete_Source_Code.zip         # Portable 5.2 MB archive with all source code
│   ├── BAMKS_D_Source_Package/                  # Uncompressed full source package
│   └── package_source_code.py                   # Automated packaging script
├── 5_Supplementary_Files/
│   ├── Cheng_et_al_2026_Base_Research_Paper_BAMKS.pdf # Base research paper (Supplementary copy)
│   ├── Additional_Experimental_Results.md       # Full benchmark tables & speedup analysis
│   ├── Dataset_Details_and_Links.md             # Clinical EHR corpus description & links
│   ├── Implementation_Details_and_Reproduction_Guide.md # Step-by-step reproduction instructions
│   ├── Web3_Sepolia_and_IPFS_Audit_Proof.md     # Sepolia contract & IPFS audit evidence
│   └── Editable_Figure_Sources/                 # Python scripts & JSON data for diagrams
│       ├── benchmark_results.json
│       ├── scalability_analysis_results.json
│       ├── generate_diagram_images.py
│       └── generate_scalability_graph.py
└── README.md                                    # This directory documentation
```

---

## 1.1 Base Research Paper Details (Cheng et al., 2026)
- **Title:** *Blockchain-assisted attribute-based multi-keyword search for dynamic encrypted data in cloud-edge-IoT*
- **Authors:** Hanlei Cheng, Sio-Long Lo, Jing Lu
- **Journal:** Elsevier *Internet of Things*, Volume 36, Article 101838, December 2025 / 2026
- **DOI:** [10.1016/j.iot.2025.101838](https://doi.org/10.1016/j.iot.2025.101838)
- **Local PDF File:** `submission_materials/Base_Research_Paper_Cheng_et_al/Cheng_et_al_2026_Base_Research_Paper_BAMKS.pdf` (23 pages, 3.28 MB)
- **Editable Word Document:** `submission_materials/2_Research_Paper_Source/Base_Research_Paper_Cheng_et_al_2026.docx` (23 pages, 1.54 MB)


---

## 2. System Requirements & Environment Setup

- **Python Version:** Python 3.10 or 3.11
- **Operating System:** Windows, Linux, or macOS
- **Key Dependencies:**
  ```bash
  pip install pycryptodome cryptography web3 reportlab python-docx python-pptx requests matplotlib
  ```

---

## 3. How to Reproduce Experimental Results

### A. Run Core Cryptographic Protocol & Benchmark
```bash
python test_demo.py
```
*Expected Outcome:* Executes GlobalSetup, Multi-Authority KeyGen, SingleDocAdd, SingleDocDelete, dynamic conjunctive search, and benchmarks baseline vs. BAMKS-D across dataset sizes L in {50, 200, 500, 1000, 5000}.

### B. Run Automated Correctness & Security Test Suite
```bash
python test_correctness_and_security.py
```
*Expected Outcome:* Executes all 5 automated security tests:
- **Test A:** Soundness & trapdoor isolation (zero false positives)
- **Test B:** On-chain deletion filtering via RVSC
- **Test C:** CP-ABE attribute-based policy enforcement (Nurse denied, Doctor permitted)
- **Test D:** Batch addition complexity verification
- **Test E:** Byte-level index storage scaling

### C. Run EVM Mathematical O(1) Deletion Proof
```bash
python proof_of_o1_complexity.py
```
*Expected Outcome:* Regression analysis across N in [1, 500] confirming dGas/dN = 0 (constant 50,111 gas in EVM; 132,131 gas in live Sepolia receipt) and dTime/dN approx 0 us/record.

### D. Launch Interactive Clinical Web Application
```bash
python app.py
```
*Expected Outcome:* Launches local HTTP server on port 8080. Open `http://127.0.0.1:8080/index.html` to access the clinical search and dynamic record management dashboard.

---

## 4. Blockchain & IPFS Configuration
- **Ethereum Sepolia Contract:** `0x17b09aad051BcD92EcfF3F08d87B1b333287cB1F`
- **Etherscan Sepolia URL:** `https://sepolia.etherscan.io/address/0x17b09aad051BcD92EcfF3F08d87B1b333287cB1F`
- **Deployment Transaction:** `0x2ac22e95065d53dbebd14125b11551ff0ccc393d85a22e29adc05e282eb6371b` (Block #11975525)
- **IPFS Storage:** Decentralized Pinata IPFS Gateway (`https://gateway.pinata.cloud/ipfs/`)

