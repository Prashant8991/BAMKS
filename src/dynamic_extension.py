import time
from .crypto_utils import PRIME_P
from .bamks_system import BAMKSSystem

class DynamicBAMKSExtension(BAMKSSystem):
    """
    PROPOSED RESEARCH GAP EXTENSION (Cheng et al., Elsevier 2026 Section 8 Gap)
    Implements:
      1. SingleDocAdd: Incremental single-document addition (O(m) complexity vs O(L x m) base re-keying)
      2. SingleDocDelete: Instant smart-contract document deletion (O(1) complexity)
      3. SearchWithFilter: Dynamic trapdoor search filtering deleted documents on-chain
    """
    def __init__(self, security_param: int = 256):
        super().__init__(security_param)
        self.deleted_doc_registry = {} # doc_id -> is_deleted (Solidity Mapping Simulation)

    def single_doc_add(self, doc_id: int, file_content: str, keywords: list, token_phi: int, version_id: int):
        """
        PROPOSED WORK: Incremental Single-Document Addition (O(m) time)
        Appends 1 file without modifying existing version keys or re-keying L files!
        """
        start_time = time.perf_counter()
        
        # 1. Encrypt file payload independently
        doc_entry = self.file_encrypt(doc_id, file_content, token_phi, version_id)
        
        # 2. Generate keyword index ONLY for this single document
        index_entry = self.index_gen(doc_id, keywords)
        
        # 3. Register as active
        self.deleted_doc_registry[doc_id] = False
        
        addition_time_ms = (time.perf_counter() - start_time) * 1000
        return doc_entry, index_entry, addition_time_ms

    def single_doc_delete(self, doc_id: int):
        """
        PROPOSED WORK: Instant Single-Document Deletion (O(1) time)
        Updates smart contract deletion mapping deletedDocRegistry[docID] = true
        """
        start_time = time.perf_counter()
        
        if doc_id in self.files:
            self.deleted_doc_registry[doc_id] = True
            self.files[doc_id]['is_deleted'] = True
        
        deletion_time_ms = (time.perf_counter() - start_time) * 1000
        return deletion_time_ms

    def single_doc_modify(self, doc_id: int, new_content: str, new_keywords: list, token_phi: int, version_id: int):
        """
        PROPOSED WORK: Single-Document Modification (Report Section 6)
        Implemented as delete of existing file entry followed by insert of updated entry.
        """
        del_time = self.single_doc_delete(doc_id)
        doc_entry, index_entry, add_time = self.single_doc_add(
            doc_id, new_content, new_keywords, token_phi, version_id
        )
        return doc_entry, index_entry, del_time + add_time


    def search_with_filter(self, trapdoor: dict):
        """
        PROPOSED WORK: Search execution skipping revoked/deleted documents
        """
        start_time = time.time()
        
        # Base paper matching logic
        raw_matches = self.search(trapdoor)
        
        # Filter out deleted documents (Smart Contract On-Chain Filter)
        active_matches = [
            doc_id for doc_id in raw_matches 
            if not self.deleted_doc_registry.get(doc_id, False)
        ]
        
        search_time_ms = (time.time() - start_time) * 1000
        return active_matches, search_time_ms

    def benchmark_full_rekeying_vs_dynamic(self, num_files: int, keywords_per_doc: int = 10):
        """
        Benchmark Comparison: Base Paper Full Version Re-keying O(L x m) vs Our Dynamic Update O(m)
        """
        # Base paper full re-keying time
        start_rekey = time.perf_counter()
        for _ in range(min(num_files * keywords_per_doc, 5000)):
            pow(2, 5000, PRIME_P) # Simulate exponentiations across L x m
        base_rekey_time_ms = (time.perf_counter() - start_rekey) * 1000

        # Our single-document addition time
        start_our = time.perf_counter()
        for _ in range(keywords_per_doc):
            pow(2, 5000, PRIME_P) # Exponentiations for 1 doc (1 x m)
        our_add_time_ms = (time.perf_counter() - start_our) * 1000

        return {
            'num_files': num_files,
            'base_full_rekey_time_ms': round(base_rekey_time_ms, 2),
            'our_single_doc_add_time_ms': round(our_add_time_ms, 2),
            'speedup_factor': round(base_rekey_time_ms / max(our_add_time_ms, 0.001), 1)
        }
