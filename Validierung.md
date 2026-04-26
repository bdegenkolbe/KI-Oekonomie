# Validierung.md — Prüfprozess für das Hauptdokument

**Gegenstand:** Arbeitspapier „Die Besteuerung von Künstlicher Intelligenz und Robotik als Ersatz menschlicher Arbeit" (`Arbeitspapier_KI_Robotik_Besteuerung.md`)
**Geltungsbereich:** Jede inhaltliche oder strukturelle Änderung am Hauptdokument löst eine Validierung aus.

---

## 1. Ablauf

1. **Prüfung** — Alle Prüfschritte aus Abschnitt 2 durchlaufen
2. **Dokumentation** — Auffälligkeiten in `Validierung-Ergebnisse.md` protokollieren (Abschnitt 3)
3. **Bereinigung** — Fehler im Hauptdokument beheben
4. **Nachprüfung** — Betroffene Prüfschritte erneut durchlaufen, um sicherzustellen, dass die Bereinigung keine neuen Fehler eingeführt hat
5. **Versionierung** — Neue Version vergeben und in `Validierung-Ergebnisse.md` abschließen (Abschnitt 4)
6. **Export** — PDF und Word aus dem Hauptdokument erstellen gemäß `Formatvorlage.md`

Eine Validierung gilt erst als abgeschlossen, wenn alle Prüfschritte durchlaufen, alle Fehler behoben, die Nachprüfung bestanden, die Ergebnisse protokolliert und die Exportdateien erstellt sind.

---

## 2. Prüfschritte

### 2.1 Strukturprüfung

#### 2.1.1 Gliederung

- Stimmen Inhaltsverzeichnis und Kapitelüberschriften in Anzahl (11 Kapitel plus Zusammenfassung), Titel und Anker-IDs überein?
- Ist die Zusammenfassung (Executive Summary) als eigenes Element vor Kapitel 1 erhalten und referenziert sie die Deutschland-These explizit?
- Referenziert jede Unterüberschrift ein existierendes Kapitel?
- Gibt es leere Abschnitte (Überschrift ohne Inhalt)?

#### 2.1.2 Nummerierung

- Ist die Kapitelnummerierung lückenlos (1 bis 11) und ohne Dopplungen?
- Ist die Unterabschnitt-Nummerierung innerhalb jedes Kapitels lückenlos (z. B. Kapitel 8 mit den Unterabschnitten 8.1 bis 8.7)?
- Stimmen alle Zähler im Dokument mit den tatsächlichen Anzahlen überein (fünf Typen der Robotersteuer in § 2.1; drei Säulen der Deutschland-These; sieben Empfehlungen in § 10.2)?

#### 2.1.3 Querverweise

- Zeigt jeder `§X.Y`-Verweis im Fließtext auf einen tatsächlich existierenden Unterabschnitt?
- Passt jeder `Kapitel X`-Verweis zum tatsächlichen Kapiteltitel?
- Sind die Verweise aus Kapitel 8 (Deutschland-These) auf § 3 (Acemoglu/Thuemmel), § 5 (Wertschöpfungsabgabe, Staatsfonds) und § 4.5 (OpenAI-Papier, Sanders-Report) nach Umnummerierungen noch korrekt?
- Sind Verweise auf die Anhang-/Referenzdatei `OpenAI_Industriepolitik_Intelligenz-Zeitalter_DE.md` korrekt, wenn sie eingesetzt werden?

#### 2.1.4 Roter Faden

- Hat jedes der 11 Kapitel eine klar abgegrenzte Funktion im Gesamtdokument?
- Ist die Progression Literaturrezeption (Kap. 3–6) → sektorale Anwendung (Kap. 7) → eigene Position (Kap. 8) → Umsetzung (Kap. 9–10) nachvollziehbar?
- Werden Themen, die in früheren Kapiteln analysiert wurden (z. B. Wertschöpfungsabgabe in § 5.1, Staatsfonds in § 5.4), in Kapitel 8 und 10 nur querverwiesen und weitergeführt, nicht wiederholt?
- Bleibt die Deutschland-These in Kapitel 8 als eigenständige Positionierung erkennbar und nicht in der Literaturrezeption aufgelöst?

#### 2.1.5 Formatierung

- Gibt es Formatierungsartefakte (doppelte Trennlinien `---`, überflüssige Leerzeilen, unausgeglichene Fettungen)?
- Sind fett gesetzte Lead-Ins (z. B. „Typ 1 — Direkte Stücksteuer pro Roboter:") einheitlich formatiert?
- Sind Tabellen syntaktisch korrekt (Anzahl Spalten konsistent, Kopfzeilen vorhanden)?

### 2.2 Inhaltsprüfung

#### 2.2.1 Sachliche Richtigkeit

- Sind alle genannten Gesetze, Verordnungen und Paragraphen korrekt referenziert (Art. 3, 14, 105 GG; EU-AI-Act; SGB-Bezüge; ISO 8373)?
- Sind alle Zahlen (IAB-Prognose 1,6 Mio. Stellen / 4,5 Bio. EUR; Acemoglu-Effekte +4,02 % Beschäftigung / +0,78 Pp. Arbeitsanteil; Südkorea −2 %-Punkte Automatisierungsabzug; OpenAI-Stipendien bis 100.000 USD / 1 Mio. USD API-Credits) aktuell und belegbar?
- Werden Autorinnen und Autoren korrekt zitiert (Acemoglu / Manera / Restrepo 2020; Thuemmel 2023; Costinot & Werning 2023; Guerreiro / Rebelo / Teles 2022; Gasteiger & Prettner 2022; de la Feria et al. 2022; Delvaux 2017; Kallas 2017; Yang 2026)?
- Hat sich der Sachstand seit der letzten Version geändert (z. B. neue EU-Richtlinien, neue nationale Digitalsteuern, neue Forschungspapiere)?

#### 2.2.2 Redundanzprüfung

- Jeden Abschnitt einzeln durchgehen: Werden die Inhalte dieses Abschnitts in anderen Textteilen inhaltlich ähnlich dargestellt?
- Besonders sensibel: Wertschöpfungsabgabe (§ 5.1, § 7.2, § 8.5, § 10.2) — ist die Aufgabenteilung „Einführung / Sektoranwendung / These / Empfehlung" sauber?
- Staatsfonds-Gedanke (§ 5.4, § 8.3, § 10.2) — wird jede Stelle nur als Kurzfassung mit Querverweis geführt oder zusätzlich eigenständig weitergeführt?
- Wenn Doppelung vorliegt: Ist sie beabsichtigt (Kurzfassung mit Querverweis) oder fehlerhaft (gleicher Inhalt, gleiche Tiefe, ohne Querverweis)?

#### 2.2.3 Argumentation

- Sind die zentralen Argumentationslinien in sich konsistent (Substitutionsargument, Lohnquoten-Argument, Rohstoff-Analogie, Systemstabilitäts-Argument)?
- Werden die fünf Typen der Robotersteuer aus § 2.1 im weiteren Verlauf konsequent auseinandergehalten?
- Wird die Acemoglu-Argumentation (Korrektur der relativen Steuerlast Arbeit/Kapital) nicht mit der Thuemmel-Argumentation (spezifische Robotersteuer als zweitbestes Instrument) vermengt?
- Ist die Deutschland-These in Kapitel 8 (drei Säulen: Veredelungsstrategie, Wertschöpfungsabgabe, Staatsfonds) in sich geschlossen und wird sie in Kapitel 10 konsistent aufgenommen?

#### 2.2.4 Ausgewogenheit

- Werden Befürworter und Kritiker einer Robotersteuer gleichgewichtig dargestellt (z. B. IW Köln / Hentze vs. Wertschöpfungsabgabe-Befürworter)?
- Wird das OpenAI-Papier sowohl inhaltlich ernst genommen als auch kritisch eingeordnet (Agenda-Setting, „Regulatory Nihilism", Europa-Leerstelle)?
- Ist der Ton sachlich und faktenbasiert?
- Werden Einschränkungen, Unsicherheiten und Gegenargumente (z. B. Kapitalabfluss, Innovationshemmung, Abgrenzungsprobleme) fair dargestellt?

### 2.3 Sprachliche Prüfung

#### 2.3.1 Tippfehler und Grammatik

- Stichprobenartige Prüfung auf Rechtschreib- und Grammatikfehler
- Bekannte Fehlermuster aus früheren Validierungen gezielt nachsuchen (dokumentiert in `Validierung-Ergebnisse.md`)

#### 2.3.2 Terminologie

- Werden Fachbegriffe beim ersten Auftreten erklärt (task-based framework, displacement effect, productivity effect, Lohnquote, Kapitalquote, IRAP, Flexicurity, Generationenkapital, Pillar 1/2)?
- Werden Abkürzungen beim ersten Auftreten ausgeschrieben (IAB, BIBB, GWS, BMAS, IW, OECD, NBER, JEEA, AfA, OLG, SaaS, BGE, AVV)?
- Wird dieselbe Sache durchgängig gleich benannt? Insbesondere:
  - „Robotersteuer" in Anführungszeichen, wenn sie den populären Oberbegriff meint, sonst präziser Typ-Verweis gemäß § 2.1
  - „Künstliche Intelligenz (KI)" bei Erstnennung, danach „KI"
  - „Wertschöpfungsabgabe" einheitlich (nicht alternierend mit „Wertschöpfungssteuer")

### 2.4 Quellenprüfung

#### 2.4.1 Vollständigkeit und Zuordnung

- Sind alle im Fließtext genannten Autorinnen, Autoren, Institutionen und Policy-Papiere im Literaturverzeichnis (Kapitel 11) aufgeführt?
- Steht jede Quelle in der inhaltlich passenden Sektion (11.1 Ökonomische Forschung / 11.2 Rechtswissenschaft / 11.3 Institutionelle und politische Dokumente / 11.4 Wertschöpfungsabgabe / 11.5 Journalistische Quellen)?
- Gibt es im Fließtext genannte Quellen, die im Literaturverzeichnis keinen Eintrag haben?
- Gibt es Einträge im Literaturverzeichnis, die im Fließtext nie zitiert werden?

#### 2.4.2 Formale Einheitlichkeit

- Hat jeder Eintrag den Zitierstil angelehnt an APA: Autor(en), Jahr, Titel (kursiv für Monographien und Journale), Zeitschrift/Verlag/Herausgeber, Band(Heft), Seiten, ggf. URL?
- Werden URLs vollständig angegeben (kein URL-Shortener, kein Redirect-Link)?
- Sind Datumsangaben einheitlich formatiert (Monat YYYY bzw. YYYY bei Jahrgängen von Zeitschriftenartikeln)?
- Werden Working-Paper- und Preprint-Angaben korrekt gekennzeichnet (NBER Working Paper 27052, MPRA Paper 121347)?

#### 2.4.3 Aktualität und Belastbarkeit

- Werden für zentrale ökonomische Aussagen (Optimalsteuer-Literatur) Primärquellen aus begutachteten Zeitschriften zitiert — keine bloßen Blog- oder Presseartikel?
- Werden für zentrale Rechtsaussagen (Delvaux-Bericht 2017, deutsches Steuer- und Sozialrecht) Primärquellen oder anerkannte Fachkommentierungen zitiert?
- Werden Unternehmens- und Institutionsangaben (OpenAI-Papier, Sanders-Report, IAB-Prognose, Deutsche-Bank-Analyse) mit datierten Belegen gestützt?
- Sind Wikipedia-Referenzen (z. B. Wertschöpfungsabgabe in § 11.4) explizit als Begriffsübersicht gekennzeichnet und nicht als wissenschaftliche Quelle ausgewiesen?

#### 2.4.4 URL-Prüfung (Stichprobe)

- Mindestens 10 % der URLs im Literaturverzeichnis stichprobenartig aufrufen — sind sie erreichbar?
- Führt die URL direkt zur zitierten Quelle (kein Redirect auf Startseite oder 404)? Insbesondere die OpenAI-PDF-URL regelmäßig prüfen, da Anbieter-URLs wechseln können.
- Wenn eine URL hinter einer Paywall oder einem Login liegt: alternative Quelle ergänzen oder Archiv-Link (archive.org) hinterlegen.

#### 2.4.5 Zitatgenauigkeit

- Werden direkte Zitate oder Zahlenangaben aus Quellen korrekt wiedergegeben? Stichprobe von mindestens 5 Kernaussagen, darunter mindestens:
  - Acemoglu/Manera/Restrepo: Beschäftigungs- und Arbeitsanteil-Effekte
  - Thuemmel: Aussage zur Wohlfahrtswirkung einer Robotersteuer bei fallenden Roboterpreisen
  - IAB: Stellen- und Wertschöpfungszahlen
  - Delvaux 2017: Abstimmungsergebnis im EP-Plenum
  - OpenAI 2026: Forschungsstipendien- und API-Credit-Volumen, 32-Stunden-Woche
- Werden Quellen inhaltlich korrekt zusammengefasst, ohne sinnentstellende Verkürzung?
- Werden Modellprognosen und Hochrechnungen als solche gekennzeichnet und nicht als Fakten dargestellt?

#### 2.4.6 Verifizierungsbedürftige Einträge

- Die im Literaturverzeichnis mit einem entsprechenden Hinweis markierten Einträge (z. B. de la Feria et al. 2022; Sanders 2025 Titelangabe) bleiben markiert, bis die vollständige Verifikation vorliegt.
- Für jede erfolgte Verifikation wird in `Validierung-Ergebnisse.md` der Beleg hinterlegt; erst dann darf der Markierungshinweis entfernt werden.

### 2.5 Versionskonsistenz und Lizenz

- Ist die Versionsnummer an allen Stellen identisch (Dokumentkopf, Abschluss-/Haftungshinweis, `README.md`, `Validierung-Ergebnisse.md`)?
- Ist der Autorenname korrekt (Björn Degenkolbe) und die Organisation konsistent (HIGL – Health Innovators Group Leipzig)?
- Ist der Lizenzhinweis CC BY 4.0 vollständig vorhanden (Dokumentende und `README.md`)?
- Ist der Haftungshinweis („Dieses Papier dient der Information und Debatte. Es stellt keine steuerrechtliche Beratung dar.") am Dokumentende erhalten?
- Ist der Hinweis zur KI-Offenlegung (Arbeit im Dialog mit Claude/Anthropic) in `README.md` erhalten?

### 2.6 Automatisierte Prüfung

Das Projekt enthält im Ausgangszustand keine dedizierten Prüfskripte. Wenn später Skripte ergänzt werden (z. B. `validate.py` für Nummerierungs-, Querverweis- und Quellenkonsistenz-Checks), sind sie hier aufzunehmen und in jeder Validierung auszuführen.

Solange keine Skripte existieren, ersetzen manuelle Stichproben zu Nummerierung (§ 2.1.2), Querverweisen (§ 2.1.3) und Quellenzuordnung (§ 2.4.1) den automatisierten Teil.

---

## 3. Dokumentation in Validierung-Ergebnisse.md

Jede Validierung wird in `Validierung-Ergebnisse.md` als eigener Block protokolliert:

```
## Validierung [Datum] — Version X.0 → Version Y.0

### Prüfergebnis

| Prüfschritt | Ergebnis | Auffälligkeiten |
|---|---|---|
| 2.1.1 Gliederung | OK / Abweichung | Beschreibung |
| 2.1.2 Nummerierung | OK / Abweichung | Beschreibung |
| 2.1.3 Querverweise | OK / Abweichung | Beschreibung |
| 2.1.4 Roter Faden | OK / Abweichung | Beschreibung |
| 2.1.5 Formatierung | OK / Abweichung | Beschreibung |
| 2.2.1 Sachliche Richtigkeit | OK / Abweichung | Beschreibung |
| 2.2.2 Redundanzprüfung | OK / Abweichung | Beschreibung |
| 2.2.3 Argumentation | OK / Abweichung | Beschreibung |
| 2.2.4 Ausgewogenheit | OK / Abweichung | Beschreibung |
| 2.3.1 Tippfehler und Grammatik | OK / Abweichung | Beschreibung |
| 2.3.2 Terminologie | OK / Abweichung | Beschreibung |
| 2.4.1 Vollständigkeit und Zuordnung | OK / Abweichung | Beschreibung |
| 2.4.2 Formale Einheitlichkeit | OK / Abweichung | Beschreibung |
| 2.4.3 Aktualität und Belastbarkeit | OK / Abweichung | Beschreibung |
| 2.4.4 URL-Prüfung (Stichprobe) | OK / Abweichung | Beschreibung |
| 2.4.5 Zitatgenauigkeit | OK / Abweichung | Beschreibung |
| 2.4.6 Verifizierungsbedürftige Einträge | OK / Abweichung | Beschreibung |
| 2.5 Versionskonsistenz und Lizenz | OK / Abweichung | Beschreibung |
| 2.6 Automatisierte Prüfung | OK / n/a | Beschreibung |

### Gefundene Fehler

| # | Stelle | Fehler | Schwere |
|---|---|---|---|
| 1 | § X.Y, Zeile Z | Beschreibung | Kritisch / Mittel / Gering |

### Durchgeführte Bereinigungen

| # | Fehler | Maßnahme | Erledigt |
|---|---|---|---|
| 1 | Beschreibung | Was wurde geändert | Ja / Nein |

### Nachprüfung

- Betroffene Prüfschritte erneut durchlaufen: OK / Abweichung
- Automatisierte Skripte (sofern vorhanden): OK / n/a

### Abschluss

- Alle Fehler behoben: Ja / Nein
- Neue Version: Y.0
- PDF erstellt: Ja / Nein
- Word erstellt: Ja / Nein
```

Jeder Block bleibt dauerhaft stehen. Die Historie wird nicht gelöscht.

---

## 4. Versionierung

### Wann wird eine neue Version vergeben?

- Nach jeder abgeschlossenen Validierung mit mindestens einem behobenen Fehler
- Bei inhaltlichen Ergänzungen (neue Quellen, neue Sachverhalte) oder strukturellen Änderungen (Neuaufnahme/Umnummerierung von Abschnitten)
- Bei Aktualisierung der Deutschland-These in Kapitel 8, auch wenn keine Fehler behoben wurden

### Versionsformat

`X.0` — ganzzahlig, aufsteigend. Beginn: `1.0` (Stand April 2026).

### Wo wird die Version eingetragen?

- Dokumentkopf des Arbeitspapiers
- Abschluss-/Aktualitätshinweis am Dokumentende
- Versionshinweis in `README.md`
- PDF/Word Footer (bei Neuerstellung gemäß `Formatvorlage.md` § 4)
- Abschlussblock in `Validierung-Ergebnisse.md`

---

## 5. Dateien

| Datei | Zweck |
|---|---|
| `Arbeitspapier_KI_Robotik_Besteuerung.md` | Hauptdokument |
| `OpenAI_Industriepolitik_Intelligenz-Zeitalter_DE.md` | Referenzübersetzung (Belegquelle für Kapitel 4.5) |
| `README.md` | Kurzbeschreibung, Deutschland-These, Zitiervorschlag, Lizenz |
| `LICENSE` | CC BY 4.0 |
| `Claude.md` | Projektanweisung für Claude |
| `Formatvorlage.md` | Gestaltungsrichtlinie PDF/Word |
| `Validierung.md` | Dieses Dokument — Prüfprozess |
| `Validierung-Ergebnisse.md` | Protokoll aller Validierungen, Fehler und Bereinigungen |
