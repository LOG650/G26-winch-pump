"""Figurer for kapittel 6 Modellering i 005 report/Prosjektrapport.md.

Kjor: uv run python "3.3 gap-deteksjon/figures.py"
Output: fig_*.png i samme mappe.
"""
import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    'font.size': 10,
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})


def box(ax, y, label, color, text_color='white', height=1.0, x=2, w=8):
    rect = FancyBboxPatch(
        (x, y), w, height,
        boxstyle='round,pad=0.08',
        facecolor=color, edgecolor='#2c3e50', linewidth=1.5
    )
    ax.add_patch(rect)
    ax.text(x + w / 2, y + height / 2, label, ha='center', va='center',
            fontsize=10, color=text_color, fontweight='bold')


def arrow_down(ax, y_top, y_bot, x=6):
    ax.annotate('', xy=(x, y_bot), xytext=(x, y_top),
                arrowprops=dict(arrowstyle='->', color='#2c3e50', lw=1.5))


# ============================================================
# Figur 6.1: Modellens arkitektur (vertikalt flytdiagram)
# ============================================================
fig, ax = plt.subplots(figsize=(8.5, 10))
ax.set_xlim(0, 12)
ax.set_ylim(-0.5, 13)
ax.axis('off')

# (y, label, color, text_color)
nodes = [
    (11.5, 'Snapshot-CSV uke $t$ og $t-1$\n(fra 004 data/<dato>_motive_baseline/)', '#bdc3c7', 'black'),
    (9.6,  'Forhåndsfiltering\n(eksklusjonsliste, sumsjekk mot Tier 1)', '#3498db', 'white'),
    (7.7,  'Statisk gap-deteksjon\n($G < 0$ + magnitudeklassifisering)', '#e67e22', 'white'),
    (5.8,  'Dynamisk endringsdeteksjon\n(nytt / forverret / forbedret / løst / uendret gap)', '#e67e22', 'white'),
    (3.9,  'Suppression-regler\n(strukturelt vedvarende underskudd)', '#9b59b6', 'white'),
    (2.0,  'Varselsutløsing\n(rute til mottaker via 3.4)', '#27ae60', 'white'),
]

for y, label, color, text_color in nodes:
    box(ax, y, label, color, text_color=text_color)

# arrows: from bottom of node i to top of node i+1
for i in range(len(nodes) - 1):
    y_top = nodes[i][0]                      # bottom of upper box (y of placement)
    y_bot = nodes[i + 1][0] + 1.0            # top of lower box (y + height)
    arrow_down(ax, y_top, y_bot)

# Side-label that the two detection rules run on the same input
ax.annotate(
    'Begge deteksjonsregler\nopererer på samme\nfilterte snapshot',
    xy=(10.2, 6.8), xytext=(10.5, 7.2),
    fontsize=8, style='italic', color='#7f8c8d',
    ha='left', va='center'
)

ax.set_title('Modellens arkitektur', fontsize=12, fontweight='bold', pad=10)

plt.tight_layout()
fig.savefig(os.path.join(SCRIPT_DIR, 'fig_modell_arkitektur.png'))
plt.close(fig)

print(f'Skrev fig_modell_arkitektur.png til {SCRIPT_DIR}')


# ============================================================
# Figur 6.2: Endringstype i (G_prev, G_curr)-fasen
# ============================================================
fig, ax = plt.subplots(figsize=(8.5, 8))

XMIN, XMAX = -8, 3
YMIN, YMAX = -8, 3

# Q1: top-right (begge >= 0) - Ingen endring
ax.fill_between([0, XMAX], 0, YMAX, color='#ecf0f1', alpha=0.7)
# Q2: top-left (forrige < 0, naa >= 0) - Loest
ax.fill_between([XMIN, 0], 0, YMAX, color='#27ae60', alpha=0.30)
# Q4: bottom-right (forrige >= 0, naa < 0) - Nytt
ax.fill_between([0, XMAX], YMIN, 0, color='#e67e22', alpha=0.30)

# Q3 below diagonal (Forverret)
ax.fill([XMIN, 0, 0], [XMIN, 0, YMIN], color='#c0392b', alpha=0.30)
# Q3 above diagonal (Forbedret)
ax.fill([XMIN, 0, XMIN], [XMIN, 0, 0], color='#f39c12', alpha=0.30)

# Diagonal (y = x), Uendret-linje
ax.plot([XMIN, 0], [XMIN, 0], color='#2c3e50', lw=2, linestyle='--')

# Axes
ax.axhline(0, color='black', lw=1.2)
ax.axvline(0, color='black', lw=1.2)

# Region labels
ax.text(1.5, 1.5, 'Ingen endring\n(begge $\\geq 0$)',
        ha='center', va='center', fontsize=10, color='#7f8c8d')
ax.text(-4, 1.5, 'Løst', ha='center', va='center',
        fontsize=14, fontweight='bold', color='#196f3d')
ax.text(1.5, -4, 'Nytt gap', ha='center', va='center',
        fontsize=14, fontweight='bold', color='#a04000')
ax.text(-1.8, -5.5, 'Forverret', ha='center', va='center',
        fontsize=13, fontweight='bold', color='#922b21')
ax.text(-5.5, -1.8, 'Forbedret', ha='center', va='center',
        fontsize=13, fontweight='bold', color='#9a7d0a')
ax.annotate('Uendret\n(på diagonalen)', xy=(-3, -3), xytext=(-7.3, -7.3),
            fontsize=9, fontweight='bold', color='#2c3e50',
            arrowprops=dict(arrowstyle='->', color='#2c3e50', lw=1))

# Example points to anchor intuition
examples = [
    (-1, -3, 'forverret: −1 → −3'),
    (-5, -2, 'forbedret: −5 → −2'),
    (0, -2, 'nytt: 0 → −2'),
    (-2, 1, 'løst: −2 → 1'),
]
for x, y, lbl in examples:
    ax.scatter(x, y, s=60, color='#2c3e50', zorder=5, edgecolors='white', linewidths=1.5)

ax.set_xlim(XMIN, XMAX)
ax.set_ylim(YMIN, YMAX)
ax.set_xlabel(r'$G_{r,a,t}^{(s_{i-1})}$  (forrige snapshot)', fontsize=11)
ax.set_ylabel(r'$G_{r,a,t}^{(s_i)}$  (nåværende snapshot)', fontsize=11)
ax.set_title('Klassifisering av cellevise endringer mellom to snapshots',
             fontsize=12, fontweight='bold', pad=10)
ax.grid(True, alpha=0.25, linestyle=':')
ax.set_aspect('equal')

plt.tight_layout()
fig.savefig(os.path.join(SCRIPT_DIR, 'fig_endringstype_fase.png'))
plt.close(fig)

print(f'Skrev fig_endringstype_fase.png til {SCRIPT_DIR}')
