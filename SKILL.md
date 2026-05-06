---
name: data-act
description: EU Data Act (Regulation (EU) 2023/2854) skill for lawyers. Use when the user asks about Data Act classification, drafting, lookup, analysis, or audit. Triggers include "Data Act", "Regulation 2023/2854", "connected product", "related service", "data processing service", "DPS switching", "Article 3(2) pre-contract", "Article 25 contract", "trade-secret handbrake", "international government access", "Chapter VI cloud switching", "Article 50 timeline", "FAQ Q22a", "data holder", "exportable data", "functional equivalence", "Art. 4(10) competing product", and similar EU Data Act phrases. The skill produces lawyer-style Word output and cites verbatim from bundled regulation and FAQ source texts.
---

# Data Act — Orchestrator

Skill for in-house counsel and external practitioners advising on the EU Data Act (Regulation (EU) 2023/2854). Produces classification memos, drafting starters, regulation lookups, legal analyses, and gap-analysis audits.

This file is the orchestrator only. It contains no rules, no examples, no content. Each step below points to the file Claude reads at that step. Read each pointed-to file before doing the work in that step.

## Workflow

1. **Mode detection.** Identify which mode the user is in:
   - **classify** — "is this offering a connected product / related service / DPS / overlap?"
   - **draft** — "draft me a [pre-contract disclosure / DPS clause / refusal letter / etc.]"
   - **lookup** — "what does Article X say?" or "what's the deadline for Y?"
   - **analyze** — "can my client refuse on trade-secret grounds here?"
   - **audit** — "compare this offering against the regulation"

   If the user's intent is unclear, ask which mode applies before proceeding. Do not guess. Use the inline A/B/C/D format defined in `references/asking-questions.md`.

   If the lawyer picks more than one mode, treat them as a combined deliverable. Order: classify → analyze → draft → audit → lookup. Skip any not requested.

2. **Per-matter facts.** Read `references/per-matter-facts.md` AND `references/asking-questions.md`. All clarifying questions to the lawyer must use the inline A/B/C/D format defined in `references/asking-questions.md`. Capture:
   - Side advised (data holder / user / third party / unclear-and-need-to-ask)
   - Sector indicators present in the facts (none / automotive / medical / financial / NIS2-essential / AI Act / multiple)
   - Member state(s) involved

3. **Sectoral overlay gate.** Read `references/sectoral-overlays.md`. If any sector indicator was captured at step 2, surface the overlay warning before any output. The skill does not cover sectoral lex specialis; the lawyer must independently verify.

4. **Scope confirmation.** Before drafting, state in 2 to 3 sentences which sections will appear, approximate density, and what is intentionally excluded. Wait for confirmation or amendment. This avoids producing a 9-page memo when 3 pages would do. For lookup mode and single-paragraph answers, this step is a no-op.

5. **Mode workflow (mandatory read).** Before continuing, read `references/workflow-{mode}.md` in full for each mode in the combined deliverable, in the order from step 1. Do not proceed to step 6 without having read every applicable workflow file. These files contain operative procedure (decision trees, carve-outs, common errors, push-back triggers) that is not in this orchestrator. Skipping them produces incomplete or incorrect outputs.

6. **Verbatim source quoting.** Whenever the workflow requires regulation, recital, or FAQ text, read it from `assets/source/regulation-2023-2854.md` (Articles 1–50 and Recitals 1–119) or `assets/source/faq-v1.4.md` (FAQ Q1–Q74 incl. sub-questions). Both files contain unabridged verbatim quotations indexed by `## Article N`, `## Recital N`, or `## FAQ Q[N|Na]` headings. Cite using `references/citation-style.md`.

   **Never paraphrase from memory.** If a needed Article, Recital, or FAQ Q-number is not present in the curated source files, **stop and report a skill defect** rather than answering without source. Output something like: "I cannot complete this answer because [Recital N | FAQ Q[N]] is not present in the bundled verbatim source. This is a skill coverage defect. The maintainer should re-run `scripts/validate_sources.py` against the current EUR-Lex / FAQ versions and add the missing provision before this answer can be relied upon." Falling back to general knowledge of the regulation is not acceptable for a legal-drafting skill.

7. **Gotchas check.** Before producing the final output, read `references/gotchas.md` and verify the output does not trigger a known failure mode.

8. **Answer in chat.** Produce the deliverable directly in the chat with structured headings, numbered paragraphs, verbatim citations from `assets/source/*`, defined terms used consistently, and a numbered "Open questions" section at the end if any unresolved issue surfaced. Apply the typography non-negotiables stated in this orchestrator. Use markdown formatting for in-chat presentation. Append the short disclaimer from `references/disclaimer-short.md` to the bottom of the chat answer.

9. **Offer Word export.** After the chat answer, offer Word export using the inline A/B/C/D format from `references/asking-questions.md`:

    ```
    **Export this to Word?**

      A) **Yes — save to current folder** ({cwd}/Data Act outputs/) *(Recommended)*
      B) Yes — save to Desktop (~/Desktop/Data Act outputs/)
      C) Yes — save to a custom path (specify)
      D) No — chat answer is enough

    Reply A / B / C / D.
    ```

    If the lawyer's `config.json` already has `output_dir` set to `cwd`, `desktop`, or a custom path, skip this prompt and use that preference. The first export in a session that uses the default may also offer a fourth option ("Always use this folder, don't ask again") which sets `output_dir` via `scripts/render_docx.py --set-output ...`.

    On approval, render via `scripts/render_docx.py --template <md> --deliverable-type <type>`. The script handles disclaimer append, output-path resolution, and pandoc invocation. Print the absolute path AND the `file://` URI so the chat hyperlinks it.

## File map

```
SKILL.md                       — this orchestrator
LICENSE                        — AGPL-3.0 + legal-advice disclaimer
README.md                      — install, scope, attribution
CHANGELOG.md                   — version-only entries
install.sh                     — one-command install for Claude Code
config.json                    — output_dir preference (cwd / desktop / custom path)
commands/data-act.md           — slash-command definition (/data-act)
references/                    — knowledge layer (read on demand)
assets/source/                 — verbatim source texts (regulation, FAQ); structured pointer for the Commission Recommendation (SCCs)
assets/templates/              — drafting starters (markdown; Word-on-request via render_docx.py)
assets/styles/                 — lawyer-reference.docx (pandoc reference template for Word styling)
assets/decision-trees/         — walkable Q&A scripts
assets/examples/               — annotated worked examples
scripts/                       — Python helpers (cite, render_docx [pandoc], timeline_check, validate_sources)
```

## Non-negotiables

- The Commission FAQ is not authoritative. Always frame it as "the Commission's interpretation, not binding."
- The skill does not produce legal advice. It produces drafts the lawyer reviews.
- Sectoral lex specialis and member-state implementing law are out of scope. The skill flags but does not cover them.
- Citations must be verbatim from `assets/source/*`. Paraphrase from memory is forbidden.
- Default output is the chat itself. Word is an explicit follow-up artifact offered after the chat answer when the lawyer wants something to save or send. Either way, the deliverable must cite verbatim from `assets/source/*`.
- Word output goes to the lawyer's current working directory under `Data Act outputs/` by default. NEVER write deliverables inside the skill folder.
- **Typography (no exceptions).** Never use em-dashes in any output Claude produces, including chat answers, Word memos, templates, presenter notes, table cells, and titles. Use a comma, colon, semicolon, parentheses, or sentence break instead. Em-dashes are preserved only inside verbatim quotations from the regulation, FAQ, or other source material. The same ban applies to "Furthermore", "Moreover", "Indeed", "It should be noted", restated-question openers, and doubled hedges; these never appear in generated prose.
- **Static-snapshot disclosure (no exceptions).** This skill is a versioned static snapshot. It does not auto-update on the lawyer's machine. Every output (chat answer or Word memo, even one-paragraph lookups) must end with the two-paragraph staleness-and-disclaimer block from `references/disclaimer-short.md`, with the FAQ version and verified-as-of date substituted from `assets/source/_versions.json`. The staleness paragraph and the live EUR-Lex / EC FAQ URLs are the lawyer's primary signal that they may be working from outdated sources. Never omit, paraphrase, or summarise this block.
