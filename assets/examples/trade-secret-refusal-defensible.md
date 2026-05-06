# Worked Example — Defensible Article 4(8) Trade-Secret Refusal

A scenario in which an exceptional refusal under Article 4(8) is potentially defensible, walking the substantiation each element requires.

> The example illustrates how the Skill walks the trade-secret ladder under `references/trade-secret-ladder.md` and `assets/decision-trees/trade-secret-refusal.md`.

---

## Facts (hypothetical)

- A specialist semiconductor manufacturer makes a connected wafer-inspection tool.
- The tool generates inspection data and uploads it to a SaaS owned by the manufacturer.
- Embedded in the inspection-data stream is "calibration profile" data — a proprietary fingerprint of the imaging sensors that took the manufacturer many years and substantial investment to develop. The fingerprint enables high-resolution defect detection.
- A competitor of the manufacturer has acquired one of the manufacturer's tools through a customer's secondary market and is the user of that tool.
- The competitor requests access to the calibration-profile data under Article 4(1).

## Step 1 — Article 4(6)

The manufacturer:
- Identifies the calibration profile in the metadata as trade-secret-protected.
- Proposes confidentiality measures to the competitor: a confidentiality agreement under Art. 4(6); strict access protocols; technical-protection measures restricting onward use; an explicit Art. 4(10) non-compete acknowledgement.
- The competitor refuses to enter into the confidentiality agreement, asserting that the data should be released under Art. 4(1) without restriction.

**No agreement on Art. 4(6) measures.** The first trigger of Art. 4(7) is met.

## Step 2 — Article 4(7)

The manufacturer:
- Withholds the sharing of the calibration-profile data, in writing to the competitor, without undue delay.
- Substantiates the withholding: identifies the specific data category, the proposed measures, and the competitor's refusal.
- Notifies the competent authority designated under Art. 37 of the Member State in which the manufacturer is established.

The withholding is **reversible**. The manufacturer remains willing to disclose if measures are agreed.

The competitor does not return to negotiate measures.

## Step 3 — Article 4(8)

The manufacturer assesses whether to escalate to exceptional refusal under Art. 4(8). The threshold is: highly likely to suffer **serious AND irreparable** economic loss from disclosure, despite measures the user *could have* taken.

Substantiation on objective elements:

### (a) Enforceability of trade-secret protection in third countries

The competitor operates principally in jurisdictions with weak trade-secret enforcement. The competitor has subsidiaries in those jurisdictions. The manufacturer documents that any onward use of the calibration profile in those jurisdictions would not be enforceable through trade-secret claims.

### (b) Nature and level of confidentiality

The calibration profile has not been disclosed in any patent application, product manual, or third-party context. Access internally is restricted to a small engineering team under a strict access protocol. The data is the manufacturer's primary engineering asset for high-resolution detection. The data is highly confidential within Art. 2(18) of the Data Act and Article 2(1) of Directive (EU) 2016/943.

### (c) Uniqueness and novelty

The wafer-inspection tool is novel in the market. No other manufacturer has demonstrated the equivalent calibration approach. The tool's competitive advantage rests substantially on the calibration profile. Disclosure to a direct competitor would materially undermine this competitive advantage.

### (d) Cybersecurity impact

[On the assumed facts, cybersecurity impact is not the primary substantiation. If the calibration profile included authentication artefacts, this would also support the analysis.]

### (e) Highly likely serious and irreparable economic loss

The manufacturer projects a quantifiable loss of competitive advantage. Specifically, the manufacturer relies on the calibration profile for differentiation against [INSERT — competitor type] competitors, and the resulting loss of revenue and margin from such disclosure is documented in the manufacturer's financial planning. The disclosure is irreversible — once the competitor has the calibration profile, no measure can recover the secret. The loss is **serious AND irreparable** within Recital 31.

## Step 3 — refusal letter

The manufacturer issues a refusal letter under Art. 4(8) using template `trade-secret-refusal-letter.md`:

- Refers to the prior Step 1 confidentiality offer and the competitor's refusal (sections 1, 2).
- Substantiates each of (a) to (d) above (section 3).
- Limits the refusal to the calibration-profile data category — **not** other inspection data the competitor is entitled to (section 4).
- Confirms competent-authority notification (section 5).
- Sets out the competitor's complaint / dispute / court rights (section 6).

## Why this refusal is defensible

- **Procedure followed.** Steps 1, 2, 3 attempted in order.
- **Specific data identified.** Not blanket refusal across all inspection data.
- **Objective substantiation.** Each element of Art. 4(8) addressed with facts, not conclusory assertions.
- **Threshold met.** Serious AND irreparable economic loss articulated.
- **Notification made.** Competent authority informed at each step.
- **GDPR rights preserved.** No personal-data access is being refused (Recital 31 final sentence).

## Where this could fail

- If the manufacturer skipped Step 1 and went straight to Art. 4(8), an Article 38 complaint would probably succeed.
- If the substantiation in section 3 was conclusory ("disclosure would damage the business"), the refusal is unlikely to satisfy "objective elements."
- If the refusal was blanket over all inspection data, it would not be "case-by-case basis."
- If the manufacturer failed to notify the competent authority, the refusal would be procedurally defective.

## Contrast — `trade-secret-refusal-not-defensible.md`

The non-defensible counterpart example (`trade-secret-refusal-not-defensible.md`) shows the same facts with procedural and substantive defects.
