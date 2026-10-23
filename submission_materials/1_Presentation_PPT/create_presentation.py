"""
BAMKS-D FINAL PRESENTATION GENERATOR (PPTX) - REVISED & DEFENSE READY
=====================================================================
Generates a stunning, publication-grade 17-slide widescreen (16:9) presentation
for Review 3 / Final Defense of BAMKS-D at VIT Chennai.
Reflects honest academic framing, fair 30-run benchmarks, live Sepolia contract receipts,
reconciled EVM opcode gas analysis, and explicit Prototype Limitations.

Authors: Prashant Singh (24BYB1042) & Rushikesh Adak (24BYB1055)
Course: Cryptography and Network Security (BCSE309L)
Institution: Vellore Institute of Technology (VIT), Chennai
Faculty Guide: Prof. Karthika V
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    project_root = r"c:\Users\Prabhat Singh\.gemini\antigravity\scratch\BAMKS_Project"
    output_dir = os.path.join(project_root, "submission_materials", "1_Presentation_PPT")
    diagrams_dir = os.path.join(project_root, "diagrams")
    os.makedirs(output_dir, exist_ok=True)
    ppt_path = os.path.join(output_dir, "BAMKS_D_Final_Presentation.pptx")

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    C_NAVY      = RGBColor(15, 23, 42)       # #0F172A Dark Slate Navy
    C_BLUE      = RGBColor(30, 58, 138)      # #1E3A8A Primary Dark Blue
    C_CYAN      = RGBColor(2, 132, 199)      # #0284C7 Vibrant Accent Cyan
    C_LIGHT_BG  = RGBColor(248, 250, 252)   # #F8FAFC Clean Card Background
    C_CARD_ALT  = RGBColor(241, 245, 249)   # #F1F5F9 Soft Alternate
    C_BORDER    = RGBColor(203, 213, 225)   # #CBD5E1 Elegant Border
    C_DARK_TXT  = RGBColor(30, 41, 59)       # #1E293B Crisp Dark Text
    C_MUTED     = RGBColor(100, 116, 139)    # #64748B Secondary Text
    C_WHITE     = RGBColor(255, 255, 255)    # #FFFFFF Pure White
    C_GREEN     = RGBColor(22, 163, 74)      # #16A34A Success Green
    C_AMBER     = RGBColor(217, 119, 6)      # #D97706 Warning/Highlight Amber
    C_RED       = RGBColor(220, 38, 38)      # #DC2626 Critical/Problem Red

    def add_header(slide, title_text, category_text="BCSE309L: CRYPTOGRAPHY & NETWORK SECURITY | VIT CHENNAI"):
        hdr_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.95))
        tf = hdr_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p_cat = tf.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = "Arial"
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = C_CYAN
        p_cat.space_after = Pt(2)

        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = "Arial"
        p_title.font.size = Pt(20)
        p_title.font.bold = True
        p_title.font.color.rgb = C_NAVY

    def add_card(slide, left, top, width, height, bg_color=C_LIGHT_BG, border_color=C_BORDER):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.2)
        return shape

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (DARK PREMIUM)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_NAVY
    bg1.line.fill.background()

    tb1 = slide1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.333), Inches(5.2))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "VELLORE INSTITUTE OF TECHNOLOGY (VIT), CHENNAI"
    p0.font.name = "Arial"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = C_CYAN
    p0.space_after = Pt(6)

    p1 = tf1.add_paragraph()
    p1.text = "BCSE309L — Cryptography and Network Security | Review 3 Final Evaluation"
    p1.font.name = "Arial"
    p1.font.size = Pt(13)
    p1.font.color.rgb = C_MUTED
    p1.space_after = Pt(18)

    p2 = tf1.add_paragraph()
    p2.text = "BAMKS-D: Enabling Dynamic File-Level Operations in Blockchain-Assisted ABKS for Cloud-Edge-IoT"
    p2.font.name = "Arial"
    p2.font.size = Pt(25)
    p2.font.bold = True
    p2.font.color.rgb = C_WHITE
    p2.space_after = Pt(14)

    p3 = tf1.add_paragraph()
    p3.text = "An Algorithmic Prototype & Architecture Integration Layer Resolving Section 8 of Cheng et al. (Elsevier IoT 2026)"
    p3.font.name = "Arial"
    p3.font.size = Pt(14)
    p3.font.italic = True
    p3.font.color.rgb = RGBColor(148, 163, 184)
    p3.space_after = Pt(28)

    p4 = tf1.add_paragraph()
    p4.text = "Student Researchers:\n• Prashant Singh (Reg. No: 24BYB1042) — Protocol Simulation, Dynamic Indexing & REST API\n• Rushikesh Adak (Reg. No: 24BYB1055) — Solidity Smart Contracts, EVM Gas Analysis & Web3 Integration\n\nFaculty Guide: Prof. Karthika V | School of Computer Science & Engineering (SCOPE)"
    p4.font.name = "Arial"
    p4.font.size = Pt(12)
    p4.font.color.rgb = C_WHITE

    # =========================================================================
    # SLIDE 2: RESEARCH CONTEXT & PROBLEM MOTIVATION
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Research Context: Healthcare IoT & Encrypted Search")

    cards2 = [
        ("Cloud-Edge Healthcare IoT", 
         "• IoMT telemetry (ECG, vitals, MRI scans) requires secure cloud archiving.\n• Regulatory compliance (HIPAA, GDPR) mandates end-to-end encryption.\n• Challenge: Cloud servers must enable search without learning plaintexts.",
         Inches(0.8), Inches(1.6), C_BLUE),
        ("Attribute-Based Keyword Search", 
         "• CP-ABE embeds access policies directly inside ciphertexts.\n• Clinicians decrypt only if their credentials satisfy access policies.\n• Conjunctive multi-keyword trapdoors enable multi-attribute diagnosis queries.",
         Inches(4.8), Inches(1.6), C_CYAN),
        ("Blockchain Result Verifiability", 
         "• Dishonest CSPs may return incomplete or stale search results.\n• Smart contracts verify aggregated Schnorr NIZK proofs.\n• Ethereum acts as an immutable arbiter enforcing state integrity.",
         Inches(8.8), Inches(1.6), C_GREEN)
    ]
    for title, desc, left, top, color in cards2:
        add_card(slide2, left, top, Inches(3.7), Inches(5.3), bg_color=C_LIGHT_BG, border_color=color)
        tb = slide2.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), Inches(3.3), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.bold = True
        pt.font.size = Pt(15)
        pt.font.color.rgb = color
        pt.space_after = Pt(10)
        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.size = Pt(11.5)
        pd.font.color.rgb = C_DARK_TXT

    # =========================================================================
    # SLIDE 3: RESEARCH GAP IN BASE PAPER (CHENG ET AL. 2026)
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Research Gap: The Open Challenge in Cheng et al. (Section 8)")

    add_card(slide3, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=RGBColor(254, 242, 242), border_color=C_RED)
    tb_gap = slide3.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_gap = tb_gap.text_frame
    tf_gap.word_wrap = True
    p = tf_gap.paragraphs[0]
    p.text = "Foundational Limitation in Base BAMKS [1]"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_RED
    p.space_after = Pt(10)
    gap_points = [
        ("Base Paper Architecture:", "Cheng et al. (Elsevier IoT, 2026) successfully established multi-authority ABE and blockchain result verification."),
        ("Monolithic Collection Overhead:", "Section 5.10 specifies index updates by multiplying X_upd across all L*m existing index entries (O(L*m)). Alternatively, full re-indexing requires re-encrypting all files."),
        ("Prohibitive at Scale:", "For L = 5,000 files and m = 3 keywords, updating 15,000 entries consumes significant computation for every single file appended."),
        ("Explicit Research Call:", "Section 8 explicitly identifies fine-grained dynamic file updates as an open research question.")
    ]
    for gt, gd in gap_points:
        pg = tf_gap.add_paragraph()
        pg.text = f"• {gt}"
        pg.font.bold = True
        pg.font.size = Pt(11.5)
        pg.font.color.rgb = C_NAVY
        pgd = tf_gap.add_paragraph()
        pgd.text = f"  {gd}"
        pgd.font.size = Pt(10.5)
        pgd.font.color.rgb = C_DARK_TXT
        pgd.space_after = Pt(4)

    add_card(slide3, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=RGBColor(240, 253, 244), border_color=C_GREEN)
    tb_sol = slide3.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_sol = tb_sol.text_frame
    tf_sol.word_wrap = True
    p = tf_sol.paragraphs[0]
    p.text = "The Proposed BAMKS-D Resolution"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(10)
    sol_points = [
        ("Atomic SingleDocAdd (O(m)):", "Decouples the inverted keyword index so appending a record requires generating tokens only for its m keywords (~0.67 ms flat at L=5,000)."),
        ("Instant SingleDocDelete (O(1)):", "Solidity hash mapping (deletedDocRegistry) executes constant-time revocation with zero array traversal."),
        ("Fair Baseline Comparison:", "Evaluates speedup against both naive re-encryption and true Cheng et al. Section 5.10 index updates across 30 runs."),
        ("Live Web3 Sepolia Deployment:", "Smart contract deployed and verified on Ethereum Sepolia Testnet with real transaction receipts.")
    ]
    for st, sd in sol_points:
        ps = tf_sol.add_paragraph()
        ps.text = f"✓ {st}"
        ps.font.bold = True
        ps.font.size = Pt(11.5)
        ps.font.color.rgb = C_NAVY
        psd = tf_sol.add_paragraph()
        psd.text = f"  {sd}"
        psd.font.size = Pt(10.5)
        psd.font.color.rgb = C_DARK_TXT
        psd.space_after = Pt(4)

    # =========================================================================
    # SLIDE 4: SYSTEM ARCHITECTURE & TOPOLOGY
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "BAMKS-D System Architecture & Seven-Entity Topology")

    arch_img = os.path.join(diagrams_dir, "diagram_architecture.png")
    if os.path.exists(arch_img):
        slide4.shapes.add_picture(arch_img, Inches(0.8), Inches(1.6), width=Inches(7.0))

    add_card(slide4, Inches(8.1), Inches(1.6), Inches(4.4), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_ent = slide4.shapes.add_textbox(Inches(8.3), Inches(1.75), Inches(4.0), Inches(5.0))
    tf_ent = tb_ent.text_frame
    tf_ent.word_wrap = True
    p = tf_ent.paragraphs[0]
    p.text = "Seven System Entities"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(8)

    entities = [
        ("1. KGC:", "Initializes global parameters and master secrets."),
        ("2. AA (Authorities):", "Issue attribute private keys to clinical users."),
        ("3. Data Owners:", "Encrypt EHRs, upload to IPFS, compute index tokens."),
        ("4. Data Users:", "Generate search trapdoors and decrypt matching EHRs."),
        ("5. CSP (Cloud):", "Maintains inverted index and executes conjunctive matching."),
        ("6. Ethereum Sepolia:", "Smart contract enforcing instant deletion registry."),
        ("7. IPFS / Pinata:", "Content-addressed storage for encrypted medical files.")
    ]
    for en, ed in entities:
        pe = tf_ent.add_paragraph()
        pe.text = f"{en} {ed}"
        pe.font.size = Pt(10.5)
        pe.font.color.rgb = C_DARK_TXT
        pe.space_after = Pt(4)

    # =========================================================================
    # SLIDE 5: DYNAMIC ADDITION: SINGLEDOCADD (O(m))
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Atomic File Ingestion: SingleDocAdd Protocol (O(m))")

    add_card(slide5, Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_add = slide5.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.6), Inches(5.0))
    tf_add = tb_add.text_frame
    tf_add.word_wrap = True
    p = tf_add.paragraphs[0]
    p.text = "SingleDocAdd: Decoupled Index Ingestion"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(8)

    steps_add = [
        ("Step 1: AES-256-GCM Payload Encryption", "Key derived via KDF(Phi, verId). Encrypts file payload with fresh 96-bit nonce."),
        ("Step 2: IPFS Decentralized Pinning", "Uploads encrypted payload to IPFS, retrieving content identifier (CID)."),
        ("Step 3: Keyword Index Token Generation", "For each keyword w_j in W_doc:\n  I_doc,j = g^(eta * H1(w_j)) mod P\nComputes index key Key_j = H2('tok_' || I_doc,j)."),
        ("Step 4: Autonomous Index Append", "Appends index tokens to cloud index. Zero existing documents are touched."),
        ("Step 5: On-Chain Root Registration", "Calls registerDocument(docId, fileHash, publicTag) on Sepolia contract.")
    ]
    for s_t, s_d in steps_add:
        ps = tf_add.add_paragraph()
        ps.text = f"• {s_t}"
        ps.font.bold = True
        ps.font.size = Pt(11.5)
        ps.font.color.rgb = C_NAVY
        psd = tf_add.add_paragraph()
        psd.text = f"  {s_d}"
        psd.font.size = Pt(10.5)
        psd.font.color.rgb = C_DARK_TXT
        psd.space_after = Pt(4)

    enc_img = os.path.join(diagrams_dir, "encryption_flow.jpg")
    if os.path.exists(enc_img):
        slide5.shapes.add_picture(enc_img, Inches(7.1), Inches(1.6), width=Inches(5.4))

    # =========================================================================
    # SLIDE 6: INSTANT REVOCATION: SINGLEDOCDELETE (O(1))
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Instant File Revocation: SingleDocDelete & EVM Mapping")

    add_card(slide6, Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_CYAN)
    tb_del = slide6.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.6), Inches(5.0))
    tf_del = tb_del.text_frame
    tf_del.word_wrap = True
    p = tf_del.paragraphs[0]
    p.text = "SingleDocDelete: Strict O(1) Solidity Revocation"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(8)

    del_points = [
        ("Why Array Traversal Fails on Blockchain:", "Iterating arrays on-chain scales linearly (O(N) gas), risking transaction failure as N expands."),
        ("Solidity Hash-Table State Mapping:", "BAMKS_Registry.sol uses:\n`mapping(uint256 => bool) public deletedDocRegistry;`\nEVM mappings do NOT iterate over array elements."),
        ("Direct EVM Keccak256 Slot Addressing:", "EVM computes storage location directly:\nSlot = keccak256(abi.encode(docId, slotNumber))\nSets boolean true in a single storage write."),
        ("RVSC Invariant Enforcement:", "Smart contract enforces `require(!deletedDocRegistry[id])`, ensuring revoked documents cannot be returned.")
    ]
    for dp_t, dp_d in del_points:
        pdp = tf_del.add_paragraph()
        pdp.text = f"• {dp_t}"
        pdp.font.bold = True
        pdp.font.size = Pt(11.5)
        pdp.font.color.rgb = C_NAVY
        pdpd = tf_del.add_paragraph()
        pdpd.text = f"  {dp_d}"
        pdpd.font.size = Pt(10.5)
        pdpd.font.color.rgb = C_DARK_TXT
        pdpd.space_after = Pt(4)

    rev_img = os.path.join(diagrams_dir, "revocation_mechanism.jpg")
    if os.path.exists(rev_img):
        slide6.shapes.add_picture(rev_img, Inches(7.1), Inches(1.6), width=Inches(5.4))

    # =========================================================================
    # SLIDE 7: CONJUNCTIVE SEARCH & MATCHING
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Conjunctive Multi-Keyword Search & Algebraic Matching")

    add_card(slide7, Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_srch = slide7.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.6), Inches(5.0))
    tf_srch = tb_srch.text_frame
    tf_srch.word_wrap = True
    p = tf_srch.paragraphs[0]
    p.text = "Algebraic Match Evaluation"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(8)

    srch_points = [
        ("Query Trapdoor Generation:", "User samples session secret phi in Z_P* and computes:\n  T1 = g^phi mod P\n  T3 = g^(phi * sum(H1(w~_j))) mod P"),
        ("Cloud Modular Evaluation (Eq. 6):", "Cloud server aggregates candidate index tokens:\n  I_prod = prod(I_doc,j) mod P\nAnd verifies the algebraic equality:\n  (I_prod)^phi == (T3)^eta mod P"),
        ("Soundness Guarantee:", "Equality holds if and only if the document contains ALL q query keywords. Mismatched queries evaluate false with high probability."),
        ("Schnorr NIZK Aggregation:", "Off-chain proof (R, pi_hat) guarantees search correctness without exposing clinician attributes.")
    ]
    for sp_t, sp_d in srch_points:
        psp = tf_srch.add_paragraph()
        psp.text = f"• {sp_t}"
        psp.font.bold = True
        psp.font.size = Pt(11.5)
        psp.font.color.rgb = C_NAVY
        pspd = tf_srch.add_paragraph()
        pspd.text = f"  {sp_d}"
        pspd.font.size = Pt(10.5)
        pspd.font.color.rgb = C_DARK_TXT
        pspd.space_after = Pt(4)

    srch_img = os.path.join(diagrams_dir, "search_decrypt_flow.jpg")
    if os.path.exists(srch_img):
        slide7.shapes.add_picture(srch_img, Inches(7.1), Inches(1.6), width=Inches(5.4))

    # =========================================================================
    # SLIDE 8: ATTRIBUTE-BASED ACCESS CONTROL
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Attribute-Based Access Control (CP-ABE Policy Modeling)")

    add_card(slide8, Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_GREEN)
    tb_abe = slide8.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.6), Inches(5.0))
    tf_abe = tb_abe.text_frame
    tf_abe.word_wrap = True
    p = tf_abe.paragraphs[0]
    p.text = "Access Policy Modeling & Evaluation"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(8)

    abe_points = [
        ("Access Policy Binding:", "Every clinical document is bound to an access policy (e.g., Role_Doctor AND Dept_Cardiology)."),
        ("Attribute Authority Secret Delegation:", "AAs manage distinct attribute sets and issue private keys to verified clinicians."),
        ("Simulated Policy Checking (Prototype Scope):", "In this software prototype, policy satisfaction is evaluated via attribute set evaluation logic before payload decryption."),
        ("Empirical Test Suite Validation (Test C):", "• Dr. Prashant [Doctor, Cardiology] -> Access Granted (Decrypted).\n• Nurse Anita [Nurse, GeneralWard] -> Access Denied (Policy Mismatch)."),
        ("Collusion Resistance Invariant:", "Session randomness t in KeyGen prevents unauthorized users from combining keys.")
    ]
    for ap_t, ap_d in abe_points:
        pap = tf_abe.add_paragraph()
        pap.text = f"• {ap_t}"
        pap.font.bold = True
        pap.font.size = Pt(11.5)
        pap.font.color.rgb = C_NAVY
        papd = tf_abe.add_paragraph()
        papd.text = f"  {ap_d}"
        papd.font.size = Pt(10.5)
        papd.font.color.rgb = C_DARK_TXT
        papd.space_after = Pt(4)

    abe_img = os.path.join(diagrams_dir, "cpabe_access_control.jpg")
    if os.path.exists(abe_img):
        slide8.shapes.add_picture(abe_img, Inches(7.1), Inches(1.6), width=Inches(5.4))

    # =========================================================================
    # SLIDE 9: FAIR BENCHMARK: CHENG ET AL. VS. BAMKS-D (30 RUNS)
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Empirical Benchmark: Naive vs. Cheng et al. vs. BAMKS-D")

    chart_path = os.path.join(diagrams_dir, "chart_scalability_multi_n.png")
    if os.path.exists(chart_path):
        slide9.shapes.add_picture(chart_path, Inches(0.8), Inches(1.6), width=Inches(6.2))

    table_shape = slide9.shapes.add_table(6, 5, Inches(7.2), Inches(1.6), Inches(5.3), Inches(3.6))
    tbl = table_shape.table
    tbl.columns[0].width = Inches(1.0)
    tbl.columns[1].width = Inches(1.2)
    tbl.columns[2].width = Inches(1.2)
    tbl.columns[3].width = Inches(1.0)
    tbl.columns[4].width = Inches(0.9)

    headers = ["L (Files)", "Naive Re-enc", "Cheng et al. [1]", "BAMKS-D", "Speedup"]
    for i, h in enumerate(headers):
        cell = tbl.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_BLUE
        p = cell.text_frame.paragraphs[0]
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = C_WHITE

    bench_rows = [
        ("L = 50", "20.31 ms", "0.084 ms", "0.409 ms", "0.21x"),
        ("L = 100", "42.89 ms", "0.164 ms", "0.447 ms", "0.37x"),
        ("L = 500", "228.79 ms", "0.816 ms", "0.533 ms", "1.53x"),
        ("L = 1,000", "467.08 ms", "1.559 ms", "0.486 ms", "3.20x"),
        ("L = 5,000", "2,363.01 ms", "8.112 ms", "0.670 ms", "12.11x")
    ]
    for r_idx, r_data in enumerate(bench_rows, start=1):
        for c_idx, val in enumerate(r_data):
            cell = tbl.cell(r_idx, c_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(236, 254, 255) if c_idx == 4 else (C_WHITE if r_idx % 2 == 1 else C_CARD_ALT)
            p = cell.text_frame.paragraphs[0]
            p.font.name = "Arial"
            p.font.size = Pt(9)
            p.font.color.rgb = C_BLUE if c_idx == 4 else C_DARK_TXT
            if c_idx == 4:
                p.font.bold = True

    add_card(slide9, Inches(7.2), Inches(5.4), Inches(5.3), Inches(1.5), bg_color=RGBColor(240, 253, 244), border_color=C_GREEN)
    tb_stat = slide9.shapes.add_textbox(Inches(7.35), Inches(5.45), Inches(5.0), Inches(1.4))
    tf_stat = tb_stat.text_frame
    tf_stat.word_wrap = True
    ps0 = tf_stat.paragraphs[0]
    ps0.text = "HONEST BENCHMARK ANALYSIS (m=3, 30 Runs, Intel i5-13420H):"
    ps0.font.bold = True
    ps0.font.size = Pt(10)
    ps0.font.color.rgb = C_GREEN
    ps1 = tf_stat.add_paragraph()
    ps1.text = "• For L <= 100, Cheng et al. index multiplication is faster than single-file AES encryption.\n• Break-even crossover occurs at L in [300, 410] files (L ~ 300 via local interpolation, L ~ 410 asymptotically against L=5,000).\n• At L=5,000, BAMKS-D achieves 12.11x speedup over Cheng et al. (and 3,527.7x over naive re-encryption)."
    ps1.font.size = Pt(9.5)
    ps1.font.color.rgb = C_DARK_TXT

    # =========================================================================
    # SLIDE 10: EVM GAS ANALYSIS: THEORETICAL SCHEDULE & LIVE SEPOLIA RECEIPTS
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "EVM Gas Schedule & Verified Ethereum Sepolia Receipts")

    add_card(slide10, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_p1 = slide10.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_p1 = tb_p1.text_frame
    tf_p1.word_wrap = True
    p = tf_p1.paragraphs[0]
    p.text = "Opcode Schedule & EVM Measurement"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(8)

    proof_points = [
        ("Base Transaction Fee:", "21,000 gas (Standard EVM baseline)."),
        ("CALLDATALOAD + KECCAK256:", "3 + 30 gas (Direct slot calculation: keccak256(docId, slotNumber))."),
        ("SSTORE (deletedDocRegistry):", "20,000 gas (0 to 1 cold slot storage write)."),
        ("SSTORE (fileRegistry.isDeleted):", "5,000 gas (Warm slot update on existing metadata struct)."),
        ("LOG3 (DocumentDeleted):", "1,500 gas (Event base + 3 indexed topics + timestamp)."),
        ("Overhead (JUMP, stack):", "~200 gas -> Theoretical Minimum: ~47,733 gas."),
        ("Measured EVM Gas (O(1)):", "72,794 gas at N=10; 72,794 at N=100; 72,806 at N=1,000 (Strictly O(1)).")
    ]
    for pp_t, pp_d in proof_points:
        ppp = tf_p1.add_paragraph()
        ppp.text = f"• {pp_t}"
        ppp.font.bold = True
        ppp.font.size = Pt(10.5)
        ppp.font.color.rgb = C_NAVY
        pppd = tf_p1.add_paragraph()
        pppd.text = f"  {pp_d}"
        pppd.font.size = Pt(9.5)
        pppd.font.color.rgb = C_DARK_TXT
        pppd.space_after = Pt(2)

    add_card(slide10, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_CYAN)
    tb_p2 = slide10.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_p2 = tb_p2.text_frame
    tf_p2.word_wrap = True
    p = tf_p2.paragraphs[0]
    p.text = "Live Mined Receipts on Ethereum Sepolia"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(8)

    rec_points = [
        ("Contract Address:", "0xfDC8615Bf6483c3B0f39c330F55A56Cb0f08C8D3 (solc 0.8.20)"),
        ("Deployment Transaction:", "Tx: 0x1f058b... in Block #11975268\nGas Used: 6,889,229 gas units"),
        ("deleteDocument(101) Receipt:", "Tx: 0x008330... in Block #11975278\nReceipt Gas: 242,834 gas | Confirmation: 21.83 s"),
        ("registerDocument(101) Receipt:", "Tx: 0x363d3e... in Block #11975277\nReceipt Gas: 792,245 gas | Confirmation: 35.22 s"),
        ("Why Real Gas Exceeds Opcode Minima:", "Solidity function selector hashing, memory allocation, struct ABI encoding, and non-optimized compiler dispatch overhead.")
    ]
    for rp_t, rp_d in rec_points:
        prp = tf_p2.add_paragraph()
        prp.text = f"• {rp_t}"
        prp.font.bold = True
        prp.font.size = Pt(11)
        prp.font.color.rgb = C_NAVY
        prpd = tf_p2.add_paragraph()
        prpd.text = f"  {rp_d}"
        prpd.font.size = Pt(10)
        prpd.font.color.rgb = C_DARK_TXT
        prpd.space_after = Pt(3)

    # =========================================================================
    # SLIDE 11: AUTOMATED SECURITY & CORRECTNESS TESTING
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Automated Security & Correctness Verification Suite")

    sec_cards = [
        ("Test A: Soundness & Trapdoor Isolation",
         "• Query for 'Dermatology' against Cardiology/Oncology docs returns 0 documents.\n• Conjunctive mismatch: Query ['Cardiology', 'Tumor'] returns 0 documents.\n• Valid query ['Cardiology', 'ECG'] matches exactly Doc #101.\n• Proves zero false-positives under wrong trapdoors.",
         Inches(0.8), Inches(1.6), C_BLUE),
        ("Test B: On-Chain Deletion RVSC Invariant",
         "• Executed single_doc_delete(101) setting deletedDocRegistry[101] = true.\n• Search query for ['Cardiology', 'ECG'] skips Doc #101 instantly.\n• Proves non-revocation invariant: Revoked records are excluded from result sets.",
         Inches(6.8), Inches(1.6), C_CYAN),
        ("Test C: CP-ABE Attribute Access Control",
         "• Dr. Prashant with attributes ['Role_Doctor', 'Dept_Cardiology'] decrypts record.\n• Nurse Anita with attributes ['Role_Nurse'] evaluates FALSE.\n• Output: [CP-ABE ACCESS DENIED: Requires (Role_Doctor AND Dept_Cardiology)].",
         Inches(0.8), Inches(4.3), C_GREEN),
        ("Test D & E: Batch Addition & Index Storage Scaling",
         "• single_doc_add_batch processes 4 clinical records in 0.852 ms (~0.21 ms/doc flat).\n• Inverted index storage scales strictly linearly at 452.0 bytes per added document.\n• Baseline 8 records: 4,098 bytes (512.2 B/doc including schema metadata).",
         Inches(6.8), Inches(4.3), C_AMBER)
    ]
    for title, desc, left, top, color in sec_cards:
        add_card(slide11, left, top, Inches(5.7), Inches(2.5), bg_color=C_LIGHT_BG, border_color=color)
        tb = slide11.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), Inches(5.3), Inches(2.2))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.bold = True
        pt.font.size = Pt(13)
        pt.font.color.rgb = color
        pt.space_after = Pt(4)
        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.size = Pt(10.5)
        pd.font.color.rgb = C_DARK_TXT

    # =========================================================================
    # SLIDE 12: LIVE ETHEREUM SEPOLIA & PINATA IPFS AUDIT
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_header(slide12, "Production Web3 Deployment: Sepolia & IPFS Audit")

    add_card(slide12, Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_w3 = slide12.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.6), Inches(4.9))
    tf_w3 = tb_w3.text_frame
    tf_w3.word_wrap = True
    p = tf_w3.paragraphs[0]
    p.text = "Verified On-Chain Deployment Artifacts"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(8)

    w3_items = [
        ("Smart Contract Address", "0xfDC8615Bf6483c3B0f39c330F55A56Cb0f08C8D3"),
        ("Deployment Transaction", "0x1f058bde75b20c2d1ce513897d77d70f47a2951cbcc83d9bc45a573116bf0dbf"),
        ("Deployment Block & Gas", "Block #11975268 | Gas Used: 6,889,229"),
        ("Target Network", "Ethereum Sepolia Testnet (Chain ID: 11155111)"),
        ("registerDocument(101) Tx", "0x363d3e8867adb49a2657b798ebb26990a5d0011ec5ddaf7de267ff191dc40ad7"),
        ("deleteDocument(101) Tx", "0x008330a08b3ad8926b19de8dc0a1b386b95712dc55077e33df2a36685c876e8d"),
        ("Pinata IPFS Gateway CID", "bafkreiegat25m4vgoltbz5l5wtvka7ipm4osl7xtyryhbg643ihctznluq"),
        ("Public GitHub Repo", "https://github.com/Prashant8991/BAMKS.git")
    ]
    for label, val in w3_items:
        pw = tf_w3.add_paragraph()
        pw.text = f"• {label}:\n  {val}"
        pw.font.size = Pt(9.5)
        pw.font.bold = True if "0x" in val else False
        pw.font.color.rgb = C_NAVY if "0x" in val else C_DARK_TXT
        pw.space_after = Pt(2)

    bc_img = os.path.join(diagrams_dir, "blockchain_role.jpg")
    if os.path.exists(bc_img):
        slide12.shapes.add_picture(bc_img, Inches(7.1), Inches(1.6), width=Inches(5.4))

    # =========================================================================
    # SLIDE 13: CLINICAL EHR DATASET & WEB APPLICATION DASHBOARD
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    add_header(slide13, "Clinical EHR Corpus & Interactive Clinician Dashboard")

    add_card(slide13, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_ds = slide13.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_ds = tb_ds.text_frame
    tf_ds.word_wrap = True
    p = tf_ds.paragraphs[0]
    p.text = "Multi-Specialty Clinical EHR Corpus"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(8)

    ehr_cases = [
        ("Doc #201 (Cardiology)", "STEMI Acute Infarction 12-lead ECG telemetry text."),
        ("Doc #202 (Cardiology)", "24-hour Holter ventricular tachycardia JSON stream."),
        ("Doc #203 (Neurology)", "3T cranial brain MRI, temporal sclerosis report."),
        ("Doc #204 (Neurology)", "Stroke perfusion biomarker lab CSV data."),
        ("Doc #205 (Oncology)", "Histopathology breast biopsy, HER2/ER/PR pathology."),
        ("Doc #207 (Pediatrics)", "Childhood immunization vitals and vaccination table."),
        ("Doc #209 (Discharge)", "Comprehensive multi-departmental inpatient summary.")
    ]
    for c_id, c_desc in ehr_cases:
        p_c = tf_ds.add_paragraph()
        p_c.text = f"• {c_id}: {c_desc}"
        p_c.font.size = Pt(10.5)
        p_c.font.color.rgb = C_DARK_TXT
        p_c.space_after = Pt(3)

    add_card(slide13, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_GREEN)
    tb_ui = slide13.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_ui = tb_ui.text_frame
    tf_ui.word_wrap = True
    p = tf_ui.paragraphs[0]
    p.text = "Interactive Clinician Dashboard (app.py)"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(8)

    ui_features = [
        ("Identity Switcher:", "Switch between Attending Physician (Dr. Prashant) and Staff Nurse (Nurse Anita) with dynamic attribute tokens."),
        ("Multi-Keyword Search:", "Input medical keywords ('Cardiology', 'ECG'); executes conjunctive match and renders decrypted records."),
        ("One-Click On-Chain Revocation:", "Revoke any record; updates on-chain registry and excludes record from search in real time."),
        ("Single-File & Batch Ingestion:", "Encrypts and uploads files to IPFS and adds index tokens in O(m) time."),
        ("Live Telemetry Panel:", "Visualizes real-time execution milliseconds and latency metrics directly in browser.")
    ]
    for uf_t, uf_d in ui_features:
        p_uf = tf_ui.add_paragraph()
        p_uf.text = f"✓ {uf_t}"
        p_uf.font.bold = True
        p_uf.font.size = Pt(11)
        p_uf.font.color.rgb = C_NAVY
        p_ufd = tf_ui.add_paragraph()
        p_ufd.text = f"  {uf_d}"
        p_ufd.font.size = Pt(10)
        p_ufd.font.color.rgb = C_DARK_TXT
        p_ufd.space_after = Pt(3)

    # =========================================================================
    # SLIDE 14: PROTOTYPE SCOPE, ASSUMPTIONS & LIMITATIONS
    # =========================================================================
    slide14 = prs.slides.add_slide(blank_layout)
    add_header(slide14, "Prototype Scope, Assumptions & Threats to Validity")

    add_card(slide14, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_AMBER)
    tb_lim = slide14.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.133), Inches(4.9))
    tf_lim = tb_lim.text_frame
    tf_lim.word_wrap = True
    p = tf_lim.paragraphs[0]
    p.text = "Transparent Limitations & Architectural Trade-offs"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_AMBER
    p.space_after = Pt(10)

    lim_items = [
        ("1. Simulated Group Algebra:", "Field operations evaluated in (Z_P*, *) with secp256k1 prime P. Order is P-1 (composite); pairing e(g,g) is simulated via modular exponentiation. Production deployment requires Type-III pairing groups (e.g., BN254 / BLS12-381)."),
        ("2. CSP Search Separation in Prototype:", "In the demonstration test script, the CSP receives eta and phi directly to evaluate modular match equations. Production pairing eliminates this requirement."),
        ("3. Inverted Index Access-Pattern Leakage:", "Keyword tokens I_doc,j = g^(eta * H1(w_j)) are deterministic across documents. The CSP can observe document frequency and search patterns over time. Forward-private DSSE is future work."),
        ("4. Simulated Policy Checking:", "CP-ABE access policy satisfaction is evaluated via attribute set evaluation rather than full algebraic LSSS pairing engine."),
        ("5. Local vs. On-Chain Deletion Latency:", "Local flag updates take < 0.001 ms in memory; real Ethereum Sepolia block mining takes 21.83 s for deletion confirmation.")
    ]
    for lt, ld in lim_items:
        pl = tf_lim.add_paragraph()
        pl.text = f"• {lt} "
        pl.font.bold = True
        pl.font.size = Pt(11.5)
        pl.font.color.rgb = C_NAVY
        pld = tf_lim.add_paragraph()
        pld.text = f"  {ld}"
        pld.font.size = Pt(10.5)
        pld.font.color.rgb = C_DARK_TXT
        pld.space_after = Pt(5)

    # =========================================================================
    # SLIDE 15: CONCLUSION & RESEARCH SUMMARY
    # =========================================================================
    slide15 = prs.slides.add_slide(blank_layout)
    add_header(slide15, "Conclusion & Summary of Research Contributions")

    add_card(slide15, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_c = slide15.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.133), Inches(4.9))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True
    p = tf_c.paragraphs[0]
    p.text = "Summary of Key Contributions"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(10)

    concl_points = [
        ("1. Addressed Section 8 Base Paper Research Gap:", "Formulated an atomic file-level update mechanism for BAMKS, eliminating collection-wide re-keying bottlenecks."),
        ("2. Demonstrated Empirical Speedup (12.11x):", "SingleDocAdd runs in O(m) time (~0.67 ms at L=5,000), achieving a 12.11x speedup over Cheng et al. Section 5.10 index updates (and 3,527.7x over naive full re-encryption)."),
        ("3. On-Chain EVM Mapping Revocation (O(1)):", "Solidity deletedDocRegistry mapping executes in constant time via keccak256 slot calculation with zero array traversal."),
        ("4. Live Ethereum Sepolia Deployment:", "Smart contract deployed and verified on public Ethereum Sepolia Testnet (0xfDC8615Bf6483c3B0f39c330F55A56Cb0f08C8D3) with live mined transaction receipts."),
        ("5. Open-Source Reproducibility:", "Complete source code, contracts, clinical dataset, and test scripts available at https://github.com/Prashant8991/BAMKS.git.")
    ]
    for num, txt in concl_points:
        p_item = tf_c.add_paragraph()
        p_item.text = f"• {num} "
        p_item.font.bold = True
        p_item.font.size = Pt(11.5)
        p_item.font.color.rgb = C_NAVY
        p_desc = tf_c.add_paragraph()
        p_desc.text = f"  {txt}"
        p_desc.font.size = Pt(10.5)
        p_desc.font.color.rgb = C_DARK_TXT
        p_desc.space_after = Pt(5)

    # =========================================================================
    # SLIDE 16: KEY ACADEMIC REFERENCES
    # =========================================================================
    slide16 = prs.slides.add_slide(blank_layout)
    add_header(slide16, "Key Academic References (IEEE Citation Format)")

    add_card(slide16, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BORDER)
    tb_ref = slide16.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.133), Inches(4.9))
    tf_ref = tb_ref.text_frame
    tf_ref.word_wrap = True
    p = tf_ref.paragraphs[0]
    p.text = "Key Academic References"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(10)

    refs = [
        "[1] H. Cheng, S.-L. Lo, and J. Lu, 'Blockchain-assisted attribute-based multi-keyword search for dynamic encrypted data in cloud-edge-IoT,' Internet of Things, Elsevier, vol. 36, Art. no. 101838, 2026. DOI: 10.1016/j.iot.2025.101838. (BASE PAPER)",
        "[2] D. Boneh, G. Di Crescenzo, R. Ostrovsky, and G. Persiano, 'Public Key Encryption with Keyword Search,' in Eurocrypt 2004, LNCS vol. 3027, Springer, pp. 506–522.",
        "[3] J. Bethencourt, A. Sahai, and B. Waters, 'Ciphertext-Policy Attribute-Based Encryption,' in IEEE Symposium on Security and Privacy (S&P), 2007, pp. 321–334.",
        "[4] C. P. Schnorr, 'Efficient signature generation by smart cards,' Journal of Cryptology, vol. 4, no. 3, pp. 161–174, 1991.",
        "[5] G. Wood, 'Ethereum: A secure decentralised generalised transaction ledger (Yellow Paper),' Berlin Version, 2024.",
        "[6] J. Benet, 'IPFS - Content Addressed, Versioned, P2P File System,' Draft 3, Protocol Labs, 2014.",
        "[7] R. Bost, 'Sigma o phi o varsigma: Forward secure searchable encryption,' in ACM CCS 2016, pp. 1143–1154."
    ]
    for r in refs:
        pr = tf_ref.add_paragraph()
        pr.text = r
        pr.font.size = Pt(10)
        pr.font.color.rgb = C_BLUE if "BASE PAPER" in r else C_DARK_TXT
        if "BASE PAPER" in r:
            pr.font.bold = True
        pr.space_after = Pt(6)

    prs.save(ppt_path)
    print(f"[SUCCESS] High-impact presentation generated: {ppt_path}")
    return ppt_path

if __name__ == '__main__':
    build_presentation()
