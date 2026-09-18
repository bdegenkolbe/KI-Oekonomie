# Konzept v2 — Werkstatt statt Umfrage

*Überarbeitung von `00-Konzept.md` auf Grundlage der gemessenen Schwächen in `10-Instrumentenkritik.md`. Neuer Ablauf: Eigenrecherche → Validierung → Gruppendiskussion → Plenum, protokolliert auf einer gemeinsamen Tafel, ausgegeben als interaktives Dashboard.*

---

## 1. Der Wechsel in einem Satz

Version 1 hat zwanzig Fachleute **parallel befragt** und die Antworten hinterher gemittelt. Version 2 lässt sie **erst getrennt recherchieren und dann aufeinandertreffen** — und protokolliert das Aufeinandertreffen so, dass es auswertbar bleibt.

Der Grund ist nicht Geschmack, sondern Messergebnis. Der Makroteil des Stimmzettels hat die Vorannahme des Modells gemessen, nicht das Urteil der Rollen: Bei der Konfidenzfrage gaben alle zwanzig Agenten denselben Wert an, Interquartilsabstand null (`10-Instrumentenkritik.md` § 1). Der Fachteil und die Mechanismusrunde dagegen haben echte Divergenz erzeugt — und in einem Fall eine Mehrheit, die sich *gegen* diese Divergenz durchsetzte (13:4:3 beim BBG-Effekt). Daraus folgt beides: die Makroschätzung fällt weg, und die Begegnung kommt hinzu.

## 2. Das Problem, das eine Diskussion zwischen Sprachmodellen hat

Zwanzig Agenten in einen gemeinsamen Gesprächsfaden zu setzen, würde das Verfahren verschlechtern, nicht verbessern. Sie sind Instanzen desselben Modells; sie einigen sich schnell, höflich und ohne dass die Einigung etwas bedeutet. Der Sonnet-Kontrollarm des ersten Laufs hat diese Homogenisierung bereits gezeigt, bevor überhaupt jemand miteinander sprach.

Die Diskussionsphase muss also so gebaut sein, dass Einigkeit teuer und Widerspruch billig ist — die Umkehrung dessen, was ein freier Chat erzeugt. Fünf Regeln leisten das:

**(1) Gehandelt wird nur durch Karten, nie durch Prosa.** Jeder Zug ist eine typisierte Karte auf der gemeinsamen Tafel (§ 3). Es gibt keinen Gesprächsverlauf, den man überfliegen und dem man sich anschließen könnte.

**(2) Zustimmung ist kein zulässiger Zug.** Es gibt keinen Kartentyp »stimme zu«. Wer einer fremden Karte nichts entgegenzusetzen hat, legt nichts. Konsens ist damit definiert als *ausgebliebener Widerspruch trotz Gelegenheit* — eine Beobachtung, keine Behauptung. Das entzieht der freundlichen Übereinstimmung ihren Ausdrucksweg.

**(3) Jede Karte außer Position und Befund muss auf eine fremde Karte zeigen.** Ein Einwand ohne Adresse ist kein Einwand. Die Tafel ist dadurch ein gerichteter Graph und nicht ein Stapel Meinungen.

**(4) Pflichtzug gegen das eigene Lager.** Jeder Agent muss in der Gruppenrunde mindestens einen Einwand gegen eine Karte aus einem *anderen* Feld legen und mindestens eine Bedingung an seine *eigene* Position hängen — den Satz, unter dem sie nicht mehr gilt. Wer seine eigene Position nicht einschränken kann, hat keine.

**(5) Die Gruppenleitung hat keine Stimme.** Sie clustert, protokolliert und stellt die Streitfrage — sie urteilt nicht. Ein moderierender Agent mit Meinung erzeugt die Einigung, die er protokolliert.

## 3. Die Tafel

Die Tafel ist kein Bild, sondern eine append-only-Liste typisierter Karten in `rohdaten/tafel.json`. Sie ist gleichzeitig Protokoll des Verfahrens **und** Datenquelle des Dashboards — es gibt keinen Übertragungsschritt zwischen beidem und damit keine Stelle, an der die Darstellung vom Protokoll abweichen könnte.

### 3.1 Kartentypen

| Typ | Wer legt sie | Bezug auf fremde Karte | Pflichtfelder zusätzlich |
|---|---|---|---|
| `position` | jede Rolle, Runde 1 | nein | `feld`, `falsifikator` |
| `befund` | jede Rolle, Runde 1 | nein | `quelle` (abgerufen, mit Datum und Fundstelle) |
| `zahl` | Rollen, Runde 1 und 3 | optional | `groesse` mit Einheit, 80-%-Intervall, **Rechenweg**, **Bezugsgruppe in VZÄ** |
| `einwand` | Rollen, Runde 2 und 3 | **ja** | `einwandtyp` (siehe unten) |
| `bedingung` | Rollen, Runde 2 | **ja** (auf eigene Position) | — |
| `attribution` | Rollen, Runde 1 | nein | konkurrierende Ursache neben KI, mit Zeitfenster |
| `dissens` | Gruppenleitung, Runde 2 | **ja** (zwei Karten) | `entscheidungsgroesse` — was gemessen werden müsste |
| `beschluss` | Plenum, Runde 3 | **ja** | Stimmenverhältnis, Gegenstimmen namentlich |

`einwandtyp` ist eine geschlossene Liste: *Faktum bestritten* · *Geltungsbereich zu weit* · *Mechanismus fehlt* · *Gegenbeispiel aus meinem Feld* · *Quelle trägt die Aussage nicht* · *Größenordnung falsch*. Freitext ist als Begründung erlaubt, aber nicht als Typ — sonst lässt sich nicht auszählen, woran die Konferenz sich reibt.

### 3.2 Schema

```json
{
  "id": "K-0137",
  "typ": "einwand",
  "autor": "J02",
  "runde": 2,
  "gruppe": "G3",
  "bezug": ["K-0042"],
  "einwandtyp": "Gegenbeispiel aus meinem Feld",
  "feld": "ML-Engineering Industrie",
  "text": "…",
  "quelle": null,
  "groesse": null,
  "status": "offen",
  "zeit": "2026-09-18T12:31:07Z"
}
```

`status` wird ausschließlich von der Validierungsinstanz gesetzt: `gueltig` · `mit-vorbehalt` · `zurueckgewiesen`. Zurückgewiesene Karten werden **nicht gelöscht**, sondern bleiben mit Begründung auf der Tafel und werden im Dashboard ausgegraut. Eine Tafel, von der Fehler verschwinden, ist kein Protokoll.

### 3.3 Einheitenzwang

Jede `zahl`-Karte trägt `einheit` als Aufzählungswert (`prozent` · `prozentpunkte` · `jahre` · `eur_mrd` · `ct_kwh` · `gw` · `vzae` · `jahreszahl`) und einen erlaubten Wertebereich. Das behebt den Skalenbruch der ersten Fassung, bei dem achtzehn Agenten auf 0–1 und zwei auf 0–100 antworteten und die Auswertung eine Konvention raten musste.

## 4. Ablauf

### Runde 0 — Aufstellung

Roster aus `02-Agenten-Roster.md`, aber neu geschnitten: **24 Rollen in vier Gruppen à sechs**, und die Gruppen sind *quer* zu den Bänken gebildet. In jeder Gruppe sitzen eine Anbieter-, eine Anwender-, eine Aufsichts-, eine Arbeitnehmer- und eine Fiskalperspektive. Wer in Version 1 gefehlt hat, ist verpflichtend besetzt: produzierendes Gewerbe, Handel, Logistik, Bau. Der Grund steht in `10-Instrumentenkritik.md` § 3e — ein Panel aus verrechtlichten Feldern überschätzt systematisch die Schutzwirkung von Recht.

Vierundzwanzig statt hundert ist eine bewusste Entscheidung. Hundert Rollen kosteten bei diesem Verfahren rund 525 USD und vierzehn Stunden Wanduhrzeit (§ 7) und brächten vor allem mehr Karten desselben Typs. Die Begegnung skaliert schlechter als die Befragung — und sie ist der Teil, der trägt.

### Runde 1 — Eigenrecherche und Position (isoliert)

Jede Rolle arbeitet allein, sieht nichts von den anderen. Sie recherchiert in **ihrem** Feld — das Recherchemandat aus `03-Stimmzettel.md` gilt weiter und weist Makrogrößen ausdrücklich den dafür zuständigen Rollen zu. Ergebnis je Rolle:

- eine `position`-Karte: die These zum eigenen Feld bis 2030, mit dem Satz, der sie widerlegen würde
- drei bis sechs `befund`-Karten, jede mit abgerufener Quelle, Datum und Fundstelle
- ein bis drei `zahl`-Karten — **nur zu Größen, die aus dem eigenen Feld hergeleitet sind**, mit Rechenweg vor Ergebnis und Bezugsgruppengröße
- eine `attribution`-Karte: welche andere Ursache im selben Zeitfenster dieselbe Wirkung hätte

Gestrichen gegenüber Version 1: V1, V2, V3, V6, V7, V13, V14. Keine Rolle schätzt mehr das deutsche BIP 2030 oder ihre eigene Konfidenz. Was das Panel zu Makrogrößen zu sagen hat, entsteht in Runde 3 aus den Feldkarten — oder gar nicht.

### Runde 1b — Validierung

Unverändert aus `06-Validierung.md`, aber auf Kartenebene statt auf Stimmzettelebene: Existenz der Quelle, Deckung der Aussage, Mandatstreue, fachliche Plausibilität. Kleines Modell. Nur Karten mit Status `gueltig` oder `mit-vorbehalt` gehen in Runde 2; zurückgewiesene bleiben sichtbar.

### Runde 2 — Gruppendiskussion an der Tafel

Die Gruppenleitung clustert die validierten Karten ihrer sechs Mitglieder und formuliert daraus **die Streitfrage der Gruppe** — sie wird nicht vorgegeben, sie wird gefunden. Dann zwei Kartenzüge je Rolle, mit den Pflichtzügen aus § 2 Regel 4.

Die Gruppe schließt mit einem `dissens`-Eintrag je offenem Streitpunkt, der drei Dinge benennt: die beiden unvereinbaren Karten, welche Bänke sich gegenüberstehen, und **die Entscheidungsgröße** — was man messen müsste, um den Streit zu beenden. Letzteres ist der eigentliche Ertrag der Runde: Nicht die Einigung, sondern die Benennung dessen, woran die Uneinigkeit hängt.

### Runde 3 — Plenum (Kreuztisch)

Alle vier Gruppen sehen alle Dissens-Einträge. Jetzt — und erst jetzt — wird quantifiziert, und zwar ausschließlich auf den Größen, die die Gruppen selbst aufgeworfen haben. Jede Rolle legt zu jeder plenumsrelevanten Größe eine `zahl`-Karte mit Rechenweg.

Gezählt wird pro Größe: Median, Interquartilsabstand, **gewichtet nach Bezugsgruppe und ungewichtet nebeneinander**. Ein `beschluss` entsteht, wenn eine Position nach der Kreuztischrunde keinen unbeantworteten Einwand mehr trägt; das Stimmenverhältnis und die Gegenstimmen stehen namentlich in der Karte.

### Runde 4 — Red Team, Synthese, Verifikation

Wie in `00-Konzept.md` § 2, mit einer Ergänzung: Das Red Team greift nicht mehr das führende Szenario an, sondern **den am breitesten getragenen Beschluss** — und zusätzlich die Tafel selbst (Welche Karte hat niemand angegriffen, obwohl sie angreifbar war?). Synthese und Verifikation bleiben getrennte Instanzen.

## 5. Konvergenz — neu definiert

Die 25-%-Regel aus `00-Konzept.md` § 3 entfällt. Sie setzte voraus, dass alle Rollen dieselben Größen schätzen, und genau das hat sich als Fehler erwiesen. An ihre Stelle treten drei Maße, die aus der Tafel direkt ablesbar sind:

| Maß | Definition | Was es bedeutet |
|---|---|---|
| **Angriffsüberleben** | Anteil der Positionskarten, gegen die ein Einwand gelegt wurde und die danach unverändert blieben | belastbarer als Zustimmung: geprüft und standgehalten |
| **Feldübergreifende Deckung** | Zahl der Befunde, die von Rollen aus mindestens drei verschiedenen Bänken unabhängig gestützt werden | das Äquivalent zur Konvergenz — vier Felder leiteten die Prüfpfad-Gegenbuchung unabhängig aus je eigenem Recht her |
| **Dissenskarte** | Liste der Streitpunkte mit benannter Entscheidungsgröße | der Befund, wenn es keinen gibt |

Keines dieser Maße lässt sich durch Höflichkeit erzeugen. Alle drei lassen sich aus dem Kartengraphen berechnen, ohne dass eine Instanz sie interpretieren muss.

## 6. Das Dashboard

Eine eigenständige HTML-Seite nach `Formatvorlage.md`, ohne externe Abhängigkeiten außer der Schrift, gespeist aus `tafel.json`. Vier Ansichten auf denselben Datensatz:

**(1) Tafel.** Der Kartengraph selbst, gruppiert nach den vier Gruppen, Karten als Kacheln, Einwände als Verbindungen. Filter nach Kartentyp, Bank, Runde und Status. Klick auf eine Karte öffnet Volltext, Quelle und alle eingehenden Einwände. Zurückgewiesene Karten ausgegraut, nicht versteckt.

**(2) Streit.** Die Dissenskarte: je Streitpunkt die beiden Positionen nebeneinander, die Bänke, die Entscheidungsgröße. Sortierbar danach, wie viele Felder betroffen sind.

**(3) Zahlen.** Je plenumsrelevanter Größe ein Punktdiagramm der Einzelschätzungen mit 80-%-Intervall, gewichtet und ungewichtet, jeder Punkt klickbar auf den Rechenweg. Kein Balkendiagramm von Mittelwerten — die Spreizung ist der Befund (`10-Instrumentenkritik.md` § 2).

**(4) Zeitachse.** Der Verlauf über die Runden: wann welche Karte kam, welche Position wann angegriffen wurde, was überlebt hat. Das macht das Verfahren nachvollziehbar statt nur sein Ergebnis.

Durchgehend sichtbar bleibt die Kennzeichnung nach § 8: Agenten sind Sprachmodelle mit Rollendossiers.

## 7. Kosten und Laufzeit

Hochgerechnet aus den gemessenen Stückkosten (1,55 USD je recherchierender Opus-Aufruf, 0,46 USD je Prüfung) bei 24 Rollen:

| Posten | Aufrufe | USD |
|---|---|---|
| Runde 1 — Position, Befunde, Zahlen (mit Recherche) | 24 | 38 |
| Runde 1b — Validierung | 24 | 11 |
| Tafelführung und Clustering | 8 | 4 |
| Runde 2 — zwei Kartenzüge je Rolle (ohne Recherche) | 48 | 38 |
| Gruppenprotokolle | 4 | 2 |
| Runde 3 — Plenum | 24 | 22 |
| Runde 4 — Red Team, Synthese, Verifikation | 6 | 10 |
| **Summe** | **138** | **rund 125 USD** |

Wanduhrzeit: 138 Aufrufe bei zwei nebenläufigen Agenten und rund drei Minuten je Aufruf ergeben **etwa 3,5 Stunden**. Die Nebenläufigkeit von zwei ist durch die vier CPUs des Containers gesetzt und nicht durch das Modell.

Zum Vergleich dieselbe Rechnung mit 100 Rollen: rund 525 USD und rund 14 Stunden. Die Empfehlung lautet 24 Rollen — nicht aus Sparsamkeit, sondern weil die zusätzlichen 76 Rollen Karten desselben Typs beitrügen, während die Qualität der Konferenz an der Besetzungsbreite hängt, die schon bei 24 erreichbar ist.

## 8. Was auch Version 2 nicht leistet

Unverändert gilt `00-Konzept.md` § 4: Die Agenten sind Sprachmodelle mit Rollendossiers, keine befragten Fachleute. Das Ergebnis ist ein strukturiertes Argumentmodell, keine Umfrage und keine Prognose.

Dazu drei Einschränkungen, die speziell für das neue Verfahren gelten:

- **Die Diskussion bleibt eine Simulation von Widerspruch.** Die Regeln aus § 2 erzwingen Einwände; sie garantieren nicht, dass die Einwände die stärksten verfügbaren sind. Ein Agent, der widersprechen *muss*, widerspricht — notfalls schwach.
- **Die Validierungsinstanz ist selbst ein Sprachmodell.** Sie erkennt erfundene Quellen und falsche Zuschreibungen; sie garantiert nicht, dass eine auffindbare Quelle richtig gelesen wurde. Ob sie zu milde urteilt, ist nach wie vor offen (`07-Pilotbericht.md` § 6).
- **Das Attributionsproblem wird sichtbar gemacht, nicht gelöst.** Die `attribution`-Karte zwingt jede Rolle, die konkurrierende Ursache zu benennen. Ob die Wirkung dann der KI oder der Krankenhausreform zuzurechnen ist, kann dieses Verfahren nicht entscheiden — es kann nur verhindern, dass die Frage unterschlagen wird.
