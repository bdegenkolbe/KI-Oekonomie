# Strategiepapier 2031 — Gerüst und Füllstand

*Was am Ende herauskommen soll, woraus jeder Abschnitt gefüllt wird, und der eine Befund, der das Papier heute verhindert.*

---

## 1. Warum dieses Dokument

Das Verfahren ist bis auf die einzelne Karte beschrieben (`11-Konzept-v2.md`), die Besetzung steht (`14-Roster-2031.md`), die Mechanik ist einmal durchgelaufen (`15-Mechanikprobe.md`), die Abbruchkriterien sind vorab festgelegt (`13-Validierungsstand.md`). Das **Produkt** ist an keiner Stelle festgelegt — es steht als Runde 6 am Ende einer Ablaufbeschreibung und sonst nirgends.

Das ist die Stelle, an der Verfahren dieser Art scheitern: Sie erzeugen einen Methodenbericht und nennen ihn Ergebnis. Dieses Dokument legt deshalb den Zielzustand fest, ordnet jedem Abschnitt seine Quelle zu und weist aus, was heute füllbar ist und was nicht. Es ist eine Form, kein Text — der Text entsteht in Runde 6.

## 2. Der Aufbau — vier Teile

Die Reihenfolge ist bindend und folgt `11-Konzept-v2.md` § 5, Runde 6.

| Teil | Gegenstand | Rückgrat | Gefüllt aus | Stand |
|---|---|---|---|---|
| **0 Gültigkeit** | wie weit die Zahlen tragen | Prüfschärfe, Modellabhängigkeit, Gerüstabhängigkeit, Attributionskonsistenz, Abdeckung und Rest der Zerlegung, Ausfälle | Sitzung A, Runde 1b | **füllbar** |
| **1 Deutschland und Gesundheitswesen** | was bis 2031 geschieht | P3-Summe in Vollkräften, daneben P1 × P2 und D, daneben die P4-Zerlegung | Runde 1 und 3 | **blockiert**, § 4 |
| **2 Europa** | wo Deutschland steht | E1 Abstand in Jahren, E2 EU-Anteil, E3 Regelungslücke | Sitzung A, Bänke K/L/M | teilweise |
| **3 Hebel** | was man tun könnte | fünf bis acht Hebel mit Urteilsmuster, Kippbedingung und Red-Team-Einwand | Sitzung C, Runde 4 und 5 | offen |

Gültigkeit steht vorn, nicht im Anhang. Das ist die Lehre aus dem ersten Lauf, dessen Kernzahl sich nachträglich als Modellvorannahme herausstellte.

## 3. Was Sitzung A für Teil 0 und Teil 1 schon liefert

Aus den 110 vorliegenden Rollenantworten der Runde 1, Stand 19.09.2026. **Erstwerte vor jeder Diskussion** — Runde 3 erhebt dieselben Größen erneut, und erst die Bewegung zwischen beiden ist das Ergebnis.

| Größe | Median | Q1–Q3 |
|---|---|---|
| P1 technisch ersetzbare Arbeitszeit | 41,5 % | 31–49 |
| P2 davon bis 2031 wirksam | 40 % | 32–45 |
| P3 Personalbedarf 2031 | +3 % | −4 bis +12 |
| P3₀ derselbe ohne KI | +10,5 % | +6 bis +20 |
| D Durchgriff | 0,45 | 0,4–0,8 |

Gelesen als Satz, den Teil 1 tragen müsste: Technisch ersetzbar wäre gut ein Drittel bis die Hälfte der Arbeitszeit; real frei würden davon rund 40 %, also etwa ein Sechstel der Arbeitszeit; davon erreichte weniger als die Hälfte den Personalbedarf. Netto bliebe ein **steigender** Bedarf (+3 %), nur weniger steil als ohne KI (+10,5 %). Weder Entlastung noch Freisetzung — ein gedämpfter Anstieg.

**Die Zusatzgrößen, die Teil 1 und Teil 3 tragen:**

| | Verteilung |
|---|---|
| A3 Engpass | Entscheidung 65, bedienendes Personal 25, Daten 10, Recht 9, **Technik 1** |
| P2 Hemmnis | Refinanzierung 29, Recht und Zulassung 28, Investitionsfähigkeit 27, Daten 16, Haftung 8 |
| P4 Ursachenanteile | KI 40, Strukturreform 28, Demografie 20 |
| P5 Verbleib des Gewinns | neue Leistung 30, **Abfluss ins Ausland 30**, Erbringer 27,5, Preis und Beitrag 10 |
| A2 Finanzierungstopf | Erbringerbudget 40, **gar kein Topf 30**, Fördermittel 15, Erlöstatbestand 5 |

Eine von hundert Rollen hielte die Technik für den Engpass. Das ist die tragfähigste Einzelaussage des bisherigen Laufs und zugleich die Brücke zur Deutschland-These des Arbeitspapiers: Nicht das Können fehlte, sondern die Entscheidung und der Rechnungsempfänger.

**Formaldisziplin:** P4, P5 und A2 summieren in 110 von 110 Fällen auf 100. Der Einheitenzwang trägt.

## 4. Der Befund, der Teil 1 heute verhindert

Runde 0a sollte die hundert Felder disjunkt in Vollkräfte zerlegen. Sie hat es für **sieben Felder** getan.

| | |
|---|---|
| Felder mit primärer, disjunkter Bezugsgröße | **7 von 100** |
| davon Summe | 1.843.170,5 VZÄ |
| Felder mit Bezugsgröße 0 und Zuordnung »unbekannt« | **91 von 100** |
| Rollenantworten mit `p3_absolut_vzae` = 0 | **94 von 110** |
| Rollenantworten, die die Bezugsgröße bestreiten | **95 von 110** |
| Abdeckung gegen den Kontrollrahmen von 4,4 Mio VZÄ | rund 42 % |

Die sieben Felder sind fünf Krankenhaus-Dienstarten, die stationäre und die ambulante Pflege. Der gesamte ambulante ärztliche und zahnärztliche Bereich, Psychotherapie, Apotheken, Rettungsdienst, Öffentlicher Gesundheitsdienst, Reha, Kostenträger, Selbstverwaltung, Handel und Vorleistungsindustrie haben keine Bezugsgröße.

**Die Recherche hat dabei nichts falsch gemacht.** Sie hat ausdrücklich festgehalten, dass es für diese Bereiche keine amtliche VZÄ-Zerlegung gibt, hat die Felder deshalb mit 0 und »unbekannt« belegt, den ungedeckten Rest als Größenordnung ohne Kennzahlqualität ausgewiesen und verboten, ihn als Differenz weiterzuverrechnen. Sie hat sich geweigert zu schätzen. Das ist das richtige Verhalten und der Grund, warum der Fehler überhaupt sichtbar ist.

**Das Panel hat den Fehler dann selbst protokolliert.** 95 Rollen haben die Vorgabe bestritten, mehrere mit dem zutreffenden Hinweis, dass eine Prozentveränderung gegen eine Basis von null nicht definiert ist. 52 haben ersatzweise eine eigene Bezugsgröße gesetzt und offengelegt.

**Warum das genau den Kern trifft:** Rückgrat von Teil 1 ist nach `11-Konzept-v2.md` § 5, Runde 6, »die über die `primaer`-Felder aggregierte P3-Tabelle in Vollkräften«. Diese Tabelle hätte heute sieben Zeilen und deckte 42 % der Gesundheitsbeschäftigten ab, sämtlich aus Krankenhaus und Pflege. Ein Strategiepapier zum deutschen Gesundheitswesen, dessen Zentraltabelle den ambulanten Sektor nicht enthält, ist keines.

**Was nicht beschädigt ist — und das ist der größere Teil.** Alle Größen des Verfahrens außer einer sind Verhältniszahlen und hängen nicht an der Basis: P1, P2, P3 und P3₀ als Prozentwerte, P4, P5, A1 bis A3, D, E1 bis E3. Beschädigt ist allein die **absolute Spalte** `p3_absolut_vzae` und damit die Aggregation. Sitzung A ist deshalb nicht verloren; sie ist um eine Spalte unvollständig.

**Die 18 Abbruchkriterien haben das nicht gesehen.** Sie prüfen Kartenmechanik und Zahlenherleitung — Prüfschärfe, Rechenweghaltbarkeit, Schemafestigkeit, Adressierung. Keines prüft, ob die Zentraltabelle des Zielprodukts überhaupt gebaut werden kann. Das ist als **neunzehntes Kriterium** nachzutragen (§ 7).

## 5. Die Reparatur

**Der Ansatz.** Die Zerlegung hat die Gesundheitspersonalrechnung des Statistischen Bundesamtes nur als Kontrollgröße für die Gesamtsumme verwendet (4,4 Mio VZÄ) und ihre **Einrichtungsgliederung** nicht ausgewertet. Genau diese Gliederung ist der fehlende Rahmen: Sie weist Beschäftigte und Vollzeitäquivalente nach Einrichtungsart aus — Arztpraxen, Zahnarztpraxen, Praxen sonstiger medizinischer Berufe, Apotheken, ambulante Pflege, Krankenhäuser, Vorsorge- und Rehabilitationseinrichtungen, stationäre Pflege, Rettungsdienst, Verwaltung, sonstige Einrichtungen, Vorleistungsindustrien. Die Krankenhaus- und die Pflegestatistik unterteilen dann **innerhalb** dieses Rahmens weiter, statt neben ihm zu stehen.

**Der Zuschnitt:** drei Aufrufe, geschätzt fünf USD, rund eine Viertelstunde. Nach Sitzung A, vor Sitzung B.

**Vier bindende Regeln:**

1. **Ein Rahmen, dann Unterteilung.** Die Einrichtungsgliederung der Gesundheitspersonalrechnung ist der Rahmen. Krankenhaus- und Pflegestatistik unterteilen innerhalb einer Einrichtungsart; ihre Summe darf die Einrichtungsart nicht überschreiten.
2. **Weiterhin nicht schätzen.** Ein Feld ohne amtliche Grundlage bleibt »unbekannt«. Die Reparatur zielt auf Abdeckung durch bessere Quellenwahl, nicht durch Schätzung.
3. **Stichtage und Abgrenzungen mitführen.** Die bestehende Zerlegung hat zu Recht darauf hingewiesen, dass Krankenhausstatistik (Jahresdurchschnitt), Pflegestatistik (15.12., zweijährlich) und Gesundheitspersonalrechnung (31.12.) nicht deckungsgleich sind. Jede Zeile trägt ihren Stichtag; wo Stichtage kollidieren, wird die Zeile als »geteilt« geführt und geht nicht in die Summe ein.
4. **Vollkräfte und Köpfe bleiben getrennt**, Leiharbeit bleibt ausgewiesen fehlend. Beides ist keine Lücke der Reparatur, sondern eine Grenze der amtlichen Statistik, und steht so in Teil 0.

**Die Rollen werden nicht erneut befragt.** Sobald ein Feld seine Bezugsgröße hat, ergibt sich die absolute Zahl aus dem bereits vorliegenden P3-Prozentwert mal der Bezugsgröße. Das ist eine Nachrechnung, keine Neuerhebung — 0 USD und wenige Sekunden. Nur für Felder, die auch nach der Reparatur ohne Grundlage bleiben, entfällt die absolute Zahl dauerhaft; sie erscheinen in Teil 1 mit Prozentwert und ohne Vollkräftezeile, und Teil 0 weist ihre Zahl aus.

## 6. Wie viele Rollen das Papier braucht

Aus den 110 Antworten empirisch gemessen, je 200 bis 400 zufällige Reihenfolgen.

| Was | Gesättigt ab | Zuwachs bei n = 110 |
|---|---|---|
| Mediane der Pflichtgrößen | **n ≈ 30** (Abweichung ≤ 2 Punkte), ab 50 ≤ 1 Punkt | 0,5 Punkte je 50 Rollen |
| benannte Institutionen und Datenquellen | **n ≈ 50** (27 von 31) | 0,3 je zehn Rollen |
| zitierte Rechtsnormen | **nicht gesättigt** — 354 verschiedene, 257 davon einmal genannt | **23,8 je zehn Rollen**, nahezu linear |

Das ist ein Ergebnis über das Instrument und gehört in Teil 0: Für den **Median** sind hundert Rollen dreifach überdimensioniert; für den **Durchgriffskanal** — welche Norm die Ersparnis konkret aufhält — reichen hundert nicht. Beides zusammen sagt, wozu die Bank da ist. Sie mittelt keine Schätzung, sie sammelt Kanäle. Genau das ist der Gegenstand der Deutschland-These, und das Papier kann sie damit als Liste führen statt als Behauptung.

**Folge für den Zuschnitt:** Runden, die nur Zahlen bewegen, kommen mit rund vierzig Rollen aus. Die volle Bank ist dort einzusetzen, wo Normen und Engpässe eingesammelt werden — Runde 1 und Runde 6.

## 7. Nachzutragen in `13-Validierungsstand.md`

| Kriterium | Schwelle | Was es prüft |
|---|---|---|
| **Bezugsgrößendeckung** | ≥ 60 % der hundert Felder tragen eine primäre, disjunkte Bezugsgröße, und die Summe deckt ≥ 70 % des Kontrollrahmens | ob die Zentraltabelle des Zielprodukts gebaut werden kann — sie ist das Rückgrat von Teil 1 und war in keinem der achtzehn Kriterien enthalten |

Gemessen am heutigen Stand: 7 % und 42 %. Das Kriterium ist gerissen, und zwar vor Sitzung B, also an der billigsten Stelle.

## 8. Was das Papier nicht sein wird

Unverändert aus `13-Validierungsstand.md`, Stufe 3, und hier wiederholt, weil es in Teil 0 wörtlich stehen muss: Die Agenten bleiben Sprachmodelle mit Rollendossiers. Ein Strategiepapier aus diesem Verfahren wäre ein **strukturiertes Argumentmodell mit benannten Quellen, gemessenen Gültigkeitsgrenzen und offengelegten Dissenspunkten** — keine Expertenbefragung, keine Prognose und keine Legitimationsgrundlage für eine politische Entscheidung.

Dazu zwei Regeln aus `11-Konzept-v2.md`, Runde 6, die beim Schreiben nicht verhandelbar sind: Was keine Kartennummer trägt, steht nicht im Papier. Und alle Aussagen über 2031 stehen im Konjunktiv (`Claude.md` § 4.2).

Die Zuordnung von Leistungsprofilen zu tatsächlichen Anbietern steht in `16-Marktschicht.md` und **nicht** in diesem Papier. Die Begründung dort gilt unverändert.

## 9. Stand

| | |
|---|---|
| Sitzung A | läuft, 172 von 233 Aufrufen, Runde 1 vollständig, Prüfungen zu 43 % |
| Teil 0 | füllbar nach Abschluss von Sitzung A |
| Teil 1 | blockiert bis zur Reparatur nach § 5 |
| Teil 2 | 51 von 110 Rollen haben E1 bis E3 beantwortet; auswertbar |
| Teil 3 | erfordert Sitzung C, nicht begonnen |

Nächste Schritte in dieser Reihenfolge: Sitzung A zu Ende laufen lassen, die vier Gültigkeitsmaße berechnen und Teil 0 schreiben, die Zerlegung nach § 5 reparieren und die absolute Spalte nachrechnen, erst danach über Sitzung B entscheiden.
