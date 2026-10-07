"""
DEPLOYMENT & INTERACTION SCRIPT FOR ETHEREUM SEPOLIA TESTNET (BAMKS-D)
----------------------------------------------------------------------
This script connects to the real Ethereum Sepolia Testnet, checks wallet
balance, deploys BAMKS_Registry.sol, and verifies contract state.
"""

import os
import sys
import json
from dotenv import load_dotenv
from web3 import Web3
from web3.middleware import ExtraDataToPOAMiddleware

# Force UTF-8 on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Load .env file
load_dotenv()

RPC_URL = os.getenv("SEPOLIA_RPC_URL", "https://ethereum-sepolia-rpc.publicnode.com")
PRIVATE_KEY = os.getenv("SEPOLIA_PRIVATE_KEY", "").strip()
CONTRACT_ADDRESS = os.getenv("SEPOLIA_CONTRACT_ADDRESS", "").strip()

def check_connection():
    print("=" * 80)
    print("   ETHEREUM SEPOLIA TESTNET CONNECTION STATUS")
    print("=" * 80)
    
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)
    
    if not w3.is_connected():
        print(f"[ERROR] Could not connect to Sepolia RPC: {RPC_URL}")
        return None, None
        
    chain_id = w3.eth.chain_id
    latest_block = w3.eth.block_number
    print(f"  RPC Endpoint : {RPC_URL}")
    print(f"  Network      : Ethereum Sepolia (Chain ID: {chain_id})")
    print(f"  Latest Block : #{latest_block}")
    
    if not PRIVATE_KEY or PRIVATE_KEY == "your_private_key_here_without_0x_prefix":
        print("\n[!] WALLET STATUS: No private key found in .env")
        print("    Please create a .env file with your SEPOLIA_PRIVATE_KEY to deploy or sign transactions.")
        return w3, None

    # Load account
    try:
        pk = PRIVATE_KEY if PRIVATE_KEY.startswith("0x") else f"0x{PRIVATE_KEY}"
        account = w3.eth.account.from_key(pk)
        balance_wei = w3.eth.get_balance(account.address)
        balance_eth = w3.from_wei(balance_wei, 'ether')
        
        print(f"  Account      : {account.address}")
        print(f"  Balance      : {balance_eth:.5f} SepoliaETH")
        
        if balance_wei == 0:
            print("\n[!] WARNING: Account balance is 0.00 SepoliaETH!")
            print("    You need testnet ETH for gas to deploy contracts.")
            print("    Get free SepoliaETH from: https://cloud.google.com/application/web3/faucet/ethereum/sepolia")
        return w3, account
    except Exception as e:
        print(f"[ERROR] Invalid private key: {e}")
        return w3, None

def deploy_contract(w3, account):
    if not account:
        print("[ABORT] Cannot deploy without a funded account.")
        return

    # Load compiled ABI and Bytecode
    abi_path = os.path.join(os.path.dirname(__file__), "contracts", "build", "contracts_BAMKS_Registry_sol_BAMKS_Registry.abi")
    bin_path = os.path.join(os.path.dirname(__file__), "contracts", "build", "contracts_BAMKS_Registry_sol_BAMKS_Registry.bin")

    if not os.path.exists(abi_path) or not os.path.exists(bin_path):
        print("[ERROR] Compiled contract files not found in contracts/build!")
        return

    with open(abi_path, 'r', encoding='utf-8') as f:
        contract_abi = json.load(f)
    with open(bin_path, 'r', encoding='utf-8') as f:
        contract_bin = f.read().strip()

    print("\n[DEPLOYMENT] Preparing to deploy BAMKS_Registry.sol to Sepolia...")
    contract_factory = w3.eth.contract(abi=contract_abi, bytecode=contract_bin)

    nonce = w3.eth.get_transaction_count(account.address)
    base_gas_price = w3.eth.gas_price
    
    tx = contract_factory.constructor().build_transaction({
        'from': account.address,
        'nonce': nonce,
        'gas': 3000000,
        'gasPrice': int(base_gas_price * 1.2),
        'chainId': 11155111
    })

    print("  * Signing deployment transaction...")
    signed_tx = account.sign_transaction(tx)
    print("  * Broadcasting to Sepolia network...")
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"  * Transaction Hash: {tx_hash.hex()}")
    print("  * Waiting for block confirmation (takes ~12-15 seconds)...")

    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=180)
    contract_address = tx_receipt.contractAddress
    print("\n" + "=" * 80)
    print("  SUCCESS! CONTRACT DEPLOYED ON ETHEREUM SEPOLIA")
    print(f"  Contract Address : {contract_address}")
    print(f"  Gas Used         : {tx_receipt.gasUsed:,}")
    print(f"  Etherscan Link   : https://sepolia.etherscan.io/address/{contract_address}")
    print("=" * 80)
    print("\n-> Add this address to your .env file:")
    print(f"   SEPOLIA_CONTRACT_ADDRESS={contract_address}\n")

if __name__ == '__main__':
    w3, account = check_connection()
    if len(sys.argv) > 1 and sys.argv[1] == '--deploy':
        deploy_contract(w3, account)
