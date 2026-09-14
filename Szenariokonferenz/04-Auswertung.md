# Auswertungsvorschrift

Die Auswertung ist vor dem Lauf festgelegt, damit das Ergebnis nicht nachträglich zurechtgelegt werden kann.

## 1. Gültigkeit einer Stimme

Eine Stimme zählt, wenn (a) alle vierzehn quantitativen Größen mit Punktschätzung und 80-%-Intervall belegt sind, (b) K1 bis K4 beantwortet sind, (c) die Werte im plausiblen Bereich liegen (Intervallgrenzen schließen die Punktschätzung ein; keine negativen Anteile; Prozentwerte ≤ 100). Ungültige Stimmen werden gezählt und ausgewiesen, nicht ersetzt.

## 2. Konvergenzmessung

**Primärkriterium.** Ein Archetyp gilt als gesammelt, wenn nach Runde 2 mindestens **25 von 100** gültigen Stimmen auf ihn entfallen **und** der Interquartilsabstand der Größen V1, V5 und V7 innerhalb dieser Gruppe kleiner ist als im Gesamtpanel. Die zweite Bedingung schließt aus, dass ein Archetyp nur deshalb führt, weil sein Wertebereich am weitesten gefasst ist.

**Wenn kein Archetyp die Schwelle erreicht,** lautet das Ergebnis „keine Konvergenz". Berichtet wird dann:
- die zwei bis drei Variablen mit dem größten Interquartilsabstand (die Streitgrößen),
- welche Bänke sich an ihnen gegenüberstehen,
- ob die Uneinigkeit eine Sach- oder eine Interessendifferenz ist (Prüfung: Streuen die Schätzungen *innerhalb* einer Bank ähnlich stark wie *zwischen* den Bänken? Dann ist es Unsicherheit, nicht Interesse).

Dieser Fall ist kein Scheitern. Die Frage „an welchen zwei Größen hängt die Entscheidung" ist für die Politikableitung wertvoller als ein Mehrheitsszenario.

## 3. Weitere auszuweisende Kennzahlen

**Drift (Runde 1 → Runde 2).** Anteil der Agenten, die den Archetyp gewechselt haben; Richtung der Wechsel; Median-Verschiebung je Variable. Hohe Drift bei gleichbleibender Verteilung bedeutet Umschichtung ohne Erkenntnisgewinn; gerichtete Drift bedeutet, dass ein Argument getragen hat.

**Ankerabhängigkeit.** Vergleich der Mediane zwischen den Agenten mit ungerader ID (Substitutionsevidenz zuerst) und gerader ID (Gegenevidenz zuerst). Eine Differenz von mehr als einem Viertel des Interquartilsabstands ist als Ankereffekt zu berichten — sie relativiert das Gesamtergebnis.

**Bankprofile.** Median je Bank für V1, V5, V7, V11. Das zeigt, welche Interessenlage systematisch optimistischer oder pessimistischer urteilt.

**Kalibrierung.** Anteil der Agenten, deren 80-%-Intervalle enger sind als der Interquartilsabstand des Gesamtpanels für dieselbe Größe. Diese Agenten werden als überkonfident markiert; ihre Punktschätzungen gehen normal in die Mediane ein, ihre Konfidenzangabe (V14) wird gesondert ausgewiesen.

**Dissens-Karte.** Für jede Variable: Median, Interquartilsabstand, die beiden Bänke mit den extremsten Medianen, und die jeweils stärkste Begründung von beiden Seiten.

**Quellenqualität.** Anteil quantitativer Behauptungen mit abgerufener Quelle; Anteil, der in der Stichprobenprüfung (Runde 4, mindestens 20 Behauptungen) bestätigt wurde.

## 4. Was im Bericht stehen muss

1. Das Ergebnis der Konvergenzmessung — gesammeltes Szenario oder Dissens-Karte.
2. Die Gegenrede des Red Teams und die benannte Bruchstelle des führenden Szenarios.
3. Die Kennzeichnung nach `00-Konzept.md` § 4: Agenten sind Sprachmodelle mit Rollendossiers, das Ergebnis ist ein strukturiertes Argumentmodell, keine Umfrage und keine Prognose.
4. Die Unterscheidung zwischen Größen, die aus dem US-Modell stammen, und Größen, die das Panel eigenständig für Europa geschätzt hat.
5. Die nicht bestätigten Quellenangaben, sofern welche gefunden wurden.

## 5. Rollen ohne Stimmrecht

| Instanz | Anzahl | Aufgabe |
|---|---|---|
| Red Team | 4 | Widerlegung des führenden Szenarios: ökonomische Konsistenz, politische Zeitachse, technische und physische Annahmen, Datenlage |
| Verifikation | 1 | Stichprobenprüfung quantitativer Behauptungen gegen Quellen und Arbeitspapier |
| Synthese | 1 | Verdichtung von Verteilung, Drift und Gegenrede zum Bericht — ohne Zugriff auf die Verifikation |

Die Trennung von Synthese und Verifikation ist bewusst: Wer das Ergebnis schreibt, prüft es nicht selbst.
