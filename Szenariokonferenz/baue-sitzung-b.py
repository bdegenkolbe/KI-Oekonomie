#!/usr/bin/env python3
"""Erzeugt workflow-sitzung-b.js: Runde 2 (Gruppendiskussion) und Runde 3 (zweite Erhebung).

150 Aufrufe: 5 Streitfragen + 30 Kartenzuege + 5 Dissensprotokolle + 100 Rollen + 10 Kontrollarm.

Abweichung von der Kostentabelle des Konzepts, bewusst: Dort stehen 60
Kartenzug-Aufrufe (30 Rollen mal zwei Zuege), hier sind es 30 - beide Zuege
einer Rolle entstehen in einem Aufruf. Beide Zuege existieren und werden
einzeln ausgewertet; die Rolle sieht beim Schreiben des zweiten Zuges ihren
ersten, was Doppelungen verhindert und die Unabhaengigkeit der beiden Zuege
mindert. Ersparnis rund 30 Aufrufe.

Alle Korrekturen aus Sitzung A und ihren drei Fehlersuchen sind eingebaut:
  - Bezugsgroesse null wird nie weitergereicht (17-Sitzung-A Paragraf 3)
  - korrigierte Zuschnitte aus 23-Teil-1 Paragraf 3
  - Begruendungspflicht fuer D ueber 1,0 (Kriterium 23)
  - Korrektur der Leistungsgruppenzahl aus 21-Quellenpruefung (61, nicht 65)
  - Anker und Geruest bleiben je Rolle unveraendert, sonst misst die Differenz
    nicht die Wirkung der Diskussion
"""
import json, pathlib, sys, statistics as st

BASIS = pathlib.Path(__file__).resolve().parent
SA = BASIS / 'rohdaten' / 'sitzung-a.json'
NA = BASIS / 'rohdaten' / 'nacharbeit.json'
ZIEL = BASIS / 'workflow-sitzung-b.js'

# Bank -> Perspektive, fuer den Gruppenschnitt quer zu den Baenken
PERSP = {'A': 'Leistungserbringer', 'B': 'Leistungserbringer', 'C': 'Leistungserbringer',
         'D': 'Kostentraeger', 'H': 'Aufsicht', 'I': 'Aufsicht',
         'F': 'Arbeitnehmer', 'G': 'Arbeitnehmer',
         'E': 'Gesamtwirtschaft', 'J': 'Gesamtwirtschaft', 'K': 'Gesamtwirtschaft',
         'L': 'Gesamtwirtschaft', 'M': 'Gesamtwirtschaft', 'N': 'Gesamtwirtschaft'}
# Korrigierte Bezugsgroessen aus 23-Teil-1 Paragraf 3
KORR = {'B07': (4000, 'Sicherstellungsbereich der 17 KVen'),
        'D03': (561, 'Kernhaushalt des GKV-Spitzenverbandes'),
        'E01': (2750, 'Market Access Deutschland'),
        'E02': (28000, 'Medizintechnik Bildgebung'),
        'E07': (24000, 'vollversorgender pharmazeutischer Grosshandel'),
        'E06': (22000, 'fachaerztliche Labore ausserhalb der Krankenhaeuser')}


def gruppen(auswahl, R):
    """Fuenf Gruppen zu sechs, quer zu den Baenken: je Gruppe moeglichst alle Perspektiven."""
    nach = {}
    for i in auswahl:
        nach.setdefault(PERSP[R[i]['bank']], []).append(i)
    g = [[] for _ in range(5)]
    k = 0
    for p in ('Leistungserbringer', 'Kostentraeger', 'Aufsicht', 'Arbeitnehmer', 'Gesamtwirtschaft'):
        for i in nach.get(p, []):
            g[k % 5].append(i)
            k += 1
    return g


def main():
    for p in (SA, NA):
        if not p.exists():
            sys.exit(f'fehlt: {p}')
    sa = json.loads(SA.read_text(encoding='utf-8'))
    na = json.loads(NA.read_text(encoding='utf-8'))
    R = {a['id']: a for a in sa['runde1']}
    Z = {f['id']: f for f in na['abbildung']['felder']}
    for i, (v, txt) in KORR.items():
        Z[i] = {**Z[i], 'vzae': v, 'bezugsgruppe': txt, 'zuordnung': 'primaer'}

    auswahl = sa['auswahl_bank']
    grp = gruppen(auswahl, R)

    # Zahlenmatrix: was jede Rolle von den anderen sieht - Zahlen, keine Volltexte
    matrix = '\n'.join(
        f"{a['id']} {a['bank']} | P1 {a['p1']} | P2 {a['p2']} | P3 {a['p3']} | P3_0 {a['p3_null']} | "
        f"P4 {a['p4_ki']}/{a['p4_demografie']}/{a['p4_strukturreform']} | "
        f"P5 {a['p5_leistungserbringer']}/{a['p5_preis_beitrag']}/{a['p5_abfluss_ausland']}/{a['p5_neue_leistung']} | "
        f"Hemmnis {a['p2_hemmnis']} | Engpass {a['a3_engpass']}"
        for a in sa['runde1'])

    def D(a):
        z = a['p1'] * a['p2'] / 100
        return round(abs(a['p3'] - a['p3_null']) / z, 2) if z else 0

    karten = {i: {
        'id': i, 'bank': R[i]['bank'], 'rolle': R[i].get('rolle', ''),
        'position': R[i]['position'], 'p1': R[i]['p1'], 'p2': R[i]['p2'],
        'p3': R[i]['p3'], 'p3_null': R[i]['p3_null'], 'd': D(R[i]),
        'p2_hemmnis': R[i]['p2_hemmnis'], 'a3_engpass': R[i]['a3_engpass'],
        'falsifikator': R[i]['falsifikator'],
    } for i in auswahl}

    rollen = [{'id': a['id'], 'bank': a['bank'], 'rolle': a.get('rolle', ''),
               'geruest': a['geruest'], 'anker': a['anker'],
               'vzae': Z[a['id']]['vzae'], 'bezugsgruppe': Z[a['id']]['bezugsgruppe'][:180],
               'zuordnung': Z[a['id']]['zuordnung'],
               'p1': a['p1'], 'p2': a['p2'], 'p3': a['p3'], 'p3_null': a['p3_null'],
               'p4': [a['p4_ki'], a['p4_demografie'], a['p4_strukturreform']],
               'p5': [a['p5_leistungserbringer'], a['p5_preis_beitrag'],
                      a['p5_abfluss_ausland'], a['p5_neue_leistung']],
               'd': D(a), 'position': a['position'][:700]}
              for a in sa['runde1']]

    ger = {'A': 'SZENARIOGERUEST A - FORTSCHREIBUNG\n' + '\n'.join(
               f"  {x['groesse']}: {x['wert']}" for x in sa['geruestA']['annahmen']),
           'B': 'SZENARIOGERUEST B - GEGENWELT\n' + '\n'.join(
               f"  {x['groesse']}: {x['wert']}" for x in sa['geruestB']['annahmen'])}

    js = VORLAGE
    for marke, wert in (('__GRUPPEN__', grp), ('__KARTEN__', karten), ('__ROLLEN__', rollen),
                        ('__MATRIX__', matrix), ('__GER__', ger)):
        js = js.replace(marke, json.dumps(wert, ensure_ascii=False))
    ZIEL.write_text(js, encoding='utf-8')
    n = 5 + len(auswahl) + 5 + len(rollen) + 10
    print(f'{ZIEL.name}: {n} Aufrufe, {round(len(js)/1024)} KB')
    print('  Hinweis: Die Kostentabelle des Konzepts setzt 60 Kartenzug-Aufrufe an (30 Rollen mal zwei Zuege).')
    print('  Dieses Skript erzeugt BEIDE Zuege einer Rolle in EINEM Aufruf - also 30 statt 60.')
    print('Gruppen:', ' | '.join(','.join(g) for g in grp))
    ohne = [r['id'] for r in rollen if not r['vzae']]
    print(f'Rollen ohne amtliche Bezugsgroesse: {len(ohne)} - erhalten den korrigierten Auftrag')


VORLAGE = r'''export const meta = {
  name: 'sitzung-b-runde-2-und-3',
  description: 'Sitzung B: Gruppendiskussion der dreissig Strittigsten und zweite Erhebung der Pflichtgroessen durch alle hundert Rollen',
  phases: [
    { title: 'Streitfragen', detail: 'Fuenf Gruppenleitungen clustern die Karten und finden die Streitfrage' },
    { title: 'Kartenzuege', detail: 'Dreissig Rollen, je zwei Zuege mit Pflichteinwand' },
    { title: 'Dissens', detail: 'Fuenf Dissensprotokolle mit Entscheidungsgroesse' },
    { title: 'Runde 3', detail: 'Hundert Rollen erheben die Pflichtgroessen erneut, dazu zehn auf dem zweiten Modell' },
  ],
}

const GRUPPEN = __GRUPPEN__
const KARTEN = __KARTEN__
const ROLLEN = __ROLLEN__
const MATRIX = __MATRIX__
const GER = __GER__

const K = id => KARTEN[id]
const kurz = k => `${k.id} (Bank ${k.bank}, ${k.rolle}): P1 ${k.p1} | P2 ${k.p2} | P3 ${k.p3} | P3_0 ${k.p3_null} | D ${k.d} | Hemmnis ${k.p2_hemmnis} | Engpass ${k.a3_engpass}\n   POSITION: ${k.position.slice(0, 600)}`

/* ----------------------------------------------------- Runde 2a: Streitfragen */

phase('Streitfragen')

const S_FRAGE = {
  type: 'object',
  properties: {
    streitfrage: { type: 'string', description: 'die eine Frage, an der sich diese Gruppe scheidet - gefunden, nicht vorgegeben' },
    begruendung: { type: 'string', description: 'welche Karten sie gegeneinander stellt' },
    cluster: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, rollen: { type: 'array', items: { type: 'string' } } }, required: ['name', 'rollen'] } },
  },
  required: ['streitfrage', 'begruendung', 'cluster'],
}

const fragen = await pipeline(GRUPPEN, (g, gi) => agent(
`Du bist Gruppenleitung der Gruppe ${gi + 1} der Szenariokonferenz 2031. Du hast keine eigene Position zur Sache und keine Stimme.

Vor dir liegen die Karten von sechs Rollen, die aus hundert nach einem Streitindex ausgewaehlt wurden - sie weichen am staerksten vom Median ihrer eigenen Bank ab. Sie sind quer zu den Baenken zusammengestellt: Leistungserbringer, Kostentraeger, Aufsicht, Arbeitnehmerseite und Gesamtwirtschaft sitzen zusammen.

DEINE AUFGABE: Clustere die Karten nach ihrer inhaltlichen Stossrichtung und formuliere daraus DIE STREITFRAGE DIESER GRUPPE.

Die Streitfrage wird nicht vorgegeben, sie wird gefunden. Sie muss:
- an den vorliegenden Karten haengen, nicht an einer allgemeinen Debatte,
- so gestellt sein, dass die sechs Rollen sie verschieden beantworten WUERDEN,
- und eine Groesse betreffen, die das Verfahren erhebt: Arbeitszeit, Personalbedarf, Durchgriff, Ursachenanteil, Verbleib des Gewinns, Engpass.

Eine Frage, auf die alle sechs dasselbe antworten, ist keine Streitfrage.

DIE SECHS KARTEN:

${g.map(id => kurz(K(id))).join('\n\n')}`,
  { label: `Streitfrage Gruppe ${gi + 1}`, phase: 'Streitfragen', schema: S_FRAGE }
).then(f => ({ gruppe: gi, rollen: g, ...f })))

const F = fragen.filter(Boolean)
log(`Streitfragen: ${F.length} von ${GRUPPEN.length} Gruppen`)

/* ------------------------------------------------------ Runde 2b: Kartenzuege */

phase('Kartenzuege')

const S_ZUG = {
  type: 'object',
  properties: {
    zug1: {
      type: 'object',
      properties: {
        art: { type: 'string', enum: ['einwand', 'bedingung', 'befund'] },
        gegen: { type: 'string', description: 'Rollen-ID der angegriffenen Karte' },
        was: { type: 'string', description: 'was in der angegriffenen Karte tatsaechlich steht und warum es nicht traegt' },
        rettungsbedingung: { type: 'string', description: 'unter welcher Bedingung die angegriffene Karte doch traegt - ohne diese Angabe ist der Zug ein Leerzug' },
      },
      required: ['art', 'gegen', 'was', 'rettungsbedingung'],
    },
    zug2: {
      type: 'object',
      properties: {
        art: { type: 'string', enum: ['einwand', 'bedingung', 'befund'] },
        gegen: { type: 'string' },
        was: { type: 'string' },
        rettungsbedingung: { type: 'string' },
      },
      required: ['art', 'gegen', 'was', 'rettungsbedingung'],
    },
    eigene_verteidigung: { type: 'string', description: 'was du gegen die erwartbaren Einwaende gegen DEINE Karte vorbringst' },
  },
  required: ['zug1', 'zug2', 'eigene_verteidigung'],
}

const paare = []
for (const f of F) for (const id of f.rollen) paare.push({ f, id })

const zuege = await pipeline(paare, (p) => agent(
`Du bist im Rollendossier ${p.id}: ${K(p.id).rolle} (Bank ${K(p.id).bank}).

Du sitzt in Gruppe ${p.f.gruppe + 1} der Szenariokonferenz 2031, zusammen mit fuenf Rollen aus anderen Baenken. Ihr seid ausgewaehlt worden, weil eure Urteile am staerksten vom Median eurer eigenen Bank abweichen.

DIE STREITFRAGE EURER GRUPPE: ${p.f.streitfrage}
(hergeleitet aus: ${p.f.begruendung})

DEINE EIGENE KARTE AUS RUNDE 1:
${kurz(K(p.id))}

DIE KARTEN DER ANDEREN FUENF:
${p.f.rollen.filter(x => x !== p.id).map(x => kurz(K(x))).join('\n\n')}

DU HAST ZWEI ZUEGE. Beide sind Pflicht, beide richten sich gegen eine FREMDE Karte.

REGELN, ohne die ein Zug nicht zaehlt:
1. Benenne, was in der angegriffenen Karte TATSAECHLICH STEHT. Ein Einwand gegen etwas, das dort nicht steht, ist ein Leerzug.
2. Nenne die RETTUNGSBEDINGUNG: unter welchem Umstand die angegriffene Karte doch traegt. Wer keine nennen kann, hat keinen Einwand, sondern eine Meinung.
3. Greife aus DEINEM Feld heraus an. Dein Mandat faerbt dein Urteil, und das ist gewollt - aber der Angriff muss aus deiner Sachkenntnis kommen, nicht aus allgemeiner Skepsis.
4. Zwei Zuege gegen dieselbe Karte sind erlaubt, wenn sie verschiedene Groessen betreffen.

Besonders zu pruefen: Ein Durchgriff D ueber 1,0 behauptet, dass mehr Personalbedarf verschwindet als Arbeitszeit frei wird. Das ist moeglich, verlangt aber einen Mechanismus - Standortschliessung, Konsolidierung, Skaleneffekt. Wer ihn nicht nennt, hat eine Luecke.`,
  { label: `Zug ${p.id}`, phase: 'Kartenzuege', schema: S_ZUG }
).then(z => ({ gruppe: p.f.gruppe, id: p.id, ...z })))

const Z2 = zuege.filter(Boolean)
const leer = Z2.filter(z => !String(z.zug1.rettungsbedingung).trim() || !String(z.zug2.rettungsbedingung).trim()).length
log(`Kartenzuege: ${Z2.length * 2} Zuege von ${Z2.length} Rollen, ${leer} ohne Rettungsbedingung`)

/* ------------------------------------------------------ Runde 2c: Dissens */

phase('Dissens')

const S_DISSENS = {
  type: 'object',
  properties: {
    dissens: {
      type: 'array', minItems: 1,
      items: {
        type: 'object',
        properties: {
          streitpunkt: { type: 'string' },
          karte_a: { type: 'string' }, karte_b: { type: 'string' },
          baenke: { type: 'string', description: 'welche Baenke sich gegenueberstehen' },
          entscheidungsgroesse: { type: 'string', description: 'was man messen muesste, um den Streit zu beenden - mit Quelle und fruehestem Messzeitpunkt' },
        },
        required: ['streitpunkt', 'karte_a', 'karte_b', 'baenke', 'entscheidungsgroesse'],
      },
    },
    beigelegt: { type: 'array', items: { type: 'string' }, description: 'Streitpunkte, die sich in der Diskussion aufgeloest haben' },
  },
  required: ['dissens', 'beigelegt'],
}

const protokolle = await pipeline(F, (f) => agent(
`Du bist Gruppenleitung der Gruppe ${f.gruppe + 1}. Die Diskussion ist gelaufen. Schreibe das Dissensprotokoll.

EURE STREITFRAGE WAR: ${f.streitfrage}

DIE ZWOELF ZUEGE:
${Z2.filter(z => z.gruppe === f.gruppe).map(z => `${z.id} gegen ${z.zug1.gegen} [${z.zug1.art}]: ${z.zug1.was}\n   Rettungsbedingung: ${z.zug1.rettungsbedingung}\n${z.id} gegen ${z.zug2.gegen} [${z.zug2.art}]: ${z.zug2.was}\n   Rettungsbedingung: ${z.zug2.rettungsbedingung}`).join('\n\n')}

Je offenem Streitpunkt ein Eintrag mit drei Angaben: die beiden unvereinbaren Karten, welche Baenke sich gegenueberstehen, und DIE ENTSCHEIDUNGSGROESSE.

Die Entscheidungsgroesse ist der eigentliche Ertrag dieser Runde. Nicht die Einigung, sondern die Benennung dessen, woran die Uneinigkeit haengt: Welche Zahl, aus welcher Quelle, ab wann messbar, wuerde den Streit beenden? Eine Entscheidungsgroesse ohne Quelle und ohne Zeitpunkt ist keine.

Was sich aufgeloest hat, kommt nach "beigelegt" - nicht in den Dissens.`,
  { label: `Dissens Gruppe ${f.gruppe + 1}`, phase: 'Dissens', schema: S_DISSENS }
).then(d => ({ gruppe: f.gruppe, streitfrage: f.streitfrage, ...d })))

const DIS = protokolle.filter(Boolean)
const punkte = DIS.reduce((n, d) => n + d.dissens.length, 0)
log(`Dissens: ${punkte} offene Streitpunkte, ${DIS.reduce((n, d) => n + d.beigelegt.length, 0)} beigelegt`)

/* ------------------------------------------------------------- Runde 3 */

phase('Runde 3')

const S_R3 = {
  type: 'object',
  properties: {
    p1: { type: 'number' }, p2: { type: 'number' }, p3: { type: 'number' }, p3_null: { type: 'number' },
    p3_absolut_vzae: { type: ['number', 'null'], description: 'null, wenn fuer dein Feld keine amtliche Bezugsgroesse existiert' },
    p4_ki: { type: 'number' }, p4_demografie: { type: 'number' }, p4_strukturreform: { type: 'number' },
    p5_leistungserbringer: { type: 'number' }, p5_preis_beitrag: { type: 'number' },
    p5_abfluss_ausland: { type: 'number' }, p5_neue_leistung: { type: 'number' },
    rechenweg: { type: 'string', description: 'Rechenweg aller vier Kernzahlen, der die Werte aus der Bezugsgroesse reproduziert' },
    aenderung: { type: 'string', description: 'was sich gegenueber Runde 1 geaendert hat und warum - oder warum nichts' },
    d_mechanismus: { type: 'string', description: 'nur wenn dein Durchgriff ueber 1,0 liegt: der Mechanismus, ueber den mehr Personalbedarf verschwindet als Arbeitszeit frei wird' },
    antwort_einwaende: { type: 'string', description: 'Antwort auf jeden Einwand gegen deine Karten' },
    stellungnahme_dissens: { type: 'string', description: 'Stellungnahme zu mindestens einem Dissenspunkt aus deiner Feldsicht' },
    bezugsgruppe_eigen: { type: 'string', description: 'nur wenn dein Feld keine amtliche Bezugsgroesse hat: die von dir benannte und belegte Bezugsgruppe' },
  },
  required: ['p1', 'p2', 'p3', 'p3_null', 'p4_ki', 'p4_demografie', 'p4_strukturreform',
             'p5_leistungserbringer', 'p5_preis_beitrag', 'p5_abfluss_ausland', 'p5_neue_leistung',
             'rechenweg', 'aenderung', 'antwort_einwaende', 'stellungnahme_dissens'],
}

const DISSENSTEXT = DIS.map(d => `GRUPPE ${d.gruppe + 1} - Streitfrage: ${d.streitfrage}\n` +
  d.dissens.map(x => `  STREITPUNKT: ${x.streitpunkt}\n    ${x.karte_a} gegen ${x.karte_b} (${x.baenke})\n    Entscheidungsgroesse: ${x.entscheidungsgroesse}`).join('\n')).join('\n\n')

function einwaendeGegen(id) {
  const e = []
  for (const z of Z2) {
    if (z.zug1.gegen === id) e.push(`von ${z.id} [${z.zug1.art}]: ${z.zug1.was}\n   Rettungsbedingung: ${z.zug1.rettungsbedingung}`)
    if (z.zug2.gegen === id) e.push(`von ${z.id} [${z.zug2.art}]: ${z.zug2.was}\n   Rettungsbedingung: ${z.zug2.rettungsbedingung}`)
  }
  return e.length ? e.join('\n') : '(keiner - dann schreibe das und begruende, ob deine Karte damit geprueft ist oder nur unbeachtet blieb)'
}

function promptR3(r) {
  const basis = r.vzae > 0
    ? `DEINE BEZUGSGRUPPE: ${r.bezugsgruppe} = ${r.vzae} Vollzeitaequivalente (Zuordnung "${r.zuordnung}").\nRechne gegen diese Zahl und gib P3 zusaetzlich in absoluten Vollkraeften an.`
    : `DEINE BEZUGSGRUPPE: Fuer dein Feld weist die amtliche Statistik KEINE Vollzeitaequivalente aus. Nenne P3 als Prozentwert gegen eine von dir selbst benannte und BELEGTE Bezugsgruppe, trage diese in "bezugsgruppe_eigen" ein, und lass die absolute Vollkraeftezahl leer (null). Eine Null waere eine falsche Zahl; eine Leerstelle ist eine Auskunft.`
  return `Du bist im Rollendossier ${r.id}: ${r.rolle} (Bank ${r.bank}). Zweite Erhebung der Pflichtgroessen.

${basis}

${GER[r.geruest]}

Dein Geruest ist dasselbe wie in Runde 1. Das ist bindend: Nur so misst die Differenz die Wirkung der Diskussion und nicht einen Wechsel der Weltannahme.

DEINE EIGENEN WERTE AUS RUNDE 1:
P1 ${r.p1} | P2 ${r.p2} | P3 ${r.p3} | P3_0 ${r.p3_null} | D ${r.d}
P4 KI ${r.p4[0]} / Demografie ${r.p4[1]} / Strukturreform ${r.p4[2]}
P5 Erbringer ${r.p5[0]} / Preis-Beitrag ${r.p5[1]} / Abfluss ${r.p5[2]} / neue Leistung ${r.p5[3]}
Deine Position war: ${r.position}

EINWAENDE GEGEN DEINE KARTEN:
${einwaendeGegen(r.id)}

DIE DISSENSPUNKTE ALLER FUENF GRUPPEN:
${DISSENSTEXT}

DIE ZAHLEN DER ANDEREN NEUNUNDNEUNZIG (Zahlen, keine Volltexte):
${MATRIX}

DEINE AUFGABE, in einem Zug:

1. DIE SECHS PFLICHTGROESSEN ERNEUT, mit Rechenweg. Aenderung ist erlaubt und Nichtaenderung auch - beides ist zu BEGRUENDEN. Wer nichts aendert, weil ihn nichts ueberzeugt hat, schreibt das und sagt warum. Wer aendert, benennt, welches Argument ihn bewegt hat.
   P4 muss auf genau 100 summieren, P5 ebenso.
2. EINE ANTWORT AUF JEDEN EINWAND gegen deine Karten. Auch auf die, die du zurueckweist - dann mit Begruendung.
3. EINE STELLUNGNAHME zu mindestens einem Dissenspunkt aus deiner Feldsicht.

ZWEI HARTE REGELN:
- Der Rechenweg muss die Werte aus der Bezugsgroesse reproduzieren. Jemand rechnet nach.
- Liegt dein Durchgriff |P3 - P3_0| geteilt durch (P1 mal P2 durch 100) ueber 1,0, dann behauptest du, dass mehr Personalbedarf verschwindet als Arbeitszeit frei wird. Das ist moeglich - ueber Standortschliessung, Konsolidierung, Skaleneffekt -, aber du musst den Mechanismus in "d_mechanismus" benennen. Ohne Mechanismus ist der Wert zu senken.

Eine Sachkorrektur aus der Quellenpruefung, die alle Rollen betrifft: Die Anlage 1 zu Paragraf 135e SGB V enthaelt 61 belegte Leistungsgruppen, nicht 65 - die Nummern 3, 16, 47 und 65 sind als "nicht belegt" gekennzeichnet.`
}

const KONTROLLARM = ['A01', 'A02', 'A06', 'A08', 'A09', 'C01', 'C03', 'B08', 'F07', 'H06']
const ITEMS = ROLLEN.map(r => ({ r, kontroll: false }))
  .concat(ROLLEN.filter(r => KONTROLLARM.includes(r.id)).map(r => ({ r, kontroll: true })))

const roh = await pipeline(ITEMS, (it) => agent(promptR3(it.r), {
  label: it.kontroll ? `R3 ${it.r.id} (Kontrollarm)` : `R3 ${it.r.id}`,
  phase: 'Runde 3', schema: S_R3, model: it.kontroll ? 'sonnet' : undefined,
}).then(a => ({ ...it, antwort: a })))

const haupt = roh.filter(Boolean).filter(x => !x.kontroll)
const kontroll = roh.filter(Boolean).filter(x => x.kontroll)
log(`Runde 3: ${haupt.length} Rollen, ${kontroll.length} Kontrollarm, ${ITEMS.length - roh.filter(Boolean).length} Ausfaelle`)

/* --------------------------------------------------- Divergenzerhalt */

function quant(xs, p) {
  const s = [...xs].sort((a, b) => a - b), i = (s.length - 1) * p, lo = Math.floor(i), hi = Math.ceil(i)
  return lo === hi ? s[lo] : s[lo] + (s[hi] - s[lo]) * (i - lo)
}
const iqr = xs => quant(xs, .75) - quant(xs, .25)
const GR = ['p1', 'p2', 'p3', 'p3_null', 'p4_ki', 'p5_abfluss_ausland']
const divergenz = {}
for (const k of GR) {
  const r1 = ROLLEN.map(r => k === 'p4_ki' ? r.p4[0] : k === 'p5_abfluss_ausland' ? r.p5[2] : r[k])
  const r3 = haupt.map(x => x.antwort[k])
  divergenz[k] = { iqr1: Math.round(iqr(r1) * 100) / 100, iqr3: Math.round(iqr(r3) * 100) / 100,
                   verhaeltnis: Math.round(iqr(r3) / Math.max(iqr(r1), 0.01) * 100) / 100 }
}
const gehalten = Object.values(divergenz).filter(d => d.verhaeltnis >= 0.5).length
log(`Divergenzerhalt: ${gehalten} von ${GR.length} Groessen halten mindestens die Haelfte des IQR aus Runde 1`)
log(`Kriterium ${gehalten >= 5 ? 'ERFUELLT' : 'GERISSEN'} (Schwelle: mindestens fuenf von sechs)`)

const geaendert = haupt.filter(x => x.antwort.p1 !== x.r.p1 || x.antwort.p2 !== x.r.p2 || x.antwort.p3 !== x.r.p3).length
log(`Bewegung: ${geaendert} von ${haupt.length} Rollen haben mindestens eine Kernzahl geaendert`)

return {
  streitfragen: F,
  kartenzuege: Z2,
  dissens: DIS,
  runde3: haupt.map(x => ({ id: x.r.id, bank: x.r.bank, geruest: x.r.geruest, anker: x.r.anker,
                            vzae: x.r.vzae, ...x.antwort })),
  kontrollarm: kontroll.map(x => ({ id: x.r.id, ...x.antwort })),
  divergenzerhalt: divergenz,
  divergenz_gehalten: gehalten,
  geaendert,
}
'''

if __name__ == '__main__':
    main()
