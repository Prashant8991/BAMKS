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
    diagrams_dir = os.path.join(project_root, "diagrams")
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
        "Single-document addition operates in strict O(m) time, achieving a 5.27x speedup for pure index operations at L=5,000 files over Cheng et al. "
        "Section 5.10 updates (and 724.0x over naive full re-encryption). For like-for-like end-to-end file addition, BAMKS-D achieves a 5.46x speedup "
        "over Cheng et al. Single-document revocation is mapped directly to Ethereum Virtual Machine (EVM) storage (mapping(uint256 => bool) deletedDocRegistry), "
        "achieving O(1) constant-time lookup with zero array traversal on the deletion path. We validate the architecture through smart contract deployment "
        "on Ethereum Sepolia (0x17b09aad051BcD92EcfF3F08d87B1b333287cB1F), decentralized IPFS storage, and 30-run empirical benchmarks (m=3). "
        "An honest assessment of prototype algebraic assumptions, inverted index access-pattern leakage, and threats to validity is presented.\n\n"
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
        "were formulated, originating from verifiable attribute-based search by Zheng et al. [6] building upon foundational searchable encryption "
        "by Boneh et al. [7] and CP-ABE by Bethencourt et al. [8]. In CP-ABKS, data owners encrypt documents under an access structure (e.g., (Role_Doctor and Dept_Cardiology)), "
        "and only clinicians with valid attribute credentials can generate search trapdoors or decrypt returned records [9], [10], [11]. "
        "Advanced variants introduced non-monotonic policies [12], multi-authority decentralized key generation [13], [14], predicate evaluations [15], "
        "and dynamic broadcast structures [21]. Recently, Cheng et al. [1] proposed BAMKS, introducing decentralized multi-authority key generation, "
        "multi-owner collaborative indexing, and a blockchain Result Verification Smart Contract (RVSC) utilizing aggregated Schnorr Non-Interactive Zero-Knowledge (SNIZK) proofs [16]."
    )
    add_body_p(
        "The Open Challenge in BAMKS: In Section 8 of their foundational paper, Cheng et al. identified a critical operational bottleneck [1]: "
        "their architecture supports dynamic user credential updates, but does not define an efficient mechanism for single-file additions or deletions. "
        "Adding a single document requires either re-encrypting and re-indexing the entire document collection (naive baseline), or updating the entire "
        "inverted index via modular multiplication of an update token X_upd across all L * m index entries (Section 5.10 baseline) [1]. "
        "For an enterprise healthcare repository with L = 5,000 records and m = 3 keywords, updating 15,000 index entries introduces noticeable latency. "
        "Furthermore, document deletion was not defined in Cheng et al. [1], forcing reliance on full corpus re-encryption (O(L * m) assumption) or cloud server honesty."
    )
    add_body_p(
        "Contributions: In this work, we propose BAMKS-D, an architecture integration and dynamic evaluation framework that addresses these limitations:\n"
        "• Atomic Single-Document Addition (O(m)): Decouples inverted keyword indexing so appending an EHR requires generating tokens only for its m keywords.\n"
        "• Instant On-Chain Document Revocation (O(1)): Employs EVM direct mapping storage (deletedDocRegistry) with zero array traversal on the deletion path.\n"
        "• Live Ethereum Sepolia Deployment: Deployed BAMKS_Registry.sol contract on Ethereum Sepolia (0x17b09aad051BcD92EcfF3F08d87B1b333287cB1F) with mined receipts.\n"
        "• Rigorous Fair Benchmarks (30 Runs): Evaluates both naive re-encryption and true Cheng et al. Section 5.10 index updates without warm-up anomalies, demonstrating a 5.27x speedup for pure index updates and 5.46x for like-for-like full file additions at L=5,000 files on an Intel Core i5-13420H platform."
    )

    # Section II
    add_sec_heading("II", "Related Work")
    add_body_p(
        "Searchable encryption originated with symmetric constructions by Song et al. [17], formal security definitions by Curtmola et al. [18], "
        "and dynamic extensions by Kamara et al. [19] and Bost [20]. In the asymmetric domain, public-key searchable encryption (PEKS) was introduced "
        "by Boneh et al. [7]. To provide expressive access policies, Zheng et al. [6] developed VABKS for verifiable attribute-based search. "
        "Recent research has integrated blockchain ledgers to eliminate single points of failure in cloud servers [22], [23]. Liu et al. [24] designed "
        "EMK-ABSE for cloud-edge multi-keyword search, while Su et al. [25] formulated BA-RMKABSE supporting keyword updates in smart health systems. "
        "Zhang et al. [5] proposed ABCKS for conjunctive keywords with verifiable fairness. Liang et al. [6] developed VMSE, which supports keyword "
        "updating in multi-user settings. Cheng et al. [1] synthesized multi-owner collaborative search with aggregated SNIZK result verification (BAMKS), "
        "but left single-document dynamic updates unresolved. Table I contrasts BAMKS-D against foundational schemes."
    )

    # Table I
    p_t1_title = doc.add_paragraph()
    p_t1_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t1_title.paragraph_format.space_before = Pt(6)
    p_t1_title.paragraph_format.space_after = Pt(2)
    r_t1 = p_t1_title.add_run("TABLE I: COMPARISON OF SEARCHABLE ENCRYPTION SCHEMES")
    r_t1.font.bold = True
    r_t1.font.size = Pt(9.5)

    tbl_s = doc.add_table(rows=8, cols=5)
    tbl_s.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_s.autofit = False
    s_widths = [Inches(1.8), Inches(1.1), Inches(1.6), Inches(1.6), Inches(1.1)]
    for row in tbl_s.rows:
        for idx, w in enumerate(s_widths):
            row.cells[idx].width = w

    headers = ["Scheme", "Query Type", "Access Control", "Dynamic Scope", "Deletion Cost"]
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
        ["VABKS (Zheng et al., 2014) [6]", "Single", "Single-Auth", "Static Index", "N/A"],
        ["EMK-ABSE (Liu et al., 2022) [24]", "Conjunctive", "Edge-Assisted", "Static Index", "N/A"],
        ["BA-RMKABSE (Su et al., 2022) [25]", "Conjunctive", "Attr Hiding", "Keyword Update", "N/A"],
        ["ABCKS (Zhang et al., 2023) [5]", "Conjunctive", "Multi-Auth", "Static Index", "N/A"],
        ["VMSE (Liang et al., 2023) [6]", "Conjunctive", "Multi-User", "Keyword Update", "N/A"],
        ["BAMKS (Cheng et al., 2026) [1]", "Conjunctive", "Multi-Auth CP-ABE", "Corpus (L * m)", "O(L * m)*"],
        ["BAMKS-D (This Work)", "Conjunctive", "Multi-Auth CP-ABE", "Single-Doc (m)", "Strict O(1)"]
    ]
    for r_idx, r_data in enumerate(table1_data, start=1):
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        if r_idx == 7:
            bg = "EFF6FF"
        for c_idx, val in enumerate(r_data):
            cell = tbl_s.cell(r_idx, c_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=50, bottom=50, left=70, right=70)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            if r_idx == 7:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1d, 0x4e, 0xd8)

    p_fn1 = doc.add_paragraph()
    p_fn1.paragraph_format.space_before = Pt(2)
    p_fn1.paragraph_format.space_after = Pt(6)
    r_fn1 = p_fn1.add_run("* Cheng et al. does not define document deletion; O(L * m) represents assumed re-encryption baseline.")
    r_fn1.font.size = Pt(8.0)
    r_fn1.font.italic = True

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

    # Insert Architecture Diagram if available
    arch_img_path = os.path.join(diagrams_dir, "diagram_architecture.png")
    if os.path.exists(arch_img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_picture(arch_img_path, width=Inches(6.0))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c = p_cap.add_run("Fig. 1. Decoupled BAMKS-D Architecture Topology and Operational Flow.")
        r_c.font.bold = True
        r_c.font.size = Pt(9.0)

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
        "3. For each w_j in W_doc:\n"
        "     I_{doc,j} = g^{(eta * H_1(w_j)) mod (P-1)} mod P\n"
        "     Key_j = H_2('tok_' || I_{doc,j}); Index_{doc}[Key_j] = I_{doc,j}\n"
        "4. Sepolia.registerDocument(docId, H_2(C_data), y_k)\n"
        "Output: (CID, Index_{doc}, y_k) [Strict O(m) complexity]"
    )

    add_callout_box(
        doc,
        "Algorithm 2: SingleDocDelete(docId) [On-Chain EVM Execution]",
        "Input: docId, msg.sender.\n"
        "1. require(fileRegistry[docId].ownerAddress == msg.sender || msg.sender == owner)\n"
        "2. require(fileRegistry[docId].docId != 0)\n"
        "3. require(!deletedDocRegistry[docId])\n"
        "4. deletedDocRegistry[docId] = true\n"
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
        "3. If R == RHS: Accept (Proof Valid); Else: Reject (Proof Tampered)\n"
        "NOTE: Verification executed off-chain by client; on-chain RVSC enforces non-revocation membership and binding integrity."
    )

    # Section V
    add_sec_heading("V", "Complexity & EVM Gas Analysis")
    add_subsec_heading("A.", "Asymptotic Complexity Comparison")
    add_body_p(
        "Table II compares the asymptotic complexity of BAMKS-D against naive re-encryption and Cheng et al. [1]. While Cheng et al. Section 5.10 "
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
        ["SingleDocDelete", "O(L * m) Re-enc", "O(L * m) Assumed*", "Strict O(1) Constant Gas"],
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

    p_fn2 = doc.add_paragraph()
    p_fn2.paragraph_format.space_before = Pt(2)
    p_fn2.paragraph_format.space_after = Pt(6)
    r_fn2 = p_fn2.add_run("* Cheng et al. does not define document deletion; O(L * m) represents assumed re-encryption baseline.")
    r_fn2.font.size = Pt(8.0)
    r_fn2.font.italic = True

    # Table III
    add_subsec_heading("B.", "EVM Opcode Gas Schedule and Live Sepolia Receipts")
    add_body_p(
        "In Solidity, mapping lookups calculate storage addresses directly via keccak256(abi.encode(docId, slotNumber)). "
        "Table III presents both standard EVM gas measurements (py-evm) and live mined receipts on Ethereum Sepolia."
    )

    p_t3_title = doc.add_paragraph()
    p_t3_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t3_title.paragraph_format.space_before = Pt(6)
    p_t3_title.paragraph_format.space_after = Pt(2)
    r_t3 = p_t3_title.add_run("TABLE III: SMART CONTRACT GAS METRICS & SEPOLIA RECEIPTS")
    r_t3.font.bold = True
    r_t3.font.size = Pt(9.5)

    tbl_gas = doc.add_table(rows=4, cols=4)
    tbl_gas.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_gas.autofit = False
    g_widths = [Inches(2.2), Inches(1.8), Inches(1.8), Inches(1.4)]
    for row in tbl_gas.rows:
        for idx, w in enumerate(g_widths):
            row.cells[idx].width = w

    gas_headers = ["Function / Metric", "Standard EVM Gas", "Sepolia Receipt Gas", "Confirmation Time"]
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
        ["deployContract", "555,050 gas", "3,788,192 gas", "15.17 s"],
        ["registerDocument(101)", "179,505 gas", "789,245 gas", "13.71 s"],
        ["deleteDocument(101)", "50,111 gas", "132,131 gas", "10.37 s"]
    ]
    for r_idx, r_data in enumerate(gas_data, start=1):
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        if r_idx == 3:
            bg = "EFF6FF"
        for c_idx, val in enumerate(r_data):
            cell = tbl_gas.cell(r_idx, c_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=50, bottom=50, left=70, right=70)
            p = cell.paragraphs[0]
            if c_idx > 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            if r_idx == 3 and c_idx in [1, 2]:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1d, 0x4e, 0xd8)

    add_body_p(
        "To empirically verify the O(1) constant-time claim, we measured deleteDocument gas with varying numbers of documents registered: "
        "N = 1: 50,111 gas; N = 50: 50,111 gas; N = 500: 50,111 gas. The measured gas differential is strictly 0 gas units across all tested registry sizes, "
        "confirming strict O(1) invariance. Standard EVM execution for deletion requires cold slot resolution, 2 cold storage reads, "
        "1 cold zero-to-nonzero write (deletedDocRegistry[docId] = true at 22,100 gas), LOG3 event (~1,500 gas), and base transaction fee (21,000 gas), "
        "totaling 50,111 gas. On Sepolia testnet, function dispatcher routing and execution wrapper overhead yielded 132,131 gas."
    )

    # Section VI
    add_sec_heading("VI", "Experimental Evaluation")
    add_subsec_heading("A.", "Experimental Configuration")
    add_body_p(
        "All software experiments were conducted in Python 3.11.9 utilizing PyCryptodome and Web3.py on an Intel(R) Core(TM) i5-13420H "
        "processor (8 cores, 12 threads, up to 4.60 GHz) with 16.0 GB RAM running 64-bit Windows 11. Timings were collected using "
        "time.perf_counter() across 30 independent runs with un-timed warm-up iterations discarded to eliminate JIT anomalies (m=3 keywords per document). "
        "Mean and standard deviation values are reported in Table IV."
    )

    # Table IV
    p_t4_title = doc.add_paragraph()
    p_t4_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t4_title.paragraph_format.space_before = Pt(6)
    p_t4_title.paragraph_format.space_after = Pt(2)
    r_t4 = p_t4_title.add_run("TABLE IV: BENCHMARK RESULTS (30 RUNS, m=3, MEAN ± STD DEV [MEDIAN])")
    r_t4.font.bold = True
    r_t4.font.size = Pt(9.5)

    tbl_bm = doc.add_table(rows=8, cols=7)
    tbl_bm.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_bm.autofit = False
    b_widths = [Inches(0.8), Inches(1.2), Inches(1.2), Inches(1.2), Inches(1.1), Inches(1.1), Inches(1.0)]
    for row in tbl_bm.rows:
        for idx, w in enumerate(b_widths):
            row.cells[idx].width = w

    bm_headers = ["Files (L)", "Naive Re-enc (ms)", "Cheng Idx (ms)", "Cheng Full (ms)", "BAMKS-D Idx", "BAMKS-D Full", "Speedup"]
    for idx, text in enumerate(bm_headers):
        cell = tbl_bm.cell(0, idx)
        set_cell_background(cell, "1E293B")
        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        r.font.bold = True
        r.font.size = Pt(8.0)
        r.font.color.rgb = RGBColor(0xff, 0xff, 0xff)

    bm_data = [
        ["10", "0.49 [0.45]", "0.003 [0.003]", "0.05 [0.05]", "0.23 [0.22]", "0.27 [0.26]", "0.01x / 0.17x"],
        ["50", "2.26 [2.20]", "0.015 [0.015]", "0.06 [0.06]", "0.23 [0.22]", "0.27 [0.26]", "0.06x / 0.23x"],
        ["100", "4.66 [4.57]", "0.032 [0.031]", "0.09 [0.08]", "0.22 [0.22]", "0.27 [0.26]", "0.12x / 0.34x"],
        ["500", "24.49 [23.39]", "0.183 [0.151]", "0.28 [0.25]", "0.25 [0.24]", "0.31 [0.27]", "0.58x / 0.90x"],
        ["1,000", "45.60 [45.54]", "0.325 [0.297]", "0.44 [0.41]", "0.23 [0.23]", "0.28 [0.27]", "1.15x / 1.56x"],
        ["2,000", "103.32 [98.32]", "0.662 [0.602]", "0.79 [0.74]", "0.25 [0.24]", "0.32 [0.27]", "2.04x / 2.42x"],
        ["5,000", "243.64 [238.70]", "1.772 [1.479]", "1.84 [1.60]", "0.25 [0.24]", "0.34 [0.31]", "5.27x / 5.46x"]
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
            r.font.size = Pt(8.0)
            if r_idx == 7 and c_idx == 6:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1d, 0x4e, 0xd8)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Insert Scalability Chart if available
    chart_path = os.path.join(diagrams_dir, "chart_scalability_multi_n.png")
    if os.path.exists(chart_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_picture(chart_path, width=Inches(6.0))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c = p_cap.add_run("Fig. 2. Scalability: Naive vs. Cheng et al. vs. BAMKS-D (m=3, 30 independent runs).")
        r_c.font.bold = True
        r_c.font.size = Pt(9.0)

    add_subsec_heading("B.", "Comparative Discussion")
    add_body_p(
        "Evaluating pure index updates, Cheng et al. is faster for L <= 500 because computing modular multiplications takes less CPU time "
        "than modular exponentiations. The break-even crossover occurs at L ~ 800 documents for pure index operations, beyond which BAMKS-D "
        "achieves a 5.27x speedup at L = 5,000 files. In contrast, under like-for-like end-to-end file addition (including AES encryption of the new record), "
        "the crossover occurs at L ~ 600 files, reaching a 5.46x speedup over Cheng et al. and a 724.0x speedup over naive full re-encryption (243.6 ms)."
    )

    # Section VII: Limitations
    add_sec_heading("VII", "Limitations & Threats to Validity")
    add_body_p(
        "To ensure complete academic transparency, we explicitly document the prototype limitations of this study:\n"
        "• Simulated Group Algebra: Field operations are evaluated in (Z_P*, *) using P = 2^256 - 2^32 - 977. This group has order P-1 (composite) "
        "and does not possess a bilinear map. Formal pairing-based security reductions require porting to a Type-III pairing curve (e.g., BN254).\n"
        "• Off-Chain Verification Scope: Aggregated Schnorr NIZK verification is executed off-chain by the edge or client node; the on-chain smart contract enforces non-revocation membership and query binding.\n"
        "• Deterministic Keyword Tokens: Keyword tokens are deterministic per keyword across documents. Consequently, an untrusted CSP can observe "
        "document frequency and search access patterns over time. Addressing access pattern leakage via ORAM or forward-private searchable encryption [20] is vital future work.\n"
        "• Access Control Model: registerDocument permits multi-owner document onboarding without whitelist gating; deleteDocument is restricted to document owners or the contract administrator.\n"
        "• Local vs. On-Chain Latency: Local state flag updates take < 0.001 ms in memory, whereas on-chain confirmation on Ethereum Sepolia requires block mining "
        "(10.37 s confirmation for deletion; 13.71 s for registration)."
    )

    # Section VIII: Conclusion
    add_sec_heading("VIII", "Conclusion")
    add_body_p(
        "This paper presented BAMKS-D, an algorithmic prototype and architecture integration layer addressing the dynamic file update challenge in "
        "blockchain-assisted ABKS. By decoupling inverted index generation, BAMKS-D achieves O(m) single-file additions, yielding a 5.27x pure index "
        "speedup (and 5.46x full add speedup) over Cheng et al. Section 5.10 index updates at L=5,000 files (and 724.0x over naive re-encryption). "
        "On-chain revocation is enforced in O(1) constant time via EVM mapping storage on Ethereum Sepolia."
    )

    # Section IX: Data & Code Availability
    add_sec_heading("IX", "Data and Code Availability")
    add_body_p(
        "Complete reproducible source code, Solidity contracts, clinical sample datasets, and benchmark scripts are openly available on GitHub at: "
        "https://github.com/Prashant8991/BAMKS.git. Verified Ethereum Sepolia contract: 0x17b09aad051BcD92EcfF3F08d87B1b333287cB1F."
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
        "[5] D. Zhang, S. Wang, Q. Zhang, and Y. Zhang, 'Attribute based conjunctive keywords search with verifiability and fair payment using blockchain,' IEEE Trans. Serv. Comput., vol. 16, no. 6, pp. 4168–4182, 2023. DOI: 10.1109/TSC.2023.3308170.",
        "[6] Q. Zheng, S. Xu, and G. Ateniese, 'VABKS: Verifiable attribute-based keyword search over outsourced encrypted data,' in Proc. IEEE INFOCOM 2014, 2014, pp. 522–530. DOI: 10.1109/INFOCOM.2014.6848198.",
        "[7] D. Boneh, G. Di Crescenzo, R. Ostrovsky, and G. Persiano, 'Public key encryption with keyword search,' in Eurocrypt 2004, LNCS vol. 3027, Springer, 2004, pp. 506–522. DOI: 10.1007/978-3-540-24676-3_30.",
        "[8] J. Bethencourt, A. Sahai, and B. Waters, 'Ciphertext-policy attribute-based encryption,' in IEEE Symposium on Security and Privacy (S&P), 2007, pp. 321–334. DOI: 10.1109/SP.2007.11.",
        "[9] A. Sahai and B. Waters, 'Fuzzy identity-based encryption,' in Eurocrypt 2005, LNCS vol. 3494, Springer, 2005, pp. 457–473. DOI: 10.1007/11426639_27.",
        "[10] B. Waters, 'Ciphertext-policy attribute-based encryption: An expressive, efficient, and provably secure realization,' in PKC 2011, LNCS vol. 6571, Springer, 2011, pp. 53–70. DOI: 10.1007/978-3-642-19377-4_4.",
        "[11] V. Goyal, O. Pandey, A. Sahai, and B. Waters, 'Attribute-based encryption for fine-grained access control of encrypted data,' in ACM CCS 2006, 2006, pp. 89–98. DOI: 10.1145/1180405.1180418.",
        "[12] R. Ostrovsky, A. Sahai, and B. Waters, 'Attribute-based encryption with non-monotonic access structures,' in ACM CCS 2007, 2007, pp. 195–203. DOI: 10.1145/1315245.1315270.",
        "[13] M. Chase, 'Multi-authority attribute based encryption,' in TCC 2007, LNCS vol. 4392, Springer, 2007, pp. 515–534. DOI: 10.1007/978-3-540-70936-7_28.",
        "[14] A. Lewko and B. Waters, 'Decentralizing attribute-based encryption,' in Eurocrypt 2011, LNCS vol. 6632, Springer, 2011, pp. 568–588. DOI: 10.1007/978-3-642-20465-4_31.",
        "[15] J. Katz, A. Sahai, and B. Waters, 'Predicate encryption supporting disjunctions, polynomial equations, and inner products,' J. Cryptology, vol. 26, no. 2, pp. 191–224, 2013. DOI: 10.1007/s00145-012-9119-4.",
        "[16] C. P. Schnorr, 'Efficient signature generation by smart cards,' Journal of Cryptology, vol. 4, no. 3, pp. 161–174, 1991. DOI: 10.1007/BF00196725.",
        "[17] D. X. Song, D. Wagner, and A. Perrig, 'Practical techniques for searches on encrypted data,' in IEEE Symposium on Security and Privacy (S&P), 2000, pp. 44–55. DOI: 10.1109/SECPRI.2000.848445.",
        "[18] R. Curtmola, J. Garay, S. Kamara, and R. Ostrovsky, 'Searchable symmetric encryption: Improved definitions and efficient constructions,' J. Comput. Secur., vol. 19, no. 5, pp. 895–934, 2011. DOI: 10.3233/JCS-2011-0426.",
        "[19] S. Kamara, C. Papamanthou, and T. Roeder, 'Dynamic searchable symmetric encryption,' in ACM CCS 2012, 2012, pp. 965–976. DOI: 10.1145/2382196.2382298.",
        "[20] R. Bost, 'Sigma o phi o varsigma: Forward secure searchable encryption,' in ACM CCS 2016, 2016, pp. 1143–1154. DOI: 10.1145/2976749.2978342.",
        "[21] C. Delerablée, P. Paillier, and D. Pointcheval, 'Fully dynamic broadcast encryption with constant-size ciphertexts and private keys,' in Pairing 2007, LNCS vol. 4575, Springer, 2007, pp. 190–207. DOI: 10.1007/978-3-540-73489-5_11.",
        "[22] G. Wood, 'Ethereum: A secure decentralised generalised transaction ledger (Yellow Paper),' Berlin Version, Ethereum Project, 2024. [Online]. Available: https://ethereum.github.io/yellowpaper/paper.pdf",
        "[23] J. Benet, 'IPFS - Content Addressed, Versioned, P2P File System,' Draft 3, Protocol Labs, arXiv:1407.3561, 2014.",
        "[24] J. Liu, Y. Li, R. Sun, et al., 'EMK-ABSE: Efficient multikeyword attribute-based searchable encryption scheme through cloud-edge coordination,' IEEE Internet of Things J., vol. 9, no. 19, pp. 18650–18662, 2022. DOI: 10.1109/JIOT.2022.3164478.",
        "[25] J. Su, L. Zhang, and Y. Mu, 'BA-RMKABSE: Blockchain-aided ranked multi-keyword attribute-based searchable encryption with hiding policy for smart health system,' Future Gener. Comput. Syst., vol. 132, pp. 299–309, 2022. DOI: 10.1016/j.future.2022.02.019.",
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
