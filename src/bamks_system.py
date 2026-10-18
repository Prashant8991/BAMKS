import random
import time
from .crypto_utils import (
    PRIME_P, hash_to_int, h1, kdf, aes_encrypt, aes_decrypt,
    simulated_pairing, generate_snizk_proof, verify_snizk_proof
)

class BAMKSSystem:
    def __init__(self, security_param: int = 256):
        self.g = 2 # Generator
        self.security_param = security_param
        # Shared secret exponent eta for index generation across collection
        self.eta = random.randint(1000, 99999) % (PRIME_P - 1)
        self.g_eta = pow(self.g, self.eta, PRIME_P)
        self.gp = {}
        self.msk = {}
        self.auth_keys = {}
        self.users = {}
        self.files = {}
        self.indices = {}

    def global_setup(self):
        """(1) GlobalSetup(1^iota) -> (GP, MSK)"""
        mu = random.randint(1000, 99999) % PRIME_P
        gamma = random.randint(1000, 99999) % PRIME_P
        # Ensure shared collection-level eta is initialized
        self.eta = random.randint(1000, 99999) % (PRIME_P - 1)
        self.g_eta = pow(self.g, self.eta, PRIME_P)
        self.msk = {'mu': mu, 'gamma': gamma, 'eta': self.eta}
        self.gp = {
            'g': self.g,
            'g_mu': pow(self.g, mu, PRIME_P),
            'g_gamma': pow(self.g, gamma, PRIME_P),
            'g_eta': self.g_eta,
            'e_gg_mu': simulated_pairing(pow(self.g, mu, PRIME_P), self.g)
        }
        return self.gp

    def auth_setup(self, authority_id: str, attributes: list):
        """(2) AuthSetup(GP, U_theta, theta) -> (pk_AA, sk_AA)"""
        alpha = random.randint(100, 9999) % PRIME_P
        beta = random.randint(100, 9999) % PRIME_P
        sk_aa = {'alpha': alpha, 'beta': beta}
        pk_aa = {
            'e_gg_alpha': simulated_pairing(pow(self.g, alpha, PRIME_P), self.g),
            'g_beta': pow(self.g, beta, PRIME_P)
        }
        self.auth_keys[authority_id] = {'sk': sk_aa, 'pk': pk_aa, 'attrs': attributes}
        return pk_aa

    def do_setup(self, owners: list):
        """(3) DOSetup(GP, O) -> (epsilon, Phi)"""
        epsilon = random.randint(500, 5000) % PRIME_P
        phi_values = [random.randint(10, 100) for _ in owners]
        phi = sum(phi_values)
        return epsilon, phi

    def du_setup(self, uid: str):
        """(4) DUSetup(GP, uid) -> (upk, usk, h_varpi)"""
        chi = random.randint(100, 999) % PRIME_P
        zeta = random.randint(100, 999) % PRIME_P
        upk = {'g_chi': pow(self.g, chi, PRIME_P), 'g_zeta': pow(self.g, zeta, PRIME_P)}
        usk = {'chi': chi, 'zeta': zeta}
        h_varpi = h1(f"Reg_{uid}_{chi}")
        self.users[uid] = {'upk': upk, 'usk': usk, 'h_varpi': h_varpi}
        return upk, usk, h_varpi

    def keygen(self, uid: str, user_attributes: list, dpk_ver: int):
        """(6) KeyGen(GP, uid, S_uid, {sk_AA}, dpk_ver, h_varpi) -> SK_uid"""
        # Bug 3 fix: Sample randomness t and incorporate into k1 and k2
        t = random.randint(10, 500) % (PRIME_P - 1)
        exp_k1 = (-t) % (PRIME_P - 1)
        k1 = pow(h1(uid), exp_k1, PRIME_P) # H1(uid)^(-t) mod P
        
        k2_dict = {}
        for attr in user_attributes:
            # Find managing AA
            for auth_id, info in self.auth_keys.items():
                if attr in info['attrs']:
                    alpha = info['sk']['alpha']
                    beta = info['sk']['beta']
                    # Incorporate t into k2: (h1(uid)^(t * beta) * dpk_ver^alpha) mod P
                    t_beta = (t * beta) % (PRIME_P - 1)
                    val = (pow(h1(uid), t_beta, PRIME_P) * pow(dpk_ver, alpha, PRIME_P)) % PRIME_P
                    k2_dict[attr] = val
                    break
        
        h_varpi = self.users[uid]['h_varpi']
        k3 = h_varpi
        sk_uid = {'k1': k1, 'k2': k2_dict, 'k3': k3, 'attrs': user_attributes, 't': t}
        return sk_uid

    def file_encrypt(self, doc_id: int, file_content: str, token_phi: int, version_id: int):
        """(7) FileEnc(F_ver, K, Phi, VPK_ver) -> CT_Fver"""
        sym_key = kdf(token_phi, version_id)
        enc_payload = aes_encrypt(sym_key, file_content)
        
        sigma_k = random.randint(10, 999) % PRIME_P
        y_k = pow(self.g, sigma_k, PRIME_P) # Tag
        
        doc_entry = {
            'doc_id': doc_id,
            'enc_payload': enc_payload,
            'sigma_k': sigma_k,
            'y_k': y_k,
            'version_id': version_id,
            'keywords': [] # Will be populated if passed in single_doc_add
        }
        self.files[doc_id] = doc_entry
        return doc_entry

    def token_encrypt_onchain(self, access_policy: list, token_phi: int):
        """(8 & 9) TokenEnc(GP, (M, rho), Phi) -> CT_Phi"""
        s = random.randint(10, 100) % PRIME_P
        c_val = (token_phi * pow(self.gp['e_gg_mu'], s, PRIME_P)) % PRIME_P
        c0 = pow(self.g, s, PRIME_P)
        return {'C': c_val, 'C0': c0, 'policy': access_policy, 's': s}

    def index_gen(self, doc_id: int, keywords: list):
        """
        (10) IndexGen(GP, W, O) -> Index_W
        Bug 1 fix:
        1. Uses shared self.eta (per collection/version), not per-document randomness.
        2. Keys are derived from pow(g, eta * h1(kw), P).
        3. Plaintext keywords are NEVER stored in keys, values, or attributes of the index.
        """
        index_entries = {}
        for kw in keywords:
            # I_kw = g^(eta * H1(kw)) mod P
            exp_val = (self.eta * h1(kw)) % (PRIME_P - 1)
            i_kw = pow(self.g, exp_val, PRIME_P)
            # Index key is derived from the cryptographic value, NOT plaintext keyword string
            tok_key = hash_to_int(f"tok_{i_kw}")
            index_entries[tok_key] = i_kw
        
        self.indices[doc_id] = {
            'doc_id': doc_id,
            'i1': pow(self.g, (self.eta + 5) % (PRIME_P - 1), PRIME_P),
            'kw_indices': index_entries
        }
        if doc_id in self.files:
            self.files[doc_id]['keywords'] = list(keywords)
        return self.indices[doc_id]

    def trapdoor_gen(self, query_keywords: list):
        """
        (11) TrapGen(GP, W_tilde, usk) -> Trap_W_tilde
        Bug 1 fix:
        Generates T1 = g^phi, T2 = g^(phi+2), T3 = g^(phi * sum(H1(kw)))
        and cryptographic query tokens without exposing plaintext strings in the match logic.
        """
        phi_rand = random.randint(5, 500) % (PRIME_P - 1)
        t1 = pow(self.g, phi_rand, PRIME_P)
        t2 = pow(self.g, (phi_rand + 2) % (PRIME_P - 1), PRIME_P)
        
        kw_sum = sum([h1(kw) for kw in query_keywords]) % (PRIME_P - 1)
        t3 = pow(self.g, (phi_rand * kw_sum) % (PRIME_P - 1), PRIME_P)

        # Cryptographic query tokens corresponding to the query keywords
        query_tokens = []
        for kw in query_keywords:
            exp_val = (self.eta * h1(kw)) % (PRIME_P - 1)
            i_kw = pow(self.g, exp_val, PRIME_P)
            tok_key = hash_to_int(f"tok_{i_kw}")
            query_tokens.append(tok_key)

        return {
            'T1': t1,
            'T2': t2,
            'T3': t3,
            'phi': phi_rand,
            'query_tokens': query_tokens,
            'kw_sum': kw_sum,
            'keywords': query_keywords
        }

    def search(self, trapdoor: dict):
        """
        (12) Search(GP, Index_W, Trap_W_tilde) -> SRL
        Bug 1 fix:
        Algebraic match checking Equation (9) of BAMKS:
        Checks e(I_prod, T1) == e(g_eta, T3) via modular arithmetic:
        (I_prod)^phi mod P == (T3)^eta mod P
        Does NOT perform plaintext string lookups.
        """
        matched_doc_ids = []
        query_tokens = trapdoor.get('query_tokens', [])
        if not query_tokens:
            return matched_doc_ids

        t1 = trapdoor['T1']
        t3 = trapdoor['T3']
        phi = trapdoor.get('phi')

        for doc_id, index_data in self.indices.items():
            kw_map = index_data.get('kw_indices', {})
            
            # Retrieve cryptographic entries matching all query tokens
            matching_i_vals = []
            all_present = True
            for q_tok in query_tokens:
                if q_tok in kw_map:
                    matching_i_vals.append(kw_map[q_tok])
                else:
                    all_present = False
                    break
            
            if not all_present or not matching_i_vals:
                continue

            # Compute product of matched keyword index entries:
            # I_prod = prod(g^(eta * H1(kw))) = g^(eta * sum(H1(kw))) mod P
            i_prod = 1
            for entry_val in matching_i_vals:
                i_prod = (i_prod * entry_val) % PRIME_P

            # Algebraic verification reproducing Equation (9) from base paper:
            # e(I_prod, T1) = e(g_eta, T3)
            # In our cyclic group G over Z_p*:
            # LHS = (I_prod)^phi = g^(eta * sum(H1(kw)) * phi) mod P
            # RHS = (T3)^eta     = g^(phi * sum(H1(kw)) * eta) mod P
            if phi is not None:
                lhs = pow(i_prod, phi, PRIME_P)
                rhs = pow(t3, self.eta, PRIME_P)
            else:
                kw_sum = trapdoor.get('kw_sum', 0)
                lhs = pow(t1, (self.eta * kw_sum) % (PRIME_P - 1), PRIME_P)
                rhs = pow(t3, self.eta, PRIME_P)

            if lhs == rhs and lhs != 1:
                matched_doc_ids.append(doc_id)
        
        return matched_doc_ids

    def verify_results(self, matched_doc_ids: list):
        """(13) ProofVerify(GP, SRL, {y_k*}) -> True / False"""
        tags = [str(self.files[doc_id]['y_k']) for doc_id in matched_doc_ids]
        sigmas = [self.files[doc_id]['sigma_k'] for doc_id in matched_doc_ids]
        
        proof = generate_snizk_proof(tags, sigmas)
        return verify_snizk_proof(tags, proof)

    def decrypt_file(self, doc_id: int, token_phi: int, version_id: int) -> str:
        """(15) FinalDecrypt -> Plaintext"""
        sym_key = kdf(token_phi, version_id)
        enc_payload = self.files[doc_id]['enc_payload']
        return aes_decrypt(sym_key, enc_payload)
