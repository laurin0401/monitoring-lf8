# Projektdokumentation – Server Monitoring System

**Ausbildungsbereich:** Fachinformatik / Anwendungsentwicklung  
**Auftraggeber:** IT-Solutions  
**Abgabedatum:** April 2026  
**Bearbeiterin:** Joanna Casper

---

## Abkürzungsverzeichnis

| Abkürzung | Bedeutung |
|-----------|-----------|
| CI        | Continuous Integration |
| CD        | Continuous Deployment |
| SDLC      | Software Development Life Cycle |
| SMTP      | Simple Mail Transfer Protocol |
| INI       | Initialization (Konfigurationsdateiformat) |
| QA        | Quality Assurance (Qualitätssicherung) |
| MoSCoW    | Must have, Should have, Could have, Won't have |
| RAM       | Random Access Memory |
| CPU       | Central Processing Unit |
| PR        | Pull Request |

---

## 1. Einleitung

### 1.1 Projektbeschreibung

Die IT-Solutions betreut eine Vielzahl von Hamburger Unternehmen im IT-Bereich. Ein Kunde hat den Bedarf geäußert, seine Serverinfrastruktur automatisiert überwachen zu lassen. Ziel ist es, bei Engpässen oder kritischen Systemzuständen frühzeitig benachrichtigt zu werden, bevor es zu ernsthaften Ausfällen kommt.

Im Rahmen dieses Projekts wurde ein zweiteiliges System entwickelt: ein **Alarm-Modul** (`alarm.py`) für die Grenzwertüberwachung und ein **Monitoring-Modul** (`monitoring.py`) für die Erfassung der Systemparameter. Beide Module werden durch eine automatisierte CI/CD-Pipeline begleitet, die Qualitätssicherung und Deployment unterstützt.

### 1.2 Projektziel

Das Ziel des Projekts ist die Entwicklung eines zweistufigen Alarmsystems (Soft- und Hardlimit), das folgende Systemparameter überwacht:

- RAM-Auslastung
- Festplattenauslastung (Dateisystem)
- Anzahl der laufenden Prozesse
- Eingeloggte Benutzer (Logging)

Bei Überschreitung des Softlimits wird eine Warnung in eine Logdatei geschrieben. Bei Überschreitung des Hardlimits wird zusätzlich eine E-Mail per SMTP versendet.

### 1.3 Projektbegründung

Eine frühzeitige Fehlererkennung in Serverumgebungen verhindert ungeplante Ausfälle und reduziert den manuellen Überwachungsaufwand. Durch ein automatisiertes Monitoring-System kann der Administrator sofort auf kritische Zustände reagieren, ohne dauerhaft manuell prüfen zu müssen. Die Einbindung in eine CI/CD-Pipeline stellt außerdem die kontinuierliche Codequalität sicher.

### 1.4 Projektabgrenzung

- Die visuelle Darstellung der Messdaten (Dashboard/Frontend) ist **nicht** Bestandteil dieses Projekts.
- Die dauerhafte Betrieb in einer Produktivumgebung ist ein optionaler Aspekt (Could have).
- Schulungen für Endanwender sind nicht vorgesehen.

---

## 2. Projektplanung

### 2.1 MoSCoW-Anforderungen

| Priorität     | Anforderung |
|---------------|-------------|
| **Must have** | CI-Pipeline mit automatisierten Unit Tests, Sequenzdiagramm, Klassendiagramm, Logdatei, Schwellenwertprüfung (Soft-/Hardlimit) |
| **Should have** | Zwei Module (alarm.py + monitoring.py), mindestens 3 QA-Maßnahmen, Integrationstests, E-Mail-Versand, INI-Konfigurationsdatei |
| **Could have** | Continuous Deployment, plattformunabhängige Module, 5+ automatisierte Tests |

### 2.2 Zeitplanung

| Phase | Tätigkeit | Dauer |
|-------|-----------|-------|
| 1 | Planung, Anforderungsanalyse, SDLC-Konzept | 1 Woche |
| 2 | Implementierung alarm.py und monitoring.py | 2 Wochen |
| 3 | Aufbau CI/CD-Pipeline (GitHub Actions) | 1 Woche |
| 4 | Tests, QA-Maßnahmen, Fehlerbehebung | 1 Woche |
| 5 | Dokumentation und Abgabe | 1 Woche |

### 2.3 Entwicklungsprozess

Die Entwicklung erfolgte iterativ nach dem **Scrum-Prinzip** mit wöchentlichen Sprints. Aufgaben wurden als GitHub Issues angelegt, priorisiert und im Sprint-Board verwaltet. Nach jedem Sprint wurde eine Retrospektive durchgeführt, um den Prozess zu reflektieren und zu verbessern.

---

## 3. Analysephase

### 3.1 Ist-Analyse

Der Kunde verfügt aktuell über keine automatisierte Serverüberwachung. Systemparameter wie RAM-Auslastung, Prozessanzahl und Festplattennutzung werden nicht kontinuierlich geprüft. Probleme werden erst erkannt, wenn es bereits zu Ausfällen oder Leistungseinbußen gekommen ist. Es fehlt ein zuverlässiges Benachrichtigungssystem.

### 3.2 Soll-Konzept

Das neue System soll:

- Systemparameter automatisiert und in regelmäßigen Abständen erfassen
- Messwerte gegen konfigurierbare Schwellenwerte (Soft- und Hardlimit) prüfen
- Warnungen in einer Logdatei festhalten
- Bei kritischen Zuständen (Hardlimit) eine E-Mail per SMTP versenden
- Über eine INI-Datei konfigurierbar sein (Schwellenwerte, SMTP-Zugangsdaten)
- Über Kommandozeilenparameter steuerbar sein (`--help`)

### 3.3 Risikoanalyse

| Risiko | Eintrittswahrscheinlichkeit | Gegenmaßnahme |
|--------|-----------------------------|---------------|
| SMTP-Konfiguration schlägt fehl | Mittel | Fehlerbehandlung mit try/except, Testmodus |
| Plattformabhängigkeit (Linux/Windows) | Hoch | psutil als plattformunabhängige Bibliothek |
| Falsche Schwellenwerte | Mittel | Konfiguration per INI-Datei, leicht anpassbar |
| Testabdeckung unzureichend | Niedrig | pytest --cov mit Mindestziel 70 % |

---

## 4. Entwurfsphase

### 4.1 Zielplattform

Das System ist eine **Python-Kommandozeilenanwendung**, die auf Linux- und Windows-Servern lauffähig ist. Die Bibliothek `psutil` wird für plattformunabhängige Systemabfragen genutzt. Konfigurationen werden über eine `config.ini`-Datei eingelesen.

### 4.2 Architekturdesign

Das System besteht aus zwei voneinander getrennten Modulen:

- **`alarm.py`** – Enthält die Alarmlogik: Grenzwertprüfung, Logging und E-Mail-Versand
- **`monitoring.py`** – Erfasst Systemdaten (RAM, Disk, Prozesse, Benutzer) und übergibt sie an `alarm.py`

Die Module kommunizieren über direkte Funktionsaufrufe. Konfigurationswerte (Schwellenwerte, SMTP-Daten) werden aus der `config.ini` geladen.

### 4.3 Klassendiagramm

Das folgende Klassendiagramm zeigt die Struktur der beiden Module sowie ihre Abhängigkeiten zu externen Klassen:

*(Klassendiagramm: siehe Anhang A.1)*

### 4.4 Maßnahmen zur Qualitätssicherung

Folgende drei QA-Maßnahmen wurden implementiert:

1. **Linting mit flake8** – Statische Codeanalyse auf PEP-8-Konformität (`--max-line-length=100`)
2. **Sicherheitsanalyse mit Bandit** – Automatischer Scan auf bekannte Sicherheitsschwachstellen im Python-Code
3. **Code Coverage mit pytest-cov** – Messung der Testabdeckung, Mindestziel: 70 %

### 4.5 Sequenzdiagramm der CI/CD-Pipeline

Das Sequenzdiagramm zeigt den vollständigen Ablauf vom `git push` bis zum Deployment:

*(Sequenzdiagramm: siehe Anhang A.2)*

---

## 5. Implementierungsphase

### 5.1 Modul alarm.py

Das Modul `alarm.py` übernimmt die gesamte Alarmlogik. Die Funktion `check_alarm()` empfängt einen Messwert sowie Soft- und Hardlimit und entscheidet, welche Aktion ausgelöst wird:

- **Wert ≤ Softlimit** → OK-Meldung in die Logdatei
- **Wert > Softlimit** → Warnung in die Logdatei
- **Wert > Hardlimit** → Warnung + E-Mail via SMTP

Die Funktion `write_log()` schreibt Einträge mit Zeitstempel, Hostname, Meldungstext und aktuellem Messwert an das Ende der Logdatei. Die Funktion `send_email()` versendet E-Mails über einen konfigurierten SMTP-Server.

### 5.2 Modul monitoring.py

Das Modul `monitoring.py` erfasst Systemdaten mithilfe der Bibliothek `psutil` und übergibt sie an `alarm.py`. Folgende Parameter werden überwacht:

- **RAM-Auslastung** (`psutil.virtual_memory()`)
- **Festplattenauslastung** (`psutil.disk_usage()`)
- **Anzahl laufender Prozesse** (`psutil.pids()`)
- **Eingeloggte Benutzer** (`psutil.users()`) – nur Logging, kein Alarm

### 5.3 Konfiguration (config.ini)

Alle Schwellenwerte und SMTP-Zugangsdaten werden aus einer `config.ini` ausgelesen:

```ini
[settings]
log_file = monitoring.log

[limits]
ram_softlimit = 80
ram_hardlimit = 90
disk_softlimit = 80
disk_hardlimit = 95
prozesse_softlimit = 150
prozesse_hardlimit = 200

[smtp]
server = smtp.example.com
port = 587
user = user@example.com
password = geheim
recipient = admin@example.com
```

### 5.4 Tests der Anwendung

Es wurden folgende automatisierte Tests mit `pytest` implementiert:

| Testdatei | Testanzahl | Testtyp | Inhalt |
|-----------|-----------|---------|--------|
| `test_alarm.py` | 5 | Unit Test | check_alarm(), write_log(), send_email() |
| `test_monitoring.py` | 7 | Integrationstest | Zusammenspiel alarm.py + monitoring.py |

Die Tests werden in der CI-Umgebung automatisch bei jedem `git push` ausgeführt.

---

## 6. CI/CD-Pipeline

### 6.1 Pipeline-Aufbau (GitHub Actions)

Die Pipeline ist in einer `.github/workflows/ci.yml`-Datei definiert und wird bei jedem Push auf den `main`-Branch automatisch ausgelöst. Sie durchläuft folgende Schritte in dieser Reihenfolge:

1. **flake8 Linting** – Codequalitätsprüfung
2. **Bandit Sicherheitsscan** – Sicherheitsanalyse
3. **pytest Unit Tests** – `test_alarm.py`
4. **pytest --cov Coverage-Prüfung** – Testabdeckung ≥ 70 %
5. **pytest Integrationstests** – `test_monitoring.py`
6. **Deployment auf main-Branch** – (Could have, optional)

### 6.2 Open Source vs. Proprietäre Software

Für die Pipeline und Software wurden ausschließlich **Open-Source-Lösungen** eingesetzt:

| Tool | Typ | Begründung |
|------|-----|------------|
| Python | Open Source | Weite Verbreitung, kostenlos, plattformübergreifend |
| GitHub Actions | Freemium (Open Source Kernfunktion) | Direkte Integration in das Repository |
| pytest / flake8 / Bandit | Open Source | Industriestandard für Python-QA |
| psutil | Open Source | Plattformunabhängige Systemabfragen |

**Vorteile:** Keine Lizenzkosten, freie Anpassbarkeit, große Community.  
**Risiken (Lock-in):** GitHub Actions bindet den Entwicklungsprozess an die GitHub-Plattform. Ein Wechsel zu GitLab CI oder Jenkins wäre jedoch mit überschaubarem Aufwand möglich, da YAML-basierte Pipeline-Definitionen leicht portierbar sind.

---

## 7. Iterativer Softwarelebenszyklus (Scrum)

### 7.1 Scrum-Rollen

| Rolle | Person | Beschreibung |
|-------|--------|-------------|
| Product Owner | Lehrerteam | Definiert Anforderungen (MoSCoW), nimmt ab |
| Scrum Master | — | Nicht explizit besetzt (Einzelprojekt) |
| Developer | Joanna Casper | Planung, Implementierung, Tests, Dokumentation |

### 7.2 Sprint-Planung

Die Entwicklung wurde in **wöchentliche Sprints** unterteilt. Aufgaben wurden als GitHub Issues angelegt und dem Sprint-Board zugewiesen. Am Ende jedes Sprints fand eine kurze Retrospektive statt:

- **Sprint 1:** Anforderungsanalyse, SDLC-Planung, Pipeline-Grundgerüst
- **Sprint 2:** Implementierung alarm.py, erste Unit Tests
- **Sprint 3:** Implementierung monitoring.py, INI-Konfiguration
- **Sprint 4:** QA-Maßnahmen, Integrationstests, Fehlerbehebung
- **Sprint 5:** Dokumentation, finaler Review, Abgabe

### 7.3 Retrospektive

Im Verlauf des Projekts zeigte sich, dass die flake8-Konformität frühzeitig beachtet werden sollte, um spätere Korrekturen (z. B. Zeilenlängen, Einrückungsfehler) zu vermeiden. Die INI-Datei erwies sich als sinnvolle Ergänzung, da sie die Flexibilität bei der Konfiguration erhöht, ohne den Code zu ändern.

---

## 8. Fazit

### 8.1 Soll-Ist-Vergleich

Alle Must-have- und Should-have-Anforderungen wurden erfolgreich umgesetzt. Die optionalen Could-have-Anforderungen (Continuous Deployment, plattformübergreifende Tests) wurden ebenfalls implementiert.

| Anforderung | Status |
|-------------|--------|
| CI-Pipeline mit Unit Tests | ✅ Umgesetzt |
| Klassendiagramm | ✅ Umgesetzt |
| Sequenzdiagramm | ✅ Umgesetzt |
| Zwei Module alarm.py + monitoring.py | ✅ Umgesetzt |
| Zweistufiges Alarmsystem (Soft-/Hardlimit) | ✅ Umgesetzt |
| E-Mail-Versand per SMTP | ✅ Umgesetzt |
| INI-Konfigurationsdatei | ✅ Umgesetzt |
| Mindestens 3 QA-Maßnahmen | ✅ Umgesetzt (flake8, Bandit, pytest-cov) |
| 5 automatisierte Tests | ✅ Umgesetzt (5 Unit + 7 Integrationstests) |

### 8.2 Lessons Learned

- **Frühzeitiges Linting** spart Zeit: flake8 sollte von Beginn an lokal ausgeführt werden, bevor ein Commit erfolgt.
- **Modulare Struktur** zahlt sich aus: Die Trennung von `alarm.py` und `monitoring.py` vereinfachte das Testen erheblich.
- **INI-Datei** ist flexibler als Hardcoded-Werte: Schwellenwerte lassen sich ohne Code-Änderungen anpassen.

### 8.3 Ausblick

Das System könnte in einer nächsten Iteration um folgende Funktionen erweitert werden:
- Visuelle Darstellung der Messdaten (Web-Dashboard)
- Unterstützung weiterer Systemparameter (CPU-Auslastung, Netzwerktraffic)
- Containerisierung mit Docker für einfaches Deployment

---

## Anhang

### A.1 Klassendiagramm

*(Klassendiagramm – alarm.py, monitoring.py, ConfigINI, LogDatei, SMTPServer, psutil)*

### A.2 Sequenzdiagramm CI/CD-Pipeline

*(Sequenzdiagramm – Entwickler → GitHub → CI → QA → Produktivumgebung)*

### A.3 Verwendete Ressourcen

| Ressource | Version | Typ |
|-----------|---------|-----|
| Python | 3.11 | Open Source |
| psutil | 5.9 | Open Source (Python-Bibliothek) |
| pytest | 7.x | Open Source |
| flake8 | 6.x | Open Source |
| Bandit | 1.7 | Open Source |
| pytest-cov | 4.x | Open Source |
| GitHub Actions | — | Freemium |
| Visual Studio Code | 1.88 | Freemium |

### A.4 config.ini (Vollständiges Beispiel)

```ini
[settings]
log_file = monitoring.log

[limits]
ram_softlimit = 80
ram_hardlimit = 90
disk_softlimit = 80
disk_hardlimit = 95
prozesse_softlimit = 150
prozesse_hardlimit = 200

[smtp]
server = smtp.gmail.com
port = 587
user = monitoring@example.com
password = passwort123
recipient = admin@example.com
```
