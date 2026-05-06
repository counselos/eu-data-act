# Workflow — Audit

Mode 5. The lawyer wants a gap analysis comparing an offering's current state against the regulation's requirements.

## Inputs expected

- Description of the offering (or set of offerings).
- Documentation, where available: pre-contract notice, T&Cs, public pages, contract templates, internal data-flow notes.
- The regulation areas to audit (often: Chapter II + Chapter VI; sometimes a subset).
- Side advised.

If documentation is missing, the audit identifies its absence as a HIGH-severity finding.

## Procedure

1. **Capture per-matter facts** per `references/per-matter-facts.md`.

2. **Sectoral overlay gate.** Surface warnings.

3. **Classify the offering** (run `workflow-classify.md` mentally if not already done) so the audit knows which regimes apply.

4. **Identify the obligation set** for each applicable regime:
   - Connected product → Art. 3(1) by-design (subject to placement-on-market date), Art. 3(2) pre-contract disclosure, Art. 4(1) access on request, Art. 4(2) safety/security clause, Art. 4(6)–(8) trade-secret regime, Art. 4(10) user constraints, Art. 4(13) data-holder constraint, Art. 5 third-party transfer.
   - Related service → Art. 3(1), Art. 3(3) pre-contract (9 fields), Art. 4 mechanics for related-service data.
   - DPS → Art. 23 obstacles, Art. 25 contract clauses (a)–(i) plus 25(3)/(4)/(5), Art. 26 information + register, Art. 28 jurisdiction page + contract listing, Art. 29 fees regime, Art. 30(1)/(2)/(3)/(5)/(6) technical aspects.
   - Cross-cutting → Art. 1(5) GDPR overlay, Art. 31 lighter-regime considerations, Art. 32 international access, Art. 37–40 enforcement.

5. **Read** the relevant reference files for each obligation cluster.

6. **For each obligation, score the offering's posture:**
   - **OK** — meets the obligation.
   - **PARTIAL** — meets some elements; gaps identified.
   - **GAP** — does not meet the obligation.
   - **N/A** — obligation does not apply (e.g., Art. 30(1) for SaaS).
   - **NEEDS-FACTS** — auditor cannot determine without more information.

7. **Severity** for each GAP and PARTIAL:
   - **HIGH** — non-compliance with a load-bearing obligation; immediate remediation needed (e.g., missing Art. 25 mandatory clauses, missing Art. 3(2) disclosure, ongoing switching-charge after 12 January 2027).
   - **MEDIUM** — non-compliance with a procedural / public-facing obligation that is fixable within weeks (e.g., outdated Art. 26(b) register, missing Art. 28 contract listing).
   - **LOW** — non-compliance with a documentation / hygiene item.

8. **Read** `references/gotchas.md`.

9. **Render to Word** via `scripts/render_docx.py`. Use the gap-analysis checklist template.

## Output structure (target)

```
1. Executive summary — total gaps by severity, top three remediations.
2. Scope of audit — what was reviewed; what was assumed; what was excluded.
3. Classification of the offering(s).
4. Findings table — one row per obligation, with status, severity, evidence, recommendation.
5. Recommendations — prioritised by severity; effort/owner notes.
6. Open questions (NEEDS-FACTS items).
7. Sectoral / member-state overlays the lawyer must verify independently.
8. Defined terms.
9. Sources.
10. Disclaimer.
```

## Findings table — column structure

| Reg. | Obligation | Status | Severity | Evidence reviewed | Gap description | Recommendation |
|------|------------|--------|----------|-------------------|-----------------|----------------|
| Art. 3(2)(a) | Type, format, estimated volume of product data disclosed pre-contract | PARTIAL | MEDIUM | Pre-contract notice draft v3 reviewed | Type and format covered; estimated volume omitted | Add volume estimate per data category |
| Art. 25(2)(a) | Mandatory 30-day transitional period in DPS contract | GAP | HIGH | DPS template v1.7 reviewed | Clause omitted | Insert clause; reference `assets/templates/dps-contract-clauses-art-25.md` |
| Art. 30(1) | Functional equivalence | N/A | — | — | SaaS service; 30(1) is IaaS-only | — |

Use this format consistently.

## Standard obligation checklists

The audit walks each of these in turn:

### Connected product checklist

- [ ] Art. 3(1) — design-by-default access (if placed on market after 12 Sep 2026)
- [ ] Art. 3(2)(a) — type / format / volume disclosed
- [ ] Art. 3(2)(b) — continuous / real-time generation indicated
- [ ] Art. 3(2)(c) — storage location + retention
- [ ] Art. 3(2)(d) — access / retrieve / erase + technical means + ToS / QoS
- [ ] Art. 4(1) — indirect access on simple electronic request
- [ ] Art. 4(1) — format: comprehensive, structured, machine-readable
- [ ] Art. 4(1) — same quality as data holder holds
- [ ] Art. 4(1) — without undue delay, with proactive automation
- [ ] Art. 4(1) — free of charge to user
- [ ] Art. 4(2) — safety/security carve-out (if invoked) — properly scoped clause + CA notification procedure
- [ ] Art. 4(6)–(8) — trade-secret three-step ladder operational
- [ ] Art. 4(10) — user constraints reflected in terms
- [ ] Art. 4(13) — internal data-use grounded in contract with user
- [ ] Art. 5(1) — third-party transfer mechanism
- [ ] Art. 5(3) — gatekeeper recipient screening
- [ ] Art. 11 — TPMs identified

### Related service checklist

- [ ] Art. 3(1) (subject to 12 Sep 2026 cut-off)
- [ ] Art. 3(3)(a)–(i) — all nine fields disclosed
- [ ] Art. 4 mechanics — applied to related-service data
- [ ] Erasure path operational (Art. 3(2)(d) analogue applied)

### DPS checklist

- [ ] Art. 23 — no obstacles (a)–(e)
- [ ] Art. 25(1) — pre-signature availability of contract
- [ ] Art. 25(2)(a) — mandatory transitional period clause (30 days, with all four sub-elements)
- [ ] Art. 25(2)(b) — exit-strategy support obligation
- [ ] Art. 25(2)(c) — termination triggers (i) and (ii)
- [ ] Art. 25(2)(d) — notice period ≤ 2 months
- [ ] Art. 25(2)(e) — exhaustive port list
- [ ] Art. 25(2)(f) — internal-functioning carve-out (without delay-creating wording)
- [ ] Art. 25(2)(g) — minimum retrieval period ≥ 30 days
- [ ] Art. 25(2)(h) — erasure
- [ ] Art. 25(2)(i) — switching charges per Art. 29
- [ ] Art. 25(3) — three customer options at end of notice
- [ ] Art. 25(4) — provider's 14-working-day infeasibility procedure
- [ ] Art. 25(5) — customer's right to extend
- [ ] Art. 26(a) — public switching info
- [ ] Art. 26(b) — public register of data structures / formats / standards / open interop specs
- [ ] Art. 28(1) — public jurisdiction + measures page
- [ ] Art. 28(2) — page URL listed in DPS contract
- [ ] Art. 29(1) — no switching charges from 12 Jan 2027
- [ ] Art. 29(2)/(4)/(6) — pre-contract + public disclosure during reduced-charges window
- [ ] Art. 30(1) — functional equivalence (IaaS only)
- [ ] Art. 30(2) — open interfaces (PaaS / SaaS)
- [ ] Art. 30(3) — interoperability standards compatibility (PaaS / SaaS)
- [ ] Art. 30(4) — register update obligation
- [ ] Art. 30(5) — pre-standards export obligation
- [ ] Art. 32(1) — default-prevent posture for third-country access
- [ ] Art. 32(2)/(3) — third-country order procedure
- [ ] Art. 32(5) — customer-notification mechanism

## Common audit errors

- Failing to apply the 12 Sep 2026 cut-off (Art. 3(1) only applies to products placed after that date).
- Marking Art. 30(1) functional equivalence as a GAP for a SaaS (it is N/A).
- Missing the Art. 25(4) infeasibility procedure as a separate item.
- Missing the Art. 28(2) "URL in contract" item — even when Art. 28(1) page is up.
- Missing Art. 5(3) gatekeeper screening.
- Missing Art. 4(13) data-holder use grounding.
