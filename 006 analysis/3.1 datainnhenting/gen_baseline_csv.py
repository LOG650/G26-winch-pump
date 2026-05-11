"""Genererer 2026-05-07_supply_demand_motive_no_75pct.csv fra transkriberte skjermbildeverdier.

Kjoer: uv run python "3.1 datainnhenting/gen_baseline_csv.py"
"""
import csv
import os

SNAPSHOT = '2026-05-07'
CUSTODIAN = 'Motive AS'
PROJECT_OWNER = 'Motive AS'
REGION = 'Motive Norway'
PROB = 75

WEEKS = [
    '2026-05-11', '2026-05-18', '2026-05-25', '2026-06-01',
    '2026-06-08', '2026-06-15', '2026-06-22', '2026-06-29',
    '2026-07-06', '2026-07-13', '2026-07-20', '2026-07-27',
    '2026-08-03', '2026-08-10', '2026-08-17', '2026-08-24',
    '2026-08-31', '2026-09-07', '2026-09-14', '2026-09-21',
    '2026-09-28', '2026-10-05', '2026-10-12', '2026-10-19',
    '2026-10-26', '2026-11-02', '2026-11-09', '2026-11-16',
    '2026-11-23', '2026-11-30', '2026-12-07', '2026-12-14',
    '2026-12-21', '2026-12-28',
]

# (asset_type, asset_tier2, [gap_value per uke w0..w33])
# Alle verdier krysssjekket mot Totalt-raden i Power BI (se verify_asset_type_sums.py)
ASSETS = [
    ('Winch', 'Hydraulic - Wide|35Te Wide Drum Winch - 35Te Wide Drum Winch',
     [-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
    ('Winch', 'Hydraulic - Wide|20Te Wide Drum Winch - 20Te Wide Drum Winch',
     [4,4,4,3,3,3,3,3,2,2,4,4,5,5,5,5,5,5,5,5,5,5,7,7,7,7,7,7,7,7,7,7,7,7]),
    ('Winch', 'Hydraulic - Narr|20Te Narrow Drum Winch - 20Te Narrow Drum Winch',
     [1,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]),
    ('Winch', 'Hydraulic - 5Te Brevini Winch',
     [1]*34),
    ('Under rollers', '- 60Te Crane Loaded Underrollers',
     [1]*34),
    ('Tensioner', 'Horizontal - 4 track - 50Te Tensioner - 4 Track',
     [-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
    ('Tensioner', 'Horizontal - 2 track - 15Te Horizontal Tensioner',
     [-1,-1,-1,-1,-1,-1,-1,-2,-2,-2,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
    ('Spoolers', 'Pneumatic - 6Te Air Spooler',
     [4]*34),
    ('Spoolers', 'Electric - 75Te Electric Spooler',
     [2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2]),
    ('RDS', '- 500Te RDS',
     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
    ('RDS', '- 150Te RDS',
     [-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
    ('LMA machines', 'LMA - LMA300 MRT Machine',
     [1]*34),
    ('HPUS', 'Electric - 90KW Electric HPU',
     [-2,-2,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),
    # Zone 1: dip til 0 i veke 8 (06.07) pga prosjektoppstart
    ('HPUS', 'Electric - 55kW Electric HPU – Zone 1',
     [1,1,2,1,1,1,1,1,0,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]),
    # 55kW: -2 i veke 9 (13.07), 0 t.o.m. 05.10, deretter 2
    ('HPUS', 'Electric - 55kW Electric HPU',
     [0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2]),
    ('HPUS', 'Electric - 37kW Electric HPU',
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]),
    ('HPUS', 'Electric - 30kW Electric HPU',
     [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2]),
    ('HPUS', 'Electric - 18.5kW Electric HPU',
     [1]*34),
    # 158KW: bruker bekreftet -1 for vekene 0-8, deretter 0
    ('HPUS', 'Electric - 158KW Electric HPU',
     [-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
    ('HPUS', 'Electric - 11kW Electric HPU',
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]),
    ('HPUS', 'Electric - 1.5kW Electric HPU',
     [1]*34),
    # Diesel Zone II: bruker bekreftet 0 heile perioden
    ('HPUS', 'Diesel - 63kW Diesel HPU Zone II',
     [0]*34),
    ('HPUS', 'Diesel - 63kW Diesel HPU',
     [1]*34),
    # Cable: -2 i vekene 08.06, 15.06 og 22.06 (indeksene 4-6), 0 ellers
    ('Cable Pulling machine', '- 2Te Linear Cable Engine',
     [0,0,0,0,-2,-2,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
OUT_PATH = os.path.join(
    PROJECT_ROOT, '004 data', '2026-05-07_motive_no_baseline', 'clean',
    '2026-05-07_supply_demand_motive_no_75pct.csv'
)

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

rows = []
for asset_type, asset_tier2, values in ASSETS:
    assert len(values) == len(WEEKS), f'{asset_tier2}: {len(values)} verdier, forventet {len(WEEKS)}'
    for week, val in zip(WEEKS, values):
        rows.append({
            'snapshot_date': SNAPSHOT,
            'week_start': week,
            'asset_type': asset_type,
            'asset_tier2': asset_tier2,
            'gap_value': val,
            'custodian': CUSTODIAN,
            'project_owner_demand': PROJECT_OWNER,
            'region': REGION,
            'probability_threshold': PROB,
        })

with open(OUT_PATH, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'snapshot_date', 'week_start', 'asset_type', 'asset_tier2',
        'gap_value', 'custodian', 'project_owner_demand', 'region',
        'probability_threshold'
    ])
    writer.writeheader()
    writer.writerows(rows)

print(f'Skrev {len(rows)} rader til:\n  {OUT_PATH}')

# Enkel sum-sjekk mot Totalt-raden
from collections import defaultdict
weekly_total: dict[str, int] = defaultdict(int)
for r in rows:
    weekly_total[r['week_start']] += r['gap_value']

EXPECTED_TOTAL = {
    '2026-05-11': 10, '2026-05-18': 11, '2026-05-25': 13, '2026-06-01': 12,
    '2026-06-08': 10, '2026-06-15': 10, '2026-06-22': 10, '2026-06-29': 11,
    '2026-07-06':  9, '2026-07-13': 14, '2026-07-20': 21, '2026-07-27': 21,
    '2026-08-03': 24, '2026-08-10': 25, '2026-08-17': 28, '2026-08-24': 28,
    '2026-08-31': 28, '2026-09-07': 27, '2026-09-14': 27, '2026-09-21': 27,
    '2026-09-28': 28, '2026-10-05': 28, '2026-10-12': 32, '2026-10-19': 34,
    '2026-10-26': 34, '2026-11-02': 34, '2026-11-09': 34, '2026-11-16': 34,
    '2026-11-23': 34, '2026-11-30': 34, '2026-12-07': 34, '2026-12-14': 34,
    '2026-12-21': 34, '2026-12-28': 34,
}

errors = 0
for week, exp in EXPECTED_TOTAL.items():
    got = weekly_total[week]
    if got != exp:
        print(f'  FEIL {week}: sum={got}, forventet={exp} (diff={got - exp})')
        errors += 1

if errors == 0:
    print('Sum-sjekk OK: alle 34 uker matcher Totalt-raden fra Power BI.')
else:
    print(f'{errors} uker har avvik – sjekk verdiene over.')
