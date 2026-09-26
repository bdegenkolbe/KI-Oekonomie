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

a.begriff{color:inherit;text-decoration:underline dotted var(--muted);text-underline-offset:3px;}
a.begriff:hover{color:var(--accent);}
dl.glossar{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:0 32px;margin:.6em 0 1.4em;}
dl.glossar div{padding:.55em 0;border-top:1px solid var(--rule);break-inside:avoid;}
dl.glossar dt{font-weight:700;font-size:.92rem;}
dl.glossar dd{margin:.2em 0 0;font-size:.88rem;color:var(--ink-2);}
aside.folgerung{border-top-color:var(--accent);}
aside.folgerung .eyebrow{color:var(--accent);}
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
  #methode ul,#methode .fuss,dl.glossar dd{font-size:8.4pt;}
  dl.glossar dt{font-size:8.8pt;}
  a.begriff{text-decoration:none;}
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

# Begriffe, die im Anhang erklärt werden. Erstnennung im Text verlinkt über B().
GLOSSAR = [
    ("preisdurchgriff", "Preisdurchgriff", "Anteil eines Produktivitätsgewinns, der beim Preis ankommt. 100 Prozent hieße: Lässt sich eine Leistung um ein Fünftel billiger herstellen, sinkt auch ihr Preis um ein Fünftel. Niedrige Werte bedeuten, dass der Preis anderen Regeln folgt, etwa einer Budgetformel."),
    ("standardauswertung", "Standardauswertung", "Analyseleistung, deren Wert im Aufwand liegt: Datenaufbereitung, Kohortenbildung, Literaturübersicht, Standardmodell, Kennzahlenbericht, Foliensatz. KI kann sie zunehmend schneller und billiger erzeugen."),
    ("haftung", "Leistung mit Haftung", "Analyseergebnis, für das der Anbieter einsteht, etwa vor dem Gemeinsamen Bundesausschuss, einer Schiedsstelle, einer Aufsicht oder einem Gericht. Ihr Preis ergibt sich aus der Zusicherung, nicht aus dem Aufwand."),
    ("szenario", "Szenario", "Einer von drei Entwicklungspfaden der US-Studie: <em>modest</em> (gering), <em>substantial</em> (deutlich), <em>extreme</em> (sehr stark). Die Autoren ordnen ihnen keine Wahrscheinlichkeiten zu."),
    ("intervall", "80-Prozent-Intervall", "Spanne, in der ein Wert nach Einschätzung der Fachrollen mit 80 Prozent Wahrscheinlichkeit läge. Je breiter, desto unsicherer."),
    ("median", "Median", "Mittlerer Wert einer Reihe: Die Hälfte der Einschätzungen liegt darüber, die Hälfte darunter. Anders als der Durchschnitt wird er von Ausreißern kaum verschoben."),
    ("entgelte", "Beitragspflichtige Entgelte", "Die Löhne und Gehälter, auf die Beiträge zur gesetzlichen Krankenversicherung erhoben werden, begrenzt durch die Beitragsbemessungsgrenze. Sie sind die Einnahmenbasis der GKV."),
    ("vorhalte", "Vorhaltevergütung", "Teil der Krankenhausvergütung nach der Krankenhausreform, der für das Bereitstellen einer Leistungsgruppe gezahlt wird, unabhängig von der Fallzahl."),
    ("erstattungsbetrag", "Erstattungsbetrag", "Preis eines neuen Arzneimittels, den Hersteller und GKV-Spitzenverband nach § 130b SGB V auf Grundlage der Nutzenbewertung vereinbaren. In Deutschland ist er öffentlich."),
    ("nutzenbewertung", "Nutzenbewertung", "Verfahren nach § 35a SGB V, in dem der Gemeinsame Bundesausschuss den Zusatznutzen eines neuen Arzneimittels feststellt. Das Ergebnis bestimmt den Erstattungsbetrag."),
    ("mfn", "Meistbegünstigung", "Englisch <em>most favoured nation</em> (MFN): Der US-Preis richtet sich nach dem niedrigsten Preis in einer Gruppe von Vergleichsländern."),
    ("kivo", "KI-Verordnung", "Verordnung (EU) 2024/1689. Für Hochrisikosysteme, etwa in Medizin und Sozialverwaltung, gelten Pflichten zu Datenqualität, Dokumentation, menschlicher Aufsicht und Konformitätsnachweis."),
    ("ehds", "Europäischer Gesundheitsdatenraum", "Englisch <em>European Health Data Space</em> (EHDS): EU-Rahmen, der die Nutzung von Gesundheitsdaten für Forschung und Versorgung über Zugangsstellen regelt."),
    ("rwe", "Real-World-Evidence", "Erkenntnisse aus Versorgungsdaten, etwa Abrechnungsdaten, Registern oder Patientenakten, im Unterschied zu Daten aus klinischen Studien."),
    ("db", "Deckungsbeitrag", "Umsatz abzüglich der direkt zurechenbaren Kosten. Er zeigt, was eine Leistung zur Deckung der Fixkosten und zum Gewinn beiträgt."),
    ("aussenumsatz", "Außenumsatz", "Umsatz mit Kunden außerhalb des Verbunds. Innenumsatz sind Leistungen zwischen den Gesellschaften; er fällt in der Verbundsicht heraus."),
]
_GL = {k: t for k, t, _ in GLOSSAR}
def B(schluessel, text=None):
    """Begriff bei Erstnennung mit dem Glossar verlinken."""
    return f'<a class="begriff" href="#g-{schluessel}">{text or _GL[schluessel]}</a>'

def folgerung(text):
    return f'<aside class="einordnung folgerung"><span class="eyebrow">Was das für den Verbund heißt</span>{text}</aside>'

# ====================================================================== Titel
TEILE.append(f'''
<section class="blatt titelblatt titel">
<div class="eyebrow">HIGL-Verbund · Strategiepapier · September 2026</div>
<h1>Die Haftungswende</h1>
<p class="unter">Was Künstliche Intelligenz bis 2031 für Europa, Deutschland, das Gesundheitswesen und die Gesellschaften des HIGL-Verbunds bedeutet</p>
<div class="meta">
<div><b>Stand</b>26. September 2026, Fassung 2.0</div>
<div><b>Zweck</b>Strategischer Rahmen für die Gesellschaften des Verbunds</div>
<div><b>Grundlage</b>Szenariokonferenz mit 100 Fachrollen; Ist-Werte aus den DATEV-Kontenblättern 2025</div>
<div><b>Für</b>Gesellschafter und Geschäftsführungen</div>
</div>
<div class="inhalt" style="margin-top:3em">
<div class="eyebrow">Inhalt</div>
<ol>
<li><span>·</span><a href="#blick">Auf einen Blick</a><em>Leitfrage, Kernaussagen, Rahmen</em></li>
<li><span>1</span><a href="#europa">Europa</a><em>Der Gewinn kommt an, der Preis folgt ihm kaum</em></li>
<li><span>2</span><a href="#deutschland">Deutschland</a><em>Die Beitragsbasis wächst weiter</em></li>
<li><span>3</span><a href="#gesundheit">Gesundheitswesen</a><em>Mehr Leistungen, knappere Preise</em></li>
<li><span>4</span><a href="#pharma">Pharma und USA</a><em>Mehr Druck, mehr Bedarf an Evidenz</em></li>
<li><span>5</span><a href="#evidenz">Unser Markt</a><em>Auswertung wird billig, Haftung wird wertvoll</em></li>
<li><span>6</span><a href="#higl">Die Gesellschaften</a><em>Wer wo steht</em></li>
<li><span>7</span><a href="#rahmen">Der strategische Rahmen</a><em>Richtung, Voraussetzungen, Handlungsfelder, Zeitfenster</em></li>
<li><span>A</span><a href="#methode">Anhang</a><em>Methode, Grenzen, Begriffe, Quellen</em></li>
</ol>
<p class="fuss" style="margin-top:2em">Alle Werte für 2031 sind Ergebnisse einer Modellrechnung, keine Prognosen, und stehen deshalb im Konjunktiv. Gemessen sind die Ist-Werte 2025 aus den Buchungsdaten und die amtlichen Kennzahlen mit Quellenangabe.</p>
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
    ("HIGL-VERBUND", "+5 % / −15 %", "Umsatz / Deckungs-|beitrag, Pfad A"),
], "Wirkungskette von der Gesamtwirtschaft bis zum HIGL-Verbund")

TEILE.append(kapitel("", "blick", "Auf einen Blick",
 "KI macht Analyse schneller und billiger. Für einen Verbund, der von Analyse lebt, ist das Chance und Risiko zugleich. Dieses Papier ordnet ein, wo bis 2031 Wert entstünde und welche Richtung sich daraus für die Gesellschaften ableitet.",
 f'''<div class="prose">
<p><strong>Leitfrage.</strong> Wo entsteht im Gesundheitswesen bis 2031 Wert, wenn KI Analyse billig macht, und wie sollte sich der Verbund dazu aufstellen?</p>
<p>Das Papier folgt dem Geld: von der Gesamtwirtschaft über die Krankenversicherung, die Krankenhäuser und die Pharmaindustrie bis zum Markt, in dem der Verbund verkauft. Jedes Kapitel endet mit der Frage, was der Befund für den Verbund bedeutet. Kapitel 7 fasst diese Folgerungen zu einem strategischen Rahmen zusammen. Beschlüsse trifft das Papier nicht; es beschreibt die Richtung und die Voraussetzungen, an denen sich die Gesellschaften ausrichten können.</p>
</div>
<ul class="kernaussagen">
<li><b>1</b><div><strong>Europa</strong><span>Der Produktivitätsgewinn käme auch in Europa an. Im Gesundheitswesen würde er sich aber kaum im Preis zeigen, weil Preise dort über Budgets und Gesetze festgelegt werden.</span></div></li>
<li><b>2</b><div><strong>Deutschland</strong><span>Die Löhne, auf die Krankenkassenbeiträge erhoben werden, würden bis 2031 auf rund 1.790 Mrd. € steigen. Der Anteil, der auf KI zurückgeht, wäre mit rund 10 Mrd. € klein.</span></div></li>
<li><b>3</b><div><strong>Gesundheitswesen</strong><span>Die Krankenkassen würden 2031 rund 27 Prozent mehr ausgeben als 2025, für die einzelne Leistung aber nur 13 Prozent mehr zahlen. Die Kunden des Verbunds hätten mehr Arbeit und weniger Spielraum.</span></div></li>
<li><b>4</b><div><strong>Pharma und USA</strong><span>Die US-Preispolitik setzt Hersteller unter Druck. Nach den meisten Einschätzungen würde das die Nachfrage nach Evidenz aus Deutschland erhöhen, im Median um rund 9 Prozent.</span></div></li>
<li><b>5</b><div><strong>Unser Markt</strong><span>Der Wert würde sich verschieben: weg von der Standardauswertung, die KI günstig erledigt, hin zu Ergebnissen, für die jemand haftet. Ihr Anteil stiege von 30 auf 68 Prozent.</span></div></li>
<li><b>6</b><div><strong>Die Gesellschaften</strong><span>WIG2 und GREENBAY Software würden wachsen, 4K ANALYTICS und CLINIBOTS stünden unter Druck. Der Verbund als Ganzes läge bei plus 5 Prozent Umsatz, aber mit sinkender Marge.</span></div></li>
</ul>
<div class="entscheidung">
<div class="eyebrow">Der strategische Rahmen in Kürze</div>
<h3>Vom Auswerten zum Einstehen</h3>
<p>Der Verbund würde seinen Wert künftig weniger aus Rechenarbeit ziehen als aus Ergebnissen, für die er einsteht. Dafür braucht es drei Voraussetzungen, die nur zusammen wirken: eine nachvollziehbare Auswertungsstrecke, einen Abnahmestandard und eine Verantwortung mit Versicherungsdeckung. Wie viel davon abhängt, zeigen die beiden Pfade, die die Modellrechnung unterscheidet:</p>
<div class="zahlen">
<div><b>+5 %</b><span>Umsatz 2031, Pfad A: Verbund kann haften</span></div>
<div><b>−30 %</b><span>Umsatz 2031, Pfad B: Verbund bleibt bei der Standardauswertung</span></div>
<div><b>5,1 Mio. €</b><span>Abstand beim Außenumsatz</span></div>
<div><b>Ende 2027</b><span>bis dahin sollte klar sein, ob Versicherungsdeckung zu bekommen ist</span></div>
</div>
</div>
''' + abb("Vom Gesamtmarkt bis zum Verbund: Aus einem Produktivitätsgewinn würde ein Margenthema",
          "Zentralwerte 2031 je Stufe der Wirkungskette",
          KETTE,
          "Quelle: Szenariokonferenz Sitzung D, Werte je Stufe; Basis 2025: GKV-Statistik KV45 und KJ1, DATEV-Kontenblätter des Verbunds. Umsatzangabe bezogen auf 14,48 Mio. € Außenumsatz 2025.")))

# ====================================================================== Kapitel 1 Europa
SZEN_TAB = '''<div class="tabelle"><table>
<thead><tr><th>Szenario der US-Studie (bis 2030)</th><th class="z">BIP ggü. Basis</th><th class="z">Wachstum p. a.</th><th class="z">Lohnquote</th><th>gewählt von</th></tr></thead>
<tbody>
<tr><td>Basis ohne transformative KI</td><td class="z">—</td><td class="z">rund 2 %</td><td class="z">rund 60 %</td><td>—</td></tr>
<tr><td><em>modest</em> (gering)</td><td class="z">gering</td><td class="z">knapp über Basis</td><td class="z">knapp unter 60 %</td><td>''' + str(SZEN["modest"]) + ''' von ''' + str(N_KETTE) + '''</td></tr>
<tr class="hervor"><td><em>substantial</em> (deutlich)</td><td class="z">+8,3 %</td><td class="z">5,4 %</td><td class="z">rund 56 %</td><td>''' + str(SZEN["substantial"]) + ''' von ''' + str(N_KETTE) + '''</td></tr>
<tr><td><em>extreme</em> (sehr stark)</td><td class="z">+32 %</td><td class="z">15 %</td><td class="z">rund 45 %</td><td>''' + str(SZEN["extreme"]) + ''' von ''' + str(N_KETTE) + '''</td></tr>
</tbody></table></div>'''

UNTERSCHIEDE = '''<div class="tabelle"><table>
<thead><tr><th>Punkt</th><th>Annahme der US-Studie</th><th>Lage im europäischen Gesundheitswesen</th><th class="z">Kennzahl</th></tr></thead>
<tbody>
<tr><td><strong>Preis</strong></td><td>Ein Produktivitätsgewinn senkt den Preis oder erhöht die Marge.</td><td>Preise folgen Budgets, Fallpauschalen und Verhandlungsterminen.</td><td class="z">''' + str(DURCHGRIFF["S2"]) + ''' % statt ''' + str(DURCHGRIFF["S0"]) + ''' %</td></tr>
<tr><td><strong>Zeit</strong></td><td>Anpassung, sobald die Technik es erlaubt.</td><td>Tarifrunden, Vergabeverfahren und Haushaltsjahre verzögern.</td><td class="z">rund 3 Jahre</td></tr>
<tr><td><strong>Haftung</strong></td><td>Kein eigener Kostenfaktor.</td><td>KI-Verordnung, Medizinprodukte- und Berufsrecht verlangen jemanden, der einsteht.</td><td class="z">7 von 12</td></tr>
<tr><td><strong>Ort</strong></td><td>Der Gewinn bleibt im Land.</td><td>Modelle und Rechenzentren liegen überwiegend außerhalb Europas.</td><td class="z">55 % bleiben in der EU</td></tr>
</tbody></table></div>'''

EUROPA = hbalken([
    ("Frankreich", 70, "Fallpauschalen, nationaler Ausgabendeckel"),
    ("Niederlande", 55, "Versicherer kaufen selektiv ein"),
    ("Deutschland, Gesamtwirtschaft", DURCHGRIFF["S0"], "alle Branchen"),
    ("EU-Gesundheitsdatenraum", 35, "Durchsatz der Zugangsstellen"),
    ("KI-Verordnung", 25, "fehlende harmonisierte Normen"),
    ("Estland", 20, "Haftung nach Art. 14 KI-VO"),
    ("Vereinigtes Königreich", 20, "Effizienzabschlag, nachlaufend"),
    ("EU-Arzneimittelpaket", 20, "Unterlagenschutz, Verfahrensdauer"),
    ("Dänemark", 15, "steuerfinanziert, Wartezeitgarantie"),
    ("Deutschland, Leistungserbringer", DURCHGRIFF["S2"], "Krankenhäuser, Praxen, Pflege"),
], 80, " %", "Preisdurchgriff im europäischen Vergleich", links=300,
   hervor={"Deutschland, Leistungserbringer", "Deutschland, Gesamtwirtschaft"})

TEILE.append(kapitel(1, "europa", "Der Produktivitätsgewinn käme nach Europa, im Preis zeigte er sich kaum",
 "Die Studie, auf der diese Arbeit aufbaut, rechnet für die USA. Ihre Grundmechanik lässt sich auf Europa übertragen, ihre Preisbildung nicht. Das bestimmt, wer im Gesundheitswesen vom Gewinn profitiert.",
 f'''<div class="prose">
<h3>Ausgangspunkt: drei Szenarien für die USA</h3>
<p>Die Studie <em>Economic Scenarios for Transformative AI</em> (Korinek, Jones, Sacher, Cotter und McCrory, Working Paper 2026-02) beschreibt drei {B("szenario", "Szenarien")} bis 2030. Im mittleren Szenario <em>substantial</em> läge das Bruttoinlandsprodukt (BIP) 2030 um 8,3 Prozent über einem Pfad ohne KI, das Wachstum bei 5,4 statt rund 2 Prozent im Jahr. Im extremen Szenario wären es 32 Prozent und 15 Prozent Wachstum. Der Anteil der Arbeitseinkommen am Volkseinkommen, die Lohnquote, fiele von rund 60 auf 56 Prozent, im extremen Fall auf 45.</p>
<p>Zwei Befunde der Studie sind für dieses Papier wichtig. Die Löhne in Wissensberufen würden im mittleren Szenario leicht sinken, um 0,3 Prozent; die Löhne in allen übrigen Berufen stiegen um 5,9 Prozent. Die Studie beschreibt also eine Verschiebung zwischen Tätigkeiten, keinen allgemeinen Stellenabbau. Außerdem verlaufen die drei Szenarien bis 2027 fast gleich und trennen sich erst danach. Wer sich vorbereiten will, kann nicht abwarten, welches eintritt.</p>
<p>Die Autoren betonen, dass ihre Szenarien keine Vorhersagen sind, und geben keine Wahrscheinlichkeiten an. Die Fachrollen der Szenariokonferenz haben trotzdem fast einhellig das mittlere Szenario gewählt (Abbildung 2). Die Zahlen dieses Papiers beschreiben deshalb im Kern einen Pfad, nicht die ganze Bandbreite.</p>
</div>
''' + abb(f"{SZEN['substantial']} von {N_KETTE} Einschätzungen wählten das mittlere Szenario",
          "Szenarien der US-Studie und ihre Wahl in der Szenariokonferenz",
          SZEN_TAB,
          "Quelle: Korinek u. a., Economic Scenarios for Transformative AI, WP 2026-02; Szenariowahl der 83 Einschätzungen entlang der Wirkungskette. Das mittlere Szenario stützt sich empirisch auf eine Befragung von 10.980 US-Erwachsenen (Morning Consult, August 2026).") +
 f'''<div class="prose">
<h3>Wo die US-Rechnung nicht auf Europa passt</h3>
<p>Die Studie nennt selbst, was ihr Modell nicht abbildet: festgelegte Preise, Haushaltsjahre, gedeckelte Budgets und politische Aushandlung. Diese Faktoren bestimmen aber, wie ein Produktivitätsgewinn im europäischen Gesundheitswesen ankommt. Die Einschätzungen aller Stufen der Wirkungskette zeigen vier Unterschiede.</p>
</div>
''' + abb("An vier Punkten weicht die europäische Lage von den Annahmen der US-Studie ab",
          "Annahmen der US-Studie und Lage im europäischen Gesundheitswesen",
          UNTERSCHIEDE,
          "Quelle: Sitzung D, Mediane zu Preisdurchgriff und Verzögerung; Engpassangaben der Fachrollen aus dem Verbund; Verbleib der Wertschöpfung in der EU aus dem Bestand der Szenariokonferenz (18 Einschätzungen, mittlere Hälfte 42 bis 68 Prozent).") +
 f'''<div class="prose">
<p><strong>Der Preis ist der wichtigste Unterschied.</strong> Die Kennzahl dafür ist der {B("preisdurchgriff")}: Welcher Anteil eines Produktivitätsgewinns zeigt sich im Preis? In der deutschen Gesamtwirtschaft läge er bei {DURCHGRIFF["S0"]} Prozent, bei Krankenhäusern, Praxen und Pflege bei {DURCHGRIFF["S2"]} Prozent. Dort folgt der Preis der Budgetformel. Ein Krankenhaus, das mit KI günstiger dokumentiert, erhält dafür weder mehr noch weniger Geld. Die Ersparnis bleibt im Haus und deckt andere Kosten.</p>
<p><strong>Europa ist dabei kein einheitlicher Raum.</strong> In Frankreich steuert der Staat Preise über Fallpauschalen und einen nationalen Ausgabendeckel; er würde einen Effizienzgewinn in ein bis zwei Tarifrunden zurückholen. Der Preisdurchgriff läge bei 70 Prozent, allerdings zugunsten der Kostenträger. In den Niederlanden kaufen Versicherer selektiv ein, der Wert läge bei 55 Prozent. In steuerfinanzierten Systemen wie Dänemark und dem Vereinigten Königreich würde der Gewinn eher in kürzeren Wartezeiten aufgehen; dort lägen die Werte bei 15 und 20 Prozent.</p>
</div>
''' + abb(f"Deutschland läge mit {DURCHGRIFF['S2']} Prozent am unteren Rand: Im Krankenhaus käme ein Effizienzgewinn kaum beim Preis an",
          "Anteil eines Produktivitätsgewinns, der sich 2031 im Preis zeigen würde, Median in Prozent",
          EUROPA,
          "Quelle: Sitzung D, Europa-Einschätzungen EU-01 bis EU-08 und Mediane der Stufen Gesamtwirtschaft und Leistungserbringer. Länderwerte beruhen auf je einer Einschätzung und zeigen die Richtung, keine Messung.") +
 f'''<div class="prose">
<h3>Die Regeln, die bis 2031 zählen</h3>
<p><strong>Die {B("kivo")}</strong> würde KI im Gesundheitswesen vor allem verlangsamen, weil sie Nachweise fordert, für die die Maßstäbe noch fehlen: Die harmonisierten Normen zu den Pflichten für Hochrisikosysteme (Artikel 8 bis 15) liegen noch nicht vor. Wann die Pflichten für die Fälle aus Anhang III beginnen, ist unter den Fachrollen umstritten: zehn nennen den 2. Dezember 2027, zwei den 2. August 2028. Das deutsche Durchführungsgesetz gilt seit dem 29. Juli 2026.</p>
<p><strong>Der {B("ehds", "Europäische Gesundheitsdatenraum")}</strong> öffnet ab März 2031 die zweite Stufe der Datennutzung für Forschung, mit Bildgebung, Laborwerten, Entlassbriefen und Genomdaten. Für alle, die mit Gesundheitsdaten arbeiten, wäre das der größte Nachfrageschub bis 2031. Der Engpass läge in der Bearbeitungskapazität der Zugangsstellen.</p>
<p><strong>Die Wettbewerbsfähigkeit Europas</strong> bleibt der Hintergrund. Nach dem Draghi-Bericht sind nur vier der fünfzig größten Technologieunternehmen der Welt europäisch. Von einem KI-Effizienzgewinn im Gesundheitswesen blieben nach den Einschätzungen rund 55 Prozent in der EU, in einer Spanne von 42 bis 68 Prozent. Der Rest ginge an die Anbieter der Modelle und der Rechenleistung.</p>
</div>
''' + folgerung(f"<p>Der Verbund verkauft an Kunden, deren Preise kaum auf Produktivität reagieren. Seine Kunden könnten mit KI sparen, hätten dafür aber nicht mehr Budget. Der eigene Markt des Verbunds funktioniert anders: Dort herrscht Wettbewerb, und ein Effizienzgewinn würde an die Kunden weitergegeben (Kapitel 5). Beides zusammen heißt: Mit billigerer Standardarbeit allein ließe sich kein höherer Preis erzielen.</p>")))

# ====================================================================== Kapitel 2 Deutschland
LOHNQUOTE = hbalken([
    ("Basis ohne transformative KI", 60, "US-Studie"),
    ("substantial", 56, f"gewählt von {SZEN['substantial']} von {N_KETTE}"),
    ("extreme", 45, f"gewählt von {SZEN['extreme']} von {N_KETTE}"),
], 80, " %", "Lohnquote je Szenario", links=280, hervor={"substantial"})

MECHANIK = hbalken([
    ("Zuwachs 2025 bis 2031 insgesamt", 240, "1.550 auf 1.790 Mrd. €, 2,4 % p. a."),
    ("Anhebung Bemessungsgrenze 2027", 18.5, "geltendes Recht, 15 bis 22"),
    ("Jahr 2030 auf 2031", 42, "36 bis 50, jenseits der Studie"),
    ("Wirkung der KI", 10, "vier Einschätzungen, 0,56 %"),
], 320, " Mrd. €", "Bewegungen der beitragspflichtigen Entgelte", links=300, hervor={"Wirkung der KI"}, d=0)

E3_ZEILEN = ["Gesamtwirtschaft", "Kranken- und Pflegekassen", "Leistungserbringer", "Pharma", "Markt des Verbunds"]
E3_WERTE = [E3[s] for s in ("S0", "S1", "S2", "S3", "S4")]
WAERME = waermefeld(E3_ZEILEN, ["Kapital", "Kunden", "Beschäftigte", "Staat"], E3_WERTE,
                    "Verteilung des Effizienzgewinns je Stufe", vmax=40)

TEILE.append(kapitel(2, "deutschland", "Die Beitragsbasis wüchse weiter, KI veränderte sie kaum",
 "Für die Finanzierung des Gesundheitswesens zählt vor allem die Summe der Löhne, auf die Beiträge erhoben werden. Sie würde bis 2031 weiter steigen, getragen von Recht und Lohnentwicklung.",
 f'''<div class="prose">
<h3>Die Einnahmenbasis der Krankenkassen</h3>
<p>Die {B("entgelte", "beitragspflichtigen Entgelte")} der Mitglieder der gesetzlichen Krankenversicherung (GKV) lagen 2025 bei 1.550 Mrd. €. Bis 2031 würden sie auf rund 1.790 Mrd. € steigen, in einer Spanne von 1.680 bis 1.930. Das entspräche 2,4 Prozent im Jahr. Treiber sind die Lohnentwicklung, die Zahl der Beschäftigten und die Beitragsbemessungsgrenze. Keiner dieser Treiber stammt aus der US-Studie.</p>
<p>Vier Einschätzungen beziffern, wie viel davon auf KI zurückgeht: rund 10 Mrd. €, also 0,56 Prozent. Allein die gesetzlich beschlossene Anhebung der Bemessungsgrenze zum 1. Januar 2027 brächte mit 15 bis 22 Mrd. € ungefähr das Doppelte. Die 1.790 Mrd. € sind daher vor allem eine Fortschreibung deutscher Regeln und Löhne. Der Einfluss von KI auf die Einnahmen bliebe bis 2031 gering.</p>
</div>
''' + abb("Die Wirkung der KI auf die Beitragsbasis wäre die kleinste der bezifferten Größen",
          "Bewegungen der beitragspflichtigen Entgelte bis 2031, Mrd. €",
          MECHANIK,
          "Quelle: Sitzung D, Stufe Gesamtwirtschaft; Basis KV45 2025: 1.550,0 Mrd. €. Anhebung der Bemessungsgrenze: Mitte der Spanne 15 bis 22 Mrd. € aus zehn Einschätzungen. Wirkung der KI: vier Einschätzungen gegen einen Pfad ohne KI.") +
 f'''<div class="prose">
<h3>Tätigkeiten verschieben sich</h3>
<p>Das Institut für Arbeitsmarkt- und Berufsforschung (IAB) rechnet damit, dass durch KI in fünfzehn Jahren rund 1,6 Millionen Stellen wegfallen oder neu entstehen. Schon seine Kurzfristprognose vom März 2026 ist zweigeteilt: 140.000 Beschäftigte weniger in der Industrie, 180.000 mehr in öffentlichen Diensten, Erziehung und Gesundheit. In einer Umfrage des ifo Instituts unter rund 3.000 Unternehmen, die KI nutzen, erwartet etwa die Hälfte in den nächsten fünf Jahren sinkende Löhne für Berufseinsteiger. Die Bundesregierung sieht nach ihrer Antwort vom August 2026 »keine belastbaren Hinweise« auf einen systematischen Stellenabbau durch KI.</p>
<p>Das passt zur US-Studie: Unter Druck gerieten vor allem die Einstiegsstufen der Wissensberufe. Gewinnen würden Tätigkeiten, bei denen Menschen vor Ort sein müssen. Im Gesundheitswesen ist das der größere Teil der Arbeit: Der Anteil körperlich gebundener Tätigkeiten läge bei den Leistungserbringern bei {de(med("S2","d1_physisch"))} Prozent, in der Gesamtwirtschaft bei {de(med("S0","d1_physisch"))} Prozent.</p>
</div>
''' + abb("Die Lohnquote würde sinken, im gewählten Szenario um vier Punkte",
          "Anteil der Arbeitseinkommen am Volkseinkommen 2030 je Szenario, US-Studie",
          LOHNQUOTE,
          "Quelle: Korinek u. a., WP 2026-02. Die Lohnquote lässt sich nicht direkt auf die deutsche Beitragsbasis übertragen und dient hier nur zur Einordnung.") +
 f'''<div class="prose">
<h3>Wer den Effizienzgewinn bekäme</h3>
<p>Jede Fachrolle hat angegeben, wie sich ein Effizienzgewinn in ihrem Bereich auf Kapitalgeber, Kunden, Beschäftigte und Staat verteilen würde (Abbildung 7). In der Gesamtwirtschaft teilten sich Kapital und Kunden den Gewinn etwa hälftig. Bei den Kranken- und Pflegekassen ginge gut ein Drittel an den Staat, über Beitragssätze, Zuschüsse und Aufsicht. Im Markt des Verbunds erhielten die Kunden mit {E3["S4"][1]} Prozent den größten Anteil.</p>
</div>
''' + abb(f"Im Markt des Verbunds bekämen die Kunden mit {E3['S4'][1]} Prozent den größten Anteil des Effizienzgewinns",
          "Verteilung eines Effizienzgewinns 2031, Median je Stufe in Prozent",
          WAERME,
          "Quelle: Sitzung D, alle 83 Einschätzungen entlang der Wirkungskette; je Einschätzung ergeben die vier Anteile 100. Die Mediane ergeben je Zeile nicht zwingend 100.") +
 folgerung("<p>Die Finanzierung des Gesundheitswesens bräche bis 2031 nicht weg; die Einnahmen würden weiter wachsen. Der Druck auf die Kunden des Verbunds käme von der Ausgabenseite (Kapitel 3). Für den eigenen Markt heißt die Verteilung: Vom Effizienzgewinn aus KI erhielten die Kunden den größten Anteil, der Anbieter behielte nur einen Teil.</p>")))

# ====================================================================== Kapitel 3 Gesundheitswesen
GKV = gruppen([
    ("Ausgaben", [26.9]),
    ("Vergütung je Leistung", [13]),
    ("Kosten der Erbringer", [22]),
    ("Vergütung real", [-7]),
], [("Veränderung 2031 gegenüber 2025", "f-accent")], -20, 40,
   "Ausgaben, Vergütung und Kosten in der GKV 2031", " %")

KETTE_DG = hbalken([
    ("Gesamtwirtschaft", DURCHGRIFF["S0"], ""),
    ("Kranken- und Pflegekassen", DURCHGRIFF["S1"], ""),
    ("Leistungserbringer", DURCHGRIFF["S2"], ""),
    ("Pharma", DURCHGRIFF["S3"], ""),
    ("Markt des Verbunds", DURCHGRIFF["S4"], ""),
], 80, " %", "Preisdurchgriff je Stufe", links=300, hervor={"Leistungserbringer", "Markt des Verbunds"})

TEILE.append(kapitel(3, "gesundheit", "Mehr Leistungen, knappere Preise",
 "Die Krankenkassen würden 2031 deutlich mehr ausgeben als heute. Beim einzelnen Krankenhaus und bei der einzelnen Praxis käme davon weniger an, als ihre Kosten stiegen. Die Kunden des Verbunds hätten mehr Arbeit und weniger Spielraum.",
 f'''<div class="prose">
<h3>Gesetzliche Krankenversicherung: Die Ausgaben wachsen schneller als die Preise</h3>
<p>Die Leistungsausgaben der GKV lagen 2025 bei 331,1 Mrd. €. Bis 2031 würden sie auf rund 420 Mrd. € steigen, ein Plus von 26,9 Prozent; mit Verwaltung und sonstigen Ausgaben wären es rund 436 Mrd. €. Das Wachstum käme aus Alterung, Krankheitslast und Menge. Die Vergütung je Leistung stiege im selben Zeitraum nur um 13 Prozent. Nach einer zweiten zulässigen Lesart des § 71 Abs. 3 SGB V wären es 16 Prozent, in einer Spanne von 8 bis 20 Prozent. Die beiden Lesarten unterscheiden sich darin, ob der Zuwachs der Einnahmen auf alle Mitglieder zusammen (2,4 Prozent im Jahr) oder je Mitglied (2,7 Prozent) gerechnet wird.</p>
<p>Die Kosten der Leistungserbringer würden nach den Einschätzungen um 18 bis 26 Prozent steigen. Real, also nach Abzug dieser Kostensteigerung, sänke die Vergütung je Leistung damit um 4 bis 10 Prozent.</p>
<p>Der steuerfinanzierte Anteil würde sinken. Die Bundesmittel entsprachen 2025 noch 4,8 Prozent der Leistungsausgaben, 2031 wären es bei nahezu unverändertem Zuschuss rund 3,7 Prozent. Die Finanzreserven der Kassen lagen Ende 2025 bei 5,1 Mrd. €, das reicht für gut fünf Tage Ausgaben. Für Investitionen, die sich erst nach drei Jahren rechnen, hätten die Kassen damit wenig Spielraum, zumal ihre Verwaltungskosten ab 2027 an den Einnahmenzuwachs gebunden sind.</p>
</div>
''' + abb("Die Ausgaben würden doppelt so schnell steigen wie die Vergütung je Leistung; real verlöre jede Leistung an Wert",
          "Veränderung 2031 gegenüber 2025 in Prozent, Zentralwerte",
          GKV,
          "Quelle: Sitzung D, Stufen Kranken- und Pflegekassen sowie Leistungserbringer (420 Mrd. € gegen 331,062 Mrd. € laut KJ1 2025). Kosten der Erbringer: Mitte der Spanne 18 bis 26 Prozent; Vergütung real: Mitte der Spanne −4 bis −10 Prozent.") +
 f'''<div class="prose">
<h3>Private Krankenversicherung: stabiler Bestand, steigende Beiträge</h3>
<p>Die private Krankenversicherung (PKV) zählte 2025 rund 8,79 Millionen Vollversicherte, 0,5 Prozent mehr als im Vorjahr. Zum 1. Januar 2026 stiegen die Beiträge im Schnitt um 12,6 Prozent, für 81 Prozent der Versicherten; im Jahr davor waren es 13,9 Prozent. Die Alterungsrückstellungen wuchsen auf 355,4 Mrd. €. Größter Kostentreiber waren die Pflegekosten im Krankenhaus mit einem Plus von 17,6 Prozent. Die PKV hätte damit einen starken Anreiz, Effizienzgewinne zu nutzen, aber wenig Einfluss: Sie verhandelt keine Krankenhauspreise.</p>

<h3>Krankenhäuser: Die Reform wirkt erst ab 2030 voll</h3>
<p>Das Krankenhausreformanpassungsgesetz (KHAG) gilt seit dem 15. April 2026. Es ordnet die Versorgung in 61 Leistungsgruppen und führt eine {B("vorhalte")} ein. Sie läuft 2026 und 2027 budgetneutral, wird 2028 und 2029 schrittweise eingeführt und wirkt ab 2030 voll. Das Institut für das Entgeltsystem im Krankenhaus (InEK) rechnet für 2026 bis 2029 mit den Daten von 2024.</p>
<p>Bis 2030 hätte ein Krankenhaus damit kaum eine Möglichkeit, einen KI-Effizienzgewinn in höhere Erlöse umzusetzen. Der Gewinn bliebe als Kostenentlastung im Haus. Deshalb läge der Preisdurchgriff bei den Leistungserbringern am niedrigsten in der ganzen Wirkungskette (Abbildung 9).</p>
</div>
''' + abb(f"Der Preis folgte der Produktivität vor allem dort, wo Wettbewerb herrscht: im Markt des Verbunds mit {DURCHGRIFF['S4']} Prozent",
          "Preisdurchgriff 2031 je Stufe der Wirkungskette, Median in Prozent",
          KETTE_DG,
          "Quelle: Sitzung D, alle 83 Einschätzungen, Median je Stufe. Bis zur Wirkung vergingen auf allen Stufen im Median drei Jahre.") +
 folgerung("<p>Kassen, Krankenhäuser und Hersteller hätten 2031 mehr Fälle, knappere Budgets und strengere Nachweispflichten. Sie würden weniger Auswertung um ihrer selbst willen einkaufen und mehr Ergebnisse, auf die sie sich vor Aufsicht, Schiedsstelle oder Gericht berufen können. Das ist die Nachfrage, auf die sich der Verbund ausrichten müsste.</p>")))

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
], 2026, 2030.8, "Zeitplan der US-Arzneimittelpolitik und der deutschen Frist", achse=170)

US_WOLKE = punktwolke(US_EFFEKT, -15, 30, US_MEDIAN, "Effekt der US-Politik je Einschätzung", schritt=5)

TEILE.append(kapitel(4, "pharma", "Die US-Preispolitik erhöhte den Druck auf Hersteller und den Bedarf an Evidenz",
 "Die amerikanische Arzneimittelpolitik schmälert die Margen der Hersteller. Zugleich macht sie den deutschen Erstattungsbetrag zum Vergleichspreis für den größten Markt der Welt. Für Anbieter von Evidenz überwöge nach den meisten Einschätzungen der zweite Effekt.",
 f'''<div class="prose">
<h3>Was in den USA beschlossen ist</h3>
<p>Mit der Proklamation 11020 vom 2. April 2026 hat die US-Regierung Zölle auf patentgeschützte Arzneimittel eingeführt. Der Regelsatz liegt bei 100 Prozent, für Erzeugnisse aus der EU bei 15 Prozent, aus dem Vereinigten Königreich bei 10 Prozent. Für 17 namentlich genannte Unternehmen gilt der Zoll seit dem 31. Juli 2026, für alle übrigen ab dem 29. September 2026. Hersteller mit einer Preisvereinbarung und Produktion in den USA zahlen bis zum 20. Januar 2029 keinen Zoll; wer nur die Produktion verlagert, zahlt 20 Prozent und ab dem 2. April 2030 den vollen Satz. Generika sind ausgenommen, laut Text allerdings nur »at this time«; eine Überprüfung ist binnen eines Jahres vorgesehen.</p>
<p>Hinzu kommen 26 Vereinbarungen zur {B("mfn")} mit Herstellern, die zusammen rund 89 Prozent des Markts für Markenarzneimittel abdecken, sowie drei Erstattungsmodelle: GENEROUS für Medicaid seit Januar 2026, GLOBE für Medicare Part B, angekündigt für Oktober 2026 (eine endgültige Regelung lag zum Stand dieses Papiers nicht vor), und GUARD für Medicare Part D ab Januar 2027.</p>

<h3>Warum Deutschland dabei besonders betroffen ist</h3>
<p>Bei der Meistbegünstigung orientiert sich der US-Preis an den Preisen anderer Länder. Deutschland gehört zu beiden US-Vergleichsgruppen und ist das einzige große EU-Land, dessen verhandelte Nettopreise öffentlich sind. Der {B("erstattungsbetrag")} gilt ab dem siebten Monat bundesweit. Jeder Euro, den ein Hersteller in Deutschland nachgibt, könnte ihn damit auch in den USA Geld kosten.</p>
<p>§ 130b Abs. 1c SGB V erlaubt derzeit einen vertraulichen Erstattungsbetrag. Diese Regel läuft am 30. Juni 2028 aus, wenn der Gesetzgeber nicht handelt. Ohne Referentenentwurf bis Mitte 2027 wäre das Auslaufen praktisch nicht mehr aufzuhalten. Die Fachrollen halten das Auslaufen für den wahrscheinlicheren Fall, mit rund 65 Prozent. Sieben von achtzehn nennen diese Frage als diejenige, die ihre Einschätzung am stärksten beeinflusst.</p>
</div>
''' + abb("Der US-Druck verschärft sich bis 2030 in mehreren Stufen; die deutsche Frist fällt in die Mitte",
          "Oben: Rechtsstand in den USA; unten: Fristen in Deutschland",
          ZOLL,
          "Quelle: Proclamation 11020 (Federal Register 2026-06956); Faktenblatt N01 der Sitzung D; § 130b Abs. 1c SGB V. Frist für den Referentenentwurf rückwärts aus dem üblichen Gesetzgebungsablauf gerechnet.") +
 f'''<div class="prose">
<h3>Mehr Preisdruck, mehr Bedarf an Evidenz</h3>
<p>Wer einen Preis verteidigen muss, braucht bessere Begründungen. {US_POS} der 18 Einschätzungen zur Pharmaindustrie erwarten deshalb, dass die US-Politik den deutschen Markt für Evidenz vergrößert; vier erwarten das Gegenteil. Der Median läge bei {de(US_MEDIAN,0,vz=True)} Prozent, in Euro bei rund 65 Mio.</p>
<p>Die Einschätzungen nennen vier Wirkungswege. Drei wirken nach oben: Hersteller würden mehr in die Begründung eines Erstattungsbetrags investieren, der zugleich US-Vergleichspreis ist; der vertrauliche Erstattungsbetrag setzt eine Forschungsabteilung in Deutschland voraus; und die Proklamation macht den Nachweis, wo ein Wirkstoff hergestellt wird, zu einer Geldfrage. Einer wirkt nach unten: Sinkt die US-Marge, sparen Hersteller zuerst bei Abteilungen ohne eigene Erlöse, und dazu gehören Evidenzabteilungen.</p>
<p>Sicher ist die Richtung nicht. Sieben der achtzehn Einschätzungen halten auch einen Effekt von null für möglich. Für Generika, Medizinprodukte und digitale Gesundheitsanwendungen spielt die US-Politik derzeit keine Rolle. Der Effekt würde den Markt deshalb eher aufteilen als insgesamt vergrößern: Er stärkte Anbieter, die Herstellern in der {B("nutzenbewertung")} helfen, und schwächte jene, deren Leistung beim Hersteller als reiner Kostenblock gilt.</p>
</div>
''' + abb(f"{US_POS} von 18 Einschätzungen sähen einen positiven US-Effekt auf die Nachfrage nach Evidenz, im Median {de(US_MEDIAN,0,vz=True)} Prozent",
          "Effekt der US-Arzneimittelpolitik auf das Volumen des deutschen Evidenzmarkts 2031, je Einschätzung in Prozent",
          US_WOLKE,
          "Quelle: Sitzung D, Einschätzungen S3-01 bis S3-18; Differenz zwischen dem Wert mit und ohne US-Politik, bezogen auf den Wert ohne. Median der Eurodifferenzen +65 Mio. €, Durchschnitt +50 Mio. €.") +
 folgerung("<p>Die Nutzenbewertung würde für Hersteller wichtiger. Wer dort mit belastbarer Evidenz aus deutschen Versorgungsdaten auftreten kann, hätte bessere Chancen. Voraussetzung wäre, dass solche Evidenz im Verfahren nach § 35a SGB V anerkannt wird, auch wenn sie mit KI erzeugt wurde. Für maschinell erzeugte Ergebnisse fehlt dafür bislang eine Regel; acht der achtzehn Einschätzungen sehen darin den wichtigsten Engpass.</p>")))

# ====================================================================== Kapitel 5 Evidenzmarkt
WERT = gestapelt([
    ("2025", [(70, "Standardauswertung", "f-accent2"), (30, "mit Haftung", "f-accent")]),
    ("2031", [(32, "Standardauswertung", "f-accent2"), (68, "mit Haftung", "f-accent")]),
], "Wertanteile von Standardauswertung und Leistung mit Haftung")

MARKT = '''<div class="tabelle"><table>
<thead><tr><th>Größe 2031</th><th class="z">Zentralwert</th><th class="z">80-%-Intervall</th><th>Lesart</th></tr></thead>
<tbody>
<tr class="hervor"><td>Extern beauftragte Evidenz und Analytik, Deutschland</td><td class="z">800 Mio. €</td><td class="z">550 bis 1.150</td><td>auf 50 Mio. € genau zu lesen</td></tr>
<tr><td>Preisindex je Leistung (2025 = 100)</td><td class="z">75</td><td class="z">55 bis 95</td><td>ein Viertel billiger</td></tr>
<tr><td>Menge gegenüber 2025</td><td class="z">rund 1,5-fach</td><td class="z">1,25 bis 1,80</td><td>die Hälfte mehr Aufträge</td></tr>
<tr><td>Preisdurchgriff im Markt des Verbunds</td><td class="z">''' + str(DURCHGRIFF["S4"]) + ''' %</td><td class="z">—</td><td>der Gewinn geht an die Kunden</td></tr>
</tbody></table></div>'''

TEILE.append(kapitel(5, "evidenz", "Auswertung würde billig, Haftung würde wertvoll",
 "Der Markt, in dem der Verbund verkauft, würde wachsen, aber über die Menge und nicht über den Preis. Zugleich teilte er sich in zwei Leistungsarten, die sich gegenläufig entwickeln.",
 f'''<div class="prose">
<h3>Mehr Aufträge zu niedrigeren Preisen</h3>
<p>Der Markt für extern beauftragte Evidenz und Analytik im deutschen Gesundheitswesen läge 2031 bei rund 800 Mio. €, in einer Spanne von 550 bis 1.150 Mio. €. Die Menge der Aufträge stiege um rund die Hälfte, der Preis je Leistung fiele um ein Viertel. Die Menge würde von den Nachweispflichten aus Kapitel 3 und 4 getrieben, von der zweiten Stufe des Gesundheitsdatenraums und vom Druck auf die Kassen, ihre Ausgaben zu begründen.</p>
<p>Die Marktgröße ist die unsicherste Zahl dieses Papiers. Der einzige öffentlich verfügbare Vergleichswert für Deutschland ist die Schätzung eines Marktforschungsinstituts für den Teilmarkt {B("rwe")}: 204,2 Mio. US-Dollar im Jahr 2023. Sechzehn der achtzehn Einschätzungen zur Pharmaindustrie nennen die Marktgröße als ihren schwächsten Punkt.</p>
</div>
''' + abb("Der Markt würde über die Menge wachsen: die Hälfte mehr Aufträge, ein Viertel billiger je Auftrag",
          "Markt für extern beauftragte Evidenz und Analytik im deutschen Gesundheitswesen 2031",
          MARKT,
          "Quelle: Sitzung D, Stufen Pharma und Markt des Verbunds. Einziger öffentlicher Vergleichswert: Marktforschungsschätzung für den Teilmarkt Real-World-Evidence in Deutschland, 204,2 Mio. USD (2023), laut Faktenblättern der Sitzung D.") +
 f'''<div class="prose">
<h3>Zwei Leistungsarten mit entgegengesetzter Entwicklung</h3>
<p>Die zwölf Fachrollen aus dem Verbund beschreiben die Entwicklung übereinstimmend: Was vor allem Rechenzeit kostet, verliert an Wert; was eine Unterschrift braucht, gewinnt. Das Papier unterscheidet deshalb zwei Leistungsarten.</p>
<p>Die {B("standardauswertung")} umfasst Datenaufbereitung, Kohortenbildung, Literaturübersichten, Standardmodelle, Kennzahlenberichte und Foliensätze. Solche Leistungen könnte ein Kunde 2031 mit eigenen Werkzeugen in einem Bruchteil der Zeit selbst erstellen. Ihr Preis würde mit ihren Kosten fallen.</p>
<p>Eine {B("haftung")} ist ein Ergebnis, für das der Anbieter einsteht: vor dem Gemeinsamen Bundesausschuss, einer Schiedsstelle, einer Aufsicht oder einem Gericht. Ihr Preis ergibt sich aus der Zusicherung, nicht aus dem Aufwand. Sie setzt drei Dinge voraus: eine nachvollziehbare Auswertungsstrecke, einen Abnahmestandard und jemanden, der das Ergebnis unterschreibt.</p>
</div>
''' + abb("Der Wertanteil der Leistung mit Haftung stiege von 30 auf 68 Prozent",
          "Anteil am Umsatz des Evidenzmarkts nach Leistungsart",
          WERT,
          "Quelle: Sitzung D, zwölf Einschätzungen aus dem Verbund; Aufteilung nachgerechnet und bestätigt.") +
 folgerung(f"<p>Ein Anbieter, der den Wechsel zur Leistung mit Haftung schafft, könnte seinen Umsatz leicht steigern. Sein {B('db')} würde trotzdem zunächst sinken, um rund 15 Prozent gegenüber 2025, weil die Zusicherung vorab Geld kostet: Versicherung, Abnahmeverfahren, Qualifikation und neue Vertragsformen. Das Wachstum läge im Umsatz, die Aufgabe in der Marge.</p>")))

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
    ("iLoc", None, 0, 0, "nicht am Markt bewertbar: 99,6 % Innenumsatz"),
    ("GREENBAY healthcare", None, 0, 0, "nicht bewertet: keine eigenen Buchungsdaten"),
    ("Verbund", 5, -35, 40, "DB −15 %"),
], -100, 60, "Umsatz 2031 je Gesellschaft", links=190, fett={"Verbund"})

ENGPASS = '''<div class="tabelle"><table>
<thead><tr><th>Wichtigster Engpass</th><th class="z">Fachrollen aus dem Verbund</th><th class="z">Frühere Befragung</th></tr></thead>
<tbody>
<tr class="hervor"><td>Haftung</td><td class="z">7 von 12</td><td class="z">7 Nennungen</td></tr>
<tr><td>Refinanzierung</td><td class="z">4 von 12</td><td class="z">29 Nennungen</td></tr>
<tr><td>Akzeptanz</td><td class="z">1 von 12</td><td class="z">—</td></tr>
<tr><td>Investitionsfähigkeit</td><td class="z">—</td><td class="z">24 Nennungen</td></tr>
<tr><td>Recht</td><td class="z">—</td><td class="z">23 Nennungen</td></tr>
</tbody></table></div>'''

TEILE.append(kapitel(6, "higl", "Die Gesellschaften entwickelten sich sehr unterschiedlich",
 "Im Durchschnitt würde der Verbund bis 2031 leicht wachsen. Dahinter stünden gegenläufige Entwicklungen. Wie es einer Gesellschaft ginge, hinge davon ab, wie viel ihres Umsatzes schon heute an Ergebnissen hängt, für die sie einsteht.",
 f'''<div class="prose">
<h3>Die Ausgangslage 2025</h3>
<p>Die sieben Gesellschaften mit eigenen Buchungsdaten erzielten 2025 zusammen 17,57 Mio. € Netto-Erlöse. Ein Teil davon sind Leistungen zwischen den Gesellschaften; der {B("aussenumsatz")} lag bei rund 14,48 Mio. €. Alle Werte für 2031 beziehen sich auf diesen Außenumsatz.</p>
<p>WIG2 und 4K ANALYTICS stehen zusammen für 89 Prozent des Außenumsatzes, und beide hängen stark an einzelnen Kunden. Bei 4K entfallen auf die IKK classic (2,12 Mio. €) und IQVIA (1,91 Mio. €) zusammen 52 Prozent des extern fakturierten Volumens. Bei WIG2 steht der größte Kunde, die ZEG, mit 1,65 Mio. € für 25 Prozent. Die Kundenbeträge sind Bruttobeträge aus der Debitorenbuchhaltung; sie lassen sich deshalb nicht direkt mit den Netto-Erlösen in Abbildung 14 verrechnen.</p>
</div>
''' + abb("WIG2 und 4K ANALYTICS tragen 89 Prozent des Außenumsatzes",
          "Netto-Erlöse 2025 je Gesellschaft in Mio. €, darunter der Anteil des Innenumsatzes",
          UMSATZ,
          "Quelle: DATEV-Kontenblätter 2025, Erlöskonten, gemessen. GREENBAY healthcare ist eine Teilbetriebsausgründung der 4K ANALYTICS GmbH und hat keinen eigenen Mandanten in den Buchungsdaten.") +
 f'''<div class="prose">
<h3>Der Ausblick je Gesellschaft</h3>
<p><strong>WIG2 und GREENBAY Software</strong> würden jeweils um rund 20 Prozent wachsen. Die Fachrollen ordnen WIG2 der Leistung mit Haftung zu; der Wert ist eher vorsichtig, denn die gesamte Spanne für WIG2 liegt unter dem Mittelwert dieser Leistungsart. Bei GREENBAY Software ist die Zuordnung offen: Als Anbieter von Leistung mit Haftung käme die Gesellschaft auf plus 40 bis 60 Prozent, als Anbieter von Standardauswertung auf minus 25 Prozent. Die angegebenen plus 20 Prozent klären diese Frage nicht.</p>
<p><strong>4K ANALYTICS</strong> würde rund 10 Prozent Umsatz und 30 Prozent Deckungsbeitrag verlieren. Ihr Geschäft liegt überwiegend in der Standardauswertung, deren Wertanteil von 70 auf 32 Prozent fiele. Die Abhängigkeit von zwei Kunden verstärkt das Risiko. In Euro stünden einem Plus von rund 1,3 Mio. € bei WIG2 ein Minus von rund 0,6 Mio. € bei 4K gegenüber.</p>
<p><strong>CLINIBOTS</strong> läge bei minus 60 Prozent Umsatz und minus 80 Prozent Deckungsbeitrag. Das Produkt wertet öffentlich zugängliche Daten aus, etwa nach § 21 KHEntgG und aus den Qualitätsberichten der Krankenhäuser. Diese Art von Auswertung könnte KI am leichtesten ersetzen. Der Betrag ist mit rund 49.000 € klein; offen ist, welches Geschäftsmodell die Gesellschaft 2031 trägt.</p>
<p><strong>iLoc</strong> lässt sich nicht bewerten, weil 99,6 Prozent ihres Umsatzes innerhalb des Verbunds entstehen. Ohne Außenmarkt würde ein Effizienzgewinn nur die interne Umlage senken. <strong>GREENBAY research</strong> (plus 10 Prozent) und <strong>INNO3</strong> (unverändert) lägen dazwischen.</p>
</div>
''' + abb("Die Gesellschaften lägen bis zu 80 Prozentpunkte auseinander; der Verbundwert beschreibt keine von ihnen",
          "Umsatz 2031 gegenüber 2025 mit 80-%-Intervall, rechts die Veränderung des Deckungsbeitrags (DB), Pfad A",
          AUSBLICK,
          "Quelle: Sitzung D, Stufe Markt des Verbunds. Pfad A: Der Verbund kann für seine Ergebnisse haften (Kapitel 7). Werte auf fünf Prozentpunkte genau zu lesen.") +
 einordnung("Offene Stelle: GREENBAY healthcare",
 "<p>GREENBAY healthcare ist in diesem Papier nicht bewertet. Die Gesellschaft ist eine Teilbetriebsausgründung der 4K ANALYTICS GmbH und hat deshalb keinen eigenen Mandanten in den Buchungsdaten, aus denen die Ausgangslage gebildet wurde. Sie beschäftigt 45 Personen und bietet mit <em>hAIppokrates</em> (ein Rahmenwerk für Sprachmodelle im klinischen Umfeld), <em>Copertino</em> (Dokumentation der Tariftreue) und der angekündigten <em>GREENBAY Suite</em> Produkte an, die nach diesem Papier an Wert gewinnen würden.</p><p>Der Wert für 4K beschreibt deshalb ein Geschäft, aus dem der wachsende Teil bereits ausgegliedert ist. Die plus 5 Prozent für den Verbund wären eher zu niedrig als zu hoch. Wie viel, lässt sich erst sagen, wenn die Erlös- und Kostenzahlen 2025 von GREENBAY healthcare getrennt vorliegen.</p>") +
 f'''<div class="prose">
<h3>Der wichtigste Engpass wäre die Haftung</h3>
<p>Sieben der zwölf Fachrollen aus dem Verbund sehen in der Haftung den wichtigsten Engpass auf dem Weg zur Leistung mit Haftung. Eine frühere Befragung hatte Refinanzierung, Investitionsfähigkeit und Recht vorn gesehen. Die Begründung der Fachrollen ist einheitlich: Für einen Anbieter entscheidet weniger, ob der Kunde kauft, als ob jemand für das Ergebnis geradesteht.</p>
<p>Keine der zwölf Fachrollen hält die dafür nötige Versicherungsdeckung für verfügbar oder die Frage für gelöst. Eine gibt an, dass derzeit kein einziges Deckungsangebot vorliege.</p>
</div>
''' + abb("Aus Sicht des Verbunds stünde die Haftung an erster Stelle",
          "Wichtigster Engpass für den Wechsel zur Leistung mit Haftung",
          ENGPASS,
          "Quelle: Sitzung D, Einschätzungen S4-01 bis S4-12; frühere Befragung aus dem Bestand der Szenariokonferenz, Zahl der Nennungen. Die Spalten haben unterschiedliche Grundgesamtheiten und sind nicht direkt vergleichbar.") +
 folgerung("<p>Eine einheitliche Verbundstrategie würde den Gesellschaften nicht gerecht. WIG2 wäre bereits nahe an der Leistung mit Haftung, 4K ANALYTICS und CLINIBOTS stünden vor einem Umbau, bei GREENBAY Software ist die Einordnung offen, und GREENBAY healthcare fehlt in der Rechnung. Der Rahmen in Kapitel 7 gibt deshalb eine gemeinsame Richtung vor und lässt jeder Gesellschaft ihren eigenen Weg dorthin.</p>")))

# ====================================================================== Kapitel 7 Strategischer Rahmen
PFADE = gruppen([
    ("Umsatz 2031", [5, -30]),
    ("Deckungsbeitrag 2031", [-15, -60]),
], [("Pfad A: Verbund kann haften", "f-accent"), ("Pfad B: nur Standardauswertung", "f-loss")], -60, 20,
   "Umsatz und Deckungsbeitrag 2031 in beiden Pfaden", " %")

FADEN = '''<div class="tabelle"><table>
<thead><tr><th>Kapitel</th><th>Befund</th><th>Folgerung für den Rahmen</th></tr></thead>
<tbody>
<tr><td>1 Europa</td><td>Im Gesundheitswesen zeigt sich ein Effizienzgewinn kaum im Preis.</td><td>Billigere Standardarbeit allein bringt keinen höheren Preis.</td></tr>
<tr><td>2 Deutschland</td><td>Die Beitragsbasis wächst weiter; im Markt des Verbunds erhielten die Kunden den größten Anteil eines Effizienzgewinns.</td><td>Die Finanzierung trägt; der Wettbewerb gibt Effizienz weiter.</td></tr>
<tr><td>3 Gesundheitswesen</td><td>Mehr Leistungen, real sinkende Vergütung, strengere Nachweise.</td><td>Kunden kaufen belastbare Ergebnisse, keine Auswertung um ihrer selbst willen.</td></tr>
<tr><td>4 Pharma und USA</td><td>Preisdruck erhöht den Bedarf an Evidenz für die Nutzenbewertung.</td><td>Wachstum liegt bei Ergebnissen, die in Verfahren bestehen.</td></tr>
<tr><td>5 Unser Markt</td><td>Wertanteil der Leistung mit Haftung steigt von 30 auf 68 Prozent.</td><td>Die Richtung: vom Auswerten zum Einstehen.</td></tr>
<tr><td>6 Die Gesellschaften</td><td>Große Unterschiede; wichtigster Engpass ist die Haftung.</td><td>Gemeinsame Richtung, eigene Wege je Gesellschaft.</td></tr>
</tbody></table></div>'''

FELDER = '''<div class="tabelle"><table>
<thead><tr><th>Handlungsfeld</th><th>Worum es geht</th><th>Leitfrage für jede Gesellschaft</th></tr></thead>
<tbody>
<tr><td><strong>Nachweisfähigkeit</strong></td><td>Ergebnisse so erzeugen und dokumentieren, dass sie vor Aufsicht, Nutzenbewertung und Gericht bestehen, auch wenn KI beteiligt ist.</td><td>Welche unserer Ergebnisse könnten wir heute unterschreiben, und was fehlt bei den übrigen?</td></tr>
<tr><td><strong>Versicherbarkeit</strong></td><td>Klären, zu welchen Bedingungen Berufshaftpflichtversicherer Zusicherungen für Analyseergebnisse decken.</td><td>Für welche Leistungen bräuchten wir Deckung, und in welcher Höhe?</td></tr>
<tr><td><strong>Portfolio</strong></td><td>Standardauswertung automatisieren und günstiger anbieten; Leistung mit Haftung gezielt aufbauen.</td><td>Welcher Anteil unseres Umsatzes hängt heute an einer Zusicherung, welcher an reinem Aufwand?</td></tr>
<tr><td><strong>Kundenbasis</strong></td><td>Abhängigkeit von einzelnen Kunden verringern, vor allem dort, wo Budgets für Auswertung unter Druck geraten.</td><td>Was geschähe, wenn unser größter Kunde sein Auswertungsbudget halbiert?</td></tr>
<tr><td><strong>Datengrundlage</strong></td><td>Kennzahlen einheitlich definieren und fehlende Zahlen nachtragen, vor allem für GREENBAY healthcare.</td><td>Welche Größen messen wir, und sind sie über die Gesellschaften hinweg vergleichbar?</td></tr>
</tbody></table></div>'''

SIGNALE = '''<div class="tabelle"><table>
<thead><tr><th>Signal</th><th class="z">Zeitpunkt</th><th>Was es anzeigen würde</th></tr></thead>
<tbody>
<tr><td>Referentenentwurf zu § 130b Abs. 1c SGB V</td><td class="z">bis Mitte 2027</td><td>Ob deutsche Erstattungsbeträge vertraulich bleiben können; ohne Entwurf gewönne die Evidenz für die Nutzenbewertung an Gewicht.</td></tr>
<tr><td>Deckungsangebote von Berufshaftpflichtversicherern</td><td class="z">bis Ende 2027</td><td>Ob Pfad A offensteht.</td></tr>
<tr><td>Harmonisierte Normen und Beginn der Hochrisikopflichten der KI-Verordnung</td><td class="z">Dez. 2027 oder Aug. 2028</td><td>Welche Nachweise für KI-gestützte Ergebnisse verlangt werden.</td></tr>
<tr><td>Anerkennungsregel für maschinell erzeugte Evidenz in der Nutzenbewertung</td><td class="z">offen</td><td>Ob KI-gestützte Evidenz im Verfahren nach § 35a SGB V verwendbar wird.</td></tr>
<tr><td>Überprüfung der US-Ausnahme für Generika; endgültige Regel zu GLOBE</td><td class="z">2026 bis 2027</td><td>Ob der US-Druck weitere Segmente erfasst.</td></tr>
<tr><td>Bearbeitungsdauer der Zugangsstellen im Gesundheitsdatenraum</td><td class="z">vor März 2031</td><td>Wie schnell die zusätzliche Datennachfrage ab 2031 bedient werden kann.</td></tr>
</tbody></table></div>'''

PLAN = zeitstrahl([
    (2027.49, "Mitte 2027", "Kennzahlen einheitlich", "intern", 3, "start"),
    (2027.99, "Ende 2027", "Versicherbarkeit geklärt", "intern", 2, "start"),
    (2028.49, "Mitte 2028", "Richtung je Gesellschaft", "intern", 1, "start"),
    (2028.99, "Ende 2028", "Datenlücken geschlossen", "intern", 0, "start"),
    (2026.74, "29. Sept. 2026", "US-Zoll für alle", "extern", 0, "start"),
    (2027.92, "2. Dez. 2027", "KI-VO Anhang III", "extern", 2, "start"),
    (2028.5, "30. Juni 2028", "§ 130b Abs. 1c endet", "extern", 1, "start"),
    (2029.05, "20. Jan. 2029", "Ende US-Nullsatz", "extern", 0, "start"),
    (2030.0, "2030", "Vorhaltevergütung voll", "extern", 1, "start"),
    (2031.2, "März 2031", "EHDS, zweite Stufe", "extern", 0, "end"),
], 2026, 2031.6, "Zeitfenster des strategischen Rahmens", achse=170)

TEILE.append(kapitel(7, "rahmen", "Der strategische Rahmen",
 "Die Kapitel 1 bis 6 führen zu einer gemeinsamen Richtung für den Verbund. Dieses Kapitel beschreibt sie, benennt die Voraussetzungen und die Handlungsfelder und zeigt, in welchem Zeitfenster sich die wichtigsten Fragen klären.",
 f'''<div class="prose">
<h3>Vom Befund zum Rahmen</h3>
<p>Jedes Kapitel hat mit einer Folgerung für den Verbund geendet. Zusammen ergeben sie ein Bild: Die Finanzierung des Gesundheitswesens trägt, die Nachfrage nach Evidenz wächst, aber der Preis für reine Auswertung fällt. Wert entsteht dort, wo jemand für ein Ergebnis einsteht.</p>
</div>
''' + abb("Die sechs Kapitel führen zu einer Richtung: vom Auswerten zum Einstehen",
          "Befunde und Folgerungen je Kapitel",
          FADEN,
          "Quelle: Kapitel 1 bis 6 dieses Papiers.") +
 f'''<div class="prose">
<h3>Die Richtung: vom Auswerten zum Einstehen</h3>
<p>Der Verbund würde seinen Wert künftig weniger aus Rechenarbeit ziehen als aus Ergebnissen, für die er einsteht. Die Standardauswertung verschwände nicht; sie würde billiger, stärker automatisiert und wäre eher Grundlage als Produkt. Das Produkt wäre das verantwortete Ergebnis.</p>
<h3>Zwei Pfade zur Orientierung</h3>
<p>Die Modellrechnung unterscheidet zwei Pfade. In <strong>Pfad A</strong> kann der Verbund für seine Ergebnisse haften, mit Versicherungsdeckung und Abnahmeverfahren. Der Außenumsatz stiege bis 2031 um rund 5 Prozent, der Deckungsbeitrag sänke um 15 Prozent. In <strong>Pfad B</strong> bliebe der Verbund bei der Standardauswertung. Der Außenumsatz fiele um rund 30 Prozent (Spanne minus 45 bis minus 20), der Deckungsbeitrag um 60 Prozent.</p>
<p>In Euro lägen die Pfade 2031 rund 5,1 Mio. € Außenumsatz auseinander: plus 0,7 Mio. € in Pfad A, minus 4,3 Mio. € in Pfad B. Die Pfade sind getrennt gerechnet und keine Ränder derselben Unsicherheit. Sie zeigen, wie viel von der Richtung abhängt, nicht, welcher Pfad eintritt.</p>
</div>
''' + abb("Zwischen den beiden Pfaden lägen 2031 rund 5,1 Mio. € Außenumsatz",
          "Veränderung 2031 gegenüber 2025 in Prozent, bezogen auf 14,48 Mio. € Außenumsatz",
          PFADE,
          "Quelle: Sitzung D, Stufe Markt des Verbunds, getrennt gerechnete Pfade.") +
 f'''<div class="prose">
<h3>Drei Voraussetzungen, die nur zusammen wirken</h3>
<ol class="empfehlung">
<li><div><strong>Eine nachvollziehbare Auswertungsstrecke.</strong> Jedes Ergebnis, für das der Verbund einsteht, müsste vom Rohdatum bis zur Aussage prüfbar sein, einschließlich der eingesetzten Modelle und ihres Versionsstands.</div></li>
<li><div><strong>Ein Abnahmestandard.</strong> Schriftlich festgelegt, was ein Ergebnis erfüllen muss, bevor es das Haus verlässt, und wer die Abnahme erklärt. Er müsste zu dem passen, was Aufsicht und Nutzenbewertung als Nachweis anerkennen.</div></li>
<li><div><strong>Eine Verantwortung mit Versicherungsdeckung.</strong> Eine Gesellschaft oder Person, die das Ergebnis vertraglich zusichert, und ein Berufshaftpflichtversicherer, der diese Zusicherung deckt.</div></li>
</ol>
<p>Fehlt eine der drei, trägt die Leistung mit Haftung nicht: Ein Abnahmestandard ohne Versicherung ist ein Versprechen ohne Deckung, und eine Versicherung ist ohne nachvollziehbare Auswertungsstrecke nicht zu bekommen.</p>
<h3>Fünf Handlungsfelder</h3>
<p>Innerhalb der Richtung lassen sich fünf Handlungsfelder unterscheiden. Sie gelten für alle Gesellschaften; welches Gewicht sie jeweils haben, hängt von der Ausgangslage ab (Kapitel 6). Die Leitfragen helfen, die eigene Position zu bestimmen.</p>
</div>
''' + abb("Fünf Handlungsfelder mit je einer Leitfrage für die Gesellschaften",
          "Handlungsfelder des strategischen Rahmens",
          FELDER,
          "Quelle: abgeleitet aus Kapitel 3 bis 6 dieses Papiers.") +
 f'''<div class="prose">
<h3>Zeitfenster und Signale</h3>
<p>Die Szenarien der US-Studie trennen sich erst nach 2027. Die Fragen, die über 2031 entscheiden, klären sich aber früher, weil sie an Gesetzgebungs-, Verfahrens- und Vergabetakten hängen, die der Verbund nicht steuert. Abbildung 20 zeigt diese äußeren Termine und darüber Orientierungsmarken, bis wann die Gesellschaften ihre Position geklärt haben sollten, damit Vorbereitungen noch wirken können. Die Marken sind keine Beschlusstermine; beschlossen wird in den dafür zuständigen Gremien.</p>
</div>
''' + abb("Die Orientierungsmarken des Verbunds liegen zwischen Mitte 2027 und Ende 2028, vor den wichtigsten äußeren Terminen",
          "Oben: Orientierungsmarken des Rahmens; unten: äußere Termine",
          PLAN,
          "Quelle: Sitzung D; Rechtsstand nach Proclamation 11020, KHAG, VO (EU) 2024/1689 und EHDS-Verordnung. Der Beginn der Hochrisikopflichten nach Anhang III ist umstritten (2. Dezember 2027 oder 2. August 2028).") +
 f'''<div class="prose">
<p>Welche Richtung sich tatsächlich durchsetzt, zeigen einige Signale, die sich beobachten lassen. Sie machen den Rahmen überprüfbar: Treten sie anders ein als hier angenommen, wäre der Rahmen anzupassen.</p>
</div>
''' + abb("Sechs Signale zeigen, ob die Annahmen des Rahmens tragen",
          "Beobachtungspunkte bis 2031",
          SIGNALE,
          "Quelle: Kapitel 1, 4 und 6 dieses Papiers; Sitzung D.")))

# ====================================================================== Anhang
GLOSSAR_HTML = '<dl class="glossar">' + "".join(
    f'<div id="g-{k}"><dt>{t}</dt><dd>{e}</dd></div>' for k, t, e in sorted(GLOSSAR, key=lambda g: g[1].lower())) + '</dl>'

TEILE.append(kapitel(None, "methode", "Methode, Grenzen, Begriffe, Quellen",
 "Woher die Zahlen kommen, wie sie zu lesen sind und wo sie nicht tragen.",
 f'''<div class="prose">
<h3>Wie die Zahlen entstanden sind</h3>
<p>Grundlage ist eine Szenariokonferenz, deren vierte Sitzung am 25. September 2026 stattfand. Hundert Fachrollen haben die US-Studie von Korinek u. a. auf Deutschland übertragen, entlang einer Wirkungskette mit fünf Stufen: Gesamtwirtschaft, Kranken- und Pflegekassen, Leistungserbringer, Pharma und der Markt des Verbunds. Jede Stufe gab einen Zentralwert mit Spanne an die nächste weiter. {N_KETTE} Einschätzungen bilden diese Kette, dazu acht Einschätzungen zu Europa und sechs zur Technik.</p>
<p><strong>Die Fachrollen sind KI-Agenten, keine befragten Menschen.</strong> Jede Rolle wurde von einem Sprachmodell eingenommen, mit einem festen Fragebogen, einem gemeinsamen Faktenstand und den Ergebnissen der vorigen Stufe. Die Einschätzungen sind deshalb als strukturierte Modellrechnung zu lesen, nicht als Expertenbefragung. Die Ist-Werte 2025 des Verbunds stammen aus den DATEV-Kontenblättern und sind gemessen.</p>

<h3>Grenzen</h3>
<p><strong>Die Endzahlen folgen vor allem aus deutschem Recht und deutschen Verträgen.</strong> Die US-Studie liefert den Rahmen der Fragen, nicht die Antworten. Die 420 Mrd. € GKV-Ausgaben etwa ergeben sich aus der Fortschreibung deutscher Regeln.</p>
<p><strong>Die Wahl des Szenarios stammt aus den USA.</strong> {round(100*SZEN["substantial"]/N_KETTE)} Prozent der Einschätzungen wählten das mittlere Szenario, obwohl die Autoren keine Wahrscheinlichkeiten angeben. Ein anderes Szenario würde die Zahlen verschieben, nach Einschätzung der Fachrollen aber nicht die Richtung.</p>
<p><strong>Die Studie rechnet bis 2030, dieses Papier bis 2031.</strong> Das zusätzliche Jahr bewegt auf der Einnahmenseite rund 42 Mrd. €, das Vier- bis Fünffache der gesamten KI-Wirkung auf die Beitragsbasis.</p>
<p><strong>Die Ergebnisse der Konferenz sind nicht abschließend geprüft.</strong> Eine interne Gegenprüfung fand sieben Rechen- und Zählfehler; alle wurden korrigiert, die Korrekturen aber nicht erneut geprüft. Für den Rückgang des Deckungsbeitrags nennen die Unterlagen drei Werte, 6,3, 15 und 25 Prozent; dieses Papier verwendet 15.</p>
<p><strong>Lesart.</strong> Werte für 2031 sind auf ihre Rundungsstufe genau zu lesen: 1.790 Mrd. € auf 10 Mrd., 420 Mrd. € auf 5 Mrd., 800 Mio. € auf 50 Mio., die Werte der Gesellschaften auf 5 Prozentpunkte. Spannen sind {B("intervall", "80-Prozent-Intervalle")}, Mittelwerte der Einschätzungen sind {B("median", "Mediane")}.</p>

<h3>Begriffe</h3>
</div>
{GLOSSAR_HTML}
<div class="prose">
<h3>Quellen</h3>
<ul>
<li>Korinek, A., Jones, C., Sacher, S., Cotter, T., McCrory, B.: <em>Economic Scenarios for Transformative AI</em>. The Anthropic Institute, Working Paper 2026-02.</li>
<li>Szenariokonferenz, Sitzung D, Rohdaten und Verfahrensbericht: <code>rohdaten/sitzung-d.json</code>, <code>30-Sitzung-D.md</code>; ausführliche Fassung mit allen Herleitungen: <code>29-Strategiepapier-2031.md</code>.</li>
<li>Gemeinsamer Faktenstand der Szenariokonferenz (<code>01-Briefing.md</code>): IAB-Prognosen März 2026, ifo-Konjunkturumfrage Juni 2026, BT-Drs. 21/7620, Draghi-Bericht.</li>
<li>GKV-Statistik KV45 und KJ1 2025; PKV-Verband, Zahlenbericht und Beitragsanpassung 2026.</li>
<li>Proclamation 11020, Federal Register 2026-06956; SGB V §§ 35a, 71, 130b; KHEntgG § 21; Krankenhausreformanpassungsgesetz; VO (EU) 2024/1689; Verordnung über den Europäischen Gesundheitsdatenraum.</li>
<li>DATEV-Kontenblätter 2025 der Gesellschaften des HIGL-Verbunds.</li>
</ul>
<p class="fuss" style="margin-top:2.4em;border-top:1px solid var(--rule);padding-top:1em">Erstellt mit Unterstützung von Künstlicher Intelligenz. Die Zahlen für 2031 sind Modellergebnisse und keine Prognosen; die Ist-Werte 2025 sind aus den Buchungsdaten gemessen. Das Papier beschreibt einen strategischen Rahmen und ersetzt keine Beschlüsse der zuständigen Gremien. HIGL-Verbund, Puschstraße 6a, 04103 Leipzig. Stand 26. September 2026, Fassung 2.0.</p>
</div>
'''))


# ====================================================================== Ausgabe
HTML = (f'<title>Die Haftungswende</title>\n<meta name="description" content="Strategiepapier des HIGL-Verbunds: Auswirkungen von KI bis 2031 auf Europa, Deutschland, das Gesundheitswesen und die Gesellschaften des Verbunds.">\n'
        f'{FONTS}\n<style>{CSS}</style>\n<main class="wrap">\n' + "\n".join(TEILE) + "\n</main>\n")

if __name__ == "__main__":
    ziel = os.path.join(HIER, "Die-Haftungswende.html")
    open(ziel, "w", encoding="utf-8").write(HTML)
    print(ziel, len(HTML), "Zeichen,", _abb[0], "Abbildungen")
