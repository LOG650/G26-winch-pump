"""Felles oppsett for pytest.

Legger 3.4-mappa paa sys.path slik at testene kan importere gap_alerting.
"""
import os
import sys

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
ANALYSIS_ROOT = os.path.dirname(THIS_DIR)

sys.path.insert(0, os.path.join(ANALYSIS_ROOT, '3.4 varsling'))
sys.path.insert(0, os.path.join(ANALYSIS_ROOT, '3.3 gap-deteksjon'))
