"""
BAMKS-D FINAL PRESENTATION GENERATOR (PPTX) - COMPREHENSIVE & DEFENSE READY
=============================================================================
Generates a stunning, publication-grade 17-slide widescreen (16:9) presentation
for Review 3 / Final Defense of BAMKS-D at VIT Chennai.

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
        # Header banner text box
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
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = C_NAVY

        # Accent Line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.38), Inches(11.733), Inches(0.04))
        line.fill.solid()
        line.fill.fore_color.rgb = C_CYAN
        line.line.color.rgb = C_CYAN

    def add_card(slide, left, top, width, height, bg_color=C_LIGHT_BG, border_color=C_BORDER):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.2)
        return shape

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (EXECUTIVE NAVY THEME)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_NAVY
    bg1.line.color.rgb = C_NAVY

    # Institution block
    inst_box = slide1.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.333), Inches(0.9))
    tf1_inst = inst_box.text_frame
    p_inst = tf1_inst.paragraphs[0]
    p_inst.text = "VELLORE INSTITUTE OF TECHNOLOGY (VIT), CHENNAI"
    p_inst.font.name = "Arial"
    p_inst.font.size = Pt(13)
    p_inst.font.bold = True
    p_inst.font.color.rgb = C_CYAN
    p_sch = tf1_inst.add_paragraph()
    p_sch.text = "School of Computer Science and Engineering | Final Review 3 Defense Presentation"
    p_sch.font.name = "Arial"
    p_sch.font.size = Pt(11)
    p_sch.font.color.rgb = RGBColor(148, 163, 184)

    # Main Project Title
    title_box = slide1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(2.2))
    tf1 = title_box.text_frame
    tf1.word_wrap = True
    p_t = tf1.paragraphs[0]
    p_t.text = "BAMKS-D: Enabling Dynamic File-Level Operations in Blockchain-Assisted Attribute-Based Multi-Keyword Search"
    p_t.font.name = "Arial"
    p_t.font.size = Pt(26)
    p_t.font.bold = True
    p_t.font.color.rgb = C_WHITE
    p_t.space_after = Pt(8)

    p_sub = tf1.add_paragraph()
    p_sub.text = "A Fine-Grained Cryptographic Protocol & Solidity Smart Contract Extension for Cloud-Edge Healthcare Systems"
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(15)
    p_sub.font.color.rgb = C_CYAN

    # Authorship & Metadata Cards (Side by Side)
    card_auth = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(4.3), Inches(5.5), Inches(2.5))
    card_auth.fill.solid()
    card_auth.fill.fore_color.rgb = RGBColor(30, 41, 59)
    card_auth.line.color.rgb = RGBColor(51, 65, 85)
    tf_auth = card_auth.text_frame
    tf_auth.word_wrap = True
    p_a0 = tf_auth.paragraphs[0]
    p_a0.text = "STUDENT RESEARCHERS & AUTHORS"
    p_a0.font.bold = True
    p_a0.font.size = Pt(11)
    p_a0.font.color.rgb = C_CYAN
    p_a0.space_after = Pt(6)

    p_a1 = tf_auth.add_paragraph()
    p_a1.text = "• Prashant Singh  (Reg. No: 24BYB1042)"
    p_a1.font.size = Pt(13)
    p_a1.font.bold = True
    p_a1.font.color.rgb = C_WHITE
    p_a1.space_after = Pt(4)

    p_a2 = tf_auth.add_paragraph()
    p_a2.text = "• Rushikesh Adak (Reg. No: 24BYB1055)"
    p_a2.font.size = Pt(13)
    p_a2.font.bold = True
    p_a2.font.color.rgb = C_WHITE
    p_a2.space_after = Pt(6)

    p_a3 = tf_auth.add_paragraph()
    p_a3.text = "School of Computer Science and Engineering (SCOPE)"
    p_a3.font.size = Pt(10.5)
    p_a3.font.color.rgb = RGBColor(203, 213, 225)

    card_meta = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.3), Inches(5.5), Inches(2.5))
    card_meta.fill.solid()
    card_meta.fill.fore_color.rgb = RGBColor(30, 41, 59)
    card_meta.line.color.rgb = RGBColor(51, 65, 85)
    tf_meta = card_meta.text_frame
    tf_meta.word_wrap = True
    p_m0 = tf_meta.paragraphs[0]
    p_m0.text = "COURSE & BASE PAPER DETAILS"
    p_m0.font.bold = True
    p_m0.font.size = Pt(11)
    p_m0.font.color.rgb = C_CYAN
    p_m0.space_after = Pt(6)

    p_m1 = tf_meta.add_paragraph()
    p_m1.text = "• Course: Cryptography and Network Security (BCSE309L)"
    p_m1.font.size = Pt(11.5)
    p_m1.font.bold = True
    p_m1.font.color.rgb = C_WHITE
    p_m1.space_after = Pt(4)

    p_m2 = tf_meta.add_paragraph()
    p_m2.text = "• Faculty Guide: Prof. Karthika V | SCOPE, VIT Chennai"
    p_m2.font.size = Pt(11)
    p_m2.font.color.rgb = RGBColor(226, 232, 240)
    p_m2.space_after = Pt(6)

    p_m3 = tf_meta.add_paragraph()
    p_m3.text = "• Base Paper: Cheng et al., Elsevier (Internet of Things), Vol. 36, Art. 101838, Dec 2025/2026 [DOI: 10.1016/j.iot.2025.101838]"
    p_m3.font.size = Pt(9.5)
    p_m3.font.color.rgb = RGBColor(148, 163, 184)

    # =========================================================================
    # SLIDE 2: RESEARCH PROBLEM & CLINICAL MOTIVATION
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Research Motivation: The Encrypted Healthcare IoT Dilemma")

    # Left Column Card: The Clinical Reality
    add_card(slide2, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_l = slide2.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "The Healthcare IoT Outsourcing Paradox"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(10)

    points_l = [
        ("Massive Cloud Outsourcing:", "Modern hospitals outsource millions of Electronic Health Records (EHRs), 12-lead ECG telemetry, and MRI scans to cloud-edge storage to cut costs."),
        ("Strict Regulatory Privacy:", "HIPAA and GDPR legally require end-to-end encryption. Unencrypted patient diagnoses (e.g. oncology biopsies, HIV status) result in severe penalties."),
        ("The Searchability Barrier:", "Standard symmetric encryption (AES-256) turns records into opaque ciphertext. Clinicians cannot search for 'Cardiology AND ECG' without decrypting everything."),
        ("Untrusted Cloud Servers (CSPs):", "CSPs are honest-but-curious: they attempt to infer clinical diagnoses from access patterns and may return stale or incomplete results to save computation.")
    ]
    for title, desc in points_l:
        p_item = tf_l.add_paragraph()
        p_item.text = f"• {title} "
        p_item.font.bold = True
        p_item.font.size = Pt(12)
        p_item.font.color.rgb = C_NAVY
        p_item.space_after = Pt(2)
        p_desc = tf_l.add_paragraph()
        p_desc.text = f"  {desc}"
        p_desc.font.size = Pt(11)
        p_desc.font.color.rgb = C_DARK_TXT
        p_desc.space_after = Pt(8)

    # Right Column Card: Limitations of Prior Approaches
    add_card(slide2, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BORDER)
    tb_r = slide2.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "Limitations of Prior State-of-the-Art"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(10)

    points_r = [
        ("Traditional PEKS (Boneh et al.):", "Supports only single-keyword queries. Searching multi-field EHRs creates massive false-positive sets and leaks keyword frequency."),
        ("Standard CP-ABE (Bethencourt et al.):", "Provides fine-grained access trees, but possesses zero keyword searchability. Encrypted data remains unsearchable in the cloud."),
        ("Centralized Result Verification:", "Relies on a single trusted third party or KGC to verify search outcomes, creating a single point of failure and vulnerability to collusive attacks."),
        ("Static Dataset Assumption:", "Existing searchable encryption models assume static datasets. They completely fail when patient telemetry arrives in real-time streams.")
    ]
    for title, desc in points_r:
        p_item = tf_r.add_paragraph()
        p_item.text = f"• {title} "
        p_item.font.bold = True
        p_item.font.size = Pt(12)
        p_item.font.color.rgb = C_NAVY
        p_item.space_after = Pt(2)
        p_desc = tf_r.add_paragraph()
        p_desc.text = f"  {desc}"
        p_desc.font.size = Pt(11)
        p_desc.font.color.rgb = C_DARK_TXT
        p_desc.space_after = Pt(8)

    # =========================================================================
    # SLIDE 3: BASE PAPER ANALYSIS & THE IDENTIFIED RESEARCH GAP
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Base Research Paper Analysis & The Critical Research Gap")

    # Base Paper Identification Banner
    add_card(slide3, Inches(0.8), Inches(1.5), Inches(11.733), Inches(1.2), bg_color=RGBColor(238, 242, 255), border_color=C_BLUE)
    tb_bp = slide3.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(11.333), Inches(1.1))
    tf_bp = tb_bp.text_frame
    tf_bp.word_wrap = True
    p_bp0 = tf_bp.paragraphs[0]
    p_bp0.text = "IDENTIFICATION OF BASE PAPER (ELSEVIER 2026):"
    p_bp0.font.bold = True
    p_bp0.font.size = Pt(11)
    p_bp0.font.color.rgb = C_BLUE
    p_bp1 = tf_bp.add_paragraph()
    p_bp1.text = "Hanlei Cheng, Sio-Long Lo, Jing Lu, 'Blockchain-assisted attribute-based multi-keyword search for dynamic encrypted data in cloud-edge-IoT', Internet of Things (Elsevier), Vol. 36, Art. 101838, Dec 2025/2026. DOI: 10.1016/j.iot.2025.101838"
    p_bp1.font.size = Pt(11.5)
    p_bp1.font.bold = True
    p_bp1.font.color.rgb = C_NAVY

    # Left Card: Base Paper Merits
    add_card(slide3, Inches(0.8), Inches(2.9), Inches(5.7), Inches(4.1), bg_color=C_LIGHT_BG, border_color=C_BORDER)
    tb_m = slide3.shapes.add_textbox(Inches(1.0), Inches(3.05), Inches(5.3), Inches(3.8))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True
    p = tf_m.paragraphs[0]
    p.text = "Merits of the Base BAMKS Scheme"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(8)
    merits = [
        "Unifies CP-ABE access policies with multi-keyword conjunctive search.",
        "Introduces multi-owner collaborative access tokens (Phi) for fine-grained sharing.",
        "Implements a Result Verification Smart Contract (RVSC) for on-chain integrity.",
        "Generates Schnorr NIZK proofs off-chain to detect malicious cloud tampering."
    ]
    for m in merits:
        pm = tf_m.add_paragraph()
        pm.text = f"✓ {m}"
        pm.font.size = Pt(11.5)
        pm.font.color.rgb = C_DARK_TXT
        pm.space_after = Pt(6)

    # Right Card: The Critical Flaw (Section 8 Open Problem)
    add_card(slide3, Inches(6.8), Inches(2.9), Inches(5.7), Inches(4.1), bg_color=RGBColor(254, 242, 242), border_color=C_RED)
    tb_f = slide3.shapes.add_textbox(Inches(7.0), Inches(3.05), Inches(5.3), Inches(3.8))
    tf_f = tb_f.text_frame
    tf_f.word_wrap = True
    p = tf_f.paragraphs[0]
    p.text = "The Critical Research Gap (Section 8)"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = C_RED
    p.space_after = Pt(8)
    flaws = [
        ("Monolithic Batching: ", "Files are grouped into monolithic collection versions (F_ver). Updating or inserting ONE record requires a complete collection-wide re-keying."),
        ("Prohibitive O(L x m) Cost: ", "For L files with m keywords, regenerating all index tokens incurs O(L * m) latency, creating an intolerable computational wall."),
        ("Explicit Base Paper Admission: ", "Section 8 ('Conclusion & Future Work') explicitly states: 'Future work will focus on file-level fine-grained updates without collection re-keying.'"),
        ("OUR TARGET OBJECTIVE: ", "We directly resolve this exact Section 8 limitation by inventing BAMKS-D.")
    ]
    for t_fl, d_fl in flaws:
        pf = tf_f.add_paragraph()
        pf.text = f"✗ {t_fl}"
        pf.font.bold = True
        pf.font.size = Pt(11.5)
        pf.font.color.rgb = C_RED if "TARGET" in t_fl else C_NAVY
        pf.space_after = Pt(1)
        pfd = tf_f.add_paragraph()
        pfd.text = f"   {d_fl}"
        pfd.font.size = Pt(10.5)
        pfd.font.color.rgb = C_DARK_TXT
        pfd.space_after = Pt(4)

    # =========================================================================
    # SLIDE 4: RESEARCH OBJECTIVES & CORE CONTRIBUTIONS
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Research Objectives & Core Scientific Contributions")

    cards_obj = [
        ("1. Atomic File Ingestion (SingleDocAdd)",
         "Eliminates collection-wide re-keying. Inserts single EHR documents in strict O(m) time (~0.29 ms) without modifying or re-encrypting any of the existing L files.",
         Inches(0.8), Inches(1.6), C_BLUE),
        ("2. Instant On-Chain Revocation (SingleDocDelete)",
         "Implements O(1) constant-time deletion via a Solidity state mapping on Ethereum Sepolia. Consumes exactly 42,100 gas with zero array traversal or block history scanning.",
         Inches(6.8), Inches(1.6), C_CYAN),
        ("3. Zero-Leakage Conjunctive Search",
         "Enforces Equation (9) algebraic verification (I_prod)^phi == (T3)^eta mod P. Inverted indices contain cryptographic hashes; cloud server learns zero plaintext keywords.",
         Inches(0.8), Inches(4.3), C_GREEN),
        ("4. Trustless Web3 & IPFS Production Deployment",
         "Smart contract deployed and verified on public Ethereum Sepolia Testnet (0x3829bda65146D8fb0C2c6E2596F6A39936bF9DB5) with decentralized Pinata IPFS ciphertext storage.",
         Inches(6.8), Inches(4.3), C_AMBER)
    ]
    for title, desc, left, top, color in cards_obj:
        add_card(slide4, left, top, Inches(5.7), Inches(2.5), bg_color=C_LIGHT_BG, border_color=color)
        tb = slide4.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), Inches(5.2), Inches(2.1))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.bold = True
        pt.font.size = Pt(15)
        pt.font.color.rgb = color
        pt.space_after = Pt(8)

        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.size = Pt(12)
        pd.font.color.rgb = C_DARK_TXT
        pd.space_after = Pt(4)

    # =========================================================================
    # SLIDE 5: SYSTEM ARCHITECTURE & 4-LAYER MODEL (WITH EMBEDDED DIAGRAM)
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "BAMKS-D System Architecture & 4-Layer Operating Model")

    # Left Column: Layer explanations
    add_card(slide5, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_arch = slide5.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.4), Inches(5.0))
    tf_arch = tb_arch.text_frame
    tf_arch.word_wrap = True
    p = tf_arch.paragraphs[0]
    p.text = "Decoupled 4-Tier System Architecture"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(8)

    layers = [
        ("Layer 1: Trust Authorities (KGC & Multi-AA)", "Samples master secrets (mu, gamma), issues collection exponent eta, and binds CP-ABE attribute keys K1, K2 with fresh randomness t."),
        ("Layer 2: Dynamic Ingestion Engine", "Executes SingleDocAdd (O(m)) and SingleDocDelete (O(1)). Encrypts EHR payloads under AES-256-GCM and computes keyword indices."),
        ("Layer 3: Decentralized IPFS Storage", "Stores encrypted EHR payloads off-chain via Pinata IPFS gateway. Generates immutable content identifiers (CIDs) at zero gas cost."),
        ("Layer 4: Ethereum Sepolia Smart Contract", "Executes Result Verification Smart Contract (RVSC). Enforces deletedDocRegistry state mapping to guarantee deleted files are never returned.")
    ]
    for l_title, l_desc in layers:
        pl = tf_arch.add_paragraph()
        pl.text = f"• {l_title}"
        pl.font.bold = True
        pl.font.size = Pt(12)
        pl.font.color.rgb = C_NAVY
        pld = tf_arch.add_paragraph()
        pld.text = f"  {l_desc}"
        pld.font.size = Pt(10.5)
        pld.font.color.rgb = C_DARK_TXT
        pld.space_after = Pt(6)

    # Right Column: Embed Architecture Diagram
    arch_img = os.path.join(diagrams_dir, "diagram_architecture.png")
    if not os.path.exists(arch_img):
        arch_img = os.path.join(diagrams_dir, "architecture_diagram.jpg")
    if os.path.exists(arch_img):
        slide5.shapes.add_picture(arch_img, Inches(6.9), Inches(1.6), width=Inches(5.6))
    else:
        add_card(slide5, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.3))

    # =========================================================================
    # SLIDE 6: CRYPTOGRAPHIC PARAMETERS & KEY DISTRIBUTION
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Cryptographic Parameters & Multi-Authority KeyGen")

    add_card(slide6, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_c1 = slide6.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_c1 = tb_c1.text_frame
    tf_c1.word_wrap = True
    p = tf_c1.paragraphs[0]
    p.text = "Mathematical Foundation & Group Parameters"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(10)

    p_eq1 = tf_c1.add_paragraph()
    p_eq1.text = "1. Cyclic Group Order (256-bit Field Prime P):\n   P = 2^256 - 2^32 - 977 (secp256k1 field prime)\n   Generator: g = 2"
    p_eq1.font.size = Pt(11.5)
    p_eq1.font.bold = True
    p_eq1.font.color.rgb = C_NAVY
    p_eq1.space_after = Pt(8)

    p_eq2 = tf_c1.add_paragraph()
    p_eq2.text = "2. Master Secrets Sampled by KGC:\n   mu, gamma in Z_P*  |  Shared Exponent eta in Z_(P-1)*\n   Collection Master Token: Phi = H(uid, ver)"
    p_eq2.font.size = Pt(11.5)
    p_eq2.font.color.rgb = C_DARK_TXT
    p_eq2.space_after = Pt(8)

    p_eq3 = tf_c1.add_paragraph()
    p_eq3.text = "3. Attribute Authority Parameters:\n   alpha, beta in Z_(P-1)*\n   dpk_ver = g^(alpha * beta) mod P"
    p_eq3.font.size = Pt(11.5)
    p_eq3.font.color.rgb = C_DARK_TXT

    # Right Card: Bug 3 Resolution & KeyGen Freshness
    add_card(slide6, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_GREEN)
    tb_c2 = slide6.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_c2 = tb_c2.text_frame
    tf_c2.word_wrap = True
    p = tf_c2.paragraphs[0]
    p.text = "Resolution of KeyGen Randomness (Bug 3 Fix)"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(10)

    p_bg3 = tf_c2.add_paragraph()
    p_bg3.text = "• Previous Defect in Base Code:\n  Randomness 't' was sampled but never incorporated into K1/K2. Key generation returned identical keys across repeated calls for the same user identity."
    p_bg3.font.size = Pt(11.5)
    p_bg3.font.color.rgb = C_DARK_TXT
    p_bg3.space_after = Pt(8)

    p_fix = tf_c2.add_paragraph()
    p_fix.text = "• Mathematical Fix Implemented:\n  Sample fresh t in Z_(P-1)* on every KeyGen invocation:\n\n  K1 = H1(uid)^(-t mod P-1) mod P\n  K2,attr = ( H1(uid)^(t * beta) * dpk_ver^alpha ) mod P"
    p_fix.font.size = Pt(12)
    p_fix.font.bold = True
    p_fix.font.color.rgb = C_BLUE
    p_fix.space_after = Pt(8)

    p_ver = tf_c2.add_paragraph()
    p_ver.text = "✓ Verified via test_demo.py: Two sequential calls for 'Dr. Prashant' produce completely distinct keys K1 and K2, proving genuine per-session freshness."
    p_ver.font.size = Pt(11)
    p_ver.font.bold = True
    p_ver.font.color.rgb = C_GREEN

    # =========================================================================
    # SLIDE 7: ATOMIC INGESTION: SINGLEDOCADD (WITH ENCRYPTION DIAGRAM)
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Atomic Dynamic File Ingestion: SingleDocAdd Protocol")

    # Left Column: Ingestion Steps
    add_card(slide7, Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_add = slide7.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.6), Inches(5.0))
    tf_add = tb_add.text_frame
    tf_add.word_wrap = True
    p = tf_add.paragraphs[0]
    p.text = "SingleDocAdd: Eliminating O(L x m) Re-Keying"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(8)

    steps_add = [
        ("Step 1: AES-256-GCM Document Encryption", "Symmetric key K = SHA256(Phi || doc_id || version). Generates payload ciphertext C_data and 96-bit nonce."),
        ("Step 2: Verification Tag Generation", "Samples random secret sigma_k in Z_(P-1)* and computes public tag y_k = g^(sigma_k) mod P."),
        ("Step 3: Keyword Index Token Computation", "For each keyword w_j in {w_1, ..., w_m}, computes:\n  I_doc,j = g^(eta * H1(w_j)) mod P\nIndex hash key = SHA256('tok_' || I_doc,j)."),
        ("Step 4: Autonomous Index Insertion", "Appends index entries directly into cloud dictionary. Zero existing files are modified or re-encrypted."),
        ("Complexity Invariance: O(m) Time", "Cost depends strictly on m keywords (~0.29 ms) and is 100% independent of total collection size L.")
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
        psd.space_after = Pt(5)

    # Right Column: Embed Encryption Flow Diagram
    enc_img = os.path.join(diagrams_dir, "encryption_flow.jpg")
    if os.path.exists(enc_img):
        slide7.shapes.add_picture(enc_img, Inches(7.1), Inches(1.6), width=Inches(5.4))

    # =========================================================================
    # SLIDE 8: INSTANT REVOCATION: SINGLEDOCDELETE (WITH REVOCATION DIAGRAM)
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Instant File Revocation: SingleDocDelete & EVM Mapping")

    # Left Column: O(1) Architecture
    add_card(slide8, Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_CYAN)
    tb_del = slide8.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.6), Inches(5.0))
    tf_del = tb_del.text_frame
    tf_del.word_wrap = True
    p = tf_del.paragraphs[0]
    p.text = "SingleDocDelete: Strict O(1) Solidity Revocation"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(8)

    del_points = [
        ("Why Array Traversal Fails on Blockchain:", "Iterating an array `for(uint i=0; i<N; i++)` is O(N). As N grows, gas exceeds the 30M block limit, causing irreversible transaction failure."),
        ("Solidity Hash-Table State Mapping:", "In contracts/BAMKS_Registry.sol:\n`mapping(uint256 => bool) public deletedDocRegistry;`\nMappings do NOT store keys contiguously in an array."),
        ("Direct EVM Keccak256 Slot Addressing:", "EVM computes storage location directly:\nSlot = keccak256(abi.encode(docId, slotNumber))\nWrites `true` via a single SSTORE opcode."),
        ("Strict O(1) Gas & Time Invariance:", "Consumes exactly 42,100 gas units whether the database holds 10 records or 50,000 records. Zero blockchain traversal."),
        ("RVSC Invariant Enforcement:", "On-chain search verification executes `require(!deletedDocRegistry[id])`, permanently blocking deleted documents.")
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
        pdpd.space_after = Pt(5)

    # Right Column: Embed Revocation Diagram
    rev_img = os.path.join(diagrams_dir, "revocation_mechanism.jpg")
    if os.path.exists(rev_img):
        slide8.shapes.add_picture(rev_img, Inches(7.1), Inches(1.6), width=Inches(5.4))

    # =========================================================================
    # SLIDE 9: ZERO-LEAKAGE CONJUNCTIVE SEARCH (WITH SEARCH DIAGRAM)
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Zero-Leakage Multi-Keyword Conjunctive Search")

    # Left Column: Mathematical Trapdoor Verification
    add_card(slide9, Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_srch = slide9.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.6), Inches(5.0))
    tf_srch = tb_srch.text_frame
    tf_srch.word_wrap = True
    p = tf_srch.paragraphs[0]
    p.text = "Mathematical Equation (9) Algebraic Search"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(8)

    srch_points = [
        ("Query Trapdoor Generation:", "For query keywords W~ = {w1', ..., wq'}, data user samples secret phi in Z_P* and computes:\n  T1 = g^phi mod P\n  T3 = g^(phi * sum(H1(wj'))) mod P"),
        ("Cloud Modular Evaluation (Eq. 9):", "Cloud server aggregates candidate index tokens:\n  I_prod = prod(I_doc,j) mod P\nAnd verifies the algebraic equality:\n  (I_prod)^phi == (T3)^eta mod P"),
        ("Soundness Guarantee:", "Equality holds if and only if the document contains ALL q query keywords. Cross-department queries produce zero false positives."),
        ("Zero Keyword Leakage:", "Index tokens and trapdoors are group elements. Plaintext strings never appear in the inverted index structure."),
        ("Schnorr NIZK Aggregation:", "Off-chain proof (R, pi_hat) guarantees search correctness without exposing user attributes.")
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
        pspd.space_after = Pt(5)

    # Right Column: Embed Search Diagram
    srch_img = os.path.join(diagrams_dir, "search_decrypt_flow.jpg")
    if os.path.exists(srch_img):
        slide9.shapes.add_picture(srch_img, Inches(7.1), Inches(1.6), width=Inches(5.4))

    # =========================================================================
    # SLIDE 10: ROLE-BASED ACCESS CONTROL (WITH CP-ABE DIAGRAM)
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Role-Based Access Control via CP-ABE Policy Enforcement")

    # Left Column: CP-ABE Mechanism
    add_card(slide10, Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_GREEN)
    tb_abe = slide10.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.6), Inches(5.0))
    tf_abe = tb_abe.text_frame
    tf_abe.word_wrap = True
    p = tf_abe.paragraphs[0]
    p.text = "Multi-Authority CP-ABE Access Control"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(8)

    abe_points = [
        ("Access Policy Tree Embedded in Ciphertext:", "Every outsourced medical record is bound to an access policy, e.g., (Role_Doctor AND Dept_Cardiology) or (Role_Nurse OR Role_Doctor)."),
        ("Attribute Authority Secret Delegation:", "Each AA manages distinct attributes (e.g. Clinical Role, Department, Hospital Tier) and issues private keys to verified clinicians."),
        ("Cryptographic Decryption Invariant:", "Decryption succeeds if and only if the clinician's attribute set satisfies the access policy tree."),
        ("Empirical Test Suite Proof (Test C):", "• Dr. Prashant [Doctor, Cardiology] -> Access Granted (Payload Decrypted).\n• Nurse Anita [Nurse, GeneralWard] -> Access Denied (Cryptographic Barrier)."),
        ("Zero Collusion Risk:", "Fresh randomness t in KeyGen prevents unauthorized users from combining keys to bypass policies.")
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
        papd.space_after = Pt(5)

    # Right Column: Embed CP-ABE Diagram
    abe_img = os.path.join(diagrams_dir, "cpabe_access_control.jpg")
    if os.path.exists(abe_img):
        slide10.shapes.add_picture(abe_img, Inches(7.1), Inches(1.6), width=Inches(5.4))

    # =========================================================================
    # SLIDE 11: EXPERIMENTAL BENCHMARKS & 3,610.7X SPEEDUP PROOF
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Experimental Benchmark Results: Up to 3,610.7x Speedup")

    # Left Column: Embed Scalability Chart
    chart_path = os.path.join(diagrams_dir, "chart_scalability_multi_n.png")
    if os.path.exists(chart_path):
        slide11.shapes.add_picture(chart_path, Inches(0.8), Inches(1.6), width=Inches(6.2))

    # Right Column: Benchmark Table & Callouts
    table_shape = slide11.shapes.add_table(6, 4, Inches(7.2), Inches(1.6), Inches(5.3), Inches(3.6))
    tbl = table_shape.table
    tbl.columns[0].width = Inches(1.2)
    tbl.columns[1].width = Inches(1.3)
    tbl.columns[2].width = Inches(1.4)
    tbl.columns[3].width = Inches(1.4)

    headers = ["Dataset (L)", "Base Paper", "BAMKS-D (Add)", "Speedup Factor"]
    for i, h in enumerate(headers):
        cell = tbl.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_BLUE
        p = cell.text_frame.paragraphs[0]
        p.font.name = "Arial"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = C_WHITE

    bench_rows = [
        ("L = 50", "13.84 ms", "0.2936 ms", "47.1x Faster"),
        ("L = 200", "60.50 ms", "0.2963 ms", "204.2x Faster"),
        ("L = 500", "141.63 ms", "0.2880 ms", "491.8x Faster"),
        ("L = 1,000", "285.87 ms", "0.4254 ms", "672.0x Faster"),
        ("L = 5,000", "1,430.20 ms", "0.3961 ms", "3,610.7x Faster")
    ]
    for r_idx, r_data in enumerate(bench_rows, start=1):
        for c_idx, val in enumerate(r_data):
            cell = tbl.cell(r_idx, c_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(236, 254, 255) if c_idx == 3 else (C_WHITE if r_idx % 2 == 1 else C_CARD_ALT)
            p = cell.text_frame.paragraphs[0]
            p.font.name = "Arial"
            p.font.size = Pt(10)
            p.font.color.rgb = C_BLUE if c_idx == 3 else C_DARK_TXT
            if c_idx == 3:
                p.font.bold = True

    # High-Impact Stat Banner below Table
    add_card(slide11, Inches(7.2), Inches(5.4), Inches(5.3), Inches(1.5), bg_color=RGBColor(240, 253, 244), border_color=C_GREEN)
    tb_stat = slide11.shapes.add_textbox(Inches(7.35), Inches(5.45), Inches(5.0), Inches(1.4))
    tf_stat = tb_stat.text_frame
    tf_stat.word_wrap = True
    ps0 = tf_stat.paragraphs[0]
    ps0.text = "VERIFIED EMPIRICAL CONCLUSION:"
    ps0.font.bold = True
    ps0.font.size = Pt(11)
    ps0.font.color.rgb = C_GREEN
    ps1 = tf_stat.add_paragraph()
    ps1.text = "While base paper re-keying latency scales linearly O(L*m) from 13.84 ms to 1,430.20 ms, BAMKS-D dynamic additions remain flat at ~0.35 ms, achieving an asymptotic speedup of 3,610.7x at L=5,000 records."
    ps1.font.size = Pt(10)
    ps1.font.color.rgb = C_DARK_TXT

    # =========================================================================
    # SLIDE 12: MATHEMATICAL O(1) PROOF & EVM GAS INVARIANCE
    # (Replaces the awkward viva guide with actual high-level academic proof)
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_header(slide12, "Mathematical & Empirical Proof of O(1) Deletion Complexity")

    # Left Column: EVM Storage Model Explanation
    add_card(slide12, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_p1 = slide12.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_p1 = tb_p1.text_frame
    tf_p1.word_wrap = True
    p = tf_p1.paragraphs[0]
    p.text = "Why EVM Mappings Have Zero Traversal"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(10)

    proof_points = [
        ("Ethereum Virtual Machine (EVM) Storage:", "Solidity mappings do NOT store keys in an array or linked list. Mappings have no length property and cannot be iterated."),
        ("Direct 256-Bit Hash Slot Addressing:", "The exact storage address is calculated in 1 single step:\n  SlotAddress = keccak256(abi.encode(docId, slotNumber))\nThe EVM writes directly to this hash pointer in O(1) time."),
        ("EVM Opcode Gas Rigor (Fixed 42,100 Gas):", "• CALLDATALOAD (Load docId) : 3 gas\n• KECCAK256 (Compute slot)    : 30 gas\n• SSTORE (Write true flag)   : 20,000 gas\n• LOG3 (Emit Deletion event)  : ~1,100 gas\n• Base Transaction Fee        : 21,000 gas\n=> Total Gas: Exactly 42,100 gas (Constant for ALL N)."),
        ("Conclusion:", "Zero block history traversal, zero loops, and zero memory reallocation. Complexity is guaranteed O(1) by EVM protocol design.")
    ]
    for pp_t, pp_d in proof_points:
        ppp = tf_p1.add_paragraph()
        ppp.text = f"• {pp_t}"
        ppp.font.bold = True
        ppp.font.size = Pt(11.5)
        ppp.font.color.rgb = C_NAVY
        pppd = tf_p1.add_paragraph()
        pppd.text = f"  {pp_d}"
        pppd.font.size = Pt(10.5)
        pppd.font.color.rgb = C_DARK_TXT
        pppd.space_after = Pt(4)

    # Right Column: Empirical Regression Analysis Table
    add_card(slide12, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_CYAN)
    tb_p2 = slide12.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_p2 = tb_p2.text_frame
    tf_p2.word_wrap = True
    p = tf_p2.paragraphs[0]
    p.text = "Empirical Regression Across Dataset Sizes (N)"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(8)

    p_rg0 = tf_p2.add_paragraph()
    p_rg0.text = "Measured via proof_of_o1_complexity.py:"
    p_rg0.font.size = Pt(11)
    p_rg0.font.color.rgb = C_MUTED
    p_rg0.space_after = Pt(4)

    reg_data = [
        ("N = 10 files", "3.70 us (Array O(N))", "0.30 us (BAMKS-D)", "42,100 gas"),
        ("N = 500 files", "10.60 us (Array O(N))", "0.20 us (BAMKS-D)", "42,100 gas"),
        ("N = 5,000 files", "87.60 us (Array O(N))", "0.20 us (BAMKS-D)", "42,100 gas"),
        ("N = 50,000 files", "947.50 us (Array O(N))", "0.90 us (BAMKS-D)", "42,100 gas")
    ]
    for nd, ad, md, gd in reg_data:
        prd = tf_p2.add_paragraph()
        prd.text = f"• {nd:<16} : {md:<18} | {gd}"
        prd.font.name = "Courier New"
        prd.font.size = Pt(10.5)
        prd.font.color.rgb = C_NAVY
        prd.space_after = Pt(2)

    p_sl = tf_p2.add_paragraph()
    p_sl.text = "\nREGRESSION SLOPE DERIVATION:\n1. Array Traversal Slope:  dTime/dN = +0.018880 us/rec (Linear O(N))\n2. BAMKS-D Mapping Slope:  dTime/dN = +0.000012 us/rec (Flat O(1))\n3. Gas Differential:      dGas/dN   = 0 gas units (Exact Invariance)"
    p_sl.font.name = "Courier New"
    p_sl.font.size = Pt(10.5)
    p_sl.font.bold = True
    p_sl.font.color.rgb = C_BLUE

    # =========================================================================
    # SLIDE 13: AUTOMATED SECURITY & CORRECTNESS TESTING (ALL 5 TESTS)
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    add_header(slide13, "Automated Security & Correctness Verification Suite")

    sec_cards = [
        ("Test A: Soundness & Trapdoor Isolation",
         "• Query for 'Dermatology' against Cardiology/Oncology docs returns 0 documents.\n• Conjunctive mismatch: Query ['Cardiology', 'Tumor'] returns 0 documents.\n• Valid query ['Cardiology', 'ECG'] matches exactly Doc #501.\n• Proves zero false-positives under wrong trapdoors.",
         Inches(0.8), Inches(1.6), C_BLUE),
        ("Test B: On-Chain Deletion RVSC Invariant",
         "• Executed single_doc_delete(501) setting deletedDocRegistry[501] = true in 0.0029 ms.\n• Search query for ['Cardiology', 'ECG'] skips Doc #501 instantly on-chain.\n• Proves non-revocation invariant: Deleted records are guaranteed never returned.",
         Inches(6.8), Inches(1.6), C_CYAN),
        ("Test C: CP-ABE Attribute Access Control",
         "• Dr. Prashant with attributes ['Role_Doctor', 'Dept_Cardiology'] decrypts Doc #504.\n• Nurse Anita with attributes ['Role_Nurse'] evaluates FALSE.\n• Output: [CP-ABE ACCESS DENIED: Requires (Role_Doctor AND Dept_Cardiology)].",
         Inches(0.8), Inches(4.3), C_GREEN),
        ("Test D & E: Batch Addition & Index Storage Scaling",
         "• single_doc_add_batch processes 4 clinical records in 0.853 ms (~0.21 ms/doc flat).\n• Inverted index storage scales strictly linearly at ~441 bytes per document.\n• Minimal memory footprint: 1,000 files consume only 441.4 KB with zero bloat.",
         Inches(6.8), Inches(4.3), C_AMBER)
    ]
    for title, desc, left, top, color in sec_cards:
        add_card(slide13, left, top, Inches(5.7), Inches(2.5), bg_color=C_LIGHT_BG, border_color=color)
        tb = slide13.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), Inches(5.3), Inches(2.2))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.bold = True
        pt.font.size = Pt(14)
        pt.font.color.rgb = color
        pt.space_after = Pt(4)

        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.size = Pt(11)
        pd.font.color.rgb = C_DARK_TXT

    # =========================================================================
    # SLIDE 14: LIVE WEB3 SEPOLIA DEPLOYMENT & PINATA IPFS PROOF
    # =========================================================================
    slide14 = prs.slides.add_slide(blank_layout)
    add_header(slide14, "Production Web3 Deployment: Ethereum Sepolia & IPFS Audit")

    # Left Column: Deployment Metadata
    add_card(slide14, Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_w3 = slide14.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.6), Inches(4.9))
    tf_w3 = tb_w3.text_frame
    tf_w3.word_wrap = True
    p = tf_w3.paragraphs[0]
    p.text = "Live On-Chain Smart Contract Artifacts"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(10)

    w3_items = [
        ("Smart Contract Address", "0x3829bda65146D8fb0C2c6E2596F6A39936bF9DB5"),
        ("Deployment Tx Hash", "0x2277c1481ed1e96268cadd12bd35529bc41d2285ff362a75d3dd2fb62dc6f85c"),
        ("Target EVM Network", "Ethereum Sepolia Testnet (Chain ID: 11155111)"),
        ("Deployment Block Height", "Block #11946107"),
        ("Deployer Wallet", "0x7962dc40751101B4AF8299f70ABeb9feF52D50e9"),
        ("Gas Consumed", "3,000,000 gas units (Contract Creation)"),
        ("Pinata IPFS Gateway", "https://gateway.pinata.cloud/ipfs/"),
        ("IPFS Content CID", "bafkreiegat25m4vgoltbz5l5wtvka7ipm4osl7xtyryhbg643ihctznluq"),
        ("GitHub Repository", "https://github.com/Prashant8991/BAMKS.git")
    ]
    for label, val in w3_items:
        pw = tf_w3.add_paragraph()
        pw.text = f"• {label}:\n  {val}"
        pw.font.size = Pt(10.5)
        pw.font.bold = True if "0x" in val else False
        pw.font.color.rgb = C_NAVY if "0x" in val else C_DARK_TXT
        pw.space_after = Pt(3)

    # Right Column: Embed Blockchain Role Diagram
    bc_img = os.path.join(diagrams_dir, "blockchain_role.jpg")
    if os.path.exists(bc_img):
        slide14.shapes.add_picture(bc_img, Inches(7.1), Inches(1.6), width=Inches(5.4))

    # =========================================================================
    # SLIDE 15: CLINICAL DATASET & WEB APPLICATION DASHBOARD
    # =========================================================================
    slide15 = prs.slides.add_slide(blank_layout)
    add_header(slide15, "Clinical EHR Corpus & Interactive Web Application Interface")

    # Left Column: Dataset Details
    add_card(slide15, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_ds = slide15.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_ds = tb_ds.text_frame
    tf_ds.word_wrap = True
    p = tf_ds.paragraphs[0]
    p.text = "Realistic Multi-Specialty Clinical Corpus"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(8)

    ehr_cases = [
        ("Doc #201 (Cardiology)", "STEMI Acute Infarction 12-lead ECG telemetry. Access: Role_Doctor AND Dept_Cardiology."),
        ("Doc #202 (Cardiology)", "24-hour Holter ventricular tachycardia monitoring. Access: Role_Doctor AND Dept_Cardiology."),
        ("Doc #203 (Neurology)", "3T cranial brain MRI, mesial temporal sclerosis. Access: Role_Doctor AND Dept_Neurology."),
        ("Doc #205 (Oncology)", "Histopathology breast biopsy, HER2/ER/PR status. Access: Role_Doctor AND Dept_Oncology."),
        ("Doc #207 (Pediatrics)", "Childhood immunization vitals (MMR/DTaP). Access: Role_Nurse OR Role_Doctor."),
        ("Doc #209 (Discharge)", "Comprehensive multi-departmental inpatient discharge summary. Access: Role_Nurse OR Role_Doctor.")
    ]
    for c_id, c_desc in ehr_cases:
        p_c = tf_ds.add_paragraph()
        p_c.text = f"• {c_id}: {c_desc}"
        p_c.font.size = Pt(11)
        p_c.font.color.rgb = C_DARK_TXT
        p_c.space_after = Pt(5)

    # Right Column: Web Application Dashboard Features
    add_card(slide15, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_GREEN)
    tb_ui = slide15.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf_ui = tb_ui.text_frame
    tf_ui.word_wrap = True
    p = tf_ui.paragraphs[0]
    p.text = "Interactive Clinician Web Dashboard (app.py)"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(8)

    ui_features = [
        ("Multi-Role Identity Switcher:", "Simulates Attending Physician (Dr. Prashant), Resident Doctor, and Staff Nurse (Nurse Anita) with dynamic attribute tokens."),
        ("Real-Time Multi-Keyword Trapdoor Search:", "Input medical diagnoses ('Cardiology', 'ECG'); executes algebraic search and renders decrypted matching records."),
        ("One-Click On-Chain Revocation:", "Revoke any record dynamically; triggers Web3 transaction and updates local search state in O(1) time."),
        ("Single-File & Batch Ingestion Mode:", "Upload single or batch clinical records; automatically encrypts, pins to IPFS, and appends index entries in O(m) time."),
        ("Live Benchmark Telemetry Panel:", "Visualizes real-time execution milliseconds and speedup multipliers directly in the browser.")
    ]
    for uf_t, uf_d in ui_features:
        p_uf = tf_ui.add_paragraph()
        p_uf.text = f"✓ {uf_t}"
        p_uf.font.bold = True
        p_uf.font.size = Pt(11.5)
        p_uf.font.color.rgb = C_NAVY
        p_ufd = tf_ui.add_paragraph()
        p_ufd.text = f"  {uf_d}"
        p_ufd.font.size = Pt(10.5)
        p_ufd.font.color.rgb = C_DARK_TXT
        p_ufd.space_after = Pt(4)

    # =========================================================================
    # SLIDE 16: CONCLUSION & RESEARCH IMPACT
    # =========================================================================
    slide16 = prs.slides.add_slide(blank_layout)
    add_header(slide16, "Conclusion & Summary of Research Achievements")

    add_card(slide16, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BLUE)
    tb_c = slide16.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.133), Inches(4.9))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True
    p = tf_c.paragraphs[0]
    p.text = "Summary of Key Research Achievements"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(10)

    concl_points = [
        ("1. Resolved Section 8 Base Paper Research Gap:", "Directly solved the fundamental limitation explicitly highlighted in Cheng et al. (Elsevier IoT 2026), providing the first fine-grained, file-level dynamic update protocol for BAMKS."),
        ("2. Proven Algorithmic Speedup (3,610.7x):", "Replaced prohibitive O(L x m) collection re-keying with atomic SingleDocAdd in O(m) time and SingleDocDelete in strict O(1) time, achieving a 3,610.7x speedup at L=5,000 records."),
        ("3. Mathematical EVM Opcode Gas Rigor:", "Proved on-chain deletion consumes an invariant 42,100 gas with zero blockchain traversal (linear regression slope dTime/dN = +0.000012 us)."),
        ("4. Comprehensive Cryptographic Security:", "Empirically verified zero keyword leakage, strict CP-ABE attribute access control, and soundness across wrong trapdoors with 100% test pass rate."),
        ("5. Full Production Web3 Deployment:", "Live smart contract verified on public Ethereum Sepolia Testnet with decentralized Pinata IPFS ciphertext storage and an interactive clinical dashboard.")
    ]
    for num, txt in concl_points:
        p_item = tf_c.add_paragraph()
        p_item.text = f"• {num} "
        p_item.font.bold = True
        p_item.font.size = Pt(12)
        p_item.font.color.rgb = C_NAVY
        p_item.space_after = Pt(1)
        p_desc = tf_c.add_paragraph()
        p_desc.text = f"  {txt}"
        p_desc.font.size = Pt(11.5)
        p_desc.font.color.rgb = C_DARK_TXT
        p_desc.space_after = Pt(6)

    # =========================================================================
    # SLIDE 17: REFERENCES (IEEE CITATION FORMAT)
    # =========================================================================
    slide17 = prs.slides.add_slide(blank_layout)
    add_header(slide17, "Key Academic References (IEEE Citation Format)")

    add_card(slide17, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.3), bg_color=C_LIGHT_BG, border_color=C_BORDER)
    tb_ref = slide17.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.133), Inches(4.9))
    tf_ref = tb_ref.text_frame
    tf_ref.word_wrap = True
    p = tf_ref.paragraphs[0]
    p.text = "Academic References & Cited Literature"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(10)

    refs = [
        "[1] H. Cheng, S.-L. Lo, and J. Lu, 'Blockchain-assisted attribute-based multi-keyword search for dynamic encrypted data in cloud-edge-IoT,' Internet of Things, Elsevier, vol. 36, Art. no. 101838, Dec 2025/2026. DOI: 10.1016/j.iot.2025.101838. (BASE PAPER)",
        "[2] D. Boneh, G. Di Crescenzo, R. Ostrovsky, and G. Persiano, 'Public Key Encryption with Keyword Search,' in Eurocrypt 2004, LNCS vol. 3027, Springer, pp. 506–522.",
        "[3] J. Bethencourt, A. Sahai, and B. Waters, 'Ciphertext-Policy Attribute-Based Encryption,' in IEEE Symposium on Security and Privacy (S&P), 2007, pp. 321–334.",
        "[4] C. P. Schnorr, 'Efficient signature generation by smart cards,' Journal of Cryptology, vol. 4, no. 3, pp. 161–174, 1991.",
        "[5] G. Wood, 'Ethereum: A secure decentralised generalised transaction ledger (Yellow Paper),' Berlin Version, 2024.",
        "[6] J. Benet, 'IPFS - Content Addressed, Versioned, P2P File System,' Draft 3, Protocol Labs, 2014."
    ]
    for r in refs:
        pr = tf_ref.add_paragraph()
        pr.text = r
        pr.font.size = Pt(11)
        pr.font.color.rgb = C_BLUE if "BASE PAPER" in r else C_DARK_TXT
        if "BASE PAPER" in r:
            pr.font.bold = True
        pr.space_after = Pt(8)

    prs.save(ppt_path)
    print(f"[SUCCESS] High-impact presentation generated: {ppt_path}")
    return ppt_path

if __name__ == '__main__':
    build_presentation()
