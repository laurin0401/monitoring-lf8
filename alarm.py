"""
alarm.py - Zweistufiges Alarmsystem (Soft- und Hardlimit)
"""

import smtplib
import logging
import socket
import configparser
from datetime import datetime
from email.mime.text import MIMEText

# Konfiguration aus INI-Datei laden
config = configparser.ConfigParser()
config.read('config.ini')

LOG_FILE = config.get('settings', 'log_file', fallback='monitoring.log')
SMTP_SERVER = config.get('smtp', 'server', fallback='smtp.gmail.com')
SMTP_PORT   = config.getint('smtp', 'port', fallback=587)
SMTP_USER   = config.get('smtp', 'user', fallback='')
SMTP_PASS   = config.get('smtp', 'password', fallback='')
EMAIL_TO    = config.get('smtp', 'recipient', fallback='')

# Logging einrichten
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def write_log(message: str):
    """Schreibt eine Meldung in die Logdatei (wird angehängt)."""
    hostname = socket.gethostname()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} | Host: {hostname} | {message}"
    logging.info(f"Host: {hostname} | {message}")
    print(log_entry)


def send_email(subject: str, message: str):
    """Sendet eine E-Mail bei Überschreitung des Hardlimits via SMTP."""
    if not SMTP_USER or not EMAIL_TO:
        print("[WARNUNG] E-Mail-Versand nicht konfiguriert (config.ini prüfen).")
        return

    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From']    = SMTP_USER
        msg['To']      = EMAIL_TO

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, EMAIL_TO, msg.as_string())

        print(f"[E-MAIL] Alarm-Mail erfolgreich gesendet an {EMAIL_TO}")
    except Exception as e:
        print(f"[FEHLER] E-Mail konnte nicht gesendet werden: {e}")


def check_alarm(wert: float, softlimit: float, hardlimit: float, meldungstext: str):
    """
    Prüft einen Messwert gegen Soft- und Hardlimit.

    - Softlimit überschritten → Warnung + Logfile
    - Hardlimit überschritten → Warnung + Logfile + E-Mail

    Args:
        wert:          Aktueller Messwert
        softlimit:     Schwellenwert für Warnung
        hardlimit:     Schwellenwert für kritischen Alarm + E-Mail
        meldungstext:  Beschreibung des Messwertes (z.B. "RAM-Auslastung")
    """
    if wert >= hardlimit:
        nachricht = f"[KRITISCH] {meldungstext}: {wert} (Hardlimit: {hardlimit})"
        write_log(nachricht)
        send_email(
            subject=f"ALARM: {meldungstext} kritisch!",
            message=nachricht
        )

    elif wert >= softlimit:
        nachricht = f"[WARNUNG]  {meldungstext}: {wert} (Softlimit: {softlimit})"
        write_log(nachricht)

    else:
        nachricht = f"[OK]       {meldungstext}: {wert} (Softlimit: {softlimit}, Hardlimit: {hardlimit})"
        write_log(nachricht)
