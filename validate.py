#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate.py — automatisierte Prüfschritte gemäß Validierung.md § 2.6.

Prüft KI-Ökonomie.md und die Begleitdateien auf strukturelle Konsistenz.
FEHLER (Exit-Code 1) bei harten Verstößen; WARNUNGEN (Exit-Code 0) bei
Auffälligkeiten, die im Validierungsprotokoll zu bewerten sind.

Aufruf: python3 validate.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
HAUPTDOKUMENT = ROOT / "KI-Ökonomie.md"

# Wächter-Schwellen (Zeichen)
MAX_ABSATZ = 5_000        # kein Fließtext-Absatz darf länger werden (Warnung)
MAX_ABSCHNITT_1_1 = 8_000  # § 1.1 hat Zielgröße ~1 Seite (Warnung)

errors: list[str] = []
warnings: list[str] = []


def check(cond: bool, msg: str, level: str = "error") -> None:
    if not cond:
        (errors if level == "error" else warnings).append(msg)


def main() -> int:
    text = HAUPTDOKUMENT.read_text(encoding="utf-8")

    # --- 2.1.2 Kapitelnummerierung -----------------------------------------
    kapitel = [int(n) for n in re.findall(r"^## (\d+)\. ", text, re.M)]
    check(kapitel == list(range(1, 12)),
          f"Kapitelnummerierung nicht lückenlos 1–11: {kapitel}")

    # Unterabschnitte je Kapitel lückenlos aufsteigend
    for kap in range(1, 12):
        subs = [int(m) for m in re.findall(rf"^### {kap}\.(\d+)", text, re.M)]
        if subs:
            check(subs == list(range(1, len(subs) + 1)),
                  f"Unterabschnitte von Kapitel {kap} nicht lückenlos: {subs}")

    # --- 2.1.1 Inhaltsverzeichnis deckt alle Kapitel ------------------------
    toc = re.search(r"## Inhaltsverzeichnis\n(.*?)\n---", text, re.S)
    check(toc is not None, "Inhaltsverzeichnis nicht gefunden")
    if toc:
        toc_nums = [int(n) for n in re.findall(r"^(\d+)\. \[", toc.group(1), re.M)]
        check(sorted(set(toc_nums)) == list(range(1, 12)),
              f"Inhaltsverzeichnis deckt nicht Kapitel 1–11: {sorted(set(toc_nums))}")

    # --- 2.1.3 Querverweise --------------------------------------------------
    headings = set(re.findall(r"^### (\d+\.\d+)", text, re.M))
    for ref in sorted(set(re.findall(r"§\s?(\d+\.\d+)", text))):
        # Literaturverzeichnis-Sektionen 11.x sind ###-Überschriften; alles andere muss existieren
        check(ref in headings,
              f"Querverweis § {ref} zeigt auf keinen existierenden Unterabschnitt")
    for kap_ref in set(int(n) for n in re.findall(r"Kapitel (\d+)", text)):
        check(1 <= kap_ref <= 11, f"Verweis auf nicht existierendes Kapitel {kap_ref}")

    # --- 2.1.2 Zähler ---------------------------------------------------------
    typen = len(re.findall(r"^\*\*Typ \d ", text, re.M))
    check(typen == 5, f"§ 2.1 nennt fünf Typen, gefunden: {typen}")

    # --- 2.5 Versionskonsistenz ----------------------------------------------
    m = re.search(r"^\*\*Version:\*\* (\d+\.0)$", text, re.M)
    check(m is not None, "Versionszeile im Dokumentkopf fehlt")
    version = m.group(1) if m else "?"
    check(f"Version {version}" in text.split("**Hinweis zur Aktualität:**")[-1],
          f"Version {version} fehlt im Aktualitätshinweis am Dokumentende")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    check(f"Version: {version}" in readme, f"README.md-Versionszeile ≠ {version}")
    check(f"Version {version}, " in readme, f"README.md-Zitiervorschlag ≠ {version}")
    claude_md = (ROOT / "Claude.md").read_text(encoding="utf-8")
    check(f"Version {version}," in claude_md, f"Claude.md-Stand-Angabe ≠ {version}")

    # --- Pflichtbestandteile ---------------------------------------------------
    check("**Haftungshinweis:**" in text, "Haftungshinweis am Dokumentende fehlt")
    check("**Lizenz:**" in text, "Lizenzhinweis am Dokumentende fehlt")
    check("Claude (Anthropic)" in readme, "KI-Offenlegung in README.md fehlt")
    check((ROOT / "Statistik.md").exists(), "Statistik.md fehlt")
    check("Statistik.md" in text, "Hauptdokument verweist nicht auf Statistik.md")

    # --- Absatzlängen-Wächter (gegen erneutes Aufblähen) -----------------------
    for para in text.split("\n\n"):
        if len(para) > MAX_ABSATZ and not para.lstrip().startswith(("|", "#")):
            head = re.sub(r"\s+", " ", para[:70])
            warnings.append(
                f"Absatz mit {len(para):,} Zeichen (> {MAX_ABSATZ:,}): {head!r} — "
                f"Fortschreibungsketten gehören nach Statistik.md")
    m = re.search(r"### 1\.1 Ausgangslage\n(.*?)\n### 1\.2", text, re.S)
    if m and len(m.group(1)) > MAX_ABSCHNITT_1_1:
        warnings.append(
            f"§ 1.1 hat {len(m.group(1)):,} Zeichen (Zielgröße ≤ {MAX_ABSCHNITT_1_1:,}) — "
            f"Zahlen-Fortschreibungen nach Statistik.md verlagern")

    # --- Bericht ----------------------------------------------------------------
    print(f"validate.py — {HAUPTDOKUMENT.name}, Version {version}, "
          f"{len(text):,} Zeichen")
    for w in warnings:
        print(f"  WARNUNG: {w}")
    for e in errors:
        print(f"  FEHLER:  {e}")
    if not errors and not warnings:
        print("  Alle automatisierten Prüfschritte OK.")
    elif not errors:
        print(f"  {len(warnings)} Warnung(en), keine Fehler.")
    else:
        print(f"  {len(errors)} Fehler, {len(warnings)} Warnung(en).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
