# Asking the lawyer a question — convention

The skill follows one consistent format for every choice it needs from the lawyer. Lawyers do not want pop-up overlays and they do not want to compose long answers; they want to read four well-framed options, pick a letter, and move on.

This file defines the format. Apply it for every clarification, mode selection, fact capture, or decision point.

## Primary format — inline A / B / C / D

```
**[Question text, ending with a question mark]**

  A) **[Recommended option]** — [short description] *(Recommended — [why])*
  B) [Option label] — [short description]
  C) [Option label] — [short description]
  D) [Option label] — [short description]

Reply A / B / C / D, or describe.
```

Rules:

- Up to **four** options. If you need more than four, the choice is too coarse — split it.
- The **recommended** option (if any) is **first** in the list, **bolded**, and labelled `*(Recommended — [reason])*`.
- Each option line is one line: `LETTER) Label — description`.
- Question text is bold.
- The closing line `Reply A / B / C / D, or describe.` is always present so the lawyer knows free text is accepted.
- Letters are uppercase A–D so they're easy to type without holding shift on most keyboards.
- Treat the lawyer's answer as case-insensitive; a bare `b`, `B)`, `B.`, or `Option B` all map to option B. Anything else is free text — interpret on the merits.

## When to ask

Ask only when:
- The information is required to produce the deliverable correctly.
- The information has not already been captured earlier in the same conversation.
- There are 2–4 distinct, mutually exclusive options the lawyer should choose between.

## When NOT to ask

- A single option is overwhelmingly correct — just proceed and surface the assumption.
- The needed input is a fact (date, name, member state, ID number) — ask open-ended instead.
- The skill could infer the answer from facts already supplied.
- The question is a yes/no the lawyer would always say yes to (e.g., "May I cite the regulation?") — don't ask, just do it.

## Yes / no variant

For binary choices, use the same format with two options:

```
**[Question]?**

  A) Yes
  B) No

Reply A or B, or describe.
```

If a recommended answer exists, mark it in the same way:

```
**Is the offering placed on the market after 12 September 2026?**

  A) **Yes** *(Recommended starting position — triggers Art. 3(1) by-design)*
  B) No

Reply A or B, or describe.
```

## Multiple-select variant

Some matters legitimately involve multiple selections (e.g., sector indicators when the client is in two regulated industries). For those, use:

```
**[Question — phrased to allow multiple]? (you can pick more than one)**

  A) [Option] — [description]
  B) [Option] — [description]
  C) [Option] — [description]
  D) [Option] — [description]

Reply with letters separated by commas (e.g., A, C), or describe.
```

## Optional richer UI — `AskUserQuestion`

When the skill is running inside Claude Code (which exposes the `AskUserQuestion` tool), the skill MAY use that tool to produce a clickable UI with the same options. Mapping:

- `question` field = the bold question text above
- `header` field = a short chip label (e.g., "Mode", "Side", "Sector")
- `options` array — first option corresponds to the recommended choice, with `(Recommended)` in its label per the AskUserQuestion convention
- The `description` field on each option matches the inline format's short description
- Set `multiSelect: true` when using the multiple-select variant

When the platform does **not** expose `AskUserQuestion` (Codex CLI, other agents, plain chat), use the inline A/B/C/D format always. Default to inline.

## Examples

### Example 1 — Mode menu (when `/data-act` is invoked without arguments)

```
**Which mode?**

  A) **classify** — is the offering a connected product / related service / DPS / overlap? *(Recommended when starting a new matter)*
  B) draft — pre-contract notice / Art. 25 clauses / refusal letter
  C) lookup — verbatim regulation / FAQ text by reference
  D) analyze — apply the regulation to specific facts

Reply A / B / C / D, or describe.
```

### Example 2 — Side advised

```
**Which side does the lawyer represent on this matter?**

  A) **Data Holder** — the manufacturer / DPS provider / service provider that holds the data *(most frequent — assume unless otherwise stated)*
  B) User — the customer, lessee, employer, or related-service recipient
  C) Third party — the recipient of an Article 5 transfer
  D) Both / mixed — internal advice spanning multiple parties

Reply A / B / C / D, or describe.
```

### Example 3 — Sector overlay (multiple-select)

```
**Does the offering touch any of these sectors? (you can pick more than one)**

  A) No specific sector — pure horizontal commercial / industrial use
  B) Automotive — Regulation 2018/858 (type-approval) may overlay
  C) Medical device — MDR / IVDR may overlay
  D) Financial services / NIS2 / AI Act / other — describe

Reply with letters separated by commas (e.g., B, D), or describe.
```

### Example 4 — Drafting choice

```
**Which trade-secret response is the matter at?**

  A) **Step 1 — propose Art. 4(6) measures** *(Recommended starting point — refusal is exceptional)*
  B) Step 2 — withhold or suspend under Art. 4(7) (measures not agreed or breached)
  C) Step 3 — exceptional refusal under Art. 4(8) (highly likely serious + irreparable economic loss)
  D) Not sure — walk me through the decision tree

Reply A / B / C / D, or describe.
```

### Example 5 — DPS contract status check

```
**Is the contract concluded after 12 September 2025?**

  A) **Yes — concluded after 12 Sep 2025** *(Recommended assumption for new contract drafting work)*
  B) No — concluded on or before 12 Sep 2025; indefinite or ≥ 10-year remaining
  C) No — concluded on or before 12 Sep 2025; fixed term ending earlier
  D) Not sure — need to check facts

Reply A / B / C / D, or describe.
```

## Why this convention

- **Portable.** Works identically across Claude Code, Codex CLI, any agent that can read markdown.
- **Fast.** One letter to reply.
- **Visible default.** A lawyer who isn't sure can pick the recommended option safely.
- **Reasoned default.** The lawyer sees *why* it's recommended.
- **Free text always allowed.** Lawyers whose facts don't match any option can type anything.
- **Persists in the transcript.** Inline answers remain readable when the lawyer reviews the matter weeks later. Pop-up answers don't survive the transcript as well.
