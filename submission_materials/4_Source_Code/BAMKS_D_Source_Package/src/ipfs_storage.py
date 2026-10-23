"""
IPFS STORAGE ADAPTER (PINATA CLOUD)
-----------------------------------
Handles uploading and pinning AES-256 encrypted patient files to IPFS via Pinata.
Returns decentralized Content Identifiers (CIDs) and public gateway URLs.
"""

import os
import sys
import json
import urllib.request
import urllib.error
from dotenv import load_dotenv

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


load_dotenv()

PINATA_JWT = os.getenv("PINATA_JWT", "").strip()
PINATA_API_KEY = os.getenv("PINATA_API_KEY", "").strip()
PINATA_API_SECRET = os.getenv("PINATA_API_SECRET", "").strip()

def upload_encrypted_file_to_ipfs(doc_id: int, enc_payload: dict, file_metadata: dict = None) -> dict:
    """
    Pins an encrypted document payload (AES-256 ciphertext + metadata) to IPFS.
    Returns: dict with 'cid', 'ipfs_uri', 'gateway_url', 'pin_size', 'timestamp'
    """
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    
    # Prepare payload body
    payload = {
        "pinataOptions": {
            "cidVersion": 1
        },
        "pinataMetadata": {
            "name": f"BAMKS_Doc_{doc_id:03d}_Encrypted.json",
            "keyvalues": {
                "doc_id": str(doc_id),
                "system": "BAMKS-D",
                "encryption": "AES-256-GCM",
                "version": str(enc_payload.get("version_id", 1))
            }
        },
        "pinataContent": {
            "doc_id": doc_id,
            "ciphertext": enc_payload.get("enc_payload", enc_payload),
            "public_tag_yk": str(enc_payload.get("y_k", "")),
            "version_id": enc_payload.get("version_id", 1),
            "metadata": file_metadata or {}
        }
    }
    
    data_bytes = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data_bytes, method='POST')
    req.add_header('Content-Type', 'application/json')
    
    # Use JWT if available, else API key + secret
    if PINATA_JWT:
        req.add_header('Authorization', f'Bearer {PINATA_JWT}')
    elif PINATA_API_KEY and PINATA_API_SECRET:
        req.add_header('pinata_api_key', PINATA_API_KEY)
        req.add_header('pinata_secret_api_key', PINATA_API_SECRET)
    else:
        raise ValueError("Missing Pinata credentials in .env")

    try:
        with urllib.request.urlopen(req) as resp:
            res_data = json.loads(resp.read().decode('utf-8'))
            cid = res_data.get('IpfsHash')
            return {
                "status": "success",
                "doc_id": doc_id,
                "cid": cid,
                "ipfs_uri": f"ipfs://{cid}",
                "gateway_url": f"https://gateway.pinata.cloud/ipfs/{cid}",
                "pin_size": res_data.get('PinSize'),
                "timestamp": res_data.get('Timestamp')
            }
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode('utf-8')
        raise RuntimeError(f"Pinata IPFS Pinning failed (HTTP {e.code}): {error_msg}")

if __name__ == '__main__':
    print("Testing real IPFS upload with sample patient record #101...")
    sample_doc = {
        "version_id": 202610,
        "y_k": 987654321,
        "enc_payload": {
            "nonce": "a1b2c3d4e5f6",
            "ciphertext": "e5c26b9a84f3...[AES-256-GCM Encrypted Patient EHR]...",
            "tag": "d8e9f0a1b2c3"
        }
    }
    res = upload_encrypted_file_to_ipfs(101, sample_doc, {"department": "Cardiology", "patient": "Patient_101"})
    print("\n" + "=" * 70)
    print("  SUCCESSFULLY PINNED ENCRYPTED RECORD TO REAL IPFS! 🚀")
    print(f"  Document ID : #{res['doc_id']}")
    print(f"  IPFS CID    : {res['cid']}")
    print(f"  IPFS URI    : {res['ipfs_uri']}")
    print(f"  Public Link : {res['gateway_url']}")
    print("=" * 70)
