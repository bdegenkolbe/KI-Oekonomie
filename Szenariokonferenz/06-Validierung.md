# Validierungsschritt

Zwischen Stimmabgabe und Delphi-Revision tritt eine eigene Runde: Jeder Stimmzettel wird von einer unabhängigen Instanz geprüft, bevor er in die Verteilung eingeht.

## 1. Warum

Im ersten Lauf hat sich gezeigt, dass Agenten die Quellenpflicht formal erfüllen, aber inhaltlich ins Leere laufen: Zwölf von 27 recherchierten überhaupt, und fast alle recherchierten dasselbe — Industriestrompreis und Rechenzentrumsleistung, weil das die einzigen im Stimmzettel vorkommenden *gegenwärtigen* Größen waren. Eine Rechtsbank, die Strompreise nachschlägt, produziert keine überprüfbare Fachaussage, sondern eine schlecht belegte Makroschätzung.

Der Fachteil (§ 03-Stimmzettel.md, Teil 3) erzwingt jetzt Aussagen über das eigene Feld. Damit wird Prüfung überhaupt erst möglich und zugleich nötig: Eine Aussage wie „Beschaffungszyklen im Krankenhaus dauern vier Jahre" ist falsifizierbar — anders als eine Schätzung des BIP 2030.

## 2. Was geprüft wird

Die Validierungsinstanz erhält den vollständigen Stimmzettel einer Rolle und prüft vier Dinge:

**(a) Existenz der Quellen.** Jede in F6 und in `sources` angegebene Quelle wird aufgerufen. Ergebnis je Quelle: *auffindbar* / *nicht auffindbar* / *existiert, aber anderer Inhalt*.

**(b) Deckung der Aussage.** Sagt die Quelle, was der Agent ihr entnimmt? Ergebnis: *stützt die Aussage* / *stützt teilweise* / *stützt nicht* / *widerspricht*.

**(c) Mandatstreue.** Liegt die Recherche im Fachgebiet der Rolle? Eine Pflegedirektion, die Strompreise recherchiert, verfehlt das Mandat — unabhängig davon, ob die Zahl stimmt.

**(d) Fachliche Plausibilität des Fachteils.** Sind die in F1 bis F5 genannten Tätigkeiten, Hemmnisse und Frühindikatoren in diesem Feld real und korrekt benannt? Geprüft wird auf erkennbare Fachfehler, nicht auf Zustimmung zur Einschätzung. Eine ungewöhnliche, aber fachlich mögliche Position besteht die Prüfung.

## 3. Ergebnis je Stimmzettel

| Status | Bedeutung | Folge für die Auswertung |
|---|---|---|
| **gültig** | Quellen auffindbar und deckend, Mandat gewahrt, keine Fachfehler | geht regulär in die Verteilung ein |
| **mit Vorbehalt** | eine Quelle nicht auffindbar oder Mandat teilweise verfehlt, Fachteil aber tragfähig | geht ein, wird im Bericht gesondert ausgewiesen |
| **zurückzuweisen** | erfundene Quelle, Quelle widerspricht der Aussage, oder klarer Fachfehler im Fachteil | Werte gehen **nicht** in die Hauptverteilung ein |

Zurückgewiesene Stimmzettel werden gezählt und im Bericht benannt — sie werden nicht stillschweigend ersetzt. Die Auswertung weist **zwei Verteilungen** aus: alle Stimmen und nur die validierten. Weichen beide erheblich voneinander ab, ist das selbst ein Befund über die Qualität der Panelarbeit.

## 4. Was die Validierung ausdrücklich nicht darf

- Sie korrigiert keine Schätzungen. Eine Zahl, die der Prüferin unplausibel erscheint, aber sauber hergeleitet und gekennzeichnet ist, bleibt stehen.
- Sie bewertet keine Positionen. Eine Minderheitsmeinung ist kein Prüfungsmangel — Rollentreue ist gefordert (§ 01-Briefing.md E.7).
- Sie schreibt den Stimmzettel nicht um. Sie urteilt, sie ersetzt nicht.

## 5. Einordnung in den Ablauf

| Runde | Inhalt | Modell |
|---|---|---|
| 1 | Unabhängige Stimmabgabe mit Fachteil | leistungsfähiges Modell (Rollentreue, Divergenz) |
| **1b** | **Validierung je Stimmzettel** | **kleineres Modell — Prüfen ist Abgleich, nicht Urteilsbildung** |
| 2 | Delphi-Revision auf Basis der validierten Verteilung | leistungsfähiges Modell |
| 3 | Red Team gegen das führende Szenario | leistungsfähiges Modell |
| 4 | Synthese und getrennte Faktenverifikation | leistungsfähiges Modell |

Die Validierung in 1b prüft die **Stimmzettel**; die Verifikation in Runde 4 prüft den **Faktenkern** und den Bericht. Beide bleiben getrennt: Wer die Stimmen prüft, prüft nicht die Grundlage, auf der sie abgegeben wurden.

## 6. Grenze des Verfahrens

Die Validierungsinstanz ist selbst ein Sprachmodell. Sie kann eine erfundene Quelle als nicht auffindbar erkennen und eine falsche Zuschreibung bemerken; sie kann nicht garantieren, dass eine auffindbare Quelle richtig gelesen wurde. Die Prüfung senkt die Fehlerquote, sie beseitigt sie nicht. Der Bericht führt aus, wie viele Stimmzettel geprüft, beanstandet und zurückgewiesen wurden — damit die Leserin die Reichweite der Prüfung selbst einschätzen kann.
