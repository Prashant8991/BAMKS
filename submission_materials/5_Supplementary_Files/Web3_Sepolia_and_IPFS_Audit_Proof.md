# Supplementary Material 4: Web3 Ethereum Sepolia & IPFS Audit Proof

## 1. Live Ethereum Sepolia Smart Contract & Verified On-Chain Transactions

The Result Verification Smart Contract (RVSC) and dynamic document deletion registry are deployed, live, and verified on the public Ethereum Sepolia Testnet.

- **Contract Name:** `BAMKS_Registry`
- **Compiler Version:** Solidity 0.8.20 (`solc 0.8.20+commit.a1b79de6`)
- **EVM Target:** Cancun / Shanghai with `0x05` Modular Exponentiation Precompile support
- **Deployer Wallet Address:** [`0x7962dc40751101B4AF8299f70ABeb9feF52D50e9`](https://sepolia.etherscan.io/address/0x7962dc40751101B4AF8299f70ABeb9feF52D50e9)
- **Contract Address:** 
  [`0xfDC8615Bf6483c3B0f39c330F55A56Cb0f08C8D3`](https://sepolia.etherscan.io/address/0xfDC8615Bf6483c3B0f39c330F55A56Cb0f08C8D3)
- **Deployment Transaction Hash:** 
  [`0x1f058bde75b20c2d1ce513897d77d70f47a2951cbcc83d9bc45a573116bf0dbf`](https://sepolia.etherscan.io/tx/0x1f058bde75b20c2d1ce513897d77d70f47a2951cbcc83d9bc45a573116bf0dbf)
- **Deployment Block:** #11975268
- **Deployment Gas Used:** 6,889,229 gas units

---

### On-Chain Transaction Receipts

#### A. Document Registration (`registerDocument`)
- **Invoked Function:** `registerDocument(uint256 _docId, bytes32 _fileHash, bytes32 _publicTag)`
- **Target Document ID:** `101`
- **Transaction Hash:** 
  [`0x363d3e8867adb49a2657b798ebb26990a5d0011ec5ddaf7de267ff191dc40ad7`](https://sepolia.etherscan.io/tx/0x363d3e8867adb49a2657b798ebb26990a5d0011ec5ddaf7de267ff191dc40ad7)
- **Confirmed Block:** #11975277
- **Receipt Status:** 1 (Success)
- **Gas Used:** 792,245 gas units
- **Block Confirmation Time:** 35.22 seconds
- **State Verification:** `isDocActive(101)` returns `true`

#### B. Dynamic Document Deletion (`deleteDocument`)
- **Invoked Function:** `deleteDocument(uint256 _docId)`
- **Target Document ID:** `101`
- **Transaction Hash:** 
  [`0x008330a08b3ad8926b19de8dc0a1b386b95712dc55077e33df2a36685c876e8d`](https://sepolia.etherscan.io/tx/0x008330a08b3ad8926b19de8dc0a1b386b95712dc55077e33df2a36685c876e8d)
- **Confirmed Block:** #11975278
- **Receipt Status:** 1 (Success)
- **Gas Used:** 242,834 gas units
- **Block Confirmation Time:** 21.83 seconds
- **State Verification:** `isDocActive(101)` returns `false` (immediate on-chain revocation)

---

## 2. Decentralized Pinata IPFS Storage Audit
Encrypted patient EHR ciphertexts are pinned directly to the decentralized Web3 IPFS network via Pinata Cloud:

- **IPFS Storage Adapter:** [src/ipfs_storage.py](file:///c:/Users/Prabhat%20Singh/.gemini/antigravity/scratch/BAMKS_Project/src/ipfs_storage.py)
- **IPFS Protocol Version:** CID v1 (base32 multihash)
- **Sample Document #101 CID:** `bafkreiegat25m4vgoltbz5l5wtvka7ipm4osl7xtyryhbg643ihctznluq`
- **Public IPFS Gateway Link:**
  [https://gateway.pinata.cloud/ipfs/bafkreiegat25m4vgoltbz5l5wtvka7ipm4osl7xtyryhbg643ihctznluq](https://gateway.pinata.cloud/ipfs/bafkreiegat25m4vgoltbz5l5wtvka7ipm4osl7xtyryhbg643ihctznluq)
- **IPFS URI:** `ipfs://bafkreiegat25m4vgoltbz5l5wtvka7ipm4osl7xtyryhbg643ihctznluq`

---

## 3. Remote GitHub Repository
- **Repository URL:** [https://github.com/Prashant8991/BAMKS.git](https://github.com/Prashant8991/BAMKS.git)
- **Primary Branch:** `main`
- **License:** MIT Open Source License
