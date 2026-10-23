import time
import json
import csv
import numpy as np
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Secp256k1 Field Prime used in BAMKS-D Prototype
P = 2**256 - 2**32 - 977
g = 2
m = 3 # keywords per document
eta = 0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b % (P - 1)
sample_keywords = ["Cardiology", "Arrhythmia", "Telemetry"]
sample_kw_hashes = [int.from_bytes(f"kw_{kw}".encode('utf-8'), 'big') % (P - 1) for kw in sample_keywords]
dummy_file_bytes = b"Clinical patient record telemetry ECG trace data block format 2026." * 10

def simulate_aes_file_enc():
    key = get_random_bytes(32)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(dummy_file_bytes)
    return len(ciphertext)

def run_benchmarks():
    dataset_sizes = [10, 50, 100, 500, 1000, 2000, 5000]
    num_runs = 30
    results = []

    print("=" * 85)
    print("RUNNING STANDARDIZED REPRODUCIBLE BENCHMARK (30 RUNS, WARM-UP DISCARDED, m=3)")
    print("=" * 85)

    for L in dataset_sizes:
        # --- 0. Warm-up (Discarded) ---
        for _ in range(2):
            simulate_aes_file_enc()
            for _ in range(L * m):
                pow(g, 123456, P)

        naive_times = []
        cheng_index_times = []
        cheng_full_times = []
        bamks_index_times = []
        bamks_full_times = []

        for _ in range(num_runs):
            # 1. Naive Full Re-encrypt & Re-index
            t0 = time.perf_counter()
            for _ in range(L):
                simulate_aes_file_enc()
            for _ in range(L * m):
                pow(g, 123456, P)
            naive_times.append((time.perf_counter() - t0) * 1000)

            # 2. Cheng et al. Sec. 5.10 (L * m modular multiplications)
            t0 = time.perf_counter()
            val = 1
            for i in range(L * m):
                val = (val * (100003 + i)) % P
            t_cheng_idx = (time.perf_counter() - t0) * 1000
            cheng_index_times.append(t_cheng_idx)

            # 3. Cheng et al. Full Add (1 file enc + L * m mults)
            t0 = time.perf_counter()
            simulate_aes_file_enc()
            val = 1
            for i in range(L * m):
                val = (val * (100003 + i)) % P
            t_cheng_full = (time.perf_counter() - t0) * 1000
            cheng_full_times.append(t_cheng_full)

            # 4. BAMKS-D Pure Index Token Generation (m modular exponentiations)
            t0 = time.perf_counter()
            for h_w in sample_kw_hashes:
                pow(g, (eta * h_w) % (P - 1), P)
            t_bamks_idx = (time.perf_counter() - t0) * 1000
            bamks_index_times.append(t_bamks_idx)

            # 5. BAMKS-D Full Single-Doc Add (1 file enc + m token exp)
            t0 = time.perf_counter()
            simulate_aes_file_enc()
            for h_w in sample_kw_hashes:
                pow(g, (eta * h_w) % (P - 1), P)
            t_bamks_full = (time.perf_counter() - t0) * 1000
            bamks_full_times.append(t_bamks_full)

        res_item = {
            "L": L,
            "m": m,
            "naive_mean_ms": round(float(np.mean(naive_times)), 4),
            "naive_std_ms": round(float(np.std(naive_times)), 4),
            "naive_median_ms": round(float(np.median(naive_times)), 4),
            "cheng_index_mean_ms": round(float(np.mean(cheng_index_times)), 4),
            "cheng_index_std_ms": round(float(np.std(cheng_index_times)), 4),
            "cheng_index_median_ms": round(float(np.median(cheng_index_times)), 4),
            "cheng_full_mean_ms": round(float(np.mean(cheng_full_times)), 4),
            "cheng_full_std_ms": round(float(np.std(cheng_full_times)), 4),
            "bamks_d_index_mean_ms": round(float(np.mean(bamks_index_times)), 4),
            "bamks_d_index_std_ms": round(float(np.std(bamks_index_times)), 4),
            "bamks_d_full_mean_ms": round(float(np.mean(bamks_full_times)), 4),
            "bamks_d_full_std_ms": round(float(np.std(bamks_full_times)), 4),
            "bamks_d_full_median_ms": round(float(np.median(bamks_full_times)), 4),
            # Speedup vs Cheng pure index
            "speedup_vs_cheng_index": round(float(np.mean(cheng_index_times) / np.mean(bamks_full_times)), 2),
            # Speedup vs Cheng full add (like-for-like end-to-end)
            "speedup_vs_cheng_full": round(float(np.mean(cheng_full_times) / np.mean(bamks_full_times)), 2),
            # Speedup vs Naive
            "speedup_vs_naive": round(float(np.mean(naive_times) / np.mean(bamks_full_times)), 2),
        }
        results.append(res_item)
        print(f"L = {L:<5} | Naive: {res_item['naive_mean_ms']:>8.2f} ms | Cheng Index: {res_item['cheng_index_mean_ms']:>6.3f} ms | BAMKS-D Full: {res_item['bamks_d_full_mean_ms']:>6.3f} ms | Speedup vs Cheng: {res_item['speedup_vs_cheng_index']:>5.2f}x")

    # Save to JSON
    json_path = "submission_materials/5_Supplementary_Files/benchmark_fair_results.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    # Save to CSV
    csv_path = "submission_materials/5_Supplementary_Files/benchmark_fair_results.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print("\n[SUCCESS] Benchmark completed and saved to JSON & CSV:")
    print(f"  JSON: {json_path}")
    print(f"  CSV : {csv_path}")

if __name__ == "__main__":
    run_benchmarks()
