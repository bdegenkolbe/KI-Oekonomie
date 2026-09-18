# Validierungsstand und Stufenplan

*Antwort auf die Frage, ob das Vorgehen validiert ist — und was daraus für einen Lauf mit 100 Rollen und 10 Rechercheuren folgt.*

---

## 1. Was validiert ist, und was nicht

**Nein, das Verfahren aus `11-Konzept-v2.md` ist nicht validiert.** Die Unterscheidung ist wichtig, weil Teile des Apparats zweimal gelaufen sind und andere noch nie.

| Bestandteil | Status | Beleg |
|---|---|---|
| Fachteil mit Tätigkeiten, Hemmnis, Frühindikator | **validiert** | 20 Rollen, 20 verschiedene Hemmnisse, keine Dopplung; 100 Tätigkeiten mit Arbeitszeitanteil |
| Quellenpflicht und Prüfinstanz | **validiert** | 73 von 73 Quellen auffindbar, 78 Abrufe, drei echte Fachfehler gefunden, darunter eine gegenteilige Zitierung |
| Feldverankerte Frage mit Rechenweg-Pflicht | **validiert** | Runde M: Streuung 2 bis 90 %, gleichzeitig Mehrheitsurteil 13:4:3 |
| Makroteil des Stimmzettels | **widerlegt** | V14: alle zwanzig Agenten derselbe Wert, IQR null (`10-Instrumentenkritik.md` § 1) |
| Delphi-Revision | nie gelaufen | — |
| **Tafel als Kartengraph** | **nie gelaufen** | — |
| **Die fünf Diskussionsregeln** | **nie gelaufen** | — |
| **Gruppenphase, Plenum** | **nie gelaufen** | — |
| **Angriffsüberleben, feldübergreifende Deckung als Konvergenzmaße** | **nie berechnet** | — |
| Red Team, Synthese-Verifikations-Trennung | nie gelaufen | — |

Die vier fett gesetzten Zeilen sind genau der Teil, der in Version 2 neu ist. Der gesamte Mehrwert des Verfahrens gegenüber einer Parallelbefragung hängt an ungeprüfter Mechanik.

## 2. Das Risiko beim Sprung auf 110 Agenten

Hochgerechnet aus den gemessenen Stückkosten (1,55 USD je recherchierender Opus-Aufruf, 0,46 USD je Prüfung; Diskussionszüge ohne Recherche, aber mit wachsendem Tafelkontext, mit 1,00 USD angesetzt):

| Phase | Aufrufe | USD |
|---|---|---|
| 10 Rechercheure, tiefe Faktenblätter | 10 | 30 |
| 100 Positionen mit Eigenrecherche | 100 | 155 |
| 100 Validierungen | 100 | 46 |
| Gruppenphase: 10 Gruppen × 10 Rollen × 2 Züge | 200 | 200 |
| 10 Gruppenprotokolle | 10 | 6 |
| Plenum | 100 | 110 |
| Red Team, Synthese, Verifikation | 12 | 21 |
| Strategiepapier, mehrstufig | 6 | 20 |
| **Summe** | **538** | **rund 590** |

**Die Wanduhrzeit ist das eigentliche Problem, nicht das Geld.** Der Container hat vier CPUs, die Nebenläufigkeit liegt damit bei zwei Agenten. 538 Aufrufe zu je rund drei Minuten ergeben **rund 13,5 Stunden** in einem Zug. Ein Abbruch nach elf Stunden verliert alles, was nicht zwischengespeichert ist — und die bisherigen Läufe schreiben erst am Ende.

Dazu kommt das inhaltliche Risiko: Läuft die Diskussionsmechanik nicht wie entworfen, merkt man das nach 590 USD und einem Arbeitstag an einem Ergebnis, das aussieht wie Konsens und keiner ist. Genau dieser Fehler ist im ersten Lauf schon einmal passiert und wurde erst in der nachträglichen Rohdatenauswertung sichtbar.

## 3. Stufenplan

### Stufe 1 — Mechanikprobe (vor allem anderen)

**Zuschnitt:** zwei Rechercheure, zehn Rollen aus einer Gruppe, alle Phasen einmal durchlaufen — Eigenrecherche, Validierung, Gruppendiskussion mit Pflichtzügen, ein verkürztes Plenum.
**Aufwand:** rund 38 Aufrufe, **rund 55 USD, rund 1,5 Stunden.**
**Zweck:** nicht das Ergebnis, sondern die Frage, ob die vier ungeprüften Bestandteile tun, was sie sollen.

**Vorab festgelegte Abbruchkriterien.** Jede Größe wird nach dem Lauf aus der Tafel berechnet, nicht beurteilt:

| Kriterium | Schwelle | Was es prüft |
|---|---|---|
| **Einwandhaltbarkeit** | ≥ 80 % der Pflichteinwände benennen etwas, das in der adressierten Karte tatsächlich steht (Prüfinstanz urteilt) | ob der Zwang echte Einwände erzeugt oder Höflichkeitsformeln |
| **Divergenzerhalt** | Streuung der Plenumsgrößen ≥ 50 % der Streuung vor der Diskussion | ob die Diskussion Erkenntnis erzeugt oder Homogenisierung |
| **Fremdbezug** | ≤ 20 % der Einwände richten sich gegen Karten aus dem eigenen Feld | ob die Gruppen quer schneiden oder in Fachnischen zerfallen |
| **Schemafestigkeit** | 100 % der Karten valide gegen das Kartenschema, Einheiten inbegriffen | ob die Tafel ohne Nacharbeit auswertbar bleibt |
| **Adressierung** | 100 % der Einwände, Bedingungen und Dissens-Karten tragen einen gültigen Bezug | ob der Kartengraph zusammenhängt |

Reißt **Divergenzerhalt** oder **Einwandhaltbarkeit**, ist das Verfahren in dieser Form widerlegt und der große Lauf wäre Geldverbrennung. Die übrigen drei sind reparierbar, ohne das Konzept zu verwerfen.

### Stufe 2 — Voller Lauf

110 Agenten nach `14-Roster-2031.md`, rund 590 USD, rund 13,5 Stunden — **mit Zwischenspeicherung nach jeder Phase** in `rohdaten/`, damit ein Abbruch höchstens eine Phase kostet und der Lauf fortsetzbar bleibt. Das ist gegenüber den bisherigen Läufen eine Änderung am Workflow-Skript und keine Option.

### Stufe 3 — Strategiepapier 2031

Aus der Tafel, nicht aus dem Gedächtnis: Jede Aussage des Papiers trägt die Kartennummern, auf denen sie beruht. Was keine Karte hat, steht nicht drin. Das ist zugleich die Prüfbarkeit, die das Arbeitspapier nach `Claude.md` § 4.2 ohnehin verlangt.

## 4. Was auch ein gelungener Lauf nicht leistet

Die Agenten bleiben Sprachmodelle mit Rollendossiers. Ein Strategiepapier aus diesem Verfahren ist ein **strukturiertes Argumentmodell mit benannten Quellen und offengelegten Dissenspunkten** — keine Expertenbefragung, keine Prognose und keine Legitimationsgrundlage für eine politische Entscheidung. Das Attributionsproblem bleibt: Vier der bisherigen zwanzig Felder nennen von sich aus eine konkurrierende Ursache, die im selben Zeitfenster dieselbe Wirkung erzeugt (`12-Gesamtauswertung.md`). Für das Gesundheitswesen ist das besonders scharf, weil Krankenhausreform, Vorhaltefinanzierung und Leistungsgruppen bis 2031 unabhängig von jeder KI wirken.
