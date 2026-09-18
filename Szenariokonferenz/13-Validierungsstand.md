# Validierungsstand und Stufenplan

*Antwort auf die Frage, ob das Vorgehen validiert ist — und was daraus für einen Lauf mit 100 Rollen und 10 Rechercheuren folgt. Stand nach der Fertigstellung von `11-Konzept-v2.md` und dem Einbau der Gültigkeitsmaße.*

---

## 1. Was validiert ist, und was nicht

**Nein, das Verfahren aus `11-Konzept-v2.md` ist nicht validiert.** Die Unterscheidung ist wichtig, weil Teile des Apparats zweimal gelaufen sind und andere noch nie.

| Bestandteil | Status | Beleg |
|---|---|---|
| Fachteil mit Tätigkeiten, Hemmnis, Frühindikator | **validiert** | 20 Rollen, 20 verschiedene Hemmnisse, keine Dopplung; 100 Tätigkeiten mit Arbeitszeitanteil |
| Quellenpflicht und Prüfinstanz | **validiert** | 73 von 73 Quellen auffindbar; in der Mechanikprobe **9 von 9 gesetzten Fehlern gefunden** und 28 weitere Beanstandungen, darunter eine 404-URL und ein Rechenfehler um den Faktor zehn |
| Feldverankerte Frage mit Rechenweg-Pflicht | **validiert** | Runde M: Streuung 2 bis 90 %, gleichzeitig Mehrheitsurteil 13:4:3 |
| Anteilsvektor mit Summenzwang | **validiert** | Runde M2 und M3: 20 von 20 Vektoren summierten exakt auf 100, keine Nachbearbeitung nötig |
| Kontrollarm auf zweitem Modell | **einmal gelaufen** | Pilotlauf: zeigte Homogenisierung, wurde aber nicht als Maß ausgewertet |
| Anker-Randomisierung nach ID-Parität | **validiert** | Pilotlauf, mechanisch fehlerfrei zugeteilt — dieselbe Mechanik trägt jetzt die Gerüstzuteilung |
| Makroteil des Stimmzettels | **widerlegt** | V14: alle zwanzig Agenten derselbe Wert, IQR null (`10-Instrumentenkritik.md` § 1) |
| Delphi-Revision | **entfallen** | durch die zweite Pflichtgrößen-Erhebung nach der Diskussion ersetzt (`11-Konzept-v2.md` § 5, Runde 3) |
| **Tafel als Kartengraph** | **geprüft** | Mechanikprobe: 20 Kartensätze schemafest, 10 von 10 Einwänden mit gültigem Bezug |
| **Die fünf Diskussionsregeln, Rettungsbedingung, Leerzug** | **geprüft** | 0 % Einwände gegen das eigene Feld, keine Rettungsbedingung unter 89 Wörtern, kein Leerzug |
| **Gruppenphase mit Pflichtzügen** | **geprüft** | eine Gruppe, zwei Züge je Rolle, neun Dissenspunkte mit Entscheidungsgröße |
| **Sechs Pflichtgrößen, zweimal erhoben** | **geprüft** | Divergenzerhalt 84–108 % bei allen sechs, alle zehn Rollen bewegten mindestens einen Wert |
| **Streitindex als Auswahlregel** | **teilweise geprüft** | Panelmedian-Form gerechnet und hat ausgewählt; die **Bankmedian-Variante** braucht sechs Rollen je Bank und ist weiterhin ungeprüft |
| **Zwei Szenariogerüste, hälftig zugeteilt** | **geprüft** | Gerüstabhängigkeit 0,22–0,48 × Panel-IQR; alle zehn Rollen widersprachen dem Gerüst und rechneten dagegen |
| **Gesetzte Fehler in der Validierung** | **geprüft** | 9 von 9 gefunden, dazu 28 ungesetzte Beanstandungen, überwiegend echt |
| **Disjunkte VZÄ-Zerlegung über hundert Felder** | **nie erstellt** | in der Probe zehn Bezugsgrößen von Hand gesetzt, drei davon von den Rollen mit amtlicher Alternative bestritten |
| **D, der Durchgriff, als berechnete Pflichtgröße** | **neu, nie als Vorgabe gelaufen** | in der Probe vom Panel selbst konstruiert, Spanne 0,30 bis 0,82; als Vorgabe mit fester Formel ungeprüft |
| **Zahlenmatrix statt Volltafel (§ 4.3)** | **neu** | die Probe lief faktisch mit einer solchen Matrix und erzeugte daraus die fünf schärfsten Einwände — bei zehn Zeilen, nicht bei hundert |
| **Status je Karte statt je Rolle** | **neu** | die Probe lief mit Rollenurteil und zeigte damit den Fehler; die Kartenvariante ist ungeprüft |
| **Wiederaufsetzen über die Lauf-Kennung (§ 8)** | **nie ausgelöst** | Mechanik vorhanden und dokumentiert, aber kein Abbruch provoziert |
| **Optionenrunde mit Kippbedingung** | **geprüft** | drei Hebel, abweichende Urteile zwischen 30 und 60 %, ein Hebel fünfmal `schadet` |
| **Die acht Konvergenz- und Gültigkeitsmaße** | **berechnet** | sieben bestanden; **Attributionskonsistenz gerissen** und ihre Formel dabei als fehlerhaft erkannt (`15-Mechanikprobe.md` § 3) |
| **Zwischenspeicherung, Wiederholung je Agent, Laufprotokoll** | **nie gelaufen** | bisherige Skripte schreiben erst am Ende |
| Red Team, Synthese-Verifikations-Trennung | nie gelaufen | — |

Die Mechanikprobe vom 18.09.2026 (`15-Mechanikprobe.md`) hat den größten Teil dieser Zeilen abgeräumt: zehn von elf prüfbaren Kriterien bestanden, 57 Aufrufe ohne einen Fehlschlag. Sie hat zugleich fünf Mängel am Konzept gefunden, die alle behoben sind — und **vier neue ungeprüfte Bestandteile erzeugt**, weil jede Behebung eine neue Mechanik einführt. Das ist der normale Preis einer Korrektur und der Grund, warum die Vollfassung der Probe mit achtzehn Rollen weiterhin vor Stufe 2 steht.

## 2. Das Risiko beim Sprung auf 110 Agenten

Die Kostenrechnung aus `11-Konzept-v2.md` § 9 in der Zusammenfassung:

| Größe | Wert |
|---|---|
| Aufrufe | 533 |
| Kosten | rund 525 USD |
| Wanduhrzeit bei Nebenläufigkeit 2 | **rund 19 Stunden** (4,28 min je Aufruf, in der Probe gemessen) |
| davon für die Gültigkeitsmaße | 31 Aufrufe, rund 25 USD |
| kleinster verlierbarer Abschnitt mit Zwischenspeicherung | eine Phase, längstens rund 3,9 Stunden |

**Korrektur früherer Angaben.** Im Gespräch war von rund 470 USD und knapp zehn Stunden die Rede; nach dem Einbau der Optionenrunde als eigenem Aufruf je Rolle waren es 500 USD und 12,5 Stunden. Mit Modellkontrollarm, zweitem Szenariogerüst und gesetzten Fehlern lag der Lauf bei rund 525 USD und rund 13,3 Stunden. Die Mechanikprobe hat die Zeitannahme dann gemessen widerlegt: statt drei Minuten je Aufruf sind es **4,28**, also **rund 19 Stunden**. Die Kostenschätzung bleibt eine Schätzung — die tatsächliche Abrechnung ist aus dem Lauf nicht ablesbar; belastbar sind allein 4,52 Mio Token für 57 Aufrufe, hochgerechnet rund 42 Mio für 533.

Das inhaltliche Risiko ist dadurch anders verteilt als vorher. Bisher galt: Läuft die Mechanik nicht wie entworfen, merkt man das nach einem Arbeitstag an einem Ergebnis, das aussieht wie Konsens und keiner ist — genau der Fehler des ersten Laufs, sichtbar erst in der nachträglichen Rohdatenauswertung. Drei der neuen Maße — Prüfschärfe, Modellabhängigkeit, Gerüstabhängigkeit — hätten diesen Fehler **während** des Laufs angezeigt. Das verlagert das Risiko von »unbemerkt falsch« zu »bemerkt unbrauchbar«, und das ist der ganze Unterschied.

## 3. Stufenplan

### Stufe 1 — Mechanikprobe (vor allem anderen)

**Zuschnitt:** zwei Rechercheure, beide Szenariogerüste in verkürzter Form, eine Bezugsgrößen-Zerlegung — und **achtzehn Rollen aus drei Bänken zu je sechs**: Bank A (stationäre Versorgung), Bank D (Kostenträger und Selbstverwaltung), Bank J (Gesamtwirtschaft und Fiskus). Alle Phasen einmal: Eigenrecherche mit den sechs Pflichtgrößen, Validierung mit gesetzten Fehlern **und kartenweisem Status**, Streitauswahl einschließlich D, Gruppendiskussion in drei Gruppen zu je drei Rollen aus je einer Bank **mit der Zahlenmatrix nach § 4.3**, zweite Pflichtgrößen-Erhebung, Optionenrunde mit drei Hebeln. Zwei der achtzehn Rollen laufen zusätzlich auf einem zweiten Modell. Nach Runde 2 wird der Lauf **absichtlich abgebrochen und neu aufgesetzt**, um § 8 zu prüfen.

**Aufwand:** 110 Aufrufe, **rund 105 USD, rund 3,9 Stunden** (Zeit nach der in der Probe gemessenen Rate von 4,28 Minuten je Aufruf).

**Warum sechs Rollen je Bank und nicht drei.** Die Auswahlregel aus `11-Konzept-v2.md` § 5 rechnet P1 bis P3 gegen den Median der eigenen Bank. Ein Median aus drei Werten ist keiner, und ein Interquartilsabstand über drei Werte erst recht nicht. Mit sechs Rollen je Bank ist die Bankkorrektur **rechenbar und damit prüfbar** — das war in der vorigen Fassung dieses Plans ausdrücklich eine offene Stelle und ist jetzt geschlossen. Der Preis sind sechs zusätzliche Rollen und rund 35 USD.

Der Zuschnitt ist auf Messbarkeit der Mechanik optimiert, nicht auf inhaltliche Breite; eine Arbeitnehmerperspektive fehlt. Die inhaltlichen Ergebnisse der Probe werden **verworfen** und gehen in kein Papier ein.

**Sechzehn vorab festgelegte Abbruchkriterien.** Jede Größe wird nach dem Lauf aus der Tafel berechnet, nicht beurteilt. Die drei letzten sind erst durch die Zehnerprobe entstanden — sie prüfen die Mechanik, mit der deren Befunde behoben wurden:

| Kriterium | Schwelle | Was es prüft |
|---|---|---|
| **Prüfschärfe** | ≥ 80 % der maschinell gesetzten Fehler von der Prüfinstanz gefunden | ob die Validierung prüft oder durchwinkt — reißt sie, ist jede andere Zahl des Laufs ungedeckt |
| **Einwandhaltbarkeit** | ≥ 80 % der Pflichteinwände benennen etwas, das in der adressierten Karte tatsächlich steht, und tragen eine belastbare Rettungsbedingung | ob der Zwang echte Einwände erzeugt oder Leerzüge |
| **Divergenzerhalt** | IQR in Runde 3 ≥ 50 % des IQR in Runde 1, bei mindestens fünf der sechs Pflichtgrößen | ob die Diskussion Erkenntnis erzeugt oder Homogenisierung |
| **Rechenweghaltbarkeit** | ≥ 90 % der `pflichtgroesse`-Karten aus Rechenweg und Bezugsgröße nachrechenbar | ob die Zahlen hergeleitet oder gesetzt sind |
| **Modellabhängigkeit** | < 1 × Panel-IQR bei mindestens vier der sechs Pflichtgrößen | ob das Panel die Rollen misst oder das Modell |
| **Gerüstabhängigkeit** | ausgewiesen je Pflichtgröße; ≤ 1 × Panel-IQR bei mindestens vier von sechs | ob die Zahlen an der Sache hängen oder an der Weltannahme |
| **Attributionskonsistenz** | ≥ 80 % der Rollen: \|P3 − P3₀\| ÷ (\|P3 − P3₀\| + \|P3₀\|) weicht um ≤ 15 Punkte vom P4-KI-Wert ab | ob die Ursachenzuschreibung hergeleitet oder geraten ist — die ursprüngliche Formel war gegen kleine Nenner nicht robust und ist korrigiert (`15-Mechanikprobe.md` § 3) |
| **Auswahlwirksamkeit** | Bankmedian- und Panelmedian-Rangfolge unterscheiden sich in ≥ 2 der 9 ausgewählten Rollen | ob die Bankkorrektur etwas bewirkt — bewirkt sie nichts, entfällt sie zugunsten der einfacheren Regel |
| **Fremdbezug** | ≤ 20 % der Einwände richten sich gegen Karten aus dem eigenen Feld | ob die Gruppen quer schneiden oder in Fachnischen zerfallen |
| **Optionenspreizung** | mindestens zwei der drei Hebel erhalten von ≥ 20 % der bewertenden Rollen ein `wirkt nicht` oder `schadet` | ob die Optionenrunde urteilt oder zustimmt |
| **Schemafestigkeit** | 100 % der Karten valide gegen das Kartenschema, Einheiten und Anteilssummen inbegriffen | ob die Tafel ohne Nacharbeit auswertbar bleibt |
| **Adressierung** | 100 % der Einwände, Bedingungen, Bewertungen und Dissens-Karten tragen einen gültigen Bezug | ob der Kartengraph zusammenhängt |
| **Wiederaufsetzbarkeit** | ein absichtlicher Abbruch nach Runde 2 und ein Neustart überspringen alle erfolgreichen Aufrufe und kosten nichts doppelt | ob § 8 des Konzepts trägt |
| **Kartenweiser Filter** | keine Rolle verliert mehr als drei ihrer neun Karten; keine verliert alle sechs Pflichtgrößen | ob der Filter aus § 5 Runde 1b das Panel erhält statt es zu halbieren |
| **Matrixtauglichkeit** | ≥ 60 % der Einwände richten sich gegen Karten, die der Angreifer nur als Zahlenzeile gesehen hat | ob die Zahlenmatrix als Angriffsfläche trägt — in der Zehnerprobe taten es 100 %, aber bei zehn Zeilen |
| **Durchgriffsspreizung** | D streut über die achtzehn Rollen um mindestens den Faktor zwei | ob D als eigene Größe etwas misst oder nur P1 bis P3 wiederholt |

**Was welcher Bruch bedeutet.** Reißt die **Prüfschärfe**, ist der Lauf sofort zu beenden — eine Instanz, die gesetzte Fehler nicht findet, macht jede Quellenangabe des Verfahrens wertlos. Reißen **Divergenzerhalt**, **Einwandhaltbarkeit** oder **Rechenweghaltbarkeit**, ist das Verfahren in dieser Form widerlegt. Reißt der **kartenweise Filter** oder die **Matrixtauglichkeit**, ist der Lauf mit hundert Rollen nicht durchführbar — beide sind erst durch die Zehnerprobe überhaupt als Fragen sichtbar geworden. Reißt die **Modellabhängigkeit** bei mehr als zwei Größen, misst das Panel das Modell, und es hilft nur ein anderes Instrument, kein größerer Lauf. **Gerüstabhängigkeit** ist kein Abbruch, sondern eine Berichtsregel: Die betroffene Größe wird getrennt nach Gerüst berichtet. **Auswahlwirksamkeit** und **Optionenspreizung** entscheiden über den Verbleib je eines Bausteins. Die restlichen vier sind reparierbar, ohne das Konzept zu verwerfen.

### Stufe 2 — Voller Lauf

110 Agenten nach `14-Roster-2031.md`, rund 525 USD, rund 19 Stunden, **mit Zwischenspeicherung, Wiederholung je Agent und Laufprotokoll** nach `11-Konzept-v2.md` § 8. Das ist gegenüber den bisherigen Läufen eine Änderung am Workflow-Skript und keine Option: ohne sie kostet ein Abbruch in Stunde elf den ganzen Lauf.

Empfohlene Teilung in drei Sitzungen: Runde 0 bis 1b (233 Aufrufe, rund 8,3 Stunden), Runde 2 bis 3 (180 Aufrufe, rund 6,4 Stunden), Runde 4 bis 6 (120 Aufrufe, rund 4,3 Stunden). Zwischen den Sitzungen liegt jeweils ein auswertbarer Zwischenstand. Zwei davon sind ausdrückliche **Haltepunkte mit Abbruchoption**: nach Runde 1b stehen Prüfschärfe, Modellabhängigkeit und Gerüstabhängigkeit fest — also die Frage, ob die Zahlen überhaupt etwas messen; nach Runde 3 steht der Divergenzerhalt fest — also die Frage, ob die Diskussion etwas bewirkt hat. Ein Lauf, der am ersten Haltepunkt abbricht, hat 233 Aufrufe und rund 250 USD gekostet und die entscheidende Auskunft trotzdem geliefert.

### Stufe 3 — Strategiepapier 2031

Aus der Tafel, nicht aus dem Gedächtnis: Jede Aussage des Papiers trägt die Kartennummern, auf denen sie beruht. Was keine Karte hat, steht nicht drin. Jede berichtete Pflichtgröße trägt ihre vier Gültigkeitsmaße neben sich. Das ist zugleich die Prüfbarkeit, die das Arbeitspapier nach `Claude.md` § 4.2 ohnehin verlangt.

## 4. Was auch ein gelungener Lauf nicht leistet

Die sechs Schwächen, die in der vorigen Fassung dieses Dokuments nur benannt waren, sind in `11-Konzept-v2.md` § 10 durch Mechanismen ersetzt — und jede Zeile jener Tabelle führt eine Restunschärfe mit, die bleibt. Zwei Grenzen darüber hinaus sind mit diesem Verfahren grundsätzlich nicht zu überwinden:

**Die Agenten bleiben Sprachmodelle mit Rollendossiers.** Ein Strategiepapier aus diesem Verfahren ist ein **strukturiertes Argumentmodell mit benannten Quellen, gemessenen Gültigkeitsgrenzen und offengelegten Dissenspunkten** — keine Expertenbefragung, keine Prognose und keine Legitimationsgrundlage für eine politische Entscheidung. Die Gültigkeitsmaße machen die Grenzen des Modells sichtbar; sie machen aus dem Modell kein Panel.

**Das Attributionsproblem bleibt sachlich offen.** P4 und die Gegenprobe P3₀ erzwingen die Bezifferung und decken Widersprüche auf; entscheiden können sie nichts, weil es keine Volkswirtschaft ohne KI zum Vergleich gibt. Für das Gesundheitswesen ist das besonders scharf, weil Krankenhausreform, Vorhaltefinanzierung und Leistungsgruppen bis 2031 unabhängig von jeder KI wirken — vier der bisherigen zwanzig Felder haben von sich aus eine konkurrierende Ursache im selben Zeitfenster genannt (`12-Gesamtauswertung.md`).
