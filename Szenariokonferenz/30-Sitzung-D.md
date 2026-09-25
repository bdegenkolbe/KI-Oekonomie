# Sitzung D — die Übertragungskette

*Bericht über den Lauf vom 25. September 2026. Was gelaufen ist, was gescheitert ist, was die
Gegenprüfung gefunden hat und warum das Papier keine Freigabe bekommen hat.*

---

## 1. Was gelaufen ist

130 Agentenaufrufe in zehn Phasen, 100 Rollen auf fünf Stationen und drei Querbänken. Grundlage ist
Korinek, Jones, Sacher, Cotter & McCrory, *Economic Scenarios for Transformative AI*, The Anthropic
Institute WP 2026-02. Laufzeit 06:01 bis 17:42 UTC, davon 82 Minuten auf die Wiederaufnahme nach dem
Abbruch (Abschnitt 3). Verbrauch der Unteragenten: 3.222.661 Token.

| Phase | Aufrufe | Ergebnis |
|---|---:|---|
| Recherche | 6 | 212 Befunde, 75 benannte Lücken |
| Querschnitt | 14 | Europa 8, KI-Technik 6 |
| Stationen 0 bis 4 | 88 | 83 Karten, 5 Übergaben |
| Kettenprüfung | 6 | 12 Bruchstellen, davon 5 ohne genannten Mechanismus |
| Angriff | 8 | 3 Gegenposition, 5 Red Team |
| Papier | 8 | 5 Kapitel, Zusammenzug, Verifikation, Schlussfassung |

Die Recherche hat sich an die Sperre gehalten: Keines der sechs Faktenblätter hat in den zehn Domänen
R01 bis R10 der Sitzung A erneut recherchiert. Der gesamte Bestand — Faktenkern, Gültigkeitsbereich,
Teil 1 Deutschland, Teil 2 Europa, Durchgriffskanäle — ging als Eingabe in jeden Prompt ein und wurde
nicht neu erarbeitet.

## 2. Die Kette

| | Übergabe | Wert 2031 | 80 % |
|---|---|---|---|
| Ü0 | beitragspflichtige Arbeitsentgelte (ohne Renten) | 1.790 Mrd. € | 1.680–1.930 |
| Ü1 | GKV-Leistungsausgaben | 420 Mrd. € | — |
| Ü2 | Nachfrage Arznei- und Medizinprodukte | 140 Mrd. € | — |
| Ü3 | Markt für extern beauftragte Evidenz und Analytik | 800 Mio. € | — |
| Ü4 | HIGL-Verbund: Umsatz / Deckungsbeitrag | +5 % / −15 % | −35…+40 / −55…+20 |

Ü4 bezieht sich auf den Netto-**Außen**umsatz von rund 14,5 Mio. € (2025), nicht auf die 17,57 Mio. €
Netto-Erlöse. Beide Größen sind ausdrücklich nur zusammen und nur mit dem Szenarioschalter
weiterzugeben.

### Kennzahlen je Station

| Station | Karten | E1 Lohnquote (Median, Pp) | D2 Preisdurchgriff (Median, %) | D4 Verzögerung (Median, Jahre) |
|---|---:|---:|---:|---:|
| 0 Makro | 20 | -3.0 | 52 | 3.0 |
| 1 GKV/PKV | 17 | -5.0 | 20 | 3.0 |
| 2 Leistungserbringer | 16 | -3.0 | 12 | 3.0 |
| 3 Pharma/US | 18 | -5.0 | 28 | 3.0 |
| 4 HIGL | 12 | -7.5 | 58 | 3.0 |

Der Preisdurchgriff fällt dort am tiefsten, wo der Preis administriert ist — 12 % bei den
Leistungserbringern gegen 52 % in der Gesamtwirtschaft. Das ist der Übertragungsbruch, den das
US-Modell nicht kennt, und er ist quer durch die Kette messbar.

Die Verteilung der Effizienzgewinne (E3) summiert sich bei **allen 83 Karten** exakt auf 100.
Szenarienwahl über die Kette: 73 *substantial*, 8 *modest*, 2 *extreme*.

## 3. Der Abbruch nach 119 Aufrufen

**Alle fünf Red-Team-Aufrufe scheiterten mit `Prompt is too long` (invalid_request).** Die fünf
Kapitel wurden daraufhin ohne jede Gegenprüfung geschrieben, weil der Befundblock leer blieb.

Ursache war eine Fehleinschätzung beim Aufsetzen: Der Angriffsprompt legt alle 83 Kettenkarten in
einen Aufruf, und die Karten sind **im Median 31.851 Zeichen lang, in der Spitze 50.458**. Zusammen
mit dem Bestand ergab das 4.569.188 Zeichen, gut 1,1 Millionen Token.

| Aufruf | vorher | nachher |
|---|---:|---:|
| Red Team | 4.569.188 Zeichen | 413.785 |
| Kapitel, größte Station | — | 365.881 |
| Verifikation | (wäre ebenso gescheitert) | rund 300.000 |

Behoben durch `minikarte()`: Die Zahlen bleiben vollständig, die Fließtexte werden auf ein Budget
gekappt, und `kappen()` schreibt die ursprüngliche Länge dazu, damit die Kürzung sichtbar bleibt. Dazu
ein Rahmen ohne den 60.000 Zeichen langen Bestand für die Aufrufe, die ohnehin die ganze Kette tragen.
Angriffe und Verifikation bekommen ausdrücklich gesagt: eine fehlende **Zahl** ist ein harter Befund,
eine fehlende **Formulierung** nicht.

`kurzkarte()` blieb unverändert, weil sie in den abgeschlossenen Verdichtungs- und Rollenprompts
steckt. Deshalb konnte der Lauf aus dem Cache wieder aufsetzen: 119 Aufrufe kamen sofort zurück, 13
liefen neu. Hätte ich die Funktion angefasst, wären alle 83 Stationskarten neu gelaufen.

**Die Lehre ist nicht neu, sondern dieselbe wie in Sitzung C:** Ein Verfahren, das seine eigenen
Zwischenergebnisse weiterreicht, muss deren Größe kennen, bevor es sie weiterreicht. In Sitzung C war
es die Bewegung der Karten, hier ihre Länge.

## 4. Was die Kettenprüfung gefunden hat

**Die Kette trägt nicht.** 12 Bruchstellen, davon 5 ohne genannten Mechanismus.

Schwächstes Glied laut Prüfung: die Übergabe Station 3 nach Station 4 und darin der Mengenfaktor 1,55.
Er folgt aus 800 Mio. € geteilt durch einen Vergleichswert 2025 von rund 690 Mio. €, der auf acht
Kartenschätzungen und auf keiner Quelle steht.

Bemerkenswert ist, wie Station 4 darauf reagiert hat: Sie hat den Punktwert **nicht** geändert,
sondern das Intervall verbreitert — von −25…+30 auf −35…+40 beim Umsatz — und dabei getrennt, was ihre
eigene Schuld war und was die der Vorstation. Ihre Formulierung: sie habe den Faktor in vier
unabhängigen Kartenrechnungen als harten Multiplikator übernommen und die Unbelegtheit in keinem
Vorbehalt und in keinem Intervall geführt; das sei genau der Fehlertyp, den diese Kette sichtbar
machen solle.

## 5. Das Red Team

Vier der fünf Angriffe kommen zu dem Schluss, dass die angegriffene Position **nicht** standhält.

| Angriff | hält stand | hart | mittel | weich |
|---|---|---:|---:|---:|
| Fuenf Gelenke, keine durchlaufende Zweitgroesse: die Kette transportiert Begle | **nein** | 5 | 8 | 1 |
| Angriff 2: Die Lohnquote ist nicht der Kanal — sie ist in der Herleitung gar n | **nein** | 3 | 5 | 1 |
| Angriff 3 — Der US-Schock wirkt umgekehrt: Referenzschutz, Ruecknahme, Verzoeg | **nein** | 2 | 7 | 2 |
| ANGRIFF 4 — Der Preis steigt, aber die Eintrittsschwelle steigt schneller: Geg | ja | 2 | 4 | 1 |
| ANGRIFF 5: Das Anthropic-Papier traegt die Uebertragung nicht | **nein** | 3 | 8 | 2 |

Die zwei Befunde, die an die Substanz gehen:

**Der Hauptwert enthält kein Modellsignal.** Die 1.790 Mrd. € sind eine Fortschreibung der gemessenen
KV45-Grundlohnsumme mit 2,4 % im Jahr aus drei Faktoren — nominales Entgelt je beitragspflichtig
Beschäftigtem, Beschäftigungsentwicklung, Rechtsmechanik der Beitragsbemessungsgrenze. Keine Größe des
Anthropic-Modells kommt in einem der drei vor. Das Papier zieht daraus im Text die Folgerung: Der
tragfähige Satz laute nicht, das Anthropic-Modell ergebe für Deutschland 420 Mrd. €, sondern die
deutsche Rechts- und Fortschreibungsmechanik ergebe 420 Mrd. €.

**Die Szenariowahl ist selbst ein importierter US-Wert.** 73 der 83 Kettenkarten tragen das Etikett
*substantial* — 88,0 %, nachgerechnet und bestätigt. Die einzige empirische Verankerung dieses
Etiketts ist die Medianantwort einer Befragung von 10.980 US-Erwachsenen. Damit verletzt die
Szenariowahl die Regel der Konferenz, keine US-Werte ohne ausgewiesene Begründung zu übertragen — und
mit ihr hängen sämtliche 80-Prozent-Intervalle der Karten.

Dazu: **Die Lohnquote ist nicht der Kanal.** Sie kommt in der Herleitung des Hauptwerts nicht vor.
Beleg aus den Karten selbst: S0-05 nennt −3,5 Punkte Lohnquote bei 1.825 Mrd. €, S0-16 nennt −1,0
Punkte bei 1.830 Mrd. €. Und beim US-Schock: Für patentgeschützte Arzneimittel nach § 130b SGB V führt
**keine** Station eine eigene Trägerzahl — die Richtung des Effekts ist in der Kette weder bestätigt
noch widerlegt, sondern nicht abgebildet.

## 6. Die verweigerte Freigabe

Die Verifikation hat **keine Freigabe** erteilt: 7 harte, 11 mittlere, 6 weiche Befunde.

Alle sieben harten Befunde sind Rechen- oder Zählfehler im Entwurf, jeder mit dem korrekten Wert
benannt: 3 bis 30 statt 3 bis 12; Faktor 1,47 statt 2,5; rund ein Sechstel statt ein Viertel; fünf
Abweichler statt vier; WIG2 rund +1,3 Mio. € und 4K rund −0,6 Mio. € statt beide um 1,3 Mio. €
gegenläufig.

Ihr eigenes Urteil über das Geprüfte lautet, der Entwurf sei in seinen nachrechenbaren Kernstücken
ungewöhnlich sauber. Exakt bestätigt wurden unter anderem die Szenarienzählung zeichengenau, alle vier
E3-Mediane der Station 1, die Hemmnistabellen aller vier Stationen sowie die K1- und K2-Mediane. Die
Freigabe blieb trotzdem aus, weil sieben harte Befunde offen waren.

Die Schlussfassung hat **alle 24 Befunde eingearbeitet**, dokumentiert in 25 Anmerkungen. Zwei
Beispiele für die Art der Korrektur:

- Befund 13: Die Zahl rund 20 bis 25 Mrd. € und die daran hängende Schlussfolgerung, das sei mehr als
  der gesamte bezifferte KI-Effekt, wurden **ersatzlos gestrichen** — nicht abgeschwächt — weil keine
  Karte einen Mechanismus dafür nannte.
- Befund 11: Die Allaussage, nach übereinstimmender Aussage aller zwölf Karten existiere die Deckung
  nicht, wurde auf die belegte Fassung zurückgeführt: keine der zwölf Karten bezeichne die Frage als
  gelöst.

## 7. Was offen bleibt

1. **Die Freigabe ist nicht nachgeholt.** Das Papier ist die überarbeitete Fassung; eine zweite
   Verifikation, die bestätigt, dass die Einarbeitung trägt, hat nicht stattgefunden. Das Verfahren
   sieht sie nicht vor — in Sitzung C war das derselbe offene Punkt.
2. **Die Angriffe haben sich selbst durchnummeriert** (n = 2, 5, 7, 11, 14 statt 1 bis 5). Das Feld
   war im Schema frei und ist nicht gegen die vorgegebene Nummer geprüft worden. Die Titel
   identifizieren die Angriffe eindeutig, die Zählung ist unbrauchbar.
3. **Die zwei tiefsten Befunde sind eingearbeitet, aber nicht behoben.** Dass der Hauptwert kein
   Modellsignal enthält und die Szenariowahl ein importierter US-Wert ist, steht jetzt im Papier.
   Beheben ließe es sich nur durch eine eigene deutsche Kalibrierung des Modells — das ist eine andere
   Arbeit als diese Konferenz.

---

*Rohdaten: `rohdaten/sitzung-d.json` (5,9 MB). Roster: `28-Roster-v2.md`. Papier:
`29-Strategiepapier-2031.md`. Lauf: `workflow-sitzung-d.js`, erzeugt aus `baue-sitzung-d.py` und
`roster_d.py`.*
