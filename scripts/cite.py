#!/usr/bin/env python3
"""cite.py — verbatim citation lookup tool.

Usage:
    python3 cite.py "Art. 25(2)(a)"
    python3 cite.py "Article 50"
    python3 cite.py "Recital 31"
    python3 cite.py "FAQ Q22a"

Looks up the requested provision in the Skill's bundled source files
(`assets/source/regulation-2023-2854.md` and `assets/source/faq-v1.4.md`)
and prints the verbatim text plus cross-references.

The Skill itself uses this script to enforce the citation discipline:
verbatim text comes from the source files, never from training data.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG_FILE = ROOT / "assets" / "source" / "regulation-2023-2854.md"
FAQ_FILE = ROOT / "assets" / "source" / "faq-v1.4.md"


def normalise_query(q: str) -> tuple[str, str]:
    """Return (kind, normalised) where kind ∈ {article, recital, faq}."""
    q = q.strip()
    # Recital
    m = re.match(r"(?:reg\.?\s*)?recital\s*(\d+)", q, re.I)
    if m:
        return ("recital", m.group(1))
    # FAQ
    m = re.match(r"(?:ec\s+)?faq\s*q?\s*(\d+[a-z]?)", q, re.I)
    if m:
        return ("faq", m.group(1).lower())
    # Article
    m = re.match(r"(?:reg\.?\s*)?(?:art(?:icle)?\.?)\s*(\d+)(.*)", q, re.I)
    if m:
        num = m.group(1)
        rest = m.group(2).strip()
        return ("article", num + rest)
    # Bare number?
    m = re.match(r"^(\d+)(.*)$", q)
    if m:
        return ("article", q)
    raise ValueError(f"Unrecognised query: {q!r}")


def find_article(num_with_subpoints: str) -> str:
    """Locate `## Article N` in the regulation file and return its body.

    Sub-points like (2)(a) are not separate headings in the verbatim source —
    Article 25(2)(a) lives inside the body of Article 25. We return the full
    Article and (where a sub-point was requested) also surface the matching
    paragraph as a hint.
    """
    if not REG_FILE.exists():
        return f"[regulation source not found at {REG_FILE}]"
    text = REG_FILE.read_text()
    m = re.match(r"(\d+)(.*)", num_with_subpoints)
    if not m:
        return f"[malformed article reference: {num_with_subpoints!r}]"
    base = m.group(1)
    rest = m.group(2).strip()
    # Find the verbatim block. Heading is "## Article {base}" on its own line.
    pattern = re.compile(
        rf"^## Article {base}\s*$.*?(?=^## Article \d+\s*$|^# |\Z)",
        re.S | re.M,
    )
    m_block = pattern.search(text)
    if not m_block:
        return f"[Article {base} not found in bundled source. Consult EUR-Lex.]"
    section = m_block.group(0).strip()
    if not rest:
        return section
    # Surface the matching sub-paragraph if the lawyer asked for a sub-point.
    # Sub-points are written inline as e.g. "(2) ..." or "(a) ..." or "1." in
    # the verbatim text. Look for a quoted line beginning with the sub-marker.
    needle = rest.lstrip("()").rstrip(")")
    # First try exact whole sub-point match like "(2)(a)" or paragraph "(1)"
    para_pattern = re.compile(
        rf"^>\s*{re.escape(rest)}\b.*?(?=^>\s*\([0-9a-z]+\)|^>\s*\d+\.\s|^## |\Z)",
        re.S | re.M,
    )
    p = para_pattern.search(section)
    if p:
        return f"## Article {base}{rest}\n\n{p.group(0).strip()}\n\n[Surrounding article shown above; full text above.]"
    # Fall back to returning the full article (the lawyer can scroll).
    return section


def find_recital(num: str) -> str:
    if not REG_FILE.exists():
        return f"[regulation source not found at {REG_FILE}]"
    text = REG_FILE.read_text()
    pattern = re.compile(
        rf"^## Recital {num}\s*$.*?(?=^## Recital \d+\s*$|^# |^---\s*$|\Z)",
        re.S | re.M,
    )
    m = pattern.search(text)
    if m:
        return m.group(0).strip()
    return f"[Recital {num} not found in bundled source. Consult EUR-Lex.]"


def find_faq(qnum: str) -> str:
    if not FAQ_FILE.exists():
        return f"[FAQ source not found at {FAQ_FILE}]"
    text = FAQ_FILE.read_text()
    pattern = re.compile(
        rf"^## FAQ Q{qnum}\s*$.*?(?=^## FAQ Q\d|^# |^---\s*$|\Z)",
        re.S | re.M | re.I,
    )
    m = pattern.search(text)
    if m:
        return (
            m.group(0).strip()
            + "\n\n[Reminder: the FAQ is non-authoritative; cite as 'the Commission's interpretation, not binding'.]"
        )
    return f"[FAQ Q{qnum} not found in bundled source. Consult the FAQ canonical URL.]"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("query", nargs="+", help="Provision to look up (e.g. 'Art. 25(2)(a)', 'Recital 31', 'FAQ Q22a')")
    args = parser.parse_args()
    query = " ".join(args.query)
    try:
        kind, norm = normalise_query(query)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)
    if kind == "article":
        print(find_article(norm))
    elif kind == "recital":
        print(find_recital(norm))
    elif kind == "faq":
        print(find_faq(norm))


if __name__ == "__main__":
    main()
