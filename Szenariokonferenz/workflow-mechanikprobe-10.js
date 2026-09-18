export const meta = {
  name: 'mechanikprobe-10',
  description: 'Mechanikprobe des Konzepts v2 mit zehn Rollen: sechs Pflichtgroessen, zwei Szenariogerueste, Modellkontrollarm, maschinell gesetzte Fehler, Streitauswahl, Kartendiskussion, zweite Erhebung, Optionenrunde',
  phases: [
    { title: 'Runde 1', detail: 'Zehn Rollen recherchieren im eigenen Feld und liefern Position, Befunde und sechs Pflichtgroessen; zwei davon zusaetzlich auf einem zweiten Modell' },
    { title: 'Validierung', detail: 'Pruefinstanz je Rolle, in neun Karten sind vorher maschinell Fehler gesetzt worden' },
    { title: 'Runde 2', detail: 'Streitfrage, zwei Kartenzuege je ausgewaehlter Rolle, Dissensprotokoll' },
    { title: 'Runde 3', detail: 'Pflichtgroessen zum zweiten Mal, Antwort auf die Einwaende' },
    { title: 'Runde 4', detail: 'Hebelsatz aus der Tafel, Optionenbewertung je Rolle' },
  ],
}

// ---------------------------------------------------------------- Aufstellung

const GERUEST = {
  A: `SZENARIOGERUEST A - Fortschreibung (Stichjahr 2031)
- Reales BIP-Wachstum im Mittel +0,8 % p.a. 2026-2031, keine Rezessionsjahre.
- Erwerbspersonenpotenzial rund 1,5 Mio niedriger als 2025.
- GKV: allgemeiner Beitragssatz einschliesslich Zusatzbeitrag rund 17,9 %, keine Leistungskuerzungen.
- Tarifabschluesse im Gesundheitswesen nominal rund +3,0 % p.a.
- Krankenhausreform (KHVVG) wie beschlossen umgesetzt; Leistungsgruppen ab 2027 verguetungswirksam, Vorhaltefinanzierung greift.
- EU AI Act: Hochrisikopflichten vollstaendig anwendbar, benannte Stellen arbeiten fristgerecht.
- EHDS-Primaernutzung ab 2029 im Regelbetrieb.
- Zinsniveau rund 2,5 %.`,
  B: `SZENARIOGERUEST B - Gegenwelt (Stichjahr 2031)
- Reales BIP-Wachstum im Mittel +0,1 % p.a. 2026-2031, darin zwei Rezessionsjahre.
- Erwerbspersonenpotenzial rund 1,9 Mio niedriger als 2025 (schwaechere Zuwanderung).
- GKV: allgemeiner Beitragssatz einschliesslich Zusatzbeitrag rund 19,1 %, Leistungskuerzungen in der politischen Debatte.
- Tarifabschluesse im Gesundheitswesen nominal rund +4,5 % p.a. (Knappheitsreaktion).
- Krankenhausreform in Teilen gescheitert: mehrere Laender setzen Leistungsgruppen abweichend um, Vorhaltefinanzierung verschoben.
- EU AI Act: Vollzug verzoegert, benannte Stellen ueberlastet, Uebergangsfristen verlaengert.
- EHDS-Primaernutzung 2031 noch nicht im Regelbetrieb.
- Zinsniveau rund 4,0 %.`,
}

const ROLLEN = [
  { id: 'A05', rolle: 'Oberarzt Radiologie im Krankenhaus', mandat: 'Befundqualitaet bei steigender Untersuchungszahl sichern', anker: 'Befundzeiten, CE-zertifizierte Befundungssoftware, Teleradiologie', blindstelle: 'am staerksten exponierte Fachrichtung, neigt zur Abwehr', bezugsgruppe: 'Aerztinnen und Aerzte in der Radiologie im Krankenhaus', vzae: 9500, zuordnung: 'primaer', geruest: 'A' },
  { id: 'A08', rolle: 'Pflegedirektor eines Krankenhauses', mandat: 'Dienstplanfaehigkeit und Pflegebudget', anker: '§ 6a KHEntgG, PpUGV, PPR 2.0, PPBV-Meldung', blindstelle: 'argumentiert regulatorisch und haelt das fuer physisch', bezugsgruppe: 'Pflegepersonal im Krankenhaus ohne Intensivpflege', vzae: 290000, zuordnung: 'primaer', geruest: 'B' },
  { id: 'B01', rolle: 'Hausaerztin im laendlichen Einzelsitz', mandat: 'Sicherstellung ohne Nachfolge', anker: 'Bedarfsplanung, Hausarztvertrag, Wegezeiten', blindstelle: 'haelt die eigene Praxisform fuer die schutzwuerdige Norm', bezugsgruppe: 'Hausaerztinnen und Hausaerzte in der vertragsaerztlichen Versorgung', vzae: 44000, zuordnung: 'primaer', geruest: 'A' },
  { id: 'B08', rolle: 'Apothekerin einer Offizinapotheke', mandat: 'Arzneimittelversorgung und Beratungsleistung', anker: 'Apothekenbetriebsordnung, E-Rezept, Fixum und Rabattvertraege', blindstelle: 'Beratungsanteil wird hoeher eingeschaetzt, als er abgerechnet wird', bezugsgruppe: 'Apothekerinnen und Apotheker in oeffentlichen Apotheken', vzae: 40000, zuordnung: 'primaer', geruest: 'B' },
  { id: 'C01', rolle: 'Pflegefachkraft Intensivstation', mandat: 'Patientensicherheit bei knapper Besetzung', anker: 'Verhaeltniszahlen, Schichtrealitaet, Uebergabeprozess', blindstelle: 'verallgemeinert die Intensivsituation auf die Normalstation', bezugsgruppe: 'Pflegefachpersonen auf Intensivstationen', vzae: 60000, zuordnung: 'primaer', geruest: 'A' },
  { id: 'D01', rolle: 'Vorstand einer grossen Ersatzkasse', mandat: 'Beitragssatzstabilitaet und Mitgliederbindung', anker: 'Verwaltungskosten je Versicherten, Morbi-RSA, § 31a SGB X', blindstelle: 'Wettbewerb um gute Risiken bleibt unausgesprochen', bezugsgruppe: 'Beschaeftigte der gesetzlichen Krankenkassen', vzae: 140000, zuordnung: 'primaer', geruest: 'A' },
  { id: 'D04', rolle: 'Begutachtung im Medizinischen Dienst', mandat: 'Pruefqualitaet und Unabhaengigkeit', anker: 'Pruefquoten § 275c SGB V, Begutachtungsanleitungen', blindstelle: 'prueft, was pruefbar ist, nicht was wichtig ist', bezugsgruppe: 'Beschaeftigte der Medizinischen Dienste', vzae: 11000, zuordnung: 'primaer', geruest: 'B' },
  { id: 'E06', rolle: 'Geschaeftsfuehrung eines Labordiagnostik-Konzerns', mandat: 'Durchsatz und Preisdruck', anker: 'EBM-Laborkapitel, Automatisierungsgrad, Skalenlogik', blindstelle: 'Vorreiterrolle in der Automatisierung erzeugt Uebertragungsoptimismus', bezugsgruppe: 'Beschaeftigte in medizinischen Laboratorien', vzae: 55000, zuordnung: 'primaer', geruest: 'B' },
  { id: 'F05', rolle: 'Medizinische Fachangestellte in einer Praxis', mandat: 'Aufgabenzuschnitt und Eingruppierung', anker: 'Delegationsfaehigkeit, Praxisorganisation, MFA-Tarifvertrag', blindstelle: 'am staerksten betroffene Gruppe mit der schwaechsten Vertretung', bezugsgruppe: 'Medizinische Fachangestellte in Arztpraxen', vzae: 350000, zuordnung: 'primaer', geruest: 'A' },
  { id: 'J02', rolle: 'Arbeitsmarktoekonomin', mandat: 'Beschaeftigung, Matching, Qualifikation', anker: 'Erwerbspersonenpotenzial, Engpassanalyse, Arbeitsmarktprojektion', blindstelle: 'Berufswechsel wird als moeglich unterstellt, wo er es nicht ist', bezugsgruppe: 'Erwerbstaetige im Gesundheitswesen insgesamt (ueberschneidet alle uebrigen Felder)', vzae: 3600000, zuordnung: 'geteilt', geruest: 'B' },
]

const KONTROLLARM = ['A05', 'D01']

const HEMMNISSE = 'Recht und Zulassung | Refinanzierung und Abrechnung | Haftung | Personalbindung und Tarif | Investitionsfaehigkeit | Akzeptanz von Patienten oder Beschaeftigten | Datenverfuegbarkeit'

function auftrag(r) {
  return `Du bist im Rollendossier: ${r.rolle}.
MANDAT (darf und soll dein Urteil faerben): ${r.mandat}
WISSENSANKER: ${r.anker}
BLINDSTELLE (dir mitgeteilt, damit die Auswertung sie pruefen kann - du sollst sie NICHT kompensieren): ${r.blindstelle}

DEINE BEZUGSGRUPPE, verbindlich vorgegeben: ${r.bezugsgruppe} = ${r.vzae} Vollzeitaequivalente (VZAE), Zuordnungsart "${r.zuordnung}".
Diese Zahl ist ein Probewert der Mechanikprobe und nicht amtlich geprueft. Rechne trotzdem ausschliesslich gegen sie.

${GERUEST[r.geruest]}

Rechne alle Groessen gegen dieses Geruest. Wenn du es fuer falsch haeltst, sag das im Feld "geruest_einwand" - aber rechne trotzdem dagegen.`
}

const PFLICHT = `DIE SECHS PFLICHTGROESSEN, Stichjahr 2031. Fuer jede gilt: erst der Rechenweg, dann das Ergebnis. Der Rechenweg muss den genannten Wert aus der genannten Bezugsgruppengroesse reproduzieren - jemand muss ihn nachrechnen koennen.

P1: Anteil der heute in deinem Feld geleisteten Arbeitszeit, der bis 2031 technisch durch KI oder Automatisierung ersetzbar ist - unabhaengig davon, ob es geschieht. Prozent, 0-100.
P2: Anteil VON P1, der bis 2031 im Regelbetrieb tatsaechlich wirksam wird. Prozent von P1, 0-100. Nenne das bindende Hemmnis aus dieser geschlossenen Liste: ${HEMMNISSE}
P3: Veraenderung des Personal-BEDARFS in deinem Feld bis 2031, in Prozent der VZAE deiner Bezugsgruppe (-100 bis +50) UND in absoluten VZAE. Achtung: Arbeitszeit, die wegfaellt, ist nicht dasselbe wie Personalbedarf, der wegfaellt.
P3_NULL: dieselbe Groesse unter der Gegenannahme, dass KI und Automatisierung bis 2031 STAGNIEREN - also nur Demografie, Recht und Strukturreform wirken. Prozent der VZAE.
P4: Ursachenanteil an P3, drei Prozentwerte mit Summe genau 100: KI und Automatisierung / Demografie und Erwerbspersonenrueckgang / Struktur- und Rechtsreform.
P5: Verbleib des Effizienzgewinns in deinem Feld, vier Prozentwerte mit Summe genau 100: bleibt beim Leistungserbringer / weitergegeben als Preis oder Beitragssatz / abgeflossen als Lizenz-, Geraete- oder Cloudentgelt ueberwiegend ausserhalb Deutschlands / finanziert zusaetzliche Leistung im eigenen Feld.

P4 und P3_NULL sind eine Gegenprobe zueinander: (P3 - P3_NULL) geteilt durch P3 muss zum P4-Wert fuer KI passen. Rechne das nach, bevor du antwortest.

QUELLENPFLICHT: Jeder Befund braucht eine Quelle, die du tatsaechlich abgerufen hast, mit Datum und Fundstelle. Erfinde keine. Wenn du nichts findest, schreibe "keine Quelle gefunden" statt zu raten.`

const S_R1 = {
  type: 'object',
  properties: {
    position: { type: 'string', description: 'Die These zu deinem Feld bis 2031, drei bis fuenf Saetze' },
    falsifikator: { type: 'string', description: 'Der Satz, der deine Position widerlegen wuerde' },
    befunde: {
      type: 'array', minItems: 3, maxItems: 5,
      items: {
        type: 'object',
        properties: { aussage: { type: 'string' }, quelle: { type: 'string' }, fundstelle: { type: 'string' }, abrufdatum: { type: 'string' } },
        required: ['aussage', 'quelle', 'fundstelle'],
      },
    },
    p1_rechenweg: { type: 'string' }, p1: { type: 'number' }, p1_intervall: { type: 'array', items: { type: 'number' }, minItems: 2, maxItems: 2 },
    p2_rechenweg: { type: 'string' }, p2: { type: 'number' }, p2_hemmnis: { type: 'string' },
    p3_rechenweg: { type: 'string' }, p3: { type: 'number' }, p3_absolut_vzae: { type: 'number' },
    p3_null_rechenweg: { type: 'string' }, p3_null: { type: 'number' },
    p4_ki: { type: 'number' }, p4_demografie: { type: 'number' }, p4_strukturreform: { type: 'number' }, p4_begruendung: { type: 'string' },
    p5_leistungserbringer: { type: 'number' }, p5_preis_beitrag: { type: 'number' }, p5_abfluss_ausland: { type: 'number' }, p5_neue_leistung: { type: 'number' }, p5_begruendung: { type: 'string' },
    geruest_einwand: { type: 'string' },
  },
  required: ['position', 'falsifikator', 'befunde', 'p1_rechenweg', 'p1', 'p1_intervall', 'p2_rechenweg', 'p2', 'p2_hemmnis', 'p3_rechenweg', 'p3', 'p3_absolut_vzae', 'p3_null_rechenweg', 'p3_null', 'p4_ki', 'p4_demografie', 'p4_strukturreform', 'p4_begruendung', 'p5_leistungserbringer', 'p5_preis_beitrag', 'p5_abfluss_ausland', 'p5_neue_leistung', 'p5_begruendung', 'geruest_einwand'],
}

// ------------------------------------------------- Runde 1 und Modellkontrollarm

phase('Runde 1')

const ITEMS = ROLLEN.map(r => ({ r, kontroll: false }))
  .concat(ROLLEN.filter(r => KONTROLLARM.includes(r.id)).map(r => ({ r, kontroll: true })))

function promptR1(r) {
  return `${auftrag(r)}

${PFLICHT}

Recherchiere zuerst in DEINEM Feld - nicht in der Gesamtwirtschaft. Dann antworte.`
}

const roh = await pipeline(
  ITEMS,
  (item) => agent(promptR1(item.r), {
    label: item.kontroll ? `R1 ${item.r.id} (Kontrollarm)` : `R1 ${item.r.id}`,
    phase: 'Runde 1',
    schema: S_R1,
    model: item.kontroll ? 'sonnet' : undefined,
  }).then(a => ({ ...item, antwort: a })),
)

const haupt = roh.filter(Boolean).filter(x => !x.kontroll)
const kontrollR1 = roh.filter(Boolean).filter(x => x.kontroll)
log(`Runde 1: ${haupt.length} Rollen, ${kontrollR1.length} Kontrollarm-Laeufe zurueck`)

// ------------------------------------------------------------ Gesetzte Fehler

const FREMDQUELLE = 'Bundesagentur fuer Arbeit, Fachkraefteengpassanalyse 2024, S. 17'
const MANDATSBRUCH = ' Dieselbe Einschaetzung gilt unveraendert auch fuer die Zahnmedizin, die Veterinaermedizin und den Rettungsdienst.'
const SAAT = { 0: ['p1', 'befund_1'], 2: ['p3'], 3: ['position', 'p2'], 5: ['befund_2'], 7: ['position', 'befund_1'], 8: ['p1'] }

const gesetzt = []
const vorgelegt = haupt.map((x, i) => {
  const a = JSON.parse(JSON.stringify(x.antwort))
  for (const wo of (SAAT[i] || [])) {
    if (wo === 'p1') { a.p1 = Math.round(a.p1 * 3 + 7); gesetzt.push({ rolle: x.r.id, wo, art: 'Zahl passt nicht mehr zum Rechenweg' }) }
    else if (wo === 'p2') { a.p2 = Math.round(a.p2 * 3 + 7); gesetzt.push({ rolle: x.r.id, wo, art: 'Zahl passt nicht mehr zum Rechenweg' }) }
    else if (wo === 'p3') { a.p3_absolut_vzae = Math.round(a.p3_absolut_vzae * 4); gesetzt.push({ rolle: x.r.id, wo, art: 'absolute VZAE passen nicht zum Prozentwert' }) }
    else if (wo === 'position') { a.position = a.position + MANDATSBRUCH; gesetzt.push({ rolle: x.r.id, wo, art: 'Rolle spricht ausserhalb ihres Mandats' }) }
    else if (wo.startsWith('befund_')) {
      const k = Number(wo.split('_')[1]) - 1
      if (a.befunde[k]) { a.befunde[k].quelle = FREMDQUELLE; a.befunde[k].fundstelle = 'S. 17'; gesetzt.push({ rolle: x.r.id, wo, art: 'Quelle deckt die Aussage nicht' }) }
    }
  }
  return { r: x.r, a }
})
log(`${gesetzt.length} Fehler in ${Object.keys(SAAT).length} von ${haupt.length} Kartensaetzen gesetzt - der Pruefinstanz unbekannt`)

// ---------------------------------------------------------------- Validierung

phase('Validierung')

const WO = ['position', 'befund_1', 'befund_2', 'befund_3', 'befund_4', 'befund_5', 'p1', 'p2', 'p3', 'p3_null', 'p4', 'p5']
const S_VAL = {
  type: 'object',
  properties: {
    beanstandungen: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          wo: { type: 'string', enum: WO },
          was: { type: 'string' },
          schwere: { type: 'string', enum: ['zurueckgewiesen', 'mit-vorbehalt'] },
        },
        required: ['wo', 'was', 'schwere'],
      },
    },
    rechenweg_traegt: { type: 'array', items: { type: 'string', enum: ['p1', 'p2', 'p3', 'p3_null'] }, description: 'welche Pflichtgroessen sich aus ihrem Rechenweg und der Bezugsgroesse nachrechnen lassen' },
    gesamturteil: { type: 'string', enum: ['gueltig', 'mit-vorbehalt', 'zurueckgewiesen'] },
  },
  required: ['beanstandungen', 'rechenweg_traegt', 'gesamturteil'],
}

function kartentext(r, a) {
  return `ROLLE ${r.id}: ${r.rolle}
MANDAT: ${r.mandat}
BEZUGSGRUPPE: ${r.bezugsgruppe} = ${r.vzae} VZAE

POSITION: ${a.position}
FALSIFIKATOR: ${a.falsifikator}

${a.befunde.map((b, i) => `BEFUND_${i + 1}: ${b.aussage}\n  Quelle: ${b.quelle} | Fundstelle: ${b.fundstelle}`).join('\n')}

P1 Rechenweg: ${a.p1_rechenweg}
P1 Wert: ${a.p1} %
P2 Rechenweg: ${a.p2_rechenweg}
P2 Wert: ${a.p2} % von P1, bindendes Hemmnis: ${a.p2_hemmnis}
P3 Rechenweg: ${a.p3_rechenweg}
P3 Wert: ${a.p3} % der VZAE = ${a.p3_absolut_vzae} VZAE absolut
P3_NULL Rechenweg: ${a.p3_null_rechenweg}
P3_NULL Wert: ${a.p3_null} %
P4: KI ${a.p4_ki} / Demografie ${a.p4_demografie} / Strukturreform ${a.p4_strukturreform}
P5: Leistungserbringer ${a.p5_leistungserbringer} / Preis-Beitrag ${a.p5_preis_beitrag} / Abfluss Ausland ${a.p5_abfluss_ausland} / neue Leistung ${a.p5_neue_leistung}`
}

const pruef = await pipeline(
  vorgelegt,
  (v) => agent(`Du bist Pruefinstanz. Du pruefst den Kartensatz einer Rolle - nicht wohlwollend, sondern genau. Du hast kein eigenes Urteil zur Sache.

Pruefe vier Dinge:
1. EXISTENZ: Gibt es die angegebene Quelle? Rufe sie ab.
2. DECKUNG: Traegt die Quelle die Aussage, die mit ihr belegt wird? Eine existierende Quelle, die etwas anderes sagt, ist eine Beanstandung.
3. MANDATSTREUE: Spricht die Rolle nur ueber ihr eigenes Feld? Aussagen ueber fremde Felder sind zu beanstanden.
4. RECHENWEGHALTBARKEIT: Reproduziert jeder Rechenweg den genannten Wert aus der genannten Bezugsgroesse? Rechne nach. Ein Prozentwert, der nicht zur absoluten VZAE-Zahl passt, ist eine Beanstandung. Pruefe auch die Gegenprobe: (P3 - P3_NULL) / P3 muss zum P4-Wert fuer KI passen, Toleranz 15 Punkte. Pruefe, ob P4 und P5 jeweils auf 100 summieren.

Melde JEDE Beanstandung einzeln mit ihrem Ort. Melde nichts, was in Ordnung ist. Wenn alles in Ordnung ist, gib eine leere Liste zurueck.

${kartentext(v.r, v.a)}`, {
    label: `Pruefung ${v.r.id}`, phase: 'Validierung', schema: S_VAL, model: 'sonnet',
  }).then(p => ({ id: v.r.id, ...p })),
)

const pruefungen = pruef.filter(Boolean)
const gefunden = gesetzt.filter(g => {
  const p = pruefungen.find(x => x.id === g.rolle)
  return p && p.beanstandungen.some(b => b.wo === g.wo)
})
const pruefschaerfe = gesetzt.length ? gefunden.length / gesetzt.length : null
const falschpositive = pruefungen.reduce((n, p) => n + p.beanstandungen.filter(b => !gesetzt.some(g => g.rolle === p.id && g.wo === b.wo)).length, 0)
log(`Pruefschaerfe: ${gefunden.length} von ${gesetzt.length} gesetzten Fehlern gefunden (${Math.round((pruefschaerfe || 0) * 100)} %), dazu ${falschpositive} weitere Beanstandungen`)

// ------------------------------------------------------------- Streitauswahl

function quantil(xs, q) {
  const s = [...xs].sort((a, b) => a - b)
  const i = (s.length - 1) * q, lo = Math.floor(i), hi = Math.ceil(i)
  return lo === hi ? s[lo] : s[lo] + (s[hi] - s[lo]) * (i - lo)
}
function streu(xs) { return { med: quantil(xs, 0.5), iqr: quantil(xs, 0.75) - quantil(xs, 0.25) } }

const w = haupt.map(x => x.antwort)
const S = { p1: streu(w.map(a => a.p1)), p2: streu(w.map(a => a.p2)), p3: streu(w.map(a => a.p3)) }
const FLOOR = { p1: 5, p2: 5, p3: 3 }
const medV = (keys) => keys.map(k => quantil(w.map(a => a[k]), 0.5))
const M4 = medV(['p4_ki', 'p4_demografie', 'p4_strukturreform'])
const M5 = medV(['p5_leistungserbringer', 'p5_preis_beitrag', 'p5_abfluss_ausland', 'p5_neue_leistung'])

const index = haupt.map(x => {
  const a = x.antwort
  let s = 0
  for (const k of ['p1', 'p2', 'p3']) s += Math.abs(a[k] - S[k].med) / Math.max(S[k].iqr, FLOOR[k])
  const v4 = [a.p4_ki, a.p4_demografie, a.p4_strukturreform]
  const v5 = [a.p5_leistungserbringer, a.p5_preis_beitrag, a.p5_abfluss_ausland, a.p5_neue_leistung]
  s += (0.5 * v4.reduce((n, v, i) => n + Math.abs(v - M4[i]), 0)) / 8
  s += (0.5 * v5.reduce((n, v, i) => n + Math.abs(v - M5[i]), 0)) / 8
  return { id: x.r.id, streitindex: Math.round(s * 1000) / 1000 }
}).sort((a, b) => b.streitindex - a.streitindex)

const AUSGEWAEHLT = index.slice(0, 5).map(x => x.id)
log(`Streitauswahl (Panelmedian-Form, 10 Rollen erlauben keinen Bankmedian): ${AUSGEWAEHLT.join(', ')}`)

// ------------------------------------------------------ Runde 2 - die Tafel

phase('Runde 2')

const tafel = haupt.map(x => `[K-${x.r.id}-POS] ${x.r.id} (${x.r.rolle}, Feld: ${x.r.bezugsgruppe}, Geruest ${x.r.geruest}):
  POSITION: ${x.antwort.position}
  P1 ${x.antwort.p1} % | P2 ${x.antwort.p2} % | P3 ${x.antwort.p3} % (${x.antwort.p3_absolut_vzae} VZAE) | P4-KI ${x.antwort.p4_ki} % | P5-Abfluss ${x.antwort.p5_abfluss_ausland} %
  bindendes Hemmnis: ${x.antwort.p2_hemmnis}`).join('\n\n')

const REGELN = `DIE DISKUSSIONSREGELN:
1. Gehandelt wird nur durch Karten, nie durch Prosa.
2. ZUSTIMMUNG IST KEIN ZULAESSIGER ZUG. Es gibt keine Karte "stimme zu". Wer nichts entgegenzusetzen hat, legt nichts.
3. Jeder Einwand zeigt auf genau eine fremde Karte.
4. Pflichtzug: mindestens ein Einwand gegen eine Karte aus einem ANDEREN Feld als deinem, und eine Bedingung an deine EIGENE Position - der Satz, unter dem sie nicht mehr gilt.
5. Jeder Einwand traegt eine RETTUNGSBEDINGUNG: was muesste zutreffen, damit die angegriffene Karte trotz deines Einwands gilt? Wer das nicht angeben kann, hat nichts Bestimmtes bestritten.

EINWANDTYPEN, geschlossene Liste: Faktum bestritten | Geltungsbereich zu weit | Mechanismus fehlt | Gegenbeispiel aus meinem Feld | Quelle traegt die Aussage nicht | Groessenordnung falsch | Rechenweg traegt das Ergebnis nicht`

const streitfrage = await agent(`Du bist Gruppenleitung. Du hast KEINE Stimme und kein eigenes Urteil zur Sache. Du clusterst die Karten und findest die Streitfrage - du gibst sie nicht vor.

Hier ist die Tafel nach Runde 1:

${tafel}

Finde die eine Streitfrage, an der sich diese Rollen tatsaechlich reiben - nicht die allgemeinste, sondern die, bei der die Karten einander widersprechen. Benenne die zwei bis drei Kartenpaare, die den Widerspruch tragen.`, { label: 'Streitfrage', phase: 'Runde 2', schema: { type: 'object', properties: { streitfrage: { type: 'string' }, widersprueche: { type: 'array', items: { type: 'string' } } }, required: ['streitfrage', 'widersprueche'] } })

const S_ZUG = {
  type: 'object',
  properties: {
    einwand_bezug: { type: 'string', description: 'Die Karten-ID, gegen die sich der Einwand richtet, z.B. K-D01-POS' },
    einwand_fremdes_feld: { type: 'string' },
    einwandtyp: { type: 'string', enum: ['Faktum bestritten', 'Geltungsbereich zu weit', 'Mechanismus fehlt', 'Gegenbeispiel aus meinem Feld', 'Quelle traegt die Aussage nicht', 'Groessenordnung falsch', 'Rechenweg traegt das Ergebnis nicht'] },
    einwand_text: { type: 'string' },
    rettungsbedingung: { type: 'string' },
    bedingung_auf_eigene_position: { type: 'string' },
  },
  required: ['einwand_bezug', 'einwand_fremdes_feld', 'einwandtyp', 'einwand_text', 'rettungsbedingung', 'bedingung_auf_eigene_position'],
}

const diskutanten = haupt.filter(x => AUSGEWAEHLT.includes(x.r.id))

const zug1 = await pipeline(diskutanten, (x) => agent(`${auftrag(x.r)}

${REGELN}

STREITFRAGE DER GRUPPE: ${streitfrage.streitfrage}

DIE TAFEL:
${tafel}

Lege deinen ersten Kartenzug. Der Einwand MUSS sich gegen eine Karte aus einem anderen Feld als deinem richten.`, { label: `Zug 1 ${x.r.id}`, phase: 'Runde 2', schema: S_ZUG }).then(z => ({ id: x.r.id, ...z })))

const z1 = zug1.filter(Boolean)
const tafel2 = z1.map(z => `[K-${z.id}-E1] ${z.id} gegen ${z.einwand_bezug} (${z.einwandtyp}): ${z.einwand_text}\n  Rettungsbedingung: ${z.rettungsbedingung}`).join('\n\n')

const zug2 = await pipeline(diskutanten, (x) => agent(`${auftrag(x.r)}

${REGELN}

STREITFRAGE DER GRUPPE: ${streitfrage.streitfrage}

DIE TAFEL AUS RUNDE 1:
${tafel}

DIE EINWAENDE DES ERSTEN ZUGES:
${tafel2}

Lege deinen zweiten Kartenzug. Greife jetzt eine der EINWANDSKARTEN an, nicht noch einmal eine Positionskarte - oder eine Positionskarte, die im ersten Zug unangegriffen geblieben ist. Wieder gegen ein fremdes Feld.`, { label: `Zug 2 ${x.r.id}`, phase: 'Runde 2', schema: S_ZUG }).then(z => ({ id: x.r.id, ...z })))

const z2 = zug2.filter(Boolean)

const dissens = await agent(`Du bist Gruppenleitung, ohne Stimme. Protokolliere den Dissens.

STREITFRAGE: ${streitfrage.streitfrage}

ERSTER ZUG:
${tafel2}

ZWEITER ZUG:
${z2.map(z => `[K-${z.id}-E2] ${z.id} gegen ${z.einwand_bezug} (${z.einwandtyp}): ${z.einwand_text}\n  Rettungsbedingung: ${z.rettungsbedingung}`).join('\n\n')}

Benenne je offenem Streitpunkt drei Dinge: die beiden unvereinbaren Karten, welche Felder sich gegenueberstehen, und die ENTSCHEIDUNGSGROESSE - was man messen muesste, um den Streit zu beenden. Die Entscheidungsgroesse ist der eigentliche Ertrag; eine Einigung ist nicht das Ziel.`, {
  label: 'Dissensprotokoll', phase: 'Runde 2',
  schema: { type: 'object', properties: { dissenspunkte: { type: 'array', minItems: 2, items: { type: 'object', properties: { streitpunkt: { type: 'string' }, karte_a: { type: 'string' }, karte_b: { type: 'string' }, felder: { type: 'string' }, entscheidungsgroesse: { type: 'string' } }, required: ['streitpunkt', 'karte_a', 'karte_b', 'felder', 'entscheidungsgroesse'] } } }, required: ['dissenspunkte'] },
})

// ------------------------------------------------- Runde 3 - zweite Erhebung

phase('Runde 3')

const DISSENSTEXT = dissens.dissenspunkte.map((d, i) => `DISSENS ${i + 1}: ${d.streitpunkt}\n  ${d.karte_a} gegen ${d.karte_b} (${d.felder})\n  Entscheidungsgroesse: ${d.entscheidungsgroesse}`).join('\n\n')
const ALLE_EINWAENDE = [...z1, ...z2]

const S_R3 = {
  type: 'object',
  properties: {
    p1: { type: 'number' }, p2: { type: 'number' }, p3: { type: 'number' }, p3_absolut_vzae: { type: 'number' }, p3_null: { type: 'number' },
    p4_ki: { type: 'number' }, p4_demografie: { type: 'number' }, p4_strukturreform: { type: 'number' },
    p5_leistungserbringer: { type: 'number' }, p5_preis_beitrag: { type: 'number' }, p5_abfluss_ausland: { type: 'number' }, p5_neue_leistung: { type: 'number' },
    aenderung_begruendung: { type: 'string', description: 'Warum du geaendert hast - oder warum du trotz der Einwaende NICHT geaendert hast' },
    antwort_auf_einwaende: { type: 'string' },
    stellungnahme_dissens: { type: 'string' },
  },
  required: ['p1', 'p2', 'p3', 'p3_absolut_vzae', 'p3_null', 'p4_ki', 'p4_demografie', 'p4_strukturreform', 'p5_leistungserbringer', 'p5_preis_beitrag', 'p5_abfluss_ausland', 'p5_neue_leistung', 'aenderung_begruendung', 'antwort_auf_einwaende', 'stellungnahme_dissens'],
}

function promptR3(r, a) {
  const gegen = ALLE_EINWAENDE.filter(e => e.einwand_bezug.includes(r.id))
  return `${auftrag(r)}

DEINE WERTE AUS RUNDE 1: P1 ${a.p1} | P2 ${a.p2} | P3 ${a.p3} % = ${a.p3_absolut_vzae} VZAE | P3_NULL ${a.p3_null} | P4 ${a.p4_ki}/${a.p4_demografie}/${a.p4_strukturreform} | P5 ${a.p5_leistungserbringer}/${a.p5_preis_beitrag}/${a.p5_abfluss_ausland}/${a.p5_neue_leistung}

DIE STREITFRAGE WAR: ${streitfrage.streitfrage}

${DISSENSTEXT}

EINWAENDE GEGEN DEINE KARTEN:
${gegen.length ? gegen.map(e => `- ${e.id} (${e.einwandtyp}): ${e.einwand_text}\n  Rettungsbedingung: ${e.rettungsbedingung}`).join('\n') : 'keine'}

Nenne jetzt dieselben sechs Pflichtgroessen ein zweites Mal. Aendern ist erlaubt und Nichtaendern auch - aber beides musst du begruenden. Rechne weiter gegen dasselbe Szenariogeruest wie in Runde 1. Antworte auf die Einwaende gegen deine Karten und nimm zu mindestens einem Dissenspunkt aus deiner Feldsicht Stellung.`
}

const ITEMS3 = haupt.map(x => ({ r: x.r, a: x.antwort, kontroll: false }))
  .concat(kontrollR1.map(x => ({ r: x.r, a: x.antwort, kontroll: true })))

const roh3 = await pipeline(ITEMS3, (item) => agent(promptR3(item.r, item.a), {
  label: item.kontroll ? `R3 ${item.r.id} (Kontrollarm)` : `R3 ${item.r.id}`,
  phase: 'Runde 3', schema: S_R3, model: item.kontroll ? 'sonnet' : undefined,
}).then(a3 => ({ ...item, antwort3: a3 })))

const h3 = roh3.filter(Boolean).filter(x => !x.kontroll)
const k3 = roh3.filter(Boolean).filter(x => x.kontroll)

// ---------------------------------------------------- Runde 4 - Optionenrunde

phase('Runde 4')

const hebel = await agent(`Du bist Syntheseinstanz. Leite aus der Tafel DREI Hebel ab - Handlungsoptionen, die auf den Dissenspunkten und Positionen beruhen. Erfinde sie nicht; jeder Hebel muss sich auf konkrete Karten stuetzen.

Jeder Hebel braucht: Adressat (Bund, Land, Selbstverwaltung, EU oder Traeger), Instrument (Gesetz, Richtlinie, Verguetungsregel, Investition oder Tarifvertrag) und die Karten, auf denen er beruht.

STREITFRAGE: ${streitfrage.streitfrage}

${DISSENSTEXT}

TAFEL:
${tafel}`, {
  label: 'Hebelsatz', phase: 'Runde 4',
  schema: { type: 'object', properties: { hebel: { type: 'array', minItems: 3, maxItems: 3, items: { type: 'object', properties: { nr: { type: 'number' }, titel: { type: 'string' }, beschreibung: { type: 'string' }, adressat: { type: 'string' }, instrument: { type: 'string' }, beruht_auf: { type: 'string' } }, required: ['nr', 'titel', 'beschreibung', 'adressat', 'instrument', 'beruht_auf'] } } }, required: ['hebel'] },
})

const HEBELTEXT = hebel.hebel.map(h => `HEBEL ${h.nr}: ${h.titel}\n  ${h.beschreibung}\n  Adressat: ${h.adressat} | Instrument: ${h.instrument}`).join('\n\n')

const S_OPT = {
  type: 'object',
  properties: {
    bewertungen: {
      type: 'array', minItems: 3, maxItems: 3,
      items: {
        type: 'object',
        properties: {
          hebel_nr: { type: 'number' },
          urteil: { type: 'string', enum: ['wirkt', 'wirkt nicht', 'schadet'] },
          mechanismus: { type: 'string' },
          nebenwirkung: { type: 'string' },
          kippbedingung: { type: 'string', description: 'der Umstand, unter dem sich dein Urteil umkehrt' },
        },
        required: ['hebel_nr', 'urteil', 'mechanismus', 'nebenwirkung', 'kippbedingung'],
      },
    },
  },
  required: ['bewertungen'],
}

const opt = await pipeline(haupt, (x) => agent(`${auftrag(x.r)}

Bewerte jeden der drei Hebel FUER DEIN EIGENES FELD. Nicht allgemein, nicht fuer das System - fuer die Menschen und Prozesse, fuer die du sprichst.

Fuer jeden Hebel: wirkt / wirkt nicht / schadet, dazu der Mechanismus, die Nebenwirkung und die Kippbedingung. "Wirkt" ohne benennbaren Mechanismus in deinem Feld ist keine Bewertung.

${HEBELTEXT}`, { label: `Optionen ${x.r.id}`, phase: 'Runde 4', schema: S_OPT }).then(o => ({ id: x.r.id, ...o })))

// ------------------------------------------------------------- Rueckgabe

return {
  rollen: ROLLEN,
  kontrollarm: KONTROLLARM,
  runde1: haupt.map(x => ({ id: x.r.id, geruest: x.r.geruest, ...x.antwort })),
  runde1_kontrollarm: kontrollR1.map(x => ({ id: x.r.id, geruest: x.r.geruest, ...x.antwort })),
  gesetzte_fehler: gesetzt,
  pruefungen,
  pruefschaerfe: { gesetzt: gesetzt.length, gefunden: gefunden.length, quote: pruefschaerfe, nicht_gefunden: gesetzt.filter(g => !gefunden.includes(g)), weitere_beanstandungen: falschpositive },
  streitindex: index,
  ausgewaehlt: AUSGEWAEHLT,
  streitfrage,
  zug1: z1,
  zug2: z2,
  dissens: dissens.dissenspunkte,
  runde3: h3.map(x => ({ id: x.r.id, geruest: x.r.geruest, ...x.antwort3 })),
  runde3_kontrollarm: k3.map(x => ({ id: x.r.id, ...x.antwort3 })),
  hebel: hebel.hebel,
  optionen: opt.filter(Boolean),
}