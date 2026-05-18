"""3.3 Gap-deteksjon - uke-til-uke-sammenligning av to snapshots.

Sammenligner baseline (snapshot 1, 2026-05-07) med snapshot 2 (2026-05-14) og
klassifiserer hver (asset, uke)-celle i endringstype basert paa gap_value og
severity_band. Genererer logg og oppsummering.

Kjor: uv run python "3.3 gap-deteksjon/gap_detection.py"
"""
import os
from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
SNAP1_CSV = os.path.join(PROJECT_ROOT, '004 data', '2026-05-07_motive_no',
                         'clean', '2026-05-07_supply_demand_motive_no_75pct.csv')
SNAP2_CSV = os.path.join(PROJECT_ROOT, '004 data', '2026-05-14_motive_no',
                         'clean', '2026-05-14_supply_demand_motive_no_75pct.csv')
OUT = SCRIPT_DIR

plt.rcParams.update({
    'font.size': 10,
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})

# ============================================================
# Last data
# ============================================================
snap1 = pd.read_csv(SNAP1_CSV, parse_dates=['snapshot_date', 'week_start'])
snap2 = pd.read_csv(SNAP2_CSV, parse_dates=['snapshot_date', 'week_start'])

print(f'Snapshot 1 ({snap1["snapshot_date"].iloc[0].date()}): '
      f'{len(snap1)} rader, {snap1["week_start"].nunique()} uker')
print(f'Snapshot 2 ({snap2["snapshot_date"].iloc[0].date()}): '
      f'{len(snap2)} rader, {snap2["week_start"].nunique()} uker')

# ============================================================
# Merge paa (asset_tier2, week_start) - kun overlappende uker
# ============================================================
key_cols = ['asset_type', 'asset_tier2', 'week_start']
merged = snap1[key_cols + ['gap_value', 'severity_band']].merge(
    snap2[key_cols + ['gap_value', 'severity_band']],
    on=key_cols, how='inner', suffixes=('_t1', '_t2')
)
print(f'\nOverlappende celler: {len(merged)} '
      f'({merged["week_start"].nunique()} uker x '
      f'{merged["asset_tier2"].nunique()} assets)')


# ============================================================
# Klassifiser endring
# ============================================================
def classify_gap_change(g1: int, g2: int) -> str:
    if g1 >= 0 and g2 >= 0:
        if g1 == g2:
            return 'STABIL'
        return 'POSITIV_ENDRING'
    if g1 >= 0 and g2 < 0:
        return 'NYTT_GAP'
    if g1 < 0 and g2 >= 0:
        return 'LOEST'
    # Begge negative
    if g1 == g2:
        return 'UENDRET_GAP'
    if g2 < g1:
        return 'FORVERRET'
    return 'FORBEDRET'


SEV_ORDER = {'black': 0, 'purple': 1, 'red': 2, 'yellow': 3, 'green': 4}


def classify_severity_change(s1: str, s2: str) -> str:
    if s1 == s2:
        return 'SAMME_FARGE'
    if SEV_ORDER[s2] > SEV_ORDER[s1]:
        return 'BEDRE_FARGE'
    return 'VERRE_FARGE'


merged['gap_delta'] = merged['gap_value_t2'] - merged['gap_value_t1']
merged['change_type'] = merged.apply(
    lambda r: classify_gap_change(r['gap_value_t1'], r['gap_value_t2']), axis=1
)
merged['severity_change'] = merged.apply(
    lambda r: classify_severity_change(r['severity_band_t1'], r['severity_band_t2']),
    axis=1,
)

# ============================================================
# Skriv full logg som CSV
# ============================================================
log_cols = [
    'week_start', 'asset_type', 'asset_tier2',
    'gap_value_t1', 'gap_value_t2', 'gap_delta',
    'severity_band_t1', 'severity_band_t2',
    'change_type', 'severity_change',
]
merged_sorted = merged[log_cols].sort_values(
    ['change_type', 'week_start', 'asset_tier2']
)
LOG_PATH = os.path.join(OUT, 'gap_changes.csv')
merged_sorted.to_csv(LOG_PATH, index=False)
print(f'\nFull logg skrevet til:\n  {LOG_PATH} ({len(merged_sorted)} rader)')

# ============================================================
# Oppsummering: antall per change_type
# ============================================================
ct_counts = merged['change_type'].value_counts()
print('\nFordeling av endringstype (gap_value):')
for ct in ['NYTT_GAP', 'FORVERRET', 'FORBEDRET', 'LOEST',
          'UENDRET_GAP', 'POSITIV_ENDRING', 'STABIL']:
    n = ct_counts.get(ct, 0)
    pct = n / len(merged) * 100
    print(f'  {ct:18s} {n:5d}  ({pct:5.1f} %)')

sev_counts = merged['severity_change'].value_counts()
print('\nFordeling av severity-endring:')
for sc in ['VERRE_FARGE', 'BEDRE_FARGE', 'SAMME_FARGE']:
    n = sev_counts.get(sc, 0)
    pct = n / len(merged) * 100
    print(f'  {sc:14s} {n:5d}  ({pct:5.1f} %)')

# ============================================================
# Interessante endringer (alt unntatt STABIL og UENDRET_GAP)
# ============================================================
interesting = merged[~merged['change_type'].isin(['STABIL', 'UENDRET_GAP'])]
print(f'\nInteressante endringer (krever oppfolging): {len(interesting)}')

# Lag tabell over alle "kritiske" endringer (NYTT_GAP og FORVERRET)
critical = merged[merged['change_type'].isin(['NYTT_GAP', 'FORVERRET'])].copy()
critical = critical.sort_values(['change_type', 'gap_delta', 'week_start'])


def write_table(df, path, caption):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(df.to_markdown(index=False))
        f.write(f'\n\n*{caption}*\n')


if len(critical) > 0:
    write_table(
        critical[['week_start', 'asset_type', 'asset_tier2',
                  'gap_value_t1', 'gap_value_t2', 'gap_delta',
                  'severity_band_t1', 'severity_band_t2']]
        .assign(week_start=critical['week_start'].dt.strftime('%Y-%m-%d')),
        os.path.join(OUT, 'tab_kritiske_endringer.md'),
        'Tabell - kritiske gap-endringer (NYTT_GAP og FORVERRET) mellom '
        'snapshot 2026-05-07 og 2026-05-14.'
    )
    print(f'\nKritiske endringer ({len(critical)}): se tab_kritiske_endringer.md')
else:
    print('\nIngen kritiske endringer (NYTT_GAP eller FORVERRET) denne uka.')

# Tilsvarende for positive endringer (LOEST og FORBEDRET)
positive = merged[merged['change_type'].isin(['LOEST', 'FORBEDRET'])].copy()
positive = positive.sort_values(['change_type', 'gap_delta', 'week_start'])

if len(positive) > 0:
    write_table(
        positive[['week_start', 'asset_type', 'asset_tier2',
                  'gap_value_t1', 'gap_value_t2', 'gap_delta',
                  'severity_band_t1', 'severity_band_t2']]
        .assign(week_start=positive['week_start'].dt.strftime('%Y-%m-%d')),
        os.path.join(OUT, 'tab_positive_endringer.md'),
        'Tabell - gap-forbedringer (LOEST og FORBEDRET) mellom '
        'snapshot 2026-05-07 og 2026-05-14.'
    )
    print(f'Positive endringer ({len(positive)}): se tab_positive_endringer.md')

# ============================================================
# Figur 1: Antall endringer per uke per type
# ============================================================
non_stable = merged[~merged['change_type'].isin(['STABIL', 'UENDRET_GAP'])]
weekly_changes = (non_stable.groupby(['week_start', 'change_type'])
                  .size().unstack(fill_value=0))

change_colors = {
    'NYTT_GAP':        '#c0392b',
    'FORVERRET':       '#e67e22',
    'FORBEDRET':       '#3498db',
    'LOEST':           '#27ae60',
    'POSITIV_ENDRING': '#95a5a6',
}
ordered = [c for c in ['NYTT_GAP', 'FORVERRET', 'POSITIV_ENDRING',
                       'FORBEDRET', 'LOEST']
           if c in weekly_changes.columns]
weekly_changes = weekly_changes[ordered]

fig, ax = plt.subplots(figsize=(11, 5))
bottom = pd.Series(0, index=weekly_changes.index)
for ct in ordered:
    ax.bar(weekly_changes.index, weekly_changes[ct], bottom=bottom,
           color=change_colors[ct], label=ct, width=5)
    bottom = bottom + weekly_changes[ct]
ax.set_xlabel('Uke (mandag)')
ax.set_ylabel('Antall (asset, uke)-celler')
ax.set_title('Endringer mellom snapshot 2026-05-07 og 2026-05-14 per uke '
             '(stabile celler ekskludert)')
ax.legend(loc='upper right', fontsize=9)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
fig.autofmt_xdate()
plt.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_endringer_per_uke.png'))
plt.close(fig)

# ============================================================
# Figur 2: Endringer per asset type
# ============================================================
asset_changes = (non_stable.groupby(['asset_type', 'change_type'])
                 .size().unstack(fill_value=0))
asset_changes = asset_changes.reindex(columns=ordered, fill_value=0)
asset_changes = asset_changes.loc[asset_changes.sum(axis=1).sort_values(ascending=False).index]

fig, ax = plt.subplots(figsize=(10, 5.5))
bottom = pd.Series(0, index=asset_changes.index)
for ct in ordered:
    ax.barh(asset_changes.index, asset_changes[ct], left=bottom,
            color=change_colors[ct], label=ct)
    bottom = bottom + asset_changes[ct]
ax.set_xlabel('Antall (asset, uke)-celler med endring')
ax.set_title('Endringer per asset type mellom snapshot 1 og 2')
ax.legend(loc='lower right', fontsize=9)
ax.invert_yaxis()
plt.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_endringer_per_asset_type.png'))
plt.close(fig)

# ============================================================
# Oppsummering pa konsollen
# ============================================================
print('\n' + '=' * 60)
print('OPPSUMMERING')
print('=' * 60)
print(f'  Totalt celler sammenlignet:        {len(merged):4d}')
print(f'  Stabile (ingen endring):           {ct_counts.get("STABIL", 0) + ct_counts.get("UENDRET_GAP", 0):4d}')
print(f'  Endringer som krever oppfolging:   {len(interesting):4d}')
print(f'    -> NYTT_GAP:                     {ct_counts.get("NYTT_GAP", 0):4d}')
print(f'    -> FORVERRET:                    {ct_counts.get("FORVERRET", 0):4d}')
print(f'    -> POSITIV_ENDRING:              {ct_counts.get("POSITIV_ENDRING", 0):4d}')
print(f'    -> FORBEDRET:                    {ct_counts.get("FORBEDRET", 0):4d}')
print(f'    -> LOEST:                        {ct_counts.get("LOEST", 0):4d}')
print(f'\n  Figurer/tabeller skrevet til: {OUT}')
