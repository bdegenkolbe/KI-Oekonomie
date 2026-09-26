# -*- coding: utf-8 -*-
"""Erzeugt 28-Roster-v2.md aus roster_d.py und baue-sitzung-d.py.

Die Rollendaten sind ASCII (damit das erzeugte JavaScript bitgleich bleibt);
lesbar.py uebersetzt sie ueber eine gepruefte Tabelle in echte Umlaute.
"""
import collections, importlib.util, os, re, sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from roster_d import als_dicts, STATIONEN
from lesbar import lesbar as L

spec = importlib.util.spec_from_file_location("bsd", os.path.join(HIER, "baue-sitzung-d.py"))
bsd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bsd)

R = als_dicts()
c = collections.Counter(r["station"] for r in R)
out = []
w = out.append

w("# Roster der Sitzung D — die Übertragungskette")
w("")
w("**Zielfrage:** Was bedeutet Künstliche Intelligenz im Jahr 2031 für Europa, Deutschland, das")
w("deutsche Gesundheitswesen und die Gesellschaften des HIGL-Verbunds?")
w("")
w("**Grundlage:** Korinek, Jones, Sacher, Cotter & McCrory, *Economic Scenarios for Transformative AI*,")
w("The Anthropic Institute Working Paper No. 2026-02, Version 1.0, September 2026. Das Modell rechnet")
w("die US-Wirtschaft **2026 bis 2030**, bildet **ausschließlich kognitive Aufgaben** ab und ordnet seinen")
w("Szenarien ausdrücklich **keine Wahrscheinlichkeiten** zu. Die Autoren nennen die fehlende Robotik als")
w("Grund, nicht über 2030 hinauszurechnen. Genau dort setzt diese Sitzung an: Der Horizont bleibt 2031,")
w("und jede Rolle beantwortet das Jahr 2030 auf 2031 gesondert.")
w("")
w("*Ergebnisse des Laufs: `29-Strategiepapier-2031.md` (Schlussfassung) und `30-Sitzung-D.md`")
w("(Bericht über Abbruch, Gegenprüfung und verweigerte Freigabe).*")
w("")
w("---")
w("")
w("## Warum eine Kette und keine Bänke")
w("")
w("In den Sitzungen A bis C haben hundert Rollen **nebeneinander** geurteilt. Das war der")
w("Konstruktionsfehler: 73 der 100 Rollen saßen im deutschen Gesundheitswesen, und der Prompt der")
w("Runde 1 wies sie ausdrücklich an, *nicht* in der Gesamtwirtschaft zu recherchieren. Entsprechend kam")
w("ausschließlich Personalbedarf heraus — die Frage nach der Volkswirtschaft war nie gestellt worden.")
w("")
w("Sitzung D ist als **Kausalkette** gebaut. Fünf Stationen, jede empfängt eine quantifizierte Größe von")
w("der vorherigen und gibt eine weiter. Wer die Kette bricht, darf das — aber nicht stillschweigend: Der")
w("Einwand wird protokolliert, und eine eigene Prüfung hält jede Übergabe gegen die Annahme der")
w("Folgestation.")
w("")
w("| | Station | empfängt | gibt weiter | Rollen |")
w("|---|---|---|---|---:|")
for s in ("S0", "S1", "S2", "S3", "S4"):
    k, t, e, g = STATIONEN[s]
    w("| **%s** | %s | %s | %s | %d |" % (s[1], L(t), L(e) if e else "— (Kettenanfang)", L(g), c[s]))
w("")
w("Station 0 ist kein Vorspann, sondern der ganze Hebel des Anthropic-Papiers für Deutschland: Das")
w("Modell lässt die Lohnquote um vier Punkte (*substantial*) bis fünfzehn Punkte (*extreme*) fallen. Die")
w("deutsche Sozialversicherung ist vollständig an die Lohnsumme gekoppelt. Zwischen diesen zwei Sätzen")
w("liegt die gesamte Arbeit dieser Sitzung.")
w("")
w("Dazu drei Querbänke außerhalb der Kette: **Europa** (%d) urteilt vor der Kette und liefert den" % c["EU"])
w("Systemvergleich, **KI-Technik und die physische Schicht** (%d) den Fähigkeitsstand — darunter zwei" % c["KI"])
w("Robotikrollen, die genau dort ansetzen, wo das Papier aufhört —, die **Gegenposition** (%d) greift" % c["GP"])
w("am Ende an.")
w("")
w("**Station 3 wird doppelt gerechnet**, mit und ohne den amerikanischen Preisschock: Section-232-Zölle")
w("auf patentierte Arzneimittel und Wirkstoffe (Proclamation 11020 vom 2. April 2026, Federal Register")
w("2026-06956 — Basissatz 100 % ad valorem, länderspezifisch 15 % für die Europäische Union und 10 % für")
w("das Vereinigte Königreich; erste Stufe seit dem 31. Juli 2026 für die in Annex III gelisteten")
w("Unternehmen, zweite Stufe **ab dem 29. September 2026** für alle übrigen, also vier Tage nach dem")
w("Aufsetzen dieser Sitzung), Meistbegünstigung über die CMMI-Modelle GENEROUS, GLOBE und GUARD, und der")
w("Umstand, dass der deutsche AMNOG-Erstattungsbetrag die einzige öffentlich zugängliche")
w("Nettopreisreferenz Europas ist. Jede Rolle der Station liefert beide Werte und die Differenz. Nur so")
w("lässt sich trennen, was KI bewirkt und was die US-Politik bewirkt.")
w("")
w("Die genauen Tarifstufen, Stichtage und der Stand der MFN-Vereinbarungen kommen aus Faktenblatt N01")
w("dieser Sitzung, nicht aus dem Aufsetzen — dort sind sie mit Fundstelle und Abrufdatum belegt.")
w("")
w("---")
w("")
w("## Teil 1 — Die Rollen (100)")
w("")
w("*Mandat* ist die Interessenlage, aus der die Rolle spricht — sie darf und soll das Urteil färben.")
w("*Wissensanker* benennt, worauf die Rolle ihr Urteil stützt. *Blindstelle* ist ihre systematische")
w("Verzerrung; sie wird dem Agenten mitgeteilt, damit die Auswertung sie prüfen kann, nicht damit er sie")
w("ausgleicht. Jede Rolle ist eine Funktionsbeschreibung, keine reale Person.")
w("")
for s in ("S0", "S1", "S2", "S3", "S4", "EU", "KI", "GP"):
    k, t, e, g = STATIONEN[s]
    kopf = ("%s — %s" % (k, L(t))) if s.startswith("S") else ("Querbank — %s" % L(t))
    w("### %s (%d)" % (kopf, c[s]))
    w("")
    if s.startswith("S"):
        w("> **empfängt:** %s  " % (L(e) if e else "— (Kettenanfang)"))
        w("> **gibt weiter:** %s" % L(g))
        w("")
    gruppe = None
    w("| ID | Rolle | Mandat | Wissensanker | Blindstelle |")
    w("|---|---|---|---|---|")
    for r in R:
        if r["station"] != s:
            continue
        if r["gruppe"] != gruppe:
            gruppe = r["gruppe"]
            w("| | *%s* | | | |" % L(gruppe))
        w("| %s | %s | %s | %s | %s |"
          % (r["id"], L(r["rolle"]), L(r["mandat"]), L(r["anker"]), L(r["blindstelle"])))
    w("")

w("---")
w("")
w("## Teil 2 — Die Recherche (6 Blöcke)")
w("")
w("Recherchiert wird **nur**, was in den Sitzungen A bis C nachweislich fehlt. Die zehn Domänen R01 bis")
w("R10 der Runde 0 sind erhoben und in `21-Quellenpruefung.md` nachgeprüft; sie gehen als Bestand in")
w("jeden Prompt ein und werden nicht erneut angefasst. Wer eine Zahl braucht, die weder im Bestand noch")
w("in diesen sechs Blättern steht, kennzeichnet sie als Schätzung, statt selbst nachzurecherchieren.")
w("")
w("| ID | Domäne | Liefergegenstand | Ausdrückliche Grenze |")
w("|---|---|---|---|")
for (i, d, a, g) in bsd.RECHERCHE:
    w("| **%s** | %s | %s | %s |" % (i, L(d), L(bsd.einzeilig(a)), L(bsd.einzeilig(g))))
w("")
w("---")
w("")
w("## Teil 3 — Der Fragebogen")
w("")
w("Der alte Fragebogen (P1 bis P5) fragte ausschließlich nach Personalbedarf. Der neue nimmt die **fünf")
w("Steuerparameter des Anthropic-Modells** als Pflichtgrößen, ergänzt sie um die **vier")
w("Übertragungsbrüche**, die das Papier selbst offenlässt, und schließt mit den **Ergebnisgrößen**, die")
w("direkt gegen die US-Tabelle lesbar sind.")
w("")
w("```")
for z in L(bsd.FRAGEBOGEN).strip().splitlines():
    w(z)
w("```")
w("")
w("---")
w("")
w("## Teil 4 — Die Regeln")
w("")
w("```")
for z in L(bsd.REGELN).strip().splitlines():
    w(z)
w("```")
w("")
w("---")
w("")
w("## Teil 5 — Der Angriff")
w("")
w("| # | Titel | Auftrag |")
w("|---|---|---|")
for (n, t, a) in bsd.ANGRIFFE:
    w("| %d | %s | %s |" % (n, L(t), L(bsd.einzeilig(a))))
w("")
w("---")
w("")
w("## Teil 6 — Umfang")
w("")
w("| Phase | Aufrufe |")
w("|---|---:|")
for z, n in [("Recherche (6 Blöcke)", 6), ("Querschnitt (Europa 8, KI-Technik 6)", 14),
             ("Station 0 — Makro (20 Rollen + Übergabe)", 21), ("Station 1 — GKV und PKV (17 + Übergabe)", 18),
             ("Station 2 — Leistungserbringer (16 + Übergabe)", 17), ("Station 3 — Pharma und US-Schock (18 + Übergabe)", 19),
             ("Station 4 — HIGL (12 + Übergabe)", 13), ("Kettenprüfung (1 Prüfung + 5 Revisionen)", 6),
             ("Angriff (3 Gegenposition + 5 Red Team)", 8), ("Papier (5 Kapitel, Zusammenzug, Verifikation, Schlussfassung)", 8)]:
    w("| %s | %d |" % (z, n))
w("| **Summe** | **130** |")
w("")
w("Zum Vergleich: Sitzungen A bis C zusammen 503 Aufrufe, Sitzung C allein 120. Dass Sitzung D mit 130")
w("auskommt, liegt daran, dass der gesamte Bestand — gemeinsamer Faktenkern, Gültigkeitsbereich,")
w("Teil 1 Deutschland, Teil 2 Europa, Durchgriffskanäle — als Eingabe mitgegeben statt neu erarbeitet")
w("wird, und dass die Streitrunde durch die Kette ersetzt ist: Der Widerspruch entsteht dort, wo eine")
w("Station den Wert der vorherigen nicht annimmt.")
w("")
w("---")
w("")
w("*Erzeugt von `baue-roster-md.py` aus `roster_d.py` und `baue-sitzung-d.py`; Lesefassung über die")
w("geprüfte Tabelle in `lesbar.py`. Der ausführbare Lauf ist `workflow-sitzung-d.js`.*")

ziel = os.path.join(HIER, "28-Roster-v2.md")
with open(ziel, "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")
print("geschrieben: %s (%d Zeichen, %d Rollenzeilen)"
      % (ziel, len("\n".join(out)),
         sum(1 for z in out if re.match(r"^\| (S[0-4]|EU|KI|GP)-", z))))
