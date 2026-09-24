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
| i-Ready | At-home practice packets, student + teacher versions ([source page](https://www.curriculumassociates.com/summer-learning-support/at-home-resources-mathematics)) | 129 worksheets, 1,176 problems |
| MathFish | Research dataset (IM + Fishtank curricula), K-5 subset | 4,428 problems |

**How questions are categorized:** four separate dimensions, not just one.

| Dimension | Values | Where it comes from |
|---|---|---|
| Response format | multiple choice, multi-select, numeric, match/sort, draw/plot, written explanation, open activity | GaDOE's labels (Milestones); hand-coded (i-Ready); text rules checked against GaDOE's labels (MathFish, 92% agreement) |
| Context | word problem, visual model, symbolic | text rules (rough) |
| Picture (multimodal) | text only, table, code-drawable diagram, illustration, interactive tool | hand-coded from page images (Milestones, i-Ready) |
| Difficulty (DOK 1-3) | printed by GaDOE | Milestones only |

**Main findings:**

- **The tests are mostly multiple choice.** Milestones: 70% multiple choice, 5% multi-select,
  25% written. i-Ready samples: 7 of 10 multiple choice.
- **MathFish is under 1% multiple choice.** It's lesson material (42% explain, 29% open
  activities), so it's a content pool, not a model of test formats.
- **Format tracks difficulty.** Every DOK-1 item is multiple choice; 71% of DOK-3 items are
  written.
- **Almost every test picture can be drawn by code:** 98% of Milestones items are text,
  tables or simple diagrams (number lines, fraction models, shapes, grids). Only 3 of 123
  need a real illustration.
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
- **Review tool:** `processed/question_types/review/index.html` shows every item with its
  labels, pictures and answers, and lets you correct labels and export them.

**Limits to mention:**

- The Milestones samples predate the 2023 standards. Current items are only in the
  interactive practice tests (gaexperienceonline.com) and GaDOE's browser-only portal.
- No Milestones below grade 3; K-2 evidence is only 4 i-Ready samples.
- i-Ready samples show which formats exist, not how often each is used.
- i-Ready standards were assigned by me (i-Ready prints none).

**To discuss:**

- **Target formats for the generator.** Proposal: 4-option multiple choice with error-based
  distractors (modeled on GaDOE's rationales), multi-select, two-part (Part A/B), numeric
  entry, written explanation with a rubric, and number-line plotting for i-Ready. Agree?
- **Next step from Sep 15 (type per standard):** start from the observed type-per-standard
  counts (`tables/standard_by_type.csv`), then have an LLM generate each type per standard,
  solve it, and discard infeasible ones. Pick one grade first (grade 4, as suggested
  earlier)?
- **Current Milestones items:** is hand-transcribing the online practice tests worth it, or
  can we get portal / GOFAR access through a district?
- **More i-Ready items:** is there a legitimate route to more Diagnostic items (e.g. a
  teacher account)?
- **Pictures:** build a code-based diagram library (geometry figures, fraction models,
  number lines, grids, line plots first)?

