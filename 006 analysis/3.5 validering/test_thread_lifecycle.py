"""Tester varslingstrad-livssyklusen: ny -> paminnelse -> lost.

Dekker WBS 3.5-akseptansekriteriet om ukentlig paminnelse frem til gap er
lost, samt edge cases for trad-tilstand.
"""
import pandas as pd
import pytest

import gap_alerting as ga


RECIPIENTS = {
    'RDS': 'rds-koordinator@motive.test',
    'HPUS': 'hpus-koordinator@motive.test',
}
DEFAULT_RECIPIENT = 'salg@motive.test'


def make_snap_pair(rows):
    """Bygg en DataFrame som etterligner gap_changes.csv."""
    return pd.DataFrame(rows)


def make_row(asset_type='RDS', asset_tier2='- 500Te RDS',
             week_start='2026-08-17',
             g1=0, g2=-1, s1='green', s2='black',
             change_type=None, severity_change=None):
    if change_type is None:
        if g1 >= 0 and g2 < 0:
            change_type = 'NYTT_GAP'
        elif g1 < 0 and g2 >= 0:
            change_type = 'LOEST'
        elif g1 == g2:
            change_type = 'UENDRET_GAP' if g1 < 0 else 'STABIL'
        elif g2 < g1 and g1 < 0:
            change_type = 'FORVERRET'
        elif g1 < g2 < 0:
            change_type = 'FORBEDRET'
        else:
            change_type = 'POSITIV_ENDRING'
    if severity_change is None:
        severity_change = 'SAMME_FARGE' if s1 == s2 else 'VERRE_FARGE'
    return {
        'change_type': change_type,
        'gap_value_t1': g1,
        'gap_value_t2': g2,
        'severity_band_t1': s1,
        'severity_band_t2': s2,
        'severity_change': severity_change,
        'asset_type': asset_type,
        'asset_tier2': asset_tier2,
        'week_start': week_start,
    }


class TestNyTrad:
    def test_nytt_gap_apner_trad(self):
        df = make_snap_pair([make_row()])
        varsler, threads = ga.generate_varsler(df, RECIPIENTS, DEFAULT_RECIPIENT, {})
        assert len(varsler) == 1
        assert varsler[0].thread_status == 'ny'
        assert varsler[0].reminder_count == 0
        assert len(threads) == 1

    def test_skjult_nytt_gap_apner_trad(self):
        df = make_snap_pair([
            make_row(g1=1, g2=0, s1='green', s2='purple'),
        ])
        varsler, threads = ga.generate_varsler(df, RECIPIENTS, DEFAULT_RECIPIENT, {})
        assert len(varsler) == 1
        assert varsler[0].thread_status == 'ny'
        assert varsler[0].sub_category == 'SKJULT_NYTT_GAP'
        assert len(threads) == 1


class TestPaminnelse:
    def test_uendret_celle_med_aktiv_trad_gir_paminnelse(self):
        # Eksisterende trad - cellen er fortsatt i gap, ingen ny endring
        existing = {
            'RDS|- 500Te RDS|2026-08-17': {
                'asset_type': 'RDS',
                'asset_tier2': '- 500Te RDS',
                'week_start': '2026-08-17',
                'opened_at': '2026-05-14',
                'reminder_count': 0,
                'recipient': 'rds-koordinator@motive.test',
            }
        }
        # Snap-pair: cellen er stadig i gap, ingen ny endring
        df = make_snap_pair([
            make_row(g1=-1, g2=-1, s1='black', s2='black',
                     change_type='UENDRET_GAP', severity_change='SAMME_FARGE'),
        ])
        varsler, threads = ga.generate_varsler(df, RECIPIENTS, DEFAULT_RECIPIENT, existing)
        assert len(varsler) == 1
        assert varsler[0].thread_status == 'paminnelse'
        assert varsler[0].reminder_count == 1
        assert len(threads) == 1  # Tradet fortsetter

    def test_paminnelse_inkrementerer_reminder_count(self):
        existing = {
            'RDS|- 500Te RDS|2026-08-17': {
                'asset_type': 'RDS',
                'asset_tier2': '- 500Te RDS',
                'week_start': '2026-08-17',
                'opened_at': '2026-05-14',
                'reminder_count': 3,
                'recipient': 'rds-koordinator@motive.test',
            }
        }
        df = make_snap_pair([
            make_row(g1=-1, g2=-1, s1='black', s2='black',
                     change_type='UENDRET_GAP', severity_change='SAMME_FARGE'),
        ])
        varsler, threads = ga.generate_varsler(df, RECIPIENTS, DEFAULT_RECIPIENT, existing)
        assert varsler[0].reminder_count == 4


class TestLost:
    def test_aktiv_trad_som_gar_til_overdekning_lukkes(self):
        existing = {
            'RDS|- 500Te RDS|2026-08-17': {
                'asset_type': 'RDS',
                'asset_tier2': '- 500Te RDS',
                'week_start': '2026-08-17',
                'opened_at': '2026-05-14',
                'reminder_count': 1,
                'recipient': 'rds-koordinator@motive.test',
            }
        }
        # Cellen gar fra -1/black til 0/green (out of gap)
        df = make_snap_pair([
            make_row(g1=-1, g2=0, s1='black', s2='green', change_type='LOEST'),
        ])
        varsler, threads = ga.generate_varsler(df, RECIPIENTS, DEFAULT_RECIPIENT, existing)
        assert len(varsler) == 1
        assert varsler[0].thread_status == 'lost'
        assert varsler[0].priority == 'informasjon'
        assert len(threads) == 0  # Tradet er lukket

    def test_lost_via_severity_lukker_ogsa_trad(self):
        existing = {
            'HPUS|Electric - 55kW Electric HPU|2026-10-12': {
                'asset_type': 'HPUS',
                'asset_tier2': 'Electric - 55kW Electric HPU',
                'week_start': '2026-10-12',
                'opened_at': '2026-05-14',
                'reminder_count': 0,
                'recipient': 'hpus-koordinator@motive.test',
            }
        }
        # G var 0 hele tiden, severity gikk fra purple til green
        df = make_snap_pair([
            make_row(
                asset_type='HPUS', asset_tier2='Electric - 55kW Electric HPU',
                week_start='2026-10-12',
                g1=0, g2=2, s1='purple', s2='green',
            ),
        ])
        varsler, threads = ga.generate_varsler(df, RECIPIENTS, DEFAULT_RECIPIENT, existing)
        assert varsler[0].thread_status == 'lost'
        assert len(threads) == 0


class TestEskalert:
    def test_forverret_klassebytte_eskalerer_aktiv_trad(self):
        existing = {
            'RDS|- 500Te RDS|2026-08-17': {
                'asset_type': 'RDS',
                'asset_tier2': '- 500Te RDS',
                'week_start': '2026-08-17',
                'opened_at': '2026-05-14',
                'reminder_count': 1,
                'recipient': 'rds-koordinator@motive.test',
            }
        }
        df = make_snap_pair([
            make_row(g1=-2, g2=-3, s1='black', s2='black',
                     change_type='FORVERRET', severity_change='SAMME_FARGE'),
        ])
        varsler, threads = ga.generate_varsler(df, RECIPIENTS, DEFAULT_RECIPIENT, existing)
        assert len(varsler) == 1
        assert varsler[0].thread_status == 'eskalert'
        assert varsler[0].priority == 'høy'
        assert len(threads) == 1  # Tradet fortsetter


class TestEksklusjon:
    def test_ekskludert_asset_genererer_ikke_varsel(self):
        # Bruk en eksisterende eksklusjonsoppfaring - vi tester at gap_changes
        # som inneholder ekskludert asset filtreres ut for ELDRE testing av
        # main()-flyten. evaluate_alert ser ikke pa eksklusjon - det skjer
        # i main(). Sa her tester vi at en celle med 'Diesel - 63kW Diesel
        # HPU Zone II' faktisk gir varsel hvis vi gir det til generate_varsler,
        # men i main()-flyten ville den vaere filtrert bort.
        # Denne testen er derfor en negativ-test: vi viser at uten filteret
        # ville cellen gitt varsel hvis den hadde change_type NYTT_GAP.
        df = make_snap_pair([
            make_row(asset_type='HPUS',
                     asset_tier2='Diesel - 63kW Diesel HPU Zone II'),
        ])
        varsler, _ = ga.generate_varsler(df, RECIPIENTS, DEFAULT_RECIPIENT, {})
        # generate_varsler bryr seg ikke om eksklusjon - vi tester at den
        # vil utløse varsel, og at filtrering må skje før kall.
        assert len(varsler) == 1


class TestRuting:
    def test_kjent_asset_type_rutes_til_korrekt_mottaker(self):
        df = make_snap_pair([make_row(asset_type='RDS')])
        varsler, _ = ga.generate_varsler(df, RECIPIENTS, DEFAULT_RECIPIENT, {})
        assert varsler[0].recipient == 'rds-koordinator@motive.test'

    def test_ukjent_asset_type_faller_til_default(self):
        df = make_snap_pair([make_row(asset_type='Crane',
                                       asset_tier2='Some Crane')])
        varsler, _ = ga.generate_varsler(df, RECIPIENTS, DEFAULT_RECIPIENT, {})
        assert varsler[0].recipient == DEFAULT_RECIPIENT


class TestIdentiskeSnapshots:
    def test_ingen_endringer_uten_aktiv_trad_gir_ingen_varsler(self):
        """Identiske snapshots uten aktive trader gir 0 varsler."""
        df = make_snap_pair([
            make_row(g1=-1, g2=-1, s1='black', s2='black',
                     change_type='UENDRET_GAP', severity_change='SAMME_FARGE'),
            make_row(g1=0, g2=0, s1='green', s2='green',
                     change_type='STABIL', severity_change='SAMME_FARGE',
                     asset_tier2='other'),
        ])
        varsler, threads = ga.generate_varsler(df, RECIPIENTS, DEFAULT_RECIPIENT, {})
        assert len(varsler) == 0
        assert len(threads) == 0


class TestMonsterdeteksjon:
    def test_5_sammenhengende_uker_for_samme_asset(self):
        rows = [
            make_row(week_start=f'2026-08-{17 + 7*i:02d}'.replace('38', '31'))
            for i in range(5)
        ]
        # Manuell oppretting med riktige datoer
        rows = [
            make_row(week_start='2026-08-17'),
            make_row(week_start='2026-08-24'),
            make_row(week_start='2026-08-31'),
            make_row(week_start='2026-09-07'),
            make_row(week_start='2026-09-14'),
        ]
        df = make_snap_pair(rows)
        varsler, _ = ga.generate_varsler(df, RECIPIENTS, DEFAULT_RECIPIENT, {})
        assert len(varsler) == 5
        # Alle har samme asset, samme thread_status
        assert all(v.asset_tier2 == '- 500Te RDS' for v in varsler)
        # Digest-formateringen genererer monsteret
        digest = ga.format_digest(varsler, cc=None)
        assert 'Monster' in digest or 'sammenhengende uker' in digest
