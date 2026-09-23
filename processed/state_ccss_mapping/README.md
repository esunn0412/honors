# State standard ↔ CCSS mapping pipeline

A generalizable pipeline that classifies any state's K-5 math standards against CCSS, using an 8-type relationship taxonomy. Built so a future user only has to provide their state's standards in the right shape — they don't need to re-derive the classification rules from scratch. `states/ga/mapping_final.json` is the adopted GA↔CCSS mapping this project uses; `states/va/` is a second demonstration on Virginia's SOL codes.

## Directory layout

```
state_ccss_mapping/
  taxonomy.py              Shared relationship taxonomy, classification rules, and
                            few-shot prompt builder. Used both by the API script's
                            prompts and as the rulebook for a manual classification
                            pass -- one source of truth either way.
  map_state_to_ccss.py      The real, API-based script (flat method) -- this is what
                            produced the adopted mapping. Ready to run with an
                            ANTHROPIC_API_KEY for a future state or a reproducible
                            headless re-run.
  map_state_to_ccss_hierarchical.py
                            Same inputs/output schema as map_state_to_ccss.py, but
                            classifies via a staged domain -> cluster -> leaf-standard
                            search instead of one flat prompt. Kept local for now --
                            see "Hierarchical classification" below.
  verify_mapping.py         Pure-Python verification (no API calls, runnable
                            directly on any mapping.json). Checks completeness,
                            valid CCSS codes, the cardinality-first rule, a
                            split-integrity check, and a "borrowed thematic
                            label" lint.
  ccss_standards/           CCSS K-5 math standards, bundled locally so anyone
                            using this pipeline for their own state doesn't need
                            to separately obtain or curate CCSS data -- it's the
                            one dataset every user needs regardless of which
                            state they're mapping.
    ccss_math_0.json ... _5.json
  states/
    ga/
      georgia_math_0.json ... _5.json           Georgia's own K-5 standards, bare
                                                 code + description.
      georgia_math_guidance_0.json ... _5.json  Georgia's own "Evidence of Student
                                                 Learning" guidance per standard
                                                 (fundamentals, strategies,
                                                 terminology, examples).
      mapping_final.json      THE adopted GA <-> CCSS mapping: the flat method's
                               classification of all 150 GA sub-standards, with
                               8 human-reviewed corrections applied.
      mapping_llm.json        The flat method's original, unedited output (before
                               the 8 corrections) -- kept for provenance and to
                               show what the script produces on its own.
      human_review.json       Full human review trail: every one of the script's
                               25 non-trivial classifications, the original
                               output, the verdict ("error" / "okay"), and the
                               correction where one was made.
      verification_report.json  verify_mapping.py's output for mapping_final.json.
    va/
      mapping_llm.json         The 21 distinct VA SOL codes whose full text is
                                currently available, classified fresh (flat method).
      comparison_to_gold.json  Comparison against EDUMath's crosswalk (see below).
      unmatched_review.json    The 2 domain-level disagreements with EDUMath,
                                reviewed in full (resolved -- see below).
      verification_report.json
```

Georgia's and Virginia's own standards are bundled here (where available), so this repo is usable standalone. A new state's own standards are NOT bundled -- those are inherently state-specific and supplied by whoever runs the pipeline for that state; only CCSS, the fixed reference every run compares against, ships with the tool regardless.

Each `mapping_llm.json` / `mapping_final.json` is a directly-authored JSON file in the same schema the API script would produce (`state_code`, `state_description`, `ccss_codes`, `relationship`, `needs_review`, `note`) -- there's no intermediate generator script. Re-verify any of them any time with:
```
python3 verify_mapping.py states/ga/mapping_final.json --state-standards "states/ga/georgia_math_*.json"
python3 verify_mapping.py states/va/mapping_llm.json   # no --state-standards: VA coverage is partial, see below
```

## Two ways to run the classification step

**With an API key** (the intended long-term path):
```
export ANTHROPIC_API_KEY=...
python3 map_state_to_ccss.py --state-standards "path/to/state_math_*.json" \
    --state-name Virginia --out states/va_full/mapping_llm.json
```
This calls Claude once per state leaf standard, with the full CCSS K-5 candidate list in the prompt every time (no retrieval/embedding pre-filter — see below), validates every response, and runs `verify_mapping.py` automatically at the end.

**Without an API key** (what `states/ga/` and `states/va/` actually used): the classification step was performed directly in a Claude Code session, following the exact same rules in `taxonomy.py`, and the results were saved in the same schema `map_state_to_ccss.py` would have produced. Same rules, same model family — but not the same reproducible, headless artifact a standalone script is. Getting an API key and re-running for real is an open item.

## Why no retrieval/embedding pre-filter

With only ~175 CCSS K-5 leaf codes total, the full candidate list fits easily in one prompt. Skipping retrieval removes a whole failure mode (a true match getting filtered out before the model ever sees it) for no real cost. Every classification call sees the complete CCSS K-5 candidate set, every time.

## The relationship taxonomy

See `taxonomy.py`'s `RELATIONSHIP_TYPES` for the full descriptions: `exact`, `merge`, `split`, `different_grade`, `state_superset`, `state_subset`, `partial`, `none`.

**`needs_review` is `true` if and only if `relationship` is one of `{partial, state_subset, none}`.** Those three are either explicitly low-confidence (`partial`, `state_subset`) or a genuine gap worth a human/advisor look (`none`). The other five are confident enough not to flag.

**Cardinality is decided before scope.** `exact` / `state_superset` / `state_subset` are reserved *exclusively* for a true one-state-standard-to-one-CCSS-standard pair. If a state standard's content requires more than one CCSS code (or several state standards jointly cover one CCSS code), it's `merge`/`split` — full stop — even if it also looks like a superset/subset of the union. That nuance goes in the `note`, not the category. `verify_mapping.py` asserts this can't regress: no `state_superset`/`state_subset` entry may cite more than one CCSS code.

**Split-integrity.** A `split` relationship means this state code is one of SEVERAL jointly covering a CCSS code, so at least one other entry in the same mapping must also cite it. `verify_mapping.py`'s `split_relationship_has_no_sibling` check catches a `split` entry whose claimed sibling doesn't actually exist — found and fixed 3 real instances of exactly this bug in the flat run's original output (see "How the adopted mapping was reviewed" below).

## `states/ga/mapping_final.json` — the adopted GA ↔ CCSS mapping

Built by running the flat method (`map_state_to_ccss.py`'s logic) once, independently, over all 150 GA sub-standards against the full CCSS K-5 candidate set — then reviewing every code by hand. 8 of the 150 needed correction; **142/150 (95%) of the script's raw output required no change at all.** Full review trail, including the script's original (wrong) output for each corrected code: `states/ga/human_review.json`.

The 8 corrections, categorized:

| Error type | Count |
|---|---|
| Invalid split — claimed sibling doesn't actually cite the same CCSS code | 3 |
| Merge boundary incomplete — right relationship type, incomplete code set | 2 |
| Scope/label judgment, same single code | 1 |
| False split claimed | 1 |
| Merge/exact cardinality miss | 1 |

Half the corrections are the same underlying bug: the script asserted `split` without verifying the sibling it named actually exists. `verify_mapping.py`'s split-integrity check (above) now catches this automatically for any future run. One of the three (`K.GSR.8.2`) wasn't found by the manual review pass at all — it was caught only by that automated check, since the classification the human reviewer was comparing against shared the identical bug (see below).

`verify_mapping.py` also flags (not an error, a lint): `3.MDR.5.1`, `4.MDR.6.2`, and `5.MDR.7.1` are each labeled `partial` while citing a CCSS code that's *also* cited by a different, confidently-matched GA entry at the same grade — worth a look on its own, not yet resolved.

## How the adopted mapping was reviewed

There is no independently-verified "gold" GA↔CCSS mapping to compare against — the thesis author is the only reviewer, so this project doesn't claim ground-truth accuracy, only that every classification has been checked by hand and makes sense on its own terms. The review process: for every one of the flat script's 150 GA classifications, an initial pass compared it against an earlier hand-built classification of the same 150 codes; wherever the two disagreed (25 codes), both were laid out side by side and independently re-examined against the actual GA and CCSS standard text, reaching one of two verdicts — **"error"** (the script's classification doesn't hold up; apply a correction) or **"okay"** (a defensible judgment call either way, or the script's own answer is actually the better one). Result: 7 errors, 18 okay. `verify_mapping.py`'s split-integrity check then caught one further bug (`K.GSR.8.2`) invisible to that comparison, because the earlier hand-built classification it was being checked against shared the identical error. Total: 8 corrections out of 150.

Full trail, including every one of the 25 non-trivial codes (not just the 8 that needed correction): `states/ga/human_review.json`.

## Generalizability: the VA demonstration

The pipeline is state-agnostic — `map_state_to_ccss.py` and `taxonomy.py` take any state's K-5 standards in the same schema, and CCSS's own standards ship bundled in `ccss_standards/` so a new user doesn't need to curate them separately. As a second demonstration beyond GA, the flat method was run on the 21 VA SOL codes whose text is available via EDUMath's crosswalk (Christ et al., "Standards-Aligned Math Word Problem Generation," from `github.com/bryanchrist/EDUMATH`). This is **not** Virginia's complete grades 3-5 standard set, and each entry also records which CCSS domain EDUMath's own crosswalk cited for that code.

**Gold for VA is EDUMath's crosswalk** — unlike GA's mapping above, this one really is independently verified: per direct correspondence with lead author Bryan Christ, it was built by an undergraduate student and then manually verified by an educator. It doesn't classify relationship type, so the comparison is domain-level only.

**A real granularity difference from GA, worth calling out before reading the disagreements below.** GA's own codes are sub-standard-level by construction (GaDOE assigns a distinct code to each lettered teaching point), so GA classification always operates at that fine a grain. VA's SOL codes don't work this way — one code like `3.NS.4` covers several lettered bullets with no separate identifier per bullet, and no source used here breaks VA's text into complete per-bullet form. So this pipeline classifies VA at the whole-standard level, while EDUMath's crosswalk cites one *specific* bullet per row. A disagreement between the two can be a real granularity mismatch (whole standard vs. one bullet of it), not either side simply being wrong.

```
python3 compare_to_edumath_gold.py states/va/mapping_llm.json --out states/va/comparison_to_gold.json
```
Result: **19/21 domain-level agreement**. Both disagreements trace directly to this granularity gap (confirmed by reading EDUMath's underlying row data — full detail in `states/va/unmatched_review.json`), not to an error on either side:
- `3.NS.4` (VA's money standard, whole-standard match: `2.MD.8`) — EDUMath's row is keyed to bullet `3.NS.4:d` specifically ("make change... using counting on or counting back strategies"), which it cites to `4.MD.2`. Read against that bullet alone, `4.MD.2`'s multi-step money-word-problem framing is a defensible match — arguably better than `2.MD.8` for that specific skill, even though `2.MD.8` is the better match for `3.NS.4` as a whole.
- `4.NS.3` (VA's fraction standard, whole-standard match: `4.NF.2`) — EDUMath's row is keyed to bullet `4.NS.3:g` ("represent the division of two whole numbers as a fraction"), unrelated to comparison, which it cites to `3.NF.1`. Read against that bullet, EDUMath's citation is closer to the right concept than this pipeline's whole-standard answer.

Accepted as an expected consequence of the standard-vs-sub-standard granularity difference, not scored as an error on either side.

## Hierarchical (domain → cluster → leaf) classification: tested, not adopted

Tested whether replacing the flat "one prompt, all ~175 CCSS leaf codes" search with a staged domain-family → cluster → leaf-standard traversal (the coarse-to-fine tagging structure used in some standards-tagging papers) improves accuracy. `map_state_to_ccss_hierarchical.py` is the API-based script for this method — same inputs, same output schema, and the same `taxonomy.py` rules as `map_state_to_ccss.py`, so a hierarchical run and the adopted flat mapping are directly comparable. Per state leaf standard it makes up to 3 calls instead of 1: pick plausible CCSS domain famil(y/ies), pick plausible cluster(s) within those famil(y/ies) across all K-5 grades, then run the same final classification prompt the flat script uses, narrowed to just those clusters' leaves. An empty answer at stage 1 or 2 short-circuits straight to `relationship: "none"`.

*Kept local for now, not included in this public repo* (the script and its run outputs) — findings summarized here so the result is documented even though the raw files aren't published yet.

**GA, full 150-code run**, independently re-derived, never consulting the adopted mapping while classifying: **111/150 relationship agreement (74%), 124/150 CCSS-code-set agreement (83%)** against the adopted mapping. Categorized (same fixed category set used for the 8 corrections above):

| Error type | Count |
|---|---|
| Scope/label judgment, same single code | 13 |
| Merge boundary incomplete | 9 |
| Split not recognized | 9 |
| Merge under-claimed | 7 |
| Merge over-claimed | 5 |
| Genuine content-interpretation miss | 5 |

Scope/label judgment is by far the largest bucket (13/48) — the two methods usually agree on *which* CCSS code is right, then disagree on how to label the relationship (`exact` vs. `state_superset`, etc.), because narrowing the candidate set to one cluster's ~5 leaves makes small wording differences more salient without making that judgment call any easier. This is the single biggest reason the hierarchical method underperforms. Its errors are almost never domain-selection mistakes either — the flat method already picks the right domain family nearly every time, so staged search targets a bottleneck that mostly isn't present in this dataset.

**VA, 21 codes**: **19/21 domain-level agreement against EDUMath's crosswalk — identical to the flat method**, on the same two disagreements (`3.NS.4`, `4.NS.3`). Unlike GA, staging the search made no difference: every VA code independently landed on the same CCSS domain family under both methods, likely because VA's SOL statements are broad enough (each usually spans a whole CCSS cluster or more) that domain-family selection was never the hard part.

**Not adopted as the default method** — the flat method remains the one recommended in "Two ways to run the classification step" above, and is what actually produced the adopted mapping — but the hierarchical script is kept and documented so a real API-key run can independently confirm or challenge this finding.

## What's still open

- **Get Virginia's full grades 3-5 SOL standards** into the `state_math_{grade}.json` schema `map_state_to_ccss.py` expects — the 21-code output above only covers what happened to already be quoted inside EDUMath's crosswalk.
- **Get an API key** and run `map_state_to_ccss.py` for real, so classification stops depending on a live Claude Code session.
- **Look at the hierarchical method's scope/label-judgment category** (largest, 13/48) — the single biggest reason it underperforms the flat method. (The VA comparison's two disagreements are resolved -- both are the expected standard-vs-sub-standard granularity gap, not errors; see above.)
- **Break VA's SOL text into complete per-bullet sub-standards**, if a source for that ever becomes available, so VA can be classified at the same granularity as GA and directly compared to EDUMath's bullet-level citations instead of only at the whole-standard level.
- **Resolve the `3.MDR.5.1`/`4.MDR.6.2`/`5.MDR.7.1` lint flag** — a real ambiguity the split-integrity fix didn't touch.
- **Publish the hierarchical method's own run outputs and full error-analysis breakdown**, currently kept local — see "Hierarchical classification" above.

## Adding a new state

1. Get that state's math standards into `state_math_{grade}.json` files (one per grade 0-5), matching `states/ga/georgia_math_{grade}.json`'s schema: `domains[].standards[].sub_standards[]`, each leaf with `code` and `description`. A richer per-standard guidance document (like GA's Evidence of Student Learning, `states/ga/georgia_math_guidance_{grade}.json`), if one exists, should go in a parallel `state_math_guidance_{grade}.json` and be passed to `taxonomy.build_classification_prompt`'s `state_guidance` argument — it materially improves accuracy on scope-nuance cases.
2. Run `map_state_to_ccss.py` (with an API key) or classify in a Claude Code session following `taxonomy.py` directly (without one).
3. Run `verify_mapping.py` on the output (the API script does this automatically).
4. Have every code a human hasn't already confidently agreed with reviewed by hand, same as the GA process above — this pipeline produces a strong first pass, not a substitute for review.
