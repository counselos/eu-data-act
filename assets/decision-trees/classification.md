# Decision Tree — Classification

Walkable Q&A. The skill walks the lawyer through this tree when the offering's classification is unclear.

---

## Q1. Is there a connected product? (Art. 2(5))

Three cumulative elements:

- (1a) Does the offering include a physical item that obtains, generates or collects data about its use or environment?
- (1b) Can it communicate product data via electronic communications service, physical connection, or on-device access?
- (1c) Is the primary function of the item NOT storing / processing / transmitting data on behalf of any party other than the user?

Branching:

- All three YES → connected product. Proceed to Q2.
- Any NO → not a connected product. Skip to Q3.

Common pitfalls:
- A USB-only device with no internet still passes (1b) — physical connection counts.
- Servers and routers usually fail (1c) and are out of Chapter II under FAQ Q7.
- Prototypes that have not finished manufacturing are out of scope under FAQ Q7.

---

## Q2. Is there a related service? (Art. 2(6))

Three cumulative elements:

- (2a) Is there a digital service or software (other than electronic communications service)?
- (2b) Is it connected with the connected product at sale, rent, or lease, OR added later by the manufacturer or a third party?
- (2c) Does it (i) prevent the product from performing one or more functions when absent, OR (ii) add to / update / adapt the product's functions?

FAQ Q10 interpretive aids (non-authoritative):
- Bidirectional data exchange between product and service provider.
- Service affects product function, behaviour, or operation.

Branching:

- All three YES → related service. Proceed to Q3.
- Any NO → not a related service. Proceed to Q3 (the digital service may still be a DPS independently).

Common pitfalls:
- Receive-only telemetry that only reports product status without affecting it is **not** a related service. (Q10 last paragraph; Recital 17.)
- Standalone analytics, repair, maintenance, financial, or consulting services are aftermarket and not related services.
- A consumer-grade configuration utility that affects product function does qualify, even on-premise.

---

## Q3. Is the digital service a DPS? (Art. 2(8))

All elements should be present:

- (3a) Provided to a customer (Art. 2(30) — contractual relationship).
- (3b) Ubiquitous + on-demand network access.
- (3c) Shared, scalable, elastic resources.
- (3d) Rapidly provisioned / released with minimal interaction.

Branching:

- All YES → DPS. Proceed to Q4.
- Any NO → not a DPS. Skip to Q5 (carve-outs and conclusion).

Common pitfalls:
- A pre-installed on-premise software shipped with the connected product is generally **not** a DPS — it lacks the on-demand, shared-pool, elastic characteristics.
- A multi-tenant SaaS sold to a customer is a DPS (per Q58a, even if the customer experiences it as a SaaS for an end-user — the customer is the DPS customer).
- IaaS, PaaS, SaaS all qualify (Recital 81; Q58a).

---

## Q4. Overlap and DPS scope nuance

If Q2 (related service) AND Q3 (DPS) are both YES → both regimes apply.

DPS scope nuance:

- Art. 30(1) functional equivalence — IaaS only.
- Art. 30(2) open interfaces — PaaS / SaaS.
- Art. 30(3) interoperability standards — PaaS / SaaS, with 12-month compatibility horizon after standards published.
- Arts. 25, 26, 28, 29 — all DPS types.

If the offering qualifies for an Article 31 carve-out → see Q5.

---

## Q5. Article 31 lighter-regime carve-outs (DPS only)

- (5a) **Custom-built (Art. 31(1)).** Does the offering have the majority of its main features custom-built for one customer, OR all components developed for one customer, AND it is **not** offered at broad commercial scale via the catalogue?
  - YES → Article 31(1) applies. Disapplied: Art. 23(d), Art. 29, Art. 30(1), Art. 30(3). Still apply: most of Chapter VI including Art. 30(2) and Art. 25.
  - NO → continue.
- (5b) **Test / beta (Art. 31(2)).** Is the offering a non-production version for testing and evaluation, for a limited period of time?
  - YES → Article 31(2) applies. All of Chapter VI disapplied. Article 31(3) pre-contract disclosure required.
  - NO → continue.

Common pitfalls:
- A multi-tenant SaaS with customer-specific configuration is **not** custom-built under Art. 31(1).
- An "indefinite beta" forfeits the Article 31(2) carve-out.

---

## Q6. SME / micro-enterprise carve-out (Chapter II)

Article 7 may exclude data holders that are micro or small enterprises from the Chapter II obligations, subject to specific conditions.

Branching:
- Data holder is a micro or small enterprise → check Art. 7 conditions; if applicable, the data holder may be excluded.
- Data holder is medium enterprise in first year of meeting threshold → similar consideration.
- Otherwise → no Art. 7 carve-out.

---

## Q7. Sectoral overlay check

Apply the Skill's `references/sectoral-overlays.md` gate. Sectoral indicators captured in per-matter facts:

- Automotive → Reg. 2018/858
- Medical devices → MDR / IVDR
- Financial services → DORA
- Cybersecurity → NIS2
- AI → AI Act
- Energy / public sector / eIDAS → as applicable

If any sectoral indicator is captured, surface the corresponding warning. The classification analysis itself does **not** address sectoral lex specialis.

---

## Conclusion structure

After walking Q1–Q7, the classification memo states:

```
Connected Product (Art. 2(5)):     YES / NO
Related Service (Art. 2(6)):       YES / NO
DPS (Art. 2(8)):                   YES / NO
Overlap (both regimes apply):      YES / NO
Article 31 lighter-regime:         (1) custom-built / (2) test-beta / N/A
Article 7 SME carve-out:           applicable / N/A
Sectoral overlay flagged:          [list]
Member-state lex specialis check:  required (lawyer)
```

Then narrative reasoning per question, then open questions, then defined terms, then sources, then disclaimer.
