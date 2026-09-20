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

---

## Lauf 2 — 19.09.2026, nach Sitzung B

**Anlass:** Zweite Erhebung abgeschlossen (150 Aufrufe, 0 Ausfälle, 6 h 16 min). Zentraltabelle, Teil 0 und Teil 1 tragen neue Werte.
**Umfang:** Standardlauf. Kernzahlen nach Prüfprofil § 2 über alle betroffenen Dokumente, dazu die neuen Größen aus Sitzung B.

### Befunde

| # | Schwere | Ort | Beschreibung | Behandlung |
|---|---|---|---|---|
| 1 | Mittel | `18-Strategiepapier-2031.md` § 5b | Zentraltabelle trug noch +102.065 / +187.714 aus der ersten Erhebung, ohne Kennzeichnung als Vorwert | behoben: beide Erhebungen nebeneinander, Runde 3 als geltender Wert |

Keine weiteren Abweichungen. Die Werte der ersten Erhebung stehen an allen übrigen Fundstellen ausdrücklich als Vorwerte.

### Neue Kernzahlen im Prüfprofil nachzutragen

| Größe | Sollwert nach Sitzung B | Steht in |
|---|---|---|
| Personalbedarf 2031 mit KI | +123.684 | 18, 23, 25 |
| dasselbe ohne KI | +201.717 | 18, 23, 25 |
| KI-Beitrag | rund 78.000 | 18, 23, 25 |
| Divergenzerhalt | 6 von 6, niedrigster Wert 0,81 | 13, 17, 18, 22, 25 |
| Einwandhaltbarkeit | 100 % | 13, 22, 25 |
| Fremdbezug | 8 % | 13, 22, 25 |

Unverändert: Basis 2.155.154 VZÄ, Deckung 48,9 %.

### Inhaltliche Prüfung

**Zurückgezogene Maße (bekanntes Fehlermuster 1).** Ein drittes Maß ist in diesem Lauf zurückgezogen worden: die Modellabhängigkeit der Runde 3. Alle Fundstellen geprüft — `13`, `22` und `25` führen sie als zurückgezogen, `17` bezieht sich ausschließlich auf Sitzung A und bleibt gültig.

**Konjunktivregel.** Stichprobe in `23` und `25`: eingehalten. Die Sitzungsbefunde selbst (Aufrufzahlen, Gütemaße, Laufzeit) stehen korrekt im Indikativ.

**Nicht geprüft.** Die 32 Dissenspunkte und 60 Kartenzüge im Einzelnen auf sachliche Richtigkeit. Die Rechenwege der zweiten Erhebung — eine Validierungsrunde ist für Runde 3 nicht vorgesehen und hat nicht stattgefunden.

### Ergebnis

Ein Befund behoben. Nachprüfung bestanden: Skriptlauf ohne neue Befunde, Kernzahlen-Abgleich ohne Abweichung. Der Satz umfasst jetzt elf Dokumente und bleibt widerspruchsfrei.

---

## Lauf 3 — 20.09.2026, nach Sitzung C

**Anlass:** Sitzung C abgeschlossen (120 Aufrufe, 0 Ausfälle). Zwei neue Dokumente, drei korrigierte. Erstmals hat der Lauf selbst eine Verifikation der bereits geschriebenen Teile enthalten.

### Mechanische Prüfung

`validate_doc.py --skip refs` über die geänderten und neuen Dokumente: `27`, `24` ohne Befund; `22`, `23` nur Hinweise (durchgestrichene Einträge, absichtlich als Korrekturspur stehengelassen). In `26` acht Befunde der Kategorie Nummerierung — sämtlich **Fehlalarme**: Das Dokument nummeriert je Kapitel neu, der Prüfer liest die Datei flach. Nicht behoben, begründet stehengelassen.

`pruefe-konzept.py`: keine Befunde.

### Kernzahlen-Abgleich

Neu aufgenommen ins Prüfprofil: Abbruchkriterien **24** statt 23, KI-Beitrag als **Spanne 50.600 bis 105.400**, Deckung als **Obergrenze 48,9 % mit unterer Grenze 44,3 %**, Aufrufe Sitzung C 120.

Ein Selbstwiderspruch gefunden und behoben: `13` führte die Bezugsgrößendeckung in derselben Tabellenzeile als »erneut gerissen« und schloss mit »und die ist erfüllt«. Das ist dasselbe Muster wie der Befund aus Lauf 2 (`17` § 3.4) — ein Satz, der bei einer Korrektur nicht mitgezogen wurde.

Das Zahlwort im Fließtext von `13` stand auf »Dreiundzwanzig« und ist auf »Vierundzwanzig« nachgezogen. Das Prüfskript hat es nicht gemeldet, weil seine Zahlwortliste bei siebzehn endet — eine Lücke des Prüfers, kein Zufall: Sie wächst mit jedem neuen Kriterium.

### Inhaltliche Prüfung

**Die Verifikation des Laufs hat 36 harte Befunde gegen `22`, `23` und `24` erhoben.** Jeder prüfbare ist gegen die Rohdaten nachgerechnet und **bestätigt** worden. Das dominierende Muster: `23` führte über weite Strecken Werte der ersten Erhebung, obwohl der Kopf die Fassung nach der zweiten auswies. Alle betroffenen Stellen sind korrigiert und als Korrektur gekennzeichnet — Einzelheiten in `27-Sitzung-C.md` § 5.

**Ein Befund ist von anderer Art als alle bisherigen.** In `24` stand ein Satz ohne jede Grundlage: vier Rollen seien vom vorgegebenen Vergleichsrahmen abgewichen. Gegen die Rohdaten nannten alle achtzehn zuständigen Rollen einen der fünf vorgegebenen Staaten. Das ist kein Übertragungs- und kein Aktualitätsfehler, sondern eine Erfindung. Sie ist gestrichen.

**Neues Fehlermuster für § 6 des Prüfprofils.** *Aktualitätsverlust bei mehreren vorliegenden Ständen:* Liegen zu derselben Größe ein älterer ausführlicher und ein neuerer knapper Stand vor, wird der ältere verwendet — unabhängig davon, welcher als maßgeblich gekennzeichnet ist. Dreimal in diesem Lauf aufgetreten: in der Hebelableitung, in `23` und in `22`. Gegenmittel: Der neuere Stand muss die Bewegung und ihre Begründung mitführen, nicht nur den Wert.

**Konjunktivregel.** Drei Indikative in `23` über Modellergebnisse für 2031 gefunden und behoben, darunter der Satz, der die Kernaussage des Teils trägt.

**Nicht geprüft.** Die 800 Hebel- und 259 Profilurteile im Einzelnen. Die Zuschnittfrage zu A06, A09 und H06 — sie ist als offen ausgewiesen und begrenzt die Deckung nach unten auf 44,3 %.

### Ergebnis

Zwölf Befunde behoben, einer davon eine Erfindung, einer ein Selbstwiderspruch. Nachprüfung bestanden: Skriptläufe ohne neue Befunde, Kernzahlen-Abgleich ohne Abweichung. Der Satz umfasst jetzt **dreizehn Dokumente** und bleibt widerspruchsfrei.

**Die Abschlussregel (`18-Strategiepapier-2031.md` § 7a) ist damit erfüllt**, mit einer benannten Ausnahme: Bedingung 5 — keine offene Korrektur — gilt nur, weil die offene Zuschnittfrage ausdrücklich als offen ausgewiesen ist, wie es die Regel zulässt.
