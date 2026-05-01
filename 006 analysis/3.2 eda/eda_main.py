"""3.2 EDA - Eksplorativ dataanalyse av snapshot 2026-04-30.

Genererer figurer og tabeller for kapitlene 4.7 (Casebeskrivelse) og 7 (Analyse)
i 005 report/Prosjektrapport.md. Output: fig_*.png og tab_*.md i denne mappen.

Kjor: uv run python "3.2 eda/eda_main.py"
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
CAL_CSV = os.path.join(PROJECT_ROOT, '004 data', '2026-04-30_motive_baseline', 'clean',
                       '2026-04-30_supply_demand_motive_alle_75pct.csv')
OV_CSV = os.path.join(PROJECT_ROOT, '004 data', '2026-04-30_motive_baseline', 'clean',
                      '2026-04-30_supply_demand_overview_motive_alle_75pct.csv')
OUT = SCRIPT_DIR

cal = pd.read_csv(CAL_CSV, parse_dates=['snapshot_date', 'week_start'])
ov = pd.read_csv(OV_CSV, parse_dates=['snapshot_date'])
ov['month_dt'] = pd.to_datetime(ov['month'] + '-01')

plt.rcParams.update({
    'font.size': 10,
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})

print(f'Calendar: {len(cal)} rader, {cal["asset_tier2"].nunique()} assets, '
      f'{cal["week_start"].nunique()} uker')
print(f'Overview: {len(ov)} rader, {ov["asset_tier1"].nunique()} kategorier, '
      f'{ov["month"].nunique()} maaneder')


def write_table(df, path, caption):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(df.to_markdown(index=False))
        f.write(f'\n\n*{caption}*\n')


# ============================================================
# Figur 1: Distribusjon av gap_value
# ============================================================
fig, ax = plt.subplots(figsize=(10, 5))
bins = np.arange(cal['gap_value'].min() - 0.5, cal['gap_value'].max() + 1.5, 1)
ax.hist(cal[cal['gap_value'] < 0]['gap_value'], bins=bins, color='#c0392b',
        edgecolor='white', label='Gap (negativ)')
ax.hist(cal[cal['gap_value'] == 0]['gap_value'], bins=bins, color='#bdc3c7',
        edgecolor='white', label='Balanse (0)')
ax.hist(cal[cal['gap_value'] > 0]['gap_value'], bins=bins, color='#27ae60',
        edgecolor='white', label='Overskudd (positiv)')
ax.set_xlabel('Gap-verdi (supply minus demand)')
ax.set_ylabel('Antall celler')
ax.set_title(f'Distribusjon av gap_value (n = {len(cal)} celler)')
ax.legend(loc='upper left')
ax.axvline(0, color='black', lw=0.8, alpha=0.5)
plt.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_gap_distribusjon.png'))
plt.close(fig)

neg = (cal['gap_value'] < 0).sum()
zero = (cal['gap_value'] == 0).sum()
pos = (cal['gap_value'] > 0).sum()
print(f'\nGap-distribusjon:')
print(f'  Negativ:  {neg:5d} ({neg / len(cal) * 100:5.1f} %)')
print(f'  Null:     {zero:5d} ({zero / len(cal) * 100:5.1f} %)')
print(f'  Positiv:  {pos:5d} ({pos / len(cal) * 100:5.1f} %)')
print(f'  Median:   {cal["gap_value"].median()}')
print(f'  P5:       {cal["gap_value"].quantile(0.05)}')

# ============================================================
# Figur 2: Total gap per uke over tid
# ============================================================
weekly = cal.groupby('week_start')['gap_value'].sum().reset_index()
fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(weekly['week_start'], weekly['gap_value'], marker='o', color='#2c3e50',
        lw=2, ms=4)
ax.fill_between(weekly['week_start'], weekly['gap_value'], 0,
                where=weekly['gap_value'] < 0, color='#c0392b', alpha=0.2,
                interpolate=True)
ax.fill_between(weekly['week_start'], weekly['gap_value'], 0,
                where=weekly['gap_value'] >= 0, color='#27ae60', alpha=0.2,
                interpolate=True)
ax.axhline(0, color='black', lw=0.8)
ax.set_xlabel('Uke (mandag)')
ax.set_ylabel('Sum gap-verdi (unit-uker)')
ax.set_title('Totalt synlig gap per uke (snapshot 2026-04-30)')
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
fig.autofmt_xdate()
plt.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_total_gap_per_uke.png'))
plt.close(fig)

# ============================================================
# Figur 3: Heatmap - topp 30 verste assets x uker
# ============================================================
asset_total = cal.groupby('asset_tier2')['gap_value'].sum().sort_values()
worst_30 = asset_total.head(30).index.tolist()
pivot = (cal[cal['asset_tier2'].isin(worst_30)]
         .pivot_table(index='asset_tier2', columns='week_start', values='gap_value')
         .reindex(worst_30))

fig, ax = plt.subplots(figsize=(14, 9))
vmax = max(abs(pivot.min().min()), abs(pivot.max().max()))
im = ax.imshow(pivot.values, aspect='auto', cmap='RdYlGn',
               vmin=-vmax, vmax=vmax, interpolation='none')
ax.set_yticks(range(len(pivot.index)))
ax.set_yticklabels([s if len(s) <= 50 else s[:47] + '...' for s in pivot.index],
                   fontsize=8)
xticks = range(0, len(pivot.columns), 4)
ax.set_xticks(list(xticks))
ax.set_xticklabels([pivot.columns[i].strftime('%d.%m.%Y') for i in xticks],
                   rotation=45, ha='right', fontsize=8)
ax.set_xlabel('Uke (mandag)')
ax.set_title('Heatmap: gap-verdi per uke for de 30 utstyrsenhetene med stoerst kumulativt underskudd')
cbar = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.02)
cbar.set_label('Gap-verdi')
plt.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_gap_heatmap_topp30.png'))
plt.close(fig)

# ============================================================
# Figur 4: Topp 10 verste assets (kumulativt gap)
# ============================================================
top10 = asset_total.head(10)
fig, ax = plt.subplots(figsize=(10, 5.5))
y = np.arange(len(top10))
ax.barh(y, top10.values, color='#c0392b', edgecolor='white')
ax.set_yticks(y)
ax.set_yticklabels([s if len(s) <= 50 else s[:47] + '...' for s in top10.index],
                   fontsize=9)
ax.set_xlabel('Kumulativ gap-verdi over 36 uker')
ax.set_title('Topp 10 utstyrsenheter med stoerst kumulativt underskudd')
ax.invert_yaxis()
for i, v in enumerate(top10.values):
    ax.text(v - 1, i, f'{int(v)}', va='center', ha='right', color='white',
            fontsize=9, fontweight='bold')
plt.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_topp10_verste_assets.png'))
plt.close(fig)

# ============================================================
# Figur 5: Per Tier 1-gruppe over tid
# ============================================================
group_weekly = cal.groupby(['week_start', 'asset_tier1'])['gap_value'].sum().reset_index()
fig, ax = plt.subplots(figsize=(11, 6))
for tier1 in sorted(cal['asset_tier1'].unique()):
    sub = group_weekly[group_weekly['asset_tier1'] == tier1]
    ax.plot(sub['week_start'], sub['gap_value'], marker='o', ms=3, lw=1.5,
            label=tier1)
ax.axhline(0, color='black', lw=0.8)
ax.set_xlabel('Uke (mandag)')
ax.set_ylabel('Sum gap-verdi')
ax.set_title('Gap-utvikling per Tier 1-kategori')
ax.legend(loc='lower right', fontsize=8, ncol=2)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
fig.autofmt_xdate()
plt.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_per_tier1_uker.png'))
plt.close(fig)

# ============================================================
# Figur 6: Overview - demand vs reservations per maaned
# ============================================================
ov_total = ov.groupby('month_dt')[['demand', 'reservations_per_av']].sum().reset_index()
fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(ov_total['month_dt'], ov_total['demand'], marker='o', lw=2, ms=8,
        color='#c0392b', label='Demand (synlig 75 %+)')
ax.plot(ov_total['month_dt'], ov_total['reservations_per_av'], marker='s', lw=2, ms=8,
        color='#2980b9', label='Reservations (Asset Voice)')
ax.fill_between(ov_total['month_dt'], ov_total['demand'], ov_total['reservations_per_av'],
                color='#e67e22', alpha=0.2, label='Reservation-gap')
ax.set_xlabel('Maaned')
ax.set_ylabel('Unit-uker')
ax.set_title('Demand vs reservations per maaned (snapshot 2026-04-30)')
ax.legend(loc='upper right')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
fig.autofmt_xdate()
plt.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_demand_vs_reservations_maanedlig.png'))
plt.close(fig)

# ============================================================
# Tabell 1: Strukturelle gaps (alltid negativ over alle 36 uker)
# ============================================================
asset_stats = cal.groupby('asset_tier2').agg(
    asset_tier1=('asset_tier1', 'first'),
    min_gap=('gap_value', 'min'),
    max_gap=('gap_value', 'max'),
    snitt_gap=('gap_value', 'mean'),
    sum_gap=('gap_value', 'sum'),
).reset_index()
strukturelle = asset_stats[asset_stats['max_gap'] < 0].copy()
strukturelle['snitt_gap'] = strukturelle['snitt_gap'].round(2)
strukturelle = strukturelle.sort_values('snitt_gap')
write_table(
    strukturelle[['asset_tier1', 'asset_tier2', 'min_gap', 'max_gap', 'snitt_gap', 'sum_gap']],
    os.path.join(OUT, 'tab_strukturelle_gaps.md'),
    'Tabell - utstyrsenheter med negativ gap-verdi i alle 36 uker av snapshot 2026-04-30 '
    '(strukturelle underskudd, ikke kontraktsdrevne nye gap).'
)
print(f'\nStrukturelle gaps (alltid negativ): {len(strukturelle)}')

# ============================================================
# Tabell 2: Topp 10 verste assets
# ============================================================
top10_table = top10.reset_index()
top10_table.columns = ['asset_tier2', 'kumulativ_gap']
top10_table = top10_table.merge(
    cal[['asset_tier2', 'asset_tier1']].drop_duplicates(),
    on='asset_tier2'
)[['asset_tier1', 'asset_tier2', 'kumulativ_gap']]
write_table(
    top10_table,
    os.path.join(OUT, 'tab_topp10_verste_assets.md'),
    'Tabell - topp 10 utstyrsenheter med stoerst kumulativt underskudd over '
    'snapshot-perioden (2026-05-04 til 2027-01-04).'
)

# ============================================================
# Tabell 3: Zero-gap assets (alltid 0)
# ============================================================
zero_assets = asset_stats[(asset_stats['min_gap'] == 0) & (asset_stats['max_gap'] == 0)]
write_table(
    zero_assets[['asset_tier1', 'asset_tier2']],
    os.path.join(OUT, 'tab_zero_gap_assets.md'),
    'Tabell - utstyrsenheter med gap-verdi 0 i alle 36 uker. '
    'Kandidater for eksklusjon fra gap-deteksjonen.'
)
print(f'Zero-gap assets (alltid 0): {len(zero_assets)}')

# ============================================================
# Sammendrag
# ============================================================
print('\nFiler skrevet til ' + OUT + ':')
for f in sorted(os.listdir(OUT)):
    if f.startswith(('fig_', 'tab_')):
        path = os.path.join(OUT, f)
        size_kb = os.path.getsize(path) / 1024
        print(f'  {f:50s} ({size_kb:6.1f} KB)')
