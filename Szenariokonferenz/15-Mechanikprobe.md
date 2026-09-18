# Mechanikprobe mit zehn Rollen

*Lauf vom 18.09.2026, Workflow `wf_228669e3-07b`. Zweck: nicht das Ergebnis, sondern die Frage, ob die ungeprüfte Mechanik aus `11-Konzept-v2.md` tut, was sie soll. Die inhaltlichen Ergebnisse werden verworfen — ausgewertet wird das Verfahren.*

---

## 1. Zuschnitt und Aufwand

Zehn Rollen aus sechs Bänken: A05 Radiologie, A08 Pflegedirektion, B01 Landhausarztpraxis, B08 Offizinapotheke, C01 Intensivpflege, D01 Ersatzkasse, D04 Medizinischer Dienst, E06 Labordiagnostik, F05 Medizinische Fachangestellte, J02 Arbeitsmarktökonomie. Fünf gegen Szenariogerüst A, fünf gegen B. A05 und D01 zusätzlich auf einem zweiten Modell. Alle Phasen einmal.

| Größe | Wert |
|---|---|
| Agentenaufrufe | 57, davon **0 Fehlschläge**, 0 Abbrüche, 0 leere Rückgaben |
| Wanduhrzeit | 2 Stunden 2 Minuten |
| Token der Unteragenten | 4,52 Mio |
| Werkzeugaufrufe (überwiegend Quellenabrufe) | 426 |

Gegenüber der Vollfassung fehlt der Zuschnitt aus drei Bänken zu je sechs; die Bankmedian-Variante des Streitindex ist bei zehn Rollen nicht rechenbar und wurde in der Panelmedian-Form gefahren.

## 2. Die Kriterien

Alle Schwellen waren vor dem Lauf in `13-Validierungsstand.md` § 3 festgelegt. Gerechnet wurde nach dem Lauf aus den Rohdaten (`rohdaten/mechanikprobe-10.json`), nicht beurteilt.

| Kriterium | Schwelle | Ergebnis | |
|---|---|---|---|
| **Prüfschärfe** | ≥ 80 % der gesetzten Fehler gefunden | **9 von 9 = 100 %** | bestanden |
| **Rechenweghaltbarkeit** | ≥ 90 % nachrechenbar | **36 von 36 = 100 %** | bestanden |
| **Divergenzerhalt** | ≥ 50 % bei ≥ 5 von 6 Größen | **6 von 6, Spanne 84–108 %** | bestanden |
| **Modellabhängigkeit** | < 1 × Panel-IQR bei ≥ 4 von 6 | **6 von 6, Spanne 0,48–0,80** | bestanden, knapp |
| **Gerüstabhängigkeit** | ≤ 1 × Panel-IQR bei ≥ 4 von 6 | **6 von 6, Spanne 0,22–0,48** | bestanden |
| **Fremdbezug** | ≤ 20 % Einwände gegen das eigene Feld | **0 von 10 = 0 %** | bestanden |
| **Optionenspreizung** | ≥ 2 von 3 Hebeln mit ≥ 20 % abweichendem Urteil | **3 von 3, Spanne 30–60 %** | bestanden |
| **Schemafestigkeit** | 100 % | **20 von 20 Kartensätzen, alle Anteilsvektoren exakt 100** | bestanden |
| **Adressierung** | 100 % | **10 von 10 Einwänden mit gültigem Bezug** | bestanden |
| **Einwandhaltbarkeit** | ≥ 80 % mit belastbarer Rettungsbedingung | **10 von 10**, kürzeste 89 Wörter, Median 155 | bestanden (Näherung, s. § 5) |
| **Attributionskonsistenz** | ≥ 80 % innerhalb 15 Punkten | **30 %** nach der festgelegten Formel, **70 %** nach korrigierter | **gerissen** |
| **Auswahlwirksamkeit** | Bank- gegen Panelmedian | bei zehn Rollen nicht rechenbar | nicht geprüft |
| **Wiederaufsetzbarkeit** | Abbruch und Neustart ohne Doppelkosten | kein Abbruch ausgelöst | nicht geprüft |

Zehn von elf prüfbaren Kriterien bestanden. Das gerissene führt nicht zum Abbruch, sondern zu einer Korrektur am Instrument — und zu genau der Kennzeichnungspflicht, die das Konzept dafür vorsieht.

## 3. Der Bruch: Die Attributionsformel war falsch gebaut

Die festgelegte Gegenprobe lautete (P3 − P3₀) ÷ P3 und sollte zum P4-Wert für KI passen. Sie erreicht 30 %. Die Prüfinstanz hat den Grund selbständig gefunden, bevor die Auswertung ihn rechnete — Beanstandung zu B01: *»Gegenprobe (P3 − P3_NULL) / P3 ergibt rechnerisch ca. −293 %«*.

**Die Formel teilt durch P3.** P3 ist die Nettoveränderung des Personalbedarfs — und die liegt genau dort nahe null, wo KI-Entlastung und Demografiebedarf sich gegenseitig aufheben. Das ist nicht der Randfall, sondern der interessanteste Fall:

| Rolle | P3 | P3₀ | alte Formel | genannt (P4-KI) |
|---|---|---|---|---|
| F05 | +1,7 | +10,9 | **−541 %** | 46 |
| B01 | +1,4 | +5,5 | **−293 %** | 43 |
| C01 | +1,5 | +4,5 | **−200 %** | 21 |

Drei von zehn Feldern haben einen Nenner unter 2,5 Punkten. Die Agenten haben nicht falsch gerechnet — sie haben den KI-Anteil als Anteil am *Gesamteffekt* verstanden, was die sachlich richtige Lesart ist. Die richtige Formel ist deshalb

> **KI-Anteil = |P3 − P3₀| ÷ (|P3 − P3₀| + |P3₀|)**

Damit steigt die Konsistenz auf 70 %, und die drei Ausreißer mit Nenner nahe null passen auf 0,3 Punkte genau. Übrig bleiben drei Felder mit echter Abweichung: A05 (32,7 Punkte), C01 (19,0), D04 (17,6). **Auch korrigiert reißt das Kriterium.** Nach `11-Konzept-v2.md` § 6 ist die Folge keine Verwerfung, sondern eine Kennzeichnung: Die Attribution des Panels ist in diesen Feldern nicht hergeleitet, und das steht neben der Zahl.

Das ist der Ertrag der Probe. Die fehlerhafte Formel wäre im vollen Lauf über hundert Felder gelaufen und hätte ein Gültigkeitsmaß geliefert, das das Panel für inkonsistent erklärt, obwohl das Messgerät defekt war.

## 4. Was die Mechanik geleistet hat

**Die gesetzten Fehler wurden vollständig gefunden** — alle drei Arten: verdreifachte Zahlen bei unverändertem Rechenweg, untergeschobene Fremdquellen, angehängte Mandatsbrüche. Dazu **28 weitere Beanstandungen**, die nicht gesetzt waren und überwiegend echt sind: eine Fundstellen-URL mit HTTP 404, ein Rechenfehler um den Faktor zehn bei abgerechneten pharmazeutischen Dienstleistungen, eine Rundung von 42,65 auf 42 statt 43, mehrere Quellen, die die mit ihnen belegte Aussage nicht tragen. Der Verdacht aus `07-Pilotbericht.md` § 6, die Prüfinstanz urteile zu milde, ist damit **nicht bestätigt**; sie urteilt eher zu streng (§ 5).

**Die Diskussionsregeln haben gegriffen.** Kein einziger Einwand richtete sich gegen das eigene Feld, keiner ging ins Leere, und keine Rettungsbedingung war eine Formel — die kürzeste hat 89 Wörter und benennt die Bedingung mit Messvorschrift. Die Einwandtypen verteilten sich auf *Rechenweg trägt das Ergebnis nicht* (5), *Gegenbeispiel aus meinem Feld* (3), *Mechanismus fehlt* (1), *Geltungsbereich zu weit* (1). Keine Zustimmungskarte, weil es keine gibt.

**Die Streuung hat die Diskussion überlebt** — sie ist bei P1, P2 und P4 sogar gewachsen (107 %, 108 %, 103 %). Gleichzeitig hat jede der zehn Rollen mindestens einen Wert geändert, A05 um 34 Punkte. Bewegung ohne Homogenisierung ist genau das, was das Maß prüfen sollte.

**Die Gerüste wurden benutzt und bestritten.** Alle zehn Rollen haben substanzielle Einwände gegen ihr zugeteiltes Gerüst formuliert und trotzdem dagegen gerechnet — mehrere hielten die Kombination aus Tarifsteigerung, BIP-Pfad und Beitragssatz für in sich unschlüssig. Drei Rollen (A05, F05, J02) haben die vorgegebene VZÄ-Bezugsgröße bestritten und die amtliche Alternative benannt. Das bestätigt die Anforderung an R03: Ohne Fundstelle zur Bezugsgröße streitet das Panel über den Nenner.

**Die Optionenrunde hat geurteilt statt zugestimmt.** Hebel 2 bekam fünf Mal *schadet* und vier Mal *wirkt* — von Rollen, die alle dasselbe Modell sind. Hebel 1 spaltete das Panel exakt fünf zu fünf.

**Das Panel hat eine Größe erfunden, die das Konzept nicht kannte.** Fünf der zehn Einwände und die Mehrzahl der Dissenspunkte drehten sich um den **Durchgriff von eingesparter Arbeitszeit auf Personalbedarf** — also um das Verhältnis von P1 × P2 zum KI-Anteil an P3:

| Rolle | P1 × P2 | KI-Anteil an P3 | Durchgriff |
|---|---|---|---|
| F05 Medizinische Fachangestellte | 11,2 | −9,2 | **0,82** |
| A05 Radiologie | 7,9 | −5,4 | 0,68 |
| D01 Ersatzkasse | 25,0 | −13,2 | 0,53 |
| B08 Apotheke | 18,9 | −8,6 | 0,46 |
| B01 Landhausarztpraxis, C01 Intensivpflege | 13,7 / 10,0 | −4,1 / −3,0 | **0,30** |

Faktor drei zwischen den Feldern. Weil die Größe nicht definiert war, rechneten die Diskutanten unterschiedlich: teils mit dem gesamten P3, teils nur mit dem KI-Anteil, und kamen für D01 auf 0,62 beziehungsweise 0,53. Dieser Definitionsstreit hat einen halben Dissenspunkt gekostet. Die Größe ist inzwischen als **D** mit fester Formel im Konzept (`11-Konzept-v2.md` § 3).

## 5. Zwei Mängel, die die Probe am Verfahren gefunden hat

**(a) Die Prüfinstanz beanstandet die Pflichtfragen selbst.** Zwei der 28 zusätzlichen Beanstandungen lauten sinngemäß, die P5-Kategorien lägen außerhalb des Mandats der Rolle (A05, C01). Das ist ein Prompt-Fehler: Der Prüfinstanz wurde nicht mitgeteilt, dass P4 und P5 von jeder Rolle verbindlich zu beantworten sind. Sie hat konsequent geprüft, was ihr gesagt wurde. Zu beheben, indem der Prüfauftrag den Pflichtteil vom Freitext trennt.

**(b) Die Wanduhrzeit des Konzepts war zu optimistisch.** Angesetzt waren drei Minuten je Aufruf, gemessen sind **4,28 Minuten** (122 Minuten × 2 Nebenläufigkeit ÷ 57 Aufrufe). Damit verschieben sich alle Zeitangaben:

| | angesetzt | gemessen hochgerechnet |
|---|---|---|
| Mechanikprobe, 18 Rollen, 110 Aufrufe | 2,75 h | **3,9 h** |
| Voller Lauf, 533 Aufrufe | 13,3 h | **19,0 h** |
| Sitzung A / B / C | 5,8 / 4,5 / 3,0 h | **8,3 / 6,4 / 4,3 h** |

Die Kostenschätzung bleibt eine Schätzung: Die tatsächliche Abrechnung ist aus dem Lauf nicht ablesbar. Belastbar ist allein der Tokenverbrauch — 4,52 Mio für 57 Aufrufe, also rund 79.000 Token je Aufruf. Für 533 Aufrufe wären das rund 42 Mio Token.

**(c) Ein Prüfurteil je Rollensatz hätte das Panel halbiert.** Die Instanz vergab **sechsmal »zurückgewiesen«, viermal »mit Vorbehalt« und kein einziges Mal »gültig«**. Jede der zehn Rollen hatte mindestens zwei Beanstandungen, meist an einer einzelnen Quelle. Der Filter des Konzepts — nur `gueltig` oder `mit-vorbehalt` gehen weiter — hätte damit sechs von zehn Rollen ausgeschlossen, ohne dass eine einzige Pflichtgröße widerlegt gewesen wäre. Der Fehler liegt in der Granularität: Der Status gehört zur Karte, nicht zum Kartensatz. Behoben in `11-Konzept-v2.md` § 4.2 und § 5.

**(d) Die Tafel passt bei hundert Rollen in keinen Auftrag.** Zehn Rollen erzeugten 167 KB Runde-1-Antworten; hundert erzeugen rund **1.675 KB**, allein Positionen und Befunde rund 432 KB, allein die Rechenwege rund 563 KB. Das Konzept sah vor, dass alle hundert Rollen in Runde 3 die Dissenspunkte und die Streitfragen sehen. Behoben durch die Zahlenmatrix und die Auszugsregel in `11-Konzept-v2.md` § 4.3 — bemerkenswerterweise lief die Zehnerprobe faktisch schon so, und die fünf schärfsten Einwände entstanden genau aus dem Zahlenvergleich, nicht aus Prosa.

**(e) Für den Streit über die Bezugsgröße gab es kein Verfahren.** Drei der zehn Rollen bestritten die vorgegebene VZÄ-Zahl und nannten die amtliche Alternative, eine mit 18 % Abweichung. Sie rechneten dann gegen einen Nenner, den sie für falsch hielten, und der Streit verschwand. Bei hundert Feldern entscheidet dieser Nenner die addierte VZÄ-Summe. Behoben in `11-Konzept-v2.md` § 5, Runde 0a: Bedingungskarte, Rechnung gegen beide Werte, Summe als Spanne.

## 6. Was weiterhin ungeprüft ist

- **Die Bankkorrektur des Streitindex.** Zehn Rollen erlauben keinen Bankmedian. Die Vollfassung der Probe mit achtzehn Rollen aus drei Bänken zu je sechs bleibt dafür notwendig.
- **Die Wiederaufsetzbarkeit.** Der Lauf ist nicht abgebrochen worden, also wurde auch kein Neustart geprüft. Der Workflow-Mechanismus bietet die Fortsetzung über die Lauf-Kennung an; ob sie trägt, ist nicht gemessen.
- **Die disjunkte VZÄ-Zerlegung** über hundert Felder. Hier wurden zehn Bezugsgrößen von Hand gesetzt, drei davon bestritten. Der eigentliche Test ist die Zerlegung selbst.
- **Der Inhalt.** Er wird verworfen. Die Bezugsgrößen waren Probewerte, die Recherchebank fehlte, und zehn Rollen sind kein Panel.

## 7. Folgerung

Die Mechanik trägt. Zehn von elf prüfbaren Kriterien sind bestanden, mehrere davon deutlich, und der eine Bruch war ein Fehler im Messgerät, nicht im Verfahren — gefunden für rund ein Zehntel dessen, was der volle Lauf kostet.

**Sieben Änderungen sind daraus im Konzept umgesetzt:** die korrigierte Attributionsformel, der Hinweis an die Prüfinstanz auf die Pflichtfragen, die Zeitplanung auf 19 Stunden, der Durchgriff D als berechnete Größe, die Zahlenmatrix mit Auszugsregel, der kartenweise Status und das Verfahren für den bestrittenen Nenner. Dazu die ehrliche Umschreibung von § 8 auf die Lauffähigkeit, die das Werkzeug tatsächlich bietet.

**Jede Behebung erzeugt neue ungeprüfte Mechanik.** Vier Bestandteile sind dadurch hinzugekommen, die es vor dieser Probe nicht gab: D als Vorgabe statt als Eigenkonstruktion, die Zahlenmatrix bei hundert statt zehn Zeilen, der kartenweise Filter und das Wiederaufsetzen. Sie sind der Grund, warum die Vollfassung der Probe mit achtzehn Rollen weiterhin vor Stufe 2 steht — zusammen mit der Bankkorrektur, dem einzigen Konstruktionsstück, das diese Probe von Anfang an nicht prüfen konnte.
