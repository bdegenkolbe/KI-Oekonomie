"""Rechnet die Abbruchkriterien aus 13-Validierungsstand.md 3 aus den Rohdaten der
Mechanikprobe nach. Keine Beurteilung, nur Rechnung. Aufruf ohne Argumente."""
import json, statistics as st
r=json.load(open('/home/user/KI-Oekonomie/Szenariokonferenz/rohdaten/mechanikprobe-10.json',encoding='utf-8'))
R1={x['id']:x for x in r['runde1']}; R3={x['id']:x for x in r['runde3']}
EIN=r['zug1']+r['zug2']
K1={x['id']:x for x in r['runde1_kontrollarm']}; K3={x['id']:x for x in r['runde3_kontrollarm']}
GER={x['id']:x['geruest'] for x in r['rollen']}
IDS=list(R1)

def q(xs,p):
    s=sorted(xs); i=(len(s)-1)*p; lo,hi=int(i//1), -(-i//1)
    lo,hi=int(lo),int(hi)
    return s[lo] if lo==hi else s[lo]+(s[hi]-s[lo])*(i-lo)
def iqr(xs): return q(xs,.75)-q(xs,.25)

GROESSEN=['p1','p2','p3','p3_null','p4_ki','p5_abfluss_ausland']
NAME={'p1':'P1 ersetzbar','p2':'P2 realisiert','p3':'P3 Personalbedarf','p3_null':'P3-null',
      'p4_ki':'P4 KI-Anteil','p5_abfluss_ausland':'P5 Abfluss Ausland'}

print("=== 1. DIVERGENZERHALT (IQR Runde 3 / IQR Runde 1) ===")
div={}
for g in GROESSEN:
    a=[R1[i][g] for i in IDS]; b=[R3[i][g] for i in IDS]
    ia,ib=iqr(a),iqr(b)
    div[g]=ib/ia if ia else None
    print(f"  {NAME[g]:22s} R1: Med {q(a,.5):7.1f} IQR {ia:6.2f} | R3: Med {q(b,.5):7.1f} IQR {ib:6.2f} | Erhalt {div[g]*100 if ia else float('nan'):6.1f} %")
ok=sum(1 for g in GROESSEN if div[g] is not None and div[g]>=0.5)
print(f"  -> {ok} von {len(GROESSEN)} Groessen halten >= 50 %   (Schwelle: 5 von 6)")

print("\n=== 2. MODELLABHAENGIGKEIT (Opus gegen Sonnet, dieselbe Rolle) ===")
for g in GROESSEN:
    panel=iqr([R1[i][g] for i in IDS])
    diffs=[abs(R1[i][g]-K1[i][g]) for i in K1]
    m=sum(diffs)/len(diffs)
    print(f"  {NAME[g]:22s} mittlere Differenz {m:7.2f} | Panel-IQR {panel:6.2f} | Verhaeltnis {m/panel if panel else float('inf'):5.2f}")
    for i in K1: print(f"        {i}: Opus {R1[i][g]:7.1f}  Sonnet {K1[i][g]:7.1f}")

print("\n=== 3. GERUESTABHAENGIGKEIT (Median A gegen Median B) ===")
A=[i for i in IDS if GER[i]=='A']; B=[i for i in IDS if GER[i]=='B']
print(f"  Geruest A: {A}\n  Geruest B: {B}")
for g in GROESSEN:
    ma,mb=q([R1[i][g] for i in A],.5), q([R1[i][g] for i in B],.5)
    panel=iqr([R1[i][g] for i in IDS])
    print(f"  {NAME[g]:22s} A {ma:7.1f} | B {mb:7.1f} | Abstand {abs(ma-mb):6.2f} | Panel-IQR {panel:6.2f} | Verhaeltnis {abs(ma-mb)/panel if panel else float('inf'):5.2f}")

print("\n=== 4. ATTRIBUTIONSKONSISTENZ ===")
kons=[]
for i in IDS:
    p3,p3n,ki=R1[i]['p3'],R1[i]['p3_null'],R1[i]['p4_ki']
    abgeleitet=(p3-p3n)/p3*100 if p3 else None
    if abgeleitet is None: continue
    d=abs(abgeleitet-ki); kons.append((i,abgeleitet,ki,d))
    print(f"  {i}: P3 {p3:6.1f} P3-null {p3n:6.1f} -> abgeleiteter KI-Anteil {abgeleitet:6.1f} % | genannt {ki:5.1f} % | Abweichung {d:5.1f}")
tr=[x for x in kons if x[3]<=15]
print(f"  -> {len(tr)} von {len(kons)} innerhalb 15 Punkten = {len(tr)/len(kons)*100:.0f} %   (Schwelle 80 %)")

print("\n=== 5. SCHEMAFESTIGKEIT: Anteilssummen ===")
bad=0
for i in IDS:
    for quelle,label in ((R1,'R1'),(R3,'R3')):
        x=quelle[i]
        s4=x['p4_ki']+x['p4_demografie']+x['p4_strukturreform']
        s5=x['p5_leistungserbringer']+x['p5_preis_beitrag']+x['p5_abfluss_ausland']+x['p5_neue_leistung']
        if abs(s4-100)>0.01 or abs(s5-100)>0.01:
            bad+=1; print(f"  ABWEICHUNG {label} {i}: P4={s4} P5={s5}")
print(f"  -> {bad} Abweichungen bei {len(IDS)*2} Kartensaetzen")

print("=== 6. FREMDBEZUG und ADRESSIERUNG ===")
eigen=0; ungueltig=0
for e in EIN:
    ziel=e['einwand_bezug']
    treffer=[i for i in IDS if i in ziel]
    if not treffer: ungueltig+=1; print(f"  UNGUELTIGER BEZUG: {e['id']} -> {ziel}")
    elif treffer[0]==e['id']: eigen+=1; print(f"  EIGENES FELD: {e['id']} -> {ziel}")
print(f"  -> {len(EIN)} Einwaende, {eigen} gegen das eigene Feld ({eigen/len(EIN)*100:.0f} %, Schwelle <= 20 %), {ungueltig} ohne gueltigen Bezug (Schwelle 0)")

print("\n=== 7. RETTUNGSBEDINGUNG / LEERZUEGE ===")
leer=[e for e in EIN if len(e.get('rettungsbedingung','').split())<6]
print(f"  {len(EIN)} Einwaende, davon {len(leer)} mit weniger als sechs Woertern Rettungsbedingung")
print(f"  kuerzeste: {min(len(e['rettungsbedingung'].split()) for e in EIN)} Woerter | Median {sorted(len(e['rettungsbedingung'].split()) for e in EIN)[len(EIN)//2]}")
for e in EIN[:2]: print(f"  Beispiel {e['id']} ({e['einwandtyp']}): {e['rettungsbedingung'][:220]}")
typen={}
for e in EIN: typen[e['einwandtyp']]=typen.get(e['einwandtyp'],0)+1
print("  Einwandtypen:", typen)

print("\n=== 8. OPTIONENSPREIZUNG ===")
urteile={}
for o in r['optionen']:
    for b in o['bewertungen']:
        urteile.setdefault(b['hebel_nr'],[]).append(b['urteil'])
for h in r['hebel']:
    u=urteile.get(h['nr'],[])
    abw=sum(1 for x in u if x!='wirkt')
    print(f"  Hebel {h['nr']} ({h['titel'][:52]}): wirkt {u.count('wirkt')}, wirkt nicht {u.count('wirkt nicht')}, schadet {u.count('schadet')} -> abweichend {abw/len(u)*100:.0f} %")
gespreizt=sum(1 for h in r['hebel'] if sum(1 for x in urteile.get(h['nr'],[]) if x!='wirkt')/len(urteile.get(h['nr'],[]))>=0.2)
print(f"  -> {gespreizt} von {len(r['hebel'])} Hebeln mit >= 20 % abweichendem Urteil (Schwelle 2 von 3)")

print("\n=== 9. RECHENWEGHALTBARKEIT ===")
SAAT={(g['rolle'],g['wo']) for g in r['gesetzte_fehler']}
ges=0; traegt=0
for p in r['pruefungen']:
    for g in ['p1','p2','p3','p3_null']:
        if (p['id'],g) in SAAT: continue   # absichtlich verfaelscht, zaehlt nicht
        ges+=1
        if g in p['rechenweg_traegt']: traegt+=1
print(f"  -> {traegt} von {ges} unverfaelschten Pflichtgroessen nachrechenbar = {traegt/ges*100:.0f} % (Schwelle 90 %)")

print("\n=== 10. WEITERE BEANSTANDUNGEN der Pruefinstanz (jenseits der gesetzten Fehler) ===")
n=0
for p in r['pruefungen']:
    for b in p['beanstandungen']:
        if (p['id'],b['wo']) in SAAT: continue
        n+=1
        if n<=12: print(f"  {p['id']} {b['wo']} [{b['schwere']}]: {b['was'][:150]}")
print(f"  insgesamt {n}")

print("\n=== 11. BEWEGUNG ZWISCHEN RUNDE 1 UND RUNDE 3 ===")
beweg=0
for i in IDS:
    d=[abs(R1[i][g]-R3[i][g]) for g in ['p1','p2','p3','p3_null','p4_ki','p5_abfluss_ausland']]
    if max(d)>0: beweg+=1
    print(f"  {i}: groesste Aenderung {max(d):5.1f} Punkte")
print(f"  -> {beweg} von {len(IDS)} Rollen haben mindestens einen Wert geaendert")
print("Vergleich der beiden Attributionsformeln\n")
print(f"{'Rolle':6} {'P3':>7} {'P3-0':>7} {'KI-Beitrag':>11} {'alt (/P3)':>11} {'neu (Anteil)':>13} {'genannt':>8} {'|alt-gen|':>10} {'|neu-gen|':>10}")
alt_ok=neu_ok=0
for i in R1:
    p3,p0,ki=R1[i]['p3'],R1[i]['p3_null'],R1[i]['p4_ki']
    beitrag=p3-p0
    alt=beitrag/p3*100 if p3 else float('nan')
    neu=abs(beitrag)/(abs(beitrag)+abs(p0))*100 if (abs(beitrag)+abs(p0)) else float('nan')
    da,dn=abs(alt-ki),abs(neu-ki)
    alt_ok+= da<=15; neu_ok+= dn<=15
    print(f"{i:6} {p3:7.1f} {p0:7.1f} {beitrag:11.1f} {alt:11.1f} {neu:13.1f} {ki:8.1f} {da:10.1f} {dn:10.1f}")
print(f"\nalte Formel (P3-P3_0)/P3:                    {alt_ok}/10 = {alt_ok*10} %")
print(f"neue Formel |P3-P3_0| / (|P3-P3_0| + |P3_0|): {neu_ok}/10 = {neu_ok*10} %   (Schwelle 80 %)")
print("\nWarum die alte Formel bricht: sie teilt durch P3. Wo P3 nahe null liegt,")
print("weil KI-Entlastung und Demografiebedarf sich fast aufheben, explodiert der Quotient.")
for i in R1:
    p3=R1[i]['p3']
    if abs(p3)<2.5: print(f"  {i}: P3 = {p3:+.1f} - Nenner nahe null")
