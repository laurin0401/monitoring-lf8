"""
test_alarm.py - Automatisierte Tests für das Alarm-Modul
"""

import os
import pytest
from unittest.mock import patch, MagicMock
from alarm import check_alarm, write_log, send_email

LOG_TEST = 'test_monitoring.log'


# ─── Test 1: Wert unter Softlimit → kein Alarm ───
def test_kein_alarm_unter_softlimit(capsys):
    check_alarm(50.0, 80.0, 95.0, "RAM-Test")
    ausgabe = capsys.readouterr().out
    assert "[OK]" in ausgabe


# ─── Test 2: Wert über Softlimit → Warnung ───
def test_warnung_bei_softlimit(capsys):
    check_alarm(85.0, 80.0, 95.0, "RAM-Test")
    ausgabe = capsys.readouterr().out
    assert "[WARNUNG]" in ausgabe


# ─── Test 3: Wert über Hardlimit → Kritisch + E-Mail-Versuch ───
@patch('alarm.send_email')
def test_kritisch_bei_hardlimit(mock_email, capsys):
    check_alarm(96.0, 80.0, 95.0, "RAM-Test")
    ausgabe = capsys.readouterr().out
    assert "[KRITISCH]" in ausgabe
    mock_email.assert_called_once()


# ─── Test 4: Logdatei wird beschrieben ───
def test_logdatei_wird_geschrieben(tmp_path):
    import alarm
    original_log = alarm.LOG_FILE
    alarm.LOG_FILE = str(tmp_path / 'test.log')

    import logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename=alarm.LOG_FILE, level=logging.INFO)

    write_log("Testmeldung RAM: 90%")

    with open(alarm.LOG_FILE, 'r') as f:
        inhalt = f.read()
    assert "Testmeldung RAM" in inhalt

    alarm.LOG_FILE = original_log


# ─── Test 5: E-Mail wird nicht gesendet wenn nicht konfiguriert ───
def test_email_nicht_gesendet_ohne_config(capsys):
    import alarm
    original_user = alarm.SMTP_USER
    alarm.SMTP_USER = ''
    send_email("Test", "Testnachricht")
    ausgabe = capsys.readouterr().out
    assert "nicht konfiguriert" in ausgabe
    alarm.SMTP_USER = original_user
