# Progression mapping

Rebuilding `../math_prereq_grounding.json` on a cleaner, two-stage
foundation, plus the MathFish/Achieve the Core comparison that motivated it.

## At a glance

| item | status | number |
|---|---|---|
| MathFish/ATC comparison | done | verdict: complementary, not a replacement (see below) |
| Stage 1 — `ccss_progressions.json` | done | 147 CCSS-native edges |
| Stage 2 — `translate_progressions_to_ga.py` | **planned, not written** | ~89-150 GA edges expected |
| Stage 3 — diff + merge into new grounding file | not started | — |

- `math_prereq_grounding_outdated.json` here = **read-only copy** of
  `../math_prereq_grounding.json`, kept as the fixed baseline stage 3 diffs
  against.
- The live file stays at `../math_prereq_grounding.json` — `proposal.typ`,
  `processed/preprocess.typ`, and `processed/README.md` all reference that
  path. This rebuild doesn't touch it until the final merge (Plan step 4).
- `processed/preprocess.typ` already independently flags that file as a
  "standing issue" needing review, for the same reasons this rebuild exists.

## Why a rewrite

The old file's 148 edges were authored by reading the CCSS Progressions PDF
and hand-translating into Georgia GSE codes **at the same time** — that's why
some citations are messy free text instead of clean codes:
- `"1.OA.1 / 1.OA.6 (strategies)"`
- `"K.OA.1-3"`

The translation was done live, in-head, while reading. Now that
`mapping_final.json` exists (a reviewed, adopted GA↔CCSS mapping for all 150
Georgia K-5 sub-standards), the two jobs split apart:

| stage | what it does | judgment involved? |
|---|---|---|
| 1. CCSS-native progressions | Read the Progressions PDF, write edges purely in CCSS-code space | Yes — this is the real content extraction |
| 2. Mechanical translation | Run every stage-1 edge through `mapping_final.json`'s reverse index | No — pure lookup, judgment already happened when the mapping was adopted |

Stage 1 also fixes the "stale OA_PROG pagination" bug flagged in the old
file's metadata, since edges are cited fresh against the PDF's real page
numbers.

## The relationship-type complication

`mapping_final.json` is indexed **by GA code**: each of the 150 GA K-5 leaf
standards has one entry naming which CCSS code(s) it corresponds to (0, 1, or
several). The `relationship` field describes that GA code's own match:

| relationship | count | reverse-lookup behavior |
|---|---|---|
| exact | 56 | clean 1:1 |
| state_superset | 12 | clean 1:1 |
| state_subset | 7 | clean 1:1 |
| merge | 32 | one GA code covers multiple CCSS codes → several CCSS edges collapse onto one GA code |
| split | 18 | several GA codes jointly cover one CCSS code → one CCSS edge fans out into several GA edges |
| different_grade | 7 | GA code sits at a different grade than the CCSS code it maps to |
| partial | 4 | weak match — keep, flag lower confidence |
| **none** | **14** | **this GA code has no CCSS equivalent at all** — patterns/PAR domain, money, time (listed below) |
| **total** | **150** | |

**`none` answers "which GA standards have no CCSS match" — not the reverse
question.** It's easy to misread the row above as being about CCSS codes
lacking a GA match; it isn't. The reverse question is a separate count,
computed directly against the full CCSS K-5 leaf-code list (191 codes, from
`../state_ccss_mapping/ccss_standards/`):

| direction | count |
|---|---|
| GA standards with no CCSS match (`relationship: none`, above) | **14** |
| CCSS K-5 codes that no GA standard cites at all | **39** |
| ...of those 39, resolvable by the parent/child fallback (the bare parent isn't cited, but at least one of its lettered children is — e.g. `1.NBT.2` uncited but `1.NBT.2a/b/c` are) | 15 |
| ...of those 39, genuinely uncited at any granularity — real gaps | **24** |

The 24 real CCSS-side gaps: `1.OA.5`, `2.G.2`, `2.MD.2`, `2.MD.5`, `2.NBT.9`,
`3.G.2`, `3.MD.5a`, `3.NF.3a`, `3.OA.1`, `3.OA.2`, `4.MD.7`, `4.NF.3a`,
`4.NF.4b`, `4.NF.4c`, `5.MD.2`, `5.MD.3`, `5.MD.3a`, `5.MD.3b`, `5.MD.5c`,
`5.NF.4b`, `K.CC.4a`, `K.CC.7`, `K.G.2`, `K.G.3` — no GA standard in
`mapping_final.json` was classified against any of them, at any granularity.
This is expected: `mapping_final.json` was built by iterating over the 150
GA codes and finding each one's best CCSS match, not the other way around,
so a CCSS code simply doesn't appear if no GA standard happened to need it as
its closest match. These overlap heavily with the 15 "genuine gaps" already
flagged in the granularity-mismatch section below (that list was scoped to
just the 133 CCSS codes touched by the 147 stage-1 edges; this one is the
full 191-code universe).

Separately: the **14 GA-side `none` codes** have no CCSS home at all — no
CCSS edge can ever translate into them; they stay hand-authored
(`provenance: ga_native`) in the stage 3 merge (full list in "Still open
after stage 2" below).

## Plan

1. ✅ Read `ccss_progressions_all.pdf`, produce `ccss_progressions.json` —
   CCSS-only edges, fresh page citations.
2. ⬜ Write `translate_progressions_to_ga.py` — reverse-index lookup + the
   algorithm below.
3. ⬜ Diff against the 148 hand-authored edges — what survives, what gets a
   cleaner citation, what's new, what (patterns/money/time) must stay
   hand-authored.
4. ⬜ Merge: `provenance: ccss_translated` + `provenance: ga_native` edges →
   replace `../math_prereq_grounding.json` (version bump from 0.12).
5. ⬜ Re-run `validate_skills.py` / resume `skills_math_*.json` authoring.

---

## Stage 1 results — `ccss_progressions.json`

| metric | value |
|---|---|
| total edges | **147** |
| source | `ccss_progressions_all.pdf`, pages 16–161 (every K-5 sub-document; page 162+ moves into Grade 6 Ratios & Proportional Relationships, out of scope) |
| invalid codes / duplicate pairs | 0 / 0 (validated against `../state_ccss_mapping/ccss_standards/`) |

**By rule:**

| rule | count |
|---|---|
| concept_foundation | 58 |
| grade_progression | 57 |
| decomposition | 16 |
| bloom_progression | 13 |
| scope_expansion | 3 |

**By domain** (of the `from` code):

| domain | count |
|---|---|
| NF | 42 |
| MD | 36 |
| OA | 21 |
| NBT | 18 |
| G | 17 |
| CC | 13 |

**Notes:**
- Sub-standard-letter sequencing included throughout (e.g. `K.CC.4a→4b→4c`,
  `5.NF.5a→5b`) — the granularity ATC/MathFish lacks (see comparison below).
- 17 edges come directly from the Measurement & Data Progression's own
  "Notable connections" table.
- One edge (`5.NF.4→5.NF.5a`) is marked `continues_beyond_k5: true` (source
  text frames it as Grade-6 prep).
- Extraction favored precision over exhaustiveness: only edges with an
  explicit, quotable code-to-code claim were kept. This is not a claim of
  *every* possible prerequisite relationship in the text — just what it
  explicitly supports.
- Page/quote citations spot-checked directly against the PDF.

---

## Stage 2 plan — `translate_progressions_to_ga.py`

### The reverse index isn't clean by relationship type

A single CCSS code can map back to GA codes carrying **different**
relationship types at once — it's a property of each (CCSS, GA) pair, not of
the CCSS code as a whole:

```
4.G.3   -> [(2.GSR.7.2, different_grade), (3.GSR.6.3, different_grade),
            (4.GSR.8.1, merge),           (4.GSR.8.2, merge)]
4.NBT.2 -> [(3.NR.1.1, different_grade),  (3.NR.1.2, different_grade),
            (4.NR.1.1, split),            (4.NR.1.3, split)]
```
(GA revisits pieces of this content at earlier grades in addition to the
grade-4 treatment CCSS states once.)

### Fan-out resolves mechanically — checked all 21 fan-out CCSS codes

| pattern | count | resolution |
|---|---|---|
| same-grade only, all `split`/`merge` | 14 | pure siblings — keep all, no ranking |
| same-grade only, mixed high-confidence types | 1 | same — both types already high-confidence individually |
| mixed same-grade + `different_grade` | 6 | keep same-grade candidate(s); set `different_grade` ones aside as an annotation |
| all candidates cross-grade | 0 | (would fall back to cross-grade set + `needs_review: true`; never occurred) |

- **Rule must be grade-match, not tag-match.** `4.NF.2`'s off-grade candidate
  is tagged `partial`, not `different_grade` — a tag-based filter would miss
  it; a grade-based filter catches it.
- **Net effect: fan-out is never itself a reason for `needs_review`.**
  Same-grade multiplicity = legitimate sibling decomposition, kept in full.

### Granularity mismatch between the two files

`mapping_final.json` cites whatever GA needed (often a lettered
sub-standard, e.g. `5.NF.5a`); stage 1 sometimes uses the bare parent
(`5.NF.4`) when the Progressions text discusses the standard before its
lettered parts.

| | count |
|---|---|
| distinct CCSS codes touched by the 147 edges | 133 |
| ...not found directly in the reverse index | 26 |
| ...recovered via children-union fallback (parent → union of its lettered children's GA codes) | 11 |
| ...genuine gaps (no GA code cites them at all) | 15 |

Genuine-gap codes: `K.CC.4a`, `K.CC.7`, `3.OA.1`, `3.G.2`, `2.G.2`, `2.MD.2`,
`2.MD.5`, `5.MD.2`, `5.MD.3`, `4.MD.7`, `3.NF.3a`, `4.NF.3a`, `4.NF.4b`,
`4.NF.4c`, `5.MD.5c` — logged for human review, not silently dropped.

(Tested a parent-fallback in the other direction too — child code looks up
its bare parent — but it recovered 0 cases in this data, so it's not worth
the extra code path.)

### Net translation yield

| | count |
|---|---|
| both endpoints resolve to ≥1 GA code | 115 |
| only one endpoint resolves (untranslatable) | 30 |
| neither endpoint resolves | 2 |
| **raw GA edges after grade-filtering** (before dedup) | **150** |
| ...`needs_review: false` | **89** |
| ...`needs_review: true` | **61** |

`needs_review: true` breakdown (61 total):

| reason | count |
|---|---|
| resolved only via children-union fallback | 44 |
| endpoint inherits `partial`/`state_subset` from `mapping_final.json` | 23 |

(Grade-filtering already dropped the naive Cartesian-product count from 161
→ 150 — and fan-out itself no longer inflates the review count.)

### Algorithm

1. Build the CCSS→GA reverse index from `mapping_final.json`: code → list of
   `(ga_code, relationship, needs_review, note)`.
2. `resolve(ccss_code)`:
   - direct hit in the index → those candidates
   - else, union of any `{code}[a-z]` lettered children present in the index
   - else unresolved
3. **Grade-filter**: keep only candidates whose grade matches `ccss_code`'s
   grade. If empty, fall back to the full cross-grade set and mark
   `needs_review: true` (never triggered in this data). Filtered-out
   candidates aren't discarded — recorded as `other_grade_ga_codes`.
4. For each of the 147 stage-1 edges, resolve + grade-filter both sides:
   - either side unresolved → log to `translation_gaps.json`, emit nothing
   - both resolve → Cartesian product (grade-filtered), drop self-loops,
     emit one edge per remaining pair — same-grade multiplicity kept in full
5. Each output edge carries both citations: the stage-1 CCSS page/quote, and
   the `mapping_final.json` note(s) for both endpoints.
6. `needs_review: true` iff either endpoint (a) used the children-union
   fallback, (b) itself carries `needs_review: true` in `mapping_final.json`,
   or (c) fell back to the cross-grade set. Fan-out alone never triggers it.
7. Dedupe: edges collapsing to the same `(ga_from, ga_to)` pair merge, union
   their citations (corroboration, not noise).
8. Output `ga_progressions_translated.json` + `translation_gaps.json` (the
   32 untranslatable edges, for a human call on whether they need a
   hand-authored GA-native edge instead).

### Worked examples

**1. Simple case — `K.CC.5 → K.MD.3` (no fan-out)**

| side | GA code | relationship |
|---|---|---|
| from: K.CC.5 | K.NR.1.1 | exact |
| to: K.MD.3 | K.MDR.7.2 | exact ("classify/sort into categories, count, sort by count, matches verbatim") |

→ one output edge, `needs_review: false`:
```json
{"from": "K.NR.1.1", "to": "K.MDR.7.2", "rule": "concept_foundation",
 "provenance": "ccss_translated",
 "ccss_from": "K.CC.5", "ccss_to": "K.MD.3",
 "ccss_citation": {"page": 80, "source": "Notable connections table..."},
 "needs_review": false}
```

**2. Sibling fan-out — `K.CC.2 → 1.OA.6`** (same-grade split, no ranking needed)

| side | GA code(s) | relationship | grade |
|---|---|---|---|
| from: K.CC.2 | K.NR.2.2 | state_superset | K |
| to: 1.OA.6 | 1.NR.2.1 | merge | 1 |
| to: 1.OA.6 | 1.NR.2.2 | split | 1 |
| to: 1.OA.6 | 1.NR.2.4 | split | 1 |

All three `to`-side candidates are grade 1 (same as `1.OA.6`) → all kept as
genuine siblings, not competing guesses → **3 output edges, all
`needs_review: false`**:
```
K.NR.2.2 → 1.NR.2.1
K.NR.2.2 → 1.NR.2.2
K.NR.2.2 → 1.NR.2.4
```
GA genuinely teaches this prerequisite across all three of its own
strategy-clause codes — keeping all three is correct, not a hedge.

**3. Grade-filtering — `4.NF.1 → 4.NF.2`**

| side | GA code | relationship | grade |
|---|---|---|---|
| from: 4.NF.1 | 4.NR.4.1 | exact | 4 |
| to: 4.NF.2 | 4.NR.4.3 | exact | 4 |
| to: 4.NF.2 | 5.NR.3.2 | partial | 5 |

`4.NF.2` is a grade-4 code, so grade-filtering keeps only `4.NR.4.3` and sets
`5.NR.3.2` aside as an annotation — **even though its tag is `partial`, not
`different_grade`**; the filter goes by actual grade, not label.
→ **1 output edge**, `needs_review: false`:
```json
{"from": "4.NR.4.1", "to": "4.NR.4.3", "rule": "concept_foundation",
 "other_grade_ga_codes": {"to": ["5.NR.3.2"]},
 "needs_review": false}
```

### Still open after stage 2

14 GA codes have `relationship: none` — no CCSS equivalent, so stage 2 can
never produce an edge touching them. Sequencing among them stays
hand-authored (`provenance: ga_native`):

| domain | codes |
|---|---|
| Money/measurement | `K.NR.1.4`, `K.MDR.7.3`, `1.MDR.6.3`, `2.MDR.5.1`, `4.MDR.6.2`, `5.MDR.7.1`, `5.MDR.7.2` |
| Patterns (PAR) | `K.PAR.6.1`, `K.PAR.6.2`, `1.PAR.3.1`, `1.PAR.3.2`, `2.PAR.4.1`, `2.PAR.4.2`, `3.PAR.3.4` |

---

## MathFish / Achieve the Core comparison

**Question:** is Achieve the Core's "Coherence Map" (the `allenai/achieve-the-core`
HuggingFace dataset behind the MathFish paper) a more comprehensive source of
K-5 prerequisite structure than the CCSS Progressions-grounded edges in
`../math_prereq_grounding.json`? Scope: K-5 only.

Data: https://huggingface.co/datasets/allenai/achieve-the-core, downloaded
2026-09-23. Note: the dataset's own "1000+ connections" figure is for the
**full K-8 + HS set**, not K-5 (see bottom of this section).

### What each source is

| | Achieve the Core (ATC/MathFish) | `math_prereq_grounding.json` (this project) |
|---|---|---|
| K-5 nodes | 191 | — (Georgia-code based) |
| K-5 edges | 246 progress-to + 55 related | 148 |
| Code space | CCSS-native (no Georgia GSE codes) | Georgia GSE codes directly — no remapping layer needed |
| Granularity | whole standards only — sub-standard letters (e.g. `K.OA.A.3a` vs `3b`) have **empty** connection lists | routinely encodes within-standard sequencing (`K.CC.4a→4b→4c`) |
| Per-edge sourcing | none — just an id pair | every edge cites a Progressions doc, page, quote, and taxonomy rule |

### Direct comparison

Method: resolve each grounding-file edge's CCSS citation to an ATC id, check
whether ATC records that pair as `progress to` or `related`.

| | count |
|---|---|
| Georgia grounding edges | 148 |
| ...citations clean enough to resolve to ATC ids on both ends | 118 |
| ...of those, confirmed by an ATC `progress to` edge | 47 |
| ...of those, confirmed only by ATC `related` (non-directional) | 6 |
| ...of those, absent from ATC entirely | 65 |
| Citations too messy to resolve to a clean ATC id | 30 |

- The 65 "absent from ATC" edges aren't disagreements — most (e.g.
  `K.NR.1.1→K.NR.1.2`, citing `K.CC.4a→K.CC.4b`) are sub-standard-letter
  sequencing ATC simply doesn't encode (confirmed: `K.CC.B.4a/4b/4c` all
  have empty `connections` in the raw data).

**Reverse check — does ATC know something the grounding file doesn't?**

| | count |
|---|---|
| ATC K-5 progress-to edges | 246 |
| ...touching ≥1 id already in the grounding file's citations | 235 (95.5%) |
| ...touching **no** id the grounding file references at all (genuine gaps) | 11 |

Notable gap edges:
- `5.NF.A.2 → 5.MD.B.2`, `5.NF.B.6 → 5.MD.B.2`, `5.NF.B.7 → 5.MD.B.2` —
  fraction operations feeding fraction-based line plots (missed because
  `DATA_PROG` and `NF_PROG` were read as separate documents).
- `4.MD.C.5 → 4.MD.C.7` — angle measurement → additive angle measure.
- `3.OA.B.6 → 5.NF.B.7`, `4.OA.A.2 → 5.NF.B.5/B.6` — long-range
  cross-grade-band foundations for grade-5 fraction operations.

### Verdict

**Complementary, not a replacement — Progressions-PDF stays the primary
method.**

- ATC corroborates 53/118 (45%) of resolvable grounding edges independently
  — worth citing alongside existing citations.
- ATC surfaces 11 concrete candidate edges not yet in the grounding file
  (mostly NF↔MD), worth drafting with a proper Progressions citation.
- ATC does **not** cover sub-standard-letter sequencing (65/118 resolvable
  edges) — can't substitute for the PDF read-through there.
- ATC has no Georgia codes and no per-edge sourcing — can't be cited
  directly in the thesis as the "why."

### Files

| file | contents |
|---|---|
| `data/standards.jsonl` | filtered to K-5 (289 of 737 records) |
| `data/domain_groups.json` | trimmed to the 6 domain groups occurring in K-5 |
| `data/README_hf.md` | dataset's own HF README/citation |
| `compare.py` | matching + comparison script |
| `comparison_output.json` | matched / unmatched / unresolvable edges, full detail |

The original unfiltered download (737 records, K-8+HS) wasn't kept — re-fetch
from the HF link above if needed again.

### The "1000+ connections" figure, explained

| scope | metric | value |
|---|---|---|
| Full K-8+HS (737 records, 656 with connections) | raw `progress to`+`progress from`+`related` list entries | 1,623 |
| Full K-8+HS | deduped unique connections | 812 |
| K-5 only (289 of 737 records) | progress-to edges | 246 |
| K-5 only | related edges | 55 |

K-5 standards branch less and have fewer cross-domain links than middle/high
school algebra, so the K-5 slice is smaller than its 289/737 (~39%) share of
total nodes would suggest.
