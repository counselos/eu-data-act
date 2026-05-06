# Decision Tree — Article 32 International Access

Walkable Q&A on receipt of a third-country governmental order requiring transfer of or access to non-personal data held in the Union.

---

## Q0. Threshold — does Article 32 apply?

Article 32 applies to providers of data processing services. The data in question must be:
- **Non-personal data.** For personal data, GDPR Chapter V (international transfers) governs separately.
- **Held in the Union** — physically located on infrastructure in the EU (or, by reasonable interpretation, processed under EU law in the absence of a specific physical-presence test).
- **Within the scope of the Regulation** — i.e., subject to Chapter VI obligations.

If any of these is NO, Article 32 may not apply directly; the lawyer must verify on the specific facts.

---

## Q1. Is the order based on an international agreement?

Article 32(2) — the order is recognised or enforceable only if it is based on an international agreement (e.g., a mutual legal assistance treaty) in force between the requesting third country and:
- the Union, OR
- the relevant Member State.

Branching:

- YES → may comply on minimum-data basis under Art. 32(4). Proceed to Q5 (notification).
- NO → proceed to Q2.

---

## Q2. Would compliance risk conflict with Union or Member-State law?

Branching:

- NO → Article 32(3) is not engaged. The provider may comply (subject to Art. 32(4) minimum-data and Art. 32(5) notification).
- YES → proceed to Q3.

---

## Q3. Are all three Article 32(3) cumulative conditions met?

- (3a) Does the third-country system require the reasons and proportionality of the decision to be set out, AND require the decision to be specific in character (e.g., establishing a sufficient link to certain suspected persons or infringements)?
- (3b) Is the reasoned objection of the addressee subject to a review by a competent third-country court or tribunal?
- (3c) Is the third-country court or tribunal empowered under the law of that third country to take into account the relevant legal interests of the provider protected by Union or Member-State law?

Branching:

- All three YES → may comply on minimum-data basis. Proceed to Q4.
- Any NO → do not comply. Preserve evidence of the order. Consider EU-side legal challenges and engagement with the relevant Member State or the Commission. Notify the customer per Q5 unless prohibited.

---

## Q4. Minimum-data scoping

Article 32(4) — provide the **minimum amount of data permissible** in response to the request, on the basis of a reasonable interpretation of the request by the provider or the relevant national body or authority referred to in Article 32(3) second subparagraph.

Operational steps:

- Map the order to specific data categories.
- Apply data-minimisation: scope to the narrowest interpretation consistent with the order's terms.
- Exclude any data outside the scope (e.g., other customers' data, unrelated time periods).
- Document the scoping reasoning.

---

## Q5. Customer notification

Article 32(5) — inform the customer about the existence of the request **before complying**, except where the request serves law-enforcement purposes and notification would defeat that purpose for as long as necessary.

Branching:

- General default → notify the customer using template `international-access-customer-notice.md`.
- Law-enforcement carve-out applies → do not notify until the law-enforcement non-disclosure period ends.

The carve-out is narrow. "It might be law enforcement" is not enough; the provider must have a basis to conclude that notification would defeat the activity.

---

## Q6. Internal procedure

For each step above, the provider should:

- Engage internal legal review before any disclosure.
- Document the assessment (what was concluded under each of (1)–(3) and why).
- Apply the contractual measures referenced in the Article 28 statement.
- Update the Article 28 statement if the assessment reveals a measures gap.
- Coordinate with sub-processors and downstream data holders where relevant.

---

## Q7. Sectoral overlay

Sectoral law (e.g., DORA for financial entities, NIS2 for essential entities) may impose additional or distinct procedures. The Skill flags but does not cover sectoral overlays.

---

## Common defects (Skill flags these)

| # | Defect | Why it fails |
|---|--------|--------------|
| 1 | Compliance based on the order alone, without Art. 32(2) / (3) analysis | Default-prevent posture under 32(1); recognition is the exception. |
| 2 | Notice to customer skipped without a basis under the law-enforcement carve-out | Art. 32(5) requires notification by default. |
| 3 | Provided more data than the minimum permissible | Art. 32(4) requires minimum-data interpretation. |
| 4 | Treated the Art. 28 measures statement as a substitute for the assessment | The statement is transparency; the assessment is per-order. |
| 5 | Failed to document the assessment | Inability to evidence the assessment is itself a regulatory risk. |
| 6 | Compliance with a personal-data transfer order under Article 32 alone | Personal-data transfers also require GDPR Chapter V analysis. |
