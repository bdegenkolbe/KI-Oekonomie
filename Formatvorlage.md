# Formatvorlage.md — Gestaltungsrichtlinie für PDF- und Word-Export

**Gilt für:** Alle PDF- und Word-Exporte des Hauptdokuments `Arbeitspapier_KI_Robotik_Besteuerung.md` (Projekt „Besteuerung von KI und Robotik", HIGL – Health Innovators Group Leipzig).

---

## 1. Seitenaufbau

| Eigenschaft | Wert |
|---|---|
| Format | A4 (210 × 297 mm) |
| Seitenränder | oben 2,5 cm, unten 2,5 cm, links 2 cm, rechts 2 cm |
| Inhaltsbreite | Seitenbreite abzüglich Ränder |
| Ausrichtung | Hochformat |

---

## 2. Schriften

| Element | Schrift | Größe | Gewicht | Farbe |
|---|---|---|---|---|
| Dokumenttitel (H1, „Arbeitspapier") | Arial / Helvetica | 22 pt | Bold | #1B3A5C |
| Haupttitel-Zeile („Die Besteuerung von KI und Robotik …") | Arial / Helvetica | 16 pt | Bold | #1B3A5C |
| Untertitel („Ökonomische, rechtliche und sozialpolitische Perspektiven") | Arial / Helvetica | 11 pt | Regular | #2E75B6 |
| Metadaten (Autor, Organisation, Stand, Version) | Arial / Helvetica | 9 pt | Regular | #666666 |
| Kapitelüberschrift (H2) | Arial / Helvetica | 14 pt | Bold | #1B3A5C |
| Abschnittsüberschrift (H3) | Arial / Helvetica | 12 pt | Bold | #2E75B6 |
| Unterabschnitt (H4) | Arial / Helvetica | 10,5 pt | Bold | #333333 |
| Fließtext | Arial / Helvetica | 9,5 pt | Regular | #000000 |
| Tabellenkopf | Arial / Helvetica | 7,5 pt | Bold | #FFFFFF |
| Tabellenzelle | Arial / Helvetica | 7,5 pt | Regular | #000000 |
| Code | Consolas / Courier | 7,5 pt | Regular | #333333 |
| Blockquote (u. a. These in § 8.5) | Arial / Helvetica | 9 pt | Italic | #333333 |
| Literaturverzeichnis (Kap. 11) | Arial / Helvetica | 9 pt | Regular | #000000 |
| Header/Footer | Arial / Helvetica | 7,5 pt | Regular | #999999 |

Zeilenabstand Fließtext: 1,15 (ca. 13 pt Leading bei 9,5 pt Schrift).
Absatzabstand: 1 mm vor, 2 mm nach.
Textausrichtung Fließtext: Blocksatz.

Im Literaturverzeichnis jeder Eintrag als eigener Absatz mit hängendem Einzug (4 mm) zur optischen Trennung der bibliographischen Angaben.

---

## 3. Farben

| Verwendung | Hex-Wert | Beschreibung |
|---|---|---|
| Primary | #1B3A5C | Dunkles Navy — Titel, H2 |
| Accent | #2E75B6 | Stahlblau — H3, Links, Trennlinien, These-Balken |
| Tabellenkopf Hintergrund | #1B3A5C | Navy |
| Tabellenkopf Text | #FFFFFF | Weiß |
| Tabelle alternierende Zeile | #F2F7FB | Hellblau |
| Tabellenrahmen | #B0C4DE | Hellgrau-Blau |
| Blockquote Hintergrund | #F0F5FA | Sehr helles Blau |
| Blockquote Seitenbalken | #2E75B6 | Accent |
| Code Hintergrund | #F5F5F5 | Hellgrau |
| Metadaten / Grautext | #666666 | Mittelgrau |
| Header/Footer Text | #999999 | Hellgrau |
| Header/Footer Linie | #CCCCCC | Sehr hellgrau |

---

## 4. Header und Footer

**Header (jede Seite ab Kapitel 1):**

- Links: Dokument-Kurztitel („Arbeitspapier — Besteuerung von KI und Robotik")
- Rechts: Organisation („HIGL — Health Innovators Group Leipzig")
- Trennlinie darunter (0,5 pt, #CCCCCC)

**Footer (jede Seite ab Kapitel 1):**

- Links: Version, Stand und Lizenzhinweis („Version X.0 — April 2026 — CC BY 4.0")
- Rechts: Seitenzahl („Seite X von N")
- Trennlinie darüber (0,5 pt, #CCCCCC)

Deckseite und Zusammenfassung (Executive Summary) erhalten weder Header noch Footer oder tragen nur die Seitenzahl.

---

## 5. Kapitelgestaltung

- Jedes H2-Kapitel beginnt auf einer neuen Seite (Seitenumbruch vor H2)
- Über jeder H2-Überschrift eine Akzentlinie (1,5 pt, #2E75B6, volle Breite)
- Ausnahme: Das erste H2 im Dokument („Zusammenfassung") direkt nach der Titelseite hat keinen Seitenumbruch davor
- Kapitel 8 („Deutschland-These") wird durch ein leicht verstärktes Akzentelement markiert (Akzentlinie 2 pt statt 1,5 pt), da es den Positionierungskern des Papiers trägt

---

## 6. Tabellen

- Volle Inhaltsbreite
- Spaltenbreiten gleichmäßig verteilt (außer bei Tabellen mit definierter Gewichtung, z. B. Typ-Übersicht in § 2.1, Kapitelstruktur in `Claude.md`)
- Kopfzeile: Navy-Hintergrund (#1B3A5C), weißer Text, Bold
- Datenzeilen: Abwechselnd weiß und hellblau (#F2F7FB)
- Rahmen: 0,5 pt, #B0C4DE
- Zellenabstand innen: 3 pt oben/unten, 4 pt links/rechts
- Kopfzeile wird bei Seitenumbruch wiederholt
- Text in Zellen bricht automatisch um

---

## 7. Blockquotes und zentrale Thesen-Hervorhebung

- Eingerückt (8 mm links)
- Hintergrund #F0F5FA
- Seitenbalken links: 3 mm breit, Vollfarbe #2E75B6
- Schrift: Italic, 9 pt
- Innenabstand: 4 mm (oben/unten/links/rechts im Inhaltsbereich)

**Sonderfall „Deutschland-These" (§ 8.5):**
Der in Kapitel 8.5 zusammengeführte Thesen-Block (beginnend mit „KI ist als eigenständiger dritter Produktionsfaktor …") wird als verstärkter Blockquote gesetzt:
- Seitenbalken 4 mm (statt 3 mm) in #1B3A5C (Primary statt Accent)
- Hintergrund #F0F5FA
- Schrift 9,5 pt Italic, #1B3A5C

**Hinweis zur PDF-Implementierung (reportlab, sofern eingesetzt):** Blockquotes werden als verschachtelte Tabelle realisiert — eine äußere Tabelle (8 mm Einzug-Spalte + Box-Spalte) und eine innere Tabelle (Balken-Spalte + Inhalts-Spalte mit #F0F5FA-Hintergrund). Innere Aufzählungspunkte als separate Bullet-Absätze im Inhaltsbereich. Kein `borderPadding` in `ParagraphStyle` verwenden — reportlab bezieht diesen Wert nicht in die Höhenberechnung ein, was zu Überlappungen mit benachbarten Elementen führt.

Bei Export über `pandoc` werden Blockquotes standardmäßig korrekt übernommen; die Deutschland-These in § 8.5 darf nicht als zusätzliche Überschrift verlinkt werden, sondern bleibt als Zitatblock erhalten.

---

## 8. Codeblöcke

Codeblöcke kommen im Arbeitspapier nicht vor. Die Regel bleibt für den Fall erhalten, dass in künftigen Versionen Beispielrechnungen oder Pandoc-Aufrufe eingebettet werden:

- Eingerückt (6 mm links)
- Hintergrund #F5F5F5
- Schrift: Consolas / Courier, 7,5 pt
- Innenabstand: 3 mm
- Kein Rahmen

---

## 9. Aufzählungen

- Eingerückt (10 mm links, 4 mm hängend)
- Aufzählungszeichen: Bullet (•)
- Zeilenabstand wie Fließtext
- Fett gesetzte Lead-Ins in Aufzählungen (z. B. die fünf Typen in § 2.1, die Produktionsfaktor-Argumente in § 8.1) bleiben in der Auszeichnung erhalten

---

## 10. Literaturverzeichnis (Kapitel 11)

- Sektionen 11.1 – 11.5 erscheinen als H3-Überschriften
- Jeder Literatureintrag als eigener Absatz, hängender Einzug 4 mm
- Zitierstil angelehnt an APA: Autor, Jahr, Titel (kursiv für Monographien und Journale), Band(Heft), Seiten, ggf. URL
- URLs in #2E75B6 (Accent), unterstrichen
- Verifizierungsbedürftige Einträge werden in Klammern mit dem Hinweis „(Bibliographische Angaben verifizierungsbedürftig)" bzw. „Vollständige Titelangabe zu verifizieren" markiert — diese Markierung bleibt auch im Export sichtbar

---

## 11. Deckseite

Empfohlene Elemente auf der ersten Seite (Deckblatt):

- Oben zentriert: Logo-Platzhalter oder dezente Akzentlinie (#2E75B6, 2 pt, 6 cm Breite)
- Haupttitel („Die Besteuerung von Künstlicher Intelligenz und Robotik als Ersatz menschlicher Arbeit"), #1B3A5C, 22 pt
- Untertitel („Ökonomische, rechtliche und sozialpolitische Perspektiven"), #2E75B6, 13 pt
- Metadatenblock (Autor, Organisation, Stand, Version, Lizenz CC BY 4.0), 10 pt, #666666
- Unten: Zitiervorschlag aus `README.md`, 8 pt, #666666

---

## 12. Erstellungsskripte

| Export | Werkzeug | Skript | Aufruf |
|---|---|---|---|
| PDF (.pdf) | reportlab | `build_pdf.py` | `python3 build_pdf.py` |
| Word (.docx) | python-docx | `build_docx.py` | `python3 build_docx.py` |

Beide Skripte lesen `Arbeitspapier_KI_Robotik_Besteuerung.md` und setzen diese Formatvorlage um: A4, Seitenränder, Schriftfamilie/-größen und Farben nach § 1–3, Header/Footer nach § 4, Akzentlinie vor jedem Kapitel (verstärkt vor Kapitel 8) nach § 5, Tabellen nach § 6, Blockquotes inklusive Thesen-Sonderfall in § 8.5 nach § 7, Aufzählungen nach § 9, Literaturverzeichnis nach § 10 und Deckseite nach § 11.

Bei Änderungen an der Formatvorlage sind beide Skripte entsprechend anzupassen. Die erzeugten Dateien (`Arbeitspapier_KI_Robotik_Besteuerung.pdf`, `Arbeitspapier_KI_Robotik_Besteuerung.docx`) werden direkt im Repo-Root abgelegt.
