# Decision Tree — Article 31 Lighter Regime

When does the Article 31 lighter regime for DPS apply, and what does it disapply?

---

## Q1. Is the offering a Data Processing Service?

Run the Article 2(8) test (see `assets/decision-trees/classification.md` Q3). If NO, Article 31 is irrelevant.

---

## Q2. Article 31(1) — custom-built service

Two cumulative elements:

- (2a) **Engineering profile.** Either (i) the majority of main features have been custom-built to accommodate the specific needs of an individual customer, OR (ii) all components have been developed for the purposes of an individual customer.
- (2b) **Commercial profile.** The service is **not** offered at broad commercial scale via the service catalogue of the provider.

Both must be met.

Branching:

- Both YES → Article 31(1) applies. Proceed to Q4.
- Either NO → Article 31(1) does not apply. Proceed to Q3.

Common pitfalls:
- A multi-tenant SaaS with customer-specific configuration is NOT custom-built — that is a productised offering with customisation, not custom-build.
- A service offered to multiple customers (even with bespoke aspects) usually fails (2b).
- "Custom-built" engineering effort is uniquely for that one customer.

---

## Q3. Article 31(2) — non-production test / beta

Two cumulative elements:

- (3a) The service is provided as a non-production version for testing and evaluation purposes.
- (3b) For a limited period of time.

Branching:

- Both YES → Article 31(2) applies. Proceed to Q5.
- Either NO → Article 31 does not apply. Full Chapter VI applies.

Common pitfalls:
- An "indefinite beta" forfeits (3b). The time-limit must be definite (a clear end date or trigger).
- An evaluation tier offered alongside a paid production tier is generally not a non-production version.

---

## Q4. What does Article 31(1) disapply?

Disapplied:

- Art. 23(d) — functional-equivalence obstacle removal.
- Art. 29 — switching-charges regime.
- Art. 30(1) — functional equivalence (this is IaaS-anyway-only; if the offering is not IaaS it is moot).
- Art. 30(3) — interoperability standards compatibility.

**Still applies** (i.e., the provider must comply):

- Art. 25 — contract terms (notice ≤ 2 mo; mandatory transitional 30 d; retrieval ≥ 30 d; etc.).
- Art. 26 — switching information + register (note: 30(4) register-update obligation may interact with disapplied 30(3); the lawyer should consider).
- Art. 27 — good-faith cooperation.
- Art. 28 — international-access transparency.
- Art. 30(2) — open interfaces (PaaS / SaaS).
- Art. 30(5) — pre-standards export obligation.
- Art. 32 — international governmental access.

Article 31(3) pre-contract disclosure obligation: tell the prospective customer which obligations of Chapter VI do not apply.

---

## Q5. What does Article 31(2) disapply?

Disapplied: **all of Chapter VI**.

Article 31(3) pre-contract disclosure: tell the prospective customer that Chapter VI does not apply.

---

## Q6. Practical drafting under Article 31

For Article 31(1) services:
- Use the standard Article 25 template, but note the disapplied items in Article 31(3) disclosure.
- For PaaS / SaaS, retain Article 30(2) open-interface obligations.
- Pre-contract disclosure under Article 31(3) should list disapplied obligations explicitly.

For Article 31(2) services:
- Time-bound the offering at signature.
- Pre-contract disclosure under Article 31(3) confirms Chapter VI does not apply.
- On expiry of the time limit, the service (if continued) falls into full Chapter VI scope; plan the transition.

Templates: see `assets/templates/dps-contract-clauses-art-25.md` (with adapted notes for Art. 31(1)) and a standalone `art-31-disclosure.md` if needed.

---

## Q7. Sectoral overlay check

Article 31 does not exempt the offering from sectoral law (DORA, NIS2, etc.). The Skill flags but does not cover sectoral overlays.
