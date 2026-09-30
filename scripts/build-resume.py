#!/usr/bin/env python3
"""
Regenerate static/resume.pdf.

The resume's design comes from Affinity Publisher (static/resume.afpub), and the
exported PDF embeds its fonts as *subset* Identity-H fonts with the text emitted as
glyph-level fragments. That makes editing the existing text in place impossible: new
characters may not exist in the subset, and their positions would have to be
recomputed by hand.

What this script does instead:

  1. Keeps only the artwork that has no substitute: the page-top bar. Everything else — every
     text line and all four section markers — is redrawn.
  2. Redacts the text in bands that skip that artwork, which REMOVES it from the content
     stream. Painting white rectangles over it is not enough: the text would still be in
     the page, so ATS parsers, screen readers and copy-paste would keep reading the old
     content (and, for a while, both versions at once).
  3. Redraws every line with the same typeface, size, colours, indents and leading as the
     original, at the original's coordinates, so the design is unchanged.

That also makes the file more parseable than the Affinity export was. The export encodes
word spaces as glyph positioning rather than as space characters, which simple extractors
do not reconstruct — it read as "AlentheaDesignCo.", "W ebDeveloper". Everything drawn
here carries real spaces. Drawing the section markers too means editing content can never
leave a marker stranded where the old heading used to be.
Two layout choices exist for parsing rather than looks, and both are load-bearing:

  * The contact details are one left-aligned line, not four icon-anchored slots. The export
    spaced them 36pt apart, which layout analysis reads as separate columns; it then emits
    them after the text on their left, taking the first job's date with them.
  * SKILLS is a wrapped list, not the original three-column grid. A grid is three vertical
    boxes, read a column at a time (JavaScript, Next.js, HTML...), not the row order a
    person sees.
Because step 2 clears every band the text lives in and step 3 redraws all of it, the script
is repeatable: re-running it on its own output produces the same document. The bytes will
differ, though — PDF generation is not byte-deterministic — so expect a changed file, not a
modified one, in version control. A re-run is only worth committing if the content changed.

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
import re
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

# Rendered as a wrapped list rather than the original three-column grid. A grid is three
# vertical boxes to layout analysis, which reads it a column at a time (JavaScript, Next.js,
# HTML...); rows keep the order a person sees.
SKILLS: list[str] = [
    "JavaScript", "TypeScript", "React",
    "Next.js", "SvelteKit", "Tailwind CSS",
    "HTML", "CSS", "Cloudflare Workers",
    "Supabase", "Stripe", "Git",
    "CI/CD", "SEO", "NGINX",
    "Apache", "Flask", "Netlify",
]
SKILLS_PER_ROW = 6

NAME = "Cody Griffith"

# One left-aligned run. The original spread these across the page in four icon-anchored slots,
# which left 36pt of white between each pair; layout analysis reads that as four separate
# columns and emits them after the block on their left — including the first job's date, which
# shares their x-band. The icons went with them, so the details now read as a single line.
CONTACT = "cody@codygriffith.com | (706)366-5561 | Columbus, GA | https://codygriffith.com"
CONTACT_TOP = 56.0
CONTACT_X = 60.0

# Each job is an optional company line, a title line with its dates right-aligned beside it,
# and bullets. The original export gave the second job's dates a line of their own, which a
# layout-based parser reads as a stray date detached from the job, so both jobs now carry
# their dates on the title line.
WORK_EXPERIENCE: list[dict] = [
    {
        "company": "Alenthea Design Co.",
        "title": "Web Developer",
        "dates": "June 2020 - Present",
        "bullets": [
            "Lead the development of client websites, ensuring high performance, security, and scalability.",
            "Worked closely with design teams to integrate user-centered design principles into development processes.",
            "Implemented and maintained web applications using modern frameworks and technologies.",
            "Optimized websites for search engines and improved overall site performance and accessibility.",
            "Provided ongoing technical support and updates for client websites, ensuring seamless operation.",
        ],
    },
    {
        "company": "",
        "title": "Freelance Web Designer",
        # The export used an en dash here while every other date used a hyphen; hyphens are the
        # safer default for parsers, and matching the rest of the page is the tidier result.
        "dates": "August 2017 - June 2020",
        "bullets": [
            "Designed and developed custom websites for small businesses, focusing on responsive design and user experience.",
            "Collaborated with clients to create tailored web solutions, from concept to deployment.",
            "Managed all aspects of web design projects, including client communication, project timelines, and technical execution.",
            "Utilized HTML, CSS, JavaScript, and various content management systems to build and maintain websites.",
        ],
    },
]

EDUCATION = {
    "school": "Columbus State University",
    "degree": "Bachelor of Science in Computer Science",
    "dates": "December 2019",
}

SECTION_TITLES = ("WORK EXPERIENCE", "EDUCATION", "PROJECTS", "SKILLS")

# Section headings are matched as whole lines, so "PROJECTS" cannot be satisfied by a
# leftover "PROJECT" (which is a substring of it) and vice versa.
SECTION_HEADINGS = {
    "WORK EXPERIENCE": True,
    "EDUCATION": True,
    "PROJECTS": True,
    "PROJECT": False,
    "SKILLS": True,
}

# Must never appear in the output: dead projects and superseded claims.
STALE_TEXT = ["Contidly", "contidly.com", "AWS Lambda", "CRM for web agencies"]


def expected_phrases() -> list[str]:
    """Every string that must be findable in the finished PDF, taken from the content itself."""
    phrases = [NAME, EDUCATION["school"], EDUCATION["degree"], EDUCATION["dates"], *SECTION_TITLES]
    phrases += [part.strip() for part in CONTACT.split("|")]
    for job in WORK_EXPERIENCE:
        phrases += [job["title"], job["dates"]]
        if job["company"]:
            phrases.append(job["company"])
        phrases += job["bullets"]
    for project, bullets in PROJECTS:
        phrases += [project, *bullets]
    return phrases + SKILLS

# --------------------------------------------------------------------------------------
# Layout constants, measured from the original export
# --------------------------------------------------------------------------------------

PAGE_W, PAGE_H = 612.0, 792.0
SIZE = 11.0
SKY = HexColor("#0EA5E9")   # section markers and the page-top bar
INK = HexColor("#171717")   # body copy

NAME_X = 60.0
NAME_TOP = 26.14
NAME_SIZE = 20.0
BULLET_X = 66.0
TEXT_X = 78.4               # bullet text; also the hang indent for wrapped lines
RIGHT = 552.0               # right margin
HEADING_X = 100.5           # section heading text
BAR_X, BAR_W, BAR_H = 60.0, 30.0, 3.8

LEAD = 14.3                 # line pitch
CONTACT_TO_HEADING = 28.2   # contact line -> first section heading
HEADING_TO_FIRST = 19.2     # heading -> the first line of its body
COMPANY_TO_TITLE = 17.7     # company line -> job title
TITLE_TO_BULLET = 17.7      # title (or the date line under it) -> first bullet
JOB_GAP = 26.3              # last bullet of a job -> the next job's first line
SECTION_GAP = 29.3          # last body line -> the next section heading
DEGREE_TO_HEADING = 28.2    # education's last line -> the next section heading
PROJECT_HEADING_TO_FIRST = 20.7  # heading -> the first project's name
NAME_TO_FIRST = 14.7        # project name -> its first bullet
PROJ_GAP = 21.8             # last bullet of a project -> the next project's name
BAR_GAP = 32.0              # last bullet -> the next section marker
BAR_TO_HEAD = 2.7           # marker sits this far below the heading's bbox top
HEAD_TO_ROW = 19.2          # heading -> the first skills row
BOTTOM_LIMIT = 774.0        # the last row must stay above this

# Text is cleared in one band. The only artwork worth keeping is the page-top bar, which sits
# above y=20; the section markers are redrawn, and the contact icons are gone so nothing has to
# be stepped around.
CLEAR_AREA = (55.0, 20.0, 557.0, 792.0)

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


def measure_ascent_ratio() -> float:
    """
    reportlab draws from a baseline; the original geometry is expressed as bbox tops. Measure
    the gap between the two, as a fraction of the font size, rather than assuming it. The ratio
    is linear in size, so one 11pt probe covers every size on the page — and the verification
    step proves it, by checking the 20pt name lands on the original's coordinate.
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
            #   top = PAGE_H - baseline - ascent * size
            return (PAGE_H - 100.0 - line["bbox"][1]) / SIZE
    raise RuntimeError("ascent calibration failed")


ASCENT_RATIO = measure_ascent_ratio()


def baseline(top: float, size: float = SIZE) -> float:
    """Top-origin line top (as measured from the original) -> reportlab baseline."""
    return PAGE_H - top - ASCENT_RATIO * size


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


def draw_page(path: Path) -> dict[str, float]:
    """Draw every text line and section marker at the original design's coordinates."""
    c = canvas.Canvas(str(path), pagesize=(PAGE_W, PAGE_H))
    anchors: dict[str, float] = {}
    drawn = 0

    def text(x: float, top: float, value: str, font: str = "Lato", size: float = SIZE) -> None:
        nonlocal drawn
        c.setFont(font, size)
        c.setFillColor(INK)
        c.drawString(x, baseline(top, size), value)
        drawn += 1

    def right_text(top: float, value: str) -> None:
        c.setFont("Lato", SIZE)
        c.setFillColor(INK)
        c.drawRightString(RIGHT, baseline(top), value)

    def heading(top: float, label: str) -> None:
        """A section's marker sits BAR_TO_HEAD below its heading's bbox top."""
        c.setFillColor(SKY)
        c.rect(BAR_X, PAGE_H - top - BAR_TO_HEAD - BAR_H, BAR_W, BAR_H, stroke=0, fill=1)
        text(HEADING_X, top, label, "Lato-Bold")
        anchors[label] = round(top, 2)

    def bullet_list(items: list[str], top: float) -> float:
        """Draw bullets from `top`; return the top of the last line drawn."""
        last = top
        for item in items:
            lines = wrap(item, RIGHT - TEXT_X)
            for j, line in enumerate(lines):
                line_top = top + j * LEAD
                if j == 0:
                    # Bullet on the first line only; continuations hang at TEXT_X, matching
                    # the original (e.g. "processes." under WORK EXPERIENCE).
                    c.setFont("Lato-Bold", SIZE)
                    c.setFillColor(INK)
                    c.drawString(BULLET_X, baseline(line_top), "\u2022")
                text(TEXT_X, line_top, line)
            last = top + (len(lines) - 1) * LEAD
            top = last + LEAD
        return last

    # Header. The page-top bar is the only kept artwork, so the name and details are placed.
    anchors["name"] = NAME_TOP
    text(NAME_X, NAME_TOP, NAME, "Lato-Bold", NAME_SIZE)
    if pdfmetrics.stringWidth(CONTACT, "Lato", SIZE) > RIGHT - CONTACT_X:
        sys.exit(f"Contact line is too wide for the page: {CONTACT!r}")
    text(CONTACT_X, CONTACT_TOP, CONTACT)

    # WORK EXPERIENCE
    top = CONTACT_TOP + CONTACT_TO_HEADING
    heading(top, "WORK EXPERIENCE")
    top += HEADING_TO_FIRST
    for index, job in enumerate(WORK_EXPERIENCE):
        if job["company"]:
            text(NAME_X, top, job["company"], "Lato-Bold")
            top += COMPANY_TO_TITLE
        text(NAME_X, top, job["title"])
        # The dates sit at the right margin, so a long title could run into them. Fail loudly
        # rather than shipping a resume where the two overlap.
        gap = (
            RIGHT
            - NAME_X
            - pdfmetrics.stringWidth(job["title"], "Lato", SIZE)
            - pdfmetrics.stringWidth(job["dates"], "Lato", SIZE)
        )
        if gap < 12:
            sys.exit(f"Title and dates collide for {job['title']!r}: only {gap:.1f}pt left")
        right_text(top, job["dates"])
        top += TITLE_TO_BULLET
        top = bullet_list(job["bullets"], top) + (
            JOB_GAP if index < len(WORK_EXPERIENCE) - 1 else SECTION_GAP
        )

    # EDUCATION
    heading(top, "EDUCATION")
    top += HEADING_TO_FIRST
    text(NAME_X, top, EDUCATION["school"], "Lato-Bold")
    top += COMPANY_TO_TITLE
    text(NAME_X, top, EDUCATION["degree"])
    right_text(top, EDUCATION["dates"])
    top += DEGREE_TO_HEADING

    # PROJECTS
    heading(top, "PROJECTS")
    top += PROJECT_HEADING_TO_FIRST
    for index, (name, bullets) in enumerate(PROJECTS):
        text(NAME_X, top, name, "Lato-Bold")
        top += NAME_TO_FIRST
        top = bullet_list(bullets, top) + (PROJ_GAP if index < len(PROJECTS) - 1 else BAR_GAP)

    # `top` now sits BAR_GAP past the last project line, i.e. on the next marker.
    heading(top - BAR_TO_HEAD, "SKILLS")
    row_top = top - BAR_TO_HEAD + HEAD_TO_ROW
    rows = [SKILLS[i : i + SKILLS_PER_ROW] for i in range(0, len(SKILLS), SKILLS_PER_ROW)]
    for index, row_items in enumerate(rows):
        row_y = row_top + index * LEAD
        joined = ", ".join(row_items)
        if pdfmetrics.stringWidth(joined, "Lato", SIZE) > RIGHT - TEXT_X:
            sys.exit(f"Skills row {index + 1} is too wide: {joined!r}")
        c.setFont("Lato-Bold", SIZE)
        c.setFillColor(INK)
        c.drawString(BULLET_X, baseline(row_y), "\u2022")
        text(TEXT_X, row_y, joined)
    anchors["last_row"] = round(row_top + (len(rows) - 1) * LEAD, 2)

    c.showPage()
    c.save()

    if anchors["last_row"] > BOTTOM_LIMIT:
        sys.exit(
            f"Content overflows: the last skills row would sit at {anchors['last_row']:.1f}, "
            f"past the {BOTTOM_LIMIT:.0f} limit. Trim a bullet or a skill."
        )
    print(f"  drew {drawn} text runs")
    return anchors


def verify(path: Path, expected: dict[str, float]) -> list[str]:
    doc = pymupdf.open(path)
    problems: list[str] = []

    if doc.page_count != 1:
        problems.append(f"expected 1 page, got {doc.page_count}")

    text = "".join(page.get_text() for page in doc)
    problems += [f"stale text still present: {t!r}" for t in STALE_TEXT if t in text]

    # Content is checked from the structures above, so adding a bullet or a skill is verified
    # automatically. Wrapped lines are compared whitespace-insensitively.
    flat = re.sub(r"\s+", " ", text)
    problems += [
        f"missing from output: {phrase!r}"
        for phrase in expected_phrases()
        if re.sub(r"\s+", " ", phrase) not in flat
    ]

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


def tidy_fonts(pdf_path: Path) -> None:
    """
    reportlab opens every page with a no-op text object that sets its default font
    (`BT /F1 12 Tf 14.4 TL ET`). Nothing is drawn with it, but the reference keeps unembedded
    Helvetica in the resources, which preflight checks report as an unembedded font. Drop that
    block, then drop whatever font it was the only reference to — checking the names actually
    used rather than assuming, so a real Helvetica would survive.
    """
    doc = pymupdf.open(pdf_path)
    page = doc[0]
    xrefs = page.get_contents()
    if len(xrefs) != 1:
        doc.close()
        return  # not the single stream this script generated; leave it alone

    content = doc.xref_stream(xrefs[0])
    trimmed = re.sub(rb"BT\s*/F\d+\s+[\d.]+ Tf\s*[\d.]+ TL\s*ET\s*", b"", content)
    if trimmed == content:
        doc.close()
        return

    doc.update_stream(xrefs[0], trimmed)
    page = doc[0]
    keep, drop = [], []
    for entry in page.get_fonts(full=True):
        name = entry[4] if entry[4].startswith("/") else f"/{entry[4]}"
        (keep if name.encode() in trimmed else drop).append((name, entry[0]))

    if not drop:
        doc.close()
        return

    # Rebuild the dictionary rather than deleting the key: PyMuPDF cannot leave a hole in an
    # existing dict, and substituting a "null" value writes a placeholder string in its place,
    # which a strict reader would reject as an invalid font.
    doc.xref_set_key(
        page.xref,
        "Resources/Font",
        "<<" + "".join(f"{name} {xref} 0 R" for name, xref in keep) + ">>",
    )

    # PyMuPDF cannot write over the file it has open, so go through a sibling path.
    tmp = pdf_path.with_suffix(".fonts.pdf")
    doc.save(str(tmp))
    doc.close()
    os.replace(tmp, pdf_path)
    print(f"  font resources tidied (dropped: {', '.join(name for name, _ in drop)})")


def main() -> int:
    if not PDF.is_file():
        sys.exit(f"not found: {PDF}")

    with tempfile.TemporaryDirectory() as tmp:
        overlay = Path(tmp) / "overlay.pdf"
        redacted = Path(tmp) / "redacted.pdf"
        output = Path(tmp) / "resume.pdf"

        anchors = draw_page(overlay)
        tidy_fonts(overlay)

        # Remove the original text from the content stream rather than hiding it: every band
        # that holds text is cleared, stepping around the artwork that is kept.
        doc = pymupdf.open(PDF)
        page = doc[0]
        page.add_redact_annot(pymupdf.Rect(*CLEAR_AREA))
        page.apply_redactions()
        doc.save(redacted)
        doc.close()

        # Merge the kept artwork with the freshly drawn page, and describe the file: an ATS
        # shows the title and may index the keywords, and a blank metadata block advertises
        # nothing.
        writer = PdfWriter()
        merged = PdfReader(str(redacted)).pages[0]
        merged.merge_page(PdfReader(str(overlay)).pages[0])
        writer.add_page(merged)
        writer.add_metadata(
            {
                "/Title": "Cody Griffith - Resume",
                "/Author": "Cody Griffith",
                "/Creator": "scripts/build-resume.py",
                "/Subject": "Resume - web developer",
                "/Keywords": (
                    "Web Developer, Front End Developer, React, Next.js, SvelteKit, "
                    "TypeScript, JavaScript, Cloudflare Workers"
                ),
            }
        )
        with open(output, "wb") as handle:
            writer.write(handle)

        problems = verify(
            output,
            {
                "Cody Griffith": anchors["name"],
                "WORK EXPERIENCE": anchors["WORK EXPERIENCE"],
                "EDUCATION": anchors["EDUCATION"],
                "PROJECTS": anchors["PROJECTS"],
                "SKILLS": anchors["SKILLS"],
                PROJECTS[0][0].split(" |")[0] + " |": round(
                    anchors["PROJECTS"] + PROJECT_HEADING_TO_FIRST, 2
                ),
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
    print("  anchors: " + ", ".join(f"{label} {top}" for label, top in anchors.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
