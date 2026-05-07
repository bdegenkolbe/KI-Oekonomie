# DailyPrompt-README.md — Begleitdokument zum Daily-Update-Prompt

**Zweck:** Diese Datei dokumentiert den täglichen Update-Prompt, der in `DailyPrompt.md` abgelegt ist. `DailyPrompt.md` enthält ausschließlich den ausführbaren Prompt-Text — diese Datei erklärt Zweck, Mechanik und Designentscheidungen.

**Aufruf:** Den Prompt über die Routines-Funktion von Claude Code mit folgendem Befehl ausführen:

```
Führe DailyPrompt.md als Prompt aus.
Phase-5b-Empfänger: email_to=<dein.empfaenger@example.com>, whatsapp_to=<491XXXXXXXX>
```

Die Empfängerangaben in Zeile 2 stehen in der **Routine-Konfiguration deines Claude-Code-Kontos** — sie sind nicht im Repository und nicht öffentlich. Telefonnummer im internationalen Format ohne `+` und ohne führende Null (Beispiel: `491721234567` für `+49 172 1234567`).

Claude Code liest dann den Inhalt von `DailyPrompt.md` und arbeitet die dort beschriebenen Phasen ab. Phase 5b verwendet die Empfänger aus der Routine-Anweisung; ohne Anweisung greift sie auf eine lokale `notify-config.json` zurück (sinnvoll für Test-Läufe in einer lokalen Claude-Code-Installation), und ohne beides bleibt die Benachrichtigung aus.

---

## Phasenüberblick

`DailyPrompt.md` ist in sechs Phasen gegliedert plus einem Stoppkriterien-Block:

| Phase | Zweck | Kernaktion |
|---|---|---|
| 0 | Vorbereitung | Session-Branch ermitteln, Pflichtdateien laden, Helper-Fallback aus `origin/main` |
| 1 | Recherche im Korridor | Cluster A–J aus `Suchthemen.md` abarbeiten, Trefferfilter anwenden |
| 2 | Einarbeitung | Treffer in `KI-Ökonomie.md` einspielen, Quellen ins Literaturverzeichnis |
| 3 | Validierung | Validierungsschritte gemäß `Validierung.md` durchlaufen, Versionssprung |
| 4 | Logging | Eintrag in `Änderungshistorie.md` (Quellenfluss) |
| 5 | Build | `build_pdf.py` und `build_docx.py` ausführen |
| 5b | Benachrichtigung | E-Mail und WhatsApp an die Empfänger aus der Routine-Anweisung (Fallback: `notify-config.json`) |
| 6 | Commit, Merge, Cleanup | Push auf Session-Branch, Merge auf `main`, Branch löschen |

**Phase 5b — Benachrichtigung:**
- Versendet die volle „Eingearbeitete Änderungen"-Tabelle per E-Mail und eine ≤ 1.000 Zeichen lange Zusammenfassung per WhatsApp.
- E-Mail: bevorzugt das Tool `mail_send` aus dem MCP-Server `graph-mcp` (Microsoft Graph).
- WhatsApp: bevorzugt das Tool `wa_send_message` aus dem MCP-Server `whatsapp`.
- Voraussetzung: Beide Tools müssen in den MCP-Berechtigungen auf „Always allow" stehen, sonst hängt die Routine an der Berechtigungsabfrage. Bei Status „Ask" muss der Lauf manuell bestätigt werden.
- **Empfängerdaten** (E-Mail-Adresse, Telefonnummer) liegen ausschließlich in der Routine-Konfiguration deines Claude-Code-Kontos. Sie werden über die Aufruf-Zeile (`email_to=…, whatsapp_to=…`) an den Prompt übergeben und kommen nicht ins Repository.
- Für lokale Test-Läufe (z. B. Claude Code Desktop/CLI auf deinem Rechner) kann zusätzlich eine `notify-config.json` im Repo-Root angelegt werden — gitignored, Schema in `notify-config.example.json`. Diese Datei ist als Fallback gedacht, nicht als primärer Speicherort.
- Wenn weder Routine-Anweisung noch `notify-config.json` Empfänger liefert, gilt der Versand als „nicht konfiguriert" — die Routine läuft trotzdem durch, vermerkt es im Logbuch und unterlässt den Versand.
- Wenn Empfänger vorhanden sind, aber kein passendes MCP-Tool erreichbar ist, wird der Inhalt in `daily-mail.txt` bzw. `daily-whatsapp.txt` im Repo-Root geschrieben — die Routine läuft weiter, der Merge auf `main` wird durch Versand-Probleme nicht verhindert.

---

## Designentscheidungen

- **Recherchekorridor in `Suchthemen.md`.** Der Prompt sucht ausschließlich entlang der dort definierten Cluster A–J. Wenn neue Themen hinzukommen sollen, ist `Suchthemen.md` zu erweitern — der Prompt selbst bleibt stabil.
- **Zwei Logbücher.** `Änderungshistorie.md` dokumentiert den Recherche- und Quellenfluss (was wurde im Web gefunden, was übernommen, was verworfen). Die fachlich-inhaltliche Validierung wird weiterhin in `Validierung-Ergebnisse.md` protokolliert. Beide Dateien sind komplementär.
- **Branch-agnostisch.** Phase 0 ermittelt den Session-Branch via `git branch --show-current`. Phasen 0 und 6 verwenden die ermittelte Variable. Damit funktioniert der Prompt auf jedem Routine-generierten Branchnamen.
- **Helper-Fallback.** Fehlt `Suchthemen.md` oder `Änderungshistorie.md` auf dem Session-Branch, wird die Datei aus `origin/main` nachgeladen. Fehlt sie auch dort, greift ein hartes Stoppkriterium in Phase 0.
- **Drei Sicherheitsanker.**
  1. Stoppkriterien stoppen den Lauf vor dem Merge auf `main`, wenn Validierung oder Build fehlschlagen.
  2. § 4.5-Themen aus `Claude.md` (Kapitelstruktur, Kernaussage Deutschland-These, Autorenname, Lizenz) werden nie ohne Eskalation geändert.
  3. Verifizierungsbedürftige Quellenmarkierungen bleiben erhalten, bis die Verifikation dokumentiert ist.
- **Leerlaufschutz.** Tage ohne valide Treffer erzeugen einen Logbucheintrag, aber keinen Versionssprung und keinen Build/Merge — verhindert „Versions-Inflation".

---

## Pflege

- **Themen breiter ziehen:** `Suchthemen.md` erweitern (neuer Cluster oder Ergänzung in bestehender Liste).
- **Phase im Ablauf ändern:** `DailyPrompt.md` an der entsprechenden Stelle anpassen. Phasennummerierung erhalten.
- **Stoppkriterium ergänzen:** Im Block „HARTE STOPPKRITERIEN" am Ende von `DailyPrompt.md` einen weiteren Punkt aufnehmen.
- **Build-Pipeline ändern:** Anpassung an `build_pdf.py`/`build_docx.py` und gegebenenfalls an `Formatvorlage.md` — Phase 5 verweist nur auf die Skripte.

---

## Verwandte Dateien

| Datei | Zweck |
|---|---|
| `DailyPrompt.md` | Ausführbarer Prompt-Text (wird vom Routine-Befehl gelesen) |
| `Suchthemen.md` | Recherchekorridor — Cluster A–J |
| `Änderungshistorie.md` | Logbuch für Recherche- und Quellenfluss |
| `Claude.md` | Übergreifende Projektregeln, Stil, Sicherheit |
| `Validierung.md` | Prüfprozess, Format des Validierungs-Logbuchs |
| `Validierung-Ergebnisse.md` | Historisches Validierungs-Logbuch |
| `KI-Ökonomie.md` | Hauptdokument |
