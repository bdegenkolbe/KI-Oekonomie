# -*- coding: utf-8 -*-
"""Wandelt Die-Haftungswende.html in eine Markdown-Lesefassung um.

Die Lesefassung ist die Grundlage für validate_doc.py. Sie bildet deshalb
die Struktur vollständig ab: Kapitel als nummerierte Überschriften, das
Inhaltsverzeichnis und die Begriffslinks als Markdown-Anker, die Begriffe
als eigene Überschriften, Listen mit Marken, Abbildungen mit Nummer, Titel,
Unterzeile, Tabelle oder Diagrammplatzhalter und Quelle.
"""
import os, re, sys, unicodedata
from html.parser import HTMLParser

HIER = os.path.dirname(os.path.abspath(__file__))
LEER = {"meta", "link", "br", "img", "hr", "input"}


class Knoten:
    def __init__(self, tag, attrs, eltern=None):
        self.tag, self.attrs, self.eltern, self.kinder = tag, dict(attrs), eltern, []

    @property
    def klassen(self):
        return set(self.attrs.get("class", "").split())

    def finde(self, pred):
        for k in self.kinder:
            if isinstance(k, Knoten):
                if pred(k):
                    yield k
                yield from k.finde(pred)


class Baum(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.wurzel = Knoten("root", {})
        self.akt = self.wurzel

    def handle_starttag(self, tag, attrs):
        k = Knoten(tag, attrs, self.akt)
        self.akt.kinder.append(k)
        if tag not in LEER:
            self.akt = k

    def handle_endtag(self, tag):
        k = self.akt
        while k is not self.wurzel and k.tag != tag:
            k = k.eltern
        if k is not self.wurzel:
            self.akt = k.eltern

    def handle_data(self, d):
        self.akt.kinder.append(d)


def slug(text):
    """Anker nach der Regel von GitHub: Kleinschreibung, Umlaute bleiben,
    Satzzeichen fallen weg, jedes Leerzeichen wird ein Bindestrich.

    Bewusst NICHT wie slugify() in validate_doc.py: Dort zerlegt NFKD die
    Umlaute, bevor sie geschützt werden, sodass aus »ä« ein »a« wird. Solche
    Anker funktionieren in keiner üblichen Markdown-Ansicht. pruefe.py prüft
    die Anker deshalb selbst mit dieser Funktion.
    """
    text = unicodedata.normalize("NFC", re.sub(r"[`*]", "", text)).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


def text_roh(k):
    if isinstance(k, str):
        return k
    if k.tag in ("style", "script", "svg", "title"):
        return ""
    return "".join(text_roh(c) for c in k.kinder)


def sauber(t):
    return re.sub(r"\s+", " ", t).strip()


class Md:
    def __init__(self, wurzel):
        self.w = wurzel
        self.anker = {}          # HTML-id -> Markdown-Anker (Slug der Überschrift)
        self.zeilen = []
        self._anker_sammeln()

    # ---------------------------------------------------------------- Anker
    def _kapitel_titel(self, sec):
        kopf = next(sec.finde(lambda k: "kapkopf" in k.klassen), None)
        if kopf is None:
            return None
        brauen = sauber(text_roh(next(kopf.finde(lambda k: "eyebrow" in k.klassen))))
        h2 = sauber(text_roh(next(kopf.finde(lambda k: k.tag == "h2"))))
        m = re.match(r"Kapitel (\d+)", brauen)
        if m:
            return f"{m.group(1)} {h2}"
        return f"{brauen}: {h2}" if brauen not in ("Zusammenfassung",) else h2

    def _anker_sammeln(self):
        for sec in self.w.finde(lambda k: k.tag == "section" and "id" in k.attrs):
            t = self._kapitel_titel(sec)
            if t:
                self.anker[sec.attrs["id"]] = slug(t)
        for div in self.w.finde(lambda k: k.tag == "div" and k.attrs.get("id", "").startswith("g-")):
            dt = next(div.finde(lambda k: k.tag == "dt"))
            self.anker[div.attrs["id"]] = slug(sauber(text_roh(dt)))

    # ---------------------------------------------------------------- Inline
    def inline(self, k):
        if isinstance(k, str):
            return k
        if k.tag in ("style", "script", "title"):
            return ""
        if k.tag == "svg":
            return ""
        innen = "".join(self.inline(c) for c in k.kinder)
        if k.tag in ("strong", "b"):
            return f"**{innen.strip()}**" if innen.strip() else ""
        if k.tag == "em":
            return f"*{innen.strip()}*" if innen.strip() else ""
        if k.tag == "code":
            return f"`{innen}`"
        if k.tag == "a" and k.attrs.get("href", "").startswith("#"):
            ziel = self.anker.get(k.attrs["href"][1:], k.attrs["href"][1:])
            return f"[{innen.strip()}](#{ziel})"
        return innen

    def absatz(self, k, vor=""):
        t = sauber(self.inline(k))
        if t:
            self.zeilen += [vor + t, ""]

    # ---------------------------------------------------------------- Blöcke
    def block(self, k):
        if isinstance(k, str):
            if k.strip():
                self.absatz(Knoten("p", {}) if False else k)
            return
        kl, tag = k.klassen, k.tag
        if tag in ("style", "script", "title", "meta", "link"):
            return
        if tag == "section":
            return self.abschnitt(k)
        if tag == "h1":
            return self.absatz(k, "# ")
        if tag == "h3":
            return self.absatz(k, "### ")
        if tag == "p":
            if "unter" in kl or "kern" in kl:
                t = sauber(self.inline(k))
                self.zeilen += [f"*{t}*", ""]
                return
            if "zitat" in kl:
                return self.absatz(k, "> ")
            return self.absatz(k)
        if tag == "figure":
            return self.abbildung(k)
        if tag == "aside":
            return self.kasten(k)
        if tag in ("ul", "ol"):
            return self.liste(k)
        if tag == "dl":
            return self.glossar(k)
        if tag == "div" and "chart" in kl:
            svg = next(k.finde(lambda x: x.tag == "svg"), None)
            self.zeilen += [f"*[Diagramm: {svg.attrs.get('aria-label', '') if svg else ''}]*", ""]
            return
        if tag == "div" and "tabelle" in kl:
            return self.tabelle(next(k.finde(lambda x: x.tag == "table")))
        if tag == "div" and ("meta" in kl or "zahlen" in kl):
            for d in k.kinder:
                if isinstance(d, Knoten) and d.tag == "div":
                    teile = [c for c in d.kinder if isinstance(c, Knoten)]
                    kopf = sauber(self.inline(teile[0])) if teile else ""
                    rest = sauber("".join(self.inline(c) for c in d.kinder[d.kinder.index(teile[0]) + 1:])) if teile else ""
                    kopf = kopf.strip("*")
                    self.zeilen.append(f"- **{kopf}:** {rest}" if "meta" in kl else f"- **{kopf}** {rest}")
            self.zeilen.append("")
            return
        if tag == "div" and "eyebrow" in kl:
            t = sauber(self.inline(k))
            if t:
                self.zeilen += [f"**{t}**", ""]
            return
        for c in k.kinder:
            self.block(c)

    def abschnitt(self, sec):
        titel = self._kapitel_titel(sec)
        for c in sec.kinder:
            if isinstance(c, Knoten) and "kapkopf" in c.klassen:
                self.zeilen += [f"## {titel}", ""]
                kern = next(c.finde(lambda k: "kern" in k.klassen), None)
                if kern is not None:
                    self.block(kern)
                continue
            self.block(c)
        self.zeilen += ["---", ""]

    def abbildung(self, fig):
        brauen = sauber(text_roh(next(fig.finde(lambda k: "eyebrow" in k.klassen))))
        titel = sauber(self.inline(next(fig.finde(lambda k: "abbtitel" in k.klassen))))
        unter = sauber(self.inline(next(fig.finde(lambda k: "abbunter" in k.klassen))))
        self.zeilen += [f"**{brauen}: {titel}**", "", f"*{unter}*", ""]
        for c in fig.kinder:
            if isinstance(c, Knoten) and c.tag == "div" and ("chart" in c.klassen or "tabelle" in c.klassen):
                self.block(c)
        cap = next(fig.finde(lambda k: k.tag == "figcaption"), None)
        if cap is not None:
            self.absatz(cap)

    def kasten(self, a):
        brauen = next(a.finde(lambda k: "eyebrow" in k.klassen), None)
        self.zeilen += [f"> **{sauber(text_roh(brauen))}**", ">"]
        for c in a.kinder:
            if isinstance(c, Knoten) and c.tag == "p":
                self.zeilen += ["> " + sauber(self.inline(c)), ">"]
        self.zeilen[-1] = ""

    def liste(self, l):
        nummer = 0
        for li in l.kinder:
            if not (isinstance(li, Knoten) and li.tag == "li"):
                continue
            nummer += 1
            marke = f"{nummer}." if l.tag == "ol" else "-"
            if "kernaussagen" in l.klassen:
                teile = [c for c in next(li.finde(lambda k: k.tag == "div")).kinder if isinstance(c, Knoten)]
                t = f"**{sauber(text_roh(teile[0]))}:** {sauber(self.inline(teile[1]))}"
            elif l.eltern is not None and "inhalt" in l.eltern.klassen:
                nr = sauber(text_roh(next(li.finde(lambda k: k.tag == "span"))))
                a = next(li.finde(lambda k: k.tag == "a"))
                em = next(li.finde(lambda k: k.tag == "em"))
                marke = "-"
                t = f"{'' if nr == '·' else nr + ' '}{self.inline(a)}: {sauber(text_roh(em))}"
            else:
                t = sauber(self.inline(li))
                wer = next(li.finde(lambda k: "wer" in k.klassen), None)
                if wer is not None:
                    w = sauber(text_roh(wer))
                    t = t.replace(w, "").strip() + f" *({w})*"
            self.zeilen.append(f"{marke} {t}")
        self.zeilen.append("")

    def glossar(self, dl):
        for div in dl.kinder:
            if isinstance(div, Knoten) and div.tag == "div":
                dt = next(div.finde(lambda k: k.tag == "dt"))
                dd = next(div.finde(lambda k: k.tag == "dd"))
                self.zeilen += [f"#### {sauber(text_roh(dt))}", "", sauber(self.inline(dd)), ""]

    def tabelle(self, t):
        reihen = list(t.finde(lambda k: k.tag == "tr"))
        for i, tr in enumerate(reihen):
            zellen = [sauber(self.inline(z)).replace("|", "/") for z in tr.kinder
                      if isinstance(z, Knoten) and z.tag in ("td", "th")]
            self.zeilen.append("| " + " | ".join(zellen) + " |")
            if i == 0:
                self.zeilen.append("|" + "---|" * len(zellen))
        self.zeilen.append("")

    def ausgabe(self):
        main = next(self.w.finde(lambda k: k.tag == "main"))
        for c in main.kinder:
            self.block(c)
        text = "\n".join(self.zeilen)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        return re.sub(r"\n---\s*$", "", text) + "\n"


def umwandeln(quelle, ziel):
    b = Baum()
    b.feed(open(quelle, encoding="utf-8").read())
    text = Md(b.wurzel).ausgabe()
    open(ziel, "w", encoding="utf-8").write(text)
    return text


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HIER, "Die-Haftungswende.html")
    z = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HIER, "Die-Haftungswende.md")
    t = umwandeln(q, z)
    print(z, len(t.split()), "Wörter")
