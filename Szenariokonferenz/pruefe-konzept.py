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
if "**533**" not in zeilen[-1]: fehler.append(f"Summenzeile Aufrufe != 533: {zeilen[-1]}")
if auf!=533: fehler.append(f"Aufrufe addieren zu {auf}, nicht 533")
if not 515<=usd<=535: fehler.append(f"USD addieren zu {usd}, ausserhalb 'rund 525'")

# --- 2. Wanduhrzeit ---
std=auf/2*3/60
print(f"Wanduhrzeit bei Nebenlaeufigkeit 2 und 3 min/Aufruf: {std:.2f} h")
if abs(std-13.3)>0.3: fehler.append(f"13,3 h passt nicht zu {std:.2f} h")

# --- 3. Sitzungsteilung im Validierungsstand ---
phasen={"R0":13,"R1":110,"R1b":110,"R2":70,"R3":110,"R4":102,"R5":12,"R6":6}
if sum(phasen.values())!=auf: fehler.append(f"Phasensumme {sum(phasen.values())} != Tabelle {auf}")
sitz={"A":["R0","R1","R1b"],"B":["R2","R3"],"C":["R4","R5","R6"]}
for name,ph in sitz.items():
    n=sum(phasen[x] for x in ph); h=n/2*3/60
    print(f"  Sitzung {name}: {n} Aufrufe = {h:.2f} h")
    if f"({n} Aufrufe" not in V: fehler.append(f"Sitzung {name}: {n} Aufrufe steht nicht in 13")
groesste=max(phasen.values()); print(f"  groesste Einzelphase: {groesste} Aufrufe = {groesste/2*3/60:.2f} h")

# --- 4. Stufe 1 ---
s1={"Faktenblaetter":2,"Geruest":2,"Zerlegung":1,"R1":18,"KontrollarmR1":2,"R1b":20,"R2":18,"Gruppenleitung":6,"R3":18,"KontrollarmR3":2,"Hebel":1,"R4":18,"RedTeam":2}
n1=sum(s1.values()); print(f"Stufe 1: {n1} Aufrufe = {n1/2*3/60:.2f} h")
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
if phasen["R2"]!=30*2+5*2: fehler.append("Runde-2-Aufrufe passen nicht zu 30 Rollen und 5 Gruppen")
if phasen["R1"]!=100+10 or phasen["R3"]!=100+10: fehler.append("Kontrollarm fehlt in R1/R3")
if phasen["R1b"]!=110: fehler.append("Validierung deckt Kontrollarm nicht ab")
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

print("\n=== BEFUNDE ===")
print("\n".join(fehler) if fehler else "keine")
