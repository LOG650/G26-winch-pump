"""Transkriberer Power BI-skjermbilder for snapshot 2026-05-21 til CSV i
004 data/2026-05-21_motive_no/clean/.

Inneholder raadata inline (gap_value + severity_band per celle). Gitignored.

Kjoer: uv run python "3.1 datainnhenting/_transcribe_2026-05-21.py"
"""
import csv
import os
from collections import defaultdict

SNAPSHOT = '2026-05-21'
CUSTODIAN = 'Motive AS'
PROJECT_OWNER = 'Motive AS'
REGION = 'Motive Norway'
PROB = 75

# 32 uker: 19 fra PNG 1 (25.05 - 28.09) + 13 fra PNG 2 (05.10 - 28.12)
WEEKS = [
    # PNG 1
    '2026-05-25', '2026-06-01', '2026-06-08', '2026-06-15', '2026-06-22',
    '2026-06-29', '2026-07-06', '2026-07-13', '2026-07-20', '2026-07-27',
    '2026-08-03', '2026-08-10', '2026-08-17', '2026-08-24', '2026-08-31',
    '2026-09-07', '2026-09-14', '2026-09-21', '2026-09-28',
    # PNG 2
    '2026-10-05', '2026-10-12', '2026-10-19', '2026-10-26', '2026-11-02',
    '2026-11-09', '2026-11-16', '2026-11-23', '2026-11-30', '2026-12-07',
    '2026-12-14', '2026-12-21', '2026-12-28',
]

# Severity-band: 'green', 'yellow', 'red', 'purple', 'black'
G = 'green'
Y = 'yellow'
R = 'red'
P = 'purple'
B = 'black'

# NB: 'Electric - 54kW Electric HPU' er ny rad i snap3 (eksisterte ikke i snap2).
ASSETS = [
    # ----- Winch -----
    ('Winch', 'Hydraulic - Wide|35Te Wide Drum Winch - 35Te Wide Drum Winch',
     [-2,-2,-2,-2,-2,-2,-2,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*8 + [G]*11 + [G]*13),

    ('Winch', 'Hydraulic - Wide|20Te Wide Drum Winch - 20Te Wide Drum Winch',
     [ 4, 3, 3, 3, 3, 3, 2, 2, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5,
       5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
     [G]*32),

    ('Winch', 'Hydraulic - Narr|20Te Narrow Drum Winch - 20Te Narrow Drum Winch',
     [ 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 3, 4, 4, 4, 4, 4,
       4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
     [G]*32),

    ('Winch', 'Hydraulic - 5Te Brevini Winch',
     [1]*32, [G]*32),

    # ----- Under rollers -----
    ('Under rollers', '- 60Te Crane Loaded Underrollers',
     [1]*32, [G]*32),

    # ----- Turntables (ny i snap3 - 60Te Turntable gar i underskudd mot slutten) -----
    ('Turntables', '- 60Te Turntable',
     [0]*17 + [-1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [G]*17 + [B]*2 + [B]*4 + [G]*9),

    # ----- Tensioner -----
    ('Tensioner', 'Horizontal - 4 track - 50Te Tensioner - 4 Track',
     [-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*8 + [G]*11 + [G]*13),

    ('Tensioner', 'Horizontal - 2 track - 15Te Horizontal Tensioner',
     [-1,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*11 + [G]*8 + [G]*13),

    # ----- Spoolers -----
    ('Spoolers', 'Pneumatic - 6Te Air Spooler',
     [ 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
       4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
     [G]*32),

    ('Spoolers', 'Electric - 75Te Electric Spooler',
     [ 2, 2, 1, 1, 0, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
     [G]*4 + [P] + [G]*14 + [G]*13),

    # ----- RDS -----
    ('RDS', '- 500Te RDS',
     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*14 + [G]*5 + [G]*13),

    ('RDS', '- 150Te RDS',
     [-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*7 + [G]*12 + [G]*13),

    # ----- LMA machines -----
    ('LMA machines', 'LMA - LMA300 MRT Machine',
     [1]*32, [G]*32),

    # ----- HPUS -----
    ('HPUS', 'Electric - 90KW Electric HPU',
     [-1,-1,-1,-1,-1,-1,-1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [B]*7 + [P] + [G]*11 + [G]*13),

    ('HPUS', 'Electric - 55kW Electric HPU - Zone 1',
     [ 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3,
       3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
     [G]*32),

    ('HPUS', 'Electric - 55kW Electric HPU',
     [ 0, 0, 0, 0, 0, 0,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
     [P]*6 + [B]*2 + [P]*11 + [G]*13),

    # NY rad i snap3 - eksisterte ikke i snap2
    ('HPUS', 'Electric - 54kW Electric HPU',
     [ 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
      -1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [P]*2 + [B]*19 + [G]*11),

    ('HPUS', 'Electric - 37kW Electric HPU',
     [ 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
     [G]*32),

    ('HPUS', 'Electric - 30kW Electric HPU',
     [ 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
     [P]*6 + [G]*13 + [G]*13),

    ('HPUS', 'Electric - 18.5kW Electric HPU',
     [1]*32, [G]*32),

    ('HPUS', 'Electric - 158KW Electric HPU',
     [-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*7 + [G]*12 + [G]*13),

    ('HPUS', 'Electric - 11kW Electric HPU',
     [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [P]*19 + [P]*2 + [G]*11),

    ('HPUS', 'Electric - 1.5kW Electric HPU',
     [1]*32, [G]*32),

    ('HPUS', 'Diesel - 63kW Diesel HPU Zone II',
     [0]*32, [P]*32),

    ('HPUS', 'Diesel - 63kW Diesel HPU',
     [1]*32, [G]*32),

    # ----- Cable Pulling machine -----
    ('Cable Pulling machine', '- 2Te Linear Cable Engine',
     [ 0, 0, 0, 0, 0, 0,-2,-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [G]*6 + [B]*2 + [G]*11 + [G]*13),
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
OUT_PATH = os.path.join(
    PROJECT_ROOT, '004 data', '2026-05-21_motive_no', 'clean',
    '2026-05-21_supply_demand_motive_no_75pct.csv'
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
    # PNG 1 (25.05 - 28.09)
    '2026-05-25': 16, '2026-06-01': 13, '2026-06-08': 11, '2026-06-15': 11,
    '2026-06-22': 11, '2026-06-29':  9, '2026-07-06':  6, '2026-07-13': 13,
    '2026-07-20': 20, '2026-07-27': 21, '2026-08-03': 20, '2026-08-10': 23,
    '2026-08-17': 24, '2026-08-24': 26, '2026-08-31': 26, '2026-09-07': 27,
    '2026-09-14': 27, '2026-09-21': 26, '2026-09-28': 26,
    # PNG 2 (05.10 - 28.12)
    '2026-10-05': 27, '2026-10-12': 31, '2026-10-19': 33, '2026-10-26': 33,
    '2026-11-02': 34, '2026-11-09': 34, '2026-11-16': 34, '2026-11-23': 34,
    '2026-11-30': 34, '2026-12-07': 34, '2026-12-14': 34, '2026-12-21': 34,
    '2026-12-28': 34,
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
    print(f'Sum-sjekk OK: alle 32 uker innen +/-2 fra Totalt-raden '
          f'({warnings} med liten avrundingsstoy, 0 transkriberingsfeil).')
else:
    print(f'{errors} uker har avvik > 2 - mistanke om transkriberingsfeil.')

# Asset-type-aggregert sjekk (Tier 1-rader fra PNG-ene)
ASSET_TYPE_TOTAL = {
    'Winch': [7,6,6,6,6,6,4,5,8,8,7,8,9,10,10,10,10,10,10,
              10,12,12,12,12,12,12,12,12,12,12,12,12],
    'Under rollers': [1]*32,
    'Turntables': [0]*17 + [-1,-1, -1,-1,-1,-1, 0,0,0,0,0,0,0,0,0],
    'Tensioner': [-2,-2,-2,-2,-2,-3,-3,-2,-1,-1,-1, 0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,0,0,0,0,0],
    'Spoolers': [6,5,4,4,4,5,5,5,5,6,6,6,6,5,5,5,5,5,5,
                 6,6,6,6,6,6,6,6,6,6,6,6,6],
    'RDS': [-2]*7 + [-1]*7 + [0]*5 + [0]*13,
    'LMA machines': [1]*32,
    'HPUS': [5,4,3,3,3,3,2,4,7,7,7,8,8,10,10,10,10,10,10,
            10,12,14,14,14,14,14,14,14,14,14,14,14],
    'Cable Pulling machine': [0,0,0,0,0,0,-2,-2, 0]*1 + [0]*10 + [0]*13,
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
