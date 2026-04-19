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
| 2.4.4 URL-Prüfung (Stichprobe) | n/a | Ohne Webzugriff in dieser Validierung nicht ausführbar; bei nächster Validierung mit verfügbarem Webzugriff durchzuführen. |
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
- PDF erstellt: Nein (kein Build-Skript / pandoc-Lauf in dieser Validierung; bei nächster Iteration mit verfügbarer Toolchain nachzuholen)
- Word erstellt: Nein (siehe oben)

**Hinweis:** Die Exporte (PDF/Word) konnten in dieser Validierungsrunde nicht erzeugt werden, da im Projekt noch keine dedizierten Build-Skripte und keine geprüfte pandoc/xelatex-Konfiguration vorliegen. Die inhaltliche Validierung gilt damit als abgeschlossen; der Exportschritt ist als offener Punkt für die nächste Validierung dokumentiert.
