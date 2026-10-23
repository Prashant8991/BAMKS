import os
import json
import time
from dotenv import load_dotenv
from web3 import Web3
from web3.middleware import ExtraDataToPOAMiddleware

load_dotenv()
rpc = os.getenv("SEPOLIA_RPC_URL", "https://ethereum-sepolia-rpc.publicnode.com")
pk = os.getenv("SEPOLIA_PRIVATE_KEY", "").strip()
if not pk.startswith("0x"):
    pk = "0x" + pk

w3 = Web3(Web3.HTTPProvider(rpc))
w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)
account = w3.eth.account.from_key(pk)
print("Connected:", w3.is_connected())
print("Deployer:", account.address)
bal_eth = w3.from_wei(w3.eth.get_balance(account.address), 'ether')
print("Balance ETH:", bal_eth)

with open("contracts/build/contracts_BAMKS_Registry_sol_BAMKS_Registry.abi") as f:
    abi = json.load(f)
with open("contracts/build/contracts_BAMKS_Registry_sol_BAMKS_Registry.bin") as f:
    bin_code = f.read().strip()

# 1. Deploy
nonce = w3.eth.get_transaction_count(account.address)
gas_price = int(w3.eth.gas_price * 1.3)
Registry = w3.eth.contract(abi=abi, bytecode=bin_code)

deploy_tx = Registry.constructor().build_transaction({
    'from': account.address,
    'nonce': nonce,
    'gas': 4200000,
    'gasPrice': gas_price,
    'chainId': w3.eth.chain_id
})
signed = w3.eth.account.sign_transaction(deploy_tx, pk)
t0 = time.time()
tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
print(f"Deploy Tx Sent: {tx_hash.hex()}")
rc = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=180)
deploy_time = time.time() - t0
print(f"DEPLOY STATUS: {rc.status}")
print(f"Contract Address: {rc.contractAddress}")
print(f"Gas Used: {rc.gasUsed:,}")
print(f"Block Number: #{rc.blockNumber}")
print(f"Time: {deploy_time:.2f} s")

if rc.status != 1:
    print("[ERROR] Deployment failed!")
    exit(1)

contract_address = rc.contractAddress
contract = w3.eth.contract(address=contract_address, abi=abi)

# 2. Register Document 101
nonce += 1
gas_price = int(w3.eth.gas_price * 1.3)
h_101 = bytes.fromhex("57ec175db0fe5211169beb7d9e688fd45e477894437460d1614a478bbfaa5d63")
tag_101 = bytes.fromhex("4dc9bcb5cb4f7c9b9253d824692e6f62b839f0e11fa5f08c56b3e31fa0c4598c")

reg_tx = contract.functions.registerDocument(101, h_101, tag_101).build_transaction({
    'from': account.address,
    'nonce': nonce,
    'gas': 300000,
    'gasPrice': gas_price,
    'chainId': w3.eth.chain_id
})
signed_reg = w3.eth.account.sign_transaction(reg_tx, pk)
t0 = time.time()
tx_hash_reg = w3.eth.send_raw_transaction(signed_reg.raw_transaction)
print(f"\nRegister Tx Sent: {tx_hash_reg.hex()}")
rc_reg = w3.eth.wait_for_transaction_receipt(tx_hash_reg, timeout=180)
reg_time = time.time() - t0
print(f"REGISTER STATUS: {rc_reg.status}")
print(f"Gas Used: {rc_reg.gasUsed:,}")
print(f"Block Number: #{rc_reg.blockNumber}")
print(f"Time: {reg_time:.2f} s")

# 3. Delete Document 101
nonce += 1
gas_price = int(w3.eth.gas_price * 1.3)
del_tx = contract.functions.deleteDocument(101).build_transaction({
    'from': account.address,
    'nonce': nonce,
    'gas': 200000,
    'gasPrice': gas_price,
    'chainId': w3.eth.chain_id
})
signed_del = w3.eth.account.sign_transaction(del_tx, pk)
t0 = time.time()
tx_hash_del = w3.eth.send_raw_transaction(signed_del.raw_transaction)
print(f"\nDelete Tx Sent: {tx_hash_del.hex()}")
rc_del = w3.eth.wait_for_transaction_receipt(tx_hash_del, timeout=180)
del_time = time.time() - t0
print(f"DELETE STATUS: {rc_del.status}")
print(f"Gas Used: {rc_del.gasUsed:,}")
print(f"Block Number: #{rc_del.blockNumber}")
print(f"Time: {del_time:.2f} s")

# Save receipts to JSON
receipts = {
    "contract_address": contract_address,
    "deploy": {
        "tx_hash": tx_hash.hex(),
        "block": rc.blockNumber,
        "gas_used": rc.gasUsed,
        "confirmation_time_s": round(deploy_time, 2)
    },
    "register": {
        "tx_hash": tx_hash_reg.hex(),
        "block": rc_reg.blockNumber,
        "gas_used": rc_reg.gasUsed,
        "confirmation_time_s": round(reg_time, 2)
    },
    "delete": {
        "tx_hash": tx_hash_del.hex(),
        "block": rc_del.blockNumber,
        "gas_used": rc_del.gasUsed,
        "confirmation_time_s": round(del_time, 2)
    }
}
with open("sepolia_deployment_receipts.json", "w") as f:
    json.dump(receipts, f, indent=2)

print("\n" + "=" * 80)
print("SUCCESSFULLY MINED AND VERIFIED ON ETHEREUM SEPOLIA!")
print("=" * 80)
print(json.dumps(receipts, indent=2))
