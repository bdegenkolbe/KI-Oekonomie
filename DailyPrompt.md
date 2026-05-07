# DailyPrompt.md — Täglicher Update-Prompt für das Arbeitspapier

**Zweck:** Dieser Prompt wird über die Routines-Funktion von Claude Code täglich aufgerufen. Er führt einen vollständigen Recherche-, Einarbeitungs-, Validierungs-, Build- und Merge-Zyklus für das Arbeitspapier `Arbeitspapier_KI_Robotik_Besteuerung.md` aus.

**Aufruf:** Den nachfolgenden Prompt-Text als Routine-Befehl hinterlegen oder kopieren.

---

## Prompt

```
Du führst den täglichen Update-Lauf für das Arbeitspapier
„Arbeitspapier_KI_Robotik_Besteuerung.md" durch. Halte dich strikt an die
folgende Phasenstruktur und an die Regeln aus Claude.md (insbesondere § 4.1
Stil, § 4.2 Wissenschaftliche Sorgfalt, § 4.3 Inhaltliche Regeln,
§ 4.5 Was nicht ohne Rückfrage geändert werden darf).

================================================================
PHASE 0 — Vorbereitung
================================================================
1. Aktuellen Branch prüfen. Wenn nicht auf
   `claude/daily-document-prompt-kF8qq`, dann dorthin wechseln (Branch bei
   Bedarf neu von `main` anlegen).
2. `git pull origin main` und `git pull origin claude/daily-document-prompt-kF8qq`,
   damit die lokale Basis aktuell ist.
3. `Suchthemen.md`, `Claude.md`, `Validierung.md`, das Hauptdokument und
   `Änderungshistorie.md` lesen. Aus dem letzten Eintrag in
   `Änderungshistorie.md` die zuletzt gefundenen Quellen merken
   (Deduplikationsbasis).
4. Heutiges Datum, aktuelle Versionsnummer und vorgesehene neue
   Versionsnummer (X.0 → Y.0) festlegen.

================================================================
PHASE 1 — Recherche im Korridor von Suchthemen.md
================================================================
1. Cluster A bis H aus `Suchthemen.md` der Reihe nach abarbeiten.
2. Pro Cluster mindestens drei Suchanfragen formulieren, die
   Schlüsselbegriffe × Akteure × Zeitfenster kombinieren. Zeitfenster gemäß
   `Suchthemen.md` (Standard 7 Tage; Cluster F: 48 Stunden).
3. Trefferfilter anwenden:
   – Datum innerhalb des Zeitfensters,
   – Quelle entspricht der bevorzugten Liste oder vergleichbarem Niveau,
   – Treffer fällt nicht unter die Negativliste,
   – Treffer ist nicht bereits im Hauptdokument oder im Literaturverzeichnis
     enthalten,
   – Treffer wurde nicht bereits in einem vorherigen Lauf eingespielt
     (Abgleich mit `Änderungshistorie.md`).
4. Treffer, die durch alle Filter laufen, in eine Arbeitsliste aufnehmen mit:
   Cluster, Quelle (Autor/Institution, Titel, Datum), URL, Kernaussage in
   einem Satz, Ziel-§ im Hauptdokument.
5. Wenn ein Cluster keine validen Treffer liefert, im Logbuch vermerken und
   weitermachen.

================================================================
PHASE 2 — Einarbeitung
================================================================
1. Für jeden gültigen Treffer den passenden Abschnitt im Hauptdokument
   identifizieren (vgl. § 3 Dokumentstruktur in `Claude.md`).
2. Inhalt knapp einarbeiten: ein Satz Sachverhalt + Quelle + Datum;
   keine Redundanzen zu bereits dokumentierten Inhalten erzeugen.
3. Aussagen aus Policy-Papieren, Working Papers, Gesetzentwürfen oder
   Vorschlägen im Konjunktiv referieren.
4. Quellenangabe in das passende Unterkapitel von Kapitel 11
   (Literaturverzeichnis) eintragen — Sektion gemäß Quellentyp:
   11.1 Ökonomische Forschung, 11.2 Rechtswissenschaft,
   11.3 Institutionelle/politische Dokumente, 11.4 Wertschöpfungsabgabe,
   11.5 Journalistische und praxisorientierte Quellen.
   Zitierstil angelehnt an APA, vollständige URL.
5. Wenn eine bestehende Aussage durch eine neuere Zahl/Quelle ersetzt wird:
   alte Quelle nicht löschen, sondern nachgelagert als zeitlich frühere
   Referenz erhalten („Stand März 2026: …, aktualisiert im Mai 2026: …").
6. Verifizierungsbedürftige Markierungen (de la Feria et al. 2022) nicht
   ohne dokumentierte Verifikation entfernen.
7. Inhaltsverzeichnis, Querverweise und alle Zähler („fünf Typen", „drei
   Säulen", „sieben Empfehlungen") nach Bedarf nachziehen.

================================================================
PHASE 3 — Validierung gemäß Validierung.md
================================================================
1. Vollständige Validierung gemäß `Validierung.md` § 2 durchlaufen.
2. Ergebnisse als neuen Block in `Validierung-Ergebnisse.md` protokollieren
   (Format gemäß `Validierung.md` § 3).
3. Gefundene Fehler beheben, Nachprüfung der betroffenen Schritte ausführen.
4. Versionssprung X.0 → Y.0 an allen vier Stellen eintragen:
   – Dokumentkopf des Hauptdokuments,
   – Abschluss-/Haftungshinweis am Dokumentende,
   – `README.md`,
   – Abschlussblock in `Validierung-Ergebnisse.md`.

================================================================
PHASE 4 — Logging in Änderungshistorie.md
================================================================
1. Neuen Eintrag in `Änderungshistorie.md` anlegen, Datum, fortlaufende
   Lauf-Nummer und Versionssprung in der Überschrift setzen.
2. Tabelle „Gefundene Quellen" mit allen geprüften Treffern füllen
   (übernommen / verworfen / Dublette).
3. Tabelle „Eingearbeitete Änderungen" mit Stelle (§), Art, Inhalt und
   Quellen-Nummer füllen.
4. Tabelle „Verworfene Treffer" mit Begründung füllen.
5. Verarbeitungsschritte (Recherche, Deduplikation, Validierung, PDF,
   Word, Versionsnummer, Merge) als Ja/Nein abhaken.
6. Auffälligkeiten und offene Punkte stichpunktartig festhalten.

================================================================
PHASE 5 — Build der abhängigen Dokumente
================================================================
1. `python3 build_pdf.py` ausführen — Ergebnis:
   `Arbeitspapier_KI_Robotik_Besteuerung.pdf`.
2. `python3 build_docx.py` ausführen — Ergebnis:
   `Arbeitspapier_KI_Robotik_Besteuerung.docx`.
3. Bei Fehlern in den Build-Skripten: Ursache prüfen, Build erneut
   ausführen, Ergebnis im Logbuch dokumentieren. Build-Skripte selbst
   nicht ohne Rückfrage anpassen (gehört zu § 4.5 Claude.md).

================================================================
PHASE 6 — Commit, Merge auf main, Branch-Cleanup
================================================================
1. Geänderte Dateien stagen:
     git add Arbeitspapier_KI_Robotik_Besteuerung.md \
             Arbeitspapier_KI_Robotik_Besteuerung.pdf \
             Arbeitspapier_KI_Robotik_Besteuerung.docx \
             Validierung-Ergebnisse.md \
             Änderungshistorie.md \
             README.md \
             Suchthemen.md
2. Commit-Nachricht im Format:
     „Daily-Update YYYY-MM-DD — Version Y.0 (Cluster: A, B, …)"
   gefolgt von einer kurzen Zusammenfassung der wesentlichen Ergänzungen.
3. Push auf den Feature-Branch:
     git push -u origin claude/daily-document-prompt-kF8qq
4. Wenn alle vorigen Phasen ohne Fehler abgeschlossen sind:
   – auf `main` wechseln, `git pull origin main`,
   – `git merge --no-ff claude/daily-document-prompt-kF8qq`,
   – `git push origin main`,
   – lokalen Branch löschen: `git branch -d claude/daily-document-prompt-kF8qq`,
   – Remote-Branch löschen: `git push origin --delete claude/daily-document-prompt-kF8qq`.
5. Branch-Status im Logbuch festhalten.

================================================================
HARTE STOPPKRITERIEN
================================================================
- Wenn die Validierung in Phase 3 nicht ohne offene Fehler abgeschlossen
  werden kann: Lauf in Phase 3 stoppen, Stand committen und pushen, Merge
  auf main NICHT ausführen, im Logbuch Status „Stop in Phase 3" eintragen
  und den Grund nennen.
- Wenn Phase 5 (Build) fehlschlägt: Lauf in Phase 5 stoppen, Stand
  committen und pushen, Merge NICHT ausführen, im Logbuch Status
  „Stop in Phase 5" eintragen.
- Wenn keine validen Treffer aus Phase 1 vorliegen: Phasen 2–6 entfallen,
  in Phase 4 einen „Leerlauf-Eintrag" anlegen (Versionssprung entfällt,
  Build entfällt, Merge entfällt) und den Lauf abschließen.
- Wenn ein Treffer Inhalte aus § 4.5 Claude.md berührt (Kapitelstruktur,
  Kernaussage Deutschland-These, Autorenname, Lizenz): Treffer NICHT
  einarbeiten, im Logbuch als „eskalationspflichtig" markieren.

================================================================
ABSCHLUSSBERICHT
================================================================
Am Ende des Laufs einen Bericht in der Antwort ausgeben mit:
- Lauf-Nummer und neuer Versionsnummer,
- Anzahl geprüfter Treffer / übernommener Treffer / verworfener Treffer
  je Cluster,
- Liste der eingearbeiteten Änderungen mit §-Verweis,
- Status der Phasen (OK / Stop),
- Verweis auf den neuen Block in `Änderungshistorie.md` und in
  `Validierung-Ergebnisse.md`,
- Status von Merge und Branch-Cleanup.
```

---

## Hinweise zum Prompt-Design

- **Recherchekorridor:** Der Prompt sucht ausschließlich entlang der in `Suchthemen.md` definierten Cluster. Wenn neue Themen hinzukommen sollen, ist `Suchthemen.md` zu erweitern — der Prompt selbst bleibt stabil.
- **Zwei Logbücher:** `Änderungshistorie.md` dokumentiert Recherche- und Quellenfluss, `Validierung-Ergebnisse.md` dokumentiert die fachlich-inhaltliche Prüfung. Beide werden gefüllt.
- **Drei Sicherheitsanker:** (1) harte Stoppkriterien stoppen den Lauf vor dem Merge auf main, wenn Validierung oder Build fehlschlagen; (2) § 4.5-Themen aus `Claude.md` werden nie ohne Eskalation geändert; (3) verifizierungsbedürftige Quellenmarkierungen bleiben erhalten, bis die Verifikation dokumentiert ist.
- **Leerlauf:** Tage ohne valide Treffer erzeugen einen Logbucheintrag, aber keinen Versionssprung und keinen Build/Merge — verhindert „Versions-Inflation".
