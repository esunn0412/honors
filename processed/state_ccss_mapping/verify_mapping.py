#!/usr/bin/env python3
"""Pure-Python verification for a state<->CCSS mapping JSON (the output of
map_state_to_ccss.py, or of a manual/Claude-Code classification run
following the same schema). No API calls, no dependency on any LLM --
this is the part that must never trust the model's own claims.

Checks:
  - every state code processed exactly once, no duplicates
  - every referenced CCSS code is real (checked against ccss_math_*.json,
    not the model's memory)
  - cardinality-first rule: no state_superset/state_subset with >1 CCSS code
  - split-integrity: a "split" relationship means this code is one of
    SEVERAL jointly covering a CCSS code, so at least one other entry in
    the SAME mapping must also cite it. Found a real bug this way: the
    original ccss_ga_skill_map.json's K.GSR.8.2 entry is labeled "split"
    but its claimed sibling (K.GSR.8.1) actually cites a different CCSS
    code entirely -- pass --code-field ga_code to check that schema too.
  - the "borrowed thematic label" lint: a different_grade/partial entry
    whose CCSS target is ALSO the same-grade match of some other state
    entry classified exact/state_superset/state_subset/merge/split -- almost
    always means the flagged entry should be "none" instead (see
    processed/preprocess.typ's classification-rule discussion for the
    worked GA examples of this exact failure mode)
  - recomputes every summary count directly from the mapping data --
    never reports a number the model asserted about itself

Usage as a script:
    python3 verify_mapping.py path/to/mapping.json
        [--state-standards "states/ga/georgia_math_*.json"]
    CCSS's full 175-code list is always loaded automatically from
    ccss_standards/ccss_math_*.json, bundled locally (fixed, not state-specific).
    Pass --state-standards (a glob, same convention as map_state_to_ccss.py)
    to also check every state code was processed exactly once -- omit it
    (e.g. for a partial-coverage run like the 21-code VA sample) to skip
    that specific check while still validating everything else.
Usage as a library:
    from verify_mapping import verify
    report = verify(mapping_dict, state_all_codes=[...], ccss_all_codes=[...])
"""
import argparse
import glob
import json
import sys
from collections import defaultdict
from pathlib import Path

REAL_MATCH_TYPES = {"exact", "state_superset", "state_subset", "merge", "split"}
NEEDS_REVIEW_TYPES = {"partial", "state_subset", "none"}


def _grade_of(code):
    # e.g. "3.CE.1" -> "3", "K.NR.1.1" -> "K"
    return code.split(".")[0]


def verify(output, state_all_codes=None, ccss_all_codes=None, code_field="state_code"):
    """code_field: the mapping's own field name for its code -- "state_code" for
    map_state_to_ccss.py-schema output (the default), "ga_code" for the original
    ccss_ga_skill_map*.json schema. Every check below is schema-agnostic once this
    is set; issue dicts always report it under a "state_code" key for a stable
    report shape regardless of which schema was checked."""
    mappings = output["mappings"]
    issues = []

    state_code_list = [m[code_field] for m in mappings]
    dupes = {c for c in state_code_list if state_code_list.count(c) > 1}
    if dupes:
        issues.append({"type": "duplicate_state_code", "codes": sorted(dupes)})

    if state_all_codes is not None:
        missing = set(state_all_codes) - set(state_code_list)
        extra = set(state_code_list) - set(state_all_codes)
        if missing:
            issues.append({"type": "state_codes_not_processed", "codes": sorted(missing)})
        if extra:
            issues.append({"type": "unknown_state_codes_in_output", "codes": sorted(extra)})

    referenced_ccss = set()
    for m in mappings:
        for c in m["ccss_codes"]:
            referenced_ccss.add(c["code"])
    if ccss_all_codes is not None:
        bogus = referenced_ccss - set(ccss_all_codes)
        if bogus:
            issues.append({"type": "nonexistent_ccss_codes_referenced", "codes": sorted(bogus)})

    cardinality_violations = [
        m[code_field] for m in mappings
        if m["relationship"] in ("state_superset", "state_subset") and len(m["ccss_codes"]) != 1
    ]
    if cardinality_violations:
        issues.append({"type": "cardinality_first_rule_violation", "codes": cardinality_violations})

    none_with_codes = [m[code_field] for m in mappings if m["relationship"] == "none" and m["ccss_codes"]]
    if none_with_codes:
        issues.append({"type": "none_relationship_has_ccss_codes", "codes": none_with_codes})

    # split-integrity check: "split" means this state code is one of SEVERAL jointly
    # covering a CCSS code, so at least one other entry in this same mapping must also
    # cite each of its ccss_codes. A "split" entry with no such sibling is internally
    # inconsistent -- it should have been exact/state_superset/state_subset/partial instead.
    citers_of = defaultdict(list)
    for m in mappings:
        for c in m["ccss_codes"]:
            citers_of[c["code"]].append(m[code_field])
    orphan_splits = []
    for m in mappings:
        if m["relationship"] != "split":
            continue
        for c in m["ccss_codes"]:
            siblings = [x for x in citers_of[c["code"]] if x != m[code_field]]
            if not siblings:
                orphan_splits.append({"state_code": m[code_field], "ccss_code": c["code"]})
    if orphan_splits:
        issues.append({"type": "split_relationship_has_no_sibling", "entries": orphan_splits})

    # "borrowed thematic label" lint
    same_grade_real_match = defaultdict(list)  # (ccss_code, grade) -> [state_codes]
    for m in mappings:
        if m["relationship"] in REAL_MATCH_TYPES:
            g = _grade_of(m[code_field])
            for c in m["ccss_codes"]:
                same_grade_real_match[(c["code"], g)].append(m[code_field])

    thematic_label_flags = []
    for m in mappings:
        if m["relationship"] in ("different_grade", "partial"):
            g = _grade_of(m[code_field])
            for c in m["ccss_codes"]:
                owners = same_grade_real_match.get((c["code"], g), [])
                if owners:
                    thematic_label_flags.append({
                        "state_code": m[code_field],
                        "relationship": m["relationship"],
                        "ccss_code": c["code"],
                        "already_matched_at_same_grade_by": owners,
                    })
    if thematic_label_flags:
        issues.append({"type": "possible_borrowed_thematic_label", "entries": thematic_label_flags})

    by_rel = defaultdict(int)
    for m in mappings:
        by_rel[m["relationship"]] += 1

    unmapped_state = [m[code_field] for m in mappings if m["relationship"] == "none"]
    unmapped_ccss = sorted(set(ccss_all_codes or []) - referenced_ccss) if ccss_all_codes is not None else None

    totals = {
        "state_leaf_count": len(mappings),
        "state_mapped_to_at_least_one_ccss": len(mappings) - len(unmapped_state),
        "state_genuine_gap": len(unmapped_state),
        "ccss_referenced": len(referenced_ccss),
        "ccss_unmapped": len(unmapped_ccss) if unmapped_ccss is not None else None,
        "by_relationship_type": dict(by_rel),
        "flagged_for_review": sum(1 for m in mappings if m["relationship"] in NEEDS_REVIEW_TYPES),
    }

    return {
        "totals": totals,
        "issues": issues,
        "clean": not issues,
    }


def _load_leaf_codes(glob_pattern):
    """Handles both schemas in this project: GA's domains[].standards[] and
    CCSS's domains[].clusters[].standards[] (CCSS has one extra nesting
    level; clusters are unlabeled in the source, see processed/preprocess.typ)."""
    codes = []
    for path in sorted(glob.glob(glob_pattern)):
        d = json.load(open(path))
        for dom in d["domains"]:
            if dom.get("is_meta"):
                continue
            for cluster in dom.get("clusters", [dom]):
                for st in cluster.get("standards", []):
                    subs = st.get("sub_standards")
                    items = subs if subs else [st]
                    for item in items:
                        codes.append(item["code"])
    return codes


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mapping_path")
    ap.add_argument("--state-standards", default=None, help='glob, e.g. "states/ga/georgia_math_*.json"')
    ap.add_argument("--code-field", default="state_code",
                     help='the mapping\'s own code field name -- "state_code" (default, map_state_to_ccss.py '
                          'schema) or "ga_code" (the original ccss_ga_skill_map*.json schema)')
    args = ap.parse_args()

    output = json.load(open(args.mapping_path))

    ccss_dir = Path(__file__).resolve().parent / "ccss_standards"
    ccss_all_codes = _load_leaf_codes(str(ccss_dir / "ccss_math_*.json"))

    state_all_codes = _load_leaf_codes(args.state_standards) if args.state_standards else None

    report = verify(output, state_all_codes=state_all_codes, ccss_all_codes=ccss_all_codes, code_field=args.code_field)
    print(json.dumps(report, indent=2))
    if not report["clean"]:
        sys.exit(1)
