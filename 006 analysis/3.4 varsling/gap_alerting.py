"""3.4 Varslingslogikk - genererer varsler fra gap_changes.csv.

Anvender regelmatrisene i 6.5 (G-baserte + severity-baserte) og rutingen i 6.7.
Bygger varselsobjekter, prioriterer og rute, og genererer digest-tekst per
mottaker per snapshot. Sender ikke faktisk e-post (det krever SMTP-credentials
i .env og er beskrevet i 6.7); skriver til varsler.csv og digests/-mappe.

Kjor: uv run python "3.4 varsling/gap_alerting.py"
"""
import csv
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
OUT_DIR = SCRIPT_DIR

# Eksklusjonsliste (kap 6.6) - enheter som filtreres bort for varsling
EXCLUSION_LIST = {
    'Diesel - 63kW Diesel HPU Zone II',
}

# Suppression-listen (kap 6.5) - manuelt konfigurerte strukturelle assets.
# Tom som default fordi K=4-kriteriet ikke kan eksercereres innenfor
# prosjektperioden (jf. 9.3). Kandidater fra front-lastet-analysen i 7.5
# kan legges inn etter koordinatorbekreftelse.
STRUCTURAL_ASSETS: set[str] = set()

OVERDEKNING = {'green', 'yellow', 'red'}
UNDERDEKNING = {'purple', 'black'}


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
    """Klassifiser severity-overgang per Tabell 6.5."""
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
    """Avgjor om en celle utloser varsel per Tabell 6.4 og 6.5.

    Returnerer (alert, rule, sub_category, priority).
    """
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

    # Tabell 6.5 - severity-supplement nar G-regelen ikke utloste varsel
    sct = severity_cross(s1, s2)
    if sct == 'SKJULT_NYTT_GAP':
        return True, 'severity-regel', sct, 'middels'
    if sct == 'SKJULT_FORVERRING':
        return True, 'severity-regel', sct, 'høy'
    if sct == 'SKJULT_LOST_GAP':
        return True, 'severity-regel', sct, 'informasjon'

    return False, '', '', ''


def format_digest(varsler: list[Varsel], cc: str | None) -> str:
    if not varsler:
        return ''

    asset_types = sorted({v.asset_type for v in varsler})
    snapshot_t = varsler[0].snapshot_t
    snapshot_t_minus_1 = varsler[0].snapshot_t_minus_1
    recipient = varsler[0].recipient

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
        f'({snapshot_t_minus_1}) viser folgende endringer for utstyrsenheter '
        f'du folger opp ({", ".join(asset_types)}):'
    )
    out.append('')

    by_prio: dict[str, list[Varsel]] = defaultdict(list)
    for v in varsler:
        by_prio[v.priority].append(v)

    prio_order = ['høy', 'middels', 'lav', 'informasjon']
    prio_labels = {
        'høy': 'HØY PRIORITET',
        'middels': 'MIDDELS PRIORITET',
        'lav': 'LAV PRIORITET',
        'informasjon': 'INFORMASJONSVARSLER',
    }

    for prio in prio_order:
        vs = by_prio.get(prio, [])
        if not vs:
            continue
        out.append('-' * 60)
        out.append(f'{prio_labels[prio]} ({len(vs)})')
        out.append('-' * 60)
        # Grupper per asset for monsterdeteksjon
        by_asset: dict[str, list[Varsel]] = defaultdict(list)
        for v in vs:
            by_asset[v.asset_tier2].append(v)
        for asset, asset_vs in sorted(by_asset.items()):
            asset_vs = sorted(asset_vs, key=lambda v: v.week_start)
            if len(asset_vs) >= 3:
                weeks = ', '.join(v.week_start for v in asset_vs)
                first_v = asset_vs[0]
                out.append(
                    f'  • {asset} ({first_v.asset_type}) - {len(asset_vs)} '
                    f'sammenhengende uker: {weeks}\n'
                    f'    gap {first_v.gap_t_minus_1} → {first_v.gap_t}, '
                    f'farge {first_v.severity_t_minus_1} → {first_v.severity_t}\n'
                    f'    Monster: ny kontrakt har sannsynligvis passert '
                    f'75 %-terskelen for denne perioden.'
                )
            else:
                for v in asset_vs:
                    out.append(
                        f'  • {v.asset_tier2} ({v.asset_type}), '
                        f'uke {v.week_start}:\n'
                        f'    gap {v.gap_t_minus_1} → {v.gap_t}, '
                        f'farge {v.severity_t_minus_1} → {v.severity_t}\n'
                        f'    [{v.sub_category}, {v.rule_triggered}]'
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

    # Snapshot-datoer (alle rader har samme snapshot-par)
    # gap_changes.csv inneholder ikke eksplicitte snapshot-datoer.
    # Hardkodes her - utvidelse: les fra metadata.
    SNAPSHOT_T = '2026-05-14'
    SNAPSHOT_T1 = '2026-05-07'

    varsler: list[Varsel] = []
    for _, row in df.iterrows():
        row_dict = row.to_dict()
        is_struct = row_dict['asset_tier2'] in STRUCTURAL_ASSETS
        alert, rule, sub_cat, prio = evaluate_alert(row_dict, is_struct)
        if not alert:
            continue

        recipient = recipients_cfg.get(row_dict['asset_type'], default_recipient)
        v = Varsel(
            snapshot_t=SNAPSHOT_T,
            snapshot_t_minus_1=SNAPSHOT_T1,
            week_start=row_dict['week_start'],
            region='Motive Norway',
            asset_type=row_dict['asset_type'],
            asset_tier2=row_dict['asset_tier2'],
            gap_t_minus_1=int(row_dict['gap_value_t1']),
            gap_t=int(row_dict['gap_value_t2']),
            severity_t_minus_1=row_dict['severity_band_t1'],
            severity_t=row_dict['severity_band_t2'],
            change_type=row_dict['change_type'],
            severity_change=row_dict['severity_change'],
            rule_triggered=rule,
            sub_category=sub_cat,
            magnitude_class=magnitude_class(int(row_dict['gap_value_t2'])),
            priority=prio,
            is_structural=is_struct,
            recipient=recipient,
        )
        varsler.append(v)

    print(f'Genererte {len(varsler)} varsler totalt.')

    # Oppsummering per regel og prioritet
    by_rule = defaultdict(int)
    by_prio = defaultdict(int)
    for v in varsler:
        by_rule[v.rule_triggered] += 1
        by_prio[v.priority] += 1
    print('\nFordeling per regel:')
    for r, c in sorted(by_rule.items()):
        print(f'  {r:18s} {c}')
    print('\nFordeling per prioritet:')
    for p in ['høy', 'middels', 'lav', 'informasjon']:
        print(f'  {p:14s} {by_prio.get(p, 0)}')

    # Skriv komplett varselsliste
    csv_path = os.path.join(OUT_DIR, 'varsler.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[fld.name for fld in fields(Varsel)])
        writer.writeheader()
        for v in varsler:
            writer.writerow(asdict(v))
    print(f'\nKomplett varselsliste: {csv_path}')

    # Grupper og generer digest per mottaker
    by_recipient: dict[str, list[Varsel]] = defaultdict(list)
    for v in varsler:
        by_recipient[v.recipient].append(v)

    digest_dir = os.path.join(OUT_DIR, 'digests')
    os.makedirs(digest_dir, exist_ok=True)
    for old in os.listdir(digest_dir):
        if old.endswith('.txt'):
            os.remove(os.path.join(digest_dir, old))

    print(f'\nDigest-e-poster (per mottaker, snapshot {SNAPSHOT_T}):')
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
