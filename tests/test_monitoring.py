"""
test_monitoring.py - Automatisierte Tests für das Monitoring-Modul
"""

from unittest.mock import patch
import monitoring


def test_ram_auslastung_gueltig():
    wert = monitoring.get_ram_auslastung()
    assert 0.0 <= wert <= 100.0


def test_disk_auslastung_gueltig():
    wert = monitoring.get_disk_auslastung()
    assert 0.0 <= wert <= 100.0


def test_prozessanzahl_positiv():
    anzahl = monitoring.get_prozessanzahl()
    assert anzahl > 0


def test_eingeloggte_nutzer_ist_liste():
    nutzer = monitoring.get_eingeloggte_nutzer()
    assert isinstance(nutzer, list)


@patch('monitoring.check_alarm')
def test_pruefe_ram_ruft_alarm(mock_alarm):
    monitoring.pruefe_ram()
    mock_alarm.assert_called_once()


@patch('monitoring.check_alarm')
def test_pruefe_disk_ruft_alarm(mock_alarm):
    monitoring.pruefe_disk()
    mock_alarm.assert_called_once()


@patch('monitoring.check_alarm')
def test_pruefe_prozesse_ruft_alarm(mock_alarm):
    monitoring.pruefe_prozesse()
    mock_alarm.assert_called_once()
