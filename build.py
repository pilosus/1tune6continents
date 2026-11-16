#!/usr/bin/env python3
"""Assemble the static pages from _parts/. Run after editing anything in _parts/."""
from pathlib import Path

ROOT = Path(__file__).parent
PARTS = ROOT / "_parts"
NAV_KEYS = ["HOME", "PROJECT", "INST", "CONTACT"]

PAGES = [
    ("index.html", "1 TUNE and 6 CONTINENTS",
     "A nonprofit music project: leading musicians from six continents interpret one tune, then young musicians worldwide join in.",
     "HOME", "index.body.html"),
    ("current-project.html", "Current project: ΑΕΩΝ Tango | 1 TUNE and 6 CONTINENTS",
     "The first collaboration: a tango by Paul Vigrass interpreted by musicians from six continents.",
     "PROJECT", "project.body.html"),
    ("music-institutions.html", "Music institutions | 1 TUNE and 6 CONTINENTS",
     "An invitation to musical and educational institutions to join the all-join-in medley.",
     "INST", "institutions.body.html"),
    ("contact.html", "Contact | 1 TUNE and 6 CONTINENTS",
     "Get in touch to play as a lead musician, join the medley, or support the project.",
     "CONTACT", "contact.body.html"),
]

head = (PARTS / "head.html").read_text()
foot = (PARTS / "foot.html").read_text()
for out, title, desc, current, body in PAGES:
    html = head.replace("__TITLE__", title).replace("__DESC__", desc)
    for key in NAV_KEYS:
        html = html.replace(f"__CUR_{key}__", ' aria-current="page"' if key == current else "")
    html += (PARTS / body).read_text() + foot
    (ROOT / out).write_text(html)
    print("built", out)
