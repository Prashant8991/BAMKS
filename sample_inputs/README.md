# BAMKS-D Sample Input Files for Testing

This directory contains realistic clinical records in multiple file formats (`.txt`, `.json`, `.csv`, `.md`) designed for evaluating **BAMKS-D** searchable encryption and attribute-based access control (CP-ABE).

---

## Sample File Catalog

| File Name | Format | Clinical Specialty | Target CP-ABE Policy | Recommended Search Keywords | Who Can Decrypt? |
|---|:---:|---|---|---|:---:|
| `Patient_201_Cardiology_ECG_Report.txt` | `.txt` | Cardiology (CathLab / STEMI) | `(Role_Doctor AND Dept_Cardiology)` | `Cardiology, ECG, Stent, Emergency` | Dr. Prashant Singh |
| `Patient_202_Cardiac_Telemetry.json` | `.json` | Cardiology (Arrhythmia / Holter) | `(Role_Doctor AND Dept_Cardiology)` | `Cardiology, ECG, Telemetry, Echo` | Dr. Prashant Singh |
| `Patient_203_Neurology_BrainMRI.txt` | `.txt` | Neurology (Epilepsy / 3T MRI) | `(Role_Doctor AND Dept_Neurology)` | `Neurology, Brain, MRI, Epilepsy` | Dr. Rushikesh Adak |
| `Patient_204_Stroke_Perfusion_Lab.csv` | `.csv` | Neurology (Acute Stroke CT Lab) | `(Role_Doctor AND Dept_Neurology)` | `Neurology, Stroke, Brain, Emergency` | Dr. Rushikesh Adak |
| `Patient_205_Oncology_Biopsy_Report.txt` | `.txt` | Oncology (Histopathology Biopsy) | `(Role_Doctor AND Dept_Oncology)` | `Oncology, Biopsy, Pathology, Tumor` | Oncologist / Specialist |
| `Patient_207_Pediatric_Vaccination.txt` | `.txt` | Pediatrics (Inpatient MMR Clinic) | `(Role_Nurse OR Role_Doctor)` | `Pediatrics, Vaccine, Routine, Child` | Nurse Anita Patel & Doctors |
| `Patient_208_GeneralWard_Vitals_Log.csv` | `.csv` | General Ward (Nursing Vitals) | `(Role_Nurse OR Role_Doctor)` | `Routine, Nurse, Inpatient, Ward` | Nurse Anita Patel & Doctors |
| `Patient_209_Discharge_Summary.md` | `.md` | Cardiology (Discharge Summary) | `(Role_Doctor AND Dept_Cardiology)` | `Cardiology, ECG, Stent, Rehab` | Dr. Prashant Singh |

---

## How to Test in the Application (http://127.0.0.1:5000)

### Method 1: Single File Upload
1. Log in as **Dr. Prashant Singh** (or any identity).
2. Go to **Screen 1: Hospital Upload**.
3. Under **Single File / Record**, drag and drop any file from this folder into the dropzone (or click to browse).
4. Notice that:
   - File contents are loaded into the diagnosis box.
   - Relevant keywords are auto-suggested.
   - The appropriate CP-ABE access policy is automatically selected.
5. Click **"Encrypt Record & Store to Cloud"**.

### Method 2: Multi-File Batch Ingestion
1. On **Screen 1**, click **"Batch Files Upload (Multi-Doc)"**.
2. Drag and drop multiple files (e.g. all files from this folder) into the multi-file dropzone at once.
3. Observe the queue showing file sizes, auto-detected departments, and extracted keywords.
4. Click **"Encrypt & Ingest All Files (O(m) Batch)"**.
5. Observe the batch completion metrics:
   - Total files ingested.
   - Total ingestion time.
   - Average per-file time demonstrating $O(m)$ flat scaling.
   - Total EVM gas consumed.

### Method 3: 1-Click Batch Demo Button
On the **Batch Files Upload** tab, simply click:
> **"⚡ Load 8 Pre-Packaged Hospital Records (1-Click Batch Demo)"**
to instantly populate the cloud database with 8 diverse clinical files.

---

## Verifying Cross-Identity Access Control (Viva Demo)
- Search for `['Cardiology', 'ECG']`:
  - **Dr. Prashant Singh:** Allowed to decrypt all matching patient records.
  - Switch to **Dr. Rushikesh Adak** or **Nurse Anita Patel**: Records appear in search results, but the plaintext displays:
    `[CP-ABE ACCESS DENIED: Requires Policy: (Role_Doctor AND Dept_Cardiology)]`.
- Search for `['Neurology', 'Brain']`:
  - **Dr. Rushikesh Adak:** Allowed to decrypt.
  - **Dr. Prashant Singh:** Blocked by neurology policy.
- Search for `['Pediatrics', 'Vaccine']`:
  - Both **Nurse Anita Patel** and **Dr. Prashant Singh** can decrypt because policy is `(Role_Nurse OR Role_Doctor)`.
- Switch to **External Guest**: All records are locked (zero clinical attributes).
