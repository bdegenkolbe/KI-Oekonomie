#!/usr/bin/env python3
"""Erzeugt workflow-kontrollarm.js: die zehn Kontrollrollen noch einmal auf dem
zweiten Modell, diesmal mit REPARIERTER Bezugsgroesse.

Warum. In Sitzung A ist die Modellabhaengigkeit gerissen (3 statt 4 von 6
Groessen unter der Schwelle). Der Bruch haengt an einem einzigen Paar: Rolle
G03 hatte die Bezugsgroesse 0, und das Kontrollmodell wies den undefinierten
Prozentwert nach eigener Konvention als -100 aus. Ohne dieses Paar waeren 5 von
6 Groessen unter der Schwelle. Die Messung war also durch einen behebbaren
Defekt kontaminiert. Erst dieser Lauf entscheidet, ob das Kriterium wirklich
reisst (`17-Sitzung-A.md` Paragraf 3.3).

Gebaut wird durch Textchirurgie am Skript von Sitzung A, damit der Prompt
BYTEGLEICH bleibt bis auf die Bezugsgroesse - sonst misst der Vergleich die
Prompt-Aenderung statt das Modell.

Eingabe:  rohdaten/sitzung-a.json, rohdaten/nacharbeit.json, workflow-sitzung-a.js
Ausgabe:  workflow-kontrollarm.js   (10 Aufrufe)
"""
import json, pathlib, sys

BASIS = pathlib.Path(__file__).resolve().parent
SA = BASIS / 'rohdaten' / 'sitzung-a.json'
NA = BASIS / 'rohdaten' / 'nacharbeit.json'
SKRIPT = BASIS / 'workflow-sitzung-a.js'
ZIEL = BASIS / 'workflow-kontrollarm.js'

# Die Rollen, deren Bezugsgroesse in Sitzung A und nach der Reparatur IDENTISCH ist.
# Nur bei ihnen ist der Prompt byteidentisch, und nur dann misst der Vergleich
# das Modell statt die geaenderte Vorgabe. Der urspruengliche Kontrollarm taugt
# dafuer nicht: acht seiner zehn Rollen haben auch nach der Reparatur keine
# Bezugsgroesse, G03 darunter - der Lauf wuerde denselben Artefakt erzeugen.
ARM = ['A01', 'A02', 'A06', 'A08', 'A09', 'C01', 'C03']

META = '''export const meta = {
  name: 'kontrollarm-nach-reparatur',
  description: 'Die zehn Kontrollrollen noch einmal auf dem zweiten Modell, mit reparierter Bezugsgroesse - entscheidet, ob die Modellabhaengigkeit wirklich reisst',
  phases: [
    { title: 'Kontrollarm', detail: 'Zehn Rollen, zweites Modell, reparierte Bezugsgroesse' },
  ],
}
'''

SCHLUSS = '''
const arm = roh.filter(Boolean)
log(`Kontrollarm: ${arm.length} von ${ITEMS.length} Rollen, ${ITEMS.length - arm.length} Ausfaelle`)
return { kontrollarm: arm.map(x => ({ id: x.r.id, bank: x.r.bank, geruest: x.r.geruest, anker: x.r.anker_reihenfolge, ...x.antwort })) }
'''


def main():
    for p in (SA, NA, SKRIPT):
        if not p.exists():
            sys.exit(f'fehlt: {p}')
    sa = json.loads(SA.read_text(encoding='utf-8'))
    na = json.loads(NA.read_text(encoding='utf-8'))
    quelle = SKRIPT.read_text(encoding='utf-8').splitlines(keepends=True)

    # Kopf bis einschliesslich ANKER/EUROPA/BLAETTER, also alles vor phase('Recherche')
    i_rech = next(i for i, z in enumerate(quelle) if z.startswith("phase('Recherche')"))
    i_r1 = next(i for i, z in enumerate(quelle) if z.startswith("phase('Runde 1')"))
    i_items = next(i for i, z in enumerate(quelle) if z.startswith('const ITEMS ='))
    i_haupt = next(i for i, z in enumerate(quelle) if z.startswith('const haupt ='))

    kopf = ''.join(quelle[1:i_rech])           # ohne die erste meta-Zeile; meta kommt aus META
    kopf = kopf[kopf.index('const ROLLEN'):]   # RECH und der alte meta-Rumpf entfallen
    runde1 = ''.join(quelle[i_r1 + 1:i_items])  # Schemata, promptR1, Konstanten
    pipeline = ''.join(quelle[i_items + 2:i_haupt])  # der agent-Aufruf, ohne die alte ITEMS-Zeile

    # Alles, was sonst aus Runde 0 kaeme, wird hier eingesetzt statt recherchiert
    zerl = {f['id']: f for f in na['abbildung']['felder']}
    inline = (
        'phase(\'Kontrollarm\')\n\n'
        '/* Eingesetzt statt erneut recherchiert: Recherchebank und Szenariogerueste aus\n'
        '   Sitzung A byteidentisch, Bezugsgroessen aus der Nacharbeit. Nur Letztere hat\n'
        '   sich geaendert - alles andere muss gleich bleiben, sonst misst der Vergleich\n'
        '   die Prompt-Aenderung statt das Modell. */\n'
        f'const FB = {json.dumps({f["id"]: f for f in sa["faktenblaetter"]}, ensure_ascii=False)}\n'
        f'const ZERL = {json.dumps(zerl, ensure_ascii=False)}\n'
        f'const geruestA = {json.dumps(sa["geruestA"], ensure_ascii=False)}\n'
        f'const geruestB = {json.dumps(sa["geruestB"], ensure_ascii=False)}\n\n'
    )
    # blatt() und geruesttext() aus dem Original uebernehmen
    q = ''.join(quelle)
    blattfn = q[q.index('function blatt(id) {'):q.index('\n}\n', q.index('function blatt(id) {')) + 3]
    gertfn = q[q.index('function geruesttext(g) {'):q.index('\n}\n', q.index('function geruesttext(g) {')) + 3]
    inline += blattfn + '\n' + gertfn + "\nconst GER = { A: geruesttext(geruestA), B: geruesttext(geruestB) }\n\n"

    items = (f'const ARM = {json.dumps(ARM)}\n'
             'const ITEMS = ROLLEN.filter(r => ARM.includes(r.id)).map(r => ({ r, kontroll: true }))\n'
             'log(`Kontrollarm nach Reparatur: ${ITEMS.length} Rollen, '
             'davon mit Bezugsgroesse ${ITEMS.filter(it => (ZERL[it.r.id] || {}).vzae > 0).length}`)\n\n')

    js = META + '\n' + kopf + '\n' + inline + runde1 + items + pipeline + SCHLUSS
    ZIEL.write_text(js, encoding='utf-8')

    print(f'{ZIEL.name}: {len(ARM)} Aufrufe, {round(len(js)/1024)} KB')
    print('Arm:', ', '.join(f"{i} ({zerl[i]['vzae']:,.0f} VZAE)" for i in ARM))


if __name__ == '__main__':
    main()
