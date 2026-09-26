# Validierung — Die Haftungswende

## Validierung 26.09.2026 — Fassung 1.0 → Fassung 2.0 — Umfang: Standardlauf mit Neuausrichtung

Auftrag: Text ohne KI-Slang, einfach lesbar, mit rotem Faden; Zweck ist ein strategischer Rahmen, keine Entscheidungsvorlage.

### Prüfergebnis (Fassung 1.0)

| Prüfschritt | Ergebnis | Auffälligkeiten |
|---|---|---|
| 1.1 Gliederung | Abweichung | Kapitel 7 und Zusammenfassung als Beschlussvorlage gebaut, widerspricht dem Zweck |
| 1.2 Nummerierung | OK | 18 Abbildungen fortlaufend |
| 1.3 Querverweise | OK | Kapitelanker vollständig |
| 1.4 Roter Faden | Abweichung | Keine Leitfrage; Folgerungen für den Verbund nur in drei von sechs Kapiteln; Kapitel 7 knüpft nicht an die Kapitel 1–6 an |
| 1.5 Formatierung | OK | — |
| 2.1 Sachliche Richtigkeit | Abweichung | 40 % Kundenanteil als „überwiegend“ nicht belegt; RWE-Wert ohne Hinweis auf Marktforschungsschätzung |
| 2.2 Redundanz | OK | Pfade A/B in Kurzfassung und Kapitel 7 beabsichtigt |
| 2.3 Argumentation | OK | Linie konsistent |
| 2.4 Ausgewogenheit | Abweichung | Beschlussformulierungen („binär“, „negativ zu entscheiden“) übersteigen, was eine Modellrechnung trägt |
| 2.5 Aktualitätsprinzip | OK | keine Selbstreferenzen |
| 3.1 Rechtschreibung/Grammatik | OK | — |
| 3.2 Terminologie/Glossar | Abweichung | Kein Glossar; Verfahrensjargon („Fachurteile“, „Station“, „Übergabe“, „haftende Schicht“, „Übertragungsbruch“, „Spaltungsverstärker“); „im Mittel“ für Mediane |
| 3.3 KI-Slang/Floskeln | Abweichung | 68 Hinweise: 37 × Verfahrensjargon, 11 Zuspitzungsformeln „nicht X, sondern Y“, 10 × Beschlussvokabular, 5 Gedankenstriche, 5 weitere Zuspitzungen („genau …“, „Das ist …“) |
| 4.1 Quellen: Vollständigkeit | Abweichung | SGB X § 31a im Verzeichnis nach Umbau ohne Textbezug |
| 4.2 Quellen: Einheitlichkeit | OK | — |
| 4.3 Quellen: Belastbarkeit | Abweichung | RWE-Marktvolumen als Marktforschungsschätzung zu kennzeichnen |
| 4.4 URL-Prüfung | n/a | keine URLs |
| 4.5 Zitatgenauigkeit | OK | Stichprobe 10 Kernzahlen gegen Rohdaten und 29-Strategiepapier: 420/331,062 = +26,9 %; 1.550→1.790 = 2,43 % p. a.; 4K 51,7 % brutto fakturiert; ZEG 24,5 %; D2-Mediane 52,5/20/12,5/27,5/57,5 (gerundet 52/20/12/28/58); E3 Kunden S4 40; Szenarien 8/73/2 (88,0 %); Pfadabstand 5,07 Mio. €; „0,56 Prozent“, „rund 65 Prozent“ belegt |
| 4.6 Verifizierungsbedürftig | OK | Marktgröße bleibt als unsicherste Zahl gekennzeichnet |
| 5 Meta | Abweichung | keine Versionsangabe |
| validate_doc.py | OK | 0 Befunde, 68 Hinweise (mit `slang-liste.txt`) |

### Gefundene Fehler

| # | Stelle | Fehler | Schwere |
|---|---|---|---|
| 1 | Auf einen Blick, Kapitel 7 | Beschlussvorlage statt strategischer Rahmen | Kritisch (Zweck) |
| 2 | gesamt | Kein durchgehender roter Faden | Mittel |
| 3 | gesamt | Verfahrensjargon und Zuspitzungsformeln | Mittel |
| 4 | Kapitel 2, Folgerung | 40 % als „überwiegend“ | Mittel |
| 5 | Kapitel 5 | RWE-Wert ohne Kennzeichnung als Schätzung | Mittel |
| 6 | Kernaussage 4 | „im Mittel“ für Median | Gering |
| 7 | Quellen | SGB X § 31a ohne Textbezug | Gering |
| 8 | Titel, Schluss | keine Fassungsangabe | Gering |

### Durchgeführte Bereinigungen

| # | Maßnahme | Erledigt |
|---|---|---|
| 1 | Kapitel 7 neu als „Der strategische Rahmen“ (Richtung, zwei Pfade zur Orientierung, drei Voraussetzungen, fünf Handlungsfelder mit Leitfragen, Zeitfenster mit Orientierungsmarken, sechs Signale); Entscheidungskasten ersetzt; Hinweis, dass das Papier keine Beschlüsse ersetzt | Ja |
| 2 | Leitfrage und Aufbau in „Auf einen Blick“; Folgerungskasten am Ende jedes Kapitels 1–6; Übersicht Befund → Folgerung (Abb. 17) | Ja |
| 3 | Jargon ersetzt (Einschätzungen, Stufe, Standardauswertung, Leistung mit Haftung, Engpass); Zuspitzungen und Gedankenstriche entfernt; Konjunktiv mit „würde“; Glossar mit 16 verlinkten Begriffen | Ja |
| 4 | „den größten Anteil“ statt „überwiegend“ | Ja |
| 5 | als Marktforschungsschätzung für einen Teilmarkt gekennzeichnet | Ja |
| 6 | „im Median“ | Ja |
| 7 | aus dem Verzeichnis entfernt | Ja |
| 8 | „Fassung 2.0“ auf Titelseite, im Schlussvermerk und in der PDF-Fußzeile | Ja |

### Nachprüfung

- validate_doc.py: 0 Befunde, 5 Hinweise; alle fünf sind „—“ als Leerfeld in Tabellen (zulässig laut Prüfprofil)
- Begriffslinks: 16 Links, 16 Ziele, keine toten Links, kein Begriff unverlinkt, kein Begriff doppelt verlinkt
- Abbildungsverweise im Text (2, 7, 9, 14, 20) zeigen auf die richtigen Abbildungen
- Beim Nachlesen gefunden und behoben: zwei Deklinationsfehler durch Begriffslinks („Der Europäischer …“, „Die Beitragspflichtige …“)
- PDF: 23 Seiten A4, Zeitachsen ohne Überschneidungen

### Prüfprofil-Änderungen

- Prüfprofil neu angelegt (`Pruefprofil.md`), projektspezifische Slang-Liste `slang-liste.txt`, Historiendatei `Die-Haftungswende_Historie.md`, Lesefassung `Die-Haftungswende.md` über `als_markdown.py`

### Abschluss

- Alle Fehler behoben: Ja
- Neue Fassung: 2.0 (Versionsstellen synchronisiert: Ja)

## Nachtrag 26.09.2026 — Fassung 2.0 — Umfang: Schnellprüfung (Prüfwerkzeug)

Anlass: Hinweis von Cursor Bugbot, die Lesefassung `Die-Haftungswende.md` verliere Links, Listenmarken und Nummerierung; `validate_doc.py` könne dadurch echte Fehler übersehen.

| Prüfschritt | Ergebnis | Auffälligkeiten |
|---|---|---|
| Automatisierte Prüfung | Abweichung → behoben | Befund zutreffend: Der Konverter v1 ließ Links fallen, reihte Inhaltsverzeichnis und Kernaussagen ohne Trennung aneinander und gab Kapitel ohne Nummer aus. Die Querverweisprüfung (`refs`) war im Hauptlauf deshalb abgeschaltet. |

**Bereinigung:** `als_markdown.py` baut jetzt einen Dokumentbaum und gibt Kapitel als `## N Titel`, Begriffe als `####`-Überschriften, Links als Markdown-Anker, Listen mit Marken und Abbildungen mit Nummer, Titel, Unterzeile, Tabelle oder Platzhalter und Quelle aus. Neuer Prüflauf `pruefe.py` mit allen Checks.

**Nachprüfung:** `python3 pruefe.py` → 21 Abbildungen, 16 Begriffe, 25 interne Links, 0 Befunde, 5 Hinweise (Leerfeld-Striche in Tabellen). Gegenprobe mit absichtlich gebrochenen Verweisen (Kapitel 9, § 6.2, Abbildung 27): alle drei gemeldet. Am Papier selbst keine Änderung nötig.
