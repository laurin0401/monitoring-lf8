"""
test_monitoring.py - Automatisierte Tests für das Monitoring-Modul
"""

import pytest
from unittest.mock import patch
import monitoring


# ─── Test 1: RAM-Auslastung ist ein gültiger Prozentwert ───
def test_ram_auslastung_gueltig():
    wert = monitoring.get_ram_auslastung()
    assert 0.0 <= wert <= 100.0


# ─── Test 2: Disk-Auslastung ist ein gültiger Prozentwert ───
def test_disk_auslastung_gueltig():
    wert = monitoring.get_disk_auslastung()
    assert 0.0 <= wert <= 100.0


# ─── Test 3: Prozessanzahl ist größer als 0 ───
def test_prozessanzahl_positiv():
    anzahl = monitoring.get_prozessanzahl()
    assert anzahl > 0


# ─── Test 4: Eingeloggte Nutzer gibt eine Liste zurück ───
def test_eingeloggte_nutzer_ist_liste():
    nutzer = monitoring.get_eingeloggte_nutzer()
    assert isinstance(nutzer, list)


# ─── Test 5: pruefe_ram ruft check_alarm auf ───
@patch('monitoring.check_alarm')
def test_pruefe_ram_ruft_alarm(mock_alarm):
    monitoring.pruefe_ram()
    mock_alarm.assert_called_once()


# ─── Test 6: pruefe_disk ruft check_alarm auf ───
@patch('monitoring.check_alarm')
def test_pruefe_disk_ruft_alarm(mock_alarm):
    monitoring.pruefe_disk()
    mock_alarm.assert_called_once()


# ─── Test 7: pruefe_prozesse ruft check_alarm auf ───
@patch('monitoring.check_alarm')
def test_pruefe_prozesse_ruft_alarm(mock_alarm):
    monitoring.pruefe_prozesse()
    mock_alarm.assert_called_once()
