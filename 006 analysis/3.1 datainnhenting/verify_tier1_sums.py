"""Verifiserer leaf-sum mot Tier 1-gruppesummer for et snapshot.

Bruk: uv run python "3.1 datainnhenting/verify_tier1_sums.py" <csv-fil>

Forskjell |diff| <= ROUNDING_TOLERANCE markeres som avrundingsstoy
(Power BI viser avrundede heltall i celler men aggregerer Tier 1 fra
desimal-grunndata). Storre forskjeller er sannsynligvis transkriberingsfeil.
"""
import csv
import sys
from collections import defaultdict

ROUNDING_TOLERANCE = 2


def main(csv_path: str, expected_tier1: dict[str, list[int]]) -> int:
    rows = []
    with open(csv_path, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            rows.append(r)

    weeks = sorted({r['week_start'] for r in rows})
    sums: dict[str, list[int]] = defaultdict(lambda: [0] * len(weeks))
    week_idx = {w: i for i, w in enumerate(weeks)}
    for r in rows:
        sums[r['asset_tier1']][week_idx[r['week_start']]] += int(r['gap_value'])

    print(f'CSV: {csv_path}')
    print(f'Uker: {weeks}')
    print()
    print(f'{"Tier 1":25s} | ' + ' | '.join(f'{w[5:]:>6s}' for w in weeks))
    print('-' * (28 + 9 * len(weeks)))
    transcription_errors = 0
    rounding_noise = 0
    for t1 in sorted(sums):
        line = f'{t1:25s} | ' + ' | '.join(f'{v:>6d}' for v in sums[t1])
        print(line)
        if t1 in expected_tier1:
            exp = expected_tier1[t1]
            diffs = [s - e for s, e in zip(sums[t1], exp)]
            if any(d != 0 for d in diffs):
                marks = []
                for d in diffs:
                    if d == 0:
                        marks.append(f'{"":>6s}')
                    elif abs(d) <= ROUNDING_TOLERANCE:
                        marks.append(f'{d:>+6d}')
                        rounding_noise += 1
                    else:
                        marks.append(f'{d:>+6d}!')
                        transcription_errors += 1
                print(f'{"  diff":25s} | ' + ' | '.join(marks))

    print()
    print(f'Avrundingsstoy (|diff| <= {ROUNDING_TOLERANCE}): {rounding_noise} celler')
    print(f'Transkriberingsfeil  (|diff| >  {ROUNDING_TOLERANCE}): {transcription_errors} celler')
    return 1 if transcription_errors > 0 else 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Bruk: verify_tier1_sums.py <csv-fil>')
        sys.exit(2)

    EXPECTED_2026_04_30 = {
        # uker:                   05-04 05-11 05-18 05-25 06-01 06-08 06-15 06-22 06-29 07-06 07-13 07-20 07-27 08-03 08-10 08-17 08-24 08-31 09-07 09-14 09-21 09-28 10-05 10-12 10-19 10-26 11-02 11-09 11-16 11-23 11-30 12-07 12-14 12-21 12-28 01-04
        'Winch':                 [-44,  -45,  -39,  -36,  -37,  -48,  -36,  -32,  -37,  -30,  -31,  -27,  -30,  -24,  -28,  -21,  -21,  -20,  -21,  -19,  -12,  -14,  -10,  -9,   -10,  -10,  -11,  -10,  -8,   -8,   -6,   -6,   0,    0,    0,    6],
        'Under rollers':         [-5,   -6,   -5,   -5,   -4,   -4,   -6,   -7,   -7,   -7,   -7,   -7,   -8,   -6,   -7,   -5,   -5,   -5,   -5,   -5,   -5,   -5,   -3,   -2,   -2,   -1,   0,    0,    0,    0,    0,    0,    0,    0,    0,    1],
        'Turntables':            [-2,   -2,   -4,   -3,   -2,   -2,   -2,   -2,   -5,   -4,   -3,   -2,   -2,   -2,   -2,   -2,   -2,   -3,   -1,   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        'Tensioner':             [-21,  -22,  -19,  -19,  -20,  -23,  -22,  -21,  -22,  -28,  -23,  -22,  -25,  -22,  -22,  -19,  -18,  -19,  -18,  -18,  -18,  -19,  -18,  -17,  -18,  -18,  -16,  -16,  -16,  -16,  -14,  -14,  -12,  -12,  -11,  -3],
        'Storage reels':         [-1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   0],
        'Spoolers':              [-19,  -13,  -8,   -15,  -13,  -13,  -13,  -13,  -12,  -9,   -6,   -6,   -5,   -4,   -4,   -3,   -3,   -6,   -3,   -2,   0,    1,    2,    2,    0,    0,    1,    2,    2,    2,    3,    3,    4,    4,    4,    6],
        'RDS':                   [-12,  -13,  -12,  -12,  -12,  -12,  -16,  -15,  -15,  -15,  -14,  -14,  -15,  -13,  -13,  -13,  -12,  -10,  -9,   -9,   -9,   -12,  -8,   -8,   -6,   -6,   -5,   -6,   -6,   -6,   -6,   -6,   -6,   -6,   -5,   -4],
        'LMA machines':          [-5,   -2,   -3,   -5,   -3,   -4,   -5,   -3,   -2,   0,    1,    1,    0,    0,    0,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1],
        'HPUS':                  [-59,  -61,  -57,  -50,  -51,  -61,  -65,  -63,  -69,  -60,  -58,  -54,  -58,  -46,  -46,  -44,  -46,  -40,  -38,  -36,  -33,  -35,  -24,  -22,  -18,  -18,  -14,  -14,  -14,  -14,  -11,  -11,  -5,   -5,   -6,   12],
        'HLS':                   [-1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   0,    0,    0,    0,    0,    0,    0,    0,    -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   0],
        'Generators':            [-1,   -2,   -3,   -2,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -2,   -1,   -2,   -2,   -2,   -2,   0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        'Cranes':                [-3,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -4,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -3,   -2,   -2,   -2,   -2,   -2,   -2,   -2,   -2,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1],
        'Cable Pulling machine': [-9,   -9,   -10,  -9,   -7,   -9,   -9,   -9,   -8,   -8,   -8,   -8,   -10,  -7,   -7,   -7,   -9,   -7,   -7,   -7,   -7,   -5,   -6,   -4,   -4,   -6,   -2,   -2,   -2,   -2,   -2,   -2,   -2,   -1,   -1,   0],
    }
    sys.exit(main(sys.argv[1], EXPECTED_2026_04_30))
