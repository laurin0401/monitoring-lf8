"""
monitoring.py - Erfasst Systemdaten und übergibt sie an das Alarmsystem.

Verwendung:
  python monitoring.py              → alle Messungen ausführen
  python monitoring.py --ram        → nur RAM prüfen
  python monitoring.py --disk       → nur Festplattenplatz prüfen
  python monitoring.py --prozesse   → nur Prozessanzahl prüfen
  python monitoring.py -h           → Hilfe anzeigen
"""

import psutil
import socket
import configparser
import argparse
from alarm import check_alarm

# Konfiguration aus INI-Datei laden
config = configparser.ConfigParser()
config.read('config.ini')

# Schwellenwerte aus config.ini lesen
RAM_SOFT     = config.getfloat('limits', 'ram_softlimit',      fallback=80.0)
RAM_HARD     = config.getfloat('limits', 'ram_hardlimit',      fallback=95.0)
DISK_SOFT    = config.getfloat('limits', 'disk_softlimit',     fallback=80.0)
DISK_HARD    = config.getfloat('limits', 'disk_hardlimit',     fallback=95.0)
PROC_SOFT    = config.getfloat('limits', 'prozesse_softlimit', fallback=150.0)
PROC_HARD    = config.getfloat('limits', 'prozesse_hardlimit', fallback=200.0)


def get_ram_auslastung() -> float:
    """Gibt die aktuelle RAM-Auslastung in Prozent zurück."""
    return psutil.virtual_memory().percent


def get_disk_auslastung(pfad: str = '/') -> float:
    """Gibt die Festplattenauslastung des angegebenen Pfades in Prozent zurück."""
    return psutil.disk_usage(pfad).percent


def get_prozessanzahl() -> int:
    """Gibt die Anzahl der aktuell laufenden Prozesse zurück."""
    return len(psutil.pids())


def get_eingeloggte_nutzer() -> list:
    """Gibt eine Liste der aktuell eingeloggten Nutzer zurück."""
    return [user.name for user in psutil.users()]


def ausgabe_systeminfo():
    """Gibt allgemeine Systeminformationen auf der Konsole aus."""
    print(f"\n{'='*50}")
    print(f"  Server-Monitoring | Host: {socket.gethostname()}")
    print(f"{'='*50}")
    print(f"  RAM-Auslastung   : {get_ram_auslastung()} %")
    print(f"  Disk-Auslastung  : {get_disk_auslastung()} %")
    print(f"  Prozessanzahl    : {get_prozessanzahl()}")
    print(f"  Eingeloggte User : {', '.join(get_eingeloggte_nutzer()) or 'Keine'}")
    print(f"{'='*50}\n")


def pruefe_ram():
    """Erfasst RAM-Auslastung und übergibt sie an das Alarmsystem."""
    wert = get_ram_auslastung()
    check_alarm(wert, RAM_SOFT, RAM_HARD, "RAM-Auslastung (%)")


def pruefe_disk():
    """Erfasst Festplattenauslastung und übergibt sie an das Alarmsystem."""
    wert = get_disk_auslastung()
    check_alarm(wert, DISK_SOFT, DISK_HARD, "Disk-Auslastung (%)")


def pruefe_prozesse():
    """Erfasst Prozessanzahl und übergibt sie an das Alarmsystem."""
    wert = get_prozessanzahl()
    check_alarm(wert, PROC_SOFT, PROC_HARD, "Anzahl Prozesse")


# ─── Hauptprogramm mit Kommandozeilenparametern ───
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Server-Monitoring mit zweistufigem Alarmsystem',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--ram',      action='store_true', help='RAM-Auslastung prüfen')
    parser.add_argument('--disk',     action='store_true', help='Festplattenplatz prüfen')
    parser.add_argument('--prozesse', action='store_true', help='Prozessanzahl prüfen')
    parser.add_argument('--info',     action='store_true', help='Systeminfo anzeigen')

    args = parser.parse_args()

    # Wenn keine Parameter → alles ausführen
    alles = not any(vars(args).values())

    ausgabe_systeminfo()

    if args.ram or alles:
        pruefe_ram()
    if args.disk or alles:
        pruefe_disk()
    if args.prozesse or alles:
        pruefe_prozesse()
