# Source coverage — required provisions

This file is the source-coverage contract. **Every Recital number and FAQ Q-number listed below must appear as a heading in the curated source files.** `scripts/validate_sources.py` enforces this. If validation fails, the skill is not safe to release until the missing provision is added.

The list is derived by grepping `references/*.md`, `assets/templates/*.md`, `assets/decision-trees/*.md`, and `assets/examples/*.md` for `Recital N` and `Q[N|Na]` citations. Re-run `scripts/validate_sources.py --regenerate` to refresh this list whenever references are edited.

## Required recitals (must appear as `## Recital N` in `assets/source/regulation-2023-2854.md`)

- 7
- 17
- 21
- 30
- 31
- 81

## Required FAQ questions (must appear as `## FAQ Q[N|Na]` in `assets/source/faq-v1.4.md`)

- 4
- 5
- 7
- 10
- 14
- 16
- 20
- 22
- 22a
- 25a
- 25b
- 31
- 56
- 58a

## Required articles (must appear as `## Article N` in `assets/source/regulation-2023-2854.md`)

All articles 1 through 50 are bundled. The articles cited materially across references and templates are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 20, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 35, 37, 38, 39, 40, 49, 50.

## Out-of-scope citations (intentionally not bundled here)

GDPR / DMA / Trade Secrets Directive / sectoral instruments are referenced but not bundled. The validate script does not check coverage of these because the skill is intentionally horizontal-only on the Data Act.