#!/usr/bin/env python3
"""validate_sources.py — assert every cited Recital N and FAQ Qn appears verbatim
in the curated source files.

Usage:
    python3 validate_sources.py            # check; exits non-zero on coverage gap
    python3 validate_sources.py --verbose  # show what was checked
    python3 validate_sources.py --regenerate  # rewrite references/_source-coverage.md
                                              # from a fresh scan of references and templates

Coverage contract:
    - Every `Recital N` cited in references/, assets/templates/, assets/decision-trees/,
      or assets/examples/ must appear as `## Recital N` in
      assets/source/regulation-2023-2854.md.
    - Every `Qn` or `Qna` cited likewise must appear as `## FAQ Qn` (or `## FAQ Qna`)
      in assets/source/faq-v1.4.md.
    - Every `Article N` cited likewise must appear as `## Article N` in the regulation file.

Run before each release. Wire into install.sh --check.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG_FILE = ROOT / "assets" / "source" / "regulation-2023-2854.md"
FAQ_FILE = ROOT / "assets" / "source" / "faq-v1.4.md"
COVERAGE_FILE = ROOT / "references" / "_source-coverage.md"

SCAN_DIRS = [
    ROOT / "references",
    ROOT / "assets" / "templates",
    ROOT / "assets" / "decision-trees",
    ROOT / "assets" / "examples",
]

# Citations we consider Data-Act-internal. Other instruments are ignored.
RECITAL_RE = re.compile(r"\bRecital\s+(\d+)\b")
ARTICLE_RE = re.compile(r"\b(?:Art(?:icle)?\.?)\s+(\d+)\b")
# FAQ Q-numbers: count a Q[N|Na] reference only when the line indicates it is
# really a FAQ citation. Decision-tree step labels (Q1, Q2, Q3) and outline
# numbering use bare Q-numbers without the "FAQ" or "Question" qualifier; we
# intentionally exclude those.
FAQ_BARE_Q_RE = re.compile(r"(?<![A-Za-z])Q\s*(\d+[a-z]?)\b")
# A line is a FAQ-citation context if it mentions FAQ or Commission's FAQ.
FAQ_CONTEXT_RE = re.compile(r"\b(?:FAQ|Commission(?:'s)?\s+FAQ|Question\s+\d)", re.I)

# Headings present in source files
REG_RECITAL_HEADING_RE = re.compile(r"^## Recital (\d+)\s*$", re.M)
REG_ARTICLE_HEADING_RE = re.compile(r"^## Article (\d+)\s*$", re.M)
FAQ_Q_HEADING_RE = re.compile(r"^## FAQ Q(\d+[a-z]?)\s*$", re.M)


def scan_citations():
    recitals: set[int] = set()
    articles: set[int] = set()
    qs: set[str] = set()
    files_scanned = 0
    for d in SCAN_DIRS:
        if not d.exists():
            continue
        for p in d.rglob("*.md"):
            # Skip the coverage manifest itself and any hidden / draft files
            if p.name.startswith("_source-coverage"):
                continue
            text = p.read_text()
            files_scanned += 1
            for m in RECITAL_RE.finditer(text):
                recitals.add(int(m.group(1)))
            for m in ARTICLE_RE.finditer(text):
                # Restrict articles to plausible Data Act range (1-50). The
                # references also cite GDPR Art. 6, Art. 15 etc., which we
                # intentionally do not check (out of scope of this skill).
                # We rely on context: if `Reg. Art. N` or `Art. N` of the
                # Data Act, N is in 1..50. We still check 1..50 only.
                n = int(m.group(1))
                if 1 <= n <= 50:
                    articles.add(n)
            # Walk line by line. A line is a FAQ-citation context if it
            # mentions FAQ explicitly. On such lines, count every Q[N|Na].
            # On other lines, only count letter-suffixed Q[Na] (sub-numbered
            # questions like Q22a never appear as decision-tree step labels).
            for line in text.splitlines():
                is_faq_line = bool(FAQ_CONTEXT_RE.search(line))
                for m in FAQ_BARE_Q_RE.finditer(line):
                    token = m.group(1).lower()
                    if is_faq_line or any(ch.isalpha() for ch in token):
                        qs.add(token)
    return recitals, articles, qs, files_scanned


def headings_in_file(path: Path, regex: re.Pattern):
    if not path.exists():
        return set()
    text = path.read_text()
    return {m.group(1).lower() if isinstance(m.group(1), str) and m.group(1)[-1].isalpha()
            else int(m.group(1))
            for m in regex.finditer(text)}


def regenerate_coverage(recitals, articles, qs):
    lines = [
        "# Source coverage — required provisions",
        "",
        "This file is the source-coverage contract. **Every Recital number and FAQ Q-number listed below must appear as a heading in the curated source files.** `scripts/validate_sources.py` enforces this. If validation fails, the skill is not safe to release until the missing provision is added.",
        "",
        "The list is derived by grepping `references/*.md`, `assets/templates/*.md`, `assets/decision-trees/*.md`, and `assets/examples/*.md` for `Recital N` and `Q[N|Na]` citations. Re-run `scripts/validate_sources.py --regenerate` to refresh this list whenever references are edited.",
        "",
        "## Required recitals (must appear as `## Recital N` in `assets/source/regulation-2023-2854.md`)",
        "",
    ]
    for n in sorted(recitals):
        lines.append(f"- {n}")
    lines.append("")
    lines.append("## Required FAQ questions (must appear as `## FAQ Q[N|Na]` in `assets/source/faq-v1.4.md`)")
    lines.append("")

    def faq_sort(k):
        m = re.match(r"^(\d+)([a-z]?)$", k)
        return (int(m.group(1)), m.group(2))

    for q in sorted(qs, key=faq_sort):
        lines.append(f"- {q}")
    lines.append("")
    lines.append("## Required articles (must appear as `## Article N` in `assets/source/regulation-2023-2854.md`)")
    lines.append("")
    lines.append("All articles 1 through 50 are bundled. The articles cited materially across references and templates are: " +
                 ", ".join(str(n) for n in sorted(articles)) + ".")
    lines.append("")
    lines.append("## Out-of-scope citations (intentionally not bundled here)")
    lines.append("")
    lines.append("GDPR / DMA / Trade Secrets Directive / sectoral instruments are referenced but not bundled. The validate script does not check coverage of these because the skill is intentionally horizontal-only on the Data Act.")
    COVERAGE_FILE.write_text("\n".join(lines))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--regenerate", action="store_true",
                    help="Rewrite references/_source-coverage.md from a fresh scan, then validate.")
    args = ap.parse_args()

    cited_recitals, cited_articles, cited_qs, files_scanned = scan_citations()

    if args.regenerate:
        regenerate_coverage(cited_recitals, cited_articles, cited_qs)
        print(f"Regenerated {COVERAGE_FILE}")

    if args.verbose:
        print(f"Scanned {files_scanned} markdown files")
        print(f"Cited recitals: {sorted(cited_recitals)}")
        print(f"Cited Data Act articles: {sorted(cited_articles)}")
        print(f"Cited FAQ Q-numbers: {sorted(cited_qs)}")

    # Headings present in source files
    reg_text = REG_FILE.read_text() if REG_FILE.exists() else ""
    faq_text = FAQ_FILE.read_text() if FAQ_FILE.exists() else ""
    present_recitals = {int(m.group(1)) for m in REG_RECITAL_HEADING_RE.finditer(reg_text)}
    present_articles = {int(m.group(1)) for m in REG_ARTICLE_HEADING_RE.finditer(reg_text)}
    present_qs = {m.group(1).lower() for m in FAQ_Q_HEADING_RE.finditer(faq_text)}

    missing_recitals = cited_recitals - present_recitals
    missing_articles = cited_articles - present_articles
    missing_qs = cited_qs - present_qs

    failed = False
    if missing_recitals:
        failed = True
        print(f"FAIL: Recitals cited but not present in {REG_FILE.name}:")
        for n in sorted(missing_recitals):
            print(f"  - Recital {n}")
    if missing_articles:
        failed = True
        print(f"FAIL: Articles cited but not present in {REG_FILE.name}:")
        for n in sorted(missing_articles):
            print(f"  - Article {n}")
    if missing_qs:
        failed = True
        print(f"FAIL: FAQ Q-numbers cited but not present in {FAQ_FILE.name}:")
        for q in sorted(missing_qs, key=lambda k: (int(re.match(r'^(\d+)', k).group(1)), k)):
            print(f"  - FAQ Q{q}")

    if failed:
        print()
        print("Coverage gap detected. The skill is not safe to release until the missing provisions are added to the curated source files.")
        sys.exit(1)
    print(f"OK — all cited provisions present.")
    print(f"  Recitals: {len(cited_recitals)} cited, all present")
    print(f"  Articles: {len(cited_articles)} cited (range 1..50), all present")
    print(f"  FAQ Qs:   {len(cited_qs)} cited, all present")


if __name__ == "__main__":
    main()
