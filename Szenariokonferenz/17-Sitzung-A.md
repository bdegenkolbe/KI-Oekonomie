# Sitzung A — Ergebnis und Gültigkeit

*Runde 0 bis 1b des vollen Laufs: Recherchebank, Bezugsgrößenzerlegung, zwei Szenariogerüste, hundert Rollen, Modellkontrollarm, Validierung mit gesetzten Fehlern. Gültigkeit zuerst, Inhalt danach — nach der Regel aus `11-Konzept-v2.md` § 5, Runde 6.*

---

## 1. Was gelaufen ist

| | |
|---|---|
| Aufrufe | 223, davon 0 mit Fehler, 0 Ausfälle |
| Laufzeit | 9 h 46 min, bei Nebenläufigkeit 2 |
| Zusammensetzung | 10 Faktenblätter · 1 Bezugsgrößenzerlegung · 2 Szenariogerüste · 100 Rollen · 10 Rollen doppelt auf einem zweiten Modell · 100 Prüfungen |
| Unterbrechungen | drei Container-Neustarts, jedes Mal über den Zwischenspeicher fortgesetzt, nichts doppelt bezahlt |
| Aufkommen | 23,8 Mio Token in den Unterinstanzen, 3.492 Werkzeugaufrufe |

Die Wiederaufsetzbarkeit nach `11-Konzept-v2.md` § 8 hat damit ihren Ernstfall bestanden: Ohne sie hätte der Lauf dreimal von vorn begonnen.

## 2. Die neunzehn Abbruchkriterien

| Kriterium | Schwelle | gemessen | |
|---|---|---|---|
| **Prüfschärfe** | ≥ 80 % | **80 %** roh (32 von 40), **97 %** bereinigt (29 von 30) | erfüllt, § 3.2 |
| **Rechenweghaltbarkeit** | ≥ 90 % | 89,2 % roh, **94,2 %** bereinigt um die gesetzten Fehler | erfüllt |
| **Attributionskonsistenz** | ≥ 80 % | **100 %**, mediane Abweichung 1,9 Punkte | erfüllt |
| **Gerüstabhängigkeit** | ≤ 1 bei ≥ 4 von 6 | P1 0,09 · P2 0,00 · P3 0,03 · P3₀ 0,11 | erfüllt, deutlich |
| **Modellabhängigkeit** | < 1 bei ≥ 4 von 6 | **3 von 6** wie vorab definiert; auf verankerten Rollen **6 von 6**, keine Größe über 0,86 | **gerissen**, Ursache behoben, § 3.3 und § 3.3a |
| **Bezugsgrößendeckung** | ≥ 70 % des Rahmens | **42 %**; nach Reparatur und Zuschnittkorrektur **48,9 %** | **gerissen**, § 3.1 und `23-Teil-1-Deutschland.md` § 3 |
| **Topfdeckung** | A2 summiert bei 100 % auf 100, Rest nicht durchgängig null | 100 von 100; Restwert »gar kein Topf« Median 30 %, bei keiner Rolle null | erfüllt |
| **Schemafestigkeit** | 100 % | P4, P5 und A2 summieren bei 100 von 100 Rollen auf 100 | erfüllt |
| **Auswahlwirksamkeit** | ≥ 2 von 30 | **8 von 30** Unterschieden zwischen Bank- und Panelmedian | erfüllt |
| **Durchgriffsspreizung** | Faktor ≥ 2 | D von 0,00 bis 1,41 | erfüllt |
| **Ausfälle** | — | 0 von 110 | — |

Acht Kriterien (Divergenzerhalt, Einwandhaltbarkeit, Fremdbezug, Optionenspreizung, Profilschärfe, Adressierung, kartenweiser Filter, Matrixtauglichkeit) setzen Runden voraus, die in Sitzung A nicht vorkommen. Sie sind offen, nicht erfüllt und nicht gerissen.

## 3. Die drei Brüche — und ihre gemeinsame Ursache

Zwei Kriterien sind gerissen, ein drittes wäre es beinahe. Alle drei gehen auf **denselben Defekt** zurück: die Bezugsgrößenzerlegung der Runde 0a.

### 3.1 Der Defekt

Sieben von hundert Feldern haben eine primäre Bezugsgröße erhalten, zusammen 1.843.170,5 Vollkräfte — 42 % des Kontrollrahmens von 4,4 Mio VZÄ. Die übrigen 93 Felder tragen 0 und »unbekannt«. Betroffen sind der gesamte ambulante Bereich, Kostenträger, Selbstverwaltung, Industrie und alle Felder außerhalb des Gesundheitswesens.

Die Recherche hat dabei korrekt gehandelt und sich ausdrücklich geweigert zu schätzen. Die Lücke liegt in der Quellenwahl: Krankenhaus- und Pflegestatistik zerlegen nur ihren eigenen Sektor; die Einrichtungsgliederung der Gesundheitspersonalrechnung, die den ganzen Rahmen zerlegt, wurde nur als Kontrollsumme verwendet. Der Auftragstext der Runde 0a nennt sie nicht (`11-Konzept-v2.md`, Liefergegenstand R03).

Reparatur in `18-Strategiepapier-2031.md` § 5, gestartet als eigener Lauf (§ 5a, dreizehn Aufrufe).

### 3.2 Erste Folge — die Prüfschärfe stand scheinbar auf der Kippe

Roh gemessen fand die Prüfinstanz 32 von 40 gesetzten Fehlern, also genau die Schwelle von 80 %. Sieben der acht nicht gefundenen Fehler sind vom Typ »absolute Vollkräftezahl passt nicht zum Prozentwert«, gesetzt durch Vervierfachung des Feldes `p3_absolut_vzae`.

Bei allen sieben Rollen stand dort **null**. Null mal vier ist null: Der Fehler wurde nie gesetzt. Dasselbe gilt für alle zehn Fehler dieses Typs — keiner von ihnen existierte. Von den dreißig tatsächlich vorhandenen Fehlern hat die Prüfinstanz **neunundzwanzig** gefunden; der einzige echte Fehlgriff ist ein nicht erkannter Mandatsbruch bei J06.

Die bereinigte Prüfschärfe beträgt damit **97 %**. Die Zahl 80 % misst nicht die Prüfinstanz, sondern denselben Defekt.

### 3.3 Zweite Folge — die Modellabhängigkeit ist gerissen

Zehn Rollen sind zusätzlich auf einem zweiten Modell gelaufen. Gemessen wird die mittlere Differenz beider Antworten im Verhältnis zum Panel-IQR derselben Größe; über 1 misst die Größe das Modell.

| | alle zehn Paare | ohne G03 |
|---|---|---|
| P1 | 0,49 | 0,51 |
| P2 | 0,95 | 1,06 |
| P3 | **1,23** | 0,59 |
| P3₀ | **1,37** | 0,56 |
| P5 (stärkste Komponente) | **1,10** | 0,94 |
| D | **1,39** | **1,23** |
| **unter 1 von sechs Pflichtgrößen** | **3** | **5** |

Ein einziges Paar trägt den Bruch. G03 (Selbsthilfeorganisation chronisch Kranker) hat ebenfalls die Bezugsgröße 0 erhalten; das Kontrollmodell hat den undefinierten Prozentwert nach eigener, offengelegter Konvention als **−100** ausgewiesen, das Hauptmodell als +12. Die Differenz von 112 Punkten bei zehn Paaren verschiebt das Mittel um mehr als den gesamten Panel-IQR.

**Das Kriterium ist trotzdem als gerissen zu führen.** Es war vorab mit der mittleren Differenz festgelegt, und eine Größe nach dem Ergebnis auf den Median umzustellen wäre eine Verschiebung des Maßstabs, nicht eine Korrektur. Festgehalten wird beides: der Bruch wie vorab definiert, und die Diagnose, dass er auf denselben Defekt zurückgeht.

**Was daraus folgt, ist nicht die Verwerfung des Verfahrens.** `13-Validierungsstand.md` sieht für diesen Bruch vor, dass nur ein anderes Instrument hilft, kein größerer Lauf. Diese Konsequenz setzt voraus, dass die Messung gültig war; hier war sie durch einen behebbaren Defekt kontaminiert. Die Entscheidung gehört deshalb hinter die Reparatur: Der Kontrollarm ist auf bereinigter Bezugsgröße zu wiederholen — zehn Aufrufe, rund fünfzehn USD. Fällt er dann erneut, gilt die vorgesehene Konsequenz ohne Vorbehalt.

### 3.3a Nachtrag — der Kontrollarm auf verankerten Rollen

Der Wiederholungslauf ist am 19.09. gelaufen, allerdings **nicht mit dem ursprünglichen Kontrollarm**. Eine Prüfung vor dem Start zeigte, dass acht seiner zehn Rollen auch nach der Reparatur keine Bezugsgröße tragen — G03 darunter, weil es für eine Selbsthilfeorganisation keine amtliche Vollkräftezahl gibt und nicht geben wird. Der Lauf hätte denselben Artefakt erzeugt.

Gelaufen sind deshalb die **sieben Rollen, deren Bezugsgröße vor und nach der Reparatur identisch ist**: A01, A02, A06, A08, A09, C01, C03. Nur bei ihnen ist der Prompt byteidentisch zu Sitzung A, und nur dann misst der Vergleich das Modell statt die geänderte Vorgabe.

| | Sitzung A, 10 Paare | ohne G03, 9 Paare | **verankerte 7** |
|---|---|---|---|
| P1 | 0,49 | 0,51 | **0,58** |
| P2 | 0,95 | 1,06 | **0,52** |
| P3 | 1,23 | 0,59 | **0,39** |
| P3₀ | 1,37 | 0,56 | **0,53** |
| P4 (stärkste Komponente) | 0,77 | 0,69 | **0,83** |
| P5 (stärkste Komponente) | 1,10 | 0,94 | **0,86** |
| D | 1,39 | 1,23 | **0,53** |
| **unter 1 von sechs** | 3 | 5 | **6** |

**Auf den verankerten Rollen ist das Kriterium mit 6 von 6 erfüllt**, und zwar mit Abstand: keine Größe kommt über 0,86. Die Attributionskonsistenz im neuen Arm beträgt 7 von 7, und jede der sieben Antworten liefert eine absolute Vollkräftezahl statt einer Null. Die in Sitzung A gemessene Modellabhängigkeit war damit ganz überwiegend die Messung dessen, wie verschieden zwei Modelle eine **unmögliche Anweisung** auflösen — »rechne einen Prozentwert gegen eine Bezugsgröße von null«.

**Was dieser Nachtrag nicht zeigt.** Sieben Rollen aus den Bänken A und C, also ausschließlich Krankenhaus und Pflege, und ausschließlich der durch eine harte Bezugszahl verankerte Teil des Panels. Das ist die Teilmenge, in der Übereinstimmung am wahrscheinlichsten ist. Das Ergebnis ist deshalb eine **Untergrenze**: Wo die Aufgabe wohldefiniert ist, misst das Panel die Sache und nicht das Modell. Für die Felder ohne amtliche Bezugsgröße bleibt die Frage **offen** und ist erst mit korrigiertem Prompt in Sitzung B zu messen — dort auf beiden Armen, weil ein geänderter Prompt sonst den Vergleich verdirbt.

**Damit revidiert sich auch das Urteil über D.** Die Aussage, D sei die einzige Größe, deren Modellabhängigkeit sich nicht auf den Defekt zurückführen lasse, beruhte auf der kontaminierten Messung. Auf verankerten Rollen liegt D bei 0,53. Die Berichtsregel »D nur als Spannweite« gilt deshalb **nur für die Felder ohne amtliche Bezugsgröße**, nicht für die Zentraltabelle.

### 3.4 Was die Brüche nicht berühren

Alle Größen außer der absoluten Vollkräftespalte sind Verhältniszahlen und hängen nicht an der Basis. Gerüstabhängigkeit (0,00 bis 0,11), Attributionskonsistenz (100 %) und Rechenweghaltbarkeit (94,2 %) sind unabhängig gemessen und erfüllt. Die Gerüstunabhängigkeit ist dabei das stärkste Einzelergebnis des Laufs: Die Hälfte des Panels rechnete gegen ein optimistisches, die andere gegen ein pessimistisches Weltszenario, und die Mediane unterscheiden sich um null bis anderthalb Punkte. Die Zahlen hängen am Fach, nicht an der vorgesetzten Weltannahme.

## 4. Was das Panel sagt

**Erstwerte der Runde 1, vor jeder Diskussion.** Runde 3 erhebt dieselben Größen erneut; erst die Bewegung zwischen beiden ist das Ergebnis. Alle Angaben sind Modellergebnisse und stehen unter dem Konjunktivvorbehalt (`Claude.md` § 4.2).

| Größe | Median | IQR | Spanne |
|---|---|---|---|
| P1 technisch ersetzbare Arbeitszeit | 42 % | 17 | 13–79 |
| P2 davon bis 2031 wirksam | 40 % | 11 | 12–92 |
| P3 Personalbedarf 2031 | +3 % | 16 | −29 bis +50 |
| P3₀ derselbe ohne KI | +11,5 % | 14 | −7 bis +50 |
| D Durchgriff | 0,53 | — | 0,00 bis 1,41 |

Technisch ersetzbar wäre danach gut zwei Fünftel der Arbeitszeit; real frei würde davon zwei Fünftel, also rund ein Sechstel; davon erreichte etwa die Hälfte den Personalbedarf. Netto bliebe ein **steigender** Bedarf, nur weniger steil als ohne KI. Weder Entlastung noch Freisetzung.

**Der schärfste Befund — der Engpass ist keine Technik.**

| A3 Engpass | |
|---|---|
| Entscheidung | **62** |
| bedienendes Personal | 21 |
| Daten | 8 |
| Recht | 8 |
| **Technik** | **1** |

Ebenso bei den Hemmnissen: Refinanzierung 29, Recht und Zulassung 23, Investitionsfähigkeit 24, Datenverfügbarkeit 15, Haftung 7. Vier von fünf Rollen nennen ein Geld- oder Rechtshemmnis, keine ein Könnenshemmnis.

**Wohin der Gewinn ginge (P5, Mediane):** neue Leistung 30 %, **Abfluss ins Ausland 30 %**, beim Erbringer 27,5 %, in Preis und Beitrag 10 %.

**Woraus bezahlt würde (A2, Mediane):** Erbringerbudget 40 %, **gar kein Topf 30 %**, Fördermittel 13,5 %, Erlöstatbestand 5 %, Verwaltungskosten 5 %.

**Wie beschafft würde (A1):** Vergaberecht 47, Zulassung oder Zertifizierung nötig 22, Auftragsverarbeitung nach § 80 SGB X 15, frei beschaffbar 12.

**Ursachenzerlegung (P4, Mediane):** KI 40 %, Strukturreform 28,5 %, Demografie 20 %.

**Europa:** Geantwortet haben 48 Rollen, zuständig waren nach `11-Konzept-v2.md` § 3.1 nur die **18** der Bänke K, L und M. Deren Werte: Abstand zum Vergleichsstaat im Median **−4 Jahre**, Spanne −7 bis −1 — **alle achtzehn sehen Deutschland im Rückstand**; EU-Anteil an der Wertschöpfung im Median **55 %**. Die dreißig nicht zuständigen Rollen verschieben beide Werte erheblich (Median +3 Jahre und 10 %), weil vierzehn von ihnen keinen Vergleichsstaat nannten und zugleich eine Null eintrugen. Ein Panelmedian über alle 48 ist deshalb kein Ergebnis, sondern ein Mischwert; maßgeblich ist K/L/M (`24-Teil-2-Europa.md` § 1).

**Die Validierung** hat 226 Beanstandungen auf 100 Karten gelegt, davon 70 zurückgewiesen; nur 7 Karten blieben ohne Beanstandung. Schwerpunkt sind die Belege (Befunde 4 und 5 mit zusammen 51 Nennungen), nicht die Pflichtgrößen. Rund vierzig davon sind die gesetzten Fehler; die übrigen rund 190 sind echte Funde und der eigentliche Ertrag der Prüfung.

## 5. Zwei Register, ohne zusätzlichen Aufruf

- `19-Falsifikatoren.md` — **92 von 100** Gegenproben tragen Jahreszahl und Zahlenschwelle, sind also entscheidbar. 41 davon bis 2029.
- `20-Durchgriffskanaele.md` — von 342 genannten Rechtsnormen sind **59** feldübergreifend gedeckt (≥ 3 Rollen aus ≥ 2 Bänken); 231 sind Einzelnennungen und gehen nicht ins Papier.

## 6. Was jetzt zu tun ist

1. **Nacharbeit** nach `18-Strategiepapier-2031.md` § 5a — läuft: zehn Quellenprüfungen der nie kontrollierten Recherchebank, drei Aufrufe für die Bezugsgrößen.
2. ~~Kontrollarm wiederholen~~ — gelaufen, § 3.3a. Offen bleibt die Messung auf den Feldern ohne amtliche Bezugsgröße; sie gehört mit korrigiertem Prompt in Sitzung B.
3. ~~Absolute Spalte nachrechnen~~ — gerechnet, `rohdaten/p3-tabelle.json` und `18-Strategiepapier-2031.md` § 5b.
4. ~~Teil 0 des Strategiepapiers~~ — geschrieben, `22-Teil-0-Gueltigkeit.md`.
5. Erst danach über Sitzung B entscheiden.

**Drei Korrekturen für jede weitere Sitzung**, kostenlos: die Nullbasis abfangen statt sie an hundert Rollen weiterzureichen; die Faktenblätter als prüfpflichtig kennzeichnen; die gesetzten Fehler vor dem Setzen darauf prüfen, ob sie den Wert überhaupt verändern — ein Fehler, der nichts verändert, misst nicht die Prüfinstanz, sondern verdirbt ihre Messung.
