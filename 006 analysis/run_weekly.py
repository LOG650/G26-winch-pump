"""Ukentlig orkestreringsskript for kapasitetsvarslingssystemet.

Kjeder hele pipelinen fra to snapshot-CSV-er til ferdige varsler og digester:

    snap1.csv, snap2.csv
            |
            v
    [3.3 gap-deteksjon/gap_detection.py]
            |
            v
    gap_changes.csv  (alle endringer klassifisert)
            |
            v
    [3.4 varsling/gap_alerting.py]
            |
            v
    varsler.csv + digests/  (ruting + paminnelser + lost)

Skriptet tar to snapshot-CSV-stier og leser snapshot-datoene direkte fra
filinnholdet (kolonnen `snapshot_date`). Snapshot-datoer trenger derfor ikke
oppgis manuelt.

Kjor:
    uv run python run_weekly.py --prev path/to/snap1.csv --curr path/to/snap2.csv

Eller default (snap 2026-05-07 til 2026-05-14):
    uv run python run_weekly.py
"""
import argparse
import os
import subprocess
import sys

import pandas as pd


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
GAP_DETECTION_SCRIPT = os.path.join(SCRIPT_DIR, '3.3 gap-deteksjon', 'gap_detection.py')
GAP_ALERTING_SCRIPT = os.path.join(SCRIPT_DIR, '3.4 varsling', 'gap_alerting.py')
GAP_CHANGES_OUT = os.path.join(SCRIPT_DIR, '3.3 gap-deteksjon', 'gap_changes.csv')

DEFAULT_PREV = os.path.join(
    PROJECT_ROOT, '004 data', '2026-05-07_motive_no',
    'clean', '2026-05-07_supply_demand_motive_no_75pct.csv'
)
DEFAULT_CURR = os.path.join(
    PROJECT_ROOT, '004 data', '2026-05-14_motive_no',
    'clean', '2026-05-14_supply_demand_motive_no_75pct.csv'
)


def read_snapshot_date(csv_path: str) -> str:
    """Hent snapshot_date fra forste rad i CSV-en."""
    df = pd.read_csv(csv_path, usecols=['snapshot_date'], nrows=1)
    return str(df['snapshot_date'].iloc[0])


def run_step(label: str, cmd: list[str]) -> None:
    """Kjor en subprocess-kommando og avbryt pipelinen ved feil."""
    print(f'\n{"=" * 60}')
    print(f'{label}')
    print(f'{"=" * 60}')
    print(f'  cmd: {" ".join(cmd)}\n')
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f'\n  ! {label} feilet (exit {result.returncode}). Avbryter pipeline.')
        sys.exit(result.returncode)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--prev', default=DEFAULT_PREV,
                        help='Sti til forrige snapshot-CSV (t-1)')
    parser.add_argument('--curr', default=DEFAULT_CURR,
                        help='Sti til inneverende snapshot-CSV (t)')
    args = parser.parse_args()

    for label, path in [('prev', args.prev), ('curr', args.curr)]:
        if not os.path.exists(path):
            print(f'! Snapshot-CSV mangler: {label} = {path}')
            sys.exit(1)

    prev_date = read_snapshot_date(args.prev)
    curr_date = read_snapshot_date(args.curr)

    print(f'Ukentlig pipeline: {prev_date} -> {curr_date}')
    print(f'  Prev: {args.prev}')
    print(f'  Curr: {args.curr}')

    # Steg 1: gap-deteksjon
    run_step(
        '[1/2] Gap-deteksjon (3.3)',
        [sys.executable, GAP_DETECTION_SCRIPT,
         '--snap1', args.prev, '--snap2', args.curr],
    )

    if not os.path.exists(GAP_CHANGES_OUT):
        print(f'\n! Forventet output mangler: {GAP_CHANGES_OUT}')
        sys.exit(1)

    # Steg 2: varslingsgenerering
    run_step(
        '[2/2] Varslingsgenerering (3.4)',
        [sys.executable, GAP_ALERTING_SCRIPT,
         '--gap-changes', GAP_CHANGES_OUT,
         '--snapshot-t', curr_date,
         '--snapshot-t-minus-1', prev_date],
    )

    print(f'\n{"=" * 60}')
    print('Pipeline ferdig.')
    print(f'{"=" * 60}')
    print(f'  Endringer: {GAP_CHANGES_OUT}')
    print(f'  Varsler:   {os.path.join(SCRIPT_DIR, "3.4 varsling", "varsler.csv")}')
    print(f'  Digester:  {os.path.join(SCRIPT_DIR, "3.4 varsling", "digests")}')
    print(f'  Tilstand:  {os.path.join(SCRIPT_DIR, "3.4 varsling", "active_alerts.json")}')


if __name__ == '__main__':
    main()
