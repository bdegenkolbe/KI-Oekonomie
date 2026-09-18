# Validierungsstand und Stufenplan

*Antwort auf die Frage, ob das Vorgehen validiert ist — und was daraus für einen Lauf mit 100 Rollen und 10 Rechercheuren folgt. Stand nach der Fertigstellung von `11-Konzept-v2.md`.*

---

## 1. Was validiert ist, und was nicht

**Nein, das Verfahren aus `11-Konzept-v2.md` ist nicht validiert.** Die Unterscheidung ist wichtig, weil Teile des Apparats zweimal gelaufen sind und andere noch nie.

| Bestandteil | Status | Beleg |
|---|---|---|
| Fachteil mit Tätigkeiten, Hemmnis, Frühindikator | **validiert** | 20 Rollen, 20 verschiedene Hemmnisse, keine Dopplung; 100 Tätigkeiten mit Arbeitszeitanteil |
| Quellenpflicht und Prüfinstanz | **validiert** | 73 von 73 Quellen auffindbar, 78 Abrufe, drei echte Fachfehler gefunden, darunter eine gegenteilige Zitierung |
| Feldverankerte Frage mit Rechenweg-Pflicht | **validiert** | Runde M: Streuung 2 bis 90 %, gleichzeitig Mehrheitsurteil 13:4:3 |
| Anteilsvektor mit Summenzwang (Kanäle, Verbleib) | **validiert** | Runde M2 und M3: 20 von 20 Vektoren summierten auf 100, keine Nachbearbeitung nötig |
| Makroteil des Stimmzettels | **widerlegt** | V14: alle zwanzig Agenten derselbe Wert, IQR null (`10-Instrumentenkritik.md` § 1) |
| Delphi-Revision | nie gelaufen | — |
| **Tafel als Kartengraph** | **nie gelaufen** | — |
| **Die fünf Diskussionsregeln** | **nie gelaufen** | — |
| **Gruppenphase mit Pflichtzügen** | **nie gelaufen** | — |
| **Fünf Pflichtgrößen, zweimal erhoben** | **nie gelaufen** | — |
| **Streitindex als Auswahlregel für die Diskussion** | **nie gerechnet** | die Bankmedian-Variante ist erst ab sechs Rollen je Bank rechenbar und in Stufe 1 gar nicht prüfbar (§ 3) |
| **Szenariogerüst als gemeinsame Setzung** | **nie gelaufen** | — |
| **Optionenrunde mit Kippbedingung** | **nie gelaufen** | — |
| **Angriffsüberleben, feldübergreifende Deckung, Divergenzerhalt als Konvergenzmaße** | **nie berechnet** | — |
| **Zwischenspeicherung, Wiederholung je Agent, Laufprotokoll** | **nie gelaufen** | bisherige Skripte schreiben erst am Ende |
| Red Team, Synthese-Verifikations-Trennung | nie gelaufen | — |

Die fett gesetzten Zeilen sind genau der Teil, der in Version 2 neu ist. Der gesamte Mehrwert des Verfahrens gegenüber einer Parallelbefragung hängt an ungeprüfter Mechanik. Zwei Bestandteile sind allerdings **nahe an Geprüftem**: Die Pflichtgrößen sind der Bauart nach die Runde-M-Frage, die funktioniert hat, und die Anteilsvektoren P4 und P5 sind M2 und M3, die sauber zurückkamen. Das senkt das Risiko an dieser Stelle, es beseitigt es nicht.

## 2. Das Risiko beim Sprung auf 110 Agenten

Die Kostenrechnung aus `11-Konzept-v2.md` § 9 in der Zusammenfassung:

| Größe | Wert |
|---|---|
| Aufrufe | 502 |
| Kosten | rund 500 USD |
| Wanduhrzeit bei Nebenläufigkeit 2 | rund 12,5 Stunden |
| kleinster verlierbarer Abschnitt mit Zwischenspeicherung | eine Phase, längstens rund 2,5 Stunden |

**Korrektur einer früheren Angabe.** Im Gespräch war von rund 470 USD und knapp zehn Stunden die Rede. Nachgerechnet mit der Optionenrunde als eigenem Aufruf je Rolle — sie lässt sich nicht mit Runde 3 zusammenlegen, ohne dass die Hebel die Zahlenrevision anfärben — liegt der Lauf bei **rund 500 USD und rund 12,5 Stunden**. Gegenüber dem Entwurfsstand (538 Aufrufe, 590 USD, 13,5 Stunden) ist das ein Gewinn, aber ein kleinerer als genannt.

Dazu kommt das inhaltliche Risiko: Läuft die Diskussionsmechanik nicht wie entworfen, merkt man das nach 500 USD und anderthalb Arbeitstagen an einem Ergebnis, das aussieht wie Konsens und keiner ist. Genau dieser Fehler ist im ersten Lauf schon einmal passiert und wurde erst in der nachträglichen Rohdatenauswertung sichtbar.

## 3. Stufenplan

### Stufe 1 — Mechanikprobe (vor allem anderen)

**Zuschnitt:** zwei Rechercheure, ein verkürztes Szenariogerüst, **zwölf Rollen aus mindestens vier Bänken**, alle Phasen einmal durchlaufen — Eigenrecherche mit den fünf Pflichtgrößen, Validierung, Streitauswahl (sechs von zwölf), Gruppendiskussion mit Pflichtzügen, zweite Pflichtgrößen-Erhebung, Optionenrunde mit drei Hebeln.

**Aufwand:** 68 Aufrufe, **rund 70 USD, knapp zwei Stunden.**

**Zweck:** nicht das Ergebnis, sondern die Frage, ob die ungeprüften Bestandteile tun, was sie sollen. Zwölf Rollen sind das Minimum, bei dem die Streitauswahl überhaupt etwas auswählt und die Bankquote greift.

**Vorab festgelegte Abbruchkriterien.** Jede Größe wird nach dem Lauf aus der Tafel berechnet, nicht beurteilt:

| Kriterium | Schwelle | Was es prüft |
|---|---|---|
| **Einwandhaltbarkeit** | ≥ 80 % der Pflichteinwände benennen etwas, das in der adressierten Karte tatsächlich steht (Prüfinstanz urteilt) | ob der Zwang echte Einwände erzeugt oder Höflichkeitsformeln |
| **Divergenzerhalt** | IQR in Runde 3 ≥ 50 % des IQR in Runde 1, bei mindestens vier der fünf Pflichtgrößen | ob die Diskussion Erkenntnis erzeugt oder Homogenisierung |
| **Rechenweghaltbarkeit** | ≥ 90 % der `pflichtgroesse`-Karten lassen sich aus dem genannten Rechenweg und der genannten Bezugsgröße nachrechnen | ob die Zahlen hergeleitet oder gesetzt sind |
| **Fremdbezug** | ≤ 20 % der Einwände richten sich gegen Karten aus dem eigenen Feld | ob die Gruppen quer schneiden oder in Fachnischen zerfallen |
| **Optionenspreizung** | mindestens zwei der drei Hebel erhalten von ≥ 20 % der bewertenden Rollen ein `wirkt nicht` oder `schadet` | ob die Optionenrunde urteilt oder zustimmt |
| **Schemafestigkeit** | 100 % der Karten valide gegen das Kartenschema, Einheiten und Anteilssummen inbegriffen | ob die Tafel ohne Nacharbeit auswertbar bleibt |
| **Adressierung** | 100 % der Einwände, Bedingungen, Bewertungen und Dissens-Karten tragen einen gültigen Bezug | ob der Kartengraph zusammenhängt |
| **Wiederaufsetzbarkeit** | ein absichtlicher Abbruch nach Runde 2 und ein Neustart überspringen alle erfolgreichen Aufrufe und kosten nichts doppelt | ob § 8 des Konzepts trägt |

Reißt **Divergenzerhalt**, **Einwandhaltbarkeit** oder **Rechenweghaltbarkeit**, ist das Verfahren in dieser Form widerlegt und der große Lauf wäre Geldverbrennung. Reißt **Optionenspreizung**, ist die Optionenrunde zu streichen oder umzubauen, der Rest bleibt. Die übrigen vier sind reparierbar, ohne das Konzept zu verwerfen.

**Was Stufe 1 ausdrücklich nicht prüfen kann.** Bei zwölf Rollen aus vier Bänken sitzen drei Rollen je Bank. Ein Bankmedian aus drei Werten ist keiner, und der Interquartilsabstand innerhalb der Bank ist es erst recht nicht. Die Streitauswahl läuft in Stufe 1 deshalb in ihrer **Panelmedian-Form** über alle fünf Pflichtgrößen. Geprüft wird damit, ob die Regel mechanisch greift und ob sie andere Rollen auswählt als der Zufall — **nicht**, ob die Bankkorrektur aus `11-Konzept-v2.md` § 5 den Feldeffekt tatsächlich herausrechnet. Das ist eine offene Stelle, die erst der volle Lauf schließt; sie ist billig abzusichern, indem in Stufe 2 beide Rangfolgen berechnet und nebeneinander ins Dashboard gestellt werden, bevor die dreißig gezogen werden.

### Stufe 2 — Voller Lauf

110 Agenten nach `14-Roster-2031.md`, rund 500 USD, rund 12,5 Stunden, **mit Zwischenspeicherung, Wiederholung je Agent und Laufprotokoll** nach `11-Konzept-v2.md` § 8. Das ist gegenüber den bisherigen Läufen eine Änderung am Workflow-Skript und keine Option: ohne sie kostet ein Abbruch in Stunde elf den ganzen Lauf.

Empfohlene Teilung in drei Sitzungen: Runde 0 bis 1b (212 Aufrufe, rund 5,5 Stunden), Runde 2 bis 3 (170 Aufrufe, rund 4,25 Stunden), Runde 4 bis 6 (120 Aufrufe, rund 3 Stunden). Zwischen den Sitzungen liegt jeweils ein auswertbarer Zwischenstand — die Streitindex-Tabelle nach Runde 1b und die Divergenzerhalt-Rechnung nach Runde 3 sind beide Punkte, an denen ein Abbruch sinnvoll sein *kann*.

### Stufe 3 — Strategiepapier 2031

Aus der Tafel, nicht aus dem Gedächtnis: Jede Aussage des Papiers trägt die Kartennummern, auf denen sie beruht. Was keine Karte hat, steht nicht drin. Das ist zugleich die Prüfbarkeit, die das Arbeitspapier nach `Claude.md` § 4.2 ohnehin verlangt.

## 4. Was auch ein gelungener Lauf nicht leistet

Die Agenten bleiben Sprachmodelle mit Rollendossiers. Ein Strategiepapier aus diesem Verfahren ist ein **strukturiertes Argumentmodell mit benannten Quellen und offengelegten Dissenspunkten** — keine Expertenbefragung, keine Prognose und keine Legitimationsgrundlage für eine politische Entscheidung.

Das Attributionsproblem bleibt, wird aber jetzt beziffert statt bekannt: P4 verlangt von jeder Rolle den Anteil, den sie der KI gegenüber Demografie und Strukturreform zuschreibt (`11-Konzept-v2.md` § 3). Das macht die Frage messbar, nicht entscheidbar. Für das Gesundheitswesen ist sie besonders scharf, weil Krankenhausreform, Vorhaltefinanzierung und Leistungsgruppen bis 2031 unabhängig von jeder KI wirken — vier der bisherigen zwanzig Felder haben von sich aus eine konkurrierende Ursache im selben Zeitfenster genannt (`12-Gesamtauswertung.md`).

Neu hinzu kommt eine Einschränkung, die das fertige Konzept selbst erzeugt: **Das Szenariogerüst macht alle hundert Rollen in ihren Weltannahmen gleich.** Das ist der Preis für Vergleichbarkeit. Trifft eine Annahme des Gerüsts nicht zu, irrt das Panel geschlossen und ohne Streuung — also genau in der Form, die im ersten Lauf als Konsens missdeutet worden wäre. Die `bedingung`-Karten gegen das Gerüst sind das einzige Gegenmittel und gehören deshalb in die Auswertung, nicht in den Anhang.
