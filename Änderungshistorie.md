# Änderungshistorie.md — Logbuch der täglichen Update-Läufe

**Zweck:** Diese Datei protokolliert jeden täglichen Recherche- und Update-Lauf des Daily-Update-Prompts. Pro Lauf entsteht ein zeitstempelbasierter Block — die Historie wird **nicht gelöscht**, sondern wächst chronologisch an.

**Verhältnis zu `Validierung-Ergebnisse.md`:** Diese Datei dokumentiert den **Recherche- und Quellenfluss** (was wurde im Web gefunden, was wurde übernommen, was wurde verworfen). Die fachlich-inhaltliche Validierung des Hauptdokuments wird weiterhin in `Validierung-Ergebnisse.md` protokolliert. Beide Dateien sind komplementär.

**Format pro Eintrag:**

```
## YYYY-MM-DD — Lauf NNN — Version X.0 → Version Y.0

### Recherchekorridor

- Genutzte Cluster aus `Suchthemen.md`: A, B, …
- Zeitfenster: letzte N Tage / Stunden
- Anzahl Suchanfragen: NN

### Gefundene Quellen

| # | Cluster | Quelle (Autor/Institution, Titel, Datum) | URL | Bewertung |
|---|---------|-----------------------------------------|-----|-----------|
| 1 |         |                                         |     | übernommen / verworfen / Dublette |

### Eingearbeitete Änderungen

| # | Stelle (§) | Art (Ergänzung / Aktualisierung / Korrektur) | Inhalt in einem Satz | Quelle # |
|---|-----------|----------------------------------------------|----------------------|----------|
| 1 |           |                                              |                      |          |

### Verworfene Treffer (mit Begründung)

| # | Quelle | Cluster | Begründung |
|---|--------|---------|------------|
| 1 |        |         | außerhalb Zeitfenster / Negativliste / Dublette / Quellenniveau |

### Verarbeitungsschritte

- Recherche abgeschlossen: Ja / Nein
- Deduplikation gegen Hauptdokument: Ja / Nein
- Validierung gemäß `Validierung.md` ausgeführt: Ja / Nein (Verweis auf Block in `Validierung-Ergebnisse.md`)
- PDF erstellt (`build_pdf.py`): Ja / Nein
- Word erstellt (`build_docx.py`): Ja / Nein
- Versionsnummer in Hauptdokument, README, Validierung-Ergebnisse aktualisiert: Ja / Nein
- Branch auf main gemerged und gelöscht: Ja / Nein

### Auffälligkeiten / offene Punkte

- 

---
```

**Erstinitialisierung:** Datei angelegt am 2026-05-07. Erster regulärer Lauf folgt mit dem nächsten Aufruf des Daily-Update-Prompts.

---

## 2026-06-28 — Lauf 001 — Version 22.0 → Version 23.0

### Recherchekorridor

- Genutzte Cluster aus `Suchthemen.md`: A, B, C, D, E, F, G, H, I, J (alle zehn Cluster gestreift; Cluster F mit zwei aufgenommenen Treffern; Cluster D mit drei aufgenommenen Treffern; Cluster B mit einem aufgenommenen Treffer; Cluster G — Gesundheitssektor — fünftes Mal in Folge ohne neue belegbare Treffer im 7-Tage-Fenster).
- Zeitfenster: Strikt 7 Tage (21.–28. Juni 2026) für Cluster A, B, C, D, E, G, H; 48 Stunden für Cluster F und I. **Einmalige Erweiterung** auf 9. Mai – 20. Juni 2026 für besonders zentrale Items zwischen dem letzten Lauf (8. Mai 2026, Version 22.0) und dem strikten Fenster — Vorgehen analog zur Lauf-003-Präzedenz vom 7. Mai 2026 (Bloomberg-Editorial 29. April 2026 im erweiterten Fenster), hier nur skaliert auf die siebenwöchige Pausenlücke. Aufnahmegrenze: Nur Items mit primärer Themenrelevanz (KI-Steuer, KI-Sozialfinanzierung, Sovereign-Wealth-/Displacement-Fund, EU-AI-Act-Trilog, SEC-Disclosure-Kausalattribution KI/Personalabbau) — keine generischen Markt-/Frontier-Updates.
- Anzahl Suchanfragen: 14 (Web-Suche).

### Gefundene Quellen

| # | Cluster | Quelle (Autor/Institution, Titel, Datum) | URL | Bewertung |
|---|---------|-----------------------------------------|-----|-----------|
| 1 | F | Bloomberg, *Oracle Layoffs Fueled by AI, Reduces Workforce by 21,000*, 22. Juni 2026 | https://www.bloomberg.com/news/articles/2026-06-22/oracle-layoffs-fueled-by-ai-reduces-workforce-by-21-000 | übernommen |
| 2 | F | CNBC, *Oracle sheds 21,000 roles over past year amid tech giant AI shift*, 23. Juni 2026 | https://www.cnbc.com/2026/06/23/oracle-ai-job-cuts-layoffs-21000.html | übernommen (Sammelbeleg) |
| 3 | F | Fast Company, *Oracle layoffs: 21,000 jobs cut amid AI shift, SaaSpocalypse*, 22./23. Juni 2026 | https://www.fastcompany.com/91563655/oracle-layoffs-orcl-stock-21000-jobs-cut-amid-ai-shift-saas-apocalypse | übernommen (Sammelbeleg) |
| 4 | F | Oracle Corp., *Form 10-K — FY2026*, SEC-Einreichung 22. Juni 2026 | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526277521/orcl-ex32_01.htm | übernommen (Primärbeleg) |
| 5 | D | sanders.senate.gov, *NEWS: Sanders Introduces Legislation to Create $7 Trillion AI Sovereign Wealth Fund*, 18. Juni 2026 | https://www.sanders.senate.gov/press-releases/news-sanders-introduces-legislation-to-create-7-trillion-ai-sovereign-wealth-fund/ | übernommen (Primärbeleg) |
| 6 | D | Roll Call, *Sovereign wealth fund tax on AI companies unveiled by Sanders*, 18. Juni 2026 | https://rollcall.com/2026/06/18/sovereign-wealth-fund-tax-on-ai-companies-unveiled-by-sanders/ | übernommen (Sammelbeleg) |
| 7 | D | Tech Times, *Sanders AI Sovereign Wealth Fund: Experts Flag Dividend Trap in $7 Trillion Seizure Bill*, 22. Juni 2026 | https://www.techtimes.com/articles/318867/20260622/sanders-ai-sovereign-wealth-fund-experts-flag-dividend-trap-7-trillion-seizure-bill.htm | übernommen (Sammelbeleg, kritische Würdigung) |
| 8 | D | Fortune, *Bernie Sanders wants Americans to own a piece of AI*, 3. Juni 2026 | https://fortune.com/2026/06/03/bernie-sanders-ai-ownership-sovereign-wealth-fund-electrification/ | übernommen (Sammelbeleg, Vorlauf) |
| 9 | D | Anthropic, *Policy on the AI Exponential — Economic Policy Framework*, 11. Juni 2026 | https://www.anthropic.com/policy-on-the-ai-exponential/epf \| https://www-cdn.anthropic.com/files/4zrzovbb/website/9ea607a5dd67c168093829b701f3a0a6d21156d5.pdf | übernommen (Primärbeleg) |
| 10 | D | Fortune, *Anthropic just proposed taxing itself to pay for the jobs its AI destroys*, 11. Juni 2026 | https://fortune.com/2026/06/11/anthropic-dario-amodei-ai-jobs-tax-displacement-fund/ | übernommen (Sammelbeleg, 3 %-Selbstverpflichtung) |
| 11 | D/I | Anthropic, *Anthropic Economic Index report: Cadences*, Juni 2026 | https://www.anthropic.com/research/economic-index-june-2026-report | übernommen (Primärbeleg, empirische Flankierung) |
| 12 | B | Rat der EU, *Artificial Intelligence: Council and Parliament agree to simplify and streamline rules*, 7. Mai 2026 | https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/ | übernommen (Primärbeleg) |
| 13 | B | Sidley Data Matters, *EU Lawmakers Reach Provisional Agreement to Delay Key EU AI Act Obligations*, 22. Juni 2026 | https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/ | übernommen (Sekundärbeleg, Schlussabstimmungstermin 16. Juni 2026 und erwartete Ratsannahme 29. Juni 2026) |
| 14 | F | Challenger, Gray & Christmas, *May 2026 Job Cuts Report*, 4. Juni 2026 | https://www.challengergray.com/wp-content/uploads/2026/06/Challenger-Report-May-2026.pdf | übernommen (Primärbeleg) |
| 15 | F | Bloomberg, *US Tech Sector Announces Most Job Cuts in Nearly Two Years*, 4. Juni 2026 | https://www.bloomberg.com/news/articles/2026-06-04/us-tech-sector-announces-most-job-cuts-in-nearly-two-years | übernommen (Sammelbeleg, Aggregat-Einordnung) |
| 16 | F | TechCrunch, *The running list: major tech layoffs in 2026 where employers cited AI*, 22. Juni 2026 | https://techcrunch.com/2026/06/22/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/ | übernommen (Sammelbeleg, 75.000+ AI-zitierte Stellen) |
| 17 | F | SkillSyncer, *Tracker Stand 27. Juni 2026 — 185.894 Personen aus 267 Layoff-Ereignissen, rund 1.044/Tag, 56 % KI-bezogen* | https://skillsyncer.com/layoffs-tracker | übernommen (Sammelbeleg) |
| 18 | C | OECD, *Pillar Two Implementation 2026 — Side-by-Side Package* | https://www.oecd.org/en/topics/sub-issues/global-minimum-tax/global-anti-base-erosion-model-rules-pillar-two.html | verworfen (außerhalb 7-Tage-Fenster; bereits in Version 9.0 / § 4.4 referenziert) |
| 19 | A | NBER WP w34873, *Public Finance in the Age of AI: A Primer* | https://www.nber.org/system/files/working_papers/w34873/w34873.pdf | verworfen (Datum unklar / vermutlich außerhalb Fenster; gegebenenfalls in einem späteren Lauf für § 3-Ergänzung zu prüfen) |
| 20 | A | NBER WP w34984 / w35046, *Forecasting the Economic Effects of AI / AI Employment Effects* | https://www.nber.org/system/files/working_papers/w35046/w35046.pdf | verworfen (Datum unklar; potenziell für späteren Lauf in § 3 zu prüfen) |
| 21 | E | IAB-Kurzbericht *Arbeitsmarktentwicklung 2026 — Erwerbstätigkeit Juni-Korridor 45,78 – 45,99 Mio.* | https://doku.iab.de/kurzber/2026/kb2026-05.pdf | verworfen (Wahrscheinlichkeit 2/3 ohne Datumsfixierung im 7-Tage-Fenster; bestehende IAB-Frühjahrsprognose vom 24. März 2026 in § 1.1 bleibt aktueller Anker) |
| 22 | E | Bundesbank-Monatsbericht Juni 2026 (Deutschland-Prognose) | https://publikationen.bundesbank.de/publikationen-de/berichte-studien/monatsberichte/aktuelle-monatsberichte-922214 | verworfen (Veröffentlichung im Monat ohne KI-spezifische Aussage zum Steuer-/Sozialstaatsbezug im 7-Tage-Fenster) |
| 23 | G | G-BA / gematik / BfArM Juni 2026 (DiGA / KI-Hochrisiko) | https://www.g-ba.de/ \| https://fachportal.gematik.de/zielgruppen/diga-hersteller | verworfen (fünftes Mal in Folge ohne KI-spezifische Beschlüsse im 7-Tage-Fenster) |
| 24 | I | Tesla Optimus / Figure 03 / Boston Dynamics Atlas — Juni-2026-Deployment-Updates | https://newmarketpitch.com/blogs/news/humanoid-robotics-optimus-deployment-tracker \| https://www.teslarati.com/tesla-optimus-awe-2026-shanghai/ | verworfen (keine Tagesmeldung mit politisch-fiskalischer Implikation im 48-Stunden-Fenster) |
| 25 | J | IFR World Robotics 2025/2026 — IRAP-Bezug Italien | https://ifr.org/worldrobotics | verworfen (keine Aktualisierung im 7-Tage-Fenster) |

### Eingearbeitete Änderungen

| # | Stelle (§) | Art | Inhalt in einem Satz | Quelle # |
|---|-----------|-----|----------------------|----------|
| 1 | § 1.1 | Ergänzung | Neuer Absatz nach dem Demografie-Satz: Oracle-Form-10-K vom 22. Juni 2026 (Belegschaft 162.000 → 141.000, Restrukturierungsaufwand 1,84 Mrd. USD, SEC-Wortlaut „adoption and deployment of AI technologies … resulted, and may continue to result, in reductions to our workforce", Bereiche Revenue/Health Sciences −30 %, OCI/AI weitgehend geschont); Challenger Mai-Report (KI 38.579 / 40 %, YTD 87.714 / 22 %; Tech 38.242 Mai / 123.653 YTD, +65 % YoY); Tracker Stand 27. Juni 2026 (185.894 Personen aus 267 Layoff-Ereignissen, rund 1.044/Tag, 56 % KI-bezogen = 156.270 Personen / 150 Unternehmen); Bloomberg US-Tech-Einordnung 4. Juni 2026. AI-Washing-Vorbehalt explizit. | 1–4, 14–17 |
| 2 | § 4.4 | Aktualisierung | EU AI Act Digital Omnibus: Schluss­abstimmung im EP 16. Juni 2026, Ratsannahme erwartet 29. Juni 2026; Hochrisiko-Verschiebung 2. Dezember 2027 (Anhang III) / 2. August 2028 (Anhang I); neues CSAM-/NCII-Verbot 2. Dezember 2026; Watermarking nach Art. 50 verschoben auf 2. Dezember 2026. | 12, 13 |
| 3 | § 4.5 | Ergänzung | Sanders-Block ergänzt um *American AI Sovereign Wealth Fund Act* (18. Juni 2026): 50 %-Equity-Transfer (OpenAI, Anthropic, xAI), Fondsvolumen rund 7 Bio. USD, geplante Jahresdividende 5 %, Pro-Kopf-Auszahlung rund 1.045 USD. Strukturelle Schwächen (kein Veräußerungsrecht, keine Dividenden der Zielunternehmen, rund 350 Mrd. USD jährlich nötig) im Konjunktiv. | 5–8 |
| 4 | § 4.5 | Ergänzung | Neuer Anthropic-Block vor Bloomberg-Editorial: Drei-Tier-Plan (5 %, 10 %, beispielloses Arbeitslosigkeitsszenario); Kandidaten-Einnahmequellen (Kapitalertrag, Konsum, sektorspezifische Abgaben auf KI-Nutzung nach Tokens/Compute/Umsatz, „Digital Dividends"); UBI, AI Sovereign Wealth Funds und Worker-Equity-Modelle als Verwendungsoptionen; 200 Mio. USD *Economic Futures Research Fund* + 150 Mio. USD Fellowship; Amodei-Selbstverpflichtung rund 3 % AI-Revenue für *Displacement Fund*; *Cadences*-Report 9.700 Survey-Antworten, US-Layoffs-and-Discharges-Rate 1,1 %/Monat. | 9–11 |
| 5 | § 5.4 | Ergänzung | Staatsfonds-Block ergänzt um Querverweis auf Sanders-SWF-Act (Equity-Variante) und Anthropic-3-%-Revenue (Revenue-Variante); definiert erstmals Korridor zwischen Equity- und Revenue-Anknüpfung für KI-Staatsfondsmodell. | 5, 9 |
| 6 | § 11.3 | Ergänzung | Sechs neue Einträge: Sanders 18. Juni 2026; Anthropic Economic Policy Framework 11. Juni 2026; Anthropic Economic Index *Cadences* Juni 2026; Rat der EU 7. Mai 2026; EP Schlussabstimmung 16. Juni 2026 zum Digital Omnibus on AI. | 5, 9, 11, 12, 13 |
| 7 | § 11.5 | Ergänzung | Fünf neue Sammelbelege: Bloomberg/CNBC/Fast Company/HR Director/SEC Oracle 22./23. Juni 2026; Challenger/Bloomberg/Tech Jacks/Outsource Accelerator Mai-Report 4. Juni 2026; Sanders/Roll Call/Fortune/Business Report/Tech Times SWF Act 3./18. Juni 2026; Fortune/Anthropic/Pebblous/Go-to-Agency Anthropic-Framework 11. Juni 2026; TechCrunch/SkillSyncer/TrueUp/InformationWeek Tracker 22./27. Juni 2026. | 1–4, 6–11, 14–17 |
| 8 | Aktualitätshinweis | Aktualisierung | Schnittangabe auf „Lauf 001 vom 28. Juni 2026" geändert; alle fünf neuen Items als Kurzfassung in den Auflistungstext aufgenommen; vorhergehende Aktualitätsanker (Mai 2026) bleiben im hinteren Teil des Hinweises erhalten. | 1–17 |
| 9 | README.md | Aktualisierung | Versionssprung 22.0 → 23.0 (Versionszeile, Zitiervorschlag, neuer Versions-Eintrag in der KI-Offenlegung mit den fünf neuen Items; Stand „Anfang Mai 2026" → „Ende Juni 2026"). | — |
| 10 | Validierung-Ergebnisse.md | Ergänzung | Neuer Validierungsblock „Validierung 28. Juni 2026 (Lauf 001 vom 28. Juni 2026) — Version 22.0 → Version 23.0" mit Prüftabelle 2.1.1 – 2.6, Aufnahmetabelle und Abschluss „alle Fehler behoben: Ja (keine Fehler gefunden)". | — |

### Verworfene Treffer (mit Begründung)

| # | Quelle | Cluster | Begründung |
|---|--------|---------|------------|
| 1 | OECD Pillar Two Side-by-Side Package | C | Außerhalb 7-Tage-Fenster; in Version 9.0 / § 4.4 bereits referenziert. |
| 2 | NBER WP w34873 *Public Finance in the Age of AI: A Primer* | A | Datum unklar / vermutlich außerhalb Fenster; potenziell für späteren Lauf zu prüfen. |
| 3 | NBER WP w34984 / w35046 (AI Employment / Forecasting) | A | Datum unklar; potenziell für späteren Lauf in § 3 zu prüfen. |
| 4 | IAB-Kurzbericht Juni 2026 (Korridor 45,78 – 45,99 Mio.) | E | Wahrscheinlichkeit 2/3 ohne Datumsfixierung im 7-Tage-Fenster; bestehende IAB-Frühjahrsprognose 24. März 2026 in § 1.1 bleibt aktueller Anker. |
| 5 | Bundesbank-Monatsbericht Juni 2026 | E | Veröffentlichung im Monat ohne KI-spezifische Aussage zum Steuer-/Sozialstaatsbezug im 7-Tage-Fenster. |
| 6 | G-BA / gematik / BfArM Juni 2026 | G | Fünftes Mal in Folge ohne KI-spezifische Beschlüsse im 7-Tage-Fenster. |
| 7 | Tesla Optimus / Figure 03 / Boston Dynamics Atlas Juni-2026-Deployment-Updates | I/J | Keine Tagesmeldung mit politisch-fiskalischer Implikation im 48-Stunden-Fenster; Markt-/Capex-Befund über Cluster F abgedeckt. |
| 8 | IFR World Robotics 2025/2026 | J | Keine Aktualisierung im 7-Tage-Fenster. |
| 9 | BAG-Mitbestimmung-Urteil 2026 (KI Betriebsrat) | B | Datum unklar / Sekundärquellen ohne Primärentscheidungs-Datum im 7-Tage-Fenster; gegebenenfalls in einem späteren Lauf zu prüfen, sobald die Primärentscheidung mit Datum vorliegt. |

### Verarbeitungsschritte

- Recherche abgeschlossen: Ja
- Deduplikation gegen Hauptdokument: Ja
- Validierung gemäß `Validierung.md` ausgeführt: Ja (Block „Validierung 28. Juni 2026 (Lauf 001 vom 28. Juni 2026) — Version 22.0 → Version 23.0" in `Validierung-Ergebnisse.md`)
- PDF erstellt (`build_pdf.py`): Ja
- Word erstellt (`build_docx.py`): Ja
- Versionsnummer in Hauptdokument, README, Validierung-Ergebnisse aktualisiert: Ja
- Branch auf main gemerged und gelöscht: erfolgt am Ende dieses Laufs
- E-Mail-Versand (Phase 5b): siehe „Auffälligkeiten / offene Punkte"
- WhatsApp-Versand (Phase 5b): siehe „Auffälligkeiten / offene Punkte"

### Auffälligkeiten / offene Punkte

- Erster Lauf nach rund siebenwöchiger Pause (vorhergehender Lauf 001 am 8. Mai 2026, Version 22.0); der Recherchekorridor wurde **einmalig** auf 9. Mai – 20. Juni 2026 erweitert (zusätzlich zum strikten 7-Tage-Fenster 21.–28. Juni 2026), um pivotale Items wie Anthropic Economic Policy Framework (11. Juni 2026), Sanders American AI Sovereign Wealth Fund Act (18. Juni 2026), EU AI Act Digital Omnibus EP-Schlussabstimmung (16. Juni 2026) und Challenger Mai-Report (4. Juni 2026) zu erfassen. Diese Erweiterung ist im Aktualitätshinweis explizit benannt; künftige Läufe kehren zum strikten 7-Tage-/48-Stunden-Fenster zurück.
- Oracle-Form-10-K-Disclosure (22. Juni 2026) ist die erste SEC-pflichtige Kausalattribution KI/Personalabbau eines Top-Cloud-/Datenbank-Konzerns; sie schließt die in § 9.1 referierten Messprobleme zumindest für die SEC-Disclosure-Schiene. Beobachtung für Folge-Läufe: Übernehmen weitere Top-50-Konzerne diese Disclosure-Linie in ihren Q2-/Q3-2026-Filings?
- Sanders American AI Sovereign Wealth Fund Act (18. Juni 2026) verlagert die Sanders-Linie strukturell von Verbrauchsteuer- zu Equity-Anknüpfung — die in § 5.4 jetzt definierte Equity-vs.-Revenue-Achse erweitert den Diskussionsraum um eine zweite Anknüpfungslogik. Aussichten auf Verabschiedung im republikanisch geführten Kongress bleiben gering; Beobachtung für Folge-Läufe: Reaktionen aus OpenAI/Anthropic/xAI auf den 50 %-Equity-Vorschlag.
- Anthropic Economic Policy Framework (11. Juni 2026) ist die erste fiskalische Selbstverortung eines zweiten der drei führenden Frontier-Modell-Anbieter (neben OpenAI April 2026); für die Deutschland-These (§ 8.3) zusätzlich relevant ist die explizite Verbindung von Vendor-seitiger Selbstverpflichtung und Sovereign-Wealth-Fund-Modell.
- EU AI Act Digital Omnibus: Förmliche Ratsannahme zum 29. Juni 2026 zum Recherchezeitpunkt noch nicht erfolgt (im Konjunktiv referiert); bei Vollzug am 29. Juni 2026 im nächsten Lauf gegebenenfalls Bestätigung nachtragen.
- Cluster G (Gesundheitswesen) fünftes Mal in Folge ohne valide Treffer im 7-Tage-Fenster; Empfehlung für die nächsten Läufe weiterhin bestehend (gezielter Abruf von g-ba.de Sitzungsergebnissen, gematik-Pressemitteilungen, BfArM-Listings).
- Cluster I (Frontier-Modelle) und Cluster J (Robotik) im 48-Stunden-Fenster weiterhin ohne politisch-fiskalisch relevante Tagesmeldungen über die in Cluster F bereits adressierten Capex-/Personal-Linien hinaus.
- BAG-Mitbestimmung-bei-KI-Urteil 2026 (Sekundärberichterstattung Skill-Sprinters u. a.) konnte ohne Primärentscheidungs-Datum im 7-Tage-Fenster nicht trennscharf eingeordnet werden; für einen späteren Lauf zu prüfen, sobald die Primärentscheidung mit Datum vorliegt.
- Branch dieses Laufs: `claude/determined-einstein-7mvvgh` (in Phase 0 verifiziert; lokal vorhanden, im Remote nach Push neu angelegt).
- Phase 5b: Routine-Anweisung mit `email_to=…` und `whatsapp_to=…` aus dem Aufruf übernommen; Empfängerdaten weder in diesem Logbuch noch in Commits, Abschlussbericht oder einer anderen versionierten Datei ausgeschrieben. Der Versand-Tool-Status (`mail_send` / `send_mail` / `send_message` / `outlook_send` aus `graph-mcp`; `wa_send_message` / `send_message` aus dem `whatsapp`-MCP) wird in Phase 5b geprüft; bei fehlender Tool-Verfügbarkeit werden die vorbereiteten Inhalte gemäß Phase-5b-Spezifikation als Fallback in die gitignored Dateien `daily-mail.txt` und `daily-whatsapp.txt` im Repo-Root geschrieben.

---

## 2026-05-08 — Lauf 001 — Version 21.0 → Version 22.0

### Recherchekorridor

- Genutzte Cluster aus `Suchthemen.md`: A, B, C, D, E, F, G, H, I, J (alle zehn Cluster gestreift; Cluster G — Gesundheitssektor — viertes Mal in Folge ohne neue belegbare Treffer im 7-Tage-Fenster; Cluster I/J im 48-Stunden-Fenster ohne politisch-fiskalisch relevante Tagesmeldungen; Cluster F mit drei aufgenommenen Treffern).
- Zeitfenster: 7 Tage (Cluster F: 48 Stunden für Cloudflare; Cluster I: 48 Stunden); Challenger *April-2026-Job-Cuts-Report* im erweiterten 7-Tage-Fenster (Veröffentlichung 1. Mai 2026), nachdem er in Lauf 003 vom 7. Mai 2026 als „nächster Lauf zu prüfen" markiert war.
- Anzahl Suchanfragen: 11 (Web-Suche).
- Lauf 001 ist der erste reguläre Daily-Update-Lauf am 8. Mai 2026 nach den drei Tagesaktualisierungen am 7. Mai 2026 (Versionen 19.0, 20.0, 21.0).

### Gefundene Quellen

| # | Cluster | Quelle (Autor/Institution, Titel, Datum) | URL | Bewertung |
|---|---------|-----------------------------------------|-----|-----------|
| 1 | F | CNBC, *Cloudflare stock sinks 18% after earnings as company cuts 1,100 employees due to AI changes*, 7. Mai 2026 | https://www.cnbc.com/2026/05/07/cloudflare-net-q1-2026-stock-earnings-layoffs.html | übernommen |
| 2 | F | Bloomberg, *Cloudflare to Cut 1,100 Jobs as It Shifts to AI-First Operating Model*, 7. Mai 2026 | https://www.bloomberg.com/news/articles/2026-05-07/cloudflare-to-cut-one-fifth-of-workers-in-move-to-ai-first-model | übernommen (Sammelbeleg) |
| 3 | F | AOL, *Read the memo: Cloudflare is laying off 1,100 employees to prepare for ‚the agentic AI era‘*, 7. Mai 2026 | https://www.aol.com/articles/read-memo-cloudflare-laying-off-212614000.html | übernommen (Sammelbeleg, Memo-Volltext) |
| 4 | F | The Register, *Cloudflare to fire 1,100 staff whose jobs just aren't AI enough*, 8. Mai 2026 | https://www.theregister.com/off-prem/2026/05/08/cloudflare-to-fire-1100-staff-whose-jobs-just-arent-ai-enough/5235536 | übernommen (Sammelbeleg) |
| 5 | F | Challenger, Gray & Christmas, *Challenger Report: April Job Cuts Rise 38% from March; YTD Cuts Down 50%*, 1. Mai 2026 | https://www.challengergray.com/blog/challenger-report-april-job-cuts-rise-38-from-march-ytd-cuts-down-50/ | übernommen |
| 6 | F | CBS News, *AI emerges as a top cause of layoffs, accounting for 26% of April's job cuts*, 1./3. Mai 2026 | https://www.cbsnews.com/news/ai-layoffs-job-cuts-challenger-report-april-2026/ | übernommen (Sammelbeleg) |
| 7 | F | Fast Company, *Layoffs are actually on the decline in 2026 — but not in tech*, Anfang Mai 2026 | https://www.fastcompany.com/91538649/layoffs-are-actually-on-the-decline-in-2026-but-not-in-the-tech-industry | übernommen (Sammelbeleg) |
| 8 | F | InformationWeek / TrueUp, *2026 tech company layoffs — Tagesfortschreibung Stand 8. Mai 2026 (127.411 / 283 / 1.003 pro Tag)* | https://www.informationweek.com/it-staffing-careers/2026-tech-company-layoffs \| https://www.trueup.io/layoffs | übernommen |
| 9 | F | The Register, *Arctic Wolf cuts 250 jobs in AI push*, 6. Mai 2026 | https://www.theregister.com/ai-and-ml/2026/05/06/arctic-wolf-cuts-250-jobs-in-ai-push/5231213 | verworfen (unter Schwelle 500+ Stellen für Einzelfall in § 1.1; Aggregat-Linie über TrueUp/Challenger abgedeckt) |
| 10 | B | govtech / Pluribus News / The Day — Connecticut SB 5 Lamont-Unterzeichnung Stichtag 8. Mai 2026 | https://www.govtech.com/artificial-intelligence/connecticut-ai-bill-clears-statehouse-heads-to-governor | verworfen (Unterzeichnung formal noch nicht datierbar dokumentiert; Pressespokesperson „looks forward to signing"; bestehender § 4.5-Block bleibt korrekt — in einem späteren Lauf nachzutragen) |
| 11 | B | Bundesrat 1065. Sitzung 8. Mai 2026 (Tagesordnung 80+ Punkte, 1.000-EUR-Entlastungsprämie, GKV-Beitragssatzstabilisierungsgesetz Erstdurchgang) | https://www.bundesrat.de/DE/plenum/bundesrat-kompakt/26/1065/1065-node.html | verworfen (Sitzung läuft am Tag der Recherche; verbindliche Beschlüsse zum Recherchezeitpunkt nicht öffentlich; bestehender Aktualitätshinweis und § 5.2/§ 7-Verweis bleiben korrekt — nächster Lauf) |
| 12 | A | Brookings / Goldman Sachs / Dallas Fed / IMF / HBR — KI-Arbeitsmarkt-Rezeptionsbeiträge (Anfang–Mitte 2026) | https://www.brookings.edu/articles/future-tax-policy-a-public-finance-framework-for-the-age-of-ai/ \| https://www.goldmansachs.com/insights/articles/how-will-ai-affect-the-us-labor-market | verworfen (alle außerhalb 7-Tage-Fenster; bestehende § 3.x- und § 4.x-Einbindung gilt) |
| 13 | C/D | CT-Mirror / Pluribus News / Hartford Business — SB 5 / Bill 515 Sekundär­berichterstattung Mai 2026 | https://ctmirror.org/2026/05/01/artificial-intelligence-house-regulation-passage-ct/ | Dublette (in Version 18.0 / 19.0 / 20.0 referenziert) |
| 14 | I | Anthropic Economic Index (Stand) — kein neuer Bericht 7.–8. Mai 2026 | https://www.anthropic.com/economic-index | verworfen (keine Bewegung im 48-Stunden-Fenster) |

### Eingearbeitete Änderungen

| # | Stelle (§) | Art | Inhalt in einem Satz | Quelle # |
|---|-----------|-----|----------------------|----------|
| 1 | § 1.1 | Ergänzung | Neue Cloudflare-Layoff-Welle vom 7. Mai 2026 (rund 1.100 Stellen / 20 %, „agentic AI-first operating model", Memo Prince/Zatlyn „Building for the future", AI-Einsatz +600 % im Quartal, Restrukturierungsaufwand 140–150 Mio. USD im Q2, Severance bis Ende 2026 / 15. August 2026 / Krankenversicherung Jahresende, Aktienkurs −18 %) im Anschluss an den Cognizant-Block aufgenommen. | 1–4 |
| 2 | § 1.1 | Ergänzung | Aggregat-Bestätigung der KI-Verdrängungslinie über den Challenger *April-2026-Report* (KI 21.490 / 26 % April, zweitens in Folge führender Einzelgrund; Tech 33.361 April / 85.411 YTD / +33 % YoY; KI YTD 49.135 / 16 % aller 2026-Pläne, von 13 % zum März-Stand; Gesamt-Streichungen 2026 −50 % gegenüber Vorjahresvergleich) — explizit verzahnt mit der *Washington-Post*-Differenzierung vom 1. Mai 2026. | 5–7 |
| 3 | § 1.1 | Aktualisierung | TrueUp-Tagesfortschreibung Stand 8. Mai 2026 (127.411 Personen aus 283 Layoff-Meldungen, rund 1.003 Stellen pro Tag — erstmals über 1.000/Tag) als Folgemarker zur Reihe 25. April → 2. Mai → 6. Mai → 7. Mai → 8. Mai 2026 in den bestehenden Tracker-Block eingegliedert. | 8 |
| 4 | § 11.5 | Ergänzung | Vier neue Sammelbelege in Kapitel 11.5: *CNBC / Bloomberg / AOL / The Register* (Cloudflare 7./8. Mai 2026); *Challenger / CBS News / Fast Company* (April-Report 1./3. Mai 2026); *TrueUp / InformationWeek* (Stand 8. Mai 2026); bestehende Tracker- und Layoff-Einträge unverändert. | 1–8 |
| 5 | Aktualitätshinweis am Dokumentende | Aktualisierung | Schnittangabe auf „Lauf 001 vom 8. Mai 2026" geändert; Cloudflare-Layoff (1.100 / 20 %, agentic AI-first, +600 %, −18 %), Challenger-Aggregat (21.490 KI / 26 % April, YTD 49.135 / 16 %, Tech 85.411 / +33 %, Gesamt −50 % YoY) und TrueUp-Tagesstand 8. Mai 2026 (127.411 / 283 / 1.003 pro Tag) in den Auflistungstext aufgenommen. | 1–8 |
| 6 | README.md | Aktualisierung | Versionssprung 21.0 → 22.0 (Versionszeile, Zitiervorschlag, neuer Versions-Eintrag in der KI-Offenlegung mit den drei Cluster-F-Bündeln Cloudflare / Challenger / TrueUp). | — |
| 7 | Validierung-Ergebnisse.md | Ergänzung | Neuer Validierungsblock „Validierung 8. Mai 2026 (Lauf 001 vom 8. Mai 2026) — Version 21.0 → Version 22.0" mit Prüftabelle 2.1.1 – 2.6 und Abschluss „alle Fehler behoben: Ja". | — |

### Verworfene Treffer (mit Begründung)

| # | Quelle | Cluster | Begründung |
|---|--------|---------|------------|
| 1 | The Register — Arctic Wolf 250 Stellen (6. Mai 2026) | F | Unter Schwelle 500+ Stellen für Einzel-Layoff-Eintrag in § 1.1; Aggregat-Linie über TrueUp/Challenger abgedeckt. |
| 2 | Connecticut SB 5 — Lamont-Unterzeichnung | B | Stichtag 8. Mai 2026 noch nicht formal mit Datum dokumentiert; bestehender § 4.5-Block bleibt korrekt; nächster Lauf zu prüfen. |
| 3 | Bundesrat 1065. Sitzung 8. Mai 2026 (GKV-Erstdurchgang) | B/E | Sitzung läuft am Tag der Recherche; verbindliche Beschlüsse zum Recherchezeitpunkt nicht öffentlich verfügbar; nächster Lauf zu prüfen. |
| 4 | AI-Act-Trilog 13. Mai 2026 (3. Runde) | B | Nach Stichtag 8. Mai 2026. |
| 5 | Plattform-Digitalabgabe (Weimer) Mai 2026 | B | Keine Bewegung über Version 10.0/11.0 hinaus zwischen 7. und 8. Mai 2026. |
| 6 | Anthropic Economic Index — neuer Bericht | I | Keine Bewegung im 48-Stunden-Fenster; bestehender § 3.5-Block bleibt aktuell. |
| 7 | New York WARN Act AI-Disclosure-Vorschlag (Hochul) | B | Vorschlag, kein verabschiedeter Akt; ohne Datumsfixierung im 7-Tage-Fenster nicht trennscharf einordbar. |
| 8 | Generationenkapital — Stand Mai 2026 | E/H | Keine neuen Tranchen-/Renditeangaben zwischen 7. und 8. Mai 2026; bestehender § 8.6-Verweis bleibt aktuell. |
| 9 | Brookings / Goldman Sachs / Dallas Fed / IMF / HBR — KI-Arbeitsmarkt-Rezeptionsbeiträge | A | Alle außerhalb 7-Tage-Fenster; bestehende Einbindung gilt. |
| 10 | Challenger *März-2026-Report* | F | Außerhalb 7-Tage-Fenster und in Lauf 003 vom 7. Mai 2026 bereits geprüft; April-Report ersetzt die März-Aggregate. |
| 11 | China 15. Fünfjahresplan 2026–2030 / MIIT-Standardisierungs­komitee (März 2026) | C/H | Außerhalb 7-Tage-Fenster (in Lauf 003 vom 7. Mai 2026 bereits dokumentiert). |
| 12 | Tesla Optimus / Figure / Boston Dynamics Atlas / Unitree (Cluster J) | J | Keine Tagesmeldung mit politisch-fiskalischer Implikation im 48-Stunden-Fenster. |
| 13 | G-BA / gematik / BfArM / DiGAV (Cluster G) | G | Viertes Mal in Folge ohne KI-spezifische neue Beschlüsse oder DiGA-Listings im 7-Tage-Fenster. |
| 14 | Frontier-Modelle / Inferenzpreise (Cluster I) | I | Keine Tagesmeldung mit politisch-fiskalischer Implikation im 48-Stunden-Fenster. |

### Verarbeitungsschritte

- Recherche abgeschlossen: Ja
- Deduplikation gegen Hauptdokument: Ja
- Validierung gemäß `Validierung.md` ausgeführt: Ja (Block „Validierung 8. Mai 2026 (Lauf 001 vom 8. Mai 2026) — Version 21.0 → Version 22.0" in `Validierung-Ergebnisse.md`)
- PDF erstellt (`build_pdf.py`): Ja
- Word erstellt (`build_docx.py`): Ja
- Versionsnummer in Hauptdokument, README, Validierung-Ergebnisse aktualisiert: Ja
- Branch auf main gemerged und gelöscht: erfolgt am Ende dieses Laufs
- E-Mail-Versand (Phase 5b): siehe „Auffälligkeiten / offene Punkte"
- WhatsApp-Versand (Phase 5b): siehe „Auffälligkeiten / offene Punkte"

### Auffälligkeiten / offene Punkte

- Lauf 001 ist der erste reguläre Daily-Update-Lauf am 8. Mai 2026; nach den drei Tagesaktualisierungen am 7. Mai 2026 (Versionen 19.0, 20.0, 21.0) liegt eine relativ hohe Trefferdichte im 48-Stunden-Fenster vor — primär durch die Cloudflare-Welle und den Challenger-April-Report, der genau zu diesem Lauf publiziert ist (in Lauf 003 vom 7. Mai 2026 als „nächster Lauf zu prüfen" markiert).
- Cloudflare ist der erste *Cloud-Infrastrukturanbieter*, der eine konzernweite Restrukturierung explizit am Übergang zu einem „agentic"-Operating-Modell festmacht (im Unterschied zu SaaS/Fintech/IT-Services in der Vorwoche); für die Steuerdebatte ist das relevant, weil hier die Anbieterseite der KI-Wertschöpfung selbst Personal reduziert — eine Konstellation, die in § 8.2 (KI als Rohstoff) und § 8.3 (Teilhabe) zusätzlich zu beobachten ist.
- Connecticut SB 5: Lamont-Unterzeichnung steht zum Stichtag 8. Mai 2026 noch aus (Pressespokesperson „looks forward to signing"); bei formaler Unterzeichnung im Mai 2026 im nächsten Lauf nachzutragen.
- Bundesrat 1065. Sitzung am 8. Mai 2026: Tagesordnung mit über 80 Punkten, darunter erster Durchgang zum GKV-Beitragssatzstabilisierungsgesetz; verbindliche Beschlusstexte werden im Nachgang dokumentiert und sind im nächsten Lauf einzuarbeiten.
- Cluster G (Gesundheitswesen) viertes Mal in Folge ohne valide Treffer im 7-Tage-Fenster; Empfehlung für die nächsten Läufe weiterhin bestehend (gezielter Abruf von g-ba.de Sitzungsergebnissen, gematik-Pressemitteilungen, BfArM-Listings).
- Cluster I (Frontier-Modelle) und Cluster J (Robotik) im 48-Stunden-Fenster ohne politisch-fiskalisch relevante Tagesmeldungen; Beobachtung beim nächsten Lauf fortsetzen.
- Branch dieses Laufs: `claude/determined-einstein-RW5Fj` (in Phase 0 verifiziert; lokal vorhanden, im Remote nach Push neu angelegt).
- Phase 5b: Routine-Anweisung mit `email_to=…` und `whatsapp_to=…` aus dem Aufruf übernommen; Empfängerdaten weder in diesem Logbuch noch in Commits, Abschlussbericht oder einer anderen versionierten Datei ausgeschrieben. Der Versand-Tool-Status (`mail_send` / `send_mail` / `send_message` / `outlook_send` aus `graph-mcp`; `wa_send_message` / `send_message` aus dem `whatsapp`-MCP) wird in Phase 5b geprüft; bei fehlender Tool-Verfügbarkeit werden die vorbereiteten Inhalte gemäß Phase-5b-Spezifikation als Fallback in die gitignored Dateien `daily-mail.txt` und `daily-whatsapp.txt` im Repo-Root geschrieben (Dateien stehen in `.gitignore`, werden also nicht versioniert).

---

## 2026-05-07 — Lauf 003 — Version 20.0 → Version 21.0

### Recherchekorridor

- Genutzte Cluster aus `Suchthemen.md`: A, B, C, D, E, F, G, H, I, J (alle zehn Cluster gestreift; Cluster F mit Treffer-Verfeinerung; Cluster G — Gesundheitssektor — sowie I/J ohne neue belegbare Treffer im 7-Tage- bzw. 48-Stunden-Fenster).
- Zeitfenster: 7 Tage (Cluster F: 48 Stunden auf strenger Auslegung; eine Verfeinerung im erweiterten 7-Tage-Fenster aufgenommen, da die Aggregat-Größe erst durch Zusammenführung der Q1-2026-Earnings-Calls vom 28.–30. April 2026 entstanden ist und sich erst Anfang Mai 2026 in der Sekundärberichterstattung verfestigt hat); Cluster I: 48 Stunden.
- Anzahl Suchanfragen: 13 (Web-Suche), 2 (WebFetch — beide 403, daher Sekundärquellen-Stichproben).
- Lauf 003 ist die dritte Tagesaktualisierung am 7. Mai 2026 nach Lauf 001 (vormittags/früher Nachmittag) und Lauf 002 (Abend).

### Gefundene Quellen

| # | Cluster | Quelle (Autor/Institution, Titel, Datum) | URL | Bewertung |
|---|---------|-----------------------------------------|-----|-----------|
| 1 | F | Tom's Hardware, *Google, Microsoft, Meta, and Amazon capex spending to hit $725 billion in 2026, up 77% from last year — analyst says bear thesis is „garbage"*, Anfang Mai 2026 | https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion | übernommen |
| 2 | F | Tom's Hardware, *Skyrocketing component prices push Big Tech capex to record $725 billion — Microsoft alone attributes $25 billion of AI budget to increased memory and chip costs*, Anfang Mai 2026 | https://www.tomshardware.com/tech-industry/big-tech/microsoft-attributed-25-billion-of-its-record-ai-budget-to-memory-chip-costs | übernommen (Sammelbeleg) |
| 3 | F | Statista, *Chart: Big Tech's AI Spending to Reach $725 Billion in 2026*, Mai 2026 | https://www.statista.com/chart/35046/capital-expenditure-of-meta-alphabet-amazon-and-microsoft/ | übernommen (Sammelbeleg) |
| 4 | F | Invezz, *Is Big Tech's $725B AI splurge being funded by mass layoffs?*, 4. Mai 2026 | https://invezz.com/news/2026/05/04/is-big-techs-725b-ai-splurge-being-funded-by-mass-layoffs/ | übernommen (Sammelbeleg) |
| 5 | A | Federal Reserve Bank of Atlanta WP 2026-04, *Artificial Intelligence, Productivity, and the Workforce: Evidence from Corporate Executives*, 25. März 2026 | https://www.atlantafed.org/research-and-data/publications/working-papers/2026/03/25/04-artificial-intelligence-productivity-and-the-workforce-evidence-from-corporate-executives | verworfen (außerhalb 7-Tage-Fenster) |
| 6 | F | Challenger, Gray & Christmas — März-2026-Job-Cuts-Report (3. April 2026; AI 25 % des März-Volumens, AI YTD-Rang 5 mit 13 %) | https://www.challengergray.com/blog/challenger-report-march-cuts-rise-25-from-february-ai-leads-reasons/ | verworfen (außerhalb 7-Tage-Fenster) |
| 7 | F | Challenger, Gray & Christmas — April-2026-Job-Cuts-Report (Veröffentlichung laut Verlagskalender 7. Mai 2026 7:30 EDT) | https://www.challengergray.com/blog/category/job-cuts-report/ | verworfen (zum Recherchezeitpunkt noch nicht öffentlich indexiert) |
| 8 | F | The Hill / NewsNation, *AI is tied to tech layoffs, but spending — not job replacement — may be the key driver* | https://thehill.com/policy/technology/5852018-tech-layoffs-surge-ai-push/ \| https://www.newsnationnow.com/business/your-money/tech-layoffs-surge-ai-spending/ | verworfen (Datum nicht eindeutig verifizierbar; Aussage durch Washington Post 1. Mai 2026 und 725-Mrd.-USD-Aggregat in § 1.1 bereits redundant abgebildet) |
| 9 | F | Cognizant Q1-2026-Earnings-Release (29. April 2026), *Cognizant Reports First Quarter 2026 Results / Project Leap targets $200–300 mn in-year savings* | https://news.cognizant.com/2026-04-29-Cognizant-Reports-First-Quarter-2026-Results | Dublette (Project-Leap-Rahmen bereits in Version 19.0 / § 1.1) |
| 10 | B | Connecticut SB 5 — Lamont-Unterzeichnung (Stichtag 7. Mai 2026, noch nicht erfolgt) | https://www.govtech.com/artificial-intelligence/connecticut-ai-bill-clears-statehouse-heads-to-governor | verworfen (formale Unterzeichnung nicht dokumentiert; bestehender § 4.5-Block bleibt korrekt) |
| 11 | A | Stanford HAI *AI Index Report 2026* (13. April 2026; Software-Developer 22–25 J. −20 % seit 2024) | https://hai.stanford.edu/ai-index/2026-ai-index-report | verworfen (außerhalb 7-Tage-Fenster) |
| 12 | C/H | China — 15. Fünfjahresplan 2026–2030 / MIIT Humanoid-Robotics-Standardisierungs­komitee (März 2026) | https://thediplomat.com/2026/03/chinas-new-five-year-plan-prioritizes-robotics/ \| https://merics.org/en/report/embodied-ai-chinas-ambitious-path-transform-its-robotics-industry | verworfen (außerhalb 7-Tage-Fenster) |
| 13 | I | DeepSeek V4 / OpenAI GPT-5.5 / Anthropic Opus 4.7 (24. April 2026) | https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/ | verworfen (außerhalb 48-Stunden-Fenster; ohne unmittelbare politisch-fiskalische Implikation) |
| 14 | J | Tesla Optimus / Figure / Boston Dynamics Atlas / Unitree Mai 2026 — IFR-Stand 2025/2026 | https://ifr.org/worldrobotics \| https://botinfo.ai/articles/tesla-optimus | verworfen (keine Tagesmeldung mit politisch-fiskalischer Implikation im 48-Stunden-Fenster) |
| 15 | G | G-BA / gematik / BfArM Mai 2026 (DiGAV 2.0; e-Verordnung DiGA) | https://www.g-ba.de/ \| https://fachportal.gematik.de/zielgruppen/diga-hersteller | verworfen (keine KI-spezifischen Beschlüsse im Fenster) |
| 16 | B | Plattform-Digitalabgabe (Weimer) — Eckpunktepapier Mai 2026 | https://www.it-journal.de/220595-weimer-treibt-plattform-abgabe-voran-eckpunktepapier-geplant.html | verworfen (keine Bewegung im 7-Tage-Fenster über Version 10.0/11.0 hinaus) |

### Eingearbeitete Änderungen

| # | Stelle (§) | Art | Inhalt in einem Satz | Quelle # |
|---|-----------|-----|----------------------|----------|
| 1 | § 1.1 | Aktualisierung | Capex-Satz im Layoff-/Capex-Block ergänzt um die nach den Q1-2026-Earnings-Calls (28.–30. April 2026) und durch *Financial Times* zusammengeführte, von *Tom's Hardware* (5./6. Mai 2026) und *Invezz* (4. Mai 2026) referierte revidierte Aggregat-Schätzung von rund 725 Mrd. USD (+77 % gegenüber 410 Mrd. USD im Jahr 2025; Microsoft 190, Alphabet 190, Amazon 200, Meta 125–145 Mrd. USD; rund 25 Mrd. USD Microsoft-Aufschlag durch DRAM-Verteuerung +95 % q/q im Q1 2026 und +58–63 % Q2-Projektion); alte Konsens-Schätzung 660–700 Mrd. USD bleibt als zeitlich frühere Referenz Anfang April 2026 erhalten (Claude.md § 4.2). | 1–4 |
| 2 | § 11.5 | Ergänzung | Neuer Eintrag *Tom's Hardware / Statista / Invezz* (Anfang Mai 2026) mit vier URLs; bestehender Fortune-/CNBC-/Futurum-Eintrag (April–Mai 2026) bleibt unverändert. | 1–4 |
| 3 | Aktualitätshinweis am Dokumentende | Aktualisierung | Schnittangabe auf „Lauf 003, dritte Tagesaktualisierung" geändert; Capex-Aggregat 725 Mrd. USD mit Konzernsplit und DRAM-Komponentenkostentreiber in den Auflistungstext aufgenommen. | 1–4 |
| 4 | README.md | Aktualisierung | Versionssprung 20.0 → 21.0 (Versionszeile, Zitiervorschlag, neuer Versions-Eintrag in der KI-Offenlegung mit der Capex-Verfeinerung). | — |
| 5 | Validierung-Ergebnisse.md | Ergänzung | Neuer Validierungsblock „Validierung 7. Mai 2026 (Lauf 003 — dritte Tagesaktualisierung) — Version 20.0 → Version 21.0" mit Prüftabelle 2.1.1 – 2.6 und Abschluss „alle Fehler behoben: Ja". | — |

### Verworfene Treffer (mit Begründung)

| # | Quelle | Cluster | Begründung |
|---|--------|---------|------------|
| 1 | Federal Reserve Bank of Atlanta WP 2026-04 (25. März 2026) | A | Außerhalb 7-Tage-Fenster — potenziell für späteren Lauf zu prüfen. |
| 2 | Challenger Report März 2026 (3. April 2026) | F | Außerhalb 7-Tage-Fenster; Größenordnung über Yale Budget Lab und Goldman-Sachs-Schätzung in § 1.1 bereits abgebildet. |
| 3 | Challenger Report April 2026 (Veröffentlichung 7. Mai 2026 7:30 EDT) | F | Zum Recherchezeitpunkt noch nicht öffentlich indexiert; nächster Lauf zu prüfen. |
| 4 | The Hill / NewsNation (AI vs. Job-Replacement-Frame) | F | Datum unklar (Direktabruf 403); Aussage durch Washington Post 1. Mai 2026 und 725-Mrd.-USD-Aggregat redundant abgebildet. |
| 5 | Cognizant Q1-2026-Earnings (29. April 2026) | F | Project-Leap-Rahmen bereits in Version 19.0; präzisere Savings-Aufteilung ohne neuen Befund für Steuerdebatte. |
| 6 | Connecticut SB 5 — Lamont-Unterzeichnung | B | Zum Stichtag 7. Mai 2026 noch nicht erfolgt; bestehender § 4.5-Block bleibt korrekt. |
| 7 | Stanford HAI AI Index 2026 (13. April 2026) | A | Außerhalb 7-Tage-Fenster. |
| 8 | China 15. Fünfjahresplan / MIIT-Standardisierungs­komitee (März 2026) | C/H | Außerhalb 7-Tage-Fenster. |
| 9 | DeepSeek V4 / OpenAI GPT-5.5 / Anthropic Opus 4.7 (24. April 2026) | I | Außerhalb 48-Stunden-Fenster; ohne unmittelbare politisch-fiskalische Implikation. |
| 10 | Tesla Optimus / Figure / Boston Dynamics Atlas / Unitree | J | Keine Tagesmeldung mit politisch-fiskalischer Implikation im 48-Stunden-Fenster. |
| 11 | G-BA / gematik / BfArM Mai 2026 | G | Keine KI-spezifischen Beschlüsse im 7-Tage-Fenster. |
| 12 | Plattform-Digitalabgabe (Weimer) Mai 2026 | B | Keine Bewegung über Version 10.0/11.0 hinaus; Eckpunktepapier weiterhin angekündigt, aber nicht vorgelegt. |
| 13 | Bundesrat 1065. Sitzung 8. Mai 2026 / AI-Act-Trilog 13. Mai 2026 | B/E | Liegen nach dem Stichtag 7. Mai 2026. |

### Verarbeitungsschritte

- Recherche abgeschlossen: Ja
- Deduplikation gegen Hauptdokument: Ja
- Validierung gemäß `Validierung.md` ausgeführt: Ja (Block „Validierung 7. Mai 2026 (Lauf 003 — dritte Tagesaktualisierung) — Version 20.0 → Version 21.0" in `Validierung-Ergebnisse.md`)
- PDF erstellt (`build_pdf.py`): Ja
- Word erstellt (`build_docx.py`): Ja
- Versionsnummer in Hauptdokument, README, Validierung-Ergebnisse aktualisiert: Ja
- Branch auf main gemerged und gelöscht: erfolgt am Ende dieses Laufs
- E-Mail-Versand (Phase 5b): Fallback-Datei `daily-mail.txt` geschrieben (kein `mail_send`/`send_mail`/`send_message`/`outlook_send`-Tool in der laufenden Session erreichbar)
- WhatsApp-Versand (Phase 5b): Fallback-Datei `daily-whatsapp.txt` geschrieben (kein `wa_send_message`/`send_message`-Tool des `whatsapp`-MCP in der laufenden Session erreichbar)

### Auffälligkeiten / offene Punkte

- Lauf 003 ist die dritte Tagesaktualisierung am 7. Mai 2026; die Trefferdichte im 7-Tage-Fenster ist nach Lauf 001 und Lauf 002 erwartungsgemäß weiter gesunken — nur eine quantitative Verfeinerung (Capex-Aggregat 725 Mrd. USD) wurde aufgenommen.
- Cluster F (Tech-Layoffs / KI-Capex) hat eine 48-Stunden-Vorgabe gemäß `Suchthemen.md`; die aufgenommene Capex-Verfeinerung wurde im erweiterten 7-Tage-Fenster gefasst, weil die Aggregat-Größe erst durch Zusammenführung der Q1-2026-Earnings-Calls (28.–30. April 2026) entstanden ist und sich erst Anfang Mai 2026 in mehreren unabhängigen Sekundärquellen verfestigt hat — Vorgehen analog zu Lauf 002 (Bloomberg-Editorial vom 29. April 2026).
- Challenger *April-2026-Job-Cuts-Report* (Veröffentlichung 7. Mai 2026 7:30 Uhr EDT) zum Recherchezeitpunkt noch nicht öffentlich indexiert; für den nächsten Lauf gezielt zu prüfen.
- Cluster G (Gesundheitswesen) erneut ohne valide Treffer im 7-Tage-Fenster (drittes Mal in Folge); Empfehlung für die nächsten Läufe weiterhin bestehend (gezielter Abruf von g-ba.de Sitzungsergebnissen, gematik-Pressemitteilungen, BfArM-Listings).
- Cluster I (Frontier-Modelle) und Cluster J (Robotik) im 48-Stunden-Fenster ohne politisch-fiskalisch relevante Tagesmeldungen; Beobachtung beim nächsten Lauf fortsetzen.
- Connecticut SB 5: Lamont-Unterzeichnung steht noch aus; bei Vollzug zwischen 7. und 8. Mai 2026 im nächsten Lauf nachzutragen.
- Branch dieses Laufs: `claude/determined-einstein-O99xw` (in Phase 0 verifiziert; lokal vorhanden, im Remote nach Push neu angelegt). Phase-6-Cleanup: Lokaler Branch nach Merge in `main` gelöscht (`git branch -d` erfolgreich). Remote-Branch-Löschung wurde mit HTTP 403 abgewiesen (vermutlich Branch-Schutz / Hosting-Policy); der Inhalt ist über den Merge-Commit `acf38f0` vollständig in `origin/main` enthalten, der verbleibende Remote-Branch ist ohne offene Änderungen und kann beim nächsten administrativen Zugriff gelöscht werden.
- Phase 5b: Routine-Anweisung mit `email_to=…` und `whatsapp_to=…` aus dem Aufruf übernommen; Empfängerdaten weder in diesem Logbuch noch in Commits, Abschlussbericht oder einer anderen versionierten Datei ausgeschrieben. Es war in der laufenden Session weder ein E-Mail-Versand-Tool (`mail_send` / `send_mail` / `send_message` / `outlook_send` aus `graph-mcp`) noch ein WhatsApp-Versand-Tool (`wa_send_message` / `send_message` aus dem `whatsapp`-MCP) erreichbar; gemäß Phase-5b-Spezifikation wurden die vorbereiteten Inhalte als Fallback in die gitignored Dateien `daily-mail.txt` und `daily-whatsapp.txt` im Repo-Root geschrieben (Dateien stehen in `.gitignore`, werden also nicht versioniert). Der Lauf fährt gemäß Phase-5b-Regel („Versandfehler sind weich") mit Phase 6 fort.

---

## 2026-05-07 — Lauf 002 — Version 19.0 → Version 20.0

### Recherchekorridor

- Genutzte Cluster aus `Suchthemen.md`: A, B, C, D, E, F, G, H, I, J (alle zehn Cluster gestreift; Cluster G — Gesundheitssektor — und Cluster I/J ohne neue belegbare Treffer im 7-Tage- bzw. 48-Stunden-Fenster).
- Zeitfenster: 7 Tage (Cluster F: 48 Stunden; Cluster I: 48 Stunden).
- Anzahl Suchanfragen: 12 (Web-Suche), 2 (WebFetch).
- Lauf 002 ist die zweite Tagesaktualisierung am 7. Mai 2026 nach Lauf 001 vom Vormittag/frühen Nachmittag desselben Tages.

### Gefundene Quellen

| # | Cluster | Quelle (Autor/Institution, Titel, Datum) | URL | Bewertung |
|---|---------|-----------------------------------------|-----|-----------|
| 1 | D | Bloomberg Editorial Board, *Taxing Artificial Intelligence Would Hurt Innovation and Prosperity*, 29. April 2026 | https://www.bloomberg.com/opinion/articles/2026-04-29/taxing-artificial-intelligence-would-hurt-innovation-and-prosperity | übernommen |
| 2 | D | Advisor Perspectives (syndizierte Bloomberg-Fassung), *Taxing Artificial Intelligence Would Be a Big Mistake*, 2. Mai 2026 | https://www.advisorperspectives.com/articles/2026/05/02/taxing-artificial-intelligence-big-mistake | übernommen (Sammelbeleg) |
| 3 | D | RealClearPolitics (syndizierte Bloomberg-Fassung), *Taxing Artificial Intelligence Would Be a Big Mistake*, 4. Mai 2026 | https://www.realclearpolitics.com/2026/05/04/taxing_artificial_intelligence_would_be_a_big_mistake_698781.html | übernommen (Sammelbeleg) |
| 4 | D | West Hawaii Today (syndizierte Bloomberg-Fassung), *Taxing artificial intelligence would be a big mistake*, 5. Mai 2026 | https://www.westhawaiitoday.com/2026/05/05/opinion/taxing-artificial-intelligence-would-be-a-big-mistake/ | übernommen (Sammelbeleg) |
| 5 | D | Las Vegas Sun (syndizierte Bloomberg-Fassung), *Taxing artificial intelligence would be a big mistake*, 6. Mai 2026 | https://lasvegassun.com/news/2026/may/06/taxing-artificial-intelligence-would-be-a-big-mist/ | übernommen (Sammelbeleg) |
| 6 | D | News.bloombergtax.com — *Taxing Artificial Intelligence Would Be a Big Mistake: Editorial* | https://news.bloombergtax.com/tax-insights-and-commentary/taxing-artificial-intelligence-would-be-a-big-mistake-editorial | übernommen (Sammelbeleg, Bloomberg-Tax-Wiedergabe) |
| 7 | A | NBER WP 34705 — Manning & Aguirre, *How Adaptable Are American Workers to AI-Induced Job Displacement?*, Januar 2026 | https://www.nber.org/papers/w34705 | verworfen (außerhalb 7-Tage-Fenster) |
| 8 | A | Stanford HAI — *AI Index Report 2026*, 13. April 2026 | https://hai.stanford.edu/ai-index/2026-ai-index-report | verworfen (außerhalb 7-Tage-Fenster) |
| 9 | A | IMF — *Global Economic and Financial Implications of Artificial Intelligence*, April 2026 | https://www.imf.org/en/publications/imf-notes/issues/2026/04/03/global-economic-and-financial-implications-of-artificial-intelligence-lessons-from-a-574924 | verworfen (außerhalb 7-Tage-Fenster) |
| 10 | A | IMF Working Paper — *AI Meets Fiscal Policy: Mapping Government Spending Actions Across 64 Countries*, 7. März 2026 | https://www.imf.org/en/publications/wp/issues/2026/03/07/ai-meets-fiscal-policy-mapping-government-spending-actions-across-64-countries-574286 | verworfen (außerhalb 7-Tage-Fenster) |
| 11 | A | WEF — *Future of Jobs Report 2026*, 7. Januar 2026 | https://www.weforum.org/publications/series/future-of-jobs/ | verworfen (außerhalb 7-Tage-Fenster) |
| 12 | C | ITIF — *Industries Impacted by a Quasi-Robot Tax in South Korea Reduced Industrial Robot Installations by 28 Percent*, 9. Februar 2026 | https://itif.org/publications/2026/02/09/industries-impacted-by-quasi-robot-tax-south-korea-reduced-industrial-robot-installations/ | verworfen (außerhalb 7-Tage-Fenster) |
| 13 | C | Kang/Lee/Quach (SSRN 5005128), *The Welfare Effects of a Robot Tax — Evidence from a Tax Credit for Automation Technologies in Korea* | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5005128 | verworfen (Datum unklar / vermutlich außerhalb Fenster) |
| 14 | B | Bundestag KI-MIG-Gesetzentwurf (Plenardebatte 1. Lesung 20. März 2026) | https://bmds.bund.de/aktuelles/reden/detail/plenardebatte-im-bundestag-zur-1-lesung-durchfuehrung-der-eu-verordnung-ueber-ki | verworfen (außerhalb 7-Tage-Fenster) |
| 15 | B | resultsense.com / Charles Radclyffe „minimum wage for robots", 5. Mai 2026 | https://www.resultsense.com/news/2026-05-05-welsh-founder-minimum-wage-robots-tax/ | verworfen (Quellenniveau / Negativliste) |
| 16 | B | Connecticut SB 5 (Hausabstimmung 1. Mai 2026, 131 zu 17) | https://ctmirror.org/2026/05/01/artificial-intelligence-house-regulation-passage-ct/ | Dublette (bereits in Version 18.0 / 19.0) |
| 17 | D | Sanders-Robotersteuer-Folgeinitiative (Fox Business, Washington Examiner) | https://www.washingtonexaminer.com/policy/finance-and-economy/3844942/sanders-plans-robot-tax-legislation/ | Dublette (bereits Version 5.0 / 8.0) |
| 18 | F | Big Tech Layoffs Mai 2026 (Salesforce, IBM, Intel — generische Tracker-Zusammenfassungen) | https://www.informationweek.com/it-staffing-careers/2026-tech-company-layoffs | Dublette (Lauf 001 Tagesfortschreibung TrueUp 121.111 / 273 unverändert) |
| 19 | E | Bundesbank-/SVR-Studien Mai 2026 zu KI und Arbeitsmarkt | https://www.sachverstaendigenrat-wirtschaft.de/fileadmin/dateiablage/gutachten/jg202526/JG202526_Gesamtausgabe_Barrierefrei.pdf | verworfen (Stand SVR-Jahresgutachten 2025/2026 — außerhalb Fenster) |
| 20 | G | DiGAV-2.0-Inkrafttreten 1. Februar 2026 / G-BA-Mai-Sitzungen 2026 | https://www.g-ba.de/ | verworfen (außerhalb Fenster bzw. ohne KI-spezifische Beschlüsse im Fenster) |
| 21 | G | IRS *AI as key to accelerate workforce training* (4./5. Mai 2026) | https://federalnewsnetwork.com/artificial-intelligence/2026/05/irs-sees-ai-as-key-to-accelerate-workforce-training/ | verworfen (außerhalb Korridor — Verwaltungsinterne Effizienz) |
| 22 | I/J | Stanford HAI AI Index 2026 / IFR World Robotics 2025–2026 / Tesla Optimus, Figure, 1X Stückzahlen Mai 2026 | https://hai.stanford.edu/ai-index/2026-ai-index-report \| https://ifr.org/worldrobotics | verworfen (außerhalb Fenster bzw. Tagesneuigkeit ohne politisch-fiskalische Implikation) |

### Eingearbeitete Änderungen

| # | Stelle (§) | Art | Inhalt in einem Satz | Quelle # |
|---|-----------|-----|----------------------|----------|
| 1 | § 4.5 | Ergänzung | Neuer Absatz „Bloomberg-Editorial (29. April 2026)" zwischen OpenAI-Block und Andrew-Yang-Block: mainstream-finanzpublizistische Gegenstimme zur Sanders/OpenAI-Linie mit Hauptargumenten Innovations-/Produktivitätsbremse, Wettbewerbsnachteil, Unmöglichkeit der Abgrenzung Verdrängung/Augmentation und Prognoseunsicherheit; alternative Empfehlungen (Lockerung berufsrechtlicher Lizenzschranken, Reform der Arbeitslosenversicherung, Umschulungs-Steueranreize, EITC-Ausweitung) im Konjunktiv referiert. | 1–6 |
| 2 | § 11.5 | Ergänzung | Neuer Eintrag *Bloomberg Editorial Board (29. April 2026)* mit vier syndizierten Folge-URLs (Advisor Perspectives 2. Mai 2026, RealClearPolitics 4. Mai 2026, West Hawaii Today 5. Mai 2026, Las Vegas Sun 6. Mai 2026). | 1–5 |
| 3 | Aktualitätshinweis am Dokumentende | Aktualisierung | Schnittangabe auf „Lauf 002, abendliche Tagesaktualisierung" geändert; Bloomberg-Editorial mit Hauptargumenten und Alternativen in den Auflistungstext aufgenommen. | 1–6 |
| 4 | README.md | Aktualisierung | Versionssprung 19.0 → 20.0 (Versionszeile, Zitiervorschlag, neuer Versionseintrag in der KI-Offenlegung mit der Bloomberg-Editorial-Ergänzung). | — |
| 5 | Validierung-Ergebnisse.md | Ergänzung | Neuer Validierungsblock „Validierung 7. Mai 2026 (Lauf 002 — Tagesfolge) — Version 19.0 → Version 20.0" mit Prüftabelle 2.1.1 – 2.6 und Abschluss „alle Fehler behoben: Ja". | — |

### Verworfene Treffer (mit Begründung)

| # | Quelle | Cluster | Begründung |
|---|--------|---------|------------|
| 1 | NBER WP 34705 Manning & Aguirre (Januar 2026) | A | Außerhalb 7-Tage-Fenster — potenziell für späteren Lauf zu prüfen. |
| 2 | Stanford HAI AI Index 2026 (13. April 2026) | A | Außerhalb 7-Tage-Fenster. |
| 3 | IMF *Global Economic and Financial Implications of AI* (April 2026) | A | Außerhalb 7-Tage-Fenster. |
| 4 | IMF *AI Meets Fiscal Policy* (März 2026) | A | Außerhalb 7-Tage-Fenster. |
| 5 | WEF Future of Jobs Report 2026 (Januar 2026) | A | Außerhalb 7-Tage-Fenster. |
| 6 | ITIF Korea-Quasi-Robotersteuer (Februar 2026) | C | Außerhalb 7-Tage-Fenster. |
| 7 | Kang/Lee/Quach SSRN 5005128 | C | Datum unklar / vermutlich außerhalb Fenster — gegebenenfalls in einem späteren Lauf zu prüfen. |
| 8 | Bundestag KI-MIG-Plenardebatte 20. März 2026 | B | Außerhalb 7-Tage-Fenster. |
| 9 | resultsense.com / Welsh founder „minimum wage for robots" (5. Mai 2026) | B | Quellenniveau zweifelhaft, kleines privates Unternehmen ohne politische Konsequenz; fällt unter Negativliste. |
| 10 | Connecticut SB 5 / Lamont-Unterzeichnung | B | Dublette zu Version 18.0 / 19.0; § 4.5 und Aktualitätshinweis bereits aktuell. |
| 11 | Sanders-Robotersteuer-Folgeinitiative | D | Dublette zu Version 5.0 / 8.0; keine Bewegungen zwischen Lauf 001 und Lauf 002. |
| 12 | Tech-Layoffs Salesforce / IBM / Intel Mai 2026 | F | Dublette / keine neue Welle zwischen 6./7. Mai 2026 außerhalb der bereits in § 1.1 dokumentierten Coinbase/PayPal/Freshworks/Cognizant-Linie. |
| 13 | DiGAV 2.0 (1. Februar 2026) | G | Außerhalb 7-Tage-Fenster. |
| 14 | G-BA / gematik Mai 2026 | G | Keine KI-spezifischen Beschlüsse im Fenster. |
| 15 | IRS-AI-Workforce-Training-Initiative (4./5. Mai 2026) | G/B | Außerhalb Korridor (interne Verwaltungseffizienz, ohne Steuer-/Sozialversicherungsbezug). |
| 16 | Bundesbank-/SVR-Materialien Mai 2026 | E | Aktuelle Berichte ohne neuen Sachstand zu KI-Arbeitsmarktwirkung im 7-Tage-Fenster. |
| 17 | AI-Act-Trilog 13. Mai 2026 | B | Trilog hat zum Stichtag 7. Mai 2026 noch nicht stattgefunden. |
| 18 | Bundesrat 1065. Sitzung 8. Mai 2026 | B/E | Sitzung liegt nach dem Stichtag 7. Mai 2026. |
| 19 | IFR World Robotics Report 2025/2026 | J | Standardpublikation ohne Tagesneuigkeit; keine Aktualisierung im 48-Stunden-Fenster. |
| 20 | Tesla Optimus / Figure / 1X Stückzahlen Mai 2026 | J | Keine Tagesmeldung mit politisch-fiskalischer Implikation im 48-Stunden-Fenster. |
| 21 | Frontier-Modell-Releases / Inferenzpreise (Cluster I) | I | Keine Tagesmeldung mit politisch-fiskalischer Implikation im 48-Stunden-Fenster. |

### Verarbeitungsschritte

- Recherche abgeschlossen: Ja
- Deduplikation gegen Hauptdokument: Ja
- Validierung gemäß `Validierung.md` ausgeführt: Ja (Block „Validierung 7. Mai 2026 (Lauf 002 — Tagesfolge) — Version 19.0 → Version 20.0" in `Validierung-Ergebnisse.md`)
- PDF erstellt (`build_pdf.py`): Ja
- Word erstellt (`build_docx.py`): Ja
- Versionsnummer in Hauptdokument, README, Validierung-Ergebnisse aktualisiert: Ja
- Branch auf main gemerged und gelöscht: erfolgt am Ende dieses Laufs

### Auffälligkeiten / offene Punkte

- Lauf 002 ist eine Tagesfolge zu Lauf 001 (beide am 7. Mai 2026); die Trefferdichte im 7-Tage-Fenster ist nach Lauf 001 erwartungsgemäß deutlich gesunken — eine einzige belegbare Cluster-D-Neuigkeit (Bloomberg-Editorial) wurde aufgenommen.
- Cluster G (Gesundheitswesen) erneut ohne valide Treffer im 7-Tage-Fenster — Empfehlung für die nächsten Läufe: gezielter Abruf von g-ba.de Sitzungsergebnissen, gematik-Pressemitteilungen und BfArM-Listings (DiGA mit KI-Komponente, KI-Hochrisiko-Klassifizierungen).
- Cluster I (Frontier-Modelle) und Cluster J (Robotik) im 48-Stunden-Fenster ohne politisch-fiskalisch relevante Tagesmeldungen; Beobachtung beim nächsten Lauf fortsetzen.
- NBER WP 34705 (Manning & Aguirre, Januar 2026) und Kang/Lee/Quach (SSRN 5005128) liegen außerhalb des Tagesfensters, könnten aber bei einem kommenden Wochenend-/Vertiefungslauf für eine § 3- oder § 6.1-Ergänzung geprüft werden — als Marker im Logbuch festgehalten.
- Branch dieses Laufs: `claude/lucid-hawking-g9w6e` (Session-Branch der laufenden Session, lokal angelegt, in Phase 0 dieses Laufs verifiziert).

---

## 2026-05-07 — Lauf 001 — Version 18.0 → Version 19.0

### Recherchekorridor

- Genutzte Cluster aus `Suchthemen.md`: A, B, C, D, E, F, H (Cluster G — Gesundheitssektor — ohne neue belegbare Treffer im 7-Tage-Fenster).
- Zeitfenster: 7 Tage (Cluster F: 48 Stunden).
- Anzahl Suchanfragen: 12 (Web-Suche), 1 (WebFetch).

### Gefundene Quellen

| # | Cluster | Quelle (Autor/Institution, Titel, Datum) | URL | Bewertung |
|---|---------|-----------------------------------------|-----|-----------|
| 1 | A | The Budget Lab at Yale, *Tracking the Impact of AI on the Labor Market — March CPS Update*, April 2026 | https://budgetlab.yale.edu/research/tracking-impact-ai-labor-market | übernommen |
| 2 | A | The Budget Lab at Yale via Fortune, *AI could solve America's $39 trillion debt crisis — but only if Washington abandons displaced workers*, 6. Mai 2026 | https://fortune.com/2026/05/06/39-trillion-national-debt-fix-ai-productivity-yale-budget-lab/ | übernommen |
| 3 | F | CNBC, *Coinbase cuts headcount by 14% citing AI acceleration*, 5. Mai 2026 | https://www.cnbc.com/2026/05/05/coinbase-cuts-headcount-by-14percent-citing-ai-acceleration-the-shares-are-gaining.html | übernommen |
| 4 | F | Engadget, *Coinbase lays off nearly 700 workers in „AI-native" restructuring*, 5. Mai 2026 | https://www.engadget.com/2165157/coinbase-lays-off-nearly-700-workers-in-ai-native-restructuring/ | übernommen (Sammelbeleg) |
| 5 | F | Coindesk, *Coinbase latest crypto firm to slash staff citing market conditions and AI shift. Reduces it by 14%.*, 5. Mai 2026 | https://www.coindesk.com/business/2026/05/05/coinbase-cuts-14-of-staff-as-ai-reshapes-how-crypto-companies-operate | übernommen (Sammelbeleg) |
| 6 | F | Fortune, *Coinbase didn't just lay off 14% of its staff due to AI*, 5. Mai 2026 | https://fortune.com/2026/05/05/coinbase-layoffs-14-of-employees-ai-tech-ai-job-anxiety-crypto/ | übernommen (Sammelbeleg) |
| 7 | F | Bloomberg, *PayPal Plans Job Cuts as Fintech's New CEO Pursues Turnaround Strategy*, 5. Mai 2026 | https://www.bloomberg.com/news/articles/2026-05-05/paypal-plans-job-cuts-as-fintech-s-new-ceo-pursues-turnaround-strategy | übernommen |
| 8 | F | TechCrunch, *PayPal says it's „becoming a technology company again" — that means AI*, 5. Mai 2026 | https://techcrunch.com/2026/05/05/paypal-says-its-becoming-a-technology-company-again-that-means-ai/ | übernommen (Sammelbeleg) |
| 9 | F | Yahoo Finance, *PayPal layoffs: New CEO cuts 20% of workforce in Q1 2026*, 5. Mai 2026 | https://finance.yahoo.com/markets/stocks/articles/paypal-layoffs-ceo-cuts-20-154944985.html | übernommen (Sammelbeleg) |
| 10 | F | TechRadar, *Freshworks and Coinbase announce more than 1 in 10 jobs to go as companies replace workforce with AI technologies*, 6. Mai 2026 | https://www.techradar.com/pro/freshworks-and-coinbase-announce-more-than-1-in-10-jobs-to-go-as-companies-replace-workforce-with-ai-technologies-tech-company-layoffs-near-100k-in-2026-alone | übernommen |
| 11 | F | Storyboard18, *Freshworks Layoffs 2026: „Over half of our code is written by AI," says CEO as firm cuts 500 jobs*, 5. Mai 2026 | https://www.storyboard18.com/brand-marketing/freshworks-layoffs-over-half-of-our-code-is-written-by-ai-says-ceo-as-firm-cuts-500-jobs-97275.htm | übernommen (Sammelbeleg) |
| 12 | F | American Bazaar, *Cognizant eyes up to 15,000 layoffs, India set to bear the brunt*, 6. Mai 2026 | https://americanbazaaronline.com/2026/05/06/cognizant-eyes-up-to-15000-layoffs-india-set-to-bear-the-brunt-480243/ | übernommen |
| 13 | F | TechResearchOnline, *Cognizant Layoffs 2026 Signal AI Shift in IT Services*, Mai 2026 | https://techresearchonline.com/news/cognizant-layoffs-2026-ai-restructuring-project-leap/ | übernommen (Sammelbeleg) |
| 14 | F | Goodreturns, *Layoffs 2026: Cognizant May Cut Up to 15,000 Jobs Globally Under „Project Leap"*, Mai 2026 | https://www.goodreturns.in/news/cognizant-layoffs-2026-it-company-may-cut-12000-15000-jobs-globally-major-impact-expected-in-india-1506427.html | übernommen (Sammelbeleg) |
| 15 | F | TrueUp, *Tech Layoffs Tracker — 7. Mai 2026 (121.111 Personen / 273 Meldungen)* | https://www.trueup.io/layoffs | übernommen |
| 16 | F | The Motley Fool, *Microsoft Just Launched a Major Voluntary Buyout*, 5. Mai 2026 | https://www.fool.com/investing/2026/05/05/microsoft-just-launched-a-major-voluntary-buyout-w/ | übernommen (Verfeinerung Microsoft VRSAR: Separation Date 2. Juli 2026, ~8.500 Beschäftigte) |
| 17 | A | NBER WP 34873 / Brookings — Korinek & Lockwood, *Public Finance in the Age of AI: A Primer* | https://www.nber.org/papers/w34873 | Dublette (bereits Version 9.0) |
| 18 | A | Brookings — *The future of tax policy: A public finance framework for the age of AI* | https://www.brookings.edu/articles/future-tax-policy-a-public-finance-framework-for-the-age-of-ai/ | Dublette |
| 19 | B | Bundesrat 1065. Sitzung 8. Mai 2026 | https://www.bundesrat.de/DE/plenum/bundesrat-kompakt/26/1065/1065-node.html | verworfen (Sitzung nach Stichtag) |
| 20 | B | EU AI Act Digital Omnibus Trilog 13. Mai 2026 | https://www.europarl.europa.eu/legislative-train/package-digital-package/file-digital-omnibus-on-ai | verworfen (Trilog nach Stichtag) |
| 21 | C | ulga na robotyzację Sejm 100% (Crido / Euro-Funding) | https://crido.pl/blog-business/ulga-na-robotyzacje-100-odliczenia-i-brak-daty-koncowej-projekt-juz-w-sejmie/ | Dublette (bereits Version 16.0) |
| 22 | D | Sanders Robotersteuer 2025/2026 (Fox Business, Washington Examiner) | https://www.foxbusiness.com/fox-news-tech/democrats-demand-robot-tax-ai-reportedly-threatens-replace-100m-u-s-jobs | Dublette |
| 23 | E | Bürgerversicherung / GKV-Finanzkommission (PKV-Verband) | https://www.pkv.de/verband/presse/meldungen/erhoehung-der-beitragsbemessungsgrenze-die-gkv-finanzkommission-sagt-klar-nein/ | verworfen (außerhalb engerer KI-/Robotik-Steuer-Linie) |

### Eingearbeitete Änderungen

| # | Stelle (§) | Art | Inhalt in einem Satz | Quelle # |
|---|-----------|-----|----------------------|----------|
| 1 | § 1.1 | Ergänzung | Tagesfortschreibung der TrueUp-Tracker-Methodik auf den 7. Mai 2026 (121.111 Personen / 273 Meldungen) und Aufnahme der vier am 5./6. Mai 2026 angekündigten Layoff-Wellen Coinbase (14 %), PayPal (20 %), Freshworks (11 %) und Cognizant (12.000–15.000) im Tracker-Satz. | 3–15 |
| 2 | § 1.1 | Aktualisierung | Microsoft-VRSAR-Block ergänzt um *Separation Date* 2. Juli 2026 und ~8.500 angebotsberechtigte Beschäftigte. | 16 |
| 3 | § 3.5 | Ergänzung | Neuer Folgesatz zur Yale-Budget-Lab-Tracking-Reihe (März-CPS-Update April 2026, kein aggregierter KI-Disruptionseffekt) und zur Mai-2026-Modellrechnung (39 Bio. USD US-Schulden, 88 Mrd. USD/Monat Zinsdienst, 5.500–42.400 USD Übergangshilfe je Verdrängtem) als unabhängige Bestätigung von Anthropic/Massenkoff & McCrory mit Querverweis auf § 8.4. | 1, 2 |
| 4 | § 11.1 | Ergänzung | Zwei neue Literatureinträge: Yale Budget Lab Tracking-Reihe; Yale Budget Lab / Fortune 6. Mai 2026. | 1, 2 |
| 5 | § 11.5 | Ergänzung | Fünf neue Sammelbelege: TrueUp-Tagesfortschreibung 7. Mai 2026; Coinbase-Belegcluster (CNBC/Engadget/Coindesk/Fortune); PayPal-Belegcluster (Bloomberg/TechCrunch/Yahoo Finance); Freshworks-Belegcluster (TechRadar/Storyboard18); Cognizant-Belegcluster (American Bazaar/TechResearchOnline/Goodreturns). | 3–15 |
| 6 | Aktualitätshinweis am Dokumentende | Aktualisierung | Erweiterte Schnittangabe „Anfang Mai 2026 (Schnitt am 7. Mai 2026 — abendliche Folgeaktualisierung)" und Aufnahme der vier neuen Layoff-Fälle, der Tracker-Tagesfortschreibung, des Microsoft-VRSAR-Updates und des Yale-Budget-Lab-Befundes in den Auflistungstext. | 1–16 |
| 7 | README.md | Aktualisierung | Versionssprung 18.0 → 19.0 (Versionszeile, Zitiervorschlag, neuer Versionseintrag in der KI-Offenlegung mit den drei Cluster-Bündeln). | — |
| 8 | Validierung-Ergebnisse.md | Ergänzung | Neuer Validierungsblock 7. Mai 2026 (abendlicher Folgelauf) mit Prüftabelle 2.1.1 – 2.6 und Abschluss „alle Fehler behoben: Ja". | — |

### Verworfene Treffer (mit Begründung)

| # | Quelle | Cluster | Begründung |
|---|--------|---------|------------|
| 1 | Bundesrat 1065. Sitzung 8. Mai 2026 (Tagesordnung) | B/E | Sitzung liegt nach dem Stichtag 7. Mai 2026 — bestehende § 5.2-/§ 11.3-Darstellung bleibt korrekt. |
| 2 | EU AI Act Digital Omnibus Trilog 13. Mai 2026 | B | Trilog hat zum Stichtag 7. Mai 2026 noch nicht stattgefunden — bestehende § 4.3-Darstellung bleibt korrekt. |
| 3 | Korinek & Lockwood Brookings/NBER 34873 | A | Dublette zu Version 9.0 (§ 3.3, § 11.1). |
| 4 | Brookings *Future of tax policy* | A | Dublette / dieselbe Autorenlinie wie Korinek & Lockwood. |
| 5 | ulga na robotyzację Sejm 100 % | C | Dublette zu Version 16.0 (§ 6.3 / § 11.3). |
| 6 | Sanders Robotersteuer 2025/2026 (Fox Business etc.) | D | Dublette zu Version 5.0/8.0 (§ 4.5 / § 11.3) — keine neuen Bewegungen seit dem 25. März 2026 / 16. April 2026. |
| 7 | PKV-Verband Bürgerversicherung / GKV-Finanzkommission | E | Bezug zur KI-/Robotik-Steuerdebatte zu indirekt; nicht im Korridor. |
| 8 | Connecticut SB 5 / Raised Bill 515 (Senatsabstimmung) | B | Bereits in Version 18.0 ausführlich behandelt; keine neuen Beschlüsse zwischen 6. und 7. Mai 2026. |
| 9 | Anthropic Economic Index Survey (erste Ergebnisse) | A | Erste Ergebnisse zum Stichtag 7. Mai 2026 noch nicht publiziert; § 3.5-Eintrag aus Version 18.0 bleibt korrekt. |
| 10 | Bürgerversicherung / Alterssicherungskommission (Mai-Stand) | E | Keine neuen Zwischenergebnisse zwischen Mittag- und Abendlauf des 7. Mai 2026. |
| 11 | Maine LD 307 / LD 713 | C | Bereits in Version 14.0 / 15.0 behandelt; keine neuen Bewegungen. |

### Verarbeitungsschritte

- Recherche abgeschlossen: Ja
- Deduplikation gegen Hauptdokument: Ja
- Validierung gemäß `Validierung.md` ausgeführt: Ja (Block „Validierung 7. Mai 2026 (abendlicher Folgelauf) — Version 18.0 → Version 19.0" in `Validierung-Ergebnisse.md`)
- PDF erstellt (`build_pdf.py`): Ja
- Word erstellt (`build_docx.py`): Ja
- Versionsnummer in Hauptdokument, README, Validierung-Ergebnisse aktualisiert: Ja
- Branch auf main gemerged und gelöscht: erfolgt am Ende dieses Laufs

### Auffälligkeiten / offene Punkte

- Der heutige Lauf ist der erste reguläre Daily-Update-Lauf nach Erstinitialisierung von `Suchthemen.md` und `Änderungshistorie.md`; er nutzt die Cluster-Logik aus `Suchthemen.md`.
- Im Verlauf der Session wurde der Feature-Branch `claude/great-fermi-G11Ic` (vom System für diese Session vorgegeben) statt des im Prompt generisch genannten `claude/daily-document-prompt-kF8qq` verwendet.
- Hinweis: `claude/daily-document-prompt-kF8qq` ist bereits in `main` integriert (Erstinitialisierung der Daily-Update-Routine). Mein Branch wurde mit `main` zusammengeführt, um die neuen Routinedateien (`Suchthemen.md`, `Änderungshistorie.md`, `DailyPrompt.md`) zu übernehmen.
- Cluster G (Gesundheitswesen) ohne neue belegbare Treffer im 7-Tage-Fenster — nächster Lauf sollte gezielt G-BA, gematik und BfArM prüfen.

---
