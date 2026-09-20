#!/usr/bin/env python3
"""Erzeugt workflow-sitzung-c.js: Runde 4 (Hebel und Leistungsprofile),
Runde 5 (Red Team und Verifikation), Runde 6 (Papier).

120 Aufrufe:
    5   Runde 4a  Hebelsatz, Leistungsprofile, Pruefung, Nachbesserung, zweite Pruefung
  100   Runde 4b  jede Rolle bewertet jeden Hebel und die Profile ihrer Bank
    6   Runde 5a  Red Team, sechs Angriffsauftraege
    3   Runde 5b  Verifikation der drei geschriebenen Teile, je ein fremder Teil
    6   Runde 6   drei Kapitel Teil 3, Zusammenzug, Verifikation, Schlussfassung

Abweichung von der Kostentabelle des Konzepts (121), bewusst und dokumentiert:
Dort stehen in Runde 5 zwoelf Aufrufe (6 Red Team + 3 Synthese + 3 Verifikation)
und in Runde 6 sechs (3 Syntheseteile + Zusammenzug + Verifikation + Schlussfassung).
Die drei Syntheseinstanzen sind darin doppelt gezaehlt - es sind dieselben drei.
Hier existieren sie einmal, als die drei Kapitel der Runde 6.

Zweite Abweichung: Teil 0, 1 und 2 des Papiers sind bereits geschrieben und geprueft
(22-, 23-, 24-*.md). Runde 6 schreibt sie nicht neu - die korrigierten Zahlen der
Zentraltabelle sollen nicht noch einmal durch ein Modell laufen. Sie schreibt Teil 3
und den Rahmen; die drei Verifikationsinstanzen pruefen die bestehenden Teile.

Alle Korrekturen aus Sitzung A, Sitzung B und den vier Fehlersuchen sind eingebaut:
  - korrigierte Bezugsgroessen und Zentraltabelle aus rohdaten/p3-tabelle.json
  - Deckung 48,9 Prozent, Kriterium gerissen - steht im Prompt, nicht im Nachwort
  - drei zurueckgezogene Guetemaße werden als zurueckgezogen uebergeben
  - Interessenpruefung als fuenfte Pruefung (Kriterium 22)
  - Ableitungsrichtung Engpass -> Profil, keine Anbieternamen (16-Marktschicht Paragraf 2)
"""
import json, pathlib, sys, collections

BASIS = pathlib.Path(__file__).resolve().parent
ROH = BASIS / 'rohdaten'
ZIEL = BASIS / 'workflow-sitzung-c.js'

QUELLEN = {'sa': ROH / 'sitzung-a.json', 'sb': ROH / 'sitzung-b.json',
           'na': ROH / 'nacharbeit.json', 'p3': ROH / 'p3-tabelle.json',
           'rost': ROH / 'roster.json'}
DOKS = {'teil0': '22-Teil-0-Gueltigkeit.md', 'teil1': '23-Teil-1-Deutschland.md',
        'teil2': '24-Teil-2-Europa.md', 'kanaele': '20-Durchgriffskanaele.md'}


def einzeilig(x):
    """Absaetze zu einer Zeile. Die Kartenbloecke im Prompt sind zeilenweise
    aufgebaut; ein Absatz im Antworttext zerlegte sonst die Karte."""
    return ' '.join(str(x or '').split())


def durchgriff(a):
    z = a['p1'] * a['p2'] / 100
    return round(abs(a['p3'] - a['p3_null']) / z, 2) if z else 0


def main():
    for p in QUELLEN.values():
        if not p.exists():
            sys.exit(f'fehlt: {p}')
    D = {k: json.loads(p.read_text(encoding='utf-8')) for k, p in QUELLEN.items()}
    for k, name in DOKS.items():
        p = BASIS / name
        if not p.exists():
            sys.exit(f'fehlt: {p}')
        D[k] = p.read_text(encoding='utf-8')

    R1 = {a['id']: a for a in D['sa']['runde1']}
    R3 = {a['id']: a for a in D['sb']['runde3']}
    ROST = {r['id']: r for r in D['rost']['rollen']}
    P3 = {f['id']: f for f in D['p3']}
    BANK = D['rost']['baenke']

    fehlend = [i for i in ROST if i not in R3]
    if fehlend:
        print(f'WARNUNG: {len(fehlend)} Rollen ohne Runde-3-Antwort: {fehlend}')

    # ---------------------------------------------------------- die hundert Rollen
    rollen = []
    for i in sorted(ROST):
        r, a1, a3 = ROST[i], R1[i], R1[i]
        t = R3.get(i, a1)
        rollen.append({
            'id': i, 'bank': r['bank'], 'bankName': r['bankName'], 'rolle': r['rolle'],
            'mandat': r['mandat'], 'blindstelle': r['blindstelle'], 'geruest': r['geruest'],
            'vzae': P3[i]['vzae'] if i in P3 else 0,
            'einrichtungsart': P3[i]['einrichtungsart'] if i in P3 else '',
            'p1': t['p1'], 'p2': t['p2'], 'p3': t['p3'], 'p3_null': t['p3_null'],
            'd': durchgriff(t),
            'p4': [t['p4_ki'], t['p4_demografie'], t['p4_strukturreform']],
            'p5': [t['p5_leistungserbringer'], t['p5_preis_beitrag'],
                   t['p5_abfluss_ausland'], t['p5_neue_leistung']],
            'hemmnis': a1['p2_hemmnis'], 'engpass': a3['a3_engpass'],
        })
        # Was nur in die Ableitungsprompts geht, steht dort und nicht noch einmal
        # in ROLLEN - die hundert Bewertungsprompts brauchen es nicht, und die
        # Doppelung kostete 120 KB Skript.
        rollen[-1]['_gross'] = {
            'engpass2': a3.get('a3_zweitnennung', ''),
            'sichtbar': einzeilig(a3.get('a3_woran_sichtbar', ''))[:400],
            'a1_norm': str(a1.get('a1_norm', ''))[:200],
            'position': einzeilig(a1['position'])[:800],
            # Runde 1 zum Vergleich und die Begruendung der Bewegung. Ohne beides
            # leitet die Syntheseinstanz aus zurueckgezogenen Aussagen ab - genau
            # das ist im ersten Anlauf am 20.09. passiert (sieben von acht Hebeln).
            'r1': {'p1': a1['p1'], 'p2': a1['p2'], 'p3': a1['p3'],
                   'p3_null': a1['p3_null'], 'd': durchgriff(a1)},
            # Zeilenumbrueche raus: sonst zerfaellt jede Karte im Prompt in
            # mehrere Bloecke und die Zuordnung Karte-zu-Begruendung geht verloren.
            'aenderung': einzeilig(t.get('aenderung', ''))[:900],
        }

    gross = {r['id']: r.pop('_gross') for r in rollen}
    for r in rollen:
        r['einrichtungsart'] = r['einrichtungsart'][:60]

    # ------------------------------------------------- Grundlage der Hebelableitung
    def bewegung(r):
        o = gross[r['id']]['r1']
        teile = []
        for k, name in (('p1', 'P1'), ('p2', 'P2'), ('p3', 'P3'), ('p3_null', 'P3_0'), ('d', 'D')):
            neu_, alt_ = (r[k], o[k])
            if neu_ != alt_:
                teile.append(f'{name} {alt_} -> {neu_}')
        return ', '.join(teile) if teile else 'keine Kernzahl bewegt'

    zeilen = []
    for r in rollen:
        g = gross[r['id']]
        zeilen.append(
            f"{r['id']} {r['bank']} {r['rolle']}\n"
            f"   RUNDE 3, MASSGEBLICH: P1 {r['p1']} | P2 {r['p2']} | P3 {r['p3']} | "
            f"P3_0 {r['p3_null']} | D {r['d']} | Hemmnis {r['hemmnis']} | Engpass {r['engpass']}\n"
            f"   BEWEGUNG gegenueber Runde 1: {bewegung(r)}\n"
            f"   WAS SICH GEAENDERT HAT UND WARUM (Runde 3): {g['aenderung']}\n"
            f"   ERSTPOSITION aus Runde 1, in Teilen ueberholt: {g['position'][:380]}")
    hebelbasis = '\n\n'.join(zeilen)
    bewegt = sum(1 for r in rollen if bewegung(r) != 'keine Kernzahl bewegt')

    dissens = '\n\n'.join(
        f"GRUPPE {n + 1} - Streitfrage: {d['streitfrage']}\n" + '\n'.join(
            f"  STREITPUNKT: {x['streitpunkt']}\n"
            f"    {x['karte_a']} gegen {x['karte_b']} (Baenke: {x['baenke']})\n"
            f"    Entscheidungsgroesse: {x['entscheidungsgroesse']}"
            for x in d['dissens'])
        for n, d in enumerate(D['sb']['dissens']))

    def norm(x):
        x = str(x).strip().lower()
        for a, b in (('\u00e4', 'ae'), ('\u00f6', 'oe'), ('\u00fc', 'ue'), ('\u00df', 'ss')):
            x = x.replace(a, b)
        return x

    def zaehl(schl):
        # Schreibweisen zusammenfuehren: 'Investitionsfaehigkeit' und
        # 'Investitionsfaehigkeit' mit Umlaut waren zwei Eintraege und haben das
        # zweithaeufigste Hemmnis des Panels unter das dritte sortiert.
        c = collections.Counter(norm(r[schl]) for r in rollen)
        return ', '.join(f'{k} {v}' for k, v in c.most_common(12))

    profilbasis = 'ENGPASSANGABEN ALLER HUNDERT ROLLEN (A3), nach Bank:\n\n' + '\n'.join(
        f"{r['id']} {r['bank']} ({r['bankName']}) {r['rolle']}\n"
        f"   Engpass: {r['engpass']} | zweitgenannt: {gross[r['id']]['engpass2']}\n"
        f"   woran sichtbar: {gross[r['id']]['sichtbar'][:300]}" for r in rollen)

    # ------------------------------------------------------------ Kernzahlen fuers Papier
    summe = sum(f['vzae'] for f in D['p3'])
    mit = sum(f['p3_vzae'] for f in D['p3'])
    ohne = sum(f['p3_null_vzae'] for f in D['p3'])
    tabelle = '\n'.join(
        f"{f['id']} {f['rolle']} | {f['einrichtungsart']} | {f['vzae']:.0f} VZAE | "
        f"P3 {f['p3_prozent']} % = {f['p3_vzae']:+.0f} | ohne KI {f['p3_null_prozent']} % = "
        f"{f['p3_null_vzae']:+.0f}{' | ZUSCHNITT KORRIGIERT: ' + str(f['begruendung'])[:120] if f.get('korrigiert') else ''}"
        for f in D['p3'])
    kern = {
        'felder': len(D['p3']), 'vzae': round(summe), 'deckung_prozent': 48.9,
        'mit_ki': round(mit), 'ohne_ki': round(ohne), 'ki_beitrag': round(mit - ohne),
        'tabelle': tabelle,
    }

    js = VORLAGE
    ersetzungen = (
        ('__ROLLEN__', rollen), ('__BEWEGT__', bewegt), ('__HEBELBASIS__', hebelbasis), ('__PROFILBASIS__', profilbasis),
        ('__DISSENS__', dissens), ('__KERN__', kern), ('__KANAELE__', D['kanaele']),
        ('__TEIL0__', D['teil0']), ('__TEIL1__', D['teil1']), ('__TEIL2__', D['teil2']),
        ('__BAENKE__', BANK),
        ('__VERTEILUNG__', f"Hemmnis (P2): {zaehl('hemmnis')}\nEngpass (A3): {zaehl('engpass')}"),
    )
    for marke, wert in ersetzungen:
        if marke not in js:
            sys.exit(f'Marke nicht in der Vorlage: {marke}')
        js = js.replace(marke, json.dumps(wert, ensure_ascii=False))
    ZIEL.write_text(js, encoding='utf-8')

    print(f'{ZIEL.name}: 120 Aufrufe, {round(len(js) / 1024)} KB')
    print(f'  Runde 4a   5  Hebelsatz, Leistungsprofile, Pruefung, Nachbesserung, zweite Pruefung')
    print(f'  Runde 4b {len(rollen):3d}  Bewertung je Rolle')
    print(f'  Runde 5    9  sechs Red Team, drei Verifikation')
    print(f'  Runde 6    6  drei Kapitel, Zusammenzug, Verifikation, Schlussfassung')
    print(f'  Zentraltabelle: {kern["felder"]} Felder, {kern["vzae"]} VZAE, '
          f'{kern["mit_ki"]:+d} mit KI / {kern["ohne_ki"]:+d} ohne KI / '
          f'KI-Beitrag {kern["ki_beitrag"]:+d}')
    print(f'  Rollen mit amtlicher Bezugsgroesse: {sum(1 for r in rollen if r["vzae"])} von {len(rollen)}')
    print(f'  Rollen, die in Runde 3 eine Kernzahl bewegt haben: {bewegt} von {len(rollen)}')


VORLAGE = r'''export const meta = {
  name: 'sitzung-c-runde-4-bis-6',
  description: 'Sitzung C: Hebel und Leistungsprofile aus der Tafel, Bewertung durch hundert Rollen, Red Team, Verifikation und das Strategiepapier 2031',
  phases: [
    { title: 'Hebelsatz', detail: 'Hebel und Leistungsprofile aus Dissens-, Positions- und Engpasskarten, dazu die Pruefung der Herleitung' },
    { title: 'Bewertung', detail: 'Hundert Rollen bewerten jeden Hebel und die Profile ihrer Bank' },
    { title: 'Angriff', detail: 'Sechs Red-Team-Instanzen und drei Verifikationen der geschriebenen Teile' },
    { title: 'Papier', detail: 'Drei Kapitel fuer Teil 3, Zusammenzug, Verifikation, Schlussfassung' },
  ],
}

const ROLLEN = __ROLLEN__
const BEWEGT = __BEWEGT__
const HEBELBASIS = __HEBELBASIS__
const PROFILBASIS = __PROFILBASIS__
const DISSENS = __DISSENS__
const KERN = __KERN__
const KANAELE = __KANAELE__
const TEIL0 = __TEIL0__
const TEIL1 = __TEIL1__
const TEIL2 = __TEIL2__
const BAENKE = __BAENKE__
const VERTEILUNG = __VERTEILUNG__

/* Der Gueltigkeitsstand, kurz. Er steht in jedem Prompt, der eine Zahl berichtet -
   nicht als Nachwort, sondern als Bedingung. */
const GUELTIG = `GEMESSENE GUELTIGKEIT DES LAUFS (24 vorab festgelegte Abbruchkriterien, Stand nach Sitzung B und fuenf Fehlersuchen):
  ERFUELLT: Pruefschaerfe 97 % bereinigt (29 von 30; die rohen 80 % waren ein Artefakt - zehn der vierzig gesetzten Fehler multiplizierten eine Null und existierten nie) | Rechenweghaltbarkeit 94,2 % | Geruestabhaengigkeit 0,00-0,11 | Schemafestigkeit 100 von 100 | Divergenzerhalt 6 von 6, niedrigster Wert 0,81 | Einwandhaltbarkeit 100 % | Fremdbezug 8 % | Quellenunabhaengigkeit 4 von 100 Karten interessengekennzeichnet
  GERISSEN: Bezugsgroessendeckung 48,9 % statt 70 % | Modellabhaengigkeit 3 von 6 (auf den verankerten Rollen 6 von 6) | Zuschnittstreue 10 von 16
  ZURUECKGEZOGEN, weil sie nichts messen: Attributionskonsistenz (Formel und Toleranz stehen woertlich im Rollenauftrag - gemessen wurde Anweisungstreue) | Modellabhaengigkeit in Runde 3 (beide Arme sahen dieselben Runde-1-Werte, der Kontrollarm reproduzierte sie in 20 von 20 Faellen exakt)

DIE ZENTRALTABELLE, korrigiert: ${KERN.felder} Felder, ${KERN.vzae} Vollzeitaequivalente, ${KERN.deckung_prozent} % des Kontrollrahmens von 4,404 Mio.
  Personalbedarf 2031 mit KI ${KERN.mit_ki > 0 ? '+' : ''}${KERN.mit_ki} VZAE | ohne KI ${KERN.ohne_ki > 0 ? '+' : ''}${KERN.ohne_ki} | KI-Beitrag ${KERN.ki_beitrag} VZAE.
  Sechs der sechzehn Felder trugen zuvor die ganze Einrichtungsart statt ihres Ausschnitts, im Extremfall um den Faktor 339. Die Werte oben sind die korrigierten.`

const ZWEI_REGELN = `ZWEI REGELN, DIE NICHT VERHANDELBAR SIND:
1. Was keine Kartennummer traegt, steht nicht im Papier. Kartennummern sind die Rollen-IDs (A01 bis N01), die Faktenblattnummern (R01 bis R10) und die Gruppennummern der Dissensprotokolle. Eine Aussage ohne Nummer ist zu streichen, nicht zu belegen.
2. Alle Aussagen ueber 2031, alle Modellergebnisse und alle Gesetzentwuerfe stehen im KONJUNKTIV. Das Papier beschreibt, was ein strukturiertes Argumentmodell ergeben hat, nicht was sein wird.`

const WAS_ES_NICHT_IST = `WAS DIESES PAPIER NICHT IST: Die Agenten sind Sprachmodelle mit Rollendossiers. Das Ergebnis ist ein strukturiertes Argumentmodell mit benannten Quellen, gemessenen Gueltigkeitsgrenzen und offengelegten Dissenspunkten - keine Expertenbefragung, keine Prognose und keine Legitimationsgrundlage fuer eine politische Entscheidung. Nicht besetzt sind unter anderem Zahnmedizin, Augenoptik und Hoerakustik, Heilmittelerbringer, Reha-Kliniken, Transportwesen, Kur- und Vorsorgeeinrichtungen, betriebliche Gesundheitsversorgung, Praeventionsanbieter und die gesamte Veterinaer- und One-Health-Perspektive.`

/* ============================================ Runde 4a - Hebel und Leistungsprofile */

phase('Hebelsatz')

const S_HEBEL = {
  type: 'object',
  properties: {
    hebel: {
      type: 'array', minItems: 5, maxItems: 8,
      items: {
        type: 'object',
        properties: {
          id: { type: 'string', description: 'H1 bis H8' },
          titel: { type: 'string' },
          was: { type: 'string', description: 'was genau getan wuerde, in einem Satz und operativ - nicht als Zielbeschreibung' },
          adressat: { type: 'string', enum: ['Bund', 'Land', 'Selbstverwaltung', 'EU', 'Traeger'] },
          instrument: { type: 'string', enum: ['Gesetz', 'Richtlinie', 'Verguetungsregel', 'Investition', 'Tarifvertrag'] },
          rechtsgrundlage: { type: 'string', description: 'die Norm, die geaendert oder geschaffen wuerde - aus dem Kanalregister, wenn moeglich' },
          baenke: { type: 'array', items: { type: 'string' }, description: 'betroffene Baenke, Buchstaben' },
          karten: { type: 'array', minItems: 2, items: { type: 'string' }, description: 'die Kartennummern, aus denen dieser Hebel hergeleitet ist' },
          herleitung: { type: 'string', description: 'welcher Dissens oder welche Position ihn erzwingt - woertlich an den genannten Karten' },
          groesse: { type: 'string', description: 'welche der erhobenen Groessen er bewegen soll: P1, P2, P3, D, P4 oder P5' },
        },
        required: ['id', 'titel', 'was', 'adressat', 'instrument', 'rechtsgrundlage', 'baenke', 'karten', 'herleitung', 'groesse'],
      },
    },
    nicht_hergeleitet: { type: 'string', description: 'welche naheliegenden Hebel du NICHT aufgenommen hast, weil keine Karte sie traegt' },
  },
  required: ['hebel', 'nicht_hergeleitet'],
}

const S_PROFIL = {
  type: 'object',
  properties: {
    profile: {
      type: 'array', minItems: 6, maxItems: 8,
      items: {
        type: 'object',
        properties: {
          id: { type: 'string', description: 'L1 bis L8' },
          titel: { type: 'string', description: 'die Leistung, nicht der Anbieter' },
          leistung: { type: 'string', description: 'was diese Instanz taete, operativ und ohne jeden Anbieter-, Marken- oder Produktnamen' },
          engpass: { type: 'string', description: 'welcher A3-Engpass geloest wird' },
          karten: { type: 'array', minItems: 3, items: { type: 'string' }, description: 'die A3-Karten, aus denen das Profil hergeleitet ist' },
          baenke: { type: 'array', items: { type: 'string' }, description: 'Baenke, fuer die es gilt - nur diese bewerten es' },
          wer_zahlt: { type: 'string', description: 'aus welchem Topf, mit Bezug auf die A2-Verteilung - "gar kein Topf" ist eine zulaessige und haeufige Antwort' },
          warum_nicht_schon_da: { type: 'string', description: 'wenn der Engpass so breit genannt wird: warum loest ihn heute niemand?' },
        },
        required: ['id', 'titel', 'leistung', 'engpass', 'karten', 'baenke', 'wer_zahlt', 'warum_nicht_schon_da'],
      },
    },
  },
  required: ['profile'],
}

const [hebelsatz, profilsatz] = await parallel([
  () => agent(
`Du bist die Syntheseinstanz der Szenariokonferenz 2031. Du hast keine eigene Position zur Sache, keine Stimme und kein Portfolio.

DEINE AUFGABE: Leite aus der Tafel FUENF BIS ACHT HEBEL ab.

Ein Hebel ist etwas, das der Staat, die EU, die Selbstverwaltung oder ein Traeger TUT. Er wird nicht erfunden, sondern hergeleitet: Jeder Hebel traegt die Kartennummern, aus denen er folgt, und die Herleitung muss an dem haengen, was auf diesen Karten tatsaechlich steht.

DIE SPERRE, die das Verfahren ueberhaupt erst begruendet: Eine von hundert Rollen haelt die TECHNIK fuer den Engpass. Die anderen 99 nennen Entscheidung, bedienendes Personal, Daten oder Recht. Ein Hebel, der Technik beschafft, adressiert damit den Engpass von einem Prozent des Panels. Das ist zulaessig, muss aber begruendet sein.

${VERTEILUNG}

DIE WICHTIGSTE REGEL DIESES AUFRUFS - lies sie, bevor du irgendeine Zahl abschreibst:

DIE WERTE DER RUNDE 3 SIND MASSGEBLICH, NICHT DIE DER RUNDE 1. Zwischen beiden Erhebungen lag die Gruppendiskussion, und ${BEWEGT} von hundert Rollen haben danach mindestens eine Kernzahl geaendert. Mehrere haben die Aussage, an der ein Streitpunkt haengt, AUSDRUECKLICH ZURUECKGEZOGEN - mit Begruendung, in ihrer eigenen Karte. Ein Hebel, der auf einer zurueckgezogenen Aussage steht, ist wertlos, und zwar unabhaengig davon, wie gut er klingt.

Die Dissensprotokolle unten zitieren durchgaengig die ERSTWERTE der Runde 1. Sie sind das Protokoll einer Diskussion, die stattgefunden hat - eine Quelle fuer Streitpunkte, KEINE Zahlenquelle. Fuer jede Karte, die du zitierst, gilt: Gleiche die Zahl gegen die Zeile "RUNDE 3, MASSGEBLICH" derselben Rolle ab und lies den Absatz "WAS SICH GEAENDERT HAT UND WARUM". Wo beides auseinanderfaellt, gewinnt Runde 3. Wo eine Rolle ihre Aussage zurueckgenommen hat, ist sie zurueckgenommen.

DIE DISSENSPUNKTE DER FUENF GRUPPEN - hier zerfiel das Panel, und hier liegen die Hebel. Die Zahlen darin sind Runde-1-Stand:

${DISSENS}

DIE DURCHGRIFFSKANAELE - die Normen, die mindestens drei Rollen aus mindestens zwei Baenken UNABHAENGIG genannt haben. Sie sind der Ertrag des Panels und die erste Quelle fuer die Rechtsgrundlage eines Hebels. Die 16 Normen, die bereits in einem Faktenblatt standen, sind dort ausgewiesen und schwaecher:

${KANAELE}

DIE HUNDERT POSITIONEN MIT IHREN ZAHLEN:

${HEBELBASIS}

${GUELTIG}

SIEBEN REGELN:
1. JEDE ZAHL, DIE DU ZITIERST, IST EINE RUNDE-3-ZAHL. Wenn du eine Zahl aus einem Dissensprotokoll uebernimmst, ohne sie gegen die Runde-3-Zeile abzugleichen, ist der Hebel ungueltig.
2. Jeder Hebel nennt eine GROESSE, die er bewegen soll - P1, P2, P3, D, P4 oder P5. Ein Hebel, der keine der erhobenen Groessen bewegt, gehoert nicht in dieses Papier.
3. Jeder Hebel nennt die RECHTSGRUNDLAGE, die geaendert oder geschaffen wuerde. "Man muesste" ist kein Instrument.
4. Kein Hebel darf ein Leistungsprofil sein. Wenn ein Externer es anbieten koennte, ist es kein Hebel.
5. JEDE KARTE, DIE EINEN BESTANDTEIL DES HEBELS TRAEGT, GEHOERT IN DIE KARTENLISTE - auch eine Gegeneinwandkarte, aus der ein einzelner Bestandteil stammt. Eine Herleitung, die eine nicht gelistete Karte braucht, ist unvollstaendig.
6. DIE HAEUFIGSTEN HEMMNISSE DES PANELS musst du abdecken oder ihr Fehlen begruenden. Wenn eine der drei groessten Hemmniskategorien in keinem Hebel vorkommt, steht die Begruendung dafuer unter "nicht_hergeleitet" - eine Luecke ohne Begruendung ist ein Fehler, keine Auswahl.
7. Halte fest, welche naheliegenden Hebel du NICHT aufgenommen hast, weil keine Karte sie traegt. Diese Liste ist so wichtig wie die Hebel selbst.`,
    { label: 'Hebelsatz', phase: 'Hebelsatz', schema: S_HEBEL }),

  () => agent(
`Du bist die Syntheseinstanz der Szenariokonferenz 2031 fuer die Leistungsschicht. Du hast keine eigene Position, keine Stimme und - das ist der Kern deines Auftrags - KEIN PORTFOLIO. Du kennst kein Angebot und keinen Anbieter.

DEINE AUFGABE: Leite aus den A3-Engpassangaben des Panels SECHS BIS ACHT LEISTUNGSPROFILE ab.

Ein Leistungsprofil ist etwas, das ein EXTERNER anbieten koennte - im Unterschied zum Hebel, den der Staat oder die Selbstverwaltung zieht.

DREI KONSTRUKTIONSREGELN, ohne die der ganze Block wertlos waere:
1. KEIN ANBIETERNAME, KEINE MARKE, KEIN PRODUKTNAME. Formuliert wird die Leistung, nicht der Anbieter - also die Taetigkeit und ihr Ergebnis, nie wer sie ausuebt. Ein Profil mit einem Namen darin ist ungueltig; ebenso eine Umschreibung, die nur auf einen einzigen Marktteilnehmer passen kann.
   Zur Bauform, bewusst aus einem fremden Feld genommen, damit du sie nicht abschreibst: "eine Instanz, die den Nachweis der Wartungsfaehigkeit einer Anlage gegenueber der Genehmigungsbehoerde fuehrt" - Taetigkeit, Gegenstand, Adressat der Leistung, kein Name. Uebertrage die BAUFORM auf die Engpaesse unten, nicht den Inhalt: ein Profil, das die Formulierung dieses Beispiels wiederholt, ist nicht aus den Karten abgeleitet, sondern aus diesem Auftrag.
2. DIE RICHTUNG IST BINDEND: vom Engpass zum Profil, nie vom Portfolio zum Profil. Wo dreissig Felder "Daten" als Engpass nennen, entsteht ein Profil, das Datenzugang loest; wo zwanzig "Recht" nennen, eines, das Konformitaet herstellt. Du kannst nicht bestaetigen, was jemand ohnehin verkauft, weil du es nicht kennst - und genau darin liegt der Wert dieser Ableitung.
3. Jedes Profil traegt die A3-Kartennummern, auf denen es beruht, und die Baenke, fuer die es gilt. Dabei gilt hart:
   - JEDE zitierte Karte muss den Engpass, den du nennst, TATSAECHLICH als A3-Erstnennung tragen. Eine Karte mit einem anderen Erstengpass ist entweder zu streichen oder als Zweitnennung ausdruecklich so zu kennzeichnen.
   - EINE PANELSTATISTIK IST KEIN BELEG FUER DIE HERLEITUNG. Die Karten sind der Beleg. Wenn du eine Panelzahl nennst ("29 Nennungen"), muss sie zu den Karten passen, die du zitierst - sonst belegst du deinen Engpass mit einer Statistik, deren Faelle gar nicht in deiner Kartenliste stehen.
   - DIE BAENKELISTE MUSS VOLLSTAENDIG SEIN. Jede Bank, aus der eine zitierte Karte stammt, gehoert hinein. Die Baenkeangabe ist das Mass fuer die feldeuebergreifende Deckung; eine unvollstaendige Liste schoent sie.

DIE HAERTESTE FRAGE, die du je Profil beantworten musst: Wenn dieser Engpass so breit genannt wird - warum loest ihn heute niemand? Wer darauf keine Antwort hat, beschreibt kein Geschaeft, sondern einen Wunsch. Moegliche Antworten: es gibt keinen Rechnungsempfaenger (30 von 100 Rollen nennen "gar kein Topf" als Finanzierungsquelle), die Rechtslage verbietet es, die Daten sind nicht abtretbar, die Ersparnis faellt bei jemand anderem an als die Kosten.

${VERTEILUNG}

${PROFILBASIS}

${GUELTIG}`,
    { label: 'Leistungsprofile', phase: 'Hebelsatz', schema: S_PROFIL }),
])

let HEBEL = (hebelsatz && hebelsatz.hebel) || []
let PROFILE = (profilsatz && profilsatz.profile) || []
log(`Runde 4a: ${HEBEL.length} Hebel, ${PROFILE.length} Leistungsprofile`)

/* ------------------------------------------- Runde 4a - Pruefung der Herleitung */

const S_PRUEF4 = {
  type: 'object',
  properties: {
    beanstandungen: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          gegenstand: { type: 'string', description: 'H1 bis H8 oder L1 bis L8' },
          art: { type: 'string', enum: ['karte_traegt_nicht', 'anbietername', 'portfolio_richtung', 'keine_groesse', 'hebel_ist_profil', 'sonstiges'] },
          was: { type: 'string', description: 'was auf der zitierten Karte tatsaechlich steht und warum es die Aussage nicht traegt' },
          schwere: { type: 'string', enum: ['hart', 'weich'] },
        },
        required: ['gegenstand', 'art', 'was', 'schwere'],
      },
    },
    gedeckt: { type: 'array', items: { type: 'string' }, description: 'Hebel und Profile, deren Herleitung traegt' },
    fehlend: { type: 'string', description: 'welcher breit belegte Engpass oder Dissens in keinem Hebel und keinem Profil vorkommt' },
  },
  required: ['beanstandungen', 'gedeckt', 'fehlend'],
}

const promptPruef = (H, P) =>
`Du bist die Pruefinstanz der Runde 4. Du pruefst die Herleitung von Hebeln und Leistungsprofilen gegen die Karten, aus denen sie hergeleitet sein sollen. Du schreibst nichts um - du meldest zurueck.

PRUEFE GENAU FUENF DINGE, sonst nichts:
1. TRAEGT DIE KARTE? Steht auf jeder zitierten Karte tatsaechlich das, was der Hebel oder das Profil ihr zuschreibt? Eine Karte, die etwas Anderes oder Schwaecheres sagt, ist eine harte Beanstandung.
2. ANBIETERNAME? Enthaelt ein Leistungsprofil einen Anbieter-, Marken- oder Produktnamen - auch verdeckt, etwa als unverwechselbare Beschreibung eines bestimmten Marktteilnehmers? Das ist hart.
3. RICHTUNG? Liest sich ein Profil so, als sei es aus einem Angebot rueckwaerts gebaut statt aus dem Engpass vorwaerts? Kennzeichen: Der Engpass ist nachgereicht, die Leistung ist praeziser beschrieben als der Bedarf, oder die zitierten A3-Karten nennen einen anderen Engpass als das Profil.
4. GROESSE? Nennt jeder Hebel eine der erhobenen Groessen - P1, P2, P3, D, P4, P5 - und ist plausibel, dass er sie bewegt?
5. INTERESSE? Hat die zitierte Quelle oder die zitierte Rolle ein eigenes Interesse an genau der Aussage, die ihr zugeschrieben wird? Das macht die Aussage nicht falsch, aber sie ist zu kennzeichnen.

DIE HEBEL:
${JSON.stringify(H, null, 1)}

DIE LEISTUNGSPROFILE:
${JSON.stringify(P, null, 1)}

DIE DISSENSPUNKTE, aus denen die Hebel stammen sollen:
${DISSENS}

DIE ENGPASSANGABEN, aus denen die Profile stammen sollen:
${PROFILBASIS}

Nenne zum Schluss, welcher breit belegte Engpass oder Dissens in KEINEM Hebel und KEINEM Profil vorkommt. Eine Luecke ist ein Befund.`

/* Die Pruefung braucht zusaetzlich die Runde-3-Lage, sonst kann sie nicht
   feststellen, ob eine zitierte Karte ihre Aussage inzwischen zurueckgezogen hat.
   Genau das war der Befund des ersten Anlaufs. */
const PRUEFKONTEXT = `

DIE HUNDERT KARTEN MIT IHREN RUNDE-3-WERTEN, DER BEWEGUNG GEGENUEBER RUNDE 1 UND DER BEGRUENDUNG:
${HEBELBASIS}`

const pruefung4 = await agent(promptPruef(HEBEL, PROFILE) + PRUEFKONTEXT,
  { label: 'Pruefung der Herleitung', phase: 'Hebelsatz', schema: S_PRUEF4 })

const HART = ((pruefung4 && pruefung4.beanstandungen) || []).filter(b => b.schwere === 'hart')
log(`Pruefung Runde 4a: ${(pruefung4 && pruefung4.beanstandungen || []).length} Beanstandungen, davon ${HART.length} hart`)

/* --------------------------------------------- Runde 4a - die Nachbesserung */

const befundtext = pr => ((pr && pr.beanstandungen) || []).map(b =>
  `[${b.schwere.toUpperCase()}] ${b.gegenstand} (${b.art})\n   ${b.was}`).join('\n\n')

const S_NACH = {
  type: 'object',
  properties: {
    hebel: S_HEBEL.properties.hebel,
    profile: S_PROFIL.properties.profile,
    geaendert: { type: 'string', description: 'was du je Beanstandung geaendert hast' },
    nicht_geaendert: { type: 'string', description: 'welche Beanstandung du zurueckweist und warum - mit Beleg' },
  },
  required: ['hebel', 'profile', 'geaendert', 'nicht_geaendert'],
}

const nachbesserung = await agent(
`Du bist die Syntheseinstanz der Runde 4. Deine Ableitung ist geprueft worden, und die Pruefung hat Beanstandungen erhoben. Du lieferst jetzt den BEREINIGTEN Satz aus Hebeln und Leistungsprofilen.

DIE BEANSTANDUNGEN:

${befundtext(pruefung4)}

WAS IN KEINEM HEBEL UND KEINEM PROFIL VORKOMMT:
${(pruefung4 && pruefung4.fehlend) || '(nichts gemeldet)'}

WAS GEDECKT IST UND SO BLEIBEN KANN:
${((pruefung4 && pruefung4.gedeckt) || []).join('\n')}

DEINE AUFGABE, und sie ist eng:

1. JEDE HARTE BEANSTANDUNG WIRD BEHOBEN. Bei "karte_traegt_nicht" heisst das: entweder du ersetzt die Zahl durch den Runde-3-Wert und schreibst die Herleitung darauf um, oder du tauschst die tragende Karte gegen eine, die die Aussage wirklich traegt, oder du streichst den Hebel. Einen Hebel zu streichen ist eine vollwertige Antwort - fuenf getragene Hebel sind mehr wert als acht, von denen drei auf zurueckgezogenen Aussagen stehen.
2. DIE LUECKE WIRD GESCHLOSSEN ODER BEGRUENDET. Wenn ein breit belegtes Hemmnis in keinem Hebel vorkommt, leite einen Hebel dafuer ab - aber nur, wenn die Karten ihn tragen. Wenn sie es nicht tun, sage das unter "nicht_geaendert" mit Beleg.
3. EINE BEANSTANDUNG ZURUECKWEISEN IST ERLAUBT, aber nur mit Beleg aus den Karten. "Ich sehe das anders" ist keine Zurueckweisung.
4. Was gedeckt ist, laesst du stehen. Du schreibst nicht um, was haelt.

DU LIEFERST DEN VOLLSTAENDIGEN SATZ, nicht nur die Aenderungen: alle Hebel und alle Profile, die danach gelten sollen, im selben Format wie zuvor.

${GUELTIG}

=============== DEINE BISHERIGEN HEBEL ===============
${JSON.stringify(HEBEL, null, 1)}

=============== DEINE BISHERIGEN PROFILE ===============
${JSON.stringify(PROFILE, null, 1)}

=============== DIE DISSENSPUNKTE (Zahlen darin sind Runde-1-Stand) ===============
${DISSENS}

=============== DIE DURCHGRIFFSKANAELE ===============
${KANAELE}

=============== DIE ENGPASSANGABEN ===============
${PROFILBASIS}

=============== DIE HUNDERT KARTEN, RUNDE 3 MASSGEBLICH ===============
${HEBELBASIS}`,
  { label: 'Nachbesserung', phase: 'Hebelsatz', schema: S_NACH })

if (nachbesserung && nachbesserung.hebel && nachbesserung.hebel.length) HEBEL = nachbesserung.hebel
if (nachbesserung && nachbesserung.profile && nachbesserung.profile.length) PROFILE = nachbesserung.profile
log(`Nachbesserung: ${HEBEL.length} Hebel, ${PROFILE.length} Profile`)

const pruefung4b = await agent(promptPruef(HEBEL, PROFILE) + PRUEFKONTEXT,
  { label: 'Pruefung nach der Nachbesserung', phase: 'Hebelsatz', schema: S_PRUEF4 })

const HART2 = ((pruefung4b && pruefung4b.beanstandungen) || []).filter(b => b.schwere === 'hart')
log(`Zweite Pruefung: ${(pruefung4b && pruefung4b.beanstandungen || []).length} Beanstandungen, davon ${HART2.length} hart (vorher ${HART.length})`)
if (HART2.length) log(`ACHTUNG: ${HART2.map(b => b.gegenstand).join(', ')} tragen weiterhin einen harten Befund - er gehoert ausgewiesen, nicht verschwiegen`)

/* ==================================================== Runde 4b - die Bewertung */

phase('Bewertung')

const hebelText = HEBEL.map(h => `${h.id} ${h.titel}
   was: ${h.was}
   Adressat ${h.adressat} | Instrument ${h.instrument} | Rechtsgrundlage ${h.rechtsgrundlage} | bewegen soll er ${h.groesse}
   hergeleitet aus ${(h.karten || []).join(', ')}: ${h.herleitung}`).join('\n\n')

const profilFuer = bank => PROFILE.filter(p => (p.baenke || []).includes(bank))
const profilText = ps => ps.map(p => `${p.id} ${p.titel}
   Leistung: ${p.leistung}
   loest den Engpass: ${p.engpass} | zahlen wuerde: ${p.wer_zahlt}
   hergeleitet aus ${(p.karten || []).join(', ')}
   warum es das heute nicht gibt: ${p.warum_nicht_schon_da}`).join('\n\n')

const S_BEWERTUNG = {
  type: 'object',
  properties: {
    hebel: {
      type: 'array', minItems: 1,
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          urteil: { type: 'string', enum: ['wirkt', 'wirkt nicht', 'schadet'] },
          mechanismus: { type: 'string', description: 'ueber welchen Weg er in DEINEM Feld wirkt oder nicht wirkt - konkret, nicht allgemein' },
          nebenwirkung: { type: 'string', description: 'was er in deinem Feld ausserdem ausloest' },
          kippbedingung: { type: 'string', description: 'der Umstand, unter dem sich dein Urteil umkehrt' },
          groesse: { type: 'string', description: 'um wieviel er deine eigene Zahl bewegte - P2 oder P3 in Punkten, mit Vorzeichen; "gar nicht" ist zulaessig' },
        },
        required: ['id', 'urteil', 'mechanismus', 'nebenwirkung', 'kippbedingung', 'groesse'],
      },
    },
    profile: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          urteil: { type: 'string', enum: ['wirkt', 'wirkt nicht', 'schadet'] },
          mechanismus: { type: 'string' },
          wer_verliert: { type: 'string', description: 'wer in deinem Feld schlechter dastuende, wenn es dieses Angebot gaebe' },
          kippbedingung: { type: 'string' },
        },
        required: ['id', 'urteil', 'mechanismus', 'wer_verliert', 'kippbedingung'],
      },
    },
    fehlender_hebel: { type: 'string', description: 'was dein Feld braeuchte und in keinem der Hebel vorkommt - oder ausdruecklich: nichts' },
  },
  required: ['hebel', 'profile', 'fehlender_hebel'],
}

function promptBewertung(r) {
  const ps = profilFuer(r.bank)
  const basis = r.vzae
    ? `Deine Bezugsgruppe: ${r.einrichtungsart}, ${r.vzae} Vollzeitaequivalente. Dein P3 von ${r.p3} % entspricht dort ${Math.round(r.vzae * r.p3 / 100)} Vollkraeften.`
    : `Fuer dein Feld weist die amtliche Statistik keine Vollzeitaequivalente aus. Rechne in Prozentpunkten gegen die von dir benannte Bezugsgruppe, nicht in Vollkraeften.`
  return `Du bist im Rollendossier ${r.id}: ${r.rolle}, Bank ${r.bank} (${r.bankName}).
Dein Mandat: ${r.mandat}.
Deine bekannte Blindstelle: ${r.blindstelle}. Sie zu kennen heisst nicht, sie zu verlassen - antworte aus deinem Mandat.

Die Konferenz hat zwei Erhebungen und eine Gruppendiskussion hinter sich. DEINE ZAHLEN nach der Diskussion:
P1 ${r.p1} % technisch ersetzbare Arbeitszeit | P2 ${r.p2} % davon bis 2031 wirksam | P3 ${r.p3} % Personalbedarf 2031 | ohne KI ${r.p3_null} % | Durchgriff D ${r.d}
P4 Ursachen: KI ${r.p4[0]} / Demografie ${r.p4[1]} / Strukturreform ${r.p4[2]}
P5 Verbleib: Erbringer ${r.p5[0]} / Preis und Beitrag ${r.p5[1]} / Abfluss ins Ausland ${r.p5[2]} / neue Leistung ${r.p5[3]}
Dein Hemmnis war ${r.hemmnis}, dein Engpass ${r.engpass}.
${basis}

Jetzt wird zum ersten Mal GEHANDELT statt gemessen. Vor dir liegen ${HEBEL.length} Hebel - Dinge, die Staat, EU, Selbstverwaltung oder Traeger taeten - und ${ps.length} Leistungsprofile, die deine Bank betreffen: Dinge, die ein Externer anboete.

DIE HEBEL - jeden einzelnen bewerten:

${hebelText}

DIE LEISTUNGSPROFILE FUER BANK ${r.bank}${ps.length ? '' : ' - keine; dann lass das Feld leer'}:

${ps.length ? profilText(ps) : '(keine)'}

DEINE AUFGABE: Zu jedem Hebel und jedem Profil ein Urteil - wirkt, wirkt nicht, oder schadet - FUER DEIN FELD, nicht fuer das Gesundheitswesen im Ganzen.

VIER REGELN:
1. "SCHADET" IST DIE WERTVOLLSTE ANTWORT. Ausgewertet wird nicht, wie viele Felder zustimmen, sondern in welchen Feldern ein Hebel schadet und warum. Zustimmung ist billig; ein begruendeter Einwand aus einem eigenen Feld ist teuer und selten. Wenn ein Hebel deinem Feld schadet, sage es und nenne den Weg.
2. JEDES URTEIL BRAUCHT EINE KIPPBEDINGUNG - den Umstand, unter dem es sich umkehrt. Ein Urteil ohne Kippbedingung ist eine Meinung.
3. DER MECHANISMUS MUSS AUS DEINEM FELD KOMMEN. "Buerokratieabbau hilft immer" ist kein Mechanismus. "Die Verguetungsregel X liesse den Aufwand Y erstmals abrechenbar werden, und erst damit kaeme Z in mein Budget" ist einer.
4. BEZIFFERE, WO DU KANNST: um wieviele Punkte bewegte der Hebel dein eigenes P2 oder P3? "Gar nicht" ist eine vollwertige und haeufig richtige Antwort - 99 von 100 Rollen halten die Technik nicht fuer den Engpass, und ein Hebel, der am Engpass vorbeigeht, bewegt nichts.

Bei den Profilen zusaetzlich: WER IN DEINEM FELD STUENDE SCHLECHTER DA, wenn es dieses Angebot gaebe? Ein Profil ohne Verlierer ist nicht geprueft, sondern unbeachtet.

Zum Schluss: Was braeuchte dein Feld, das in KEINEM der Hebel vorkommt? Wenn nichts fehlt, schreibe das.`
}

const bewertungen = await pipeline(ROLLEN, (r) => agent(promptBewertung(r), {
  label: `Bewertung ${r.id}`, phase: 'Bewertung', schema: S_BEWERTUNG,
}).then(b => ({ id: r.id, bank: r.bank, rolle: r.rolle, ...b })))

const B = bewertungen.filter(Boolean)
log(`Runde 4b: ${B.length} von ${ROLLEN.length} Rollen, ${ROLLEN.length - B.length} Ausfaelle`)

/* Urteilsmuster - gezaehlt wird, wo es schadet */
const muster = {}
for (const h of HEBEL) {
  const u = B.flatMap(b => (b.hebel || []).filter(x => x.id === h.id))
  muster[h.id] = {
    titel: h.titel,
    wirkt: u.filter(x => x.urteil === 'wirkt').length,
    wirkt_nicht: u.filter(x => x.urteil === 'wirkt nicht').length,
    schadet: u.filter(x => x.urteil === 'schadet').length,
    schadet_in: B.filter(b => (b.hebel || []).some(x => x.id === h.id && x.urteil === 'schadet')).map(b => b.id),
  }
}
const musterP = {}
for (const p of PROFILE) {
  const u = B.flatMap(b => (b.profile || []).filter(x => x.id === p.id))
  musterP[p.id] = {
    titel: p.titel,
    wirkt: u.filter(x => x.urteil === 'wirkt').length,
    wirkt_nicht: u.filter(x => x.urteil === 'wirkt nicht').length,
    schadet: u.filter(x => x.urteil === 'schadet').length,
    schadet_in: B.filter(b => (b.profile || []).some(x => x.id === p.id && x.urteil === 'schadet')).map(b => b.id),
  }
}
for (const [id, m] of Object.entries(muster)) log(`${id}: wirkt ${m.wirkt} | wirkt nicht ${m.wirkt_nicht} | SCHADET ${m.schadet}`)
for (const [id, m] of Object.entries(musterP)) log(`${id}: wirkt ${m.wirkt} | wirkt nicht ${m.wirkt_nicht} | SCHADET ${m.schadet}`)

const MUSTERTEXT = Object.entries(muster).map(([id, m]) =>
  `${id} ${m.titel}: wirkt ${m.wirkt}, wirkt nicht ${m.wirkt_nicht}, SCHADET ${m.schadet}${m.schadet_in.length ? ' (in ' + m.schadet_in.join(', ') + ')' : ''}`).join('\n')
const MUSTERTEXT_P = Object.entries(musterP).map(([id, m]) =>
  `${id} ${m.titel}: wirkt ${m.wirkt}, wirkt nicht ${m.wirkt_nicht}, SCHADET ${m.schadet}${m.schadet_in.length ? ' (in ' + m.schadet_in.join(', ') + ')' : ''}`).join('\n')

const SCHADENSTEXT = B.flatMap(b => [
  ...(b.hebel || []).filter(x => x.urteil === 'schadet').map(x => `${b.id} (${b.rolle}) gegen ${x.id}: ${x.mechanismus} | Nebenwirkung: ${x.nebenwirkung} | kippt bei: ${x.kippbedingung}`),
  ...(b.profile || []).filter(x => x.urteil === 'schadet').map(x => `${b.id} (${b.rolle}) gegen ${x.id}: ${x.mechanismus} | verliert: ${x.wer_verliert} | kippt bei: ${x.kippbedingung}`),
]).join('\n')

const FEHLTEXT = B.map(b => `${b.id}: ${b.fehlender_hebel}`).join('\n')
'''

VORLAGE += r'''
/* ============================================ Runde 5 - Red Team und Verifikation */

phase('Angriff')

const S_ANGRIFF = {
  type: 'object',
  properties: {
    bruch: { type: 'string', enum: ['gefunden', 'keiner gefunden'] },
    gegenstand: { type: 'string', description: 'die Karte, Zahl oder Aussage, die bricht - mit Nummer' },
    der_bruch: { type: 'string', description: 'was genau nicht traegt' },
    was_gelten_muesste: { type: 'string', description: 'unter welcher Bedingung die angegriffene Aussage falsch ist' },
    plausibel: { type: 'string', description: 'ob diese Bedingung plausibel ist - und woran man das bis 2031 sehen wuerde' },
    groesse: { type: 'string', description: 'wie gross der Fehler waere, in der Einheit der angegriffenen Groesse' },
    konsequenz: { type: 'string', enum: ['Aussage streichen', 'Aussage einschraenken', 'Aussage kennzeichnen', 'Aussage haelt'] },
  },
  required: ['bruch', 'gegenstand', 'der_bruch', 'was_gelten_muesste', 'plausibel', 'groesse', 'konsequenz'],
}

const KONTEXT_KURZ = `${GUELTIG}

DIE ZENTRALTABELLE IM EINZELNEN (16 Felder):
${KERN.tabelle}

DIE DISSENSPUNKTE:
${DISSENS}

DIE HEBEL:
${hebelText}

DAS URTEILSMUSTER UEBER DIE HEBEL (hundert Felder):
${MUSTERTEXT}

DAS URTEILSMUSTER UEBER DIE LEISTUNGSPROFILE:
${MUSTERTEXT_P}`

const ANGRIFFE = [
  { n: 1, titel: 'der am breitesten getragene Befund',
    auftrag: `Greife den Befund an, den das Panel am breitesten traegt. Das ist nach Lage der Dinge der Satz, dass nicht die Technik der Engpass ist: 99 von 100 Rollen nennen Entscheidung, bedienendes Personal, Daten oder Recht, genau eine nennt Technik.

WAS MUESSTE GELTEN, DAMIT DIESER SATZ FALSCH IST - und ist das plausibel? Pruefe insbesondere: Ist die Einmuetigkeit ein Befund oder ein Artefakt? Sie koennte daher ruehren, dass alle hundert Rollen dieselbe Frage in derselben Formulierung bekamen, dass "Engpass" in der Frage bereits nicht-technisch konnotiert war, oder dass ein Sprachmodell die verbreitete Erzaehlung vom Umsetzungsdefizit reproduziert. Suche die Formulierung, die den Befund erzeugt haben koennte.` },
  { n: 2, titel: 'der bestbewertete Hebel',
    auftrag: `Nimm den Hebel mit den meisten "wirkt"-Urteilen. WELCHES FELD SCHAEDIGT ER, DAS IHN NICHT BEWERTET HAT?

Die hundert Rollen decken zwei Drittel des Gesundheitswesens ab. Nicht besetzt sind Zahnmedizin, Augenoptik und Hoerakustik, Heilmittelerbringer, Reha-Kliniken, Transportwesen, Kur- und Vorsorgeeinrichtungen, betriebliche Gesundheitsversorgung, Praeventionsanbieter und die Veterinaer- und One-Health-Perspektive. Dazu kommen die Beschaeftigten selbst, Angehoerige und pflegende Laien.

Ein Hebel, dem alle zustimmen, die ihn bewerten duerfen, ist nicht geprueft - er ist unter Beteiligten abgestimmt.` },
  { n: 3, titel: 'die aggregierte P3-Summe',
    auftrag: `Greife die Zentraltabelle an. Sie deckt 16 Felder und 2,16 Mio Vollzeitaequivalente, also 48,9 Prozent des Kontrollrahmens.

DREI ANGRIFFSFLAECHEN, und du sollst alle drei pruefen:
1. UEBERLAPPEN BEZUGSGRUPPEN trotz der Zerlegung? Die Einrichtungsgliederung der Gesundheitspersonalrechnung soll disjunkt sein, die Krankenhaus- und Pflegestatistik unterteilen INNERHALB einer Einrichtungsart. Wo koennte dieselbe Person in zwei Zeilen stehen? Wie gross waere die Doppelzaehlung?
2. IST DER ZUSCHNITT JETZT RICHTIG? Sechs Felder wurden korrigiert, weil sie die ganze Einrichtungsart trugen statt ihres Ausschnitts - im Extremfall um den Faktor 339. Pruefe die zehn NICHT korrigierten Zeilen mit demselben Blick: Rechnet die Rolle ueber die ganze Einrichtungsart, oder ueber einen Ausschnitt davon?
3. DARF MAN DIE FEHLENDEN 51 PROZENT WEGLASSEN? Die nicht gedeckten Felder sind nicht zufaellig verteilt - fehlend sind unter anderem der grosse Teil der ambulanten aerztlichen Versorgung, Zahnmedizin, Psychotherapie, Verwaltung und Vorleistungsindustrie. Wenn genau die Felder fehlen, in denen KI am staerksten wirkte, ist der berichtete KI-Beitrag systematisch zu klein - und umgekehrt. In welche Richtung geht der Fehler?` },
  { n: 4, titel: 'die Stille auf der Tafel',
    auftrag: `DAS IST DER WICHTIGSTE ANGRIFF. Sprachmodelle einigen sich schweigend. Eine unangegriffene Karte ist kein Konsens, sondern eine Luecke - und du fuellst sie stellvertretend.

WELCHE KARTE HAT NIEMAND ANGEGRIFFEN, OBWOHL SIE ANGREIFBAR WAR? Suche nach: Zahlen, die alle uebernommen haben, ohne sie herzuleiten. Annahmen, die in allen hundert Positionen gleich lauten. Begriffe, die nie bestritten wurden. Der Gruppendiskussion lagen nur dreissig der hundert Karten vor - siebzig Karten hat nie jemand angegriffen.

Du legst die fehlenden Einwaende SELBST. Nenne die Karte, den Einwand, den niemand erhoben hat, und was sich aendern wuerde, wenn er traefe.` },
  { n: 5, titel: 'die Gueltigkeitsmaße',
    auftrag: `WELCHE BERICHTETE ZAHL TRAEGT EIN MASS, DAS SIE EIGENTLICH VERWIRFT?

Drei Kriterien sind gerissen und drei Maße zurueckgezogen. Pruefe systematisch, ob im Papier eine Zahl berichtet wird, deren eigenes Gueltigkeitsmaß sie nicht deckt:
- Die Bezugsgroessendeckung von 48,9 Prozent ist gerissen. Welche Aussagen des Papiers haengen an der Zentraltabelle und duerften nach dieser Regel gar nicht so stehen?
- Die Modellabhaengigkeit ist mit 3 von 6 gerissen und nur auf den sieben verankerten Rollen gehalten. Welche berichtete Groesse stammt ueberwiegend von unverankerten Feldern?
- Die Zuschnittstreue liegt bei 10 von 16. Sechs Felder waren falsch - was sagt das ueber die verbleibenden zehn, die nie unabhaengig geprueft wurden?
- Der Durchgriff D wurde fuer Felder ohne amtliche Bezugsgroesse auf eine Spannweite eingeschraenkt. Wird er irgendwo doch als Zahl gefuehrt?

Du greifst hier das Papier an, nicht das Panel. Ein Papier, das seine eigene Abbruchregel verletzt, ist schlechter als eines, das gar keine hatte.` },
  { n: 6, titel: 'die Besetzung',
    auftrag: `WELCHE AUSSAGE DES PAPIERS HINGE ANDERS AUS, WENN EINE DER NICHT BESETZTEN GRUPPEN AM TISCH SAESSE?

Nicht besetzt sind: Zahnmedizin, Augenoptik und Hoerakustik, Heilmittelerbringer (Physio-, Ergotherapie, Logopaedie), Reha-Kliniken, Kranken- und Rettungstransport, Kur- und Vorsorgeeinrichtungen, betriebliche Gesundheitsversorgung, Sport- und Praeventionsanbieter, Veterinaer- und One-Health.

Nicht besetzt sind ausserdem, und das wiegt schwerer: die Beschaeftigten in der direkten Pflege am Bett selbst (die Bank F vertritt Organisationen, nicht Schichten), pflegende Angehoerige, Patientinnen mit chronischer Mehrfacherkrankung, und Beschaeftigte ohne Berufsabschluss im Gesundheitswesen.

Nimm die drei Gruppen, deren Fehlen das Ergebnis am staerksten verzerrt. Sage bei jeder: welche konkrete Zahl oder Aussage anders ausfiele, in welche Richtung, und wie gross der Unterschied waere.` },
]

const [redteam, verifikationen] = await parallel([
  () => parallel(ANGRIFFE.map(a => () => agent(
`Du bist Red-Team-Instanz ${a.n} der Szenariokonferenz 2031. Du hast genau EINEN Angriffsauftrag und keinen anderen. Allgemeine Kritik ist wertlos; du lieferst entweder einen benannten Bruch oder die ausdrueckliche Feststellung, keinen gefunden zu haben.

DEIN ANGRIFFSGEGENSTAND: ${a.titel}

${a.auftrag}

DU BEKOMMST DEN GESAMTEN STAND DES VERFAHRENS:

${KONTEXT_KURZ}

DIE BISHER GESCHRIEBENEN TEILE DES PAPIERS:

--- TEIL 0 ---
${TEIL0}

--- TEIL 1 ---
${TEIL1}

--- TEIL 2 ---
${TEIL2}

DIE URTEILE, DIE "SCHADET" LAUTEN (der teuerste Teil des Laufs):
${SCHADENSTEXT}

REGELN:
- Ein Bruch ohne benannte Groesse ist keiner. Sage, wie gross der Fehler waere.
- "Keinen gefunden" ist eine vollwertige Antwort und besser als ein erfundener Bruch. Wenn du sie gibst, sage, was du geprueft hast.
- Du greifst nicht den Ton an, sondern die Haltbarkeit.
- Deine Konsequenz ist bindend fuer die Schlussfassung: streichen, einschraenken, kennzeichnen, oder haelt.`,
    { label: `Red Team ${a.n}: ${a.titel}`, phase: 'Angriff', schema: S_ANGRIFF }
  ).then(x => ({ nummer: a.n, titel: a.titel, ...x })))),

  () => parallel([
    { teil: 'Teil 0 - Gueltigkeit', text: TEIL0 },
    { teil: 'Teil 1 - Deutschland und Gesundheitswesen', text: TEIL1 },
    { teil: 'Teil 2 - Europa', text: TEIL2 },
  ].map(t => () => agent(
`Du bist Verifikationsinstanz der Szenariokonferenz 2031. Du hast diesen Teil NICHT geschrieben - wer das Ergebnis schreibt, prueft es nicht selbst. Du schreibst nicht um; du meldest zurueck.

DU PRUEFST GENAU DREI DINGE UND NICHTS SONST:
1. TRAEGT JEDE KARTENNUMMER DIE AUSSAGE, UNTER DER SIE STEHT? Nimm die zitierten Rollen-IDs und pruefe gegen die Zahlen und Positionen, die dir unten vorliegen.
2. IST EINE ZAHL BERICHTET, DEREN GUELTIGKEITSMASS SIE VERWIRFT? Die Bezugsgroessendeckung ist gerissen (48,9 %), die Modellabhaengigkeit ist gerissen (3 von 6), die Zuschnittstreue liegt bei 10 von 16, und drei Maße sind zurueckgezogen.
3. FEHLT EIN DISSENSPUNKT, DER ZU EINER BERICHTETEN AUSSAGE GEHOERT? Eine Aussage, die im Panel strittig war und im Papier glatt steht, ist ein Fehler.

ZUSAETZLICH, weil es in diesem Lauf zweimal schiefging:
4. Steht irgendwo eine Aussage ueber 2031 im INDIKATIV statt im Konjunktiv?
5. Steht irgendwo eine Zahl ohne Kartennummer?

DER ZU PRUEFENDE TEIL:

${t.text}

DER STAND DES VERFAHRENS, gegen den du pruefst:

${GUELTIG}

DIE ZENTRALTABELLE IM EINZELNEN:
${KERN.tabelle}

DIE DISSENSPUNKTE:
${DISSENS}

DIE HUNDERT ROLLEN MIT IHREN ZAHLEN UND POSITIONEN:
${HEBELBASIS}`,
    { label: `Verifikation ${t.teil}`, phase: 'Angriff', schema: {
      type: 'object',
      properties: {
        befunde: {
          type: 'array',
          items: {
            type: 'object',
            properties: {
              art: { type: 'string', enum: ['karte_traegt_nicht', 'zahl_ohne_deckung', 'dissens_fehlt', 'indikativ', 'zahl_ohne_karte'] },
              stelle: { type: 'string', description: 'die Textstelle, woertlich zitiert' },
              was: { type: 'string' },
              schwere: { type: 'string', enum: ['hart', 'weich'] },
              vorschlag: { type: 'string', description: 'wie die Stelle lauten muesste - als Vorschlag, nicht als Aenderung' },
            },
            required: ['art', 'stelle', 'was', 'schwere', 'vorschlag'],
          },
        },
        geprueft: { type: 'string', description: 'was du geprueft hast und was gehalten hat' },
      },
      required: ['befunde', 'geprueft'],
    } }
  ).then(x => ({ teil: t.teil, ...x })))),
])

const RT = (redteam || []).filter(Boolean)
const VF = (verifikationen || []).filter(Boolean)
const bruchzahl = RT.filter(r => r.bruch === 'gefunden').length
const vbefunde = VF.flatMap(v => (v.befunde || []).map(b => ({ teil: v.teil, ...b })))
log(`Red Team: ${bruchzahl} von ${RT.length} Instanzen haben einen Bruch gefunden`)
log(`Verifikation: ${vbefunde.length} Befunde, davon ${vbefunde.filter(b => b.schwere === 'hart').length} hart`)

const RTTEXT = RT.map(r => `ANGRIFF ${r.nummer} - ${r.titel}: ${r.bruch.toUpperCase()}
   Gegenstand: ${r.gegenstand}
   Der Bruch: ${r.der_bruch}
   Waere falsch, wenn: ${r.was_gelten_muesste}
   Plausibel? ${r.plausibel}
   Groesse des Fehlers: ${r.groesse}
   KONSEQUENZ: ${r.konsequenz}`).join('\n\n')

const VFTEXT = vbefunde.map(b => `[${b.schwere}] ${b.teil} - ${b.art}\n   Stelle: ${b.stelle}\n   Befund: ${b.was}\n   Vorschlag: ${b.vorschlag}`).join('\n\n')
'''

VORLAGE += r'''
/* ================================================== Runde 6 - das Strategiepapier */

phase('Papier')

const S_KAPITEL = {
  type: 'object',
  properties: {
    markdown: { type: 'string', description: 'das fertige Kapitel in Markdown, mit Ueberschriften ab Ebene 2, Tabellen wo sie tragen, und Kartennummern an jedem Satz, der eine Aussage macht' },
    karten: { type: 'array', items: { type: 'string' }, description: 'alle im Kapitel zitierten Kartennummern' },
    nicht_geschrieben: { type: 'string', description: 'was du weglassen musstest, weil keine Karte es traegt' },
  },
  required: ['markdown', 'karten', 'nicht_geschrieben'],
}

const SCHREIBAUFTRAG = `DU BIST SYNTHESEINSTANZ. DU DARFST KEINE KARTE ANLEGEN. Was du nicht vorfindest, kannst du nicht behaupten.

${ZWEI_REGELN}

SPRACHE: Deutsch, Fliesstext, kurze Saetze. Keine Aufzaehlung, wo ein Satz reicht; eine Tabelle nur, wo sie mehr traegt als der Satz. Keine Fuellwoerter, keine Beschwoerung von Bedeutung, kein "es ist wichtig zu betonen". Zahlen mit Tausenderpunkt. Kartennummern in Klammern hinter der Aussage, nicht als Fussnote.

WAS EINEN ABSATZ WERTLOS MACHT: dass er sagt, etwas sei komplex, vielschichtig oder differenziert zu betrachten. Sage stattdessen, WAS strittig ist, ZWISCHEN WEM, und WORAN es sich entscheidet.`

const KAPITEL = [
  { id: 'K1', titel: 'Die Hebel',
    auftrag: `Schreibe das Hebelkapitel von Teil 3.

Je Hebel ein Abschnitt, und in jedem Abschnitt in dieser Reihenfolge:
1. WAS getan wuerde, in einem Satz, operativ - Adressat, Instrument, Rechtsgrundlage.
2. WORAUS er hergeleitet ist: die Dissens- oder Positionskarten, an denen er haengt.
3. DAS URTEILSMUSTER ueber die hundert Felder - wieviele "wirkt", wieviele "wirkt nicht", wieviele "SCHADET", und in WELCHEN Feldern er schadet. Das Muster ist die Aussage, nicht die Mehrheit: Ein Hebel, der in vierzig Feldern wirkt und in fuenf schadet, ist etwas voellig anderes als einer, der ueberall schwach wirkt - und beides saehe in einem Balkendiagramm gleich aus. Schreibe den Unterschied hin.
4. DIE KIPPBEDINGUNGEN, unter denen die Urteile sich umkehren - die genannten, nicht erfundene.
5. WAS DAS RED TEAM gegen ihn vorgebracht hat, wenn etwas vorliegt.

Ordne die Hebel danach, wie stark sie tragen - aber trage nicht auf: Wenn kein Hebel breit traegt, ist DAS das Ergebnis des Kapitels und muss im ersten Absatz stehen.

Ein Satz, den du pruefen und dann entweder belegen oder streichen musst: 99 von 100 Rollen halten nicht die Technik fuer den Engpass. Ein Hebel, der Technik beschafft, adressiert den Engpass von einer Rolle. Wenn die Hebel das spiegeln, sage es; wenn nicht, sage auch das.` },
  { id: 'K2', titel: 'Die Leistungsprofile',
    auftrag: `Schreibe das Kapitel ueber die Leistungsprofile.

Ein Leistungsprofil ist etwas, das ein Externer anbieten koennte - im Unterschied zum Hebel, den der Staat zieht. Die Profile sind aus den Engpassangaben des Panels hergeleitet, nicht aus einem Angebotskatalog; die Richtung ist die ganze Konstruktion und gehoert in den ersten Absatz.

DREI BINDENDE VORGABEN:
1. KEIN ANBIETERNAME, KEINE MARKE, KEIN PRODUKTNAME - auch nicht in einer Umschreibung, die nur einen Marktteilnehmer meinen kann. Die Zuordnung von Profilen zu tatsaechlichen Anbietern geschieht ausserhalb dieses Papiers, in einem eigenen Dokument, und ist ausdruecklich interessengeleitet. Das ist im Kapitel zu vermerken.
2. GEZAEHLT WIRD, WO EIN PROFIL SCHADET. Ein Profil, das in achtzig Feldern schwach wirkt und in fuenf klar schadet, beschreibt ein Geschaeft mit fuenf ernsten Gegnern - und diese fuenf sind die interessanteste Information, die der ganze Lauf ueber ein Angebot hervorbringt. Nenne sie namentlich mit Kartennummer und Mechanismus. Zustimmung ist billig; ein begruendeter Einwand aus einem fremden Feld ist teuer und selten.
3. JE PROFIL DIE FRAGE BEANTWORTEN: Wenn der Engpass so breit genannt wird - warum loest ihn heute niemand? Dreissig von hundert Rollen nennen "gar kein Topf" als Finanzierungsquelle fuer KI im eigenen Feld. Ein Profil ohne Rechnungsempfaenger ist kein Geschaeft, und das gehoert hin.

Schliesse mit dem, was das Panel ueber den Verbleib des Gewinns sagt: P5 weist im Median dreissig Prozent Abfluss ins Ausland aus, gleichauf mit dem Anteil, der in neue Leistung ginge. Eine Leistungsschicht, die den Abfluss vergroessert, loest ein Problem und schafft ein anderes.` },
  { id: 'K3', titel: 'Was strittig bleibt',
    auftrag: `Schreibe das Schlusskapitel von Teil 3: was strittig bleibt, was fehlt, und woran sich beides entscheidet.

DREI TEILE:
1. DIE DISSENSPUNKTE mit ihrer Entscheidungsgroesse. Je Punkt: welche beiden Karten unvereinbar sind, welche Baenke sich gegenueberstehen, und WELCHE ZAHL AUS WELCHER QUELLE AB WANN den Streit beenden wuerde. Die Entscheidungsgroesse ist der eigentliche Ertrag der Diskussion - nicht die Einigung, sondern die Benennung dessen, woran die Uneinigkeit haengt. Eine Entscheidungsgroesse ohne Quelle und ohne Zeitpunkt ist keine, und das ist dann zu sagen.
2. DIE FEHLENDEN HEBEL. Hundert Rollen haben benannt, was ihr Feld braeuchte und in keinem Hebel vorkommt. Fasse zusammen, was mehrfach genannt wurde - und pruefe, ob es fehlt, weil keine Karte es traegt, oder weil die Syntheseinstanz es uebersehen hat. Der Unterschied ist wesentlich.
3. DIE STILLE. Das Red Team hat stellvertretend die Einwaende gelegt, die niemand erhoben hat. Referiere sie als das, was sie sind: nicht Kritik am Ergebnis, sondern die Messung dessen, wieviel Zustimmung in diesem Verfahren nichts bedeutet. Der Gruppendiskussion lagen dreissig von hundert Karten vor; siebzig hat nie jemand angegriffen.

${WAS_ES_NICHT_IST}

Dieses Kapitel darf am wenigsten glaetten. Wenn das Verfahren an einer Stelle nichts hergibt, steht das hier und nicht in einer Fussnote.` },
]

const gemeinsam = `${GUELTIG}

DIE ZENTRALTABELLE IM EINZELNEN (16 Felder, 2,16 Mio Vollzeitaequivalente, 48,9 % Deckung):
${KERN.tabelle}

DIE HEBEL:
${hebelText}

DIE LEISTUNGSPROFILE:
${profilText(PROFILE)}

DAS URTEILSMUSTER UEBER DIE HEBEL:
${MUSTERTEXT}

DAS URTEILSMUSTER UEBER DIE PROFILE:
${MUSTERTEXT_P}

ALLE URTEILE, DIE "SCHADET" LAUTEN, mit Mechanismus und Kippbedingung:
${SCHADENSTEXT}

WAS DIE HUNDERT ROLLEN ALS FEHLENDEN HEBEL GENANNT HABEN:
${FEHLTEXT}

DIE DISSENSPUNKTE MIT ENTSCHEIDUNGSGROESSE:
${DISSENS}

DIE DURCHGRIFFSKANAELE:
${KANAELE}

WAS DAS RED TEAM GEFUNDEN HAT:
${RTTEXT}

DIE BEANSTANDUNGEN AN DER HERLEITUNG DER HEBEL UND PROFILE:
${JSON.stringify((pruefung4b && pruefung4b.beanstandungen) || [], null, 1)}
Luecke laut Pruefinstanz: ${(pruefung4b && pruefung4b.fehlend) || '-'}
Was die Nachbesserung geaendert hat: ${(nachbesserung && nachbesserung.geaendert) || '-'}
Welche Beanstandung sie zurueckgewiesen hat: ${(nachbesserung && nachbesserung.nicht_geaendert) || '-'}`

const kapitel = await parallel(KAPITEL.map(k => () => agent(
`Du schreibst das Kapitel "${k.titel}" von Teil 3 des Strategiepapiers 2031.

Teil 0 (Gueltigkeit), Teil 1 (Deutschland) und Teil 2 (Europa) sind geschrieben und liegen dir vor. Du schreibst sie NICHT neu. Du schreibst Teil 3 - den einzigen Teil, in dem das Verfahren von der Messung zur Handlung uebergeht.

${k.auftrag}

${SCHREIBAUFTRAG}

=============== DER STAND DES VERFAHRENS ===============

${gemeinsam}

=============== DIE GESCHRIEBENEN TEILE, zur Anschlussfaehigkeit in Ton und Begriff ===============

--- TEIL 0 ---
${TEIL0}

--- TEIL 1 ---
${TEIL1}

--- TEIL 2 ---
${TEIL2}`,
  { label: `Kapitel ${k.id}: ${k.titel}`, phase: 'Papier', schema: S_KAPITEL }
).then(x => ({ id: k.id, titel: k.titel, ...x }))))

const KAP = kapitel.filter(Boolean)
log(`Runde 6a: ${KAP.length} von 3 Kapiteln, zusammen ${KAP.reduce((n, k) => n + k.markdown.length, 0)} Zeichen`)

const KAPTEXT = KAP.map(k => `=============== ${k.id} ${k.titel} ===============\n\n${k.markdown}`).join('\n\n')

/* ------------------------------------------------------------ Zusammenzug */

const zusammenzug = await agent(
`Du ziehst das Strategiepapier 2031 zusammen. Vier Teile liegen vor: Teil 0, 1 und 2 sind geschrieben und geprueft, Teil 3 besteht aus drei getrennt geschriebenen Kapiteln.

DEIN AUFTRAG HAT ZWEI TEILE, und der erste ist der wichtigere:

1. WIDERSPRUECHE BENENNEN, NICHT GLAETTEN. Drei getrennt geschriebene Kapitel koennen einander widersprechen, und sie koennen den geschriebenen Teilen widersprechen. Genau dieser Widerspruch ist zu BENENNEN. Suche systematisch nach:
   - derselben Zahl mit zwei verschiedenen Werten,
   - derselben Kartennummer unter zwei unvereinbaren Aussagen,
   - einer Aussage in Teil 3, die eine Aussage in Teil 1 voraussetzt, welche dort eingeschraenkt ist,
   - einem Hebel, der eine Groesse bewegen soll, deren Gueltigkeitsmaß gerissen ist,
   - einer Doppelung, in der zwei Kapitel dasselbe mit verschiedenen Worten sagen.
   Ein geglaetteter Widerspruch ist ein verlorener Befund. Wo zwei Kapitel sich widersprechen und du nicht entscheiden kannst, welches recht hat, bleibt der Widerspruch im Papier stehen und wird als solcher ausgewiesen.

2. DEN RAHMEN SCHREIBEN, der aus vier Teilen ein Papier macht:
   - einen TITEL und einen Untertitel,
   - einen VORSPANN von hoechstens zwanzig Zeilen: was dieses Papier ist, wie es entstanden ist, und in einem Satz, was herauskam. Der Vorspann sagt zuerst, was das Papier NICHT ist - die Reihenfolge ist die Lehre des ganzen Verfahrens.
   - eine LESEHILFE: in welcher Reihenfolge die vier Teile zu lesen sind und warum Gueltigkeit vorne steht und nicht im Anhang,
   - ein SCHLUSSKAPITEL "Was daraus folgt": nicht Zusammenfassung, sondern die drei bis fuenf Saetze, die ein Leser behalten soll, jeder mit Kartennummern und im Konjunktiv.

${ZWEI_REGELN}

${SCHREIBAUFTRAG}

=============== TEIL 0 ===============
${TEIL0}

=============== TEIL 1 ===============
${TEIL1}

=============== TEIL 2 ===============
${TEIL2}

=============== TEIL 3, drei Kapitel ===============
${KAPTEXT}

=============== WAS DAS RED TEAM GEFUNDEN HAT ===============
${RTTEXT}

=============== WAS DIE VERIFIKATION AN TEIL 0 BIS 2 BEANSTANDET HAT ===============
${VFTEXT || '(keine Befunde)'}

=============== DER GEMESSENE STAND ===============
${GUELTIG}`,
  { label: 'Zusammenzug', phase: 'Papier', schema: {
    type: 'object',
    properties: {
      titel: { type: 'string' },
      untertitel: { type: 'string' },
      vorspann: { type: 'string', description: 'Markdown' },
      lesehilfe: { type: 'string', description: 'Markdown' },
      schluss: { type: 'string', description: 'Markdown, das Kapitel "Was daraus folgt"' },
      widersprueche: {
        type: 'array',
        items: {
          type: 'object',
          properties: {
            zwischen: { type: 'string', description: 'welche beiden Stellen' },
            was: { type: 'string' },
            aufloesbar: { type: 'string', enum: ['aufloesbar', 'bleibt stehen'] },
            aufloesung: { type: 'string', description: 'wie er aufzuloesen ist, oder warum er stehen bleibt' },
          },
          required: ['zwischen', 'was', 'aufloesbar', 'aufloesung'],
        },
      },
      streichliste: { type: 'array', items: { type: 'string' }, description: 'Aussagen aus Teil 3, die nach Red Team oder Verifikation zu streichen oder einzuschraenken sind' },
    },
    required: ['titel', 'untertitel', 'vorspann', 'lesehilfe', 'schluss', 'widersprueche', 'streichliste'],
  } })

const ZTEXT = zusammenzug ? `TITEL: ${zusammenzug.titel}
UNTERTITEL: ${zusammenzug.untertitel}

VORSPANN:
${zusammenzug.vorspann}

LESEHILFE:
${zusammenzug.lesehilfe}

SCHLUSSKAPITEL:
${zusammenzug.schluss}

WIDERSPRUECHE:
${(zusammenzug.widersprueche || []).map(w => `  [${w.aufloesbar}] ${w.zwischen}: ${w.was}\n     ${w.aufloesung}`).join('\n')}

STREICHLISTE:
${(zusammenzug.streichliste || []).map(s => '  - ' + s).join('\n')}` : '(Zusammenzug ausgefallen)'

log(`Zusammenzug: ${(zusammenzug && zusammenzug.widersprueche || []).length} Widersprueche, ${(zusammenzug && zusammenzug.streichliste || []).length} Streichungen`)

/* --------------------------------------------- Verifikation des Zusammenzugs */

const vzus = await agent(
`Du bist die Verifikationsinstanz des Zusammenzugs. Du hast ihn nicht geschrieben. Du schreibst nicht um; du meldest zurueck.

DU PRUEFST FUENF DINGE:
1. Traegt jede Kartennummer die Aussage, unter der sie steht?
2. Ist eine Zahl berichtet, deren Gueltigkeitsmaß sie verwirft? Gerissen sind Bezugsgroessendeckung (48,9 %), Modellabhaengigkeit (3 von 6) und Zuschnittstreue (10 von 16); zurueckgezogen sind Attributionskonsistenz und die Modellabhaengigkeit der Runde 3.
3. Fehlt ein Dissenspunkt, der zu einer berichteten Aussage gehoert?
4. Steht eine Aussage ueber 2031 im Indikativ statt im Konjunktiv?
5. HAT DER ZUSAMMENZUG EINEN WIDERSPRUCH GEGLAETTET, STATT IHN ZU BENENNEN? Vergleiche die drei Kapitel mit dem, was der Zusammenzug als Widerspruchsliste ausweist. Ein Widerspruch, der in den Kapiteln steht und in der Liste fehlt, ist der schwerste Befund, den du melden kannst.

Zusaetzlich: Ist ein Befund des Red Teams mit der Konsequenz "streichen" oder "einschraenken" NICHT in der Streichliste? Das ist hart.

=============== DER ZUSAMMENZUG ===============
${ZTEXT}

=============== TEIL 3, die drei Kapitel ===============
${KAPTEXT}

=============== DAS RED TEAM ===============
${RTTEXT}

=============== DIE GESCHRIEBENEN TEILE ===============
--- TEIL 0 ---
${TEIL0}
--- TEIL 1 ---
${TEIL1}
--- TEIL 2 ---
${TEIL2}

=============== DER GEMESSENE STAND ===============
${GUELTIG}`,
  { label: 'Verifikation des Zusammenzugs', phase: 'Papier', schema: {
    type: 'object',
    properties: {
      befunde: {
        type: 'array',
        items: {
          type: 'object',
          properties: {
            art: { type: 'string', enum: ['karte_traegt_nicht', 'zahl_ohne_deckung', 'dissens_fehlt', 'indikativ', 'widerspruch_geglaettet', 'redteam_ignoriert'] },
            stelle: { type: 'string' },
            was: { type: 'string' },
            schwere: { type: 'string', enum: ['hart', 'weich'] },
            vorschlag: { type: 'string' },
          },
          required: ['art', 'stelle', 'was', 'schwere', 'vorschlag'],
        },
      },
      freigabe: { type: 'string', enum: ['frei', 'frei mit Auflagen', 'nicht frei'] },
      begruendung: { type: 'string' },
    },
    required: ['befunde', 'freigabe', 'begruendung'],
  } })

const VZTEXT = vzus ? `FREIGABE: ${vzus.freigabe} - ${vzus.begruendung}\n\n` +
  (vzus.befunde || []).map(b => `[${b.schwere}] ${b.art}\n   Stelle: ${b.stelle}\n   Befund: ${b.was}\n   Vorschlag: ${b.vorschlag}`).join('\n\n') : '(ausgefallen)'
log(`Verifikation des Zusammenzugs: ${(vzus && vzus.freigabe) || '-'}, ${(vzus && vzus.befunde || []).length} Befunde`)

/* ------------------------------------------------------------ Schlussfassung */

const schluss = await agent(
`Du schreibst die SCHLUSSFASSUNG von Teil 3 des Strategiepapiers 2031 samt Rahmen. Das ist der letzte Aufruf des Verfahrens; danach wird nichts mehr erhoben.

DU LIEFERST EIN EINZIGES MARKDOWN-DOKUMENT, das genau das enthaelt und in dieser Reihenfolge:
1. Titel und Untertitel (Ebene 1), darunter der Vorspann.
2. Die Lesehilfe.
3. "Teil 3 - Die Hebel" mit den drei Kapiteln, ueberarbeitet.
4. Ein Abschnitt "Widersprueche, die stehen bleiben" - jeder Widerspruch, den der Zusammenzug als "bleibt stehen" ausgewiesen hat, mit beiden Seiten und ohne Entscheidung.
5. Das Schlusskapitel "Was daraus folgt".
6. Ein Abschnitt "Was dieses Papier nicht ist", woertlich in der Sache, am Ende und nicht versteckt.

WAS DU EINARBEITEST, und zwar vollstaendig:
- JEDE Konsequenz des Red Teams: "Aussage streichen" heisst streichen, "Aussage einschraenken" heisst einschraenken, "Aussage kennzeichnen" heisst kennzeichnen. Du diskutierst das nicht; du fuehrst es aus. Wo du eine Aussage wegen eines Red-Team-Befundes streichst oder einschraenkst, vermerkst du das an Ort und Stelle in einem Halbsatz - der Leser soll sehen, wo das Verfahren sich selbst korrigiert hat.
- JEDEN harten Befund der Verifikation des Zusammenzugs.
- JEDEN Widerspruch: aufgeloest, wo der Zusammenzug ihn aufgeloest hat; stehengelassen und ausgewiesen, wo nicht.
- Die Streichliste vollstaendig.

${ZWEI_REGELN}

${SCHREIBAUFTRAG}

DREI DINGE, DIE DU NICHT TUST:
1. Du schreibst Teil 0, 1 und 2 NICHT neu und zitierst ihre Zahlen nur so, wie sie dort stehen. Die Zentraltabelle lautet: 16 Felder, 2.155.154 Vollzeitaequivalente, 48,9 % Deckung, Personalbedarf 2031 mit KI rund +124.000, ohne KI rund +202.000, KI-Beitrag rund -78.000 Vollkraefte. Weiche von keiner dieser Zahlen ab.
2. Du erfindest keine Karte. Was keine Nummer traegt, streichst du.
3. Du glaettest nichts, um das Papier runder zu machen. Ein Papier, das seine Angreifbarkeit ausweist, ist brauchbar; eines, das erst erscheint, wenn es unangreifbar ist, erscheint nicht.

=============== DER ZUSAMMENZUG ===============
${ZTEXT}

=============== DIE VERIFIKATION DES ZUSAMMENZUGS ===============
${VZTEXT}

=============== TEIL 3, die drei Kapitel im Entwurf ===============
${KAPTEXT}

=============== DAS RED TEAM ===============
${RTTEXT}

=============== DIE VERIFIKATION VON TEIL 0 BIS 2 ===============
${VFTEXT || '(keine Befunde)'}

=============== DER STAND DES VERFAHRENS ===============
${gemeinsam}

=============== DIE GESCHRIEBENEN TEILE ===============
--- TEIL 0 ---
${TEIL0}
--- TEIL 1 ---
${TEIL1}
--- TEIL 2 ---
${TEIL2}`,
  { label: 'Schlussfassung', phase: 'Papier', schema: {
    type: 'object',
    properties: {
      markdown: { type: 'string', description: 'das vollstaendige Dokument' },
      eingearbeitet: { type: 'array', items: { type: 'string' }, description: 'welche Red-Team- und Verifikationsbefunde eingearbeitet wurden und wie' },
      offen: { type: 'array', items: { type: 'string' }, description: 'was ausdruecklich offen bleibt - wird im Papier als offen ausgewiesen' },
      gestrichen: { type: 'array', items: { type: 'string' }, description: 'Aussagen, die du gestrichen hast, weil keine Karte sie traegt' },
    },
    required: ['markdown', 'eingearbeitet', 'offen', 'gestrichen'],
  } })

log(`Schlussfassung: ${schluss ? schluss.markdown.length : 0} Zeichen, ${schluss ? schluss.eingearbeitet.length : 0} Befunde eingearbeitet, ${schluss ? schluss.offen.length : 0} offen`)

return {
  hebel: HEBEL,
  profile: PROFILE,
  nicht_hergeleitet: (hebelsatz && hebelsatz.nicht_hergeleitet) || '',
  pruefung_herleitung: pruefung4,
  nachbesserung,
  pruefung_nach_nachbesserung: pruefung4b,
  bewertungen: B,
  muster, musterP,
  red_team: RT,
  verifikation_teile: VF,
  kapitel: KAP,
  zusammenzug,
  verifikation_zusammenzug: vzus,
  schlussfassung: schluss,
  ausfaelle: (ROLLEN.length - B.length) + (6 - RT.length) + (3 - VF.length) + (3 - KAP.length),
}
'''


if __name__ == '__main__':
    main()
