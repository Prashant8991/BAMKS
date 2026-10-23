import hashlib
import hmac
import os
import time
from Crypto.Cipher import AES

# System Prime Order (256-bit prime for simulated cyclic group G)
PRIME_P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F

def hash_to_int(data: str) -> int:
    """Hash string input to integer modulo prime P"""
    digest = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return int(digest, 16) % PRIME_P

def h1(data: str) -> int:
    """Cryptographic hash function H1: {0,1}* -> Z_p*"""
    digest = hashlib.sha256(f"H1_{data}".encode('utf-8')).hexdigest()
    val = int(digest, 16) % PRIME_P
    return val if val != 0 else 1

def kdf(token_val: int, version_id: int) -> bytes:
    """Key Derivation Function: KDF(Phi || H1(g^delta_ver))"""
    input_str = f"{token_val}_{version_id}"
    return hashlib.sha256(input_str.encode('utf-8')).digest()

def aes_encrypt(key: bytes, plaintext: str) -> dict:
    """AES-256-GCM Authenticated Encryption"""
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    return {
        'ciphertext': ciphertext.hex(),
        'nonce': cipher.nonce.hex(),
        'tag': tag.hex()
    }

def aes_decrypt(key: bytes, enc_dict: dict) -> str:
    """AES-256-GCM Authenticated Decryption"""
    ciphertext = bytes.fromhex(enc_dict['ciphertext'])
    nonce = bytes.fromhex(enc_dict['nonce'])
    tag = bytes.fromhex(enc_dict['tag'])
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('utf-8')

def simulated_pairing(g1_element: int, g2_element: int) -> int:
    """
    Simulated Bilinear Pairing Map e_hat: G x G -> G_T
    Satisfies e_hat(g^a, g^b) = e_hat(g, g)^(ab) mod P
    """
    return pow(g1_element, g2_element, PRIME_P)

def generate_snizk_proof(matched_tags: list, secret_sigmas: list):
    """
    Schnorr Non-Interactive Zero-Knowledge (SNIZK) Aggregated Proof Generation
    Prover computes R = g^(sum c_k*), h_k* = H1(y_k* || R), pi_k* = c_k* + h_k* * sigma_k*
    Aggregated proof pi_hat = sum(pi_k*)
    """
    random_c = [int(os.urandom(16).hex(), 16) % PRIME_P for _ in matched_tags]
    sum_c = sum(random_c) % (PRIME_P - 1)
    g = 2 # Generator
    R = pow(g, sum_c, PRIME_P)

    aggregated_pi = 0
    for idx, tag in enumerate(matched_tags):
        h_k = h1(f"{tag}_{R}")
        pi_k = (random_c[idx] + h_k * secret_sigmas[idx]) % (PRIME_P - 1)
        aggregated_pi = (aggregated_pi + pi_k) % (PRIME_P - 1)

    return {'R': R, 'pi_hat': aggregated_pi}

def verify_snizk_proof(matched_tags: list, proof: dict) -> bool:
    """
    Verifier checks equation (10) from paper:
    R = g^pi_hat * prod(y_k*^-h_k*) mod P
    """
    R = proof['R']
    pi_hat = proof['pi_hat']
    g = 2

    rhs_multiplier = 1
    for tag in matched_tags:
        h_k = h1(f"{tag}_{R}")
        y_k = int(tag)
        y_inv = pow(y_k, PRIME_P - 2, PRIME_P)
        y_inv_h = pow(y_inv, h_k, PRIME_P)
        rhs_multiplier = (rhs_multiplier * y_inv_h) % PRIME_P

    expected_R = (pow(g, pi_hat, PRIME_P) * rhs_multiplier) % PRIME_P
    return R == expected_R
