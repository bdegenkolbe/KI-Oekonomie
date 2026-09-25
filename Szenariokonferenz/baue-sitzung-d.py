# -*- coding: utf-8 -*-
"""Baut workflow-sitzung-d.js — die Uebertragungskette.

Grundlage ist das Anthropic-Papier (Korinek/Jones/Sacher/Cotter/McCrory,
Economic Scenarios for Transformative AI, WP 2026-02). Die Kette laeuft
Makro -> GKV/PKV -> Leistungserbringer -> Pharma/US-Schock -> HIGL.

Alles, was in den Sitzungen A bis C bereits erhoben und geprueft wurde, wird
als Bestand mitgegeben und darf nicht neu hergeleitet werden. Recherchiert wird
nur, was dort nachweislich fehlt.
"""
import json, os, sys
from roster_d import ROLLEN, STATIONEN, als_dicts

HIER = os.path.dirname(os.path.abspath(__file__))

def lies(name):
    with open(os.path.join(HIER, name), encoding="utf-8") as fh:
        return fh.read()

def einzeilig(x):
    """Absaetze zu einer Zeile — Kartenbloecke im Prompt sind zeilenweise aufgebaut."""
    return " ".join(str(x or "").split())

# ---------------------------------------------------------------- Bestand
BRIEFING   = lies("01-Briefing.md")
GUELTIG    = lies("22-Teil-0-Gueltigkeit.md")
DEUTSCHLAND= lies("23-Teil-1-Deutschland.md")
EUROPA     = lies("24-Teil-2-Europa.md")
KANAELE    = lies("20-Durchgriffskanaele.md")
QUELLPRUEF = lies("21-Quellenpruefung.md")

BESTAND = (
 "# BESTAND — bereits erhoben, geprueft und nicht neu herzuleiten\n\n"
 "Die folgenden Unterlagen stammen aus den Sitzungen A bis C derselben Konferenz. "
 "Sie sind validiert. Du darfst ihnen widersprechen, aber nur mit Begruendung, und "
 "du darfst ihre Zahlen nicht ohne Not neu herleiten.\n\n"
 "## Gemeinsamer Faktenkern\n\n" + BRIEFING +
 "\n\n## Teil 0 — Gueltigkeitsbereich und Grenzen des Instruments\n\n" + GUELTIG +
 "\n\n## Teil 1 — Deutschland (Personalbedarf im Gesundheitswesen)\n\n" + DEUTSCHLAND +
 "\n\n## Teil 2 — Europaeischer Vergleich\n\n" + EUROPA +
 "\n\n## Durchgriffskanaele\n\n" + KANAELE
)

KEINE_DOPPELUNG = """
# RECHERCHEREGEL — keine Quelle zweimal

Folgende Domaenen sind in Runde 0 der Sitzung A vollstaendig recherchiert und in
der Quellenpruefung nachgeprueft worden. Recherchiere darin NICHT erneut; nimm die
Werte aus dem Bestand:

  R01 GKV- und SPV-Finanzen        R02 Versorgungsstrukturen
  R03 Gesundheitspersonal          R04 KI in der Versorgung
  R05 Recht und Regulierung        R06 Digitale Infrastruktur
  R07 Europaeischer Systemvergleich R08 Makrooekonomie und Szenariogeruste
  R09 Compute, Energie, Souveraenitaet  R10 Geopolitik und Lieferketten

Neu recherchiert wird in dieser Sitzung ausschliesslich das, was dort fehlt und
in Runde 0 dieser Sitzung geliefert wird (Bloecke N01 bis N06). Wenn du eine Zahl
brauchst, die weder im Bestand noch in den neuen Faktenblaettern steht, kennzeichne
sie als Schaetzung — recherchiere sie nicht selbst nach.
"""

# ---------------------------------------------------------------- Rechercheure
RECHERCHE = [
 ("N01", "US-Arzneimittelpolitik",
  "Section-232-Zoelle auf patentierte Arzneimittel und Wirkstoffe (Proklamation vom 2. April 2026): "
  "Tarifstufen, Stichtage 31.07.2026 und 29.09.2026, Nullsatz bei MFN- plus Onshoring-Vereinbarung, "
  "Auslaufen am 20.01.2029. Meistbeguenstigung: Executive Order vom 12.05.2025, Umsetzung ueber die "
  "CMMI-Modelle GENEROUS, GLOBE und GUARD mit ihren Startterminen, Stand und Zahl der Herstellerdeals, "
  "abgedeckter Marktanteil. Und der fuer Deutschland entscheidende Punkt: die Rolle des deutschen "
  "AMNOG-Erstattungsbetrags als einzige oeffentlich zugaengliche Nettopreisreferenz Europas.",
  "Jede Angabe mit Fundstelle und Abrufdatum. Angekuendigte Massnahme, in Kraft getretene Massnahme und "
  "gerichtlich angegriffene Massnahme streng trennen. Keine Prognose ueber den Rechtsstand hinaus."),
 ("N02", "Private Krankenversicherung",
  "Vollversichertenbestand und Entwicklung, Beitragsanpassungen der letzten Jahre, Alterungsrueckstellung "
  "und Rechnungszins, Beihilfesysteme der Laender und die pauschale Beihilfe, Wanderungsbewegungen "
  "zwischen GKV und PKV, Versicherungspflichtgrenze, Ertragslage der Branche.",
  "Bestandszahlen und Beitragseinnahmen nie vermischen. Branchenmittelwerte kennzeichnen — die Spreizung "
  "zwischen den Unternehmen ist gross."),
 ("N03", "Krankenhausfinanzierung nach dem KHVVG",
  "Stand der Umsetzung je Land, Leistungsgruppenzuweisung, Vorhaltefinanzierung und ihr Zeitpfad, "
  "Transformationsfonds, Landesbasisfallwerte, Investitionsquote der Laender, Insolvenzen und "
  "Traegerwechsel, Ergebnislage der Krankenhaeuser.",
  "Landesrecht ist uneinheitlich — Unterschiede benennen, nicht mitteln. Plan und Vollzug trennen."),
 ("N04", "GKV-Finanzlage nach dem Stabilisierungsgesetz",
  "Beitragssatz und durchschnittlicher Zusatzbeitrag, beitragspflichtige Einnahmen je Mitglied, "
  "Ruecklagen, Bundeszuschuss, Konsolidierungsvolumen des GKV-Beitragssatzstabilisierungsgesetzes und "
  "seine Instrumente, Ausgabenentwicklung je Leistungsbereich.",
  "Nicht ueber das letzte veroeffentlichte Jahr hinaus fortschreiben. Gesetzentwuerfe im Konjunktiv."),
 ("N05", "AMNOG, Evidenzmarkt und Versorgungsforschung",
  "Zahl der Nutzenbewertungsverfahren und Erstattungsbetragsverhandlungen je Jahr, Verfahrensdauer, "
  "Anteil der Verfahren mit Zusatznutzen, anwendungsbegleitende Datenerhebung, Marktvolumen fuer "
  "Health Economics and Outcomes Research und Versorgungsforschung in Deutschland, Zahl der Anbieter, "
  "typische Projektvolumina, Nutzung von Sekundaerdaten nach Paragraf 303 SGB V.",
  "Marktvolumenangaben sind oft Schaetzungen von Marktforschern — als solche kennzeichnen und die "
  "Methode benennen. Keine eigene Hochrechnung ohne ausgewiesene Annahme."),
 ("N06", "KI-Faehigkeitsstand und physische Schicht",
  "Gemessener Stand der Agentenfaehigkeit bei laengeren Arbeitsvorgaengen, Inferenzkosten je Leistung "
  "und ihr Verlauf, Einsatzquoten in deutschen Unternehmen nach Branche, Stand der Service- und "
  "Pflegerobotik einschliesslich Stueckkosten und Sicherheitszulassung. Genau die Schicht, die das "
  "Anthropic-Papier ausdruecklich ausblendet und deretwegen es nicht ueber 2030 hinausrechnet.",
  "Laborergebnis, Pilotbetrieb und Regelbetrieb streng trennen. Angekuendigte Faehigkeit ist keine "
  "verfuegbare Faehigkeit. Herstellerangaben als solche kennzeichnen."),
]

# ---------------------------------------------------------------- Angriffe
ANGRIFFE = [
 (1, "Die Kette haelt nicht",
  "Pruefe die fuenf Uebergabegroessen gegeneinander. Wo ist der Wert, den eine Station weitergibt, "
  "nicht derselbe, den die naechste entgegennimmt? Wo wurde eine Groesse stillschweigend umdefiniert? "
  "Jede Bruchstelle mit Station, Groesse und Betrag."),
 (2, "Die Lohnquote ist nicht der Kanal",
  "Die ganze Kette haengt daran, dass eine fallende Lohnquote die beitragspflichtigen Entgelte senkt. "
  "Greife das an: Beitragsbemessungsgrenze, Verschiebung zwischen Beschaeftigungsformen, "
  "Mindestbeitraege, Bundeszuschuss, steigende Beschaeftigung bei fallender Quote. "
  "Zeige, unter welchen Bedingungen der Kanal bricht."),
 (3, "Der US-Schock wirkt umgekehrt",
  "Die Kette unterstellt, dass die US-Preispolitik den deutschen Preisdruck erhoeht. Begruende das "
  "Gegenteil: hoehere deutsche Preise, weil Hersteller den Referenzpunkt schuetzen; Marktruecknahmen; "
  "verzoegerte Markteintritte; Verlagerung in vertrauliche Erstattungsbetraege. Was davon ist belegbar?"),
 (4, "HIGL profitiert, statt zu verlieren",
  "Die HIGL-Station rechnet mit sinkenden Preisen fuer Evidenz und Analytik. Begruende die Gegenthese: "
  "Wenn der deutsche Erstattungsbetrag zur amerikanischen Rechengroesse wird, steigt der Einsatz je "
  "Dossier erheblich. Was folgt daraus fuer Umsatz, Preis und Wettbewerb?"),
 (5, "Das Anthropic-Papier traegt die Uebertragung nicht",
  "Das Modell ist vollstaendig an US-Daten kalibriert, bildet nur kognitive Aufgaben ab, kennt keine "
  "Preisrigiditaeten und keine Politoekonomie, und die Autoren nennen die Szenarien ausdruecklich "
  "keine Prognosen. Zeige, an welchen Stellen die Konferenz dieses Modell traegt, wo es das nicht "
  "aushaelt — und welche Ergebnisse dadurch ungueltig werden."),
]

KAPITEL = [
 ("K1", "Station 0 — Was KI mit der deutschen Lohnsumme macht"),
 ("K2", "Station 1 — GKV und PKV: die Finanzierungsstruktur unter Druck"),
 ("K3", "Station 2 — Krankenhaeuser, Praxen, Pflege: wer die Kuerzung traegt"),
 ("K4", "Station 3 — Pharma zwischen deutschem Preisdruck und amerikanischem Zugriff"),
 ("K5", "Station 4 — Was das fuer die HIGL-Gesellschaften heisst"),
]

# ---------------------------------------------------------------- Schemata
S_FAKTEN = {
 "type":"object",
 "properties":{
  "id":{"type":"string"},
  "befunde":{"type":"array","items":{"type":"object","properties":{
     "groesse":{"type":"string"},"wert":{"type":"string"},"stand":{"type":"string"},
     "quelle":{"type":"string"},"art":{"type":"string","enum":["Messung","amtliche Statistik","Rechtsstand","Schaetzung","Herstellerangabe","Prognose"]}},
     "required":["groesse","wert","stand","quelle","art"]}},
  "luecken":{"type":"array","items":{"type":"string"}},
  "warnungen":{"type":"array","items":{"type":"string"}}},
 "required":["id","befunde","luecken","warnungen"]}

def s_rolle(mit_us=False):
    p = {
     "id":{"type":"string"},
     "szenario":{"type":"string","enum":["modest","substantial","extreme"]},
     "k1":{"type":"number"},"k1_u":{"type":"number"},"k1_o":{"type":"number"},
     "k2":{"type":"number"},"k2_u":{"type":"number"},"k2_o":{"type":"number"},
     "k3":{"type":"number"},"k3_u":{"type":"number"},"k3_o":{"type":"number"},
     "k4_automatisiert":{"type":"number"},
     "k5_neue_aufgaben":{"type":"number"},
     "d1_physisch":{"type":"number"},
     "d2_preisdurchgriff":{"type":"number"},
     "d3_wechselabschlag":{"type":"number"},
     "d4_verzoegerung_jahre":{"type":"number"},
     "d4_institution":{"type":"string"},
     "e1_lohnquote_pp":{"type":"number"},
     "e2_beschaeftigung_prozent":{"type":"number"},
     "e3_kapital":{"type":"number"},"e3_kunden":{"type":"number"},
     "e3_beschaeftigte":{"type":"number"},"e3_staat":{"type":"number"},
     "mechanismus":{"type":"string"},
     "hemmnis":{"type":"string"},
     "jahr_2030_auf_2031":{"type":"string"},
     "uebergabe_wert":{"type":"string"},
     "uebergabe_begruendung":{"type":"string"},
     "eingang_akzeptiert":{"type":"boolean"},
     "eingang_einwand":{"type":"string"},
     "s1_faellt_weg":{"type":"string"},
     "s2_neu":{"type":"string"},
     "s3_entscheidung":{"type":"string"},
     "s3_frist":{"type":"string"},
     "s3_groessenordnung":{"type":"string"},
     "feldfremde_behauptung":{"type":"string"},
     "quellen":{"type":"array","items":{"type":"string"}},
    }
    req = ["id","szenario","k1","k1_u","k1_o","k2","k2_u","k2_o","k3","k3_u","k3_o",
           "k4_automatisiert","k5_neue_aufgaben","d1_physisch","d2_preisdurchgriff",
           "d3_wechselabschlag","d4_verzoegerung_jahre","d4_institution",
           "e1_lohnquote_pp","e2_beschaeftigung_prozent","e3_kapital","e3_kunden",
           "e3_beschaeftigte","e3_staat","mechanismus","hemmnis","jahr_2030_auf_2031",
           "uebergabe_wert","uebergabe_begruendung","eingang_akzeptiert","eingang_einwand",
           "s1_faellt_weg","s2_neu","s3_entscheidung","s3_frist","s3_groessenordnung",
           "feldfremde_behauptung","quellen"]
    if mit_us:
        p["us_effekt_isoliert"] = {"type":"string"}
        p["us_mechanismus"] = {"type":"string"}
        p["uebergabe_wert_ohne_us"] = {"type":"string"}
        req += ["us_effekt_isoliert","us_mechanismus","uebergabe_wert_ohne_us"]
    return {"type":"object","properties":p,"required":req}

S_UEBERGABE = {
 "type":"object",
 "properties":{
  "station":{"type":"string"},
  "wert_zentral":{"type":"string"},"wert_unten":{"type":"string"},"wert_oben":{"type":"string"},
  "einheit":{"type":"string"},
  "herleitung":{"type":"string"},
  "gestuetzt_auf":{"type":"array","items":{"type":"string"}},
  "ausreisser":{"type":"array","items":{"type":"object","properties":{
     "id":{"type":"string"},"wert":{"type":"string"},"warum":{"type":"string"}},
     "required":["id","wert","warum"]}},
  "dissens":{"type":"array","items":{"type":"string"}},
  "eingang_bestritten_von":{"type":"array","items":{"type":"string"}},
  "weitergabe":{"type":"string"},
  "vorbehalte":{"type":"array","items":{"type":"string"}}},
 "required":["station","wert_zentral","wert_unten","wert_oben","einheit","herleitung",
             "gestuetzt_auf","ausreisser","dissens","eingang_bestritten_von","weitergabe","vorbehalte"]}

S_ANGRIFF = {
 "type":"object",
 "properties":{"n":{"type":"number"},"titel":{"type":"string"},
  "befunde":{"type":"array","items":{"type":"object","properties":{
     "schwere":{"type":"string","enum":["hart","mittel","weich"]},
     "stelle":{"type":"string"},"befund":{"type":"string"},"beleg":{"type":"string"},
     "folge":{"type":"string"}},"required":["schwere","stelle","befund","beleg","folge"]}},
  "haelt_stand":{"type":"boolean"},"begruendung":{"type":"string"}},
 "required":["n","titel","befunde","haelt_stand","begruendung"]}

S_KETTE = {
 "type":"object",
 "properties":{
  "bruchstellen":{"type":"array","items":{"type":"object","properties":{
    "zwischen":{"type":"string"},"groesse":{"type":"string"},"abgegeben":{"type":"string"},
    "angenommen":{"type":"string"},"differenz":{"type":"string"},"mechanismus_genannt":{"type":"boolean"}},
    "required":["zwischen","groesse","abgegeben","angenommen","differenz","mechanismus_genannt"]}},
  "kette_traegt":{"type":"boolean"},
  "schwaechstes_glied":{"type":"string"},
  "begruendung":{"type":"string"}},
 "required":["bruchstellen","kette_traegt","schwaechstes_glied","begruendung"]}

S_KAPITEL = {"type":"object","properties":{
  "id":{"type":"string"},"titel":{"type":"string"},"markdown":{"type":"string"},
  "kernsaetze":{"type":"array","items":{"type":"string"}},
  "offen":{"type":"array","items":{"type":"string"}}},
  "required":["id","titel","markdown","kernsaetze","offen"]}

S_TEXT = {"type":"object","properties":{
  "markdown":{"type":"string"},"anmerkungen":{"type":"array","items":{"type":"string"}}},
  "required":["markdown","anmerkungen"]}

S_VERIF = {"type":"object","properties":{
  "befunde":{"type":"array","items":{"type":"object","properties":{
    "schwere":{"type":"string","enum":["hart","mittel","weich"]},
    "stelle":{"type":"string"},"behauptung":{"type":"string"},
    "pruefung":{"type":"string"},"urteil":{"type":"string"}},
    "required":["schwere","stelle","behauptung","pruefung","urteil"]}},
  "freigabe":{"type":"boolean"},"begruendung":{"type":"string"}},
  "required":["befunde","freigabe","begruendung"]}

# ---------------------------------------------------------------- Regeln
REGELN = """
# REGELN (gelten fuer jede Antwort)

1. Konjunktiv bei allem, was Modellergebnis, Gesetzentwurf oder Politikvorschlag ist.
2. Modellprognose, Schaetzung und empirische Messung in jeder Aussage kenntlich trennen.
3. Zu jeder Zahl ein 80-Prozent-Intervall. Ein enges Intervall ohne Begruendung gilt als ueberkonfident.
4. Jede Zahl braucht einen benannten Mechanismus — einen Satz, der sagt, WODURCH sie zustande kommt.
   Eine Zahl ohne Mechanismus ist in der Auswertung wertlos.
5. Keine Uebertragung von US-Werten auf Deutschland ohne ausgewiesene Begruendung, welcher
   Strukturunterschied wie wirkt.
6. Keine unbelegten Allaussagen. Saetze der Form "alle", "kein", "immer", "nie" nur mit Beleg.
7. Keine Imitation realer benannter Personen. Du sprichst als Rolle, nicht als Person.
8. Rollentreue vor Konsens. Deine Interessenlage darf und soll dein Urteil faerben; deine Blindstelle
   wird dir genannt, damit die Auswertung sie pruefen kann, nicht damit du sie ausgleichst.
9. Du antwortest in deinem Feld. Zusaetzlich nennst du GENAU EINE feldfremde Behauptung, von der du
   annimmst, dass sie falsch sein koennte — das ersetzt die frueher verbotene Sicht ueber den Tellerrand.
"""

FRAGEBOGEN = """
# DER FRAGEBOGEN

## Teil A — Die fuenf Steuerparameter des Anthropic-Modells, auf DEIN Feld kalibriert

K1  Anteil der Aufgaben in deinem Feld, die KI bis 2031 beruehrt, in Prozent der Arbeitszeit.
    US-Referenz im Szenario substantial: 12 Prozent gesamtwirtschaftlich, rund 20 Prozent der
    kognitiven Aufgaben. Mit Unter- und Obergrenze des 80-Prozent-Intervalls (k1_u, k1_o).
K2  Verbreitung der TATSAECHLICHEN Nutzung bis 2031, in Prozent der Betriebe oder Beschaeftigten
    deines Feldes. Nicht die Zahl derer, die es einmal ausprobiert haben. Mit Intervall.
K3  Produktivitaetsgewinn je beruehrter Aufgabe, in Prozent. US-Referenz: plus 57 Prozent. Mit Intervall.
K4  Von dem, was KI beruehrt: welcher Anteil wird AUTOMATISIERT statt augmentiert, in Prozent.
    US-Referenz: drei Viertel automatisiert.
K5  Neuentstehung von Aufgaben: wie viel Prozent der wegfallenden Arbeitszeit wird bis 2031 durch
    neue Aufgaben in deinem Feld ersetzt.

Dazu: ordne dein Feld einem der drei Szenarien zu — modest, substantial oder extreme.

## Teil B — Die vier Uebertragungsbrueche, die das Papier selbst offenlaesst

D1  Welcher Anteil der Arbeit in deinem Feld ist koerperlich, in Prozent? Das Modell bildet
    ausschliesslich kognitive Aufgaben ab; das ist der Grund, warum die Autoren nicht ueber 2030
    hinausrechnen.
D2  Preisdurchgriff: welcher Anteil des Produktivitaetsgewinns kommt im Preis deiner Leistung an,
    in Prozent? Das Modell kennt keine Preisrigiditaeten. Administrierte Preise, Honorarordnungen,
    Tarifvertraege und Festbetraege wirken hier.
D3  Wechselabschlag: um wie viel Prozent sinkt das Entgelt einer Person, die aus deinem Feld in ein
    anderes wechseln muss? Das Modell unterstellt sofortigen Wechsel ohne Abschlag.
D4  Politoekonomie: welche Institution in deinem Feld kann den Effekt verzoegern, und um wie viele
    Jahre? Das Modell hat keine Politoekonomie. Institution benennen.

## Teil C — Die Ergebnisgroessen, vergleichbar mit der Tabelle des Papiers

E1  Lohnquote in deinem Feld 2031, in Prozentpunkten gegenueber 2025. Leitgroesse des Papiers:
    minus 4 Punkte im Szenario substantial, minus 15 im Szenario extreme.
E2  Beschaeftigung in deinem Feld 2031, in Prozent gegenueber 2025.
E3  Wer bekommt den Effizienzgewinn: Kapitaleigner, Kunden, Beschaeftigte, Staat und
    Sozialversicherung. Vier Zahlen, Summe genau 100. Das Papier laesst diese Frage ausdruecklich
    offen — der aggregierte Zugewinn sei fast das Dreifache dessen, was kognitiv Beschaeftigte an
    Lohn und Beschaeftigung verlieren, ob die Mittel ankommen, liefere Wachstum aber nicht von selbst.

## Teil D — Das Jahr, an dem das Papier endet

jahr_2030_auf_2031: Was geschieht in deinem Feld zwischen 2030 und 2031? Die Autoren rechnen
ausdruecklich nicht weiter, weil Robotik nicht abgebildet ist. Antworte gesondert fuer dieses Jahr.

## Teil E — Die Uebergabe an die naechste Station

Das ist der Kern dieser Sitzung. Du bekommst eine Zahl von der vorherigen Station und gibst eine
weiter. Wenn du den Eingangswert nicht akzeptierst, sage das (eingang_akzeptiert = false) und
begruende es (eingang_einwand) — die Kette darf brechen, aber nicht stillschweigend.

## Teil F — Strategie (beantworten ALLE Rollen, nicht nur die HIGL-Rollen)

S1  Welche heute bezahlte Leistung des HIGL-Verbunds wuerdest du 2031 nicht mehr kaufen, und warum
    nicht? Wenn du kein Kunde bist: welche Leistung dieser Art wird in deinem Feld nicht mehr gekauft?
S2  Welche Leistung wuerdest du 2031 kaufen, die es heute nicht gibt, und was waerest du bereit,
    dafuer zu zahlen?
S3  Was muss bis wann entschieden sein, damit S2 traegt? Eine Entscheidung, eine Frist, eine
    Groessenordnung der Kosten.
"""

HIGL_LAGE = """
# HIGL — die Ist-Lage 2025 aus den Buchungsdaten (DATEV-Kontenblaetter, Export 29.03.2026)

Diese Zahlen sind erhoben, nicht geschaetzt. Debitorensicht, brutto fakturiert.

| Gesellschaft | Debitoren | fakturiert | Netto-Erloese 8xxx | konzernintern |
|---|---|---|---|---|
| 4K ANALYTICS | 83 | 8.110.435 EUR | 6.502.941 EUR | 4 % |
| WIG2 | 123 | 7.028.857 EUR | 6.823.084 EUR | 4 % |
| GREENBAY Software | 15 | 2.263.029 EUR | 1.952.412 EUR | 52 % |
| iLoc | 12 | 1.291.198 EUR | 1.058.861 EUR | 100 % |
| Inno3 | 88 | 567.085 EUR | 744.334 EUR | 23 % |
| GREENBAY research | 3 | 380.263 EUR | 404.164 EUR | 67 % |
| CLINIBOTS | 4 | 96.335 EUR | 80.954 EUR | 48 % |

Kundenkonzentration und Abhaengigkeiten:
- 4K: IKK classic 2.115.310 und IQVIA 1.906.422 sind zusammen 52 Prozent des Aussenumsatzes,
  die drei groessten 61 Prozent. Dahinter Universitaetsklinikum Leipzig 725.332, Medizinische
  Universitaet Lausitz-Carl Thiem 697.036, DAVASO 449.775, rund 50 Krankenkassen und ein langer
  Schwanz von Pflegediensten mit 200 bis 900 EUR.
- WIG2: ZEG Berlin 1.654.228 ist 25 Prozent des Aussenumsatzes. Dahinter Bayerisches Landesamt
  529.984, Lilly 438.575, Temedica 348.670, vdek 188.900, DRV Bund 170.384 sowie internationale
  Auftraggeber (Cytel, OXON, ZS Associates, Adelphi, Evidera, P95) und die Hersteller Pfizer,
  Novartis, Sanofi, Bristol Myers Squibb, AbbVie, Gilead, Novo Nordisk, Daiichi Sankyo, Takeda,
  Boehringer, Bayer, MSD, AstraZeneca, Chiesi, Ipsen, Alfasigma. Die Brutto-Netto-Spreizung
  betraegt nur 3 Prozent — ein grosser Teil des Geschaefts ist umsatzsteuerfrei oder Reverse Charge
  ins Ausland.
- GREENBAY Software: 4K allein 1.186.712, also 52 Prozent. Extern Helmholtz-Zentrum fuer
  Umweltforschung 319.916, IQVIA 143.270, SUEDVERS 140.468, InfAI 125.339, GEOMAGIC 120.104.
- GREENBAY research: WIG2 252.998 (67 Prozent), mementor DE 67.692, Rocketlane Medical Ventures 59.573.
- CLINIBOTS: Vicondo Healthcare 45.294, 4K 46.654, Medtronic 4.165, iVascular 222. Das Produkt
  (Qlinik Suite, Paragraf-21-Leistungsmonitor, Qualitaetsberichte) richtet sich laut eigener
  Darstellung an Krankenhaeuser; die zahlenden Kunden sind Industrie.
- Inno3: 88 Debitoren, groesster BITMARCK Holding 35.818, dann AOK Plus, IKK classic, STACKIT, SBK —
  ein Netzwerk- und Veranstaltungsgeschaeft mit vielen Kleinbetraegen.
- iLoc: kein nennenswertes Aussengeschaeft (5.223 EUR), 1,29 Mio. EUR reine Innenverrechnung.
"""

# ---------------------------------------------------------------- JS-Vorlage
VORLAGE = r'''export const meta = {
  name: 'sitzung-d-uebertragungskette',
  description: 'Uebertragungskette Makro zu GKV/PKV zu Leistungserbringern zu Pharma zu HIGL, 100 Rollen auf Basis des Anthropic-Papiers',
  phases: [
    { title: 'Recherche',      detail: 'sechs Bloecke, nur die Luecken des Bestands' },
    { title: 'Querschnitt',    detail: 'Europa und KI-Technik, vierzehn Rollen' },
    { title: 'Station 0',      detail: 'Makro — Kalibrierung der fuenf Steuerparameter' },
    { title: 'Station 1',      detail: 'GKV und PKV — Finanzierungsstruktur' },
    { title: 'Station 2',      detail: 'Krankenhaeuser, ambulante Versorgung, Pflege' },
    { title: 'Station 3',      detail: 'Pharma und MedTech, mit und ohne US-Schock' },
    { title: 'Station 4',      detail: 'HIGL-Verbund, zwoelf Rollen' },
    { title: 'Kettenpruefung', detail: 'Uebergabegroessen gegeneinander' },
    { title: 'Angriff',        detail: 'Gegenposition und fuenf gezielte Angriffe' },
    { title: 'Papier',         detail: 'fuenf Kapitel, Zusammenzug, Verifikation, Schlussfassung' },
  ],
}

const REGELN = __REGELN__
const FRAGEBOGEN = __FRAGEBOGEN__
const BESTAND = __BESTAND__
const KEINE_DOPPELUNG = __KEINE_DOPPELUNG__
const HIGL_LAGE = __HIGL_LAGE__
const RECHERCHE = __RECHERCHE__
const ROLLEN = __ROLLEN__
const STATIONEN = __STATIONEN__
const ANGRIFFE = __ANGRIFFE__
const KAPITEL = __KAPITEL__
const S_FAKTEN = __S_FAKTEN__
const S_ROLLE = __S_ROLLE__
const S_ROLLE_US = __S_ROLLE_US__
const S_UEBERGABE = __S_UEBERGABE__
const S_ANGRIFF = __S_ANGRIFF__
const S_KETTE = __S_KETTE__
const S_KAPITEL = __S_KAPITEL__
const S_TEXT = __S_TEXT__
const S_VERIF = __S_VERIF__

const RAHMEN = REGELN + '\n' + KEINE_DOPPELUNG + '\n' + BESTAND

function karte(r) {
  return 'DEINE ROLLE\n' +
    '  Kennung:      ' + r.id + '\n' +
    '  Gruppe:       ' + r.gruppe + '\n' +
    '  Rolle:        ' + r.rolle + '\n' +
    '  Mandat:       ' + r.mandat + '\n' +
    '  Wissensanker: ' + r.anker + '\n' +
    '  Blindstelle:  ' + r.blindstelle + '\n'
}

function eingangsblock(e) {
  if (!e) {
    return 'EINGANG: keiner. Du stehst am Anfang der Kette. Setze eingang_akzeptiert auf true und\n' +
           'eingang_einwand auf "entfaellt, Kettenanfang".\n'
  }
  return 'EINGANG VON ' + e.station + ' — dieser Wert ist fuer dich verbindlich, solange du ihn nicht\n' +
    'ausdruecklich bestreitest:\n' +
    '  Groesse:    ' + e.einheit + '\n' +
    '  Wert:       ' + e.wert_zentral + '   (80 % von ' + e.wert_unten + ' bis ' + e.wert_oben + ')\n' +
    '  Herleitung: ' + e.herleitung + '\n' +
    '  Vorbehalte: ' + (e.vorbehalte || []).join(' | ') + '\n' +
    '  Dissens in der abgebenden Station: ' + (e.dissens || []).join(' | ') + '\n'
}

function promptRecherche(n, i) {
  return 'Du bist Rechercheur ' + n.id + ' der Szenariokonferenz. Du hast KEINE Rolle, kein Mandat und\n' +
    'keine Stimme. Du lieferst ein Faktenblatt: gepruefte Gegenwartswerte mit Fundstelle, Erhebungsdatum\n' +
    'und ausdruecklich benannten Luecken.\n\n' +
    'DOMAENE: ' + n.domaene + '\n\n' +
    'LIEFERGEGENSTAND\n' + n.auftrag + '\n\n' +
    'AUSDRUECKLICHE GRENZE\n' + n.grenze + '\n\n' +
    KEINE_DOPPELUNG + '\n' +
    'Recherchiere aktiv im Netz. Jede Zahl braucht eine abgerufene Quelle mit Datum. Wo du nichts\n' +
    'findest, sagst du das unter luecken — eine Luecke ist ein Befund, keine Schwaeche.\n\n' +
    'Gib das Faktenblatt strukturiert zurueck. id ist ' + n.id + '.'
}

function promptQuer(r) {
  return 'Du bist eine Stimme der Querbank in der Szenariokonferenz zur Frage, was Kuenstliche\n' +
    'Intelligenz fuer Europa, Deutschland, das Gesundheitswesen und den HIGL-Verbund im Jahr 2031\n' +
    'bedeutet. Die Querbank urteilt vor der Kette und liefert den Stationen den Rahmen.\n\n' +
    karte(r) + '\n' + FRAGEBOGEN + '\n' +
    'Fuer dich gilt: Du stehst nicht in der Uebergabekette. Setze eingang_akzeptiert auf true,\n' +
    'eingang_einwand auf "entfaellt, Querbank", und schreibe unter uebergabe_wert die eine Groesse,\n' +
    'die die Stationen von dir kennen muessen, mit Einheit.\n\n' + HIGL_LAGE + '\n' + RAHMEN
}

function promptRolle(r, eingang, fakten, quer) {
  const ist_us = r.station === 'S3'
  const st = STATIONEN[r.station]
  let t = 'Du bist eine Stimme in ' + st.kurz + ' der Szenariokonferenz zur Frage, was Kuenstliche\n' +
    'Intelligenz fuer Europa, Deutschland, das Gesundheitswesen und den HIGL-Verbund im Jahr 2031\n' +
    'bedeutet.\n\n' +
    'DIESE STATION: ' + st.titel + '\n' +
    'SIE EMPFAENGT:  ' + (st.empfaengt || 'nichts, Kettenanfang') + '\n' +
    'SIE GIBT WEITER: ' + st.gibt + '\n\n' +
    karte(r) + '\n' + eingangsblock(eingang) + '\n' + FRAGEBOGEN + '\n'
  if (ist_us) {
    t += '\n# ZUSAETZLICH FUER DIESE STATION — der amerikanische Schock\n\n' +
      'Auf dein Feld wirken zwei Dinge gleichzeitig: die KI-Entwicklung und die amerikanische\n' +
      'Arzneimittelpreispolitik (Section-232-Zoelle, Meistbeguenstigung, CMMI-Modelle, und der\n' +
      'Umstand, dass der deutsche AMNOG-Erstattungsbetrag die einzige oeffentlich zugaengliche\n' +
      'Nettopreisreferenz Europas ist). Du musst beides TRENNEN:\n' +
      '  uebergabe_wert          = dein Wert MIT dem US-Schock\n' +
      '  uebergabe_wert_ohne_us  = derselbe Wert OHNE den US-Schock, nur mit KI\n' +
      '  us_effekt_isoliert      = die Differenz, mit Vorzeichen und Einheit\n' +
      '  us_mechanismus          = wodurch genau die Differenz zustande kommt\n' +
      'Wenn du keinen Effekt siehst, schreibe das hin und begruende es. Ein Nulleffekt ist ein\n' +
      'Befund, kein Ausweichen.\n'
  }
  t += '\n# NEUE FAKTENBLAETTER DIESER SITZUNG\n\n' + fakten + '\n' +
       '\n# WAS DIE QUERBANK VORGELEGT HAT\n\n' + quer + '\n' +
       '\n' + HIGL_LAGE + '\n' + RAHMEN
  return t
}

function kurzkarte(x) {
  return x.id + ' | Szenario ' + x.szenario +
    ' | K1 ' + x.k1 + ' (' + x.k1_u + '-' + x.k1_o + ')' +
    ' | K2 ' + x.k2 + ' | K3 ' + x.k3 + ' | K4 ' + x.k4_automatisiert + ' | K5 ' + x.k5_neue_aufgaben +
    ' | D1 ' + x.d1_physisch + ' | D2 ' + x.d2_preisdurchgriff + ' | D3 ' + x.d3_wechselabschlag +
    ' | D4 ' + x.d4_verzoegerung_jahre + 'J (' + x.d4_institution + ')' +
    ' | E1 ' + x.e1_lohnquote_pp + 'Pp | E2 ' + x.e2_beschaeftigung_prozent + '%' +
    ' | E3 K' + x.e3_kapital + '/Ku' + x.e3_kunden + '/B' + x.e3_beschaeftigte + '/S' + x.e3_staat + '\n' +
    '   UEBERGABE: ' + x.uebergabe_wert +
    (x.uebergabe_wert_ohne_us ? '   OHNE US: ' + x.uebergabe_wert_ohne_us : '') + '\n' +
    '   BEGRUENDUNG: ' + x.uebergabe_begruendung + '\n' +
    '   MECHANISMUS: ' + x.mechanismus + '\n' +
    '   HEMMNIS: ' + x.hemmnis + '\n' +
    '   EINGANG: ' + (x.eingang_akzeptiert ? 'angenommen' : 'BESTRITTEN — ' + x.eingang_einwand) + '\n' +
    '   2030 AUF 2031: ' + x.jahr_2030_auf_2031 + '\n' +
    '   S1 faellt weg: ' + x.s1_faellt_weg + '\n' +
    '   S2 neu: ' + x.s2_neu + '\n' +
    '   S3: ' + x.s3_entscheidung + ' bis ' + x.s3_frist + ', ' + x.s3_groessenordnung + '\n'
}

function promptVerdichtung(s, karten, eingang) {
  const st = STATIONEN[s]
  return 'Du verdichtest ' + st.kurz + ' der Szenariokonferenz zu EINER Uebergabegroesse fuer die\n' +
    'naechste Station. Du bist keine Rolle und hast kein Mandat.\n\n' +
    'STATION: ' + st.titel + '\n' +
    'WEITERZUGEBENDE GROESSE: ' + st.gibt + '\n\n' +
    eingangsblock(eingang) + '\n' +
    'DIE KARTEN DIESER STATION (' + karten.length + '):\n\n' + karten.map(kurzkarte).join('\n') + '\n\n' +
    'AUFTRAG\n' +
    '1. Bilde den zentralen Wert und das 80-Prozent-Intervall. Nicht der Mittelwert um jeden Preis:\n' +
    '   wenn die Karten zwei Lager bilden, ist das ein Ergebnis und gehoert unter dissens.\n' +
    '2. Schreibe die Herleitung so, dass sie nachgerechnet werden kann — welche Karten tragen den\n' +
    '   Wert (gestuetzt_auf), welche Karten liegen ausserhalb und warum (ausreisser).\n' +
    '3. Wer den Eingangswert bestritten hat, kommt namentlich unter eingang_bestritten_von. Wenn die\n' +
    '   Mehrheit ihn bestreitet, musst du das in der Weitergabe beruecksichtigen, nicht glaetten.\n' +
    '4. Unter vorbehalte steht, was die naechste Station wissen muss, bevor sie mit dem Wert rechnet.\n' +
    '5. Keine Zahl ohne Mechanismus. Eine geglaettete Zahl, die keine Karte stuetzt, ist ein Fehler.\n\n' +
    RAHMEN
}

// ------------------------------------------------------------------ Lauf
phase('Recherche')
log('Runde 0: sechs Faktenblaetter — nur die Luecken des Bestands, keine Quelle zweimal.')
const fakten = (await parallel(RECHERCHE.map((n, i) => () =>
  agent(promptRecherche(n, i), { label: 'Recherche ' + n.id + ': ' + n.domaene,
    phase: 'Recherche', schema: S_FAKTEN })))).filter(Boolean)

const FAKTENBLOCK = fakten.map(f =>
  '## Faktenblatt ' + f.id + '\n' +
  f.befunde.map(b => '- ' + b.groesse + ': ' + b.wert + ' (Stand ' + b.stand + ', ' + b.art + ') — ' + b.quelle).join('\n') +
  '\nLUECKEN: ' + f.luecken.join(' | ') +
  '\nWARNUNGEN: ' + f.warnungen.join(' | ')).join('\n\n')
log('Faktenblaetter: ' + fakten.length + ' von ' + RECHERCHE.length + '.')

phase('Querschnitt')
const querrollen = ROLLEN.filter(r => r.station === 'EU' || r.station === 'KI')
log('Querbank: ' + querrollen.length + ' Rollen (Europa und KI-Technik) urteilen vor der Kette.')
const quer = (await parallel(querrollen.map(r => () =>
  agent(promptQuer(r), { label: r.id + ' ' + r.rolle, phase: 'Querschnitt', schema: S_ROLLE })))).filter(Boolean)
const QUERBLOCK = quer.map(kurzkarte).join('\n')

const KETTE = ['S0', 'S1', 'S2', 'S3', 'S4']
const ergebnisse = {}
const uebergaben = []
let eingang = null

for (const s of KETTE) {
  const st = STATIONEN[s]
  const rollen = ROLLEN.filter(r => r.station === s)
  log(st.kurz + ' — ' + st.titel + ' (' + rollen.length + ' Rollen).')
  const res = (await parallel(rollen.map(r => () =>
    agent(promptRolle(r, eingang, FAKTENBLOCK, QUERBLOCK), {
      label: r.id + ' ' + r.rolle, phase: st.kurz,
      schema: s === 'S3' ? S_ROLLE_US : S_ROLLE })))).filter(Boolean)
  ergebnisse[s] = res
  if (res.length < rollen.length) log('ACHTUNG ' + st.kurz + ': nur ' + res.length + ' von ' + rollen.length + ' Karten.')
  const u = await agent(promptVerdichtung(s, res, eingang), {
    label: 'Uebergabe ' + s, phase: st.kurz, schema: S_UEBERGABE })
  uebergaben.push(u)
  eingang = u ? Object.assign({ station: s }, u) : null
  if (u) log('Uebergabe ' + s + ': ' + u.wert_zentral + ' ' + u.einheit)
}

phase('Kettenpruefung')
const kettenbild = uebergaben.filter(Boolean).map(u =>
  u.station + ' gibt weiter: ' + u.wert_zentral + ' ' + u.einheit +
  ' (' + u.wert_unten + ' bis ' + u.wert_oben + ')\n' +
  '   Herleitung: ' + u.herleitung + '\n' +
  '   Eingang bestritten von: ' + (u.eingang_bestritten_von || []).join(', ') + '\n' +
  '   Dissens: ' + (u.dissens || []).join(' | ') + '\n' +
  '   Vorbehalte: ' + (u.vorbehalte || []).join(' | ')).join('\n\n')

const kettenpruefung = await agent(
  'Du pruefst die Uebertragungskette der Szenariokonferenz. Du bist keine Rolle.\n\n' +
  'Die Kette laeuft: Station 0 Makro, Station 1 GKV und PKV, Station 2 Leistungserbringer,\n' +
  'Station 3 Pharma und US-Schock, Station 4 HIGL. Jede Station bekommt eine Zahl und gibt eine weiter.\n\n' +
  'DIE UEBERGABEN\n\n' + kettenbild + '\n\n' +
  'AUFTRAG\n' +
  'Pruefe Uebergabe fuer Uebergabe, ob der abgegebene Wert und der angenommene Wert derselbe sind.\n' +
  'Suche nach stillschweigenden Umdefinitionen: eine Groesse, die als Prozentwert abgegeben und als\n' +
  'Absolutbetrag angenommen wird; ein Bezugsjahr, das sich verschiebt; eine Abgrenzung, die sich\n' +
  'weitet. Fuer jede Bruchstelle: zwischen welchen Stationen, welche Groesse, welcher Betrag, und ob\n' +
  'ein Mechanismus fuer den Sprung genannt wurde.\n' +
  'Sage am Ende, ob die Kette traegt, und benenne das schwaechste Glied.\n\n' + RAHMEN,
  { label: 'Kettenpruefung', phase: 'Kettenpruefung', schema: S_KETTE })

const revisionen = (await parallel(uebergaben.filter(Boolean).map(u => () =>
  agent('Du ueberarbeitest die Uebergabegroesse der Station ' + u.station + ' nach der Kettenpruefung.\n\n' +
    'DEINE BISHERIGE UEBERGABE\n' +
    '  Wert: ' + u.wert_zentral + ' ' + u.einheit + ' (' + u.wert_unten + ' bis ' + u.wert_oben + ')\n' +
    '  Herleitung: ' + u.herleitung + '\n' +
    '  Vorbehalte: ' + (u.vorbehalte || []).join(' | ') + '\n\n' +
    'DIE KETTENPRUEFUNG HAT ERGEBEN\n' +
    '  Kette traegt: ' + (kettenpruefung ? kettenpruefung.kette_traegt : 'unbekannt') + '\n' +
    '  Schwaechstes Glied: ' + (kettenpruefung ? kettenpruefung.schwaechstes_glied : '') + '\n' +
    '  Begruendung: ' + (kettenpruefung ? kettenpruefung.begruendung : '') + '\n' +
    '  Bruchstellen:\n' + (kettenpruefung ? kettenpruefung.bruchstellen.map(b =>
      '   - zwischen ' + b.zwischen + ', Groesse ' + b.groesse + ': abgegeben ' + b.abgegeben +
      ', angenommen ' + b.angenommen + ', Differenz ' + b.differenz +
      (b.mechanismus_genannt ? ' (Mechanismus genannt)' : ' (KEIN Mechanismus genannt)')).join('\n') : '') + '\n\n' +
    'AUFTRAG\n' +
    'Aendere deinen Wert NUR, wenn die Pruefung einen Fehler in deiner Herleitung zeigt. Wenn der\n' +
    'Einwand die Nachbarstation betrifft und nicht dich, lass den Wert stehen und sage das unter\n' +
    'vorbehalte. Eine Angleichung um der Glaettung willen ist ein Fehler. Gib die vollstaendige\n' +
    'Uebergabe erneut zurueck, auch wenn nichts sich aendert.\n\n' + RAHMEN,
    { label: 'Revision ' + u.station, phase: 'Kettenpruefung', schema: S_UEBERGABE })))).filter(Boolean)

phase('Angriff')
const gegenrollen = ROLLEN.filter(r => r.station === 'GP')
const stand = revisionen.map(u => u.station + ': ' + u.wert_zentral + ' ' + u.einheit +
  ' — ' + u.herleitung).join('\n')

const [gegen, redteam] = await parallel([
  () => parallel(gegenrollen.map(r => () =>
    agent(promptQuer(r) + '\n\n# DER STAND DER KETTE, DEN DU ANGREIFST\n\n' + stand,
      { label: r.id + ' ' + r.rolle, phase: 'Angriff', schema: S_ROLLE }))),
  () => parallel(ANGRIFFE.map(a => () =>
    agent('Du bist Red Team der Szenariokonferenz. Dein Auftrag ist ausschliesslich, die folgende\n' +
      'Position zu widerlegen. Du bist keine Rolle und schuldest niemandem Ausgewogenheit.\n\n' +
      'ANGRIFF ' + a[0] + ': ' + a[1] + '\n\n' + a[2] + '\n\n' +
      '# DER STAND DER KETTE\n\n' + stand + '\n\n' +
      '# DIE UEBERGABEN IM EINZELNEN\n\n' + kettenbild + '\n\n' +
      '# WAS DIE STATIONEN GESAGT HABEN (Auszug)\n\n' +
      KETTE.map(s => '## ' + s + '\n' + (ergebnisse[s] || []).map(kurzkarte).join('\n')).join('\n\n') + '\n\n' +
      'Ein Befund ist hart, wenn er die Kette ungueltig macht; mittel, wenn er eine Zahl verschiebt;\n' +
      'weich, wenn er nur eine Formulierung trifft. Nenne zu jedem Befund den Beleg. Sage am Ende,\n' +
      'ob die angegriffene Position standhaelt — auch wenn dein Auftrag war, sie zu widerlegen.\n\n' + RAHMEN,
      { label: 'Red Team ' + a[0] + ': ' + a[1], phase: 'Angriff', schema: S_ANGRIFF })))
])
const gegenK = (gegen || []).filter(Boolean)
const redteamK = (redteam || []).filter(Boolean)

phase('Papier')
const BEFUNDE = redteamK.map(a => '## Angriff ' + a.n + ': ' + a.titel +
  ' — haelt stand: ' + a.haelt_stand + '\n' +
  a.befunde.map(b => '- [' + b.schwere + '] ' + b.stelle + ': ' + b.befund + ' (Beleg: ' + b.beleg + ') Folge: ' + b.folge).join('\n')).join('\n\n')
const GEGENBLOCK = gegenK.map(kurzkarte).join('\n')

const kapitel = (await parallel(KAPITEL.map((k, i) => () =>
  agent('Du schreibst Kapitel ' + k[0] + ' des Strategiepapiers 2031 der Szenariokonferenz.\n\n' +
    'KAPITEL: ' + k[1] + '\n\n' +
    'Grundlage ist das Arbeitspapier von Korinek, Jones, Sacher, Cotter und McCrory,\n' +
    'Economic Scenarios for Transformative AI, The Anthropic Institute WP 2026-02, September 2026.\n' +
    'Das Modell rechnet bis 2030 und bildet ausschliesslich kognitive Aufgaben ab; die Autoren nennen\n' +
    'die Szenarien ausdruecklich keine Prognosen und ordnen ihnen keine Wahrscheinlichkeiten zu.\n' +
    'Beides gehoert in den Text, nicht in eine Fussnote.\n\n' +
    '# DIE KARTEN DEINER STATION\n\n' +
    (ergebnisse[KETTE[i]] || []).map(kurzkarte).join('\n') + '\n\n' +
    '# DIE UEBERGABEN DER GANZEN KETTE\n\n' + revisionen.map(u =>
      u.station + ': ' + u.wert_zentral + ' ' + u.einheit + ' (' + u.wert_unten + ' bis ' + u.wert_oben + ')\n' +
      '   ' + u.herleitung + '\n   Dissens: ' + (u.dissens || []).join(' | ')).join('\n\n') + '\n\n' +
    '# WAS DAS RED TEAM GEFUNDEN HAT\n\n' + BEFUNDE + '\n\n' +
    '# DIE GEGENPOSITION\n\n' + GEGENBLOCK + '\n\n' +
    'AUFTRAG\n' +
    'Schreibe deutschen Fliesstext mit Zwischenueberschriften und Tabellen, wo Zahlen zu vergleichen\n' +
    'sind. Keine Aufzaehlung als Ersatz fuer ein Argument. Jede Zahl, die du nennst, kommt aus den\n' +
    'Karten oder den Uebergaben — du erfindest keine. Wo die Karten auseinandergehen, schreibst du\n' +
    'den Dissens hin und nicht den Mittelwert. Wo das Red Team einen harten Befund hat, nimmst du ihn\n' +
    'auf; du verteidigst nichts. Unter offen stehen die Fragen, die dein Kapitel nicht beantwortet.\n\n' + RAHMEN,
    { label: 'Kapitel ' + k[0] + ': ' + k[1], phase: 'Papier', schema: S_KAPITEL })))).filter(Boolean)

const zusammenzug = await agent(
  'Du ziehst die fuenf Kapitel des Strategiepapiers 2031 zusammen.\n\n' +
  kapitel.map(k => '# ' + k.titel + '\n\n' + k.markdown).join('\n\n---\n\n') + '\n\n' +
  '# KERNSAETZE DER KAPITEL\n\n' +
  kapitel.map(k => k.id + ': ' + k.kernsaetze.join(' / ')).join('\n') + '\n\n' +
  '# WAS OFFEN BLEIBT\n\n' + kapitel.map(k => k.id + ': ' + k.offen.join(' | ')).join('\n') + '\n\n' +
  'AUFTRAG\n' +
  'Schreibe Rahmen und Lesehilfe voran: was die Konferenz war, worauf sie sich stuetzt, was das\n' +
  'Anthropic-Papier leistet und was es ausdruecklich nicht leistet, und wie die Uebertragungskette\n' +
  'zu lesen ist. Dann die fuenf Kapitel in einer Reihenfolge, die die Kette abbildet. Dann drei\n' +
  'Abschnitte: Widersprueche, die stehen bleiben; Was daraus folgt (hoechstens fuenf Saetze, jeder\n' +
  'eine Entscheidung mit Frist); Was dieses Papier nicht ist.\n' +
  'Streiche Doppelungen zwischen den Kapiteln, aber keine Widersprueche — die bleiben sichtbar.\n\n' + RAHMEN,
  { label: 'Zusammenzug', phase: 'Papier', schema: S_TEXT })

const verifikation = await agent(
  'Du pruefst den Entwurf des Strategiepapiers 2031 gegen die Rohdaten. Du bist keine Rolle und\n' +
  'schuldest dem Text nichts.\n\n' +
  '# DER ENTWURF\n\n' + (zusammenzug ? zusammenzug.markdown : '') + '\n\n' +
  '# DIE UEBERGABEN\n\n' + revisionen.map(u => u.station + ': ' + u.wert_zentral + ' ' + u.einheit +
    ' (' + u.wert_unten + ' bis ' + u.wert_oben + ') — ' + u.herleitung).join('\n') + '\n\n' +
  '# DIE KARTEN\n\n' + KETTE.map(s => '## ' + s + '\n' +
    (ergebnisse[s] || []).map(kurzkarte).join('\n')).join('\n\n') + '\n\n' +
  '# DIE QUERBANK UND DIE GEGENPOSITION\n\n' + QUERBLOCK + '\n' + GEGENBLOCK + '\n\n' +
  'AUFTRAG\n' +
  'Pruefe jede Zahl im Entwurf gegen die Karten und Uebergaben. Suche insbesondere:\n' +
  '  - Zahlen, die im Entwurf stehen und in keiner Karte,\n' +
  '  - Allaussagen ohne Beleg (alle, kein, immer, nie, saemtliche),\n' +
  '  - Indikativ, wo Konjunktiv noetig waere (Modellergebnis, Gesetzentwurf, Politikvorschlag),\n' +
  '  - geglaettete Mittelwerte, wo die Karten zwei Lager bilden,\n' +
  '  - US-Werte, die ohne Begruendung auf Deutschland uebertragen wurden,\n' +
  '  - Aussagen ueber den US-Schock, die den Schalter mit und ohne nicht trennen.\n' +
  'Ein Befund ist hart, wenn eine Aussage falsch ist; mittel, wenn sie ungedeckt ist; weich, wenn sie\n' +
  'nur unscharf formuliert ist. Gib die Freigabe nur, wenn kein harter Befund offen ist.\n\n' + RAHMEN,
  { label: 'Verifikation', phase: 'Papier', schema: S_VERIF })

const schluss = await agent(
  'Du erstellst die Schlussfassung des Strategiepapiers 2031.\n\n' +
  '# DER ENTWURF\n\n' + (zusammenzug ? zusammenzug.markdown : '') + '\n\n' +
  '# DIE VERIFIKATION\n\n' +
  'Freigabe: ' + (verifikation ? verifikation.freigabe : 'unbekannt') + '\n' +
  (verifikation ? verifikation.begruendung : '') + '\n\n' +
  (verifikation ? verifikation.befunde.map(b => '- [' + b.schwere + '] ' + b.stelle + ': ' +
    b.behauptung + '\n  Pruefung: ' + b.pruefung + '\n  Urteil: ' + b.urteil).join('\n') : '') + '\n\n' +
  'AUFTRAG\n' +
  'Arbeite JEDEN harten und jeden mittleren Befund ein. Eine Aussage, die die Pruefung nicht deckt,\n' +
  'wird gestrichen oder auf das zurueckgefuehrt, was die Karten hergeben — nicht abgeschwaecht und\n' +
  'stehen gelassen. Wo du streichst, schreibst du in einem Satz hin, was dort stand und warum es\n' +
  'nicht haltbar war; das Papier verschweigt seine eigenen Korrekturen nicht.\n' +
  'Unter anmerkungen listest du, was du geaendert hast, je Befund eine Zeile.\n\n' + RAHMEN,
  { label: 'Schlussfassung', phase: 'Papier', schema: S_TEXT })

log('Fertig. Karten: ' + KETTE.reduce((n, s) => n + (ergebnisse[s] || []).length, 0) +
    ' in der Kette, ' + quer.length + ' Querbank, ' + gegenK.length + ' Gegenposition.')

return {
  fakten, quer, ergebnisse, uebergaben, kettenpruefung, revisionen,
  gegen: gegenK, redteam: redteamK, kapitel, zusammenzug, verifikation, schluss,
}
'''

def baue():
    rollen = als_dicts()
    stationen = {k: {"kurz": v[0], "titel": v[1], "empfaengt": v[2], "gibt": v[3]}
                 for k, v in STATIONEN.items()}
    # Querbaenke bekommen sprechende Kurznamen
    stationen["EU"]["kurz"] = "Querschnitt"
    stationen["KI"]["kurz"] = "Querschnitt"
    stationen["GP"]["kurz"] = "Angriff"

    recherche = [{"id": i, "domaene": d, "auftrag": einzeilig(a), "grenze": einzeilig(g)}
                 for (i, d, a, g) in RECHERCHE]

    ersetzungen = {
        "__REGELN__": REGELN, "__FRAGEBOGEN__": FRAGEBOGEN, "__BESTAND__": BESTAND,
        "__KEINE_DOPPELUNG__": KEINE_DOPPELUNG, "__HIGL_LAGE__": HIGL_LAGE,
        "__RECHERCHE__": recherche, "__ROLLEN__": rollen, "__STATIONEN__": stationen,
        "__ANGRIFFE__": ANGRIFFE, "__KAPITEL__": KAPITEL,
        "__S_FAKTEN__": S_FAKTEN, "__S_ROLLE__": s_rolle(False), "__S_ROLLE_US__": s_rolle(True),
        "__S_UEBERGABE__": S_UEBERGABE, "__S_ANGRIFF__": S_ANGRIFF, "__S_KETTE__": S_KETTE,
        "__S_KAPITEL__": S_KAPITEL, "__S_TEXT__": S_TEXT, "__S_VERIF__": S_VERIF,
    }
    js = VORLAGE
    for marke, wert in ersetzungen.items():
        if marke not in js:
            sys.exit("Marke fehlt in der Vorlage: " + marke)
        js = js.replace(marke, json.dumps(wert, ensure_ascii=False))
    offen = [m for m in ersetzungen if m in js]
    if offen:
        sys.exit("Marken nicht ersetzt: " + ", ".join(offen))
    ziel = os.path.join(HIER, "workflow-sitzung-d.js")
    with open(ziel, "w", encoding="utf-8") as fh:
        fh.write(js)

    aufrufe = (len(recherche) + len([r for r in rollen if r["station"] in ("EU","KI")])
               + sum(1 for r in rollen if r["station"] in ("S0","S1","S2","S3","S4")) + 5
               + 1 + 5 + len([r for r in rollen if r["station"] == "GP"]) + len(ANGRIFFE)
               + len(KAPITEL) + 3)
    print("geschrieben: %s  (%.0f KB)" % (ziel, os.path.getsize(ziel) / 1024))
    print("Rollen: %d   Aufrufe geplant: %d" % (len(rollen), aufrufe))
    return ziel

if __name__ == "__main__":
    baue()
