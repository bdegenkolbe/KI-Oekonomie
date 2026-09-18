# Instrumentenkritik — was die beiden Läufe tatsächlich gemessen haben

*Auswertung des Pilotlaufs (14.09.2026, 20 Rollen, Stimmzettel mit Fachteil) und der Mechanismusrunde M (15.09.2026, dieselben 20 Rollen). Grundlage sind die Rohdaten in `rohdaten/`, nicht die Berichtstexte.*

---

## 1. Der zentrale Befund: zwei Instrumente, zwei völlig verschiedene Messergebnisse

Dieselben zwanzig Agenten, dieselben Rollendossiers, derselbe Faktenkern, ein Tag Abstand. Der einzige Unterschied liegt im Zuschnitt der Frage. Das Ergebnis:

| | Runde 1 — Makrogrößen (V1–V14) | Runde M — Mechanismus im eigenen Feld |
|---|---|---|
| Verschiedene Werte je Größe (von 20) | 5 bis 13 | 9 bis 17 |
| Interquartilsabstand, relativ zum Median | 0,00 bis 0,54 | 0,25 bis 0,80 |
| Spannweite (Beispiel) | V7: 44,2 bis 44,9 | m3: 2 bis 90 |
| Begründungstiefe | drei Sätze | 2.000 bis 5.100 Zeichen je Block |

Die Einzelwerte der ersten Runde:

| Größe | verschiedene Werte | Median | IQR | IQR/Median |
|---|---|---|---|---|
| V14 Eigene Konfidenz | **5** | 55,0 | **0,00** | 0,000 |
| V7 Sozialversicherungsbeitragssatz | 7 | 44,5 | 0,40 | 0,009 |
| V6 Arbeitslosenquote | 8 | 6,4 | 0,28 | 0,044 |
| V9 Industriestrompreis | 7 | 16,0 | 1,00 | 0,063 |
| V13 Schockwahrscheinlichkeit | 5 | 70,0 | 5,00 | 0,071 |
| V3 KI-berührte Aufgaben | 6 | 8,0 | 1,00 | 0,125 |
| V8 Diffusionsverzug | 5 | 5,0 | 0,88 | 0,175 |
| V10 RZ-Anschlussleistung | 7 | 2,8 | 0,50 | 0,179 |
| V12 Netto-Abfluss | 6 | 22,0 | 4,00 | 0,182 |
| V2 BIP EU-27 | 13 | 2,4 | 0,55 | 0,229 |
| V11 EU-Souveränitätsgrad | 7 | 20,0 | 5,50 | 0,275 |
| V4 Automatisierungsgrad | 6 | 45,0 | 20,00 | 0,444 |
| V1 BIP Deutschland | 10 | 2,5 | 1,35 | 0,540 |
| V5 Lohnquote | 11 | −1,45 | 0,78 | 0,538 |

**V14 ist der Beleg, der die ganze Auswertung trägt: Zwanzig Rollen aus zwanzig Fachgebieten geben für ihre eigene Konfidenz denselben Wert an — 55.** Der Interquartilsabstand ist exakt null. Eine Größe, die keine Rolle aus ihrem Fachwissen beantworten kann, produziert keine Verteilung, sondern die Vorgabe des Modells. Dasselbe in schwächerer Form bei V6 und V7: Beides sind Größen, für die der Stimmzettel in der Spalte *Referenz* einen Punktwert mitliefert (»rund 6 %«, »rund 42 %«). Die Agenten haben um diesen Wert herum minimal variiert.

Die Gegenprobe steht in derselben Tabelle: V4 trug ebenfalls einen Anker (US-Modell: 75 %), und hier haben die Rollen ihn *verlassen* — Median 45, IQR 20. Das ist die Größe, zu der mehrere Rollen aus ihrem Feld etwas beizutragen hatten. Anker allein erklärt die Enge also nicht; die Regel lautet schärfer:

> **Wo eine Rolle kein Fachwissen einbringen kann, füllt das Modell die Lücke mit seiner eigenen Vorannahme — und weil alle Agenten dasselbe Modell sind, sieht diese Lücke wie Konsens aus.**

Damit ist die Konvergenzmessung der ersten Fassung entwertet. Sechs von zwanzig Stimmen auf Archetyp S2 sind keine 30-Prozent-Häufung von Fachurteilen, sondern eine Häufung der Modellvorannahme, die eine Rollenzuweisung nicht aufbrechen konnte. Die vorab festgelegte Zusatzbedingung aus `04-Auswertung.md` § 2 — engerer IQR in der Gruppe als im Panel — konnte das nicht abfangen, weil der Panel-IQR selbst schon bei null lag.

## 2. Was funktioniert hat

Drei Bestandteile haben in beiden Läufen belastbar geliefert.

**Der Fachteil.** Zwanzig Rollen nennen zwanzig verschiedene bindende Hemmnisse, jedes mit Rechts- oder Institutionengrundlage, keine Dopplung. 100 konkrete Tätigkeiten mit Arbeitszeitanteil. 73 Fachquellen, drei bis fünf je Rolle, alle auffindbar. Das ist das genaue Gegenteil des Makroteils: maximale Divergenz bei prüfbarem Inhalt.

**Die Validierung.** 78 Seitenabrufe und 19 Suchen über zwanzig Prüfinstanzen, keine Instanz ohne Abruf. Drei echte Fachfehler gefunden, darunter eine Quelle, der das Gegenteil ihres Inhalts entnommen wurde. Zu 0,46 USD je Prüfung gegenüber 1,55 USD je Stimmzettel ist das der billigste Bestandteil des Verfahrens und der einzige mit harter Trefferbilanz.

**Die feldverankerte Frage mit Rechenweg-Pflicht (Runde M).** Hier entsteht Streuung *und* Mehrheit gleichzeitig — und beides ist informativ. Die Verteilung der Kreuzungsjahre ist zweigipflig (zwölf Felder bis 2032, acht »nie« oder »nicht vor 2035«), die Kanalaufteilung spreizt von 5 bis 55 Prozent, und quer dazu steht ein klares Mehrheitsurteil von 13 zu 4 zu 3 zum BBG-Effekt. Eine Mehrheit, die sich gegen sichtbare Streuung durchsetzt, ist ein Befund. Eine Mehrheit ohne Streuung ist ein Artefakt.

## 3. Was nicht funktioniert hat

**(a) Der Makroblock misst das Modell, nicht das Panel.** Siehe § 1. Konsequenz für Konzept v2: V1, V2, V3, V6, V7, V13 und V14 verlieren den Status auswertbarer Panelgrößen.

**(b) Einheiten und Skalen sind nicht erzwungen.** Bei V14 haben achtzehn Agenten auf der Skala 0–1 geantwortet (0,45 bis 0,58) und zwei auf 0–100 (55). Der Median 55 in der Tabelle oben entsteht erst nach Normalisierung. Ein Auswertungsschritt, der eine Konvention rät, ist ein Auswertungsschritt zu viel.

**(c) Die Recherche folgte der Struktur des Instruments, nicht der Kompetenz der Rolle.** Im ersten Lauf recherchierten zwölf von 27 Agenten, und fast alle dieselben zwei Größen — Industriestrompreis und Rechenzentrumsleistung, die einzigen *gegenwärtigen* Größen im Stimmzettel. Der Fachteil hat das repariert, aber die Ursache bleibt lehrreich: Agenten recherchieren dort, wo eine Quelle existieren *kann*. Jede Frage nach einem 2030-Wert ist recherchefest und damit rechercheabweisend.

**(d) Es gab nie eine Begegnung.** Beide Läufe sind reine Parallelbefragungen. Jede Rolle hat isoliert geantwortet, kein Agent hat je einen Einwand gegen die Aussage eines anderen formuliert. Die Delphi-Runde des Ursprungskonzepts hätte das nur halb geheilt: Sie zeigt anonymisierte Verteilungen, nicht Argumente. Damit fehlt genau die Operation, die aus zwanzig Einzelurteilen ein gemeinsames Ergebnis machen könnte — und es fehlt der Test, ob eine Fachaussage einem fachfremden Angriff standhält.

**(e) Das Panel ist verzerrt, und die Verzerrung ist einseitig.** Recht, Medizin, Sozialversicherung, Finanzwesen sind stark besetzt — durchweg Felder, in denen Verrechtlichung bremst. Produzierendes Gewerbe, Handel, Logistik, Bau fehlen in den ausgewerteten Antworten. Acht von zwanzig »nie« oder »nicht vor 2035« überschätzen daher die Schutzwirkung von Recht.

**(f) Ungewichtete Mittelwerte über Bezugsgruppen von 3.000 bis 350.000 Beschäftigten.** Ein Faktor von mehr als hundert verschwindet in der Angabe »25,7 Prozent Gewinn«.

**(g) Das Attributionsproblem ist offen.** Die Pflegedirektion sagt es selbst: Bis 2030 falle Beschäftigung in ihrem Feld vermutlich nicht wegen KI weg, sondern wegen Bettenabbau durch die Krankenhausreform. Kein Agent kann Kausalität von Gleichzeitigkeit trennen; das Instrument fragt auch nicht danach.

## 4. Was daraus für das Verfahren folgt

| Befund | Konsequenz in Konzept v2 |
|---|---|
| Makrogrößen messen die Modellvorannahme (§ 1) | Quantifizierung nur noch auf Größen, die aus dem Feld hergeleitet werden — mit Rechenweg vor Ergebnis |
| Fachteil und Validierung tragen (§ 2) | bleiben, werden zum Kern statt zum Anhang |
| Keine Begegnung (§ 3d) | Gruppen- und Plenumsphase mit erzwungenem Einwand |
| Modelle konvergieren im Gespräch von selbst | Diskussion nur über typisierte Karten mit Zielbezug, nicht als freier Chat |
| Skalenchaos (§ 3b) | Schema mit Einheit, Wertebereich und Aufzählungstyp je Feld |
| Panelverzerrung (§ 3e) | Bänke im Gruppenschnitt gemischt, Produktion/Handel/Logistik/Bau verpflichtend besetzt |
| Ungewichtete Mittel (§ 3f) | Bezugsgruppengröße ist Pflichtfeld, Aggregate werden gewichtet *und* ungewichtet ausgewiesen |
| Attribution (§ 3g) | eigenes Pflichtfeld: konkurrierende Ursache neben KI |

---

## 5. Kosten und Laufzeit als Randbedingung

Gemessen: 1,55 USD je Stimmzettel (Opus 5, mit Recherche), 0,46 USD je Prüfung (Sonnet 5). Der Container hat vier CPUs, die Nebenläufigkeit liegt damit bei zwei Agenten. Die Wanduhrzeit skaliert linear mit der Agentenzahl, nicht mit dem Modell — 40 Agenten brauchten 63 Minuten.

Das ist die härteste Randbedingung für jede Diskussionsphase: Eine echte Mehrrunden-Diskussion mit zwanzig Teilnehmern wäre nicht nur teuer, sondern vor allem langsam. Konzept v2 löst das nicht durch Verzicht auf Diskussion, sondern durch ihre Form — schriftliche Kartenzüge auf einer gemeinsamen Tafel statt gesprochener Runden (siehe `11-Konzept-v2.md` § 3).
