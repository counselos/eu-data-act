# Per-matter facts — capture before output

The skill captures four facts at the start of each matter and holds them in conversation memory for the duration of the conversation. They are NOT written to any file and they are NOT stored in the global config; they are matter-specific and live only in the active conversation.

## Categories

### 1. Side advised

- **data holder** — the lawyer represents the manufacturer / DPS provider / service provider that holds the data
- **user** — the lawyer represents the customer / lessee / data-subject-equivalent receiving the related service
- **third party** — the lawyer represents a recipient of an Article 5 transfer
- **both / not yet known** — surface as an open question

The skill changes its drafting framing depending on side. A trade-secret refusal letter (data-holder side) is structurally different from a complaint to the competent authority (user side).

### 2. Sector indicators

Scan the facts for the trigger keywords listed in `references/sectoral-overlays.md`. Capture each match.

If multiple sectoral indicators apply, all are captured and all relevant warnings are surfaced.

### 3. Member state(s) involved

Look for member-state references in the facts:
- Place of establishment of the data holder.
- Place of establishment of the user.
- Place where the connected product is placed on the market.
- Place of the ICT infrastructure for a DPS.

If multiple member states are implicated (e.g., German manufacturer, French customer), capture both and note the choice-of-law / forum considerations as an open question.

## How to capture

Ask the lawyer once at the start of the matter, then persist. **Use the inline A/B/C/D format defined in `references/asking-questions.md` for every question.**

If the lawyer has already provided a fact in the original request, do not re-ask — capture it from context and proceed. Only ask for facts that are missing.

### Question 1 — Side advised

```
**Which side does the lawyer represent on this matter?**

  A) **Data Holder** — the manufacturer / DPS provider / service provider that holds the data *(most frequent — assume unless otherwise stated)*
  B) User — the customer, lessee, employer, or related-service recipient
  C) Third party — the recipient of an Article 5 transfer
  D) Both / mixed — internal advice spanning multiple parties

Reply A / B / C / D, or describe.
```

### Question 2 — Sector indicators (multiple-select)

```
**Does the offering touch any of these sectors? (you can pick more than one)**

  A) No specific sector — horizontal commercial / industrial use
  B) Automotive — Regulation 2018/858 (type-approval) may overlay
  C) Medical device — MDR / IVDR may overlay
  D) Other regulated sector — financial / NIS2 / AI Act / energy / public sector / eIDAS — describe

Reply with letters separated by commas (e.g., B, D), or describe.
```

### Question 3 — Member state(s)

This one asks for a fact, not a choice. Ask open-ended:

> Which EU member state(s) are material to the matter (place of establishment of data holder, user, ICT infrastructure, or contract jurisdiction)?

If the lawyer's answer mentions multiple states, capture all. If unclear, do not block — flag as an open question and proceed.

## Update during conversation

If the lawyer supplies new facts mid-conversation that change a captured category (e.g., introduces an additional member state, adds a sector indicator), refresh the captured facts in conversation memory and re-run the sectoral-overlay gate before the next output.

## Privilege

Captured facts may include privileged information about clients, matters, and offerings. The skill holds these facts only in active conversation memory:

- No file is written. Facts are not persisted to disk by the skill.
- No facts are transmitted by the skill.
- No facts are logged to any telemetry.

## Reset

If the lawyer says "new matter" or "different client," discard the captured facts and start the capture flow again from Question 1. Do not carry facts across matters.
