# 🎓 Review 2 Presentation & Viva Guide (September 16 – 22, 2026)

**Project Title:** Enabling Dynamic File-Level Operations in Blockchain-Assisted Attribute-Based Multi-Keyword Search (BAMKS-D)  
**Base Paper:** Cheng et al., *Internet of Things* (Elsevier), Volume 36, Art 101838, Dec 2025 / 2026.  
**Review 2 Deliverables (As per Course Rubric):**  
1. *Implementation of the proposed methodology*  
2. *Algorithm / Code*  
3. *Intermediate Results (A little execution)*  
4. *Individual contributions assessment*  

---

## 👥 Individual Contributions (Mention this clearly!)

- **Prashant Singh (24BYB1042):**  
  > *"Ma’am, I developed the **Python Cryptographic Engine and dynamic algorithms** — establishing the 256-bit cyclic group $\mathbb{Z}_p^*$, the conjunctive trapdoor token generation equations $(T_1, T_2, T_3)$, and the single-file dynamic operations (`SingleDocAdd` in $O(m)$, `SingleDocDelete` in $O(1)$, and `SingleDocModify`)."*

- **Adak Rushikesh (24BYB1055):**  
  > *"Ma’am, I developed the **Blockchain layer and Solidity smart contract (`BAMKS_Registry.sol`)** — implementing the on-chain `deletedDocRegistry` state mapping, the EVM gas metering, and the Result Verification Smart Contract (`RVSC`) to mathematically verify the cloud's Schnorr Zero-Knowledge proof."*

---

## ⏱️ Step-by-Step 3-Minute Presentation Flow for Tomorrow

### 1. The Opening (30 Seconds) — Tab 1: Aim & Methodology
1. Open your browser at **`http://127.0.0.1:5000`**.
2. Tab 1 is already open. Say:
> *"Good morning Ma’am. This is our Review 2 progress presentation for BAMKS-D.*  
> *As submitted in our Review 1 report, our aim is to implement **dynamic file-level operations** on top of Cheng et al.'s base architecture.*  
> *In the base paper, files are bound into a single dataset version ($F_{ver}$), meaning adding or deleting 1 file forces re-keying all $L$ files ($O(L \times m)$). In Section 8, the authors left single-file operations for future work.*  
> *Our proposed methodology introduces a Dynamic Update Handler and an on-chain Ethereum registry to achieve $O(m)$ insertion and $O(1)$ deletion."*

---

### 2. The Codes & Algorithms (60 Seconds) — Tab 2: Algorithms & Code
Click on **"2. Algorithms & Code"** on the sidebar:
> *"Ma’am, here are the core algorithms we have implemented:*
> 1. ***Algorithm 1 (`SingleDocAdd`)***: *Encrypts the payload with AES-256-GCM and generates keyword tokens only for the $m$ keywords of that new file in $O(m)$ time without touching existing files.*
> 2. ***Algorithm 2 (`SingleDocDelete`)***: *Updates the `deletedDocRegistry[docId] = true` state mapping in our Solidity smart contract in $O(1)$ constant time.*
> 3. ***Algorithm 3 (`SingleDocModify`)***: *As defined in Section 6 of our Review 1 report, modification is executed as a clean Delete followed by an Insert.*
> 4. ***Algorithm 4 (`verifyResultProof`)***: *Our RVSC contract mathematically audits the cloud's Schnorr Zero-Knowledge proof and ensures revoked files are automatically filtered out."*

*(If she wants to see the actual Python or Solidity files, open [`src/dynamic_extension.py`](file:///c:/Users/Prabhat%20Singh/.gemini/antigravity/scratch/BAMKS_Project/src/dynamic_extension.py) and [`contracts/BAMKS_Registry.sol`](file:///c:/Users/Prabhat%20Singh/.gemini/antigravity/scratch/BAMKS_Project/contracts/BAMKS_Registry.sol) in VS Code).*

---

### 3. Intermediate Results Execution (60 Seconds) — Tab 3: Intermediate Results
Click on **"3. Intermediate Results"** on the sidebar:
1. **Show the records table at the bottom:**  
   > *"Here are 5 initial hospital patient records encrypted and stored."*
2. **Click `➕ Insert Doc #106`:**  
   > *"We insert Doc #106. Notice it finishes in under 1 millisecond ($O(m)$) and logs an Ethereum registration transaction."*
3. **Click `❌ Delete Doc #101`:**  
   > *"We delete Doc #101. It updates the on-chain mapping in 0.0001 ms ($O(1)$) with only ~42,100 gas."*
4. **Click `🔍 Execute Conjunctive Search`:**  
   > *"Now we search for `['Cardiology', 'ECG']`. Notice the intermediate result: the smart contract accepts the Schnorr proof as `VALID`, includes newly added #106, and automatically omits the deleted #101 on-chain!"*

---

### 4. Hand-off to Review 3 (15 Seconds) — Tab 5: Review 3 Roadmap
Click on **"5. Review 3 Roadmap"**:
> *"Ma'am, for Review 3 next month, as per the syllabus, we will present:*
> 1. *The exhaustive comparative performance analysis against existing schemes across 50 to 5,000 files.*
> 2. *Migration from local EVM to the public Ethereum Sepolia testnet.*
> 3. *Hardware energy and battery profiling on an IoT edge node.*
> 4. *Final document submission using the official template."*

---

## ❓ Top 4 Questions Ma'am Might Ask & Direct Answers

**Q1: "Where does the O(1) complexity in deletion come from?"**
> *"Ma'am, instead of re-encrypting the entire dataset in the cloud, we update a single boolean flag `deletedDocRegistry[docId] = true` in the Ethereum smart contract. Since a key-value hash lookup in EVM storage is constant time, deletion executes in $O(1)$ time."*

**Q2: "What if the cloud cheats and returns a deleted document?"**
> *"The RVSC smart contract iterates through matched IDs in `verifyResultProof` and verifies `require(!deletedDocRegistry[id])`. If the cloud returns a revoked document, the transaction reverts and the cloud is caught cheating."*

**Q3: "Why did you use AES-256-GCM alongside CP-ABE?"**
> *"CP-ABE is asymmetric and computationally heavy. Following standard cryptographic practice, we use CP-ABE to protect the shared symmetric decryption key ($\Phi$), and use lightweight AES-256-GCM for the actual medical record payloads."*

**Q4: "What is left for Review 3?"**
> *"Review 3 is dedicated to exhaustive performance comparison curves against baseline schemes, public Sepolia testnet gas auditing, and the final project documentation."*
