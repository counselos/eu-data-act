# Workflow — Classify

Mode 1. The lawyer wants to determine whether an offering is a connected product, related service, DPS, or some combination.

## Input expected

The lawyer provides facts about an offering. Typical inputs:
- What the offering does
- What hardware (if any) is involved
- What software (mobile app, on-prem, SaaS) is involved
- Whether software affects, controls, configures, updates, or merely observes the hardware
- Where data is stored / processed
- How customers contract for and use it
- Sectoral context

If material facts are missing, ask before classifying. Do not guess.

## Procedure

1. **Read** `references/definitions.md` to refresh the definitions of (5) connected product, (6) related service, (8) DPS, (12) user, (13) data holder, (15) product data, (16) related service data.

2. **Read** `references/chapter-2-access.md` for the operative provisions on connected product / related service.

3. **Read** `references/chapter-6-dps.md` for DPS scope and the IaaS / PaaS / SaaS split.

4. **Read** `assets/decision-trees/classification.md`. Walk the four questions in sequence.

5. **Sectoral overlay gate.** If `references/per-matter-facts.md` captured any sector indicator, surface the corresponding warning from `references/sectoral-overlays.md` BEFORE the classification conclusion.

6. **Apply each test.**

   ### Q1 — Is there a connected product?
   - (a) Does the offering include a physical item that obtains, generates or collects data about its use or environment? (Art. 2(5))
   - (b) Can it communicate product data via electronic communications service, physical connection, or on-device access? (Art. 2(5))
   - (c) Is the primary function of the item NOT storing / processing / transmitting data on behalf of any party other than the user? (Art. 2(5))
   - All three YES → connected product.
   - Any NO → not a connected product. (Note: a server, router, or pure storage device usually fails (c); a prototype not yet placed on the market fails per FAQ Q7.)

   ### Q2 — Is there a related service?
   - (a) Is there a digital service or software (other than electronic communications service)?
   - (b) Is it connected with the connected product at sale, rent, or lease, OR added later by the manufacturer or a third party?
   - (c) Does it (i) prevent the product from performing one or more functions when absent, OR (ii) add to / update / adapt the product's functions?
   - All three YES → related service.
   - FAQ Q10 interpretive aids: (i) bidirectional data exchange between product and service provider; (ii) the service affects product function, behaviour, or operation. Both are commonly necessary in practice but the regulation's text in Art. 2(6) is the authoritative test.

   ### Q3 — Is the digital service a DPS?
   - All Art. 2(8) elements should be present:
     - Provided to a customer (Art. 2(30))
     - Ubiquitous + on-demand network access
     - Shared, scalable, elastic computing resources
     - Rapid provisioning / release with minimal interaction
   - YES → DPS. Covers IaaS, PaaS, SaaS (FAQ Q58a, Recital 81).

   ### Q4 — Overlap?
   - If Q2 (related service) AND Q3 (DPS) are both YES: BOTH regimes apply. Chapter II governs access to product data + related-service data; Chapter VI governs DPS switching / portability / interoperability.
   - If pure SaaS not tied to product function (Q2 NO, Q3 YES): DPS only.

7. **Carve-outs to consider.**
   - Art. 7 — micro / small enterprises as data holders may be exempt from Chapter II under conditions.
   - Art. 31(1) — custom-built DPS may benefit from lighter regime.
   - Art. 31(2) — non-production test/beta DPS may be fully out of Chapter VI.
   - Sectoral lex specialis (per `references/sectoral-overlays.md`).

8. **Read** `references/gotchas.md`. In particular, watch for:
   - Direct-access not being mandatory (gotcha 7).
   - Functional equivalence being IaaS-only (gotcha 3).
   - "Customised tenant" not being "custom-built" (gotcha 19).
   - Prototypes not being a free pass (gotcha 18).

9. **Produce the classification memo** using `assets/templates/classification-memo.md` filled with the matter facts.

11. **Render to Word** via `scripts/render_docx.py`.

## Memo structure (target output)

```
1. Bottom line — one sentence stating the classification.
2. Conclusion in detail — which regimes apply and why; carve-outs considered.
3. Facts assumed.
4. Analysis under each test (Q1 connected product, Q2 related service, Q3 DPS).
5. Sectoral overlay warning (if any).
6. Open questions / additional facts needed.
7. Defined terms.
8. Sources used (regulation + FAQ version + verified date).
9. Disclaimer.
```

## Common classification errors

- Assuming "no internet" means "not a connected product" (Art. 2(5) covers physical connection / on-device access too).
- Assuming a SaaS that processes connected-product data is automatically a related service (Art. 2(6) requires functional effect on the product).
- Conflating "data holder" with "manufacturer" (data holder is a definitional role under Art. 2(13)).
- Assuming custom-tenanted SaaS qualifies for Art. 31(1) (it does not).
- Treating the FAQ as authoritative on close calls.

## When to push back on the lawyer's assumed classification

If the facts plainly do not support the lawyer's stated assumption, the memo states the analytical disagreement explicitly in the "Conclusion in detail" section and identifies what facts would change the answer. Do not rubber-stamp.
