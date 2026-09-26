# -*- coding: utf-8 -*-
"""Prüflauf für »Die Haftungswende«.

1. Erzeugt die Lesefassung Die-Haftungswende.md aus der HTML-Seite.
2. Ruft validate_doc.py (Skill dokument-validierung) mit allen Checks und
   der projekteigenen Slang-Liste auf. §-Treffer, die in derselben Zeile ein
   Gesetz nennen (SGB, KHEntgG), sind Normzitate und keine internen Verweise;
   sie werden herausgefiltert, alle anderen Befunde bleiben stehen.
   Markdown-Anker prüft dieser Lauf selbst nach der Regel von GitHub
   (Umlaute bleiben erhalten); die Ankerprüfung von validate_doc.py bildet
   Umlaute auf Grundbuchstaben ab und würde gültige Anker verwerfen.
3. Prüft zusätzlich, was validate_doc.py nicht kennt: Abbildungsverweise im
   Fließtext, verbotenen Verfahrensjargon und dass jeder Begriff im Anhang
   im Text verlinkt ist.

Aufruf: python3 pruefe.py [PFAD/ZU/validate_doc.py]
Exit-Code 0 = keine Befunde, 1 = Befunde.
"""
import glob, os, re, subprocess, sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from als_markdown import umwandeln

MD = os.path.join(HIER, "Die-Haftungswende.md")
umwandeln(os.path.join(HIER, "Die-Haftungswende.html"), MD)
zeilen = open(MD, encoding="utf-8").read().splitlines()
befunde = []

# ---------------------------------------------------------------- validate_doc.py
kandidaten = sys.argv[1:] or glob.glob("/root/.claude/skills/**/dokument-validierung/scripts/validate_doc.py", recursive=True)
if not kandidaten:
    print("validate_doc.py nicht gefunden; Pfad als Argument übergeben.")
    sys.exit(2)
lauf = subprocess.run([sys.executable, kandidaten[0], MD, "--slang-liste", os.path.join(HIER, "slang-liste.txt")],
                      capture_output=True, text=True)
NORM = re.compile(r"§\s?\d+[a-z]?(?:\s+Abs\.\s*\d+[a-z]?)?(?:\s+(?:Nr\.|Satz)\s*\d+)?\s+(?:SGB|KHEntgG)"
                  r"|(?:SGB\s+[IVX]+|KHEntgG)\s+§§?\s?\d")
hinweise = []
for z in lauf.stdout.splitlines():
    m = re.match(r"\s*Zeile\s+(\d+)\s+\[(.+?)\]\s+(.*)", z)
    if not m:
        continue
    nr, art, text = int(m.group(1)), m.group(2), m.group(3)
    if art == "Querverweis" and text.startswith("§") and NORM.search(zeilen[nr - 1]):
        continue
    if art == "Querverweis" and text.startswith("Anker #"):
        continue          # Anker prüft dieser Lauf selbst, siehe unten

    (hinweise if "Hinweis" in art else befunde).append(f"Zeile {nr} [{art}] {text}")

# ---------------------------------------------------------------- eigene Checks
volltext = "\n".join(zeilen)
abb = {int(n): i for i, z in enumerate(zeilen) for n in re.findall(r"^\*\*Abbildung (\d+):", z)}
if sorted(abb) != list(range(1, len(abb) + 1)):
    befunde.append(f"Abbildungsnummern nicht fortlaufend: {sorted(abb)}")
for i, z in enumerate(zeilen, 1):
    if z.startswith("**Abbildung"):
        continue
    for n in re.findall(r"Abbildung (\d+)\b", z):
        if int(n) not in abb:
            befunde.append(f"Zeile {i} [Abbildungsverweis] Abbildung {n} existiert nicht")

VERBOTEN = [r"\bFachurteil", r"\bKettenurteil", r"\bStation\b", r"\bÜbergabe", r"\bhaftende[nr]? Schicht",
            r"\bÜbertragungsbr", r"\bSpaltungsverst", r"\bbinär", r"\bzu beschließen", r"\bZwischenmarke"]
for i, z in enumerate(zeilen, 1):
    if z.startswith("Quelle:") or z.startswith("- Szenariokonferenz"):
        continue
    for v in VERBOTEN:
        if re.search(v, z):
            befunde.append(f"Zeile {i} [Wortschatz] „{re.search(v, z).group(0)}“ ist laut Prüfprofil zu ersetzen")

from als_markdown import slug
ueberschriften = {slug(re.sub(r"^#+\s+", "", z)) for z in zeilen if re.match(r"^#{1,6}\s", z)}
for i, z in enumerate(zeilen, 1):
    for ziel in re.findall(r"\]\(#([^)]+)\)", z):
        if ziel not in ueberschriften:
            befunde.append(f"Zeile {i} [Anker] #{ziel} hat kein Überschriften-Ziel")

begriffe = [z[5:].strip() for z in zeilen if z.startswith("#### ")]
for b in begriffe:
    if f"](#{slug(b)})" not in volltext:
        befunde.append(f"[Glossar] Begriff „{b}“ wird im Text nicht verlinkt")

# ---------------------------------------------------------------- Ergebnis
links = len(re.findall(r"\]\(#", volltext))
print(f"{len(abb)} Abbildungen, {len(begriffe)} Begriffe, {links} interne Links")
for b in befunde:
    print("BEFUND ", b)
for h in hinweise:
    print("Hinweis", h)
print(f"{len(befunde)} Befund(e), {len(hinweise)} Hinweis(e)")
sys.exit(1 if befunde else 0)
