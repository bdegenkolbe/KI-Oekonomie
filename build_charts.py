#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_charts.py — erzeugt Diagramme aus den Tabellen in Statistik.md.

Liest die Zeitreihen-Tabellen (Layoff-Tracker, Challenger-Monatsreihe,
AI-Capex) und schreibt drei druckfähige PNG-Diagramme nach charts/.
Farbwelt gemäß Formatvorlage.md (Stahlblau #2E75B6), Datenreihen-Palette
validiert (Lightness/Chroma/CVD; zweite Reihe #245A92 mit Sekundär-
codierung über Marker und Strichelung).

Aufruf: python3 build_charts.py
"""

import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).parent
STATISTIK = ROOT / "Statistik.md"
CHARTS = ROOT / "charts"

# Validierte Datenfarben (siehe Validierungsprotokoll v28.0)
BLAU = "#2E75B6"      # Stahlblau (Formatvorlage Accent)
BLAU_DUNKEL = "#245A92"
NEUTRAL = "#C7CDD4"   # neutrales Grau für Nicht-KI-Segmente
INK = "#333333"
INK_MUTED = "#666666"
GRID = "#E6E9EC"

MONATE = {"Jan": 1, "Feb": 2, "Mär": 3, "Apr": 4, "Mai": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Okt": 10, "Nov": 11, "Dez": 12}


def zahl(cell: str):
    """Erste Zahl einer Tabellenzelle als int (deutsche Tausenderpunkte)."""
    m = re.search(r"(\d{1,3}(?:\.\d{3})+|\d+)", cell)
    return int(m.group(1).replace(".", "")) if m else None


def tabelle(text: str, ab: str) -> list[list[str]]:
    """Datenzeilen der ersten Markdown-Tabelle nach der Überschrift `ab`."""
    sec = text[text.index(ab):]
    rows = []
    for line in sec.split("\n"):
        if line.startswith("|"):
            rows.append([c.strip() for c in line.strip("|").split("|")])
        elif rows:
            break
    return rows[2:]  # Kopf + Trennzeile überspringen


def datum(cell: str):
    """'05. Jul 2026' → (2026, 7, 5); None bei unscharfen Angaben."""
    m = re.search(r"(\d{1,2})\.\s*(\w{3})\w*\s*(\d{4})", cell)
    if not m or m.group(2)[:3] not in MONATE:
        return None
    return (int(m.group(3)), MONATE[m.group(2)[:3]], int(m.group(1)))


def fmt_tsd(x, _pos=None):
    return f"{int(x):,}".replace(",", ".")


def style(ax):
    ax.set_facecolor("white")
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(GRID)
    ax.tick_params(colors=INK_MUTED, labelsize=9)
    ax.yaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def quelle(fig, text):
    fig.text(0.01, 0.01, text, fontsize=7.5, color=INK_MUTED)


def chart_tracker(text: str) -> None:
    """Diagramm 1: kumulierte Tracker-Stände 2026 als Zeitreihe."""
    reihen = {"TrueUp": [], "SkillSyncer": []}
    ref_2025 = None
    for row in tabelle(text, "## 1."):
        if len(row) < 5:
            continue
        if "2025" in row[0] and "Gesamtjahr" in row[0]:
            ref_2025 = zahl(row[1])
            continue
        d = datum(row[0])
        if d is None:
            continue
        tu, ss = zahl(row[1]), zahl(row[4])
        # nur belastbare kumulative Stände (keine ">"-Schätzungen)
        if tu and ">" not in row[1]:
            reihen["TrueUp"].append((d, tu))
        if ss and ">" not in row[4]:
            reihen["SkillSyncer"].append((d, ss))

    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)
    fig.patch.set_facecolor("white")
    style(ax)

    import datetime as dt
    stil = {"TrueUp": (BLAU, "o", "-"), "SkillSyncer": (BLAU_DUNKEL, "s", "--")}
    for name, punkte in reihen.items():
        punkte.sort()
        xs = [dt.date(*d) for d, _ in punkte]
        ys = [v for _, v in punkte]
        farbe, marker, ls = stil[name]
        ax.plot(xs, ys, ls, marker=marker, color=farbe, linewidth=2,
                markersize=7, markeredgecolor="white", markeredgewidth=1)
        ax.annotate(f"{name}  {fmt_tsd(ys[-1])}", (xs[-1], ys[-1]),
                    xytext=(8, 0), textcoords="offset points",
                    va="center", fontsize=9, color=INK, fontweight="bold")
    if ref_2025:
        ax.axhline(ref_2025, color=INK_MUTED, linewidth=1, linestyle=":")
        ax.annotate(f"Gesamtjahr 2025 (TrueUp): {fmt_tsd(ref_2025)}",
                    (0.02, ref_2025), xycoords=("axes fraction", "data"),
                    xytext=(0, 5), textcoords="offset points",
                    fontsize=8, color=INK_MUTED)

    ax.set_title("Tech-Layoffs 2026 — kumulierte Tracker-Stände",
                 fontsize=12, color=INK, fontweight="bold", loc="left", pad=14)
    ax.yaxis.set_major_formatter(FuncFormatter(fmt_tsd))
    ax.set_ylim(bottom=0)
    ax.set_xlim(right=ax.get_xlim()[1] + 28)  # Platz für Direktbeschriftung
    import matplotlib.dates as mdates
    de_mon = {1: "Jan.", 2: "Feb.", 3: "März", 4: "Apr.", 5: "Mai", 6: "Juni",
              7: "Juli", 8: "Aug.", 9: "Sep.", 10: "Okt.", 11: "Nov.", 12: "Dez."}
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(
        lambda x, _p: (lambda d: f"{d.day}. {de_mon[d.month]} {d.year}")(mdates.num2date(x))))
    ax.legend(handles=[plt.Line2D([], [], color=BLAU, marker="o", ls="-",
                                  markeredgecolor="white", label="TrueUp"),
                       plt.Line2D([], [], color=BLAU_DUNKEL, marker="s", ls="--",
                                  markeredgecolor="white", label="SkillSyncer")],
              frameon=False, fontsize=9, loc="upper left", labelcolor=INK)
    quelle(fig, "Quellen: TrueUp, SkillSyncer (via Statistik.md Tabelle 1). Methodikunterschiede — Niveaus nicht direkt vergleichbar.")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(CHARTS / "layoff-tracker-2026.png")
    plt.close(fig)


def chart_challenger(text: str) -> None:
    """Diagramm 2: Challenger-Monatswerte, KI-Segment gestapelt."""
    monate, ki, rest, anteil = [], [], [], []
    for row in tabelle(text, "## 2."):
        if len(row) < 4:
            continue
        gesamt, ki_wert = zahl(row[1]), zahl(row[2])
        if gesamt is None or ki_wert is None:
            continue
        monate.append(row[0].split()[0])
        ki.append(ki_wert)
        rest.append(gesamt - ki_wert)
        m = re.search(r"(\d+)\s*%", row[3])
        anteil.append(m.group(1) if m else "")

    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)
    fig.patch.set_facecolor("white")
    style(ax)

    ax.bar(monate, ki, color=BLAU, width=0.6, edgecolor="white", linewidth=2,
           label="KI-begründet")
    ax.bar(monate, rest, bottom=ki, color=NEUTRAL, width=0.6,
           edgecolor="white", linewidth=2, label="übrige Gründe")
    for i, (k, r, a) in enumerate(zip(ki, rest, anteil)):
        ax.annotate(f"KI-Anteil {a} %", (i, k + r), xytext=(0, 6),
                    textcoords="offset points", ha="center",
                    fontsize=9, color=INK, fontweight="bold")
        ax.annotate(fmt_tsd(k), (i, k / 2), ha="center", va="center",
                    fontsize=8.5, color="white", fontweight="bold")

    ax.set_title("US-Stellenstreichungen 2026 nach Monat — KI als Einzelgrund",
                 fontsize=12, color=INK, fontweight="bold", loc="left", pad=14)
    ax.yaxis.set_major_formatter(FuncFormatter(fmt_tsd))
    ax.set_ylim(0, max(k + r for k, r in zip(ki, rest)) * 1.18)
    ax.legend(frameon=False, fontsize=9, loc="upper right", labelcolor=INK)
    quelle(fig, "Quelle: Challenger, Gray & Christmas Monatsreports (via Statistik.md Tabelle 2).")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(CHARTS / "challenger-ki-anteil-2026.png")
    plt.close(fig)


def chart_capex(text: str) -> None:
    """Diagramm 3: Hyperscaler-AI-Capex 2025 → 2026 → Ausblick 2027."""
    rows = tabelle(text, "## 5.")
    werte = {}
    for row in rows:
        if len(row) < 2:
            continue
        label, wert = row[0], row[1]
        if "Vorjahr 2025" in label:
            werte["2025"] = zahl(wert)
        elif "revidiert" in label:
            werte["2026"] = zahl(wert)
        elif "2027" in label:
            m = re.search(r"(\d+)\s*Bio", wert)
            werte["2027"] = int(m.group(1)) * 1000 if m else None

    jahre = ["2025", "2026", "2027"]
    vals = [werte.get(j) for j in jahre]
    if None in vals:
        raise RuntimeError(f"Capex-Werte unvollständig: {werte}")

    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=200)
    fig.patch.set_facecolor("white")
    style(ax)

    farben = [BLAU, BLAU, "white"]
    for i, (jahr, v) in enumerate(zip(jahre, vals)):
        proj = jahr == "2027"
        ax.bar(jahr, v, color="white" if proj else BLAU, width=0.55,
               edgecolor=BLAU if proj else "white", linewidth=2,
               hatch="//" if proj else None)
        praefix = "> " if proj else "~"
        ax.annotate(f"{praefix}{fmt_tsd(v)}", (i, v), xytext=(0, 6),
                    textcoords="offset points", ha="center",
                    fontsize=10, color=INK, fontweight="bold")
    ax.annotate("Projektion", (2, vals[2] / 2), ha="center", va="center",
                fontsize=8.5, color=BLAU_DUNKEL)

    ax.set_title("AI-Capex der Hyperscaler (Mrd. US-Dollar pro Jahr)",
                 fontsize=12, color=INK, fontweight="bold", loc="left", pad=14)
    ax.yaxis.set_major_formatter(FuncFormatter(fmt_tsd))
    ax.set_ylim(0, max(vals) * 1.18)
    quelle(fig, "Quellen: Financial Times (Aggregat), Wall-Street-Konsens 2027 (via Statistik.md Tabelle 5).")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(CHARTS / "ai-capex-hyperscaler.png")
    plt.close(fig)


def main() -> None:
    CHARTS.mkdir(exist_ok=True)
    text = STATISTIK.read_text(encoding="utf-8")
    chart_tracker(text)
    chart_challenger(text)
    chart_capex(text)
    for p in sorted(CHARTS.glob("*.png")):
        print(f"Diagramm geschrieben: {p}")


if __name__ == "__main__":
    main()
