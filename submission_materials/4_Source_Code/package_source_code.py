"""
PACKAGE SOURCE CODE FOR SUBMISSION
==================================
Copies complete functional codebase, dependencies, and configuration
into submission_materials/4_Source_Code/ and creates a portable zip archive.
"""

import os
import shutil
import zipfile

def package_code():
    project_root = r"c:\Users\Prabhat Singh\.gemini\antigravity\scratch\BAMKS_Project"
    dest_dir = os.path.join(project_root, "submission_materials", "4_Source_Code")
    extracted_folder = os.path.join(dest_dir, "BAMKS_D_Source_Package")
    os.makedirs(extracted_folder, exist_ok=True)

    # Core items to bundle
    dirs_to_copy = ["src", "contracts", "sample_inputs", "diagrams"]
    files_to_copy = [
        "app.py",
        "index.html",
        "test_demo.py",
        "test_correctness_and_security.py",
        "proof_of_o1_complexity.py",
        "deploy_sepolia.py",
        "test_pinata.py",
        "requirements.txt",
        ".env.example",
        "README.md"
    ]

    for d in dirs_to_copy:
        src_path = os.path.join(project_root, d)
        dst_path = os.path.join(extracted_folder, d)
        if os.path.exists(dst_path):
            shutil.rmtree(dst_path)
        shutil.copytree(src_path, dst_path, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.git*'))
        print(f"Copied directory: {d}")

    for f in files_to_copy:
        src_path = os.path.join(project_root, f)
        dst_path = os.path.join(extracted_folder, f)
        if os.path.exists(src_path):
            shutil.copy2(src_path, dst_path)
            print(f"Copied file: {f}")

    # Create zip archive
    zip_path = os.path.join(dest_dir, "BAMKS_D_Complete_Source_Code.zip")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(extracted_folder):
            for file in files:
                file_full = os.path.join(root, file)
                rel_path = os.path.relpath(file_full, extracted_folder)
                zipf.write(file_full, arcname=rel_path)

    print(f"\n[SUCCESS] Source code packaged successfully:")
    print(f"  Folder : {extracted_folder}")
    print(f"  Zip    : {zip_path} ({os.path.getsize(zip_path):,} bytes)")

if __name__ == '__main__':
    package_code()
