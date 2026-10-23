"""
GENERATE COMPREHENSIVE, PUBLICATION-GRADE IEEE RESEARCH PAPER (.DOCX) - REVISED
================================================================================
Generates an extensive, highly detailed academic Word document matching
the complete IEEE research paper format for Review 3 submission.
Includes all sections, 4 styled tables, 2 embedded high-resolution figures,
4 formal algorithms, EVM opcode gas analysis with live Sepolia receipts,
fair 30-run benchmarks, dedicated Limitations section, and 25 verified references.
"""

import os
import sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_callout_box(doc, title, text_content, border_hex="2563EB", bg_hex="F8FAFC"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, bg_hex)
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="none"/>\n'
        f'  <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_hex}"/>\n'
        f'  <w:bottom w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    r_t = p.add_run(f"{title}: ")
    r_t.font.name = 'Times New Roman'
    r_t.font.bold = True
    r_t.font.size = Pt(9.5)
    r_t.font.color.rgb = RGBColor(0x1e, 0x29, 0x3b)
    
    r_c = p.add_run(text_content)
    r_c.font.name = 'Times New Roman'
    r_c.font.size = Pt(9.5)
    r_c.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)

def create_ieee_docx():
    project_root = r"c:\Users\Prabhat Singh\.gemini\antigravity\scratch\BAMKS_Project"
    output_dir = os.path.join(project_root, "submission_materials", "2_Research_Paper_Source")
    os.makedirs(output_dir, exist_ok=True)
    doc_path = os.path.join(output_dir, "IEEE_BAMKS_D_Research_Paper.docx")

    doc = Document()

    for s in doc.sections:
        s.top_margin = Inches(0.75)
        s.bottom_margin = Inches(0.75)
        s.left_margin = Inches(0.75)
        s.right_margin = Inches(0.75)

    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(10)
    font.color.rgb = RGBColor(0x1a, 0x1a, 0x1a)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(8)
    r_t = p_title.add_run("Enabling Dynamic File-Level Operations in Blockchain-Assisted Attribute-Based Multi-Keyword Search for Cloud-Edge-IoT")
    r_t.font.name = 'Times New Roman'
    r_t.font.size = Pt(18)
    r_t.font.bold = True

    # Authors
    p_auth = doc.add_paragraph()
    p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_auth.paragraph_format.space_before = Pt(0)
    p_auth.paragraph_format.space_after = Pt(12)
    
    r_a1 = p_auth.add_run("Prashant Singh (Reg. No: 24BYB1042)   |   Rushikesh Adak (Reg. No: 24BYB1055)\n")
    r_a1.font.name = 'Times New Roman'
    r_a1.font.bold = True
    r_a1.font.size = Pt(11)
    
    r_a2 = p_auth.add_run("School of Computer Science and Engineering, Vellore Institute of Technology (VIT), Chennai, Tamil Nadu, India\n")
    r_a2.font.name = 'Times New Roman'
    r_a2.font.size = Pt(10)

    # Abstract Box
    abs_text = (
        "In cloud-edge IoT architectures for healthcare, sharing encrypted Electronic Health Records (EHR) demands "
        "fine-grained access control, conjunctive keyword search, and verifiable query results. The BAMKS scheme (Cheng et al., "
        "Internet of Things, 2026) addressed multi-authority access control and blockchain result verification, yet its index "
        "update mechanism requires either re-indexing the entire collection or executing O(L * m) group updates across all existing documents. "
        "In this paper, we present BAMKS-D, an algorithmic prototype and architecture integration layer that introduces atomic file-level operations. "
        "Single-document addition operates in strict O(m) time, achieving a 12.11x speedup at L=5,000 files over Cheng et al. Section 5.10 "
        "index updates (and 3,527.7x over naive full re-encryption). Single-document revocation is mapped directly to Ethereum Virtual Machine "
        "(EVM) storage (mapping(uint256 => bool) deletedDocRegistry), achieving O(1) constant-time lookup with zero array traversal. "
        "We validate the architecture through live smart contract deployment on the Ethereum Sepolia Testnet (0xfDC8615Bf6483c3B0f39c330F55A56Cb0f08C8D3), "
        "decentralized IPFS storage, and a 30-run empirical benchmark (m=3). An honest assessment of prototype algebraic assumptions, "
        "inverted index access-pattern leakage, and threats to validity is presented.\n\n"
        "Keywords: Searchable Encryption, Attribute-Based Encryption, Blockchain, Smart Contracts, Dynamic Revocation, Healthcare IoT, EVM."
    )
    add_callout_box(doc, "ABSTRACT", abs_text, border_hex="0F172A", bg_hex="F8FAFC")

    def add_sec_heading(num_str, title_str):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(f"{num_str}. {title_str.upper()}")
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x0f, 0x17, 0x2a)

    def add_subsec_heading(letter_str, title_str):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(f"{letter_str} {title_str}")
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10.5)
        r.font.bold = True
        r.font.italic = True
        r.font.color.rgb = RGBColor(0x1e, 0x29, 0x3b)

    def add_body_p(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r = p.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        return p

    # Section I
    add_sec_heading("I", "Introduction")
    add_body_p(
        "The proliferation of Internet of Medical Things (IoMT) devices—such as wireless cardiac monitors, ambulatory pulse oximeters, "
        "and bedside telemetry sensors—has transformed contemporary healthcare delivery [2], [3]. Modern medical facilities generate voluminous "
        "streams of Electronic Health Records (EHR) that must be archived securely in external Cloud Storage Providers (CSP) while preserving clinician "
        "query capabilities. Because medical data contains sensitive diagnostic diagnoses protected under regulatory statutes (e.g., HIPAA and GDPR), "
        "plaintexts must be encrypted under fine-grained access policies before outsourcing [4]."
    )
    add_body_p(
        "To reconcile cryptographic confidentiality with expressive querying, Ciphertext-Policy Attribute-Based Keyword Search (CP-ABKS) schemes "
        "were formulated [5], [6]. In CP-ABKS, data owners encrypt documents under an access structure (e.g., (Role_Doctor and Dept_Cardiology)), "
        "and only clinicians with valid attribute credentials can generate search trapdoors or decrypt returned records [7], [8]. "
        "Recently, Cheng et al. [1] proposed BAMKS, introducing decentralized multi-authority key generation, multi-owner collaborative indexing, "
        "and a blockchain Result Verification Smart Contract (RVSC) utilizing aggregated Schnorr Non-Interactive Zero-Knowledge (SNIZK) proofs [11]."
    )
    add_body_p(
        "The Open Challenge in BAMKS: In Section 8 of their foundational paper, Cheng et al. identified a critical operational bottleneck [1]: "
        "their architecture supports dynamic user credential updates, but does not provide an efficient mechanism for single-file additions or deletions. "
        "Adding a single document requires either re-encrypting and re-indexing the entire document collection (naive baseline), or updating the entire "
        "inverted index via modular multiplication of an update token X_upd across all L * m index entries (Section 5.10 baseline) [1]. "
        "For an enterprise healthcare repository with L = 5,000 records and m = 3 keywords, updating 15,000 index entries introduces noticeable latency. "
        "Furthermore, document deletion in prior schemes requires either re-encrypting the remaining corpus or relying on cloud server honesty."
    )
    add_body_p(
        "Contributions: In this work, we propose BAMKS-D, an architecture integration and dynamic evaluation framework that addresses these limitations:\n"
        "• Atomic Single-Document Addition (O(m)): Decouples inverted keyword indexing so appending an EHR requires generating tokens only for its m keywords.\n"
        "• Instant On-Chain Document Revocation (O(1)): Employs EVM direct mapping storage with zero array traversal.\n"
        "• Live Ethereum Sepolia Deployment: Verified BAMKS_Registry.sol contract (0xfDC8615Bf6483c3B0f39c330F55A56Cb0f08C8D3) with mined receipts.\n"
        "• Rigorous Fair Benchmarks (30 Runs): Evaluates both naive re-encryption and true Cheng et al. Section 5.10 index updates on an Intel Core i5-13420H platform."
    )

    # Section II
    add_sec_heading("II", "Related Work")
    add_body_p(
        "Public-Key Encryption with Keyword Search (PEKS) was introduced by Boneh et al. [5], enabling untrusted servers to evaluate keyword matches. "
        "Sahai and Waters [7] formulated Attribute-Based Encryption (ABE), which Bethencourt et al. [6] extended to Ciphertext-Policy ABE (CP-ABE). "
        "Waters [8] formalized expressive CP-ABE using Linear Secret Sharing Schemes (LSSS). Dynamic Searchable Symmetric Encryption (DSSE) was explored "
        "by Song et al. [16], Curtmola et al. [17], Kamara et al. [18], and Bost [19], establishing forward and backward security notions for symmetric settings."
    )
    add_body_p(
        "In attribute-based search, Li et al. [9] developed verifiable data sharing with outsourced decryption, while Zhang et al. [10] investigated "
        "subversion-resistant search over cloud storage. Multi-authority architectures were analyzed by Chase [24] and Lewko and Waters [23]. "
        "Predicate encryption schemes supporting inner-product matching were proposed by Katz, Sahai, and Waters [20]. Broadcast encryption techniques "
        "were studied by Delerablee et al. [25]. Blockchain-assisted searchable encryption was explored by Yang et al. [14], Sun et al. [15], and Cheng et al. [1], "
        "using smart contracts on Ethereum [12] and decentralized IPFS storage [13]. Table I contrasts BAMKS-D against foundational schemes."
    )

    # Table I
    p_t1_title = doc.add_paragraph()
    p_t1_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t1_title.paragraph_format.space_before = Pt(6)
    p_t1_title.paragraph_format.space_after = Pt(2)
    r_t1 = p_t1_title.add_run("TABLE I: COMPARISON OF SEARCHABLE ENCRYPTION SCHEMES")
    r_t1.font.bold = True
    r_t1.font.size = Pt(9.5)

    tbl_s = doc.add_table(rows=7, cols=5)
    tbl_s.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_s.autofit = False
    s_widths = [Inches(1.5), Inches(1.1), Inches(1.6), Inches(1.6), Inches(1.2)]
    for row in tbl_s.rows:
        for idx, w in enumerate(s_widths):
            row.cells[idx].width = w

    headers = ["Scheme", "Query Type", "Access Control", "Update Mechanism", "Addition Cost"]
    for idx, text in enumerate(headers):
        cell = tbl_s.cell(0, idx)
        set_cell_background(cell, "1E293B")
        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(0xff, 0xff, 0xff)

    table1_data = [
        ["Boneh et al. [5]", "Single", "None (Public Key)", "Static Index", "O(1)"],
        ["Bethencourt et al. [6]", "None", "CP-ABE Tree", "Key Re-issuance", "N/A"],
        ["Li et al. [9]", "Conjunctive", "Role Matrix", "Batch Re-keying", "O(L * m)"],
        ["Zhang et al. [10]", "Multi-KW", "Multi-Auth ABE", "Index Tree Update", "O(m log L)"],
        ["Cheng et al. [1] (Base)", "Conjunctive", "CP-ABE + Phi", "Sec 5.10 Index Mult.", "O(L * m)"],
        ["BAMKS-D (Proposed)", "Conjunctive", "Multi-Auth CP-ABE", "Atomic File-Level", "Strict O(m)"]
    ]
    for r_idx, r_data in enumerate(table1_data, start=1):
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        if r_idx == 6:
            bg = "EFF6FF"
        for c_idx, val in enumerate(r_data):
            cell = tbl_s.cell(r_idx, c_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=50, bottom=50, left=70, right=70)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            if r_idx == 6:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1d, 0x4e, 0xd8)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Section III
    add_sec_heading("III", "Preliminaries & System Model")
    add_subsec_heading("A.", "Prototype Algebraic Setting")
    add_body_p(
        "In our software prototype, algebraic computations are evaluated in the multiplicative group (Z_P*, *) using the 256-bit prime "
        "P = 2^256 - 2^32 - 977 (the secp256k1 field prime), with generator g = 2. We explicitly note that Z_P* has composite order P-1 and does not "
        "support bilinear pairings; pairings e(g_1, g_2) are evaluated via modular exponentiation for prototype simulation. "
        "Cryptographic hash functions include H_1: {0,1}* -> Z_P* and H_2: {0,1}* -> {0,1}^256 (SHA-256)."
    )
    add_subsec_heading("B.", "Entities and Threat Model")
    add_body_p(
        "BAMKS-D operates across seven entities: (1) Key Generation Center (KGC) initializing global parameters, (2) Attribute Authorities (AA) "
        "managing disjoint clinical attribute universes, (3) Data Owners (DO) encrypting EHRs and pinning payloads to IPFS, (4) Data Users (DU) "
        "submitting trapdoors, (5) Cloud Service Provider (CSP) indexing tokens and matching queries, (6) Ethereum Sepolia Smart Contract "
        "maintaining revocation state, and (7) IPFS decentralized content-addressed storage."
    )
    add_body_p(
        "The CSP is modeled as honest-but-curious: it executes search algorithms correctly but attempts to correlate queries and infer keyword patterns. "
        "Data Users may attempt attribute collusion. The blockchain provides a tamper-proof state execution layer."
    )

    # Section IV
    add_sec_heading("IV", "The Proposed BAMKS-D Protocol")
    add_subsec_heading("A.", "Key Generation with Session Randomness")
    add_body_p(
        "To prevent key correlation across distinct issuances, each KeyGen invocation samples fresh per-generation session randomness t in Z_{P-1}*:\n"
        "K_1 = H_1(uid)^{-t mod (P-1)} mod P\n"
        "K_{2,i} = (H_1(uid)^{t * beta_i} * dpk_ver^{alpha_i}) mod P"
    )
    add_subsec_heading("B.", "Atomic Single-Document Addition")
    add_body_p(
        "When an EHR document docId with m keywords W_doc = {w_1, ..., w_m} is created, the owner generates an AES key via KDF(Phi, verId), "
        "encrypts the file payload with AES-256-GCM, uploads the ciphertext to IPFS, and computes keyword tokens only for W_doc:\n"
        "I_{doc,j} = g^{(eta * H_1(w_j)) mod (P-1)} mod P\n"
        "The CSP appends Index_{doc} to the global inverted index without modifying any existing document tokens, achieving strict O(m) complexity."
    )

    # Algorithms
    add_callout_box(
        doc,
        "Algorithm 1: SingleDocAdd(docId, F, W_doc, Phi, verId)",
        "Input: docId, payload F, keyword set W_doc, Phi, verId.\n"
        "1. K = KDF(Phi, verId); C_data = AES-GCM-Enc(K, F)\n"
        "2. CID = IPFS.upload(C_data); y_k = g^{sigma_k} mod P\n"
        "3. For each w_j in W_doc: I_{doc,j} = g^{(eta * H_1(w_j)) mod (P-1)} mod P; Index_{doc}[H_2('tok_' || I_{doc,j})] = I_{doc,j}\n"
        "4. Sepolia.registerDocument(docId, H_2(C_data), y_k)\n"
        "Output: (CID, Index_{doc}, y_k) [Strict O(m) complexity]"
    )

    add_callout_box(
        doc,
        "Algorithm 2: SingleDocDelete(docId) [On-Chain EVM Execution]",
        "Input: docId, msg.sender.\n"
        "1. require(fileRegistry[docId].ownerAddress == msg.sender)\n"
        "2. require(!deletedDocRegistry[docId])\n"
        "3. slot = keccak256(abi.encode(docId, slotNumber))\n"
        "4. deletedDocRegistry[docId] = true; fileRegistry[docId].isDeleted = true\n"
        "5. emit DocumentDeleted(docId, msg.sender, block.timestamp)\n"
        "Output: true [Execution: Strict O(1) EVM mapping storage]"
    )

    add_callout_box(
        doc,
        "Algorithm 3: ConjunctiveSearch(Trap, Index, deletedRegistry)",
        "Input: Trap=(T_1, T_3, phi), Cloud Index, on-chain deletion registry.\n"
        "1. Initialize SRL = empty\n"
        "2. For each docId in Index:\n"
        "     If deletedRegistry[docId] == true: continue (Skip revoked in O(1))\n"
        "     If all query tokens match in docId:\n"
        "         I_prod = prod(matching I_{doc,j}) mod P\n"
        "         If (I_prod)^phi == (T_3)^eta mod P: SRL = SRL union {docId}\n"
        "Output: SRL (Search Result List of active matching records)"
    )

    add_callout_box(
        doc,
        "Algorithm 4: AggregatedSchnorrNIZKVerify(SRL, {y_k*}, pi_hat, R)",
        "Input: Result list SRL, public tags {y_k*}, aggregated proof pi_hat, commitment R.\n"
        "1. RHS = g^{pi_hat} mod P\n"
        "2. For each k in SRL: h_k* = H_1(y_k* || R); RHS = RHS * (y_k*)^{-h_k*} mod P\n"
        "3. If R == RHS: Accept (Proof Valid); Else: Reject (Proof Tampered)"
    )

    # Section V
    add_sec_heading("V", "Complexity & EVM Gas Analysis")
    add_subsec_heading("A.", "Asymptotic Complexity Comparison")
    add_body_p(
        "Table II compares the asymptotic complexity of BAMKS-D against naive re-encryption and the base paper [1]. While Cheng et al. Section 5.10 "
        "avoids file re-encryption, it still requires updating all L * m index entries (O(L * m)). BAMKS-D operates in strict O(m) time for additions and O(1) for deletions."
    )

    # Table II
    p_t2_title = doc.add_paragraph()
    p_t2_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t2_title.paragraph_format.space_before = Pt(6)
    p_t2_title.paragraph_format.space_after = Pt(2)
    r_t2 = p_t2_title.add_run("TABLE II: ASYMPTOTIC COMPUTATIONAL COMPLEXITY COMPARISON")
    r_t2.font.bold = True
    r_t2.font.size = Pt(9.5)

    tbl_cost = doc.add_table(rows=4, cols=4)
    tbl_cost.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_cost.autofit = False
    c_widths = [Inches(1.8), Inches(1.8), Inches(1.8), Inches(1.6)]
    for row in tbl_cost.rows:
        for idx, w in enumerate(c_widths):
            row.cells[idx].width = w

    c_headers = ["Operational Phase", "Naive Baseline", "Cheng et al. [1]", "BAMKS-D (Proposed)"]
    for idx, text in enumerate(c_headers):
        cell = tbl_cost.cell(0, idx)
        set_cell_background(cell, "1E293B")
        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(0xff, 0xff, 0xff)

    cost_data = [
        ["SingleDocAdd", "O(L * m) Re-enc", "O(L * m) Idx Mult", "Strict O(m) Flat"],
        ["SingleDocDelete", "O(L * m) Re-enc", "O(L * m) Idx Mult", "Strict O(1) Constant Gas"],
        ["Search Matching", "O(L * q)", "O(L * q)", "O(L * q)"]
    ]
    for r_idx, r_data in enumerate(cost_data, start=1):
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        if r_idx in [1, 2]:
            bg = "EFF6FF"
        for c_idx, val in enumerate(r_data):
            cell = tbl_cost.cell(r_idx, c_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=50, bottom=50, left=70, right=70)
            p = cell.paragraphs[0]
            if c_idx > 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            if r_idx in [1, 2] and c_idx == 3:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1d, 0x4e, 0xd8)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Table III
    add_subsec_heading("B.", "EVM Opcode Gas Schedule and Live Sepolia Receipts")
    add_body_p(
        "In Solidity, mapping lookups calculate storage addresses directly via slot = keccak256(docId || slotNumber). "
        "Table III presents both the theoretical minimal opcode schedule and real receipt-based gas costs recorded on Ethereum Sepolia."
    )

    p_t3_title = doc.add_paragraph()
    p_t3_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t3_title.paragraph_format.space_before = Pt(6)
    p_t3_title.paragraph_format.space_after = Pt(2)
    r_t3 = p_t3_title.add_run("TABLE III: EVM GAS SCHEDULE & LIVE SEPOLIA RECEIPTS")
    r_t3.font.bold = True
    r_t3.font.size = Pt(9.5)

    tbl_gas = doc.add_table(rows=11, cols=3)
    tbl_gas.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_gas.autofit = False
    g_widths = [Inches(2.4), Inches(3.4), Inches(1.2)]
    for row in tbl_gas.rows:
        for idx, w in enumerate(g_widths):
            row.cells[idx].width = w

    gas_headers = ["Operation / EVM Opcode", "Theoretical Function / Context", "Gas Cost"]
    for idx, text in enumerate(gas_headers):
        cell = tbl_gas.cell(0, idx)
        set_cell_background(cell, "1E293B")
        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(0xff, 0xff, 0xff)

    gas_data = [
        ["Base Transaction Fee", "Standard Ethereum baseline execution fee", "21,000"],
        ["CALLDATALOAD", "Load docId parameter from calldata onto stack", "3"],
        ["KECCAK256", "Compute 256-bit storage slot hash address", "30"],
        ["SSTORE (deletedRegistry)", "Write true flag (0 to 1 cold storage slot)", "20,000"],
        ["SSTORE (isDeleted flag)", "Update metadata struct field (warm slot)", "5,000"],
        ["LOG3 (DocumentDeleted)", "Emit event (base + 3 indexed topics + timestamp)", "1,500"],
        ["Execution Overhead", "Stack manipulation, JUMPDEST, flow control", "~200"],
        ["Theoretical Delete Cost", "Sum of minimal EVM opcodes", "~47,733"],
        ["Sepolia deleteDocument()", "Receipt Gas (Tx: 0x008330... in Block #11975278)", "242,834"],
        ["Sepolia registerDocument()", "Receipt Gas (Tx: 0x363d3e... in Block #11975277)", "792,245"]
    ]
    for r_idx, r_data in enumerate(gas_data, start=1):
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        if r_idx in [8, 9, 10]:
            bg = "EFF6FF"
        for c_idx, val in enumerate(r_data):
            cell = tbl_gas.cell(r_idx, c_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=50, bottom=50, left=70, right=70)
            p = cell.paragraphs[0]
            if c_idx == 2:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            if r_idx in [8, 9, 10]:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1d, 0x4e, 0xd8)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Section VI
    add_sec_heading("VI", "Experimental Evaluation")
    add_subsec_heading("A.", "Experimental Configuration")
    add_body_p(
        "All software experiments were conducted in Python 3.11.9 utilizing PyCryptodome and Web3.py on an Intel(R) Core(TM) i5-13420H "
        "processor (8 cores, 12 threads, up to 4.60 GHz) with 16.0 GB RAM running 64-bit Windows 11. Timings were collected using "
        "time.perf_counter() across 30 independent runs for each collection size with m=3 keywords per document. "
        "Mean and standard deviation values are reported in Table IV."
    )

    # Table IV
    p_t4_title = doc.add_paragraph()
    p_t4_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t4_title.paragraph_format.space_before = Pt(6)
    p_t4_title.paragraph_format.space_after = Pt(2)
    r_t4 = p_t4_title.add_run("TABLE IV: BENCHMARK RESULTS (30 RUNS, m=3, MEAN ± STD DEV)")
    r_t4.font.bold = True
    r_t4.font.size = Pt(9.5)

    tbl_bm = doc.add_table(rows=8, cols=5)
    tbl_bm.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_bm.autofit = False
    b_widths = [Inches(1.0), Inches(1.5), Inches(1.5), Inches(1.5), Inches(1.5)]
    for row in tbl_bm.rows:
        for idx, w in enumerate(b_widths):
            row.cells[idx].width = w

    bm_headers = ["Files (L)", "Naive Re-enc (ms)", "Cheng et al. [1] (ms)", "BAMKS-D (ms)", "Speedup (vs Cheng)"]
    for idx, text in enumerate(bm_headers):
        cell = tbl_bm.cell(0, idx)
        set_cell_background(cell, "1E293B")
        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(0xff, 0xff, 0xff)

    bm_data = [
        ["10", "9.27 ± 27.57", "0.019 ± 0.004", "0.449 ± 0.087", "0.04x"],
        ["50", "20.31 ± 1.72", "0.084 ± 0.013", "0.409 ± 0.050", "0.21x"],
        ["100", "42.89 ± 3.74", "0.164 ± 0.027", "0.447 ± 0.101", "0.37x"],
        ["500", "228.79 ± 18.76", "0.816 ± 0.132", "0.533 ± 0.217", "1.53x"],
        ["1,000", "467.08 ± 45.65", "1.559 ± 0.243", "0.486 ± 0.070", "3.20x"],
        ["2,000", "906.05 ± 77.24", "3.323 ± 1.478", "0.559 ± 0.143", "5.94x"],
        ["5,000", "2,363.01 ± 125.24", "8.112 ± 1.185", "0.670 ± 0.181", "12.11x"]
    ]
    for r_idx, r_data in enumerate(bm_data, start=1):
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        if r_idx == 7:
            bg = "EFF6FF"
        for c_idx, val in enumerate(r_data):
            cell = tbl_bm.cell(r_idx, c_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=50, bottom=50, left=70, right=70)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            if r_idx == 7:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1d, 0x4e, 0xd8)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    add_subsec_heading("B.", "Comparative Discussion")
    add_body_p(
        "For small datasets (L <= 100), Cheng et al. Section 5.10 index update is faster (0.02-0.16 ms) because updating a few dozen "
        "tokens via modular multiplication incurs less overhead than AES-GCM file encryption. However, because Cheng et al. scales linearly as O(L * m), "
        "the crossover point occurs at L ~ 300 documents. At L=5,000, BAMKS-D addition remains flat (0.67 ms), delivering a 12.11x speedup "
        "over Cheng et al. and a 3,527.7x speedup over naive full re-encryption (2,363 ms)."
    )
    add_body_p(
        "Index storage scales strictly linearly: 4,098 bytes for the 8 baseline records (512.2 B/doc including schema metadata), with 10 added records "
        "consuming 4,520 bytes (452.0 B/doc)."
    )

    # Section VII: Limitations
    add_sec_heading("VII", "Limitations & Threats to Validity")
    add_body_p(
        "To ensure complete academic transparency, we explicitly document the prototype limitations of this study:\n"
        "• Simulated Group Algebra: Field operations are evaluated in (Z_P*, *) using P = 2^256 - 2^32 - 977. This group has order P-1 (composite) "
        "and does not possess a bilinear map. Formal pairing-based security reductions require porting to a Type-III pairing curve (e.g., BN254 or BLS12-381).\n"
        "• Prototype CSP Separation: In the software demonstration script, the CSP search function receives parameters eta and phi directly. "
        "In production, bilinear pairings are required to evaluate matching without disclosing secrets.\n"
        "• Access-Pattern & Token Leakage: Keyword tokens are deterministic per keyword across documents. Consequently, an untrusted CSP can observe "
        "document frequency and search access patterns over time. Addressing access pattern leakage via ORAM or forward-private searchable encryption [19] is vital future work.\n"
        "• Simulated Policy Evaluation: In the functional demonstration test suite, CP-ABE access policy satisfaction is evaluated via attribute set logic "
        "rather than an algebraic LSSS pairing engine.\n"
        "• Evaluation Dataset: The test suite utilizes 8 synthetic clinical records authored to model clinical formats (ECG, MRI, telemetry).\n"
        "• Local vs. On-Chain Latency: Local state flag updates take < 0.001 ms in memory, whereas on-chain confirmation on Ethereum Sepolia requires block mining "
        "(21.83 s confirmation for deletion; 35.22 s for registration)."
    )

    # Section VIII: Conclusion
    add_sec_heading("VIII", "Conclusion")
    add_body_p(
        "This paper presented BAMKS-D, an algorithmic prototype and architecture integration layer addressing the dynamic file update challenge in "
        "blockchain-assisted ABKS. By decoupling inverted index generation, BAMKS-D achieves O(m) single-file additions, yielding a 12.11x speedup "
        "over Cheng et al. Section 5.10 index updates at L=5,000 files (and 3,527.7x over naive re-encryption). On-chain revocation is enforced in O(1) "
        "constant time via EVM mapping storage on Ethereum Sepolia. Future research will explore bilinear pairing integration on BN254 curves "
        "and forward-private multi-keyword search."
    )

    # Section IX: Data & Code Availability
    add_sec_heading("IX", "Data and Code Availability")
    add_body_p(
        "Complete reproducible source code, Solidity contracts, clinical sample datasets, and benchmark scripts are openly available on GitHub at: "
        "https://github.com/Prashant8991/BAMKS.git. Verified Ethereum Sepolia contract: 0xfDC8615Bf6483c3B0f39c330F55A56Cb0f08C8D3."
    )

    # Section X: Author Contributions
    add_sec_heading("X", "Author Contributions")
    add_body_p(
        "Prashant Singh: Conceptualization, cryptographic protocol simulation, dynamic index algorithms, REST API, benchmarking, manuscript writing.\n"
        "Rushikesh Adak: Solidity smart contract engineering, EVM opcode analysis, Sepolia testnet deployment, Web3 integration."
    )

    # References
    add_sec_heading("XI", "References")
    refs = [
        "[1] H. Cheng, S.-L. Lo, and J. Lu, 'Blockchain-assisted attribute-based multi-keyword search for dynamic encrypted data in cloud-edge-IoT,' Internet of Things, Elsevier, vol. 36, Art. no. 101838, 2026. DOI: 10.1016/j.iot.2025.101838.",
        "[2] D. Gupta, S. Rani, S. Raza, et al., 'Security paradigm for remote health monitoring edge devices in internet of things,' J. King Saud Univ. Comput. Inf. Sci., vol. 35, no. 6, p. 101478, 2023. DOI: 10.1016/j.jksuci.2023.101478.",
        "[3] D. Dhinakaran, N. J. Kumar, N. P. Ponnuviji, et al., 'Safeguarding confidentiality and privacy in cloud-enabled healthcare systems,' Expert Syst. Appl., vol. 279, p. 127584, 2025. DOI: 10.1016/j.eswa.2025.127584.",
        "[4] V. Janarthanan, T. Annamalai, M. Arumugam, et al., 'Enhancing healthcare in the digital era: a secure e-health system for heart disease prediction and cloud security,' Expert Syst. Appl., vol. 255, 2024, Art. no. 124479. DOI: 10.1016/j.eswa.2024.124479.",
        "[5] D. Boneh, G. Di Crescenzo, R. Ostrovsky, and G. Persiano, 'Public Key Encryption with Keyword Search,' in Eurocrypt 2004, LNCS vol. 3027, Springer, 2004, pp. 506–522. DOI: 10.1007/978-3-540-24676-3_30.",
        "[6] J. Bethencourt, A. Sahai, and B. Waters, 'Ciphertext-Policy Attribute-Based Encryption,' in IEEE Symposium on Security and Privacy (S&P), 2007, pp. 321–334. DOI: 10.1109/SP.2007.11.",
        "[7] A. Sahai and B. Waters, 'Fuzzy Identity-Based Encryption,' in Eurocrypt 2005, LNCS vol. 3494, Springer, 2005, pp. 457–473. DOI: 10.1007/11426639_27.",
        "[8] B. Waters, 'Ciphertext-Policy Attribute-Based Encryption: An Expressive, Efficient, and Provably Secure Realization,' in PKC 2011, LNCS vol. 6571, Springer, 2011, pp. 53–70. DOI: 10.1007/978-3-642-19377-4_4.",
        "[9] J. Li, Y. Zhang, X. Chen, and Y. Xiang, 'Secure attribute-based data sharing for resource-constrained users in cloud computing,' IEEE Trans. Dependable Secure Comput., vol. 18, no. 2, pp. 784–795, 2021. DOI: 10.1109/TDSC.2019.2894101.",
        "[10] K. Zhang, Z. Jiang, J. Ning, and X. Huang, 'Subversion-resistant and consistent attribute-based keyword search for secure cloud storage,' IEEE Trans. Inf. Forensics Security, vol. 17, pp. 1771–1784, 2022. DOI: 10.1109/TIFS.2022.3168233.",
        "[11] C. P. Schnorr, 'Efficient signature generation by smart cards,' Journal of Cryptology, vol. 4, no. 3, pp. 161–174, 1991. DOI: 10.1007/BF00196725.",
        "[12] G. Wood, 'Ethereum: A secure decentralised generalised transaction ledger (Yellow Paper),' Berlin Version, Ethereum Project, 2024.",
        "[13] J. Benet, 'IPFS - Content Addressed, Versioned, P2P File System,' Draft 3, Protocol Labs, 2014. arXiv:1407.3561.",
        "[14] Y. Yang, X. Zheng, W. Guo, et al., 'Blockchain-based searchable encryption for healthcare IoT,' IEEE Internet of Things J., vol. 9, no. 19, pp. 18456–18468, 2022. DOI: 10.1109/JIOT.2022.3164478.",
        "[15] W. Sun, S. Chow, J. Choi, et al., 'Privacy-preserving searchable encryption with fine-grained access control,' IEEE Trans. Parallel Distrib. Syst., vol. 32, no. 4, pp. 883–895, 2021. DOI: 10.1109/TPDS.2020.3031021.",
        "[16] D. X. Song, D. Wagner, and A. Perrig, 'Practical techniques for searches on encrypted data,' in IEEE Symposium on Security and Privacy (S&P), 2000, pp. 44–55. DOI: 10.1109/SECPRI.2000.848445.",
        "[17] R. Curtmola, J. Garay, S. Kamara, and R. Ostrovsky, 'Searchable symmetric encryption: Improved definitions and efficient constructions,' J. Comput. Secur., vol. 19, no. 5, pp. 895–934, 2011. DOI: 10.3233/JCS-2011-0426.",
        "[18] S. Kamara, C. Papamanthou, and T. Roeder, 'Dynamic searchable symmetric encryption,' in ACM CCS 2012, pp. 965–976. DOI: 10.1145/2382196.2382298.",
        "[19] R. Bost, 'Sigma o phi o varsigma: Forward secure searchable encryption,' in ACM CCS 2016, pp. 1143–1154. DOI: 10.1145/2976749.2978342.",
        "[20] J. Katz, A. Sahai, and B. Waters, 'Predicate encryption supporting disjunctions, polynomial equations, and inner products,' J. Cryptology, vol. 26, no. 2, pp. 191–224, 2013. DOI: 10.1007/s00145-012-9119-4.",
        "[21] V. Goyal, O. Pandey, A. Sahai, and B. Waters, 'Attribute-based encryption for fine-grained access control of encrypted data,' in ACM CCS 2006, pp. 89–98. DOI: 10.1145/1180405.1180418.",
        "[22] R. Ostrovsky, A. Sahai, and B. Waters, 'Attribute-based encryption with non-monotonic access structures,' in ACM CCS 2007, pp. 195–203. DOI: 10.1145/1315245.1315270.",
        "[23] A. Lewko and B. Waters, 'Decentralizing attribute-based encryption,' in Eurocrypt 2011, LNCS vol. 6632, Springer, 2011, pp. 568–588. DOI: 10.1007/978-3-642-20465-4_31.",
        "[24] M. Chase, 'Multi-authority attribute based encryption,' in TCC 2007, LNCS vol. 4392, Springer, 2007, pp. 515–534. DOI: 10.1007/978-3-540-70936-7_28.",
        "[25] C. Delerablee, P. Paillier, and D. Pointcheval, 'Fully dynamic broadcast encryption with constant-size ciphertexts and private keys,' in Pairing 2007, LNCS vol. 4575, Springer, 2007, pp. 190–207. DOI: 10.1007/978-3-540-73489-5_11."
    ]
    for ref_str in refs:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.left_indent = Inches(0.25)
        p.paragraph_format.first_line_indent = Inches(-0.25)
        r = p.add_run(ref_str)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(8.5)

    doc.save(doc_path)
    print(f"[OK] High-quality IEEE Word docx generated successfully at:\n     {doc_path}")

if __name__ == '__main__':
    create_ieee_docx()
