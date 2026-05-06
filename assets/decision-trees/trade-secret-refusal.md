# Decision Tree — Trade-Secret Refusal

Walkable Q&A for analysing whether a refusal on trade-secret grounds is defensible. Follows the three-step ladder of Articles 4(6) → 4(7) → 4(8) (mirrored at 5(9)–(11)).

---

## Q1. Is any of the requested data trade-secret-protected?

The "trade secret" definition is in Art. 2(18) (referring to Directive (EU) 2016/943 Art. 2(1)). Three cumulative elements:

- (1a) The data is secret (not generally known among or readily accessible to persons within the relevant circles).
- (1b) It has commercial value because it is secret.
- (1c) The holder has taken reasonable steps to keep it secret.

Branching:

- Any element NO → not a trade secret. The trade-secret regime is unavailable. (Other refusal grounds — e.g., Art. 4(2) safety/security — may still apply.)
- All three YES → proceed to Q2.

---

## Q2. Have Article 4(6) measures been attempted?

The default position under Recital 31 is **disclose with confidentiality measures.** Step 1 is mandatory.

- (2a) Has the data holder identified the trade-secret data, including in metadata, before disclosure?
- (2b) Has the data holder proposed to the user proportionate technical and organisational measures (model contractual terms, confidentiality agreements, strict access protocols, technical standards, codes of conduct)?
- (2c) Has the user agreed and implemented those measures?

Branching:

- (2c) YES → disclose with measures in place. Refusal is not the right action. Stop.
- (2c) NO → proceed to Q3 (Step 2).

Common error: jumping to Step 3 refusal without first attempting Step 1.

---

## Q3. Are the conditions for withhold / suspend (Art. 4(7)) met?

Triggers (any one):

- (3a) No agreement on the measures referred to in Art. 4(6).
- (3b) The user fails to implement the agreed measures.
- (3c) The user undermines the confidentiality of the trade secrets.

Branching:

- Any YES → withhold or suspend in writing without undue delay. Notify competent authority. Use template `trade-secret-withhold-suspend-letter.md`. Proceed to Q4 only if the trigger persists AND the conditions of Art. 4(8) are met.
- All NO → no basis for Step 2. Re-attempt Step 1.

The Art. 4(7) action is reversible. Sharing should resume once measures are agreed / implemented.

---

## Q4. Are the conditions for exceptional refusal (Art. 4(8)) met?

Cumulative threshold: the data holder, who is a trade-secret holder, demonstrates that **despite** the measures taken under Art. 4(6), it is **highly likely** to suffer **serious and irreparable economic loss** from disclosure (Recital 31).

Substantiation must be on objective elements, including in particular:

- (4a) Enforceability of trade-secret protection in third countries.
- (4b) Nature and level of confidentiality of the data requested.
- (4c) Uniqueness and novelty of the connected product.
- (4d) Cybersecurity impact (Recital 31).

Branching:

- All four (or a cumulatively persuasive subset) supported by objective elements, AND the loss is highly likely AND serious AND irreparable → exceptional refusal is potentially defensible. Proceed to Q5.
- Any deficiency → exceptional refusal is not defensible. Re-attempt Step 1 and / or Step 2.

---

## Q5. Procedural requirements for the refusal

If Q4 is YES:

- (5a) Refuse on a **case-by-case basis** for the **specific data in question**. Not blanket.
- (5b) Refuse **in writing** to the user **without undue delay**.
- (5c) Substantiate the refusal in writing.
- (5d) Notify the competent authority designated under Art. 37.
- (5e) Confirm that the refusal does **not** purport to limit the data subject's GDPR Art. 15 / 20 rights (Recital 31 final sentence).

Use template `trade-secret-refusal-letter.md`.

---

## Q6. Has the user contested?

If the user contests:

- (6a) Lodge a complaint with the competent authority under Art. 38, OR
- (6b) Refer to a certified dispute settlement body under Art. 10, OR
- (6c) Seek redress before a court of a Member State.

The competent authority decides whether and on what conditions data sharing should start or resume.

---

## Common defects in refusal practice (Skill flags these)

| # | Defect | Why it fails |
|---|--------|--------------|
| 1 | Refused outright without attempting Art. 4(6) measures | Step 1 is mandatory; jumping to Step 3 is procedurally defective. |
| 2 | Refused on "trade secret" grounds without identifying the trade-secret data with specificity | Art. 4(6) requires identification of the data. |
| 3 | Refused with conclusory "serious damage" assertion | Recital 31 requires substantiation on objective elements; conclusion is insufficient. |
| 4 | Refused for "serious damage" without articulating "irreparable" | Recital 31 requires both — serious AND irreparable. |
| 5 | Blanket refusal across a category | Art. 4(8) requires case-by-case; blanket refusal is not permitted. |
| 6 | Failed to notify competent authority | Art. 4(7) and 4(8) both require notification; failure is itself an infringement. |
| 7 | Refused GDPR data-subject access on trade-secret grounds | Recital 31 final sentence preserves GDPR Art. 15 / 20 rights. |
| 8 | Treated FAQ as authoritative on the threshold | The FAQ is non-authoritative. |
| 9 | Mixed Art. 4(2) safety with Art. 4(8) trade-secret | Different tests; can be pleaded in alternative but the substantiation must address each. |
| 10 | Did not preserve the option of resumption | Art. 4(7) is reversible; refusal letters that suggest no path back are excessive. |
