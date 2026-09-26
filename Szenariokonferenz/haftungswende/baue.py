# -*- coding: utf-8 -*-
"""Erzeugt das Strategiepapier "Die Haftungswende" als HTML-Seite.

Alle Zahlen stammen aus rohdaten/sitzung-d.json (Sitzung D der
Szenariokonferenz), dem Faktenkern 01-Briefing.md und den
DATEV-Kontenblaettern 2025. Die Diagramme werden aus diesen Werten berechnet.
"""
import json, os, statistics as st, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from grafik import (de, hbalken, punkte_intervall, punktwolke, gestapelt,
                    waermefeld, zeitstrahl, kette, gruppen, svg, _t, W, MINUS)

ROH = json.load(open(os.path.join(HIER, "..", "rohdaten", "sitzung-d.json"), encoding="utf-8"))

# ------------------------------------------------------------ Werte aus den Rohdaten
ERG = ROH["ergebnisse"]
def med(station, feld):
    return st.median([c[feld] for c in ERG[station]])

# gerundet wie in 30-Sitzung-D.md (Python rundet ,5 auf die gerade Zahl: 52,5 -> 52; 27,5 -> 28)
DURCHGRIFF = {s: round(med(s, "d2_preisdurchgriff")) for s in ERG}
E3 = {s: [round(med(s, f)) for f in ("e3_kapital", "e3_kunden", "e3_beschaeftigte", "e3_staat")] for s in ERG}
SZEN = {k: sum(1 for s in ERG for c in ERG[s] if c["szenario"] == k) for k in ("modest", "substantial", "extreme")}
N_KETTE = sum(SZEN.values())

# US-Effekt je Fachurteil der Station 3 (aus dem Wortlaut der Karten gelesen und geprueft)
US_EFFEKT = [("S3-01", 13.6), ("S3-02", -5), ("S3-03", -8), ("S3-04", -11), ("S3-05", 8),
             ("S3-06", 4), ("S3-07", -6), ("S3-08", 11), ("S3-09", 21), ("S3-10", 15),
             ("S3-11", 11), ("S3-12", 5), ("S3-13", 16), ("S3-14", 8), ("S3-15", 8),
             ("S3-16", 10.3), ("S3-17", 25), ("S3-18", 10.2)]
US_MEDIAN = st.median([v for _, v in US_EFFEKT])
US_POS = sum(1 for _, v in US_EFFEKT if v > 0)

assert DURCHGRIFF["S2"] == 12 and DURCHGRIFF["S0"] == 52 and DURCHGRIFF["S4"] == 58
assert SZEN == {"modest": 8, "substantial": 73, "extreme": 2}
assert len(US_EFFEKT) == 18

# ------------------------------------------------------------ Gestaltung
CSS = r"""
:root{
  --paper:#F3F5F8; --surface:#FFFFFF; --ink:#132339; --ink-2:#34435A; --muted:#627089;
  --rule:#D4DAE3; --accent:#0B5AA2; --accent-2:#8FB3DA; --accent-soft:#E1EBF6;
  --gain:#2A7A55; --loss:#B2432B; --band:#EDF1F6;
  --serif:"Source Serif 4","Iowan Old Style","Georgia",serif;
  --sans:"IBM Plex Sans","Segoe UI","Helvetica Neue",Arial,sans-serif;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --paper:#0E1520; --surface:#151F2D; --ink:#E6EBF2; --ink-2:#BAC4D2; --muted:#8B97AA;
    --rule:#2B3748; --accent:#6EA8DE; --accent-2:#35587E; --accent-soft:#1B2A3D;
    --gain:#5CB689; --loss:#E27B60; --band:#182434; color-scheme:dark;
  }
}
:root[data-theme="dark"]{
  --paper:#0E1520; --surface:#151F2D; --ink:#E6EBF2; --ink-2:#BAC4D2; --muted:#8B97AA;
  --rule:#2B3748; --accent:#6EA8DE; --accent-2:#35587E; --accent-soft:#1B2A3D;
  --gain:#5CB689; --loss:#E27B60; --band:#182434; color-scheme:dark;
}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.62;
  -webkit-font-smoothing:antialiased;font-variant-numeric:tabular-nums;}
.wrap{max-width:1000px;margin:0 auto;padding-inline:20px;padding-block:0 64px;}
.blatt{background:var(--surface);padding:clamp(22px,5vw,64px);margin-block:28px;border:1px solid var(--rule);}
.prose{max-width:700px;}
p{margin:0 0 1em;}
h1,h2{font-family:var(--serif);font-weight:600;letter-spacing:-0.01em;text-wrap:balance;margin:0;color:var(--ink);}
h3{font-family:var(--sans);font-size:1.08rem;font-weight:700;margin:2em 0 .6em;color:var(--ink);text-wrap:balance;}
strong{font-weight:650;color:var(--ink);}
.eyebrow{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);}
.muted{color:var(--muted);}
a{color:var(--accent);}
a:focus-visible{outline:2px solid var(--accent);outline-offset:2px;}

/* Titelseite */
.titel{padding-block:clamp(40px,9vw,110px);}
.titel h1{font-size:clamp(2.1rem,8.6vw,4.6rem);overflow-wrap:anywhere;line-height:1.02;margin:.35em 0 .3em;}
.titel .unter{font-family:var(--serif);font-size:clamp(1.15rem,2.4vw,1.5rem);line-height:1.35;color:var(--ink-2);max-width:640px;font-weight:500;}
.titel .meta{margin-top:2.6em;display:flex;flex-wrap:wrap;gap:10px 36px;font-size:.88rem;color:var(--muted);border-top:1px solid var(--rule);padding-top:1em;}
.titel .meta b{display:block;color:var(--ink);font-weight:600;}

/* Inhalt */
.inhalt ol{list-style:none;margin:0;padding:0;display:grid;gap:0;}
.inhalt li{display:grid;grid-template-columns:3.2em 1fr auto;gap:12px;padding:.7em 0;border-bottom:1px solid var(--rule);align-items:baseline;}
.inhalt li span:first-child{font-family:var(--serif);font-size:1.25rem;color:var(--accent);font-weight:600;}
.inhalt li a{color:var(--ink);text-decoration:none;font-weight:500;}
.inhalt li a:hover{color:var(--accent);}
.inhalt li em{font-style:normal;color:var(--muted);font-size:.85rem;}

/* Kapitel */
.kapkopf{border-bottom:2px solid var(--ink);padding-bottom:1.1em;margin-bottom:1.6em;}
.kapkopf h2{font-size:clamp(1.8rem,3.8vw,2.55rem);line-height:1.12;margin-top:.3em;}
.kern{font-family:var(--serif);font-size:clamp(1.12rem,2vw,1.28rem);line-height:1.5;color:var(--ink-2);max-width:720px;margin:1em 0 0;}

/* Kernaussagen */
.kernaussagen{list-style:none;margin:1.6em 0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:0 36px;}
.kernaussagen li{padding:1em 0;border-top:1px solid var(--rule);display:grid;grid-template-columns:2em 1fr;gap:6px;}
.kernaussagen li b{font-family:var(--serif);color:var(--accent);font-size:1.3rem;line-height:1.2;}
.kernaussagen li strong{display:block;margin-bottom:.25em;font-size:1.02rem;}
.kernaussagen li span{color:var(--ink-2);font-size:.95rem;}

/* Entscheidungskasten */
.entscheidung{border:1px solid var(--ink);border-top:5px solid var(--accent);padding:22px 26px;margin:2em 0;background:var(--surface);}
.entscheidung h3{margin-top:.2em;font-size:1.25rem;font-family:var(--serif);font-weight:600;}
.zahlen{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:16px;margin-top:1em;}
.zahlen div{border-top:1px solid var(--rule);padding-top:.6em;}
.zahlen b{display:block;font-family:var(--serif);font-size:1.9rem;line-height:1.1;color:var(--ink);font-weight:600;}
.zahlen span{font-size:.85rem;color:var(--muted);}

/* Abbildungen */
figure{margin:2.2em 0;padding:0;break-inside:avoid;}
.abbkopf{border-top:1px solid var(--ink);padding-top:.7em;margin-bottom:.8em;}
.abbkopf .eyebrow{color:var(--muted);}
.abbtitel{font-weight:700;font-size:1.08rem;line-height:1.35;margin:.2em 0 .15em;text-wrap:balance;}
.abbunter{font-size:.86rem;color:var(--muted);}
.chart{overflow-x:auto;}
.chart svg{display:block;width:100%;min-width:560px;height:auto;}
figcaption{font-size:.78rem;color:var(--muted);border-top:1px solid var(--rule);padding-top:.55em;margin-top:.7em;line-height:1.5;}
svg text{font-family:var(--sans);}
.t-ink{fill:var(--ink);} .t-muted{fill:var(--muted);} .t-inv{fill:var(--surface);}
.f-accent{fill:var(--accent);} .f-accent2{fill:var(--accent-2);} .f-soft{fill:var(--accent-soft);}
.f-gain{fill:var(--gain);} .f-loss{fill:var(--loss);} .f-muted{fill:var(--muted);} .f-rule{fill:var(--rule);}
.s-rule{stroke:var(--rule);} .s-ink{stroke:var(--ink);} .s-muted{stroke:var(--muted);} .s-accent{stroke:var(--accent);}
.s-gain{stroke:var(--gain);} .s-loss{stroke:var(--loss);}

/* Tabellen */
.tabelle{overflow-x:auto;}
table{border-collapse:collapse;width:100%;font-size:.9rem;min-width:560px;}
th{text-align:left;font-weight:700;font-size:.76rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding:.55em .7em;border-bottom:1.5px solid var(--ink);vertical-align:bottom;}
td{padding:.6em .7em;border-bottom:1px solid var(--rule);vertical-align:top;}
td.z,th.z{text-align:right;white-space:nowrap;}
tr.hervor td{background:var(--accent-soft);font-weight:600;}
.pos{color:var(--gain);font-weight:700;} .neg{color:var(--loss);font-weight:700;}

/* Einordnung */
aside.einordnung{background:var(--band);padding:18px 22px;margin:1.8em 0;font-size:.93rem;border-top:2px solid var(--muted);}
aside.einordnung .eyebrow{color:var(--muted);display:block;margin-bottom:.35em;}
aside.einordnung p:last-child{margin-bottom:0;}

.zitat{font-family:var(--serif);font-size:clamp(1.3rem,2.6vw,1.7rem);line-height:1.3;border-left:3px solid var(--accent);padding:.1em 0 .1em .9em;margin:1.6em 0;color:var(--ink);font-weight:500;}
.empfehlung{list-style:none;padding:0;margin:1em 0;counter-reset:e;}
.empfehlung li{counter-increment:e;display:grid;grid-template-columns:2.4em 1fr;gap:10px;padding:1em 0;border-top:1px solid var(--rule);}
.empfehlung li::before{content:counter(e);font-family:var(--serif);font-size:1.4rem;color:var(--accent);font-weight:600;line-height:1.1;}
.empfehlung li strong{display:block;}
.empfehlung li .wer{font-size:.82rem;color:var(--muted);display:block;margin-top:.3em;}
.fuss{font-size:.8rem;color:var(--muted);}

@media (max-width:520px){ body{font-size:15.5px;} .inhalt li{grid-template-columns:2.4em 1fr;} .inhalt li em{display:none;} }
@media (prefers-reduced-motion:reduce){ *{scroll-behavior:auto;} }
@page{size:A4;margin:14mm 15mm 16mm;}
@media print{
  body{background:#fff;font-size:9.4pt;line-height:1.5;}
  .titel{padding-block:8mm 0;}
  .titel h1{font-size:40pt;}
  .titel .unter{font-size:14pt;}
  .titel .meta{margin-top:1.6em;}
  .inhalt li{padding:.45em 0;}
  .kapkopf{padding-bottom:.7em;margin-bottom:1em;}
  .kapkopf h2{font-size:21pt;}
  .kern{font-size:11.5pt;margin-top:.6em;}
  h3{margin:1.3em 0 .45em;}
  figure{margin:1.3em 0;}
  .abbtitel{font-size:10.5pt;}
  aside.einordnung{margin:1.2em 0;padding:12px 16px;}
  .kernaussagen{margin:1em 0;}
  .kernaussagen li{padding:.6em 0;}
  .entscheidung{margin:1.2em 0;padding:14px 18px;}
  .empfehlung li{padding:.55em 0;}
  table{font-size:8.6pt;}
  #methode ul,#methode .fuss{font-size:8.4pt;}
  #methode h3{margin-top:1em;}
  .wrap{max-width:none;padding:0;}
  .blatt{border:0;margin:0;padding:0;break-before:page;}
  .blatt.titelblatt{break-before:auto;}
  figure,aside,table,.entscheidung{break-inside:avoid;}
  h3{break-after:avoid;}
  .chart svg{min-width:0;}
}
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400'
         '&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&display=swap">')

_abb = [0]
def abb(titel, unter, inhalt, quelle):
    _abb[0] += 1
    return (f'<figure><div class="abbkopf"><div class="eyebrow">Abbildung {_abb[0]}</div>'
            f'<div class="abbtitel">{titel}</div><div class="abbunter">{unter}</div></div>'
            f'{inhalt}<figcaption>{quelle}</figcaption></figure>')

def kapitel(nr, anker, titel, kern, rumpf):
    kopf = f'<div class="eyebrow">{"Kapitel " + str(nr) if nr else ("Zusammenfassung" if nr == "" else "Anhang")}</div>'
    return (f'<section class="blatt" id="{anker}"><div class="kapkopf">{kopf}<h2>{titel}</h2>'
            f'<p class="kern">{kern}</p></div>{rumpf}</section>')

def einordnung(titel, text):
    return f'<aside class="einordnung"><span class="eyebrow">{titel}</span>{text}</aside>'

TEILE = []

# ====================================================================== Titel
TEILE.append(f'''
<section class="blatt titelblatt titel">
<div class="eyebrow">HIGL-Verbund · Strategiepapier · September 2026</div>
<h1>Die Haftungswende</h1>
<p class="unter">Was Künstliche Intelligenz bis 2031 für Europa, Deutschland, das Gesundheitswesen und die Gesellschaften des HIGL-Verbunds bedeutet</p>
<div class="meta">
<div><b>Stand</b>26. September 2026</div>
<div><b>Grundlage</b>Szenariokonferenz, Sitzung D: 100 Fachrollen, 83 Urteile entlang der Kette</div>
<div><b>Ist-Werte</b>DATEV-Kontenblätter 2025</div>
<div><b>Für</b>Gesellschafterversammlung und Geschäftsführungen</div>
</div>
<div class="inhalt" style="margin-top:3em">
<div class="eyebrow">Inhalt</div>
<ol>
<li><span>·</span><a href="#blick">Auf einen Blick</a><em>Die Kernaussagen und die Entscheidung</em></li>
<li><span>1</span><a href="#europa">Europa</a><em>Der Gewinn kommt an, der Preis folgt ihm nicht</em></li>
<li><span>2</span><a href="#deutschland">Deutschland</a><em>Die Lohnsumme schrumpft nicht, sie verschiebt sich</em></li>
<li><span>3</span><a href="#gesundheit">Gesundheitswesen</a><em>Mehr Leistungen, schlechter bezahlt</em></li>
<li><span>4</span><a href="#pharma">Pharma und die USA</a><em>Der Zollfahrplan trifft auf den offenen Preis</em></li>
<li><span>5</span><a href="#evidenz">Der Markt für Evidenz</a><em>Rechnen wird billig, Einstehen wird knapp</em></li>
<li><span>6</span><a href="#higl">Die Gesellschaften des Verbunds</a><em>Achtzig Punkte Spreizung</em></li>
<li><span>7</span><a href="#entscheidung">Die Entscheidung</a><em>Ein Beschluss, drei Bausteine, fünf Fristen</em></li>
<li><span>A</span><a href="#methode">Methode, Grenzen, Quellen</a><em>Was die Zahlen hergeben und was nicht</em></li>
</ol>
<p class="fuss" style="margin-top:2em">Alle Werte für 2031 sind Ergebnisse einer Modellrechnung und stehen deshalb im Konjunktiv. Sie sind keine Prognosen. Gemessen sind nur die Ist-Werte 2025 aus den Buchungsdaten und die amtlichen Kennzahlen mit Quellenangabe.</p>
</div>
</section>
''')

# ====================================================================== Auf einen Blick
KETTE = kette([
    ("GESAMTWIRTSCHAFT", "1.790 Mrd. €", "beitragspflichtige|Entgelte 2031"),
    ("GKV", "420 Mrd. €", "Leistungsausgaben|+26,9 % ggü. 2025"),
    ("LEISTUNGSERBRINGER", "+13 %", "Vergütung je Einheit|real −4 bis −10 %"),
    ("ARZNEI, MEDIZINPRODUKTE", "140 Mrd. €", "Nachfrage 2031"),
    ("EVIDENZMARKT", "800 Mio. €", "extern beauftragt|550 bis 1.150"),
    ("HIGL-VERBUND", "+5 % / −15 %", "Umsatz / Deckungs-|beitrag, mit Entscheidung"),
], "Wirkungskette von der Gesamtwirtschaft bis zum HIGL-Verbund")

TEILE.append(kapitel("", "blick", "Auf einen Blick",
 "Künstliche Intelligenz macht die Arbeit des Verbunds billiger. Das ist 2031 nicht die gute Nachricht, sondern das Problem: Was billig wird, lässt sich nicht mehr teuer verkaufen. Bezahlt wird dann, wer für ein Ergebnis einsteht.",
 f'''
<ul class="kernaussagen">
<li><b>1</b><div><strong>Europa bekäme den Produktivitätsgewinn, aber nicht in voller Höhe als Preis.</strong><span>Das zugrunde liegende US-Modell rechnet mit freien Preisen. In Europa sind Gesundheitspreise administriert; in Deutschland spiegelten sich bei den Leistungserbringern nur {DURCHGRIFF["S2"]} Prozent eines Gewinns im Preis wider.</span></div></li>
<li><b>2</b><div><strong>Die Lohnsumme schrumpfte nicht, sie verschöbe sich.</strong><span>Die beitragspflichtigen Entgelte stiegen bis 2031 auf rund 1.790 Mrd. €. Der KI-Effekt darin wäre mit rund 10 Mrd. € die kleinste bezifferte Bewegung.</span></div></li>
<li><b>3</b><div><strong>Die GKV gäbe mehr aus und zahlte je Leistung schlechter.</strong><span>Die Leistungsausgaben stiegen um knapp 27 Prozent auf 420 Mrd. €, das Vergütungsniveau je Einheit nur um 13 Prozent. Der Einkauf würde härter, nicht weicher.</span></div></li>
<li><b>4</b><div><strong>Die US-Pharmapolitik wirkte auf den Verbund eher positiv.</strong><span>{US_POS} von 18 Fachurteilen sehen einen positiven Effekt auf die Evidenznachfrage, im Median {de(US_MEDIAN,0,vz=True)} Prozent: Wer Preise gegenüber den USA verteidigen muss, braucht Daten aus Deutschland.</span></div></li>
<li><b>5</b><div><strong>Der Wert verschöbe sich vom Rechnen zum Einstehen.</strong><span>Der Anteil der beschreibenden Leistung fiele von rund 70 auf 32 Prozent, der Anteil der haftenden stiege von 30 auf 68 Prozent.</span></div></li>
<li><b>6</b><div><strong>Die Gesellschaften liefen auseinander.</strong><span>WIG2 und GREENBAY Software gewännen je rund 20 Prozent, 4K ANALYTICS verlöre 10, CLINIBOTS 60. Der Verbundwert von plus 5 Prozent beschreibt keine einzige Gesellschaft.</span></div></li>
<li><b>7</b><div><strong>Knapp wäre nicht die Technik, sondern die Haftung.</strong><span>Sieben von zwölf Fachurteilen aus dem Verbund nennen sie als bindendes Hemmnis. Keines bezeichnet die dafür nötige Versicherungsdeckung als verfügbar.</span></div></li>
</ul>

<div class="entscheidung">
<div class="eyebrow">Die Entscheidung</div>
<h3>Bis zum 30. Juni 2028 wäre zu beschließen, ob der Verbund die Haftung für seine Analyseergebnisse übernimmt.</h3>
<p>Versichert, vertraglich zugesichert, mit einem Abnahmeverfahren dahinter. Der Beschluss ist binär. Zwischenmarke ist der 31. Dezember 2027: eine schriftliche Vorabstimmung mit mindestens einem Berufshaftpflichtversicherer. Wird sie gerissen, wäre negativ zu entscheiden und nicht zu verschieben.</p>
<div class="zahlen">
<div><b>+5 %</b><span>Umsatz 2031 mit Entscheidung</span></div>
<div><b>−30 %</b><span>Umsatz 2031 ohne Entscheidung</span></div>
<div><b>5,1 Mio. €</b><span>Abstand beim Außenumsatz</span></div>
<div><b>45 Punkte</b><span>Abstand beim Deckungsbeitrag</span></div>
</div>
</div>
''' + abb("Die Kette: Von der Gesamtwirtschaft bis zum Verbund wird aus einem Produktivitätsgewinn ein Margenproblem",
          "Zentralwerte 2031 je Glied der Wirkungskette",
          KETTE,
          "Quelle: Szenariokonferenz Sitzung D, Übergabewerte Ü0 bis Ü4; Basis 2025: GKV-Statistik KV45 und KJ1, DATEV-Kontenblätter des Verbunds. Umsatzangabe bezogen auf 14,48 Mio. € Außenumsatz 2025.")))

# ====================================================================== Kapitel 1 Europa
SZEN_TAB = '''<div class="tabelle"><table>
<thead><tr><th>Szenario (US-Modell, bis 2030)</th><th class="z">BIP ggü. Basis</th><th class="z">Wachstum p.a.</th><th class="z">Lohnquote</th><th>Wahl in der Kette</th></tr></thead>
<tbody>
<tr><td>Basis ohne transformative KI</td><td class="z">—</td><td class="z">rund 2 %</td><td class="z">rund 60 %</td><td>—</td></tr>
<tr><td><em>modest</em></td><td class="z">gering</td><td class="z">knapp über Basis</td><td class="z">knapp unter 60 %</td><td>''' + str(SZEN["modest"]) + ''' von ''' + str(N_KETTE) + '''</td></tr>
<tr class="hervor"><td><em>substantial</em></td><td class="z">+8,3 %</td><td class="z">5,4 %</td><td class="z">rund 56 %</td><td>''' + str(SZEN["substantial"]) + ''' von ''' + str(N_KETTE) + '''</td></tr>
<tr><td><em>extreme</em></td><td class="z">+32 %</td><td class="z">15 %</td><td class="z">rund 45 %</td><td>''' + str(SZEN["extreme"]) + ''' von ''' + str(N_KETTE) + '''</td></tr>
</tbody></table></div>'''

BRUECHE = '''<div class="tabelle"><table>
<thead><tr><th>Übertragungsbruch</th><th>Was das US-Modell annimmt</th><th>Was in Europa gilt</th><th class="z">Kennzahl</th></tr></thead>
<tbody>
<tr><td><strong>Preis</strong></td><td>Ein Produktivitätsgewinn senkt den Preis oder erhöht die Marge, je nach Wettbewerb.</td><td>Gesundheitspreise folgen Budgetformeln, Fallpauschalen und Verhandlungsterminen.</td><td class="z">''' + str(DURCHGRIFF["S2"]) + ''' % statt ''' + str(DURCHGRIFF["S0"]) + ''' %</td></tr>
<tr><td><strong>Zeit</strong></td><td>Anpassung, sobald die Technik es erlaubt.</td><td>Tarifrunden, Kündigungsschutz, Vergabeverfahren und Haushaltsjahre verzögern.</td><td class="z">3 Jahre</td></tr>
<tr><td><strong>Haftung</strong></td><td>Kein eigener Kostenblock.</td><td>KI-Verordnung, Medizinprodukterecht und Berufsrecht verlangen einen, der einsteht.</td><td class="z">7 von 12</td></tr>
<tr><td><strong>Ort</strong></td><td>Der Gewinn bleibt in der Volkswirtschaft.</td><td>Modelle und Rechenzentren liegen überwiegend außerhalb Europas; ein Teil der Wertschöpfung fließt ab.</td><td class="z">55 % Verbleib</td></tr>
</tbody></table></div>'''

EUROPA = hbalken([
    ("Frankreich", 70, "T2A-Fallpauschalen, ONDAM-Deckel"),
    ("Niederlande", 55, "Versicherer kaufen selektiv ein"),
    ("Deutschland, Gesamtwirtschaft", DURCHGRIFF["S0"], "Station 0"),
    ("EU-Gesundheitsdatenraum", 35, "Durchsatz der Zugangsstellen"),
    ("KI-Verordnung", 25, "fehlende harmonisierte Normen"),
    ("Estland", 20, "Haftung nach Art. 14 KI-VO"),
    ("Vereinigtes Königreich", 20, "Effizienzabschlag, nachlaufend"),
    ("EU-Arzneimittelpaket", 20, "Unterlagenschutz, Verfahrensdauer"),
    ("Dänemark", 15, "steuerfinanziert, Wartezeitgarantie"),
    ("Deutschland, Leistungserbringer", DURCHGRIFF["S2"], "Station 2"),
], 80, " %", "Preisdurchgriff im europäischen Vergleich", links=300,
   hervor={"Deutschland, Leistungserbringer", "Deutschland, Gesamtwirtschaft"})

TEILE.append(kapitel(1, "europa", "Der Produktivitätsgewinn käme nach Europa, der Preis folgte ihm nicht",
 "Das Modell, auf dem diese Arbeit aufsetzt, beschreibt die USA. Seine Mechanik ließe sich übertragen, seine Preisbildung nicht. An vier Stellen bricht die Übertragung, und jede davon verschiebt, wer vom Gewinn profitiert.",
 f'''<div class="prose">
<h3>Der Ausgangspunkt: drei Szenarien, keines davon eine Prognose</h3>
<p>Die Studie <em>Economic Scenarios for Transformative AI</em> (Korinek, Jones, Sacher, Cotter und McCrory, Working Paper 2026-02) rechnet für die USA drei Pfade bis 2030. Im mittleren, <em>substantial</em> genannten Pfad läge das Bruttoinlandsprodukt 2030 um 8,3 Prozent über dem Pfad ohne transformative KI, das Wachstum bei 5,4 statt rund 2 Prozent im Jahr. Im extremen Pfad wären es 32 Prozent und 15 Prozent Wachstum. Die Lohnquote fiele von rund 60 auf 56 Prozent, im extremen Fall auf 45.</p>
<p>Zwei Befunde der Studie sind für alles Weitere wichtig. Erstens: Die Löhne kognitiver Berufe fielen im mittleren Pfad leicht, um 0,3 Prozent, die der übrigen Berufe stiegen um 5,9 Prozent. Die Studie beschreibt also keinen Arbeitsplatzabbau, sondern eine Umschichtung zu den Tätigkeiten, die KI nicht übernimmt. Zweitens: Die Pfade liefen bis 2027 fast gleich und trennten sich erst danach. Wer heute entscheiden muss, kann nicht abwarten, welcher Pfad eintritt.</p>
<p>Die Autoren bezeichnen ihre Szenarien ausdrücklich als <em>not predictions</em> und ordnen ihnen keine Wahrscheinlichkeiten zu. Die Fachurteile dieser Arbeit haben trotzdem fast einhellig den mittleren Pfad gewählt.</p>
</div>
''' + abb(f"{SZEN['substantial']} von {N_KETTE} Fachurteilen wählten den mittleren Pfad: die Kette rechnet faktisch mit einem einzigen Szenario",
          "Szenarien der Studie für die USA und ihre Wahl in der Kette",
          SZEN_TAB,
          "Quelle: Korinek u. a., Economic Scenarios for Transformative AI, WP 2026-02; Szenariowahl der 83 Kettenurteile aus Sitzung D (Stationen 0 bis 4). Die einzige empirische Verankerung des mittleren Pfads ist die Medianantwort einer Befragung von 10.980 US-Erwachsenen (Morning Consult, August 2026).") +
 f'''<div class="prose">
<h3>Vier Brüche zwischen dem US-Modell und Europa</h3>
<p>Das Modell kennt nach eigener Grenzenliste keine Preisrigiditäten, keine Haushaltsjahre, keine gedeckelten Kostenzeilen und keine Politökonomie. Genau diese Dinge bestimmen aber, wie ein Produktivitätsgewinn im europäischen Gesundheitswesen ankommt. Die Fachurteile aller Stationen laufen unabhängig voneinander auf dieselben vier Brüche hinaus.</p>
</div>
''' + abb("Das Modell rechnet mit freien Preisen, sofortiger Anpassung, ohne Haftung und ohne Abfluss. Keine der vier Annahmen trägt in Europa",
          "Übertragungsbrüche zwischen US-Modell und europäischem Gesundheitswesen",
          BRUECHE,
          "Quelle: Sitzung D, Mediane D2 (Preisdurchgriff) und D4 (Verzögerung) je Station; Hemmnisangaben Station 4; EU-Verbleib der Wertschöpfung aus dem Bestand, Teil 2 § 3 (18 Urteile, Quartile 42 und 68 Prozent).") +
 f'''<div class="prose">
<p><strong>Der Preisbruch ist der wichtigste.</strong> Die Kennzahl dafür heißt Preisdurchgriff: Welcher Anteil eines Produktivitätsgewinns spiegelt sich im Preis wider? In der deutschen Gesamtwirtschaft läge er bei {DURCHGRIFF["S0"]} Prozent. Bei den Leistungserbringern, also Krankenhäusern, Praxen und Pflege, läge er bei {DURCHGRIFF["S2"]} Prozent. Der Preis folgt dort nicht der Produktivität, sondern der Budgetformel. Ein Krankenhaus, das mit KI günstiger dokumentiert, bekommt dafür nicht weniger und nicht mehr Geld; es bekommt dasselbe, und die Ersparnis bleibt im Haus oder deckt andere Kosten.</p>
<p><strong>Europa ist dabei kein einheitlicher Raum.</strong> Wo Preise über Fallpauschalen und einen nationalen Ausgabendeckel gesteuert werden, wie in Frankreich, holt der Staat einen Effizienzgewinn in ein bis zwei Tarifrunden zurück: Der Durchgriff läge bei 70 Prozent, allerdings zu Gunsten des Kostenträgers, nicht des Patienten. In den Niederlanden kaufen Versicherer selektiv ein, der Wert läge bei 55 Prozent. In steuerfinanzierten Systemen wie Dänemark und dem Vereinigten Königreich versickerte der Gewinn dagegen in Wartezeiten und Budgetmechanik; dort lägen die Werte bei 15 und 20 Prozent.</p>
</div>
''' + abb(f"Deutschland stünde mit {DURCHGRIFF['S2']} Prozent am unteren Rand: Ein Effizienzgewinn im Krankenhaus kommt beim Preis kaum an",
          "Anteil eines Produktivitätsgewinns, der sich 2031 im Preis widerspiegelte, Median in Prozent",
          EUROPA,
          "Quelle: Sitzung D, Europabank (Urteile EU-01 bis EU-08) und Mediane D2 der Stationen 0 und 2. Länderwerte je ein Fachurteil, daher als Richtung zu lesen, nicht als Messung.") +
 f'''<div class="prose">
<h3>Die Regeln, die 2027 bis 2031 zählen</h3>
<p><strong>Die KI-Verordnung</strong> (VO (EU) 2024/1689) wäre der größte einzelne Bremsfaktor, nicht weil sie verbietet, sondern weil sie verlangt, was es noch nicht gibt. Die Pflichten für Hochrisikosysteme setzen harmonisierte Normen zu Artikel 8 bis 15 voraus, die bislang fehlen. Der Geltungsbeginn für die Hochrisikofälle aus Anhang III ist in den Fachurteilen selbst strittig: Zehn datieren ihn auf den 2. Dezember 2027, zwei auf den 2. August 2028. Das deutsche Durchführungsgesetz ist seit dem 29. Juli 2026 in Kraft.</p>
<p><strong>Der Europäische Gesundheitsdatenraum</strong> öffnete ab März 2031 die zweite Tranche der Sekundärnutzung, mit Bildgebung, Laborwerten, Entlassbriefen und Genomdaten. Das wäre das größte Nachfrageereignis des Horizonts für jeden, der mit Gesundheitsdaten arbeitet. Engpass wäre nicht der Zugang auf dem Papier, sondern der Bescheidungsdurchsatz der Zugangsstellen.</p>
<p><strong>Die Wettbewerbsfähigkeit Europas</strong> bleibt das Hintergrundthema. Der Draghi-Bericht zählt unter den fünfzig größten Technologieunternehmen der Welt vier europäische. Für die Wertschöpfung heißt das: Rund 55 Prozent eines KI-Effizienzgewinns im Gesundheitswesen verblieben nach den Fachurteilen in der EU, die Spanne reicht von 42 bis 68 Prozent. Der Rest ginge an die Anbieter der Modelle und der Rechenleistung.</p>
</div>
''' + einordnung("Was das für den Verbund heißt",
 "<p>Der Verbund verkauft in einen der Märkte, in denen der Preis am wenigsten der Produktivität folgt. Er kann dort mit KI billiger produzieren, bekäme dafür aber nicht mehr Geld. Umgekehrt steht er in seinem eigenen Markt im Wettbewerb, und dort würde der Gewinn weitergereicht (Kapitel 5).</p>")))

# ====================================================================== Kapitel 2 Deutschland
LOHNQUOTE = hbalken([
    ("Basis ohne transformative KI", 60, "US-Modell"),
    ("substantial", 56, f"{SZEN['substantial']} von {N_KETTE} Urteilen"),
    ("extreme", 45, f"{SZEN['extreme']} von {N_KETTE} Urteilen"),
], 80, " %", "Lohnquote je Szenario", links=280, hervor={"substantial"})

MECHANIK = hbalken([
    ("Zuwachs 2025 bis 2031 insgesamt", 240, "1.550 auf 1.790 Mrd. €, 2,4 % p. a."),
    ("Anhebung Bemessungsgrenze 2027", 18.5, "verkündetes Recht, 15 bis 22"),
    ("Jahresscheibe 2030 auf 2031", 42, "36 bis 50, jenseits des Modells"),
    ("KI-Effekt", 10, "vier Urteile, 0,56 % des Werts"),
], 320, " Mrd. €", "Rechtsmechanik gegen KI-Effekt", links=300, hervor={"KI-Effekt"}, d=0)

E3_ZEILEN = ["Gesamtwirtschaft", "GKV und PKV", "Leistungserbringer", "Pharma und USA", "HIGL-Verbund"]
E3_WERTE = [E3[s] for s in ("S0", "S1", "S2", "S3", "S4")]
WAERME = waermefeld(E3_ZEILEN, ["Kapital", "Kunden", "Beschäftigte", "Staat"], E3_WERTE,
                    "Verteilung des Effizienzgewinns je Station", vmax=40)

TEILE.append(kapitel(2, "deutschland", "Die Lohnsumme schrumpfte nicht, sie verschöbe sich",
 "Für die Finanzierung des Gesundheitswesens zählt nicht das Bruttoinlandsprodukt, sondern die beitragspflichtige Lohnsumme. Sie stiege bis 2031 weiter, getragen von Recht und Fortschreibung. Die KI verändert, wer sie verdient, kaum, wie viel.",
 f'''<div class="prose">
<h3>Die Beitragsbasis wüchse, und fast nichts davon käme aus der KI</h3>
<p>Die beitragspflichtigen Arbeitsentgelte der GKV-Mitglieder lagen 2025 bei 1.550 Mrd. €. Bis 2031 stiegen sie auf rund 1.790 Mrd. € (Spanne 1.680 bis 1.930), in der Abgrenzung ohne Renten. Das entspräche 2,4 Prozent im Jahr. Die Faktoren dafür sind das Entgelt je Beschäftigtem, die Beschäftigungsentwicklung und die Beitragsbemessungsgrenze. Keiner davon ist eine Größe des KI-Modells.</p>
<p>Den KI-Effekt beziffern vier Fachurteile unabhängig gegen einen Pfad ohne KI. Er läge bei rund 10 Mrd. €, 0,56 Prozent des Werts. Allein die Anhebung der Bemessungsgrenze zum 1. Januar 2027 bewegte mit 15 bis 22 Mrd. € ungefähr das Doppelte. Die Aussage »das Modell ergibt für Deutschland 1.790 Mrd. €« wäre deshalb falsch. Richtig ist: Die deutsche Rechts- und Fortschreibungsmechanik ergibt 1.790 Mrd. €, und der KI-Effekt ist darin die kleinste Bewegung.</p>
</div>
''' + abb("Der KI-Effekt auf die Beitragsbasis wäre die kleinste der bezifferten Bewegungen",
          "Bewegungen der beitragspflichtigen Entgelte bis 2031, Mrd. €",
          MECHANIK,
          "Quelle: Sitzung D, Station 0 und Übergabe Ü0; Basis KV45 2025: 1.550,0 Mrd. €. Anhebung der Bemessungsgrenze: Mitte der Spanne 15 bis 22 Mrd. € aus zehn Urteilen. KI-Effekt: vier Urteile gegen einen Referenzpfad ohne KI.") +
 f'''<div class="prose">
<h3>Umschichtung statt Abbau</h3>
<p>Das Institut für Arbeitsmarkt- und Berufsforschung rechnet im KI-Szenario mit dem Wegfall oder der Neuentstehung von rund 1,6 Millionen Stellen in fünfzehn Jahren. Schon die Kurzfristprognose vom März 2026 ist zweigeteilt: minus 140.000 Beschäftigte in der Industrie, plus 180.000 in öffentlichen Diensten, Erziehung und Gesundheit. In der ifo-Umfrage unter rund 3.000 KI-nutzenden Unternehmen erwartet etwa die Hälfte über fünf Jahre sinkende Löhne für Berufseinsteiger. Die Bundesregierung sieht nach eigener Antwort vom August 2026 »keine belastbaren Hinweise« auf einen systematischen KI-bedingten Beschäftigungsabbau.</p>
<p>Das Bild passt zur Lohnkomposition des US-Modells: Unter dem kognitiven Druck stünden die Einstiegsstufen der Wissensberufe, gewinnen würden die Tätigkeiten, bei denen Menschen körperlich, räumlich oder persönlich präsent sein müssen. Im deutschen Gesundheitswesen ist das der größere Teil der Beschäftigung. Der Anteil physisch gebundener Tätigkeit läge bei den Leistungserbringern bei {de(med("S2","d1_physisch"))} Prozent, in der Gesamtwirtschaft bei {de(med("S0","d1_physisch"))} Prozent.</p>
</div>
''' + abb("Die Lohnquote fiele, aber im gewählten Pfad nur um vier Punkte",
          "Anteil der Arbeitseinkommen am Volkseinkommen 2030 je Szenario, US-Modell",
          LOHNQUOTE,
          "Quelle: Korinek u. a., WP 2026-02. Die Lohnquote verlässt die Kette ohne verwendbaren Kanal zur deutschen Beitragsbasis und ist deshalb nur als Plausibilitätsaussage zu lesen.") +
 f'''<div class="prose">
<h3>Wer den Effizienzgewinn bekäme</h3>
<p>Jedes Fachurteil hat angegeben, wie sich ein Effizienzgewinn in seinem Feld auf Kapital, Kunden, Beschäftigte und Staat verteilte. Das Muster ist deutlicher als jede Einzelzahl. In der Gesamtwirtschaft teilten sich Kapital und Kunden den Gewinn etwa hälftig. Bei den Kassen ginge ein gutes Drittel an den Staat, weil Beitragssätze, Zuschüsse und Aufsicht ihn abschöpfen. Im Markt des Verbunds läge der Kundenanteil mit {E3["S4"][1]} Prozent am höchsten: Wer im Wettbewerb anbietet, gibt den Gewinn an den Kunden weiter.</p>
</div>
''' + abb(f"Im Markt des Verbunds bekämen die Kunden mit {E3['S4'][1]} Prozent den größten Anteil des Effizienzgewinns",
          "Verteilung eines Effizienzgewinns 2031, Median je Station in Prozent",
          WAERME,
          "Quelle: Sitzung D, Frage E3 in allen 83 Kettenurteilen; je Urteil summieren sich die vier Anteile auf 100. Die Mediane summieren sich je Zeile nicht zwingend auf 100.")))

# ====================================================================== Kapitel 3 Gesundheitswesen
GKV = gruppen([
    ("Ausgabenvolumen", [26.9]),
    ("Vergütung je Einheit", [13]),
    ("Kosten der Erbringer", [22]),
    ("Vergütung real", [-7]),
], [("Veränderung 2031 gegenüber 2025", "f-accent")], -20, 40,
   "Ausgabenvolumen, Vergütung und Kosten der GKV 2031", " %")

KETTE_DG = hbalken([
    ("Gesamtwirtschaft", DURCHGRIFF["S0"], "Station 0"),
    ("GKV und PKV", DURCHGRIFF["S1"], "Station 1"),
    ("Leistungserbringer", DURCHGRIFF["S2"], "Station 2"),
    ("Pharma und USA", DURCHGRIFF["S3"], "Station 3"),
    ("HIGL-Verbund, eigener Markt", DURCHGRIFF["S4"], "Station 4"),
], 80, " %", "Preisdurchgriff je Station", links=300, hervor={"Leistungserbringer", "HIGL-Verbund, eigener Markt"})

TEILE.append(kapitel(3, "gesundheit", "Mehr Leistungen, schlechter bezahlt",
 "Die gesetzliche Krankenversicherung gäbe 2031 deutlich mehr aus als heute. Beim einzelnen Krankenhaus, der einzelnen Praxis käme davon weniger an als die Kosten stiegen. Für Anbieter von Analyse heißt das: Die Kunden hätten mehr Arbeit und weniger Spielraum.",
 f'''<div class="prose">
<h3>Die GKV: Volumen wächst, Preis hält nicht mit</h3>
<p>Die Leistungsausgaben der GKV lagen 2025 bei gemessenen 331,1 Mrd. €. Bis 2031 stiegen sie auf rund 420 Mrd. €, ein Plus von 26,9 Prozent; mit Verwaltung und sonstigen Ausgaben wären es rund 436 Mrd. €. Das Wachstum käme aus Alter, Morbidität und Menge. Das Vergütungsniveau je Leistungseinheit stiege im selben Zeitraum nur um 13 Prozent, nach der zweiten zulässigen Lesart des § 71 Abs. 3 SGB V um 16 Prozent (Spanne +8 bis +20).</p>
<p>Gegen die Kostenentwicklung der Leistungserbringer, die in den Fachurteilen implizit bei plus 18 bis 26 Prozent läge, wäre das real ein Minus von 4 bis 10 Prozent je Einheit. Die beiden Lesarten unterscheiden sich allein darin, welche Grundlohnrate zählt: 2,4 Prozent im Jahr auf die gesamte Entgeltmasse oder 2,7 Prozent je Mitglied nach dem Wortlaut des Gesetzes.</p>
<p>Der steuerfinanzierte Anteil fiele. Die Bundesmittel entsprachen 2025 noch 4,8 Prozent der Leistungsausgaben, 2031 wären es bei nominal nahezu eingefrorenem Zuschuss rund 3,7 Prozent. Jeder Euro wäre damit stärker beitragsfinanziert als heute. Die Finanzreserven der Kassen lagen Ende 2025 bei 5,1 Mrd. €, das sind 0,18 Monatsausgaben. Spielraum für Investitionen, die sich erst im dritten Jahr rechneten, hätten die Kassen damit kaum, zumal ihre Verwaltungskosten ab 2027 an den Einnahmenzuwachs gebunden wären.</p>
</div>
''' + abb("Das Volumen stiege doppelt so schnell wie der Preis je Leistung; real verlöre jede Einheit an Wert",
          "Veränderung 2031 gegenüber 2025 in Prozent, Zentralwerte",
          GKV,
          "Quelle: Sitzung D, Übergabe Ü1 (420 Mrd. € gegen 331,062 Mrd. € KJ1 2025) und Stationen 1 und 2. Kosten der Erbringer: Mitte der implizierten Spanne +18 bis +26 Prozent; Vergütung real: Mitte der Spanne −4 bis −10 Prozent.") +
 f'''<div class="prose">
<h3>Die private Krankenversicherung: stabil im Bestand, teuer im Beitrag</h3>
<p>Die PKV zählte 2025 rund 8,79 Millionen Vollversicherte, 0,5 Prozent mehr als im Vorjahr. Zum 1. Januar 2026 stiegen die Beiträge im Schnitt um 12,6 Prozent, für 81 Prozent der Versicherten; im Jahr davor waren es 13,9 Prozent. Die Alterungsrückstellungen wuchsen auf 355,4 Mrd. €. Größter Kostentreiber waren die Pflegekosten im Krankenhaus mit plus 17,6 Prozent. Die PKV hätte damit einen stärkeren Anreiz als die GKV, Effizienzgewinne tatsächlich zu heben, aber einen kleineren Hebel: Sie verhandelt keine Krankenhauspreise.</p>

<h3>Die Krankenhäuser: eine Reform, die bis 2030 budgetneutral läuft</h3>
<p>Das Krankenhausreformanpassungsgesetz ist seit dem 15. April 2026 in Kraft. Es ordnet die Versorgung in 61 Leistungsgruppen und führt eine Vorhaltevergütung ein, die 2026 und 2027 budgetneutral läuft, 2028 und 2029 konvergiert und erst ab 2030 voll wirkt. Das Institut für das Entgeltsystem rechnet für die Jahre 2026 bis 2029 mit den Daten von 2024.</p>
<p>Für die Frage dieses Papiers ist das entscheidend: Bis 2030 gäbe es für ein Krankenhaus kaum einen Weg, einen KI-Effizienzgewinn in höhere Erlöse zu übersetzen. Der Gewinn bliebe als Kostenentlastung im Haus. Genau deshalb läge der Preisdurchgriff bei den Leistungserbringern mit {DURCHGRIFF["S2"]} Prozent am tiefsten in der ganzen Kette.</p>
</div>
''' + abb(f"Der Preis folgte der Produktivität nur dort, wo Wettbewerb herrscht: im Markt des Verbunds mit {DURCHGRIFF['S4']} Prozent",
          "Preisdurchgriff 2031 je Station der Kette, Median in Prozent",
          KETTE_DG,
          "Quelle: Sitzung D, Frage D2 in allen 83 Kettenurteilen, Median je Station. Die Verzögerung bis zur Wirkung (D4) läge in allen fünf Stationen bei drei Jahren.") +
 einordnung("Was das für den Verbund heißt",
 "<p>Die Kunden des Verbunds, Kassen, Krankenhäuser und Hersteller, hätten 2031 mehr Fälle, knappere Budgets und strengere Nachweispflichten. Sie kauften weniger Auswertung als Selbstzweck und mehr Ergebnisse, auf die sie sich vor Aufsicht, Schiedsstelle oder Gericht berufen können.</p>")))

# ====================================================================== Kapitel 4 Pharma und USA
ZOLL = zeitstrahl([
    (2026.25, "2. Apr. 2026", "Proklamation 11020", "intern", 3, "start"),
    (2026.58, "31. Juli 2026", "Zoll für 17 Unternehmen", "intern", 2, "start"),
    (2026.74, "29. Sept. 2026", "Zoll für alle übrigen", "intern", 1, "start"),
    (2027.0, "Jan. 2027", "GUARD, Medicare Part D", "intern", 0, "start"),
    (2029.05, "20. Jan. 2029", "Ende des Nullsatzes", "intern", 0, "start"),
    (2030.25, "2. Apr. 2030", "Onshoring-Satz 100 %", "intern", 1, "end"),
    (2027.5, "30. Juni 2027", "Frist Referentenentwurf", "extern", 0, "start"),
    (2028.5, "30. Juni 2028", "§ 130b Abs. 1c läuft aus", "extern", 0, "start"),
], 2026, 2030.8, "Zeitplan der US-Arzneimittelpolitik und der deutschen Weiche", achse=170)

US_WOLKE = punktwolke(US_EFFEKT, -15, 30, US_MEDIAN, "Isolierter US-Effekt je Fachurteil", schritt=5)

TEILE.append(kapitel(4, "pharma", "Der Zollfahrplan träfe auf den einzigen offenen Preis Europas",
 "Die amerikanische Arzneimittelpolitik drückt auf die Margen der Hersteller. Zugleich macht sie den deutschen Erstattungsbetrag zur Referenz für den größten Markt der Welt. Für Anbieter von Evidenz überwöge nach den Fachurteilen der zweite Effekt.",
 f'''<div class="prose">
<h3>Was in Washington beschlossen ist</h3>
<p>Mit der Proklamation 11020 vom 2. April 2026 hat die US-Regierung Zölle auf patentgeschützte Arzneimittel nach Section 232 eingeführt. Der Grundsatz liegt bei 100 Prozent, für Erzeugnisse aus der EU bei 15 Prozent, aus dem Vereinigten Königreich bei 10 Prozent. Für 17 namentlich genannte Unternehmen gilt der Zoll seit dem 31. Juli 2026, für alle übrigen ab dem 29. September 2026. Wer eine Meistbegünstigungsvereinbarung geschlossen und Produktion in die USA verlegt hat, zahlt bis zum 20. Januar 2029 null; wer nur verlagert, zahlt 20 Prozent, ab dem 2. April 2030 den vollen Satz. Generika sind ausgenommen, ausdrücklich nur »at this time«, mit einer Überprüfung binnen eines Jahres.</p>
<p>Daneben stehen 26 Meistbegünstigungsvereinbarungen mit Herstellern, die rund 89 Prozent des Markts für Markenarzneimittel abdecken, und drei Erstattungsmodelle: GENEROUS für Medicaid seit Januar 2026, GLOBE für Medicare Part B, angekündigt für Oktober 2026 (eine endgültige Regel war zum Stand dieses Papiers nicht auffindbar), und GUARD für Medicare Part D ab Januar 2027.</p>

<h3>Warum Deutschland dabei eine Sonderrolle hat</h3>
<p>Meistbegünstigung heißt: Der amerikanische Preis orientiert sich an den Preisen anderer Länder. Deutschland ist in beiden amerikanischen Referenzkörben enthalten und das einzige große EU-Land, dessen verhandelte Nettopreise öffentlich sind. Der Erstattungsbetrag nach § 130b SGB V gilt ab dem siebten Monat bundesweit einheitlich. Jeder Euro, den ein Hersteller in Deutschland nachgibt, kostete ihn damit potenziell auch in den USA.</p>
<p>Die Vertraulichkeitsoption nach § 130b Abs. 1c SGB V, die einen nicht öffentlichen Erstattungsbetrag erlaubt, läuft am 30. Juni 2028 aus, wenn der Gesetzgeber nicht handelt. Ohne Referentenentwurf bis zum 30. Juni 2027 wäre das Auslaufen praktisch entschieden. Die Fachurteile schätzen diese Unterlassung als den wahrscheinlicheren Ausgang ein, mit rund 65 Prozent. Sieben von achtzehn nennen genau diese Weiche als die Entscheidung, die ihren Wert am stärksten bewegt.</p>
</div>
''' + abb("Zwischen 2026 und 2030 verschärfte sich der US-Druck in sechs Stufen; die deutsche Weiche fiele dazwischen, im Juni 2028",
          "Oben: US-Rechtsstand; unten: deutsche Frist",
          ZOLL,
          "Quelle: Proclamation 11020 (Federal Register 2026-06956); Faktenblatt N01 der Sitzung D; § 130b Abs. 1c SGB V. Frist Referentenentwurf rückwärts gerechnet aus dem Gesetzgebungstakt.") +
 f'''<div class="prose">
<h3>Mehr Preisdruck, mehr Nachfrage nach Evidenz</h3>
<p>Das Vorzeichen läuft der Erwartung zuwider. Derselbe Vorgang, der den Preis unter Druck setzt, erhöhte die Zahlungsbereitschaft für die Analyse, die ihn verteidigt. {US_POS} der 18 Fachurteile der Pharmastation sehen einen positiven Effekt auf das Volumen des deutschen Evidenzmarkts, vier einen negativen. Der Median läge bei {de(US_MEDIAN,0,vz=True)} Prozent, in Euro bei rund 65 Mio.</p>
<p>Die Urteile nennen vier Kanäle. Der stärkste wirkt nach oben: Wer einen Erstattungsbetrag verhandelt, der zugleich Referenzpreis für die USA ist, investiert mehr in die Begründung. Nach oben wirken auch die Vertraulichkeitsoption, die eine Forschungsabteilung in Deutschland voraussetzt, und der Nachweis des Wirkstoffursprungs, den die Proklamation zu einer Geldgröße macht. Nach unten wirkt die Marge: Ein Hersteller mit sinkendem US-Ergebnis kürzt zuerst die Stäbe ohne eigenen Erlös, und dazu gehören Evidenzabteilungen.</p>
<p><strong>Gesichert ist das Vorzeichen nicht.</strong> Sieben der achtzehn Urteile führen ein Intervall, das die Null einschließt. Und in drei Segmenten wirkte der Schock gegenwärtig gar nicht: bei Generika, bei Medizinprodukten und bei digitalen Gesundheitsanwendungen. Der US-Effekt ist damit kein Niveaueffekt, sondern ein Spaltungsverstärker: Er stärkt die Anbieter, die Preise im Nutzenbewertungsverfahren verteidigen helfen, und schwächt die, deren Leistung ein Kostenblock beim Hersteller ist.</p>
</div>
''' + abb(f"{US_POS} von 18 Urteilen sähen einen positiven US-Effekt auf die Nachfrage nach Evidenz, im Median {de(US_MEDIAN,0,vz=True)} Prozent",
          "Isolierter Effekt der US-Arzneimittelpolitik auf das Volumen des deutschen Evidenzmarkts 2031, je Fachurteil in Prozent",
          US_WOLKE,
          "Quelle: Sitzung D, Station 3, Urteile S3-01 bis S3-18; Differenz zwischen dem Wert mit und ohne US-Politik, bezogen auf den Wert ohne. Median der Eurodifferenzen +65 Mio. €, Mittel +50 Mio. €.") +
 einordnung("Was das für den Verbund heißt",
 "<p>Die Nutzenbewertung wird für Hersteller wichtiger, nicht unwichtiger. Wer dort mit belastbarer Evidenz aus deutschen Versorgungsdaten auftreten kann, gewönne. Dafür müsste diese Evidenz aber im Verfahren nach § 35a SGB V verwendbar sein, und genau dafür fehlt bislang eine Anerkennungsregel für maschinell erzeugte Ergebnisse. Acht der achtzehn Urteile nennen diese fehlende Regel als bindendes Hemmnis.</p>")))

# ====================================================================== Kapitel 5 Evidenzmarkt
WERT = gestapelt([
    ("2025", [(70, "beschreibend", "f-accent2"), (30, "haftend", "f-accent")]),
    ("2031", [(32, "beschreibend", "f-accent2"), (68, "haftend", "f-accent")]),
], "Wertanteile beschreibender und haftender Leistung")

MARKT = '''<div class="tabelle"><table>
<thead><tr><th>Größe 2031</th><th class="z">Zentralwert</th><th class="z">80-%-Intervall</th><th>Lesart</th></tr></thead>
<tbody>
<tr class="hervor"><td>Extern beauftragte Evidenz und Analytik, Deutschland</td><td class="z">800 Mio. €</td><td class="z">550 bis 1.150</td><td>auf 50 Mio. € genau zu lesen</td></tr>
<tr><td>Preisindex je Leistungseinheit (2025 = 100)</td><td class="z">75</td><td class="z">55 bis 95</td><td>ein Viertel billiger</td></tr>
<tr><td>Mengenfaktor gegenüber 2025</td><td class="z">rund 1,5</td><td class="z">1,25 bis 1,80</td><td>die Hälfte mehr Aufträge</td></tr>
<tr><td>Preisdurchgriff im eigenen Markt</td><td class="z">''' + str(DURCHGRIFF["S4"]) + ''' %</td><td class="z">—</td><td>der Gewinn geht an den Kunden</td></tr>
</tbody></table></div>'''

TEILE.append(kapitel(5, "evidenz", "Rechnen würde billig, Einstehen würde knapp",
 "Der Markt, in dem der Verbund verkauft, wüchse. Aber er wüchse über die Menge, nicht über den Preis, und er teilte sich in zwei Leistungen mit entgegengesetzter Richtung.",
 f'''<div class="prose">
<h3>Die Menge stiege, der Preis fiele</h3>
<p>Der Markt für extern beauftragte Evidenz und Analytik im deutschen Gesundheitswesen läge 2031 bei rund 800 Mio. €, mit einer Spanne von 550 bis 1.150 Mio. €. Die Menge stiege um rund die Hälfte, der Preis je Leistungseinheit fiele um ein Viertel. Treiber der Menge wären die Nachweispflichten aus Kapitel 3 und 4, die zweite Tranche des Gesundheitsdatenraums und der Druck auf Kassen, ihre Ausgaben zu begründen.</p>
<p>Die Marktgröße selbst ist die schwächste Zahl dieser Arbeit. Der einzige öffentlich verfügbare Wert für Deutschland ist ein Marktvolumen für Real-World-Evidence von 204,2 Mio. US-Dollar für 2023. Sechzehn der achtzehn Urteile der Pharmastation nennen die Marktgröße als ihren schwächsten Punkt.</p>
</div>
''' + abb("Der Markt wüchse über die Menge: die Hälfte mehr Aufträge, ein Viertel billiger je Auftrag",
          "Markt für extern beauftragte Evidenz und Analytik im deutschen Gesundheitswesen 2031",
          MARKT,
          "Quelle: Sitzung D, Übergabe Ü3 und Station 4 (Preisdurchgriff D2). Einziger öffentlicher Vergleichswert: RWE-Marktvolumen Deutschland 204,2 Mio. USD (2023).") +
 f'''<div class="prose">
<h3>Zwei Leistungen, zwei Richtungen</h3>
<p>Alle zwölf Fachurteile aus dem Verbund führen denselben Satz: <strong>Was an der Rechenzeit hängt, fällt; was an einer Unterschrift hängt, steigt.</strong> Die Trennlinie verläuft nicht zwischen guter und schlechter Analytik, sondern zwischen beschreibender und verantworteter Leistung.</p>
<p><strong>Beschreibend</strong> heißt: Datenaufbereitung, Kohortenbildung, Literaturübersicht, Standardmodell, Kennzahlenband, Routinedatenbericht, Foliensatz. Diese Leistungen kann ein Kunde 2031 mit eigenen Werkzeugen in einem Bruchteil der Zeit selbst erzeugen. Ihr Preis fiele mit ihren Kosten.</p>
<p><strong>Haftend</strong> heißt: ein Ergebnis, für das der Anbieter einsteht, vor dem Gemeinsamen Bundesausschuss, einer Schiedsstelle, einer Aufsicht oder einem Gericht. Diese Leistung zieht ihren Preis aus der Zusicherung, nicht aus dem Aufwand. Sie setzt drei Dinge voraus: eine nachvollziehbare Auswertungsstrecke, einen Abnahmestandard und eine Person oder Gesellschaft, die zeichnet.</p>
</div>
''' + abb("Der Wertanteil der haftenden Leistung stiege von 30 auf 68 Prozent",
          "Anteil am Umsatz des Evidenzmarkts nach Leistungsart",
          WERT,
          "Quelle: Sitzung D, Station 4, zwölf Urteile aus dem Verbund; Aufteilung nachgerechnet und bestätigt.") +
 f'''<div class="prose">
<p>Weil die haftende Schicht ihren Preis aus einer Zusicherung zieht, stiege der Umsatz eines Anbieters, der den Wechsel schafft, leicht. Sein Deckungsbeitrag fiele trotzdem, um rund 15 Prozent seines Werts von 2025, weil die Zusicherung vorher Geld kostet: Versicherung, Abnahmeverfahren, Qualifikation und eine andere Vertragsform. Der Umsatz 2031 wäre nicht das Problem. Die Marge wäre es.</p>
</div>
'''))

# ====================================================================== Kapitel 6 HIGL
NETTO = [("WIG2", 6823084, 4), ("4K ANALYTICS", 6502941, 4), ("GREENBAY Software", 1952412, 52),
         ("iLoc", 1058861, 99.6), ("INNO3", 744334, 23), ("GREENBAY research", 404164, 67), ("CLINIBOTS", 80954, 48)]
assert sum(n for _, n, _ in NETTO) == 17566750
UMSATZ = hbalken([(n, v / 1e6, f"{de(i, 1 if i % 1 else 0)} % Innenumsatz") for n, v, i in NETTO],
                 8, " Mio. €", "Netto-Erlöse 2025 je Gesellschaft", links=250, hervor={"WIG2", "4K ANALYTICS"}, d=2)

AUSBLICK = punkte_intervall([
    ("WIG2", 20, -10, 55, "DB +15 %"),
    ("GREENBAY Software", 20, -20, 60, "DB +10 %"),
    ("GREENBAY research", 10, -25, 45, "DB −15 %"),
    ("INNO3", 0, -20, 25, "DB −10 %"),
    ("4K ANALYTICS", -10, -40, 15, "DB −30 %"),
    ("CLINIBOTS", -60, -90, -10, "DB −80 %"),
    ("iLoc", None, 0, 0, "nicht marktbewertbar: 99,6 % Innenumsatz"),
    ("GREENBAY healthcare", None, 0, 0, "nicht bewertet: keine eigenen Buchungsdaten"),
    ("Verbund", 5, -35, 40, "DB −15 %"),
], -100, 60, "Umsatz 2031 je Gesellschaft", links=190, fett={"Verbund"})

HEMMNIS = '''<div class="tabelle"><table>
<thead><tr><th>Bindendes Hemmnis</th><th class="z">Verbund, Sitzung D</th><th class="z">Früheres Panel</th></tr></thead>
<tbody>
<tr class="hervor"><td>Haftung</td><td class="z">7 von 12</td><td class="z">7 Nennungen</td></tr>
<tr><td>Refinanzierung</td><td class="z">4 von 12</td><td class="z">29 Nennungen</td></tr>
<tr><td>Akzeptanz</td><td class="z">1 von 12</td><td class="z">—</td></tr>
<tr><td>Investitionsfähigkeit</td><td class="z">—</td><td class="z">24 Nennungen</td></tr>
<tr><td>Recht</td><td class="z">—</td><td class="z">23 Nennungen</td></tr>
</tbody></table></div>'''

TEILE.append(kapitel(6, "higl", "Achtzig Punkte Spreizung: Der Verbund liefe auseinander",
 "Im Mittel wüchse der Verbund bis 2031 leicht. Das Mittel verdeckt, dass seine Gesellschaften in entgegengesetzte Richtungen liefen. Welche gewinnt, hängt daran, wie viel ihres Umsatzes heute schon an einer Zusicherung hängt.",
 f'''<div class="prose">
<h3>Die Ausgangslage 2025</h3>
<p>Die sieben Gesellschaften mit eigenen Buchungsdaten erzielten 2025 zusammen 17,57 Mio. € Netto-Erlöse. Ein Teil davon ist Innenumsatz zwischen den Gesellschaften; der Außenumsatz lag bei rund 14,48 Mio. €. Alle Werte für 2031 beziehen sich auf diesen Außenumsatz.</p>
<p>Zwei Gesellschaften tragen den Verbund: WIG2 und 4K ANALYTICS stehen zusammen für 89 Prozent des Außenumsatzes. Beide sind konzentriert. Bei 4K tragen zwei Kunden, die IKK classic mit 2,12 Mio. € und IQVIA mit 1,91 Mio. €, zusammen 52 Prozent des Außenumsatzes. Bei WIG2 steht der größte Kunde, die ZEG, mit 1,65 Mio. € für 25 Prozent.</p>
</div>
''' + abb("WIG2 und 4K ANALYTICS trügen 89 Prozent des Außenumsatzes",
          "Netto-Erlöse 2025 je Gesellschaft in Mio. €, darunter der Anteil des Innenumsatzes",
          UMSATZ,
          "Quelle: DATEV-Kontenblätter 2025, Erlöskonten, gemessen. GREENBAY healthcare ist eine Teilbetriebsausgründung der 4K ANALYTICS GmbH und hat keinen eigenen Mandanten in den Buchungsdaten.") +
 f'''<div class="prose">
<h3>Der Ausblick je Gesellschaft</h3>
<p><strong>WIG2 und GREENBAY Software gewännen</strong>, je rund 20 Prozent Umsatz. Die Fachurteile ordnen WIG2 der haftenden Schicht zu; der Wert wäre eher vorsichtig, denn die ganze WIG2-Spanne läge unter dem Zentralwert dieser Schicht. Bei GREENBAY Software ist die Zuordnung strittig: Wer sie der haftenden Schicht zurechnet, käme auf plus 40 bis 60 Prozent, wer der beschreibenden, auf minus 25. Der Übergabewert von plus 20 Prozent löst diesen Streit nicht auf; die Spanne liegt 85 Punkte breit.</p>
<p><strong>4K ANALYTICS verlöre</strong> rund 10 Prozent Umsatz und 30 Prozent Deckungsbeitrag. Ihr Geschäft ist die Auswertungsschicht, also genau der Wertanteil, der von 70 auf 32 Prozent fiele. Die Kundenkonzentration verschärfte das: Kürzte einer der beiden großen Kunden sein Budget für Auswertung, träfe das die Gesellschaft überproportional. In Euro stünden sich damit ein Plus von rund 1,3 Mio. € bei WIG2 und ein Minus von rund 0,6 Mio. € bei 4K gegenüber.</p>
<p><strong>CLINIBOTS stünde vor einer eigenen Entscheidung.</strong> Minus 60 Prozent Umsatz, minus 80 Prozent Deckungsbeitrag. Das Produkt verarbeitet öffentlich zugängliche Rohdaten, etwa nach § 21 KHEntgG und aus den Qualitätsberichten, zu einer Auswertung. Das ist die angreifbarste Stelle im gesamten Portfolio. Der Betrag ist klein, rund 49.000 €; die Frage ist, ob die Gesellschaft ein Geschäftsmodell für 2031 hat.</p>
<p><strong>iLoc ist nicht zu bewerten</strong>, und das ist keine Bewertung mit null. 99,6 Prozent ihres Volumens sind Innenumsatz. Ohne Außenmarkt wird ein Produktivitätsgewinn nicht zu einem Preis, sondern zu einer Umlagezeile.</p>
</div>
''' + abb("Die Gesellschaften lägen 80 Punkte auseinander; der Verbundwert beschriebe keine von ihnen",
          "Umsatz 2031 gegenüber 2025 mit 80-%-Intervall, rechts die Veränderung des Deckungsbeitrags (DB)",
          AUSBLICK,
          "Quelle: Sitzung D, Station 4 und Übergabe Ü4. Szenario mit Grundsatzentscheidung und Versicherungsdeckung (Kapitel 7). Werte auf fünf Punkte genau zu lesen.") +
 einordnung("Die Lücke: GREENBAY healthcare",
 "<p>GREENBAY healthcare ist nicht bewertet. Die Gesellschaft ist eine Teilbetriebsausgründung der 4K ANALYTICS GmbH und hat deshalb keinen eigenen Mandanten in den Buchungsdaten, aus denen die Ausgangslage gebildet wurde. Sie beschäftigt 45 Personen und führt mit <em>hAIppokrates</em> (ein Sprachmodell-Rahmenwerk für das klinische Umfeld), <em>Copertino</em> (Tariftreue-Dokumentation) und der angekündigten <em>GREENBAY Suite</em> genau das Portfolio, das nach der Logik dieses Papiers auf der Gewinnerseite stünde.</p><p>Der 4K-Wert von minus 10 Prozent beschreibt deshalb ein Geschäft, aus dem der wachsende Teil bereits herausgelöst wurde. Die Verbundzahl von plus 5 Prozent wäre eher zu niedrig als zu hoch. Um wie viel, lässt sich erst sagen, wenn die Erlös- und Kostenzahlen 2025 von GREENBAY healthcare getrennt vorliegen.</p>") +
 f'''<div class="prose">
<h3>Das bindende Hemmnis wäre die Haftung</h3>
<p>Sieben der zwölf Fachurteile aus dem Verbund nennen die Haftung als das Hemmnis, das den Wechsel zur haftenden Leistung bindet. Sie weichen damit begründet vom früheren Panel ab, das Refinanzierung, Investitionsfähigkeit und Recht vorn sah und die Haftung hinten. Die Begründung ist einheitlich: Für einen Anbieter ist nicht die Kaufentscheidung des Kunden die knappe Größe, sondern die Frage, ob jemand für das Ergebnis geradesteht.</p>
<p>Keines der zwölf Urteile bezeichnet die dafür nötige Versicherungsdeckung als verfügbar oder die Frage als gelöst. Eines beziffert die Zahl heute vorliegender Deckungsangebote mit null.</p>
</div>
''' + abb("Aus Sicht des Verbunds stünde die Haftung vorn, nicht das Geld",
          "Bindendes Hemmnis für den Wechsel zur haftenden Leistung",
          HEMMNIS,
          "Quelle: Sitzung D, Station 4 (S4-01 bis S4-12); früheres Panel aus dem Bestand der Szenariokonferenz, Zahl der Nennungen. Beide Spalten sind wegen unterschiedlicher Grundgesamtheit nicht direkt vergleichbar.")))

# ====================================================================== Kapitel 7 Entscheidung
SCHALTER = gruppen([
    ("Umsatz 2031", [5, -30]),
    ("Deckungsbeitrag 2031", [-15, -60]),
], [("mit Entscheidung und Deckung", "f-accent"), ("ohne", "f-loss")], -60, 20,
   "Umsatz und Deckungsbeitrag 2031 mit und ohne Entscheidung", " %")

PLAN = zeitstrahl([
    (2027.49, "30. Juni 2027", "Konventionen, § 130b", "intern", 3, "start"),
    (2027.99, "31. Dez. 2027", "Zwischenmarke Versicherer", "intern", 2, "start"),
    (2028.49, "30. Juni 2028", "Gesellschafterbeschluss", "intern", 1, "start"),
    (2028.99, "31. Dez. 2028", "Amtliche Größen", "intern", 0, "start"),
    (2026.74, "29. Sept. 2026", "US-Zoll für alle", "extern", 0, "start"),
    (2027.92, "2. Dez. 2027", "KI-VO Anhang III", "extern", 2, "start"),
    (2028.5, "30. Juni 2028", "§ 130b Abs. 1c endet", "extern", 1, "start"),
    (2029.05, "20. Jan. 2029", "Ende US-Nullsatz", "extern", 0, "start"),
    (2030.0, "2030", "Vorhaltevergütung voll", "extern", 1, "start"),
    (2031.2, "März 2031", "EHDS, zweite Tranche", "extern", 0, "end"),
], 2026, 2031.6, "Zeitplan der Entscheidung", achse=170)

TEILE.append(kapitel(7, "entscheidung", "Ein Beschluss, drei Bausteine, fünf Fristen",
 "Die Szenarien liefen bis 2027 fast gleich. Die Fristen, die über 2031 entscheiden, liegen trotzdem davor, weil sie an Verfahrens-, Rechts- und Vergabetakten hängen, die der Verbund nicht steuert.",
 f'''<div class="prose">
<h3>Zwei Ausgänge, kein dritter</h3>
<p>Die Werte der Kapitel 5 und 6 gelten für ein Szenario, in dem der Verbund eine Grundsatzentscheidung trifft und Versicherungsdeckung erhält. Das Gegenszenario ist getrennt gerechnet. Ohne Entscheidung fiele der Außenumsatz bis 2031 um rund 30 Prozent (Spanne minus 45 bis minus 20), der Deckungsbeitrag um 60 Prozent. Mit Entscheidung stiege der Umsatz um 5 Prozent, der Deckungsbeitrag fiele um 15.</p>
<p>In Euro läge der Außenumsatz 2031 mit Entscheidung um rund 0,7 Mio. € über dem Stand von 2025, ohne um rund 4,3 Mio. € darunter. <strong>Die Entscheidung wäre damit rund 5,1 Mio. € Außenumsatz wert</strong>, 35 Punkte beim Umsatz und 45 beim Deckungsbeitrag. Das ist nicht der Rand einer Unsicherheit, sondern ein eigener Zustand: Auch wer die Marktunsicherheit wegdenkt, stünde noch vor diesen beiden Ausgängen.</p>
</div>
''' + abb("Die Entscheidung wäre rund 5,1 Mio. € Außenumsatz und 45 Punkte Deckungsbeitrag wert",
          "Veränderung 2031 gegenüber 2025 in Prozent, bezogen auf 14,48 Mio. € Außenumsatz",
          SCHALTER,
          "Quelle: Sitzung D, Übergabe Ü4 mit Szenarioschalter. Die beiden Balkenpaare sind getrennt gerechnete Szenarien, keine Intervallränder.") +
 f'''<div class="prose">
<h3>Was zu beschließen wäre</h3>
<p>Der Beschluss hätte drei Bausteine, und sie wirkten nur zusammen. Ein Abnahmestandard ohne Versicherung ist ein Versprechen ohne Deckung; eine Versicherung ohne nachvollziehbare Auswertungsstrecke ist nicht zu bekommen; beides ohne eine Stelle, die zeichnet, ist keine Haftung.</p>
<ol class="empfehlung">
<li><div><strong>Eine nachvollziehbare Auswertungsstrecke.</strong> Jedes Ergebnis, für das der Verbund einsteht, müsste vom Rohdatum bis zur Aussage prüfbar sein, einschließlich der eingesetzten Modelle und ihres Änderungsstands.<span class="wer">Produkt und Regulatory</span></div></li>
<li><div><strong>Ein Abnahmestandard.</strong> Schriftlich festgelegt, was ein Ergebnis erfüllen muss, bevor es das Haus verlässt, und wer die Abnahme erklärt. Er müsste zu dem passen, was Aufsicht und Nutzenbewertung als Konformitätsnachweis anerkennen.<span class="wer">Geschäftsführungen der Gesellschaften</span></div></li>
<li><div><strong>Eine zeichnende Verantwortung mit Deckung.</strong> Eine Gesellschaft oder Person, die das Ergebnis vertraglich zusichert, und ein Berufshaftpflichtversicherer, der diese Zusicherung deckt.<span class="wer">Gesellschafter</span></div></li>
</ol>

<h3>Fünf Empfehlungen</h3>
<ol class="empfehlung">
<li><div><strong>Bis 30. Juni 2027 die Herleitungskonventionen festlegen</strong> und zur § 130b-Weiche Position beziehen. Bezugsgröße, Zuschnitt, Einheit, Basisjahr, Preisstufe und Deflator je Kennzahl. Die Kette dieser Arbeit ist an vier Gelenken nicht am Rechnen gescheitert, sondern daran, dass niemand vorher gesagt hat, was gezählt wird.<span class="wer">Controlling; Geschäftsführung und Verbände</span></div></li>
<li><div><strong>Bis 31. Dezember 2027 die Zwischenmarke erreichen:</strong> eine schriftliche Vorabstimmung mit mindestens einem Berufshaftpflichtversicherer. Parallel klären, welcher Konformitätsnachweis einen KI-gestützten Leistungsbescheid nach § 31a SGB X und ein maschinell erzeugtes Ergebnis im Verfahren nach § 35a SGB V trägt.<span class="wer">Geschäftsführung; Produkt und Regulatory</span></div></li>
<li><div><strong>Bis 30. Juni 2028 binär beschließen.</strong> Wurde die Zwischenmarke gerissen, wäre negativ zu entscheiden und nicht zu verschieben, weil die nachfolgenden Verfahrenstakte kein weiteres Jahr zuließen.<span class="wer">Gesellschafter</span></div></li>
<li><div><strong>4K ANALYTICS und CLINIBOTS je eine eigene Antwort geben.</strong> Bei 4K ist die Kundenkonzentration das drängendere Thema als der Modellwert; bei CLINIBOTS die Frage, ob es ein Geschäftsmodell für 2031 gibt.<span class="wer">Geschäftsführungen der beiden Gesellschaften</span></div></li>
<li><div><strong>GREENBAY healthcare vor dem Beschluss nachbewerten.</strong> Die Gesellschaft mit dem Portfolio, das gewinnen würde, ist in dieser Rechnung nicht enthalten. Nötig sind die Erlös- und Kostenzahlen 2025, getrennt vom 4K-Mandanten.<span class="wer">Controlling</span></div></li>
</ol>
</div>
''' + abb("Vier Fristen lägen im Haus, sechs außerhalb; die Vorbereitung müsste 2027 beginnen, nicht 2028",
          "Oben: Fristen des Verbunds; unten: äußere Takte, an denen sie hängen",
          PLAN,
          "Quelle: Sitzung D, Station 4 und Kettenprüfung; Rechtsstand nach Proclamation 11020, KHAG, VO (EU) 2024/1689 und EHDS-Verordnung. Der Geltungsbeginn der Anhang-III-Pflichten ist strittig (2. Dezember 2027 oder 2. August 2028).") +
 '<p class="zitat">Die einzige Frist, die allein im Haus liegt, ist der Gesellschafterbeschluss. Alle anderen hängen an Dritten.</p>'))

# ====================================================================== Anhang
TEILE.append(kapitel(None, "methode", "Methode, Grenzen, Quellen",
 "Woher die Zahlen kommen, wie sie zu lesen sind und wo sie nicht tragen.",
 f'''<div class="prose">
<h3>Wie die Zahlen entstanden sind</h3>
<p>Grundlage ist eine Szenariokonferenz, deren vierte Sitzung am 25. September 2026 lief. Hundert Fachrollen, verteilt auf fünf Stationen und drei Querbänke, haben die Studie von Korinek u. a. entlang einer Wirkungskette auf Deutschland übertragen: von der Gesamtwirtschaft über die Finanzierung von GKV und PKV und die Leistungserbringer bis zu Pharma und den Gesellschaften des Verbunds. Jede Station übergab einen Zentralwert mit Intervall an die nächste. {N_KETTE} Urteile bilden die Kette, dazu acht Urteile zu Europa und sechs zur Technik.</p>
<p><strong>Die Fachrollen sind KI-Agenten, keine befragten Menschen.</strong> Jede Rolle wurde von einem Sprachmodell eingenommen, mit einem festen Fragebogen, dem gemeinsamen Faktenkern und den Übergaben der Vorstation als Eingabe. Die Urteile sind deshalb als strukturierte Modellrechnung zu lesen, nicht als Expertenbefragung. Die Ist-Werte 2025 des Verbunds stammen aus den DATEV-Kontenblättern und sind gemessen.</p>

<h3>Vier Grenzen, die jeder Leser kennen sollte</h3>
<p><strong>Die Endzahlen sind Rechtsfolge- und Vertragsaussagen, keine Modellaussagen.</strong> Die Studie liefert den Rahmen, in dem die Fragen gestellt werden, nicht die Antworten. Die 420 Mrd. € GKV-Ausgaben folgen aus deutscher Rechts- und Fortschreibungsmechanik.</p>
<p><strong>Die Szenariowahl ist importiert.</strong> {round(100*SZEN["substantial"]/N_KETTE)} Prozent der Urteile wählten den mittleren Pfad, obwohl die Autoren ihren Szenarien keine Wahrscheinlichkeiten zuordnen. Ein anderes Szenario verschöbe die Zahlen, nach Einschätzung der Kette aber nicht die Richtung der Aussage.</p>
<p><strong>Das Modell rechnet bis 2030, diese Arbeit bis 2031.</strong> Die zusätzliche Jahresscheibe bewegte auf der Einnahmenseite rund 42 Mrd. €, das Vier- bis Fünffache des gesamten KI-Effekts auf die Beitragsbasis.</p>
<p><strong>Die Schlussfassung der Konferenz hat keine zweite Freigabe erhalten.</strong> Eine interne Gegenprüfung fand sieben harte Rechen- und Zählfehler; alle wurden eingearbeitet, die Einarbeitung wurde nicht erneut geprüft. Für den Deckungsbeitrag zirkulieren drei Werte, 6,3, 15 und 25 Prozent Rückgang; maßgeblich ist 15.</p>

<p><strong>Lesart.</strong> Werte für 2031 stehen im Konjunktiv und sind auf ihre Ableseeinheit genau zu lesen: 1.790 Mrd. € auf 10 Mrd., 420 Mrd. € auf 5 Mrd., 800 Mio. € auf 50 Mio., die Verbundwerte auf 5 Prozentpunkte. Intervalle sind 80-Prozent-Intervalle. Mediane stammen aus den Urteilen der jeweiligen Station und sind auf ganze Zahlen gerundet.</p>

<h3>Quellen</h3>
<ul>
<li>Korinek, A., Jones, C., Sacher, S., Cotter, T., McCrory, B.: <em>Economic Scenarios for Transformative AI</em>. The Anthropic Institute, Working Paper 2026-02.</li>
<li>Szenariokonferenz, Sitzung D, Rohdaten und Verfahrensbericht: <code>rohdaten/sitzung-d.json</code>, <code>30-Sitzung-D.md</code>; ausführliche Fassung mit allen Herleitungen: <code>29-Strategiepapier-2031.md</code>.</li>
<li>Gemeinsamer Faktenkern der Szenariokonferenz (<code>01-Briefing.md</code>): IAB-Prognosen März 2026, ifo-Konjunkturumfrage Juni 2026, BT-Drs. 21/7620, Draghi-Bericht.</li>
<li>GKV-Statistik KV45 und KJ1 2025; PKV-Verband, Zahlenbericht und Beitragsanpassung 2026.</li>
<li>Proclamation 11020, Federal Register 2026-06956; SGB V §§ 35a, 71, 130b; SGB X § 31a; KHEntgG § 21; Krankenhausreformanpassungsgesetz; VO (EU) 2024/1689; Verordnung über den Europäischen Gesundheitsdatenraum.</li>
<li>DATEV-Kontenblätter 2025 der Gesellschaften des HIGL-Verbunds.</li>
</ul>
<p class="fuss" style="margin-top:2.4em;border-top:1px solid var(--rule);padding-top:1em">Erstellt mit Unterstützung von Künstlicher Intelligenz. Die Zahlen für 2031 sind Modellergebnisse und keine Prognosen; die Ist-Werte 2025 sind aus den Buchungsdaten gemessen. HIGL-Verbund, Puschstraße 6a, 04103 Leipzig. Stand 26. September 2026.</p>
</div>
'''))

# ====================================================================== Ausgabe
HTML = (f'<title>Die Haftungswende</title>\n<meta name="description" content="Strategiepapier des HIGL-Verbunds: Auswirkungen von KI bis 2031 auf Europa, Deutschland, das Gesundheitswesen und die Gesellschaften des Verbunds.">\n'
        f'{FONTS}\n<style>{CSS}</style>\n<main class="wrap">\n' + "\n".join(TEILE) + "\n</main>\n")

if __name__ == "__main__":
    ziel = os.path.join(HIER, "Die-Haftungswende.html")
    open(ziel, "w", encoding="utf-8").write(HTML)
    print(ziel, len(HTML), "Zeichen,", _abb[0], "Abbildungen")
