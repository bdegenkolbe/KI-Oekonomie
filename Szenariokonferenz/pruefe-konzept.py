"""Prueft das Konzeptpaket auf Rechen- und Querverweisfehler. Nur Befunde, keine Urteile."""
import re, itertools
SZ="/home/user/KI-Oekonomie/Szenariokonferenz/"
K=open(SZ+"11-Konzept-v2.md",encoding="utf-8").read()
V=open(SZ+"13-Validierungsstand.md",encoding="utf-8").read()
R=open(SZ+"14-Roster-2031.md",encoding="utf-8").read()
fehler=[]

# --- 1. Kostentabelle im Konzept: Spaltensummen ---
tab=K.split("| Phase | Aufrufe | USD |")[1].split("\n\n")[0]
zeilen=[z for z in tab.strip().split("\n") if z.startswith("|") and "---" not in z]
auf=usd=0
for z in zeilen[:-1]:
    sp=[s.strip() for s in z.strip("|").split("|")]
    a=re.match(r"(\d+)",sp[1]); u=re.match(r"(\d+)",sp[2])
    auf+=int(a.group(1)) if a else 0
    usd+=int(u.group(1)) if u else 0
print(f"Kostentabelle: {len(zeilen)-1} Posten, Aufrufe {auf}, USD {usd}")
if "**503**" not in zeilen[-1]: fehler.append(f"Summenzeile Aufrufe != 503: {zeilen[-1]}")
if auf!=503: fehler.append(f"Aufrufe addieren zu {auf}, nicht 503")
if not 505<=usd<=525: fehler.append(f"USD addieren zu {usd}, ausserhalb 'rund 515'")

# --- 2. Wanduhrzeit ---
m=re.search(r"\*\*(\d+,\d+) Minuten je Aufruf\*\*",K)
if not m: fehler.append("Konzept nennt keine gemessene Minutenrate je Aufruf")
RATE=float(m.group(1).replace(",",".")) if m else 3.0
std=auf/2*RATE/60
print(f"Wanduhrzeit bei Nebenlaeufigkeit 2 und {RATE} min/Aufruf: {std:.2f} h")
m2=re.search(r"ergeben 503 Aufrufe damit \*\*rund (\d+) Stunden\*\*",K)
if not m2: fehler.append("Konzept nennt keine Gesamtstundenzahl fuer 503 Aufrufe")
elif abs(std-int(m2.group(1)))>0.5: fehler.append(f"Konzept nennt {m2.group(1)} h, gerechnet {std:.2f} h")

# --- 3. Sitzungsteilung im Validierungsstand ---
# Phasen so, wie die Kostentabelle sie fuehrt. R0 enthaelt die Quellenpruefung (0c),
# R1b nur den Hauptarm (der Kontrollarm wird nicht validiert), R2 beide Zuege je Rolle
# in einem Aufruf (siehe Konzept Paragraf 5, Runde 2).
phasen={"R0":23,"R1":110,"R1b":100,"R2":40,"R3":110,"R4":105,"R5":9,"R6":6}
if sum(phasen.values())!=auf: fehler.append(f"Phasensumme {sum(phasen.values())} != Tabelle {auf}")
sitz={"A":["R0","R1","R1b"],"B":["R2","R3"],"C":["R4","R5","R6"]}
for name,ph in sitz.items():
    n=sum(phasen[x] for x in ph); h=n/2*RATE/60
    print(f"  Sitzung {name}: {n} Aufrufe = {h:.2f} h")
    if f"({n} Aufrufe" not in V: fehler.append(f"Sitzung {name}: {n} Aufrufe steht nicht in 13")
    else:
        ms=re.search(rf"\({n} Aufrufe, rund ([\d,]+) Stunden\)",V)
        if not ms: fehler.append(f"Sitzung {name}: keine Stundenangabe zu {n} Aufrufen in 13")
        elif abs(float(ms.group(1).replace(",","."))-h)>0.3: fehler.append(f"Sitzung {name}: 13 nennt {ms.group(1)} h, gerechnet {h:.2f} h")
groesste=max(phasen.values()); print(f"  groesste Einzelphase: {groesste} Aufrufe = {groesste/2*RATE/60:.2f} h")

# --- 4. Stufe 1 ---
s1={"Faktenblaetter":2,"Geruest":2,"Zerlegung":1,"R1":18,"KontrollarmR1":2,"R1b":20,"R2":18,"Gruppenleitung":6,"R3":18,"KontrollarmR3":2,"Hebel":1,"R4":18,"RedTeam":2}
n1=sum(s1.values()); print(f"Stufe 1: {n1} Aufrufe = {n1/2*RATE/60:.2f} h")
if f"{n1} Aufrufe" not in V: fehler.append(f"Stufe 1: {n1} Aufrufe steht nicht in 13")

# --- 5. Roster: Bankgroessen gegen Teil 3 ---
baenke={}
for m in re.finditer(r"^## Bank ([A-N]) — (.+?) \((\d+)\)$",R,re.M): baenke[m.group(1)]=int(m.group(3))
ist={b:len(re.findall(rf"^\| {b}\d\d \|",R,re.M)) for b in baenke}
for b in baenke:
    if baenke[b]!=ist[b]: fehler.append(f"Bank {b}: Ueberschrift {baenke[b]}, Tabellenzeilen {ist[b]}")
print("Baenke:",{b:baenke[b] for b in sorted(baenke)},"Summe",sum(baenke.values()))
if sum(baenke.values())!=100: fehler.append(f"Baenke summieren zu {sum(baenke.values())}")
eng=sum(baenke[b] for b in "ABCDEFGH"); recht=baenke["I"]
print(f"engeres Gesundheitswesen {eng}, Recht/Ethik {recht}, Summe {eng+recht}, Rest {100-eng-recht}")
if f"| Gesundheitswesen im engeren Sinn (A, B, C, D, E, F, G, H) | {eng} |" not in R:
    fehler.append("Teil-3-Tabelle nennt nicht die berechneten "+str(eng))
if f"**{eng+recht} Stimmen im Gesundheitswesen und seinem Recht, {100-eng-recht} in" not in R:
    fehler.append(f"Kopfzeile nennt nicht {eng+recht}/{100-eng-recht}")

# --- 6. Streitauswahl: 14 Baenke + 16 = 30, 5 Gruppen a 6 ---
if len(baenke)!=14: fehler.append(f"{len(baenke)} Baenke, Bankquote im Konzept nennt 14")
if 14+16!=30 or 5*6!=30: fehler.append("Streitauswahl-Arithmetik")
# 30 Rollen mit je EINEM Aufruf fuer beide Zuege, dazu 5 Gruppen mit Streitfrage und Protokoll
if phasen["R2"]!=30+5*2: fehler.append("Runde-2-Aufrufe passen nicht zu 30 Rollen und 5 Gruppen")
if phasen["R1"]!=100+10 or phasen["R3"]!=100+10: fehler.append("Kontrollarm fehlt in R1/R3")
# Der Kontrollarm wird bewusst nicht validiert: Er misst die Modellabhaengigkeit,
# nicht die Kartenqualitaet, und eine Pruefung wuerde ihn nur teurer machen.
if phasen["R1b"]!=100: fehler.append("Validierung deckt nicht genau den Hauptarm ab")
# Stufe 1: Bankmedian braucht >=6 Rollen je Bank
import math
if 18//3<6: fehler.append("Stufe 1: weniger als 6 Rollen je Bank")

# --- 7. Pflichtgroessen P1..P5 durchgaengig ---
for p in ["P1","P2","P3","P3\u2080","P4","P5"]:
    if f"**{p}**" not in K: fehler.append(f"{p} fehlt in der Pflichtgroessen-Tabelle")
# --- 8. Kartentypen: jeder in 4.1 genannte Typ kommt im Ablauf vor ---
typen=set(re.findall(r"^\| `(\w+)` \|",K,re.M))
print("Kartentypen:",sorted(typen))
for t in typen:
    if K.count(f"`{t}`")<2: fehler.append(f"Kartentyp {t} nur einmal erwaehnt")

# --- 9. Querverweise auf Abschnittsnummern ---
absch={int(m.group(1)) for m in re.finditer(r"^## (\d+)\.",K,re.M)}
print("Abschnitte im Konzept:",sorted(absch))
import glob
for d in glob.glob(SZ+"*.md"):
    t=open(d,encoding="utf-8").read()
    for m in re.finditer(r"`11-Konzept-v2\.md` § (\d+)",t):
        if int(m.group(1)) not in absch: fehler.append(f"{d.split('/')[-1]}: Verweis auf § {m.group(1)}, den es nicht gibt")


# --- 10. Neue Bestandteile nach der Mechanikprobe ---
pflicht = {
    "Marktgroessen":       "### 3.2 Die Marktgr\u00f6\u00dfen",
    "Leistungsprofile":    "Leistungsprofile",
    "Ableitungsrichtung":  "vom Engpass zum Profil, nie vom Portfolio zum Profil",
    "Interessenkonflikt":  "16-Marktschicht.md",
    "D-Formel":            "|P3 \u2212 P3\u2080| \u00f7 (P1 \u00d7 P2 \u00f7 100)",
    "Zahlenmatrix":        "Zahlenmatrix",
    "Auszugsregel":        "### 4.3 Wer welchen Ausschnitt sieht",
    "Status je Karte":     "Der Status geh\u00f6rt zur Karte, nicht zur Rolle",
    "Filter je Karte":     "Gefiltert wird je Karte, nie je Rolle",
    "bestrittener Nenner": "Wenn eine Rolle ihren Nenner bestreitet",
    "Lauffaehigkeit":      "keinen Dateisystemzugriff",
}
for name, marke in pflicht.items():
    if marke not in K:
        fehler.append(f"Konzept: Baustein '{name}' fehlt")
_lauf = K.split("**Was es nicht gibt.**")
if "rohdaten/lauf/" in _lauf[0] or (len(_lauf) > 1 and "rohdaten/lauf/" in _lauf[1].split("**Was es gibt")[1]):
    fehler.append("Konzept verlangt weiterhin eine Zwischenspeicherung ins Dateisystem")
if "D" not in K.split("Der **Streitindex** einer Rolle ist die Summe dieser sechs Werte")[0][-600:]:
    fehler.append("Streitindex nennt D nicht")

# Auszugsregel: jede Runde des Ablaufs kommt in der Tabelle vor
auszug = K.split("### 4.3 Wer welchen Ausschnitt sieht")[1].split("### 4.4")[0]
for runde in ["1", "1b", "2", "3", "4", "5"]:
    if f"| {runde} |" not in auszug:
        fehler.append(f"Auszugsregel: Runde {runde} fehlt in der Tabelle")

# --- 11. Querbezuege in die Mechanikprobe muessen existieren ---
M = open(SZ + "15-Mechanikprobe.md", encoding="utf-8").read()
import re as _re
for m in _re.finditer(r"`15-Mechanikprobe\.md` \u00a7 (\d+[a-e]?)", K + V):
    ziel = m.group(1)
    nr = _re.match(r"(\d+)([a-e]?)", ziel)
    if f"## {nr.group(1)}." not in M:
        fehler.append(f"Verweis auf 15-Mechanikprobe.md \u00a7 {ziel}, den es nicht gibt")
    if nr.group(2) and f"**({nr.group(2)})" not in M:
        fehler.append(f"Verweis auf 15-Mechanikprobe.md \u00a7 {ziel}: Unterpunkt ({nr.group(2)}) fehlt")

# --- 12. Zahlen der Probe in allen drei Dokumenten gleich ---
for zahl, wo in [("57", "Aufrufe der Probe"), ("4,28", "Minuten je Aufruf"), ("19", "Stunden voller Lauf")]:
    if zahl not in M:
        fehler.append(f"Mechanikprobe nennt {wo} ({zahl}) nicht")

# --- 12b. Zahl der Abbruchkriterien muss zum Text passen ---
_tab = V.split("| Kriterium | Schwelle | Was es pr\u00fcft |")[1].split("\n\n")[0]
_k = [z for z in _tab.strip().split("\n") if z.startswith("|") and "---" not in z]
ZAHLWORT = {12:"zw\u00f6lf",13:"dreizehn",14:"vierzehn",15:"f\u00fcnfzehn",16:"sechzehn",17:"siebzehn"}
if ZAHLWORT.get(len(_k)) and f"{ZAHLWORT[len(_k)]} vorab festgelegte" not in V.lower():
    _gefunden = [w for w in ZAHLWORT.values() if f"{w} vorab festgelegte" in V.lower()]
    fehler.append(f"13 hat {len(_k)} Abbruchkriterien, Text sagt {_gefunden or 'nichts'}")
print(f"Abbruchkriterien in 13: {len(_k)}")

# --- 13. Interne Abschnittsverweise im Konzept ---
unter = set(re.findall(r"^### (\d+\.\d+) ", K, re.M))
for m in re.finditer(r"\u00a7 (\d+\.\d+)", K):
    if m.group(1) not in unter:
        fehler.append(f"Konzept: interner Verweis auf \u00a7 {m.group(1)}, den es nicht gibt (vorhanden: {sorted(unter)})")
GESETZ = "(?!\\s*[a-z]?\\s+(?:SGB|AO|StGB|StBerG|StBVV|KHEntgG|KHVVG|BetrVG|GewStG|ApBetrO|VVG|PflBG|IfSG|NotSanG|DSGVO|GG|BGB|HGB|EBM|MDR))"
for m in re.finditer("\u00a7 (\\d+)[a-z]?" + GESETZ + "(?![\\.\\d])", K):
    if int(m.group(1)) not in absch:
        fehler.append(f"Konzept: interner Verweis auf \u00a7 {m.group(1)}, den es nicht gibt")

# --- 14. Anker und Geruest duerfen nicht an derselben Regel haengen ---
R = open(SZ + "14-Roster-2031.md", encoding="utf-8").read()
for datei, txt in (("11-Konzept-v2.md", K), ("14-Roster-2031.md", R)):
    if "modulo vier" not in txt and "Ger\u00fcstzuteilung" in txt:
        fehler.append(f"{datei}: Ger\u00fcstzuteilung nennt keinen von der Ankerparit\u00e4t getrennten Plan")
if "ungerade IDs rechnen gegen" in K + R:
    fehler.append("Ger\u00fcst h\u00e4ngt weiterhin an der ID-Parit\u00e4t - konfundiert mit dem Anker")
if "laufenden Index" not in K or "laufenden Index" not in R:
    fehler.append("Zuteilung nennt nicht den laufenden Index - ID-Regel waere mit der Bankgroesse konfundiert")
import json as _j, os as _os
_rp = SZ + "rohdaten/roster.json"
if _os.path.exists(_rp):
    _r = _j.load(open(_rp, encoding="utf-8"))["rollen"]
    from collections import Counter as _C
    _z = _C((x["geruest"], x["anker_reihenfolge"]) for x in _r)
    print("Roster-Zellen:", dict(_z))
    if len(_r) != 100: fehler.append(f"roster.json hat {len(_r)} Rollen")
    if set(_z.values()) != {25}: fehler.append(f"Zellen nicht 25/25/25/25: {dict(_z)}")

print("\n=== BEFUNDE (erweitert) ===")

print("\n".join(fehler) if fehler else "keine")
