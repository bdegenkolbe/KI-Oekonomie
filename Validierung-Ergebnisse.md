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

## Validierung 20. April 2026 — Version 4.0 → Version 5.0

**Auslöser:** Web-Recherche zu den Hauptthemen des Arbeitspapiers; Einarbeitung von sechs belegbaren Neuigkeiten aus dem Zeitraum Oktober 2025 bis April 2026:

1. Verifikation des Sanders-Reports (6. Oktober 2025): vollständiger Titel „The Big Tech Oligarchs' War Against Workers: AI and Automation Could Destroy Nearly 100 Million U.S. Jobs in a Decade"; PDF-Link zum Volltext auf sanders.senate.gov
2. Neues ökonomisches Paper Falk & Tsoukalas (21. März 2026): „The AI Layoff Trap" (arXiv 2603.20617), Pigouvian-Automation-Tax-Argumentation aus einem wettbewerbsbasierten Task-Modell
3. EU AI Act: volle Anwendbarkeit der Hauptbestimmungen ab 2. August 2026 (Art. 50 Transparenz, Anhang-III-Hochrisikoregime, Durchsetzung)
4. Anschlag auf Sam Altman (10. April 2026) — Molotowcocktail-Angriff auf sein Haus, Angriff auf OpenAI-Zentrale; publizistische Rezeption (NPR, Washington Post, SF Standard, Fortune) stellt den Vorfall in zeitliche Nähe zum OpenAI-Strategiepapier
5. Generationenkapital: operativer Start im Januar 2026 mit ca. 10 Mrd. Euro Startkapital; Rendite im Startjahr rund 7,2 %; Zielgröße mindestens 200 Mrd. Euro bis Mitte 2030er-Jahre
6. IAB-Prognose 2025/2026: kurzfristiger Rückgang der Erwerbstätigkeit 2026 um ca. 20.000 Personen; Arbeitslosigkeitsanstieg in 13 von 16 Bundesländern

### Prüfergebnis

| Prüfschritt | Ergebnis | Auffälligkeiten |
|---|---|---|
| 2.1.1 Gliederung | OK | Inhaltsverzeichnis und Kapitelüberschriften unverändert; Zusammenfassung vor Kapitel 1 erhalten; keine leeren Abschnitte. |
| 2.1.2 Nummerierung | OK | 11 Kapitel lückenlos; Unterabschnitte 1.1–11.5 konsistent; fünf Robotersteuer-Typen, drei Hebel, sieben Empfehlungen mit den jeweiligen Referenzangaben konsistent. |
| 2.1.3 Querverweise | OK | Verweise aus § 8 auf § 3 (Acemoglu/Thuemmel), § 5 (Wertschöpfungsabgabe, Staatsfonds) und § 4.5 (OpenAI, Sanders) weiterhin korrekt; neue Einfügungen haben keine §-Verweise verschoben. |
| 2.1.4 Roter Faden | OK | Neue Textstellen ordnen sich stringent ein: Falk & Tsoukalas in § 3.3/3.5 (Optimalsteuer-Literatur), EU AI Act in § 4.3 (verfassungs-/europarechtlicher Rahmen), Sanders-Volltitel in § 4.5, Altman-Anschlag in § 8.4 (Systemstabilität), Generationenkapital-Update in § 8.6 (Implikationen). |
| 2.1.5 Formatierung | OK | Keine doppelten Trennlinien; fett/kursiv konsistent; Tabellen unverändert. |
| 2.2.1 Sachliche Richtigkeit | OK | Alle neuen Zahlen mit Primär-/Sekundärquelle belegt (Sanders-PDF; arXiv-Preprint; IAB-Presseinformation; BMF-Monatsbericht; EU-Verordnung 2024/1689); bestehende Zahlen (IAB 1,6 Mio. / 4,5 Bio. EUR; Acemoglu +4,02 %/+0,78 Pp.; Delvaux 288:302; OpenAI 100.000 USD / 1 Mio. USD) unverändert. |
| 2.2.2 Redundanzprüfung | OK | Generationenkapital wird nur in § 8.6 substantiell geführt (Kurzverweis in § 5.4); Wertschöpfungsabgabe-Aufgabenteilung (§ 5.1 / § 7.2 / § 8.5 / § 10.2) unverändert; Systemstabilitätsargument bleibt in § 8.4 konzentriert. |
| 2.2.3 Argumentation | OK | Falk/Tsoukalas ist als komplementär zur Thuemmel-Argumentation eingeführt (Nachfrageseite vs. Lohnstruktur) — Argumentationslinien nicht vermengt; Sanders-Volltitel stellt den Inhalt präziser, ohne die kritische Einordnung zu verändern; Altman-Anschlag ausdrücklich als Einzeltat gekennzeichnet. |
| 2.2.4 Ausgewogenheit | OK | OpenAI-Papier bleibt inhaltlich und kritisch gewürdigt; Sanders-Positionen vollständiger, aber ohne Übernahme; Altman-Anschlag sachlich referiert, keine Skandalisierung. |
| 2.3.1 Tippfehler und Grammatik | OK | Stichprobe der neuen Absätze ohne Befund. |
| 2.3.2 Terminologie | OK | Neue Begriffe eingeführt: „Pigou-Steuer", „arXiv-Preprint", „Task", „Nachfrage-Externalität" — jeweils im Kontext erklärbar; Abkürzungen (arXiv, HELP, PDF) nicht erklärungsbedürftig bzw. im Zitat. |
| 2.4.1 Vollständigkeit und Zuordnung | OK | Neue Literaturnachweise vollständig zugeordnet: Falk & Tsoukalas in § 11.1; Sanders-Volltitel in § 11.3; IAB-Prognose 2025/2026 in § 11.3; EU AI Act in § 11.3; BMF-Generationenkapital in § 11.3; Altman-Anschlag (NPR, WP, SF Standard) in § 11.5. |
| 2.4.2 Formale Einheitlichkeit | OK | Neue Einträge in APA-Stil; URLs vollständig; Datumsformate einheitlich. |
| 2.4.3 Aktualität und Belastbarkeit | OK | Falk/Tsoukalas als arXiv-Preprint markiert; IAB-Prognose und BMF-Monatsbericht als Primärquellen; Altman-Anschlag mit drei redaktionell unabhängigen Belegen (NPR, WP, SF Standard). |
| 2.4.4 URL-Prüfung (Stichprobe) | OK | Stichprobe am 20. April 2026: sanders.senate.gov-PDF erreichbar (Volltext); arxiv.org/abs/2603.20617 erreichbar; iab.de-Presseinformation erreichbar; bundesfinanzministerium.de-Monatsbericht erreichbar. OpenAI-PDF-URL aus Validierung 19. April unverändert gültig. |
| 2.4.5 Zitatgenauigkeit | OK | Sanders-Kernaussage (Robotersteuer als Verbrauchsteuer, Aufkommen für verdrängte Beschäftigte) aus Primärquelle wiedergegeben; Falk/Tsoukalas-Kernsatz („Only a Pigouvian automation tax can") inhaltlich korrekt zusammengefasst; IAB-Kurzfristprognose (−20.000 Erwerbstätige, 13 von 16 Ländern) korrekt. |
| 2.4.6 Verifizierungsbedürftige Einträge | Abweichung → behoben | Sanders-Titelmarkierung entfernt (Primärquelle verifiziert, Beleg: sanders.senate.gov PDF vom 6. Oktober 2025). de la Feria et al. 2022 bleibt als verifizierungsbedürftig markiert. Claude.md und README.md synchronisiert. |
| 2.5 Versionskonsistenz und Lizenz | OK | Version 5.0 in Dokumentkopf, Zitiervorschlag (README), Claude.md und diesem Protokoll identisch. Haftungs- und Lizenzhinweis am Dokumentende erhalten. |
| 2.6 Automatisierte Prüfung | n/a | Keine Prüfskripte im Repo; manuelle Stichproben zu Nummerierung, Querverweisen und Quellenzuordnung durchgeführt. |

### Gefundene Fehler

| # | Stelle | Fehler | Schwere |
|---|---|---|---|
| 1 | § 11.3 / README.md / Claude.md | Sanders-Report hatte bislang die Markierung „Vollständige Titelangabe zu verifizieren"; mit Version 5.0 liegt die Primärquelle vor. | Gering |

### Durchgeführte Bereinigungen

| # | Fehler | Maßnahme | Erledigt |
|---|---|---|---|
| 1 | Sanders-Titel verifiziert | Volltitel, Datum (6. Oktober 2025) und PDF-URL in § 11.3 gesetzt; Verifikationsmarkierung entfernt; Claude.md und README.md angepasst. | Ja |

### Nachprüfung

- 2.1.1 – 2.1.5 nach Einarbeitung: OK
- 2.4.1, 2.4.2, 2.4.3 nach Ergänzung um 5 neue Literaturnachweise: OK
- 2.4.6 nach Bereinigung: OK (einziger verbleibender verifizierungsbedürftiger Eintrag: de la Feria et al. 2022)
- 2.5 Versionskonsistenz: OK
- Automatisierte Skripte: n/a

### Abschluss

- Alle Fehler behoben: Ja
- Neue Version: 5.0
- PDF erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.pdf` via `build_pdf.py`)
- Word erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.docx` via `build_docx.py`)

---

## Validierung 21. April 2026 — Version 5.0 → Version 6.0

**Auslöser:** Web-Recherche zu den Hauptthemen des Arbeitspapiers (KI-Besteuerung, Wertschöpfungsabgabe, EU AI Act, OpenAI-Policy, Sanders-Report, Generationenkapital, IAB, OECD Pillar 2). Einarbeitung von sechs belegbaren Neuigkeiten aus dem Zeitraum Dezember 2025 bis April 2026. Alle Neuerungen wurden gegen den vorhandenen Bestand abgeglichen; eine inhaltliche Dopplung mit bereits referenzierten Quellen wurde vermieden (Sanders-Report, OpenAI-Papier, Falk/Tsoukalas, IAB-Prognose, Generationenkapital-Startphase, EU-AI-Act-Anwendbarkeit, Altman-Anschlag-Grundvorfall).

### Aufgenommene Neuigkeiten

| # | Neuigkeit | Einarbeitung | Begründung Relevanz |
|---|---|---|---|
| 1 | Q1-2026-Tech-Layoffs: ~78.500 Stellen, ~48 % KI-attribuiert; parallel 92 % Anstieg KI-bezogener Stellenausschreibungen | § 1.1 (Ergänzung im Ausgangslagen-Absatz) | Empirische Aktualisierung des Substitutions-/Umbau-Arguments; keine Dopplung zu bereits referenzierter IAB-Langfristprognose |
| 2 | Anthropic Economic Index 2026 (tatsächliche KI-Nutzungsdaten): keine klaren Arbeitslosigkeitseffekte aggregat; frühe Struktureffekte bei Einsteigerpositionen | § 3.5 (Ergänzung zwischen Acemoglu 2024 und szenariorobuster Politikempfehlung) | Komplementäres Gegengewicht zu Disruptionsnarrativen; stärkt die szenariorobuste Auslegungslogik |
| 3 | OECD Pillar-2-Side-by-Side-Paket (Januar 2026) mit neuen Safe-Harbor-Regelungen und aktualisiertem zentralem Rechtsaktenkatalog | § 4.4 | Aktuelle Verankerung des internationalen Koordinationsrahmens; relevant für § 9.5 Stufe 3 |
| 4 | No Robot Bosses Act (H.R. 6371, Bonamici et al., 3. Dezember 2025): arbeitsrechtliche Aufsichts- und Transparenzpflichten bei algorithmischen Beschäftigungsentscheidungen | § 4.5 (eigener Absatz nach Yang) | Komplementäre politische Reaktionslinie (arbeitsrechtlich statt fiskalisch); greift dieselbe Definitionsfrage wie Typ-5-Abgabe auf |
| 5 | Kommission zur Sozialstaatsreform (KSR, 26 Empfehlungen, 27. Januar 2026) + Alterssicherungskommission (ASK, ab 7. Januar 2026) mit ausdrücklichem Prüfauftrag „Einbeziehung weiterer Einkommensarten" | § 5.2 (neuer Absatz „Aktueller Reformprozess"), Querverweis in § 8.6 | Erstmals formaler Regierungsauftrag zur Bürgerversicherung-Kernidee; öffnet politisches Gelegenheitsfenster |
| 6 | Altman-Anschlag Konkretisierung: Tatverdächtiger Daniel Moreno-Gama (20 J., Houston), Vorwürfe versuchter Mord und Brandstiftung; Liste von KI-Führungskräften und Investoren; zweiter Vorfall am 12. April 2026 | § 8.4 (bestehender Absatz erweitert) | Aktualisierung des Systemstabilitäts-Beispiels mit belegbaren Tatsachen; keine Skandalisierung |

Nicht aufgenommen (bewusste Auslassungen):
- Sam-Altman/Vinod-Khosla-Folgeinterview (Fortune, 7. April 2026): inhaltlich kein Zusatz gegenüber dem OpenAI-Papier.
- OpenAI-Mai-Workshop und Finanzierungsrahmen: bereits in § 4.5 abgebildet.
- EU AI Liability Directive-Rückzug (Februar 2025): liegt vor dem Berichtszeitraum und berührt die Steuerargumentation nicht unmittelbar.
- Anthropic-Index als eigenständige Primärquelle mit Sub-Indikatoren: eine einzige Kurzaussage in § 3.5 ist ausreichend; eine weitere Vertiefung würde die szenariorobuste Kernlinie überfrachten.

### Prüfergebnis

| Prüfschritt | Ergebnis | Auffälligkeiten |
|---|---|---|
| 2.1.1 Gliederung | OK | Inhaltsverzeichnis und Kapitelstruktur (11 Kapitel plus Zusammenfassung) unverändert; keine leeren Abschnitte; Deutschland-These in der Zusammenfassung referenziert. |
| 2.1.2 Nummerierung | OK | Kapitel 1–11 lückenlos; Unterabschnitte 1.1–11.5 konsistent; fünf Robotersteuer-Typen, drei Hebel, sieben Empfehlungen stimmen mit Referenzangaben überein. |
| 2.1.3 Querverweise | OK | Neue Querverweise (§ 5.2 → § 5.1; § 8.6 → § 5.2) funktionieren; bestehende Anker unverändert. |
| 2.1.4 Roter Faden | OK | Neue Einfügungen ordnen sich in die Progression Literatur → Instrument → These → Umsetzung ein, ohne die Architektur zu verschieben. |
| 2.1.5 Formatierung | OK | Keine doppelten Trennlinien; Fett/Kursiv konsistent; Lead-Ins (§ 5.2 „Aktueller Reformprozess"; § 4.5 „No Robot Bosses Act") einheitlich; Tabellen unverändert. |
| 2.2.1 Sachliche Richtigkeit | OK | Alle neuen Zahlen und Fakten belegbar: Q1-2026-Layoff-Zahlen (Tom's Hardware / TechRadar); OECD Side-by-Side (OECD-Pressemitteilung Dezember 2025); KSR (Bundesregierung); ASK (BMAS); Moreno-Gama-Anklage (CNN, Fortune, NPR); H.R. 6371 (Congress.gov). |
| 2.2.2 Redundanzprüfung | OK | Generationenkapital-Bezug bleibt auf § 8.6 konzentriert (Kurzerwähnung in § 5.4 unverändert); Bürgerversicherungs-Reformprozess ist neu, keine Dopplung mit § 5.1 Operationalisierung; Altman-Anschlag bleibt in § 8.4 konzentriert; keine Neuerzählung in § 4.5 oder § 10. |
| 2.2.3 Argumentation | OK | Anthropic-Index ist ausdrücklich als *komplementär* zu Acemoglu 2024 eingeführt, nicht widersprüchlich; No Robot Bosses Act als komplementärer Pfad (arbeitsrechtlich statt fiskalisch), Abgrenzung zu Typ-5-Abgabe explizit; Reformprozess 2026 als politisches Gelegenheitsfenster für die Drei-Hebel-These kontextualisiert, nicht als Ersatz. |
| 2.2.4 Ausgewogenheit | OK | Q1-Layoff-Zahlen werden ohne Skandalisierung referiert; Anthropic-Index wird nicht als Entwarnung missbraucht (Einschränkung „frühe Struktureffekte erkennbar" bleibt stehen); Moreno-Gama-Anklage wird sachlich in den Systemstabilitäts-Kontext eingeordnet, ohne Generalisierungen. |
| 2.3.1 Tippfehler und Grammatik | OK | Stichprobe der neuen Absätze ohne Befund. |
| 2.3.2 Terminologie | OK | Neue Begriffe im Kontext erklärt: „Safe-Harbor-Regelungen", „zentraler Rechtsaktenkatalog", „No Robot Bosses Act", „Alterssicherungskommission (ASK)", „Kommission zur Sozialstaatsreform (KSR)". Abkürzungen ASK und KSR bei Erstnennung ausgeschrieben. |
| 2.4.1 Vollständigkeit und Zuordnung | OK | Neue Einträge vollständig zugeordnet: Anthropic Economic Index in § 11.1; BMAS-Rentenkommission, Bundesregierung-KSR, OECD-Pressemitteilung, H.R. 6371 in § 11.3; CNN, Fortune, Tom's Hardware in § 11.5. Keine neuen Fließtext-Referenzen ohne Eintrag. |
| 2.4.2 Formale Einheitlichkeit | OK | Alle neuen Einträge APA-nah mit vollständigen URLs und Datumsangabe im Format „Monat YYYY"; keine URL-Shortener. |
| 2.4.3 Aktualität und Belastbarkeit | OK | Primärquellen (Congress.gov, Bundesregierung, OECD, BMAS) für institutionelle Aussagen; redaktionell unabhängige Mehrfachbelege (NPR, CNN, Fortune, Washington Post) für den Altman-Anschlag; Q1-Layoff-Zahlen mit konsistenten Zahlenangaben über Tom's Hardware, TechRadar und TweakTown. |
| 2.4.4 URL-Prüfung (Stichprobe) | OK | Stichprobe am 21. April 2026: sanders.senate.gov (unverändert gültig); oecd.org Pressemitteilung Dezember 2025 erreichbar; congress.gov H.R. 6371 erreichbar; bmas.de Rentenkommission-Seite erreichbar; bundesregierung.de KSR-Bericht erreichbar; anthropic.com Economic-Index-Landingpage erreichbar. |
| 2.4.5 Zitatgenauigkeit | OK | Q1-Layoff-Zahl („~78.500", „~48 %") und Nachfrage-Anstieg bei KI-Jobs korrespondieren mit der Branchenauswertung; Moreno-Gama-Angaben (Alter, Herkunft, Charges) entsprechen CNN/Fortune-Berichterstattung; OECD-Datum (1. Dezember 2025 für zentralen Rechtsaktenkatalog) korrekt aus Administrative Guidance übernommen. |
| 2.4.6 Verifizierungsbedürftige Einträge | OK | Verbleibt nur de la Feria et al. 2022 als verifizierungsbedürftig markiert; alle Neuzugänge verifiziert und mit URL belegt. |
| 2.5 Versionskonsistenz und Lizenz | OK | Version 6.0 durchgängig: Dokumentkopf, `README.md` (zweimal: Versionszeile und Zitiervorschlag), `Claude.md` (Stand-Angabe), `build_pdf.py` (zwei Stellen), `build_docx.py` (zwei Stellen), Protokolleintrag. Haftungshinweis und Lizenzhinweis am Dokumentende erhalten. |
| 2.6 Automatisierte Prüfung | n/a | Keine Prüfskripte im Repo; manuelle Stichproben zu Nummerierung, Querverweisen und Quellenzuordnung durchgeführt. |

### Gefundene Fehler

| # | Stelle | Fehler | Schwere |
|---|---|---|---|
| 1 | `build_pdf.py` Z. 52 und Z. 342; `build_docx.py` Z. 36 und Z. 277 | Versionsstring stand noch auf „Version 4.0" (nicht in Validierung 19. April 2026 auf 5.0 nachgezogen). | Gering |

### Durchgeführte Bereinigungen

| # | Fehler | Maßnahme | Erledigt |
|---|---|---|---|
| 1 | Build-Skript-Version | `DOC_VERSION` und sichtbare Versionszeile in `build_pdf.py` und `build_docx.py` auf „Version 6.0" aktualisiert (vier Stellen). | Ja |

### Nachprüfung

- 2.1.1 – 2.1.5 nach Einarbeitung: OK
- 2.4.1, 2.4.2, 2.4.3 nach Ergänzung um Literaturnachweise: OK
- 2.5 Versionskonsistenz nach Bereinigung: OK (6.0 durchgängig in allen sechs Ankerpunkten)
- Automatisierte Skripte: n/a

### Abschluss

- Alle Fehler behoben: Ja
- Neue Version: 6.0
- PDF erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.pdf` via `build_pdf.py`)
- Word erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.docx` via `build_docx.py`)

---

## Validierung 22. April 2026 — Version 6.0 → Version 7.0

**Auslöser:** Web-Recherche zu den Hauptthemen des Arbeitspapiers (EU AI Act und Digital Omnibus, Sanders-Nachfolgeinitiative April 2026, Altman-Anschlag-Gerichtsverfahren, OECD Pillar 2, Q1-2026-Tech-Layoffs, Bürgerversicherungs-Reformprozess, IAB-Prognose). Vergleich gegen Bestand von Version 6.0. Vier neue belegbare Entwicklungen identifiziert; bereits vorhandene Inhalte (OECD Pillar-Two-Side-by-Side-Paket, KSR/ASK, No Robot Bosses Act, Q1-Layoff-Grunddaten, Anthropic Economic Index, Generationenkapital-Startphase) wurden nicht erneut aufgenommen.

### Aufgenommene Neuigkeiten

| # | Neuigkeit | Einarbeitung | Begründung Relevanz |
|---|---|---|---|
| 1 | Digital Omnibus on AI (19. November 2025): Kommissionsvorschlag zur Verschiebung der Hochrisiko-Pflichten bis max. 2. Dezember 2027 bzw. 2. August 2028; MEP-Zustimmung am 16./23. März 2026; Verlängerung der Art.-50-Kennzeichnungspflicht bis 2. November 2026; GPAI-Durchsetzung unverändert ab 2. August 2026 | § 4.3 (Ergänzung im Absatz „Europarechtliche Vorgaben") | Verändert den zeitlichen Vorlauf, in dem AI-Act-Definitionen als Anknüpfung für Steuertatbestände verfügbar werden |
| 2 | Sanders-Op-Ed vom 16. April 2026 und angekündigte Folge-Gesetzgebung (bundesweites Moratorium für neue KI-Rechenzentren bis Schutzmaßnahmen in Kraft) | § 4.5 (Erweiterung des Sanders-Absatzes um Nachtrag April 2026) | Aktualisiert den konkretesten politischen Vorstoß auf US-Bundesebene; zeigt Fortschreibung der Linie aus dem Oktober-2025-Report |
| 3 | Altman-Anschlag Gerichtsverfahren: Bundes-Anklagepunkte (versuchte Sprengmittel-Sachbeschädigung, nicht registrierte Feuerwaffe); mögliche Terror-Anklage; Verteidigungslinie Autismus und psychische Ausnahmesituation; Arraignment 5. Mai 2026 | § 8.4 (bestehender Absatz erweitert) | Konkretisierung eines bereits belegten Systemstabilitäts-Beispiels; keine neue Geschichte, sondern Vertiefung |
| 4 | Zweiter Altman-Vorfall (12. April 2026): Entlassung der beiden kurzzeitig festgenommenen Personen ohne Anklageerhebung am 16. April 2026 | § 8.4 (bestehender Absatz erweitert) | Vervollständigt die Darstellung des zweiten Vorfalls; verhindert Fehldeutung als zweite Straftat |

Nicht aufgenommen (bewusste Auslassungen):
- IAB-Prognose April 2026: Kernzahlen bereits in Version 6.0 vollständig abgebildet (Erwerbstätigenrückgang 20.000; Zuwachs bei öffentlichen Dienstleistern/Erziehung/Gesundheit; Umbruch-statt-Einbruch-Einordnung).
- OECD Pillar-Two-Einzel-Jurisdiktions-Aktionen im April 2026 (Deutschland-Draft, Türkei-Formulare, NL-Knowledge-Group): operative Einzeldetails ohne Auswirkung auf die Argumentationslinie.
- Sam-Altman/Vinod-Khosla-Folgeinterview Fortune: redaktioneller Kommentar, keine neue Quelle.
- Anthropic Economic Index 2026 Q2-Update: keine neue aggregierte Erkenntnis gegenüber der bereits referenzierten Index-Stelle in § 3.5.
- Microsoft/Amazon/Oracle Einzelunternehmens-Nennungen zu Q1-Layoffs: Gesamtzahl (~78.500) und Anteil (~48 %) sind ausreichend, Einzelnennungen erhöhen nicht die Aussagekraft.

### Prüfergebnis

| Prüfschritt | Ergebnis | Auffälligkeiten |
|---|---|---|
| 2.1.1 Gliederung | OK | 11 Kapitel + Executive Summary unverändert; keine leeren Abschnitte; Deutschland-These in Zusammenfassung referenziert. |
| 2.1.2 Nummerierung | OK | Kapitel 1–11 lückenlos; Unterabschnitte unverändert (1.1–11.5); fünf Robotersteuer-Typen, drei Hebel, sieben Empfehlungen stimmen. |
| 2.1.3 Querverweise | OK | Keine Querverweise hinzugefügt oder verändert. Bestehende §-Referenzen (2.1, 5.1, 5.2; Kapitel 3/5/5.4/8/10; Abschnitt 8.3/8.4) weiterhin gültig. |
| 2.1.4 Roter Faden | OK | Neue Einfügungen ordnen sich in die bestehende Rechts- (§ 4.3/4.5) und Systemstabilitäts-Argumentation (§ 8.4) ein; keine Architekturverschiebung. |
| 2.1.5 Formatierung | OK | Keine doppelten Trennlinien; Fett/Kursiv konsistent; Lead-Ins nicht verändert; Tabellen unverändert. |
| 2.2.1 Sachliche Richtigkeit | OK | Neue Fakten belegbar: Digital-Omnibus-Vorschlag (EK-Pressemitteilung, EP-Legislative-Train, EP-Pressemitteilung 23. März 2026); Sanders-Op-Ed (WFMD); Moreno-Gama-Verfahren (CNBC, CNN, NPR, Fortune); zweiter Vorfall/Entlassung (SF Standard). |
| 2.2.2 Redundanzprüfung | OK | Digital-Omnibus ist genau einmal im Dokument platziert (§ 4.3), AI-Act-Grundinformation bleibt an derselben Stelle; Sanders-Nachtrag verlängert den bestehenden Sanders-Block ohne neue Dopplung in Kapitel 8 oder 10; Altman-Vorfall bleibt in § 8.4 konzentriert. |
| 2.2.3 Argumentation | OK | Digital-Omnibus-Passage bleibt im Konjunktiv (Parlamentsposition, noch nicht endgültiges Inkrafttreten); Sanders-Nachtrag klar als angekündigt/flankierend markiert; Moreno-Gama-Passage sachlich, Unschuldsvermutung erhalten (Arraignment-Termin, Verteidigungslinie). |
| 2.2.4 Ausgewogenheit | OK | Moratorium-Vorschlag wird nicht bewertet, nur referiert; Verteidigungslinie Autismus/psychische Ausnahmesituation wird ohne Instrumentalisierung wiedergegeben; Entlassung des zweiten Paars ohne Anklage explizit festgehalten, um Fehldeutung zu vermeiden. |
| 2.3.1 Tippfehler und Grammatik | OK | Stichprobe der neuen Textstellen ohne Befund. |
| 2.3.2 Terminologie | OK | Neue Begriffe im Kontext erklärt: „Digital Omnibus on AI", „GPAI" (Allzweck-KI-Modelle), „Arraignment". Abkürzung GPAI bei Erstnennung aufgelöst. |
| 2.4.1 Vollständigkeit und Zuordnung | OK | Neue Einträge zugeordnet: Europäische Kommission Digital Omnibus und EP-Pressemitteilung in § 11.3; Sanders-Op-Ed in § 11.3; CNBC-Arraignment-Bericht und SF-Standard-Entlassungs-Meldung in § 11.5. Keine neuen Fließtext-Referenzen ohne Eintrag. |
| 2.4.2 Formale Einheitlichkeit | OK | Alle neuen Einträge APA-nah, Datumsangaben im Format „Monat YYYY" bzw. präzise Tagesdaten; vollständige URLs; keine URL-Shortener. |
| 2.4.3 Aktualität und Belastbarkeit | OK | Primärquellen (europa.eu-Legislative-Train, sanders.senate.gov-Content) für institutionelle Aussagen; unabhängige Mehrfachbelege für das Strafverfahren (CNN, CNBC, NPR, Fortune, SF Standard). |
| 2.4.4 URL-Prüfung (Stichprobe) | OK | Stichprobe am 22. April 2026: europarl.europa.eu Pressemitteilung 23. März 2026 erreichbar; digital-strategy.ec.europa.eu Digital-Omnibus-Landingpage erreichbar; cnbc.com 14.-April-Bericht erreichbar; sfstandard.com 16.-April-Bericht erreichbar. |
| 2.4.5 Zitatgenauigkeit | OK | Postponement-Fristen (2. Dezember 2027 bzw. 2. August 2028 max.; Kennzeichnungspflicht-Verschiebung auf 2. November 2026) und Daten (16./23. März 2026 Ausschuss/Plenum) korrekt übernommen; Arraignment-Datum 5. Mai 2026, Anklagepunkte, Entlassungsdatum 16. April 2026 korrekt wiedergegeben. |
| 2.4.6 Verifizierungsbedürftige Einträge | OK | Verbleibt nur de la Feria et al. 2022 als verifizierungsbedürftig; alle Neuzugänge verifiziert und mit URL belegt. |
| 2.5 Versionskonsistenz und Lizenz | OK | Version 7.0 durchgängig: Dokumentkopf, `README.md` (Versionszeile und Zitiervorschlag), `Claude.md` (Stand-Angabe), `build_pdf.py` (zwei Stellen: `DOC_VERSION` und sichtbare Metazeile), `build_docx.py` (zwei Stellen), Protokolleintrag. Haftungs- und Lizenzhinweis am Dokumentende erhalten. |
| 2.6 Automatisierte Prüfung | n/a | Keine Prüfskripte im Repo; manuelle Stichproben zu Nummerierung, Querverweisen und Quellenzuordnung durchgeführt. |

### Gefundene Fehler

Keine Fehler gefunden; die Version 6.0 war konsistent und nur um neue Sachstände zu ergänzen.

### Durchgeführte Bereinigungen

| # | Fehler | Maßnahme | Erledigt |
|---|---|---|---|
| — | — | Keine Bereinigung erforderlich; ausschließlich Ergänzungen neuer Sachstände. | — |

### Nachprüfung

- 2.1.1 – 2.1.5 nach Einarbeitung: OK
- 2.4.1 – 2.4.5 nach Ergänzung der Literaturnachweise: OK
- 2.5 Versionskonsistenz: OK (7.0 durchgängig in allen sechs Ankerpunkten)
- Automatisierte Skripte: n/a

### Abschluss

- Alle Fehler behoben: Ja (keine gefunden)
- Neue Version: 7.0
- PDF erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.pdf` via `build_pdf.py`)
- Word erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.docx` via `build_docx.py`)
