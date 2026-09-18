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

## 3. Die Pflichtgrößen

Das ist die tragende Änderung gegenüber der ersten Fassung dieses Konzepts. Ohne eine gemeinsame Größe zerfällt ein Lauf mit hundert Rollen in hundert Dossiers, die nebeneinanderliegen und sich nicht widersprechen können. Runde M hat funktioniert, weil sie **eine** Frage mit **einer** Einheit war.

Jede Rolle beantwortet fünf Größen und eine Gegenprobe — **nicht aus Makroprojektionen, sondern hergeleitet aus dem eigenen Feld**, mit Rechenweg vor dem Ergebnis und mit der Bezugsgruppengröße, die die Recherchebank geliefert hat (§ 5, Runde 0a). Stichjahr ist durchgehend **2031**.

| ID | Größe | Einheit | Wertebereich | Pflichtangaben |
|---|---|---|---|---|
| **P1** | Anteil der heute im eigenen Feld geleisteten Arbeitszeit, der bis 2031 technisch durch KI oder Automatisierung ersetzbar ist — unabhängig davon, ob es geschieht | Prozent | 0–100 | Rechenweg aus Tätigkeiten und Arbeitszeitanteilen, 80-%-Intervall |
| **P2** | Anteil von **P1**, der bis 2031 im Regelbetrieb tatsächlich wirksam wird | Prozent von P1 | 0–100 | das bindende Hemmnis aus geschlossener Liste, 80-%-Intervall |
| **P3** | Veränderung des Personal**bedarfs** im eigenen Feld bis 2031 | Prozent der VZÄ der Bezugsgruppe **und** absolute VZÄ | −100 bis +50 | Bezugsgröße in VZÄ nach R03 mit ihrer Zuordnungsart, Rechenweg, 80-%-Intervall |
| **P3₀** | dieselbe Größe unter der Gegenannahme, dass KI und Automatisierung bis 2031 **stagnieren** | Prozent der VZÄ | −100 bis +50 | Rechenweg |
| **P4** | Ursachenanteil an **P3**: KI und Automatisierung / Demografie und Erwerbspersonenrückgang / Struktur- und Rechtsreform | drei Prozentwerte, Summe 100 | je 0–100 | je Ursache ein Satz, woran man sie erkennen würde |
| **P5** | Verbleib des Effizienzgewinns: beim Leistungserbringer / weitergegeben als Preis oder Beitragssatz / abgeflossen als Lizenz-, Geräte- oder Cloudentgelt überwiegend außerhalb Deutschlands / finanziert zusätzliche Leistung im eigenen Feld | vier Prozentwerte, Summe 100 | je 0–100 | der Vertrag oder Abrechnungsweg, über den der jeweilige Anteil läuft |

**Aus P1, P2, P3 und P3₀ wird eine weitere Größe berechnet, nicht gefragt.**

> **D — Durchgriff** = |P3 − P3₀| ÷ (P1 × P2 ÷ 100)

Im Zähler steht die Veränderung des Personalbedarfs, die der KI zuzurechnen ist, in Prozentpunkten der Bezugsgruppe. Im Nenner steht die bis 2031 tatsächlich eingesparte Arbeitszeit, ebenfalls in Prozentpunkten derselben Bezugsgruppe. D ist damit dimensionslos und sagt, wie viel von der gesparten Stunde beim Stellenbedarf ankommt. Erlaubter Bereich 0 bis 1,5; oberhalb von 1,0 ist eine Begründung verpflichtend, weil dann mehr Bedarf verschwindet als Arbeitszeit.

**D wird gerechnet, nicht geschätzt** — die Rolle kann ihn also nicht direkt setzen, und er kann nicht im Widerspruch zu ihren eigenen Zahlen stehen. Er erscheint in der Zahlenmatrix (§ 4.3), die alle sehen, und ist dort angreifbar wie jede andere Karte.

**Warum D nicht fehlen darf.** In der Mechanikprobe hat das Panel diese Größe von sich aus erfunden, weil es sie brauchte: Fünf der zehn Einwände und die Mehrzahl der Dissenspunkte drehten sich um nichts anderes. Die gemessene Spanne reichte von 0,30 (Landhausarztpraxis, Intensivpflege) bis 0,82 (Medizinische Fachangestellte) — Faktor drei zwischen den Feldern. Und weil die Formel nicht festgelegt war, rechneten die Diskutanten teils mit |P3|, teils mit dem KI-Anteil und kamen für dieselbe Rolle auf 0,53 und auf 0,62; dieser Definitionsstreit hat einen halben Dissenspunkt gekostet (`15-Mechanikprobe.md` § 4). D ist zugleich das Bindeglied zwischen dem Arbeitszeitteil (P1, P2) und dem Stellenteil (P3) — also die Stelle, an der das Strategiepapier steht oder fällt.

**P3₀ ist keine sechste Frage, sondern die Gegenprobe zu P4.** Wer den KI-Anteil an der Veränderung mit 60 % beziffert, muss dieselbe Zahl noch einmal treffen, wenn er die Welt ohne KI durchrechnet. Der KI-Beitrag ist P3 − P3₀, der Beitrag aller übrigen Ursachen ist P3₀, und der abgeleitete Anteil ist ihr Verhältnis am Gesamteffekt:

> **|P3 − P3₀| ÷ (|P3 − P3₀| + |P3₀|)** muss zum P4-Wert für KI passen, Toleranz fünfzehn Punkte.

Weicht beides stärker ab, ist die Attribution geraten und nicht hergeleitet — rechnerisch feststellbar, ohne dass jemand die Antwort beurteilen müsste (§ 6, *Attributionskonsistenz*).

**Warum nicht der naheliegende Quotient (P3 − P3₀) ÷ P3.** Weil P3 die *Netto*veränderung ist und genau dort nahe null liegt, wo KI-Entlastung und Demografiebedarf sich aufheben — also im interessantesten Fall. Die Mechanikprobe hat das gemessen: Drei von zehn Feldern hatten einen Nenner unter 2,5 Punkten, und der Quotient sprang dort auf −200 bis −541 % (`15-Mechanikprobe.md` § 3). Die Formel oben ist gegen kleine Nenner unempfindlich und traf in denselben drei Feldern auf 0,3 Punkte genau.

Die geschlossene Hemmnisliste zu **P2**: *Recht und Zulassung* · *Refinanzierung und Abrechnung* · *Haftung* · *Personalbindung und Tarif* · *Investitionsfähigkeit* · *Akzeptanz von Patienten oder Beschäftigten* · *Datenverfügbarkeit*. Freitext ist als Begründung erlaubt, nicht als Typ.

**Warum gerade diese fünf.** P3 ist die einzige Größe, die sich über hundert Felder **addieren** lässt, sobald jede Rolle ihre Bezugsgröße in Vollkräften nennt — sie trägt damit die Zentraltabelle des Strategiepapiers. Damit die Summe trägt, ist die Zuordnung der Vollkräfte **disjunkt** (§ 5, Runde 0a): Jede Vollkraft gehört genau einem Feld, und Felder, die über dieselben Menschen sprechen, sind als solche ausgewiesen und gehen nicht doppelt in die Summe ein. P1 und P2 zerlegen sie in das technisch Mögliche und das tatsächlich Eintretende, und die Differenz beider ist genau die Stelle, an der der Pilotlauf seine belastbarsten Befunde hatte (`12-Gesamtauswertung.md` § 1, § 5). P4 macht aus dem Attributionsproblem eine Zahl statt eines Bekenntnisses: Wer behauptet, KI verändere das Gesundheitswesen bis 2031, muss beziffern, wie viel davon ohnehin Demografie und Krankenhausreform sind. P5 knüpft an die Frage an, die Runde M mit 13:4:3 beantwortet hat, und liefert dem Arbeitspapier den Abflusskanal, auf den seine Wertschöpfungsabgabe zielt.

**Die Pflichtgrößen werden zweimal beantwortet** — in Runde 1 isoliert und in Runde 3 nach der Diskussion (§ 5, Runde 3). Die Differenz zwischen beiden Erhebungen *ist* das Divergenzerhalt-Kriterium aus `13-Validierungsstand.md` § 3 und muss nicht mehr geschätzt werden.

## 4. Die Tafel

Die Tafel ist kein Bild, sondern eine append-only-Liste typisierter Karten in `rohdaten/tafel.json`. Sie ist gleichzeitig Protokoll des Verfahrens **und** Datenquelle des Dashboards — es gibt keinen Übertragungsschritt zwischen beidem und damit keine Stelle, an der die Darstellung vom Protokoll abweichen könnte.

### 4.1 Kartentypen

| Typ | Wer legt sie | Bezug auf fremde Karte | Pflichtfelder zusätzlich |
|---|---|---|---|
| `position` | jede Rolle, Runde 1 | nein | `feld`, `falsifikator` |
| `befund` | jede Rolle, Runde 1 | nein | `quelle` (abgerufen, mit Datum und Fundstelle) |
| `pflichtgroesse` | jede Rolle, Runde 1 **und** Runde 3 | nein | `groesse_id` (P1–P5), `einheit`, `rechenweg`, `bezugsgroesse_vzae`, `intervall_80` |
| `zahl` | Rollen, jederzeit | optional | `groesse` mit Einheit, 80-%-Intervall, Rechenweg, Bezugsgruppe in VZÄ |
| `einwand` | Rollen, Runde 2 und 3 | **ja** | `einwandtyp` (siehe unten), **`rettungsbedingung`** |
| `bedingung` | Rollen, Runde 2 und 3 | **ja** (auf eigene Position oder auf das Szenariogerüst) | — |
| `dissens` | Gruppenleitung, Runde 2 | **ja** (zwei Karten) | `entscheidungsgroesse` — was gemessen werden müsste |
| `hebel` | Syntheseinstanz, Runde 4 | **ja** (auf Dissens- oder Positionskarten) | `adressat`, `rechtsgrundlage_oder_instrument`, betroffene Bänke |
| `bewertung` | jede Rolle, Runde 4 | **ja** (auf eine `hebel`-Karte) | `urteil` ∈ {wirkt, wirkt nicht, schadet}, `mechanismus`, `nebenwirkung`, `kippbedingung` |
| `beschluss` | Runde 5 | **ja** | Stimmenverhältnis, Gegenstimmen namentlich |

`einwandtyp` ist eine geschlossene Liste: *Faktum bestritten* · *Geltungsbereich zu weit* · *Mechanismus fehlt* · *Gegenbeispiel aus meinem Feld* · *Quelle trägt die Aussage nicht* · *Größenordnung falsch* · *Rechenweg trägt das Ergebnis nicht*. Der letzte Typ ist neu und richtet sich ausdrücklich gegen `pflichtgroesse`-Karten.

**Die Rettungsbedingung ist der Filter gegen den Pflichteinwand ohne Substanz.** Jeder Einwand muss benennen, was zutreffen müsste, damit die angegriffene Karte trotz des Einwands gilt. Eine Höflichkeitsformel kann das nicht leisten: Wer nichts Bestimmtes bestreitet, kann auch nicht angeben, was ihn widerlegen würde. Ein Einwand ohne belastbare Rettungsbedingung wird von der Prüfinstanz als **Leerzug** markiert; er bleibt auf der Tafel, zählt aber in keinem Konvergenzmaß mit (§ 6). Der Zwang aus § 2 Regel 4 erzeugt damit weiterhin schwache Einwände — sie verfälschen nur die Messung nicht mehr.

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
  "quelle_bezugsgroesse": "R03-Faktenblatt, Tabelle 4",
  "zuordnung": "primaer",
  "geruest": "B",
  "modell": "opus"
}
```

`zuordnung` ∈ {`primaer`, `geteilt`, `unbekannt`} entscheidet, ob die Karte in die addierte Gesamtsumme eingeht (§ 5, Runde 0a). `geruest` ∈ {`A`, `B`} hält fest, gegen welches der beiden Szenariogerüste gerechnet wurde, `modell` welches Modell geantwortet hat — beides wird in Runde 0 und 1 zugeteilt und ist die Grundlage der Gerüst- und Modellabhängigkeit in § 6.

`status` wird ausschließlich von der Validierungsinstanz gesetzt: `gueltig` · `mit-vorbehalt` · `zurueckgewiesen` · `leerzug`. Zurückgewiesene Karten werden **nicht gelöscht**, sondern bleiben mit Begründung auf der Tafel und werden im Dashboard ausgegraut. Eine Tafel, von der Fehler verschwinden, ist kein Protokoll.

**Der Status gehört zur Karte, nicht zur Rolle.** Die Prüfinstanz urteilt je Karte und gibt kein Gesamturteil über einen Kartensatz ab. Das ist keine Feinheit: In der Mechanikprobe vergab eine Instanz, die je Rollensatz urteilte, **sechsmal »zurückgewiesen«, viermal »mit Vorbehalt« und kein einziges Mal »gültig«** — jede der zehn Rollen hatte mindestens zwei Beanstandungen, meist berechtigte, meist an einer einzelnen Quelle. Wer daraus einen Filter auf Rollenebene baut, verliert die Hälfte des Panels, ohne dass eine einzige Pflichtgröße widerlegt wäre (`15-Mechanikprobe.md` § 5c). Eine tote Quelle in Befund 1 darf Position, Rechenweg und Pflichtgrößen nicht mitreißen.

### 4.3 Wer welchen Ausschnitt sieht

Die Tafel ist bei hundert Rollen zu groß für jeden Auftrag. Gemessen an der Mechanikprobe: Zehn Rollen erzeugten 167 KB Runde-1-Antworten, hundert erzeugen rund **1.675 KB**; allein Positionen und Befunde sind rund 432 KB, allein die Rechenwege rund 563 KB. Ein Auftrag, der »die Tafel« enthält, ist nicht ausführbar.

Die Lösung ist keine Kürzung der Karten, sondern eine **Zahlenmatrix**: eine Zeile je Rolle mit ID, Feld, Bank, Gerüst, P1, P2, P1 × P2, P3 in Prozent und in VZÄ, P3₀, **D**, P4-KI und P5-Abfluss. Hundert Zeilen sind rund 12 KB. Sie trägt alles, was zum Vergleichen und Angreifen nötig ist, und nichts, was nur zum Lesen schön wäre.

| Runde | Wer | sieht |
|---|---|---|
| 1 | jede Rolle | nichts von den anderen — nur Faktenblätter, eigene Bezugsgröße, zugeteiltes Gerüst |
| 1b | Prüfinstanz | genau einen Kartensatz, sonst nichts |
| 2 | Gruppenmitglied und Gruppenleitung | die Karten der eigenen sechs **vollständig**, dazu die Zahlenmatrix aller hundert und die Streitfrage |
| 3 | jede Rolle | die eigenen Karten, die Einwände gegen sie, alle Dissenspunkte, die Zahlenmatrix |
| 4 | jede Rolle | die Hebelkarten und die Zahlenmatrix |
| 5 | Red Team, Synthese, Verifikation | Volltexte, aber je Aufruf höchstens eine Bank; die Zusammenführung erfolgt über mehrere Aufrufe |

Volltexte fremder Karten außerhalb der eigenen Gruppe stehen niemandem in Runde 2 bis 4 zur Verfügung. Das ist eine Einschränkung und wird als solche im Dashboard ausgewiesen: Ein Einwand gegen eine Karte, die der Angreifer nur als Zahlenzeile gesehen hat, ist etwas anderes als einer gegen den Volltext. Die Mechanikprobe zeigt allerdings, dass die Zahlenzeile trägt — dort entstanden die fünf schärfsten Einwände genau aus dem Vergleich von P1 × P2 gegen P3, also aus Zahlen, nicht aus Prosa.

### 4.4 Einheitenzwang

Jede Karte mit Zahlenwert trägt `einheit` als Aufzählungswert (`prozent` · `prozent_von_p1` · `prozent_vzae` · `prozentpunkte` · `jahre` · `eur_mrd` · `vzae` · `jahreszahl`) und einen erlaubten Wertebereich. Das behebt den Skalenbruch der ersten Fassung, bei dem achtzehn Agenten auf 0–1 und zwei auf 0–100 antworteten und die Auswertung eine Konvention raten musste. Anteilsvektoren (P4, P5) werden auf Summe 100 geprüft und bei Abweichung über drei Punkten zurückgewiesen, nicht normiert.

## 5. Ablauf

### Runde 0 — Recherchebank, Szenariogerüst, Bezugsgrößen

Zehn Rechercheure ohne Stimmrecht liefern je ein Faktenblatt (`14-Roster-2031.md` Teil 1). Drei Lieferungen sind für alles Weitere verbindlich:

**(0a) Bezugsgrößen als disjunkte Zerlegung.** R03 liefert für jedes der hundert Felder die Bezugsgruppe in Vollkräften mit Fundstelle — und zwar so, dass **jede Vollkraft genau einem Feld zugeordnet ist**. Das ist mehr als eine Zahlenliste: Wo zwei Rollen über dieselben Menschen sprechen (der Pflegedirektor in Bank A und die Intensivpflegekraft in Bank C, die Hausärztin in Bank B und der Verband in Bank F), weist R03 die Vollkräfte **einem** Feld als `primaer` zu und dem anderen als `geteilt mit <Feld>`. In die addierte Gesamtsumme gehen nur `primaer`-Felder ein; `geteilt`-Felder liefern ihr Urteil, aber kein Gewicht. Wo keine amtliche Zahl existiert, gilt `unbekannt`.

Ausgewiesen wird zu jeder Summe dreierlei: wie viele Felder sie deckt, wie viele Vollkräfte das sind — und **der Rest**, also die Vollkräfte im deutschen Gesundheitswesen, die kein Feld dieses Rosters abdeckt. Ohne diese drei Angaben ist eine addierte VZÄ-Zahl eine Behauptung über ein Ganzes, von dem niemand weiß, wie viel davon gemessen wurde.

**Wenn eine Rolle ihren Nenner bestreitet.** Das ist kein Randfall: In der Mechanikprobe haben drei von zehn Rollen die vorgegebene VZÄ-Zahl zurückgewiesen und die amtliche Alternative benannt, eine davon mit 18 % Abweichung. Ohne Verfahren rechnet die Rolle dann gegen einen Nenner, den sie für falsch hält, und der Streit verschwindet in einer Zahl, die die Zentraltabelle des Papiers trägt. Deshalb gilt:

1. Die Rolle legt eine `bedingung`-Karte auf die Bezugsgröße, mit Gegenwert und Fundstelle.
2. Sie rechnet P3 **gegen beide Werte** — der vorgegebene bleibt der Hauptwert, der eigene steht daneben.
3. Die addierte Gesamtsumme wird in diesen Feldern als **Spanne** ausgewiesen, nicht als Zahl.
4. R03 prüft die Gegenwerte nach dem Lauf einmal gesammelt; wo die Rolle recht hat, wird die Zerlegung für den nächsten Lauf korrigiert, nicht der laufende nachgerechnet.

**(0b) Zwei Szenariogerüste statt einem.** R08 legt mit R01 und R05 **zwei** ausdrücklich gegensätzliche Rahmen für 2031 fest — je mit BIP-Pfad, Erwerbspersonenpotenzial, Beitragssatzkorridor, Tarifentwicklung, Zinsniveau und dem Stand von EU AI Act, MDR, EHDS und Krankenhausreform:

- **Gerüst A — Fortschreibung:** die amtlichen Projektionen treten ein, die Krankenhausreform wird wie beschlossen umgesetzt, der Rechtsrahmen gilt zum angekündigten Termin.
- **Gerüst B — Gegenwelt:** schwächeres Wachstum, schnellerer Beitragssatzanstieg, verzögerter Vollzug des EU-Rechts, Krankenhausreform in Teilen gescheitert oder landesweise auseinanderlaufend.

Die hundert Rollen werden hälftig zugeteilt — aber **nicht nach derselben Regel wie die Anker-Randomisierung**. Beide an die ID-Parität zu hängen, hieße Anker und Gerüst vollständig zu konfundieren: Zeigte die B-Hälfte höhere Werte, wäre nicht entscheidbar, ob das am Gerüst oder am Anker liegt, und die Gerüstabhängigkeit wäre als Maß wertlos. Stattdessen ein gekreuzter Plan nach dem Zahlenteil der ID modulo vier:

| Rest | Anker | Gerüst |
|---|---|---|
| 1 | Substitutionsevidenz zuerst | A |
| 2 | Gegenevidenz zuerst | A |
| 3 | Substitutionsevidenz zuerst | B |
| 0 | Gegenevidenz zuerst | B |

Damit sind bei hundert Rollen alle vier Zellen mit rund 25 besetzt, und Anker- und Gerüstwirkung lassen sich getrennt schätzen. **Die Differenz der Pflichtgrößen zwischen beiden Hälften ist damit eine gemessene Größe** (§ 6, *Gerüstabhängigkeit*) und kein blinder Fleck. Ein einziges Gerüst hätte alle hundert Rollen in denselben Weltannahmen gleichgerichtet: Wäre eine Annahme falsch, irrte das Panel geschlossen und ohne Streuung — also in genau der Form, die im ersten Lauf als Konsens missdeutet worden wäre. Wer auch von seinem zugeteilten Gerüst abweichen will, legt zusätzlich eine `bedingung`-Karte darauf.

**(0c) Gegenwartswerte** mit Fundstelle, Erhebungsdatum und ausdrücklich benannten Lücken, je Domäne.

Damit wird zugleich der Konstruktionsfehler des ersten Laufs behoben: Dort recherchierten zwölf von 27 Rollen, und fast alle dasselbe, weil das Instrument nur zwei gegenwärtige Größen enthielt.

### Runde 1 — Eigenrecherche, Position, Pflichtgrößen (isoliert)

Jede der hundert Rollen arbeitet allein und sieht nichts von den anderen — nur die Faktenblätter und das Szenariogerüst. Sie recherchiert in **ihrem** Feld. Ergebnis je Rolle:

- eine `position`-Karte: die These zum eigenen Feld bis 2031, mit dem Satz, der sie widerlegen würde
- drei bis sechs `befund`-Karten, jede mit abgerufener Quelle, Datum und Fundstelle
- sechs `pflichtgroesse`-Karten P1 bis P5 und P3₀, Rechenweg vor Ergebnis
- optional weitere `zahl`-Karten zu Größen, die aus dem eigenen Feld hergeleitet sind

**Modellkontrollarm.** Zehn der hundert Rollen — je eine aus zehn verschiedenen Bänken, vorab festgelegt — durchlaufen Runde 1 und Runde 3 ein zweites Mal mit **identischem Auftrag auf einem anderen Modell**. Die Differenz zwischen beiden Antworten derselben Rolle ist die **Modellabhängigkeit** (§ 6). Das schließt die Lücke, an der der erste Lauf gescheitert ist: Dort war erst in der nachträglichen Rohdatenauswertung erkennbar, dass eine Variable die Vorannahme des Modells statt das Urteil der Rollen maß. Übersteigt die Modellabhängigkeit die Streuung im Panel, misst die betreffende Pflichtgröße das Modell — und wird nicht berichtet, sondern verworfen.

Gestrichen gegenüber Version 1: V1, V2, V3, V6, V7, V13, V14. Keine Rolle schätzt mehr das deutsche BIP 2031 oder ihre eigene Konfidenz. Was das Panel zu Makrogrößen zu sagen hat, entsteht aus der Aggregation von P3 über die Bezugsgruppen — oder gar nicht.

### Runde 1b — Validierung

Unverändert aus `06-Validierung.md`, aber auf Kartenebene: Existenz der Quelle, Deckung der Aussage, Mandatstreue, fachliche Plausibilität. Neu hinzu für `pflichtgroesse`-Karten: **Rechenweghaltbarkeit** — der genannte Rechenweg muss den genannten Wert aus der genannten Bezugsgröße reproduzieren. Für `einwand`-Karten: trägt die Rettungsbedingung, oder ist der Zug leer (§ 4.1)? Der Prüfauftrag muss dabei den **Pflichtteil vom Freitext trennen**: P1 bis P5 sind von jeder Rolle verbindlich zu beantworten und deshalb nie ein Mandatsbruch, auch wenn sie über das engste Fachgebiet hinausreichen. Ohne diesen Hinweis beanstandet die Prüfinstanz die Pflichtfragen selbst — zweimal geschehen in der Mechanikprobe (`15-Mechanikprobe.md` § 5a). Kleines Modell. **Gefiltert wird je Karte, nie je Rolle:** Zurückgewiesene Einzelkarten scheiden aus der Weiterverarbeitung aus, alle übrigen Karten derselben Rolle bleiben im Verfahren, und die Rolle selbst bleibt in jedem Fall stimmberechtigt. Zurückgewiesene Karten und Leerzüge bleiben auf der Tafel sichtbar.

Eine Rolle fällt nur dann ganz aus der Auswertung, wenn **alle sechs Pflichtgrößen** zurückgewiesen sind — dann fehlt ihr die gemeinsame Sprache. Wie oft das eintritt, ist auszuweisen; in der Mechanikprobe wäre es null von zehn Mal gewesen.

**Gesetzte Fehler.** Ob die Prüfinstanz zu milde urteilt, war bisher offen (`07-Pilotbericht.md` § 6) — eine Instanz, die alles durchwinkt, ist von einer, die alles prüft, am Ergebnis nicht zu unterscheiden. Deshalb werden **zehn Prozent der vorgelegten Karten vorher maschinell verfälscht**: eine geänderte Ziffer, eine Quelle, die die Aussage nicht deckt, eine Rolle, die außerhalb ihres Mandats spricht. Welche Karten das sind, weiß die Auswertung und nicht die Prüfinstanz. Ihre **Trefferquote auf den gesetzten Fehlern** ist damit eine gemessene Zahl. Liegt sie unter 80 %, ist nicht eine Karte widerlegt, sondern die gesamte Validierung wertlos, und der Lauf bricht ab. Die verfälschten Karten werden nach der Prüfung durch ihre Originale ersetzt; sie gehen in kein inhaltliches Ergebnis ein.

### Runde 2 — Gruppendiskussion der dreißig Strittigsten

Nicht alle hundert diskutieren. Wer nahe am Median liegt, hat der Tafel in einer Diskussion wenig hinzuzufügen und erzeugt vor allem Karten desselben Typs. Ausgewählt werden **dreißig Rollen nach einer rechnerischen Regel, nicht nach Urteil**:

> Für P1, P2, P3 und **D** wird gegen den Median der **eigenen Bank** gerechnet: *d* = |*x* − Median(*g*, Bank)| ÷ max(IQR(*g*, Bank), Mindestspreizung(*g*)).
> Für P4 und P5 wird gegen den Median des **gesamten Panels** gerechnet, und an die Stelle des Betrags tritt die halbe Summe der absoluten Abweichungen vom Medianvektor.
> Der **Streitindex** einer Rolle ist die Summe dieser sechs Werte. P3₀ geht nicht ein: Es ist die Gegenprobe zu P4 und keine eigene Streitfrage.

D geht ein, obwohl es aus P1, P2, P3 und P3₀ berechnet wird — das ist keine Doppelzählung. Eine Rolle kann bei allen vier Ausgangsgrößen nahe am Median liegen und trotzdem einen ungewöhnlichen Durchgriff haben, weil D ein Verhältnis ist. Und der Durchgriff ist nach der Mechanikprobe genau das, worüber gestritten wird.

Die Trennung ist nicht kosmetisch. P1 bis P3 sind feldabhängig: Dass die Radiologie einen höheren automatisierbaren Arbeitszeitanteil nennt als die Intensivpflege, ist kein Streit, sondern der Unterschied der beiden Felder. Gegen den Panelmedian gemessen kämen genau die Rollen in die Diskussion, deren Feld ungewöhnlich ist — nicht die, deren *Urteil* ungewöhnlich ist. Innerhalb der Bank fällt der Feldeffekt weitgehend heraus, und übrig bleibt die Abweichung im Urteil. P4 und P5 dagegen sind Mechanismusfragen: Wie viel der Veränderung der KI zuzurechnen ist und wohin der Gewinn fließt, ist zwischen den Feldern unmittelbar vergleichbar, und dort ist die Abweichung vom Gesamtpanel genau das Gesuchte.

Die Mindestspreizung je Größe (P1, P2: 5 Punkte; P3: 3 Punkte; D: 0,10; P4, P5: 8 Punkte) ist vorab festgelegt und verhindert die Division durch null, in die der erste Lauf gelaufen wäre — dort war der IQR einer Variablen exakt null (`10-Instrumentenkritik.md` § 1). Bänke mit weniger als sechs Rollen (M, N) haben keinen belastbaren Bankmedian; für sie gilt der Median der nächstgrößeren verwandten Bank, vorab festgelegt: M rechnet gegen K, N gegen J.

Besetzt werden zuerst **vierzehn Plätze, einer je Bank** (die Rolle mit dem höchsten Streitindex ihrer Bank), danach die **sechzehn** verbleibenden nach Streitindex über alle Bänke. Die Bankquote ist notwendig, weil sonst zwei streitfreudige Bänke die ganze Diskussion stellen und das Verfahren genau die feldübergreifende Deckung verliert, deretwegen es gebaut ist.

Die dreißig sitzen in **fünf Gruppen à sechs, quer zu den Bänken** geschnitten: in jeder Gruppe eine Leistungserbringer-, eine Kostenträger-, eine Aufsichts-, eine Arbeitnehmer- und eine gesamtwirtschaftliche Perspektive. Die Gruppenleitung clustert die validierten Karten und formuliert daraus **die Streitfrage der Gruppe** — sie wird nicht vorgegeben, sie wird gefunden. Dann zwei Kartenzüge je Rolle mit den Pflichtzügen aus § 2 Regel 4.

**Die siebzig Nichtdiskutierenden sind nicht ausgeschlossen.** Ihre Karten aus Runde 1 liegen auf der Tafel und dürfen angegriffen werden; wer angegriffen wurde, antwortet in Runde 3, die er ohnehin durchläuft. Die Diskussion ist damit kein geschlossener Kreis, sondern eine Verdichtung.

Jede Gruppe schließt mit einem `dissens`-Eintrag je offenem Streitpunkt, der drei Dinge benennt: die beiden unvereinbaren Karten, welche Bänke sich gegenüberstehen, und **die Entscheidungsgröße** — was man messen müsste, um den Streit zu beenden. Letzteres ist der eigentliche Ertrag der Runde: Nicht die Einigung, sondern die Benennung dessen, woran die Uneinigkeit hängt.

### Runde 3 — Pflichtgrößen zum zweiten Mal

Alle hundert Rollen sehen jetzt sämtliche Dissens-Einträge, die Einwände gegen ihre eigenen Karten, die Streitfragen der fünf Gruppen und die Zahlenmatrix (§ 4.3) — Volltexte fremder Karten nicht. Jede Rolle liefert in einem Aufruf:

1. die sechs Pflichtgrößen **erneut**, mit Rechenweg — Änderung erlaubt, Begründung der Änderung verpflichtend, Nichtänderung ebenfalls zu begründen; das zugeteilte Szenariogerüst bleibt dasselbe wie in Runde 1, sonst wäre die Differenz nicht die Wirkung der Diskussion
2. eine Antwort auf jeden Einwand, der gegen ihre Karten gelegt wurde (`einwand` oder `bedingung`)
3. bei mindestens einem Dissenspunkt eine Stellungnahme aus der eigenen Feldsicht

Ein eigenes Plenum entfällt. Es hätte dasselbe geleistet und hundert Aufrufe zusätzlich gekostet — die Kreuztischwirkung entsteht hier dadurch, dass jede Rolle die Dissenspunkte *aller* fünf Gruppen vor sich hat.

Eine `beschluss`-Karte entsteht am Ende dieser Runde, wenn eine Position keinen unbeantworteten Einwand mehr trägt. Sie führt das Stimmenverhältnis und die Gegenstimmen namentlich. Eine Position, die nie angegriffen wurde, wird **nicht** zum Beschluss — sie bleibt Position, und das Dashboard weist sie als ungeprüft aus.

Gezählt wird pro Pflichtgröße: Median, Interquartilsabstand, **gewichtet nach Bezugsgruppe und ungewichtet nebeneinander** — und zwar für beide Erhebungen getrennt, je Bank und über das ganze Panel. Zusätzlich ausgewiesen werden das Produkt P1 × P2, der bis 2031 tatsächlich automatisierte Arbeitszeitanteil, und der Durchgriff **D**, der beide Teile verbindet. P1 × P2 erlaubt den Vergleich mit externen Automatisierungsstudien; D erklärt, warum daraus kein Stellenabbau folgen muss. Beide sind für Runde 1 und Runde 3 getrennt auszuweisen — eine Bewegung in D ist die aussagekräftigste Einzelbewegung des ganzen Verfahrens, weil sie genau die Größe betrifft, die die Diskussion trägt. P3 wird zusätzlich über alle Felder mit bekannter Bezugsgröße zu einer Summe in Vollkräften aggregiert, mit ausgewiesener Abdeckung («diese Summe deckt *n* von 100 Feldern und *m* Vollkräfte»).

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

Angriffsüberleben und feldübergreifende Deckung zählen **nur Einwände, die keine Leerzüge sind** (§ 4.1). Eine Position, die nur von substanzlosen Pflichteinwänden getroffen wurde, gilt nicht als geprüft, sondern als ungeprüft.

Dazu vier **Gültigkeitsmaße**. Sie sagen nichts über den Inhalt, sondern darüber, ob die Zahlen überhaupt etwas über die Sache aussagen — und sie werden **je Pflichtgröße** berechnet und neben jedem berichteten Wert ausgewiesen:

| Maß | Definition | Konsequenz |
|---|---|---|
| **Prüfschärfe** | Anteil der maschinell gesetzten Fehler, die die Prüfinstanz gefunden hat (§ 5, Runde 1b) | unter 80 % ist die Validierung wertlos und der Lauf abzubrechen |
| **Modellabhängigkeit** | mittlere Differenz zwischen den beiden Antworten derselben Rolle auf zwei Modellen, im Verhältnis zum Panel-IQR derselben Größe | über 1 misst die Größe das Modell und wird nicht berichtet |
| **Gerüstabhängigkeit** | Abstand der Mediane zwischen Gerüst-A- und Gerüst-B-Hälfte, im Verhältnis zum Panel-IQR | über 1 wird die Größe getrennt nach Gerüst berichtet, nie zusammengefasst |
| **Attributionskonsistenz** | Anteil der Rollen, bei denen \|P3 − P3₀\| ÷ (\|P3 − P3₀\| + \|P3₀\|) um höchstens 15 Punkte vom P4-Wert für KI abweicht | unter 80 % ist die Attribution des Panels geraten und in den abweichenden Feldern als solche zu kennzeichnen |

Keines dieser Maße lässt sich durch Höflichkeit erzeugen. Alle acht lassen sich aus dem Kartengraphen berechnen, ohne dass eine Instanz sie interpretieren muss. Drei von ihnen — Prüfschärfe, Modellabhängigkeit, Gerüstabhängigkeit — hätten den Fehlschlag des ersten Laufs **während** des Laufs angezeigt statt in der nachträglichen Rohdatenauswertung.

## 7. Das Dashboard

Eine eigenständige HTML-Seite nach `Formatvorlage.md`, ohne externe Abhängigkeiten außer der Schrift, gespeist aus `tafel.json`. Sechs Ansichten auf denselben Datensatz:

**(1) Tafel.** Der Kartengraph selbst, gruppiert nach den fünf Gruppen, Karten als Kacheln, Einwände als Verbindungen. Filter nach Kartentyp, Bank, Runde und Status. Klick auf eine Karte öffnet Volltext, Quelle und alle eingehenden Einwände. Zurückgewiesene Karten ausgegraut, nicht versteckt.

**(2) Pflichtgrößen.** Je Größe ein Punktdiagramm der hundert Einzelwerte mit 80-%-Intervall, **Runde 1 und Runde 3 nebeneinander**, gewichtet und ungewichtet. Jeder Punkt klickbar auf den Rechenweg. Kein Balkendiagramm von Mittelwerten — die Spreizung ist der Befund (`10-Instrumentenkritik.md` § 2).

**(2b) Durchgriff.** Die Zahlenmatrix aus § 4.3 als sortierbare Tabelle, dazu P1 × P2 gegen P3 als Streudiagramm mit D als Steigung. Wer wissen will, warum ein Feld viel Arbeitszeit spart und trotzdem keine Stellen verliert, liest es hier ab — und sieht sofort, welche Felder aus der Reihe fallen.

**(3) Streit.** Die Dissenskarte: je Streitpunkt die beiden Positionen nebeneinander, die Bänke, die Entscheidungsgröße. Dazu die Streitindex-Rangliste, aus der die dreißig Diskutierenden hervorgegangen sind — die Auswahl ist damit nachprüfbar und nicht behauptet.

**(4) Hebel.** Je Hebel eine Matrix aus hundert Feldern × drei Urteilen, Kippbedingungen als aufklappbare Liste. Sortierbar nach Anteil `schadet`, nicht nach Zustimmung.

**(5) Attribution.** Die P4-Zerlegung über alle Felder, als gestapelte Anteile nach Bank — die Antwort auf die Frage, wie viel von 2031 überhaupt der KI zuzurechnen wäre. Daneben die Gegenprobe aus P3₀ und die Attributionskonsistenz je Rolle.

**(5b) Gültigkeit.** Eine eigene Ansicht für die vier Maße aus § 6: Prüfschärfe mit der Liste der gesetzten Fehler und was die Prüfinstanz mit ihnen gemacht hat, Modellabhängigkeit als Gegenüberstellung der zehn doppelt gelaufenen Rollen, Gerüstabhängigkeit als zwei Verteilungen je Pflichtgröße, Attributionskonsistenz als Streudiagramm. Diese Ansicht steht **vor** den inhaltlichen Ansichten, nicht im Anhang: Wer die Zahlen liest, soll zuerst sehen, wie weit sie tragen.

**(6) Zeitachse.** Der Verlauf über die Runden: wann welche Karte kam, welche Position wann angegriffen wurde, was überlebt hat, welche Zahl sich zwischen Runde 1 und Runde 3 bewegt hat. Das macht das Verfahren nachvollziehbar statt nur sein Ergebnis.

Durchgehend sichtbar bleibt die Kennzeichnung nach § 10: Agenten sind Sprachmodelle mit Rollendossiers.

## 8. Lauffähigkeit

Ein Lauf dieser Größe dauert länger als eine Sitzung (§ 9). Die Mechanikprobe hat gezeigt, welche Mechanik dafür tatsächlich zur Verfügung steht — und welche nicht.

**Was es nicht gibt.** Ein Workflow-Skript hat **keinen Dateisystemzugriff**. Die frühere Fassung dieses Abschnitts verlangte, nach jeder Runde den Zwischenstand nach `rohdaten/lauf/<phase>.json` zu schreiben und im Laufprotokoll die Kosten je Aufruf zu führen. Beides ist aus dem Skript heraus nicht möglich. Die Anforderung stand da, ohne dass irgendjemand sie hätte erfüllen können.

**Was es gibt, und was die Probe bestätigt hat:**

**Zwischenspeicherung je Aufruf statt je Phase.** Die Umgebung schreibt für jeden abgeschlossenen Agenten eine Zeile mit seiner vollständigen Rückgabe in ein Laufjournal. Das ist feiner als geplant: Verloren geht höchstens der eine Aufruf, der gerade lief, nicht eine ganze Phase.

**Wiederaufsetzen über die Lauf-Kennung.** Ein Neustart mit derselben Kennung liefert jeden Aufruf, dessen Auftrag unverändert ist, aus dem Journal zurück und führt nur Neues oder Geändertes wirklich aus. Das trägt zugleich die Nachbearbeitung: Wer nur die Auswertung am Ende ändern will, ändert das Skript und lässt die 533 Agenten aus dem Zwischenspeicher laufen. Damit ist der Lauf über mehrere Sitzungen fortsetzbar, ohne dass eine eigene Speicherlogik nötig wäre.

**Wiederholung je Agent.** Fehlgeschlagene Aufrufe werden von der Umgebung wiederholt; wer danach nicht antwortet, liefert einen leeren Wert zurück, und der Lauf läuft weiter. Diese Werte sind vor der Auswertung auszufiltern und ihre Zahl ist auszuweisen — eine ausgefallene Rolle darf nicht neunundneunzig andere kosten, muss aber im Ergebnis sichtbar bleiben. In der Mechanikprobe waren es null von 57.

**Das Herausschreiben geschieht nach dem Lauf.** Rohdaten und Tafel werden aus der Rückgabe des Skripts nach `rohdaten/` geschrieben, nicht aus dem Skript heraus. Das ist ein Arbeitsschritt und keine Fußnote: Wird er vergessen, hängt alles am Journal der Sitzung.

**Die Kosten bleiben eine Schätzung.** Die tatsächliche Abrechnung ist aus dem Lauf nicht auslesbar. Belastbar ist allein der Tokenverbrauch — die Mechanikprobe meldete 4,52 Mio Token für 57 Aufrufe, also rund 79.000 je Aufruf. Jede USD-Angabe in § 9 ist eine Hochrechnung aus früher gemessenen Stückkosten und als solche zu lesen.

## 9. Kosten und Laufzeit

Hochgerechnet aus den gemessenen Stückkosten (1,55 USD je recherchierender Opus-Aufruf, 0,46 USD je Prüfung mit kleinem Modell; Karten- und Bewertungszüge ohne Recherche, aber mit wachsendem Tafelkontext, mit 0,60 bis 1,00 USD angesetzt):

| Phase | Aufrufe | USD |
|---|---|---|
| Runde 0 — zehn Faktenblätter, mehrere Abrufe je Blatt | 10 | 30 |
| Runde 0 — disjunkte Bezugsgrößen, Gerüst A, Gerüst B | 3 | 9 |
| Runde 1 — Position, Befunde, sechs Pflichtgrößen, mit Eigenrecherche | 100 | 155 |
| Runde 1 — Modellkontrollarm, zehn Rollen auf zweitem Modell | 10 | 6 |
| Runde 1b — Validierung mit gesetzten Fehlern, kleines Modell | 110 | 51 |
| Streitauswahl nach § 5 Runde 2 | 0 (rechnerisch) | 0 |
| Runde 2 — dreißig Rollen × zwei Kartenzüge | 60 | 60 |
| Runde 2 — fünf Gruppenleitungen × Streitfrage und Dissensprotokoll | 10 | 6 |
| Runde 3 — Pflichtgrößen zum zweiten Mal, Antwort auf Einwände | 100 | 100 |
| Runde 3 — Modellkontrollarm | 10 | 6 |
| Runde 4 — Hebelsatz aus der Tafel | 2 | 4 |
| Runde 4 — Optionenbewertung je Rolle | 100 | 60 |
| Runde 5 — Red Team, Synthese, Verifikation | 12 | 16 |
| Runde 6 — Strategiepapier, mehrstufig | 6 | 20 |
| **Summe** | **533** | **rund 525** |

**Die Wanduhrzeit ist das eigentliche Problem, nicht das Geld.** Der Container hat vier CPUs, die Nebenläufigkeit liegt damit bei zwei Agenten; das ist eine Eigenschaft der Umgebung und keine des Modells.

Der frühere Ansatz von drei Minuten je Aufruf ist **gemessen widerlegt**: Die Mechanikprobe brauchte für 57 Aufrufe zwei Stunden und zwei Minuten, also **4,28 Minuten je Aufruf** bei Nebenläufigkeit zwei (`15-Mechanikprobe.md` § 5b). Hochgerechnet ergeben 533 Aufrufe damit **rund 19 Stunden** statt der zuvor angesetzten 13,3. Mit der Zwischenspeicherung aus § 8 zerfällt der Lauf in drei Abschnitte von rund 8,3, 6,4 und 4,3 Stunden, die nicht an einem Stück laufen müssen.

**Was die Gültigkeitsmaße kosten.** Modellkontrollarm, zweites Szenariogerüst und gesetzte Fehler schlagen mit 31 Aufrufen und rund 25 USD zu Buche — fünf Prozent des Laufs. Dafür sind die drei Fragen, an denen der erste Lauf gescheitert ist, nicht mehr offen: ob die Zahlen das Modell messen, ob sie an einer Weltannahme hängen und ob die Prüfinstanz überhaupt prüft. Das ist der billigste Teil dieses Verfahrens und der einzige, der es von einer aufwendig verpackten Modellabfrage unterscheidet.

Zum Vergleich der Entwurfsstand vor dieser Fassung: 538 Aufrufe, rund 590 USD, rund 13,5 Stunden — bei deutlich weniger Inhalt, weil Optionenrunde, zweite Quantifizierung und sämtliche Gültigkeitsmaße fehlten.

## 10. Was bleibt

Sechs Schwächen dieses Verfahrens waren in der vorigen Fassung nur benannt. Sie sind jetzt jeweils durch einen Mechanismus ersetzt, der sie entweder beseitigt oder in eine Zahl verwandelt, die neben dem Ergebnis steht:

| Schwäche | Mechanismus | Rest |
|---|---|---|
| Die Prüfinstanz könnte alles durchwinken | zehn Prozent gesetzte Fehler, Trefferquote als Abbruchkriterium (§ 5, Runde 1b) | gemessen wird die Schärfe gegenüber **gesetzten** Fehlertypen; unbekannte Fehlerarten bleiben unerfasst |
| Alle hundert Rollen sind dasselbe Modell | Kontrollarm: zehn Rollen doppelt auf einem zweiten Modell, Modellabhängigkeit je Pflichtgröße (§ 5, Runde 1) | auch das zweite Modell ist ein Sprachmodell mit verwandten Vorannahmen; gleichgerichtete Irrtümer beider bleiben unsichtbar |
| Ein Szenariogerüst macht das Panel gleichgerichtet falsch | zwei gegensätzliche Gerüste, hälftig zugeteilt, Gerüstabhängigkeit je Pflichtgröße (§ 5, Runde 0b) | zwei Setzungen sind nicht die Welt; eine Annahme, die **beide** Gerüste teilen, bleibt ungeprüft |
| Erzwungene Einwände sind notfalls leer | Rettungsbedingung als Pflichtfeld, Leerzüge zählen in keinem Maß mit (§ 4.1) | der Zwang erzeugt weiterhin schwache Einwände; sie verfälschen nur die Messung nicht mehr |
| P3 addiert sich über überlappende Bezugsgruppen nicht sauber | disjunkte Zuordnung durch R03, nur `primaer`-Felder gehen in die Summe, Deckung und Rest werden ausgewiesen (§ 5, Runde 0a) | die Zerlegung ist eine Entscheidung von R03 und an den Grenzen strittig; sie ist dokumentiert, nicht objektiv |
| Die Attribution auf KI könnte geraten sein | Gegenprobe P3₀ und Attributionskonsistenz (§ 3, § 6) | Konsistenz ist nicht Richtigkeit: Eine Rolle kann sich zweimal im selben Sinn irren |

Fünf weitere hat die Mechanikprobe aufgedeckt; sie sind in dieser Fassung behoben:

| Befund der Probe | Änderung | Rest |
|---|---|---|
| Die Tafel ist bei hundert Rollen rund 1.675 KB groß und passt in keinen Auftrag | Zahlenmatrix als gemeinsamer Ausschnitt, Volltexte nur in der eigenen Gruppe (§ 4.3) | Einwände gegen eine bloße Zahlenzeile sind schwächer als gegen den Volltext; das ist auszuweisen |
| Ein Urteil je Rollensatz hätte 60 % des Panels ausgeschlossen | Status gehört zur Karte, nicht zur Rolle (§ 4.2, § 5 Runde 1b) | eine Rolle mit sechs zurückgewiesenen Pflichtgrößen fällt weiterhin aus — zu Recht |
| Das Panel stritt über eine Größe, die das Konzept nicht kannte | **D**, der Durchgriff, wird berechnet und ausgewiesen (§ 3) | D erbt die Unsicherheit aller vier Größen, aus denen er entsteht |
| § 8 verlangte eine Zwischenspeicherung, die das Werkzeug nicht kann | auf die vorhandene Mechanik umgeschrieben (§ 8) | die Kosten bleiben eine Schätzung, weil die Abrechnung nicht auslesbar ist |
| Drei von zehn Rollen bestritten ihren Nenner, ohne dass es ein Verfahren gab | `bedingung`-Karte, Rechnung gegen beide Werte, Summe als Spanne (§ 5 Runde 0a) | wo Haupt- und Gegenwert weit auseinanderliegen, wird die Zentraltabelle unscharf statt falsch |

Was dadurch **nicht** behoben ist und sich mit diesem Verfahren auch nicht beheben lässt:

**Die Agenten sind Sprachmodelle mit Rollendossiers, keine befragten Fachleute.** Das Ergebnis ist ein strukturiertes Argumentmodell mit benannten Quellen und offengelegten Dissenspunkten — keine Umfrage, keine Prognose und keine Legitimationsgrundlage für eine politische Entscheidung. Alle Mechanismen dieses Abschnitts machen die Grenzen des Modells messbar; sie verwandeln das Modell nicht in ein Panel.

**Das Attributionsproblem bleibt sachlich offen.** P4 und P3₀ zwingen zur Bezifferung und machen Widersprüche sichtbar. Ob die Wirkung im Jahr 2031 der KI, der Demografie oder der Krankenhausreform zuzurechnen ist, kann kein Verfahren entscheiden, das keine Kontrollgruppe hat — und eine Volkswirtschaft ohne KI gibt es nicht zum Vergleich.

**Die Gültigkeitsmaße können selbst reißen.** Prüfschärfe unter 80 % bricht den Lauf ab; Modellabhängigkeit über 1 verwirft eine Pflichtgröße; Gerüstabhängigkeit über 1 zwingt zur getrennten Berichterstattung. Das ist der Zweck dieser Maße und kein Fehler des Verfahrens — aber es heißt, dass ein Lauf über 525 USD mit dem Ergebnis enden kann, dass zwei der Pflichtgrößen nicht berichtbar sind. Die Mechanikprobe hat diesen Fall schon einmal geliefert: Die Attributionskonsistenz riss, auch nach Korrektur der Formel (`15-Mechanikprobe.md` § 3). Genau dafür steht die Probe vor dem Lauf.
