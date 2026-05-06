# Workflow — Draft

Mode 2. The lawyer wants a drafting starter.

## Inputs expected

- What is being drafted (pre-contract notice for product / related service / DPS clauses / refusal letter / public-page text / etc.)
- Side advised (data holder / user / third party)
- Matter facts material to the draft (offering description, parties, jurisdiction)

## Templates

| Template | Side | Source / authority |
|----------|------|--------------------|
| `precontract-disclosure-art-3-2.md` | data holder | Reg. Art. 3(2) — connected product, 4 mandatory items |
| `precontract-disclosure-art-3-3.md` | data holder | Reg. Art. 3(3) — related service, 9 mandatory items |
| `dps-contract-clauses-art-25.md` | data holder | Reg. Art. 25 — clauses (a)–(i) |
| `dps-public-page-art-26.md` | data holder | Reg. Art. 26 — switching info + register reference |
| `dps-public-page-art-28.md` | data holder | Reg. Art. 28 — jurisdiction + measures |
| `dps-public-page-art-29.md` | data holder | Reg. Art. 29 — fees disclosure (until 12 Jan 2027) |
| `trade-secret-confidentiality-agreement.md` | data holder | Reg. Art. 4(6) — measures with user |
| `trade-secret-withhold-suspend-letter.md` | data holder | Reg. Art. 4(7) — escalation + CA notification |
| `trade-secret-refusal-letter.md` | data holder | Reg. Art. 4(8) — exceptional refusal + CA notification |
| `safety-security-restriction-clause.md` | data holder | Reg. Art. 4(2) |
| `international-access-customer-notice.md` | data holder | Reg. Art. 32(5) |
| `third-party-data-sharing-request.md` | user | Reg. Art. 5(1) |
| `complaint-art-37.md` | user | Reg. Art. 38 (lodge complaint with CA) |
| `switching-initiation-notice.md` | user (DPS customer) | Reg. Art. 25(3) |
| `data-export-verification-checklist.md` | user | Quality / completeness check on receipt |
| `classification-memo.md` | either | Internal classification record |
| `gap-analysis-checklist.md` | either | Audit checklist |

If the lawyer asks for something not on this list, propose the closest template and ask whether to adapt or to start from scratch. Adaptation is preferred.

## Procedure

1. **Identify the template** that best matches the request. If unclear, ask. If the lawyer wants something not in the catalogue, propose the closest match.

2. **Read** the template file from `assets/templates/`.

3. **Read** the relevant reference file(s) for legal grounding:
   - Pre-contract notices → `references/chapter-2-access.md`
   - DPS clauses → `references/chapter-6-dps.md`
   - Trade-secret items → `references/trade-secret-ladder.md`
   - Safety items → `references/safety-security.md`
   - International access → `references/international-access.md`

4. **Read** the verbatim source from `assets/source/regulation-2023-2854.md` for any text that appears in the draft as a direct quote or recital.

5. **Sectoral overlay gate.** If applicable, prepend the warning from `references/sectoral-overlays.md`.

6. **Read** `references/gotchas.md`.

7. **Read** `references/citation-style.md`.

8. **Capture missing inputs.** Templates contain placeholders like `[NAME OF DATA HOLDER]`, `[OFFERING NAME]`, `[JURISDICTION]`, `[DATE]`. Ask the lawyer to provide each before rendering, or mark them clearly as `[INSERT — facts]` in the rendered output.

9. **Render to Word** via `scripts/render_docx.py`.

10. **Append disclaimer** from `references/disclaimer-short.md`.

## What every draft must include

- Title block: deliverable type, parties (or `[INSERT]`), date.
- "Bottom line" / purpose statement.
- The substantive clauses or text.
- Article and FAQ references next to each substantive clause.
- A "Starting-Point Notice" footer at the top of every output: "This is a starting-point draft. Substantive review by qualified counsel is required before any reliance, signing, dispatch, or filing."
- The short disclaimer at the end.

## What every draft must NOT include

- Any specific company name unless the lawyer supplied it.
- Any sectoral lex-specialis content (the gate may flag, but the draft itself does not include sectoral law).
- The original creator's name.
- Member-state-specific content unless the lawyer supplied the member state and the template supports it.
- A "we recommend" without an article citation.
- A claim that the draft is final.

## Common drafting errors

- Omitting Art. 25(2)(a) mandatory transitional period from a DPS clause set.
- Omitting Art. 25(2)(g) retrieval period from a DPS clause set.
- Treating Art. 25(4) as optional (it is mandatory once infeasibility is asserted).
- Omitting Art. 28(2) — listing the jurisdiction-info URL in the contract.
- Trade-secret refusal letter that skips Steps 1 and 2.
- Pre-contract notice that omits any of the four / nine fields.

## When to ask before drafting

- When the offering classification is not yet established (run `workflow-classify.md` first).
- When the side advised is unclear.
- When sector indicators suggest the lawyer should be considering sectoral law before horizontal Data Act drafting.
- When a date is essential (e.g., for fee-clause structure given the 12 January 2027 cutover) and the lawyer has not stated whether the contract pre- or post-dates the cutover.
