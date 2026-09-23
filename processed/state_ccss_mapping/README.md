# State standard ↔ CCSS mapping pipeline

A generalizable pipeline that classifies any state's K-5 math standards against CCSS, using a fixed relationship taxonomy — so a future user doesn't need to re-derive the classification rules from scratch.

- **`states/ga/mapping_final.json`** — the adopted GA↔CCSS mapping this project uses.
- **`states/va/`** — a second demonstration, on Virginia's SOL codes.

## Directory layout

```
state_ccss_mapping/
  taxonomy.py                          Relationship taxonomy + classification rules
                                        (single source of truth for both scripts below).
  map_state_to_ccss.py                 Flat method -- the script that produced the
                                        adopted mapping. Needs ANTHROPIC_API_KEY.
  map_state_to_ccss_hierarchical.py    Alternative method, tested and not adopted
                                        (kept local, not in this repo yet).
  verify_mapping.py                    Pure-Python checks, no API calls -- see below.
  compare_to_gold.py                   Compares two mapping.json files against each other.
  compare_to_edumath_gold.py           Compares a VA mapping against EDUMath's crosswalk.
  ccss_standards/
    ccss_math_0.json ... _5.json       CCSS K-5 standards, bundled so no user has to
                                        curate this themselves.
  states/
    ga/
      georgia_standards/
        georgia_math_0.json ... _5.json           GA's own K-5 standards.
        georgia_math_guidance_0.json ... _5.json  GA's per-standard teaching guidance.
      mapping_final.json      THE adopted GA <-> CCSS mapping (150 codes, 11 corrections applied).
      mapping_llm.json        The script's original, unedited output.
      human_review.json       Every reviewed code: original output, verdict, correction.
      coverage_gap_proposed_corrections.json  Candidate corrections found while writing up
                               the coverage-loss discussion below -- pending your verdict,
                               not yet applied to mapping_final.json.
      verification_report.json
    va/
      mapping_llm.json         21 distinct VA SOL codes, classified fresh.
      comparison_to_gold.json  Comparison against EDUMath's crosswalk.
      unmatched_review.json    The 2 disagreements with EDUMath, reviewed (resolved).
      verification_report.json
```

## How the mapping was built

1. Run the flat method (`map_state_to_ccss.py`) once, independently, over every GA sub-standard against the full CCSS K-5 candidate set.
2. Run `verify_mapping.py` — checks completeness, valid CCSS codes, and the rules below.
3. Human review: every non-trivial classification checked against the actual GA and CCSS text (see "Review results" below).
4. Apply corrections → `states/ga/mapping_final.json`.

**Two ways to run step 1:**

| | With an API key | Without one |
|---|---|---|
| How | `map_state_to_ccss.py` calls Claude once per standard | Classified directly in a Claude Code session, same rules |
| Output | Same schema either way | Same schema either way |
| Used for GA/VA here? | Not yet — open item | Yes, this is what produced the current data |

```
export ANTHROPIC_API_KEY=...
python3 map_state_to_ccss.py --state-standards "path/to/state_math_*.json" \
    --state-name Virginia --out states/va_full/mapping_llm.json
```

No retrieval/embedding pre-filter: only ~175 CCSS codes total, so the full list fits in one prompt — skipping retrieval avoids a true match ever getting filtered out before the model sees it.

## The relationship taxonomy

| Type | Meaning |
|---|---|
| `exact` | Same requirement and scope, reworded at most. |
| `merge` | One state standard covers more than one CCSS code. |
| `split` | One of several state standards jointly covering a single CCSS code. |
| `different_grade` | Same skill, different K-5 grade — not a gap. |
| `state_superset` | State requires everything CCSS does, plus more. |
| `state_subset` | State requires less than CCSS does (rare). |
| `partial` | Related but narrower/different; lower confidence. |
| `none` | No CCSS match at any grade — a genuine gap. |

**Three checks `verify_mapping.py` enforces automatically:**

| Rule | What it checks | What it catches |
|---|---|---|
| Cardinality-first | `state_superset`/`state_subset` only ever cite exactly 1 CCSS code | A 2+-code entry mislabeled as superset/subset instead of `merge`/`split` |
| Split-integrity | A `split` entry's claimed sibling code actually exists and cites the same CCSS code | 3 real bugs in the flat run's raw output — see below |
| Borrowed thematic label | A `partial`/`different_grade` entry's cited CCSS code is *also* already claimed, confidently, by a different entry at the same grade | 3 more real bugs — see below |

`needs_review` is `true` iff relationship is `partial`, `state_subset`, or `none` (the three low-confidence/gap types).

Running `map_state_to_ccss.py` or `map_state_to_ccss_hierarchical.py` runs all three checks automatically at the end: `verification_report.json` always gets written, but if anything is flagged, the script **also prints every issue to stderr and exits with status 1** — a run isn't silently "successful" just because the API calls didn't error.

### The "borrowed thematic label" lint, with real examples

The idea: a low-confidence (`partial`) entry that cites a CCSS code is only a real match if nothing else already owns that code more confidently at the same grade. If some other entry already claims it `exact`/`merge`/`split`/etc., the `partial` entry probably just grabbed the nearest topically-related code because its own GA text was vague — not because it's a genuine match. Three GA codes tripped this, each resolved individually against the actual standard text (not a blanket fix):

| Code | GA text (paraphrased) | Was cited | Already confidently owned by | Fix |
|---|---|---|---|---|
| `3.MDR.5.1` | Ask questions from graphical displays | `3.MD.3`, `3.MD.4` | `3.MD.4` → `3.MDR.5.4` (ruler measurement, unrelated topic) | Dropped `3.MD.4`; kept `3.MD.3` (unclaimed elsewhere, a real match); stayed `partial` |
| `4.MDR.6.2` | Ask questions from graphical displays | `4.MD.4` | `4.MD.4` → `4.MDR.6.3` (dot plots) | No CCSS code left once the borrowed one was ruled out → `none` (genuine gap) |
| `5.MDR.7.1` | Explore problems with different measurement units | `5.MD.1` | `5.MD.1` → `5.MDR.7.3` + `5.MDR.7.4` (metric + customary conversions, jointly covering all of it) | Same — nothing left to attach to → `none` (genuine gap) |

`3.MDR.5.1` and `4.MDR.6.2` are two different grades of the *same* recurring GA sentence ("ask questions and answer them... graphical displays..."), which is why they hit the same pattern; `5.MDR.7.1` is a different, unrelated GA standard that happened to trip the identical check on a different CCSS code.

## Error type definitions

Used both for the 11 GA corrections below and for the hierarchical-vs-adopted comparison. 5 categories, applied in this order — **every disagreement gets exactly one**, never more than one:

| Step | Check | Category if matched |
|---|---|---|
| 1 | Either side's `split` claim has no real sibling in its own mapping (a structural bug, checked on its own terms — not by comparing the two sides) | **Invalid split** |
| 2 | The two sides' CCSS code sets are identical, but exactly one side calls it `split` | **Split-status disagreement** |
| 3 | The two sides' CCSS code sets are identical, and neither calls it `split` (they disagree among `exact`/`state_superset`/`state_subset`/`partial`/`different_grade` instead) | **Scope/label judgment** |
| 4 | The two sides' CCSS code sets overlap, but aren't identical | **Code-set boundary mismatch** |
| 5 | The two sides' CCSS code sets share nothing in common | **Genuine content miss** |

Earlier drafts of this table used 8 categories (e.g. separate "merge under/over-claimed," "false split claimed," "split not recognized") that described the *same* underlying disagreements from different angles and could overlap on a single code. This version classifies by two hard facts only — does either side's split claim actually hold up, and how much do the two cited code sets overlap — so categories can't collide.

## Review results — GA

**11 of 150 codes corrected (139/150, 93%, needed no change).** Full trail: `states/ga/human_review.json`.

**Relationship-type breakdown (`states/ga/mapping_final.json`, 150 codes):**

| Relationship | Count | % |
|---|---|---|
| `exact` | 56 | 37.3% |
| `merge` | 32 | 21.3% |
| `split` | 18 | 12.0% |
| `none` | 14 | 9.3% |
| `state_superset` | 12 | 8.0% |
| `different_grade` | 7 | 4.7% |
| `state_subset` | 7 | 4.7% |
| `partial` | 4 | 2.7% |

**Corrections by error type:**

| Error type | Count | Codes |
|---|---|---|
| Invalid split | 3 | `K.GSR.8.2`, `3.GSR.7.2`, `3.GSR.7.3` — claimed sibling never actually cited the same CCSS code |
| Code-set boundary mismatch | 3 | `3.NR.4.1`, `4.GSR.7.1`, `4.GSR.8.2` — right idea, code set incomplete |
| Borrowed thematic label | 3 | `3.MDR.5.1`, `4.MDR.6.2`, `5.MDR.7.1` — cited a CCSS code a same-grade sibling already confidently owns (see below) |
| Split-status disagreement | 1 | `3.MDR.5.4` — script said `split`, correct answer is `exact` |
| Scope/label judgment | 1 | `3.GSR.6.2` — same code, `exact` vs. `state_superset` |

**How the review worked:**
1. Compare the flat script's 150 classifications against an earlier hand-built classification of the same codes.
2. Where they disagreed (25 codes): lay both side by side, re-examine against the actual standard text, assign a verdict — `error` (script is wrong, fix it) or `okay` (defensible either way, or script was already right). → 7 errors, 18 okay.
3. `verify_mapping.py`'s split-integrity check catches 1 more bug (`K.GSR.8.2`) invisible to step 2, because the hand-built classification it was compared against shared the identical bug.
4. `verify_mapping.py`'s "borrowed thematic label" lint flags 3 more (`3.MDR.5.1`, `4.MDR.6.2`, `5.MDR.7.1`) — each `partial`, citing a CCSS code a same-grade sibling already confidently owns. Resolved individually, not as a blanket fix:
   - `3.MDR.5.1` cited two codes; only one was actually borrowed. Dropped it, kept the other, stayed `partial`.
   - `4.MDR.6.2` and `5.MDR.7.1` had no other CCSS code left once the borrowed one was ruled out → genuine gaps, `none`.
5. **Total: 11 corrections.**

There's no independently-verified "gold" mapping for GA — the thesis author is the only reviewer. This process checks that every classification makes sense on its own terms, not that it matches ground truth. `verify_mapping.py` now reports **clean: true** — zero open lint flags.

### Coverage loss: how much of each standard set isn't matched

`mapping_final.json` is indexed by GA code — so "coverage" is actually two
different questions that are easy to conflate:

| direction | denominator | not matched | % |
|---|---|---|---|
| GA → CCSS (GA code has no CCSS equivalent, `relationship: none`) | 150 GA codes | 14 | **9.3%** |
| CCSS → GA (no GA code cites this CCSS code, at any granularity) | 191 CCSS K-5 leaf codes | 39 | **20.4%** |
| ...of those 39, a parent/child granularity artifact (bare parent uncited, but a lettered child of it *is* cited — e.g. `1.NBT.2` vs. `1.NBT.2a/b/c`) | 191 | 15 | 7.9% |
| ...of those 39, genuine gaps (uncited at any granularity) | 191 | **24** | **12.6%** |

The CCSS-side number is structurally larger, and that's expected, not a
quality problem: this mapping was built by finding each of GA's 150 codes
its single best CCSS anchor, not by working through the CCSS list looking
for a GA match for every code. A CCSS code can go uncited simply because no
GA code happened to need it as its *closest* match — even when GA's
curriculum functionally covers that content elsewhere. `3.OA.1`/`3.OA.2`
(the base definitions of multiplication/division) are a likely example of
this: GA surely teaches the underlying ideas, they just weren't any single
GA code's best/closest anchor.

**What kind of content is lost on each side:**

GA's 14 uncited codes, by content type:

| type | count | codes |
|---|---|---|
| Patterns (PAR domain — repeating/growing/shrinking patterns, equal-sign reasoning) | 7 | `K.PAR.6.1`, `K.PAR.6.2`, `1.PAR.3.1`, `1.PAR.3.2`, `2.PAR.4.1`, `2.PAR.4.2`, `3.PAR.3.4` |
| Open-ended data inquiry ("ask and answer questions from gathered information") | 3 | `K.MDR.7.3`, `4.MDR.6.2`, `5.MDR.7.2` |
| Money | 2 | `K.NR.1.4`, `1.MDR.6.3` |
| Measurement construction/units (building instruments, realistic multi-unit problems) | 2 | `2.MDR.5.1`, `5.MDR.7.1` |

CCSS's 24 genuinely-uncited codes, by domain:

| domain | count | codes |
|---|---|---|
| MD (Measurement & Data) | 9 | `2.MD.2`, `2.MD.5`, `3.MD.5a`, `4.MD.7`, `5.MD.2`, `5.MD.3`, `5.MD.3a`, `5.MD.3b`, `5.MD.5c` |
| NF (Number & Operations—Fractions) | 5 | `3.NF.3a`, `4.NF.3a`, `4.NF.4b`, `4.NF.4c`, `5.NF.4b` |
| G (Geometry) | 4 | `2.G.2`, `3.G.2`, `K.G.2`, `K.G.3` |
| OA (Operations & Algebraic Thinking) | 3 | `1.OA.5`, `3.OA.1`, `3.OA.2` |
| CC (Counting & Cardinality) | 2 | `K.CC.4a`, `K.CC.7` |
| NBT (Number & Operations in Base Ten) | 1 | `2.NBT.9` |

**Whole standards vs. single missing sub-clauses.** Of the 24, **14 are bare,
unlettered standards** with no sub-parts to compare (`1.OA.5`, `2.G.2`,
`2.MD.2`, `2.MD.5`, `2.NBT.9`, `3.G.2`, `3.OA.1`, `3.OA.2`, `4.MD.7`,
`5.MD.2`, `K.CC.7`, `K.G.2`, `K.G.3`, and `5.MD.3` — whose own two lettered
children are *also* both uncited, so all of `5.MD.3` is a gap, not just the
parent). The other **10 are one specific lettered clause of an otherwise
GA-covered standard** — checking each against its siblings:

| gap code | siblings' status | which clause is missing |
|---|---|---|
| `3.NF.3a` | b, c, d all cited | the **definition** ("two fractions are equivalent if same size / same point on a number line") — b/c/d (generate, express as whole number, compare) are covered |
| `4.NF.3a` | b, c, d all cited | same shape: the definition ("understand addition/subtraction of fractions as joining/separating parts") — b/c/d covered |
| `K.CC.4a` | b, c cited | the definition (pair each object with one number name in order) — b, c (cardinality, "one more") covered |
| `3.MD.5a` | b cited | the definition ("a unit square... has one square unit of area") |
| `4.NF.4b`, `4.NF.4c` | **a** is cited, b and c are not | reverse shape: the definition (a — "a multiple of a/b as a multiple of 1/b") is covered; the two application clauses (scale a fraction by a whole number; solve word problems) are not |
| `5.NF.4b` | a cited | the application clause (find area of a rectangle with fractional side lengths) — the definition (a) is covered |
| `5.MD.5c` | a, b cited | the composite-shapes application clause ("volume is additive... find volumes of composite figures") — the basic volume-formula clauses (a, b) are covered |
| `5.MD.3a`, `5.MD.3b` | (each other) both uncited | looked like a full-standard gap at first — **but see the follow-up below: likely a mapping omission, not a true gap** |

So it's not a single clean rule ("GA always skips the definition" or "always
skips the last clause") — it goes both ways. What's consistent is *shape*:
in most of these 10 codes, GA cites most of a CCSS standard's sub-parts but leaves one or two
out, and the one left out is either the standalone conceptual
definition (`3.NF.3a`, `4.NF.3a`, `K.CC.4a`, `3.MD.5a`) or a narrower
real-world/composite application that extends past what any single GA code
was anchored to (`4.NF.4b/c`, `5.NF.4b`, `5.MD.5c`). Worth a closer look
per-code before treating any of these 10 as truly uncovered by GA — several
are plausibly implicit in the sibling clause GA *did* cite.

**Follow-up: checked each of the 10 against the actual text of the GA code
that already cites its sibling(s), looking for whether that code's own
description already states the "missing" content.** Findings, and 4
candidate corrections to `mapping_final.json`, are in
`states/ga/coverage_gap_proposed_corrections.json` — pending review, not yet
applied:

| code | verdict | why |
|---|---|---|
| `5.MD.3a`/`3b` | **likely mapping omission** | `5.GSR.8.3`'s own text ("packing... with unit cubes without gaps or overlaps... determine total volume") already states this definition — it's currently merged to `5.MD.4`/`5.MD.5a` only |
| `4.NF.4b`/`4c` | **likely mapping omission** | GA doesn't skip this content — it teaches it one grade later, at `5.NR.3.4` ("multiplication of a fraction and a whole number"), which should probably carry `4.NF.4b/4c` as `different_grade` |
| `3.MD.5a` | **likely mapping omission** | same shape as `5.MD.3a/3b` — `3.GSR.7.1`'s text already states the unit-square definition |
| `3.NF.3a` | **weaker candidate** | `3.NR.4.4` ("recognize and generate simple equivalent fractions") presupposes the definition but doesn't state it |
| `5.NF.4b`, `5.MD.5c` | **confirmed genuine gaps** | searched every GA standard for the relevant content (fraction-side-length area; composite-figure volume) — neither exists anywhere in GA K-5 |
| `K.CC.4a` | **ambiguous** | plausibly an implicit prerequisite skill for `K.NR.1.1` rather than the same content point; already modeled as a real prerequisite edge in `../progression_mapping/ccss_progressions.json` |

**Discussion, for the thesis writeup:** the 9.3% GA-side figure is the more
load-bearing number, since it identifies content Georgia teaches that has
*no* CCSS Progressions document to ground prerequisite edges against at all
— exactly the `provenance: ga_native` set called out in
`../progression_mapping/README.md`'s stage 2 plan. The 20.4%/12.6% CCSS-side
figures are a property of this mapping's GA-anchored construction method
more than a claim about GA's curricular coverage, and shouldn't be read as
"CCSS content Georgia doesn't teach" without checking each code individually
first.

## Review results — VA

21 distinct VA SOL codes (not Virginia's full grade 3-5 set — only what EDUMath's crosswalk happens to cite). Gold here **is** independently verified: EDUMath's crosswalk was built by a student, checked by an educator (Christ et al., `github.com/bryanchrist/EDUMATH`).

| | |
|---|---|
| Agreement | 19/21 (90%), domain-level only |
| Disagreements | `3.NS.4`, `4.NS.3` — both resolved, see below |

**Relationship-type breakdown (`states/va/mapping_llm.json`, 21 codes — identical for the hierarchical run too):**

| Relationship | Count | % |
|---|---|---|
| `merge` | 8 | 38.1% |
| `exact` | 5 | 23.8% |
| `different_grade` | 2 | 9.5% |
| `state_superset` | 2 | 9.5% |
| `partial` | 2 | 9.5% |
| `split` | 1 | 4.8% |
| `state_subset` | 1 | 4.8% |

**Why domain-level only, and why GA uses sub-standard-level:** GA's own codes are sub-standard-level by construction (one code per lettered teaching point). VA's SOL codes aren't — one code covers several lettered bullets with no separate ID per bullet, and no available source breaks VA's text into complete per-bullet form. So this pipeline classifies VA at the whole-standard level, while EDUMath cites one specific bullet per row.

| Code | This pipeline (whole standard) | EDUMath (one bullet) | Resolution |
|---|---|---|---|
| `3.NS.4` | `2.MD.8` (money computation) | `4.MD.2`, keyed to bullet d) "make change using a strategy" | Granularity gap, not an error — `4.MD.2` is defensible for that specific bullet |
| `4.NS.3` | `4.NF.2` (fraction comparison) | `3.NF.1`, keyed to bullet g) "represent division as a fraction" | Granularity gap, not an error — bullet isn't about comparison at all |

Full detail: `states/va/unmatched_review.json`.

## Hierarchical method: tested, not adopted

Alternative to the flat method: stage the search (pick domain family → pick cluster → classify against just those leaves) instead of showing all ~175 CCSS codes at once. *Kept local, not in this repo yet* — findings summarized here regardless.

**Relationship-type breakdown, GA hierarchical run (150 codes) vs. the adopted mapping:**

| Relationship | Hierarchical (n, %) | Adopted (n, %) |
|---|---|---|
| `exact` | 56, 37.3% | 56, 37.3% |
| `merge` | 31, 20.7% | 32, 21.3% |
| `state_superset` | 18, 12.0% | 12, 8.0% |
| `state_subset` | 16, 10.7% | 7, 4.7% |
| `different_grade` | 11, 7.3% | 7, 4.7% |
| `none` | 9, 6.0% | 12, 8.0% |
| `split` | 8, 5.3% | 18, 12.0% |
| `partial` | 1, 0.7% | 6, 4.0% |

Same total per-type usage overall, but shifted heavily toward `state_superset`/`state_subset` and away from `split`/`partial` — consistent with the error-type finding below (narrower candidate view → more scope/label judgment calls, less recognition that a code is jointly split with siblings).

| Dataset | Relationship agreement | Code-set agreement |
|---|---|---|
| GA, 150 codes | 111/150 (74%) | 124/150 (83%) |
| VA, 21 codes | 19/21 (90%), identical to flat | domain-level only |

**GA disagreements by error type (48 total):**

| Error type | Count |
|---|---|
| Code-set boundary mismatch | 20 |
| Scope/label judgment | 13 |
| Split-status disagreement | 9 |
| Genuine content miss | 6 |
| Invalid split | 0 |

**Why it underperforms:** code-set boundary mismatch and scope/label judgment together are 33/48 — both methods usually agree on *which* CCSS code is right, then disagree on the exact code set or how to label the relationship. Narrowing to one cluster's ~5 leaves makes small wording differences louder without making that judgment easier. It's almost never a domain-selection mistake (flat already picks the right family nearly every time), so staging fixes a bottleneck that mostly isn't there.

**VA:** staging made no difference — every code landed on the same domain family either way, since VA's SOL statements are broad enough that domain selection was never the hard part.

**Flat method remains the recommended default and is what produced the adopted mapping.**

## What's still open

- Get an API key and run `map_state_to_ccss.py` for real, instead of a manual session.
- Publish the hierarchical method's run outputs + full error analysis (currently local-only).

## Adding a new state

1. Get standards into `state_math_{grade}.json` files (grades 0-5), matching `states/ga/georgia_standards/georgia_math_{grade}.json`'s schema: `domains[].standards[].sub_standards[]`, each leaf with `code` + `description`. Guidance content (optional, improves accuracy), matching `states/ga/georgia_standards/georgia_math_guidance_{grade}.json`, goes in a parallel `state_math_guidance_{grade}.json` and is passed via `taxonomy.build_classification_prompt`'s `state_guidance` argument.
2. Run `map_state_to_ccss.py` (with a key) or classify by hand following `taxonomy.py` (without one).
3. Run `verify_mapping.py` — automatic if using the API script.
4. Review every non-obvious code by hand, same as the GA process above. This pipeline produces a strong first pass, not a substitute for review.
