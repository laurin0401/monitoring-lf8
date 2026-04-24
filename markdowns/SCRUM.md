# Teil 3: Iterativer Softwarelebenszyklus – Scrum-Dokumentation

**Projekt:** Server Monitoring System  
**Team:** Laurin, Ahmed, Waleed, Markuss, Tim  
**Zeitraum:** 3 Sprints (3 Wochen)

---

## 1. Scrum-Rollen

| Rolle | Person | Aufgaben |
|-------|--------|---------|
| **Product Owner** | Tim | Definiert Anforderungen, priorisiert Aufgaben im Backlog, nimmt fertige Features ab |
| **Scrum Master** | Markuss | Moderiert Daily Standups und Retrospektiven, beseitigt Hindernisse im Team |
| **Developer** | Laurin | Hauptentwickler – setzt Aufgaben technisch um, schreibt Code und Tests |
| **Developer** | Ahmed | Unterstützt bei der Entwicklung, schreibt Dokumentation |
| **Developer** | Waleed | Unterstützt bei Tests und Qualitätssicherung |

### Rollenbeschreibungen

**Product Owner (Tim)**  
Der Product Owner ist verantwortlich für das Product Backlog. Er priorisiert die Anforderungen
nach Geschäftswert und stellt sicher, dass das Team stets an den wichtigsten Aufgaben arbeitet.
Er ist die Schnittstelle zwischen dem Team und den Stakeholdern (z. B. dem Lehrerteam).

**Scrum Master (Markuss)**  
Der Scrum Master sorgt dafür, dass das Team die Scrum-Regeln einhält. Er moderiert alle
Scrum-Events (Sprint Planning, Daily Standup, Sprint Review, Retrospektive) und beseitigt
Hindernisse, die das Team bei der Arbeit blockieren.

**Developer (Laurin, Ahmed, Waleed)**  
Die Entwickler setzen die Anforderungen aus dem Sprint Backlog technisch um. Sie sind
verantwortlich für Code, Tests und Dokumentation. Im Scrum-Sinne sind alle Entwickler
gleichberechtigt – es gibt keine Hierarchie innerhalb des Entwicklungsteams.

---

## 2. Sprint-Planung

### Sprint 1 – Woche 1: Grundentwicklung

**Sprint-Ziel:** Funktionsfähige Monitoring-Module entwickeln

| Aufgabe | Priorität | Verantwortlich | Schätzung | Status |
|---------|-----------|----------------|-----------|--------|
| GitHub Repository einrichten | Hoch | Laurin | 1h | ✅ Fertig |
| alarm.py entwickeln | Hoch | Laurin | 4h | ✅ Fertig |
| monitoring.py entwickeln | Hoch | Waleed | 4h | ✅ Fertig |
| config.ini erstellen | Mittel | Ahmed | 1h | ✅ Fertig |
| Anforderungen analysieren (MoSCoW) | Hoch | Tim | 2h | ✅ Fertig |

### Sprint 2 – Woche 2: Pipeline & Tests

**Sprint-Ziel:** CI/CD-Pipeline einrichten und automatisierte Tests implementieren

| Aufgabe | Priorität | Verantwortlich | Schätzung | Status |
|---------|-----------|----------------|-----------|--------|
| CI/CD Pipeline (ci.yml) erstellen | Hoch | Laurin | 3h | ✅ Fertig |
| Unit Tests schreiben (test_alarm.py) | Hoch | Waleed | 2h | ✅ Fertig |
| Integrationstests schreiben | Mittel | Waleed | 2h | ✅ Fertig |
| README.md verfassen | Niedrig | Ahmed | 1h | ✅ Fertig |
| .gitignore & Sicherheit (config.ini) | Hoch | Laurin | 1h | ✅ Fertig |

### Sprint 3 – Woche 3: Dokumentation & Abgabe

**Sprint-Ziel:** Vollständige Dokumentation und Abgabevorbereitung

| Aufgabe | Priorität | Verantwortlich | Schätzung | Status |
|---------|-----------|----------------|-----------|--------|
| Klassendiagramm erstellen | Mittel | Markuss | 1h | ✅ Fertig |
| Sequenzdiagramm erstellen | Mittel | Markuss | 1h | ✅ Fertig |
| Dokumentation Teil 3 (Scrum) | Hoch | Tim | 2h | ✅ Fertig |
| Dokumentation Teil 4 (Open Source) | Hoch | Tim | 2h | ✅ Fertig |
| Abgabe vorbereiten | Hoch | Ahmed | 1h | ✅ Fertig |

---

## 3. Retrospektiven

### Retrospektive Sprint 1

| Kategorie | Inhalt |
|-----------|--------|
| ✅ Was lief gut? | Aufgabenverteilung hat funktioniert, Laurins Code lief beim ersten Test |
| ❌ Was lief schlecht? | E-Mail-Konfiguration mit Gmail hat Zeit gekostet, Pfadprobleme bei pytest |
| 🔄 Was verbessern wir? | Frühzeitig .gitignore anlegen, pytest mit `python -m pytest` starten |

### Retrospektive Sprint 2

| Kategorie | Inhalt |
|-----------|--------|
| ✅ Was lief gut? | Pipeline läuft automatisch durch, alle Tests sind grün |
| ❌ Was lief schlecht? | Bandit-Konfiguration hat mehrere Versuche gebraucht |
| 🔄 Was verbessern wir? | CI/CD früher testen, nicht erst am Ende des Sprints |

### Retrospektive Sprint 3

| Kategorie | Inhalt |
|-----------|--------|
| ✅ Was lief gut? | Alle Diagramme fertiggestellt, Dokumentation vollständig |
| ❌ Was lief schlecht? | Zeitdruck bei der Abgabevorbereitung in der letzten Woche |
| 🔄 Was verbessern wir? | Dokumentation früher parallel zur Entwicklung beginnen |

---

## 4. Planungsmethode & Tool

**Verwendetes Tool: GitHub Projects (Kanban-Board)**

GitHub Projects wurde von Tim zur Aufgabenplanung eingerichtet. Die Aufgaben wurden als
Issues angelegt, priorisiert und den Teammitgliedern zugewiesen. Das Board enthielt die
Spalten „Backlog", „In Progress", „Review" und „Done".

**War dies ein Zugewinn für das Team?**  
Ja – GitHub Projects war ein klarer Zugewinn, da alle Fortschritte transparent sichtbar waren
und Laurin, Ahmed und Waleed stets wussten, woran gearbeitet wird. Da das Tool direkt in
GitHub integriert ist, war kein separates Tool notwendig. Der einzige Nachteil war, dass
GitHub Projects etwas Einarbeitungszeit benötigt.

---

## 5. Scrum vs. Wasserfallmodell (Could-have)

| Kriterium | Scrum (iterativ) | Wasserfallmodell (klassisch) |
|-----------|-----------------|------------------------------|
| **Vorgehen** | Iterativ in Sprints | Linear, Phase für Phase |
| **Flexibilität** | Hoch – Änderungen jederzeit möglich | Gering – Änderungen sehr aufwändig |
| **Feedback** | Nach jedem Sprint | Erst am Projektende |
| **Risiko** | Früh erkennbar | Oft erst spät sichtbar |
| **Dokumentation** | Minimal, Code im Vordergrund | Umfangreich vor der Entwicklung |
| **Geeignet für** | Komplexe, sich ändernde Projekte | Klar definierte, stabile Projekte |

**Vorteile Scrum:**
- Probleme werden früh erkannt und können sofort behoben werden
- Das Team kann schnell auf neue Anforderungen reagieren
- Kontinuierliche Verbesserung durch Retrospektiven

**Nachteile Scrum:**
- Erfordert ein diszipliniertes und selbstorganisiertes Team
- Schwer planbar für feste Deadlines und Budgets

**Vorteile Wasserfallmodell:**
- Klare Struktur und einfache Planung
- Gut geeignet wenn Anforderungen von Anfang an vollständig bekannt sind

**Nachteile Wasserfallmodell:**
- Fehler werden oft erst sehr spät entdeckt
- Keine Flexibilität bei sich ändernden Anforderungen

---

## 6. Erweiterte Scrum-Rollen (Could-have)

| Rolle | Beschreibung |
|-------|-------------|
| **Stakeholder** | Auftraggeber oder Endnutzer, die Anforderungen definieren und Feedback geben |
| **DevOps Engineer** | Verantwortlich für Infrastruktur, Deployment und Betrieb der CI/CD-Pipeline |
| **QA Engineer** | Spezialist für Qualitätssicherung und Testautomatisierung |
| **UI/UX Designer** | Gestaltet Benutzeroberflächen und sorgt für gute Nutzererfahrung |
| **Security Engineer** | Verantwortlich für Sicherheitsanalysen und Penetrationstests |

In unserem Schulprojekt wurden diese Rollen von den vorhandenen Teammitgliedern
mit übernommen, da das Team klein war und die Aufgaben überschaubar.
