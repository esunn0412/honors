#!/usr/bin/env python3
"""Shared relationship taxonomy, classification rules, and few-shot prompt
construction for the state-standard <-> CCSS mapping pipeline.

This module is imported by BOTH map_state_to_ccss.py (the real API script)
and by the manual/offline classification runs in states/ga and states/va --
so the exact same rules and exemplars are used whether a real API key is
calling Claude or a human/agent is doing the classification by hand. That
is the whole point: the two paths must be interchangeable.

Few-shot exemplars are pulled programmatically from this project's own
adopted GA mapping (states/ga/mapping_final.json -- the flat method's output
with 8 human-reviewed corrections, see README.md), not hand-retyped, so
they can never drift out of sync with the real, reviewed data as that file
changes.
"""
import json
from pathlib import Path

STATES_DIR = Path(__file__).resolve().parent / "states"

RELATIONSHIP_TYPES = {
    "exact": "Same requirement and scope, reworded at most.",
    "merge": "One state sub-standard covers more than one CCSS leaf code.",
    "split": "This state sub-standard is one of several jointly covering a single CCSS leaf code.",
    "different_grade": "Same operation/skill in both documents, at different K-5 grades -- not a gap.",
    "state_superset": "The state standard requires everything CCSS does, plus more. Reserved for a TRUE one-to-one pair -- see the cardinality rule below.",
    "state_subset": "The state standard requires less than CCSS does (rare). Reserved for a TRUE one-to-one pair -- see the cardinality rule below.",
    "partial": "Related but genuinely narrower/different in a way that isn't a clean superset or subset; lower confidence.",
    "none": "No CCSS K-5 leaf code judged equivalent at any grade -- a genuine gap.",
}

NEEDS_REVIEW_TYPES = {"partial", "state_subset", "none"}

CLASSIFICATION_RULES = """
CLASSIFICATION RULES (apply in this order):

1. CARDINALITY FIRST. Count how many CCSS codes this state standard's own
   content actually requires, and whether other state standards jointly
   cover a single CCSS code.
   - Exactly one state standard <-> exactly one CCSS code: proceed to rule 2.
   - One state standard covers MULTIPLE CCSS codes: relationship = "merge",
     regardless of whether it also happens to look like a superset of the
     union of those codes. Record any scope nuance in the note, but the
     category is merge.
   - Multiple state standards are needed to jointly cover ONE CCSS code:
     relationship = "split". Same rule: don't relabel as subset just because
     one piece alone looks narrower than the CCSS target -- if it takes more
     than one state standard to cover the CCSS code, it's split.
   state_superset and state_subset are reserved EXCLUSIVELY for the true
   one-to-one case. If you are about to output state_superset or state_subset and
   you have cited more than one CCSS code, STOP -- it should be merge.

2. SAME GRADE, ONE-TO-ONE: is it the same requirement, reworded at most
   (exact), does the state version require strictly more (state_superset), or
   strictly less (state_subset, rare)?

3. DIFFERENT GRADE: if the best one-to-one CCSS match is at a different
   K-5 grade, first ask whether it is the SAME OPERATION at a narrower or
   equal scope (e.g. "identify perpendicular lines" one grade earlier than
   CCSS introduces "identify AND draw" them) -- if so, "different_grade",
   not a gap. If it is a genuinely DIFFERENT operation that merely shares a
   topic with some CCSS code (e.g. "identify a coin's value" vs. "compute a
   total using coins" -- identification is not computation), do not label
   it different_grade just because a CCSS standard on the same topic exists
   at another grade. Check whether that CCSS code is already the correct,
   same-grade match for a DIFFERENT state standard -- if so, this one is
   almost certainly "none", not different_grade or partial, since the topic
   is just being borrowed as the nearest available label.

4. PARTIAL vs. NONE: if related but you cannot confidently call it a clean
   subset/superset/different_grade match, and no other state standard
   already owns the CCSS code as its real match, use "partial" and explain
   the imprecision in the note. If the state standard describes a genuinely
   different operation with no CCSS analog at any grade, use "none" with an
   empty ccss_codes list.

5. Never force a link with false confidence. An honest "none" or "partial"
   flagged for review is better than a wrong "exact" or "different_grade".
"""


def _mapping_by_code(code):
    d = json.load(open(STATES_DIR / "ga" / "mapping_final.json"))
    for m in d["mappings"]:
        if m["state_code"] == code:
            return m
    raise KeyError(code)


# code chosen per relationship type from the adopted GA<->CCSS mapping,
# picked to also illustrate the trickiest distinctions (cardinality-first
# for merge, same-operation-different-scope for different_grade, etc.)
FEW_SHOT_SOURCE_CODES = {
    "exact": "K.NR.1.2",
    "state_superset": "K.NR.1.3",
    "state_subset": "5.NR.4.3",
    "merge": "K.NR.5.1",
    "split": "K.NR.5.3",
    "different_grade": "2.GSR.7.2",
    "partial": "2.MDR.5.4",
    "none": "K.NR.1.4",
}


def build_few_shot_block():
    """Renders one worked example per relationship type, pulled live from
    the adopted GA mapping, for inclusion in the classification prompt."""
    lines = []
    for rel, code in FEW_SHOT_SOURCE_CODES.items():
        m = _mapping_by_code(code)
        lines.append(f"### Example: {rel}")
        lines.append(f"State standard {m['state_code']}: {m['state_description']}")
        if m["ccss_codes"]:
            for c in m["ccss_codes"]:
                lines.append(f"  CCSS {c['code']}: {c['description']}")
        else:
            lines.append("  (no CCSS code -- genuine gap)")
        lines.append(f"-> relationship: {rel}")
        lines.append(f"-> note: {m['note']}")
        lines.append("")
    return "\n".join(lines)


def build_domain_family_prompt(state_code, state_description, family_summaries, state_guidance=None):
    """Stage 1 of the hierarchical (domain -> cluster -> leaf) classification
    path: pick which CCSS domain famil(y/ies) (CC, OA, NBT, MD, G, NF -- each
    spanning every K-5 grade it appears at) could plausibly contain a match,
    before ever looking at individual leaf standards."""
    lines = []
    for fam, info in family_summaries.items():
        grades = ", ".join(str(g) for g in info["grades"])
        lines.append(f"{fam} (grades: {grades}):")
        for d in info["cluster_descriptions"]:
            lines.append(f"  - {d}")
    families_block = "\n".join(lines)
    guidance_block = f"\n\nAdditional guidance/context for this state standard:\n{state_guidance}" if state_guidance else ""
    return f"""You are classifying a state math standard against CCSS K-5 using a STAGED search: first pick a domain family, then a cluster within it, then the leaf standard(s) -- instead of scanning all ~175 CCSS leaf codes at once.

STATE STANDARD:
{state_code}: {state_description}{guidance_block}

STEP 1: Which CCSS domain famil(y/ies) below could plausibly contain a matching standard? A domain family spans every K-5 grade it appears at (e.g. "OA" covers K.OA through 5.OA) -- select across grades freely, a match need not be at the same grade as the state standard. If the state standard's content genuinely spans two families at once (e.g. it is about both angle measurement and drawing shapes), select both. If truly no domain family could contain a match (a genuine gap), return an empty list.

DOMAIN FAMILIES (each line under a family is one of its clusters' descriptions, to give you a sense of what it covers):
{families_block}

Respond with ONLY JSON: {{"families": ["<family code>", ...]}}
"""


def build_cluster_selection_prompt(state_code, state_description, clusters, state_guidance=None):
    """Stage 2: within the domain famil(y/ies) picked in stage 1, pick the
    best cluster(s). clusters: list of {cluster_id, domain_code, grade,
    cluster_description, leaf_codes}."""
    lines = []
    for c in clusters:
        codes = ", ".join(l["code"] for l in c["leaves"])
        lines.append(f"  {c['cluster_id']} (grade {c['grade']}, domain {c['domain_code']}): {c['cluster_description']} [leaf codes: {codes}]")
    clusters_block = "\n".join(lines)
    guidance_block = f"\n\nAdditional guidance/context for this state standard:\n{state_guidance}" if state_guidance else ""
    return f"""STAGE 2 of a staged domain -> cluster -> leaf-standard search for classifying a state math standard against CCSS K-5.

STATE STANDARD:
{state_code}: {state_description}{guidance_block}

STEP 2: Within the domain famil(y/ies) already selected, which cluster(s) below are plausible candidates for the final leaf-standard match? Select every cluster worth examining more closely at the leaf level -- it's fine to select more than one, including clusters at different grades from the state standard. If none of these clusters actually fit on closer look, return an empty list (this is a genuine gap).

CLUSTERS:
{clusters_block}

Respond with ONLY JSON: {{"clusters": ["<cluster_id>", ...]}}
"""


def build_classification_prompt(state_code, state_description, ccss_candidates, state_guidance=None):
    """ccss_candidates: list of {code, description} for every CCSS K-5 leaf
    code at the same grade as state_code, plus every CCSS leaf code at every
    other K-5 grade (the full 175, in practice) -- no retrieval pre-filter.
    See README for why retrieval was deliberately dropped."""
    candidate_lines = "\n".join(f"  {c['code']}: {c['description']}" for c in ccss_candidates)
    guidance_block = f"\n\nAdditional guidance/context for this state standard:\n{state_guidance}" if state_guidance else ""
    return f"""You are classifying how one state math standard relates to the CCSS K-5 math standards, using the taxonomy below. You are comparing against the FULL list of CCSS K-5 leaf codes -- do not assume a match must be at the same grade.

RELATIONSHIP TYPES:
{json.dumps(RELATIONSHIP_TYPES, indent=2)}

{CLASSIFICATION_RULES}

WORKED EXAMPLES (from a verified gold mapping, GA<->CCSS):
{build_few_shot_block()}

NOW CLASSIFY THIS STATE STANDARD:
{state_code}: {state_description}{guidance_block}

CANDIDATE CCSS K-5 LEAF CODES (the complete set -- choose zero, one, or more):
{candidate_lines}

Respond with ONLY a JSON object with this exact shape:
{{
  "state_code": "{state_code}",
  "ccss_codes": ["<code>", ...],
  "relationship": "<one of: {', '.join(RELATIONSHIP_TYPES.keys())}>",
  "note": "<your reasoning, citing specific text from both standards>"
}}
If relationship is "none", ccss_codes must be an empty list.
If you are about to output state_superset or state_subset with more than one ccss_codes entry, that is a rule violation -- use merge or split instead.
"""
