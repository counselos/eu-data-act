# Safety / security carve-out — Article 4(2)

A narrow ground for restricting access. Distinct from the trade-secret ladder.

## Article 4(2) verbatim

> "Users and data holders may contractually restrict or prohibit accessing, using or further sharing data, if such processing could undermine security requirements of the connected product, as laid down by Union or national law, resulting in a serious adverse effect on the health, safety or security of natural persons. Sectoral authorities may provide users and data holders with technical expertise in that context. Where the data holder refuses to share data pursuant to this Article, it shall notify the competent authority designated pursuant to Article 37."

## Cumulative conditions

All of the following must hold for an Art. 4(2) restriction to be lawful:

1. **Identifiable security requirement under Union or national law** — not a generic security concern. There must be a specific legal requirement (sectoral or horizontal).
2. **Processing the data could undermine that requirement** — direct causal link between disclosure and the undermining.
3. **The undermining results in a serious adverse effect on health, safety or security of natural persons** — natural persons, not corporate interests.
4. **The restriction is contractual** — agreed with the user. A unilateral refusal without contractual basis does not fit Art. 4(2).
5. **Competent-authority notification** when refusal occurs — Art. 4(2) sentence 3.

## What Art. 4(2) is not

- It is not a generic "we don't want to share for security reasons" excuse.
- It is not a blanket category exclusion. It must address specific risks to specific natural persons.
- It is not a substitute for the trade-secret ladder (Arts. 4(6)–(8)). Different test, different procedure.
- It is not retroactive. The contractual restriction must have been agreed before the request.
- It does not displace GDPR (Art. 1(5)) where personal data is involved.

## Sectoral law that may engage Art. 4(2)

Common Union-law security requirements likely to support Art. 4(2):

- **NIS2** (Directive (EU) 2022/2555) — cybersecurity risk-management for essential / important entities.
- **Cyber Resilience Act** (Regulation (EU) 2024/2847) — security requirements for products with digital elements.
- **MDR / IVDR** (Regulations (EU) 2017/745, 2017/746) — medical device safety and performance.
- **Type-approval Regulation** (Regulation (EU) 2018/858) — vehicle safety provisions.
- **DORA** (Regulation (EU) 2022/2554) — operational resilience for financial entities.
- **NIS / Critical Infrastructure** national implementing measures.

National-law requirements (member-state) also count. The skill flags but does not enumerate per member state.

## Practical drafting

### Restriction clause (data holder–user contract)

A starting-point clause is at `assets/templates/safety-security-restriction-clause.md`. The clause should:

- Identify the specific data elements covered.
- Identify the specific Union or national security requirement engaged.
- Articulate the causal link between disclosure and undermining the requirement.
- Identify the natural persons whose health, safety or security is at risk.
- Reserve the right to refuse on Art. 4(2) grounds when the conditions are met.
- Commit to notify the competent authority on any refusal.

### Refusal letter

When an Art. 4(2) refusal is invoked, the letter should:
1. Recite the cumulative conditions and how each is met on the specific facts.
2. Identify the data withheld at category level.
3. Identify the underlying Union / national security requirement.
4. Identify the affected natural persons.
5. Confirm competent-authority notification.
6. Confirm that the refusal is specific, not blanket.

## Interaction with trade-secret refusal (Recital 31)

Recital 31 notes that "a possible negative impact on cybersecurity can be taken into account" in the trade-secret refusal context (Art. 4(8)). This means cybersecurity impact may be evidence in either:
- An Art. 4(2) safety/security restriction, OR
- An Art. 4(8) trade-secret exceptional refusal.

The two grounds are distinct but can co-exist. The choice between them depends on the underlying source of the harm:
- Harm flows from undermining a specific security-law requirement → Art. 4(2).
- Harm flows from disclosure of trade-secret-protected information that creates serious + irreparable economic loss → Art. 4(8).

A refusal letter can rely on both, in the alternative, if the facts support each independently.

## Competent-authority notification

Art. 37 designates competent authorities at member-state level. The notification should:

- Be in writing.
- Identify the data withheld and the legal basis (Art. 4(2) and / or Art. 4(8)).
- Provide the substantiation provided to the user.
- Reference the underlying security requirement (for 4(2)) or the objective elements of serious + irreparable economic loss (for 4(8)).

The skill does not enumerate competent authorities by member state. The lawyer must verify the relevant authority for the member state in question.
