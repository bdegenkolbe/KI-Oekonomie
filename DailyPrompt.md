Du führst den täglichen Update-Lauf für das Arbeitspapier
„KI-Ökonomie.md" durch. Halte dich strikt an die folgende Phasenstruktur
und an die Regeln aus Claude.md (insbesondere § 4.1 Stil, § 4.2
Wissenschaftliche Sorgfalt, § 4.3 Inhaltliche Regeln, § 4.5 Was nicht
ohne Rückfrage geändert werden darf).

================================================================
PHASE 0 — Vorbereitung
================================================================
1. Den aktuellen Session-Branch ermitteln:
     SESSION_BRANCH=$(git branch --show-current)
   Auf diesem Branch wird der gesamte Lauf ausgeführt. Wenn der Branch
   nicht existiert oder leer ist (Detached HEAD), einen frischen Branch
   `claude/daily-update-YYYY-MM-DD` von `main` anlegen.
2. `git fetch origin` und anschließend `git pull origin $SESSION_BRANCH`
   (falls Remote-Tracking) oder die Basis von `main` ziehen, damit die
   lokale Basis aktuell ist.
3. Pflichtdateien einlesen: `Claude.md`, `Validierung.md`, das
   Hauptdokument `KI-Ökonomie.md`, `Suchthemen.md` und
   `Änderungshistorie.md`.
   Wenn `Suchthemen.md` oder `Änderungshistorie.md` auf dem Session-Branch
   fehlen, von `origin/main` nachladen:
     git checkout origin/main -- Suchthemen.md Änderungshistorie.md
   Wenn die Dateien auch auf `main` fehlen, den Lauf in Phase 0 stoppen
   und den Status „Stop in Phase 0 — Helper-Dateien fehlen" eintragen.
4. Aus dem letzten Eintrag in `Änderungshistorie.md` die zuletzt
   gefundenen Quellen merken (Deduplikationsbasis).
5. Heutiges Datum, aktuelle Versionsnummer und vorgesehene neue
   Versionsnummer (X.0 → Y.0) festlegen.

================================================================
PHASE 1 — Recherche im Korridor von Suchthemen.md
================================================================
1. Cluster A bis J aus `Suchthemen.md` der Reihe nach abarbeiten.
2. Pro Cluster mindestens drei Suchanfragen formulieren, die
   Schlüsselbegriffe × Akteure × Zeitfenster kombinieren. Zeitfenster gemäß
   `Suchthemen.md` (Standard 7 Tage; Cluster F und Cluster I: 48 Stunden).
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
6. Breite vor Tiefe: Pro Lauf höchstens zwei Cluster wirklich vertiefen,
   die übrigen mit knappen Ergänzungen abdecken — das Dokument soll an
   Breite gewinnen, ohne in einzelnen Themen zu kippen.

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
1. `python3 build_pdf.py` ausführen — Ergebnis: `KI-Ökonomie.pdf`.
2. `python3 build_docx.py` ausführen — Ergebnis: `KI-Ökonomie.docx`.
3. Bei Fehlern in den Build-Skripten: Ursache prüfen, Build erneut
   ausführen, Ergebnis im Logbuch dokumentieren. Build-Skripte selbst
   nicht ohne Rückfrage anpassen (gehört zu § 4.5 Claude.md).

================================================================
PHASE 5b — Benachrichtigung (E-Mail und WhatsApp)
================================================================
Diese Phase versendet die Tagesänderungen per E-Mail und eine
Kurzzusammenfassung per WhatsApp.

Empfänger werden zur Laufzeit aus der lokalen, gitignorierten Datei
`notify-config.json` im Repo-Root gelesen (Schema siehe
`notify-config.example.json`). Pflichtfelder: `email_to`,
`whatsapp_to`. Wenn die Datei fehlt oder unvollständig ist, gilt das
als „Versand nicht konfiguriert" (siehe Schritt 3 unten).

1. Aus dem soeben in Phase 4 angelegten Block in
   `Änderungshistorie.md` zwei Texte erzeugen:

   a) **E-Mail-Inhalt** (Plaintext oder leichtes Markdown):
      – Betreff: „Daily-Update KI-Ökonomie YYYY-MM-DD — Version Y.0"
      – Body: Datum, Versionssprung X.0 → Y.0, Anzahl geprüfter und
        übernommener Treffer, vollständige Tabelle „Eingearbeitete
        Änderungen" (Stelle, Art, Inhalt, Quelle), Status der Phasen
        (OK / Stop), Verweis auf den Block in `Änderungshistorie.md`.
      – Maximal 5.000 Zeichen.

   b) **WhatsApp-Zusammenfassung** (Plaintext, ≤ 1.000 Zeichen):
      – Eine Zeile mit Datum und Versionssprung.
      – Drei bis fünf Bulletpoints mit den wichtigsten eingearbeiteten
        Änderungen (Stelle § + Inhalt in einem halben Satz).
      – Eine Zeile zum Lauf-Status (alle Phasen OK / Stop in Phase X).

2. Versandkanäle ansteuern. Empfänger jeweils aus
   `notify-config.json` (`email_to` und `whatsapp_to`) übernehmen —
   keine Empfängerdaten im Prompt, im Logbuch, in Commits oder im
   Abschlussbericht ausschreiben:

   a) **E-Mail:** Bevorzugtes Tool ist `mail_send` aus dem MCP-Server
      `graph-mcp` (Microsoft Graph). Sollte dieses nicht erreichbar
      sein, ein anderes verfügbares Tool zum Versand einer Outlook-/
      Microsoft-Graph-E-Mail wählen (Tool-Namen-Muster, das *eines*
      der folgenden enthält: `mail_send`, `send_mail`, `send_message`,
      `outlook_send`). Wenn kein solches Tool in der laufenden Session
      erreichbar ist, den vorbereiteten E-Mail-Inhalt nach
      `daily-mail.txt` im Repo-Root schreiben und im Logbuch unter
      „Auffälligkeiten" vermerken.

   b) **WhatsApp:** Bevorzugtes Tool ist `wa_send_message` aus dem
      MCP-Server `whatsapp`. Sollte dieses nicht erreichbar sein,
      ein anderes Tool aus dem `whatsapp`-Server wählen, dessen Name
      `send` oder `send_message` enthält (z. B. `wa_send_message` für
      Text, ggf. `wa_send_media` mit Text-Caption als Notlösung).
      Wenn kein solches Tool erreichbar ist, die Zusammenfassung nach
      `daily-whatsapp.txt` im Repo-Root schreiben und im Logbuch unter
      „Auffälligkeiten" vermerken.

3. **Versandfehler sind weich.** Schlägt der eigentliche Versand
   fehl, wird der Fehler im Logbuch unter „Auffälligkeiten"
   dokumentiert (ohne Empfängerdaten zu nennen) und der Lauf fährt
   mit Phase 6 fort. Der Merge auf `main` wird durch fehlgeschlagene
   Benachrichtigung NICHT verhindert — die Aktualisierung des
   Dokuments ist wichtiger als die Zustellung der Benachrichtigung.
   Fehlt `notify-config.json` ganz, gilt der Versand als „nicht
   konfiguriert"; in diesem Fall werden weder Tools aufgerufen noch
   Fallback-Textdateien geschrieben, und der Lauf vermerkt im Logbuch
   einen entsprechenden Hinweis.

4. Ergebnisse beider Kanäle (versendet / Fallback-Datei / nicht
   konfiguriert / Fehler) im Logbuch unter „Verarbeitungsschritte" als
   zusätzliche Punkte aufnehmen — ohne Empfängerangabe.

================================================================
PHASE 6 — Commit, Merge auf main, Branch-Cleanup
================================================================
1. Geänderte Dateien stagen:
     git add KI-Ökonomie.md \
             KI-Ökonomie.pdf \
             KI-Ökonomie.docx \
             Validierung-Ergebnisse.md \
             Änderungshistorie.md \
             README.md \
             Suchthemen.md
2. Commit-Nachricht im Format:
     „Daily-Update YYYY-MM-DD — Version Y.0 (Cluster: A, B, …)"
   gefolgt von einer kurzen Zusammenfassung der wesentlichen Ergänzungen.
3. Push auf den Session-Branch:
     git push -u origin "$SESSION_BRANCH"
4. Wenn alle vorigen Phasen ohne Fehler abgeschlossen sind:
   – auf `main` wechseln, `git pull origin main`,
   – `git merge --no-ff "$SESSION_BRANCH"`,
   – `git push origin main`,
   – lokalen Branch löschen: `git branch -d "$SESSION_BRANCH"`,
   – Remote-Branch löschen: `git push origin --delete "$SESSION_BRANCH"`.
5. Branch-Status (Name des Session-Branches und Cleanup-Ergebnis) im
   Logbuch festhalten.

================================================================
HARTE STOPPKRITERIEN
================================================================
- Wenn `Suchthemen.md` oder `Änderungshistorie.md` weder auf dem
  Session-Branch noch auf `origin/main` vorhanden sind: Lauf in Phase 0
  stoppen, KEIN Commit, KEIN Merge, im Logbuch (sobald wieder verfügbar)
  Status „Stop in Phase 0 — Helper-Dateien fehlen" eintragen.
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
- Status von E-Mail- und WhatsApp-Versand (versendet / Fallback-Datei
  geschrieben / Fehler),
- Status von Merge und Branch-Cleanup.
