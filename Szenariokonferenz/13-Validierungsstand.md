# Validierungsstand und Stufenplan

*Antwort auf die Frage, ob das Vorgehen validiert ist — und was daraus für einen Lauf mit 100 Rollen und 10 Rechercheuren folgt. Stand nach der Fertigstellung von `11-Konzept-v2.md` und dem Einbau der Gültigkeitsmaße.*

---

## 1. Was validiert ist, und was nicht

**Nein, das Verfahren aus `11-Konzept-v2.md` ist nicht validiert.** Die Unterscheidung ist wichtig, weil Teile des Apparats zweimal gelaufen sind und andere noch nie.

| Bestandteil | Status | Beleg |
|---|---|---|
| Fachteil mit Tätigkeiten, Hemmnis, Frühindikator | **validiert** | 20 Rollen, 20 verschiedene Hemmnisse, keine Dopplung; 100 Tätigkeiten mit Arbeitszeitanteil |
| Quellenpflicht und Prüfinstanz | **teilweise validiert** | 73 von 73 Quellen auffindbar, 78 Abrufe, drei echte Fachfehler gefunden — aber die **Schärfe** der Instanz wurde nie gemessen, weil es keine gesetzten Fehler gab |
| Feldverankerte Frage mit Rechenweg-Pflicht | **validiert** | Runde M: Streuung 2 bis 90 %, gleichzeitig Mehrheitsurteil 13:4:3 |
| Anteilsvektor mit Summenzwang | **validiert** | Runde M2 und M3: 20 von 20 Vektoren summierten exakt auf 100, keine Nachbearbeitung nötig |
| Kontrollarm auf zweitem Modell | **einmal gelaufen** | Pilotlauf: zeigte Homogenisierung, wurde aber nicht als Maß ausgewertet |
| Anker-Randomisierung nach ID-Parität | **validiert** | Pilotlauf, mechanisch fehlerfrei zugeteilt — dieselbe Mechanik trägt jetzt die Gerüstzuteilung |
| Makroteil des Stimmzettels | **widerlegt** | V14: alle zwanzig Agenten derselbe Wert, IQR null (`10-Instrumentenkritik.md` § 1) |
| Delphi-Revision | nie gelaufen | — |
| **Tafel als Kartengraph** | **nie gelaufen** | — |
| **Die fünf Diskussionsregeln, Rettungsbedingung, Leerzug** | **nie gelaufen** | — |
| **Gruppenphase mit Pflichtzügen** | **nie gelaufen** | — |
| **Sechs Pflichtgrößen, zweimal erhoben** | **nie gelaufen** | P1–P3 sind der Bauart nach die Runde-M-Frage, P4/P5 sind M2/M3 — das senkt das Risiko, beseitigt es nicht |
| **Streitindex als Auswahlregel** | **nie gerechnet** | — |
| **Zwei Szenariogerüste, hälftig zugeteilt** | **nie gelaufen** | — |
| **Gesetzte Fehler in der Validierung** | **nie gelaufen** | — |
| **Disjunkte VZÄ-Zerlegung über hundert Felder** | **nie erstellt** | — |
| **Optionenrunde mit Kippbedingung** | **nie gelaufen** | — |
| **Die acht Konvergenz- und Gültigkeitsmaße** | **nie berechnet** | — |
| **Zwischenspeicherung, Wiederholung je Agent, Laufprotokoll** | **nie gelaufen** | bisherige Skripte schreiben erst am Ende |
| Red Team, Synthese-Verifikations-Trennung | nie gelaufen | — |

Die fett gesetzten Zeilen sind genau der Teil, der neu ist. Der gesamte Mehrwert des Verfahrens gegenüber einer Parallelbefragung hängt an ungeprüfter Mechanik.

## 2. Das Risiko beim Sprung auf 110 Agenten

Die Kostenrechnung aus `11-Konzept-v2.md` § 9 in der Zusammenfassung:

| Größe | Wert |
|---|---|
| Aufrufe | 533 |
| Kosten | rund 525 USD |
| Wanduhrzeit bei Nebenläufigkeit 2 | rund 13,3 Stunden |
| davon für die Gültigkeitsmaße | 31 Aufrufe, rund 25 USD |
| kleinster verlierbarer Abschnitt mit Zwischenspeicherung | eine Phase, längstens rund 2,75 Stunden |

**Korrektur zweier früherer Angaben.** Im Gespräch war von rund 470 USD und knapp zehn Stunden die Rede; nach dem Einbau der Optionenrunde als eigenem Aufruf je Rolle waren es 500 USD und 12,5 Stunden. Mit Modellkontrollarm, zweitem Szenariogerüst und gesetzten Fehlern liegt der Lauf jetzt bei **rund 525 USD und rund 13,3 Stunden** — praktisch beim Entwurfsstand von 590 USD und 13,5 Stunden, aber mit zwei zusätzlichen Runden und acht statt drei Auswertungsmaßen.

Das inhaltliche Risiko ist dadurch anders verteilt als vorher. Bisher galt: Läuft die Mechanik nicht wie entworfen, merkt man das nach einem Arbeitstag an einem Ergebnis, das aussieht wie Konsens und keiner ist — genau der Fehler des ersten Laufs, sichtbar erst in der nachträglichen Rohdatenauswertung. Drei der neuen Maße — Prüfschärfe, Modellabhängigkeit, Gerüstabhängigkeit — hätten diesen Fehler **während** des Laufs angezeigt. Das verlagert das Risiko von »unbemerkt falsch« zu »bemerkt unbrauchbar«, und das ist der ganze Unterschied.

## 3. Stufenplan

### Stufe 1 — Mechanikprobe (vor allem anderen)

**Zuschnitt:** zwei Rechercheure, beide Szenariogerüste in verkürzter Form, eine Bezugsgrößen-Zerlegung — und **achtzehn Rollen aus drei Bänken zu je sechs**: Bank A (stationäre Versorgung), Bank D (Kostenträger und Selbstverwaltung), Bank J (Gesamtwirtschaft und Fiskus). Alle Phasen einmal: Eigenrecherche mit den sechs Pflichtgrößen, Validierung mit gesetzten Fehlern, Streitauswahl (neun von achtzehn), Gruppendiskussion in drei Gruppen zu je drei Rollen aus je einer Bank, zweite Pflichtgrößen-Erhebung, Optionenrunde mit drei Hebeln. Zwei der achtzehn Rollen laufen zusätzlich auf einem zweiten Modell.

**Aufwand:** 110 Aufrufe, **rund 105 USD, rund 2,75 Stunden.**

**Warum sechs Rollen je Bank und nicht drei.** Die Auswahlregel aus `11-Konzept-v2.md` § 5 rechnet P1 bis P3 gegen den Median der eigenen Bank. Ein Median aus drei Werten ist keiner, und ein Interquartilsabstand über drei Werte erst recht nicht. Mit sechs Rollen je Bank ist die Bankkorrektur **rechenbar und damit prüfbar** — das war in der vorigen Fassung dieses Plans ausdrücklich eine offene Stelle und ist jetzt geschlossen. Der Preis sind sechs zusätzliche Rollen und rund 35 USD.

Der Zuschnitt ist auf Messbarkeit der Mechanik optimiert, nicht auf inhaltliche Breite; eine Arbeitnehmerperspektive fehlt. Die inhaltlichen Ergebnisse der Probe werden **verworfen** und gehen in kein Papier ein.

**Vorab festgelegte Abbruchkriterien.** Jede Größe wird nach dem Lauf aus der Tafel berechnet, nicht beurteilt:

| Kriterium | Schwelle | Was es prüft |
|---|---|---|
| **Prüfschärfe** | ≥ 80 % der maschinell gesetzten Fehler von der Prüfinstanz gefunden | ob die Validierung prüft oder durchwinkt — reißt sie, ist jede andere Zahl des Laufs ungedeckt |
| **Einwandhaltbarkeit** | ≥ 80 % der Pflichteinwände benennen etwas, das in der adressierten Karte tatsächlich steht, und tragen eine belastbare Rettungsbedingung | ob der Zwang echte Einwände erzeugt oder Leerzüge |
| **Divergenzerhalt** | IQR in Runde 3 ≥ 50 % des IQR in Runde 1, bei mindestens fünf der sechs Pflichtgrößen | ob die Diskussion Erkenntnis erzeugt oder Homogenisierung |
| **Rechenweghaltbarkeit** | ≥ 90 % der `pflichtgroesse`-Karten aus Rechenweg und Bezugsgröße nachrechenbar | ob die Zahlen hergeleitet oder gesetzt sind |
| **Modellabhängigkeit** | < 1 × Panel-IQR bei mindestens vier der sechs Pflichtgrößen | ob das Panel die Rollen misst oder das Modell |
| **Gerüstabhängigkeit** | ausgewiesen je Pflichtgröße; ≤ 1 × Panel-IQR bei mindestens vier von sechs | ob die Zahlen an der Sache hängen oder an der Weltannahme |
| **Attributionskonsistenz** | ≥ 80 % der Rollen: (P3 − P3₀) ÷ P3 weicht um ≤ 15 Punkte vom P4-KI-Wert ab | ob die Ursachenzuschreibung hergeleitet oder geraten ist |
| **Auswahlwirksamkeit** | Bankmedian- und Panelmedian-Rangfolge unterscheiden sich in ≥ 2 der 9 ausgewählten Rollen | ob die Bankkorrektur etwas bewirkt — bewirkt sie nichts, entfällt sie zugunsten der einfacheren Regel |
| **Fremdbezug** | ≤ 20 % der Einwände richten sich gegen Karten aus dem eigenen Feld | ob die Gruppen quer schneiden oder in Fachnischen zerfallen |
| **Optionenspreizung** | mindestens zwei der drei Hebel erhalten von ≥ 20 % der bewertenden Rollen ein `wirkt nicht` oder `schadet` | ob die Optionenrunde urteilt oder zustimmt |
| **Schemafestigkeit** | 100 % der Karten valide gegen das Kartenschema, Einheiten und Anteilssummen inbegriffen | ob die Tafel ohne Nacharbeit auswertbar bleibt |
| **Adressierung** | 100 % der Einwände, Bedingungen, Bewertungen und Dissens-Karten tragen einen gültigen Bezug | ob der Kartengraph zusammenhängt |
| **Wiederaufsetzbarkeit** | ein absichtlicher Abbruch nach Runde 2 und ein Neustart überspringen alle erfolgreichen Aufrufe und kosten nichts doppelt | ob § 8 des Konzepts trägt |

**Was welcher Bruch bedeutet.** Reißt die **Prüfschärfe**, ist der Lauf sofort zu beenden — eine Instanz, die gesetzte Fehler nicht findet, macht jede Quellenangabe des Verfahrens wertlos. Reißen **Divergenzerhalt**, **Einwandhaltbarkeit** oder **Rechenweghaltbarkeit**, ist das Verfahren in dieser Form widerlegt. Reißt die **Modellabhängigkeit** bei mehr als zwei Größen, misst das Panel das Modell, und es hilft nur ein anderes Instrument, kein größerer Lauf. **Gerüstabhängigkeit** ist kein Abbruch, sondern eine Berichtsregel: Die betroffene Größe wird getrennt nach Gerüst berichtet. **Auswahlwirksamkeit** und **Optionenspreizung** entscheiden über den Verbleib je eines Bausteins. Die restlichen vier sind reparierbar, ohne das Konzept zu verwerfen.

### Stufe 2 — Voller Lauf

110 Agenten nach `14-Roster-2031.md`, rund 525 USD, rund 13,3 Stunden, **mit Zwischenspeicherung, Wiederholung je Agent und Laufprotokoll** nach `11-Konzept-v2.md` § 8. Das ist gegenüber den bisherigen Läufen eine Änderung am Workflow-Skript und keine Option: ohne sie kostet ein Abbruch in Stunde elf den ganzen Lauf.

Empfohlene Teilung in drei Sitzungen: Runde 0 bis 1b (233 Aufrufe, rund 5,8 Stunden), Runde 2 bis 3 (180 Aufrufe, rund 4,5 Stunden), Runde 4 bis 6 (120 Aufrufe, rund 3 Stunden). Zwischen den Sitzungen liegt jeweils ein auswertbarer Zwischenstand. Zwei davon sind ausdrückliche **Haltepunkte mit Abbruchoption**: nach Runde 1b stehen Prüfschärfe, Modellabhängigkeit und Gerüstabhängigkeit fest — also die Frage, ob die Zahlen überhaupt etwas messen; nach Runde 3 steht der Divergenzerhalt fest — also die Frage, ob die Diskussion etwas bewirkt hat. Ein Lauf, der am ersten Haltepunkt abbricht, hat 233 Aufrufe und rund 250 USD gekostet und die entscheidende Auskunft trotzdem geliefert.

### Stufe 3 — Strategiepapier 2031

Aus der Tafel, nicht aus dem Gedächtnis: Jede Aussage des Papiers trägt die Kartennummern, auf denen sie beruht. Was keine Karte hat, steht nicht drin. Jede berichtete Pflichtgröße trägt ihre vier Gültigkeitsmaße neben sich. Das ist zugleich die Prüfbarkeit, die das Arbeitspapier nach `Claude.md` § 4.2 ohnehin verlangt.

## 4. Was auch ein gelungener Lauf nicht leistet

Die sechs Schwächen, die in der vorigen Fassung dieses Dokuments nur benannt waren, sind in `11-Konzept-v2.md` § 10 durch Mechanismen ersetzt — und jede Zeile jener Tabelle führt eine Restunschärfe mit, die bleibt. Zwei Grenzen darüber hinaus sind mit diesem Verfahren grundsätzlich nicht zu überwinden:

**Die Agenten bleiben Sprachmodelle mit Rollendossiers.** Ein Strategiepapier aus diesem Verfahren ist ein **strukturiertes Argumentmodell mit benannten Quellen, gemessenen Gültigkeitsgrenzen und offengelegten Dissenspunkten** — keine Expertenbefragung, keine Prognose und keine Legitimationsgrundlage für eine politische Entscheidung. Die Gültigkeitsmaße machen die Grenzen des Modells sichtbar; sie machen aus dem Modell kein Panel.

**Das Attributionsproblem bleibt sachlich offen.** P4 und die Gegenprobe P3₀ erzwingen die Bezifferung und decken Widersprüche auf; entscheiden können sie nichts, weil es keine Volkswirtschaft ohne KI zum Vergleich gibt. Für das Gesundheitswesen ist das besonders scharf, weil Krankenhausreform, Vorhaltefinanzierung und Leistungsgruppen bis 2031 unabhängig von jeder KI wirken — vier der bisherigen zwanzig Felder haben von sich aus eine konkurrierende Ursache im selben Zeitfenster genannt (`12-Gesamtauswertung.md`).
