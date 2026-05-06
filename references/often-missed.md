# Often-missed provisions

Constraints lawyers and engineers routinely miss when reading the regulation top-to-bottom. Many of these matter materially in drafting and analysis.

## Article 4(10) — User non-compete and no insights about the manufacturer (favourable to the data holder)

> "The user shall not use the data obtained pursuant to a request referred to in paragraph 1 to develop a connected product that competes with the connected product from which the data originate, nor share the data with a third party with that intent and shall not use such data to derive insights about the economic situation, assets and production methods of the manufacturer or, where applicable the data holder."

Three distinct prohibitions on the user:
1. Develop a competing connected product using the data.
2. Share with a third party with that intent.
3. Derive insights about the manufacturer's / data holder's economic situation, assets, or production methods.

**Drafting implication.** Pre-contract notices and access-channel terms should reference Art. 4(10) so that subsequent enforcement is not impeded by argument about whether the user was on notice. A short clause noting the user's Art. 4(10) constraints belongs in the standard data-access terms of use.

## Article 4(13) — Data holder constraint on use of customer non-personal data (binding on data holder)

> "A data holder shall only use any readily available data that is non-personal data on the basis of a contract with the user. A data holder shall not use such data to derive insights about the economic situation, assets and production methods of, or the use by, the user in any other manner that could undermine the commercial position of that user on the markets in which the user is active."

Two binding limits on the data holder:
1. Use of readily available non-personal data requires a **contract with the user**. Use is not implicit in the sale.
2. The data holder may not derive insights about the user's economic position that could undermine the user's commercial position on its markets.

**Drafting implication.** Internal product-analytics, performance-monitoring, and cross-customer benchmarking pipelines drawn from connected-product or related-service data require an explicit contractual grant from the user. Standard EULAs and SaaS terms should include this grant or anonymise data before such use.

## Article 5(3) — DMA gatekeepers excluded as third parties

> "Any undertaking designated as a gatekeeper, pursuant to Article 3 of Regulation (EU) 2022/1925, shall not be an eligible third party under this Article and therefore shall not:
> (a) solicit or commercially incentivise a user in any manner, including by providing monetary or any other compensation, to make data available to one of its services that the user has obtained pursuant to a request under Article 4(1);
> (b) solicit or commercially incentivise a user to request the data holder to make data available to one of its services pursuant to paragraph 1 of this Article;
> (c) receive data from a user that the user has obtained pursuant to a request under Article 4(1)."

Three distinct prohibitions on gatekeepers (and corresponding data-holder right to refuse a transfer where the recipient is a gatekeeper).

**Drafting implication.** Third-party transfer flows (Art. 5) should include an attestation from the recipient that it is not a designated gatekeeper, and the data holder retains a right to verify. The current Commission list of designated gatekeepers should be checked at the time of each transfer.

## Article 25(5) — Customer's right to extend the transitional period (favourable to the customer)

The customer may extend the transitional period **once** for a length the customer considers more appropriate. This is a one-way ratchet: providers cannot decline.

**Drafting implication.** DPS contracts should not phrase the 30-day transitional period as a fixed limit; the clause should track the regulation by allowing customer-initiated extension. Provider-side internal procedures must accommodate the extension.

## Article 25(4) — Provider's 14-working-day infeasibility window (procedural)

If the 30-day mandatory transitional period is technically infeasible, the provider must justify the infeasibility **in writing within 14 working days** of the switching request. Alternative period ≤ **7 months**.

**Drafting implication.** Internal switching procedures must include a 14-working-day technical assessment gate. Missing it forfeits the right to extend.

## Article 26(b) — Online register obligation (public)

The Art. 26(b) register of data structures, formats, standards, and open interoperability specifications is public. It must be current and updated under Art. 30(4) as standards are published.

**Drafting implication.** Engineering and legal share ownership: legal owns the description, engineering owns the technical content and update cadence.

## Article 28(2) — Website URL must be in the contract

The Art. 28(1) website URL must be **listed in every DPS contract**. Easy to miss in template contracts where the website is referenced informally in marketing collateral but not in the contract body.

## Article 29(4)–(6) — Pre-contract disclosure of fees (during the reduced-charges window)

Until 12 January 2027, providers may charge reduced switching charges (Art. 29(2)). The pre-contract disclosure obligations under 29(4) require the prospective customer to be told about:
- standard service fees;
- early-termination penalties; and
- reduced switching charges that may apply.

This information must be **publicly available** in a dedicated section of the website or otherwise easily accessible (29(6)).

**Drafting implication.** A DPS pricing page that omits switching charges is non-compliant during the reduced-charges window.

## Article 31 — Lighter regime carve-outs

### 31(1) — Custom-built (narrow)

Disapplied: Art. 23(d) functional-equivalence obstacle removal; Art. 29 charges; Arts. 30(1) and 30(3).
Still apply: most of Chapter VI, including Art. 30(2) open interfaces and Art. 25 contract terms.

### 31(2) — Test / beta (broad)

Disapplied: all of Chapter VI.

### 31(3) — Disclosure

Both carve-outs require pre-contract disclosure to the prospective customer of which obligations do not apply.

**Drafting implication.** Beta agreements, evaluation licences, and proof-of-concept arrangements must time-bound the offering to qualify for 31(2). "Indefinite beta" forfeits the carve-out.

## Article 9 — Compensation only between data holder and data recipient

Art. 9 permits compensation between data holder and data recipient (third party). It does **not** permit charging the user for Art. 4 access. Confusing the two leads to unlawful charges on user-side requests.

## Article 11 — Technical protection measures and unauthorised use

Art. 11 allows the data holder to apply technical protection measures. Users / third parties must not circumvent them or use unauthorised data. This is the affirmative right that backs trade-secret protections in code: encryption, watermarking, access tokens.

## Article 27 — Good-faith cooperation in switching

> "All parties involved, including destination providers of data processing services, shall cooperate in good faith to make the switching process effective, enable the timely transfer of data and maintain the continuity of the data processing service."

Often missed because it is short. It binds the **destination provider** as well as the source — relevant when the destination provider is uncooperative on data-format issues.

## Article 5(1) is independent of how the user accesses data

Per FAQ Q31 (non-authoritative), even if the user has direct access via the device, the data holder must support Art. 5 third-party transfer on request. Direct access does not extinguish the third-party-transfer obligation.

## Recital 31 final sentence — trade-secret refusal does not displace GDPR access rights

> "The exceptions to data access rights in this Regulation should not in any case limit the right of access and right to data portability of data subjects under Regulation (EU) 2016/679."

A refusal letter that purports to deny GDPR Art. 15 / 20 rights on Data Act trade-secret grounds is invalid.

## Article 7 — SME / micro-enterprise carve-outs

Micro-enterprises and small enterprises are excluded from data-holder obligations under Chapter II, subject to specific conditions. Medium enterprises in their first year of meeting the threshold also benefit. The skill flags this; the lawyer must verify size status and whether the carve-out applies.

## Article 12 — Member-state extension to SMEs

Member states may extend Chapter II to SMEs in specific sectoral regimes. Always check member-state implementing law.
