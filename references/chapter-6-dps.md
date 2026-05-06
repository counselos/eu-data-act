# Chapter VI — Switching between data processing services

Articles 23–32. The cloud / SaaS / PaaS / IaaS switching, portability, and international-access regime. Read full verbatim from `assets/source/regulation-2023-2854.md`.

## Article 23 — Removing obstacles to effective switching

> "Providers of data processing services shall take the measures provided for in Articles 25, 26, 27, 29 and 30 to enable customers to switch to a data processing service, covering the same service type, which is provided by a different provider of data processing services, or to on-premises ICT infrastructure, or, where relevant, to use several providers of data processing services at the same time. In particular, providers of data processing services shall not impose and shall remove pre-commercial, commercial, technical, contractual and organisational obstacles, which inhibit customers from:"

The five obstacle categories (Art. 23(a)–(e)):
- (a) terminating after notice + successful switching, per Art. 25
- (b) concluding new contracts with a different provider of the same service type
- (c) porting exportable data and digital assets, including after a free-tier offering
- (d) achieving functional equivalence (Art. 24, IaaS-only via Art. 30(1))
- (e) unbundling Art. 30(1) services from other services where technically feasible

## Article 24 — Scope

> "The responsibilities of providers of data processing services laid down in Articles 23, 25, 29, 30 and 34 shall apply only to the services, contracts or commercial practices provided by the source provider of data processing services."

## Article 25 — Contractual terms (the load-bearing article for drafting)

### 25(1) — Pre-signature availability

The customer's switching rights and the provider's obligations must be in a written contract, made available before signing in a form the customer can store and reproduce.

### 25(2) — Mandatory clauses (a)–(i)

> "Without prejudice to Directive (EU) 2019/770, the contract referred to in paragraph 1 of this Article shall include at least the following:"

- **(a) Mandatory transitional period — 30 calendar days, after the notice period.** During this period, the contract remains in force and the provider must:
  - (i) provide reasonable assistance to the customer and authorised third parties;
  - (ii) act with due care to maintain business continuity, continuing to provide functions/services under the contract;
  - (iii) provide clear information on known continuity risks;
  - (iv) maintain a high level of security throughout the switch and during the retrieval period.
- **(b) Exit-strategy support obligation** — provider must support the customer's exit strategy, including by providing all relevant information.
- **(c) Termination triggers** — contract is considered terminated either (i) on successful switch, or (ii) at end of notice period if the customer chooses to erase rather than switch.
- **(d) Notice period — maximum 2 months.**
- **(e) Exhaustive port list** — exhaustive specification of categories of data and digital assets that can be ported, which must at minimum include all exportable data.
- **(f) Internal-functioning carve-out** — exhaustive specification of provider-internal data exempted from porting where there is risk of trade-secret breach. The carve-out must NOT impede or delay the switching process.
- **(g) Minimum data-retrieval period — at least 30 calendar days.** Starts after the transitional period ends.
- **(h) Erasure** — full erasure of customer's exportable data and digital assets after retrieval (or after an alternative agreed later date).
- **(i) Switching charges** — if any, only as permitted by Art. 29.

### 25(3) — Customer's three options at end of notice

> "(a) switch to a different provider of data processing services, in which case the customer shall provide the necessary details of that provider;
> (b) switch to an on-premises ICT infrastructure;
> (c) erase its exportable data and digital assets."

### 25(4) — Technical-infeasibility extension

If the 30-day transitional period is technically infeasible, the provider must notify the customer **within 14 working days** of the switching request, justify the infeasibility in writing, and indicate an alternative transitional period **not exceeding 7 months**. Service continuity must be maintained throughout.

### 25(5) — Customer's right to extend

The customer may extend the transitional period once for a length the customer considers more appropriate.

### Time-window summary

| Window | Limit | Article |
|--------|-------|---------|
| Notice period (initiate switch) | ≤ 2 months | 25(2)(d) |
| Mandatory transitional period | 30 calendar days, after notice | 25(2)(a) |
| Customer extension right | once, customer-defined length | 25(5) |
| Provider extension on infeasibility | ≤ 7 months — must justify in writing within 14 working days | 25(4) |
| Minimum data-retrieval period | ≥ 30 calendar days, after transitional | 25(2)(g) |
| Erasure | after retrieval or later agreed date | 25(2)(h) |

## Article 26 — Information

> "The provider of data processing services shall provide the customer with:
> (a) information on available procedures for switching and porting to the data processing service, including information on available switching and porting methods and formats as well as restrictions and technical limitations which are known to the provider of data processing services;
> (b) a reference to an up-to-date online register hosted by the provider of data processing services, with details of all the data structures and data formats as well as the relevant standards and open interoperability specifications, in which the exportable data referred to in Article 25(2), point (e), are available."

The Art. 26(b) **online register** is a public obligation. It must be current. Updates obligated under Art. 30(4) when interoperability standards are published.

## Article 27 — Good faith

> "All parties involved, including destination providers of data processing services, shall cooperate in good faith to make the switching process effective, enable the timely transfer of data and maintain the continuity of the data processing service."

## Article 28 — Contractual transparency on international access

> "1. Providers of data processing services shall make the following information available on their websites, and keep that information up to date:
> (a) the jurisdiction to which the ICT infrastructure deployed for data processing of their individual services is subject;
> (b) a general description of the technical, organisational and contractual measures adopted by the provider of data processing services in order to prevent international governmental access to or transfer of non-personal data held in the Union where such access or transfer would create a conflict with Union law or the national law of the relevant Member State.
> 2. The websites referred to in paragraph 1 shall be listed in contracts for all data processing services offered by providers of data processing services."

The website URL must be **listed in every DPS contract** (Art. 28(2)).

## Article 29 — Gradual withdrawal of switching charges

- **29(1) — From 12 January 2027:** no switching charges at all for the switching process.
- **29(2) — 11 January 2024 → 12 January 2027:** reduced switching charges allowed.
- **29(3):** reduced charges cannot exceed direct switching costs.
- **29(4):** pre-contract disclosure of standard service fees, early-termination penalties, and reduced switching charges.
- **29(5):** information on highly complex / costly switching scenarios.
- **29(6):** the information in (4) and (5) must be publicly available — dedicated section of website or otherwise easily accessible.

Standard service fees and early-termination penalties remain permitted in either window. The prohibition is on charges *for switching itself*.

## Article 30 — Technical aspects of switching (split by service type)

### 30(1) — IaaS only: functional equivalence

> "Providers of data processing services that concern scalable and elastic computing resources limited to infrastructural elements such as servers, networks and the virtual resources necessary for operating the infrastructure, but that do not provide access to the operating services, software and applications that are stored, otherwise processed, or deployed on those infrastructural elements, shall, in accordance with Article 27, take all reasonable measures in their power to facilitate that the customer, after switching to a service covering the same service type, achieves functional equivalence in the use of the destination data processing service."

This applies only to IaaS as defined here. PaaS and SaaS do not owe functional equivalence (FAQ Q58a).

### 30(2) — PaaS / SaaS: open interfaces

> "Providers of data processing services, other than those referred to in paragraph 1, shall make open interfaces available to an equal extent to all their customers and the concerned destination providers of data processing services free of charge to facilitate the switching process. Those interfaces shall include sufficient information on the service concerned to enable the development of software to communicate with the services, for the purposes of data portability and interoperability."

### 30(3) — PaaS / SaaS: interoperability standards

> "For data processing services other than those referred to in paragraph 1 of this Article, providers of data processing services shall ensure compatibility with common specifications based on open interoperability specifications or harmonised standards for interoperability at least 12 months after the references to those common specifications or harmonised standards [...] were published in the central Union standards repository."

### 30(4) — Register update

The Art. 26(b) register must be updated in line with 30(3).

### 30(5) — Until standards exist

If no interoperability standards have been published, the provider must, on customer request, export all exportable data in a structured, commonly used and machine-readable format.

### 30(6) — IP / security carve-out

Providers are not required to develop new technologies or services, or to disclose / transfer digital assets protected by IP rights or constituting a trade secret, or to compromise security and integrity of service.

## Article 31 — Lighter regime (custom-built and test/beta)

### 31(1) — Custom-built carve-out

The following obligations do **not** apply to data processing services where the majority of main features are custom-built for one customer or all components are developed for one customer, AND the service is not offered at broad commercial scale:
- Art. 23(d) — functional-equivalence obstacle removal
- Art. 29 — switching charges regime
- Art. 30(1) and 30(3) — functional equivalence and interoperability standards

Other Chapter VI obligations still apply, including Art. 30(2) open interfaces and Art. 25 contract terms.

A multi-tenant SaaS with customer-specific configuration is NOT custom-built under 31(1).

### 31(2) — Test / beta carve-out

Data processing services provided as a non-production version for testing and evaluation, for a limited period of time, are out of scope of Chapter VI in full.

### 31(3) — Pre-contract disclosure

Before any contract for an Art. 31 service, the provider must inform the prospective customer which Chapter VI obligations do not apply.

## Article 32 — International governmental access and transfer

### 32(1) — General duty

Providers must take adequate technical, organisational and legal measures (including contracts) to prevent international and third-country governmental access to and transfer of non-personal data held in the Union where this would conflict with Union or member-state law.

### 32(2) — Recognition based on international agreement

Third-country court or administrative orders requiring transfer / access are recognised or enforceable only if based on an international agreement (e.g., a mutual legal assistance treaty).

### 32(3) — Conditions in absence of international agreement

If no agreement exists and compliance would risk conflict with Union / national law, transfer / access only takes place where:
- (a) the third-country system requires reasoned, proportionate, specific decisions;
- (b) the addressee may bring a reasoned objection before a competent third-country court;
- (c) that court can take into account the legal interests protected by Union / national law.

### 32(4) — Minimum necessary data

Provide only the minimum amount of data permissible.

### 32(5) — Notify the customer

Inform the customer about the existence of the third-country request before complying, except where the request serves law enforcement purposes and notice would defeat that.

## Cross-cutting Chapter VI principles

- **Switching is between services of the same service type** (Art. 2(9)) — same primary objective, same service model, same main functionalities.
- **Customer is in the driver's seat.** They notify, they choose between three options at end of notice (25(3)), they may extend the transitional period (25(5)).
- **No fees for switching itself from 12 Jan 2027.** Standard service fees and early termination penalties remain permitted.
- **Public-facing pages required.** Art. 26 (switching register), Art. 28 (jurisdiction + measures), Art. 29 (charges info while applicable).
- **The Art. 31 lighter regime is narrow.** Custom-built ≠ customised; test/beta must be time-bound.
- **International access is a default-prevent posture** (Art. 32(1)). Recognition is the exception.

## See also

- `references/timeline.md` — Article 50 dates
- `references/international-access.md` — fuller treatment of Arts. 28 and 32
- `references/often-missed.md` — Arts. 4(10), 4(13), 5(3), 31, and the customer-extend right
