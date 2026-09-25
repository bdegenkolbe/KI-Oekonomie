# -*- coding: utf-8 -*-
"""Rueckfuehrung der ASCII-Transliteration in roster_d.py auf echte Umlaute.

Nur fuer die Lesefassung. Die JS-Fassung bleibt ASCII, damit der laufende
Workflow bitgleich bleibt.
"""
import re

# Stellen, an denen 'ue' kein transliteriertes ü ist
SCHUTZ_UE = ("teuer", "neuer", "treuer", "dauer", "zuerst", "quer", "quel", "quen")
# ss -> ß nur dort, wo es wirklich hingehoert (nach Umlautersetzung angewandt)
SCHARF = {
    "Grösse": "Größe", "Massstab": "Maßstab",
    "Honorarverteilungsmassstab": "Honorarverteilungsmaßstab",
    "grossen": "großen", "Grossauftragsgeschäft": "Großauftragsgeschäft",
    "Grosshandelszuschlag": "Großhandelszuschlag", "Grosskunden": "Großkunden",
    "Grossunternehmen": "Großunternehmen", "Pharmagrosshandels": "Pharmagroßhandels",
    "Aussenmarkt": "Außenmarkt", "zweckmässige": "zweckmäßige", "gross": "groß", "Gross": "Groß",
}

def _wort(w):
    roh = w
    w = w.replace("ae", "ä").replace("Ae", "Ä")
    w = w.replace("oe", "ö").replace("Oe", "Ö")
    if not any(s in roh.lower() for s in SCHUTZ_UE):
        w = w.replace("ue", "ü").replace("Ue", "Ü")
    else:  # gemischte Woerter: nur die ue ausserhalb der Schutzstellen
        teile, i, out = [], 0, ""
        low = roh.lower()
        while i < len(w):
            if w[i:i+2].lower() == "ue" and any(
                    low[max(0, i-6):i+6].find(s) >= 0 for s in SCHUTZ_UE):
                out += w[i]; i += 1
            elif w[i:i+2] == "ue":
                out += "ü"; i += 2
            elif w[i:i+2] == "Ue":
                out += "Ü"; i += 2
            else:
                out += w[i]; i += 1
        w = out
    return SCHARF.get(w, w)

def lesbar(text):
    return re.sub(r"[A-Za-zÄÖÜäöüß-]+", lambda m: _wort(m.group(0)), str(text))

if __name__ == "__main__":
    from roster_d import ROLLEN
    txt = " ".join(" ".join(map(str, r)) for r in ROLLEN)
    tok = sorted({t for t in re.findall(r"[A-Za-zÄÖÜäöüß-]+", txt)
                  if re.search(r"ue|ae|oe|ss", t)})
    fehler = []
    for t in tok:
        u = _wort(t)
        if u != t:
            print("%-42s -> %s" % (t, u))
        else:
            fehler.append(t)
    print("\nUNVERAENDERT (muessen alle korrekt sein):")
    print("  " + ", ".join(fehler))
