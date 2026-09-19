# Prüfprotokoll — Dokumentensatz Szenariokonferenz

*Fortlaufend. Ältere Läufe bleiben stehen.*

---

## Lauf 1 — 19.09.2026, Erstvalidierung

**Anlass:** Nachvalidierung nach drei Korrekturrunden (Zuschnitt der Bezugsgrößen, Quellenunabhängigkeit, zirkuläres Gütemaß).
**Umfang:** Standardlauf über zehn Dokumente. Prüfprofil bei diesem Lauf erstmals erzeugt.
**Werkzeug:** `validate_doc.py --skip refs`, dazu ein dokumentübergreifender Kernzahlen-Abgleich.

### Maschinelle Prüfung

| Dokument | Befunde | Hinweise |
|---|---|---|
| 11-Konzept-v2 | 1 (Fehlalarm) | 0 |
| 13-Validierungsstand | 1 (Fehlalarm) | 2 |
| 17-Sitzung-A | 0 | 4 |
| 18, 19, 20, 21, 23, 24 | 0 | 0 |
| 22-Teil-0 | 0 | 1 |

### Befunde

| # | Schwere | Ort | Beschreibung | Behandlung |
|---|---|---|---|---|
| 1 | **Kritisch** | `17-Sitzung-A.md` § 3.4 | Die Attributionskonsistenz wurde dort weiter als „unabhängig gemessen und erfüllt" geführt, obwohl sie in § 2 und § 3.3a desselben Dokuments als zirkulär zurückgezogen ist. Direkter Selbstwiderspruch. | behoben: Satz umgeschrieben, Verweis auf § 2 ergänzt |
| 2 | Mittel | `11-Konzept-v2.md` § 5 Runde 0a | Deckung der Bezugsgrößen mit 73,6 % angegeben — Wert aus der Fassung vor der Zuschnittkorrektur | behoben: 48,9 % mit Verweis |
| 3 | Mittel | `18-Strategiepapier-2031.md` § 5b | »Maßgeblich bleibt die Deckung, und die ist mit 73,6 % erfüllt« — widersprach § 5c desselben Dokuments, wo das Kriterium als gerissen geführt wird | behoben: 48,9 %, Kriterium als gerissen ausgewiesen |
| 4 | Gering | `17-Sitzung-A.md` § 6 | Abgehakte Aufgabenliste mit vier Durchstreichungen — Dokumenthistorie im Hauptdokument (Katalog 2.5) | behoben: ersetzt durch Aussage über Erledigtes und Offenes |
| 5 | — | `11` Z. 387, `13` Z. 84 | Tabellen-Spaltenzahl beanstandet | **Fehlalarm**: escapte senkrechte Striche in den Betragsformeln werden vom Skript als Spaltentrenner gezählt. Ins Prüfprofil § 7 aufgenommen |
| 6 | — | `13` Z. 92/96, `17` Z. 25, `22` Z. 25 | Durchstreichungen als Dokumenthistorie gemeldet | **kein Fehler**: Ein zurückgezogenes Kriterium und eine als fehlspezifiziert markierte Schwelle sind aktueller Stand und müssen sichtbar bleiben, damit sie nicht wieder eingeführt werden |

### Inhaltliche Prüfung

**Kernzahlen (Katalog 2.1).** Alle elf Kernzahlen aus Prüfprofil § 2 in allen Dokumenten geprüft, in denen sie vorkommen. Nach Behebung der Befunde 2 und 3 **keine Abweichung**. Die Zählwortprobe (»Dreiundzwanzig Abbruchkriterien« gegen 23 Tabellenzeilen) geht auf.

**Ausgewogenheit (Katalog 2.4).** Erfüllt, und zwar ungewöhnlich weitgehend: Der Satz führt eigene Fehler mit Ursache und Größenordnung, weist zwei gerissene Kriterien aus, zieht ein eigenes Gütemaß zurück und kennzeichnet interessengestützte Quellen. Modellrechnungen sind durchgängig als solche benannt.

**Konjunktivregel (Katalog 3, Prüfprofil § 4).** Stichprobe in `22`, `23`, `24`: eingehalten. Aussagen über 2031 stehen im Konjunktiv, gemessene Verfahrensgrößen im Indikativ — die Abgrenzung ist konsistent.

**Redundanz (Katalog 2.2).** Die Doppelungen zwischen `17` und `22` sowie zwischen `18` § 5b und `23` § 2 sind beabsichtigt und im Prüfprofil § 5 dokumentiert; Tiefe und Adressat unterscheiden sich.

**Quellen (Katalog 4).** Die Register `19` und `20` sind aus `rohdaten/sitzung-a.json` erzeugt und gegen die Rohdaten reproduzierbar. Externe URL-Prüfung nicht durchgeführt — die Dokumente enthalten keine URLs; die Quellen liegen in den Rohdaten und wurden im eigenen Lauf `21-Quellenpruefung.md` geprüft (140 Kennzahlen, keine nicht existierende Quelle).

**Nicht geprüft.** Die Rechenwege von P1 und P2 der 84 Felder außerhalb der Zentraltabelle im Einzelnen. Die inhaltliche Richtigkeit der 43 unabhängigen Normzitate — ein Plausibilitätsscan auf nicht existierende Paragrafennummern war ohne Befund, nachdem ein Fehlalarm zu § 380 SGB V aufgeklärt war (SGB V reicht seit den Telematik-Paragrafen bis § 383).

### Ergebnis

Vier Befunde behoben, zwei als Fehlalarm des Prüfskripts dokumentiert. Nachprüfung der betroffenen Schritte bestanden: Skriptlauf ohne neue Befunde, Kernzahlen-Abgleich ohne Abweichung.

**Der Satz ist in sich widerspruchsfrei.** Was er behauptet, ist damit nicht belegt — die Gültigkeitsgrenzen stehen in `22-Teil-0-Gueltigkeit.md` und sind erheblich.
