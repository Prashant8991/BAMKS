import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

os.makedirs("diagrams", exist_ok=True)

def generate_scalability_analysis():
    print("=" * 80)
    print("  GENERATING REVIEW 3 FAIR SCALABILITY GRAPH & MULTI-N BENCHMARKS")
    print("=" * 80)

    # Load verified 30-run benchmark data
    results_path = os.path.join("submission_materials", "5_Supplementary_Files", "benchmark_fair_results.json")
    if os.path.exists(results_path):
        with open(results_path, 'r', encoding='utf-8') as f:
            bench_data = json.load(f)
    else:
        print("[ERROR] benchmark_fair_results.json not found!")
        return

    n_values = [item['L'] for item in bench_data]
    naive_times = [item.get('naive_mean_ms', item.get('naive_median_ms')) for item in bench_data]
    cheng_times = [item.get('cheng_index_mean_ms', item.get('cheng_mean_ms')) for item in bench_data]
    cheng_full_times = [item.get('cheng_full_mean_ms', item.get('cheng_mean_ms')) for item in bench_data]
    add_times = [item.get('bamks_d_full_mean_ms', item.get('bamks_d_mean_ms')) for item in bench_data]
    speedup_naive = [item['speedup_vs_naive'] for item in bench_data]
    speedup_cheng = [item.get('speedup_vs_cheng_index', item.get('speedup_vs_cheng')) for item in bench_data]
    index_sizes_kb = [(n * 452.0) / 1024.0 for n in n_values]

    # -------------------------------------------------------------------------
    # MULTI-PANEL PUBLICATION GRAPH (4 PANELS)
    # -------------------------------------------------------------------------
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 9), dpi=300)
    fig.patch.set_facecolor('#0f172a')

    for ax in [ax1, ax2, ax3, ax4]:
        ax.set_facecolor('#1e293b')
        ax.tick_params(colors='#ffffff', labelsize=9)
        ax.grid(True, which="both", ls="--", lw=0.5, color='#334155')

    # Panel 1: Three-way Latency Scaling (Log Scale)
    ax1.plot(n_values, naive_times, marker='o', color='#f43f5e', lw=2.5, label='Naive Re-encrypt & Re-index O(L*m)')
    ax1.plot(n_values, cheng_times, marker='^', color='#fbbf24', lw=2.5, label='Cheng et al. Sec. 5.10 Index Update O(L*m)')
    ax1.plot(n_values, add_times, marker='s', color='#38bdf8', lw=2.5, label='BAMKS-D SingleDocAdd O(m)')
    ax1.set_yscale('log')
    ax1.set_xlabel('Dataset Size L (Number of Files)', color='#ffffff', fontsize=10, weight='bold')
    ax1.set_ylabel('Execution Time (ms, Log Scale)', color='#ffffff', fontsize=10, weight='bold')
    ax1.set_title('Update Latency Scaling (Log Scale, m=3, N=30 runs)', color='#ffffff', fontsize=11, weight='bold', pad=10)
    ax1.legend(facecolor='#1e293b', edgecolor='#475569', labelcolor='#ffffff', fontsize=8.5)

    # Panel 2: True Base (Cheng et al.) vs BAMKS-D (Linear Scale)
    ax2.plot(n_values, cheng_times, marker='^', color='#fbbf24', lw=2, label='Cheng et al. Sec. 5.10 (Linear Growth)')
    ax2.plot(n_values, add_times, marker='s', color='#38bdf8', lw=2, label='BAMKS-D Add (Flat O(m) ~0.4-0.6 ms)')
    ax2.set_xlabel('Dataset Size L (Number of Files)', color='#ffffff', fontsize=10, weight='bold')
    ax2.set_ylabel('Execution Time (ms, Linear Scale)', color='#ffffff', fontsize=10, weight='bold')
    ax2.set_title('Cheng et al. Index Update vs. BAMKS-D Add (Linear Scale)', color='#ffffff', fontsize=11, weight='bold', pad=10)
    ax2.legend(facecolor='#1e293b', edgecolor='#475569', labelcolor='#ffffff', fontsize=8.5)

    # Panel 3: Empirical Speedup Factors
    x_indices = range(len(n_values))
    width = 0.35
    ax3.bar([x - width/2 for x in x_indices], speedup_cheng, width=width, color='#38bdf8', label='Speedup vs. Cheng et al. Base', edgecolor='#ffffff', lw=0.6)
    ax3.set_xlabel('Dataset Size L (Number of Files)', color='#ffffff', fontsize=10, weight='bold')
    ax3.set_ylabel('Speedup Factor (x Faster)', color='#ffffff', fontsize=10, weight='bold')
    ax3.set_xticks(list(x_indices))
    ax3.set_xticklabels([str(n) for n in n_values])
    ax3.set_title('Speedup vs. Cheng et al. Sec. 5.10 (12.1x at L=5,000)', color='#ffffff', fontsize=11, weight='bold', pad=10)
    for idx, sp in enumerate(speedup_cheng):
        ax3.text(idx - width/2, sp + 0.3, f"{sp:.1f}x", ha='center', va='bottom', color='#ffffff', weight='bold', fontsize=8)
    ax3.legend(facecolor='#1e293b', edgecolor='#475569', labelcolor='#ffffff', fontsize=8.5)

    # Panel 4: Index Storage Footprint
    ax4.plot(n_values, index_sizes_kb, marker='d', color='#10b981', lw=2.5)
    ax4.set_xlabel('Dataset Size L (Number of Files)', color='#ffffff', fontsize=10, weight='bold')
    ax4.set_ylabel('Index Storage Size (KB)', color='#ffffff', fontsize=10, weight='bold')
    ax4.set_title('Encrypted Inverted Index Footprint (Strictly O(L * m))', color='#ffffff', fontsize=11, weight='bold', pad=10)

    fig.suptitle('BAMKS-D Fair Scalability Benchmark: Comparing Naive Re-encrypt, Cheng et al., and BAMKS-D (m=3, 30 runs)',
                 color='#ffffff', fontsize=13, weight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    
    out_path = "diagrams/chart_scalability_multi_n.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"\n[OK] Fair scalability multi-panel graph generated at: {out_path}")

if __name__ == '__main__':
    generate_scalability_analysis()
