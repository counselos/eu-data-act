# International access — Articles 28 and 32

Two distinct provisions: Art. 28 sets contractual transparency; Art. 32 sets the substantive rule for third-country access requests. Both apply to data processing services (Chapter VI).

## Article 28 — Contractual transparency

### Verbatim

> "1. Providers of data processing services shall make the following information available on their websites, and keep that information up to date:
> (a) the jurisdiction to which the ICT infrastructure deployed for data processing of their individual services is subject;
> (b) a general description of the technical, organisational and contractual measures adopted by the provider of data processing services in order to prevent international governmental access to or transfer of non-personal data held in the Union where such access or transfer would create a conflict with Union law or the national law of the relevant Member State.
> 2. The websites referred to in paragraph 1 shall be listed in contracts for all data processing services offered by providers of data processing services."

### Operational requirements

- A **public website** with two pieces of information.
- The information must be **current**.
- The relevant URL must be **listed in every DPS contract**.

### What goes on the website

#### (a) Jurisdiction of ICT infrastructure

Per service / per region. The granularity should match the customer's ability to reason about applicable law. Example structure:

| Service | Region | Country / jurisdiction of infrastructure |
|---------|--------|------------------------------------------|
| Service X | EU-West | Republic of Ireland |
| Service X | EU-Central | Federal Republic of Germany |
| Service Y | Global | Multiple — see service-specific data location supplement |

#### (b) Measures against third-country governmental access / transfer

A **general description** of:
- Technical measures — e.g., encryption with customer-controlled keys, data residency controls, segregated processing environments.
- Organisational measures — e.g., access-control policies, request-handling procedures, executive-review protocols for compelled access.
- Contractual measures — e.g., supplier flow-down clauses, sub-processor restrictions, government-access clauses with sub-processors.

The description is "general" — it does not need to disclose proprietary security architecture, but must give a customer a meaningful basis on which to evaluate the regime.

### Public-page template

`assets/templates/dps-public-page-art-28.md`.

## Article 32 — International governmental access and transfer

### Verbatim — 32(1)

> "Providers of data processing services shall take all adequate technical, organisational and legal measures, including contracts, in order to prevent international and third-country governmental access and transfer of non-personal data held in the Union where such transfer or access would create a conflict with Union law or with the national law of the relevant Member State, without prejudice to paragraph 2 or 3."

### Verbatim — 32(2)

> "Any decision or judgment of a third-country court or tribunal and any decision of a third-country administrative authority requiring a provider of data processing services to transfer or give access to non-personal data falling within the scope of this Regulation held in the Union shall be recognised or enforceable in any manner only if based on an international agreement, such as a mutual legal assistance treaty, in force between the requesting third country and the Union, or any such agreement between the requesting third country and a Member State."

### Verbatim — 32(3) — the no-treaty conditions

> "In the absence of an international agreement as referred to in paragraph 2, where a provider of data processing services is the addressee of a decision or judgment of a third-country court or tribunal or a decision of a third-country administrative authority to transfer or give access to non-personal data falling within the scope of this Regulation held in the Union and compliance with such a decision would risk putting the addressee in conflict with Union law or with the national law of the relevant Member State, transfer to or access to such data by that third-country authority shall take place only where:
> (a) the third-country system requires the reasons and proportionality of such a decision or judgment to be set out and requires such a decision or judgment to be specific in character, for instance by establishing a sufficient link to certain suspected persons or infringements;
> (b) the reasoned objection of the addressee is subject to a review by a competent third-country court or tribunal; and
> (c) the competent third-country court or tribunal issuing the decision or judgment or reviewing the decision of an administrative authority is empowered under the law of that third country to take duly into account the relevant legal interests of the provider of the data protected by Union law or by the national law of the relevant Member State."

All three conditions cumulative.

### 32(4) — minimum data

> "If the conditions laid down in paragraph 2 or 3 are met, the provider of data processing services shall provide the minimum amount of data permissible in response to a request, on the basis of the reasonable interpretation of that request by the provider or relevant national body or authority referred to in paragraph 3, second subparagraph."

### 32(5) — customer notification

> "The provider of data processing services shall inform the customer about the existence of a request of a third-country authority to access its data before complying with that request, except where the request serves law enforcement purposes and for as long as this is necessary to preserve the effectiveness of the law enforcement activity."

## Decision flow on receipt of a third-country order

```
Third-country authority order received
  │
  ▼
Is it covered by an international agreement (e.g. MLAT)?
  │ Yes → may be recognised / enforceable; comply on minimum data (32(4))
  │ No
  ▼
Would compliance risk conflict with Union / member-state law?
  │ No → comply on minimum data
  │ Yes
  ▼
Are the three 32(3) conditions all met?
  │ (a) reasoned + proportionate + specific decision
  │ (b) reasoned objection subject to review
  │ (c) third-country court can take Union / national-law interests into account
  │
  │ All three Yes → comply on minimum data (32(4))
  │ Any No → do not comply; preserve evidence; consider EU-side legal challenges
  ▼
Notify customer (32(5)) unless law-enforcement non-disclosure requirement applies
```

## Practical drafting

### DPS contract clause

The contract should:
- Reference the Art. 28 website URL.
- Commit to the Art. 32 default-prevent posture.
- Define notification procedure to the customer (Art. 32(5) carve-out for law enforcement).
- Where relevant, identify the technical measures customer-controlled (e.g., customer-managed encryption keys).

### Customer notification template (Art. 32(5))

A starting-point notification is at `assets/templates/international-access-customer-notice.md`. The notification should identify:
- The third-country authority and order reference.
- Categories of data sought.
- The provider's posture (comply / object / partial).
- The customer's options (intervene, challenge, request redirection).
- The basis for any non-disclosure period (32(5) carve-out).

## Interaction with US CLOUD Act and similar laws

The skill does not give member-state-specific or non-EU-jurisdictional advice. Common interaction points:

- **US CLOUD Act** — US-issued production orders for data held by US-providers' EU subsidiaries fall squarely within Art. 32. Art. 32(2)/(3) provide the framework for evaluating compliance / objection.
- **PRC data security laws** (Data Security Law, Personal Information Protection Law, etc.) — outbound data transfers from PRC affiliates of EU customers may invoke PRC data-export controls; these are out of scope for this skill.
- **UK regime** — post-Brexit, UK is a third country for Art. 32 purposes. Adequacy decisions under GDPR are a separate question.

The lawyer must verify the third-country regime independently.

## See also

- `references/chapter-6-dps.md` — Arts. 28 and 32 in context
- `references/often-missed.md` — interplay with Arts. 4(13) and 5(3)
- `assets/decision-trees/international-access-art-32.md` — walkable Q&A
