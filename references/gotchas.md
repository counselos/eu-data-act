# Gotchas

High-signal failure modes the skill must guard against. This is the first reference file Claude reads before producing any output. Update as new failure modes are observed.

---

## 0a. Templates are filled, not rewritten

When customising a template from `assets/templates/`, replace `[INSERT — ...]` markers and add matter-specific paragraphs at marked extension points. Do not regenerate sections that already exist. Rewriting templates breaks consistency across matters and burns tokens.

## 0b. Density before length

Length budgets are advisory. Density is the rule: every paragraph must do work the previous paragraph didn't.

## 0c. Demote to lookup when the question is narrow

A request like "what's the timing?" wants a paragraph plus a date table, not a memo subsection. If the question is single-issue and answerable in under 250 words, demote to lookup mode regardless of the mode the lawyer initially picked.

## 1. Article 2 numbering trap

The numbering inside Article 2 is non-obvious. These five definitions are commonly miscited:

- **(30) "customer"** — NOT switching, NOT exportable data
- **(32) "digital assets"** — NOT exportable data
- **(34) "switching"** — the actual switching definition
- **(37) "functional equivalence"**
- **(38) "exportable data"** — for the purpose of Articles 23 to 31 and Article 35

Always verify the point number against `assets/source/regulation-2023-2854.md` before citing.

## 2. Article 31 vs Article 32 confusion

These articles are easy to swap because they sound related and are adjacent:

- **Article 31** — "Specific regime for certain data processing services" — the lighter regime for custom-built and non-production test/beta DPS.
- **Article 32** — "International governmental access and transfer" — the third-country access regime for non-personal data.

When the user says "the cloud third-country access article," they mean 32, not 31.

## 3. Functional equivalence is IaaS-only

Article 30 splits its obligations:

- **30(1) functional equivalence** — applies only to IaaS (services limited to infrastructural elements without operating services / software / applications).
- **30(2) open interfaces** — applies to PaaS and SaaS.
- **30(3) interoperability standards** — applies to PaaS and SaaS, with a 12-month compatibility horizon after standards are published.

A common error is asserting SaaS providers owe functional equivalence. They do not. (FAQ Q58a.)

## 4. The DPS time windows are three distinct periods

Lawyers and engineers routinely conflate these:

- **Notice period** — ≤ 2 months from the customer's switching request (Art. 25(2)(d)).
- **Mandatory transitional period** — 30 calendar days, starting *after* the notice period ends (Art. 25(2)(a)).
- **Minimum retrieval period** — ≥ 30 calendar days, starting after the transitional period ends (Art. 25(2)(g)).

Plus the technical-infeasibility extension: provider must justify in writing within **14 working days** of the request; alternative transitional period ≤ **7 months** (Art. 25(4)). And the customer's right to extend the transitional period once (Art. 25(5)).

## 5. Reduced switching charges window closes 12 January 2027 (not 2025)

- **11 January 2024 → 12 January 2027** — reduced switching charges allowed; cannot exceed direct switching cost (Art. 29(2)).
- **From 12 January 2027** — no switching charges for the switching process at all (Art. 29(1)).

Standard service fees and early-termination penalties remain permitted in either window.

## 6. Article 50 has four dates, not three

- **12 September 2025** — general application; Chapter II live; Chapter VI applies in full to all DPS contracts (new and pre-existing), with no grandfather; Chapter IV applies to B2B data-sharing contracts concluded after this date.
- **12 September 2026** — Article 3(1) "by design" applies to connected products and related services placed on the market *after* this date.
- **12 January 2027** — no DPS switching charges (per Art. 29(1)).
- **12 September 2027** — Chapter IV only. Chapter IV applies to pre-existing B2B data-sharing contracts (concluded on or before 12 September 2025) that are of indefinite duration OR due to expire ≥ 10 years from 11 January 2024. This grandfather does NOT extend any Chapter VI deadline.

Missing the 12 September 2027 date is a frequent error for long-running B2B data-sharing contracts. Applying it to Chapter VI DPS switching obligations is also wrong.

## 7. Article 3(1) does NOT mandate direct access for everything

Article 3(1) requires direct access "where relevant and technically feasible." The Commission's FAQ Q22 confirms this gives the manufacturer significant discretion. Indirect access on a simple electronic request (Art. 4(1)) is sufficient where direct is not chosen or not feasible. Stating that direct access is mandatory is wrong.

## 8. Data Act is NOT a GDPR Article 6 legal basis

When the user (in the Data Act sense) is not the data subject, the Data Act does not provide a GDPR Article 6 legal basis for disclosing personal data (Recital 7; FAQ Q25a). The data holder must establish a basis separately or anonymise the data. This applies in the common employer-requesting-employee-data scenario.

## 9. Article 1(5) — GDPR prevails

In any conflict between the Data Act and the GDPR concerning personal data, the GDPR prevails. Outputs that treat the Data Act as overriding GDPR are wrong.

## 10. Trade-secret refusal is a three-step ladder

Refusal on trade-secret grounds is exceptional. The default is disclosure with confidentiality measures.

1. **Article 4(6)** — identify trade secrets, mark in metadata, agree proportionate technical and organisational measures. Default: disclose.
2. **Article 4(7)** — withhold or suspend if no agreement or if user fails to implement / undermines confidentiality. Substantiated in writing; notify competent authority.
3. **Article 4(8)** — exceptional case-by-case refusal where the trade-secret holder demonstrates highly likely "serious economic damage" (Recital 31 defines this as "serious *and irreparable* economic loss"), based on objective elements: enforceability in third countries, level of confidentiality, uniqueness/novelty, cybersecurity impact.

Articles 5(9) to 5(11) mirror this for third-party requests. Skipping straight to refusal without first attempting Step 1 is procedurally defective.

## 11. The Commission FAQ is not authoritative

Outputs must frame any reliance on the FAQ as "the Commission's interpretation, not binding." The FAQ itself states this on its first pages.

## 12. Article 5(3) — DMA gatekeepers are excluded as third parties

Undertakings designated as gatekeepers under Regulation 2022/1925 cannot be eligible third parties under Article 5. They cannot solicit or commercially incentivise data sharing, and the data holder is not required to ship data to them on user request. Easy to miss and may matter in B2B engagements.

## 13. Article 4(10) — user non-compete and no insights about the manufacturer

The user may not use the data to develop a connected product that competes with the one the data came from, share with a third party with that intent, or derive insights about the manufacturer's economic situation, assets, or production methods. This protects the data holder side and is often forgotten when drafting access flows.

## 14. Article 4(13) — data holder needs a contract to use non-personal data

A data holder may use readily available non-personal data only on the basis of a contract with the user, and may not derive insights about the user's economic situation that could undermine the user's commercial position. Internal product analytics drawn from customer telemetry need a contractual basis — they are not implicit from the sale.

## 15. Sectoral lex specialis may pre-empt or override

The Data Act is horizontal. Sectoral instruments — Reg. 2018/858 (motor vehicles), Reg. 2017/745 (medical devices), DORA (Reg. 2022/2554), NIS2 (Dir. 2022/2555), the AI Act (Reg. 2024/1689), and others — may impose stricter, additional, or alternative obligations. The skill flags but does not cover sectoral overlays. Always check.

## 16. Member-state implementing law and competent authority vary

Article 37 designates competent authorities at member-state level. Each member state may also adopt implementing measures. The skill points to Art. 37 and the Commission's published list; it does not enumerate national designations.

## 17. "Without undue delay" has no numeric SLA

The Regulation does not set a numeric time limit for Chapter II responses. Recital 21 and FAQ Q22a require proactive automation. Outputs that quote a specific number of days as "the Article 4 deadline" are wrong; the right answer is "without undue delay, with proactive automation expected."

## 18. Prototypes are out of scope (FAQ Q7), but "early-stage commercial product" is not

Only un-finalised prototypes that have not completed manufacturing are out of scope under FAQ Q7. A first commercial release is in scope.

## 19. "Customised tenant" ≠ "custom-built service" under Art. 31(1)

A multi-tenant SaaS with customer-specific configuration is not "custom-built" under Article 31(1). Custom-built means the engineering effort is uniquely for that one customer and the service is not offered at broad commercial scale via the catalogue.

## 20. Word is the durable artifact, offered after the chat answer

The chat answer is the default deliverable (per orchestrator step 8). After the chat answer, offer Word export (per orchestrator step 9). Word is rendered via `scripts/render_docx.py`. Do not produce raw markdown as a deliverable — the lawyer cannot edit or send markdown. If the lawyer declines the Word offer, the chat answer stands. If the lawyer accepts, render to .docx and print the absolute path. Markdown in `assets/templates/` is internal authoring only — never paste raw template markdown into the chat as a final deliverable.
