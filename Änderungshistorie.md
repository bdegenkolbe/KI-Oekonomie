# Änderungshistorie.md — Logbuch der täglichen Update-Läufe

**Zweck:** Diese Datei protokolliert jeden täglichen Recherche- und Update-Lauf des Daily-Update-Prompts. Pro Lauf entsteht ein zeitstempelbasierter Block — die Historie wird **nicht gelöscht**, sondern wächst chronologisch an.

**Verhältnis zu `Validierung-Ergebnisse.md`:** Diese Datei dokumentiert den **Recherche- und Quellenfluss** (was wurde im Web gefunden, was wurde übernommen, was wurde verworfen). Die fachlich-inhaltliche Validierung des Hauptdokuments wird weiterhin in `Validierung-Ergebnisse.md` protokolliert. Beide Dateien sind komplementär.

**Format pro Eintrag:**

```
## YYYY-MM-DD — Lauf NNN — Version X.0 → Version Y.0

### Recherchekorridor

- Genutzte Cluster aus `Suchthemen.md`: A, B, …
- Zeitfenster: letzte N Tage / Stunden
- Anzahl Suchanfragen: NN

### Gefundene Quellen

| # | Cluster | Quelle (Autor/Institution, Titel, Datum) | URL | Bewertung |
|---|---------|-----------------------------------------|-----|-----------|
| 1 |         |                                         |     | übernommen / verworfen / Dublette |

### Eingearbeitete Änderungen

| # | Stelle (§) | Art (Ergänzung / Aktualisierung / Korrektur) | Inhalt in einem Satz | Quelle # |
|---|-----------|----------------------------------------------|----------------------|----------|
| 1 |           |                                              |                      |          |

### Verworfene Treffer (mit Begründung)

| # | Quelle | Cluster | Begründung |
|---|--------|---------|------------|
| 1 |        |         | außerhalb Zeitfenster / Negativliste / Dublette / Quellenniveau |

### Verarbeitungsschritte

- Recherche abgeschlossen: Ja / Nein
- Deduplikation gegen Hauptdokument: Ja / Nein
- Validierung gemäß `Validierung.md` ausgeführt: Ja / Nein (Verweis auf Block in `Validierung-Ergebnisse.md`)
- PDF erstellt (`build_pdf.py`): Ja / Nein
- Word erstellt (`build_docx.py`): Ja / Nein
- Versionsnummer in Hauptdokument, README, Validierung-Ergebnisse aktualisiert: Ja / Nein
- Branch auf main gemerged und gelöscht: Ja / Nein

### Auffälligkeiten / offene Punkte

- 

---
```

**Erstinitialisierung:** Datei angelegt am 2026-05-07. Erster regulärer Lauf folgt mit dem nächsten Aufruf des Daily-Update-Prompts.
