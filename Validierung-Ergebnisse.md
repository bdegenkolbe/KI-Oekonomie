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

Systematische Web-Recherche zu den Hauptthemen des Papiers (KI-/Robotersteuer, Wertschöpfungsabgabe, OECD Pillar 2, OpenAI-Papier, Sanders, Mistral, deutsche KI-Politik, IAB-Prognose 2026) ergab mehrere seit Veröffentlichung von Version 4.0 erschienene bzw. nicht berücksichtigte Quellen und Ereignisse. Keine Korrektur eigenständiger Fehler, sondern inhaltliche Aktualisierung mit neuen Belegen; entsprechend Versionsanhebung gemäß `Validierung.md` § 4 (inhaltliche Ergänzung → neue Version).

### Neu aufgenommene Sachverhalte

| # | Thema | Stelle im Hauptdokument | Quelle (neu im Lit.-Verzeichnis) |
|---|---|---|---|
| 1 | Korinek/Lockwood „Public Finance in the Age of AI: A Primer" (NBER WP 34873 / Brookings, Jan. 2026) — Zwei-Phasen-Framework, Konsumsteuer statt KI-Kapital-Steuer in Phase 1, AGI-Szenario in Phase 2 | § 3.3 (neuer Absatz) | § 11.1 |
| 2 | Arthur Mensch / Mistral: Vorschlag einer EU-weiten umsatzbasierten KI-Abgabe (1–1,5 %) mit Zweckbindung Kulturfonds (FT-Gastbeitrag 20. März 2026) | § 4.5 (neuer Absatz) | § 11.5 |
| 3 | Sanders / Ocasio-Cortez, AI Data Center Moratorium Act (25. März 2026) — Kontext-Ergänzung zum Sanders-Report Oktober 2025 | § 4.5 (in vorhandenen Sanders-Absatz integriert) | § 11.3 |
| 4 | Bundeskanzler Merz, Hannover Messe April 2026: Forderung nach Lockerung der EU-KI-Regulierung; keine KI-/Robotersteuer in Koalitionsvereinbarung | § 4.5 (neuer Absatz) | § 11.3 |
| 5 | OECD Pillar 2 in Deutschland: Mindeststeuergesetz-Anpassung 23. Dez. 2025; BMF-Entwurfsverordnung 8. April 2026; Erstfrist 30. Juni 2026 | § 4.4 (neuer Absatz) | § 11.3 (BMF 2026) |
| 6 | EU Digital Services Tax 2025/26: Italien ohne Inlandsschwelle; Sätze 3–5 %; Meta überwälzt ab 1. Juli 2026 an Werbetreibende | § 4.4 (neuer Absatz) | § 11.5 (Euronews Jan. 2026) |
| 7 | HDE-Position gegen KI-Steuer (2026) — Ergänzung des wirtschaftsnahen Ablehnungsfeldes neben IW Köln | § 4.2 (Ergänzungssatz) | § 11.3 |
| 8 | Generationenkapital-Start Januar 2026 mit 10 Mrd. Euro Startkapital | § 8.6 (Satz im Absatz „Sozialpolitik") | bereits in § 11 implizit, keine Dubletten |
| 9 | IAB-Prognose März 2026: Sozialversicherungspflichtige Beschäftigung sinkt 2026 erstmals seit 2009 — Transformationskrise/Demografie überlagert KI-Effekte mittelfristig | neuer Eintrag in § 11.5 | § 11.5 |
| 10 | Sanders-Report: vollständige Titelangabe „The Big Tech Oligarchs' War Against Workers: AI and Automation" verifiziert | § 11.3 (Titel ergänzt, Verifizierungsvermerk entfernt) | § 11.3 |

### Prüfergebnis

| Prüfschritt | Ergebnis | Auffälligkeiten |
|---|---|---|
| 2.1.1 Gliederung | OK | 11-Kapitel-Struktur, Zusammenfassung und ToC unverändert; neue Absätze bleiben in bestehenden Unterabschnitten. |
| 2.1.2 Nummerierung | OK | Keine Änderung an Unterabschnitt-Nummerierung. Fünf Typen, drei Hebel, sieben Empfehlungen weiterhin konsistent. |
| 2.1.3 Querverweise | OK | Keine Umnummerierungen; bestehende §-Verweise bleiben gültig. Neue Abschnitte setzen keine zusätzlichen Querverweise, die pflegepflichtig wären. |
| 2.1.4 Roter Faden | OK | Korinek/Lockwood stärkt § 3 (Forschungsstand), Mensch/Merz/Sanders-AOC stärken § 4.5 (jüngste Initiativen), OECD-Pillar-2- und DST-Updates stärken § 4.4 (Sekundärrecht). Die Deutschland-These bleibt unberührt. |
| 2.1.5 Formatierung | OK | Keine doppelten Trennlinien, Lead-Ins („Arthur Mensch / Mistral (März 2026):", „Deutsche Bundesregierung / Merz (April 2026):", „Korinek & Lockwood (2026):") folgen der etablierten Fettungskonvention. |
| 2.2.1 Sachliche Richtigkeit | OK | Alle neuen Zahlen belegt (Mensch 1–1,5 %; Generationenkapital 10 Mrd. EUR Startkapital, 0,2 Pp.; Pillar-2-Frist 30. Juni 2026; DST-Sätze 3/5 %; Meta-Überwälzung 1. Juli 2026). |
| 2.2.2 Redundanzprüfung | OK | Mensch-Vorschlag in § 4.5 mit klarer Abgrenzung gegenüber OpenAI-Vorschlag (KI-Trainingsdaten-Kontext, nicht Beschäftigungs-Substitution). Sanders-Moratorium als Kontext-Satz im bestehenden Sanders-Absatz, nicht als Parallel-Eintrag. |
| 2.2.3 Argumentation | OK | Korinek/Lockwood-Phasenlogik passt zum in § 3.5 bereits formulierten „szenariorobust"-Plädoyer; Merz-Position flankiert die in § 4.2 beschriebene wirtschaftsnahe Linie, ohne die Deutschland-These zu durchkreuzen. |
| 2.2.4 Ausgewogenheit | OK | Wirtschaftsnahes Ablehnungsfeld (IW Köln + HDE) jetzt breiter; Gegengewichte aus Forschung (Korinek/Lockwood, Mensch) ausgewogen gegenübergestellt. |
| 2.3.1 Tippfehler und Grammatik | OK | Stichprobe der neuen Absätze ohne Befund. |
| 2.3.2 Terminologie | OK | Neue Abkürzungen IIR, UTPR, QDMTT im Kontext eingebettet; DAC9 genannt, Bezug zu Pillar 2 im selben Absatz. HDE (Handelsverband Deutschland) ausgeschrieben. AGI bei Erstnennung in § 3.3 erklärt. |
| 2.4.1 Vollständigkeit und Zuordnung | OK | Alle neuen Fließtext-Erwähnungen haben korrespondierende Einträge in § 11; Sanders-Titel verifiziert und Verifizierungshinweis entfernt. Der Vermerk zu de la Feria et al. 2022 bleibt erhalten. |
| 2.4.2 Formale Einheitlichkeit | OK | APA-Stil in neuen Einträgen beibehalten; URLs vollständig; Datumsangaben „Monat YYYY". |
| 2.4.3 Aktualität und Belastbarkeit | OK | Korinek/Lockwood als NBER-Arbeitspapier / Brookings-Working-Paper direkt bei den Primärstellen verlinkt; Mensch-Vorschlag über Tech.eu / AI Business verlinkt; OECD Pillar 2 mit BMF-Primärquelle. |
| 2.4.4 URL-Prüfung (Stichprobe) | OK | Zwei neue URLs stichprobenartig geprüft: NBER-Link zu WP 34873 liefert Abstract und PDF-Link; Tech.eu-Beitrag vom 20. März 2026 erreichbar; Sanders-PDF (HELP-Minderheitsbericht) über sanders.senate.gov erreichbar. Vorbestehende OpenAI-URL wurde in Validierung 1.0 → 2.0 geprüft und bleibt gültig. |
| 2.4.5 Zitatgenauigkeit | OK | Mensch-Vorschlag 1–1,5 % und Kulturfonds-Zweck korrekt wiedergegeben; Korinek/Lockwood-Phasenlogik entspricht Abstract und Brookings-Zusammenfassung; Generationenkapital-Zahl 10 Mrd. Euro und Beitragssatz 0,2 Pp. entsprechen BMF-Monatsbericht und aktueller Projektbeschreibung. |
| 2.4.6 Verifizierungsbedürftige Einträge | Bereinigt | Sanders-Titel vollständig verifiziert („The Big Tech Oligarchs' War Against Workers: AI and Automation"); Verifizierungsvermerk in § 11.3 entfernt. de la Feria et al. 2022 bleibt weiter als verifizierungsbedürftig markiert. |
| 2.5 Versionskonsistenz und Lizenz | OK | Version 5.0 in Dokumentkopf, `README.md` (Stand und Zitiervorschlag), `Claude.md` (Aktueller Stand), `build_pdf.py` und `build_docx.py` einheitlich. Lizenzhinweis am Dokumentende und in `README.md` erhalten. |
| 2.6 Automatisierte Prüfung | n/a | Keine dedizierten Prüfskripte. Manuelle Stichproben gemäß § 2.6. |

### Durchgeführte Bereinigungen

| # | Fehler / Lücke | Maßnahme | Erledigt |
|---|---|---|---|
| 1 | Fehlender Forschungsstand Korinek/Lockwood (Januar 2026) | § 3.3 um eigenen Absatz ergänzt; Literatureintrag § 11.1 | Ja |
| 2 | Fehlender Mensch/Mistral-Vorschlag (März 2026) | § 4.5 um eigenen Absatz ergänzt; Literatureintrag § 11.5 | Ja |
| 3 | Sanders-Report ohne vollständigen Titel und ohne Moratorium-Kontext | § 4.5 Sanders-Absatz um AI Data Center Moratorium Act erweitert; § 11.3 Titel „The Big Tech Oligarchs' War Against Workers" verifiziert, Verifizierungsvermerk entfernt; zweiter Eintrag für Moratorium-Gesetzentwurf in § 11.3 | Ja |
| 4 | Fehlende Position der Bundesregierung Merz (April 2026) | § 4.5 um eigenen Absatz zur deutschen Regierungslinie ergänzt; Literatureintrag § 11.3 | Ja |
| 5 | Fehlende OECD-Pillar-2-Implementationsdaten Deutschland | § 4.4 um Absatz (Mindeststeuergesetz, BMF-Entwurfsverordnung, Frist 30. Juni 2026) ergänzt; Literatureintrag § 11.3 | Ja |
| 6 | Fehlende DST-Updates 2025/26 (Italien, Österreich/Tschechien, Meta-Überwälzung) | § 4.4 um Absatz ergänzt; Literatureintrag § 11.5 (Euronews Jan. 2026) | Ja |
| 7 | HDE-Position nicht abgebildet | § 4.2 Satz ergänzt; Literatureintrag § 11.3 | Ja |
| 8 | Generationenkapital-Start 2026 nicht ausgewiesen | § 8.6 Satz ergänzt (10 Mrd. EUR, Erträge ab Mitte 2030er) | Ja |
| 9 | IAB-Kurzfristprognose 2026 nicht verortet | § 11.5 um IAB-Prognose März 2026 ergänzt (keine Änderung am Fließtext von § 7/§ 8 nötig, da Langfristzahlen dort weiter tragen) | Ja |
| 10 | Versionsanhebung 4.0 → 5.0 | Hauptdokument-Kopf, `README.md`, `Claude.md`, Build-Skripte, dieses Protokoll | Ja |

### Nachprüfung

- 2.1.1 / 2.1.2 / 2.1.3 / 2.1.4 nach Bereinigung: OK (Struktur/Nummerierung/Querverweise/Roter Faden stimmig)
- 2.2.2 Redundanzprüfung nach Bereinigung: OK (keine Doppelung — OpenAI-Vorschlag, Mensch-Vorschlag, Merz-Position, Sanders-Vorstoß klar abgegrenzt)
- 2.4.1 Vollständigkeit nach Bereinigung: OK (alle Fließtext-Nennungen mit Literatureinträgen)
- 2.4.6 Verifizierungsbedürftige Einträge nach Bereinigung: OK (Sanders verifiziert; de la Feria bleibt markiert)
- 2.5 Versionskonsistenz nach Bereinigung: OK (5.0 durchgängig)
- Automatisierte Skripte: n/a

### Abschluss

- Alle Aktualisierungen eingearbeitet: Ja
- Neue Version: 5.0
- PDF erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.pdf`, via `build_pdf.py`)
- Word erstellt: Ja (`Arbeitspapier_KI_Robotik_Besteuerung.docx`, via `build_docx.py`)

**Hinweis:** Die Aktualisierung hält die Grundarchitektur (11 Kapitel, Deutschland-These, Drei-Hebel-Modell) unverändert. Die Ergänzungen erweitern die Literatur- und Initiativen-Basis so, dass der Stand bis Mitte April 2026 abgebildet ist. Künftige Iterationen sollten, sobald verfügbar, die finale Fassung des Korinek/Lockwood-Kapitels im NBER-Band „The Economics of Transformative AI" nachtragen sowie die Umsetzung oder das Scheitern des Mensch-Vorschlags in der EU-Kommission verfolgen.
