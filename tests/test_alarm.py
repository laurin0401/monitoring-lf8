"""
test_alarm.py - Automatisierte Tests für das Alarm-Modul
"""

from unittest.mock import patch
from alarm import check_alarm, write_log, send_email


def test_kein_alarm_unter_softlimit(capsys):
    check_alarm(50.0, 80.0, 95.0, "RAM-Test")
    ausgabe = capsys.readouterr().out
    assert "[OK]" in ausgabe


def test_warnung_bei_softlimit(capsys):
    check_alarm(85.0, 80.0, 95.0, "RAM-Test")
    ausgabe = capsys.readouterr().out
    assert "[WARNUNG]" in ausgabe


@patch('alarm.send_email')
def test_kritisch_bei_hardlimit(mock_email, capsys):
    check_alarm(96.0, 80.0, 95.0, "RAM-Test")
    ausgabe = capsys.readouterr().out
    assert "[KRITISCH]" in ausgabe
    mock_email.assert_called_once()


def test_logdatei_wird_geschrieben(tmp_path):
    import alarm
    import logging
    alarm.LOG_FILE = str(tmp_path / 'test.log')
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename=alarm.LOG_FILE, level=logging.INFO)
    write_log("Testmeldung RAM: 90%")
    with open(alarm.LOG_FILE, 'r') as f:
        inhalt = f.read()
    assert "Testmeldung RAM" in inhalt


def test_email_nicht_gesendet_ohne_config(capsys):
    import alarm
    original_user = alarm.SMTP_USER
    alarm.SMTP_USER = ''
    send_email("Test", "Testnachricht")
    ausgabe = capsys.readouterr().out
    assert "nicht konfiguriert" in ausgabe
    alarm.SMTP_USER = original_user
