# Research Paper — Source Files

This directory contains both the **Foundational Base Research Paper** and the **Editable Manuscript Source Files** for the proposed BAMKS-D research project, satisfying all faculty and institutional submission requirements.

---

## 1. Foundational Base Research Paper
- **File:** `Base_Research_Paper_Cheng_et_al_2026.docx` (Editable Microsoft Word Document, 23 pages)
- **Full Title:** *Blockchain-assisted attribute-based multi-keyword search for dynamic encrypted data in cloud-edge-IoT*
- **Authors:** Hanlei Cheng, Sio-Long Lo, Jing Lu
- **Journal:** Elsevier *Internet of Things*, Volume 36, Article 101838, December 2025 / 2026
- **DOI:** [10.1016/j.iot.2025.101838](https://doi.org/10.1016/j.iot.2025.101838)
- **Role in Project:** This is the baseline academic literature extended by our work. While Cheng et al. pioneered multi-authority ABKS with user-level dynamic revocation, their scheme incurred O(L) linear client-side download complexity during document updates. Our project (BAMKS-D) eliminates this bottleneck, achieving O(1) constant-time dynamic file deletion and verification.

---

## 2. Editable Manuscript Sources (Our Work)
Per the BCSE309L Review 3 submission guidelines:
> *"Research Paper – Source File: Editable source file of the research paper (e.g., LaTeX source files or an editable Word document)."*

We provide the complete editable source code and manuscript in both standard academic formats:

1. **LaTeX Source File:**
   - **File:** `IEEE_BAMKS_D_Research_Paper.tex`
   - **Format:** Standard `IEEEtran` 2-column conference/transactions class.
   - **Contents:** Complete formal mathematical formulas, Algorithms 1–4, Table I (Comparative Analysis), Table II (EVM Opcode Gas Audit), Table III (Empirical Benchmarks), and formal Theorem 1–3 proofs.

2. **Microsoft Word Editable Document:**
   - **File:** `IEEE_BAMKS_D_Research_Paper.docx`
   - **Format:** Fully formatted Microsoft Word (.docx) document formatted with standard IEEE headings, author affiliations, formatted mathematical expressions, and tables.
   - **Utility:** Allows direct editing, track-changes review, and plagiarism verification (Urkund / Turnitin).

3. **Word Generation Script:**
   - **File:** `create_word_paper.py`
   - **Purpose:** Synchronizes the content of the Word document directly with the latest LaTeX source.

---

## 3. Compiled Camera-Ready PDF
The compiled, publication-ready 2-column PDF of our paper is located in:
- `../3_Research_Paper_PDF/IEEE_BAMKS_D_Research_Paper.pdf`
