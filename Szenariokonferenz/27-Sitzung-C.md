# Sitzung C — Auswertung

*Runde 4 bis 6 der Szenariokonferenz 2031: acht Hebel, sieben Leistungsprofile, hundert Bewertungen, sechs Angriffe, drei Verifikationen und das Papier. 120 Aufrufe, 0 Ausfälle, 5 h 50 min, 13,7 Mio Token. Gelaufen am 20.09.2026.*

---

## 1. Was gelaufen ist

| Runde | Aufrufe | Ergebnis |
|---|---:|---|
| 4a Ableitung | 2 | 8 Hebel, 8 Leistungsprofile aus Dissens-, Positions- und Engpasskarten |
| 4a Prüfung | 1 | 17 Beanstandungen, davon 4 hart |
| 4a Nachbesserung | 1 | 8 Hebel, 7 Profile — eines gestrichen |
| 4a zweite Prüfung | 1 | 16 Beanstandungen, davon 6 hart |
| 4b Bewertung | 100 | 800 Hebelurteile, 259 Profilurteile |
| 5a Red Team | 6 | **6 von 6 haben einen Bruch gefunden** |
| 5b Verifikation | 3 | 53 Befunde gegen Teil 0, 1 und 2, davon **36 hart** |
| 6 Papier | 6 | drei Kapitel, Zusammenzug, Verifikation, Schlussfassung |

Der Lauf ist zweimal angehalten und einmal aus dem Zwischenspeicher fortgesetzt worden. Beide Abbrüche gingen auf Mängel des Auftrags zurück, nicht auf Ausfälle.

## 2. Der Abbruch nach fünf Aufrufen — Ableitungsaktualität

Die Prüfinstanz hat **sieben der acht** zuerst abgeleiteten Hebel mit einem harten Befund zurückgewiesen. Alle vom selben Typ: Die Ableitung stützte sich auf Karten, deren Aussage die Rolle in Runde 3 verändert oder **ausdrücklich zurückgenommen** hatte.

| Karte | Runde 1 | Runde 3 | Was die Rolle selbst schreibt |
|---|---|---|---|
| D06 | D 0,94 | **0,60** | »kein Sachbefund, sondern eine Buchungskonvention … Zähler und Nenner standen auf verschiedenen Mengen« |
| C06 | D 1,11 | **1,000** | »Das gehört korrigiert, und zwar von mir, nicht von der Auswertung« |
| C08 | P3 +50 | **+12,9** | »Zwischen Zähler und Nenner des Durchgriffs lag ein Populationswechsel« |
| L07 | P3 +26 | **+9,5** | die Begründung widerlegt die Schlussfigur, die der Hebel aus ihr zog |

**Die Ursache lag im Zuschnitt des Auftrags.** Er reichte die Runde-3-Werte nur als Kopfzeile weiter, die Prosa dagegen als Runde-1-Position — und die Dissensprotokolle aus Sitzung B zitieren durchgängig Runde-1-Zahlen, weil es zum Zeitpunkt ihrer Entstehung keine anderen gab. Das Feld, in dem die Rücknahmen stehen, kam im Auftrag nicht vor. **92 von 100 Rollen** hatten in Runde 3 mindestens eine Kernzahl bewegt.

Derselbe Fehlertyp wie der Zuschnittfehler aus `18-Strategiepapier-2031.md` § 5c: ein Verarbeitungsschritt, dem das Material vorenthalten wurde, das ihn korrigiert hätte. Als **24. Abbruchkriterium** nachgetragen.

**Die zweite Prüfung fand die vier harten Befunde behoben und sechs neue, anderer Art.** Die Substanz der Hebel stand; beanstandet waren die Superlative der Begründungen: »die einzige Karte«, »alle acht Erstnennungen«, »sechs korrigieren aus demselben Grund« — jedes Mal mit Gegenbeispiel. Das Modell quantifiziert universell über Mengen, die es nicht ausgezählt hat. Zweimal in derselben Form gemessen; behoben nicht durch eine dritte Schleife, sondern durch ein Verbot ungeprüfter Allaussagen im Schreibauftrag.

## 3. Das Urteilsmuster — gezählt wird, wo es schadet

Hundert Rollen, je acht Hebelurteile.

| | Hebel | wirkt | wirkt nicht | schadet |
|---|---|---:|---:|---:|
| H6 | Format, Struktur und Semantik in die Dokumentationspflicht (§ 630f BGB) | **78** | 6 | 16 |
| H7 | Erfüllungsaufwand je Folgepflicht offenlegen | **66** | 3 | 31 |
| H4 | Betreiber- und Aufsichtspflichten bündeln (§ 2 KI-MIG) | 38 | 20 | 42 |
| H8 | Ein Adressat für den Alarm (§ 45a/b SGB XI) | 36 | 33 | 31 |
| H5 | § 31a SGB X für gebundene Teilentscheidungen | 35 | 39 | 26 |
| H3 | Transformationsfonds ohne Kofinanzierungsschwelle | 31 | 24 | **45** |
| H2 | Katalogposition mit Beschlussdatum vor 2029 | 30 | 28 | 42 |
| H1 | Anrechnungsverbot: der Digitalgewinn bleibt im Feld | **8** | 38 | **54** |

**Zwei Hebel tragen breit, und beide bewegen kein Geld.** H6 und H7 sind reine Transparenz- und Formatpflichten. Von den vier Hebeln, die Geld bewegen, haben drei mehr Schadens- als Wirkungsurteile.

**H1 ist der schlechteste des Satzes** — 8 zu 54, Schaden in allen vierzehn Bänken. Die durchgehende Begründung: Die drei Vergütungsnormen erfassen das eigene Feld nicht, und ein Zuschlag für die Pflege ist für das Krankenhaus keine Entlastung, sondern eine Asymmetrie. Seine eigene Kippbedingung hebt sich auf: Wären alle Vergütungskanäle erstreckt, gäbe es keine Anrechnung mehr — also genau das, was die Zahlerseite bestreitet.

Bei den Leistungsprofilen ist das Bild schärfer:

| | Profil | wirkt | schadet |
|---|---|---:|---:|
| L5 | Nachweisführung der Zulässigkeitskette | 27 | 7 |
| L7 | Veröffentlichte Zuteilungsregel | 23 | 5 |
| L3 | Betriebsträgerschaft als bezogene Leistung | 22 | 13 |
| L4 | Auswertbarer, rechtlich gedeckter Datensatz | 17 | 13 |
| L1 | Herstellung der Zeichnungsreife | 15 | 10 |
| L8 | Umstellungsfähigkeit gegenüber Festlegungen | 9 | 10 |
| **L6** | **Belastbare Messung des Effizienzgewinns** | **1** | **43** |

L6 ist das schärfste Einzelergebnis des ganzen Verfahrens: *»Der Nachweis zahlt gegen den, der ihn bestellt — im Pflegebudget ist die Erstattung ist-kostenbasiert.«* Wer belegt, dass er schneller arbeitet, liefert das Kürzungsargument. Das eine Wirkungsurteil trägt keine Kartennummer und ist deshalb gestrichen.

## 4. Was das Red Team gefunden hat

Sechs Instanzen, sechs Brüche, alle mit der Konsequenz **einschränken** — keiner mit »streichen«, keiner mit »hält«.

**1. Der meistzitierte Befund ist zur Hälfte ein Artefakt.** Der Satz »vier von fünf Feldern nennen ein Geld- oder Rechtshemmnis, **keines ein Könnenshemmnis**« stand auf einer **abschließenden** Antwortliste, die ein Könnenshemmnis gar nicht enthielt. Der mögliche Wertebereich betrug 0 bis 0 von 100. Der Satz ist gestrichen (`23-Teil-1-Deutschland.md` § 6). Der A3-Teil — eine von hundert wählt »Technik« — steht, weil die Option dort existierte, bleibt aber eine geschlossene Liste von fünf Vorgaben.

**2. Der bestbewertete Hebel ist der einzige mit zivilrechtlicher Grundlage.** § 630f BGB adressiert »jeden Behandelnden« und überschreitet damit den Roster. Mindestens vier der neun benannten Besetzungslücken sind Volladressaten — Zahnmedizin, Heilmittelerbringer, Reha, Kur und Vorsorge. Bei ihrer Besetzung fiele H6s Verhältnis von 4,9 auf 2,6 bis 3,0.

**3. Die Zuschnittkorrektur ist nicht zu Ende geführt.** A06 trägt mit 166.256 Vollkräften den gesamten medizinisch-technischen Dienst statt des Laborausschnitts — derselbe Fehlertyp wie D03 (Faktor 339) und B07 (118), nur eine Ebene tiefer: Dienstart statt Ausschnitt, nicht Einrichtungsart statt Ausschnitt. Dasselbe gilt für A09 und H06. Die Deckung läge damit zwischen **48,9 % und 44,3 %**, die Zuschnittstreue zwischen 10 und 7 von 16.

**4. Der Gegenpfad wurde nie angegriffen.** Die Spalte »ohne KI« erzeugt die Kernzahl — der KI-Beitrag **ist** die Differenz —, und in den vier tragenden Zeilen hat sie niemand bestritten. Bei ±2 Prozentpunkten Gegenpfad auf 1,37 Mio Vollkräften liegt der KI-Beitrag zwischen **50.641 und 105.425 Vollkräften**. Die berichteten 78.000 sind ein Punkt in einer Spanne von ±35 %.

**5. Eine Kernzahl trägt ein Maß, das sie verwirft.** P1 × P2 = 16,4 % ist ein ungewichteter Median über hundert Felder, von denen 82 keine Bezugsgröße haben — für genau diese stellt Teil 0 selbst die Regel auf, ihre Werte seien nicht gewichtbar. Bezugsgrößengewichtet ergäben sich **8,4 %**, Faktor 1,87.

**6. Die Spreizungsdeutung ist eine Aussage über den Roster.** »Rückgang, wo verarbeitet wird — Anstieg, wo am Menschen gearbeitet wird« steht auf einer Tabelle mit genau **einer** körpernahen Einrichtungsart außerhalb der Pflege. Die größte unbesetzte ist »Praxen sonstiger medizinischer Berufe« mit 352.000 Vollkräften; der Kipppunkt liegt bei 40.029 Vollkräften, und die einzige Karte in diesem Feld liegt darüber.

## 5. Was die Verifikation an den geschriebenen Teilen gefunden hat

Drei Instanzen, je ein fremder Teil, 53 Befunde, **36 hart**. Alle prüfbaren sind gegen die Rohdaten nachgerechnet und bestätigt worden. Der Befund ist einheitlich und unangenehm:

**Teil 1 führte über weite Strecken die Werte der ersten Erhebung, obwohl er die Fassung nach der zweiten auswies.** Dieselbe Fehlerklasse, die den Lauf nach fünf Aufrufen angehalten hatte — diesmal in von Hand geschriebenem Text.

| Stand vorher | maßgeblich | Art |
|---|---|---|
| »Elf Rollen geben ein D über 1,0 an« | **drei** (M03 1,42, E05 1,41, E07 1,04), alle mit Mechanismus | Runde-1-Wert |
| »Spannweite über den Faktor sieben, 0,32 bis 0,79« | Faktor **33** (0,04 bis 1,42); über Bankmediane **2,1** | Rechenfehler und Runde-1-Werte |
| »Zehn Felder verlören Bedarf, sechs gewännen« | **neun und sieben** | Auszählfehler gegen die eigene Tabelle |
| »+19 %« für die KV-Karte | **+16 %** in der Spalte »ohne KI« | Runde-1-Wert |
| P1 41,3 / P1 × P2 15,8 / D 0,53 | **41,8 / 16,4 / 0,51** | Runde-1-Werte |
| »mehr als die Summe aller Rückgänge« | gut **ein Drittel** davon (15.660 von 43.099) | Vergleichsfehler |
| Median »+3 %« | **+4,2 %** | Runde-1-Wert |

**Der schwerste Einzelbefund steht in Teil 2 und ist eine Erfindung.** Dort stand, vier Rollen seien vom vorgegebenen Vergleichsrahmen abgewichen und hätten die Vereinigten Staaten, Japan oder Österreich genannt. Gegen die Rohdaten: **Alle achtzehn zuständigen Rollen nannten einen der fünf vorgegebenen Staaten** — Dänemark 9, Frankreich 4, Niederlande 2, Vereinigtes Königreich 2, Estland 1. Der Satz hatte keine Grundlage. Er ist gestrichen und durch die tatsächliche Einschränkung ersetzt.

Ebenfalls hart und behoben: Teil 2 führte **keine einzige Kartennummer**, obwohl die erste Regel des Papiers lautet, dass ohne Kartennummer nichts im Papier steht.

Alle genannten Stellen sind korrigiert. Die Korrekturen sind im Text als solche ausgewiesen und nicht stillschweigend eingearbeitet.

## 6. Die Freigabe wurde verweigert

Die Verifikation des Zusammenzugs hat **»nicht frei«** gemeldet, mit dreizehn Befunden, davon zehn hart — darunter vier geglättete Widersprüche und ein Rechenfehler: »in der Bundessumme glichen sich die beiden Bewegungen zu gut zwei Dritteln aus«, tatsächlich zu **25,8 %** (Rückgänge 43.099 gegen Zuwächse 166.783). Die Schlussfassung hat zwanzig Befunde eingearbeitet, die Zahl berichtigt und **vierzehn Punkte ausdrücklich offen gelassen**; sechs Widersprüche stehen mit beiden Seiten und ohne Entscheidung im Papier.

Das ist die vorgesehene Wirkung der Trennung von Schreiben und Prüfen. Wer schreibt, prüft nicht — und wer prüft, darf die Freigabe verweigern.

## 7. Was Sitzung C über das Verfahren sagt

**Die Prüfstufen haben zum ersten Mal vor dem Geld gegriffen.** Vier frühere Fehlerklassen wurden nach vollständigen Läufen gefunden, drei davon erst auf eine Rückfrage. Diese wurde nach fünf von 120 Aufrufen gefunden, von einer eingebauten Stufe, für rund fünf Dollar.

**Die charakteristische Schwäche ist benennbar geworden.** Sie ist nicht Halluzination im landläufigen Sinn, sondern **Aktualitätsverlust und Übergeneralisierung**: Das Modell greift auf den ausführlicheren älteren Stand zurück, wenn beide vorliegen, und quantifiziert universell über Mengen, die es nicht ausgezählt hat. Beides ist durch den Zuschnitt des Auftrags steuerbar und nicht durch mehr Aufrufe.

**Der Befund gegen die eigenen Texte wiegt schwerer als der gegen das Panel.** 36 harte Befunde stehen gegen von Hand geschriebene Teile, darunter eine Erfindung und mehrere Rechenfehler. Das Panel hat sich in Runde 3 selbst korrigiert; der geschriebene Text hat das nicht getan, bis eine fremde Instanz ihn dazu zwang.

## 8. Stand der Abbruchkriterien

Von 24 vorab festgelegten Kriterien sind **drei gerissen** (Bezugsgrößendeckung 48,9 % bis 44,3 %, Modellabhängigkeit 3 von 6, Zuschnittstreue 10 bis 7 von 16), **eines neu gerissen** (Ableitungsaktualität) und **zwei zurückgezogen** (Attributionskonsistenz, Modellabhängigkeit in Runde 3).

Damit ist die Abschlussregel aus `18-Strategiepapier-2031.md` § 7a erfüllbar: Sie verlangt nicht, dass kein Kriterium reißt, sondern dass jedes gerissene mit Wert, Ursache und Konsequenz vor der ersten inhaltlichen Aussage steht.

**Nicht erfüllt und offen:** Die Zuschnittprüfung für A06, A09 und H06 steht aus. Bis dahin ist 48,9 % eine Obergrenze.
