# Worked Example — Article 32 international access with no treaty in place

A scenario in which a DPS provider receives a third-country authority order requiring access to non-personal data held in the Union, without an international agreement in place.

The example walks the Article 32 analysis from `references/international-access.md` and `assets/decision-trees/international-access-art-32.md`.

---

## Facts (hypothetical)

- A DPS provider operates a SaaS platform for European enterprise customers.
- The provider's parent company is incorporated in a third country (the "Third Country").
- A Third-Country administrative authority issues an order to the provider's parent company, requiring production of customer data held in the Union under the SaaS platform.
- The order is not based on a mutual legal assistance treaty in force between the Third Country and the Union or with the relevant Member State.
- The data sought is non-personal data: customer-uploaded inventory records and configuration metadata for one of the provider's enterprise customers in the Union.
- The provider does not have an established channel with the Third Country authority for objections.

## Q0 — Threshold

- Non-personal data: **YES.**
- Held in the Union: **YES.**
- Within scope of the Regulation: **YES** (Chapter VI applies).

Article 32 applies.

## Q1 — Is the order based on an international agreement?

NO. Proceed to Q2.

## Q2 — Would compliance risk conflict with Union or Member-State law?

The provider's preliminary assessment, reviewed by counsel: compliance would risk conflict with the law of the Member State where the data is processed (the relevant Member State's data-sovereignty principles, plus Art. 32(1) of the Data Act itself which obliges the provider to take measures to prevent such transfers).

YES. Proceed to Q3.

## Q3 — Are the three Article 32(3) cumulative conditions met?

### (3a) Third-country system requires reasoned + proportionate + specific decisions

The provider's analysis: the Third Country's procedural law does not require the requesting authority to set out the reasons and proportionality with the specificity required by Art. 32(3)(a). The order is broad, with no documented link to specific suspected persons or infringements.

**Condition (3a) is NOT met.**

### (3b) Reasoned objection subject to review

The provider's analysis: the Third Country provides a procedure under which the addressee may file a written objection, but the objection is reviewed by the same administrative authority that issued the order, not a competent court or tribunal.

**Condition (3b) is NOT met.**

### (3c) Court empowered to take Union / Member-State legal interests into account

The provider's analysis: the Third Country's courts are not empowered under Third-Country law to weigh Union or Member-State legal interests. The applicable Third-Country statute does not recognise foreign-state-law considerations as grounds for declining to enforce.

**Condition (3c) is NOT met.**

## Conclusion

All three conditions of Art. 32(3) are NOT met. Compliance is **not permissible** under Article 32.

## Provider action

The provider:

1. **Does not comply.** It takes adequate technical, organisational and legal measures to prevent the transfer (Art. 32(1)).
2. **Notifies the customer** (Art. 32(5)) using template `international-access-customer-notice.md`. The law-enforcement carve-out is considered and rejected on the facts (the order is not a law-enforcement order in the relevant sense, and no specific non-disclosure requirement applies).
3. **Engages with the relevant Member State authority** for guidance, where appropriate.
4. **Documents the assessment** with the substantive reasoning under each Q3 condition, supported by exhibits (the order itself, Third-Country procedural law analysis, etc.).
5. **Considers EU-side legal challenges** to any compelled-cooperation assertion at the parent-company level.

## Customer notification (Art. 32(5))

The provider sends the customer notice in advance of any compliance decision. The notice:

- Discloses the existence of the order (Art. 32(5)).
- Summarises the categories of data sought.
- States the provider's preliminary assessment that compliance is not permissible.
- Identifies the customer's options:
  - Intervene in the Third Country proceedings.
  - Confirm the customer's position on the provider's intended response.
  - Consider whether customer-controlled encryption keys (if any) put the data outside the provider's effective custody.

## Documentation

The provider preserves a documented record of:

- The order itself.
- The Third Country procedural-law analysis under Q3.
- The customer notification.
- Any subsequent communications with the Third Country authority, the customer, the relevant Member State authority, or the Commission.

## Public-page implications

The provider's Article 28(1)(b) measures statement should describe the technical, organisational and contractual measures the provider has in place — including the assessment-and-notify procedure that this scenario triggered. If the Article 28 page is silent on Article 32 procedure, the provider should update the page in light of this matter.

## Personal data variant

If the order had sought personal data instead of non-personal data:

- Article 32 of the Data Act would not directly apply (it concerns non-personal data).
- GDPR Chapter V (international transfers) would apply.
- The CJEU's Schrems II framework (Case C-311/18) on adequate safeguards would govern.

The Skill flags this variant; the lawyer must conduct the GDPR Chapter V analysis separately.

## Sectoral overlay

If the customer is a financial entity, DORA's third-party data-disclosure framework applies in addition to Article 32. If the customer is a NIS2 essential entity, NIS2 incident-reporting may engage. The lawyer must verify independently.

## Outcome

The provider does not comply with the order. The Third Country authority may pursue the order through other means (escalation, parallel proceedings against the parent), which the provider addresses through Third-Country counsel.

The provider documents the entire assessment as part of its Article 32 compliance posture and updates the Article 28 page.
