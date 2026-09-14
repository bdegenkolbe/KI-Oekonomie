# Szenariokonferenz 2030 — Zwischenstand Runde 1

**Stand:** Lauf am 14. September 2026 nach 29 von 100 Stimmzetteln auf Anweisung abgebrochen.

Dieses Dokument hält fest, was gemessen wurde, und was daraus **nicht** folgt. Die Rohdaten liegen in `rohdaten/`.

## 1. Was gelaufen ist

| | |
|---|---|
| Abgegebene Stimmzettel (Opus 5) | 29 von 100 |
| Vertretene Bänke | A, B, C, D, E von A–S |
| Nicht vertreten | F Banken, G/H/I Politik, J Technik, K Datenschutz, L Industrie, M Startups, N Arbeitnehmer, O Öffentliche Finanzen, P Energie, Q Rechenzentren, R Geopolitik, S Autor |
| Kontrollarm (Sonnet 5, verworfener Vorlauf) | 20 Stimmzettel, Rollen A01–D01 |
| Durchlaufene Runden | nur Runde 1; Delphi-Revision, Red Team, Verifikation und Synthese sind **nicht** gelaufen |

## 2. Medianwerte Runde 1 (unvollständig)

| Nr. | Größe | Median | Q1 | Q3 | versch. Werte |
|---|---|---|---|---|---|
| V1 | BIP Deutschland 2030 gegenüber Nicht-KI-Pfad (%) | **2.4** | 2.1 | 2.4 | 13/29 |
| V2 | BIP EU-27 (%) | **2.1** | 1.9 | 2.6 | 15/29 |
| V3 | KI-berührte Aufgaben (% aller Aufgaben) | **7.5** | 7.4 | 8.5 | 13/29 |
| V4 | Automatisierungsgrad der berührten Aufgaben (%) | **42.0** | 41.0 | 55.0 | 14/29 |
| V5 | Lohnquote, Veränderung (Prozentpunkte) | **-1.3** | -1.7 | -0.9 | 12/29 |
| V6 | Arbeitslosenquote (%) | **6.4** | 6.1 | 6.4 | 9/29 |
| V7 | Gesamtsozialversicherungsbeitragssatz (%) | **44.8** | 44.6 | 44.9 | 11/29 |
| V8 | Diffusionsverzug regulierter Sektoren (Jahre) | **4.6** | 4.5 | 5.5 | 11/29 |
| V9 | Industriestrompreis (ct/kWh) | **16.5** | 15.8 | 16.9 | 15/29 |
| V10 | KI-Rechenzentrums-Nennanschlussleistung (GW) | **2.4** | 2.2 | 2.8 | 12/29 |
| V11 | Inferenz auf EU-Infrastruktur (%) | **19.0** | 16.0 | 22.0 | 13/29 |
| V12 | Netto-Abfluss KI-Vorleistungen (Mrd. EUR) | **21.0** | 19.0 | 23.0 | 14/29 |
| V13 | Wahrscheinlichkeit geopolitischer Schock (%) | **72.0** | 72.0 | 72.0 | 5/29 |
| V14 | Konfidenz (0–100) | **52.0** | 47.0 | 53.0 | 11/29 |

## 3. Archetyp-Verteilung

| Archetyp | Stimmen |
|---|---|
| ungebunden | 12 |
| S3 | 7 |
| S1 | 6 |
| S6 | 3 |
| S2 | 1 |

Der größte Einzelposten ist **ungebunden** mit 12 von 29 Stimmen — die Wertekombinationen dieser Rollen passen in keinen der sieben vorab definierten Archetypen. Die Definitionen wurden bewusst **nicht** nachträglich geweitet (Begründung: `00-Konzept.md` § 1).

## 4. Gemessener Modelleffekt (Kontrollarm)

Dieselben Rollen, zwei Modelle. Der Vorlauf auf Sonnet 5 wurde abgebrochen, weil die Streuung zusammenfiel; der Kontrollarm beziffert das:

| Größe | Opus: versch. Werte | Sonnet: versch. Werte |
|---|---|---|
| V1 | 10/20 | 6/20 |
| V5 | 10/20 | 7/20 |
| V11 | 11/20 | 4/20 |
| V13 | 5/20 | 2/20 |
| V7 | 8/20 | 5/20 |
| V3 | 10/20 | 4/20 |

Die Mehrheitsantwort auf K2 (wer trägt die Hauptlast) **kippt allein durch den Modellwechsel**: Opus {'öffentliche Haushalte und Beitragszahler': 21, 'Berufseinsteiger in kognitiven Berufen': 8} gegenüber Sonnet {'Berufseinsteiger in kognitiven Berufen': 15, 'öffentliche Haushalte und Beitragszahler': 5}.

## 5. Was daraus nicht folgt

- **Keine Konvergenzaussage.** Die 25-Prozent-Regel setzt 100 Stimmen und die Delphi-Revision voraus. Beides fehlt.
- **Keine Repräsentativität.** Es fehlen vierzehn von neunzehn Bänken, darunter Energie, Rechenzentren, Geopolitik, Arbeitnehmerseite und die gesamte Politik. Die vorliegenden Stimmen stammen aus Makroökonomie, Recht, Betriebswirtschaft, Medizin und Sozialversicherung — also überwiegend aus analytischen, nicht aus umsetzenden oder betroffenen Rollen.
- **Keine belastbaren Werte bei V11 und V12.** Für den Anteil in der EU betriebener Inferenz und den Abfluss für importierte KI-Vorleistungen hat kein Agent eine Datenquelle gefunden; beides sind begründete Schätzungen ohne Messgrundlage.
- **Kein Ersatz für eine Befragung.** Die Agenten sind Sprachmodelle mit Rollendossiers. Das Ergebnis ist ein strukturiertes Argumentmodell.

## 6. Bekannter Datenfehler

Das Schema-Feld `confidence` wurde von einem Teil der Agenten auf einer Skala 0–1, vom anderen auf 0–100 angegeben. Bei einer Auswertung sind Werte ≤ 1 mit 100 zu multiplizieren. Das separate Stimmzettel-Feld V14 ist davon nicht betroffen.

## 7. Fortsetzung

Der Lauf ist reproduzierbar: Konzept, Faktenkern, Roster, Stimmzettel und Auswertungsvorschrift liegen vollständig vor. Eine Fortsetzung würde bei Bank F beginnen und die Runden 2 bis 4 anschließen. Die hier gesicherten Stimmzettel bleiben verwendbar, solange Faktenkern und Stimmzettel unverändert bleiben.
