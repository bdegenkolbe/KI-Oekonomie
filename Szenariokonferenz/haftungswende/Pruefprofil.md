# Prüfprofil — Die Haftungswende

**Dokumentdatei:** `Die-Haftungswende.html` (erzeugt aus `baue.py`), Druckfassung `Die-Haftungswende.pdf`, Lesefassung für die Prüfung `Die-Haftungswende.md` (erzeugt aus `als_markdown.py`)
**Dokumenttyp:** Strategiepapier
**Zielgruppe:** Gesellschafter und Geschäftsführungen des HIGL-Verbunds, keine Fachökonomen
**Sprache:** de
**Letzte Validierung:** 26.09.2026, Fassung 2.0

## Zweck
Das Papier schafft einen **strategischen Rahmen**: Richtung, Voraussetzungen, Handlungsfelder, Zeitfenster und Signale. Es ist **keine Beschlussvorlage**. Formulierungen, die Beschlüsse vorwegnehmen („zu beschließen“, „binär“, „negativ zu entscheiden“, Fristen mit Zuständigen), sind Fehler.

## Struktur-Sollzustand
- Titelseite mit Inhalt, „Auf einen Blick“, Kapitel 1–7, Anhang (Methode, Grenzen, Begriffe, Quellen)
- Querverweis-Syntax: „Kapitel N“, „Abbildung N“; Begriffe per Ankerlink `#g-<schlüssel>`
- Zählerstellen: 21 Abbildungen; sechs Kernaussagen; drei Voraussetzungen; fünf Handlungsfelder; sechs Signale; vier Unterschiede US-Studie/Europa (Abb. 3); 16 Begriffe
- Wiederkehrende Formatmuster: Kapitelkopf mit Kernsatz; jedes der Kapitel 1–6 endet mit dem Kasten „Was das für den Verbund heißt“; Abbildung = Nummer, Aussagetitel, Unterzeile, Grafik, Quelle
- Progression / roter Faden: Leitfrage (Auf einen Blick) → Europa → Deutschland → Gesundheitswesen → Pharma/USA → Markt des Verbunds → Gesellschaften → Rahmen (Kapitel 7 fasst die sechs Folgerungen in Abbildung 17 zusammen)
- Historiendatei: `Die-Haftungswende_Historie.md`

## Inhalt
- Normen: SGB V §§ 35a, 71 Abs. 3, 130b (Abs. 1c); KHEntgG § 21; KHAG; VO (EU) 2024/1689; EHDS-Verordnung; Proclamation 11020
- Kernzahlen (Soll): Beitragsbasis 1.790 Mrd. € (1.680–1.930), KI-Anteil ~10 Mrd. €; GKV-Leistungsausgaben 420 Mrd. € (+26,9 % ggü. 331,062), Vergütung je Leistung +13 % (+16 %; +8…+20), real −4…−10 %; Preisdurchgriff 52/20/12/28/58 %; Szenariowahl 73/8/2 von 83; US-Effekt 14 von 18 positiv, Median +9 %; Evidenzmarkt 800 Mio. € (550–1.150), Preisindex 75, Menge ×1,5; Wertanteil 70/30 → 32/68; Verbund +5 % / DB −15 % (Pfad A), −30 % / −60 % (Pfad B), Abstand 5,1 Mio. €; Außenumsatz 2025 14,48 Mio. €, Netto-Erlöse 17,57 Mio. €
- Volatile Sachverhalte: Referentenentwurf § 130b Abs. 1c; Beginn Hochrisikopflichten KI-VO; GLOBE-Endregel; Überprüfung Generika-Ausnahme; EHDS-Umsetzung
- Redundanzsensibel: Pfade A/B (Auf einen Blick = Kurzfassung, Kapitel 7 = ausführlich); drei Voraussetzungen (Kapitel 5 = Definition, Kapitel 7 = Rahmen); Szenarien trennen sich nach 2027 (Kapitel 1, in Kapitel 7 nur aufgegriffen)
- Argumentationslinie: Preis folgt im Gesundheitswesen kaum der Produktivität → Kunden haben mehr Arbeit, knappe Budgets, strengere Nachweise → Wert wandert von der Standardauswertung zur Leistung mit Haftung → Richtung „vom Auswerten zum Einstehen“
- Auseinanderzuhalten: Standardauswertung vs. Leistung mit Haftung; Pfad A vs. Pfad B (getrennte Szenarien, keine Intervallränder); Netto-Erlöse vs. Außenumsatz vs. brutto fakturiertes Volumen

## Terminologie, Register und Stil
- Register: laienverständlich; jeder Fachbegriff bei Erstnennung erklärt oder mit dem Glossar verlinkt
- Glossar: ja, Anhang „Begriffe“; jede Erstnennung verlinkt, jeder Eintrag im Text verwendet
- Verbindliche Begriffe: „Fachrollen“ und „Einschätzungen“ (nicht „Fachurteile“, „Karten“, „Urteile“); „Stufe der Wirkungskette“ (nicht „Station“); „Standardauswertung“ und „Leistung mit Haftung“ (nicht „beschreibende/haftende Schicht“); „Engpass“ (nicht „bindendes Hemmnis“); „Pfad A/B“
- Abkürzungen mit Erstnennungspflicht: BIP, GKV, PKV, IAB, KHAG, InEK, EHDS, MFN, DB
- Werte für 2031 im Konjunktiv (Claude.md § 4.2); Ist-Werte und geltendes Recht im Indikativ
- Projektspezifische Stilregeln: keine Gedankenstriche im Fließtext (in Tabellen als Leerfeld zulässig); keine Zuspitzungsformeln „nicht X, sondern Y“ als Stilmittel; kein Verfahrensjargon der Konferenz im Fließtext
- KI-Slang-Liste: `slang-liste.txt` (für `validate_doc.py --slang-liste`)

## Automatisierte Prüfung
- `python3 pruefe.py` erzeugt die Lesefassung, ruft `validate_doc.py` mit **allen** Checks auf (auch Querverweise) und filtert nur §-Treffer mit Gesetzesbezug in derselben Zeile (SGB, KHEntgG). Zusätzlich: Abbildungsnummern fortlaufend, Abbildungsverweise gültig, verbotener Verfahrensjargon, jeder Begriff verlinkt. Exit-Code 1 bei Befund.
- Lesefassung: Kapitel als nummerierte Überschriften (`## N Titel`), Begriffe als `####`-Überschriften, Inhaltsverzeichnis und Begriffslinks als Markdown-Anker

## Quellen
- Zitierstil: Kurzangaben in Bildunterschriften, Verzeichnis im Anhang
- Pflichtstichproben: 1.790/1.550 Mrd. € (29-Strategiepapier K1); 420 vs. 331,062 Mrd. € (Ü1); 12 % Preisdurchgriff Leistungserbringer (Rohdaten D2); 14 von 18 positiv (S3-Karten); 52 % Kundenkonzentration 4K (baue-sitzung-d.py, brutto fakturiert)
- Verifizierungsbedürftig: Marktgröße Evidenzmarkt (einziger Vergleichswert RWE 204,2 Mio. USD 2023)

## Meta
- Organisation: HIGL-Verbund, Puschstraße 6a, 04103 Leipzig
- Versionsformat: X.0; Versionsstellen: Titelseite (Stand), Schlussvermerk im Anhang, PDF-Fußzeile (`drucke.js`), Protokoll
- Pflichthinweise: KI-Offenlegung (Anhang, Methode und Schlussvermerk); Hinweis, dass das Papier keine Beschlüsse ersetzt

## Export
- HTML-Artefakt und PDF (A4, Seitenzahlen, rund 20–24 Seiten) über `python3 baue.py && node drucke.js Die-Haftungswende.html Die-Haftungswende.pdf light`
- Gestaltung: eigene Vorlage in `baue.py` (IBM Plex Sans / Source Serif 4), nicht die Aptos-Standardvorlage

## Bekannte Fehlermuster
- Anker ohne Umlaute (`slugify()` in validate_doc.py zerlegt ä/ö/ü per NFKD); Anker folgen der GitHub-Regel, Prüfung in `pruefe.py`
- Lesefassung verlor Links, Listenmarken und Kapitelnummern (Konverter v1); Querverweisprüfung war deshalb abgeschaltet. Seit Konverter v2 läuft sie mit.
- Begriffslinks brechen die Deklination („Der Europäischer …“, „Die Beitragspflichtige …“): beim Einsetzen von `B()` die gebeugte Form übergeben
- Anteile ohne Mehrheit als „überwiegend“ bezeichnet (40 % Kundenanteil)
- Bezugsgröße der Kundenkonzentration: brutto fakturiert, nicht Netto-Außenumsatz
- Mittelwert und Median verwechselt („im Mittel“ bei Medianen)
