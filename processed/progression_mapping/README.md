# Progression mapping

This directory holds the work to rebuild `../math_prereq_grounding.json` on a
cleaner, two-stage foundation, plus the MathFish/Achieve the Core comparison
that led to that decision.

`math_prereq_grounding_outdated.json` in this directory is a **read-only
copy** of `../math_prereq_grounding.json`, kept here as the fixed baseline
stage 3's diff step compares against. The live file stays at its original
path since `proposal.typ`, `processed/preprocess.typ`, and
`processed/README.md` all reference it there — this rebuild doesn't touch
that path until the final merge (Plan step 4). `processed/preprocess.typ`
already independently flags that file as a "standing issue" needing review,
for the same reasons this rebuild exists.

## Why a rewrite

`../math_prereq_grounding.json`'s 148 edges were authored by reading the CCSS
Progressions PDF and hand-translating into Georgia GSE codes *at the same
time* — that's why some citations are messy free text
(`"1.OA.1 / 1.OA.6 (strategies)"`, `"K.OA.1-3"`) instead of clean codes: the
translation was done live, in your head, while reading. Now that
`../state_ccss_mapping/states/ga/mapping_final.json` exists — a reviewed,
adopted GA↔CCSS mapping for all 150 Georgia K-5 sub-standards — the two jobs
can be split apart:

1. **Stage 1 — CCSS-native progressions.** Read the Progressions PDF
   (`../scripts/ccss_progressions_all.pdf`, 333 pages, all domains) and write
   prerequisite edges purely in CCSS-code space (`ccss_from → ccss_to`, same
   5-rule taxonomy, page + quote citation), checked only against the CCSS K-5
   standards list. No Georgia judgment calls mixed in. This also fixes the
   "stale OA_PROG pagination" issue flagged in the current grounding file's
   metadata, since edges are cited fresh against this PDF's real page numbers.
2. **Stage 2 — mechanical translation.** Run every stage-1 edge through
   `mapping_final.json`'s reverse index (CCSS code → GA code) to produce GA
   edges. This is a lookup, not a judgment call — the judgment already
   happened once, when `mapping_final.json` was reviewed and adopted.

### The complication stage 2 has to handle

`mapping_final.json`'s relationship types aren't all 1:1, so the reverse
lookup isn't trivial:

| relationship | count | reverse-lookup behavior |
|---|---|---|
| exact / state_superset / state_subset | 56+12+7=75 | clean 1:1, no issue |
| merge | 32 | one GA code covers multiple CCSS codes → several CCSS edges may collapse onto the same GA code |
| split | 18 | several GA codes jointly cover one CCSS code → one CCSS edge may fan out into several GA edges |
| different_grade | 7 | GA code sits at a different grade than the CCSS code it maps to — affects which grade an edge "counts" as |
| partial | 6 | weak match — keep, but flag lower confidence |
| none | 12 | no GA equivalent exists — these CCSS-side edges can't be translated at all |

And separately: Georgia has content with **no CCSS home at all** (the
`none`-mapped codes — patterns/PAR domain sequencing, money, time). Those can
never come out of stage 2, since there's no CCSS edge to translate. They stay
hand-authored, same as today, but labeled as a distinct provenance category
instead of blended in with the auto-translated edges.

### Plan

1. Re-read `ccss_progressions_all.pdf` and produce `ccss_progressions.json`
   in this directory — CCSS-only edges, fresh page citations. **(this step)**
2. Write `translate_progressions_to_ga.py`: build the CCSS→GA reverse index
   from `mapping_final.json`, apply it to every stage-1 edge, drop edges
   touching a `none`-mapped code (logging what got dropped, same idea as the
   ATC gap-list below), tag `partial`/`state_subset`-derived edges as
   lower-confidence, dedupe edges that collapse together, and union citations
   (CCSS Progressions quote + the specific `mapping_final.json` note) so each
   output edge carries the full chain of custody.
   - Default for `split` (one CCSS edge → several GA edges): emit **all**
     resulting GA edge combinations rather than picking one "primary" —
     under-connecting silently would be worse than a few edges a human
     review pass can prune.
3. Diff the result against the current 148 hand-authored edges — what
   survives unchanged, what gets a cleaner citation, what's genuinely new,
   and what (patterns/money/time) has no automatic equivalent and must stay
   hand-authored.
4. Merge: final grounding file = auto-translated edges
   (`provenance: ccss_translated`) + the residual GA-only hand-authored edges
   (`provenance: ga_native`), replacing `../math_prereq_grounding.json`
   (version bump from 0.12).
5. Re-run `validate_skills.py` / resume `skills_math_*.json` authoring once
   the new grounding file is in place.

### Status

- [x] MathFish/Achieve the Core comparison (see below) — informed the
      decision to keep the Progressions-PDF as the primary source and use
      ATC only for cross-validation and gap-finding.
- [x] Stage 1 — `ccss_progressions.json` (2026-09-23): **147 edges**, from a
      full page-by-page read of `ccss_progressions_all.pdf` pages 16–161
      (every K-5 sub-document; the PDF moves into Grade 6+ Ratios &
      Proportional Relationships at page 162, out of scope). By rule:
      concept_foundation 58, grade_progression 57, decomposition 16,
      bloom_progression 13, scope_expansion 3. By domain (of the `from`
      code): NF 42, MD 36, OA 21, NBT 18, G 17, CC 13. All 147 edges
      validated against the authoritative K-5 CCSS leaf-code list in
      `../state_ccss_mapping/ccss_standards/` (0 invalid codes, 0 duplicate
      from/to pairs); page/quote citations spot-checked directly against the
      PDF. Sub-standard-letter sequencing (e.g. `K.CC.4a→4b→4c`,
      `5.NF.5a→5b`) is included throughout — the granularity ATC lacks (see
      comparison above). 17 edges come directly from the Measurement & Data
      Progression's own "Notable connections" table. One edge
      (`5.NF.4→5.NF.5a`) is marked `continues_beyond_k5: true` since the
      source text frames it as Grade-6 prep. Extraction favored precision
      over exhaustiveness: only edges with an explicit, quotable
      code-to-code claim were kept, so this is not a claim of *every*
      possible prerequisite relationship in the text, just what it
      explicitly supports.
- [ ] Stage 2 — `translate_progressions_to_ga.py` — **planned, not yet
      written** (see "Stage 2 plan" below).
- [ ] Diff + merge into new `math_prereq_grounding.json`

## Stage 2 plan

`mapping_final.json` (copied into this directory) is per-GA-code: each of the
150 GA leaf standards lists the CCSS code(s) it corresponds to. Stage 2 needs
the reverse direction — CCSS code → GA code(s) — so the first thing the
script builds is that reverse index. Before writing the script, I ran the
actual reverse lookup against all 147 stage-1 edges to find the real shape of
the problem, rather than guess at it:

**The reverse index is not cleanly split by relationship type.** A single
CCSS code can map back to several GA codes carrying *different* relationship
types at once — it's a property of each (CCSS, GA) pair, not of the CCSS code
as a whole. E.g.:
```
4.G.3   -> [(2.GSR.7.2, different_grade), (3.GSR.6.3, different_grade),
            (4.GSR.8.1, merge), (4.GSR.8.2, merge)]
4.NBT.2 -> [(3.NR.1.1, different_grade), (3.NR.1.2, different_grade),
            (4.NR.1.1, split), (4.NR.1.3, split)]
```
(GA apparently revisits pieces of 4.G.3/4.NBT.2's content at earlier grades
in addition to the grade-4 treatment CCSS states once.)

**This mixed-type fan-out doesn't need a human pick between candidates —
grade-matching resolves it mechanically.** Checked all 21 CCSS codes that
have more than one GA candidate:

| pattern | count | resolution |
|---|---|---|
| same-grade only, all `split`/`merge` | 14 | pure siblings — GA jointly decomposes one CCSS standard into co-equal parts; keep all, no ranking needed |
| same-grade only, other types (e.g. `merge`+`state_superset`) | 1 | same as above — both types are already high-confidence individually |
| mixed same-grade + `different_grade` | 6 | keep only the same-grade candidate(s); set the `different_grade` ones aside as a "GA also revisits this at grade X" annotation, not a parallel edge |
| all candidates cross-grade, nothing at the code's own grade | 0 | (would fall back to the cross-grade set with `needs_review: true`; never occurred) |

One case (`4.NF.2`) confirmed the rule needs to be **grade-match, not
relationship-type-match**: its off-grade candidate is tagged `partial`, not
`different_grade`, so a rule that only special-cased the `different_grade`
label would have missed it. Filtering by the candidate's actual grade against
the CCSS code's own grade catches it too. Net effect: **fan-out (multiple GA
candidates) is never itself a reason to flag an edge for review** — same-grade
multiplicity is always a legitimate sibling decomposition in this data, so
it's kept in full; cross-grade multiplicity is resolved by preferring the
same-grade candidate(s) and demoting the rest to an annotation.

**Granularity mismatch between the two files.** `mapping_final.json`'s CCSS
citations are keyed to whatever GA needed to cite (often a lettered
sub-standard, e.g. `5.NF.5a`); stage 1's edges sometimes use the bare parent
code (`5.NF.5`) when the Progressions text discusses the standard before
drilling into its lettered parts. Checked against all 133 distinct CCSS
codes touched by the 147 edges: 26 don't appear directly in the reverse
index. Of those, 11 are recoverable by falling back to the **union of GA
codes mapped to that parent's lettered children** (e.g. `5.NF.4` → union of
whoever maps to `5.NF.4a`) — tested a parent-fallback in the other direction
(child code → look up its bare parent) too, but it recovered zero cases in
this data, so it's not worth the extra code path. The remaining 15 are
genuine gaps — no GA standard in `mapping_final.json` was classified against
them at all (`K.CC.4a`, `K.CC.7`, `3.OA.1`, `3.G.2`, `2.G.2`, `2.MD.2`,
`2.MD.5`, `5.MD.2`, `5.MD.3`, `4.MD.7`, `3.NF.3a`, `4.NF.3a`, `4.NF.4b`,
`4.NF.4c`, `5.MD.5c`) — logged for human review, not silently dropped.

**Net result across all 147 edges**, using direct lookup + the
children-union fallback + grade-preference filtering:

| | count |
|---|---|
| both endpoints resolve to ≥1 GA code | 115 |
| only one endpoint resolves (edge can't be translated) | 30 |
| neither endpoint resolves | 2 |
| **raw GA edges (after grade-filtering, before deduping identical pairs across different source CCSS edges)** | **150** |
| ...of those, `needs_review: false` | **89** |
| ...of those, `needs_review: true` | **61** (44 from the children-union fallback's granularity guess, 23 inherited from an endpoint's own `partial`/`state_subset` tag in `mapping_final.json`) |

Grade-filtering (see above) already dropped the raw combination count from
161 (naive Cartesian product) to 150 — and, more importantly, fan-out is no
longer counted as a reason for review at all, so the 61 `needs_review: true`
edges are exactly the ones with a *genuine* judgment call baked in, not
inflated by ordinary sibling multiplicity.

### Algorithm
1. Build the CCSS→GA reverse index from `mapping_final.json` (code →
   list of `(ga_code, relationship, needs_review, note)`).
2. `resolve(ccss_code)`:
   a. Direct hit in the index → those candidates.
   b. Else, union of any `{code}[a-z]` lettered children present in the
      index (the parent/child granularity-mismatch fallback).
   c. Else unresolved.
3. **Grade-filter** the resolved candidate set: keep only candidates whose
   own grade matches `ccss_code`'s grade. If that leaves the set empty, fall
   back to the full (cross-grade) set and mark it `needs_review: true`
   (never triggered in this data, but a real possibility for a future state
   or a grounding-file update). The candidates filtered *out* aren't
   discarded — recorded as `other_grade_ga_codes` on the edge, since "GA
   also covers this a grade earlier" is useful provenance even when it's not
   this edge's translation target.
4. For each of the 147 stage-1 edges: resolve + grade-filter both `from` and
   `to`.
   - Either side unresolved → log to `translation_gaps.json` with a reason
     (`no_ga_mapping` / `only_beyond_k5` / etc.), emit no GA edge.
   - Both resolve → Cartesian product of the (already grade-filtered)
     candidates on each side, drop any pair where `ga_from == ga_to`
     (self-loop), emit one candidate GA edge per remaining pair. Same-grade
     multiplicity on either side is kept in full as siblings — no ranking or
     pruning among them.
5. Each candidate GA edge carries the full chain of citations: the stage-1
   CCSS page + quote, *and* the `mapping_final.json` note(s) for both
   endpoints — so a reviewer can see both "why this is a real CCSS
   prerequisite" and "why this GA code is that CCSS code."
6. **`needs_review` rule** (fan-out is *not* one of the triggers): an edge is
   `needs_review: true` if *either* endpoint (a) resolved only via the
   children-union fallback, (b) itself carries `needs_review: true` in
   `mapping_final.json` (i.e. relationship `partial` or `state_subset`), or
   (c) fell back to the cross-grade candidate set in step 3. Otherwise
   `false` — including when there's same-grade fan-out, since that's an
   expected sibling decomposition, not uncertainty.
7. Dedupe: if two different stage-1 CCSS edges translate to the same
   `(ga_from, ga_to)` pair, merge into one output edge and union their
   citations (this is a corroboration signal worth keeping, not noise).
8. Output: `ga_progressions_translated.json` (the auto-translated edges) +
   `translation_gaps.json` (the 32 untranslatable stage-1 edges, for a human
   decision on whether they need a hand-authored GA-native edge instead).

### Worked examples

**Simple case: `K.CC.5 → K.MD.3` (no fan-out).** Stage-1 edge:
```json
{"from": "K.CC.5", "to": "K.MD.3", "rule": "concept_foundation", "page": 80,
 "source": "Notable connections table (K.MD.3 row): K.CC. Counting to tell the number of objects."}
```
Reverse-lookup each side in `mapping_final.json` (which GA `state_code` cites
this CCSS code):
- `K.CC.5` ← `K.NR.1.1` (`exact`)
- `K.MD.3` ← `K.MDR.7.2` (`exact`, note: *"Classify/sort into categories,
  count, sort by count, matches verbatim"*)

Both sides singleton, direct, `exact` → exactly **one** output edge,
`needs_review: false`:
```json
{"from": "K.NR.1.1", "to": "K.MDR.7.2", "rule": "concept_foundation",
 "provenance": "ccss_translated",
 "ccss_from": "K.CC.5", "ccss_to": "K.MD.3",
 "ccss_citation": {"page": 80, "source": "Notable connections table..."},
 "ga_mapping_notes": {"K.NR.1.1": "exact match to K.CC.5",
                       "K.MDR.7.2": "exact match to K.MD.3"},
 "needs_review": false}
```

**Sibling fan-out case: `K.CC.2 → 1.OA.6`** (same-grade split — no ranking
needed).
- `K.CC.2` ← `K.NR.2.2` only (`state_superset`, grade K).
- `1.OA.6` ← **three** GA codes, all grade 1: `1.NR.2.1` (`merge`),
  `1.NR.2.2` (`split`), `1.NR.2.4` (`split`) — GA splits 1.OA.6's strategy
  content across three codes.

Both `1.OA.6`'s candidates are at grade 1, same as `1.OA.6` itself, so
grade-filtering keeps all three — they're genuine siblings, not competing
guesses. Cartesian product (1 × 3, no self-loops) → **three** output edges,
**all `needs_review: false`** (no fallback used, no endpoint carries its own
`partial`/`state_subset` flag — the fan-out itself doesn't trigger review):
```
K.NR.2.2 → 1.NR.2.1   (needs_review: false)
K.NR.2.2 → 1.NR.2.2   (needs_review: false)
K.NR.2.2 → 1.NR.2.4   (needs_review: false)
```
GA genuinely teaches this prerequisite relationship across all three of its
own strategy-clause codes, so keeping all three is correct, not a hedge.

**Grade-filtering case: `4.NF.1 → 4.NF.2`.**
- `4.NF.1` ← `4.NR.4.1` only (`exact`, grade 4).
- `4.NF.2` ← **two** candidates: `4.NR.4.3` (`exact`, grade 4) and
  `5.NR.3.2` (`partial`, grade 5 — GA's 5.NR.3.2 extends this to
  three-fraction comparison, a scope extension beyond 4.NF.2 itself).

`4.NF.2` is a grade-4 CCSS code, so grade-filtering keeps only `4.NR.4.3`
(grade 4) and sets `5.NR.3.2` aside as an `other_grade_ga_codes` annotation
rather than a translation target — even though its own relationship tag is
`partial`, not `different_grade`; the filter goes by actual grade, not by
label. Result: **one** output edge, `needs_review: false`:
```json
{"from": "4.NR.4.1", "to": "4.NR.4.3", "rule": "concept_foundation",
 "other_grade_ga_codes": {"to": ["5.NR.3.2"]},
 "needs_review": false}
```

### Still open after stage 2
The 14 GA codes with `relationship: none` in `mapping_final.json`
(`K.NR.1.4`, `K.PAR.6.1/6.2`, `K.MDR.7.3`, `1.PAR.3.1/3.2`, `1.MDR.6.3`,
`2.PAR.4.1/4.2`, `2.MDR.5.1`, `3.PAR.3.4`, `4.MDR.6.2`, `5.MDR.7.1/7.2` —
patterns, money, time) have no CCSS equivalent at all, so stage 2 can never
produce an edge touching them. Whatever internal sequencing they need stays
hand-authored (`provenance: ga_native`) in the stage 3 merge.

---

## MathFish / Achieve the Core comparison

Question: is the Achieve the Core "Coherence Map" (shipped as the
`allenai/achieve-the-core` HuggingFace dataset, the resource behind the
MathFish paper) a more comprehensive source of K-5 prerequisite structure
than the CCSS Progressions-PDF-grounded edges in `../math_prereq_grounding.json`?
Scope is K-5 only, per project scope.

Data source: https://huggingface.co/datasets/allenai/achieve-the-core
(`standards.jsonl`, `domain_groups.json`, downloaded into `data/` on 2026-09-23).
Not the "1000+ connections" figure quoted for the full dataset — that count is
K-8 + high school. K-5 is a subset.

### What each source actually is

**Achieve the Core (ATC) / MathFish**
- 737 total records across all levels (Grade/Domain/Cluster/Standard/Sub-standard),
  K-8 + HS. Restricting to K-5 Standard/Sub-standard records: **191 nodes**.
- Each node carries `connections: {progress to, progress from, related}` —
  edges are between whole CCSS standards (e.g. `K.OA.A.3`), essentially never
  between sub-standard letters (`K.OA.A.3a` vs `3b`) — those sub-parts exist
  as separate nodes but have **empty connection lists** in every case checked.
- K-5 → K-5 `progress to` edges: **246** (294 total if you count edges that
  spill into grade 6+). K-5 `related` edges (undirected, deduped): **55**.
- No sourcing per edge — each connection is just an id pair, with no citation
  to a page or passage explaining *why*. It's a curated map, not an annotated one.
- CCSS-native. Has no notion of Georgia's GSE codes (NR/PAR/MDR/GSR) — using
  it for this project requires a CCSS→Georgia remapping layer, and Georgia's
  domain consolidation is already documented as nontrivial (see
  `math_prereq_grounding.json` metadata.notes — e.g. Georgia's `PAR` domain
  doesn't correspond to any single CCSS domain).

**`math_prereq_grounding.json` (this project)**
- **148 edges**, authored directly against Georgia GSE sub-standard codes —
  no remapping layer needed, since the project's actual skill graph is built
  on GSE codes.
- Finer granularity: routinely encodes sequencing *within* a CCSS standard
  (e.g. `K.CC.4a → K.CC.4b → K.CC.4c`) that ATC does not represent at all.
- Every edge cites a specific Progressions document, page, and quoted passage,
  plus a rule from the 5-rule taxonomy (grade_progression, scope_expansion,
  concept_foundation, bloom_progression, decomposition) — defensible
  provenance for the thesis write-up, not just an asserted link.

### Direct comparison

Method (`compare.py`): resolve each grounding-file edge's `ccss_from`/`ccss_to`
citation to Achieve the Core standard ids (ignoring the CCSS cluster letter,
which the grounding file's citations omit), then check whether ATC records
that same pair as `progress to` or `related`.

| | count |
|---|---|
| Georgia grounding edges | 148 |
| ...with citations clean enough to resolve to ATC ids on both ends | 118 |
| ...of those, confirmed by an ATC `progress to` edge | 47 |
| ...of those, confirmed only by ATC `related` (non-directional) | 6 |
| ...of those, absent from ATC entirely | 65 |
| Citations that didn't resolve to a clean ATC id (patterns domain, GA-only, or non-standard-level) | 30 |

The 65 "absent from ATC" edges are not really disagreements — inspecting them,
the large majority (e.g. `K.NR.1.1→K.NR.1.2`, citing `K.CC.4a→K.CC.4b`) are
sub-standard-letter sequencing that ATC's coherence map simply doesn't encode
(confirmed by checking `K.CC.B.4a/4b/4c` directly: all three have empty
`connections` in `data/standards.jsonl`). This is the expected consequence of ATC
operating at coarser granularity, not evidence that the grounding-file edges
are wrong.

**Reverse check — does ATC know something the grounding file doesn't?**
Of ATC's 246 K-5 `progress to` edges, 235 touch at least one standard id that
already appears somewhere in the grounding file's citations (95.5% overlap in
node coverage). Only **11 ATC edges touch two standards neither of which the
grounding file references at all** — these are the genuine gaps, listed in
`comparison_output.json` under a query for edges where neither endpoint is in
the referenced-id set (see below for the list). Notable ones:
- `5.NF.A.2 → 5.MD.B.2`, `5.NF.B.6 → 5.MD.B.2`, `5.NF.B.7 → 5.MD.B.2`: fraction
  operations feeding into fraction-based line plots — a Data/Measurement
  connection the current grounding file doesn't have because `DATA_PROG` and
  `NF_PROG` were read as separate documents.
- `4.MD.C.5 → 4.MD.C.7`: angle measurement → additive angle measure, within
  the Geometric Measurement progression.
- `3.OA.B.6 → 5.NF.B.7`, `4.OA.A.2 → 5.NF.B.5/B.6`: division-as-unknown-factor
  and multiplicative comparison as long-range foundations for grade-5 fraction
  operations — a genuinely useful cross-grade-band edge the taxonomy's
  "grade_progression" rule would cover but that hasn't been drafted yet.

### Verdict

**Neither replaces the other; they're complementary, and the Progressions-PDF
approach should stay the primary method.** ATC is not more comprehensive for
this project's purposes — it has more raw edges only because it's not
Georgia-native and not sub-standard-granular, so its role here is as a
**cross-validation and gap-finding tool**, not a replacement:

1. It corroborates 53/118 (45%) of currently-resolvable grounding edges via
   an independent source (Achieve the Core, not the Progressions narrative),
   which is worth citing alongside the existing citations for those edges.
2. It surfaces 11 concrete candidate edges (above) not yet in the grounding
   file, mostly cross-domain (NF↔MD) connections worth drafting with a full
   Progressions citation before adding them.
3. It does **not** cover the sub-standard-letter sequencing that is a large
   fraction of the grounding file's value (65/118 resolvable edges), so it
   can't substitute for the Progressions-PDF read-through for that part of
   the graph.
4. It has no Georgia GSE codes and no per-edge sourcing, so it can't be cited
   directly in the thesis as the "why" — only the Progressions documents can.

### Files

- `data/standards.jsonl` — filtered to K-5 only (289 of the original 737
  records: Grade/Domain/Cluster/Standard/Sub-standard nodes whose id is grade
  K-5). This is what `compare.py` reads. Connection fields are left
  un-pruned, so a K-5 standard that progresses into grade 6+ still shows that
  target id even though the grade-6+ node itself isn't a record in this file.
- `data/domain_groups.json` — domain-taxonomy lookup, trimmed to the 6
  domain groups that actually occur in K-5 (CC, OA, NBT, MD, G, NF); the
  K-8/HS-only domain groups (Ratios & Proportional Relationships, Number
  Systems and Quantity, Statistics & Probability, Functions, Modeling) and
  the K-8/HS-only cats within kept groups (EE, A under Operations & Algebra)
  were removed.
- `data/README_hf.md` — the dataset's own HuggingFace README/citation.
- `compare.py` — matching + comparison script.
- `comparison_output.json` — full machine-readable output: matched edges (with
  which ATC edge confirmed them), unmatched edges, and unresolvable citations.

The original, unfiltered download (737 records, K-8 + HS) was not kept in
this repo since only K-5 is in scope; re-fetch it from
https://huggingface.co/datasets/allenai/achieve-the-core if the full dataset
is needed again.

### Note on the "1000+ connections" figure

That count describes the **full K-8 + HS dataset**, not the K-5 slice this
project cares about. Across all 737 raw records (656 with a populated
`connections` field), summing `progress to` + `progress from` + `related` as
raw list entries gives 1,623; deduping direction-mirrored progress pairs and
undirected related pairs gives 812 unique connections. Restricted to K-5
(289 of 737 records), that shrinks to 246 progress-to edges + 55 related
edges, per the table above — K-5 standards branch less and have fewer
cross-domain links than middle/high school algebra, so the K-5 slice is
smaller than 289/737 (~39%) of the total nodes would suggest.
