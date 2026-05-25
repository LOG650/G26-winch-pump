"""Tester evaluate_alert mot Tabell 6.4 (G-regel) og Tabell 6.5 (severity-regel).

Dekker akseptansekriteriene fra WBS 3.5 om at modellen identifiserer ulike
endringstyper korrekt.
"""
import pytest

import gap_alerting as ga


def make_row(g1, g2, s1='green', s2='green', change_type=None,
             severity_change=None, asset_type='RDS',
             asset_tier2='- 500Te RDS', week_start='2026-08-17'):
    """Bygger en syntetisk gap_changes-rad."""
    if change_type is None:
        if g1 >= 0 and g2 >= 0:
            change_type = 'STABIL' if g1 == g2 else 'POSITIV_ENDRING'
        elif g1 >= 0 and g2 < 0:
            change_type = 'NYTT_GAP'
        elif g1 < 0 and g2 >= 0:
            change_type = 'LOEST'
        elif g1 == g2:
            change_type = 'UENDRET_GAP'
        elif g2 < g1:
            change_type = 'FORVERRET'
        else:
            change_type = 'FORBEDRET'
    if severity_change is None:
        if s1 == s2:
            severity_change = 'SAMME_FARGE'
        elif ga.SEV_ORDER[s2] > ga.SEV_ORDER[s1] if hasattr(ga, 'SEV_ORDER') else False:
            severity_change = 'BEDRE_FARGE'
        else:
            order = {'black': 0, 'purple': 1, 'red': 2, 'yellow': 3, 'green': 4}
            severity_change = 'BEDRE_FARGE' if order[s2] > order[s1] else 'VERRE_FARGE'
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


# ============================================================
# Tabell 6.4 - G-regel
# ============================================================


class TestNyttGap:
    def test_nytt_gap_mildt_gir_middels_prioritet(self):
        row = make_row(g1=0, g2=-1, s1='green', s2='black')
        alert, rule, sub_cat, prio = ga.evaluate_alert(row, is_structural=False)
        assert alert
        assert rule == 'G-regel'
        assert sub_cat == 'NYTT_GAP'
        assert prio == 'middels'

    def test_nytt_gap_moderat_gir_hoy_prioritet(self):
        row = make_row(g1=0, g2=-3, s1='green', s2='black')
        alert, rule, sub_cat, prio = ga.evaluate_alert(row, is_structural=False)
        assert alert
        assert prio == 'høy'

    def test_nytt_gap_kritisk_gir_hoy_prioritet(self):
        row = make_row(g1=0, g2=-7, s1='green', s2='black')
        alert, rule, sub_cat, prio = ga.evaluate_alert(row, is_structural=False)
        assert alert
        assert prio == 'høy'

    def test_nytt_gap_trigger_ogsa_for_strukturell(self):
        """Per Tabell 6.4 utloser nytt gap varsel uansett strukturell-status."""
        row = make_row(g1=0, g2=-1, s1='green', s2='black')
        alert, _, _, _ = ga.evaluate_alert(row, is_structural=True)
        assert alert


class TestForverret:
    def test_forverret_klassebytte_gir_hoy_prioritet(self):
        row = make_row(g1=-2, g2=-3, change_type='FORVERRET')  # mildt -> moderat
        alert, rule, sub_cat, prio = ga.evaluate_alert(row, is_structural=False)
        assert alert
        assert sub_cat == 'FORVERRET_KLASSEBYTTE'
        assert prio == 'høy'

    def test_forverret_innen_klasse_gir_lav_prioritet(self):
        row = make_row(g1=-1, g2=-2, change_type='FORVERRET')  # mildt -> mildt
        alert, rule, sub_cat, prio = ga.evaluate_alert(row, is_structural=False)
        assert alert
        assert sub_cat == 'FORVERRET_INNEN_KLASSE'
        assert prio == 'lav'

    def test_forverret_innen_klasse_for_strukturell_loggfores(self):
        row = make_row(g1=-1, g2=-2, change_type='FORVERRET')
        alert, _, _, _ = ga.evaluate_alert(row, is_structural=True)
        assert not alert

    def test_forverret_klassebytte_for_strukturell_utloser_varsel(self):
        row = make_row(g1=-2, g2=-3, change_type='FORVERRET')
        alert, _, sub_cat, prio = ga.evaluate_alert(row, is_structural=True)
        assert alert
        assert sub_cat == 'FORVERRET_KLASSEBYTTE'


class TestLoest:
    def test_loest_gap_gir_informasjon(self):
        row = make_row(g1=-1, g2=0, s1='black', s2='green', change_type='LOEST')
        alert, rule, sub_cat, prio = ga.evaluate_alert(row, is_structural=False)
        assert alert
        assert sub_cat == 'LOEST'
        assert prio == 'informasjon'


class TestStabilUtenEndring:
    def test_stabil_uten_severity_endring_gir_ikke_varsel(self):
        row = make_row(g1=0, g2=0, s1='green', s2='green',
                       severity_change='SAMME_FARGE')
        alert, _, _, _ = ga.evaluate_alert(row, is_structural=False)
        assert not alert

    def test_uendret_gap_uten_severity_endring_gir_ikke_varsel(self):
        row = make_row(g1=-1, g2=-1, s1='black', s2='black',
                       severity_change='SAMME_FARGE')
        alert, _, _, _ = ga.evaluate_alert(row, is_structural=False)
        assert not alert


# ============================================================
# Tabell 6.5 - severity-regel
# ============================================================


class TestSeverityRegel:
    def test_skjult_nytt_gap_green_til_purple_gir_middels(self):
        row = make_row(g1=1, g2=0, s1='green', s2='purple',
                       severity_change='VERRE_FARGE')
        alert, rule, sub_cat, prio = ga.evaluate_alert(row, is_structural=False)
        assert alert
        assert rule == 'severity-regel'
        assert sub_cat == 'SKJULT_NYTT_GAP'
        assert prio == 'middels'

    def test_skjult_nytt_gap_yellow_til_black_gir_middels(self):
        row = make_row(g1=1, g2=0, s1='yellow', s2='black',
                       severity_change='VERRE_FARGE')
        alert, _, sub_cat, _ = ga.evaluate_alert(row, is_structural=False)
        assert alert
        assert sub_cat == 'SKJULT_NYTT_GAP'

    def test_skjult_forverring_purple_til_black_gir_hoy(self):
        row = make_row(g1=-1, g2=-1, s1='purple', s2='black',
                       severity_change='VERRE_FARGE')
        alert, rule, sub_cat, prio = ga.evaluate_alert(row, is_structural=False)
        assert alert
        assert sub_cat == 'SKJULT_FORVERRING'
        assert prio == 'høy'

    def test_skjult_lost_gap_purple_til_green_gir_informasjon(self):
        row = make_row(g1=0, g2=2, s1='purple', s2='green',
                       severity_change='BEDRE_FARGE')
        alert, _, sub_cat, prio = ga.evaluate_alert(row, is_structural=False)
        assert alert
        assert sub_cat == 'SKJULT_LOST_GAP'
        assert prio == 'informasjon'

    def test_skjult_forbedring_black_til_purple_loggfores(self):
        """Tabell 6.5: svart -> lilla loggfores, ikke varsel."""
        row = make_row(g1=-1, g2=-1, s1='black', s2='purple',
                       severity_change='BEDRE_FARGE')
        alert, _, _, _ = ga.evaluate_alert(row, is_structural=False)
        assert not alert

    def test_innen_overdekning_sone_gir_ikke_varsel(self):
        row = make_row(g1=3, g2=2, s1='green', s2='yellow',
                       severity_change='VERRE_FARGE')
        alert, _, _, _ = ga.evaluate_alert(row, is_structural=False)
        assert not alert


# ============================================================
# Severity-cross-hjelper
# ============================================================


class TestSeverityCross:
    @pytest.mark.parametrize('s1,s2,expected', [
        ('green', 'purple', 'SKJULT_NYTT_GAP'),
        ('green', 'black', 'SKJULT_NYTT_GAP'),
        ('yellow', 'purple', 'SKJULT_NYTT_GAP'),
        ('red', 'black', 'SKJULT_NYTT_GAP'),
        ('purple', 'green', 'SKJULT_LOST_GAP'),
        ('black', 'green', 'SKJULT_LOST_GAP'),
        ('black', 'yellow', 'SKJULT_LOST_GAP'),
        ('purple', 'black', 'SKJULT_FORVERRING'),
        ('black', 'purple', 'SKJULT_FORBEDRING'),
        ('green', 'green', None),
        ('green', 'yellow', None),
        ('yellow', 'red', None),
        ('purple', 'purple', None),
    ])
    def test_alle_overganger(self, s1, s2, expected):
        assert ga.severity_cross(s1, s2) == expected


# ============================================================
# Magnitudeklasse-hjelper
# ============================================================


class TestMagnitudeClass:
    @pytest.mark.parametrize('gap,expected', [
        (5, 'ingen'),
        (0, 'ingen'),
        (-1, 'mildt'),
        (-2, 'mildt'),
        (-3, 'moderat'),
        (-5, 'moderat'),
        (-6, 'kritisk'),
        (-13, 'kritisk'),
    ])
    def test_magnitudeklasser(self, gap, expected):
        assert ga.magnitude_class(gap) == expected
