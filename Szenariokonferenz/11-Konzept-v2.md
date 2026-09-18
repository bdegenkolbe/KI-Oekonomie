# Konzept v2 — Werkstatt statt Umfrage

*Fertige Fassung. Überarbeitung von `00-Konzept.md` auf Grundlage der gemessenen Schwächen in `10-Instrumentenkritik.md` und der inhaltlichen Ausbeute in `12-Gesamtauswertung.md`. Ablauf: Recherchebank → Eigenrecherche mit Pflichtgrößen → Validierung → Gruppendiskussion der Strittigsten → zweite Quantifizierung → Optionenbewertung → Red Team, Synthese, Verifikation. Protokolliert auf einer gemeinsamen Tafel, ausgegeben als interaktives Dashboard, mündend in ein Strategiepapier 2031.*

---

## 1. Der Wechsel in einem Satz

Version 1 hat zwanzig Fachleute **parallel befragt** und die Antworten hinterher gemittelt. Version 2 lässt sie **erst getrennt recherchieren, dann aufeinandertreffen und danach dieselben Zahlen noch einmal nennen** — und protokolliert alles drei so, dass es auswertbar bleibt.

Der Grund ist nicht Geschmack, sondern Messergebnis. Der Makroteil des Stimmzettels hat die Vorannahme des Modells gemessen, nicht das Urteil der Rollen: Bei der Konfidenzfrage gaben alle zwanzig Agenten denselben Wert an, Interquartilsabstand null (`10-Instrumentenkritik.md` § 1). Der Fachteil und die Mechanismusrunde dagegen haben echte Divergenz erzeugt — und in einem Fall eine Mehrheit, die sich *gegen* diese Divergenz durchsetzte (13:4:3 beim BBG-Effekt). Daraus folgt beides: die freihändige Makroschätzung fällt weg, und die Begegnung kommt hinzu.

## 2. Das Problem, das eine Diskussion zwischen Sprachmodellen hat

Hundert Agenten in einen gemeinsamen Gesprächsfaden zu setzen, würde das Verfahren verschlechtern, nicht verbessern. Sie sind Instanzen desselben Modells; sie einigen sich schnell, höflich und ohne dass die Einigung etwas bedeutet. Der Sonnet-Kontrollarm des ersten Laufs hat diese Homogenisierung bereits gezeigt, bevor überhaupt jemand miteinander sprach.

Die Diskussionsphase muss also so gebaut sein, dass Einigkeit teuer und Widerspruch billig ist — die Umkehrung dessen, was ein freier Chat erzeugt. Fünf Regeln leisten das:

**(1) Gehandelt wird nur durch Karten, nie durch Prosa.** Jeder Zug ist eine typisierte Karte auf der gemeinsamen Tafel (§ 4). Es gibt keinen Gesprächsverlauf, den man überfliegen und dem man sich anschließen könnte.

**(2) Zustimmung ist kein zulässiger Zug.** Es gibt keinen Kartentyp »stimme zu«. Wer einer fremden Karte nichts entgegenzusetzen hat, legt nichts. Konsens ist damit definiert als *ausgebliebener Widerspruch trotz Gelegenheit* — eine Beobachtung, keine Behauptung. Das entzieht der freundlichen Übereinstimmung ihren Ausdrucksweg.

**(3) Jede Karte außer Position, Befund und Pflichtgröße muss auf eine fremde Karte zeigen.** Ein Einwand ohne Adresse ist kein Einwand. Die Tafel ist dadurch ein gerichteter Graph und nicht ein Stapel Meinungen.

**(4) Pflichtzug gegen das eigene Lager.** Jeder Agent in der Diskussionsrunde muss mindestens einen Einwand gegen eine Karte aus einem *anderen* Feld legen und mindestens eine Bedingung an seine *eigene* Position hängen — den Satz, unter dem sie nicht mehr gilt. Wer seine eigene Position nicht einschränken kann, hat keine.

**(5) Die Gruppenleitung hat keine Stimme.** Sie clustert, protokolliert und stellt die Streitfrage — sie urteilt nicht. Ein moderierender Agent mit Meinung erzeugt die Einigung, die er protokolliert.

## 3. Die fünf Pflichtgrößen

Das ist die tragende Änderung gegenüber der ersten Fassung dieses Konzepts. Ohne eine gemeinsame Größe zerfällt ein Lauf mit hundert Rollen in hundert Dossiers, die nebeneinanderliegen und sich nicht widersprechen können. Runde M hat funktioniert, weil sie **eine** Frage mit **einer** Einheit war.

Jede Rolle beantwortet fünf Größen — **nicht aus Makroprojektionen, sondern hergeleitet aus dem eigenen Feld**, mit Rechenweg vor dem Ergebnis und mit der Bezugsgruppengröße, die die Recherchebank geliefert hat (§ 5.0). Stichjahr ist durchgehend **2031**.

| ID | Größe | Einheit | Wertebereich | Pflichtangaben |
|---|---|---|---|---|
| **P1** | Anteil der heute im eigenen Feld geleisteten Arbeitszeit, der bis 2031 technisch durch KI oder Automatisierung ersetzbar ist — unabhängig davon, ob es geschieht | Prozent | 0–100 | Rechenweg aus Tätigkeiten und Arbeitszeitanteilen, 80-%-Intervall |
| **P2** | Anteil von **P1**, der bis 2031 im Regelbetrieb tatsächlich wirksam wird | Prozent von P1 | 0–100 | das bindende Hemmnis aus geschlossener Liste, 80-%-Intervall |
| **P3** | Veränderung des Personal**bedarfs** im eigenen Feld bis 2031 | Prozent der VZÄ der Bezugsgruppe **und** absolute VZÄ | −100 bis +50 | Bezugsgröße in VZÄ nach R03, Rechenweg, 80-%-Intervall |
| **P4** | Ursachenanteil an **P3**: KI und Automatisierung / Demografie und Erwerbspersonenrückgang / Struktur- und Rechtsreform | drei Prozentwerte, Summe 100 | je 0–100 | je Ursache ein Satz, woran man sie erkennen würde |
| **P5** | Verbleib des Effizienzgewinns: beim Leistungserbringer / weitergegeben als Preis oder Beitragssatz / abgeflossen als Lizenz-, Geräte- oder Cloudentgelt überwiegend außerhalb Deutschlands / finanziert zusätzliche Leistung im eigenen Feld | vier Prozentwerte, Summe 100 | je 0–100 | der Vertrag oder Abrechnungsweg, über den der jeweilige Anteil läuft |

Die geschlossene Hemmnisliste zu **P2**: *Recht und Zulassung* · *Refinanzierung und Abrechnung* · *Haftung* · *Personalbindung und Tarif* · *Investitionsfähigkeit* · *Akzeptanz von Patienten oder Beschäftigten* · *Datenverfügbarkeit*. Freitext ist als Begründung erlaubt, nicht als Typ.

**Warum gerade diese fünf.** P3 ist die einzige Größe, die sich über hundert Felder **addieren** lässt, sobald jede Rolle ihre Bezugsgröße in Vollkräften nennt — sie trägt damit die Zentraltabelle des Strategiepapiers. P1 und P2 zerlegen sie in das technisch Mögliche und das tatsächlich Eintretende, und die Differenz beider ist genau die Stelle, an der der Pilotlauf seine belastbarsten Befunde hatte (`12-Gesamtauswertung.md` § 1, § 5). P4 macht aus dem Attributionsproblem eine Zahl statt eines Bekenntnisses: Wer behauptet, KI verändere das Gesundheitswesen bis 2031, muss beziffern, wie viel davon ohnehin Demografie und Krankenhausreform sind. P5 knüpft an die Frage an, die Runde M mit 13:4:3 beantwortet hat, und liefert dem Arbeitspapier den Abflusskanal, auf den seine Wertschöpfungsabgabe zielt.

**Die Pflichtgrößen werden zweimal beantwortet** — in Runde 1 isoliert und in Runde 3 nach der Diskussion (§ 5.3). Die Differenz zwischen beiden Erhebungen *ist* das Divergenzerhalt-Kriterium aus `13-Validierungsstand.md` § 3 und muss nicht mehr geschätzt werden.

## 4. Die Tafel

Die Tafel ist kein Bild, sondern eine append-only-Liste typisierter Karten in `rohdaten/tafel.json`. Sie ist gleichzeitig Protokoll des Verfahrens **und** Datenquelle des Dashboards — es gibt keinen Übertragungsschritt zwischen beidem und damit keine Stelle, an der die Darstellung vom Protokoll abweichen könnte.

### 4.1 Kartentypen

| Typ | Wer legt sie | Bezug auf fremde Karte | Pflichtfelder zusätzlich |
|---|---|---|---|
| `position` | jede Rolle, Runde 1 | nein | `feld`, `falsifikator` |
| `befund` | jede Rolle, Runde 1 | nein | `quelle` (abgerufen, mit Datum und Fundstelle) |
| `pflichtgroesse` | jede Rolle, Runde 1 **und** Runde 3 | nein | `groesse_id` (P1–P5), `einheit`, `rechenweg`, `bezugsgroesse_vzae`, `intervall_80` |
| `zahl` | Rollen, jederzeit | optional | `groesse` mit Einheit, 80-%-Intervall, Rechenweg, Bezugsgruppe in VZÄ |
| `einwand` | Rollen, Runde 2 und 3 | **ja** | `einwandtyp` (siehe unten) |
| `bedingung` | Rollen, Runde 2 und 3 | **ja** (auf eigene Position oder auf das Szenariogerüst) | — |
| `dissens` | Gruppenleitung, Runde 2 | **ja** (zwei Karten) | `entscheidungsgroesse` — was gemessen werden müsste |
| `hebel` | Syntheseinstanz, Runde 4 | **ja** (auf Dissens- oder Positionskarten) | `adressat`, `rechtsgrundlage_oder_instrument`, betroffene Bänke |
| `bewertung` | jede Rolle, Runde 4 | **ja** (auf eine `hebel`-Karte) | `urteil` ∈ {wirkt, wirkt nicht, schadet}, `mechanismus`, `nebenwirkung`, `kippbedingung` |
| `beschluss` | Runde 5 | **ja** | Stimmenverhältnis, Gegenstimmen namentlich |

`einwandtyp` ist eine geschlossene Liste: *Faktum bestritten* · *Geltungsbereich zu weit* · *Mechanismus fehlt* · *Gegenbeispiel aus meinem Feld* · *Quelle trägt die Aussage nicht* · *Größenordnung falsch* · *Rechenweg trägt das Ergebnis nicht*. Der letzte Typ ist neu und richtet sich ausdrücklich gegen `pflichtgroesse`-Karten.

### 4.2 Schema

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

Eine `pflichtgroesse`-Karte trägt zusätzlich:

```json
{
  "groesse_id": "P3",
  "einheit": "prozent_vzae",
  "wert": -12.5,
  "intervall_80": [-22.0, -4.0],
  "bezugsgroesse_vzae": 41800,
  "absolut_vzae": -5225,
  "rechenweg": "41 800 VZÄ Bezugsgruppe nach R03 · …",
  "quelle_bezugsgroesse": "R03-Faktenblatt, Tabelle 4"
}
```

`status` wird ausschließlich von der Validierungsinstanz gesetzt: `gueltig` · `mit-vorbehalt` · `zurueckgewiesen`. Zurückgewiesene Karten werden **nicht gelöscht**, sondern bleiben mit Begründung auf der Tafel und werden im Dashboard ausgegraut. Eine Tafel, von der Fehler verschwinden, ist kein Protokoll.

### 4.3 Einheitenzwang

Jede Karte mit Zahlenwert trägt `einheit` als Aufzählungswert (`prozent` · `prozent_von_p1` · `prozent_vzae` · `prozentpunkte` · `jahre` · `eur_mrd` · `vzae` · `jahreszahl`) und einen erlaubten Wertebereich. Das behebt den Skalenbruch der ersten Fassung, bei dem achtzehn Agenten auf 0–1 und zwei auf 0–100 antworteten und die Auswertung eine Konvention raten musste. Anteilsvektoren (P4, P5) werden auf Summe 100 geprüft und bei Abweichung über drei Punkten zurückgewiesen, nicht normiert.

## 5. Ablauf

### Runde 0 — Recherchebank, Szenariogerüst, Bezugsgrößen

Zehn Rechercheure ohne Stimmrecht liefern je ein Faktenblatt (`14-Roster-2031.md` Teil 1). Drei Lieferungen sind für alles Weitere verbindlich:

**(a) Bezugsgrößen.** R03 liefert für jedes der hundert Felder die Bezugsgruppe in Vollkräften mit Fundstelle. Ohne diesen Nenner ist P3 nicht addierbar, und hundert Rollen würden hundert verschiedene Grundgesamtheiten unterstellen. Wo R03 für ein Feld keine amtliche Zahl findet, wird das Feld als `bezugsgroesse: unbekannt` geführt — die Rolle rechnet dann nur relativ und geht in die Gesamtsumme nicht ein.

**(b) Szenariogerüst.** R08 legt mit R01 und R05 einen gemeinsamen Rahmen für 2031 fest: BIP-Pfad, Erwerbspersonenpotenzial, Beitragssatzkorridor, Tarifentwicklung, Zinsniveau, Stand von EU AI Act, MDR, EHDS und Krankenhausreform. Alle Rollen rechnen gegen dasselbe Gerüst. Wer davon abweichen will, legt eine `bedingung`-Karte auf das Gerüst — das ist zulässig und wird ausgewertet. Ohne Gerüst streiten hundert Rollen über die Welt statt über die Frage, und die Streuung misst dann Weltbilder statt Fachurteile.

**(c) Gegenwartswerte** mit Fundstelle, Erhebungsdatum und ausdrücklich benannten Lücken, je Domäne.

Damit wird zugleich der Konstruktionsfehler des ersten Laufs behoben: Dort recherchierten zwölf von 27 Rollen, und fast alle dasselbe, weil das Instrument nur zwei gegenwärtige Größen enthielt.

### Runde 1 — Eigenrecherche, Position, Pflichtgrößen (isoliert)

Jede der hundert Rollen arbeitet allein und sieht nichts von den anderen — nur die Faktenblätter und das Szenariogerüst. Sie recherchiert in **ihrem** Feld. Ergebnis je Rolle:

- eine `position`-Karte: die These zum eigenen Feld bis 2031, mit dem Satz, der sie widerlegen würde
- drei bis sechs `befund`-Karten, jede mit abgerufener Quelle, Datum und Fundstelle
- fünf `pflichtgroesse`-Karten P1 bis P5, Rechenweg vor Ergebnis
- optional weitere `zahl`-Karten zu Größen, die aus dem eigenen Feld hergeleitet sind

Gestrichen gegenüber Version 1: V1, V2, V3, V6, V7, V13, V14. Keine Rolle schätzt mehr das deutsche BIP 2031 oder ihre eigene Konfidenz. Was das Panel zu Makrogrößen zu sagen hat, entsteht aus der Aggregation von P3 über die Bezugsgruppen — oder gar nicht.

### Runde 1b — Validierung

Unverändert aus `06-Validierung.md`, aber auf Kartenebene: Existenz der Quelle, Deckung der Aussage, Mandatstreue, fachliche Plausibilität. Neu hinzu für `pflichtgroesse`-Karten: **Rechenweghaltbarkeit** — der genannte Rechenweg muss den genannten Wert aus der genannten Bezugsgröße reproduzieren. Kleines Modell. Nur Karten mit Status `gueltig` oder `mit-vorbehalt` gehen weiter; zurückgewiesene bleiben sichtbar.

### Runde 2 — Gruppendiskussion der dreißig Strittigsten

Nicht alle hundert diskutieren. Wer nahe am Median liegt, hat der Tafel in einer Diskussion wenig hinzuzufügen und erzeugt vor allem Karten desselben Typs. Ausgewählt werden **dreißig Rollen nach einer rechnerischen Regel, nicht nach Urteil**:

> Für P1, P2 und P3 wird gegen den Median der **eigenen Bank** gerechnet: *d* = |*x* − Median(*g*, Bank)| ÷ max(IQR(*g*, Bank), Mindestspreizung(*g*)).
> Für P4 und P5 wird gegen den Median des **gesamten Panels** gerechnet, und an die Stelle des Betrags tritt die halbe Summe der absoluten Abweichungen vom Medianvektor.
> Der **Streitindex** einer Rolle ist die Summe dieser fünf Werte.

Die Trennung ist nicht kosmetisch. P1 bis P3 sind feldabhängig: Dass die Radiologie einen höheren automatisierbaren Arbeitszeitanteil nennt als die Intensivpflege, ist kein Streit, sondern der Unterschied der beiden Felder. Gegen den Panelmedian gemessen kämen genau die Rollen in die Diskussion, deren Feld ungewöhnlich ist — nicht die, deren *Urteil* ungewöhnlich ist. Innerhalb der Bank fällt der Feldeffekt weitgehend heraus, und übrig bleibt die Abweichung im Urteil. P4 und P5 dagegen sind Mechanismusfragen: Wie viel der Veränderung der KI zuzurechnen ist und wohin der Gewinn fließt, ist zwischen den Feldern unmittelbar vergleichbar, und dort ist die Abweichung vom Gesamtpanel genau das Gesuchte.

Die Mindestspreizung je Größe (P1, P2: 5 Punkte; P3: 3 Punkte; P4, P5: 8 Punkte) ist vorab festgelegt und verhindert die Division durch null, in die der erste Lauf gelaufen wäre — dort war der IQR einer Variablen exakt null (`10-Instrumentenkritik.md` § 1). Bänke mit weniger als sechs Rollen (M, N) haben keinen belastbaren Bankmedian; für sie gilt der Median der nächstgrößeren verwandten Bank, vorab festgelegt: M rechnet gegen K, N gegen J.

Besetzt werden zuerst **vierzehn Plätze, einer je Bank** (die Rolle mit dem höchsten Streitindex ihrer Bank), danach die **sechzehn** verbleibenden nach Streitindex über alle Bänke. Die Bankquote ist notwendig, weil sonst zwei streitfreudige Bänke die ganze Diskussion stellen und das Verfahren genau die feldübergreifende Deckung verliert, deretwegen es gebaut ist.

Die dreißig sitzen in **fünf Gruppen à sechs, quer zu den Bänken** geschnitten: in jeder Gruppe eine Leistungserbringer-, eine Kostenträger-, eine Aufsichts-, eine Arbeitnehmer- und eine gesamtwirtschaftliche Perspektive. Die Gruppenleitung clustert die validierten Karten und formuliert daraus **die Streitfrage der Gruppe** — sie wird nicht vorgegeben, sie wird gefunden. Dann zwei Kartenzüge je Rolle mit den Pflichtzügen aus § 2 Regel 4.

**Die siebzig Nichtdiskutierenden sind nicht ausgeschlossen.** Ihre Karten aus Runde 1 liegen auf der Tafel und dürfen angegriffen werden; wer angegriffen wurde, antwortet in Runde 3, die er ohnehin durchläuft. Die Diskussion ist damit kein geschlossener Kreis, sondern eine Verdichtung.

Jede Gruppe schließt mit einem `dissens`-Eintrag je offenem Streitpunkt, der drei Dinge benennt: die beiden unvereinbaren Karten, welche Bänke sich gegenüberstehen, und **die Entscheidungsgröße** — was man messen müsste, um den Streit zu beenden. Letzteres ist der eigentliche Ertrag der Runde: Nicht die Einigung, sondern die Benennung dessen, woran die Uneinigkeit hängt.

### Runde 3 — Pflichtgrößen zum zweiten Mal

Alle hundert Rollen sehen jetzt sämtliche Dissens-Einträge, die Einwände gegen ihre eigenen Karten und die Streitfragen der fünf Gruppen. Jede Rolle liefert in einem Aufruf:

1. die fünf Pflichtgrößen **erneut**, mit Rechenweg — Änderung erlaubt, Begründung der Änderung verpflichtend, Nichtänderung ebenfalls zu begründen
2. eine Antwort auf jeden Einwand, der gegen ihre Karten gelegt wurde (`einwand` oder `bedingung`)
3. bei mindestens einem Dissenspunkt eine Stellungnahme aus der eigenen Feldsicht

Ein eigenes Plenum entfällt. Es hätte dasselbe geleistet und hundert Aufrufe zusätzlich gekostet — die Kreuztischwirkung entsteht hier dadurch, dass jede Rolle die Dissenspunkte *aller* fünf Gruppen vor sich hat.

Eine `beschluss`-Karte entsteht am Ende dieser Runde, wenn eine Position keinen unbeantworteten Einwand mehr trägt. Sie führt das Stimmenverhältnis und die Gegenstimmen namentlich. Eine Position, die nie angegriffen wurde, wird **nicht** zum Beschluss — sie bleibt Position, und das Dashboard weist sie als ungeprüft aus.

Gezählt wird pro Pflichtgröße: Median, Interquartilsabstand, **gewichtet nach Bezugsgruppe und ungewichtet nebeneinander** — und zwar für beide Erhebungen getrennt, je Bank und über das ganze Panel. Zusätzlich ausgewiesen wird das Produkt P1 × P2, der bis 2031 tatsächlich automatisierte Arbeitszeitanteil; es ist die Größe, die den Vergleich mit externen Automatisierungsstudien erlaubt, und es ist nicht dasselbe wie P3, weil entfallende Arbeitszeit und entfallender Personalbedarf auseinanderfallen können. P3 wird zusätzlich über alle Felder mit bekannter Bezugsgröße zu einer Summe in Vollkräften aggregiert, mit ausgewiesener Abdeckung («diese Summe deckt *n* von 100 Feldern und *m* Vollkräfte»).

### Runde 4 — Optionenrunde

Bis hierher bewertet das Verfahren an keiner Stelle eine Handlungsoption. Für ein Strategiepapier ist das zu wenig: Ein Lagebild ohne bewertete Hebel ist kein Strategiepapier, sondern ein Befund.

Die Syntheseinstanz leitet aus der Tafel **fünf bis acht Hebel** ab — jeder mit Adressat (Bund, Land, Selbstverwaltung, EU, Träger), Instrument (Gesetz, Richtlinie, Vergütungsregel, Investition, Tarifvertrag) und den betroffenen Bänken. Die Hebel werden nicht erfunden, sondern aus Dissens- und Positionskarten hergeleitet; jede `hebel`-Karte trägt die Kartennummern, auf denen sie beruht.

Dann bewertet **jede der hundert Rollen jeden Hebel für ihr eigenes Feld** mit je einer `bewertung`-Karte: `wirkt` / `wirkt nicht` / `schadet`, dazu der Mechanismus, die Nebenwirkung und die Kippbedingung — der Umstand, unter dem das Urteil sich umkehrt. Ausgewertet wird nicht die Mehrheit, sondern **das Muster**: Ein Hebel, der in vierzig Feldern wirkt und in fünf schadet, ist etwas anderes als einer, der überall schwach wirkt, und beides ist im Balkendiagramm dasselbe.

### Runde 5 — Red Team, Synthese, Verifikation

Wie in `00-Konzept.md` § 2, mit zwei Ergänzungen: Das Red Team greift **den am breitesten getragenen Beschluss** an, zusätzlich die Tafel selbst (Welche Karte hat niemand angegriffen, obwohl sie angreifbar war?) und **den bestbewerteten Hebel**. Synthese und Verifikation bleiben getrennte Instanzen — wer das Ergebnis schreibt, prüft es nicht selbst.

### Runde 6 — Strategiepapier 2031

Aus der Tafel, nicht aus dem Gedächtnis: Jede Aussage trägt die Kartennummern, auf denen sie beruht. Was keine Karte hat, steht nicht drin. Drei Teile — Europa, Deutschland, deutsches Gesundheitswesen — mit der aggregierten P3-Tabelle als Rückgrat, der P4-Zerlegung als Attributionsvorbehalt und den bewerteten Hebeln als Schluss. Modellergebnisse und Gesetzentwürfe im Konjunktiv (`Claude.md` § 4.2).

## 6. Konvergenz — neu definiert

Die 25-%-Regel aus `00-Konzept.md` § 3 entfällt. Sie setzte voraus, dass alle Rollen dieselben Größen schätzen, und genau das hat sich als Fehler erwiesen. An ihre Stelle treten vier Maße, die aus der Tafel direkt ablesbar sind:

| Maß | Definition | Was es bedeutet |
|---|---|---|
| **Angriffsüberleben** | Anteil der Positionskarten, gegen die ein Einwand gelegt wurde und die danach unverändert blieben | belastbarer als Zustimmung: geprüft und standgehalten |
| **Feldübergreifende Deckung** | Zahl der Befunde, die von Rollen aus mindestens drei verschiedenen Bänken unabhängig gestützt werden | das Äquivalent zur Konvergenz — vier Felder leiteten die Prüfpfad-Gegenbuchung unabhängig aus je eigenem Recht her |
| **Divergenzerhalt** | IQR jeder Pflichtgröße in Runde 3 im Verhältnis zum IQR derselben Größe in Runde 1; bei den Anteilsvektoren P4 und P5 komponentenweise | fällt er unter die Hälfte, hat die Diskussion homogenisiert statt aufgeklärt |
| **Dissenskarte** | Liste der Streitpunkte mit benannter Entscheidungsgröße | der Befund, wenn es keinen gibt |

Keines dieser Maße lässt sich durch Höflichkeit erzeugen. Alle vier lassen sich aus dem Kartengraphen berechnen, ohne dass eine Instanz sie interpretieren muss.

## 7. Das Dashboard

Eine eigenständige HTML-Seite nach `Formatvorlage.md`, ohne externe Abhängigkeiten außer der Schrift, gespeist aus `tafel.json`. Sechs Ansichten auf denselben Datensatz:

**(1) Tafel.** Der Kartengraph selbst, gruppiert nach den fünf Gruppen, Karten als Kacheln, Einwände als Verbindungen. Filter nach Kartentyp, Bank, Runde und Status. Klick auf eine Karte öffnet Volltext, Quelle und alle eingehenden Einwände. Zurückgewiesene Karten ausgegraut, nicht versteckt.

**(2) Pflichtgrößen.** Je Größe ein Punktdiagramm der hundert Einzelwerte mit 80-%-Intervall, **Runde 1 und Runde 3 nebeneinander**, gewichtet und ungewichtet. Jeder Punkt klickbar auf den Rechenweg. Kein Balkendiagramm von Mittelwerten — die Spreizung ist der Befund (`10-Instrumentenkritik.md` § 2).

**(3) Streit.** Die Dissenskarte: je Streitpunkt die beiden Positionen nebeneinander, die Bänke, die Entscheidungsgröße. Dazu die Streitindex-Rangliste, aus der die dreißig Diskutierenden hervorgegangen sind — die Auswahl ist damit nachprüfbar und nicht behauptet.

**(4) Hebel.** Je Hebel eine Matrix aus hundert Feldern × drei Urteilen, Kippbedingungen als aufklappbare Liste. Sortierbar nach Anteil `schadet`, nicht nach Zustimmung.

**(5) Attribution.** Die P4-Zerlegung über alle Felder, als gestapelte Anteile nach Bank — die Antwort auf die Frage, wie viel von 2031 überhaupt der KI zuzurechnen wäre.

**(6) Zeitachse.** Der Verlauf über die Runden: wann welche Karte kam, welche Position wann angegriffen wurde, was überlebt hat, welche Zahl sich zwischen Runde 1 und Runde 3 bewegt hat. Das macht das Verfahren nachvollziehbar statt nur sein Ergebnis.

Durchgehend sichtbar bleibt die Kennzeichnung nach § 10: Agenten sind Sprachmodelle mit Rollendossiers.

## 8. Lauffähigkeit

Ein Lauf dieser Größe dauert länger als eine Sitzung (§ 9). Drei Anforderungen an das Workflow-Skript sind deshalb keine Option:

**Zwischenspeicherung je Phase.** Nach jeder Runde wird der vollständige Zwischenstand nach `rohdaten/lauf/<phase>.json` geschrieben, nicht erst am Ende. Die bisherigen Läufe schreiben am Ende; ein Abbruch nach elf Stunden verlöre alles.

**Wiederholung je Agent.** Ein fehlgeschlagener Aufruf wird zweimal wiederholt; danach wird für diese Rolle ein Eintrag `status: luecke` mit Fehlertext geschrieben und der Lauf läuft weiter. Eine ausgefallene Rolle darf nicht neunundneunzig andere kosten — aber sie muss im Ergebnis sichtbar sein und aus allen Kennzahlen ausgewiesen herausfallen.

**Laufprotokoll.** `rohdaten/lauf/manifest.json` führt je Aufruf Phase, Rolle, Status, Modell, Kosten und den Hash der Aufgabenstellung. Ein Wiederaufsetzen überspringt alles, was mit unverändertem Hash bereits erfolgreich war. Das macht den Lauf über mehrere Sitzungen fortsetzbar und die Kostenangaben in § 9 nachprüfbar statt geschätzt.

## 9. Kosten und Laufzeit

Hochgerechnet aus den gemessenen Stückkosten (1,55 USD je recherchierender Opus-Aufruf, 0,46 USD je Prüfung mit kleinem Modell; Karten- und Bewertungszüge ohne Recherche, aber mit wachsendem Tafelkontext, mit 0,60 bis 1,00 USD angesetzt):

| Phase | Aufrufe | USD |
|---|---|---|
| Runde 0 — zehn Faktenblätter, mehrere Abrufe je Blatt | 10 | 30 |
| Runde 0 — Szenariogerüst und Bezugsgrößen | 2 | 6 |
| Runde 1 — Position, Befunde, fünf Pflichtgrößen, mit Eigenrecherche | 100 | 155 |
| Runde 1b — Validierung, kleines Modell | 100 | 46 |
| Streitauswahl nach § 5 Runde 2 | 0 (rechnerisch) | 0 |
| Runde 2 — dreißig Rollen × zwei Kartenzüge | 60 | 60 |
| Runde 2 — fünf Gruppenleitungen × Streitfrage und Dissensprotokoll | 10 | 6 |
| Runde 3 — Pflichtgrößen zum zweiten Mal, Antwort auf Einwände | 100 | 100 |
| Runde 4 — Hebelsatz aus der Tafel | 2 | 4 |
| Runde 4 — Optionenbewertung je Rolle | 100 | 60 |
| Runde 5 — Red Team, Synthese, Verifikation | 12 | 16 |
| Runde 6 — Strategiepapier, mehrstufig | 6 | 20 |
| **Summe** | **502** | **rund 500** |

**Die Wanduhrzeit ist das eigentliche Problem, nicht das Geld.** Der Container hat vier CPUs, die Nebenläufigkeit liegt damit bei zwei Agenten; das ist eine Eigenschaft der Umgebung und keine des Modells. 502 Aufrufe zu je rund drei Minuten ergeben **rund 12,5 Stunden**. Mit der Zwischenspeicherung aus § 8 zerfällt das in drei Abschnitte von je rund vier Stunden, die nicht an einem Stück laufen müssen.

Zum Vergleich der Entwurfsstand vor dieser Fassung: 538 Aufrufe, rund 590 USD, rund 13,5 Stunden — bei weniger Inhalt, weil die Optionenrunde und die zweite Quantifizierung fehlten. Der Gewinn kommt aus der Verdichtung der Diskussion auf dreißig Rollen und dem Wegfall des Plenums; er wird zu etwa zwei Dritteln wieder in die Optionenrunde investiert.

## 10. Was auch Version 2 nicht leistet

Unverändert gilt `00-Konzept.md` § 4: Die Agenten sind Sprachmodelle mit Rollendossiers, keine befragten Fachleute. Das Ergebnis ist ein strukturiertes Argumentmodell, keine Umfrage und keine Prognose.

Dazu fünf Einschränkungen, die speziell für dieses Verfahren gelten:

- **Die Diskussion bleibt eine Simulation von Widerspruch.** Die Regeln aus § 2 erzwingen Einwände; sie garantieren nicht, dass die Einwände die stärksten verfügbaren sind. Ein Agent, der widersprechen *muss*, widerspricht — notfalls schwach.
- **Die Validierungsinstanz ist selbst ein Sprachmodell.** Sie erkennt erfundene Quellen und falsche Zuschreibungen; sie garantiert nicht, dass eine auffindbare Quelle richtig gelesen wurde. Ob sie zu milde urteilt, ist nach wie vor offen (`07-Pilotbericht.md` § 6).
- **Die Aggregation von P3 ist nur so gut wie die Bezugsgrößen.** Hundert Felder mit teils überlappenden Grundgesamtheiten addieren sich nicht sauber; die Doppelzählung zwischen etwa Bank A und Bank F ist zu prüfen und, wo sie nicht auflösbar ist, als Spanne auszuweisen. Eine Summe mit einer Kommastelle wäre hier eine Lüge.
- **Das Szenariogerüst ist eine Setzung.** Es beseitigt eine Fehlerquelle und schafft eine neue: Alle hundert Rollen teilen jetzt dieselben Annahmen über die Welt, und wenn diese falsch sind, sind alle gleichgerichtet falsch. Die `bedingung`-Karten auf das Gerüst sind das einzige Gegenmittel und müssen in der Auswertung ausdrücklich vorkommen.
- **Das Attributionsproblem wird beziffert, nicht gelöst.** P4 zwingt jede Rolle, den Anteil zu nennen, den sie der KI gegenüber Demografie und Strukturreform zuschreibt. Ob diese Zuschreibung stimmt, kann das Verfahren nicht entscheiden — es kann nur verhindern, dass die Frage unterschlagen wird, und es kann zeigen, ob hundert Felder sie unterschiedlich beantworten.
