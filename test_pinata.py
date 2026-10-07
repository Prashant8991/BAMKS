"""
TEST PINATA IPFS CONNECTION
---------------------------
Tests authentication with Pinata IPFS using either JWT or API Key + Secret.
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

jwt = os.getenv("PINATA_JWT", "").strip()
api_key = os.getenv("PINATA_API_KEY", "").strip()
api_secret = os.getenv("PINATA_API_SECRET", "").strip()

print("=" * 70)
print("   PINATA IPFS CREDENTIAL VERIFICATION")
print("=" * 70)

# Check JWT
if jwt and jwt.startswith("eyJ"):
    print(f"[*] Testing Pinata JWT (Length: {len(jwt)} chars)...")
    req = urllib.request.Request("https://api.pinata.cloud/data/testAuthentication")
    req.add_header("Authorization", f"Bearer {jwt}")
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"[SUCCESS] Pinata IPFS Connected Successfully! 🎉")
            print(f"  Message : {data.get('message')}")
            sys.exit(0)
    except urllib.error.HTTPError as e:
        print(f"[ERROR] JWT Authentication Failed (HTTP {e.code}): {e.read().decode()}")

# Check API Key + Secret
elif api_key:
    print(f"[*] Found Pinata API Key: {api_key[:6]}...{api_key[-4:]} (Length: {len(api_key)})")
    if not api_secret or "PASTE" in api_secret:
        print("\n[!] MISSING PINATA SECRET KEY:")
        print("    You pasted the 'API Key', but Pinata also requires the 'API Secret'!")
        print("    When Pinata generates a key, it shows two things on the screen:")
        print("    1. API Key:    (20 chars) -> Already saved")
        print("    2. API Secret: (64 chars) -> Needs to be pasted in .env as PINATA_API_SECRET")
        print("\n    OR copy the single long 'JWT' (starts with 'eyJ...') into PINATA_JWT.")
        sys.exit(1)
        
    print(f"[*] Testing Pinata API Key + Secret...")
    req = urllib.request.Request("https://api.pinata.cloud/data/testAuthentication")
    req.add_header("pinata_api_key", api_key)
    req.add_header("pinata_secret_api_key", api_secret)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"[SUCCESS] Pinata IPFS Connected Successfully! 🎉")
            print(f"  Message : {data.get('message')}")
            sys.exit(0)
    except urllib.error.HTTPError as e:
        print(f"[ERROR] API Key Authentication Failed (HTTP {e.code}): {e.read().decode()}")

else:
    print("[!] No Pinata credentials found in .env.")
    print("    Please set either PINATA_JWT or (PINATA_API_KEY and PINATA_API_SECRET).")
