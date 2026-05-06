# Worked Example — SaaS that controls a connected device

A common pattern: a hardware manufacturer offers a connected device, and a SaaS that the customer uses to configure, monitor, and control the device. The SaaS is tenant-isolated, multi-tenant cloud-hosted.

This example walks the classification analysis the Skill should produce.

---

## Facts (hypothetical)

- A company manufactures a connected industrial measurement instrument.
- The instrument logs measurements (current, voltage, temperature) and uploads them to a SaaS hosted on a multi-tenant cloud.
- Customers access the SaaS to view dashboards, configure measurement parameters that are pushed back to the instrument, and download exports.
- The SaaS is sold to enterprise customers under a subscription contract.
- The customer's employees operate the instrument on the customer's premises.

## Classification

### Q1 — Connected product (Art. 2(5))

- (1a) The instrument generates and collects use and environment data (current, voltage, temperature). **YES.**
- (1b) The instrument can communicate the data to the SaaS — electronic communications service. **YES.**
- (1c) The instrument's primary function is measurement, not data storage / transmission for someone else. **YES.**

**Conclusion:** the instrument is a connected product.

### Q2 — Related service (Art. 2(6))

- (2a) The SaaS is a digital service / software, other than electronic communications service. **YES.**
- (2b) The SaaS is connected with the instrument at the time of sale (sold together) or added later. **YES** (assumed sold together).
- (2c) The SaaS adapts and configures the instrument's measurement parameters and is needed for the instrument's full functionality. **YES.**

FAQ Q10 indicators: bidirectional data exchange (YES — measurements up, configurations down); affects product function (YES). Both indicators support classification.

**Conclusion:** the SaaS is a related service.

### Q3 — DPS (Art. 2(8))

- (3a) Provided to a customer (Art. 2(30) — contractual relationship). **YES.**
- (3b) Ubiquitous + on-demand network access. **YES** (cloud-hosted, network-accessible).
- (3c) Shared, scalable, elastic resources. **YES** (multi-tenant cloud).
- (3d) Rapid provisioning / release with minimal interaction. **YES** (typical SaaS provisioning).

**Conclusion:** the SaaS is a DPS.

### Q4 — Overlap

Q2 and Q3 are both YES. **Both regimes apply.** Chapter II governs access to product data and related-service data; Chapter VI governs DPS switching, portability, interoperability, and international access.

DPS scope nuance:
- Art. 30(1) functional equivalence — N/A (this is SaaS, not IaaS).
- Art. 30(2) open interfaces — applies.
- Art. 30(3) interoperability standards — applies (12-month compatibility horizon).
- Arts. 25, 26, 28, 29 — apply.

### Q5 — Article 31 carve-outs

Multi-tenant SaaS sold to multiple enterprise customers does **not** qualify under Art. 31(1) (commercial-scale catalogue offering). Not a non-production beta either, on the assumed facts. **Article 31 does not apply.**

### Q6 — Article 7 SME

Assuming the manufacturer is not a micro or small enterprise as defined, Article 7 does not apply.

### Q7 — Sectoral overlay

[On the assumed facts, no specific sector is engaged. If the customer is, e.g., a financial entity, DORA may add ICT-third-party requirements.]

## Outputs the manufacturer must produce

Given the classification:

| Output | Article | Side | Status |
|--------|---------|------|--------|
| Pre-contract notice for connected product | Art. 3(2) | Data Holder | Required at sale |
| Pre-contract notice for related service | Art. 3(3) | Data Holder | Required at SaaS subscription |
| DPS contract clauses (Art. 25) | Art. 25 | Data Holder (DPS provider) | Required in SaaS contract |
| Public switching info + register | Arts. 26 + 30(4) | Data Holder | Required public page |
| Public Art. 28 jurisdiction + measures page | Art. 28 | Data Holder | Required public page; URL listed in contract |
| Public reduced-charges info (until 12 Jan 2027) | Art. 29 | Data Holder | Required public page |
| Open interfaces (Art. 30(2)) | Art. 30(2) | Data Holder | Required for switching |
| Indirect-access mechanism for product data + related-service data | Art. 4(1) | Data Holder | Required (12 Sep 2025) |
| Trade-secret confidentiality agreement template | Art. 4(6) | Data Holder | Available on request |

The lawyer's classification memo for this offering states the bottom line in section 1, walks Q1–Q7 in section 4, and recommends the outputs above in section 9.

## Two-flow architecture

Because both Chapter II and Chapter VI apply, the manufacturer's customer-facing portal should expose two logically distinct flows:

- **Flow A (Chapter II)** — User access to product data and related-service data. Requester: Data Act user (the customer entity). Free of charge. Format: structured machine-readable.
- **Flow B (Chapter VI)** — DPS customer switching / export. Requester: the DPS customer (the contracting entity). Subject to Art. 25 timing (notice ≤ 2 mo, transitional 30 days, retrieval ≥ 30 days, erasure).

A single portal can serve both, with clearly labelled sections.

## Open questions the memo flags

- Where do employees of the customer fit (Art. 2(12))? Likely not users; the contracting entity is the user. Personal data of employees is governed by GDPR; if the customer requests employee personal data, see `references/gdpr-overlay.md` Case B.
- Are any data fields trade-secret-protected? If so, prepare Art. 4(6) measures.
- Is the Customer in a sector that engages sectoral overlay (DORA / NIS2)?
- Is the Customer in a Member State whose competent authority has issued specific guidance?
