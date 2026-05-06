# Workflow — Analyze

Mode 4. The lawyer wants legal analysis applying the regulation to facts.

## Inputs expected

- A factual matrix (real or hypothetical).
- A question or set of questions.
- Side advised.

## Procedure

1. **Capture per-matter facts** per `references/per-matter-facts.md`. Confirm with the lawyer before proceeding.

2. **Sectoral overlay gate.** Surface any applicable warnings before substantive analysis.

3. **Identify the issues.** Reduce the question to legally distinct issues. Number them. Common issue patterns:
   - Classification → see `workflow-classify.md`
   - Scope of access right (what data, who can request)
   - Refusal grounds (trade-secret ladder; safety/security carve-out)
   - GDPR overlay (user is / is not data subject)
   - DPS contract compliance
   - International access posture
   - Timeline / applicability of obligations

4. **Read** the relevant reference file(s) for each issue:
   - `references/chapter-2-access.md`
   - `references/chapter-6-dps.md`
   - `references/trade-secret-ladder.md`
   - `references/safety-security.md`
   - `references/gdpr-overlay.md`
   - `references/international-access.md`
   - `references/timeline.md`
   - `references/often-missed.md`
   - `references/enforcement.md`

5. **Read verbatim source** for any provision quoted or substantially relied upon. Quote in the output.

6. **Apply the framework.** For each issue:
   - State the rule (regulation provision + recital interpretive aid + FAQ if relevant, framed non-authoritatively).
   - State the facts as understood.
   - Apply the rule to the facts.
   - State the conclusion with appropriate hedging.
   - Identify any factual gaps that change the answer.

7. **Read** `references/gotchas.md` and verify the analysis does not trigger a known failure mode.

8. **Render to Word** via `scripts/render_docx.py`.

## Memo structure (target output)

```
1. Bottom line — one sentence per issue.
2. Issues — numbered, in order analysed.
3. Per issue:
   3.1 Rule
   3.2 Facts assumed
   3.3 Application
   3.4 Conclusion
   3.5 Open questions / facts that would change the answer
4. Cross-issue interactions (if any).
5. Sectoral / member-state overlays (if any).
6. Recommended next steps.
7. Defined terms.
8. Sources.
9. Disclaimer.
```

## Length

Three to six pages typical. If longer, split into a memo plus an annex (worked examples, full citations, draft clauses).

## Hedging requirements

The analysis must hedge where the law hedges. Examples of correct framing:

- "The better view is that…"
- "On the current state of the FAQ (non-authoritative), …"
- "Subject to sectoral overlays not addressed here, …"
- "Pending member-state implementing measures, …"
- "On the facts as currently understood, …"

Examples of incorrect framing (overconfident):
- "The Data Act requires the data holder to…" without subsection citation.
- "The Commission has decided that…" (the FAQ does not decide).
- "The deadline is X days" without citing the source.

## Where to push back

If the lawyer's question contains a presupposition that the analysis cannot support, the analysis says so explicitly. Examples:

- Question: "Can my client refuse this access request on trade-secret grounds because the data is sensitive?"
- Pushback: The analysis explains that "sensitive" alone does not establish trade-secret status, and walks the three-step ladder. It identifies what additional facts would support a defensible refusal.

## Where to acknowledge limits

The analysis explicitly identifies:
- Facts the lawyer should obtain to firm up the answer.
- Sectoral overlays not covered by the skill.
- Member-state implementing law not covered by the skill.
- Contested interpretive points where the FAQ has not addressed the question.
- Risk that the FAQ may be revised.

## Common analysis errors

- Assuming the Data Act provides a GDPR Article 6 legal basis when the user is not the data subject (it does not — Recital 7).
- Treating refusal as the default; it is the exception.
- Importing GDPR's one-month deadline as the Data Act's deadline.
- Applying functional equivalence (Art. 30(1)) to a SaaS analysis.
- Treating a multi-tenant SaaS as Art. 31(1) custom-built.
- Failing to consider Art. 4(13) when analysing data-holder use of customer data.
