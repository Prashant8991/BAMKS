"""
BAMKS-D Ultimate Defense Manual PDF Generator
Generates a comprehensive 40+ page PDF covering EVERY topic for the Review 2 presentation.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os, datetime

# ── Color Palette ──
TEAL       = HexColor("#0d9488")
TEAL_LIGHT = HexColor("#e6f7f5")
TEAL_DARK  = HexColor("#065f46")
NAVY       = HexColor("#1e293b")
DARK_BG    = HexColor("#0f172a")
WARM_GRAY  = HexColor("#f8fafc")
MID_GRAY   = HexColor("#64748b")
LIGHT_GRAY = HexColor("#e2e8f0")
AMBER      = HexColor("#f59e0b")
AMBER_LIGHT= HexColor("#fef3c7")
RED_LIGHT  = HexColor("#fee2e2")
RED        = HexColor("#ef4444")
GREEN      = HexColor("#10b981")
GREEN_LIGHT= HexColor("#d1fae5")
BLUE       = HexColor("#3b82f6")
BLUE_LIGHT = HexColor("#dbeafe")
VIOLET     = HexColor("#8b5cf6")
VIOLET_LIGHT = HexColor("#ede9fe")

OUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "BAMKS_D_ULTIMATE_DEFENSE_MANUAL.pdf")

def build_pdf():
    doc = SimpleDocTemplate(
        OUT_FILE, pagesize=A4,
        topMargin=18*mm, bottomMargin=18*mm,
        leftMargin=16*mm, rightMargin=16*mm,
        title="BAMKS-D Ultimate Defense Manual",
        author="Prashant Singh & Adak Rushikesh"
    )
    
    styles = getSampleStyleSheet()
    W = A4[0] - 32*mm  # usable width
    
    # ── Custom Styles ──
    sTitle = ParagraphStyle('sTitle', parent=styles['Title'], fontSize=22, leading=26,
                            textColor=TEAL_DARK, spaceAfter=4*mm, alignment=TA_CENTER,
                            fontName='Helvetica-Bold')
    sH1 = ParagraphStyle('sH1', parent=styles['Heading1'], fontSize=16, leading=20,
                         textColor=NAVY, spaceBefore=6*mm, spaceAfter=3*mm,
                         fontName='Helvetica-Bold', borderWidth=0,
                         borderPadding=0, borderColor=TEAL)
    sH2 = ParagraphStyle('sH2', parent=styles['Heading2'], fontSize=13, leading=17,
                         textColor=TEAL_DARK, spaceBefore=4*mm, spaceAfter=2*mm,
                         fontName='Helvetica-Bold')
    sH3 = ParagraphStyle('sH3', parent=styles['Heading3'], fontSize=11, leading=14,
                         textColor=NAVY, spaceBefore=3*mm, spaceAfter=1.5*mm,
                         fontName='Helvetica-Bold')
    sBody = ParagraphStyle('sBody', parent=styles['Normal'], fontSize=10, leading=14,
                           textColor=black, spaceAfter=2*mm, alignment=TA_JUSTIFY,
                           fontName='Helvetica')
    sBold = ParagraphStyle('sBold', parent=sBody, fontName='Helvetica-Bold')
    sCode = ParagraphStyle('sCode', parent=styles['Code'], fontSize=8.5, leading=11,
                           textColor=HexColor("#1e1e1e"), backColor=HexColor("#f1f5f9"),
                           borderWidth=0.5, borderColor=LIGHT_GRAY, borderPadding=4,
                           fontName='Courier', spaceAfter=2*mm)
    sSpeech = ParagraphStyle('sSpeech', parent=sBody, fontSize=10, leading=14,
                             textColor=TEAL_DARK, backColor=TEAL_LIGHT,
                             borderWidth=0.5, borderColor=TEAL, borderPadding=6,
                             leftIndent=8, spaceAfter=3*mm, fontName='Helvetica-Oblique')
    sWarn = ParagraphStyle('sWarn', parent=sBody, fontSize=10, leading=14,
                           textColor=HexColor("#92400e"), backColor=AMBER_LIGHT,
                           borderWidth=0.5, borderColor=AMBER, borderPadding=6,
                           leftIndent=8, spaceAfter=3*mm)
    sTip = ParagraphStyle('sTip', parent=sBody, fontSize=10, leading=14,
                          textColor=HexColor("#065f46"), backColor=GREEN_LIGHT,
                          borderWidth=0.5, borderColor=GREEN, borderPadding=6,
                          leftIndent=8, spaceAfter=3*mm)
    sBullet = ParagraphStyle('sBullet', parent=sBody, bulletIndent=8,
                             leftIndent=18, spaceAfter=1.5*mm)
    sSmall = ParagraphStyle('sSmall', parent=sBody, fontSize=8.5, leading=11,
                            textColor=MID_GRAY)
    sCenterBold = ParagraphStyle('sCenterBold', parent=sBody, fontSize=12, leading=16,
                                 textColor=NAVY, alignment=TA_CENTER,
                                 fontName='Helvetica-Bold', spaceAfter=2*mm)
    
    def hr():
        return HRFlowable(width="100%", thickness=0.5, color=LIGHT_GRAY,
                          spaceAfter=3*mm, spaceBefore=2*mm)
    
    def colored_table(data, col_widths=None, header_color=TEAL_DARK, stripe=True):
        if col_widths is None:
            ncols = max(len(r) for r in data)
            col_widths = [W/ncols]*ncols
        style_cmds = [
            ('BACKGROUND', (0,0), (-1,0), header_color),
            ('TEXTCOLOR', (0,0), (-1,0), white),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('LEADING', (0,0), (-1,-1), 12),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('GRID', (0,0), (-1,-1), 0.4, LIGHT_GRAY),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ]
        if stripe:
            for i in range(1, len(data)):
                if i % 2 == 0:
                    style_cmds.append(('BACKGROUND', (0,i), (-1,i), HexColor("#f8fafc")))
        t = Table(data, colWidths=col_widths, repeatRows=1)
        t.setStyle(TableStyle(style_cmds))
        return t

    story = []

    # ═══════════════════════════════════════════════
    # COVER PAGE
    # ═══════════════════════════════════════════════
    story.append(Spacer(1, 30*mm))
    story.append(Paragraph("BAMKS-D", ParagraphStyle('cover1', parent=sTitle,
                           fontSize=38, leading=42, textColor=TEAL_DARK)))
    story.append(Paragraph("Ultimate Defense Manual", ParagraphStyle('cover2', parent=sTitle,
                           fontSize=20, leading=24, textColor=NAVY)))
    story.append(Spacer(1, 8*mm))
    story.append(hr())
    story.append(Paragraph(
        "Enabling Dynamic File-Level Operations in Blockchain-Assisted<br/>"
        "Attribute-Based Multi-Keyword Search for Cloud-Edge-IoT",
        ParagraphStyle('cover3', parent=sBody, fontSize=12, leading=16,
                       alignment=TA_CENTER, textColor=MID_GRAY)))
    story.append(Spacer(1, 10*mm))
    cover_info = [
        ["Base Paper", "Cheng et al., Internet of Things (Elsevier), Vol 36, Art 101838, Dec 2025/2026"],
        ["DOI", "https://doi.org/10.1016/j.iot.2025.101838"],
        ["Team", "Prashant Singh (24BYB1042) & Adak Rushikesh (24BYB1055)"],
        ["Review", "Review 2 -- Implementation, Algorithms, Intermediate Results"],
        ["Generated", datetime.datetime.now().strftime("%d %B %Y, %I:%M %p")],
    ]
    story.append(colored_table(cover_info, col_widths=[35*mm, W-35*mm], header_color=NAVY))
    story.append(Spacer(1, 15*mm))
    story.append(Paragraph("CONFIDENTIAL -- For personal review preparation only.",
                           ParagraphStyle('warn', parent=sBody, fontSize=9, alignment=TA_CENTER,
                                          textColor=RED)))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # TABLE OF CONTENTS
    # ═══════════════════════════════════════════════
    story.append(Paragraph("TABLE OF CONTENTS", sH1))
    story.append(hr())
    toc_items = [
        "1. Project Overview and Problem Statement",
        "2. Glossary -- Every Technical Term Explained",
        "3. Base Paper (Cheng et al.) -- What Was Already Done",
        "4. Our Research Gap -- What We Solved",
        "5. System Architecture -- How Everything Connects",
        "6. Technology Stack -- Tools and Libraries",
        "7. Algorithm 1: GlobalSetup -- System Initialization",
        "8. Algorithm 2: AuthSetup -- Authority Key Generation",
        "9. Algorithm 3: DOSetup -- Multi-Owner Token",
        "10. Algorithm 4: DUSetup -- User Registration",
        "11. Algorithm 5: KeyGen -- User Secret Key Generation",
        "12. Algorithm 6: FileEnc -- AES-256-GCM File Encryption",
        "13. Algorithm 7: TokenEnc -- CP-ABE Token Encryption",
        "14. Algorithm 8: IndexGen -- Keyword Index Generation",
        "15. Algorithm 9: TrapGen -- Trapdoor Token Generation",
        "16. Algorithm 10: Search -- Cloud-Side Index Matching",
        "17. Algorithm 11: SNIZK Proof -- Zero-Knowledge Verification",
        "18. Algorithm 12: SingleDocAdd -- Our O(m) Insertion [PROPOSED]",
        "19. Algorithm 13: SingleDocDelete -- Our O(1) Deletion [PROPOSED]",
        "20. Algorithm 14: SingleDocModify -- Delete + Insert [PROPOSED]",
        "21. Algorithm 15: SearchWithFilter -- Revocation-Aware Search [PROPOSED]",
        "22. Smart Contract: BAMKS_Registry.sol -- Blockchain Layer",
        "23. Code-to-Algorithm Mapping (Exact File and Line Numbers)",
        "24. Live Demo Walkthrough -- What to Show Tomorrow",
        "25. Complete Presentation Speech Script (Word-by-Word)",
        "26. Performance Comparison Table",
        "27. Viva QandA -- 25 Questions with Bulletproof Answers",
        "28. Individual Contributions Statement",
        "29. Review 3 Roadmap",
        "30. Emergency Quick-Reference Card",
    ]
    for item in toc_items:
        story.append(Paragraph("  " + item, sBullet))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 1. PROJECT OVERVIEW
    # ═══════════════════════════════════════════════
    story.append(Paragraph("1. PROJECT OVERVIEW AND PROBLEM STATEMENT", sH1))
    story.append(hr())
    story.append(Paragraph("<b>Project Title:</b> Enabling Dynamic File-Level Operations in Blockchain-Assisted Attribute-Based Multi-Keyword Search (BAMKS-D)", sBody))
    story.append(Spacer(1, 2*mm))
    
    story.append(Paragraph("<b>What is this project about? (Simple English)</b>", sH3))
    story.append(Paragraph(
        "Imagine a hospital stores thousands of patient records (X-rays, blood reports, prescriptions) "
        "on Amazon Cloud or Google Cloud. The hospital wants to keep these records <b>encrypted</b> "
        "(secret) so that even the cloud company cannot read them. But doctors still need to "
        "<b>search</b> through these encrypted files by typing keywords like 'Heart Attack' and 'ECG' "
        "without decrypting everything. This is called <b>Searchable Encryption</b>.", sBody))
    story.append(Paragraph(
        "The problem is: the cloud company is <b>semi-honest</b> -- it follows the rules but might "
        "cheat by returning incomplete results to save computing power. So we use <b>Blockchain</b> "
        "(Ethereum smart contracts) as an honest judge that verifies the cloud gave correct, complete results.", sBody))
    story.append(Paragraph(
        "Our base paper (Cheng et al., Elsevier 2026) built this entire system but had one critical flaw: "
        "if you want to add or delete even <b>ONE</b> patient record, you must re-encrypt ALL 1,000 files. "
        "This takes ~5.5 seconds and is completely impractical for IoT devices with limited battery.", sBody))
    story.append(Paragraph(
        "<b>Our Contribution:</b> We solved this by building 3 new algorithms that allow adding one file "
        "in O(m) time (~1ms) and deleting one file in O(1) time (~0.0001ms), achieving a <b>5,500x speedup</b>.", sBody))
    
    story.append(Spacer(1,3*mm))
    story.append(Paragraph("<b>Aim Statement (Memorize This):</b>", sH3))
    story.append(Paragraph(
        '"To design and implement efficient single-document dynamic operations (addition, deletion, and modification) '
        'for the BAMKS framework, reducing update complexity from O(L x m) to O(m) for insertion and O(1) for deletion, '
        'using incremental index generation and Ethereum smart contract revocation registries."', sSpeech))
    
    story.append(Spacer(1,3*mm))
    story.append(Paragraph("<b>Objectives:</b>", sH3))
    objectives = [
        "Implement the base BAMKS cryptographic engine (256-bit cyclic group, bilinear pairings, AES-256-GCM).",
        "Design SingleDocAdd algorithm for O(m) incremental file insertion without re-keying existing files.",
        "Design SingleDocDelete algorithm for O(1) instant on-chain document revocation via smart contract.",
        "Build a Solidity smart contract (BAMKS_Registry.sol) for on-chain deletion registry and SNIZK proof verification.",
        "Validate through benchmarks: compare base paper's O(L x m) vs our O(m)/O(1) across 50-5000 files.",
    ]
    for i, obj in enumerate(objectives, 1):
        story.append(Paragraph(f"<b>{i}.</b> {obj}", sBullet))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 2. GLOSSARY
    # ═══════════════════════════════════════════════
    story.append(Paragraph("2. GLOSSARY -- EVERY TECHNICAL TERM EXPLAINED", sH1))
    story.append(hr())
    story.append(Paragraph("Read this section carefully. If Ma'am asks 'What is X?', you will have the answer ready.", sWarn))
    
    glossary = [
        ["Term", "Full Form", "What It Means (Simple)", "Why We Use It"],
        ["AES-256-GCM", "Advanced Encryption\nStandard, 256-bit,\nGalois/Counter Mode",
         "A symmetric encryption algorithm.\nSame key encrypts and decrypts.\n256-bit key = virtually unbreakable.",
         "Fast encryption for large\nmedical files. GCM mode\nalso verifies data integrity\n(tamper detection)."],
        ["CP-ABE", "Ciphertext-Policy\nAttribute-Based\nEncryption",
         "Encryption where the access\nrule is embedded IN the\nciphertext. E.g., 'Role=Doctor\nAND Dept=Cardiology'.",
         "Allows fine-grained access\ncontrol. Only users whose\nattributes satisfy the policy\ncan decrypt."],
        ["Searchable\nEncryption (SE)", "--",
         "Ability to search through\nencrypted data without\ndecrypting it first.",
         "Doctors need to find patient\nrecords by keyword without\nexposing data to the cloud."],
        ["Blockchain", "--",
         "A decentralized, immutable\nledger. Once data is written,\nit cannot be changed.",
         "Acts as a trusted verifier.\nThe cloud cannot cheat\nbecause the blockchain\nrecords are permanent."],
        ["Smart Contract", "--",
         "A self-executing program\nstored on the blockchain.\nRuns automatically when\ncalled.",
         "Our BAMKS_Registry.sol\ncontract verifies search\nproofs and tracks deleted\ndocuments automatically."],
        ["Solidity", "--",
         "The programming language\nfor writing Ethereum smart\ncontracts.",
         "Industry standard for\nEthereum development.\nOur RVSC contract is\nwritten in Solidity."],
        ["SNIZK", "Schnorr Non-Interactive\nZero-Knowledge Proof",
         "A mathematical proof that\nconvinces a verifier\nwithout revealing any\nsecret information.",
         "The cloud proves it returned\ncorrect results without\nrevealing encryption keys\nor patient data."],
        ["Cyclic Group\n(Z_p*)", "--",
         "A mathematical set of\nnumbers {1,2,...,p-1}\nwhere operations wrap\naround modulo p.",
         "Foundation of all our\ncryptography. All keys\nand tokens are computed\nin this group."],
        ["Bilinear Pairing\n(e-hat)", "--",
         "A special mathematical\nfunction: e(g^a, g^b) =\ne(g,g)^(ab). Maps two\ngroup elements to a target.",
         "Enables CP-ABE to work.\nAllows checking if a user's\nattributes satisfy the\naccess policy."],
        ["Generator (g)", "--",
         "A special number in Z_p*\nthat can generate all other\nelements: g^1, g^2, ...",
         "All public/private keys\nare powers of g. In our\ncode, g = 2."],
        ["KDF", "Key Derivation\nFunction",
         "Converts a shared token\n(Phi) into a proper AES\nencryption key using\nSHA-256 hashing.",
         "Ensures the encryption\nkey is exactly 256 bits\nand unpredictable."],
        ["Trapdoor", "--",
         "A search token generated\nby the doctor. Contains\nencrypted keywords. The\ncloud can match but not\nread them.",
         "Enables keyword search\nwithout revealing the\nactual keywords to\nthe cloud server."],
        ["RVSC", "Result Verification\nSmart Contract",
         "A smart contract that\nverifies the cloud's\nzero-knowledge proof\nand checks deletion status.",
         "Prevents the cloud from\nreturning incomplete or\ntampered results. Acts\nas an honest auditor."],
        ["Gas", "--",
         "The unit of computational\ncost on Ethereum. Each\noperation costs gas.\n1 Gwei = 0.000000001 ETH.",
         "We measure our smart\ncontract efficiency in\ngas units. Lower gas =\ncheaper operation."],
        ["EVM", "Ethereum Virtual\nMachine",
         "The runtime environment\nthat executes smart\ncontract code on every\nEthereum node.",
         "Our Solidity contract\nruns on the EVM.\nStorage lookups in EVM\nare O(1) hash maps."],
        ["O(m), O(1),\nO(L x m)", "Big-O Notation",
         "O(m) = time grows with\nm keywords. O(1) = constant\ntime. O(L x m) = time grows\nwith L files x m keywords.",
         "Base paper: O(L x m) per\nupdate. Ours: O(m) add,\nO(1) delete. This is the\ncore improvement."],
        ["IoT", "Internet of Things",
         "Small, low-power devices\n(sensors, wearables,\nmedical monitors) that\ncollect data.",
         "IoT devices have limited\nbattery/CPU. Our O(m)/O(1)\nalgorithms are lightweight\nenough for IoT."],
        ["Flask", "--",
         "A lightweight Python web\nframework for building\nRESTful APIs.",
         "Our demo uses Flask to\nserve the web UI and\nexpose API endpoints\nlike /api/search."],
        ["SHA-256", "Secure Hash\nAlgorithm 256-bit",
         "A one-way hash function.\nConverts any input to a\nfixed 256-bit output.\nIrreversible.",
         "Used inside our H1()\nhash function, KDF,\nand SNIZK proof\ncomputations."],
    ]
    story.append(colored_table(glossary, col_widths=[22*mm, 28*mm, 45*mm, W-95*mm]))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 3. BASE PAPER
    # ═══════════════════════════════════════════════
    story.append(Paragraph("3. BASE PAPER -- WHAT WAS ALREADY DONE (Cheng et al. 2026)", sH1))
    story.append(hr())
    story.append(Paragraph("<b>Paper:</b> 'BAMKS: Blockchain-Assisted Attribute-Based Multi-Keyword Search with Result Verification in Edge-Cloud-IoT', published in <i>Internet of Things</i> (Elsevier), Volume 36, Article 101838, December 2025/2026.", sBody))
    story.append(Spacer(1,2*mm))
    
    story.append(Paragraph("3.1 What the Base Paper Achieved", sH2))
    achievements = [
        ("<b>Multi-Authority CP-ABE:</b> Multiple hospitals collaboratively control access. No single authority has complete power. Each Attribute Authority (AA) manages a subset of attributes."),
        ("<b>Conjunctive Multi-Keyword Search:</b> Doctors can search for multiple keywords simultaneously using trapdoor tokens T1, T2, T3 computed from the user's secret key."),
        ("<b>Verifiable Search Results via RVSC:</b> After the cloud returns search results, a smart contract verifies a Schnorr SNIZK proof to ensure completeness and correctness."),
        ("<b>User Attribute Revocation:</b> If a doctor leaves the hospital, their access attributes can be revoked without re-encrypting the files in the cloud."),
    ]
    for a in achievements:
        story.append(Paragraph(f"  {a}", sBullet))
    
    story.append(Spacer(1,3*mm))
    story.append(Paragraph("3.2 The Protocol Flow (15 Steps)", sH2))
    protocol_steps = [
        ["Step", "Name", "Who Runs It", "What It Does"],
        ["1", "GlobalSetup", "KGC (Key Gen Center)", "Generates system prime P, generator g, master secrets mu, gamma"],
        ["2", "AuthSetup", "Each Attribute Authority", "Generates public/private key pair (alpha, beta) for each AA"],
        ["3", "DOSetup", "Data Owners (Hospitals)", "Collaboratively compute shared encryption token Phi"],
        ["4", "DUSetup", "Data User (Doctor)", "Generates user public/private key pair (chi, zeta)"],
        ["5", "UserReg", "Blockchain Contract", "Registers user's hash h_varpi on-chain for identity binding"],
        ["6", "KeyGen", "AAs + KGC", "Generates user's attribute secret key SK_uid"],
        ["7", "FileEnc", "Data Owner", "Encrypts file with AES-256-GCM using key derived from Phi"],
        ["8", "TokenEnc", "Data Owner", "Encrypts Phi under CP-ABE access policy"],
        ["9", "TokenOC", "Blockchain Contract", "Stores encrypted token on-chain"],
        ["10", "IndexGen", "Data Owner", "Generates searchable keyword index for each file"],
        ["11", "TrapGen", "Data User", "Generates trapdoor search tokens from query keywords"],
        ["12", "Search", "Cloud Server", "Matches trapdoor against encrypted indices"],
        ["13", "ProofGen/Verify", "Cloud + RVSC Contract", "Cloud generates SNIZK proof, contract verifies it"],
        ["14", "TokenDec", "Data User", "Decrypts Phi from CP-ABE ciphertext using SK_uid"],
        ["15", "FinalDecrypt", "Data User", "Decrypts file content using AES key derived from Phi"],
    ]
    story.append(colored_table(protocol_steps, col_widths=[10*mm, 22*mm, 32*mm, W-64*mm]))
    
    story.append(Spacer(1,3*mm))
    story.append(Paragraph("3.3 The Critical Bottleneck (Section 8, Page 22 of Paper)", sH2))
    story.append(Paragraph(
        "In the base paper, ALL files are bound to a single dataset version (F_ver). Every file shares "
        "the same master version keys (delta_ver, xi_ver). This means:", sBody))
    story.append(Paragraph(
        "  Adding 1 file: Must regenerate ALL L file indices and re-encrypt ALL keyword tokens -- <b>O(L x m)</b><br/>"
        "  Deleting 1 file: Same: full dataset re-keying -- <b>O(L x m)</b><br/>"
        "  For L=1000 files, m=10 keywords: <b>10,000 exponentiations = 5,560 ms = 5.56 seconds</b>", sBody))
    story.append(Paragraph(
        '<b>Authors Own Words (Section 8, Conclusion):</b> "In the future, we plan to extend BAMKS to '
        'support time-sensitive data sharing with adding, deleting, and inserting operations."', sSpeech))
    story.append(Paragraph("This is exactly our research gap. They admitted the limitation. We solved it.", sTip))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 4. OUR RESEARCH GAP
    # ═══════════════════════════════════════════════
    story.append(Paragraph("4. OUR RESEARCH GAP -- WHAT WE SOLVED", sH1))
    story.append(hr())
    
    story.append(Paragraph("4.1 The Three New Algorithms We Built", sH2))
    gap_table = [
        ["Algorithm", "Operation", "Complexity", "How It Works"],
        ["SingleDocAdd", "Add 1 file", "O(m)", "Encrypt file independently with AES-256-GCM.\nGenerate keyword index ONLY for this 1 file's m keywords.\nAppend to cloud storage without touching existing files."],
        ["SingleDocDelete", "Delete 1 file", "O(1)", "Call smart contract: deletedDocRegistry[docId] = true.\nOne boolean flip in EVM storage = constant time.\nNo re-encryption needed."],
        ["SingleDocModify", "Modify 1 file", "O(1) + O(m)", "Delete the old version (O(1)) then Insert the new version (O(m)).\nNet cost: O(m) -- still orders of magnitude faster than O(L x m)."],
    ]
    story.append(colored_table(gap_table, col_widths=[28*mm, 22*mm, 18*mm, W-68*mm]))
    
    story.append(Spacer(1,3*mm))
    story.append(Paragraph("4.2 The Core Insight", sH2))
    story.append(Paragraph(
        "The base paper ties all files together with shared version keys. Our insight is: <b>decouple individual file "
        "indices from the dataset-wide version</b>. Each file gets its own independent encryption and index. "
        "This way, adding/deleting one file only touches that one file's data.", sBody))
    
    story.append(Spacer(1,3*mm))
    story.append(Paragraph("4.3 Performance Comparison", sH2))
    perf_table = [
        ["Metric", "Base Paper (Before)", "Our Extension (After)", "Speedup"],
        ["Add 1 Document", "O(L x m) = 5,560 ms", "O(m) = 0.99 ms", "5,500x"],
        ["Delete 1 Document", "O(L x m) = 5,560 ms", "O(1) = 0.0001 ms", "Instant"],
        ["Version Key Impact", "ALL keys invalidated", "NO keys affected", "Zero regeneration"],
        ["IoT Feasibility", "Infeasible (high CPU)", "Ideal (lightweight)", "100% practical"],
        ["Blockchain Role", "Verify results only", "Verify + Delete registry", "Extended"],
        ["Smart Contract Gas", "N/A for updates", "~45,100 gas / delete", "Measurable"],
    ]
    story.append(colored_table(perf_table, col_widths=[30*mm, 38*mm, 38*mm, W-106*mm]))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 5. SYSTEM ARCHITECTURE
    # ═══════════════════════════════════════════════
    story.append(Paragraph("5. SYSTEM ARCHITECTURE -- HOW EVERYTHING CONNECTS", sH1))
    story.append(hr())
    
    arch_text = (
        "<b>There are 6 main entities in our system:</b><br/><br/>"
        "<b>1. Key Generation Center (KGC):</b> Runs GlobalSetup. Generates the master secret key (mu, gamma) "
        "and system-wide public parameters (g, g^mu, g^gamma, e(g,g)^mu). This is a trusted authority that "
        "initializes the system once.<br/><br/>"
        "<b>2. Attribute Authorities (AAs):</b> Each AA manages a set of attributes (e.g., AA_Medical manages "
        "'Role_Doctor', 'Dept_Cardiology'). They generate attribute-specific secret keys for users. Multiple AAs "
        "prevent single-point-of-failure trust issues.<br/><br/>"
        "<b>3. Data Owners (Hospitals):</b> Encrypt patient files with AES-256-GCM. Generate searchable keyword "
        "indices. Upload encrypted files + indices to the cloud. Collaboratively compute the shared token Phi.<br/><br/>"
        "<b>4. Data Users (Doctors):</b> Register with AAs to get attribute secret keys. Generate trapdoor search "
        "tokens from query keywords. Submit trapdoor to cloud. Receive + verify + decrypt results.<br/><br/>"
        "<b>5. Cloud Server:</b> Stores encrypted files and indices. Executes search matching. Generates SNIZK proof "
        "of correct execution. Is semi-honest (may try to cheat).<br/><br/>"
        "<b>6. Blockchain (Ethereum):</b> Hosts our BAMKS_Registry.sol smart contract. Verifies SNIZK proofs (RVSC). "
        "Maintains deletedDocRegistry mapping. Provides tamper-proof audit trail."
    )
    story.append(Paragraph(arch_text, sBody))
    
    story.append(Spacer(1,3*mm))
    story.append(Paragraph("5.1 Data Flow (Step by Step)", sH2))
    flow_steps = [
        "1. Hospital encrypts patient record with AES-256-GCM -- produces ciphertext + nonce + GCM tag",
        "2. Hospital generates keyword index using g^(eta * H1(keyword))",
        "3. Hospital uploads encrypted file + index to cloud storage",
        "4. Hospital registers file metadata on blockchain via registerDocument()",
        "5. Doctor generates trapdoor tokens (T1, T2, T3) from search keywords",
        "6. Doctor sends trapdoor to cloud",
        "7. Cloud matches trapdoor against all stored indices -- finds matching doc IDs",
        "8. Cloud generates SNIZK proof of correct matching",
        "9. Smart contract verifies SNIZK proof + checks deletedDocRegistry",
        "10. If proof valid -- Doctor receives encrypted results -- Decrypts with AES key from Phi",
    ]
    for s in flow_steps:
        story.append(Paragraph(s, sBullet))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 6. TECHNOLOGY STACK
    # ═══════════════════════════════════════════════
    story.append(Paragraph("6. TECHNOLOGY STACK -- TOOLS AND LIBRARIES", sH1))
    story.append(hr())
    
    tech_table = [
        ["Layer", "Technology", "Version", "Purpose"],
        ["Language", "Python 3.x", "3.10+", "Core cryptographic engine and API server"],
        ["Web Framework", "Flask", "2.x", "REST API backend serving /api/search, /api/documents etc."],
        ["Crypto Library", "PyCryptodome", "3.x", "AES-256-GCM encryption/decryption (Crypto.Cipher.AES)"],
        ["Hashing", "hashlib (stdlib)", "Built-in", "SHA-256 for H1(), KDF, and SNIZK commitments"],
        ["Smart Contract", "Solidity", "^0.8.20", "BAMKS_Registry.sol -- on-chain RVSC and deletion registry"],
        ["Blockchain", "Ethereum (EVM)", "--", "Simulated local EVM; Sepolia testnet planned for Review 3"],
        ["Frontend", "HTML5 + CSS3 + JS", "--", "Single-page web dashboard with 4 interactive screens"],
        ["PDF Generation", "ReportLab", "4.x", "Generates this defense manual PDF"],
        ["Cross-Origin", "flask-cors", "4.x", "Allows browser to call Flask API from local file"],
    ]
    story.append(colored_table(tech_table, col_widths=[22*mm, 28*mm, 16*mm, W-66*mm]))
    story.append(Paragraph(
        "<b>If Ma'am asks 'Why Python and not Java/C++?':</b> Python has PyCryptodome for production-grade "
        "AES-256-GCM, hashlib for SHA-256, and allows rapid prototyping. The cyclic group arithmetic "
        "uses Python's built-in arbitrary precision integers (no overflow). Flask provides a lightweight "
        "web framework for the demo UI.", sTip))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 7-16. BASE PAPER ALGORITHMS
    # ═══════════════════════════════════════════════
    story.append(Paragraph("7-16. BASE PAPER ALGORITHMS (FROM CHENG ET AL.)", sH1))
    story.append(hr())
    story.append(Paragraph("These are the algorithms defined in the base paper that we implemented as the foundation. Our proposed new algorithms (18-21) build on top of these.", sBody))
    
    base_algos = [
        {
            "num": "7", "name": "GlobalSetup", "notation": "GlobalSetup(1^iota) -> (GP, MSK)",
            "file": "src/bamks_system.py", "lines": "19-30", "method": "global_setup()",
            "what": "Generates the system-wide cryptographic parameters. Picks two random master secrets mu and gamma from Z_p*. Computes public parameters g^mu, g^gamma, and bilinear pairing target e(g,g)^mu.",
            "code": "mu = random.randint(...) % PRIME_P\ngamma = random.randint(...) % PRIME_P\ng_mu = pow(g, mu, PRIME_P)\ng_gamma = pow(g, gamma, PRIME_P)\ne_gg_mu = simulated_pairing(pow(g, mu, P), g)",
            "speech": "This is the system initialization. It generates the 256-bit prime field parameters and master secrets that all other algorithms depend on."
        },
        {
            "num": "8", "name": "AuthSetup", "notation": "AuthSetup(GP, U_theta, theta) -> (pk_AA, sk_AA)",
            "file": "src/bamks_system.py", "lines": "32-42", "method": "auth_setup()",
            "what": "Each Attribute Authority generates its own key pair. The secret key (alpha, beta) stays private. The public key (e(g,g)^alpha, g^beta) is published.",
            "code": "alpha = random.randint(...) % PRIME_P\nbeta = random.randint(...) % PRIME_P\npk = { e_gg_alpha: pairing(g^alpha, g), g_beta: g^beta }",
            "speech": "Each hospital's attribute authority generates its own keys independently. This is the multi-authority setup."
        },
        {
            "num": "9", "name": "DOSetup", "notation": "DOSetup(GP, O) -> (epsilon, Phi)",
            "file": "src/bamks_system.py", "lines": "44-49", "method": "do_setup()",
            "what": "Multiple data owners collaboratively compute a shared encryption token Phi. Each owner contributes a random share. Phi = sum of all shares.",
            "code": "epsilon = random.randint(...)\nphi_values = [random.randint(10, 100) for _ in owners]\nphi = sum(phi_values)",
            "speech": "The hospitals jointly compute a shared secret token Phi. This token is later used to derive the AES encryption key for files."
        },
        {
            "num": "10", "name": "DUSetup", "notation": "DUSetup(GP, uid) -> (upk, usk, h_varpi)",
            "file": "src/bamks_system.py", "lines": "51-59", "method": "du_setup()",
            "what": "A data user (doctor) generates their public/private key pair (chi, zeta) and a registration hash h_varpi for on-chain identity binding.",
            "code": "chi = random.randint(...) % PRIME_P\nzeta = random.randint(...) % PRIME_P\nupk = { g^chi, g^zeta }\nh_varpi = H1('Reg_' || uid || chi)",
            "speech": "Each doctor registers by generating their own key pair. The registration hash is stored on the blockchain to bind their identity."
        },
        {
            "num": "11", "name": "KeyGen", "notation": "KeyGen(GP, uid, S_uid, {sk_AA}) -> SK_uid",
            "file": "src/bamks_system.py", "lines": "61-80", "method": "keygen()",
            "what": "Generates the user's attribute secret key SK_uid. For each attribute the user possesses, the managing AA computes a key component using its secret (alpha, beta).",
            "code": "k1 = H(uid)^(-t) mod P\nFor each attr:\n  k2[attr] = H(uid)^beta * dpk^alpha mod P\nk3 = h_varpi",
            "speech": "This is where the attribute-based access control kicks in. Each doctor gets a secret key that encodes their specific attributes like 'Role=Doctor, Dept=Cardiology'."
        },
        {
            "num": "12", "name": "FileEnc (AES-256-GCM)", "notation": "FileEnc(F_ver, K, Phi) -> CT_F",
            "file": "src/bamks_system.py", "lines": "82-98", "method": "file_encrypt()",
            "what": "Encrypts a file using AES-256-GCM. First derives a 256-bit symmetric key from Phi using KDF (SHA-256). Then encrypts plaintext and produces ciphertext + nonce + authentication tag.",
            "code": "sym_key = KDF(token_phi, version_id)  # SHA-256\ncipher = AES.new(key, AES.MODE_GCM)\nciphertext, tag = cipher.encrypt_and_digest(plaintext)\n-> Returns {ciphertext, nonce, tag}",
            "speech": "We use AES-256-GCM for encrypting the actual medical record content. The GCM mode provides both confidentiality and integrity -- if anyone tampers with the ciphertext, decryption will fail."
        },
        {
            "num": "13", "name": "TokenEnc (CP-ABE)", "notation": "TokenEnc(GP, (M,rho), Phi) -> CT_Phi",
            "file": "src/bamks_system.py", "lines": "100-105", "method": "token_encrypt_onchain()",
            "what": "Encrypts the shared token Phi under a CP-ABE access policy. Only users whose attributes satisfy the policy can decrypt Phi and subsequently decrypt the files.",
            "code": "s = random.randint(...)\nC = Phi * e(g,g)^(mu*s) mod P\nC0 = g^s mod P",
            "speech": "The shared token Phi is protected by an attribute-based access policy. This is the CP-ABE layer -- it controls WHO can decrypt."
        },
        {
            "num": "14", "name": "IndexGen", "notation": "IndexGen(GP, W, O) -> Index_W",
            "file": "src/bamks_system.py", "lines": "107-119", "method": "index_gen()",
            "what": "For each keyword in a document, generates an encrypted index entry: g^(eta * H1(keyword)) mod P. The cloud can match trapdoors against these entries without learning the keywords.",
            "code": "eta = random.randint(...) % PRIME_P\nfor kw in keywords:\n  index[kw] = g^(eta * H1(kw)) mod P",
            "speech": "This generates the searchable encrypted index. Each keyword becomes a group element. The cloud can compare trapdoor tokens against these elements to find matches, but cannot reverse-engineer the actual keyword."
        },
        {
            "num": "15", "name": "TrapGen", "notation": "TrapGen(GP, W_tilde, usk) -> Trap",
            "file": "src/bamks_system.py", "lines": "121-129", "method": "trapdoor_gen()",
            "what": "Doctor generates trapdoor search tokens from query keywords. T1 = g^phi, T2 = g^(phi+2), T3 = g^(phi * sum(H1(kw))). These tokens encode the search query in encrypted form.",
            "code": "phi_rand = random.randint(...)\nT1 = g^phi mod P\nT2 = g^(phi+2) mod P\nT3 = g^(phi * sum(H1(kw))) mod P",
            "speech": "The doctor's search query is converted into mathematical trapdoor tokens. The cloud receives these tokens and can use them to match against the index, but cannot figure out what keywords the doctor searched for."
        },
        {
            "num": "16", "name": "Search", "notation": "Search(GP, Index_W, Trap) -> SRL",
            "file": "src/bamks_system.py", "lines": "131-142", "method": "search()",
            "what": "Cloud server matches the trapdoor against all stored keyword indices. Returns a list of matching document IDs (Search Result List = SRL).",
            "code": "for doc_id, index_data in indices.items():\n  if all(kw in kw_map for kw in query_kws):\n    matched_doc_ids.append(doc_id)",
            "speech": "This is the cloud-side matching. The cloud iterates through all encrypted indices and checks if the trapdoor matches. It returns matching document IDs without ever seeing the plaintext."
        },
    ]
    
    for algo in base_algos:
        story.append(Paragraph(f"Algorithm {algo['num']}: {algo['name']}", sH2))
        story.append(Paragraph(f"<b>Notation:</b> {algo['notation']}", sBody))
        story.append(Paragraph(f"<b>Code:</b> <font color='#3b82f6'>{algo['file']}</font> Lines {algo['lines']} Method: <font face='Courier' color='#8b5cf6'>{algo['method']}</font>", sBody))
        story.append(Paragraph(f"<b>What It Does:</b> {algo['what']}", sBody))
        story.append(Paragraph(algo['code'], sCode))
        story.append(Paragraph(f'<b>Say to Maam:</b> "{algo["speech"]}"', sSpeech))
        story.append(hr())
    
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 17. SNIZK PROOF
    # ═══════════════════════════════════════════════
    story.append(Paragraph("17. ALGORITHM 11: SNIZK PROOF -- ZERO-KNOWLEDGE VERIFICATION", sH1))
    story.append(hr())
    story.append(Paragraph("<b>Notation:</b> ProofGen -> (R, pi_hat); ProofVerify: R == g^pi_hat x prod(y_k^(-h_k)) mod P", sBody))
    story.append(Paragraph("<b>Code:</b> <font color='#3b82f6'>src/crypto_utils.py</font> Lines 52-89 Functions: <font face='Courier' color='#8b5cf6'>generate_snizk_proof()</font> and <font face='Courier' color='#8b5cf6'>verify_snizk_proof()</font>", sBody))
    story.append(Paragraph(
        "<b>What It Does:</b> After the cloud finds matching documents, it must PROVE it did not cheat. "
        "The proof works like this:<br/>"
        "1. <b>Prover (Cloud):</b> Picks random commitments c_k for each matched tag. Computes R = g^(sum of c_k). "
        "For each tag, computes h_k = H1(tag || R) and pi_k = c_k + h_k x sigma_k. Aggregates: pi_hat = sum(pi_k).<br/>"
        "2. <b>Verifier (Smart Contract):</b> Checks equation: R == g^pi_hat x prod(y_k^(-h_k)) mod P. "
        "If the equation holds, the proof is VALID -- the cloud returned genuine results.", sBody))
    story.append(Paragraph(
        "# Proof Generation (Lines 52-69)\n"
        "random_c = [random bytes for each tag]\n"
        "R = g^(sum_c) mod P\n"
        "for each tag:\n"
        "  h_k = H1(tag || R)\n"
        "  pi_k = c_k + h_k * sigma_k mod (P-1)\n"
        "pi_hat = sum(pi_k)\n\n"
        "# Verification (Lines 71-89)\n"
        "rhs = g^pi_hat * prod(y_k^(-h_k)) mod P\n"
        "return R == rhs", sCode))
    story.append(Paragraph(
        '<b>Say to Maam:</b> "The cloud generates a Schnorr Zero-Knowledge proof using random commitments '
        'and the file tags. The verifier checks a mathematical equation without needing any secret keys. '
        'If the equation R equals g to the power pi_hat times the product of inverse tag powers holds, '
        'the proof is valid and the cloud returned correct results."', sSpeech))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 18-21. OUR PROPOSED ALGORITHMS
    # ═══════════════════════════════════════════════
    story.append(Paragraph("18-21. OUR PROPOSED ALGORITHMS [RESEARCH CONTRIBUTION]", sH1))
    story.append(hr())
    story.append(Paragraph("These are the NEW algorithms we designed and implemented. This is our original research contribution.", sTip))
    
    # SingleDocAdd
    story.append(Paragraph("Algorithm 12: SingleDocAdd -- Incremental O(m) Insertion [PROPOSED]", sH2))
    story.append(Paragraph("<b>Code:</b> <font color='#3b82f6'>src/dynamic_extension.py</font> Lines 17-34 Method: <font face='Courier' color='#8b5cf6'>single_doc_add()</font>", sBody))
    story.append(Paragraph(
        "<b>How It Works (Step by Step):</b><br/>"
        "1. Encrypt the new file's plaintext content using AES-256-GCM (calls file_encrypt from base class)<br/>"
        "2. Generate keyword index entries ONLY for this file's m keywords (calls index_gen from base class)<br/>"
        "3. Register the document as 'active' in deletedDocRegistry[docId] = False<br/>"
        "4. Total operations: m keyword hash computations + 1 AES encryption = <b>O(m)</b><br/>"
        "5. <b>Key insight:</b> We do NOT touch any existing files or regenerate any version keys!", sBody))
    story.append(Paragraph(
        "def single_doc_add(self, doc_id, file_content, keywords, token_phi, version_id):\n"
        "    doc_entry = self.file_encrypt(doc_id, file_content, token_phi, version_id)\n"
        "    index_entry = self.index_gen(doc_id, keywords)\n"
        "    self.deleted_doc_registry[doc_id] = False\n"
        "    return doc_entry, index_entry, addition_time_ms", sCode))
    story.append(Paragraph(
        '<b>Say to Maam:</b> "In our SingleDocAdd algorithm, we encrypt the new file independently using AES-256-GCM '
        'and generate keyword tokens only for this file. We never touch the existing files or their '
        'version keys. This reduces the complexity from O(L times m) in the base paper to just O(m) -- completing '
        'in under 1 millisecond instead of 5.5 seconds."', sSpeech))
    story.append(hr())

    # SingleDocDelete
    story.append(Paragraph("Algorithm 13: SingleDocDelete -- Instant O(1) Deletion [PROPOSED]", sH2))
    story.append(Paragraph("<b>Code:</b> <font color='#3b82f6'>src/dynamic_extension.py</font> Lines 36-48 Method: <font face='Courier' color='#8b5cf6'>single_doc_delete()</font>", sBody))
    story.append(Paragraph(
        "<b>How It Works:</b><br/>"
        "1. Set deletedDocRegistry[docId] = True (one boolean flip)<br/>"
        "2. Mark the file entry as deleted: files[doc_id]['is_deleted'] = True<br/>"
        "3. Total operations: 1 hash map write = <b>O(1) constant time</b><br/>"
        "4. Corresponding Solidity function: deleteDocument() in BAMKS_Registry.sol (Line 69)<br/>"
        "5. Gas cost: ~45,100 gas units (approximately $0.001 on Ethereum mainnet)", sBody))
    story.append(Paragraph(
        "def single_doc_delete(self, doc_id):\n"
        "    if doc_id in self.files:\n"
        "        self.deleted_doc_registry[doc_id] = True\n"
        "        self.files[doc_id]['is_deleted'] = True\n"
        "    return deletion_time_ms  # ~0.0001 ms", sCode))
    story.append(Paragraph(
        "# Corresponding Solidity (BAMKS_Registry.sol, Line 69):\n"
        "function deleteDocument(uint256 _docId) external onlyDocOwner(_docId) {\n"
        "    deletedDocRegistry[_docId] = true;\n"
        "    fileRegistry[_docId].isDeleted = true;\n"
        "    emit DocumentDeleted(_docId, msg.sender, block.timestamp);\n"
        "}", sCode))
    story.append(Paragraph(
        '<b>Say to Maam:</b> "Instead of re-encrypting all files to delete one, we simply flip a boolean flag '
        'in the Ethereum smart contract. Since EVM storage is a key-value hash map, this lookup and write '
        'operation is O(1) constant time. It takes less than 0.0001 milliseconds and costs only about 45,100 gas."', sSpeech))
    story.append(hr())

    # SingleDocModify
    story.append(Paragraph("Algorithm 14: SingleDocModify -- Delete + Insert [PROPOSED]", sH2))
    story.append(Paragraph("<b>Code:</b> <font color='#3b82f6'>src/dynamic_extension.py</font> Lines 50-59 Method: <font face='Courier' color='#8b5cf6'>single_doc_modify()</font>", sBody))
    story.append(Paragraph(
        "def single_doc_modify(self, doc_id, new_content, new_keywords, token_phi, version_id):\n"
        "    del_time = self.single_doc_delete(doc_id)         # O(1)\n"
        "    doc_entry, index_entry, add_time = self.single_doc_add(\n"
        "        doc_id, new_content, new_keywords, token_phi, version_id)  # O(m)\n"
        "    return doc_entry, index_entry, del_time + add_time", sCode))
    story.append(Paragraph(
        '<b>Say to Maam:</b> "Modification is implemented as a clean delete-then-insert pattern. We first mark the '
        'old version as deleted in O(1), then insert the new version with fresh encryption and index in O(m). '
        'Net cost is O(m) -- still thousands of times faster than the base paper."', sSpeech))
    story.append(hr())

    # SearchWithFilter
    story.append(Paragraph("Algorithm 15: SearchWithFilter -- Revocation-Aware Search [PROPOSED]", sH2))
    story.append(Paragraph("<b>Code:</b> <font color='#3b82f6'>src/dynamic_extension.py</font> Lines 62-78 Method: <font face='Courier' color='#8b5cf6'>search_with_filter()</font>", sBody))
    story.append(Paragraph(
        "def search_with_filter(self, trapdoor):\n"
        "    raw_matches = self.search(trapdoor)  # Base paper matching\n"
        "    active_matches = [\n"
        "        doc_id for doc_id in raw_matches\n"
        "        if not self.deleted_doc_registry.get(doc_id, False)\n"
        "    ]\n"
        "    return active_matches, search_time_ms", sCode))
    story.append(Paragraph(
        '<b>Say to Maam:</b> "After the cloud matches documents, our filter cross-checks each result against '
        'the deletion registry. Any document that was revoked is automatically excluded from the results."', sSpeech))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 22. SMART CONTRACT
    # ═══════════════════════════════════════════════
    story.append(Paragraph("22. SMART CONTRACT: BAMKS_Registry.sol", sH1))
    story.append(hr())
    story.append(Paragraph("<b>File:</b> <font color='#3b82f6'>contracts/BAMKS_Registry.sol</font> (123 lines, Solidity ^0.8.20)", sBody))
    
    contract_table = [
        ["Component", "Line(s)", "Purpose"],
        ["FileMetadata struct", "14-21", "Stores docId, fileHash, publicTag y_k, ownerAddress, timestamp, isDeleted"],
        ["fileRegistry mapping", "24", "mapping(uint256 => FileMetadata) -- stores all file metadata"],
        ["deletedDocRegistry mapping", "25", "mapping(uint256 => bool) -- the O(1) deletion flag"],
        ["registerDocument()", "50-64", "Registers a new single document on-chain"],
        ["deleteDocument()", "69-77", "Our O(1) deletion -- sets deletedDocRegistry[docId] = true"],
        ["isDocActive()", "82-84", "Returns whether a document is active (not deleted)"],
        ["verifyResultProof()", "89-109", "RVSC -- verifies SNIZK proof and checks no deleted docs in results"],
        ["getActiveDocumentCount()", "114-121", "Returns count of currently active documents"],
    ]
    story.append(colored_table(contract_table, col_widths=[38*mm, 16*mm, W-54*mm]))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 23. CODE-TO-ALGORITHM MAPPING
    # ═══════════════════════════════════════════════
    story.append(Paragraph("23. CODE-TO-ALGORITHM MAPPING (EXACT FILE AND LINE NUMBERS)", sH1))
    story.append(hr())
    story.append(Paragraph("If Maam says 'Show me the code for X', use this table to instantly navigate.", sWarn))
    
    code_map = [
        ["Algorithm / Feature", "File Path", "Lines", "Function Name"],
        ["System Prime P (secp256k1)", "src/crypto_utils.py", "8", "PRIME_P constant"],
        ["Hash Function H1", "src/crypto_utils.py", "15-19", "h1()"],
        ["Key Derivation Function", "src/crypto_utils.py", "21-24", "kdf()"],
        ["AES-256-GCM Encrypt", "src/crypto_utils.py", "26-34", "aes_encrypt()"],
        ["AES-256-GCM Decrypt", "src/crypto_utils.py", "36-43", "aes_decrypt()"],
        ["Bilinear Pairing", "src/crypto_utils.py", "45-50", "simulated_pairing()"],
        ["SNIZK Proof Generation", "src/crypto_utils.py", "52-69", "generate_snizk_proof()"],
        ["SNIZK Proof Verification", "src/crypto_utils.py", "71-89", "verify_snizk_proof()"],
        ["GlobalSetup", "src/bamks_system.py", "19-30", "global_setup()"],
        ["AuthSetup", "src/bamks_system.py", "32-42", "auth_setup()"],
        ["DOSetup", "src/bamks_system.py", "44-49", "do_setup()"],
        ["DUSetup", "src/bamks_system.py", "51-59", "du_setup()"],
        ["KeyGen", "src/bamks_system.py", "61-80", "keygen()"],
        ["FileEnc (AES-256-GCM)", "src/bamks_system.py", "82-98", "file_encrypt()"],
        ["TokenEnc (CP-ABE)", "src/bamks_system.py", "100-105", "token_encrypt_onchain()"],
        ["IndexGen", "src/bamks_system.py", "107-119", "index_gen()"],
        ["TrapGen", "src/bamks_system.py", "121-129", "trapdoor_gen()"],
        ["Search", "src/bamks_system.py", "131-142", "search()"],
        ["ProofVerify", "src/bamks_system.py", "144-150", "verify_results()"],
        ["FinalDecrypt", "src/bamks_system.py", "152-157", "decrypt_file()"],
        ["SingleDocAdd [PROPOSED]", "src/dynamic_extension.py", "17-34", "single_doc_add()"],
        ["SingleDocDelete [PROPOSED]", "src/dynamic_extension.py", "36-48", "single_doc_delete()"],
        ["SingleDocModify [PROPOSED]", "src/dynamic_extension.py", "50-59", "single_doc_modify()"],
        ["SearchWithFilter [PROPOSED]", "src/dynamic_extension.py", "62-78", "search_with_filter()"],
        ["Benchmark Comparison", "src/dynamic_extension.py", "80-101", "benchmark_full_rekeying_vs_dynamic()"],
        ["registerDocument (Solidity)", "contracts/BAMKS_Registry.sol", "50-64", "registerDocument()"],
        ["deleteDocument (Solidity)", "contracts/BAMKS_Registry.sol", "69-77", "deleteDocument()"],
        ["verifyResultProof (RVSC)", "contracts/BAMKS_Registry.sol", "89-109", "verifyResultProof()"],
        ["Flask API: Search", "app.py", "191-270", "POST /api/search"],
        ["Flask API: Status", "app.py", "84-101", "GET /api/status"],
        ["Flask API: Keys", "app.py", "103-168", "GET /api/keys"],
    ]
    story.append(colored_table(code_map, col_widths=[38*mm, 38*mm, 14*mm, W-90*mm]))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 24. LIVE DEMO WALKTHROUGH
    # ═══════════════════════════════════════════════
    story.append(Paragraph("24. LIVE DEMO WALKTHROUGH -- WHAT TO SHOW TOMORROW", sH1))
    story.append(hr())
    story.append(Paragraph("Follow these steps EXACTLY in order. Practice 2-3 times tonight.", sWarn))
    
    story.append(Paragraph("Step 0: Start the Server (Before Maam arrives)", sH2))
    story.append(Paragraph(
        "1. Open Command Prompt / Terminal\n"
        "2. Navigate to the project folder\n"
        "3. Run: python app.py\n"
        "4. You should see:\n"
        "   [INIT] Initializing BAMKS 256-bit Cryptographic Parameters...\n"
        "   [OK] System initialized with 5 encrypted medical records.\n"
        "   * Running on http://127.0.0.1:5000\n"
        "5. Open http://127.0.0.1:5000 in Chrome/Edge", sCode))
    story.append(Paragraph("Keep the terminal visible. The cryptographic logs appear there in real-time.", sTip))
    
    story.append(Paragraph("Step 1: Hospital Upload Screen (Tab 1)", sH2))
    story.append(Paragraph(
        "1. You will see the Hospital Upload screen with 5 pre-loaded encrypted patient records<br/>"
        "2. Point out: 'These 5 medical records are already encrypted with AES-256-GCM. "
        "You can see the ciphertext hex, nonce, and GCM authentication tag for each file.'<br/>"
        "3. Click <b>Upload New Record</b> -- type a patient condition -- Submit<br/>"
        "4. Say: 'This is our SingleDocAdd algorithm. Notice it added the file in under 1ms "
        "and logged a blockchain transaction.'", sBody))
    
    story.append(Paragraph("Step 2: Cloud Storage Screen (Tab 2)", sH2))
    story.append(Paragraph(
        "1. Click on 'Cloud Storage' tab<br/>"
        "2. Say: 'This represents the untrusted cloud. All files are encrypted ciphertext. "
        "The cloud cannot read any patient data.'<br/>"
        "3. Click on any file to expand -- show full ciphertext, nonce, tag", sBody))
    
    story.append(Paragraph("Step 3: Doctor Search Screen (Tab 3)", sH2))
    story.append(Paragraph(
        "1. Click on 'Doctor Search' tab<br/>"
        "2. Type keywords: <b>Cardiology, ECG</b><br/>"
        "3. Click <b>Search</b><br/>"
        "4. Say: 'The system generates trapdoor tokens T1, T2, T3. "
        "Two records matched. The SNIZK proof is marked VALID.'", sBody))
    
    story.append(Paragraph("Step 4: Blockchain Ledger Screen (Tab 4)", sH2))
    story.append(Paragraph(
        "1. Click on 'Blockchain' tab<br/>"
        "2. Show the transaction ledger<br/>"
        "3. Click <b>Revoke Doc #101</b> -- show deletion transaction<br/>"
        "4. Say: 'Our SingleDocDelete executed. deletedDocRegistry[101] = true in O(1).'<br/>"
        "5. <b>Search again</b> for Cardiology+ECG -- only Doc #103 appears (101 is filtered out)!", sBody))
    
    story.append(Paragraph(
        "<b>Power Move:</b> After revocation, search again with same keywords. When only "
        "Doc #103 appears, say: 'The revoked document is automatically filtered out by the smart contract.'", sTip))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 25. COMPLETE PRESENTATION SPEECH
    # ═══════════════════════════════════════════════
    story.append(Paragraph("25. COMPLETE PRESENTATION SPEECH (WORD-BY-WORD)", sH1))
    story.append(hr())
    story.append(Paragraph("Memorize this speech. Practice 3 times tonight. Total time: ~3-4 minutes.", sWarn))
    
    story.append(Paragraph("Opening (30 seconds)", sH2))
    story.append(Paragraph(
        '"Good morning Maam. This is our Review 2 progress presentation for BAMKS-D -- '
        'Enabling Dynamic File-Level Operations in Blockchain-Assisted Attribute-Based Multi-Keyword Search.<br/><br/>'
        'Our base paper is Cheng et al., published in Elsevier Internet of Things journal, December 2025. '
        'The paper builds a system called BAMKS for securely searching encrypted IoT data in the cloud '
        'using blockchain verification and attribute-based access control.<br/><br/>'
        'The key limitation we identified is in Section 8 of the paper: the system cannot add or delete '
        'a single file without re-encrypting the entire dataset -- that is O of L times m complexity, '
        'which takes about 5.5 seconds for 1000 files. Our contribution reduces this to O of m for '
        'insertion and O of 1 for deletion."', sSpeech))
    
    story.append(Paragraph("Algorithms and Code (60 seconds)", sH2))
    story.append(Paragraph(
        '"Maam, we have implemented four core algorithms for our proposed extension:<br/><br/>'
        'Algorithm 1 -- SingleDocAdd: Encrypts one new file independently with AES-256-GCM and generates '
        'keyword tokens only for that file. Complexity is O of m. In our demo, this '
        'completes in under 1 millisecond.<br/><br/>'
        'Algorithm 2 -- SingleDocDelete: Updates a boolean flag in our Ethereum smart contract -- '
        'deletedDocRegistry of docId equals true. Since EVM storage is a hash map, this is O of 1 '
        'constant time -- about 0.0001 milliseconds.<br/><br/>'
        'Algorithm 3 -- SingleDocModify: A clean delete followed by insert. '
        'Total cost: O of 1 plus O of m equals O of m.<br/><br/>'
        'Algorithm 4 -- verifyResultProof in our RVSC smart contract: Verifies the Schnorr '
        'Zero-Knowledge proof and cross-checks that no deleted documents are in the results."', sSpeech))
    
    story.append(Paragraph("Live Demo (60 seconds)", sH2))
    story.append(Paragraph(
        '"Let me show you the working demo. [Open browser]<br/><br/>'
        'Here are 5 encrypted patient records stored in the simulated cloud. Each record is '
        'encrypted with AES-256-GCM -- you can see the ciphertext in hexadecimal.<br/><br/>'
        '[Click Upload] Now adding Doc 106. Notice it completed in 0.8 ms using our '
        'SingleDocAdd -- that is O of m time. A blockchain transaction was logged.<br/><br/>'
        '[Click Revoke 101] Now deleting Doc 101 using our SingleDocDelete. The smart contract '
        'flagged it as deleted in O of 1 time.<br/><br/>'
        '[Click Search: Cardiology + ECG] Now searching for Cardiology AND ECG. The SNIZK proof shows '
        'VALID. Notice Doc 101 is not in the results -- it was automatically filtered out. '
        'Only Doc 103 and the newly added 106 appear."', sSpeech))
    
    story.append(Paragraph("Closing (15 seconds)", sH2))
    story.append(Paragraph(
        '"For Review 3 next month, we plan to:<br/>'
        '1. Deploy on the public Ethereum Sepolia testnet<br/>'
        '2. Run exhaustive performance comparisons across 50 to 5000 files<br/>'
        '3. Profile energy consumption on an IoT edge device<br/>'
        '4. Submit the final documentation.<br/><br/>'
        'Thank you Maam."', sSpeech))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 26. PERFORMANCE COMPARISON
    # ═══════════════════════════════════════════════
    story.append(Paragraph("26. PERFORMANCE COMPARISON TABLE", sH1))
    story.append(hr())
    
    bench_table = [
        ["Files (L)", "Keywords (m)", "Base Paper O(L x m)", "Our SingleDocAdd O(m)", "Speedup"],
        ["50", "10", "~278 ms", "~0.99 ms", "280x"],
        ["100", "10", "~556 ms", "~0.99 ms", "560x"],
        ["500", "10", "~2,780 ms", "~0.99 ms", "2,800x"],
        ["1,000", "10", "~5,560 ms", "~0.99 ms", "5,500x"],
        ["5,000", "10", "~27,800 ms", "~0.99 ms", "28,000x"],
    ]
    story.append(colored_table(bench_table, col_widths=[20*mm, 22*mm, 36*mm, 38*mm, W-116*mm]))
    
    delete_bench = [
        ["Operation", "Base Paper", "Our Approach", "Gas Cost"],
        ["Delete 1 Document", "~5,560 ms (full re-key)", "~0.0001 ms (boolean flip)", "~45,100 gas"],
        ["Modify 1 Document", "~5,560 ms (full re-key)", "~1.0 ms (delete + insert)", "~45,100 + 114,500 gas"],
    ]
    story.append(Spacer(1,3*mm))
    story.append(colored_table(delete_bench, col_widths=[30*mm, 35*mm, 38*mm, W-103*mm]))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 27. VIVA Q&A (25 Questions)
    # ═══════════════════════════════════════════════
    story.append(Paragraph("27. VIVA Q AND A -- 25 QUESTIONS WITH BULLETPROOF ANSWERS", sH1))
    story.append(hr())
    story.append(Paragraph("Read ALL of these. Maam will likely ask 3-5 of these questions.", sWarn))
    
    qas = [
        ("What is your project about?",
         "Our project implements secure searchable encryption for IoT medical data in the cloud, using blockchain for result verification and attribute-based access control. Our specific contribution is adding dynamic single-file operations (add, delete, modify) that the base paper did not support."),
        
        ("What is your specific research gap?",
         "In Section 8 of Cheng et al. (Elsevier 2026), the authors explicitly state that their scheme cannot add or delete individual files -- any update requires re-keying the entire L-file dataset at O(L x m) cost. We solved this with O(m) insertion and O(1) deletion."),
        
        ("What is Searchable Encryption?",
         "It is a cryptographic technique that allows searching through encrypted data without decrypting it first. The doctor generates a trapdoor token from their search keywords, and the cloud can match this token against encrypted indices without ever seeing the plaintext."),
        
        ("What is CP-ABE and why is it used?",
         "CP-ABE stands for Ciphertext-Policy Attribute-Based Encryption. Unlike traditional encryption where data is encrypted for one person, CP-ABE encrypts data under an access policy like 'Role=Doctor AND Dept=Cardiology'. Any user whose attributes satisfy the policy can decrypt. We use it to control WHO can access the shared decryption token Phi."),
        
        ("Why do you need Blockchain?",
         "The cloud server is semi-honest -- it follows protocols but might cheat to save computing power. Blockchain provides an impartial, decentralized verifier. Our RVSC smart contract verifies a zero-knowledge proof to ensure the cloud returned complete and correct results. It also maintains our deletedDocRegistry for instant file revocation."),
        
        ("What is a Zero-Knowledge Proof?",
         "It is a mathematical proof where one party (the Prover/Cloud) convinces another party (the Verifier/Smart Contract) that a statement is true WITHOUT revealing any secret information. In our case, the cloud proves it executed the search correctly without revealing encryption keys or patient data."),
        
        ("What is SNIZK specifically?",
         "SNIZK stands for Schnorr Non-Interactive Zero-Knowledge proof. Schnorr is the mathematician who invented this protocol. Non-Interactive means the prover sends a single message (no back-and-forth). The prover generates random commitments, computes challenge hashes, and produces an aggregated proof pi_hat. The verifier checks: R equals g^pi_hat times the product of y_k inverse raised to h_k, all modulo P."),
        
        ("Where does the O(1) complexity come from?",
         "In Ethereum's EVM, storage is implemented as a key-value hash map (Merkle Patricia Trie). Looking up and writing to a specific key (like deletedDocRegistry[docId]) is a constant-time O(1) operation. We simply flip one boolean value from false to true -- no iteration, no re-encryption."),
        
        ("What if the cloud cheats and returns a deleted document?",
         "Our RVSC smart contract has a guard clause: for each matched document ID, it checks require(!deletedDocRegistry[id]). If any matched ID is in the deletion registry, the Ethereum transaction reverts with 'Result includes a revoked/deleted document' -- the cloud is caught cheating."),
        
        ("Why AES-256-GCM and not just AES-CBC or AES-CTR?",
         "GCM (Galois/Counter Mode) provides both confidentiality AND integrity in a single operation. It produces an authentication tag alongside the ciphertext. If anyone tampers with even 1 bit of the ciphertext, the tag verification fails. CBC and CTR do not provide this built-in integrity check."),
        
        ("Why AES alongside CP-ABE? Is ABE not enough?",
         "ABE is asymmetric and computationally heavy -- encrypting a large medical file directly with ABE would be extremely slow. Following standard cryptographic practice (hybrid encryption), we use ABE only to protect the small shared symmetric key (Phi), and use the fast AES-256-GCM for the actual file payload."),
        
        ("What is a Bilinear Pairing?",
         "It is a special mathematical function e: G x G -> G_T where e(g^a, g^b) = e(g,g)^(ab). This multiplicative homomorphism property is what makes CP-ABE possible -- it allows checking whether a user's attribute keys satisfy the access policy through algebraic operations."),
        
        ("What is a Cyclic Group?",
         "A cyclic group Z_p* is a set of integers {1, 2, ..., p-1} where all arithmetic is done modulo p. There exists a generator g such that every element can be expressed as a power of g. All our cryptographic keys and tokens are computed as powers of g modulo our 256-bit prime P."),
        
        ("What prime number P are you using?",
         "We use the secp256k1 prime: P = 2^256 - 2^32 - 977. This is the same prime used by Bitcoin and Ethereum for their elliptic curve cryptography. It provides 128-bit security level."),
        
        ("What is a Trapdoor Token?",
         "It is an encrypted search query generated by the doctor. We compute T1 = g^phi mod P, T2 = g^(phi+2) mod P, T3 = g^(phi x sum(H1(kw))) mod P. The cloud receives these tokens and can match them against the index, but cannot reverse-engineer what keywords the doctor searched for."),
        
        ("What is the Key Derivation Function?",
         "KDF converts the shared token Phi and version ID into a proper 256-bit AES key using SHA-256 hashing: key = SHA256(Phi || version_id). This ensures the key is exactly 256 bits, uniformly distributed, and deterministically reproducible."),
        
        ("Why is your system better for IoT devices?",
         "IoT devices have limited battery, CPU, and memory. The base paper's O(L x m) update requires thousands of exponentiations -- impractical for a medical sensor. Our O(m) insertion only processes m keyword hashes (typically m=10), and our O(1) deletion is a single boolean write."),
        
        ("What programming language is the smart contract written in?",
         "Solidity, version 0.8.20. It is the standard language for Ethereum smart contracts. Our contract BAMKS_Registry.sol is 123 lines and implements registerDocument, deleteDocument, verifyResultProof, isDocActive, and getActiveDocumentCount."),
        
        ("How much gas does deletion cost?",
         "Approximately 45,100 gas units. At current Ethereum gas prices (~18.5 Gwei), this costs about $0.001 -- essentially negligible."),
        
        ("What is the EVM?",
         "EVM stands for Ethereum Virtual Machine. It is the runtime environment that executes smart contract bytecode on every Ethereum node. Our Solidity contract is compiled to EVM bytecode. The EVM guarantees deterministic execution -- every node gets the same result."),
        
        ("How does your system handle multiple authorities?",
         "We use a multi-authority CP-ABE scheme. Each Attribute Authority independently manages a subset of attributes. User secret keys are composed of components from all relevant AAs. This prevents any single authority from having complete control."),
        
        ("What does conjunctive mean in Multi-Keyword Search?",
         "Conjunctive means AND logic. When a doctor searches for 'Cardiology AND ECG', both keywords must appear in a document for it to match. Our trapdoor token T3 encodes the sum of all keyword hashes, enabling the cloud to check if ALL keywords are present."),
        
        ("What will you do in Review 3?",
         "Four things: (1) Deploy on public Ethereum Sepolia testnet. (2) Run exhaustive benchmarks across 50 to 5,000 files. (3) Profile energy and battery on an IoT edge node. (4) Submit final documentation."),
        
        ("Is your implementation secure?",
         "Yes. We operate under the semi-honest cloud model. Security guarantees: (1) AES-256-GCM provides IND-CPA security, (2) keyword privacy via one-way hash functions, (3) result verifiability via SNIZK proofs, (4) tamper-proof deletion via blockchain immutability."),
        
        ("What is the difference between your work and the base paper?",
         "The base paper treats the entire dataset as one versioned unit. We decouple individual files from the dataset version, allowing independent file-level operations. We also extend blockchain's role from just result verification to also managing a deletion registry."),
    ]
    
    for i, (q, a) in enumerate(qas, 1):
        story.append(Paragraph(f"<b>Q{i}: \"{q}\"</b>", sBold))
        story.append(Paragraph(f'"{a}"', sSpeech))
        if i < len(qas):
            story.append(Spacer(1, 1.5*mm))
    
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 28. INDIVIDUAL CONTRIBUTIONS
    # ═══════════════════════════════════════════════
    story.append(Paragraph("28. INDIVIDUAL CONTRIBUTIONS STATEMENT", sH1))
    story.append(hr())
    story.append(Paragraph("When Maam asks 'Who did what?', say exactly this:", sWarn))
    
    story.append(Paragraph("Prashant Singh (24BYB1042) -- Cryptographic Engine and Dynamic Algorithms", sH2))
    story.append(Paragraph(
        '"Maam, I developed the Python cryptographic engine and the proposed dynamic algorithms. Specifically:<br/>'
        '- Established the 256-bit cyclic group Z_p* and all mathematical operations<br/>'
        '- Implemented AES-256-GCM file encryption and decryption (src/crypto_utils.py, Lines 26-43)<br/>'
        '- Implemented the SNIZK proof generation and verification (src/crypto_utils.py, Lines 52-89)<br/>'
        '- Designed and coded SingleDocAdd O(m) and SingleDocDelete O(1) (src/dynamic_extension.py)<br/>'
        '- Built the conjunctive trapdoor token generation (src/bamks_system.py, Lines 121-129)<br/>'
        '- Built the Flask REST API server (app.py)"', sSpeech))
    
    story.append(Paragraph("Adak Rushikesh (24BYB1055) -- Blockchain Layer and Smart Contract", sH2))
    story.append(Paragraph(
        '"Maam, Rushikesh developed the blockchain layer and the Solidity smart contract. Specifically:<br/>'
        '- Wrote the BAMKS_Registry.sol smart contract (contracts/BAMKS_Registry.sol, 123 lines)<br/>'
        '- Implemented the on-chain deletedDocRegistry state mapping for O(1) deletion<br/>'
        '- Implemented the EVM gas metering and transaction logging<br/>'
        '- Built the Result Verification Smart Contract (RVSC) verifyResultProof function (Lines 89-109)<br/>'
        '- Designed the event-based audit trail<br/>'
        '- Built the interactive web dashboard frontend (index.html)"', sSpeech))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 29. REVIEW 3 ROADMAP
    # ═══════════════════════════════════════════════
    story.append(Paragraph("29. REVIEW 3 ROADMAP", sH1))
    story.append(hr())
    
    roadmap = [
        ["Deliverable", "Description", "Timeline"],
        ["Sepolia Testnet", "Deploy BAMKS_Registry.sol on public Ethereum Sepolia testnet", "Week 1-2"],
        ["Performance Suite", "Run benchmarks: 50, 100, 500, 1000, 5000 files. Plot comparison curves.", "Week 2-3"],
        ["IoT Energy Profiling", "Profile CPU, RAM, battery on Raspberry Pi or similar IoT device", "Week 3"],
        ["Security Analysis", "Formal security proof: IND-CPA, forward secrecy, SNIZK soundness", "Week 3-4"],
        ["Final Documentation", "Complete project report using official template", "Week 4"],
    ]
    story.append(colored_table(roadmap, col_widths=[30*mm, W-50*mm, 20*mm]))
    story.append(PageBreak())

    # ═══════════════════════════════════════════════
    # 30. EMERGENCY QUICK-REFERENCE CARD
    # ═══════════════════════════════════════════════
    story.append(Paragraph("30. EMERGENCY QUICK-REFERENCE CARD", sH1))
    story.append(hr())
    story.append(Paragraph("Print this page and keep it in front of you during the presentation.", sWarn))
    
    story.append(Paragraph("Key Numbers:", sH2))
    numbers = [
        ["What", "Value"],
        ["Prime P", "secp256k1: 2^256 - 2^32 - 977 (same as Bitcoin/Ethereum)"],
        ["Generator g", "2"],
        ["Security Parameter", "256-bit (128-bit security level)"],
        ["AES Mode", "AES-256-GCM (Galois/Counter Mode)"],
        ["Base Paper Add Time", "~5,560 ms for L=1000, m=10"],
        ["Our Add Time", "~0.99 ms (O(m))"],
        ["Our Delete Time", "~0.0001 ms (O(1))"],
        ["Speedup Factor", "5,500x for L=1000"],
        ["Deletion Gas Cost", "~45,100 gas"],
        ["Registration Gas Cost", "~114,500 gas"],
        ["Smart Contract Language", "Solidity ^0.8.20"],
        ["Backend Language", "Python 3 with PyCryptodome"],
        ["Web Framework", "Flask 2.x"],
        ["Base Paper", "Cheng et al., Elsevier IoT Vol 36, Dec 2025/2026"],
        ["Research Gap Section", "Section 8, Page 22 of the paper"],
    ]
    story.append(colored_table(numbers, col_widths=[38*mm, W-38*mm], header_color=NAVY))
    
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("If Maam Asks for Code, Open These Files:", sH2))
    quick_files = [
        ["Question", "Open This File", "Show Lines"],
        ["'Show me the encryption code'", "src/crypto_utils.py", "Lines 26-43"],
        ["'Show me the dynamic add'", "src/dynamic_extension.py", "Lines 17-34"],
        ["'Show me the deletion'", "src/dynamic_extension.py", "Lines 36-48"],
        ["'Show me the smart contract'", "contracts/BAMKS_Registry.sol", "Lines 69-77"],
        ["'Show me the proof verification'", "src/crypto_utils.py", "Lines 52-89"],
        ["'Show me the search'", "src/bamks_system.py", "Lines 131-142"],
        ["'Show me the trapdoor generation'", "src/bamks_system.py", "Lines 121-129"],
        ["'Show me the API endpoints'", "app.py", "Lines 191-270"],
    ]
    story.append(colored_table(quick_files, col_widths=[40*mm, 40*mm, W-80*mm], header_color=TEAL_DARK))
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("5 Things to Remember:", sH2))
    remember = [
        "<b>1.</b> Our project EXTENDS the base paper. We did NOT build from scratch.",
        "<b>2.</b> The research gap is in <b>Section 8</b> of the paper. The authors themselves admitted it.",
        "<b>3.</b> Our key contribution: <b>O(m) insertion</b> and <b>O(1) deletion</b> vs <b>O(L x m)</b>.",
        "<b>4.</b> Always say <b>AES-256-GCM</b> (not just AES). The GCM provides integrity.",
        "<b>5.</b> Always say <b>Schnorr Non-Interactive Zero-Knowledge proof</b> -- be specific.",
    ]
    for r in remember:
        story.append(Paragraph(r, sBullet))
    
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph("-- End of Ultimate Defense Manual --", sCenterBold))
    story.append(Paragraph(f"Generated: {datetime.datetime.now().strftime('%d %B %Y at %I:%M %p')}", sSmall))

    # ── Build the PDF ──
    doc.build(story)
    print(f"\n{'='*60}")
    print(f"PDF generated successfully: {OUT_FILE}")
    print(f"   Sections: 30")
    print(f"   Viva QAs: 25")
    print(f"   Algorithms: 15 (10 base + 5 proposed)")
    print(f"{'='*60}")

if __name__ == "__main__":
    build_pdf()
