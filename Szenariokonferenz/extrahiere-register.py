#!/usr/bin/env python3
"""Zwei Register aus dem Ergebnis von Sitzung A — ohne einen einzigen zusaetzlichen Aufruf.

  1. Falsifikatorenregister: die datierten, entscheidbaren Gegenproben des Panels
  2. Durchgriffskanalregister: die Rechtsnormen, die feldübergreifend gedeckt sind

Eingabe:  Szenariokonferenz/rohdaten/sitzung-a.json  (Rueckgabe des Laufs, mit echten Rollen-IDs)
Ausgabe:  Szenariokonferenz/19-Falsifikatoren.md
          Szenariokonferenz/20-Durchgriffskanaele.md
"""
import json, re, sys, collections, pathlib

BASIS = pathlib.Path(__file__).resolve().parent
QUELLE = BASIS / 'rohdaten' / 'sitzung-a.json'

# --- Normerkennung: § <Nummer> [Abs./Satz/Nr. ...] <Gesetz> [roemische Ziffer], dazu EU-Verordnungen
UEBERSPRINGEN = r'(?:(?:Abs|Satz|Nr|Buchst|Halbsatz|Alt|lit)\.?\s*[\w\d]+\.?\s*)*'
NORM = re.compile(
    r'§+\s*(\d+[a-z]?)\s*' + UEBERSPRINGEN +
    r'([A-ZÄÖÜ][A-Za-zÄÖÜäöüß-]{1,14}(?:\s+[IVX]{1,4}\b)?)'
    r'|(?:VO|Verordnung)\s*\(EU\)\s*(?:Nr\.\s*)?(\d{4}/\d+)'
    r'|Art\.\s*(\d+[a-z]?)\s*' + UEBERSPRINGEN + r'(DSGVO|KI-VO|EHDS)'
)
# Woerter, die nach einem Paragrafen stehen koennen, aber kein Gesetz sind
UNGESETZ = {'Die','Der','Das','Ein','Eine','Im','In','Und','Wenn','Damit','Dies','Diese','Dieser',
            'Satz','Absatz','Nummer','Buchstabe','Anlage','Anhang','Ziffer','Halbsatz','Alternative',
            'Abs','Nr','Buchst','Alt','lit','ff','iVm','bis','und','oder','sowie','des','der'}

FELDER = ('falsifikator','a1_norm','e3_regelung','p1_rechenweg','p2_rechenweg','p3_rechenweg',
          'p3_null_rechenweg','a2_begruendung','p4_begruendung','p5_begruendung','position',
          'a3_woran_sichtbar','befunde','geruest_einwand')

def text(a):
    return ' '.join(json.dumps(a.get(k, ''), ensure_ascii=False) if not isinstance(a.get(k), str)
                    else a[k] for k in FELDER)

def normen(a):
    out = set()
    for m in NORM.finditer(text(a)):
        if m.group(3):
            out.add(f'VO (EU) {m.group(3)}')
        elif m.group(4):
            out.add(f'Art. {m.group(4)} {m.group(5)}')
        elif m.group(2) and m.group(2).split()[0] not in UNGESETZ:
            gesetz = re.sub(r'\s+', ' ', m.group(2)).strip()
            out.add('§ ' + m.group(1) + ' ' + gesetz)
    return out

JAHR = re.compile(r'\b(20(?:2[6-9]|3[0-5]))\b')
BIS_JAHR = re.compile(r'bis\s+(?:sp[aä]testens\s+)?(?:zum\s+|Ende\s+|Mitte\s+)?'
                      r'(?:\d{1,2}\.\d{1,2}\.)?\s*(20(?:2[6-9]|3[0-5]))')

def pruefjahr(f):
    """Das Jahr, bis zu dem die Gegenprobe entschieden ist - nicht ein beilaeufig genanntes Bezugsjahr."""
    bis = BIS_JAHR.findall(f)
    if bis:
        return max(bis)
    alle = JAHR.findall(f)
    return max(alle) if alle else None
SCHWELLE = re.compile(r'(?:unter|über|ueber|mehr als|weniger als|mindestens|höchstens|hoechstens|<|>|=)\s*[\d.,]+')

def lade():
    if not QUELLE.exists():
        sys.exit(f'fehlt: {QUELLE}\nErst die Rueckgabe von Sitzung A dorthin schreiben.')
    d = json.loads(QUELLE.read_text(encoding='utf-8'))
    r = d.get('runde1') if isinstance(d, dict) else d
    if not r:
        sys.exit('kein Feld "runde1" in der Eingabe')
    return d, r

def falsifikatoren(runde1):
    zeilen = []
    for a in runde1:
        f = str(a.get('falsifikator', ''))
        zeilen.append({
            'id': a.get('id'), 'bank': a.get('bank'), 'rolle': a.get('rolle', ''),
            'jahr': pruefjahr(f),
            'schwelle': bool(SCHWELLE.search(f)),
            'text': re.sub(r'\s+', ' ', f).strip(),
        })
    return zeilen

def kanaele(runde1):
    rollen, baenke = collections.defaultdict(set), collections.defaultdict(set)
    for a in runde1:
        for n in normen(a):
            rollen[n].add(a.get('id'))
            baenke[n].add(a.get('bank'))
    return rollen, baenke

def main():
    d, runde1 = lade()
    # ---------- Register 1
    z = falsifikatoren(runde1)
    voll = [x for x in z if x['jahr'] and x['schwelle']]
    voll.sort(key=lambda x: (x['jahr'], x['id'] or ''))
    t = ['# Falsifikatorenregister — die Gegenproben des Panels', '',
         '*Jede Rolle musste angeben, woran sie merken würde, dass sie falsch liegt. '
         'Dieses Register führt die Gegenproben, die eine Jahreszahl und eine Zahlenschwelle tragen — '
         'also entscheidbar sind, ohne dass jemand über sie befinden muss.*', '',
         '---', '',
         f'**{len(voll)} von {len(z)} Falsifikatoren sind datiert und beziffert.** '
         'Die übrigen sind als Gegenprobe formuliert, aber ohne Stichtag oder ohne Schwelle; '
         'sie stehen in den Rohdaten, nicht in diesem Register.', '',
         '| Prüfjahr | Feld | Rolle | Gegenprobe |', '|---|---|---|---|']
    for x in voll:
        kurz = x['text'][:400] + ('…' if len(x['text']) > 400 else '')
        kurz = kurz.replace('|', '\\|')
        t.append('| ' + x['jahr'] + ' | ' + str(x['id']) + ' | ' + str(x['rolle']) + ' | ' + kurz + ' |')
    nach = collections.Counter(x['jahr'] for x in voll)
    t += ['', '## Verteilung der Prüfjahre', '', '| Jahr | Gegenproben |', '|---|---|']
    t += [f'| {j} | {n} |' for j, n in sorted(nach.items())]
    t += ['', '## Wie dieses Register zu benutzen ist', '',
          'Es ist kein Anhang, sondern der Prüfplan des Strategiepapiers. Wer im jeweiligen Prüfjahr '
          'die genannte Quelle aufschlägt, kann die zugehörige Aussage des Papiers annehmen oder verwerfen, '
          'ohne das Verfahren zu wiederholen. Ein Papier über 2031, das sich vor 2031 nicht widerlegen lässt, '
          'behauptet nichts.']
    (BASIS / '19-Falsifikatoren.md').write_text('\n'.join(t) + '\n', encoding='utf-8')

    # ---------- Register 2
    rollen, baenke = kanaele(runde1)
    gedeckt = sorted(((len(rollen[n]), len(baenke[n]), n) for n in rollen
                      if len(rollen[n]) >= 3 and len(baenke[n]) >= 2), reverse=True)
    einmal = sum(1 for n in rollen if len(rollen[n]) == 1)
    u = ['# Durchgriffskanäle — die feldübergreifend gedeckten Rechtsnormen', '',
         '*Welche Norm die Ersparnis konkret aufhält. Aufgenommen ist nur, was mindestens drei Rollen '
         'aus mindestens zwei Bänken unabhängig voneinander genannt haben — das Konvergenzmaß des Verfahrens '
         '(`11-Konzept-v2.md` § 6, feldübergreifende Deckung), angewandt auf Normen statt auf Befunde.*', '',
         '---', '',
         f'**{len(rollen)} verschiedene Normen genannt, davon {einmal} von nur einer Rolle. '
         f'{len(gedeckt)} sind feldübergreifend gedeckt.** Die Einzelnennungen sind nicht falsch, aber '
         'ungeprüft: Sie tragen keine unabhängige Bestätigung und gehen deshalb nicht in das Papier ein.', '',
         '| Rollen | Bänke | Norm |', '|---|---|---|']
    u += [f'| {r} | {b} | {n} |' for r, b, n in gedeckt]
    u += ['', '## Vorbehalt', '',
          'Die Norm ist gedeckt, ihre **Auslegung** ist es nicht. Dass eine Norm aus vielen Bänken genannt '
          'wird, heißt, dass sie in vielen Feldern als Engpass wahrgenommen würde — nicht, dass die dort '
          'jeweils gezogene Rechtsfolge zutrifft. Normen, die aus der Recherchebank stammen, teilen deren '
          'Prüfstand (`21-Quellenpruefung.md`); die Zählung unterscheidet sie nicht.', '',
          'Gezählt werden Nennungen, nicht Normen im juristischen Sinn: Eine Norm, die eine Rolle mehrfach '
          'anführt, zählt einmal, und Absatz-, Satz- und Nummernangaben sind auf den Paragrafen verdichtet.']
    (BASIS / '20-Durchgriffskanaele.md').write_text('\n'.join(u) + '\n', encoding='utf-8')

    print(f'19-Falsifikatoren.md      {len(voll)} von {len(z)} datiert und beziffert')
    print(f'20-Durchgriffskanaele.md  {len(gedeckt)} gedeckt von {len(rollen)} genannt, {einmal} Einzelnennungen')

if __name__ == '__main__':
    main()
