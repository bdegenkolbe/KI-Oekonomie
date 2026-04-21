# Claude.md — Projektanweisung

**Projekt:** Arbeitspapier „Besteuerung von Künstlicher Intelligenz und Robotik als Ersatz menschlicher Arbeit"
**Organisation:** HIGL – Health Innovators Group Leipzig
**Autor:** Björn Degenkolbe

---

## 1. Projektbeschreibung

Dieses Projekt pflegt ein Arbeitspapier zum Diskussionsstand rund um die Besteuerung von KI und Robotik, wenn diese menschliche Arbeit substituieren. Das Papier verbindet drei Perspektiven — ökonomisch-wissenschaftlich, rechtlich-steuerpolitisch und sozial-/verteilungspolitisch — und entwickelt in Kapitel 8 mit der Deutschland-These eine eigenständige Position. Es dient als Wissens- und Diskussionsgrundlage und wird regelmäßig aktualisiert, validiert und als PDF und Word-Dokument exportiert.

**Aktueller Stand:** Version 6.0, April 2026, 11 Kapitel, rund 26 Seiten.

Das Papier steht unter der Creative-Commons-Lizenz CC BY 4.0.

---

## 2. Dateien

| Datei | Zweck |
|---|---|
| `Arbeitspapier_KI_Robotik_Besteuerung.md` | Hauptdokument (Single Source of Truth) |
| `OpenAI_Industriepolitik_Intelligenz-Zeitalter_DE.md` | Arbeitsübersetzung des OpenAI-Strategiepapiers vom April 2026 (Referenzquelle für Kapitel 4.5) |
| `README.md` | Kurzbeschreibung, Deutschland-These, Zitiervorschlag |
| `LICENSE` | Lizenztext (CC BY 4.0) |
| `Validierung.md` | Prüfprozess — regelt Ablauf, Prüfschritte und Versionierung |
| `Validierung-Ergebnisse.md` | Historisches Protokoll aller Validierungen |
| `Formatvorlage.md` | Gestaltungsrichtlinie für PDF- und Word-Export |
| `Claude.md` | Dieses Dokument — Projektanweisung für Claude |
| `build_pdf.py` | PDF-Export (reportlab) — setzt `Formatvorlage.md` um |
| `build_docx.py` | Word-Export (python-docx) — setzt `Formatvorlage.md` um |
| `Arbeitspapier_KI_Robotik_Besteuerung.pdf` | Generierter PDF-Export (aus `build_pdf.py`) |
| `Arbeitspapier_KI_Robotik_Besteuerung.docx` | Generierter Word-Export (aus `build_docx.py`) |

---

## 3. Dokumentstruktur (11 Kapitel)

| § | Kapitel | Kernthema |
|---|---|---|
| 1 | Einleitung und Problemstellung | Ausgangslage, drei Dimensionen der Debatte, Vorgehen und Quellen |
| 2 | Begriffsklärung und Typologie | Fünf Typen der Robotersteuer; Definitionsprobleme (Roboter / KI); Kausalität Ersatz menschlicher Arbeit |
| 3 | Ökonomische Perspektive: Forschungsstand | Acemoglu/Manera/Restrepo, Thuemmel, Costinot & Werning, Guerreiro et al., Gasteiger & Prettner, Nakatani, Gegenposition de la Feria |
| 4 | Rechtliche und steuerpolitische Perspektive (DE/EU) | Delvaux-Debatte 2017; deutsche Rechtslage; Verfassungs- und Europarecht; Sanders-Report 2025; OpenAI-Papier April 2026; Yang |
| 5 | Alternative Finanzierungsmodelle | Wertschöpfungsabgabe, Bürgerversicherung, Bedingungsloses Grundeinkommen, Staatsfonds-/Dividendenmodelle |
| 6 | Internationale Praxis und Fallbeispiele | Südkorea, italienische IRAP, EU Digital Services Tax, nationale Digitalsteuern, skandinavische Modelle |
| 7 | Sektorspezifische Perspektive: Gesundheitswesen | Substitutions-/Ergänzungseffekte, Wertschöpfungsstruktur, Konsequenzen für Akteure im Gesundheits-IT |
| **8** | **Deutschland-These** | **KI als dritter Produktionsfaktor; KI als globaler Rohstoff; Teilhabefrage; Systemstabilität; Veredelungsstrategie, Wertschöpfungsabgabe, Staatsfonds** |
| 9 | Praktische Umsetzungsfragen | Abgrenzungsprobleme, Messbarkeit, internationale Steuerarbitrage, Umgehungsstrategien |
| 10 | Bewertung und Empfehlungen | Bewertung der Ansätze, sieben Empfehlungen, offene Forschungsfragen |
| 11 | Literaturverzeichnis | Ökonomische Forschung, Rechtswissenschaft, institutionelle/politische Dokumente, Wertschöpfungsabgabe, journalistische Quellen |

---

## 4. Regeln

### 4.1 Stil und Tonalität

- Sachlich, faktenbasiert, nicht polemisch
- Neutral, aber mit Haltung — Kapitel 8 ist bewusst positionierend („Deutschland-These")
- Fließtext bevorzugt, keine unnötigen Aufzählungen
- Fachbegriffe beim ersten Auftreten erklären (z. B. „task-based framework", „displacement effect", „Lohnquote", „IRAP")
- Abkürzungen beim ersten Auftreten ausschreiben (IAB, BMAS, OECD, AfA, SGB, GG usw.)
- Kein Marketing-Sprech, keine PR-Floskeln bei der Darstellung von OpenAI, IW Köln, Bundesbank oder anderen Stakeholdern
- Knapp formulieren — keine Redundanzen zu anderen Kapiteln aufbauen. Wenn ein Thema anderswo vertieft wird: ein Satz + Querverweis, nicht nochmal ausführen.

### 4.2 Wissenschaftliche und rechtliche Sorgfalt

- Das Dokument stellt keine steuerrechtliche Beratung dar — der Haftungshinweis am Dokumentende muss erhalten bleiben
- Konjunktiv verwenden, wenn auf Gesetzentwürfe, Policy-Papiere oder Politikvorschläge Bezug genommen wird, die noch nicht beschlossen oder umgesetzt sind (Sanders-Report, OpenAI-Papier, Bürgerversicherung, Vorschläge der Deutschland-These)
- Aussagen aus der Optimalsteuer-Literatur (Acemoglu, Thuemmel, Costinot & Werning etc.) nicht als politische Empfehlungen ausgeben, sondern als Modellergebnisse unter definierten Annahmen darstellen
- Unterscheidung zwischen Modellprognose, Schätzung und empirischer Messung konsequent durchhalten
- Deutschland-These in Kapitel 8 klar als eigene Position des Autors markieren — nicht mit Literaturbefunden vermengen

### 4.3 Inhaltliche Regeln

- Die fünf Typen der Robotersteuer (§ 2.1) dürfen in der öffentlichen Diskussion nicht vermengt werden — wenn ein Akteur „Robotersteuer" sagt, im Text präzisieren, welcher Typ gemeint ist
- US-, EU- und deutsche Perspektiven auseinanderhalten — US-Optimalsteuer-Ergebnisse nicht unreflektiert auf deutsche Verhältnisse übertragen
- OpenAI-Vorschlag ausgewogen darstellen: sowohl die inhaltliche Substanz (Steuerverlagerung, Staatsfonds, 32-Stunden-Woche) als auch die Kritik (Agenda-Setting, „Regulatory Nihilism", Europa-Leerstelle)
- Alle Fakten müssen belegbar sein — keine Behauptungen ohne Quelle
- Zahlen (z. B. IAB: 1,6 Mio. Stellen / 4,5 Bio. EUR; Acemoglu: +4,02 % Beschäftigung; Südkorea: −2 %-Punkte bei Automatisierungsabzügen) konsistent und mit Quelle angeben
- Das Arbeitspapier wurde im Dialog mit Claude (Anthropic) erstellt — dieser Hinweis muss in `README.md` stehen bleiben
- Ein Literatureintrag ist als verifizierungsbedürftig markiert (de la Feria et al. 2022) — diese Markierung darf nicht entfernt werden, bevor die Verifikation erfolgt ist. Der Sanders-Report (Oktober 2025) ist mit Version 5.0 vollständig verifiziert (Primärquelle: sanders.senate.gov).
- **Keine Redundanzen:** Jeder Sachverhalt hat genau einen Ort im Dokument. Andere Stellen verweisen per §-Querverweis. Beispiel: Der Staatsfonds-Gedanke wird in § 5.4 eingeführt und in § 8.3 eigenständig weitergeführt — keine Dopplung der Grundidee.

### 4.4 Änderungen am Hauptdokument

- Jede Änderung löst eine Validierung gemäß `Validierung.md` aus
- Ergebnisse werden in `Validierung-Ergebnisse.md` protokolliert
- Nach jeder abgeschlossenen Validierung: PDF und Word neu erstellen
- Versionsnummer wird hochgezählt (Dokumentkopf, Abschlusshinweis, `README.md`, `Validierung-Ergebnisse.md`)
- Exports:
  - `python3 build_pdf.py` → `Arbeitspapier_KI_Robotik_Besteuerung.pdf` (reportlab, setzt `Formatvorlage.md` um)
  - `python3 build_docx.py` → `Arbeitspapier_KI_Robotik_Besteuerung.docx` (python-docx, setzt `Formatvorlage.md` um)

### 4.5 Was nicht ohne Rückfrage geändert werden darf

- Kapitelstruktur (Reihenfolge, Anzahl, Nummerierung der 11 Kapitel)
- Kernaussage der Deutschland-These in Kapitel 8 (drei Säulen: Veredelungsstrategie, Wertschöpfungsabgabe, Teilhabefonds)
- Autorenname und Organisationszuordnung
- Lizenz (CC BY 4.0) und Zitiervorschlag in `README.md`
- Literaturverzeichnis — keine Quellen löschen, nur ergänzen; Verifizierungshinweise nur entfernen, wenn die Verifikation dokumentiert ist

---

## 5. Build-Pipeline

Das Projekt enthält zwei dedizierte Build-Skripte, die die Vorgaben aus `Formatvorlage.md` umsetzen (A4, Navy/Stahlblau, Header/Footer, Akzentlinien vor Kapiteln, Sonderformat für den Thesen-Block in § 8.5). Keine pandoc-/xelatex-Abhängigkeit.

```bash
# Python-Abhängigkeiten (einmalig)
pip install reportlab python-docx

# PDF (reportlab)
python3 build_pdf.py
# → Arbeitspapier_KI_Robotik_Besteuerung.pdf

# Word (python-docx)
python3 build_docx.py
# → Arbeitspapier_KI_Robotik_Besteuerung.docx
```

Beide Skripte lesen das Hauptdokument, übernehmen H2/H3/H4-Hierarchie, Blockquotes (inkl. Thesen-Sonderfall), Aufzählungen und Tabellen und schreiben das Ergebnis direkt ins Repo-Root.

---

## 6. Typischer Arbeitsablauf

1. Autor bringt inhaltliche Änderung, neue Quelle oder Positionsschärfung ein
2. Claude setzt die Änderung in `Arbeitspapier_KI_Robotik_Besteuerung.md` um
3. Claude führt die Validierung gemäß `Validierung.md` durch (manuelle Prüfschritte; automatisierte Skripte optional)
4. Ergebnisse werden in `Validierung-Ergebnisse.md` protokolliert
5. Fehler werden behoben, Nachprüfung durchgeführt
6. Neue Version wird vergeben (Dokumentkopf, Abschlusshinweis, `README.md`, `Validierung-Ergebnisse.md`)
7. Exports: PDF und Word neu erstellt gemäß § 5 und `Formatvorlage.md`
8. Commit und Push auf den Entwicklungs-Branch

---

## 7. Querverweiskonventionen

- `§X.Y` — Verweis auf Unterabschnitt (z. B. § 8.3 = Deutschland-These, Teilhabefrage)
- `Kapitel X` — Verweis auf ganzes Kapitel (z. B. Kapitel 3 = Ökonomische Perspektive)
- `→ §X.Y` oder `(→ §X.Y)` — Weiterleitungsverweis in Tabellen und Kurztexten
- `vgl. §X.Y` — Vergleichsverweis
- `Ausführlich in §X / Kapitel X` — Redundanzvermeidung bei bewussten Kurzfassungen
- Innerhalb des Literaturverzeichnisses: Sektionen 11.1 bis 11.5 in der im Hauptdokument festgelegten Reihenfolge

Bei Kapitelverschiebungen oder -umnummerierungen: **alle** §-Querverweise im Fließtext, in Tabellen und im Inhaltsverzeichnis aktualisieren. Besonders sensibel sind die Querverweise aus Kapitel 8 zurück auf § 3 (Acemoglu, Thuemmel), § 5 (Wertschöpfungsabgabe, Staatsfonds) und § 4.5 (OpenAI-Papier).
