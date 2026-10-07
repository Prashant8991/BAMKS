import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

os.makedirs("diagrams", exist_ok=True)

# -----------------------------------------------------------------------------
# 1. Architecture Flowchart Diagram
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.axis('off')
fig.patch.set_facecolor('#0f172a')

# Boxes
colors = {'hosp': '#10b981', 'cloud': '#0284c7', 'bc': '#e11d48', 'doc': '#8b5cf6'}

# Hospital Box
box1 = patches.FancyBboxPatch((0.5, 4.2), 2.6, 2.2, boxstyle="round,pad=0.1", fc='#1e293b', ec=colors['hosp'], lw=2.5)
ax.add_patch(box1)
ax.text(1.8, 6.0, "Hospital (Data Owner)", color='#ffffff', weight='bold', fontsize=12, ha='center')
ax.text(1.8, 5.2, "• Plaintext EHR Record\n• AES-256-GCM Encryption\n• Tag y_k = g^σ_k mod P\n• Index Tokens g^(η*H1(kw))", color='#cbd5e1', fontsize=9, ha='center')

# Cloud Box
box2 = patches.FancyBboxPatch((4.7, 4.2), 2.6, 2.2, boxstyle="round,pad=0.1", fc='#1e293b', ec=colors['cloud'], lw=2.5)
ax.add_patch(box2)
ax.text(6.0, 6.0, "Cloud Storage (Off-Chain)", color='#ffffff', weight='bold', fontsize=12, ha='center')
ax.text(6.0, 5.2, "• Encrypted AES Payload\n• 96-bit Nonce & 128-bit Tag\n• Inverted Keyword Index\n• Untrusted Storage", color='#cbd5e1', fontsize=9, ha='center')

# Blockchain Box
box3 = patches.FancyBboxPatch((4.7, 0.8), 2.6, 2.2, boxstyle="round,pad=0.1", fc='#1e293b', ec=colors['bc'], lw=2.5)
ax.add_patch(box3)
ax.text(6.0, 2.6, "Ethereum Smart Contract", color='#ffffff', weight='bold', fontsize=12, ha='center')
ax.text(6.0, 1.8, "• BAMKS_Registry.sol\n• deletedDocRegistry[docId]\n• Tag y_k Verification\n• O(1) Instant Revocation", color='#cbd5e1', fontsize=9, ha='center')

# Doctor Box
box4 = patches.FancyBboxPatch((8.9, 4.2), 2.6, 2.2, boxstyle="round,pad=0.1", fc='#1e293b', ec=colors['doc'], lw=2.5)
ax.add_patch(box4)
ax.text(10.2, 6.0, "Doctor (Data User)", color='#ffffff', weight='bold', fontsize=12, ha='center')
ax.text(10.2, 5.2, "• CP-ABE Attribute Key\n• Trapdoors (T1, T2, T3)\n• Decrypts if Policy Matches\n• SNIZK Proof Check", color='#cbd5e1', fontsize=9, ha='center')

# Arrows
ax.annotate("", xy=(4.6, 5.3), xytext=(3.2, 5.3), arrowprops=dict(arrowstyle="->", color='#38bdf8', lw=2.5))
ax.text(3.9, 5.5, "1. Upload Payload", color='#38bdf8', fontsize=8.5, ha='center', weight='bold')

ax.annotate("", xy=(4.6, 1.9), xytext=(1.8, 4.1), arrowprops=dict(arrowstyle="->", color='#f43f5e', lw=2.5))
ax.text(2.9, 2.8, "2. Register y_k & Status", color='#f43f5e', fontsize=8.5, ha='center', weight='bold')

ax.annotate("", xy=(8.8, 5.3), xytext=(7.4, 5.3), arrowprops=dict(arrowstyle="->", color='#a78bfa', lw=2.5))
ax.text(8.1, 5.5, "3. Trapdoor Query", color='#a78bfa', fontsize=8.5, ha='center', weight='bold')

ax.annotate("", xy=(7.4, 1.9), xytext=(8.8, 4.1), arrowprops=dict(arrowstyle="->", color='#34d399', lw=2.5))
ax.text(8.3, 2.8, "4. Verify Status O(1)", color='#34d399', fontsize=8.5, ha='center', weight='bold')

plt.title("BAMKS-D System Architecture & Interaction Flow", color='#ffffff', fontsize=15, pad=15, weight='bold')
plt.tight_layout()
plt.savefig("diagrams/diagram_architecture.png", dpi=300)
plt.close()

# -----------------------------------------------------------------------------
# 2. Performance Bar Chart Comparison
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
fig.patch.set_facecolor('#0f172a')
ax.set_facecolor('#1e293b')

categories = ['Full Re-keying\n(Base Paper)', 'SingleDocAdd\n(Our Work)', 'SingleDocDelete\n(Our Work)']
times = [5560.0, 0.12, 0.001]
bar_colors = ['#f43f5e', '#38bdf8', '#34d399']

bars = ax.bar(categories, times, color=bar_colors, width=0.55, edgecolor='#ffffff', linewidth=1)
ax.set_yscale('log')
ax.set_ylabel('Execution Time in ms (Log Scale)', color='#ffffff', fontsize=11, weight='bold')
ax.set_title('Latency Comparison: Base Paper O(L x m) vs. Our BAMKS-D O(1)', color='#ffffff', fontsize=13, weight='bold', pad=15)
ax.tick_params(colors='#ffffff', labelsize=10)
ax.grid(True, which="both", ls="--", lw=0.5, color='#334155')

for bar in bars:
    yval = bar.get_height()
    txt = f"{yval:.3f} ms" if yval < 1 else f"{yval:,.0f} ms"
    ax.text(bar.get_x() + bar.get_width()/2.0, yval * 1.5, txt, ha='center', va='bottom', color='#ffffff', weight='bold', fontsize=10)

plt.tight_layout()
plt.savefig("diagrams/chart_performance.png", dpi=300)
plt.close()

print("[OK] All diagram images generated successfully in diagrams/ folder.")
