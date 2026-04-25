"""
build_pdf.py — PDF-Export gemäß Formatvorlage.md.

Erzeugt aus `Arbeitspapier_KI_Robotik_Besteuerung.md` ein PDF im
Corporate-Layout (A4, Navy/Stahlblau, Header/Footer, Akzentlinien
über Kapiteln, Sonderformat für die Deutschland-These in § 8.5).
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Arbeitspapier_KI_Robotik_Besteuerung.md"
OUTPUT = ROOT / "Arbeitspapier_KI_Robotik_Besteuerung.pdf"

PRIMARY = colors.HexColor("#1B3A5C")
ACCENT = colors.HexColor("#2E75B6")
GREY = colors.HexColor("#666666")
LIGHT_GREY = colors.HexColor("#999999")
TABLE_HEAD_BG = PRIMARY
TABLE_HEAD_FG = colors.white
TABLE_ALT = colors.HexColor("#F2F7FB")
TABLE_BORDER = colors.HexColor("#B0C4DE")
QUOTE_BG = colors.HexColor("#F0F5FA")
CODE_BG = colors.HexColor("#F5F5F5")
HEADER_LINE = colors.HexColor("#CCCCCC")

DOC_TITLE = "Die Besteuerung von Künstlicher Intelligenz und Robotik als Ersatz menschlicher Arbeit"
DOC_SHORT_TITLE = "Arbeitspapier — Besteuerung von KI und Robotik"
DOC_ORG = "HIGL — Health Innovators Group Leipzig"
DOC_AUTHOR = "Björn Degenkolbe"
DOC_VERSION = "Version 10.0 — April 2026 — CC BY 4.0"

LEFT_MARGIN = 2 * cm
RIGHT_MARGIN = 2 * cm
TOP_MARGIN = 2.5 * cm
BOTTOM_MARGIN = 2.5 * cm
CONTENT_WIDTH = A4[0] - LEFT_MARGIN - RIGHT_MARGIN


@dataclass
class StyleSet:
    title_main: ParagraphStyle
    title_sub: ParagraphStyle
    title_small: ParagraphStyle
    meta: ParagraphStyle
    h2: ParagraphStyle
    h3: ParagraphStyle
    h4: ParagraphStyle
    body: ParagraphStyle
    list_item: ParagraphStyle
    quote: ParagraphStyle
    thesis: ParagraphStyle
    table_head: ParagraphStyle
    table_cell: ParagraphStyle


def make_styles() -> StyleSet:
    base = ParagraphStyle(
        "base",
        fontName="Helvetica",
        fontSize=9.5,
        leading=13,
        textColor=colors.black,
        spaceBefore=1,
        spaceAfter=2,
        alignment=4,  # justify
    )
    return StyleSet(
        title_main=ParagraphStyle(
            "title_main",
            parent=base,
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=26,
            textColor=PRIMARY,
            alignment=1,
            spaceAfter=4 * mm,
        ),
        title_sub=ParagraphStyle(
            "title_sub",
            parent=base,
            fontName="Helvetica-Bold",
            fontSize=16,
            leading=20,
            textColor=PRIMARY,
            alignment=1,
            spaceAfter=3 * mm,
        ),
        title_small=ParagraphStyle(
            "title_small",
            parent=base,
            fontName="Helvetica",
            fontSize=11,
            leading=14,
            textColor=ACCENT,
            alignment=1,
            spaceAfter=10 * mm,
        ),
        meta=ParagraphStyle(
            "meta",
            parent=base,
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            textColor=GREY,
            alignment=1,
            spaceAfter=1 * mm,
        ),
        h2=ParagraphStyle(
            "h2",
            parent=base,
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            textColor=PRIMARY,
            alignment=0,
            spaceBefore=3 * mm,
            spaceAfter=3 * mm,
        ),
        h3=ParagraphStyle(
            "h3",
            parent=base,
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            textColor=ACCENT,
            alignment=0,
            spaceBefore=3 * mm,
            spaceAfter=2 * mm,
        ),
        h4=ParagraphStyle(
            "h4",
            parent=base,
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            textColor=colors.HexColor("#333333"),
            alignment=0,
            spaceBefore=2 * mm,
            spaceAfter=1 * mm,
        ),
        body=base,
        list_item=ParagraphStyle(
            "list_item",
            parent=base,
            leftIndent=10 * mm,
            firstLineIndent=-4 * mm,
            bulletIndent=6 * mm,
            spaceAfter=1 * mm,
        ),
        quote=ParagraphStyle(
            "quote",
            parent=base,
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#333333"),
            alignment=0,
        ),
        thesis=ParagraphStyle(
            "thesis",
            parent=base,
            fontName="Helvetica-Oblique",
            fontSize=9.5,
            leading=13,
            textColor=PRIMARY,
            alignment=0,
        ),
        table_head=ParagraphStyle(
            "table_head",
            parent=base,
            fontName="Helvetica-Bold",
            fontSize=7.5,
            leading=10,
            textColor=colors.white,
            alignment=0,
        ),
        table_cell=ParagraphStyle(
            "table_cell",
            parent=base,
            fontName="Helvetica",
            fontSize=7.5,
            leading=10,
            textColor=colors.black,
            alignment=0,
        ),
    )


_INLINE_BOLD = re.compile(r"\*\*(.+?)\*\*")
_INLINE_ITALIC = re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)")
_INLINE_CODE = re.compile(r"`([^`]+)`")
_INLINE_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def md_inline_to_rl(text: str) -> str:
    """Convert a subset of markdown inline syntax to reportlab markup."""

    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = _INLINE_LINK.sub(lambda m: f'<link href="{m.group(2)}" color="#2E75B6">{m.group(1)}</link>', text)
    text = _INLINE_BOLD.sub(r"<b>\1</b>", text)
    text = _INLINE_ITALIC.sub(r"<i>\1</i>", text)
    text = _INLINE_CODE.sub(r'<font face="Courier" size="8.5">\1</font>', text)
    return text


def parse_table(lines: list[str], idx: int) -> tuple[list[list[str]], int]:
    rows: list[list[str]] = []
    while idx < len(lines) and lines[idx].lstrip().startswith("|"):
        raw = lines[idx].strip()
        cells = [c.strip() for c in raw.strip("|").split("|")]
        rows.append(cells)
        idx += 1
    if len(rows) >= 2 and all(set(c) <= set("-:") for c in rows[1]):
        rows.pop(1)
    return rows, idx


def build_table(rows: list[list[str]], styles: StyleSet) -> Table:
    head = [Paragraph(md_inline_to_rl(c), styles.table_head) for c in rows[0]]
    body = [
        [Paragraph(md_inline_to_rl(c), styles.table_cell) for c in r] for r in rows[1:]
    ]
    data = [head] + body
    n_cols = len(rows[0])
    col_width = CONTENT_WIDTH / n_cols
    table = Table(data, colWidths=[col_width] * n_cols, repeatRows=1)
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEAD_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), TABLE_HEAD_FG),
        ("GRID", (0, 0), (-1, -1), 0.5, TABLE_BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]
    for i, _ in enumerate(body, start=1):
        if i % 2 == 1:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), TABLE_ALT))
    table.setStyle(TableStyle(style_cmds))
    return table


def quote_block(text: str, styles: StyleSet, *, thesis: bool = False) -> Table:
    """Render blockquote (with optional emphasised "thesis" variant)."""

    bar_color = PRIMARY if thesis else ACCENT
    bar_width = 4 if thesis else 3
    para = Paragraph(md_inline_to_rl(text), styles.thesis if thesis else styles.quote)
    inner = Table(
        [["", para]],
        colWidths=[bar_width, CONTENT_WIDTH - 8 * mm - bar_width],
    )
    inner.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), bar_color),
                ("BACKGROUND", (1, 0), (1, 0), QUOTE_BG),
                ("LEFTPADDING", (1, 0), (1, 0), 4),
                ("RIGHTPADDING", (1, 0), (1, 0), 4),
                ("TOPPADDING", (1, 0), (1, 0), 4),
                ("BOTTOMPADDING", (1, 0), (1, 0), 4),
                ("LEFTPADDING", (0, 0), (0, 0), 0),
                ("RIGHTPADDING", (0, 0), (0, 0), 0),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    outer = Table([["", inner]], colWidths=[8 * mm, CONTENT_WIDTH - 8 * mm])
    outer.setStyle(
        TableStyle(
            [
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return outer


def chapter_accent(thick: bool = False) -> Table:
    width = CONTENT_WIDTH
    height = 2 if thick else 1.5
    line = Table([[" "]], colWidths=[width], rowHeights=[height])
    line.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), ACCENT),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return line


def build_story(md_text: str, styles: StyleSet) -> list:
    lines = md_text.splitlines()
    story: list = []

    # --- Cover -------------------------------------------------------
    story.append(Spacer(1, 6 * cm))
    story.append(Paragraph("Arbeitspapier", styles.title_sub))
    story.append(Paragraph(DOC_TITLE, styles.title_main))
    story.append(
        Paragraph(
            "Ökonomische, rechtliche und sozialpolitische Perspektiven",
            styles.title_small,
        )
    )
    story.append(Spacer(1, 3 * cm))
    story.append(Paragraph(DOC_AUTHOR, styles.meta))
    story.append(Paragraph(DOC_ORG, styles.meta))
    story.append(Paragraph("Stand: April 2026", styles.meta))
    story.append(Paragraph("Version 10.0", styles.meta))
    story.append(Paragraph("Lizenz: Creative Commons CC BY 4.0", styles.meta))
    story.append(PageBreak())

    in_thesis_quote = False
    quote_buffer: list[str] = []
    list_buffer: list[str] = []
    paragraph_buffer: list[str] = []
    body_started = False

    def flush_paragraph() -> None:
        if paragraph_buffer:
            text = " ".join(paragraph_buffer).strip()
            if text:
                story.append(Paragraph(md_inline_to_rl(text), styles.body))
            paragraph_buffer.clear()

    def flush_list() -> None:
        if list_buffer:
            for item in list_buffer:
                story.append(
                    Paragraph(
                        md_inline_to_rl(item),
                        styles.list_item,
                        bulletText="•",
                    )
                )
            list_buffer.clear()

    def flush_quote() -> None:
        nonlocal in_thesis_quote
        if quote_buffer:
            text = " ".join(s.strip() for s in quote_buffer if s.strip())
            story.append(quote_block(text, styles, thesis=in_thesis_quote))
            quote_buffer.clear()
            in_thesis_quote = False

    def flush_all() -> None:
        flush_paragraph()
        flush_list()
        flush_quote()

    i = 0
    skip_until_chapter1 = True

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip the markdown front-matter (cover content) until we reach Kapitel 1.
        if skip_until_chapter1:
            if re.match(r"^##\s+1\.\s", stripped):
                skip_until_chapter1 = False
            else:
                i += 1
                continue

        # Headings ----------------------------------------------------
        if stripped.startswith("## "):
            flush_all()
            heading = stripped[3:].strip()
            if body_started:
                story.append(PageBreak())
            body_started = True
            thick = heading.lower().startswith("8.")
            story.append(chapter_accent(thick=thick))
            story.append(Spacer(1, 1 * mm))
            story.append(Paragraph(md_inline_to_rl(heading), styles.h2))
            i += 1
            continue
        if stripped.startswith("### "):
            flush_all()
            story.append(Paragraph(md_inline_to_rl(stripped[4:].strip()), styles.h3))
            i += 1
            continue
        if stripped.startswith("#### "):
            flush_all()
            story.append(Paragraph(md_inline_to_rl(stripped[5:].strip()), styles.h4))
            i += 1
            continue

        # Tables ------------------------------------------------------
        if stripped.startswith("|"):
            flush_all()
            rows, i = parse_table(lines, i)
            story.append(build_table(rows, styles))
            story.append(Spacer(1, 2 * mm))
            continue

        # Blockquotes -------------------------------------------------
        if stripped.startswith(">"):
            flush_paragraph()
            flush_list()
            content = stripped[1:].strip()
            if content.startswith("**KI ist als eigenständiger dritter Produktionsfaktor"):
                in_thesis_quote = True
            quote_buffer.append(content)
            i += 1
            continue
        if quote_buffer and not stripped.startswith(">"):
            flush_quote()

        # Lists -------------------------------------------------------
        if stripped.startswith("- "):
            flush_paragraph()
            list_buffer.append(stripped[2:].strip())
            i += 1
            continue
        if list_buffer and not stripped.startswith("- "):
            flush_list()

        # Numbered lists (treat as paragraphs to avoid re-numbering)
        # Horizontal rules / blank lines -----------------------------
        if not stripped or stripped == "---":
            flush_paragraph()
            if not stripped:
                pass
            else:
                story.append(Spacer(1, 2 * mm))
            i += 1
            continue

        # Default: collect paragraph text
        paragraph_buffer.append(stripped)
        i += 1

    flush_all()
    return story


def header_footer(canvas, doc):  # noqa: ANN001 — reportlab callback
    page_num = canvas.getPageNumber()
    canvas.saveState()
    if page_num == 1:
        canvas.restoreState()
        return
    width, height = A4
    # Header
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(LIGHT_GREY)
    canvas.drawString(LEFT_MARGIN, height - TOP_MARGIN + 12, DOC_SHORT_TITLE)
    canvas.drawRightString(width - RIGHT_MARGIN, height - TOP_MARGIN + 12, DOC_ORG)
    canvas.setStrokeColor(HEADER_LINE)
    canvas.setLineWidth(0.5)
    canvas.line(LEFT_MARGIN, height - TOP_MARGIN + 8, width - RIGHT_MARGIN, height - TOP_MARGIN + 8)
    # Footer
    canvas.setStrokeColor(HEADER_LINE)
    canvas.line(LEFT_MARGIN, BOTTOM_MARGIN - 10, width - RIGHT_MARGIN, BOTTOM_MARGIN - 10)
    canvas.setFillColor(LIGHT_GREY)
    canvas.drawString(LEFT_MARGIN, BOTTOM_MARGIN - 20, DOC_VERSION)
    canvas.drawRightString(
        width - RIGHT_MARGIN, BOTTOM_MARGIN - 20, f"Seite {page_num}"
    )
    canvas.restoreState()


def main() -> int:
    if not SOURCE.exists():
        print(f"Quelle nicht gefunden: {SOURCE}", file=sys.stderr)
        return 1
    md_text = SOURCE.read_text(encoding="utf-8")
    styles = make_styles()
    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN,
        title=DOC_TITLE,
        author=DOC_AUTHOR,
    )
    frame = Frame(
        LEFT_MARGIN,
        BOTTOM_MARGIN,
        CONTENT_WIDTH,
        A4[1] - TOP_MARGIN - BOTTOM_MARGIN,
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    template = PageTemplate(id="main", frames=[frame], onPage=header_footer)
    doc.addPageTemplates([template])
    story = build_story(md_text, styles)
    doc.build(story)
    print(f"PDF geschrieben: {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
