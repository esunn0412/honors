#!/usr/bin/env python3
"""Compares one mapping.json against another mapping.json (either schema:
--code-field state_code for map_state_to_ccss.py-style output, or ga_code
for the original ccss_ga_skill_map.json-style schema, now archived in
processed/history/).

Usage (comparing the hierarchical method against the adopted GA mapping):
    python3 compare_to_gold.py states/ga/mapping_llm_hierarchical.json \\
        states/ga/mapping_final.json --code-field state_code

There is no independently-verified ground truth for GA -- states/ga/mapping_final.json
is a single-reviewer product (see README.md's "How the adopted mapping was
reviewed"), so a disagreement here means "worth a second look," not
necessarily "the other side is wrong." This is a different situation from
VA: EDUMath's crosswalk actually IS independently verified (built by a
student, checked by an educator, per direct correspondence with the lead
author) -- use compare_to_edumath_gold.py for that one, not this script; do
not conflate the two files' evidentiary status.
"""
import argparse
import json


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mapping_path", help="e.g. states/ga/mapping_llm.json")
    ap.add_argument("gold_path", help="e.g. states/ga/mapping_final.json")
    ap.add_argument("--code-field", default="ga_code", help="the gold file's code field name")
    ap.add_argument("--out", default=None, help="optional path to write the full comparison JSON")
    args = ap.parse_args()

    gold_raw = json.load(open(args.gold_path))["mappings"]
    gold = {m[args.code_field]: m for m in gold_raw}

    run = json.load(open(args.mapping_path))["mappings"]

    rows = []
    rel_match = 0
    ccss_set_match = 0
    missing_from_gold = []
    for m in run:
        code = m["state_code"]
        g = gold.get(code)
        if g is None:
            missing_from_gold.append(code)
            continue
        rel_agree = m["relationship"] == g["relationship"]
        run_ccss = set(c["code"] for c in m["ccss_codes"])
        gold_ccss = set(c["code"] for c in g["ccss_codes"])
        ccss_agree = run_ccss == gold_ccss
        rel_match += rel_agree
        ccss_set_match += ccss_agree
        rows.append({
            "code": code,
            "run_relationship": m["relationship"],
            "gold_relationship": g["relationship"],
            "relationship_agrees": rel_agree,
            "run_ccss_codes": sorted(run_ccss),
            "gold_ccss_codes": sorted(gold_ccss),
            "ccss_codes_agree": ccss_agree,
            "run_note": m["note"],
            "gold_note": g["note"],
        })

    n = len(rows)
    report = {
        "n_compared": n,
        "missing_from_gold": missing_from_gold,
        "relationship_agreement_rate": rel_match / n if n else None,
        "ccss_code_set_agreement_rate": ccss_set_match / n if n else None,
        "disagreements": [r for r in rows if not (r["relationship_agrees"] and r["ccss_codes_agree"])],
        "rows": rows,
    }

    print(f"n={n}  relationship agreement={rel_match}/{n}  ccss-code-set agreement={ccss_set_match}/{n}")
    if missing_from_gold:
        print(f"WARNING: {len(missing_from_gold)} run codes not found in gold: {missing_from_gold}")
    print(f"Disagreements: {len(report['disagreements'])}")
    for d in report["disagreements"]:
        print(f"  {d['code']}: run={d['run_relationship']} {d['run_ccss_codes']}  vs  gold={d['gold_relationship']} {d['gold_ccss_codes']}")

    if args.out:
        json.dump(report, open(args.out, "w"), indent=2)
        print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
