# -*- coding: utf-8 -*-
"""Wandelt Die-Haftungswende.html in eine Markdown-Lesefassung um.

Die Markdown-Fassung dient der Prüfung (validate_doc.py) und als reine
Textfassung zum Gegenlesen. Diagramme erscheinen als Platzhalter mit Titel.
"""
import html, os, re, sys
from html.parser import HTMLParser

HIER = os.path.dirname(os.path.abspath(__file__))


class Md(HTMLParser):
    BLOCK = {"p", "h1", "h2", "h3", "li", "figcaption", "tr", "div"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.buf, self.stack = [], [], []
        self.skip = 0          # in <style>, <svg>, <title>
        self.zelle = []
        self.ol = []

    def flush(self, prefix=""):
        t = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        self.buf = []
        if t:
            self.out.append(prefix + t)
            self.out.append("")

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("style", "svg", "title", "script"):
            self.skip += 1
            if tag == "svg":
                self.out.append(f"*[Diagramm: {a.get('aria-label', '')}]*")
                self.out.append("")
            return
        if self.skip:
            return
        if tag in ("h1", "h2", "h3", "p", "li", "figcaption", "dt"):
            self.flush()
        if tag in ("strong", "b"):
            self.buf.append("**")
        if tag == "em":
            self.buf.append("*")
        if tag == "ol":
            self.ol.append(0)
        if tag == "li" and self.ol:
            self.ol[-1] += 1
        if tag in ("td", "th"):
            self.zelle = []
        self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in ("style", "svg", "title", "script"):
            self.skip -= 1
            return
        if self.skip:
            return
        if tag in ("strong", "b"):
            self.buf.append("** ")
        if tag == "em":
            self.buf.append("* ")
        if tag in ("dt",):
            self.buf.append(": ")
        if tag == "h1":
            self.flush("# ")
        elif tag == "h2":
            self.flush("## ")
        elif tag == "h3":
            self.flush("### ")
        elif tag == "li":
            self.flush(f"{self.ol[-1]}. " if self.ol else "- ")
        elif tag in ("p", "figcaption"):
            self.flush()
        elif tag == "ol":
            self.ol.pop()
        elif tag in ("td", "th"):
            self.zelle.append(re.sub(r"\s+", " ", "".join(self.buf)).strip())
            self.buf = []
            self.reihe.append(self.zelle[-1])
        elif tag == "tr":
            self.out.append("| " + " | ".join(self.reihe) + " |")
            if self.kopf:
                self.out.append("|" + "---|" * len(self.reihe))
                self.kopf = False
            self.reihe = []
        elif tag == "table":
            self.out.append("")
        elif tag == "div":
            self.flush()
        if self.stack:
            self.stack.pop()

    def handle_data(self, d):
        if not self.skip:
            self.buf.append(d)

    reihe = []
    kopf = False

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


def umwandeln(quelle, ziel):
    roh = open(quelle, encoding="utf-8").read()
    roh = re.sub(r"<thead>", "<thead data-kopf>", roh)
    p = Md()
    # Kopfzeilen erkennen
    orig = p.handle_starttag
    def start(tag, attrs):
        if tag == "thead":
            p.kopf = True
        orig(tag, attrs)
    p.handle_starttag = start
    p.feed(roh)
    p.flush()
    text = "\n".join(p.out)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    open(ziel, "w", encoding="utf-8").write(text)
    return text


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HIER, "Die-Haftungswende.html")
    z = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HIER, "Die-Haftungswende.md")
    t = umwandeln(q, z)
    print(z, len(t.split()), "Wörter")
