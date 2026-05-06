# Worked Example — Multi-user rental scenario (employer / employee / lessor)

Pattern: a connected product is owned by a rental company, rented to a service provider, operated by the service provider's employee on a third-party customer's site.

This example walks the user-identification analysis under Art. 2(12) and FAQ Q14 / Q16, the GDPR overlay, and the practical implications for the data holder's access flow.

---

## Facts (hypothetical)

- The Manufacturer makes a connected industrial measurement instrument.
- The Manufacturer sells the instrument to RentalCo, which buys the instrument and includes it in its rental fleet.
- RentalCo rents the instrument to ServiceCo for two weeks under a rental contract.
- ServiceCo's employee, the Operator, takes the instrument to EndCustomer's site to perform a measurement.
- The instrument generates measurements during the use, including ambient conditions and equipment performance.
- The Manufacturer hosts a SaaS that the instrument uploads to. RentalCo and ServiceCo have separate accounts.
- The Operator's identity is not recorded by the instrument or the SaaS.

## Question

Who is "the user" under the Data Act?

## Analysis

### Article 2(12) and FAQ Q14

Article 2(12): a "user" is a natural or legal person that owns a connected product, or to whom temporary contractual rights to use it have been transferred, or that receives a related service.

FAQ Q14 (non-authoritative): the user must have a "stable right" — ownership or rent / lease contract — that pertains to the object. A passenger using an aircraft is not the user.

### Applying to the facts

- **RentalCo** — owns the instrument. **User under Art. 2(12).**
- **ServiceCo** — has temporary contractual rights to use the instrument under the rental contract. **User under Art. 2(12).** (FAQ Q16 confirms multi-user scenarios.)
- **Operator (the employee)** — operates the instrument on ServiceCo's behalf. **NOT a user under Art. 2(12)** — operating company equipment as an employee does not transfer property-type rights. (FAQ Q14 airline-passenger comparison.)
- **EndCustomer** — the site owner where the measurement occurs. **NOT a user** — EndCustomer has no contractual right over the instrument itself. (Even if EndCustomer's premises sensors generated similar data, that does not give EndCustomer rights over the instrument's data.)

### Multi-user mechanism

FAQ Q16 (non-authoritative): "data holders should have mechanisms in place to ensure that each user can access the data to which they are entitled."

For the Manufacturer (data holder), this means:

- A clear segregation in the SaaS / data layer between RentalCo's account and ServiceCo's account.
- A policy on what data is accessible to whom for the rental period:
  - During the rental period, ServiceCo (as renter) is entitled to access the data generated during its use.
  - RentalCo (as owner) is entitled to access — but the data generated during ServiceCo's rental period may include personal data of the Operator, in which case RentalCo's access is constrained by GDPR.
- After the rental period ends, only RentalCo retains user status. ServiceCo's access right ceases prospectively, though data already retrieved by ServiceCo during the rental remains with ServiceCo.

### GDPR overlay (referencing `references/gdpr-overlay.md`)

If the data generated during the Operator's use includes personal data of the Operator (e.g., timestamps tied to the Operator's identity, geolocation that maps to the Operator, biometric authentication on the device), then:

- **Operator** is the data subject, but **NOT** the Data Act user.
- **ServiceCo** (the user) is **not the data subject** for that personal data — Case B from `references/gdpr-overlay.md`.
- The Data Act is **not** a GDPR Art. 6 legal basis for ServiceCo's access (Recital 7; FAQ Q25a).
- The Manufacturer (data holder) must establish a separate Article 6 basis (e.g., contract necessity for the rental, legitimate interest of ServiceCo as employer balanced against employee rights) OR provide the data anonymised / aggregated.

This is the common employer-requesting-employee-data trap. It must be flagged as a privacy review trigger before any disclosure.

### EndCustomer

EndCustomer is not a user. If EndCustomer wants the data (e.g., to verify a measurement on its own equipment), the routes are:

- ServiceCo (as user) requests the data and shares it with EndCustomer pursuant to a separate commercial agreement (not Article 5 — Article 5 is for transfer to a third party at the user's request, but the third party would be EndCustomer; check the gatekeeper screening).
- ServiceCo invokes Article 5 to direct the Manufacturer to share with EndCustomer.

### Operator and personal data

The Operator may have GDPR Art. 15 rights to the personal data the Manufacturer holds about them. These are independent of the Data Act and operate alongside.

## Outputs the lawyer might produce

For RentalCo or ServiceCo (user side):

- Data access request under Article 4(1) (template `third-party-data-sharing-request.md` adapted, or a direct request).
- Verification checklist on receipt (`data-export-verification-checklist.md`).

For the Manufacturer (data holder side):

- Pre-contract notices that anticipate multi-user scenarios.
- Internal policy on multi-user access in the SaaS.
- Privacy-review gate on disclosures that include personal data of operators where the requester is the employer.

## Open questions the memo flags

- Does the rental contract address Data Act user status explicitly? If not, both RentalCo and ServiceCo may make competing access requests; the Manufacturer should have a documented policy.
- Does the SaaS collect Operator personal data? If so, what is the GDPR posture for ServiceCo's access?
- Is the Operator's identity recoverable from the data alone (e.g., via behavioural patterns)? Even pseudonymous data may be personal data under GDPR.
- Are EndCustomer's premises subject to a separate data regime (e.g., EndCustomer is a NIS2 essential entity)? Sectoral overlay may apply.
