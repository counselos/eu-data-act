# Timeline — Article 50 (entry into force and application)

Four load-bearing dates, plus the entry-into-force date. Read full verbatim from `assets/source/regulation-2023-2854.md`.

## Article 50 verbatim

> "This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.
>
> It shall apply from 12 September 2025.
>
> The obligation resulting from Article 3(1) shall apply to connected products and the services related to them placed on the market after 12 September 2026.
>
> Chapter III shall apply in relation to obligations to make data available under Union law or national legislation adopted in accordance with Union law, which enters into force after 12 September 2025.
>
> Chapter IV shall apply to contracts concluded after 12 September 2025.
>
> Chapter IV shall apply from 12 September 2027 to contracts concluded on or before 12 September 2025 provided that they are:
> (a) of indefinite duration; or
> (b) due to expire at least 10 years from 11 January 2024.
>
> This Regulation shall be binding in its entirety and directly applicable in all Member States."

## Date table

| Date | Trigger | Source |
|------|---------|--------|
| 11 January 2024 | Entry into force (20 days after OJ publication on 22.12.2023). Start of reduced-charges window. | Art. 50; Art. 29(2) |
| **12 September 2025** | General application date. Chapter II rights start. **Chapter VI applies in full to all DPS contracts (new and pre-existing) — no grandfather.** Chapter III data-availability obligations from this date forward. Chapter IV applies to B2B data-sharing contracts concluded after this date. | Art. 50 |
| **12 September 2026** | Article 3(1) (access by design) applies to connected products and related services placed on the market AFTER this date. | Art. 50 |
| **12 January 2027** | All switching charges prohibited (no charges for the switching process itself). | Art. 29(1) |
| **12 September 2027** | **Chapter IV only.** Chapter IV applies to pre-existing B2B data-sharing contracts (concluded on or before 12 September 2025) that are of indefinite duration OR due to expire ≥ 10 years from 11 January 2024. **This grandfather does NOT extend any Chapter VI deadline.** | Art. 50 |
| 12 September 2028 | Commission evaluation report due. | Art. 49(2) |

## Common errors to avoid

- **The 12 September 2026 access-by-design line does not exempt earlier products from Article 4(1).** Connected products and related services placed on the market BEFORE 12 September 2026 are still subject to Article 4(1) indirect-access duty. Only the design-by-default obligation in Article 3(1) is gated on the 2026 date.
- **The 12 January 2027 charge prohibition concerns switching charges only.** Standard service fees and early-termination penalties remain permitted.
- **The 12 September 2027 trigger is easy to miss for B2B data-sharing contracts within Chapter IV's scope.** Pre-existing indefinite or long-duration B2B data-sharing contracts (Art. 13 unfair-terms regime) need to be in compliance with Chapter IV by this date. This date does NOT govern Chapter VI / DPS switching obligations — those applied from 12 September 2025.
- **Do not apply the 12 September 2027 grandfather to DPS contracts on their Chapter VI obligations.** Article 50's 12 September 2027 grandfather is for Chapter IV (unfair B2B data-sharing contractual terms — Art. 13) only. Chapter VI obligations (Art. 25 switching clauses, Art. 26 transparency, Art. 28 international-access disclosure, Art. 29 fees, Art. 30 interfaces / functional equivalence) applied from 12 September 2025 to all DPS contracts, including pre-existing ones, with no transition period. A pre-existing DPS contract that is also a B2B data-sharing contract within Chapter IV's scope may benefit from the 2027 grandfather for those Chapter IV terms only.

## How the skill uses this

- For drafting deliverables: the skill computes which obligations apply given the offering's "placed on market" date (or, for DPS, the contract start date and duration).
- For audit deliverables: the skill flags any date that has passed without remediation as a HIGH severity item.
- The script `scripts/timeline_check.py` accepts a launch date (or contract start date + duration) and returns the applicable obligations.

## See also

- `references/chapter-6-dps.md` — Art. 25 / 29 / 50 interplay
- `references/chapter-2-access.md` — Art. 3(1) by-design vs Art. 4(1) indirect access
