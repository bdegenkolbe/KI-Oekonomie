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

## 2026-06-06 — Lauf 001 — Version 22.0 → Version 23.0

### Recherchekorridor

- Genutzte Cluster aus `Suchthemen.md`: A, B, C, D, E, F, G, H, I, J (alle zehn Cluster gestreift; Cluster G — Gesundheitssektor — fünftes Mal in Folge ohne valide Treffer im 7-Tage-Fenster; Cluster J im 48-Stunden-Fenster ohne politisch-fiskalisch relevante Tagesmeldungen; Cluster F mit zwei aufgenommenen Treffern Mai-Challenger + Uber + Tracker-Stand; Cluster D mit aufgenommenem Treffer Sanders + Trump).
- Zeitfenster: 7 Tage (Cluster F: 48 Stunden für Uber und Tracker-Tagesstand; Cluster D: 7 Tage für Sanders/Trump-Konvergenz, dabei NYT-Op-Ed vom 1. Juni 2026 + Trump-Aussage 5. Juni 2026 im Fenster); Challenger-Mai-Report (Veröffentlichung 5. Juni 2026) im 48-Stunden-Fenster.
- Anzahl Suchanfragen: 10 (Web-Suche) + 3 (Web-Fetch zur Primärquellenverifikation).
- Lauf 001 ist der erste Daily-Update-Lauf am 6. Juni 2026 nach Lauf 001 vom 8. Mai 2026 (Version 22.0) — die längste Pause der bisherigen Lauf-Folge.

### Gefundene Quellen

| # | Cluster | Quelle (Autor/Institution, Titel, Datum) | URL | Bewertung |
|---|---------|-----------------------------------------|-----|-----------|
| 1 | D | Sanders, B., *The Public Should Own Half of the Big A.I. Companies* — NYT-Namensbeitrag / sanders.senate.gov, 1. Juni 2026 | https://www.sanders.senate.gov/op-eds/the-public-should-own-half-of-the-big-a-i-companies/ | übernommen |
| 2 | D | CNBC, *Trump administration, OpenAI discussing possible government stake in the AI startup*, 5. Juni 2026 | https://www.cnbc.com/2026/06/05/trump-open-ai-altman-stake.html | übernommen (Trump-Konvergenzsignal) |
| 3 | D | Fortune, *Bernie Sanders wants Americans to own a piece of AI. The Trump White House seems to agree*, 3. Juni 2026 | https://fortune.com/2026/06/03/bernie-sanders-ai-ownership-sovereign-wealth-fund-electrification/ | übernommen (Sammelbeleg) |
| 4 | D | Fortune, *MAGA hates AI, but Trump agrees with Bernie it might be time for partial government ownership*, 5. Juni 2026 | https://fortune.com/2026/06/05/trump-partnership-openai-anthropic-xai-nationalization-bernie-sanders-altman/ | übernommen (Sammelbeleg) |
| 5 | D | The Hill, *Bernie Sanders to propose bill allowing for 50% public stake in AI companies*, 1.–2. Juni 2026 | https://thehill.com/policy/technology/5906140-sanders-ai-ownership-wealth/ | übernommen (Sammelbeleg) |
| 6 | D | Common Dreams, *Sanders Sovereign Wealth Fund Plan Would Give US Public 'Direct Ownership Stake' in AI Giants*, 1.–2. Juni 2026 | https://www.commondreams.org/news/bernies-sanders-ai-sovereign-wealth-fund | übernommen (Sammelbeleg) |
| 7 | D | Newsweek, *Millions Would Get 'Direct Payments' Under Bernie Sanders' Proposed AI Sovereign Wealth Fund*, 1.–2. Juni 2026 | https://www.newsweek.com/direct-payments-ai-sovereign-wealth-fund-bernie-sanders-12021907 | übernommen (Sammelbeleg) |
| 8 | D | Benzinga, *Bernie Sanders Wants Americans To Own 50% Of OpenAI, xAI And Anthropic*, 2. Juni 2026 | https://www.benzinga.com/markets/tech/26/06/52932722/bernie-sanders-wants-americans-to-own-50-of-openai-xai-and-anthropic-in-sweeping-new-bill-heres-what-that-means | übernommen (Sammelbeleg) |
| 9 | D | Yahoo Finance / Futurism, *Bernie Sanders Announces Plan to Seize Half of AI Industry for the Public Good*, 1.–2. Juni 2026 | https://finance.yahoo.com/economy/policy/articles/bernie-sanders-announces-plan-seize-180301711.html | übernommen (Sammelbeleg) |
| 10 | D | Washington Post (Opinion), *Bernie Sanders wants a government stake in AI companies*, 3. Juni 2026 | https://www.washingtonpost.com/opinions/2026/06/03/bernie-sanders-wants-government-stake-ai-companies/ | übernommen (Mainstream-Kommentierung) |
| 11 | D | Reason, *Bernie Sanders' AI wealth fund bill shows that he doesn't understand AI or wealth*, 2. Juni 2026 | https://reason.com/2026/06/02/bernie-sanders-ai-wealth-fund-bill-shows-that-he-doesnt-understand-ai-or-wealth/ | übernommen (libertäre Gegenstimme) |
| 12 | F | Challenger, Gray & Christmas, *Challenger Report: May Job Cuts Rise 16 % from April; Highest May Total Since 2020*, 5. Juni 2026 | https://www.challengergray.com/blog/challenger-report-may-job-cuts-rise-16-from-april-highest-may-total-since-2020/ | übernommen |
| 13 | F | CNBC, *„AI is now the leading reason companies give for cutting jobs," says new report*, 5. Juni 2026 | https://www.cnbc.com/2026/06/05/ai-is-now-the-leading-reason-companies-give-for-cutting-jobs-says-new-report-what-that-means-for-workers.html | übernommen (Sammelbeleg) |
| 14 | F | Tom's Hardware, *US tech layoffs record single-highest month in two years*, 5. Juni 2026 | https://www.tomshardware.com/tech-industry/artificial-intelligence/tech-sector-cut-us-jobs-by-38242-in-may | übernommen (Sammelbeleg) |
| 15 | F | Yahoo Finance, *AI Has Cut More US Jobs in 2026 Than in All of 2025 Already*, 5. Juni 2026 | https://finance.yahoo.com/economy/articles/ai-cut-more-us-jobs-082155018.html | übernommen (Sammelbeleg) |
| 16 | F | Quartz, *U.S. tech sector hits two-year high for job cuts in May 2026*, 5. Juni 2026 | https://qz.com/tech-job-cuts-ai-layoffs-may-2026-060526 | übernommen (Sammelbeleg) |
| 17 | F | Human Resources Director, *AI-driven tech job cuts hit two-year high*, 5. Juni 2026 | https://www.hcamag.com/us/specialization/recruitment/ai-driven-tech-job-cuts-hit-two-year-high-leaving-hr-leaders-to-adapt/577778 | übernommen (Sammelbeleg) |
| 18 | F | CNBC, *Uber layoffs: People division cut by nearly a quarter*, 3. Juni 2026 | https://www.cnbc.com/2026/06/03/uber-layoffs-people-division-ai.html | übernommen (Primärbericht) |
| 19 | F | TechTimes, *Uber Cuts 23 % of HR Staff: New President Denies AI Role as 95 % of Engineers Use It Daily*, 5. Juni 2026 | https://www.techtimes.com/articles/317842/20260605/uber-cuts-23-hr-staff-new-president-denies-ai-role-95-engineers-use-it-daily.htm | übernommen (Sammelbeleg) |
| 20 | F | NewsX, *Mass Layoffs At Uber: Here's Why New President Cut 23 % Of HR Team And Denies Any AI Role*, 3.–5. Juni 2026 | https://www.newsx.com/tech-and-auto/mass-layoffs-at-uber-heres-why-new-president-cut-23-of-hr-team-and-denies-any-ai-role-230048/ | übernommen (Sammelbeleg) |
| 21 | F | Layoffhedge, *Uber Layoffs 2026 — 23 % of People Division Cut*, 3.–5. Juni 2026 | https://layoffhedge.com/company/uber | übernommen (Sammelbeleg) |
| 22 | F | TechTimes, *Tech Layoffs 2026 Hit 149,935: Uber Cuts HR Days After AI Drained Its Coding Budget*, 5. Juni 2026 | https://www.techtimes.com/articles/317848/20260605/tech-layoffs-2026-hit-149935-uber-cuts-hr-days-after-ai-drained-its-coding-budget.htm | übernommen (Tracker-Aggregat) |
| 23 | I | NVIDIA Q1 FY27 Earnings (CFO Commentary 20.–21. Mai 2026): $81,6 Mrd. Gesamterlös, $75,2 Mrd. Data Center, Sovereign AI > $30 Mrd. in FY26 | https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000051/q1fy27cfocommentary.htm | verworfen (außerhalb 48-Stunden-Fenster für Cluster I; bestehender § 1.1-Capex-Block bereits ausreichend; in nächstem Lauf optional einarbeiten) |
| 24 | A/D | Anthropic-CEO Dario Amodei, Jevons-Paradox-Pivot (Anthropic-Briefing Lower Manhattan, Anfang Mai 2026; Fortune 5. Mai 2026) | https://fortune.com/2026/05/05/dario-amodei-jevons-paradox-will-ai-wipe-out-white-collar-jobs/ | verworfen (außerhalb 7-Tage-Fenster; in nächstem Lauf zu prüfen, wenn schriftliches Folgepapier vorliegt) |
| 25 | B | BMDS, *Kabinett beschließt schlanke KI-Aufsicht in Deutschland* (KI-MIG-Kabinettsbeschluss 11. Februar 2026, Federführung Bundesnetzagentur) | https://bmds.bund.de/aktuelles/pressemitteilungen/detail/kabinett-beschliesst-schlanke-ki-aufsicht-in-deutschland | verworfen (außerhalb 7-Tage-Fenster; thematisch primär AI-Act-Implementierung, nicht KI-Besteuerung; im Aktualitätshinweis-Verweis auf 2. August 2026 [AI-Act-Anwendungsbeginn] abgedeckt) |
| 26 | B/E | Bundesrat — 1. Durchgang GKV-Beitragssatzstabilisierungsgesetz am 12. Juni 2026, 2. Durchgang am 10. Juli 2026 | https://www.bundesgesundheitsministerium.de/service/gesetze-und-verordnungen/detail/gkv-beitragssatzstabilisierungsgesetz | verworfen (Termine nach Stichtag; in nächsten Läufen aufzunehmen — bestehender Aktualitätshinweis aktualisiert auf 12. Juni 2026) |
| 27 | A | Acemoglu, D., Autor, D., & Johnson, S., *Building Pro-Worker Artificial Intelligence* (Februar 2026) | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6290347 | Dublette (in Version 16.0 bereits in § 3.5 und § 11.1 referenziert) |
| 28 | A | Anthropic Economic Index Reports (Januar, März 2026) | https://www.anthropic.com/economic-index | Dublette (in Versionen 16.0 und 18.0 bereits referenziert; kein neuer Bericht seit März 2026) |
| 29 | J | IFR World Robotics 2026, *Top 5 Global Robotics Trends* (Januar 2026) | https://ifr.org/ifr-press-releases | verworfen (außerhalb 7-Tage-Fenster; thematisch in § 1.1-Robotik-Abschnitt bereits abgedeckt) |
| 30 | E | IAB-Prognose 2026 / Regionalprognose 2026 (24. März 2026) | https://iab.de | Dublette (in Version 15.0 in § 11.3 referenziert) |
| 31 | A/D | OECD AI & Tax Dashboard / *Governing with AI in Tax Administration* | https://oecd.ai/en/dashboards/policy-areas/PA18 | verworfen (keine spezifische neue OECD-Publikation im 7-Tage-Fenster zur Robotersteuer/KI-Besteuerung identifiziert) |
| 32 | H | Bundesbank-Symposium 2026 / Sachverständigenrat-Frühjahrsgutachten | https://www.bundesbank.de/de/aufgaben/themen/bundesbank-symposium-2026 | verworfen (keine spezifische Robotersteuer- oder Wertschöpfungsabgaben-Bewegung im 7-Tage-Fenster) |
| 33 | D | EU-Kommission, *Digital AI Omnibus on AI Act* (Trilog-Folgerunden Mai 2026) | https://digital-strategy.ec.europa.eu/en/library/digital-omnibus-ai-regulation-proposal | Dublette (in Version 22.0 in § 11.3 referenziert; politische Einigung 7. Mai 2026 bereits dokumentiert) |

### Eingearbeitete Änderungen

| # | Stelle (§) | Art | Inhalt in einem Satz | Quelle # |
|---|-----------|-----|----------------------|----------|
| 1 | § 4.5 | Ergänzung | Neuer Block *„Sanders' American AI Sovereign Wealth Fund Act (Juni 2026)"* — NYT-Op-Ed vom 1. Juni 2026, einmalige Anteilsabgabe von 50 % der Aktien (nicht des Gewinns) an OpenAI, Anthropic, xAI in einen US-Staatsfonds mit Stimmrechten und Vorstandsvertretung; Verlängerung des OpenAI-*Public-Wealth-Fund*-Vorschlags und der Anthropic-CEO-Befürwortung; Konvergenzsignal Trump 5. Juni 2026; Sanders-Altman-Gespräch 3. Juni 2026; Bessent-Lutnick-Vorentwurf; Annahmewahrscheinlichkeit von „nahezu null" auf „nicht auszuschließen" verschoben; verfassungsrechtliche Vorfragen Art. 14 GG (Eigentumsgarantie) und Art. 15 GG (Sozialisierung) für deutschen Kontext markiert. | 1–11 |
| 2 | § 5.4 | Ergänzung | Anhängsel-Satz: Sanders-Bill überführt den ersten Pfad (Pflichtbeteiligung des Staates) erstmals in eine kongressreif vorbereitete Gesetzesfigur; Verschiebung des Diskussionspunkts von „politischer Unmöglichkeit" auf verfassungsrechtliche Tragfähigkeit über Art. 14 GG / Art. 15 GG. | 1, 2 |
| 3 | § 8.3 | Ergänzung | Erweiterung der „Eigentums-/Verstaatlichungslogik"-Passage um den US-Vergleichsmaßstab (Sanders-Bill, Trump-Konvergenzsignal) und um die Bekräftigung, dass die abschöpfungsbasierte deutsche Position konzeptionell überlegen bleibt, weil Art. 14 GG und Art. 15 GG nicht in Anspruch genommen werden müssen. | 1, 2 |
| 4 | § 1.1 | Ergänzung | Aggregat-Bestätigung der KI-Verdrängungslinie über den Challenger *Mai-2026-Job-Cuts-Report* (97.006 Mai-Streichungen +16 % vs. April, höchster Mai-Wert seit 2020; KI 38.579 / 40 %, höchster Monatswert seit Tracking-Beginn 2023; YTD-Gesamt 397.755 mit KI 87.714 / 22 % — übersteigt 2025-Gesamt von 54.836 vor Jahresmitte; Tech Mai 38.242 / YTD 123.653 +66 % YoY) sowie Spiegelfall *Uber Technologies* (3. Juni 2026, 23 % der People-and-Places-Division, „nicht KI-getrieben" *vs.* 95 % KI-Tool-Nutzung der Ingenieure / 70 % KI-Code, Forrester-„AI washing"-Einordnung). | 12–21 |
| 5 | § 1.1 | Aktualisierung | TechTimes/TrueUp-Tracker-Tagesstand 5. Juni 2026 (149.935 Personen aus 363 Layoff-Meldungen, rund 974 Stellen pro Tag, 2026-Tempo +44 % vs. 2025) als vierte Stufe der Tracker-Reihe (127.411 zum 8. Mai → 149.935 zum 5. Juni) eingegliedert. | 22 |
| 6 | § 11.3 | Ergänzung | Zwei neue Einträge: Sanders, B. (1. Juni 2026, NYT-Op-Ed) und White House / CNBC / Fortune-Sammelbeleg (3.–5. Juni 2026) zum Trump-Konvergenzsignal und Bessent-Lutnick-Vorentwurf. | 1, 2, 3, 4 |
| 7 | § 11.5 | Ergänzung | Fünf neue Sammelbelege: Challenger-Mai-Report-Berichterstattung (Challenger Gray / CNBC / Tom's Hardware / Yahoo Finance / Quartz / Human Resources Director), Uber-Layoff-Berichterstattung (CNBC / TechTimes / NewsX / Layoffhedge), TechTimes-Tracker-Aggregat (5. Juni 2026), Sammelberichterstattung zur Sanders-Initiative (Fortune / Common Dreams / Newsweek / The Hill / Yahoo Finance) sowie Mainstream-/libertäre Kommentierung (Washington Post / Reason). | 5–22 |
| 8 | Aktualitätshinweis am Dokumentende | Aktualisierung | Schnittangabe auf „Lauf 001 vom 6. Juni 2026" geändert; Sanders/Trump-Konvergenz, Challenger-Mai-Aggregat, Uber-Spiegelfall und Tracker-5.-Juni-Stand neu aufgenommen; bisheriger Mai-Schnitt unter neuer Überschrift *„Frühere Aktualitäts-Schnitte"* als historischer Block erhalten. | 1–22 |
| 9 | Dokumentkopf KI-Ökonomie.md | Aktualisierung | Stand: Juni 2026 (statt Mai 2026); Version: 23.0 (statt 22.0). | — |
| 10 | README.md | Aktualisierung | Versionssprung 22.0 → 23.0 (Versionszeile, Zitiervorschlag, Aktualisierungs-Satz, neuer Versions-Eintrag in der KI-Offenlegung mit Beschreibung der vier Cluster-D/F-Treffer). | — |
| 11 | Validierung-Ergebnisse.md | Ergänzung | Neuer Validierungsblock „Validierung 6. Juni 2026 (Lauf 001 vom 6. Juni 2026) — Version 22.0 → Version 23.0" mit vollständiger Prüftabelle 2.1.1 – 2.6 und Abschluss „alle Fehler behoben: Ja". | — |

### Verworfene Treffer (mit Begründung)

| # | Quelle | Cluster | Begründung |
|---|--------|---------|------------|
| 1 | NVIDIA Q1 FY27 Earnings (CFO Commentary, 20.–21. Mai 2026) | I | außerhalb 48-Stunden-Fenster (Cluster I); bestehender § 1.1-Capex-Block bereits ausreichend abgedeckt; Lauf-Empfehlung: bei nächster Tagesaktualisierung im Capex-Block aufnehmen |
| 2 | Dario Amodei Jevons-Paradox-Pivot (Fortune, 5. Mai 2026) | A/D | außerhalb 7-Tage-Fenster; in nächstem Lauf zu prüfen, wenn ein schriftliches Folgepapier vorliegt |
| 3 | BMDS KI-MIG-Kabinettsbeschluss 11. Februar 2026 | B | außerhalb 7-Tage-Fenster; thematisch primär AI-Act-Implementierung, nicht KI-Besteuerung; im Aktualitätshinweis-Verweis auf 2. August 2026 (AI-Act-Anwendungsbeginn) abgedeckt |
| 4 | Bundesrat 1. Durchgang GKV-Beitragssatzstabilisierungsgesetz 12. Juni 2026 | B/E | Termin nach Stichtag; im neuen Aktualitätshinweis explizit als anstehendes Verfahren genannt; in nächstem Lauf nach 12. Juni 2026 aufzunehmen |
| 5 | Acemoglu/Autor/Johnson „Building Pro-Worker AI" | A | Dublette (in Version 16.0 in § 3.5 und § 11.1 bereits referenziert) |
| 6 | Anthropic Economic Index (Januar/März 2026) | A/I | Dublette (in Versionen 16.0 und 18.0 bereits referenziert; kein neuer Hauptbericht seit März 2026) |
| 7 | IFR World Robotics 2026 *Top 5 Trends* (Januar 2026) | J | außerhalb 7-Tage-Fenster; thematisch in § 1.1-Robotik-Abschnitt bereits abgedeckt |
| 8 | IAB-Prognose 2026 / Regionalprognose 2026 (März 2026) | E | Dublette (in Version 15.0 in § 11.3 referenziert) |
| 9 | OECD AI & Tax Dashboard | A/D | keine spezifische neue OECD-Publikation im 7-Tage-Fenster zur Robotersteuer/KI-Besteuerung identifiziert |
| 10 | Bundesbank-Symposium 2026 / Sachverständigenrat-Frühjahrsgutachten | H | keine spezifische Robotersteuer- oder Wertschöpfungsabgaben-Bewegung im 7-Tage-Fenster identifiziert |
| 11 | EU-Kommission *Digital AI Omnibus on AI Act* (Trilog Mai 2026) | D | Dublette (in Version 22.0 in § 11.3 referenziert; politische Einigung 7. Mai 2026 bereits dokumentiert) |
| 12 | Cluster G (Gesundheitswesen) — keine validen Treffer | G | fünftes Mal in Folge ohne valide Treffer im 7-Tage-Fenster; Empfehlung für die nächsten Läufe bestehend |
| 13 | Cluster J (Robotik) — keine validen Treffer im 48-Stunden-Fenster | J | keine politisch-fiskalisch relevanten Tagesmeldungen |
| 14 | Microsoft VRSAR — Annahmefrist 8. Juni 2026 | F | Vorlauf, kein Vollzug; im Aktualitätshinweis weiterhin nur als laufendes Verfahren referenziert |

### Verarbeitungsschritte

- Recherche abgeschlossen: Ja
- Deduplikation gegen Hauptdokument: Ja
- Validierung gemäß `Validierung.md` ausgeführt: Ja (Block „Validierung 6. Juni 2026 (Lauf 001 vom 6. Juni 2026) — Version 22.0 → Version 23.0" in `Validierung-Ergebnisse.md`)
- PDF erstellt (`build_pdf.py`): Ja
- Word erstellt (`build_docx.py`): Ja
- Versionsnummer in Hauptdokument, README, Validierung-Ergebnisse aktualisiert: Ja (22.0 → 23.0 in allen vier Stellen)
- E-Mail-Benachrichtigung (Phase 5b): siehe Eintrag im Logbuch unter „Auffälligkeiten" (Versandkanal-Auflösung)
- WhatsApp-Benachrichtigung (Phase 5b): siehe Eintrag im Logbuch unter „Auffälligkeiten" (Versandkanal-Auflösung)
- Branch auf main gemerged und gelöscht: siehe Logbuch-Block am Ende des Laufs (Phase 6)

### Auffälligkeiten / offene Punkte

- **Versandkanal-Auflösung (Phase 5b):** Die Routine-Anweisung hat E-Mail- und WhatsApp-Empfänger übergeben. In der Recherchesitzung waren weder ein `mail_send`/`send_mail`-Tool aus dem `graph-mcp`-Server (Microsoft Graph) noch ein `wa_send_message`-Tool aus einem `whatsapp`-Server erreichbar — die in dieser Session verfügbaren MCP-Server (Canva, Context7, Crypto-com, Mermaid-Chart, Microsoft-365 [nur lesende Tools wie outlook_email_search], PubMed, Supabase, bioRxiv, github) decken den Versand nicht ab. Gemäß Phase-5b-Fallback wurden die vorbereiteten Inhalte daher in `daily-mail.txt` und `daily-whatsapp.txt` im Repo-Root abgelegt (Empfängerdaten ausschließlich auf diesem Pfad, nicht im Logbuch, nicht in Commits, nicht im Hauptdokument).
- **Sanders/Trump-Konvergenz:** Markiert den ersten Fall einer parteienübergreifenden Annäherung an einen US-KI-Staatsfonds — eine Pfad-Verschiebung, die in den nächsten Läufen genau zu beobachten ist (Bill-Einbringung „in den kommenden Wochen"; Bessent-Lutnick-Vorentwurf-Status im Weißen Haus weiterhin in Bewegung). Empfehlung: Cluster D in den nächsten Läufen auf Vollständigkeit prüfen.
- **NVIDIA Q1 FY27 (20.–21. Mai 2026):** Außerhalb des Cluster-I-48-Stunden-Fensters, aber wirtschaftlich hochrelevant (Data Center $75,2 Mrd. +92 % YoY; Sovereign AI > $30 Mrd. in FY26). In einem der nächsten Läufe als Verlängerung des § 1.1-Capex-Blocks integrieren, sobald ein neuer Auslöser im Zeitfenster verfügbar ist.
- **GKV-Beitragssatzstabilisierungsgesetz 12. Juni 2026:** Erster Bundesratsdurchgang nach dem heutigen Stichtag; im nächsten Lauf nachzuholen.
- **Lauf-Lücke vom 9. Mai bis 5. Juni 2026:** Die Pause von rund 28 Tagen ist die längste der bisherigen Lauf-Folge; entsprechend höhere Treffer-Dichte in diesem Lauf. Empfehlung: bei Wiederaufnahme der Tageskadenz die Treffer aus dem unmittelbar zurückliegenden 7-Tage-Fenster konsequent nachziehen, um keine Sekundär-Aggregat-Bewegung zu verpassen.
- **Phase 6 Branch-Status:** Session-Branch `claude/determined-einstein-zPCjB` lokal angelegt und auf origin gepusht (Commit-Hash `ce13f3a`). Lokaler Merge auf `main` mit `--no-ff` erfolgreich; `git push origin main` schlug — wie bereits in Lauf 001 vom 8. Mai 2026 dokumentiert — mit HTTP 403 fehl (drei Retries mit Backoff 2 s / 4 s / 8 s ohne Erfolg). Der Remote-Branch wurde nicht gelöscht, weil der lokale Main-Stand wegen des 403 nicht authoritativ auf den Remote übertragen werden kann; Cleanup wird übersprungen, der Session-Branch bleibt remote bestehen und ist die authoritative Quelle für diesen Lauf.

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
