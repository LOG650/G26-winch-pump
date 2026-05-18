"""3.4 Varslingslogikk - genererer varsler fra gap_changes.csv.

Anvender regelmatrisene i 6.5 (G-baserte + severity-baserte) og rutingen i 6.7.
Sporer aktive varslingstrader i active_alerts.json mellom snapshot-kjoringer,
slik at samme celle som forblir i gap utloser ukentlig paminnelse og avsluttes
med varsel nar gapet er lost.

Kjor: uv run python "3.4 varsling/gap_alerting.py"
"""
import csv
import json
import os
from collections import defaultdict
from dataclasses import asdict, dataclass, fields

import pandas as pd
import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
RECIPIENTS_PATH = os.path.join(SCRIPT_DIR, 'recipients.yaml')
GAP_CHANGES_PATH = os.path.join(
    PROJECT_ROOT, '006 analysis', '3.3 gap-deteksjon', 'gap_changes.csv'
)
STATE_PATH = os.path.join(SCRIPT_DIR, 'active_alerts.json')
OUT_DIR = SCRIPT_DIR

EXCLUSION_LIST = {
    'Diesel - 63kW Diesel HPU Zone II',
}
STRUCTURAL_ASSETS: set[str] = set()

OVERDEKNING = {'green', 'yellow', 'red'}
UNDERDEKNING = {'purple', 'black'}

# Hardkodede snapshot-datoer for denne kjoringen. Utvidelse: les fra metadata.
SNAPSHOT_T = '2026-05-14'
SNAPSHOT_T1 = '2026-05-07'


@dataclass
class Varsel:
    snapshot_t: str
    snapshot_t_minus_1: str
    week_start: str
    region: str
    asset_type: str
    asset_tier2: str
    gap_t_minus_1: int
    gap_t: int
    severity_t_minus_1: str
    severity_t: str
    change_type: str
    severity_change: str
    rule_triggered: str
    sub_category: str
    magnitude_class: str
    priority: str
    is_structural: bool
    thread_status: str  # 'ny' / 'paminnelse' / 'eskalert' / 'lost' / 'informasjon'
    reminder_count: int  # 0 for nye varsler, 1+ for paminnelser
    opened_at: str  # snapshot-dato da threaden ble apnet
    recipient: str


def magnitude_class(gap: int) -> str:
    if gap >= 0:
        return 'ingen'
    if -2 <= gap <= -1:
        return 'mildt'
    if -5 <= gap <= -3:
        return 'moderat'
    return 'kritisk'


def severity_cross(s1: str, s2: str) -> str | None:
    if s1 in OVERDEKNING and s2 in UNDERDEKNING:
        return 'SKJULT_NYTT_GAP'
    if s1 in UNDERDEKNING and s2 in OVERDEKNING:
        return 'SKJULT_LOST_GAP'
    if s1 == 'purple' and s2 == 'black':
        return 'SKJULT_FORVERRING'
    if s1 == 'black' and s2 == 'purple':
        return 'SKJULT_FORBEDRING'
    return None


def evaluate_alert(row: dict, is_structural: bool) -> tuple[bool, str, str, str]:
    """Avgjor om en celle utloser varsel per Tabell 6.4 og 6.5."""
    ct = row['change_type']
    g1, g2 = int(row['gap_value_t1']), int(row['gap_value_t2'])
    s1, s2 = row['severity_band_t1'], row['severity_band_t2']

    # Tabell 6.4 - G-baserte regler
    if ct == 'NYTT_GAP':
        prio = 'høy' if magnitude_class(g2) in ('moderat', 'kritisk') else 'middels'
        return True, 'G-regel', 'NYTT_GAP', prio
    if ct == 'FORVERRET':
        if magnitude_class(g1) != magnitude_class(g2):
            return True, 'G-regel', 'FORVERRET_KLASSEBYTTE', 'høy'
        if is_structural:
            return False, '', '', ''
        return True, 'G-regel', 'FORVERRET_INNEN_KLASSE', 'lav'
    if ct == 'LOEST':
        return True, 'G-regel', 'LOEST', 'informasjon'

    # Tabell 6.5 - severity-supplement
    sct = severity_cross(s1, s2)
    if sct == 'SKJULT_NYTT_GAP':
        return True, 'severity-regel', sct, 'middels'
    if sct == 'SKJULT_FORVERRING':
        return True, 'severity-regel', sct, 'høy'
    if sct == 'SKJULT_LOST_GAP':
        return True, 'severity-regel', sct, 'informasjon'
    return False, '', '', ''


def cell_in_gap(gap: int, severity: str) -> bool:
    """Cellen er 'i gap-tilstand' hvis G negativ eller severity i underdekning."""
    return gap < 0 or severity in UNDERDEKNING


def thread_key(asset_type: str, asset_tier2: str, week_start: str) -> str:
    return f'{asset_type}|{asset_tier2}|{week_start}'


def load_state() -> dict:
    if not os.path.exists(STATE_PATH):
        return {'last_run': None, 'threads': {}}
    with open(STATE_PATH, encoding='utf-8') as f:
        return json.load(f)


def save_state(state: dict) -> None:
    with open(STATE_PATH, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def is_gap_opening_alert(sub_category: str) -> bool:
    """Avgjor om denne alert-typen apner en ny varslingstrad."""
    return sub_category in (
        'NYTT_GAP',
        'SKJULT_NYTT_GAP',
        'FORVERRET_KLASSEBYTTE',
        'FORVERRET_INNEN_KLASSE',
        'SKJULT_FORVERRING',
    )


def make_varsel(
    row: dict, recipient: str, is_structural: bool,
    rule: str, sub_cat: str, priority: str,
    thread_status: str, reminder_count: int, opened_at: str,
) -> Varsel:
    return Varsel(
        snapshot_t=SNAPSHOT_T,
        snapshot_t_minus_1=SNAPSHOT_T1,
        week_start=row['week_start'],
        region='Motive Norway',
        asset_type=row['asset_type'],
        asset_tier2=row['asset_tier2'],
        gap_t_minus_1=int(row['gap_value_t1']),
        gap_t=int(row['gap_value_t2']),
        severity_t_minus_1=row['severity_band_t1'],
        severity_t=row['severity_band_t2'],
        change_type=row['change_type'],
        severity_change=row['severity_change'],
        rule_triggered=rule,
        sub_category=sub_cat,
        magnitude_class=magnitude_class(int(row['gap_value_t2'])),
        priority=priority,
        is_structural=is_structural,
        thread_status=thread_status,
        reminder_count=reminder_count,
        opened_at=opened_at,
        recipient=recipient,
    )


def generate_varsler(
    df: pd.DataFrame, recipients: dict, default_recipient: str,
    existing_threads: dict,
) -> tuple[list[Varsel], dict]:
    """Bygg varsler og oppdatert trad-tilstand.

    Returnerer (varsler, new_threads).
    """
    varsler: list[Varsel] = []
    new_threads: dict = {}
    seen_keys: set[str] = set()

    for _, row in df.iterrows():
        r = row.to_dict()
        key = thread_key(r['asset_type'], r['asset_tier2'], r['week_start'])
        seen_keys.add(key)

        is_struct = r['asset_tier2'] in STRUCTURAL_ASSETS
        recipient = recipients.get(r['asset_type'], default_recipient)
        alert, rule, sub_cat, prio = evaluate_alert(r, is_struct)
        in_gap_now = cell_in_gap(int(r['gap_value_t2']), r['severity_band_t2'])

        prior = existing_threads.get(key)

        if prior is not None:
            # Eksisterende trad
            if not in_gap_now:
                # Lukker - emit lost varsel
                varsler.append(make_varsel(
                    r, recipient, is_struct,
                    rule='thread-closure', sub_cat='LØST_TRAD',
                    priority='informasjon',
                    thread_status='lost',
                    reminder_count=prior.get('reminder_count', 0),
                    opened_at=prior['opened_at'],
                ))
                # Tråden lukkes (ikke videreført)
            else:
                # Fortsatt i gap
                if alert and sub_cat == 'FORVERRET_KLASSEBYTTE':
                    status = 'eskalert'
                    varsler.append(make_varsel(
                        r, recipient, is_struct,
                        rule=rule, sub_cat=sub_cat, priority=prio,
                        thread_status=status,
                        reminder_count=prior.get('reminder_count', 0) + 1,
                        opened_at=prior['opened_at'],
                    ))
                else:
                    varsler.append(make_varsel(
                        r, recipient, is_struct,
                        rule='reminder', sub_cat='PÅMINNELSE',
                        priority='informasjon',
                        thread_status='paminnelse',
                        reminder_count=prior.get('reminder_count', 0) + 1,
                        opened_at=prior['opened_at'],
                    ))
                # Oppdater trad
                new_threads[key] = {
                    **prior,
                    'reminder_count': prior.get('reminder_count', 0) + 1,
                    'last_seen_at': SNAPSHOT_T,
                    'last_gap_value': int(r['gap_value_t2']),
                    'last_severity': r['severity_band_t2'],
                }
        else:
            # Ingen tidligere trad
            if not alert:
                continue
            if in_gap_now and is_gap_opening_alert(sub_cat):
                # Apne ny trad
                varsler.append(make_varsel(
                    r, recipient, is_struct,
                    rule=rule, sub_cat=sub_cat, priority=prio,
                    thread_status='ny',
                    reminder_count=0,
                    opened_at=SNAPSHOT_T,
                ))
                new_threads[key] = {
                    'asset_type': r['asset_type'],
                    'asset_tier2': r['asset_tier2'],
                    'week_start': r['week_start'],
                    'opened_at': SNAPSHOT_T,
                    'opening_change_type': r['change_type'],
                    'opening_severity_change': r['severity_change'],
                    'opening_sub_category': sub_cat,
                    'reminder_count': 0,
                    'last_seen_at': SNAPSHOT_T,
                    'last_gap_value': int(r['gap_value_t2']),
                    'last_severity': r['severity_band_t2'],
                    'recipient': recipient,
                }
            else:
                # Informasjons-varsel uten trad (f.eks. SKJULT_LOST_GAP for celle uten tidligere trad)
                varsler.append(make_varsel(
                    r, recipient, is_struct,
                    rule=rule, sub_cat=sub_cat, priority=prio,
                    thread_status='informasjon',
                    reminder_count=0,
                    opened_at=SNAPSHOT_T,
                ))

    # Trader som tidligere var aktive men ikke ble sett (uken har passert kalenderhorisonten)
    # ignoreres per kap 6.2 - ingen varsel og ingen vidererforing.
    return varsler, new_threads


def format_digest(varsler: list[Varsel], cc: str | None) -> str:
    if not varsler:
        return ''
    asset_types = sorted({v.asset_type for v in varsler})
    recipient = varsler[0].recipient
    snapshot_t = varsler[0].snapshot_t
    snapshot_t1 = varsler[0].snapshot_t_minus_1

    out: list[str] = []
    out.append(f'To: {recipient}')
    if cc:
        out.append(f'Cc: {cc}')
    suffix = 'er' if len(varsler) != 1 else ''
    out.append(
        f'Subject: Kapasitetsvarsler {snapshot_t} (Motive Norway) - '
        f'{len(varsler)} endring{suffix}'
    )
    out.append('')
    out.append('Hei,')
    out.append('')
    out.append(
        f'Ukens snapshot ({snapshot_t}) sammenlignet med forrige '
        f'({snapshot_t1}) viser folgende endringer for utstyrsenheter du '
        f'folger opp ({", ".join(asset_types)}):'
    )
    out.append('')

    # Grupper etter thread_status, så etter prioritet
    status_order = ['ny', 'eskalert', 'paminnelse', 'lost', 'informasjon']
    status_labels = {
        'ny': 'NYE VARSLER',
        'eskalert': 'ESKALERTE VARSLER (krever umiddelbar oppfolging)',
        'paminnelse': 'PÅMINNELSER (aktive saker fra tidligere snapshots)',
        'lost': 'LØSTE SAKER (avslutter varslingstrad)',
        'informasjon': 'INFORMASJONSVARSLER',
    }
    by_status: dict[str, list[Varsel]] = defaultdict(list)
    for v in varsler:
        by_status[v.thread_status].append(v)

    for status in status_order:
        vs = by_status.get(status, [])
        if not vs:
            continue
        out.append('-' * 60)
        out.append(f'{status_labels[status]} ({len(vs)})')
        out.append('-' * 60)

        by_asset: dict[str, list[Varsel]] = defaultdict(list)
        for v in vs:
            by_asset[v.asset_tier2].append(v)
        for asset, asset_vs in sorted(by_asset.items()):
            asset_vs = sorted(asset_vs, key=lambda v: v.week_start)
            if len(asset_vs) >= 3:
                weeks = ', '.join(v.week_start for v in asset_vs)
                first_v = asset_vs[0]
                out.append(
                    f'  • {asset} ({first_v.asset_type}) - '
                    f'{len(asset_vs)} sammenhengende uker: {weeks}\n'
                    f'    gap {first_v.gap_t_minus_1} → {first_v.gap_t}, '
                    f'farge {first_v.severity_t_minus_1} → {first_v.severity_t}'
                )
                if status == 'ny':
                    out.append(
                        '    Monster: ny kontrakt har sannsynligvis '
                        'passert 75 %-terskelen for denne perioden.'
                    )
            else:
                for v in asset_vs:
                    detail = f'[{v.sub_category}, {v.rule_triggered}]'
                    if v.reminder_count > 0:
                        detail += f' (uke {v.reminder_count} i tråden, åpnet {v.opened_at})'
                    out.append(
                        f'  • {v.asset_tier2} ({v.asset_type}), '
                        f'uke {v.week_start}:\n'
                        f'    gap {v.gap_t_minus_1} → {v.gap_t}, '
                        f'farge {v.severity_t_minus_1} → {v.severity_t}\n'
                        f'    {detail}'
                    )
        out.append('')

    out.append('Detaljer: varsler.csv (vedlagt)')
    out.append('')
    return '\n'.join(out)


def main() -> None:
    with open(RECIPIENTS_PATH, encoding='utf-8') as f:
        recipients_cfg = yaml.safe_load(f)
    cc = recipients_cfg.pop('cc', None)
    default_recipient = recipients_cfg.pop('default', 'salg@motive-offshore.no')

    df = pd.read_csv(GAP_CHANGES_PATH)
    initial_count = len(df)
    df = df[~df['asset_tier2'].isin(EXCLUSION_LIST)]
    excluded = initial_count - len(df)
    print(f'Forhandsfilter: ekskluderte {excluded} celler '
          f'({len(EXCLUSION_LIST)} enheter)')

    state = load_state()
    existing_threads = state.get('threads', {})
    print(f'Lastet {len(existing_threads)} aktive trader fra state '
          f'(siste kjoring: {state.get("last_run")})')

    varsler, new_threads = generate_varsler(
        df, recipients_cfg, default_recipient, existing_threads
    )

    print(f'\nGenererte {len(varsler)} varsler:')
    by_status = defaultdict(int)
    for v in varsler:
        by_status[v.thread_status] += 1
    for s in ['ny', 'eskalert', 'paminnelse', 'lost', 'informasjon']:
        print(f'  {s:14s} {by_status.get(s, 0)}')

    print(f'\nTrad-tilstand: {len(existing_threads)} -> {len(new_threads)}')

    # Skriv csv
    csv_path = os.path.join(OUT_DIR, 'varsler.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[fld.name for fld in fields(Varsel)])
        writer.writeheader()
        for v in varsler:
            writer.writerow(asdict(v))
    print(f'\nVarsler: {csv_path}')

    # Lagre tilstand
    state['last_run'] = SNAPSHOT_T
    state['threads'] = new_threads
    save_state(state)
    print(f'State: {STATE_PATH}')

    # Digest per mottaker
    by_recipient: dict[str, list[Varsel]] = defaultdict(list)
    for v in varsler:
        by_recipient[v.recipient].append(v)

    digest_dir = os.path.join(OUT_DIR, 'digests')
    os.makedirs(digest_dir, exist_ok=True)
    for old in os.listdir(digest_dir):
        if old.endswith('.txt'):
            os.remove(os.path.join(digest_dir, old))

    print(f'\nDigest-e-poster (snapshot {SNAPSHOT_T}):')
    for recipient, vs in sorted(by_recipient.items()):
        text = format_digest(vs, cc)
        local_part = recipient.split('@')[0]
        filename = f'digest_{SNAPSHOT_T}_{local_part}.txt'
        path = os.path.join(digest_dir, filename)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'  {recipient:50s} {len(vs):3d} varsler -> {filename}')


if __name__ == '__main__':
    main()
