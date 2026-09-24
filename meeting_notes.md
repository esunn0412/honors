# Meeting prep: progress since Sep 15

Prepared Sep 24. Covers the three work streams from the last two meetings: state–CCSS
mapping, progression mapping, and question types.

## Status against the last to-dos

| To-do (meeting) | Status |
|---|---|
| Mapping stats: how much mapped, what's unmapped, how inferred, numbers with zero ambiguity (Sep 1) | **Done.** See §1 |
| Can the progression be implied from the mapping? Skill mapping first, then progression (Sep 1) | **Partly.** Stage 1 (CCSS progressions) done; stage 2 (translate to GA) designed, not coded. See §2 |
| Evaluate whether the progression mapping is correct (Sep 1) | **Partly.** Cross-checked against Achieve the Core; no evaluation against student data yet |
| Run the EDUMath-style mapping for Virginia and compare (Sep 15) | **Done** on the 21 VA codes EDUMath cites: 19/21 agree. See §1 |
| Error analysis of frequent LLM mapping errors (Sep 15) | **Done.** 5-category error taxonomy. See §1 |
| Conclude the mapping with full verification (Sep 15) | **Done** for GA: every non-trivial code reviewed by hand; `verify_mapping.py` reports clean |
| Question-type list per grade from i-Ready and Milestones; categorize; multimodal categories (Sep 15) | **Done.** See §3 |
| Find legitimate free sample tests (Sep 15) | **Done**, with limits. See §3 |
| Map which question type fits each standard (LLM generate → solve → discard) (Sep 15) | **Not started.** Observed type-per-standard counts exist as a starting point |

---

## 1. State ↔ CCSS mapping (`processed/state_ccss_mapping/`)

**What it is:** a reusable pipeline that classifies any state's K-5 math standards against
CCSS with a fixed 8-type relationship taxonomy (exact, merge, split, different_grade,
state_superset, state_subset, partial, none), plus automatic checks (`verify_mapping.py`).

**Georgia result** (`states/ga/mapping_final.json`, 150 GA sub-standards):

| Question from Sep 1 | Answer |
|---|---|
| How was the mapping inferred? | Flat LLM classification of each GA code against all ~175 CCSS K-5 codes, then automatic checks, then my review of every non-trivial code |
| How much needed correcting? | 14 of 150 corrected over two review passes (136 unchanged, 90.7%) |
| GA standards with no CCSS match | **14 (9.3%)**: 7 patterns (PAR), 3 open-ended data inquiry, 2 money, 2 measurement construction |
| CCSS codes no GA standard cites | **18 of 175 (10.3%)**: 13 whole standards, 5 single lettered clauses |
| Relationship mix | exact 56, merge 32, split 18, none 14, superset 12, different_grade 7, subset 7, partial 4 |

**Verification and error analysis:**

- **Automatic checks** catch structural bugs: an invalid split sibling, a mislabeled
  superset/subset, and a "borrowed thematic label" (a weak match citing a code another
  standard already owns). They found 4 of the 14 errors that side-by-side review missed.
- **Error taxonomy:** 5 exclusive categories (invalid split, split-status disagreement,
  scope/label judgment, code-set boundary mismatch, genuine content miss). The GA
  corrections break down as 3 invalid splits, 3 boundary mismatches, 3 borrowed labels,
  1 split-status and 1 scope/label.
- **Alternative method tested and rejected:** a hierarchical search (domain → cluster →
  code) agreed with the adopted mapping only 74% of the time. It mostly disagreed on code-set
  boundaries and labels, not on picking the right area, so the flat method stays.

**Virginia / EDUMath comparison:** classified the 21 VA codes EDUMath's crosswalk cites;
**19/21 agree**. Both disagreements are granularity differences, not errors: EDUMath maps one
bullet of a VA standard, while we map the whole standard.

**To discuss:**

- There is no independent gold mapping for GA; I'm the only reviewer. Is that acceptable
  for the thesis, or should a second person review a sample?
- The 14 GA-only standards (mostly patterns and money) have no CCSS Progressions to ground
  prerequisites on. The plan is to author those edges by hand from GA's own documents
  (`provenance: ga_native`), or by hierarchical connection. OK?
- Still open: run `map_state_to_ccss.py` with an API key for reproducibility; currently the
  classification was done with claude, so not reproducible.

---

## 2. Progression mapping (`processed/progression_mapping/`)

**Why:** the old prerequisite file (148 edges) translated CCSS Progressions into GA codes by
hand *while* reading, which left messy citations. With an adopted mapping, this splits into
two clean stages.

| Stage | Status | Result |
|---|---|---|
| 1. Read the CCSS Progressions PDF, write edges in CCSS codes only | **Done** | **147 edges**, each with page + quote; 0 invalid codes; includes sub-standard sequencing (e.g. K.CC.4a → 4b → 4c) |
| 2. Translate edges to GA codes mechanically through the mapping | **Designed, not coded** | Dry run: ~150 GA edges, 89 clean, 61 needing review; 32 edges can't translate |
| 3. Diff against the old 148 edges and merge | Not started | — |

**Other evidence gathered:**

- **Achieve the Core coherence map** (from MathFish)
- **Georgia's own "Learning Progressions" table** : 5 table cells describe content no standard
  contains.

**To discuss:**

- How should the progression be evaluated for correctness? Options: agreement with Achieve
  the Core and with GA's own table (available now), or self-review again.
---

## 3. Question types (`processed/question_types/`)

**Sources used (all free, public):**

| Source | What | Items |
|---|---|---|
| Georgia Milestones | GaDOE study guides + assessment guides, grades 3-5 (2016-2017 editions, from Fair Oaks ES and other district sites) | 123 unique items, labeled by GaDOE with type, DOK and standard |
| i-Ready | Diagnostic sample items (Curriculum Associates) | 10 K-5 items (screenshots) |
| i-Ready | At-home practice packets, student + teacher versions ([source page](https://www.curriculumassociates.com/summer-learning-support/at-home-resources-mathematics)) | 129 worksheets: 1,176 numbered problems + 37 pages without numbers = 1,213 questions |
| MathFish | Research dataset (IM + Fishtank curricula), K-5 subset | 4,428 problems |

**How questions are categorized:** three separate dimensions (full rules in
`processed/question_types/CODEBOOK.md`).

| Dimension | Values |
|---|---|
| Answer mode | select one, select many, enter (number/expression), write (explanation), construct (plot/shade/draw), match/order/sort, drop-down |
| Structure | single, or multi-part (Part A/B, a./b., and item sets on one shared situation). Each part keeps its own answer mode, e.g. *enter → write* |
| Stimulus | none, table, diagram, illustration, interactive tool. A table holding pictures counts as a picture |

- **Not used:** DOK (only Milestones prints it; kept as GaDOE metadata) and context (word
  problem vs. bare numbers).
- **Outside the scheme:** MathFish games, centers and teacher-led routines, marked "open".
- **Unit:** one question. i-Ready worksheets are now counted per problem (1,213).
- **Labels:** a rule-based first pass, validated by hand in the review page. The only
  automatic check is Milestones, where the labels agree with GaDOE's printed item type on
  all 123 items.

**Main findings (first-pass labels):**

- **The tests are mostly "select one".** Milestones: 67% select one, 2% select many, 9% write,
  21% multi-part (usually *enter → write* or two *select one* parts). i-Ready samples: 7 of 10
  select one.
- **MathFish rarely asks students to select:** only 6% of problems have a select part. It's
  lesson material (37% multi-part chains, 27% open activities, 15% write, 14% enter), so it's
  a content pool, not a model of test formats.
- **i-Ready practice worksheets are drills:** 91% of problems are *enter*.
- **Almost every test picture is a diagram code could draw:** Milestones is 56% none, 6%
  table, 36% diagram (number lines, fraction models, shapes, grids). Only 3 of 123 need a
  real illustration.
- **i-Ready's distinctive feature is interaction:** 8 of 10 samples are answered with an
  on-screen tool (ruler, protractor, counters, click-to-plot).

**Extraction and answers:**

- **Questions extracted as text with separate figures.** Milestones figures are vector
  drawings, so they were read with PyMuPDF; 131 of 132 items extract cleanly.
- **Answers:**
  - Milestones: all 132, with GaDOE's explanation of every wrong choice.
  - i-Ready worksheets: 1,098 of 1,176, from the teacher packets.
  - i-Ready samples: 8 of 10, worked out by me.
  - MathFish: none; the publishers' solutions are behind a teacher login.
- **Review tool:** `processed/question_types/review/index.html` shows every question with its
  labels, pictures and answers. It is also where labels are validated: correct the question
  type, part modes and stimulus, mark a card checked, and export as CSV.

**Limits to mention:**

- The Milestones samples predate the 2023 standards. Current items are only in the
  interactive practice tests (gaexperienceonline.com) and GaDOE's browser-only portal.
- No Milestones below grade 3; K-2 evidence is only 4 i-Ready samples.
- i-Ready samples show which formats exist, not how often each is used.
- i-Ready standards were assigned by me (i-Ready prints none).

**To discuss:**

- **Is the categorization right?** Three dimensions (answer mode, structure, stimulus), with
  item sets counted as multi-part and DOK/context left out. Agree?
- **Validation plan:** who checks the labels in the review page, and on how big a sample per
  source?
