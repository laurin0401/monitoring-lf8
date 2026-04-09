# 🖥️ Server Monitoring System

Ein zweistufiges Server-Monitoring-System mit automatischer Alarmfunktion,
entwickelt im Rahmen des Lernfelds 8

---

## 📋 Funktionen

- Überwachung von RAM-Auslastung, Festplattenplatz und Prozessanzahl
- Zweistufiges Alarmsystem (Softlimit → Warnung, Hardlimit → E-Mail)
- Automatische Logdatei mit Datum, Uhrzeit und Hostname
- E-Mail-Benachrichtigung via SMTP bei kritischen Werten
- Konfigurierbare Schwellenwerte über `config.ini`
- CI/CD-Pipeline mit GitHub Actions (Linting, Sicherheitsanalyse, Tests)

---

## ⚙️ Voraussetzungen

- Python 3.11 oder neuer
- pip
- Git

---

## 🚀 Installation

### 1. Repository klonen

```bash
git clone https://github.com/laurin0401/monitoring-lf8.git
cd monitoring-lf8
```

### 2. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 3. Konfiguration einrichten

Kopiere die Beispiel-Konfiguration und passe sie an:

```bash
cp config.ini.example config.ini
```

Öffne `config.ini` und trage deine Werte ein:

```ini
[settings]
log_file = monitoring.log

[limits]
ram_softlimit      = 80.0
ram_hardlimit      = 95.0
disk_softlimit     = 80.0
disk_hardlimit     = 95.0
prozesse_softlimit = 150
prozesse_hardlimit = 200

[smtp]
server    = smtp.gmail.com
port      = 587
user      = DEINE-EMAIL@gmail.com
password  = DEIN-APP-PASSWORT
recipient = EMPFAENGER@gmail.com
```

> ⚠️ **Hinweis:** Bei Gmail kein normales Passwort verwenden!
> Ein App-Passwort erstellen unter:
> [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

---

## ▶️ Verwendung

```bash
# Alle Messungen ausführen
python monitoring.py

# Nur RAM prüfen
python monitoring.py --ram

# Nur Festplatte prüfen
python monitoring.py --disk

# Nur Prozesse prüfen
python monitoring.py --prozesse

# Hilfe anzeigen
python monitoring.py -h
```

### Beispielausgabe
```bash
==================================================
Server-Monitoring | Host: MeinServer
==================================================
RAM-Auslastung : 42.5%
Disk-Auslastung : 95.7%
Prozessanzahl : 278
Eingeloggte User : nutzer
==================================================

[OK] RAM-Auslastung (%): 42.5
[KRITISCH] Disk-Auslastung (%): 95.7 (Hardlimit: 95.0)
[E-MAIL] Alarm-Mail erfolgreich gesendet
```

---

## 🧪 Tests ausführen

```bash
python -m pytest tests/ -v
```

Mit Code-Coverage:

```bash
python -m pytest tests/ --cov=. --cov-report=term
```

---

## 🔧 CI/CD Pipeline

Die GitHub Actions Pipeline führt bei jedem Push automatisch aus:

| Schritt | Tool | Beschreibung |
|---------|------|--------------|
| Linting | flake8 | Code-Qualität prüfen |
| Sicherheit | Bandit | Sicherheitslücken erkennen |
| Unit Tests | pytest | Automatisierte Tests |
| Coverage | pytest-cov | Mindestens 70% Abdeckung |
| Integration | pytest | Integrationstests |

---

## 📦 Abhängigkeiten

- psutil - Systemdaten auslesen
- pytest - Automatisierte Tests
- pytest-cov - Code-Coverage
- flake8 - Code-Qualität
- bandit - Sicherheitsanalyse


---





