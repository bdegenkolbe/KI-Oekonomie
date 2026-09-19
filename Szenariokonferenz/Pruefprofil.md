# Prüfprofil — Dokumentensatz Szenariokonferenz

*Dokumentspezifische Konkretisierung des generischen Prüfkatalogs (Skill `dokument-validierung`). Angelegt bei der Erstvalidierung am 19.09.2026.*

## 1. Prüfgegenstand

Kein Einzeldokument, sondern ein **Satz von zehn zusammenhängenden Dokumenten** plus Rohdaten und Prüfskripte. Die Besonderheit dieses Satzes: Die Dokumente berichten **dieselben Kennzahlen mehrfach**, und die Zahlen ändern sich, wenn ein Fehler gefunden wird. Der wichtigste Prüfschritt ist deshalb die dokumentübergreifende Zahlenkonsistenz, nicht die Binnenstruktur.

| Dokument | Funktion | Ändert sich, wenn … |
|---|---|---|
| `11-Konzept-v2.md` | Verfahrensbeschreibung, Sollzustand | eine Regel ergänzt oder korrigiert wird |
| `13-Validierungsstand.md` | Abbruchkriterien und Stand | ein Kriterium hinzukommt, reißt oder zurückgezogen wird |
| `17-Sitzung-A.md` | Auswertung des ersten Laufs | Gütemaße neu berechnet werden |
| `18-Strategiepapier-2031.md` | Zielprodukt, Füllstand, Nacharbeitsplan | ein Teil geschrieben oder eine Zahl korrigiert wird |
| `19-Falsifikatoren.md`, `20-Durchgriffskanaele.md` | erzeugte Register | `extrahiere-register.py` neu läuft |
| `21-Quellenpruefung.md` | Prüfung der Recherchebank | ein neuer Prüflauf stattfindet |
| `22-Teil-0-Gueltigkeit.md` | Teil 0 des Papiers | ein Gütemaß sich ändert |
| `23-Teil-1-Deutschland.md`, `24-Teil-2-Europa.md` | Teil 1 und 2 des Papiers | die Zentraltabelle sich ändert |

## 2. Kernzahlen — bei jeder Änderung in allen Dokumenten nachziehen

| Größe | Sollwert 19.09.2026 | Steht in |
|---|---|---|
| Basis der Zentraltabelle | 2.155.154 VZÄ | 13, 18, 22, 23 |
| Deckung des Rahmens | 48,9 % | 11, 13, 17, 18, 22, 23 |
| Personalbedarf 2031 mit KI | +102.065 | 18, 23 |
| dasselbe ohne KI | +187.714 | 18, 23 |
| KI-Beitrag | rund 86.000 | 18, 23 |
| Prüfschärfe bereinigt | 97 % | 11, 17, 22, 23 |
| Rechenweghaltbarkeit bereinigt | 94,2 % | 17, 22 |
| Aufrufe Sitzung A | 223 | 11, 13, 17, 18, 22 |
| unabhängige Durchgriffskanäle | 43 von 59 | 11, 19, 20, 22, 23 |
| datierte Falsifikatoren | 92 von 100 | 17, 18, 19, 22, 23 |
| Abbruchkriterien | 23 | 13 (Tabelle **und** Zahlwort im Fließtext) |

## 3. Terminologie — festgelegt, nicht verhandelbar

**Pflichtgrößen** P1, P2, P3, P3₀, P4, P5 · **Marktgrößen** A1 bis A3 · **europäische Vergleichsgrößen** E1 bis E3 · **Durchgriff D** · **Bezugsgröße** (die VZÄ-Zahl) gegen **Bezugsgruppe** (die Menschen) · **Gerüst** (Szenariorahmen) gegen **Anker** (Fragereihenfolge) · **Bank** (Rollengruppe) gegen **Feld** (eine Rolle und ihr Gegenstand).

Nicht mischen: **Arbeitszeit** (P1, P2) und **Personalbedarf** (P3). Die Verwechslung ist der häufigste inhaltliche Fehler dieses Satzes.

## 4. Konjunktivregel

`Claude.md` § 4.2: Modellergebnisse, Gesetzentwürfe und alle Aussagen über 2031 stehen im Konjunktiv. Betrifft vor allem `22`, `23` und `24`. **Nicht** im Konjunktiv stehen: gemessene Gütemaße, Aufrufzahlen, Laufzeiten und alle Aussagen über das Verfahren selbst — das sind Tatsachen über einen durchgeführten Lauf.

## 5. Redundanz — beabsichtigt und unbeabsichtigt

Beabsichtigt: `17` berichtet die Gütemaße vollständig, `22` wiederholt sie in Leserform mit Einschränkungen. Beabsichtigt: `18` § 5b fasst die Zentraltabelle zusammen, `23` § 2 führt sie aus.

Unbeabsichtigt wäre: dieselbe Zahl mit unterschiedlichem Wert, oder eine Bewertung in `17`, die `22` nicht kennt.

## 6. Bekannte Fehlermuster

1. **Zurückgezogene Maße bleiben irgendwo stehen.** Die Attributionskonsistenz wurde in drei Dokumenten geführt; nach dem Rückzug stand sie in `17` § 3.4 noch als erfüllt. Bei jedem Rückzug alle Fundstellen durchsuchen.
2. **Zahlen aus einer verworfenen Fassung.** Nach der Zuschnittkorrektur standen 73,6 % noch in `11` und `18` als geltender Wert.
3. **Zählwörter im Fließtext.** »Dreiundzwanzig Abbruchkriterien« gegen die Tabellenlänge.
4. **Abgehakte Aufgabenlisten.** Durchgestrichene To-do-Punkte sind Dokumenthistorie und gehören ersetzt durch eine Aussage über den aktuellen Stand.
5. **Mandatsreichweite als Bezugsgruppe.** Der inhaltlich teuerste Fehler des Satzes, zweimal aufgetreten.

## 7. Bekannte Fehlalarme des Prüfskripts

- **Tabellenspalten bei escapten Pipes.** Zeilen mit `\|` in Formeln (`|P3 − P3₀|`) werden als zusätzliche Spalten gezählt. Betrifft `11` Zeile 387 und `13` Zeile 84. Kein Dokumentfehler.
- **Querverweise.** Die Dokumente verweisen mit `§X` auf Abschnitte *anderer* Dokumente. Der Querverweis-Check ist deshalb mit `--skip refs` zu fahren.
- **Durchstreichungen als Dokumenthistorie.** Ein zurückgezogenes Kriterium oder eine als fehlspezifiziert markierte Schwelle ist aktueller Stand, keine Historie, und bleibt stehen.

## 8. Export

Kein Export definiert. Der Satz lebt als Markdown im Repository; das Arbeitspapier `KI-Ökonomie.md` hat seine eigene Bau-Kette (`build_docx.py`, `build_pdf.py`) und ist nicht Teil dieses Profils.

## 9. Prüfumfang

- **Schnellprüfung** nach einer Textänderung in einem Dokument: Skriptlauf mit `--skip refs` plus Kernzahlen-Abgleich aus § 2.
- **Standardlauf** nach jeder Korrektur eines Befundes: zusätzlich alle Fundstellen der geänderten Zahl in allen zehn Dokumenten.
- **Vollvalidierung** vor einer Weitergabe außer Haus: zusätzlich Quellenprüfung der Register gegen die Rohdaten und Konjunktivdurchsicht von `22` bis `24`.
