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
        start_time = time.perf_counter()
        
        # Base paper matching logic
        raw_matches = self.search(trapdoor)
        
        # Filter out deleted documents (Smart Contract On-Chain Filter)
        active_matches = [
            doc_id for doc_id in raw_matches 
            if not self.deleted_doc_registry.get(doc_id, False)
        ]
        
        search_time_ms = (time.perf_counter() - start_time) * 1000
        return active_matches, search_time_ms

    def full_reindex_baseline(self, num_files: int, keywords_sample: list = None, token_phi: int = 12345, version_id: int = 1):
        """
        Base Paper Baseline: Re-encrypting and re-indexing all L files in the collection
        due to lack of dynamic single-document update support.
        Actually calls file_encrypt and index_gen for every document in an L-file collection, timed for real.
        """
        if keywords_sample is None:
            keywords_sample = ["Cardiology", "ECG", "Emergency"]
        
        start_time = time.perf_counter()
        # Save indices and files state
        old_indices = self.indices
        old_files = self.files
        temp_indices = {}
        temp_files = {}
        
        try:
            self.indices = temp_indices
            self.files = temp_files
            for i in range(1, num_files + 1):
                self.file_encrypt(i, f"Simulated Patient Record #{i}", token_phi, version_id)
                self.index_gen(i, keywords_sample)
        finally:
            self.indices = old_indices
            self.files = old_files
            
        elapsed_ms = (time.perf_counter() - start_time) * 1000
        return elapsed_ms

    def benchmark_full_rekeying_vs_dynamic(self, num_files: int, keywords_per_doc: int = 3, token_phi: int = 12345, version_id: int = 1):
        """
        Real benchmark comparison: Base Paper Full Re-indexing O(L x m) vs Our Dynamic Update O(m).
        Uses actual execution calls and time.perf_counter().
        """
        keywords_sample = ["Cardiology", "ECG", "Emergency"][:keywords_per_doc]
        if not keywords_sample:
            keywords_sample = ["Cardiology", "ECG"]

        # 1. Base paper full re-indexing of all L files
        base_rekey_time_ms = self.full_reindex_baseline(num_files, keywords_sample, token_phi, version_id)

        # 2. Our single-document addition
        test_doc_id = 999999
        _, _, our_add_time_ms = self.single_doc_add(test_doc_id, "Benchmark test doc", keywords_sample, token_phi, version_id)
        # Clean up benchmark doc
        self.indices.pop(test_doc_id, None)
        self.files.pop(test_doc_id, None)
        self.deleted_doc_registry.pop(test_doc_id, None)

        speedup = base_rekey_time_ms / max(our_add_time_ms, 0.0001)

        return {
            'num_files': num_files,
            'base_full_rekey_time_ms': base_rekey_time_ms,
            'our_single_doc_add_time_ms': our_add_time_ms,
            'speedup_factor': speedup
        }

    def single_doc_add_batch(self, list_of_docs: list, token_phi: int, version_id: int):
        """
        Batch Document Addition: Adds multiple files in a single invocation.
        list_of_docs format: [(doc_id, file_content, keywords), ...]
        Returns: (results_list, total_time_ms, per_file_avg_ms)
        Demonstrates that per-file cost stays flat O(m) even under batch processing O(B x m).
        """
        start_time = time.perf_counter()
        results = []
        for doc_id, file_content, keywords in list_of_docs:
            doc_entry, index_entry, _ = self.single_doc_add(doc_id, file_content, keywords, token_phi, version_id)
            results.append((doc_entry, index_entry))
        
        total_time_ms = (time.perf_counter() - start_time) * 1000
        per_file_avg_ms = total_time_ms / max(len(list_of_docs), 1)
        return results, total_time_ms, per_file_avg_ms

    def measure_index_storage_bytes(self) -> int:
        """
        Measures actual serialized byte count of the current encrypted inverted index.
        """
        import json
        serializable_indices = {}
        for doc_id, data in self.indices.items():
            serializable_indices[str(doc_id)] = {
                'doc_id': data['doc_id'],
                'i1': str(data.get('i1', '')),
                'kw_indices': {str(k): str(v) for k, v in data.get('kw_indices', {}).items()}
            }
        return len(json.dumps(serializable_indices).encode('utf-8'))

