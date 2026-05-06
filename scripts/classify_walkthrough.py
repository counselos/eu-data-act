#!/usr/bin/env python3
"""classify_walkthrough.py — interactive Q&A walkthrough of the classification decision tree.

Usage:
    python3 classify_walkthrough.py

Walks the four classification questions (Q1 connected product, Q2 related service, Q3 DPS, Q4 overlap)
plus the Article 31 carve-out questions, and prints a structured summary at the end.
The script is non-authoritative; it produces a starter analysis the lawyer reviews.
"""
import sys
from textwrap import fill


def ask(prompt, options=None):
    print()
    print(fill(prompt, width=92))
    if options:
        print()
        for k, v in options.items():
            print(f"  [{k}] {v}")
    while True:
        ans = input("> ").strip().lower()
        if not options:
            return ans
        if ans in options:
            return ans
        print("Please answer one of:", ", ".join(options.keys()))


YES_NO = {"y": "Yes", "n": "No", "u": "Unclear"}


def main():
    print("=" * 72)
    print("Data Act Classification Walkthrough")
    print("=" * 72)
    print(fill("This script walks the four classification questions of Article 2 (5)/(6)/(8)/(12) plus the Article 31 carve-outs. The output is a starting-point classification for the lawyer to review.", width=92))

    # Q1
    print("\n--- Q1. Is there a connected product? (Art. 2(5)) ---")
    q1a = ask("(1a) Does the offering include a physical item that obtains, generates or collects data about its use or environment?", YES_NO)
    q1b = ask("(1b) Can the physical item communicate product data via electronic communications service, physical connection, or on-device access?", YES_NO)
    q1c = ask("(1c) Is the primary function of the physical item NOT storing / processing / transmitting data on behalf of any party other than the user?", YES_NO)
    cp = (q1a == "y" and q1b == "y" and q1c == "y")

    # Q2
    print("\n--- Q2. Is there a related service? (Art. 2(6)) ---")
    q2a = ask("(2a) Is there a digital service or software (other than electronic communications service)?", YES_NO)
    q2b = ask("(2b) Is the digital service connected with the connected product at sale, rent, or lease — OR added later by the manufacturer or a third party?", YES_NO)
    q2c = ask("(2c) Does the digital service either prevent the product from performing one or more functions when absent, OR add to / update / adapt its functions?", YES_NO)
    rs = (q2a == "y" and q2b == "y" and q2c == "y")

    # Q3
    print("\n--- Q3. Is the digital service a Data Processing Service? (Art. 2(8)) ---")
    q3a = ask("(3a) Is the service provided to a customer (i.e., a contractual relationship under Art. 2(30))?", YES_NO)
    q3b = ask("(3b) Does it enable ubiquitous + on-demand network access?", YES_NO)
    q3c = ask("(3c) Are the resources shared, scalable, and elastic?", YES_NO)
    q3d = ask("(3d) Is it rapidly provisioned and released with minimal management effort or interaction?", YES_NO)
    dps = all(x == "y" for x in [q3a, q3b, q3c, q3d])

    # Q5 — Article 31 carve-outs
    art31 = None
    if dps:
        print("\n--- Q5. Article 31 carve-outs (custom-built or test/beta) ---")
        cust_engineering = ask("Is the majority of main features custom-built for one customer, OR all components developed for one customer?", YES_NO)
        not_catalog = ask("Is the service NOT offered at broad commercial scale via the catalogue?", YES_NO)
        if cust_engineering == "y" and not_catalog == "y":
            art31 = "31(1)"
        else:
            test_beta = ask("Is the service a non-production version for testing and evaluation, for a limited period of time?", YES_NO)
            if test_beta == "y":
                art31 = "31(2)"

    # Sectoral overlay
    print("\n--- Q7. Sectoral overlay indicators ---")
    sectors = []
    for sector, prompt in [
        ("automotive", "Does the offering touch motor vehicles, type-approval, or in-vehicle data?"),
        ("medical", "Does the offering touch medical devices or in-vitro diagnostics?"),
        ("financial", "Does the customer or the service touch a financial entity / DORA scope?"),
        ("nis2", "Is the customer an NIS2 essential or important entity?"),
        ("ai_act", "Does the offering involve AI systems / models in AI Act scope?"),
        ("eidas", "Does the offering touch electronic identification / qualified trust services?"),
    ]:
        ans = ask(prompt, YES_NO)
        if ans == "y":
            sectors.append(sector)

    # Summary
    print("\n" + "=" * 72)
    print("CLASSIFICATION SUMMARY (starting-point — not legal advice)")
    print("=" * 72)
    print(f"Connected Product (Art. 2(5)):     {'YES' if cp else 'NO'}")
    print(f"Related Service (Art. 2(6)):       {'YES' if rs else 'NO'}")
    print(f"Data Processing Service (Art. 2(8)): {'YES' if dps else 'NO'}")
    print(f"Overlap (Chapter II + Chapter VI): {'YES' if (rs and dps) else 'NO'}")
    if art31:
        print(f"Article 31 lighter regime:         {art31}")
    print(f"Sectoral overlay flagged:          {', '.join(sectors) if sectors else 'none'}")
    print(f"Member-state lex specialis:        always check — not covered by this Skill")
    print()

    # Recommended next steps
    print("Recommended next steps:")
    if cp:
        print(" - Prepare Article 3(2) pre-contract notice (template precontract-disclosure-art-3-2.md).")
    if rs:
        print(" - Prepare Article 3(3) pre-contract notice (template precontract-disclosure-art-3-3.md).")
    if dps:
        print(" - Prepare Article 25 contract clauses (template dps-contract-clauses-art-25.md).")
        print(" - Stand up Article 26 + 28 + 29 public pages.")
        if art31:
            print(f" - Prepare Article 31(3) pre-contract disclosure for the {art31} carve-out.")
    print(" - Review applicable Article 50 dates with timeline_check.py.")
    if sectors:
        print(f" - Verify sectoral lex specialis: {', '.join(sectors)}.")
    print(" - Run gap-analysis audit (template gap-analysis-checklist.md).")
    print()
    print("Disclaimer: this output is a starting-point classification produced by an")
    print("interactive script. It is not legal advice. Substantive review by qualified")
    print("counsel is required.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[interrupted]")
        sys.exit(130)
