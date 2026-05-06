#!/usr/bin/env python3
"""timeline_check.py — given a launch / contract date, identify applicable Data Act obligations.

Usage:
    python3 timeline_check.py --type connected-product --placed-on-market 2026-10-15
    python3 timeline_check.py --type related-service --placed-on-market 2025-08-01
    python3 timeline_check.py --type dps-contract --concluded 2024-06-01 --duration indefinite
    python3 timeline_check.py --type dps-contract --concluded 2025-06-01 --duration "10 years from 11 January 2024"

Outputs the applicable Article 50 dates and the obligations they trigger for the date provided.
"""
import argparse
from datetime import date


KEY_DATES = {
    "entry_into_force": date(2024, 1, 11),
    "general_application": date(2025, 9, 12),
    "art_3_1_design_by_default": date(2026, 9, 12),
    "art_29_no_switching_charges": date(2027, 1, 12),
    "chapter_iv_grandfather_b2b_data_sharing": date(2027, 9, 12),
}


def for_connected_product(placed: date) -> str:
    out = []
    out.append(f"Connected Product placed on the market: {placed.isoformat()}")
    out.append("")
    out.append("Applicable obligations:")
    out.append("")
    if placed >= KEY_DATES["general_application"]:
        out.append(f"- Art. 3(2) pre-contract disclosure — applies (general application from {KEY_DATES['general_application']}).")
        out.append(f"- Art. 4(1) indirect access on simple electronic request — applies.")
        out.append(f"- Art. 4(6)–(8) trade-secret regime — applies.")
        out.append(f"- Art. 4(10), 4(13) — applies.")
        out.append(f"- Art. 5 third-party transfer — applies.")
    else:
        out.append(f"- Connected Product was placed on the market BEFORE {KEY_DATES['general_application']}.")
        out.append(f"  As of {KEY_DATES['general_application']}, Chapter II obligations apply for products in scope.")
    if placed > KEY_DATES["art_3_1_design_by_default"]:
        out.append(f"- Art. 3(1) design-by-default — APPLIES (placed AFTER {KEY_DATES['art_3_1_design_by_default']}).")
    else:
        out.append(f"- Art. 3(1) design-by-default — does NOT apply on placement-date basis (placed on or before {KEY_DATES['art_3_1_design_by_default']}).")
        out.append("  Note: Art. 4(1) indirect access still applies regardless of placement date.")
    return "\n".join(out)


def for_related_service(placed: date) -> str:
    out = []
    out.append(f"Related Service placed on the market: {placed.isoformat()}")
    out.append("")
    out.append("Applicable obligations:")
    out.append("")
    if placed >= KEY_DATES["general_application"]:
        out.append(f"- Art. 3(3) pre-contract disclosure (9 fields) — applies.")
        out.append(f"- Art. 4(1) indirect access — applies for related-service data.")
        out.append(f"- Art. 4(6)–(8) trade-secret regime — applies.")
        out.append(f"- Art. 5 third-party transfer — applies.")
    if placed > KEY_DATES["art_3_1_design_by_default"]:
        out.append(f"- Art. 3(1) design-by-default — applies (placed AFTER {KEY_DATES['art_3_1_design_by_default']}).")
    else:
        out.append(f"- Art. 3(1) design-by-default — does NOT apply on placement-date basis.")
    return "\n".join(out)


def for_dps_contract(concluded: date, duration: str) -> str:
    out = []
    out.append(f"DPS contract concluded: {concluded.isoformat()}")
    out.append(f"Duration: {duration}")
    out.append("")
    out.append("Applicable obligations:")
    out.append("")
    if concluded > KEY_DATES["general_application"]:
        out.append(f"- Chapter VI applies in full from contract start (concluded after {KEY_DATES['general_application']}).")
        out.append(f"  Art. 23 access; Art. 25 switching contract clauses; Art. 26 transparency; Art. 27 good-faith cooperation;")
        out.append(f"  Art. 28 international-access disclosure; Art. 30 interfaces / functional equivalence; Art. 32 international access regime.")
        out.append(f"- Art. 29 switching charges: reduced charges allowed until {KEY_DATES['art_29_no_switching_charges']}, none thereafter.")
        out.append(f"- Chapter IV (unfair B2B data-sharing terms — Art. 13) may also apply if the contract contains terms within Chapter IV's scope. Verify independently.")
    else:
        out.append(f"- Contract concluded on or before {KEY_DATES['general_application']}.")
        out.append(f"- Chapter VI applied from {KEY_DATES['general_application']} (general application date in Art. 50).")
        out.append(f"  There is NO Article 50 grandfather for Chapter VI. Pre-existing DPS contracts had to be Art. 25 / 26 / 28 / 30 compliant from {KEY_DATES['general_application']}.")
        out.append(f"- Art. 29 switching charges: reduced charges allowed until {KEY_DATES['art_29_no_switching_charges']}, none thereafter, regardless of contract date.")
        is_indef = "indefinite" in duration.lower()
        is_long = "10 years" in duration.lower() or "ten years" in duration.lower()
        if is_indef or is_long:
            out.append("")
            out.append(f"- Chapter IV note: if this contract contains B2B data-sharing terms within Chapter IV's scope (Art. 13 unfair contractual terms), the Article 50 Chapter IV grandfather defers Chapter IV's application to those terms until {KEY_DATES['chapter_iv_grandfather_b2b_data_sharing']}, on the {'indefinite-duration' if is_indef else 'long-duration (≥ 10 years from 11 January 2024)'} basis.")
            out.append(f"  This grandfather applies to Chapter IV ONLY. It does not extend any Chapter VI deadline.")
        else:
            out.append("")
            out.append("- Chapter IV note: the Article 50 Chapter IV grandfather (to 12 September 2027) does not apply to this contract on the duration basis.")
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--type", required=True, choices=["connected-product", "related-service", "dps-contract"])
    p.add_argument("--placed-on-market", help="ISO date for connected-product or related-service")
    p.add_argument("--concluded", help="ISO date for dps-contract")
    p.add_argument("--duration", default="fixed", help="DPS contract duration (e.g., 'indefinite', '10 years from 11 January 2024', 'fixed 3-year term')")
    args = p.parse_args()
    if args.type == "connected-product":
        if not args.placed_on_market:
            p.error("--placed-on-market required")
        d = date.fromisoformat(args.placed_on_market)
        print(for_connected_product(d))
    elif args.type == "related-service":
        if not args.placed_on_market:
            p.error("--placed-on-market required")
        d = date.fromisoformat(args.placed_on_market)
        print(for_related_service(d))
    elif args.type == "dps-contract":
        if not args.concluded:
            p.error("--concluded required")
        d = date.fromisoformat(args.concluded)
        print(for_dps_contract(d, args.duration))
    print()
    print("---")
    print("Disclaimer: this script applies only the Article 50 (and Article 29) date triggers.")
    print("It does not apply sectoral lex specialis or member-state implementing law.")
    print("This is not legal advice.")


if __name__ == "__main__":
    main()
