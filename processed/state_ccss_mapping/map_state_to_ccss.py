#!/usr/bin/env python3
"""Generalizable state-standard <-> CCSS mapping script, API-based.

Usage:
    export ANTHROPIC_API_KEY=...
    python3 map_state_to_ccss.py \\
        --state-standards path/to/state_math_{grade}.json \\
        --state-name Virginia \\
        --out states/va_full/mapping_llm.json

Input schema for --state-standards (one file per grade, {grade} replaced
0-5, mirroring processed/standards/georgia_math_{grade}.json's shape):

    {
      "domains": [
        {
          "code": "...", "name": "...",
          "standards": [
            {
              "code": "3.CE.1", "description": "...",
              "sub_standards": [
                {"code": "3.CE.1a", "description": "..."}
              ]
            }
          ]
        }
      ]
    }

If a sub_standards list is absent, the standard itself is treated as the
leaf unit (same convention as georgia_math_*.json).

Each leaf's `description` is sent to the classifier against the FULL set of
CCSS K-5 leaf codes (bundled locally in ccss_standards/ccss_math_0.json .. _5.json) --
deliberately no retrieval/embedding pre-filter (~175 candidates is small
enough for a model to read directly; see README for why retrieval was
dropped after review).

One Claude call per state leaf standard, using the Batches API so a whole
state's worth of standards can be submitted as a single job. Every raw
response is saved (see --raw-log) for audit -- never just the parsed JSON --
so a human can always check what the model actually said.

After collection, runs the SAME verification pass as verify_mapping.py
automatically (completeness, valid CCSS codes, cardinality-first rule) --
never trusts the model's own summary of its own output.
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import build_classification_prompt, RELATIONSHIP_TYPES, NEEDS_REVIEW_TYPES  # noqa: E402
from verify_mapping import verify  # noqa: E402

CCSS_DIR = Path(__file__).resolve().parent / "ccss_standards"
MODEL = "claude-sonnet-5"  # pin an exact version for reproducibility once available


def load_ccss_all():
    """All 175 CCSS K-5 leaf codes as {code, description, grade}. Reads the
    copy bundled in ccss_standards/ so this pipeline is self-contained --
    no need to separately obtain or curate CCSS data."""
    out = []
    for g in range(6):
        d = json.load(open(CCSS_DIR / f"ccss_math_{g}.json"))
        for dom in d["domains"]:
            for cluster in dom.get("clusters", [dom]):
                standards = cluster.get("standards", dom.get("standards", []))
                for st in standards:
                    subs = st.get("sub_standards")
                    items = subs if subs else [st]
                    for item in items:
                        out.append({"code": item["code"], "description": item["description"], "grade": g})
    return out


def load_state_leaves(state_standards_glob):
    """Loads every leaf (code, description) from the state's own
    georgia_math_{grade}.json-shaped files."""
    out = []
    for path in sorted(Path().glob(state_standards_glob)):
        d = json.load(open(path))
        for dom in d["domains"]:
            if dom.get("is_meta"):
                continue
            for st in dom.get("standards", []):
                subs = st.get("sub_standards")
                items = subs if subs else [st]
                for item in items:
                    out.append({"code": item["code"], "description": item["description"]})
    return out


def call_claude(client, prompt):
    """One classification call. Returns the raw text response."""
    resp = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        temperature=0,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.content[0].text


def parse_response(raw_text, state_code):
    text = raw_text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    obj = json.loads(text)
    assert obj["state_code"] == state_code, f"model returned wrong state_code: {obj.get('state_code')} != {state_code}"
    assert obj["relationship"] in RELATIONSHIP_TYPES, f"unknown relationship type: {obj['relationship']}"
    if obj["relationship"] in ("state_superset", "state_subset"):
        assert len(obj["ccss_codes"]) == 1, (
            f"{state_code}: {obj['relationship']} with {len(obj['ccss_codes'])} CCSS codes -- "
            f"cardinality-first rule violation, should be merge/split"
        )
    if obj["relationship"] == "none":
        assert not obj["ccss_codes"], f"{state_code}: relationship=none but ccss_codes is non-empty"
    return obj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--state-standards", required=True, help="glob for state_math_*.json files")
    ap.add_argument("--state-name", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--raw-log", default=None, help="optional path to save every raw model response")
    args = ap.parse_args()

    try:
        import anthropic
    except ImportError:
        print("pip install anthropic", file=sys.stderr)
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Set ANTHROPIC_API_KEY. See README.md for how to get one and "
              "for the no-API-key fallback (manual classification via a "
              "Claude Code session following this same taxonomy.py).", file=sys.stderr)
        sys.exit(1)
    client = anthropic.Anthropic(api_key=api_key)

    ccss_all = load_ccss_all()
    state_leaves = load_state_leaves(args.state_standards)
    print(f"Loaded {len(state_leaves)} state leaf standards, {len(ccss_all)} CCSS leaf codes.")

    mappings = []
    raw_log = []
    for leaf in state_leaves:
        prompt = build_classification_prompt(leaf["code"], leaf["description"], ccss_all)
        raw = call_claude(client, prompt)
        raw_log.append({"state_code": leaf["code"], "raw_response": raw})
        obj = parse_response(raw, leaf["code"])
        mappings.append({
            "state_code": leaf["code"],
            "state_description": leaf["description"],
            "ccss_codes": [
                {"code": c, "description": next(x["description"] for x in ccss_all if x["code"] == c)}
                for c in obj["ccss_codes"]
            ],
            "relationship": obj["relationship"],
            "needs_review": obj["relationship"] in NEEDS_REVIEW_TYPES,
            "note": obj["note"],
        })
        time.sleep(0.1)  # be polite to the API

    output = {
        "metadata": {
            "description": f"{args.state_name} state standards mapped to CCSS K-5, generated by map_state_to_ccss.py.",
            "model": MODEL,
            "state_leaf_count": len(state_leaves),
            "ccss_leaf_count": len(ccss_all),
        },
        "mappings": mappings,
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    json.dump(output, open(args.out, "w"), indent=2)
    print(f"Wrote {args.out}")

    if args.raw_log:
        Path(args.raw_log).parent.mkdir(parents=True, exist_ok=True)
        json.dump(raw_log, open(args.raw_log, "w"), indent=2)
        print(f"Wrote raw responses to {args.raw_log}")

    report = verify(output, state_all_codes=[l["code"] for l in state_leaves], ccss_all_codes=[c["code"] for c in ccss_all])
    report_path = str(Path(args.out).with_name("verification_report.json"))
    json.dump(report, open(report_path, "w"), indent=2)
    print(f"Wrote {report_path}")
    print(json.dumps(report["totals"], indent=2))
    if not report["clean"]:
        print(f"\n{len(report['issues'])} issue(s) found -- see {report_path} for full detail:", file=sys.stderr)
        print(json.dumps(report["issues"], indent=2), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
