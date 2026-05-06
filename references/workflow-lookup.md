# Workflow — Lookup

Mode 3. The lawyer wants a verbatim quotation, an article citation, a deadline, or a cross-reference.

## Inputs expected

- A specific article number ("Art. 25(2)(a)"), recital number ("Recital 31"), or FAQ question ("Q22a"), OR
- A topical query ("what is the deadline for switching charges?"), OR
- A definition request ("what does 'exportable data' mean?")

## Procedure

1. **Identify the source.** Determine whether the answer is in:
   - The regulation (`assets/source/regulation-2023-2854.md`) — verbatim
   - The FAQ (`assets/source/faq-v1.4.md`) — verbatim
   - "Data Act Explained" page (`assets/source/data-act-explained.md`) — snapshot
   - The Commission Recommendation on SCCs (`assets/source/model-contractual-terms.md`) — **pointer only**; for clause-text lookups, redirect the lawyer to the Commission's PDF at `https://digital-strategy.ec.europa.eu/en/library/standard-contractual-clauses-data-sharing-and-cloud-computing-contracts`. Do not fabricate verbatim SCC clause text.

2. **Read the relevant section** from the source file. Do NOT paraphrase from training data.

3. **Cross-reference.** For any provision the user asked about, identify:
   - Related articles within the regulation (e.g., Art. 25(2)(a) → Art. 23, Art. 24, Art. 30, Art. 50)
   - Related recitals (e.g., Art. 4(8) → Recital 31)
   - Related FAQ questions (e.g., Art. 25 → FAQ Q56)

4. **Check `references/gotchas.md`** for known confusion points (e.g., the Art. 31 vs Art. 32 numbering, the Art. 2 (30)/(32)/(34)/(37)/(38) trap).

5. **Apply citation style** per `references/citation-style.md`.

6. **Answer in chat first**, per `SKILL.md` step 8. After the chat answer, **offer Word export** per `SKILL.md` step 9. Do not auto-render. Lookups are short by definition; the chat answer is often enough, and the Word offer lets the lawyer pick.

## Output structure

```
1. Title — what was looked up.
2. Verbatim quotation — exact text from source, in quotation marks, with article/recital/Q reference.
3. Cross-references — bulleted list of related provisions and FAQ questions.
4. Brief practical note — one paragraph maximum on what the provision means in practice. Hedged.
5. FAQ context — if any FAQ question elaborates, the elaboration is quoted here, with the "non-authoritative" framing.
6. Disclaimer.
```

## Length

A standard lookup is one page. If the lawyer asked a topical question that touches multiple provisions, the lookup may run to two pages with cross-references.

If the topical question is too broad to answer with a lookup (e.g., "tell me everything about trade secrets"), suggest the lawyer use **analyze** mode instead.

## What lookup mode does NOT do

- Apply law to facts. That is `analyze` mode.
- Draft anything. That is `draft` mode.
- Issue conclusions on contested interpretive questions. State both views with citations.

## Verbatim discipline

The reason this skill exists (in part) is to give lawyers a reliable verbatim citation tool. The model must NEVER reproduce regulation text from training data. Always read from `assets/source/*` and quote directly.

If the source file does not contain the requested text (because the v1 release ships a partial extract), the skill says so and points the lawyer to the canonical EUR-Lex URL:

> "The bundled source extract does not include this provision verbatim. Consult the consolidated text at https://eur-lex.europa.eu/eli/reg/2023/2854 for the authoritative text."

## Common lookup pitfalls

- Citing Art. 2(30) as "switching" (it is "customer"; switching is at 2(34)).
- Citing Art. 31 for international access (it is the lighter regime; international access is at Art. 32).
- Citing GDPR-equivalent timelines for Art. 4 ("one month" — the Data Act says "without undue delay").
- Treating an FAQ answer as the legal answer rather than the Commission's interpretation.
