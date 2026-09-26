# -*- coding: utf-8 -*-
"""Diagrammbausteine fuer das Strategiepapier "Die Haftungswende".

Alle Diagramme sind Inline-SVG, maszstabsgetreu aus den Werten berechnet.
Farben kommen ausschliesslich ueber CSS-Klassen aus den Theme-Tokens, damit
Hell- und Dunkeldarstellung stimmen.
"""
from html import escape

W = 900  # Breite der viewBox

MINUS = "−"


def de(x, d=0, vz=False):
    """Deutsche Zahl: Komma als Dezimaltrenner, Punkt als Tausender, echtes Minus."""
    s = f"{abs(x):,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if x < 0:
        return MINUS + s
    if vz and x > 0:
        return "+" + s
    return s


def _t(x, y, text, cls="t-ink", size=13, anchor="start", weight=400, extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" font-size="{size}" '
            f'text-anchor="{anchor}" font-weight="{weight}"{extra}>{escape(str(text))}</text>')


def svg(h, body, label):
    return (f'<div class="chart"><svg viewBox="0 0 {W} {h}" role="img" aria-label="{escape(label)}" '
            f'preserveAspectRatio="xMinYMin meet">{body}</svg></div>')


def hbalken(zeilen, vmax, einheit="%", label="", links=270, hervor=None, ref=None, d=0):
    """Horizontale Balken. zeilen: [(name, wert, unterzeile)]; hervor: Menge hervorgehobener Namen."""
    hervor = hervor or set()
    rechts = W - 70
    breite = rechts - links
    zh = 44
    top = 18
    h = top + zh * len(zeilen) + 34
    b = []
    # Gitter
    for i in range(0, 5):
        v = vmax * i / 4
        x = links + breite * i / 4
        b.append(f'<line x1="{x:.1f}" y1="{top-6}" x2="{x:.1f}" y2="{top + zh*len(zeilen)}" class="s-rule" stroke-width="1"/>')
        b.append(_t(x, top + zh * len(zeilen) + 20, de(v, d) + einheit, "t-muted", 11, "middle"))
    if ref is not None:
        x = links + breite * ref[0] / vmax
        b.append(f'<line x1="{x:.1f}" y1="{top-10}" x2="{x:.1f}" y2="{top + zh*len(zeilen)}" class="s-ink" stroke-width="1.2" stroke-dasharray="4 3"/>')
        b.append(_t(x + 5, top - 1, ref[1], "t-muted", 11))
    for i, (name, wert, unter) in enumerate(zeilen):
        y = top + i * zh
        cls = "f-accent" if name in hervor else "f-accent2"
        w = max(2.0, breite * wert / vmax)
        b.append(_t(links - 14, y + 17, name, "t-ink", 13.5, "end", 600 if name in hervor else 500))
        if unter:
            b.append(_t(links - 14, y + 33, unter, "t-muted", 11, "end"))
        b.append(f'<rect x="{links}" y="{y+6}" width="{w:.1f}" height="22" class="{cls}" rx="2"/>')
        stellen = d if float(wert).is_integer() else max(d, 1)
        b.append(_t(links + w + 8, y + 22, de(wert, stellen) + einheit, "t-ink", 13, "start", 700))
    return svg(h, "".join(b), label)


def punkte_intervall(zeilen, xmin, xmax, label="", links=250, fett=None):
    """Punkt mit 80-%-Intervall. zeilen: [(name, wert|None, lo, hi, notiz)]."""
    fett = fett or set()
    spalte = W - 150          # Beginn der Beschriftungsspalte rechts neben der Achse
    rechts = spalte - 24
    breite = rechts - links
    zh = 40
    top = 30
    h = top + zh * len(zeilen) + 36
    sx = lambda v: links + breite * (v - xmin) / (xmax - xmin)
    b = []
    for v in range(int(xmin), int(xmax) + 1, 20):
        x = sx(v)
        cls = "s-ink" if v == 0 else "s-rule"
        b.append(f'<line x1="{x:.1f}" y1="{top-12}" x2="{x:.1f}" y2="{top + zh*len(zeilen)-8}" class="{cls}" stroke-width="{1.3 if v==0 else 1}"/>')
        b.append(_t(x, top + zh * len(zeilen) + 12, de(v, 0, vz=True) + " %", "t-muted", 11, "middle"))
    b.append(_t(links, top - 18, "Umsatz 2031 gegenüber 2025, Punktwert und 80-%-Intervall", "t-muted", 11))
    for i, (name, wert, lo, hi, notiz) in enumerate(zeilen):
        y = top + i * zh + 10
        w8 = 700 if name in fett else 500
        b.append(_t(links - 14, y + 5, name, "t-ink", 13.5, "end", w8))
        if wert is None:
            b.append(_t(sx(0) + 10, y + 5, notiz, "t-muted", 12, "start", 400, ' font-style="italic"'))
            continue
        cls = "f-gain" if wert > 0 else ("f-loss" if wert < 0 else "f-muted")
        scls = "s-gain" if wert > 0 else ("s-loss" if wert < 0 else "s-muted")
        b.append(f'<line x1="{sx(lo):.1f}" y1="{y}" x2="{sx(hi):.1f}" y2="{y}" class="{scls}" stroke-width="3" stroke-linecap="round" opacity="0.45"/>')
        r = 8 if name in fett else 6.5
        b.append(f'<circle cx="{sx(wert):.1f}" cy="{y}" r="{r}" class="{cls}"/>')
        b.append(_t(spalte, y + 5, de(wert, 0, vz=True) + " %", "t-ink", 12.5, "start", 700))
        if notiz:
            b.append(_t(spalte + 52, y + 5, notiz, "t-muted", 12, "start", 500))
    return svg(h, "".join(b), label)


def punktwolke(werte, xmin, xmax, median, label="", schritt=5):
    """Einzelurteile als Punkte auf einer Achse, gestapelt bei Kollision."""
    links, rechts = 40, W - 40
    breite = rechts - links
    sx = lambda v: links + breite * (v - xmin) / (xmax - xmin)
    basis = 150
    b = []
    for v in range(int(xmin), int(xmax) + 1, schritt):
        x = sx(v)
        cls = "s-ink" if v == 0 else "s-rule"
        b.append(f'<line x1="{x:.1f}" y1="30" x2="{x:.1f}" y2="{basis+6}" class="{cls}" stroke-width="{1.3 if v==0 else 1}"/>')
        b.append(_t(x, basis + 24, de(v, 0, vz=True) + " %", "t-muted", 11, "middle"))
    belegt = {}
    for name, v in sorted(werte, key=lambda t: t[1]):
        schlitz = round(v / 2.5)
        k = belegt.get(schlitz, 0)
        belegt[schlitz] = k + 1
        y = basis - 12 - k * 20
        cls = "f-gain" if v > 0 else "f-loss"
        b.append(f'<circle cx="{sx(v):.1f}" cy="{y}" r="8" class="{cls}"/>')
    xm = sx(median)
    b.append(f'<line x1="{xm:.1f}" y1="22" x2="{xm:.1f}" y2="{basis+6}" class="s-accent" stroke-width="2"/>')
    b.append(_t(xm + 8, 26, f"Median {de(median,0,vz=True)} %", "t-ink", 12.5, "start", 700))
    neg = sum(1 for _, v in werte if v < 0)
    pos = sum(1 for _, v in werte if v > 0)
    b.append(_t(sx(xmin) + 4, 26, f"{neg} Einschätzungen negativ", "t-muted", 12, "start", 600))
    b.append(_t(sx(xmax) - 4, 26, f"{pos} Einschätzungen positiv", "t-muted", 12, "end", 600))
    return svg(basis + 40, "".join(b), label)


def gestapelt(balken, label=""):
    """Zwei oder mehr 100-%-Balken. balken: [(jahr, [(anteil, name, cls)])]."""
    links, rechts = 110, W - 30
    breite = rechts - links
    zh = 70
    top = 20
    h = top + zh * len(balken) + 10
    b = []
    for i, (jahr, teile) in enumerate(balken):
        y = top + i * zh
        b.append(_t(links - 16, y + 30, jahr, "t-ink", 15, "end", 700))
        x = links
        for anteil, name, cls in teile:
            w = breite * anteil / 100
            b.append(f'<rect x="{x:.1f}" y="{y+6}" width="{w:.1f}" height="40" class="{cls}"/>')
            tcls = "t-inv" if cls in ("f-accent", "f-loss", "f-gain") else "t-ink"
            b.append(_t(x + 12, y + 31, f"{de(anteil)} %  {name}", tcls, 13.5, "start", 700))
            x += w
    return svg(h, "".join(b), label)


def waermefeld(zeilen, spalten, werte, label="", vmax=45):
    """Tabelle mit Flaechenschattierung nach Wert. werte[zeile][spalte]."""
    links = 250
    sb = (W - links - 20) / len(spalten)
    zh = 42
    top = 40
    h = top + zh * len(zeilen) + 10
    b = []
    for j, s in enumerate(spalten):
        b.append(_t(links + sb * j + sb / 2, top - 14, s, "t-muted", 12, "middle", 600))
    for i, z in enumerate(zeilen):
        y = top + i * zh
        b.append(_t(links - 14, y + 26, z, "t-ink", 13.5, "end", 500))
        for j, v in enumerate(werte[i]):
            x = links + sb * j
            op = 0.12 + 0.80 * min(1, v / vmax)
            b.append(f'<rect x="{x+3:.1f}" y="{y+3}" width="{sb-6:.1f}" height="{zh-6}" class="f-accent" opacity="{op:.2f}" rx="2"/>')
            tcls = "t-inv" if op > 0.55 else "t-ink"
            b.append(_t(x + sb / 2, y + 27, f"{de(v)} %", tcls, 14, "middle", 700))
    return svg(h, "".join(b), label)


def zeitstrahl(ereignisse, start, ende, label="", achse=170):
    """Ereignisse auf einer Zeitachse, Lage je Ereignis fest vorgegeben.

    ereignisse: [(jahr_dezimal, datum, text, art, ebene, anker)]; art 'intern' steht oben
    (Akzent), sonst unten; ebene 0 liegt an der Achse; anker 'start' oder 'end'.
    Die Lage ist von Hand gesetzt, weil jede automatische Stapelung bei eng
    liegenden Terminen Beschriftungen kreuzt.
    """
    links, rechts = 40, W - 40
    breite = rechts - links
    sx = lambda t: links + breite * (t - start) / (ende - start)
    b = [f'<line x1="{links}" y1="{achse}" x2="{rechts}" y2="{achse}" class="s-ink" stroke-width="1.5"/>']
    for j in range(int(start), int(ende) + 1):
        x = sx(j)
        b.append(f'<line x1="{x:.1f}" y1="{achse-5}" x2="{x:.1f}" y2="{achse+5}" class="s-ink" stroke-width="1.5"/>')
        b.append(_t(x, achse + 22, str(j), "t-muted", 12, "middle", 600))
    unten_max = 0
    for t, datum, text, art, ebene, anker in ereignisse:
        x = sx(t)
        oben = art == "intern"
        cls, scls = ("f-accent", "s-accent") if oben else ("f-muted", "s-muted")
        dx = 6 if anker == "start" else -6
        if oben:
            ty = achse - 22 - ebene * 34
            ende_linie = ty - 26
        else:
            ty = achse + 50 + ebene * 34
            ende_linie = ty + 2
            unten_max = max(unten_max, ebene + 1)
        b.append(f'<line x1="{x:.1f}" y1="{achse}" x2="{x:.1f}" y2="{ende_linie:.1f}" class="{scls}" stroke-width="1"/>')
        b.append(f'<circle cx="{x:.1f}" cy="{achse}" r="5.5" class="{cls}"/>')
        b.append(_t(x + dx, ty - 14, datum, "t-ink", 12.5, anker, 700))
        b.append(_t(x + dx, ty, text, "t-muted", 12, anker))
    return svg(achse + 40 + unten_max * 34, "".join(b), label)


def kette(glieder, label=""):
    """Wirkungskette: Kaesten mit Pfeilen. glieder: [(titel, wert, einheit)]."""
    n = len(glieder)
    luecke = 22
    kb = (W - 20 - luecke * (n - 1)) / n
    h = 150
    b = []
    for i, (titel, wert, einheit) in enumerate(glieder):
        x = 10 + i * (kb + luecke)
        letzte = i == n - 1
        cls = "f-accent" if letzte else "f-soft"
        tc = "t-inv" if letzte else "t-ink"
        mc = "t-inv" if letzte else "t-muted"
        b.append(f'<rect x="{x:.1f}" y="14" width="{kb:.1f}" height="120" class="{cls}" rx="4"/>')
        b.append(_t(x + 12, 38, titel, mc, 11.5, "start", 700, ' letter-spacing="0.4"'))
        b.append(_t(x + 12, 78, wert, tc, 18 if len(wert) > 10 else 20, "start", 700))
        for k, zeile in enumerate(einheit.split("|")):
            b.append(_t(x + 12, 102 + k * 15, zeile, mc, 11.5))
        if not letzte:
            ax = x + kb + 3
            b.append(f'<path d="M{ax:.1f},74 l{luecke-8:.1f},0 m-6,-6 l6,6 l-6,6" class="s-ink" stroke-width="1.6" fill="none"/>')
    return svg(h, "".join(b), label)


def gruppen(gruppen_, reihen, vmin, vmax, label="", einheit="%"):
    """Gruppierte senkrechte Balken mit Nulllinie. gruppen_: [(name, [wert je reihe])]; reihen: [(name, cls)]."""
    links, rechts = 60, W - 20
    top, unten = 36, 250
    sy = lambda v: top + (unten - top) * (vmax - v) / (vmax - vmin)
    b = []
    schritt = 20 if (vmax - vmin) > 50 else 10
    v = vmin
    while v <= vmax + 0.001:
        y = sy(v)
        cls = "s-ink" if abs(v) < 1e-9 else "s-rule"
        b.append(f'<line x1="{links}" y1="{y:.1f}" x2="{rechts}" y2="{y:.1f}" class="{cls}" stroke-width="{1.3 if abs(v)<1e-9 else 1}"/>')
        b.append(_t(links - 8, y + 4, de(v, 0, vz=True) + einheit, "t-muted", 11, "end"))
        v += schritt
    gb = (rechts - links) / len(gruppen_)
    bb = min(62, (gb - 40) / len(reihen))
    for g, (name, werte) in enumerate(gruppen_):
        gx = links + g * gb + (gb - bb * len(reihen)) / 2
        for r, (w, (rn, cls)) in enumerate(zip(werte, reihen)):
            x = gx + r * bb
            y0, y1 = sy(0), sy(w)
            y, hh = (y1, y0 - y1) if w >= 0 else (y0, y1 - y0)
            b.append(f'<rect x="{x+3:.1f}" y="{y:.1f}" width="{bb-6:.1f}" height="{max(1.5,hh):.1f}" class="{cls}" rx="2"/>')
            ty = y1 - 7 if w >= 0 else y1 + 16
            b.append(_t(x + bb / 2, ty, de(w, 0, vz=True) + einheit, "t-ink", 12.5, "middle", 700))
        b.append(_t(links + g * gb + gb / 2, unten + 26, name, "t-ink", 13, "middle", 600))
    lx = links
    for rn, cls in reihen:
        b.append(f'<rect x="{lx}" y="8" width="14" height="14" class="{cls}" rx="2"/>')
        b.append(_t(lx + 20, 20, rn, "t-muted", 12))
        lx += 22 + len(rn) * 7.2
    return svg(unten + 40, "".join(b), label)
