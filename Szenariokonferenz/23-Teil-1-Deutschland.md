# Strategiepapier 2031 — Teil 1: Deutschland und das Gesundheitswesen

*Fassung nach der zweiten Erhebung (`25-Sitzung-B.md`). Die Zahlen sind damit Ergebnisse und nicht mehr Eingaben. Alle Zahlen sind Modellergebnisse und stehen im Konjunktiv (`Claude.md` § 4.2). Gültigkeitsgrenzen in `22-Teil-0-Gueltigkeit.md`.*

---

## 1. Der Satz, um den es geht

Hundert Felder des deutschen Gesundheitswesens haben dieselbe Frage für ihr eigenes Feld gerechnet. Sie kommen zu einem Ergebnis, das weder der Entlastungs- noch der Freisetzungserzählung entspricht:

> **Künstliche Intelligenz nähme dem Personalbedarf bis 2031 nicht seinen Anstieg, sondern gut ein Drittel davon.**

Auf den 2,16 Mio Vollkräften, für die eine belegte und im Zuschnitt geprüfte Bezugsgröße vorliegt, stiege der Personalbedarf bis 2031 um **+123.684 Vollkräfte**. Unter der Gegenannahme, dass KI und Automatisierung stagnieren, stiege er um **+201.717**. Die Differenz von rund **78.000 Vollkräften** ist der gesamte Beitrag der Technik — er dämpft, er kehrt nicht um.

Nach der Diskussion fällt dieser Beitrag kleiner aus als davor: In der ersten Erhebung waren es 86.000 Vollkräfte, in der zweiten 78.000. Die Richtung ist über beide Spalten konsistent — mehr Bedarf, weniger KI-Wirkung.

## 2. Die Zentraltabelle

Personalbedarf 2031 gegenüber heute. Deckung: **2.155.154 Vollkräfte, 48,9 %** des amtlichen Rahmens von 4,4 Mio Vollzeitäquivalenten.

Sechs Zeilen tragen eine **korrigierte** Bezugsgröße (mit \*): Dort hatte die Abbildung der Nacharbeit dem Feld die ganze Einrichtungsart zugewiesen, während die Rolle nachweislich über einen engeren Ausschnitt rechnete. Maßgeblich ist der von der Rolle selbst belegte Gegenwert (§ 3).

| Feld | Bezugsgruppe | Vollkräfte | P3 | 2031 | ohne KI |
|---|---|---:|---:|---:|---:|
| A06 | Krankenhäuser, med.-techn. Dienst | 166.256 | −8,2 % | −13.633 | −9.144 |
| B08 | Apotheken | 136.000 | −10,0 % | −13.600 | −4.080 |
| A09 | Krankenhäuser, Funktionsdienst | 112.027 | −7,8 % | −8.738 | −4.481 |
| E06 \* | fachärztliche Labore außerhalb der Krankenhäuser | 22.000 | −10,3 % | −2.266 | +1.672 |
| A01 | Krankenhäuser, ärztlicher Dienst | 180.418 | −0,8 % | −1.443 | +5.413 |
| E07 \* | vollversorgender Pharmagroßhandel | 24.000 | −6,0 % | −1.440 | +1.440 |
| E02 \* | Medizintechnik Bildgebung | 28.000 | −3,7 % | −1.036 | +1.680 |
| A02 | Krankenhäuser, Verwaltungsdienst | 70.542 | −1,3 % | −889 | +6.349 |
| D03 \* | Kernhaushalt GKV-Spitzenverband | 561 | −9,7 % | −54 | +16 |
| B07 \* | Sicherstellungsbereich der 17 KVen | 4.000 | +3,0 % | +120 | +640 |
| E01 \* | Market Access Deutschland | 2.750 | +8,0 % | +220 | +605 |
| H06 | Gesundheitsschutz, ÖGD | 39.000 | +7,0 % | +2.730 | +5.070 |
| F07 | Rettungsdienste | 70.000 | +19,0 % | +13.300 | +14.700 |
| A08 | Krankenhäuser, Pflegedienst | 408.599 | +4,3 % | +17.570 | +21.247 |
| B09 | Ambulante Pflege | 311.000 | +15,3 % | +47.583 | +59.090 |
| C02 | Stationäre Pflege | 580.000 | +14,7 % | +85.260 | +101.500 |
| | **Summe** | **2.155.154** | | **+123.684** | **+201.717** |

**Die Spreizung ist das Eigentliche.** Zehn Felder verlören Bedarf, sechs gewännen. Der Rückgang läge fast vollständig dort, wo **verarbeitet** wird — Apotheken, medizinisch-technischer Dienst, Funktionsdienst, Labore, Großhandel. Der Anstieg läge dort, wo **am Menschen** gearbeitet wird: Pflege stationär und ambulant, Rettungsdienst, Krankenhaus-Pflegedienst.

Das ist der politische Kern. Die beiden Bewegungen dämpfen sich in der Summe, aber sie betreffen verschiedene Menschen, verschiedene Qualifikationen und verschiedene Orte. Eine Apothekerin in Gelsenkirchen wird nicht zur Pflegefachkraft in Cottbus, weil eine Bundestabelle sich ausgleicht.

**Vier Zeilen tragen fast alles.** Stationäre Pflege, ambulante Pflege, Krankenhaus-Pflegedienst und Rettungsdienst stellen zusammen **1,37 Mio** der 2,16 Mio Vollkräfte und den gesamten Zuwachs. Die stationäre Pflege allein hat ihren Beitrag in der zweiten Erhebung um 15.660 Vollkräfte erhöht — mehr als die Summe aller Rückgänge der Tabelle. Die Tabelle ist damit im Wesentlichen eine Aussage über die **Pflege** — alle übrigen zwölf Felder zusammen bewegen weniger als ein Viertel davon.

## 3. Die Korrektur der Bezugsgrößen — und was sie über das Verfahren sagt

In der ersten Fassung dieser Tabelle standen 3.242.842 Vollkräfte, 73,6 % Deckung und ein KI-Beitrag von 258.000 Vollkräften. Das war **falsch**, und der Fehler stammt nicht aus dem Panel, sondern aus der Abbildung der Nacharbeit.

Sie hat sechs Feldern die **ganze Einrichtungsart** zugewiesen, obwohl die Rolle über einen engeren Ausschnitt rechnete — und in jedem dieser Fälle hatte die Rolle ihren eigenen Wert mit Fundstelle im Feld `bezugsgroesse_bestritten` genannt:

| Feld | zugewiesen | selbst belegt | Faktor |
|---|---:|---:|---:|
| D03 GKV-Spitzenverband | 190.000 (alle Sozialversicherungsverwaltung) | 561 | 339× |
| B07 Kassenärztliche Vereinigung | 470.000 (alle Arztpraxen) | 4.000 | 118× |
| E01 Market Access Pharma | 160.000 (pharmazeutische Industrie) | 2.750 | 58× |
| E02 Medizintechnik Bildgebung | 160.000 (Medizintechnik gesamt) | 28.000 | 5,7× |
| E07 Pharmagroßhandel | 123.000 (Großhandel gesamt) | 24.000 | 5,1× |
| E06 Labordiagnostik | 66.000 (alle Laboratorien) | 22.000 | 3,0× |

**Der auffälligste Fall war zugleich der größte Posten der alten Tabelle.** B07 ist die Kassenärztliche Vereinigung. Ihre Rechnung beschreibt den **Sicherstellungsapparat der KVen** — Akutleitstelle, Terminservicestelle, Bedarfsplanung, Nachbesetzungsverfahren —, nicht das Personal der Arztpraxen. Multipliziert mit 470.000 statt 4.000 ergab das +89.300 Vollkräfte in der Spalte »ohne KI«, also **27 % der damaligen Gesamtsumme**, aus einem Feld von rund viertausend Menschen.

**Drei Ursachen, alle im Verfahren, nicht im Panel:**

1. **Die Abbildung kannte die Gegenwerte nicht.** 95 von 100 Rollen hatten ihre Bezugsgröße bestritten und einen belegten Gegenwert genannt. Diese Angaben wurden der Abbildung nicht vorgelegt — obwohl `11-Konzept-v2.md` § 5, Runde 0a, ihre gesammelte Auswertung ausdrücklich vorsieht.
2. **Mandatsreichweite wurde mit Bezugsgruppe verwechselt.** Die Begründung der Abbildung für B07 lautete wörtlich, das Mandat reiche »über die gesamte vertragsärztliche Versorgung«. Das stimmt — und ist das falsche Kriterium. Wofür jemand zuständig ist, ist nicht, für wie viele Menschen er spricht.
3. **Die Prüfung der Abbildung prüfte die falsche Richtung.** Ihr Auftrag war, Überschreitungen der Einrichtungsart zu finden. B07 überschreitet nichts — es füllt die Einrichtungsart exakt aus. Der Fehler war eine Untererfüllung des *Feldes*, keine Übererfüllung des *Rahmens*, und danach war nicht gefragt.

**Die Folge für das Kriterium:** Die Bezugsgrößendeckung liegt korrigiert bei **48,9 %** statt 73,6 % und reißt die Schwelle von 70 % erneut. Die Reparatur hat die Deckung real von 42 % auf 48,9 % gehoben — deutlich weniger, als sie zu leisten schien.

**Ein zweiter Vorbehalt zu demselben Feld.** B07 ist zugleich eine der vier Karten, die als `interessengestützt` gekennzeichnet sind: Vier ihrer fünf Befunde stehen auf Veröffentlichungen der KBV oder einer KV, darunter deren eigene Stellungnahme zu einem Gesetzentwurf, der die Aufgaben der KVen erweitert. Die +19 % sind damit die Schätzung einer Organisation über ihren eigenen künftigen Umfang. Nach der Zuschnittkorrektur trägt diese Karte noch 0,4 % der Tabelle; vor ihr waren es 27 %. Beide Fehler hingen zusammen — eine interessengestützte Schätzung wurde durch einen Zuordnungsfehler auf das Hundertfache ihres Gewichts gehoben.

**Was das Verfahren richtig gemacht hat:** Jede der sechs Rollen hat ihren korrekten Wert genannt, mit Quelle, im dafür vorgesehenen Feld. Die Information war vorhanden und belegt. Sie wurde nicht ausgewertet. Das ist ein Verarbeitungsfehler, kein Erkenntnisfehler — und er wäre beim Schreiben dieses Teils nur deshalb aufgefallen, weil jemand nach der Herkunft einer einzelnen Zahl gefragt hat.

## 4. Der Arbeitszeiteffekt — und warum er nicht durchschlägt

| | |
|---|---|
| **P1** technisch ersetzbare Arbeitszeit | **41,3 %** ankerbereinigt, ±3 Punkte Methodenunsicherheit |
| **P2** davon bis 2031 wirksam | **40 %** |
| **P1 × P2** tatsächlich automatisierte Arbeitszeit | **15,8 %** (Q1 9,9 – Q3 22,5) |
| **D** Durchgriff auf den Personalbedarf | **0,53** |

Rund ein Sechstel der Arbeitszeit würde bis 2031 tatsächlich frei. Davon erreichte **gut die Hälfte** den Personalbedarf. Die andere Hälfte verschwindet in Vorhaltung, Schichtfloors und Mindestbesetzung: Ein 24/7-Dienstplan spart bei zehn Prozent weniger Schreibarbeit keine zehn Prozent Personal, weil Nacht, Wochenende und Bereitschaft nicht teilbar sind.

**Elf Rollen geben ein D über 1,0 an** — sie behaupten damit, dass mehr Personalbedarf verschwindet als Arbeitszeit frei wird. Das ist möglich, etwa über Standortschließung oder Konsolidierung, aber es verlangt nach § 3 des Konzepts eine Begründung. **Nur zwei der elf nennen einen Mechanismus.** Keine liegt außerhalb des erlaubten Bereichs von 1,5, und die Werte gehen nicht in die Zentraltabelle ein; für Runde 3 sind sie gezielt anzugreifen.

Die Spannweite von D reicht über den Faktor sieben — von 0,32 in der Pflege bis 0,79 in der Gesundheitsindustrie. Wo eine Kopfzahl gesetzlich oder organisatorisch gebunden ist, kommt die gesparte Stunde nicht an. Wo Arbeit in Stückzahlen anfällt, kommt sie an.

**P1 × P2 ist die Größe, die mit externen Automatisierungsstudien vergleichbar ist. D ist die Größe, die erklärt, warum aus ihr kein Stellenabbau folgt.** Beide gehören zusammen berichtet; einzeln ist jede von beiden irreführend.

## 5. Der Attributionsvorbehalt

Auf die Frage, woher die Veränderung des Personalbedarfs rührt, antwortet das Panel im Median:

| | KI und Automatisierung | Struktur- und Rechtsreform | Demografie |
|---|---|---|---|
| erste Erhebung | 40 % | 28,5 % | 20 % |
| **nach der Diskussion** | **35,5 %** | **31,5 %** | **22 %** |

**Die Diskussion hat die Zuschreibung von der Technik weg verschoben.** Das ist die stärkste Medianbewegung der zweiten Erhebung und stützt die Deutschland-These aus einer zweiten Richtung: Wer hundert Felder über ihre eigenen Zahlen streiten lässt, bekommt nicht mehr KI-Wirkung heraus, sondern weniger.

Das ist der wichtigste Vorbehalt dieses Teils und gehört neben jede Zahl, nicht in den Anhang: **Weniger als die Hälfte der Bewegung wäre der Technik zuzurechnen.** Wer 2031 einen veränderten Personalbedarf sieht und ihn der KI zuschreibt, schreibt ihr mindestens zur Hälfte etwas zu, das aus Krankenhausreform und Alterung ohnehin gekommen wäre.

Die Zuschreibung ist rechnerisch konsistent — aber das ist weniger wert, als es klingt: Der Rollenauftrag verlangt diese Gegenprobe ausdrücklich, mit Formel und Toleranz. Dass 100 von 100 Rollen sie einhalten, belegt Anweisungstreue, nicht Herleitung (`22-Teil-0-Gueltigkeit.md` § 5).

Und die Anteile sind auf fünf Punkte genau, nicht auf einen: 93 bis 97 % aller Werte in P4, P5 und A2 sind Vielfache von fünf. »40 %« ist als »gut ein Drittel bis knapp die Hälfte« zu lesen.

## 6. Wo die Ersparnis hängen bleibt

Auf die Frage, was 2031 im eigenen Feld knapper wäre, antworten hundert Rollen:

| Engpass | |
|---|---|
| **Entscheidung** | **62** |
| bedienendes Personal | 21 |
| Daten | 8 |
| Recht | 8 |
| **Technik** | **1** |

Eine einzige Rolle von hundert hält die Technik für den Engpass. Dasselbe Bild beim bindenden Hemmnis: Refinanzierung und Abrechnung 29, Investitionsfähigkeit 24, Recht und Zulassung 23, Datenverfügbarkeit 15, Haftung 7. **Vier von fünf Feldern nennen ein Geld- oder Rechtshemmnis, keines ein Könnenshemmnis.**

Das ist die Deutschland-These des Arbeitspapiers, und das Panel liefert sie als Liste: `20-Durchgriffskanaele.md` führt 59 feldübergreifend gedeckte Rechtsnormen. **Davon sind 43 unabhängig** — die übrigen 16 standen bereits in einem Faktenblatt und lagen den Rollen damit vor, darunter fünf der sechs meistgenannten.

**Die breitesten unabhängigen Kanäle sind Vergaberecht, nicht Gesundheitsrecht:**

| Norm | Rollen | Bänke |
|---|---|---|
| § 99 GWB — öffentlicher Auftraggeber | 31 | 10 |
| § 21 VgV — Verhandlungsverfahren | 19 | 9 |
| § 17 VgV — Verfahrensablauf | 11 | 7 |
| § 35 SGB I — Sozialgeheimnis | 10 | 7 |

Dass zehn von vierzehn Bänken unabhängig voneinander beim **Vergaberecht** landen, ist der dichteste eigenständige Befund des Laufs — und er passt zur Engpassantwort: 47 von 100 Feldern nennen das Vergaberecht als Beschaffungsweg. Nicht das Gesundheitsrecht entscheidet, ob eine Leistung eingekauft werden kann, sondern allgemeines Binnenmarktrecht.

**Vorgelegt, aber eigenständig durchdacht:** § 80 SGB X — die Auftragsverarbeitung von Sozialdaten — erscheint bei 93 von 100 Feldern. Die Norm stand in Faktenblatt R05 und steht zugleich wörtlich in der Antwortliste zur Marktgröße A1. Aber nur 15 Rollen haben sie dort angekreuzt; **90 leiten sie im Freitext her**. Sie ist damit kein unabhängiger Fund, aber auch kein bloßes Echo.

## 7. Wohin der Gewinn ginge, und woraus er bezahlt würde

**P5 — Verbleib des Effizienzgewinns** (Mediane):

| finanziert zusätzliche Leistung | **fließt ab ins Ausland** | bleibt beim Erbringer | senkt Preis oder Beitrag |
|---|---|---|---|
| 30 % | **30 %** | 27,5 % | 10 % |

Knapp ein Drittel des Gewinns verließe das Land als Lizenz-, Geräte- oder Cloudentgelt. Und **nur ein Zehntel** erreichte Beitragszahler oder Patienten. Wer KI im Gesundheitswesen als Beitragssatzargument führt, führt nach diesem Modell das schwächste der vier verfügbaren Argumente.

**A2 — aus welchem Topf bezahlt würde** (Mediane):

| Erbringerbudget | **gar kein Topf** | Fördermittel | Verwaltungskosten | Erlöstatbestand |
|---|---|---|---|---|
| 40 % | **30 %** | 13,5 % | 5 % | 5 % |

Für **drei Zehntel** der benötigten Leistung gäbe es 2031 keinen Rechnungsempfänger. Das ist die Marktantwort zur Engpassantwort: Der Bedarf ist da, die Entscheidung fehlt, und die Rechnung ginge an niemanden. Ein Erlöstatbestand — also der Weg, auf dem eine Leistung regulär vergütet wird — trüge 5 %.

## 8. Der Dissens

Die zehn Rollen mit dem höchsten Streitindex, also dem größten Abstand zum Panel über P1, P2, P3 und D zusammen:

| | Feld | P1 | P2 | P3 | P3₀ |
|---|---|---:|---:|---:|---:|
| 16,0 | N01 Verfasser des Arbeitspapiers | 79 | 92 | −29,0 | +10,0 |
| 13,1 | B09 ambulante Pflege | 14 | 35 | +15,2 | +19,0 |
| 12,9 | C06 Pflege und Langzeitversorgung | 18 | 25 | +26,0 | +31,0 |
| 12,6 | G05 Patienten und Zivilgesellschaft | 15 | 30 | +12,0 | +16,0 |
| 11,9 | A08 Pflegedienst der Krankenhäuser | 16 | 30 | +4,0 | +5,2 |
| 11,4 | E06 medizinische Laboratorien | 48 | 60 | −15,0 | +3,0 |

Zwei Pole. Am einen Ende die **körpernahe Pflege** mit sehr niedrigem P1 (14 bis 18 %) und trotzdem steigendem Bedarf — sie bestreitet nicht die Technik, sondern ihre Anwendbarkeit auf Arbeit am Bett. Am anderen Ende die **verarbeitenden Felder** mit hohem P1 und fallendem Bedarf.

Dazwischen steht, mit dem höchsten Streitindex des ganzen Panels, das Feld des **Verfassers selbst**: P1 79, P2 92, P3 −29. Die Rolle, die das Arbeitspapier schreibt, hält ihr eigenes Feld für das am stärksten exponierte der ganzen Bank. Das ist kein Kuriosum, sondern gehört in das Papier, weil es dessen eigene Voraussetzung betrifft.

**Kein Dissenspunkt ist bisher ausgetragen.** Die Gruppendiskussion der dreißig strittigsten Rollen ist Runde 2 und hat nicht stattgefunden. Bis dahin ist dieser Abschnitt eine Streitanzeige, kein Streitergebnis.

## 9. Was Runde 3 klären müsste

1. **Ob die Diskussion Erkenntnis erzeugt oder homogenisiert.** Der Divergenzerhalt — der Interquartilsabstand nach der Diskussion im Verhältnis zu dem davor — ist das entscheidende Maß. Fällt er unter die Hälfte, hat das Verfahren geglättet statt aufgeklärt.
2. **Ob D sich bewegt.** Die aussagekräftigste Einzelbewegung des Verfahrens, weil D genau die Größe ist, um die gestritten wird.
3. **Ob die Pflegefelder ihr niedriges P1 halten**, wenn ihnen die Rechnung der verarbeitenden Felder vorliegt.
4. **Ob die Felder ohne amtliche Bezugsgröße** mit dem korrigierten Auftrag (`11-Konzept-v2.md` § 5, Runde 0a) belastbare Werte liefern — davon hängt ab, ob die Zentraltabelle über 48,9 % hinauswächst. Vorrangig ist dabei die Lücke bei den Arztpraxen: 470.000 Vollkräfte ohne sprechendes Feld.

   **Ein bequemer Weg dorthin ist versperrt.** 32 der 84 nicht-primären Felder nennen selbst einen Zahlenwert; zusammen mit der primären Summe übersteigen sie den amtlichen Rahmen um rund 194.000 Vollkräfte. Die Werte überlappen einander und die Tabelle — jeder müsste einzeln disjunkt gemacht werden. Die Tabelle wächst nicht durch Hinzunehmen, sondern nur durch Zuschneiden.

5. **Ob die elf Rollen mit D über 1,0** ihren Mechanismus nachliefern oder ihren Wert senken.
