#!/usr/bin/env python3
"""Erzeugt workflow-nacharbeit.js aus dem Ergebnis von Sitzung A.

Dreizehn Aufrufe, rund zehn USD:
  Quellenpruefung  10 - je ein Pruefer fuer ein Faktenblatt der Recherchebank.
                        Die Recherchebank ist der einzige Teil des Verfahrens, den
                        die Validierung nie angefasst hat, obwohl 64 von 110 Rollen
                        aus ihr zitieren. Ein Fehler dort sitzt in bis zu 19 Karten.
  Bezugsgroessen    3 - Rahmen aus der Gesundheitspersonalrechnung, Abbildung der
                        hundert Felder darauf, Pruefung der Abbildung.

Eingabe:  Szenariokonferenz/rohdaten/sitzung-a.json
Ausgabe:  Szenariokonferenz/workflow-nacharbeit.js
"""
import json, pathlib, sys

BASIS = pathlib.Path(__file__).resolve().parent
QUELLE = BASIS / 'rohdaten' / 'sitzung-a.json'
ZIEL = BASIS / 'workflow-nacharbeit.js'

VORLAGE = r'''export const meta = {
  name: 'nacharbeit-sitzung-a',
  description: 'Nacharbeit zu Sitzung A: Pruefung der zehn Faktenblaetter der Recherchebank und Reparatur der Bezugsgroessen ueber die Einrichtungsgliederung der Gesundheitspersonalrechnung',
  phases: [
    { title: 'Quellenpruefung', detail: 'Je ein Pruefer fuer ein Faktenblatt - der einzige nie validierte Teil des Verfahrens' },
    { title: 'Bezugsgroessen', detail: 'Rahmen, Abbildung der hundert Felder, Pruefung der Abbildung' },
  ],
}

const FAKTENBLAETTER = __FB__
const ROLLENLISTE = __ROLLEN__
const ALT = __ALT__

/* ------------------------------------------------------- Quellenpruefung */

phase('Quellenpruefung')

const S_QP = {
  type: 'object',
  properties: {
    beanstandungen: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          groesse: { type: 'string', description: 'die beanstandete Kennzahl, wortgleich aus dem Blatt' },
          art: { type: 'string', enum: ['Quelle existiert nicht', 'Quelle traegt die Zahl nicht', 'Stand falsch oder fehlend', 'Einheit oder Abgrenzung falsch', 'Fortschreibung statt Messung'] },
          was: { type: 'string', description: 'was die abgerufene Quelle tatsaechlich sagt' },
          schwere: { type: 'string', enum: ['zurueckgewiesen', 'mit-vorbehalt'] },
        },
        required: ['groesse', 'art', 'was', 'schwere'],
      },
    },
    geprueft: { type: 'number', description: 'Zahl der Kennzahlen, deren Quelle tatsaechlich abgerufen wurde' },
    nicht_abrufbar: { type: 'array', items: { type: 'string' }, description: 'Kennzahlen, deren Quelle sich nicht erreichen liess - weder Beleg noch Widerlegung' },
  },
  required: ['beanstandungen', 'geprueft', 'nicht_abrufbar'],
}

const pruefungen = await pipeline(FAKTENBLAETTER, (f) => agent(
`Du bist Pruefinstanz fuer EIN Faktenblatt der Recherchebank. Du hast kein eigenes Urteil zur Sache.

Dieses Blatt ist von hundert Rollen als Grundlage benutzt worden. Es ist bisher nie geprueft worden - anders als die Rollenkarten, die gegen ihre eigenen Quellen geprueft wurden. Ein Fehler hier steht deshalb gleichzeitig in vielen Karten und ist dort nicht auffindbar.

Pruefe JEDE Kennzahl einzeln auf vier Dinge:
1. EXISTENZ: Gibt es die angegebene Quelle an der angegebenen Fundstelle? Rufe sie ab.
2. DECKUNG: Steht dort der genannte Wert - nicht ungefaehr, sondern der Wert?
3. STAND: Stimmt das angegebene Jahr oder Stichdatum mit dem der abgerufenen Quelle ueberein?
4. ABGRENZUNG: Stimmen Einheit und Grundgesamtheit? Vollkraefte und Koepfe, Beschaeftigte und sozialversicherungspflichtig Beschaeftigte, Faelle und Patienten sind verschiedene Dinge.

Melde nur, was nicht in Ordnung ist. Ist alles in Ordnung, gib eine leere Liste zurueck. Was du nicht abrufen kannst, kommt nach "nicht_abrufbar" - nicht in die Beanstandungen: eine unerreichbare Quelle ist weder belegt noch widerlegt.

FAKTENBLATT ${f.id} - ${f.domaene}

${f.kennzahlen.map((k, i) => `${i + 1}. ${k.groesse}: ${k.wert} ${k.einheit} (Stand ${k.stand})\n   Quelle: ${k.quelle} | Fundstelle: ${k.fundstelle}`).join('\n')}

AUSGEWIESENE LUECKEN DES BLATTES: ${(f.luecken || []).join('; ') || 'keine'}
HINWEIS DES BLATTES: ${f.hinweis || '-'}`,
  { label: `Quellenpruefung ${f.id}`, phase: 'Quellenpruefung', schema: S_QP, model: 'sonnet' }
).then(p => ({ id: f.id, domaene: f.domaene, kennzahlen: f.kennzahlen.length, ...p })))

const qp = pruefungen.filter(Boolean)
const bean = qp.reduce((n, p) => n + p.beanstandungen.length, 0)
const hart = qp.reduce((n, p) => n + p.beanstandungen.filter(b => b.schwere === 'zurueckgewiesen').length, 0)
const kz = qp.reduce((n, p) => n + p.kennzahlen, 0)
log(`Quellenpruefung: ${qp.length} Blaetter, ${kz} Kennzahlen, ${bean} Beanstandungen davon ${hart} zurueckgewiesen`)

/* -------------------------------------------------------- Bezugsgroessen */

phase('Bezugsgroessen')

const S_RAHMEN = {
  type: 'object',
  properties: {
    einrichtungsarten: {
      type: 'array', minItems: 8,
      items: {
        type: 'object',
        properties: {
          name: { type: 'string' },
          vzae: { type: 'number' },
          stand: { type: 'string' },
          quelle: { type: 'string' },
          fundstelle: { type: 'string' },
        },
        required: ['name', 'vzae', 'stand', 'quelle', 'fundstelle'],
      },
    },
    summe_vzae: { type: 'number' },
    disjunkt: { type: 'string', description: 'Beleg dafuer, dass die Einrichtungsarten einander nicht ueberlappen' },
    grenzen: { type: 'array', items: { type: 'string' } },
  },
  required: ['einrichtungsarten', 'summe_vzae', 'disjunkt', 'grenzen'],
}

const rahmen = await agent(
`Du bist R03, Rechercheur fuer Gesundheitspersonal. Du lieferst den RAHMEN, auf den anschliessend hundert Felder abgebildet werden.

Der erste Versuch ist gescheitert, und zwar an der Quellenwahl: Er stuetzte sich auf die Krankenhausstatistik und die Pflegestatistik. Beide zerlegen nur ihren eigenen Sektor. Ergebnis waren sieben von hundert Feldern mit einer Bezugsgroesse und 42 Prozent Abdeckung; der gesamte ambulante Bereich, die Kostentraeger, die Selbstverwaltung und die Vorleistungsindustrien blieben leer.

DEIN AUFTRAG: Die Gesundheitspersonalrechnung des Statistischen Bundesamtes gliedert das gesamte Gesundheitspersonal nach EINRICHTUNGSART und weist dazu Beschaeftigte UND Vollzeitaequivalente aus. Diese Gliederung ist der gesuchte Rahmen. Liefere sie vollstaendig, auf der tiefsten Ebene, die amtlich ausgewiesen ist - also nicht nur "ambulante Einrichtungen", sondern deren Untergliederung in Arztpraxen, Zahnarztpraxen, Praxen sonstiger medizinischer Berufe, Apotheken, ambulante Pflege und so fort, ebenso fuer die stationaeren Einrichtungen, den Rettungsdienst, die Verwaltung, die sonstigen Einrichtungen und die Vorleistungsindustrien.

REGELN:
- Rufe die Quelle wirklich ab. Nenne Tabelle und Stichtag.
- Nur Vollzeitaequivalente. Koepfe nie mit VZAE mischen.
- Die Einrichtungsarten muessen einander ausschliessen. Belege das ausdruecklich im Feld "disjunkt": Die Summe der Teile muss die amtlich ausgewiesene Gesamtsumme ergeben.
- Schaetze nichts. Eine Einrichtungsart ohne amtliche VZAE-Zahl wird mit 0 geliefert und in "grenzen" benannt.
- In "grenzen" gehoeren ausserdem: Stichtagsunterschiede zu anderen Statistiken, die Behandlung von Leiharbeit, und jede Abgrenzung, die spaeter zu Doppelzaehlung fuehren koennte.`,
  { label: 'Einrichtungsrahmen', phase: 'Bezugsgroessen', schema: S_RAHMEN })

const S_ABB = {
  type: 'object',
  properties: {
    felder: {
      type: 'array', minItems: 100, maxItems: 100,
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          bezugsgruppe: { type: 'string' },
          einrichtungsart: { type: 'string', description: 'aus dem Rahmen, wortgleich; leer wenn unbekannt' },
          vzae: { type: 'number' },
          anteil_begruendung: { type: 'string', description: 'wie der Anteil an der Einrichtungsart hergeleitet ist' },
          zuordnung: { type: 'string', enum: ['primaer', 'geteilt', 'unbekannt'] },
          geteilt_mit: { type: 'string' },
          quelle: { type: 'string' },
        },
        required: ['id', 'bezugsgruppe', 'einrichtungsart', 'vzae', 'zuordnung', 'quelle'],
      },
    },
    summe_primaer: { type: 'number' },
    abdeckung_prozent: { type: 'number' },
    rest_vzae: { type: 'number' },
    rest_begruendung: { type: 'string' },
  },
  required: ['felder', 'summe_primaer', 'abdeckung_prozent', 'rest_vzae', 'rest_begruendung'],
}

const abbildung = await agent(
`Du bist R03. Bilde die hundert Felder auf den Rahmen ab, den du gerade geliefert hast.

DER RAHMEN:
${rahmen.einrichtungsarten.map(e => `${e.name}: ${e.vzae} VZAE (Stand ${e.stand}, ${e.quelle})`).join('\n')}
Summe: ${rahmen.summe_vzae} VZAE
Disjunktheit: ${rahmen.disjunkt}
Grenzen: ${(rahmen.grenzen || []).join(' | ')}

DIE HUNDERT FELDER:
${ROLLENLISTE}

DIE ALTE ZUORDNUNG, soweit sie amtlich belegt war und weiter gilt - uebernimm sie unveraendert, wenn sie zum Rahmen passt, und begruende jede Abweichung:
${ALT}

VORGEHEN je Feld:
1. Welche Einrichtungsart des Rahmens enthaelt diese Menschen? Trage sie wortgleich ein.
2. Welcher Teil dieser Einrichtungsart ist es? Leite den Anteil her - aus einer Berufsgruppenstatistik, einer Fachgruppenzaehlung, einer Mitgliederzahl. Schreibe die Herleitung in "anteil_begruendung". Wo nur die ganze Einrichtungsart passt, nimm sie ganz.
3. Wo zwei Felder ueber dieselben Menschen sprechen, entscheide: eines "primaer", das andere "geteilt" mit Nennung des Feldes. Nur "primaer" geht in die Summe.
4. Felder, die ueber das gesamte Gesundheitswesen oder die Gesamtwirtschaft sprechen (Baenke J, K, M und die Rolle N01), sind "geteilt", nicht "primaer".

REGELN, die ueber allem stehen:
- SCHAETZE NICHT. Ein Feld ohne amtliche Grundlage bleibt vzae 0 und "unbekannt". Die Reparatur zielt auf bessere Quellenwahl, nicht auf Schaetzung.
- Die Summe der primaeren Felder je Einrichtungsart darf deren Rahmenwert NICHT ueberschreiten. Pruefe das und weise es nach.
- Vollkraefte und Koepfe bleiben getrennt.
- Nenne "abdeckung_prozent" als Summe primaer geteilt durch Rahmensumme.

Genau hundert Eintraege, einer je Feld-ID.`,
  { label: 'Abbildung der hundert Felder', phase: 'Bezugsgroessen', schema: S_ABB })

const S_PRAB = {
  type: 'object',
  properties: {
    beanstandungen: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          feld: { type: 'string' },
          art: { type: 'string', enum: ['Ueberschreitung der Einrichtungsart', 'Doppelzaehlung', 'geschaetzt statt belegt', 'falsche Einrichtungsart', 'Koepfe statt VZAE', 'Rechenfehler'] },
          was: { type: 'string' },
        },
        required: ['feld', 'art', 'was'],
      },
    },
    summenprobe: { type: 'string', description: 'Nachrechnung: Summe primaer je Einrichtungsart gegen den Rahmenwert' },
    abdeckung_bestaetigt: { type: 'number' },
  },
  required: ['beanstandungen', 'summenprobe', 'abdeckung_bestaetigt'],
}

const pruefungAbb = await agent(
`Du bist Pruefinstanz. Pruefe eine Abbildung von hundert Feldern auf einen Rahmen aus Einrichtungsarten. Du hast kein eigenes Urteil zur Sache; du rechnest nach.

Pruefe genau vier Dinge:
1. UEBERSCHREITUNG: Uebersteigt die Summe der primaeren Felder einer Einrichtungsart deren Rahmenwert? Rechne jede Einrichtungsart einzeln nach und schreibe das Ergebnis in "summenprobe".
2. DOPPELZAEHLUNG: Sind zwei Felder primaer, die ueber dieselben Menschen sprechen?
3. SCHAETZUNG: Traegt ein Feld eine Zahl, deren Herleitung keine Quelle nennt, sondern eine Annahme? Das ist zu beanstanden, auch wenn die Zahl plausibel ist.
4. EINHEIT: Wird irgendwo eine Kopfzahl als VZAE gefuehrt?

Melde nur Beanstandungen. "abdeckung_bestaetigt" ist die von dir nachgerechnete Abdeckung in Prozent.

DER RAHMEN:
${rahmen.einrichtungsarten.map(e => `${e.name}: ${e.vzae} VZAE`).join('\n')}
Summe: ${rahmen.summe_vzae}

DIE ABBILDUNG (Feld | Einrichtungsart | VZAE | Zuordnung | Herleitung):
${abbildung.felder.map(f => `${f.id} | ${f.einrichtungsart || '-'} | ${f.vzae} | ${f.zuordnung} | ${(f.anteil_begruendung || f.quelle || '').slice(0, 200)}`).join('\n')}

Behauptete Summe primaer: ${abbildung.summe_primaer}, behauptete Abdeckung: ${abbildung.abdeckung_prozent} Prozent`,
  { label: 'Pruefung der Abbildung', phase: 'Bezugsgroessen', schema: S_PRAB, model: 'sonnet' })

const mitZahl = abbildung.felder.filter(f => f.vzae > 0).length
const primaer = abbildung.felder.filter(f => f.zuordnung === 'primaer').length
log(`Bezugsgroessen: ${mitZahl} von 100 Feldern mit Zahl, davon ${primaer} primaer, Abdeckung ${abbildung.abdeckung_prozent} Prozent (nachgerechnet ${pruefungAbb.abdeckung_bestaetigt})`)
log(`Kriterium Bezugsgroessendeckung: ${primaer >= 60 && abbildung.abdeckung_prozent >= 70 ? 'ERFUELLT' : 'GERISSEN'} (Schwelle 60 Felder und 70 Prozent)`)

return {
  quellenpruefung: qp,
  quellenpruefung_summe: { blaetter: qp.length, kennzahlen: kz, beanstandungen: bean, zurueckgewiesen: hart },
  rahmen,
  abbildung,
  pruefung_abbildung: pruefungAbb,
  kriterium: { felder_primaer: primaer, abdeckung: abbildung.abdeckung_prozent, erfuellt: primaer >= 60 && abbildung.abdeckung_prozent >= 70 },
}
'''


def main():
    if not QUELLE.exists():
        sys.exit(f'fehlt: {QUELLE}\nErst die Rueckgabe von Sitzung A dorthin schreiben.')
    d = json.loads(QUELLE.read_text(encoding='utf-8'))
    fb = d.get('faktenblaetter') or []
    r1 = d.get('runde1') or []
    zerl = (d.get('zerlegung') or {}).get('felder') or []
    if not fb:
        sys.exit('kein Feld "faktenblaetter" in der Eingabe')

    rollen = '\n'.join(f"{a.get('id')} | {a.get('rolle', '?')} | Bank {a.get('bank')}" for a in r1)
    alt = '\n'.join(
        f"{f['id']} | {f.get('bezugsgruppe', '')[:90]} | {f.get('vzae')} VZAE | {f.get('zuordnung')} | {f.get('quelle', '')[:120]}"
        for f in zerl if f.get('vzae'))

    js = VORLAGE
    js = js.replace('__FB__', json.dumps(fb, ensure_ascii=False))
    js = js.replace('__ROLLEN__', json.dumps(rollen, ensure_ascii=False))
    js = js.replace('__ALT__', json.dumps(alt, ensure_ascii=False))
    ZIEL.write_text(js, encoding='utf-8')
    print(f'{ZIEL.name} geschrieben: {len(fb)} Faktenblaetter, {len(r1)} Rollen, '
          f'{len(alt.splitlines())} belegte Altzuordnungen, {round(len(js)/1024)} KB')
    print('Start:  Workflow({scriptPath: "<Scratchpad>/nacharbeit.js"})   13 Aufrufe, rund 10 USD')


if __name__ == '__main__':
    main()
