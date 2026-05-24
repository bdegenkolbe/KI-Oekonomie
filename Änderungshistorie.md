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

## 2026-05-24 — Lauf 001 — Version 22.0 → Version 23.0

### Recherchekorridor

- Genutzte Cluster aus `Suchthemen.md`: A, B, C, D, E, F, G, H, I, J (alle zehn Cluster gestreift; Schwerpunkte auf B/F/C; Cluster G — Gesundheitssektor — fünftes Mal in Folge ohne neue belegbare Treffer im 7-Tage-Fenster; Cluster I/J im 48-Stunden-Fenster ohne politisch-fiskalisch relevante Tagesmeldungen).
- Zeitfenster: 7 Tage (17.–24. Mai 2026) Standard; Cluster F: 48 Stunden Standard, aber Catch-up-Fenster bis 9. Mai 2026, da Lauf 001 vom 8. Mai 2026 das letzte reguläre Daily-Update war (16-tägige Pause); Cluster I: 48 Stunden. Zwei Hochrelevanz-Items wurden aus dem erweiterten Catch-up-Fenster aufgenommen (EU Digital Omnibus on AI Einigung vom 7. Mai 2026 und chinesische Gerichtsurteile vom 28. April / Anfang Mai 2026), die im Lauf 001 vom 8. Mai 2026 nicht erfasst wurden.
- Anzahl Suchanfragen: 17 (Web-Suche), 2 (WebFetch — eine erfolgreich, eine 403).
- Lauf 001 vom 24. Mai 2026 ist der erste reguläre Daily-Update-Lauf nach 16-tägiger Pause (letzter Lauf 001 vom 8. Mai 2026 mit Versionssprung 21.0 → 22.0).

### Gefundene Quellen

| # | Cluster | Quelle (Autor/Institution, Titel, Datum) | URL | Bewertung |
|---|---------|-----------------------------------------|-----|-----------|
| 1 | B | Council of the EU, *Artificial Intelligence: Council and Parliament agree to simplify and streamline rules*, 7. Mai 2026 | https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/ | übernommen |
| 2 | B | Bird & Bird, *Digital Omnibus on AI Provisional Agreement Reached at the May Trilogue*, 7./8. Mai 2026 | https://www.twobirds.com/en/insights/2026/digital-omnibus-on-ai-provisional-agreement-reached-at-the-may-trilogue | übernommen (Sammelbeleg) |
| 3 | B | White & Case LLP, *EU agrees Digital Omnibus deal to simplify AI rules*, Mai 2026 | https://www.whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules | übernommen (Sammelbeleg) |
| 4 | B | Lexology, *EU Digital Omnibus Deal: Simplification of AI Act and Postponed Deadlines*, Mai 2026 | https://www.lexology.com/library/detail.aspx?g=34c6a42f-af33-4189-a32c-dc2e3d7a109f | übernommen (Sammelbeleg) |
| 5 | B | Modulos, *EU AI Act Delayed: The Omnibus Deal Closed on 7 May 2026*, Mai 2026 | https://www.modulos.ai/blog/eu-ai-act-omnibus-deal/ | übernommen (Sammelbeleg) |
| 6 | B | Orrick, *EU's Digital Omnibus on AI: 7 Key Changes You Need to Know*, Mai 2026 | https://www.orrick.com/en/Insights/2026/05/EUs-Digital-Omnibus-on-AI-7-Key-Changes-You-Need-to-Know | übernommen (Sammelbeleg) |
| 7 | B | Inside Privacy / Covington, *EU AI Act Update: Timeline Relief, Targeted Simplification, and New Prohibitions*, Mai 2026 | https://www.insideprivacy.com/artificial-intelligence/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/ | übernommen (Sammelbeleg) |
| 8 | B | TechPolicy.Press, *What the EU AI Omnibus Deal Changes for the AI Act and What Lies Ahead*, Mai 2026 | https://www.techpolicy.press/what-the-eu-ai-omnibus-deal-changes-for-the-ai-act-and-what-lies-ahead/ | übernommen (Sammelbeleg) |
| 9 | F | TechCrunch, *Cisco cuts nearly 4,000 jobs to spend more on AI, reports „record quarterly revenue"*, 14. Mai 2026 | https://techcrunch.com/2026/05/14/cisco-cuts-nearly-4000-jobs-to-spend-more-on-ai-reports-record-quarterly-revenue/ | übernommen |
| 10 | F | Cisco Systems, *SEC-Form-8-K Q3 FY2026*, 13. Mai 2026 | https://www.sec.gov/Archives/edgar/data/0000858877/000085887726000075/exhibit991pressrelease-q3f.htm | übernommen (Primärquelle) |
| 11 | F | Fox Business, *Cisco to cut thousands of jobs as AI push accelerates after earnings beat*, 13. Mai 2026 | https://www.foxbusiness.com/technology/cisco-cut-thousands-jobs-ai-push-accelerates-earnings-beat | übernommen (Sammelbeleg) |
| 12 | F | Bloomberg, *LinkedIn Cuts Jobs as Microsoft Streamlines Workforce for AI Growth*, 13. Mai 2026 | https://www.bloomberg.com/news/articles/2026-05-13/microsoft-s-linkedin-is-cutting-jobs-in-latest-industry-cull | übernommen |
| 13 | F | TechRepublic, *LinkedIn Cuts Jobs Despite Revenue Growth as Tech Layoffs Keep Spreading*, Mai 2026 | https://www.techrepublic.com/article/news-linkedin-layoffs-may-2026/ | übernommen (Sammelbeleg) |
| 14 | F | Republic World, *LinkedIn Layoffs 2026: 900 Jobs Cut as Microsoft-Owned Platform Restructures Teams Around AI*, 14. Mai 2026 | https://www.republicworld.com/tech/linkedin-layoffs-2026-900-jobs-cut-as-microsoft-owned-platform-restructures-teams-around-ai-2026-05-14-124183 | übernommen (Sammelbeleg) |
| 15 | F | NPR, *Meta slashes 8,000 jobs as it pivots towards AI*, 20. Mai 2026 | https://www.npr.org/2026/05/20/nx-s1-5826917/meta-layoffs-ai-jobs | übernommen |
| 16 | F | OPB, *Meta slashes 8,000 jobs as it pivots towards AI*, 20. Mai 2026 | https://www.opb.org/article/2026/05/20/meta-slashes-8000-jobs-as-it-pivots-towards-ai/ | übernommen (Sammelbeleg) |
| 17 | F | PYMNTS, *Meta Prepares 8000 Layoffs to Offset AI Infrastructure Investments*, Mai 2026 | https://www.pymnts.com/meta/2026/meta-prepares-8000-layoffs-to-offset-ai-infrastructure-investments/ | übernommen (Sammelbeleg) |
| 18 | F | TechCrunch, *Intuit to lay off over 3,000 employees to refocus on AI*, 20. Mai 2026 | https://techcrunch.com/2026/05/20/intuit-to-lay-off-over-3000-employees-to-refocus-on-ai/ | übernommen |
| 19 | F | Slashdot, *Intuit To Lay Off Over 3,000 Employees To Refocus On AI*, 20. Mai 2026 | https://slashdot.org/story/26/05/20/2038203/intuit-to-lay-off-over-3000-employees-to-refocus-on-ai | übernommen (Sammelbeleg) |
| 20 | F | KOLO TV, *Intuit announces layoffs, winds down operations in Reno*, 21. Mai 2026 | https://www.kolotv.com/2026/05/21/intuit-announces-layoffs-winds-down-operations-reno/ | übernommen (Sammelbeleg) |
| 21 | F | TrueUp / SkillSyncer, *Tech Layoffs Tracker — Stand 24. Mai 2026: 142.985 Personen aus 339 Layoff-Meldungen* | https://www.trueup.io/layoffs \| https://skillsyncer.com/layoffs-tracker | übernommen |
| 22 | F | Washington Post, *Layoffs might feel like they're soaring, but they're not*, 21. Mai 2026 | https://www.washingtonpost.com/technology/2026/05/21/layoffs-might-feel-like-theyre-soaring-they-not/ | übernommen |
| 23 | C | Caixin Global, *Chinese Courts Rule Companies Cannot Fire Workers Simply to Replace Them With AI*, 30. April 2026 | https://www.caixinglobal.com/2026-04-30/chinese-courts-rule-companies-cannot-fire-workers-simply-to-replace-them-with-ai-102439602.html | übernommen |
| 24 | C | NPR, *A tech worker in China is laid off and replaced by AI. Is it legal?*, 1. Mai 2026 | https://www.npr.org/2026/05/01/nx-s1-5807131/tech-worker-china-ai | übernommen (Sammelbeleg) |
| 25 | C | Bloomberg, *Chinese Court Bars Companies From Firing Workers Solely for AI Replacement*, 2. Mai 2026 | https://www.bloomberg.com/news/articles/2026-05-02/chinese-court-rules-firms-can-t-lay-off-workers-on-ai-grounds | übernommen (Sammelbeleg) |
| 26 | C | Fortune, *Chinese court rules firms can't lay off workers on AI grounds*, 3. Mai 2026 | https://fortune.com/2026/05/03/chinese-court-layoffs-workers-ai-replacement-labor-market/ | übernommen (Sammelbeleg) |
| 27 | C | China.org.cn / SCIO, *Chinese court defends labor rights in new AI-replacement case*, 30. April 2026 | http://english.scio.gov.cn/m/chinavoices/2026-04/30/content_118471189.html | übernommen (Sammelbeleg) |
| 28 | B | YouGov, *47 % of Britons would back an AI tax*, 5. Mai 2026 | https://yougov.com/en-gb/daily-results/20260505-eadfa-3 \| https://www.resultsense.com/news/2026-05-07-yougov-britons-ai-tax-impact-poll/ | verworfen (außerhalb Catch-up-Fenster und Meinungsumfrage-Niveau) |
| 29 | C | Stephensons / ITIF / ScienceDirect / SSRN, *South Korea Robot Tax 2018 Reduction; Industries Impacted Reduced Robot Installations 28 %; ITIF Fact-of-the-Week*, Februar 2026 | https://itif.org/publications/2026/02/09/industries-impacted-by-quasi-robot-tax-south-korea-reduced-industrial-robot-installations/ | verworfen (außerhalb Catch-up-Fenster, bestehender § 6.1-Block bleibt korrekt) |
| 30 | B/G | Bundesrat 1065. Sitzung 8. Mai 2026 / GKV-Beitragssatzstabilisierungsgesetz | https://www.bundesrat.de/DE/plenum/bundesrat-kompakt/26/1065/1065-node.html | verworfen (Gesetz nicht auf Tagesordnung, keine Bundesratsstellungnahme erfolgt; in einem späteren Lauf zu prüfen) |
| 31 | B | Connecticut SB 5 — Lamont-Unterzeichnung (Stichtag 24. Mai 2026, noch nicht öffentlich datiert) | https://www.transparencycoalition.ai/news/tcai-bill-guide-sb-5-connecticuts-omnibus-ai-and-online-safety-bill | verworfen (Unterzeichnung formal noch nicht datierbar; bestehender § 4.5-Block bleibt korrekt; nächster Lauf zu prüfen) |
| 32 | F | Bungie Layoff (21. Mai 2026, Destiny-2-Entwicklung) | (Yahoo Finance referenziert) | verworfen (unter Schwelle 500+ Stellen für Einzelfall in § 1.1; Aggregat-Linie über TrueUp/Challenger abgedeckt) |
| 33 | F | Microsoft VRSAR — Acceptance-Update 30 Tage nach 7. Mai 2026 noch nicht öffentlich aggregiert | (Yahoo Finance, Quartz, CNN Business) | verworfen (keine neuen Aggregat-Zahlen über die in Version 18.0 dokumentierten Programmkonditionen hinaus; in einem späteren Lauf nach 8. Juni 2026 erneut zu prüfen) |
| 34 | A | Korinek/Lockwood Public Finance in the Age of AI (NBER Working Paper 34873, Revision April 2026) | https://www.nber.org/papers/w34873 | Dublette (in Version 9.0 / § 11.1 referenziert) |
| 35 | A | Hamilton Project / Acemoglu, Autor, Johnson, *Building Pro-Worker AI* (Februar 2026) | https://www.hamiltonproject.org/publication/paper/building-pro-worker-ai/ | Dublette (in Version 16.0 / § 11.1 referenziert) |
| 36 | A/F | Yale Budget Lab — Tracking Impact of AI on Labor Market, März-CPS-Update April 2026 | https://budgetlab.yale.edu/research/tracking-impact-ai-labor-market | Dublette (in Version 19.0 / § 11.3 referenziert) |
| 37 | I | Anthropic Economic Index (Stand) — kein neuer Bericht zwischen 9. und 24. Mai 2026 | https://www.anthropic.com/economic-index | verworfen (keine Bewegung im erweiterten Fenster) |

### Eingearbeitete Änderungen

| # | Stelle (§) | Art | Inhalt in einem Satz | Quelle # |
|---|-----------|-----|----------------------|----------|
| 1 | § 4.4 | Aktualisierung | Trilog-Block aktualisiert: Stand 28. April 2026 (zweite Runde ohne Einigung) als zeitlich frühere Referenz erhalten, ergänzt um die in der Nacht zum 7. Mai 2026 erzielte vorläufige politische Einigung mit Machinery-Regulation-Umstufung von Sektion A nach Sektion B des Anhang I, neuem Artikel 2 (13), neuem Artikel-5-Verbot (KI-CSAM/NCII) und Übergangsregelung zu Artikel 50 (2) (Stichtag 2. August 2026 für Neusysteme, Übergangsfrist bis 2. Dezember 2026 für Bestandssysteme). | 1–8 |
| 2 | § 1.1 | Ergänzung | Neuer Satzkomplex nach dem Cloudflare-Block zur zweiten Mai-Hälfte 2026: Cisco (rund 4.000 Stellen am 13. Mai 2026, ~5 %, Pre-Tax-Charges bis 1 Mrd. USD), LinkedIn (rund 875 Stellen am 13. Mai 2026, ~5 % von 17.500), Meta-Vollzug am 20. Mai 2026 (rund 8.000 Stellen, Verlegung von 7.000 auf KI-Teams, Capex 2026: 115–135 Mrd. USD), Intuit am 20. Mai 2026 (rund 3.000 Stellen, 17 %, Anthropic/OpenAI-Partnerschaften, letzter Arbeitstag 31. Juli 2026), TrueUp-Tagesstand 24. Mai 2026 (142.985 / 339, rund 1.000 pro Tag, Projektion 2026: rund 370.000), Washington-Post-Relativierung vom 21. Mai 2026. | 9–22 |
| 3 | § 6.4 | Ergänzung | Neuer Block „VR China — judizielle Begrenzung KI-induzierter Entlassungen (April/Mai 2026)" als viertes Modell auf dem internationalen Spektrum (Südkorea, Italien, Polen, China); Hangzhou-Verfahren (Quality-Assurance-Supervisor, 300.000 Yuan Jahresgehalt, KI-Substitution als strategische Geschäftsentscheidung nicht als „erheblicher Wandel der objektiven Umstände") mit Begleit-Set typischer Beispiele und zusätzlichem Beijing-Fall; Querverweise zu § 2.1, § 2.3, § 4.5, § 5.1, § 6.1–§ 6.3, § 8.3, § 9.1. | 23–27 |
| 4 | § 11.3 | Aktualisierung | Bestehender Trilog-Eintrag „Europäisches Parlament / Rat der EU. (April–Mai 2026)" um die 7.-Mai-Einigung erweitert; neuer Sammelbeleg „Council of the EU / European Parliament / Bird & Bird / White & Case / Lexology / Modulos / Orrick / Inside Privacy / TechPolicy.Press" mit acht URLs. | 1–8 |
| 5 | § 11.5 | Ergänzung | Sieben neue Sammelbelege: TechCrunch / Cisco SEC-8-K / Fox Business (13./14. Mai); Bloomberg / TechRepublic / Republic World / IndMoney (13. Mai); NPR / OPB / PYMNTS (20. Mai); TechCrunch / Slashdot / KOLO TV (20./21. Mai); TrueUp / SkillSyncer (24. Mai); Washington Post (21. Mai); Caixin Global / NPR / Fortune / Bloomberg / China.org.cn (28. April – 3. Mai). | 9–27 |
| 6 | Aktualitätshinweis am Dokumentende | Aktualisierung | Schnittangabe auf „Lauf 001 vom 24. Mai 2026" geändert; Tracker-Stichdaten 6./7./8. Mai durch 24.-Mai-Stand ersetzt; EU-Einigung vom 7. Mai 2026 statt der zuvor referierten „nächsten Trilogrunde 13. Mai 2026" eingetragen; Cisco/LinkedIn/Meta/Intuit-Layoffs und Washington-Post-21.-Mai-Analyse aufgenommen; Hangzhou-Urteil als neuer Punkt angefügt. | 1–27 |
| 7 | README.md | Aktualisierung | Versionssprung 22.0 → 23.0 (Versionszeile, Zitiervorschlag, neuer Versions-Eintrag in der KI-Offenlegung mit den drei Hauptkomplexen Digital Omnibus on AI / Tech-Layoff-Welle Mai 2/ Hangzhou-Urteil). | — |
| 8 | Validierung-Ergebnisse.md | Ergänzung | Neuer Validierungsblock „Validierung 24. Mai 2026 (Lauf 001 vom 24. Mai 2026) — Version 22.0 → Version 23.0" mit Prüftabelle 2.1.1 – 2.6 und Abschluss „alle Fehler behoben: Ja". | — |

### Verworfene Treffer (mit Begründung)

| # | Quelle | Cluster | Begründung |
|---|--------|---------|------------|
| 1 | YouGov-Umfrage UK (5. Mai 2026, 47 % AI-Steuer-Unterstützung) | B | Außerhalb Catch-up-Fenster; Quellenniveau Meinungsumfrage; in einem späteren Lauf zu erwägen, sollte Treasury-Reaktion oder Folgestudie erscheinen. |
| 2 | HMRC-Quantexa-Vertrag (14. Mai 2026, 175 Mio. £) | B | Bezieht sich auf KI-Einsatz in der Steuerverwaltung, nicht auf KI-Besteuerung; außerhalb Geltungsbereich des Arbeitspapiers. |
| 3 | Connecticut SB 5 — Lamont-Unterzeichnung | B | Stichtag 24. Mai 2026 in offen zugänglichen Quellen weiterhin nicht mit Datum dokumentiert; bestehender § 4.5-Block bleibt korrekt; nächster Lauf zu prüfen. |
| 4 | Bundesrat 1065. Sitzung 8. Mai 2026 / GKV-Beitragssatzstabilisierungsgesetz | B/G | Direktrecherche der Bundesrat-Sitzungsübersicht ergab, dass das Dossier nicht auf der Tagesordnung stand; in der Vorlauf-Version (Lauf 001 vom 8. Mai 2026) als „nächster Lauf" vorgemerkt. Verbleibt offen, bis Bundesrats-Stellungnahme oder Bundestags-Erste-Lesung mit Datum belegt ist. |
| 5 | Bungie-Layoff (21. Mai 2026, Destiny-2-Entwicklung) | F | Unter Schwelle 500+ Stellen für Einzel-Layoff-Eintrag in § 1.1; Aggregat-Linie über TrueUp/Challenger abgedeckt. |
| 6 | Microsoft VRSAR — Acceptance-Update | F | Keine Aggregat-Zahlen über die in Version 18.0 dokumentierten Programmkonditionen hinaus; nach 8. Juni 2026 (Annahmefrist) erneut zu prüfen. |
| 7 | Korinek/Lockwood Public Finance in the Age of AI | A | Dublette (in Version 9.0 referenziert). |
| 8 | Hamilton Project / Acemoglu, Autor, Johnson, *Building Pro-Worker AI* | A | Dublette (in Version 16.0 referenziert). |
| 9 | Yale Budget Lab — Tracking Impact of AI on Labor Market, März-CPS-Update April 2026 | A/F | Dublette (in Version 19.0 referenziert). |
| 10 | Anthropic Economic Index — neuer Bericht | I | Keine Bewegung im erweiterten Fenster (9.–24. Mai 2026); bestehender § 3.5-Block bleibt aktuell. |
| 11 | Frontier-Modelle / Inferenzpreise (Cluster I) | I | Keine Tagesmeldung mit politisch-fiskalischer Implikation im 48-Stunden-Fenster. |
| 12 | Tesla Optimus / Figure / Boston Dynamics / Unitree (Cluster J) | J | Keine Tagesmeldung mit politisch-fiskalischer Implikation im 48-Stunden-Fenster. |
| 13 | G-BA / gematik / BfArM / DiGAV (Cluster G) | G | Fünftes Mal in Folge ohne KI-spezifische neue Beschlüsse oder DiGA-Listings im 7-Tage-Fenster. |
| 14 | Plattform-Digitalabgabe (Weimer) | B | Keine Bewegung über Version 10.0/11.0 hinaus im Catch-up-Fenster; Eckpunktepapier weiterhin angekündigt, aber nicht vorgelegt. |
| 15 | Stanford HAI AI Index 2026 (13. April 2026) | A | Außerhalb 7-Tage- und Catch-up-Fenster. |
| 16 | ITIF / ScienceDirect / SSRN South-Korea-Robot-Tax-Empirie (Februar 2026) | C | Außerhalb Catch-up-Fenster; bestehender § 6.1-Block bleibt korrekt. |

### Verarbeitungsschritte

- Recherche abgeschlossen: Ja
- Deduplikation gegen Hauptdokument: Ja (Korinek/Lockwood, Hamilton-Project, Yale Budget Lab, Stanford HAI als bereits referenziert identifiziert)
- Validierung gemäß `Validierung.md` ausgeführt: Ja (Block „Validierung 24. Mai 2026 (Lauf 001 vom 24. Mai 2026) — Version 22.0 → Version 23.0" in `Validierung-Ergebnisse.md`)
- PDF erstellt (`build_pdf.py`): Ja
- Word erstellt (`build_docx.py`): Ja
- Versionsnummer in Hauptdokument, README, Validierung-Ergebnisse aktualisiert: Ja
- Branch auf main gemerged und gelöscht: erfolgt am Ende dieses Laufs
- E-Mail-Versand (Phase 5b): siehe „Auffälligkeiten / offene Punkte"
- WhatsApp-Versand (Phase 5b): siehe „Auffälligkeiten / offene Punkte"

### Auffälligkeiten / offene Punkte

- Lauf 001 vom 24. Mai 2026 ist der erste Daily-Update-Lauf nach 16-tägiger Pause (letzter regulärer Lauf 001 vom 8. Mai 2026). Aufgrund der Pause wurde ein erweitertes Catch-up-Fenster bis 9. Mai 2026 zugelassen, um zwei Hochrelevanz-Items aufzunehmen, die im Lauf 001 vom 8. Mai 2026 nicht erfasst wurden: (a) die EU Digital Omnibus on AI Einigung vom 7. Mai 2026 (in der Nacht zum 7. Mai 2026, also vor dem ursprünglich angesetzten Folgetermin am 13. Mai 2026 — der Lauf 001 vom 8. Mai 2026 lag damit unmittelbar nach der Einigung, hatte sie aber noch nicht aufgenommen) und (b) die chinesischen Gerichtsurteile vom 28. April / Anfang Mai 2026.
- Die EU Digital Omnibus on AI Einigung schließt einen seit Version 16.0 wiederholt referierten Trilog-Verlauf ab. Der zentrale Streitpunkt (Konformitätsbewertungs-Architektur für Anhang I) wurde durch eine Umstufung der Machinery Regulation von Sektion A nach Sektion B gelöst. Damit ist die Definitions- und Klassifikationsbasis des AI Act jetzt mit konkreten Stichtagen unterlegt — eine in § 4.4 thesenartig formulierte „mittelfristige Anknüpfung steuerlicher Tatbestände an AI-Act-Kategorien" wird dadurch verlässlicher.
- Das Hangzhou-Urteil eröffnet ein systematisch neues Politikfeld auf dem in § 6 (Internationale Praxis) dargestellten Spektrum: Während US-bundesstaatliche Initiativen (Connecticut WARN-AI-Disclosure, § 4.5) die Kausalitätsmessung auf der Aggregat-Ebene adressieren und Wertschöpfungsabgabe-/Staatsfonds-Vorschläge (§ 5.1, § 8.3) auf der fiskalischen Ebene, verlagert China die Frage auf die Einzelarbeitsvertragsebene — judizielle Begrenzung statt fiskalischer Abschöpfung. Beobachtung in den kommenden Läufen, ob (i) weitere chinesische Untergerichte dem Hangzhou-Muster folgen und (ii) das chinesische Arbeitsministerium (MOHRSS) die im Januar 2026 angekündigte dedizierte KI-Arbeitsmarkt-Policy formal veröffentlicht.
- Die Meta-Vollzugsmeldung vom 20. Mai 2026 dokumentiert erstmals explizit den Mechanismus „AI-finanzierungsinduzierter Stellenabbau" aus Konzernsicht (Zuckerberg-interne Kommunikation: „Capex statt Personal", nicht algorithmische Substitution). Für die in § 8.3 (Teilhabefonds) und § 5.1 (Wertschöpfungsabgabe) entwickelte Anknüpfung an Maschinenkapital ist das ein qualitatives Argument, das die in § 1.1 dokumentierte Asymmetrie-Linie zwischen Personalreduktion und Infrastrukturausbau weiter schärft.
- Cluster G (Gesundheitswesen) fünftes Mal in Folge ohne valide Treffer im 7-Tage-Fenster; Empfehlung für die nächsten Läufe weiterhin bestehend (gezielter Abruf von g-ba.de Sitzungsergebnissen, gematik-Pressemitteilungen, BfArM-Listings, BMG-Tabellen GKV).
- Cluster I (Frontier-Modelle) und Cluster J (Robotik) im 48-Stunden-Fenster ohne politisch-fiskalisch relevante Tagesmeldungen; Beobachtung beim nächsten Lauf fortsetzen.
- Connecticut SB 5 — Lamont-Unterzeichnung bleibt nach inzwischen drei Läufen (vom 8. Mai 2026, 14. Mai 2026 Sekundärberichterstattung, 24. Mai 2026) ohne präzises Unterzeichnungsdatum dokumentiert; Kanzleianalysen (Davis Wright Tremaine, Littler, DLA Piper, Inside Global Tech, Freshfields) sprechen weiter von „expected to be signed" bzw. „passed and awaiting governor's signature". In einem späteren Lauf nachzutragen, sobald die formale Unterzeichnung mit Datum belegt ist.
- GKV-Beitragssatzstabilisierungsgesetz — die Bundesrat-Tagesordnung der 1065. Sitzung am 8. Mai 2026 weist das Dossier nicht als Beratungsgegenstand aus; der im Vorlauf-Lauf 001 vom 8. Mai 2026 erwartete Erstdurchgang hat in dieser Sitzung nicht stattgefunden. Bestehender Aktualitätshinweis bleibt korrekt; verbleibt offen, bis Bundesrats-Stellungnahme oder Bundestags-Erste-Lesung mit Datum belegt ist (geplant: vor Sommerpause 2026).
- Branch dieses Laufs: `claude/determined-einstein-vfRdL` (in Phase 0 verifiziert; nach Phase-6-Commit lokal und im Remote vorhanden — Push auf den Session-Branch erfolgreich).
- Phase 5b: Routine-Anweisung mit `email_to=…` und `whatsapp_to=…` aus dem Aufruf übernommen; Empfängerdaten werden in diesem Logbuch, in Commits, im Abschlussbericht oder in einer anderen versionierten Datei nicht ausgeschrieben. Der Versand-Tool-Status wurde in Phase 5b geprüft: In dieser Session standen weder `mail_send` / `send_mail` / `send_message` / `outlook_send` aus `graph-mcp` noch `wa_send_message` / `send_message` aus einem `whatsapp`-MCP zur Verfügung; die vorbereiteten Inhalte wurden daher gemäß Phase-5b-Spezifikation als Fallback in die gitignored Dateien `daily-mail.txt` und `daily-whatsapp.txt` im Repo-Root geschrieben (Dateien stehen in `.gitignore`, werden also nicht versioniert).
- Phase 6: Merge auf `main` lokal mit `--no-ff` durchgeführt; Push des `main`-Branches auf das Remote scheiterte mit HTTP 403 nach vier Backoff-Versuchen (2 s, 4 s, 8 s, 16 s) — derselbe Befund wie in Lauf 003 vom 7. Mai 2026 (Berechtigungsbarriere des Hosting-Endpoints, kein transientes Netzwerkproblem). Der Session-Branch ist auf dem Remote vollständig verfügbar und enthält alle Änderungen; der `main`-Merge ist lokal vollständig durchgeführt und kann beim nächsten Lauf bzw. durch einen autorisierten Push direkt auf `main` nachgezogen werden. Lokaler Session-Branch und Remote-Session-Branch werden für diesen Lauf nicht gelöscht, damit der nicht gepushte `main`-Merge im Folgelauf prüfbar bleibt.

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
