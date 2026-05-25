"""Genererer 2026-05-07_supply_demand_motive_no_75pct.csv fra transkriberte
skjermbildeverdier (gap_value + severity_band per celle).

Kjoer: uv run python "3.1 datainnhenting/gen_baseline_csv.py"
"""
import csv
import os
from collections import defaultdict

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

# Severity-band-koder
G = 'green'
Y = 'yellow'
R = 'red'
P = 'purple'
B = 'black'

# (asset_type, asset_tier2, [gap_value per uke], [severity_band per uke])
# Verdier krysssjekket mot Totalt-raden i Power BI; farger lest fra PNG-bildene
# i 004 data/2026-05-07_motive_no/raw/.
ASSETS = [
    ('Winch', 'Hydraulic - Wide|35Te Wide Drum Winch - 35Te Wide Drum Winch',
     [-2,-2,-2,-2,-2,-2,-2,-2,-2,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*10 + [G]*24),

    ('Winch', 'Hydraulic - Wide|20Te Wide Drum Winch - 20Te Wide Drum Winch',
     [ 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5,
       5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
     [G]*34),

    # Veke 0 (11.05) er gul (1 = liten overdekning); resten gronn
    ('Winch', 'Hydraulic - Narr|20Te Narrow Drum Winch - 20Te Narrow Drum Winch',
     [ 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4,
       4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
     [Y] + [G]*33),

    ('Winch', 'Hydraulic - 5Te Brevini Winch',
     [1]*34, [G]*34),

    ('Under rollers', '- 60Te Crane Loaded Underrollers',
     [1]*34, [G]*34),

    ('Tensioner', 'Horizontal - 4 track - 50Te Tensioner - 4 Track',
     [-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*9 + [G]*25),

    ('Tensioner', 'Horizontal - 2 track - 15Te Horizontal Tensioner',
     [-1,-1,-1,-1,-1,-1,-1,-2,-2,-2,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*13 + [G]*21),

    ('Spoolers', 'Pneumatic - 6Te Air Spooler',
     [4]*34, [G]*34),

    ('Spoolers', 'Electric - 75Te Electric Spooler',
     [ 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
     [G]*34),

    ('RDS', '- 500Te RDS',
     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*14 + [G]*20),

    ('RDS', '- 150Te RDS',
     [-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*9 + [G]*25),

    ('LMA machines', 'LMA - LMA300 MRT Machine',
     [1]*34, [G]*34),

    # Veke 9 (13.07) er lilla nar verdien gar fra -1 til 0
    ('HPUS', 'Electric - 90KW Electric HPU',
     [-2,-2,-1,-1,-1,-1,-1,-1,-1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [B]*9 + [P] + [G]*24),

    # Veke 8 (06.07) er lilla pga dip til 0 ved prosjektoppstart
    ('HPUS', 'Electric - 55kW Electric HPU - Zone 1',
     [ 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3,
       3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
     [G]*8 + [P] + [G]*25),

    # Lilla mens verdi=0 (underliggende lite negativt), svart ved -2,
    # gronn nar verdi gar til +2 fra veke 23 (19.10)
    ('HPUS', 'Electric - 55kW Electric HPU',
     [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
     [P]*9 + [B] + [P]*13 + [G]*11),

    ('HPUS', 'Electric - 37kW Electric HPU',
     [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
     [G]*34),

    # Lilla mens verdi=0, gronn fra veke 9 (13.07) nar verdi blir 1+
    ('HPUS', 'Electric - 30kW Electric HPU',
     [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
     [P]*9 + [G]*25),

    ('HPUS', 'Electric - 18.5kW Electric HPU',
     [1]*34, [G]*34),

    # -1 vises gronn i PNG, men negativ gap maa egentlig vere lilla/svart;
    # her merket svart for konsistens (samme som andre -1 leaf-rader)
    ('HPUS', 'Electric - 158KW Electric HPU',
     [-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [B]*9 + [G]*25),

    # Lilla mens verdi=0, gronn fra veke 22 (12.10) nar verdi blir 1
    ('HPUS', 'Electric - 11kW Electric HPU',
     [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [P]*22 + [G]*12),

    ('HPUS', 'Electric - 1.5kW Electric HPU',
     [1]*34, [G]*34),

    # Verdi alltid 0; lilla hele perioden
    ('HPUS', 'Diesel - 63kW Diesel HPU Zone II',
     [0]*34, [P]*34),

    ('HPUS', 'Diesel - 63kW Diesel HPU',
     [1]*34, [G]*34),

    # 0 gronn, -2 svart i vekene 08.06, 15.06, 22.06 (idx 4-6)
    ('Cable Pulling machine', '- 2Te Linear Cable Engine',
     [ 0, 0, 0, 0,-2,-2,-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [G]*4 + [B]*3 + [G]*27),
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
OUT_PATH = os.path.join(
    PROJECT_ROOT, '004 data', '2026-05-07_motive_no', 'clean',
    '2026-05-07_supply_demand_motive_no_75pct.csv'
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

# Totalt-sjekken aksepterer +/-2 som avrundingsstoy (jf. tab_kolonner.md)
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
    print(f'Sum-sjekk OK: alle 34 uker innen +/-2 fra Totalt-raden '
          f'({warnings} med liten avrundingsstoy, 0 transkriberingsfeil).')
else:
    print(f'{errors} uker har avvik > 2 - mistanke om transkriberingsfeil.')

# Farge-konsistens-sjekk: negativ gap kan ikke vere gronn/gul/rod
color_errors = 0
for r in rows:
    g, s = r['gap_value'], r['severity_band']
    if g < 0 and s in (G, Y, R):
        print(f"  FARGE-FEIL {r['week_start']} {r['asset_tier2']}: "
              f"gap={g} men severity={s}")
        color_errors += 1
    if g > 0 and s in (P, B):
        print(f"  FARGE-FEIL {r['week_start']} {r['asset_tier2']}: "
              f"gap={g} men severity={s}")
        color_errors += 1

if color_errors == 0:
    print('Farge-konsistens OK: ingen umulige (gap, severity)-kombinasjoner.')
else:
    print(f'{color_errors} celler har umulig (gap, severity)-kombinasjon.')
