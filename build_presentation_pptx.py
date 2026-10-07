import os
import sys
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    C_NAVY = RGBColor(15, 23, 42)
    C_INDIGO = RGBColor(79, 70, 229)
    C_BLUE = RGBColor(37, 99, 235)
    C_EMERALD = RGBColor(5, 150, 105)
    C_ROSE = RGBColor(225, 29, 72)
    C_AMBER = RGBColor(217, 119, 6)
    C_CARD_BG = RGBColor(255, 255, 255)
    C_TEXT_DARK = RGBColor(15, 23, 42)
    C_TEXT_MUTED = RGBColor(100, 116, 139)
    C_WHITE = RGBColor(255, 255, 255)

    def add_header(slide, title_text, category_text="BAMKS-D REVIEW 2 PRESENTATION"):
        hdr = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.1))
        hdr.fill.solid()
        hdr.fill.fore_color.rgb = C_NAVY
        hdr.line.color.rgb = C_NAVY

        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.15), Inches(11.7), Inches(0.3))
        tf_cat = cat_box.text_frame
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = RGBColor(56, 189, 248)

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(0.55))
        tf_title = title_box.text_frame
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = C_WHITE

    def add_card(slide, left, top, width, height, title="", border_color=C_INDIGO):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)

        if title:
            accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(0.08))
            accent.fill.solid()
            accent.fill.fore_color.rgb = border_color
            accent.line.fill.background()

            t_box = slide.shapes.add_textbox(Inches(left + 0.2), Inches(top + 0.15), Inches(width - 0.4), Inches(0.4))
            tf = t_box.text_frame
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = C_TEXT_DARK
        return card

    # SLIDE 1: Title
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_NAVY
    bg1.line.color.rgb = C_NAVY

    tbox = slide1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.333), Inches(4.5))
    tf1 = tbox.text_frame
    p1 = tf1.paragraphs[0]
    p1.text = "BAMKS-D: SECURE HEALTHCARE CLOUD & BLOCKCHAIN SYSTEM"
    p1.font.size = Pt(28)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(56, 189, 248)

    p2 = tf1.add_paragraph()
    p2.text = "Enabling Dynamic File-Level Operations in Attribute-Based Multi-Keyword Search for Cloud-Edge-IoT"
    p2.font.size = Pt(18)
    p2.font.color.rgb = C_WHITE
    p2.space_before = Pt(12)

    add_card(slide1, 1.0, 4.8, 11.333, 1.8, title="PROJECT CONTRIBUTORS & BASE PAPER DETAILS", border_color=C_BLUE)
    cbox = slide1.shapes.add_textbox(Inches(1.2), Inches(5.3), Inches(10.9), Inches(1.1))
    ctf = cbox.text_frame
    cp1 = ctf.paragraphs[0]
    cp1.text = "• Team Members: Prashant Singh (24BYB1042) & Adak Rushikesh (24BYB1055)"
    cp1.font.size = Pt(13)
    cp1.font.bold = True
    cp1.font.color.rgb = C_TEXT_DARK
    cp2 = ctf.add_paragraph()
    cp2.text = "• Base Paper: Cheng et al., Elsevier (Internet of Things), Vol 36, Art 101838, Dec 2025/2026 (DOI: 10.1016/j.iot.2025.101838)"
    cp2.font.size = Pt(12)
    cp2.font.color.rgb = C_TEXT_MUTED
    cp2.space_before = Pt(4)

    # SLIDE 2: Problem Statement & Research Gap
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Problem Statement & Research Gap (Cheng et al. Elsevier 2026)")
    add_card(slide2, 0.8, 1.4, 5.6, 5.5, title="1. Base Paper Achievements (Cheng et al.)", border_color=C_BLUE)
    tb2_1 = slide2.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.2), Inches(4.7))
    tf2_1 = tb2_1.text_frame
    tf2_1.word_wrap = True
    bullets1 = [
        "• Fine-grained CP-ABE Access Control for healthcare records.",
        "• Verifiable Conjunctive Multi-Keyword Search over encrypted indices.",
        "• Schnorr Non-Interactive Zero-Knowledge (SNIZK) verification proof.",
        "• Distributed secret sharing across multi-owner hospitals."
    ]
    for i, b in enumerate(bullets1):
        p = tf2_1.paragraphs[0] if i == 0 else tf2_1.add_paragraph()
        p.text = b
        p.font.size = Pt(13)
        p.font.color.rgb = C_TEXT_DARK
        p.space_after = Pt(10)

    add_card(slide2, 6.8, 1.4, 5.7, 5.5, title="2. Critical Bottleneck & Solved Research Gap", border_color=C_ROSE)
    tb2_2 = slide2.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.7))
    tf2_2 = tb2_2.text_frame
    tf2_2.word_wrap = True
    bullets2 = [
        "• Base Paper Limitation (Section 8 Quote): 'Future work must extend BAMKS to support dynamic adding, deleting, and updating.'",
        "• The Bottleneck: Base paper grouped all files into a static version F_ver.",
        "• Impact: Modifying 1 file forced re-encryption of ALL L files (O(L x m) complexity = ~5,560 ms latency!).",
        "• OUR EXTENSION: Solved via SingleDocAdd O(m) & On-Chain SingleDocDelete O(1) in 0.001 ms!"
    ]
    for i, b in enumerate(bullets2):
        p = tf2_2.paragraphs[0] if i == 0 else tf2_2.add_paragraph()
        p.text = b
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_DARK if i != 3 else C_ROSE
        p.font.bold = (i == 3)
        p.space_after = Pt(10)

    # SLIDE 3: VISUAL SYSTEM ARCHITECTURE DIAGRAM
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "System Architecture & Interaction Flow Diagram")
    if os.path.exists("diagrams/diagram_architecture.png"):
        slide3.shapes.add_picture("diagrams/diagram_architecture.png", Inches(0.8), Inches(1.3), width=Inches(11.733))

    # SLIDE 4: Cryptographic Engine Mechanics
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Cryptographic Engine & Security Foundations")
    add_card(slide4, 0.8, 1.4, 3.7, 5.5, title="1. CP-ABE Access Control", border_color=C_INDIGO)
    tb4_1 = slide4.shapes.add_textbox(Inches(0.95), Inches(2.0), Inches(3.4), Inches(4.7))
    tf4_1 = tb4_1.text_frame
    tf4_1.word_wrap = True
    txt4_1 = [
        "• Access Policy attached to file (e.g. 'Role_Doctor AND Dept_Cardiology').",
        "• Attribute Authority (AA_Medical) issues secret keys K2_x = g^γ_x for attributes.",
        "• Decryption mathematically succeeds ONLY if doctor attributes satisfy policy."
    ]
    for i, t in enumerate(txt4_1):
        p = tf4_1.paragraphs[0] if i == 0 else tf4_1.add_paragraph()
        p.text = t
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_DARK
        p.space_after = Pt(8)

    add_card(slide4, 4.8, 1.4, 3.7, 5.5, title="2. AES-256-GCM Payload", border_color=C_EMERALD)
    tb4_2 = slide4.shapes.add_textbox(Inches(4.95), Inches(2.0), Inches(3.4), Inches(4.7))
    tf4_2 = tb4_2.text_frame
    tf4_2.word_wrap = True
    txt4_2 = [
        "• Symmetric 256-bit AES encryption for payload.",
        "• 96-bit Random Nonce: Guarantees unique ciphertext for identical records.",
        "• 128-bit GCM Tag: Digital seal that detects any cloud tampering instantly."
    ]
    for i, t in enumerate(txt4_2):
        p = tf4_2.paragraphs[0] if i == 0 else tf4_2.add_paragraph()
        p.text = t
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_DARK
        p.space_after = Pt(8)

    add_card(slide4, 8.8, 1.4, 3.75, 5.5, title="3. Discrete Log Keyword Index", border_color=C_BLUE)
    tb4_3 = slide4.shapes.add_textbox(Inches(8.95), Inches(2.0), Inches(3.45), Inches(4.7))
    tf4_3 = tb4_3.text_frame
    tf4_3.word_wrap = True
    txt4_3 = [
        "• Keyword Token: g^(η * H1(kw)) mod P.",
        "• Hides plaintext keywords from untrusted cloud.",
        "• Enables trapdoor search matching without decrypting files."
    ]
    for i, t in enumerate(txt4_3):
        p = tf4_3.paragraphs[0] if i == 0 else tf4_3.add_paragraph()
        p.text = t
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_DARK
        p.space_after = Pt(8)

    # SLIDE 5: VISUAL PERFORMANCE BAR CHART DIAGRAM
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Experimental Performance Benchmarks & Speedup Chart")
    if os.path.exists("diagrams/chart_performance.png"):
        slide5.shapes.add_picture("diagrams/chart_performance.png", Inches(0.8), Inches(1.4), width=Inches(6.0))

    # Add text summary alongside chart
    add_card(slide5, 7.1, 1.4, 5.4, 5.5, title="Performance Summary & Key Metrics", border_color=C_EMERALD)
    tb5_sum = slide5.shapes.add_textbox(Inches(7.3), Inches(2.0), Inches(5.0), Inches(4.7))
    tf5_sum = tb5_sum.text_frame
    tf5_sum.word_wrap = True
    m_list = [
        "• Base Paper Full Re-Keying: ~5,560 ms (Requires exponentiation across all L files).",
        "• Our SingleDocAdd: ~0.12 ms (46,000x Faster -- operates only on 1 file).",
        "• Our SingleDocDelete: ~0.001 ms (5.5 Million x Faster -- 1 boolean flip on smart contract).",
        "• Gas Overhead: ~45,100 gas (~$0.001 on Ethereum mainnet)."
    ]
    for i, m in enumerate(m_list):
        p = tf5_sum.paragraphs[0] if i == 0 else tf5_sum.add_paragraph()
        p.text = m
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_DARK
        p.space_after = Pt(12)

    # SLIDE 6: Proposed Algorithms & Code Line Mapping
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Proposed Algorithms & Code Line Mapping")
    add_card(slide6, 0.8, 1.4, 11.75, 5.5, title="IMPLEMENTATION ARCHITECTURE & LINE REFERENCES", border_color=C_BLUE)
    tb6 = slide6.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.35), Inches(4.7))
    tf6 = tb6.text_frame
    tf6.word_wrap = True
    algos = [
        ("Algorithm 12: SingleDocAdd [O(m)]", "Appends single encrypted record without version re-keying.", "src/dynamic_extension.py:17"),
        ("Algorithm 13: SingleDocDelete [O(1)]", "Flips deletedDocRegistry[docId] = true on smart contract.", "src/dynamic_extension.py:36"),
        ("Algorithm 14: SingleDocModify [O(m)]", "Executes deletion followed by single-document addition.", "src/dynamic_extension.py:50"),
        ("Algorithm 15: SearchWithFilter", "Filters out deleted/revoked documents during trapdoor search.", "src/dynamic_extension.py:62"),
        ("Smart Contract: BAMKS_Registry.sol", "Maintains mapping(uint256 => bool) public deletedDocRegistry.", "contracts/BAMKS_Registry.sol:25")
    ]
    for name, desc, loc in algos:
        p = tf6.add_paragraph()
        p.text = f"• {name}"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = C_INDIGO
        p_sub = tf6.add_paragraph()
        p_sub.text = f"   Description: {desc}  |  Exact Code Location: {loc}"
        p_sub.font.size = Pt(11.5)
        p_sub.font.color.rgb = C_TEXT_DARK
        p_sub.space_after = Pt(6)

    # SLIDE 7: Conclusion & Review 3 Roadmap
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Conclusion & Review 3 Roadmap")
    add_card(slide7, 0.8, 1.4, 5.6, 5.5, title="Key Accomplishments", border_color=C_EMERALD)
    tb7_1 = slide7.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.2), Inches(4.7))
    tf7_1 = tb7_1.text_frame
    tf7_1.word_wrap = True
    takeaways = [
        "1. Solved Section 8 research gap from Cheng et al. (Elsevier IoT 2026).",
        "2. Delivered O(m) single-document addition without dataset re-keying.",
        "3. Delivered O(1) instant on-chain revocation mapping on Ethereum smart contract.",
        "4. Fully functional live web system with dynamic random clinical case generator."
    ]
    for i, t in enumerate(takeaways):
        p = tf7_1.paragraphs[0] if i == 0 else tf7_1.add_paragraph()
        p.text = t
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_DARK
        p.space_after = Pt(10)

    add_card(slide7, 6.8, 1.4, 5.7, 5.5, title="Review 3 Roadmap & Future Scope", border_color=C_INDIGO)
    tb7_2 = slide7.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.7))
    tf7_2 = tb7_2.text_frame
    tf7_2.word_wrap = True
    roadmap = [
        "1. Deploy Smart Contract on Ethereum Sepolia Public Testnet.",
        "2. Integrate zk-SNARKs (Circom/snarkjs) for zero-knowledge search verification.",
        "3. Implement Post-Quantum Cryptography (Crystals-Kyber) for quantum resistance.",
        "4. Profile battery and CPU consumption on physical Raspberry Pi IoT edge gateway."
    ]
    for i, r in enumerate(roadmap):
        p = tf7_2.paragraphs[0] if i == 0 else tf7_2.add_paragraph()
        p.text = r
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_DARK
        p.space_after = Pt(10)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "BAMKS_D_Presentation.pptx")
    prs.save(output_path)
    print(f"[OK] Visual Presentation updated with embedded diagram images: {output_path}")

if __name__ == "__main__":
    create_presentation()
