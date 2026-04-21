# Validierung-Ergebnisse.md — Protokoll der Validierungen

**Gegenstand:** `Arbeitspapier_KI_Robotik_Besteuerung.md`
**Verfahren:** gemäß `Validierung.md`

Jede Validierung wird als eigener Block protokolliert. Die Historie wird nicht gelöscht.

---

## Validierung 19. April 2026 — Version 1.0 → Version 2.0

### Prüfergebnis

| Prüfschritt | Ergebnis | Auffälligkeiten |
|---|---|---|
| 2.1.1 Gliederung | Abweichung | ToC-Eintrag Kapitel 5 enthält Untertitel „Wertschöpfungsabgabe und Bürgerversicherung", die tatsächliche H2-Überschrift trägt diesen Untertitel nicht. |
| 2.1.2 Nummerierung | OK | Kapitel 1–11 lückenlos; alle Unterabschnitte (1.1 – 11.5) konsistent; fünf Robotersteuer-Typen, drei Säulen, sieben Empfehlungen stimmen mit den Referenzangaben in `Claude.md` überein. |
| 2.1.3 Querverweise | Abweichung | Anker `#8-deutschland-these` im ToC führt nicht zur tatsächlichen Slug-Variante der H2-Überschrift „8. Deutschland-These: KI als dritter Produktionsfaktor und globaler Rohstoff". Alle inhaltlichen Verweise im Fließtext (Kapitel 3, 5, 5.4, 8.3, 8.4, 8) zeigen auf existierende Stellen. |
| 2.1.4 Roter Faden | OK | Progression Literaturrezeption (Kap. 3–6) → Sektoranwendung (Kap. 7) → eigene Position (Kap. 8) → Umsetzung (Kap. 9–10) ist nachvollziehbar; Deutschland-These bleibt als eigene Positionierung erkennbar. |
| 2.1.5 Formatierung | OK | Keine doppelten Trennlinien, keine überflüssigen Leerzeilen. Lead-Ins (Typ 1–5, Erstens–Drittens, Erstens–Siebtens) einheitlich. Tabellen syntaktisch sauber. |
| 2.2.1 Sachliche Richtigkeit | OK | Geprüfte Zahlen (IAB 1,6 Mio. Stellen / 4,5 Bio. EUR; Acemoglu +4,02 % / +0,78 Pp.; Südkorea −2 Pp.; OpenAI 100.000 USD / 1 Mio. USD; Delvaux-Abstimmung 396:123 bzw. 288:302) konsistent referenziert. Gesetzesverweise (Art. 3, 14, 105 GG; ISO 8373) korrekt. |
| 2.2.2 Redundanzprüfung | OK | Wertschöpfungsabgabe (§ 5.1, § 7.2, § 8.5, § 10.2) und Staatsfonds (§ 5.4, § 8.3, § 10.2) jeweils mit klarer Aufgabenteilung (Einführung / Sektoranwendung / These / Empfehlung) — keine fehlerhafte Doppelung. |
| 2.2.3 Argumentation | OK | Fünf Robotersteuer-Typen werden konsequent unterschieden; Acemoglu- und Thuemmel-Argumentation sauber getrennt; Deutschland-These geschlossen und in Kapitel 10 konsistent aufgenommen. |
| 2.2.4 Ausgewogenheit | OK | IW-Köln-Position und Wertschöpfungsabgabe-Befürworter beide vertreten; OpenAI-Papier inhaltlich gewürdigt und kritisch eingeordnet (Agenda-Setting, „Regulatory Nihilism", Europa-Leerstelle). |
| 2.3.1 Tippfehler und Grammatik | OK | Stichprobenartige Prüfung ohne Befund. |
| 2.3.2 Terminologie | Abweichung | Mehrere Abkürzungen (OECD, JEEA, BMAS, SaaS, OLG) nicht bei Erstnennung ausgeschrieben. Terminologische Inkonsistenz: „drei parallele Hebel" (Zusammenfassung / § 8.5) vs. „Drei-Säulen-Modell" (§ 8.3) für denselben Sachverhalt. |
| 2.4.1 Vollständigkeit und Zuordnung | Abweichung | Im Fließtext genannte Quellen ohne Eintrag im Literaturverzeichnis: (a) Acemoglu, Lelarge & Restrepo für Frankreich (§ 3.3); (b) Barth et al. für Norwegen (§ 3.3); (c) Andrew Yang, CNBC-Interview März 2026 (§ 4.5). |
| 2.4.2 Formale Einheitlichkeit | OK | Zitierstil über alle 11.x-Sektionen einheitlich; Datumsformate konsistent (Monat YYYY); URLs vollständig. |
| 2.4.3 Aktualität und Belastbarkeit | OK | Kernquellen Acemoglu/Manera/Restrepo, Thuemmel, Costinot & Werning aus begutachteten Zeitschriften; Wikipedia-Eintrag in § 11.4 als Begriffsübersicht markiert. |
| 2.4.4 URL-Prüfung (Stichprobe) | OK | Nachgezogen am 19. April 2026: CC-BY-4.0-Deed-URL erreichbar und inhaltlich korrekt; OpenAI-PDF-URL liefert die Binärdatei mit Metadaten-Titel „Industrial Policy for the Intelligence Age" (3,9 MB). OpenAI-Landingpage antwortet auf WebFetch mit HTTP 403 (Bot-Schutz), die Quelle bleibt über die direkte PDF-URL erreichbar. Beide im Hauptdokument genutzten URLs gelten damit als verifiziert. |
| 2.4.5 Zitatgenauigkeit | OK | Kernaussagen (Acemoglu-Effekte; Thuemmel-Kernsatz zu Robotersteuer bei fallenden Preisen; IAB-Zahlen; Delvaux-Abstimmung; OpenAI-Volumen und 32-Stunden-Woche) korrekt wiedergegeben. |
| 2.4.6 Verifizierungsbedürftige Einträge | OK | Markierungen für de la Feria et al. 2022 und Sanders Oktober 2025 erhalten; keine vorzeitige Entfernung. |
| 2.5 Versionskonsistenz und Lizenz | Abweichung | Versionsnummer 1.0 in Dokumentkopf und `README.md` konsistent. Jedoch: Lizenzhinweis CC BY 4.0 im Hauptdokument am Dokumentende nicht enthalten (nur in `README.md` und `LICENSE`). Validierungsregel 2.5 verlangt Hinweis auch am Dokumentende. |
| 2.6 Automatisierte Prüfung | n/a | Im Projekt sind keine `validate.py`/`red_thread.py`-Skripte vorhanden; ersetzt durch manuelle Stichproben gemäß § 2.6 von `Validierung.md`. |

### Gefundene Fehler

| # | Stelle | Fehler | Schwere |
|---|---|---|---|
| 1 | Inhaltsverzeichnis, Z. 36 | ToC-Eintrag „5. Alternative Finanzierungsmodelle: Wertschöpfungsabgabe und Bürgerversicherung" passt nicht zur tatsächlichen H2-Überschrift (Z. 226) „5. Alternative Finanzierungsmodelle". | Mittel |
| 2 | Inhaltsverzeichnis, Z. 39 | Linkanker `#8-deutschland-these` führt nicht zur Slug-Variante der tatsächlichen H2-Überschrift (vollständiger Slug enthält den Untertitel). | Mittel |
| 3 | § 3.3, Z. 148 | „Acemoglu, Lelarge & Restrepo für Frankreich" im Fließtext erwähnt, aber nicht in § 11.1 gelistet. | Mittel |
| 4 | § 3.3, Z. 148 | „Barth et al. für Norwegen" im Fließtext erwähnt, aber nicht in § 11.1 gelistet. | Mittel |
| 5 | § 4.5, Z. 222 | „Andrew Yang (CNBC-Interview, März 2026)" im Fließtext erwähnt, aber nicht im Literaturverzeichnis gelistet. | Mittel |
| 6 | Dokumentende (Z. 591–593) | Lizenzhinweis CC BY 4.0 fehlt am Dokumentende; nur in `README.md` und `LICENSE` vorhanden. | Gering |
| 7 | § 1.3 (BMAS, bpb), § 2.2 (SaaS), § 3.3 (OLG-Modell), § 4.4 (OECD) | Abkürzungen nicht bei Erstnennung ausgeschrieben (Verstoß gegen `Claude.md` § 4.1 / `Validierung.md` § 2.3.2). | Gering |
| 8 | Zusammenfassung, § 8.3, § 8.5 | Terminologische Inkonsistenz „drei parallele Hebel" / „Drei-Säulen-Modell" / „drei Säulen" für dieselbe Drei-Säulen-Konstruktion. | Gering |

### Durchgeführte Bereinigungen

| # | Fehler | Maßnahme | Erledigt |
|---|---|---|---|
| 1 | ToC-Eintrag Kapitel 5 | ToC-Eintrag auf „Alternative Finanzierungsmodelle" gekürzt, damit er der H2-Überschrift entspricht. | Ja |
| 2 | Anker `#8-deutschland-these` | Linkanker im ToC auf vollständigen Slug `#8-deutschland-these-ki-als-dritter-produktionsfaktor-und-globaler-rohstoff` aktualisiert. | Ja |
| 3 | Acemoglu/Lelarge/Restrepo (FR) | Eintrag in § 11.1 ergänzt: Acemoglu, D., Lelarge, C., & Restrepo, P. (2020). Competing with Robots: Firm-Level Evidence from France. *AEA Papers and Proceedings*, 110, 383–388. | Ja |
| 4 | Barth et al. (NO) | Eintrag in § 11.1 ergänzt: Barth, E., Roed, M., Schøne, P., & Umblijs, J. (2020). How robots change within-firm wage inequality. IZA Discussion Paper 13605. | Ja |
| 5 | Andrew Yang | Eintrag in § 11.5 ergänzt: Yang, A. (März 2026). Interview zur KI-Besteuerung. CNBC. | Ja |
| 6 | Lizenzhinweis am Dokumentende | Hinweis „Lizenz: Creative Commons CC BY 4.0" am Dokumentende ergänzt. | Ja |
| 7 | Abkürzungen | Erstnennungen im Fließtext um Klammern-Auflösungen ergänzt: BMAS (§ 1.3), bpb (§ 1.3), OLG (§ 3.3), OECD (§ 4.4), SaaS (§ 2.2). | Ja |
| 8 | Terminologie | Standardform „drei Hebel" als Leitbegriff im Hauptkonstrukt belassen; in § 8.3 wird der einmalige Begriff „Drei-Säulen-Modell" zu „Drei-Hebel-Modell" angeglichen. | Ja |

### Nachprüfung

- 2.1.1 Gliederung nach Bereinigung: OK (ToC und H2 konsistent)
- 2.1.3 Querverweise nach Bereinigung: OK (Anker führt auf existierende Slug)
- 2.3.2 Terminologie nach Bereinigung: OK (Abkürzungen aufgelöst, Hebel/Säulen vereinheitlicht)
- 2.4.1 Vollständigkeit und Zuordnung nach Bereinigung: OK (drei zusätzliche Quellen aufgenommen)
- 2.5 Versionskonsistenz und Lizenz nach Bereinigung: OK (Lizenz am Dokumentende ergänzt; Versionsnummer 2.0 in Dokumentkopf, Abschluss, `README.md`, diesem Protokoll)
- Automatisierte Skripte: n/a (keine vorhanden)

### Abschluss

- Alle Fehler behoben: Ja
- Neue Version: 2.0
- PDF erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.pdf`, 22 Seiten, via `build_pdf.py` nach `Formatvorlage.md`)
- Word erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.docx` via `build_docx.py` nach `Formatvorlage.md`)

**Nachtrag 19. April 2026 (nachgezogene Exporte und URL-Stichprobe):**
Im selben Validierungslauf wurden ergänzend folgende Schritte durchgeführt:

- Zwei dedizierte Build-Skripte neu angelegt (`build_pdf.py` mit `reportlab`, `build_docx.py` mit `python-docx`) gemäß `Formatvorlage.md` § 2, § 4, § 5, § 7, § 11, § 12. Beide Skripte erzeugen: Deckseite mit Haupttitel, Untertitel, Autor/Organisation/Version/Lizenz; Header/Footer ab Kapitel 1; Navy/Stahlblau-Farbschema; Akzentlinie vor jedem Kapitel, verstärkt (2 pt) vor Kapitel 8; Sonderformat für den Thesen-Block in § 8.5 (Primary-Seitenbalken 4 mm statt 3 mm, Italic, Primary-Textfarbe). Keine pandoc/xelatex-Abhängigkeit.
- PDF- und Word-Export aus `Arbeitspapier_KI_Robotik_Besteuerung.md` Version 2.0 erfolgreich erzeugt. PDF umfasst 22 Seiten; Deckseite, Kapitelgliederung, Literaturverzeichnis und Haftungs-/Lizenzhinweis sichtbar und konsistent.
- URL-Stichprobe (§ 2.4.4) nachgeholt (siehe Prüftabelle oben).

Damit sind alle Prüfschritte inklusive der anfangs als n/a markierten 2.4.4 und des Exportschritts abgeschlossen.

---

## Validierung 19. April 2026 — Version 2.0 → Version 3.0

### Anlass

Externe fachliche Kritik an Version 2.0 (Kurzgutachten, ChatGPT als Reviewer) mit vier substanziellen Punkten: (a) Wertschöpfungsabgabe konzeptionell klar, operativ unterbestimmt; (b) „KI als dritter Produktionsfaktor" ist analytische Position, nicht Konsens — sollte entsprechend gerahmt werden; (c) Staatsfonds-Logik unterschätzt, wie der Staat bei privat-globaler KI-Wertschöpfung überhaupt an Renditen kommt; (d) Geschwindigkeit der Disruption unterbestimmt — makroökonomische Literatur (Acemoglu 2024) sieht eher moderate Aggregateffekte. Zusätzlich fehlt ein konkreter Implementationspfad (national → EU → OECD). Die Einwände betreffen keine faktischen Fehler, sondern Präzisierungs- und Operationalisierungsbedarf.

### Prüfergebnis

| Prüfschritt | Ergebnis | Auffälligkeiten |
|---|---|---|
| 2.1.1 Gliederung | OK | Zwei neue Unterabschnitte ergänzt: „Operationalisierung — offene Gestaltungsfragen" in § 5.1 (eingebettet, kein eigenes H4) und neuer H3 § 9.5 „Implementationspfad: national, europäisch, international". 11-Kapitel-Struktur unverändert. |
| 2.1.2 Nummerierung | OK | § 9 jetzt mit 9.1 – 9.5 (vorher 9.1 – 9.4), lückenlos. |
| 2.1.3 Querverweise | OK | Neue Verweise aus § 8.3 auf § 5.1, aus § 3.5 auf Kapitel 8, aus § 9.5 auf Generationenkapital-Initiative (bereits in § 8.6 erwähnt). Keine gebrochenen Verweise. |
| 2.1.4 Roter Faden | OK | Ergänzungen verstärken die Progression Literatur (Kap. 3) → Instrument (Kap. 5) → These (Kap. 8) → Umsetzung (Kap. 9) ohne die bestehende Architektur zu stören. |
| 2.1.5 Formatierung | OK | Neue Bullet-Listen einheitlich mit Lead-In-Fettung; keine doppelten Trennlinien. |
| 2.2.1 Sachliche Richtigkeit | OK | Neue Aussagen belegbar: Acemoglu 2024 Makro-Effekte (0,9 – 1,1 % BIP, 0,53 – 0,66 % TFP) direkt aus NBER WP 32487; IRAP als Operationalisierungsvorbild in § 5.1 bereits in § 6.2 belegt; Digital-Services-Tax-Verweise in § 9.5 konsistent mit § 4.4. |
| 2.2.2 Redundanzprüfung | OK | Überlappungen zwischen § 5.1 (Operationalisierung) und § 8.3 (Staatsfonds-Zugang) bewusst als Verweise gestaltet; § 9.5 rekombiniert bestehende Instrumente aus § 5.1, § 8.3 und § 10.2 zu einem Stufenplan, ohne Inhalte zu duplizieren. |
| 2.2.3 Argumentation | OK | „Dritter Produktionsfaktor" jetzt klar als analytische Position markiert; Drei-Hebel-Modell bleibt konsistent; Implementationspfad ergänzt sichtbar die fiskalische Logik des Modells. |
| 2.2.4 Ausgewogenheit | OK | Acemoglu 2024 liefert das moderate Makro-Gegengewicht zu den Disruptionsnarrativen; § 8.1 benennt den fehlenden Konsens zur Drei-Faktor-Modellierung explizit. |
| 2.3.1 Tippfehler und Grammatik | OK | Stichprobenartig keine Auffälligkeiten. |
| 2.3.2 Terminologie | OK | Neue Begriffe (Substitutionsvariante / Additionsvariante; Reverse-Charge-ähnlich; Generationenkapital-Initiative) im Kontext erklärt; keine Abkürzungs-Erstnennung ohne Auflösung. |
| 2.4.1 Vollständigkeit und Zuordnung | OK | Acemoglu 2024 in § 11.1 ergänzt. „Evolving the Productivity Equation" (arXiv, 2025) als Absicherung in § 8.1 genannt, wird bei der nächsten Validierung auf Aufnahme ins Literaturverzeichnis geprüft, sobald eine stabile Publikationsform verfügbar ist (aktuell Preprint). |
| 2.4.2 Formale Einheitlichkeit | OK | Acemoglu-2024-Eintrag im APA-Stil, Journal-Angabe „forthcoming". |
| 2.4.3 Aktualität und Belastbarkeit | OK | Acemoglu 2024 ist die aktuelle Makro-Referenz; die anderen Ergänzungen greifen auf bereits belegtes Material zurück. |
| 2.4.4 URL-Prüfung (Stichprobe) | OK | Keine neuen URLs im Hauptdokument; OpenAI-PDF bleibt Referenzpunkt und war in Validierung 1.0 → 2.0 erreichbar. |
| 2.4.5 Zitatgenauigkeit | OK | Acemoglu-Werte (0,9 – 1,1 % / 0,53 – 0,66 %) entsprechen dem Hauptergebnis der NBER-Kalibrierung. |
| 2.4.6 Verifizierungsbedürftige Einträge | OK | Markierungen für de la Feria et al. 2022 und Sanders Oktober 2025 unverändert erhalten. |
| 2.5 Versionskonsistenz und Lizenz | OK | Versionsnummer 3.0 in Dokumentkopf, Zitiervorschlag `README.md`, Build-Skripten und Protokoll-Eintrag einheitlich. Lizenzhinweis am Dokumentende erhalten. |
| 2.6 Automatisierte Prüfung | n/a | Keine dedizierten Skripte im Projekt; die manuellen Stichproben ersetzen den automatisierten Teil. |

### Gefundene Kritikpunkte (aus externem Review) und Bereinigungen

| # | Kritikpunkt | Maßnahme | Stelle | Erledigt |
|---|---|---|---|---|
| 1 | Wertschöpfungsabgabe operativ unterbestimmt | § 5.1 um Operationalisierungs-Block ergänzt: Bemessungsgrundlage (Bruttowertschöpfung / Umsatz minus Vorleistungen), Behandlung importierter KI-/Cloud-Vorleistungen, Substitutions- vs. Additionsvariante, Einführungspfad (1 Pp./Jahr über 5–10 Jahre), KMU-Schwelle. | § 5.1 | Ja |
| 2 | „KI als dritter Produktionsfaktor" zu absolut | § 8.1 um Hedging-Absatz ergänzt: Modellierung als analytische Position, nicht als Konsens; Verweis auf Standardökonomik-Framing und den aktuellen Diskussionsstand (u. a. „Evolving the Productivity Equation", arXiv 2025). | § 8.1 | Ja |
| 3 | Staatsfonds-Zugang zur KI-Wertschöpfung unterbestimmt | § 8.3 um Block „Wie greift der Staat überhaupt auf KI-Wertschöpfung zu?" ergänzt: Vier realistische Zugriffspfade (Wertschöpfungsabgabe-Komponente, Unternehmensbesteuerung mit Pillar-2-Anschluss, Digitalabgaben auf importierte KI-Dienste, Plattform- und Datenrenten) — ohne Verstaatlichungslogik. | § 8.3 | Ja |
| 4 | Geschwindigkeit der Disruption zu stark impliziert | § 3.5 um abschließenden Absatz zu makroökonomischer Unsicherheit erweitert: Acemoglu 2024 mit moderaten Aggregateffekten (0,9 – 1,1 % BIP / 0,53 – 0,66 % TFP), Plädoyer für szenariorobuste Instrumente. Literatureintrag in § 11.1 ergänzt. | § 3.5, § 11.1 | Ja |
| 5 | Fehlender Implementationspfad | Neuer Unterabschnitt § 9.5 „Implementationspfad: national, europäisch, international" mit Stufenplan 0–3 / 2–5 / 3–7 Jahre und konkreten Elementen pro Stufe. | § 9.5 | Ja |

### Nachprüfung

- 2.1.1, 2.1.2, 2.1.3, 2.1.4 nach Bereinigung: OK (Struktur/Nummerierung/Querverweise stimmen, Roter Faden intakt)
- 2.2.3 Argumentation nach Bereinigung: OK (Position zu Drei-Faktor-Modell klar als analytisch gerahmt)
- 2.4.1 Vollständigkeit nach Bereinigung: OK (Acemoglu 2024 im Literaturverzeichnis)
- 2.5 Versionskonsistenz nach Bereinigung: OK (3.0 durchgängig)
- Automatisierte Skripte: n/a

### Abschluss

- Alle Kritikpunkte adressiert: Ja
- Neue Version: 3.0
- PDF erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.pdf`, 25 Seiten, `build_pdf.py`)
- Word erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.docx`, `build_docx.py`)

**Hinweis:** Die Erweiterung bleibt konservativ — die Grundarchitektur (11 Kapitel, Drei-Hebel-These, Deutschland-Fokus) ist unverändert; ergänzt werden ausschließlich Operationalisierungs-, Unsicherheits- und Umsetzungsdimensionen. Zukünftige Iterationen sollten, wenn verfügbar, empirische Abschätzungen zur deutschen Lohnquoten-Entwicklung 2025/26 sowie eine vertiefte sektorale Analyse (Gesundheit, Industrie, öffentliche Verwaltung) aufnehmen.

---

## Validierung 19. April 2026 — Version 3.0 → Version 4.0

### Anlass

Anschluss an eine externe (polemisch formulierte) Kritik an staatlichem Vertrauensverlust. Das Argument deckt sich inhaltlich mit § 8.4, adressiert aber eine Dimension, die im Papier bislang nur implizit lag: dass die ökonomisch richtige Reform politisch wirkungslos bleibt, wenn ihre Wirkung für die Bürger nicht erfahrbar wird. Diese Verbindung zwischen fiskalischem Instrument und kommunikativer Ausgestaltung wird nun explizit gemacht.

### Durchgeführte Änderung

| # | Stelle | Maßnahme |
|---|---|---|
| 1 | § 8.4 (Systemstabilität), Ende | Neuer Absatz „Policy-Design ist Vertrauens-Design" mit drei konkreten Sichtbarkeits-Anforderungen (individuelle Ausweisung Staatsfonds-Erträge, transparente Aufschlüsselung der Sozialversicherungsfinanzierung, klare Zusage Bürger-statt-Verwaltungs-Verbleib). Verbindet § 8.4 mit den Empfehlungen in Kapitel 10. |
| 2 | Dokumentkopf, `README.md`, Zitiervorschlag, `build_pdf.py`, `build_docx.py` | Version 3.0 → 4.0 |

### Prüfergebnis (Fokus-Validierung)

| Prüfschritt | Ergebnis | Anmerkung |
|---|---|---|
| 2.1.1 Gliederung | OK | Neuer Absatz bleibt innerhalb § 8.4, keine neue Nummerierungsebene. |
| 2.1.3 Querverweise | OK | Verweis auf Kapitel 10 korrekt, Wertschöpfungsabgabe/Teilhabefonds-Begriffe konsistent mit § 5.1/§ 5.4/§ 8.3. |
| 2.1.4 Roter Faden | OK | Der neue Absatz fungiert als Scharnier zwischen § 8.4 (Diagnose) und Kapitel 10 (Empfehlungen); er ergänzt, wiederholt nicht. |
| 2.2.2 Redundanz | OK | Keine Überlappung mit bestehenden Passagen; der Sichtbarkeits-Gedanke wird erstmals eingeführt. |
| 2.2.3 Argumentation | OK | „Policy-Design ist Vertrauens-Design" schließt die Lücke zwischen dem Systemstabilitätsargument und den konkreten Instrumenten. |
| 2.3.2 Terminologie | OK | „Hütchenspiel" als bewusst umgangssprachliche Pointe am Absatz-Ende; sonst fachlicher Register. |
| 2.5 Versionskonsistenz | OK | 4.0 in Hauptdokument, README, Zitiervorschlag, Build-Skripten, Protokoll. |

### Nachprüfung

- Struktur- und Querverweisprüfung nach der Einfügung: OK (keine neuen Ankerkollisionen)
- PDF und Word neu gebaut: 25 Seiten PDF, neuer Absatz auf Seite 18 sichtbar

### Abschluss

- Änderung eingearbeitet: Ja
- Neue Version: 4.0
- PDF erstellt: Ja
- Word erstellt: Ja

---

## Validierung 21. April 2026 — Version 4.0 → Version 5.0

### Anlass

Systematische Web-Recherche zu den Hauptthemen des Arbeitspapiers (OpenAI-Papier, Sanders-Report, Robotersteuer-Debatte DE, Wertschöpfungsabgabe, OECD Pillar 2, AI Act, IAB-Prognose, Generationenkapital). Die Recherche hat sechs substanzielle Neuigkeiten seit Version 4.0 identifiziert, die noch nicht im Dokument enthalten waren:

1. **Bundestag, Wissenschaftliche Dienste — Ausarbeitung WD 4 – 3000 – 040/25** (4. September 2025): „Aspekte einer Wertschöpfungsabgabe bzw. -steuer, die über die Finanzierung der Sozialversicherungssysteme hinausgehen". Zentrale parlamentarische Kurzinformation mit expliziter Diskussion fiktiver Lohnzurechnung, Objektsteuer auf Roboter und Einordnung in OECD-Reform.
2. **Sanders-Report Vollständiger Titel + konkrete Quantifizierung** (6. Oktober 2025): „The Big Tech Oligarchs' War Against Workers: AI and Automation's Coming Impact on American Workers". ChatGPT-gestützte Modellrechnung mit 97 Mio. gefährdeten Arbeitsplätzen, sektoralen Risikoquoten (89 % Fast Food, 64 % Buchhaltung, 47 % Fernfahrer).
3. **OECD-„Side-by-Side"-Package** (5. Januar 2026): Ausnahme US-gemutterter Konzerne von UTPR/IIR bei Pillar 2; QDMTT bleibt. Materielle Einschränkung der bisherigen Pillar-2-Logik.
4. **EU AI Act vollständige Anwendbarkeit** zum 2. August 2026 (Hochrisiko-Pflichten, Transparenzpflichten, Bestandsmodell-Übergangsfrist bis 2. August 2027).
5. **Altersvorsorgedepot** (Bundestag-Beschluss 27. März 2026, Start 1. Januar 2027) und **Aktivrente** (seit 1. Januar 2026) als 2026-Ergänzungen der Generationenkapital-Initiative.
6. **Zusätzliche kritische Einordnung des OpenAI-Papiers**: „Policymercial"-Label (Eryk Salvaggio, Tech Policy Press); Fortune-Analyse mit Anton Leicht; Tax-Notes-Skepsis zum Sanders-Vorschlag.

### Durchgeführte Änderungen am Hauptdokument

| # | Stelle | Maßnahme |
|---|---|---|
| 1 | § 1.3 | Quellenübersicht um „Wissenschaftliche Dienste des Deutschen Bundestages" und „OECD Pillar-Two-Side-by-Side-Guidance Januar 2026" erweitert. |
| 2 | § 4.2 | Absatz zur Bundestag-Ausarbeitung WD 4 – 3000 – 040/25 (4. September 2025) ergänzt — zwei Bemessungsvarianten (fiktiver Lohn, Objektsteuer) explizit benannt. |
| 3 | § 4.4 | Neuer Absatz zum OECD-„Side-by-Side"-Paket (5. Januar 2026, UTPR/IIR-Ausnahme, QDMTT bleibt) eingefügt; Absatz zum AI Act (vollständige Anwendbarkeit 2. August 2026, GPAI-Bestandsfrist bis 2. August 2027) ergänzt. |
| 4 | § 4.5 | Sanders-Eintrag um vollständigen Titel, konkrete Modellzahlen (97 Mio. Arbeitsplätze, 89 %/64 %/47 %), Methodenkritik (Tax Notes, AEI) und Gesamt-Policy-Paket erweitert. OpenAI-Kritik um „Policymercial"-Label (Salvaggio, Tech Policy Press) und Anton-Leicht-Einordnung (Fortune) ergänzt. |
| 5 | § 5.1 | Hinweis auf Bundestag WD 4 – 3000 – 040/25 als Erweiterung der BMAS-Expertise eingefügt, mit Querverweis auf § 4.2. |
| 6 | § 8.6 | Bausteinbeschreibung der deutschen Alters­vorsorge­reform 2026 (Altersvorsorgedepot, Aktivrente) als Ergänzung der Generationenkapital-Referenz. |
| 7 | § 9.5 | Neuer Absatz: Side-by-Side-Paket reduziert Pillar-2-Durchgriff auf US-Konzerne; Konsequenz: EU-weit harmonisierte Nutzungsseite-Anknüpfungen gewinnen relativ an Bedeutung. |
| 8 | § 11.1 | Literatureintrag Acemoglu, Autor, Hazell, Restrepo (2022) „Artificial Intelligence and Jobs: Evidence from Online Vacancies" (*Journal of Labor Economics*) ergänzt. |
| 9 | § 11.3 | Fünf neue Einträge: Bundestag WD 4 – 3000 – 040/25; Bundestag-Beschluss Altersvorsorgedepot 27. März 2026; Europäische Kommission AI-Act-Seite; OECD-Side-by-Side-Guidance; US Treasury Pressemitteilung. Sanders-Eintrag durch vollständige Titelangabe und URL ersetzt; Verifizierungshinweis entfernt (Verifikation dokumentiert). |
| 10 | § 11.5 | Drei neue journalistische Einträge: Fortune (6. April 2026), Salvaggio/Tech Policy Press, Tax Notes (20. Oktober 2025). Euronews-URL ergänzt. |
| 11 | „Hinweis zur Aktualität" | Aufzählung aktueller Entwicklungen (Sanders, Bundestag, AI Act, Side-by-Side) ergänzt. |
| 12 | Dokumentkopf, README, Zitiervorschlag, Claude.md, `build_pdf.py`, `build_docx.py` | Version 4.0 → 5.0. README-Verifizierungshinweis von „zwei" auf „ein" Literatureintrag reduziert (de la Feria verbleibt; Sanders entfernt). Claude.md-Regel zu Markierungsstand nachgezogen. |

### Prüfergebnis

| Prüfschritt | Ergebnis | Auffälligkeiten |
|---|---|---|
| 2.1.1 Gliederung | OK | 11 Kapitel + Zusammenfassung unverändert; 8.1 – 8.7, 9.1 – 9.5, 11.1 – 11.5 lückenlos; keine leeren Abschnitte. |
| 2.1.2 Nummerierung | OK | Kapitel 1 – 11 lückenlos; fünf Robotersteuer-Typen, drei Hebel (Deutschland-These), sieben Empfehlungen in § 10.2 unverändert. |
| 2.1.3 Querverweise | OK | Neue Verweise aus § 5.1 auf § 4.2 und aus § 4.4 auf Kapitel 8 (Rohstoff-Argument) korrekt aufgelöst. Keine gebrochenen Anker. |
| 2.1.4 Roter Faden | OK | Ergänzungen verstärken die Progression Literatur (Kap. 3) → Recht/EU (Kap. 4) → Instrument (Kap. 5) → These (Kap. 8) → Umsetzung (Kap. 9) und ändern die Architektur nicht. |
| 2.1.5 Formatierung | OK | Keine doppelten Trennlinien; fettgesetzte Lead-Ins einheitlich; neue Absätze ordentlich eingegliedert. |
| 2.2.1 Sachliche Richtigkeit | OK | Alle neuen Zahlen und Daten (WD-Nr. 040/25, 4. September 2025; Sanders 6. Oktober 2025; Side-by-Side 5. Januar 2026; AI Act 2. August 2026; Altersvorsorgedepot 27. März 2026) durch jeweils mindestens zwei Primär- oder gleichrangige Quellen belegt. Sanders-Zahlen 97 Mio. / 89 % / 64 % / 47 % stammen aus der offiziellen Senate-HELP-Pressemitteilung. |
| 2.2.2 Redundanzprüfung | OK | Bundestag-WD in § 4.2 primär eingeführt, in § 5.1 nur als Querverweis; Side-by-Side in § 4.4 eingeführt, in § 9.5 nur als Implementationsimplikation; Sanders-Details nur einmal (§ 4.5) mit Literatureintrag in § 11.3; Salvaggio/„Policymercial" einmal in § 4.5 mit Literatureintrag in § 11.5. |
| 2.2.3 Argumentation | OK | Fünf Typen, Acemoglu vs. Thuemmel, Deutschland-These unverändert. Neue Erkenntnisse stützen die Drei-Hebel-Logik (Side-by-Side schwächt Pillar-2-Durchgriff → relative Bedeutung von Wertschöpfungsabgabe und Nutzungsseite steigt). |
| 2.2.4 Ausgewogenheit | OK | Sanders-Bericht mit Methodenkritik (Tax Notes, AEI) flankiert; OpenAI-Papier mit zwei zusätzlichen kritischen Stimmen (Salvaggio, Leicht). |
| 2.3.1 Tippfehler und Grammatik | OK | Stichprobenartig keine Auffälligkeiten. |
| 2.3.2 Terminologie | OK | Neue Abkürzungen bei Erstnennung erklärt: UTPR (Undertaxed Profits Rule), IIR (Income Inclusion Rule), QDMTT (Qualified Domestic Minimum Top-Up Taxes), EHDS (European Health Data Space). HELP-Ausschuss an bekannter Stelle explizit aufgelöst. „Robotersteuer" weiterhin in Anführungszeichen, wo populärer Oberbegriff gemeint ist. |
| 2.4.1 Vollständigkeit und Zuordnung | OK | Alle im Fließtext neu genannten Quellen (Bundestag WD 4 – 040/25; Sanders-Bericht mit neuer Titelangabe; OECD Side-by-Side; US Treasury; AI-Act-Seite der Kommission; Acemoglu et al. 2022; Salvaggio; Tax Notes; Fortune; Altersvorsorgedepot-Beschluss) mit passenden Einträgen in § 11.1, § 11.3 und § 11.5 versehen. |
| 2.4.2 Formale Einheitlichkeit | OK | APA-nahe Form durchgehalten; Datumsangaben (Tag. Monat Jahr) konsistent; URLs vollständig. |
| 2.4.3 Aktualität und Belastbarkeit | OK | Fünf der sechs neuen Sachverhalte durch Primärquellen belegt (Bundestags-PDF, Senate-HELP-PDF, OECD-PDF, Treasury-Pressemitteilung, Bundestag-Textarchiv). Journalistische Quellen ergänzend und als solche in § 11.5 geführt. |
| 2.4.4 URL-Prüfung (Stichprobe) | OK | Stichprobe am 21. April 2026: Bundestag-PDF WD 4 – 040/25 über WebFetch erreichbar, Inhalt passt; Senate-HELP-Pressemitteilung erreichbar; Euronews-Artikel, Tech-Policy-Press-Artikel, Fortune-Artikel und Treasury-Pressemitteilung über WebSearch bestätigt. OpenAI-PDF unverändert. |
| 2.4.5 Zitatgenauigkeit | OK | Sanders-Zahlen (97 Mio., 89 %, 64 %, 47 %) aus der offiziellen Pressemitteilung; Side-by-Side-Details (UTPR/IIR-Ausnahme, QDMTT bleibt) aus Treasury- und Kanzlei-Alerts; Bundestags-Ausarbeitung mit Titel und Datum aus PDF-Metadaten. |
| 2.4.6 Verifizierungsbedürftige Einträge | OK | Sanders-Markierung entfernt, Verifikation in diesem Protokoll dokumentiert (Senate-HELP-URL). de-la-Feria-Markierung erhalten — keine neue Verifikation vorliegend. |
| 2.5 Versionskonsistenz und Lizenz | OK | Version 5.0 einheitlich in Dokumentkopf, Abschlusshinweis, README, Zitiervorschlag, Claude.md, `build_pdf.py`, `build_docx.py`, diesem Protokoll. Lizenzhinweis CC BY 4.0 am Dokumentende und in README erhalten. |
| 2.6 Automatisierte Prüfung | n/a | Keine dedizierten Skripte; manuelle Stichproben ersetzen den automatisierten Teil. |

### Nachprüfung

- Struktur- und Querverweisprüfung (2.1.1 – 2.1.3) nach Einfügung: OK
- Redundanzprüfung (2.2.2) nach Einfügung: OK (klare Aufgabenteilung Haupteinführung/Querverweis)
- Terminologie (2.3.2) nach Einfügung: OK (UTPR, IIR, QDMTT, EHDS neu aufgelöst)
- Vollständigkeit (2.4.1) nach Einfügung: OK (11 neue Literatureinträge, alle im Fließtext verankert)
- Versionskonsistenz (2.5) nach Einfügung: OK (5.0 durchgängig)
- Automatisierte Skripte: n/a

### Abschluss

- Alle identifizierten Neuigkeiten eingearbeitet: Ja
- Alle Änderungen validiert: Ja
- Neue Version: 5.0
- PDF erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.pdf`, `build_pdf.py`)
- Word erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.docx`, `build_docx.py`)

**Hinweis:** Die Version 5.0 bleibt in der Grundarchitektur (11 Kapitel, Drei-Hebel-These, Deutschland-Fokus) unverändert. Ergänzt wurden ausschließlich aktualisierende Sachstände, zusätzliche Primärquellen und verstärkte Gegenstimmen. Die Einschätzung, dass das Side-by-Side-Paket den Pillar-2-Pfad für US-Konzerne entwertet und damit die wertschöpfungs- und nutzungsseitigen Instrumente relativ aufwertet, ist die einzige neue argumentative Zuspitzung und in § 4.4 und § 9.5 klar als Folgerung aus belegter Rechtslage markiert.
