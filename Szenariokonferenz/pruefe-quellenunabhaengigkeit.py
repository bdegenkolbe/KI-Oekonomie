#!/usr/bin/env python3
"""Quellenunabhaengigkeit je Karte — Screening, nicht Urteil.

Weist aus, wie viele Befunde einer Karte auf einer Quelle stehen, die die EIGENE
Interessenvertretung des Feldes ist: Verband, Kammer, Selbstverwaltungskoerperschaft
oder Unternehmen desselben Feldes. Ab der Haelfte der Befunde gilt die Karte als
`interessengestuetzt`.

Die Kennzeichnung ist KEINE Zurueckweisung. Eine Kammer ist oft die einzige Stelle,
die ueber ihr Feld ueberhaupt Zahlen erhebt. Sie macht aus einem Verdacht eine Zahl.

Aufruf:  python3 pruefe-quellenunabhaengigkeit.py [rohdaten/sitzung-a.json]
"""
import json, re, sys, pathlib, statistics as st

BASIS = pathlib.Path(__file__).resolve().parent
QUELLE = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else BASIS / 'rohdaten' / 'sitzung-a.json'
SCHWELLE = 0.5

# Je Bank die Organisationen, die fuer dieses Feld die eigene Interessenvertretung sind.
# Bewusst eng gefasst: Aufsicht und amtliche Statistik gehoeren NICHT hierher,
# auch wenn sie demselben Sektor angehoeren.
EIGEN = {
    'A': r'\bDKG\b|Krankenhausgesellschaft|\bVKD\b|Helios|Asklepios|Sana|Rh[oö]n-Klinikum|Marburger Bund',
    'B': r'\bKBV\b|Kassen[aä]rztliche|\bKZBV\b|ABDA|Haus[aä]rzteverband|Virchow',
    'C': r'\bbpa\b|\bDBfK\b|Diakonie|Caritas|\bAWO\b|Pflegerat|\bDEVAP\b',
    'D': r'GKV-Spitzenverband|\bvdek\b|\bAOK\b|\bTK\b|Barmer|\bPKV\b|Ersatzkassen|\bIKK\b|Knappschaft',
    'E': r'\bBVMed\b|\bvfa\b|\bBPI\b|Spectaris|\bZVEI\b|Bitkom|Pharma Deutschland|\bBAH\b|\bALM\b|PHAGRO',
    'F': r'Marburger Bund|ver\.?di|\bDBfK\b|Hartmannbund|\bvmf\b|Pflegerat|Gewerkschaft',
    'G': r'Selbsthilfe|\bBAGP\b|\bSoVD\b|\bVdK\b|Verbraucherzentrale',
    'L': r'Bitkom|\bbvitg\b|Industrieverband',
}


def main():
    if not QUELLE.exists():
        sys.exit(f'fehlt: {QUELLE}')
    R = json.loads(QUELLE.read_text(encoding='utf-8'))['runde1']
    zeilen = []
    for a in R:
        pat = EIGEN.get(a['bank'])
        n = len(a['befunde'])
        eigen = sum(1 for b in a['befunde']
                    if pat and re.search(pat, f"{b.get('quelle','')} {b.get('fundstelle','')}", re.I))
        zeilen.append({'id': a['id'], 'bank': a['bank'], 'befunde': n, 'eigen': eigen,
                       'anteil': round(eigen / n, 2) if n else 0.0,
                       'interessengestuetzt': bool(n) and eigen / n >= SCHWELLE,
                       'p3': a['p3'], 'p3_null': a['p3_null']})
    (BASIS / 'rohdaten' / 'quellenunabhaengigkeit.json').write_text(
        json.dumps(zeilen, ensure_ascii=False, indent=1), encoding='utf-8')

    flag = [z for z in zeilen if z['interessengestuetzt']]
    rest = [z for z in zeilen if not z['interessengestuetzt']]
    bef, eig = sum(z['befunde'] for z in zeilen), sum(z['eigen'] for z in zeilen)
    print(f'Karten: {len(zeilen)} | interessengestuetzt: {len(flag)} '
          f'({len(flag)/len(zeilen)*100:.0f} %, Schwelle 10 %) -> '
          f'{"ERFUELLT" if len(flag) <= 0.1*len(zeilen) else "GERISSEN"}')
    print(f'Befunde: {bef} | aus eigener Interessenvertretung: {eig} ({eig/bef*100:.1f} %)')
    print(f'mindestens eine solche Quelle: {sum(1 for z in zeilen if z["eigen"])} Karten')
    for z in sorted(flag, key=lambda x: -x['anteil']):
        print(f"  {z['id']} Bank {z['bank']}  {z['eigen']}/{z['befunde']} Befunde  "
              f"P3 {z['p3']:+6.1f}  P3_0 {z['p3_null']:+6.1f}")
    if flag:
        print(f"\nP3-Median gekennzeichnet {st.median([z['p3'] for z in flag]):+.1f} % | "
              f"uebrige {st.median([z['p3'] for z in rest]):+.1f} %")
        print(f"KI-Effekt (P3 - P3_0) gekennzeichnet "
              f"{st.median([z['p3']-z['p3_null'] for z in flag]):+.1f} | "
              f"uebrige {st.median([z['p3']-z['p3_null'] for z in rest]):+.1f}")
        print('\nEine Verschiebung zugunsten des eigenen Feldes liegt nur vor, wenn die '
              'gekennzeichneten Karten MEHR Personalbedarf sehen als die uebrigen.')


if __name__ == '__main__':
    main()
