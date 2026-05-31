"""Transkriberer Power BI-skjermbilder for snapshot 2026-05-14 til CSV i
004 data/2026-05-14_motive_no/clean/.

Inneholder raadata inline (gap_value + severity_band per celle). Gitignored.

Kjoer: uv run python "3.1 datainnhenting/_transcribe_2026-05-14.py"
"""
import csv
import os
from collections import defaultdict

SNAPSHOT = '2026-05-14'
CUSTODIAN = 'Motive AS'
PROJECT_OWNER = 'Motive AS'
REGION = 'Motive Norway'
PROB = 75

# 33 uker: 18 fra PNG 1 (18.05 - 14.09) + 15 fra PNG 2 (21.09 - 28.12)
WEEKS = [
    '2026-05-18', '2026-05-25', '2026-06-01', '2026-06-08', '2026-06-15',
    '2026-06-22', '2026-06-29', '2026-07-06', '2026-07-13', '2026-07-20',
    '2026-07-27', '2026-08-03', '2026-08-10', '2026-08-17', '2026-08-24',
    '2026-08-31', '2026-09-07', '2026-09-14',
    '2026-09-21', '2026-09-28', '2026-10-05', '2026-10-12', '2026-10-19',
    '2026-10-26', '2026-11-02', '2026-11-09', '2026-11-16', '2026-11-23',
    '2026-11-30', '2026-12-07', '2026-12-14', '2026-12-21', '2026-12-28',
]

# Hver rad: (asset_type, asset_tier2, [gap_value per uke], [severity_band per uke])
# Severity-band: 'green', 'yellow', 'red', 'purple', 'black'
G = 'green'
Y = 'yellow'
R = 'red'
P = 'purple'
B = 'black'

ASSETS = [
    # ----- Winch -----
    ('Winch', 'Hydraulic - Wide|35Te Wide Drum Winch - 35Te Wide Drum Winch',
     [-2,-2,-2,-2,-2,-2,-2,-2,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*9 + [G]*9 + [G]*15),

    ('Winch', 'Hydraulic - Wide|20Te Wide Drum Winch - 20Te Wide Drum Winch',
     [ 4, 4, 3, 3, 3, 3, 3, 2, 2, 4, 4, 4, 5, 5, 5, 5, 5, 5,
       5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
     [G]*33),

    ('Winch', 'Hydraulic - Narr|20Te Narrow Drum Winch - 20Te Narrow Drum Winch',
     [ 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 3, 4, 4, 4, 4,
       4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
     [G]*33),

    ('Winch', 'Hydraulic - 5Te Brevini Winch',
     [1]*33, [G]*33),

    # ----- Under rollers -----
    ('Under rollers', '- 60Te Crane Loaded Underrollers',
     [1]*33, [G]*33),

    # ----- Tensioner -----
    ('Tensioner', 'Horizontal - 4 track - 50Te Tensioner - 4 Track',
     [-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*8 + [G]*10 + [G]*15),

    ('Tensioner', 'Horizontal - 2 track - 15Te Horizontal Tensioner',
     [-1,-1,-1,-1,-1,-1,-2,-2,-2,-1,-1,-1, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*12 + [G]*6 + [G]*15),

    # ----- Spoolers -----
    ('Spoolers', 'Pneumatic - 6Te Air Spooler',
     [4]*33, [G]*33),

    ('Spoolers', 'Electric - 75Te Electric Spooler',
     [ 2, 2, 2, 1, 1, 0, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1,
       1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
     [G]*5 + [P] + [G]*12 + [G]*15),

    # ----- RDS -----
    ('RDS', '- 500Te RDS',
     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*18 + [G]*15),

    ('RDS', '- 150Te RDS',
     [-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*8 + [G]*10 + [G]*15),

    # ----- LMA machines -----
    ('LMA machines', 'LMA - LMA300 MRT Machine',
     [1]*33, [G]*33),

    # ----- HPUS -----
    ('HPUS', 'Electric - 90KW Electric HPU',
     [-2,-1,-1,-1,-1,-1,-1,-1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [B]*8 + [P] + [G]*9 + [G]*15),

    ('HPUS', 'Electric - 55kW Electric HPU - Zone 1',
     [ 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3,
       3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
     [G]*33),

    ('HPUS', 'Electric - 55kW Electric HPU',
     [ 0, 0, 0, 0, 0, 0, 0, 0,-2,-2, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
     [P]*8 + [B]*2 + [P]*8 + [P]*3 + [G]*12),

    ('HPUS', 'Electric - 37kW Electric HPU',
     [ 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
     [G]*33),

    ('HPUS', 'Electric - 30kW Electric HPU',
     [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
     [P]*9 + [G]*9 + [G]*4 + [G]*11),

    ('HPUS', 'Electric - 18.5kW Electric HPU',
     [1]*33, [G]*33),

    ('HPUS', 'Electric - 158KW Electric HPU',
     [-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*9 + [G]*9 + [G]*15),

    ('HPUS', 'Electric - 11kW Electric HPU',
     [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [P]*18 + [P]*4 + [G]*11),

    ('HPUS', 'Electric - 1.5kW Electric HPU',
     [1]*33, [G]*33),

    ('HPUS', 'Diesel - 63kW Diesel HPU Zone II',
     [0]*33, [P]*33),

    ('HPUS', 'Diesel - 63kW Diesel HPU',
     [1]*33, [G]*33),

    # ----- Cable Pulling machine -----
    ('Cable Pulling machine', '- 2Te Linear Cable Engine',
     [ 0, 0, 0,-2,-2,-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [G]*3 + [B]*3 + [G]*12 + [G]*15),
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
OUT_PATH = os.path.join(
    PROJECT_ROOT, '004 data', '2026-05-14_motive_no', 'clean',
    '2026-05-14_supply_demand_motive_no_75pct.csv'
)

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

rows = []
for asset_type, asset_tier2, values, severities in ASSETS:
    assert len(values) == len(WEEKS), f'{asset_tier2}: {len(values)} verdier, forventet {len(WEEKS)}'
    assert len(severities) == len(WEEKS), f'{asset_tier2}: {len(severities)} farger, forventet {len(WEEKS)}'
    for week, val, sev in zip(WEEKS, values, severities):
        rows.append({
            'snapshot_date': SNAPSHOT,
            'week_start': week,
            'asset_type': asset_type,
            'asset_tier2': asset_tier2,
            'gap_value': val,
            'severity_band': sev,
            'custodian': CUSTODIAN,
            'project_owner_demand': PROJECT_OWNER,
            'region': REGION,
            'probability_threshold': PROB,
        })

with open(OUT_PATH, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'snapshot_date', 'week_start', 'asset_type', 'asset_tier2',
        'gap_value', 'severity_band', 'custodian', 'project_owner_demand',
        'region', 'probability_threshold'
    ])
    writer.writeheader()
    writer.writerows(rows)

print(f'Skrev {len(rows)} rader til:\n  {OUT_PATH}')

# Sum-sjekk mot Totalt-raden fra PNG-ene
EXPECTED_TOTAL = {
    # PNG 1
    '2026-05-18': 14, '2026-05-25': 16, '2026-06-01': 14, '2026-06-08': 11,
    '2026-06-15': 11, '2026-06-22': 10, '2026-06-29': 12, '2026-07-06':  8,
    '2026-07-13': 13, '2026-07-20': 20, '2026-07-27': 21, '2026-08-03': 20,
    '2026-08-10': 23, '2026-08-17': 24, '2026-08-24': 26, '2026-08-31': 26,
    '2026-09-07': 27, '2026-09-14': 27,
    # PNG 2
    '2026-09-21': 27, '2026-09-28': 27, '2026-10-05': 28, '2026-10-12': 32,
    '2026-10-19': 34, '2026-10-26': 34, '2026-11-02': 34, '2026-11-09': 34,
    '2026-11-16': 34, '2026-11-23': 34, '2026-11-30': 34, '2026-12-07': 34,
    '2026-12-14': 34, '2026-12-21': 34, '2026-12-28': 34,
}

weekly_total: dict[str, int] = defaultdict(int)
for r in rows:
    weekly_total[r['week_start']] += r['gap_value']

# Totalt-sjekken aksepterer +/-2 som avrundingsstoy (jf. tab_kolonner.md).
# Power BI viser cellene som avrundede heltall mens Totalt aggregeres fra
# underliggende desimaler, saa leaf-sum kan avvike med +/-1-2 per uke.
errors = 0
warnings = 0
for week, exp in EXPECTED_TOTAL.items():
    got = weekly_total[week]
    diff = got - exp
    if abs(diff) > 2:
        print(f'  FEIL {week}: leaf-sum={got}, Totalt={exp} (diff={diff:+d})')
        errors += 1
    elif diff != 0:
        print(f'  info {week}: leaf-sum={got}, Totalt={exp} '
              f'(diff={diff:+d}, innenfor +/-2 avrundingsstoy)')
        warnings += 1

if errors == 0:
    print(f'Sum-sjekk OK: alle 33 uker innen +/-2 fra Totalt-raden '
          f'({warnings} med liten avrundingsstoy, 0 transkriberingsfeil).')
else:
    print(f'{errors} uker har avvik > 2 - mistanke om transkriberingsfeil.')

# Asset-type-aggregert sjekk (Tier 1-rader fra PNG-ene)
ASSET_TYPE_TOTAL = {
    'Winch': [7,7,6,6,6,6,6,4,5,8,8,7,8,9,10,10,10,10,
              10,10,10,12,12,12,12,12,12,12,12,12,12,12,12],
    'Under rollers': [1]*33,
    'Tensioner': [-2,-2,-2,-2,-2,-2,-3,-3,-2,-1,-1,-1,0,0,0,0,0,0] + [0]*15,
    'Spoolers': [6,6,6,5,5,4,5,5,5,5,6,6,6,6,5,5,5,5,
                 5,5,6,6,6,6,6,6,6,6,6,6,6,6,6],
    'RDS': [-2]*8 + [-1]*10 + [0]*15,
    'LMA machines': [1]*33,
    'HPUS': [3,5,4,4,4,4,4,2,4,7,7,7,8,8,10,10,10,10,
             10,10,10,12,14,14,14,14,14,14,14,14,14,14,14],
    'Cable Pulling machine': [0,0,0,-2,-2,-2,0,0,0,0,0,0,0,0,0,0,0,0] + [0]*15,
}

at_weekly: dict[tuple[str, str], int] = defaultdict(int)
for r in rows:
    at_weekly[(r['asset_type'], r['week_start'])] += r['gap_value']

at_errors = 0
for at, expected_per_week in ASSET_TYPE_TOTAL.items():
    for i, week in enumerate(WEEKS):
        got = at_weekly[(at, week)]
        exp = expected_per_week[i]
        diff = got - exp
        if abs(diff) > 2:
            print(f'  TIER1-FEIL {at:25s} {week}: leaf-sum={got}, '
                  f'Tier1={exp} (diff={diff:+d}, tolererer +/-2 for avrundingsstoy)')
            at_errors += 1

if at_errors == 0:
    print('Tier 1-sjekk OK: alle asset type-summer innen +/-2 fra Power BI.')
else:
    print(f'{at_errors} (asset-type, uke)-par har avvik > 2.')
