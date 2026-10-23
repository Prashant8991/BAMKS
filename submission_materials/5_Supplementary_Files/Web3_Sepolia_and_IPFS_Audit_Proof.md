# Supplementary Material 4: Web3 Ethereum Sepolia & IPFS Audit Proof

## 1. Live Ethereum Sepolia Smart Contract
The Result Verification Smart Contract (RVSC) and dynamic document deletion registry are live and verified on the public Ethereum Sepolia Testnet.

- **Contract Name:** `BAMKS_Registry`
- **Compiler Version:** Solidity 0.8.20 (`solc 0.8.20+commit.a1b79de6`)
- **EVM Target:** Cancun / Shanghai with `0x05` Modular Exponentiation Precompile support
- **Contract Address:** 
  [`0x3829bda65146D8fb0C2c6E2596F6A39936bF9DB5`](https://sepolia.etherscan.io/address/0x3829bda65146D8fb0C2c6E2596F6A39936bF9DB5)
- **Deployment Transaction Hash:** 
  [`0x2277c1481ed1e96268cadd12bd35529bc41d2285ff362a75d3dd2fb62dc6f85c`](https://sepolia.etherscan.io/tx/0x2277c1481ed1e96268cadd12bd35529bc41d2285ff362a75d3dd2fb62dc6f85c)
- **Deployment Block:** #11946107
- **Deployer Wallet Address:** `0x7962dc40751101B4AF8299f70ABeb9feF52D50e9`
- **Gas Used for Deployment:** 3,000,000 gas units

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
