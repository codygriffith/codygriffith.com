#!/usr/bin/env python3
"""
Regenerate static/resume.pdf.

The resume's design comes from Affinity Publisher (static/resume.afpub), and the
exported PDF embeds its fonts as *subset* Identity-H fonts with the text emitted as
glyph-level fragments. That makes editing the existing text in place impossible: new
characters may not exist in the subset, and their positions would have to be
recomputed by hand.

What this script does instead:

  1. Leaves the original artwork alone. The top bar, contact icons, WORK EXPERIENCE
     and EDUCATION sections are carried over untouched.
  2. Redacts the PROJECTS heading and the PROJECT + SKILLS region, which REMOVES that
     text from the content stream. Painting a white rectangle over it is not enough: the
     text would still be in the page, so ATS parsers, screen readers and copy-paste
     would keep reading the old content (and, for a while, both versions at once).
  3. Redraws that region from the text below with the same typeface, size, colours,
     indents and leading as the original, then merges the two.

Because step 2 clears everything below REWRITE_TOP (plus the renamed heading) and step 3
redraws all of it, the script is repeatable: re-running it on its own output produces the same
document. The bytes will differ, though — PDF generation is not byte-deterministic — so expect
a changed file, not a modified one, in version control. A re-run is only worth committing if
the content changed.

Geometry is measured from the original export (see get_drawings()/get_text("dict")
coordinates), not guessed, so the PROJECT and SKILLS anchors land on the same y
positions the original design used and the page keeps its original extent.

Requires: reportlab, pymupdf, pypdf  (pip install reportlab pymupdf pypdf)
Requires: the Lato family installed, or LATO_DIR pointing at the TTFs.

NOTE: once you run this, the PDF is the source of truth. Publishing from Affinity
later will overwrite these changes.
"""

from __future__ import annotations

import io
import os
import sys
import tempfile
from pathlib import Path

import pymupdf
from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# --------------------------------------------------------------------------------------
# Content
# --------------------------------------------------------------------------------------

PROJECTS: list[tuple[str, list[str]]] = [
    (
        "Cull-Pro | https://cull-pro.com",
        [
            "Built a browser-based RAW culling app for photographers: keep or reject each frame with one keystroke, then deliver private client galleries.",
            "Decoded 40+ camera RAW formats on-device via LibRaw and WebAssembly.",
            "Shipped Supabase accounts and Stripe billing on Cloudflare Workers, with originals in S3-compatible object storage.",
        ],
    ),
    (
        "Pathlight | https://pathlight.dev",
        [
            "Built a free website-audit tool running Google Lighthouse, with Core Web Vitals, SEO and accessibility reporting.",
            "Implemented user authentication and saved audit history.",
            "Added email report sharing and a stateless SVG audit badge, and served the prerendered React app from Cloudflare Workers.",
        ],
    ),
]

# Filled column by column (i % 3, i // 3). Three columns of six keeps the block on the
# original 6-row footprint; a seventh row would run into the bottom margin.
SKILLS: list[str] = [
    "Cloudflare Workers", "Next.js", "React", "SvelteKit", "TypeScript", "Tailwind CSS",
    "Supabase", "Stripe", "WebAssembly", "Git", "CI/CD", "SEO",
    "NGINX", "Apache", "Gunicorn", "Flask", "AWS", "Netlify",
]

# Text above REWRITE_TOP must survive every run; it is not redrawn.
PRESERVED_TEXT = [
    "Cody Griffith", "cody@codygriffith.com", "(706)366-5561", "Columbus, GA",
    "https://codygriffith.com", "WORK EXPERIENCE", "Alenthea Design Co.",
    "Web Developer", "June 2020 - Present", "Freelance Web Designer",
    "August 2017", "EDUCATION", "Columbus State University",
    "Bachelor of Science in Computer Science", "December 2019", "PROJECTS", "SKILLS",
]

# Section headings are matched as whole lines, so "PROJECTS" cannot be satisfied by a
# leftover "PROJECT" (which is a substring of it) and vice versa.
SECTION_HEADINGS = {"PROJECTS": True, "PROJECT": False}

# Must never appear in the output: dead projects and superseded claims.
STALE_TEXT = ["Contidly", "contidly.com", "AWS Lambda", "CRM for web agencies"]

# --------------------------------------------------------------------------------------
# Layout constants, measured from the original export
# --------------------------------------------------------------------------------------

PAGE_W, PAGE_H = 612.0, 792.0
SIZE = 11.0
SKY = HexColor("#0EA5E9")   # section markers and the page-top bar
INK = HexColor("#171717")   # body copy

NAME_X = 60.0               # project name column
BULLET_X = 66.0
TEXT_X = 78.4               # bullet text; also the hang indent for wrapped lines
RIGHT = 552.0               # right margin
HEADING_X = 100.5           # "SKILLS" text
COL_X = (66.0, 201.1, 343.5)
BAR_X, BAR_W, BAR_H = 60.0, 30.0, 3.8

LEAD = 14.3                 # line pitch
NAME_TO_FIRST = 14.7        # project name -> its first bullet
PROJ_GAP = 21.8             # last bullet of a project -> next project name
BAR_GAP = 32.0              # last bullet -> next section marker
BAR_TO_HEAD = 2.7           # marker sits this far below the heading's bbox top
HEAD_TO_ROW = 19.2          # heading -> first skills row
FIRST_LINE_TOP = 472.9      # first project name
REWRITE_TOP = 466.0         # everything below this line is cleared and redrawn
BOTTOM_LIMIT = 774.0        # last baseline must stay above this

# The existing heading is part of the artwork above REWRITE_TOP, so it has to be redacted
# and redrawn on its own. PROJECT_HEADING_TOP is its measured bbox top; the clear box
# starts at x=95 so it cannot touch the section's marker bar (x 60-90).
PROJECT_HEADING_TOP = 452.2
PROJECT_HEADING_CLEAR = (95.0, 446.0, 260.0, REWRITE_TOP)

REPO = Path(__file__).resolve().parents[1]
PDF = REPO / "static" / "resume.pdf"


def find_fonts() -> Path:
    """Locate the Lato TTFs. Override with LATO_DIR if they live elsewhere."""
    candidates = [Path(p) for p in filter(None, [os.environ.get("LATO_DIR")])]
    for env in ("LOCALAPPDATA", "APPDATA"):
        if os.environ.get(env):
            candidates.append(Path(os.environ[env]) / "Microsoft" / "Windows" / "Fonts")
    candidates.append(Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts")

    for directory in candidates:
        if (directory / "Lato-Regular.ttf").is_file():
            return directory
    sys.exit(
        "Lato-Regular.ttf / Lato-Bold.ttf not found. Install the Lato family or set "
        "LATO_DIR to the folder containing them."
    )


FONT_DIR = find_fonts()
pdfmetrics.registerFont(TTFont("Lato", str(FONT_DIR / "Lato-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Lato-Bold", str(FONT_DIR / "Lato-Bold.ttf")))


def measure_ascent_offset() -> float:
    """
    reportlab draws from a baseline; the original geometry is expressed as bbox tops.
    Measure the gap between the two for this font/size rather than assuming it.
    """
    buf = io.BytesIO()
    probe = canvas.Canvas(buf, pagesize=(PAGE_W, PAGE_H))
    probe.setFont("Lato", SIZE)
    probe.drawString(100, 100, "NGINX")
    probe.showPage()
    probe.save()
    buf.seek(0)

    page = pymupdf.open(stream=buf.read(), filetype="pdf")[0]
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            # drawn at bottom-origin baseline 100 -> top-origin top
            #   top = PAGE_H - baseline - ascent
            return PAGE_H - 100.0 - line["bbox"][1]
    raise RuntimeError("ascent calibration failed")


ASCENT = measure_ascent_offset()


def baseline(top: float) -> float:
    """Top-origin line top (as measured from the original) -> reportlab baseline."""
    return PAGE_H - top - ASCENT


def wrap(text: str, max_width: float) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if pdfmetrics.stringWidth(trial, "Lato", SIZE) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def build_overlay(path: Path) -> tuple[float, int]:
    canvas_ = canvas.Canvas(str(path), pagesize=(PAGE_W, PAGE_H))
    canvas_.setTitle("Cody Griffith - Resume")

    # Renamed section heading, drawn in the gap above the cleared region.
    canvas_.setFont("Lato-Bold", SIZE)
    canvas_.setFillColor(INK)
    canvas_.drawString(HEADING_X, baseline(PROJECT_HEADING_TOP), "PROJECTS")

    # Clear the region being redrawn (the heading sits above it).
    canvas_.setFillColor(HexColor("#FFFFFF"))
    canvas_.rect(55.0, 0.0, 502.0, PAGE_H - REWRITE_TOP, stroke=0, fill=1)

    pos = FIRST_LINE_TOP
    last_line = pos
    lines_used = 0

    for index, (name, bullets) in enumerate(PROJECTS):
        canvas_.setFont("Lato-Bold", SIZE)
        canvas_.setFillColor(INK)
        canvas_.drawString(NAME_X, baseline(pos), name)
        lines_used += 1
        pos += NAME_TO_FIRST

        for bullet in bullets:
            wrapped = wrap(bullet, RIGHT - TEXT_X)
            lines_used += len(wrapped)
            for j, line in enumerate(wrapped):
                top = pos + j * LEAD
                if j == 0:
                    # Bullet on the first line only; continuations hang at TEXT_X,
                    # matching the original (e.g. "processes." under WORK EXPERIENCE).
                    canvas_.setFont("Lato-Bold", SIZE)
                    canvas_.drawString(BULLET_X, baseline(top), "\u2022")
                canvas_.setFont("Lato", SIZE)
                canvas_.drawString(TEXT_X, baseline(top), line)
            last_line = pos + (len(wrapped) - 1) * LEAD
            pos = last_line + LEAD

        # Anchor to the last line actually drawn. Adding the gap to the next line slot
        # instead inserts a phantom line and stretches the section.
        if index < len(PROJECTS) - 1:
            pos = last_line + PROJ_GAP

    marker_top = last_line + BAR_GAP
    canvas_.setFillColor(SKY)
    canvas_.rect(BAR_X, PAGE_H - marker_top - BAR_H, BAR_W, BAR_H, stroke=0, fill=1)
    canvas_.setFont("Lato-Bold", SIZE)
    canvas_.setFillColor(INK)
    canvas_.drawString(HEADING_X, baseline(marker_top - BAR_TO_HEAD), "SKILLS")
    lines_used += 1

    row_top = marker_top - BAR_TO_HEAD + HEAD_TO_ROW
    rows = (len(SKILLS) + 2) // 3
    for i, skill in enumerate(SKILLS):
        column, row = i % 3, i // 3
        x = COL_X[column]
        top = row_top + row * LEAD
        canvas_.setFont("Lato-Bold", SIZE)
        canvas_.drawString(x, baseline(top), "\u2022")
        canvas_.setFont("Lato", SIZE)
        canvas_.drawString(x + 11.5, baseline(top), skill)
    lines_used += len(SKILLS)

    canvas_.showPage()
    canvas_.save()

    last_baseline = row_top + (rows - 1) * LEAD
    if last_baseline > BOTTOM_LIMIT:
        sys.exit(
            f"Content overflows: the last skills row baseline would be {last_baseline:.1f}, "
            f"past the {BOTTOM_LIMIT:.0f} limit. Trim a bullet or a skill."
        )
    return marker_top, lines_used


def verify(path: Path, expected: dict[str, float]) -> list[str]:
    doc = pymupdf.open(path)
    problems: list[str] = []

    if doc.page_count != 1:
        problems.append(f"expected 1 page, got {doc.page_count}")

    text = "".join(page.get_text() for page in doc)
    problems += [f"stale text still present: {t!r}" for t in STALE_TEXT if t in text]
    problems += [f"lost untouched text: {t!r}" for t in PRESERVED_TEXT if t not in text]

    lines = [
        "".join(span["text"] for span in line["spans"]).strip()
        for block in doc[0].get_text("dict")["blocks"]
        for line in block.get("lines", [])
    ]
    for heading, wanted in SECTION_HEADINGS.items():
        present = heading in lines
        if present != wanted:
            problems.append(
                f"section heading {heading!r} is {'present' if present else 'missing'} "
                f"but should be {'present' if wanted else 'missing'}"
            )

    def top_of(snippet: str) -> float | None:
        for block in doc[0].get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                if snippet in "".join(s["text"] for s in line["spans"]):
                    return round(line["bbox"][1], 1)
        return None

    for snippet, want in expected.items():
        got = top_of(snippet)
        if got is None:
            problems.append(f"missing from output: {snippet!r}")
        elif abs(got - want) > 0.2:
            problems.append(f"{snippet!r} at y={got}, expected {want}")
    return problems


def main() -> int:
    if not PDF.is_file():
        sys.exit(f"not found: {PDF}")

    with tempfile.TemporaryDirectory() as tmp:
        overlay = Path(tmp) / "overlay.pdf"
        redacted = Path(tmp) / "redacted.pdf"
        output = Path(tmp) / "resume.pdf"

        marker_top, lines_used = build_overlay(overlay)
        heading_top = round(marker_top - BAR_TO_HEAD, 1)

        # Remove the old copy from the content stream rather than hiding it: the drawn
        # region below, plus the old section heading, which is renamed.
        doc = pymupdf.open(PDF)
        page = doc[0]
        page.add_redact_annot(pymupdf.Rect(55.0, REWRITE_TOP, 557.0, PAGE_H))
        page.add_redact_annot(pymupdf.Rect(*PROJECT_HEADING_CLEAR))
        page.apply_redactions()
        doc.save(redacted)
        doc.close()

        # Merge the untouched artwork with the redrawn region.
        writer = PdfWriter()
        merged = PdfReader(str(redacted)).pages[0]
        merged.merge_page(PdfReader(str(overlay)).pages[0])
        writer.add_page(merged)
        with open(output, "wb") as handle:
            writer.write(handle)

        problems = verify(
            output,
            {
                "PROJECTS": PROJECT_HEADING_TOP,
                PROJECTS[0][0].split(" |")[0] + " |": FIRST_LINE_TOP,
                "SKILLS": heading_top,
            },
        )
        if problems:
            print("FAILED:", file=sys.stderr)
            for problem in problems:
                print(f"  - {problem}", file=sys.stderr)
            return 1

        # Only replace the real file once the new one has passed verification.
        os.replace(output, PDF)

    print(f"wrote {PDF.relative_to(REPO)}")
    print(f"  {lines_used} lines drawn; SKILLS heading at y={heading_top}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
