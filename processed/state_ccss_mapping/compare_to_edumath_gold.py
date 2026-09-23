#!/usr/bin/env python3
"""Compares states/va/mapping_llm.json against EDUMath's VA SOL -> CCSS
crosswalk, treated as verified gold for VA: per direct correspondence with
lead author Bryan Christ, the crosswalk was built by an undergraduate
student and then manually verified by an educator (two-stage human review,
distinct from the paper's separate teacher-annotation pipeline for the MWP
dataset itself).

EDUMath's crosswalk only cites a CCSS domain (e.g. "3.NBT"), never a
specific numbered sub-point, and doesn't classify relationship type -- so
this comparison is domain-level only, coarser than the GA-vs-gold
comparison (compare_to_gold.py), which checks exact CCSS sub-point sets and
relationship type. Each run entry already carries the domain EDUMath cited
in its own "edumath_cited_domain" field.

Any disagreement here is a candidate error in THIS PIPELINE's classification,
not in EDUMath's (now gold) crosswalk -- report it that way in error analysis.
"""
import argparse
import json


def domain_of(code):
    parts = code.split(".")
    return f"{parts[0]}.{parts[1]}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mapping_path", nargs="?", default="states/va/mapping_llm.json")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    run = json.load(open(args.mapping_path))["mappings"]

    rows = []
    agree = 0
    for m in run:
        our_domains = sorted(set(domain_of(c["code"]) for c in m["ccss_codes"]))
        gold_domain = m["edumath_cited_domain"]
        domain_agrees = gold_domain in our_domains
        agree += domain_agrees
        rows.append({
            "va_code": m["state_code"],
            "our_relationship": m["relationship"],
            "our_ccss_codes": [c["code"] for c in m["ccss_codes"]],
            "our_ccss_domains": our_domains,
            "gold_domain_edumath": gold_domain,
            "domain_agrees": domain_agrees,
        })

    n = len(run)
    report = {
        "gold_source": "EDUMath crosswalk (papers/edumath_data/matched_standards_summarized.csv) -- undergrad-mapped, educator-verified per author correspondence",
        "n": n,
        "domain_level_agreement_rate": agree / n,
        "candidate_script_errors": [r for r in rows if not r["domain_agrees"]],
        "rows": rows,
    }
    print(f"n={n}  domain-level agreement with gold={agree}/{n}")
    print(f"Candidate script errors ({len(report['candidate_script_errors'])}) -- this pipeline likely got these wrong, not the gold:")
    for d in report["candidate_script_errors"]:
        print(f"  {d['va_code']}: this run says {d['our_ccss_domains']}, gold (EDUMath) says {d['gold_domain_edumath']}")

    if args.out:
        json.dump(report, open(args.out, "w"), indent=2)
        print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
