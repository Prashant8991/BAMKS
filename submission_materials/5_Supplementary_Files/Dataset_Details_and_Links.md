# Supplementary Material 1: Dataset Details and Documentation

## 1. Overview of Clinical EHR Corpus
The research evaluation of **BAMKS-D** utilizes a structured corpus of realistic, multi-departmental Electronic Health Records (EHRs) designed to model real-world hospital workflows, emergency admissions, and continuous medical IoT telemetry.

The dataset is located in the repository under:
`c:\Users\Prabhat Singh\.gemini\antigravity\scratch\BAMKS_Project\sample_inputs\`

---

## 2. Document Inventory & Metadata Specifications

| Doc ID | Clinical File Name | Department / Specialty | File Format | Extracted Keywords ($m$) | Bound CP-ABE Access Policy | Clinical Case Summary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **#201** | `Patient_201_Cardiology_ECG_Report.txt` | Cardiology | Plaintext | `Cardiology`, `ECG`, `STEMI`, `Emergency` | `(Role_Doctor AND Dept_Cardiology)` | Acute ST-Elevation Myocardial Infarction, 12-lead ECG telemetry showing ST-elevation in leads V1–V4. |
| **#202** | `Patient_202_Cardiac_Telemetry.json` | Cardiology | JSON | `Cardiology`, `ECG`, `Telemetry`, `Tachycardia` | `(Role_Doctor AND Dept_Cardiology)` | 24-hour continuous Holter telemetry monitoring, non-sustained ventricular tachycardia runs. |
| **#203** | `Patient_203_Neurology_BrainMRI.txt` | Neurology | Plaintext | `Neurology`, `MRI`, `Brain`, `Epilepsy` | `(Role_Doctor AND Dept_Neurology)` | 3T cranial MRI scan, mesial temporal sclerosis, drug-resistant focal epilepsy protocol. |
| **#204** | `Patient_204_Stroke_Perfusion_Lab.csv` | Neurology | CSV | `Neurology`, `Stroke`, `Perfusion`, `Emergency` | `(Role_Doctor AND Dept_Neurology)` | CT cerebral perfusion scan, core ischemic penumbra volumetric metrics, emergency IV-tPA candidate. |
| **#205** | `Patient_205_Oncology_Biopsy_Report.txt` | Oncology | Plaintext | `Oncology`, `Biopsy`, `HER2`, `Pathology` | `(Role_Doctor AND Dept_Oncology)` | Histopathology core needle biopsy, invasive ductal carcinoma, estrogen/progesterone/HER2 status. |
| **#207** | `Patient_207_Pediatric_Vaccination.txt` | Pediatrics | Plaintext | `Pediatrics`, `Vaccine`, `Child`, `Routine` | `(Role_Nurse OR Role_Doctor)` | Pediatric developmental milestone vitals and routine MMR / DTaP / Polio immunization schedule. |
| **#208** | `Patient_208_GeneralWard_Vitals_Log.csv` | General Ward | CSV | `Nursing`, `Inpatient`, `Vitals`, `Ward` | `(Role_Nurse OR Role_Doctor)` | Continuous post-operative vital signs log: SpO2, heart rate, blood pressure, analgesic administration. |
| **#209** | `Patient_209_Discharge_Summary.md` | General Hospital | Markdown | `Discharge`, `Hospital`, `Summary`, `Clinical` | `(Role_Nurse OR Role_Doctor)` | Comprehensive inpatient discharge summary, medication reconciliation, outpatient cardiology follow-up. |

---

## 3. Data Schema & Cryptographic Representation
Every document in the corpus is processed through client-side symmetric encryption:
1. **Plaintext Payload:** Converted to canonical UTF-8 bytes.
2. **Payload Ciphertext:** Encrypted using **AES-256-GCM** with a random 96-bit nonce and 128-bit authentication tag.
3. **Public Verification Tag ($y_k$):** Formulated as $y_k = g^{\sigma_k} \pmod P$, where $\sigma_k \in_R \mathbb{Z}_{P-1}^*$.
4. **Decentralized CID:** Serialized payload is uploaded to Pinata IPFS, producing a content identifier (e.g., `ipfs://bafkreiegat25m4vgoltbz5l5wtvka7ipm4osl7xtyryhbg643ihctznluq`).

---

## 4. Public Reference Standards & Benchmarking Sources
The synthetic clinical documents are modeled in strict conformance with standard clinical terminologies and open scientific datasets:
- **PhysioNet / MIT-BIH Arrhythmia Database:** Reference for ECG telemetry lead waveforms and cardiac arrhythmias. Link: https://physionet.org/content/mitdb/
- **MIMIC-IV (Medical Information Mart for Intensive Care):** Reference for ICU de-identified patient vitals and discharge summaries. Link: https://physionet.org/content/mimiciv/
- **HL7 FHIR (Fast Healthcare Interoperability Resources):** Standard JSON diagnostic report resource structure. Link: https://hl7.org/fhir/

---

## 5. Base Research Paper & Experimental Baseline Model
- **Base Paper:** Hanlei Cheng, Sio-Long Lo, Jing Lu, *"Blockchain-assisted attribute-based multi-keyword search for dynamic encrypted data in cloud-edge-IoT"*, Elsevier *Internet of Things*, Vol. 36, Art. 101838, Dec 2025/2026. DOI: [10.1016/j.iot.2025.101838](https://doi.org/10.1016/j.iot.2025.101838)
- **Local Reference PDF:** [`Cheng_et_al_2026_Base_Research_Paper_BAMKS.pdf`](file:///c:/Users/Prabhat%20Singh/.gemini/antigravity/scratch/BAMKS_Project/submission_materials/Base_Research_Paper_Cheng_et_al/Cheng_et_al_2026_Base_Research_Paper_BAMKS.pdf)
- **Baseline Scale:** Cheng et al. established the benchmark scale across collection sizes $L \in \{50, 200, 500, 1000, 5000\}$ files with $m=5$ keywords per document. Our reproduction and speedup evaluation (`test_demo.py`) directly mirrors this baseline configuration.

