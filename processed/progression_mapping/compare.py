"""
Compare Taeeun's hand-authored CCSS-Progressions grounding
(processed/math_prereq_grounding.json) against the Achieve the Core
"Coherence Map" connections shipped in the MathFish dataset
(allenai/achieve-the-core on HuggingFace).

Scope: K-5 only (project scope). Writes a report to report.md and
a machine-readable diff to comparison_output.json.
"""
import json
import re
from collections import defaultdict

DATA_DIR = "data"
GROUNDING_PATH = "../math_prereq_grounding.json"

K5_GRADES = {"K", "1", "2", "3", "4", "5"}


def grade_of(ccss_id: str) -> str:
    return ccss_id.split(".")[0]


def load_achieve_the_core():
    records = [json.loads(l) for l in open(f"{DATA_DIR}/standards.jsonl")]
    by_id = {r["id"]: r for r in records}
    return records, by_id


def normalize_ccss_token(token: str):
    """
    Taeeun's ccss_from/ccss_to fields are free-text, e.g.
    'K.CC.4a', 'K.OA.1-3', 'K.CC.6 / K.CC.7', '5.OA.1-2'.
    Achieve the Core uses cluster-lettered ids, e.g. 'K.CC.A.4a', 'K.OA.A.1'.
    We can't algorithmically insert the correct cluster letter (A/B/C...)
    without a lookup, so instead we build a lookup from (grade, domain, number-suffix)
    -> full Achieve-the-Core id, ignoring the cluster letter, and match on that.
    Returns a list of plain (grade, domain, suffix) tuples extracted from the token,
    splitting on '/' and '-' for compound citations.
    """
    tokens = re.split(r"\s*/\s*", token)
    out = []
    for t in tokens:
        t = t.strip()
        # handle ranges like K.OA.1-3 -> K.OA.1, K.OA.3 (endpoints only, not full expansion)
        m = re.match(r"^(K|\d)\.([A-Z]+)\.(\d+)(?:-(\d+))?([a-z]?)$", t)
        if not m:
            continue
        g, dom, n1, n2, suffix = m.groups()
        out.append((g, dom, n1, suffix))
        if n2:
            out.append((g, dom, n2, ""))
    return out


def build_atc_lookup(records):
    """Map (grade, domain, number, suffix) -> Achieve the Core standard id,
    ignoring the cluster letter that Taeeun's citations omit."""
    lookup = {}
    for r in records:
        if r["level"] not in ("Standard", "Sub-standard"):
            continue
        m = re.match(r"^(K|\d)\.([A-Z]+)\.([A-Z])\.(\d+)([a-z]?)$", r["id"])
        if not m:
            continue
        g, dom, _cluster, n, suffix = m.groups()
        lookup[(g, dom, n, suffix)] = r["id"]
        if suffix:
            lookup.setdefault((g, dom, n, ""), r["id"])  # fallback: base standard
    return lookup


def resolve_to_atc_ids(token, lookup):
    ids = set()
    for key in normalize_ccss_token(token):
        if key in lookup:
            ids.add(lookup[key])
        else:
            # try without suffix
            g, dom, n, _s = key
            if (g, dom, n, "") in lookup:
                ids.add(lookup[(g, dom, n, "")])
    return ids


def main():
    grounding = json.load(open(GROUNDING_PATH))
    georgia_edges = [d for d in grounding["dependencies"] if "from" in d]

    records, by_id = load_achieve_the_core()
    lookup = build_atc_lookup(records)

    # Build ATC progression edge set, K-5 scope only (both endpoints in K-5,
    # OR source in K-5 even if target spills into grade 6 -- track both).
    atc_progress_pairs = set()  # (from_id, to_id)
    atc_progress_pairs_all = set()
    atc_k5_standards = 0
    for r in records:
        if r["level"] not in ("Standard", "Sub-standard"):
            continue
        if grade_of(r["id"]) not in K5_GRADES:
            continue
        atc_k5_standards += 1
        for t in r["connections"]["progress to"]:
            atc_progress_pairs_all.add((r["id"], t))
            if grade_of(t) in K5_GRADES:
                atc_progress_pairs.add((r["id"], t))

    atc_related_pairs = set()
    for r in records:
        if r["level"] not in ("Standard", "Sub-standard"):
            continue
        if grade_of(r["id"]) not in K5_GRADES:
            continue
        for rel in r["connections"]["related"]:
            if grade_of(rel) in K5_GRADES:
                atc_related_pairs.add(frozenset((r["id"], rel)))

    print(f"Achieve the Core (MathFish) K-5 standard/sub-standard nodes: {atc_k5_standards}")
    print(f"Achieve the Core K-5 -> K-5 'progress to' edges: {len(atc_progress_pairs)}")
    print(f"Achieve the Core K-5 -> (any grade) 'progress to' edges: {len(atc_progress_pairs_all)}")
    print(f"Achieve the Core K-5 'related' edges (undirected, deduped): {len(atc_related_pairs)}")
    print(f"Taeeun's grounding file: {len(georgia_edges)} Georgia sub-standard edges")

    # Now try to match each Georgia edge to an ATC edge via ccss_from/ccss_to
    matched = []
    unmatched = []
    unresolvable = []  # couldn't even resolve the CCSS citation to an ATC id

    for e in georgia_edges:
        from_ids = resolve_to_atc_ids(e.get("ccss_from", ""), lookup)
        to_ids = resolve_to_atc_ids(e.get("ccss_to", ""), lookup)
        if not from_ids or not to_ids:
            unresolvable.append(e)
            continue

        hit = None
        for f in from_ids:
            for t in to_ids:
                if (f, t) in atc_progress_pairs_all:
                    hit = ("progress_to", f, t)
                    break
                if frozenset((f, t)) in atc_related_pairs:
                    hit = ("related", f, t)
                    break
            if hit:
                break

        if hit:
            matched.append({"georgia_edge": e, "atc_match": hit})
        else:
            unmatched.append({"georgia_edge": e, "from_ids": sorted(from_ids), "to_ids": sorted(to_ids)})

    print()
    print(f"Georgia edges resolvable to an ATC standard id on both ends: {len(matched) + len(unmatched)}")
    print(f"  -> confirmed by an ATC 'progress to' or 'related' edge:   {len(matched)}")
    print(f"  -> NOT found in ATC connections (novel or GA-specific):   {len(unmatched)}")
    print(f"Georgia edges whose ccss_from/ccss_to citation didn't resolve to a clean ATC id: {len(unresolvable)}")

    # Coverage the other direction: how many ATC K-5 progression edges have
    # no corresponding Georgia edge at all (regardless of match quality)?
    # Build set of all ATC ids referenced anywhere in Taeeun's file (loosely)
    referenced_atc_ids = set()
    for e in georgia_edges:
        referenced_atc_ids |= resolve_to_atc_ids(e.get("ccss_from", ""), lookup)
        referenced_atc_ids |= resolve_to_atc_ids(e.get("ccss_to", ""), lookup)

    atc_edges_touching_referenced = sum(
        1 for (f, t) in atc_progress_pairs if f in referenced_atc_ids or t in referenced_atc_ids
    )
    print()
    print(f"Distinct ATC standard ids touched anywhere by Taeeun's citations: {len(referenced_atc_ids)}")
    print(f"ATC K-5 progress-to edges touching at least one of those ids: {atc_edges_touching_referenced}")
    print(f"  (out of {len(atc_progress_pairs)} total ATC K-5 progress-to edges)")

    out = {
        "summary": {
            "atc_k5_standard_nodes": atc_k5_standards,
            "atc_k5_to_k5_progress_edges": len(atc_progress_pairs),
            "atc_k5_progress_edges_any_target_grade": len(atc_progress_pairs_all),
            "atc_k5_related_edges": len(atc_related_pairs),
            "georgia_grounding_edges": len(georgia_edges),
            "georgia_edges_resolvable_to_atc_ids": len(matched) + len(unmatched),
            "georgia_edges_confirmed_by_atc": len(matched),
            "georgia_edges_unmatched_in_atc": len(unmatched),
            "georgia_edges_citation_unresolvable": len(unresolvable),
            "distinct_atc_ids_touched_by_georgia_citations": len(referenced_atc_ids),
            "atc_edges_touching_those_ids": atc_edges_touching_referenced,
        },
        "matched": matched,
        "unmatched": unmatched,
        "unresolvable": unresolvable,
    }
    with open("comparison_output.json", "w") as f:
        json.dump(out, f, indent=2)
    print("\nWrote comparison_output.json")


if __name__ == "__main__":
    main()
