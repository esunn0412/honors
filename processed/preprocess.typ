#set page(
  paper: "a4",
  margin: (x: 22mm, y: 20mm),
)

#set text(
  font: "Libertinus Serif",
  size: 10.5pt,
  lang: "en",
)

#set heading(numbering: "1.")
#set par(justify: true, leading: 0.72em)
#set list(indent: 1.2em, body-indent: 0.55em)
#set enum(indent: 1.2em, body-indent: 0.55em)

#show heading.where(level: 1): it => block(
  above: 1.4em,
  below: 0.6em,
  text(size: 16pt, weight: "bold", it.body),
)

#show heading.where(level: 2): it => block(
  above: 1.1em,
  below: 0.4em,
  text(size: 12.5pt, weight: "semibold", it.body),
)

#let keybox(title, body) = block(
  inset: 10pt,
  radius: 4pt,
  stroke: 0.6pt + luma(170),
  fill: luma(246),
  width: 100%,
  [
    *#title* \
    #body
  ],
)

#align(center)[
  #text(size: 18pt, weight: "bold")[Preprocessing math standards data (K--5)]
]

#v(0.3em)
#align(center)[Reference notes on turning the CCSS and Georgia standards documents into structured JSON, mapping GA sub-standards to their CCSS equivalents, and mapping Georgia's own K-5 Learning Progressions table to GA sub-standard codes.]
#v(1em)

This file documents the preprocessing pipeline, not the thesis argument -- see `../proposal.typ` for that. Two independent sources are processed: the official CCSS Math Standards PDF and Georgia's own K-12 Mathematics Standards PDF. Both are turned into structured, verbatim-checked JSON (sections 1-2), then cross-referenced against each other (skill mapping, section 3) and against Georgia's own progression table (section 4).

= CCSS standards #sym.arrow.r JSON

`dat/ccss-math-standards.pdf` (corestandards.org, 93 pages) is transcribed page-by-page into `processed/standards/ccss_math_0.json` (K) through `ccss_math_5.json`, one file per grade.

CCSS's structure is *domain #sym.arrow.r cluster #sym.arrow.r standard #sym.arrow.r (optional) lettered sub-standard* -- one level deeper than Georgia's *domain #sym.arrow.r standard #sym.arrow.r sub_standard*. Clusters are unlabeled heading text in the source; standards are numbered and coded (`K.CC.1`); some break into lettered parts (`K.CC.4a/b/c`), the finest-grained citable unit when present.

*Footnotes* (scope-limiting or clarifying text attached to a standard/cluster/domain, e.g. "limited to fractions with denominators 2, 3, 4, 6, and 8") are concatenated into the relevant node's `description` field in parentheses, at the exact level the source attaches them to.

*Glossary references*: six standards cite "see Glossary, Table 1/2" instead of restating content inline -- these tables are full word-problem taxonomies, too long for a description string. The pointer text is stripped from the citing standard's `description`, and a `glossary_ref` key is added naming a block in `processed/standards/ccss_glossary.json`, which reproduces each table as structured natural-language categories (e.g. "Add to" / "Result Unknown" / "Change Unknown") with the source's own worked examples kept verbatim. `glossary_ref` resolves against a block's own `id` field, not the JSON key it sits under, so it survives restructuring.

#table(
  columns: (auto, auto),
  align: (left, left),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*Glossary slug*], [*Referenced by*],
  [`addition_subtraction_situations`], [`1.OA.1`, `2.OA.1`, `2.MD.10`],
  [`multiplication_division_situations`], [`3.OA.3`, `3.MD.2`, `4.OA.2`],
)

== CCSS coverage, K--5

#table(
  columns: (auto, auto, auto, auto),
  align: (left, center, center, left),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*Grade*], [*Top-level standards*], [*Leaf units#footnote[Lettered sub-parts (e.g. `K.CC.4a/b/c`) counted separately; a standard with no lettered parts counts as 1 either way.]*], [*Domains*],
  [K (0)], [22], [24], [`CC`, `OA`, `NBT`, `MD`, `G`],
  [1], [21], [23], [`OA`, `NBT`, `MD`, `G`],
  [2], [26], [27], [`OA`, `NBT`, `MD`, `G`],
  [3], [25], [33], [`OA`, `NBT`, `NF`, `MD`, `G`],
  [4], [28], [34], [`OA`, `NBT`, `NF`, `MD`, `G`],
  [5], [26], [34], [`OA`, `NBT`, `NF`, `MD`, `G`],
  [*Total*], [*148*], [*175*], [],
)

= Georgia standards #sym.arrow.r JSON

Two separate JSON layers, from two different sources:

+ `georgia_math_{grade}.json` -- bare code + one-line description, parsed from `dat/georgia-math-stardards.txt`, cross-checked against the live CASE API (`case.georgiastandards.org`).
+ `georgia_math_guidance_{grade}.json` -- the "Evidence of Student Learning" content GaDOE prints alongside each standard in its own PDF (`dat/ga_k8_math_standards.pdf`, K-5 content pp. 7--70), confirmed absent from the CASE API (API items carry only a bare `fullStatement`). Fields, where present: `fundamentals`, `strategies_and_methods`, `terminology`, `age_developmentally_appropriate`, `relevance_and_application`, `examples`.

== Diagrams: extracted as real images

The source's `Examples` column often includes a diagram rather than only text. Images were extracted with `pdfimages` (pulling the actual embedded image, not a screenshot crop). Two complications: some images are stored as a separate RGB layer plus transparency mask, recomposed with `magick base.png mask.png -alpha off -compose CopyOpacity -composite out.png`; two diagrams are vector-drawn rather than raster (invisible to `pdfimages`), salvaged by rendering the page at 300dpi and cropping directly.

#keybox("Three-way classification, applied to every image found")[
  *(1) Decorative logo* (repeated "GELDS" Pre-K badge) -- dropped; adjacent text citation kept. \
  *(2) Photograph of real student handwork* -- excluded by scope decision. Where the source has its own explanatory prose, that text is kept verbatim as `examples` content, with a separate `diagram_excluded` key recording what was omitted -- never blended into the same string as the verbatim quote. \
  *(3) Clean instructional diagram* -- kept as a real extracted PNG under `processed/standards/diagrams/`, referenced by the sub-standard's `diagrams` array as `{"image": ..., "caption": ...}`, caption hand-written (not verbatim).
]

One table (Sam/Terri fish-count, `5.PAR.6.1`) was kept as text in `examples` rather than an image, since it is plain tabular data.

== Georgia guidance coverage, K--5

#table(
  columns: (auto, auto, auto, auto),
  align: (left, center, center, left),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*Grade*], [*Sub-standards*], [*Diagrams kept*], [*Notes*],
  [K (0)], [22], [3], [1 photo exclusion (ladybug, reused across 2 sub-standards)],
  [1], [22], [8], [1 photo exclusion (2 garden photos, no source caption)],
  [2], [22], [6 refs / 5 files], [1 photo exclusion (2 circle-partition photos); 1 vector-drawn diagram salvaged],
  [3], [29], [3], [--],
  [4], [30], [17], [largest diagram set; 1 vector-drawn diagram salvaged],
  [5], [25], [3], [1 table kept as text, not image],
  [*Total*], [*150*], [*40 refs / 39 files*], [],
)

Sub-standard count matches `georgia_math_*.json`'s independently-parsed K-5 total exactly (150).

== Cross-verification against `georgia_math_*.json`

`processed/scripts/verify_guidance_descriptions.py` checks, for every code in `georgia_math_{grade}.json`, whether the same code exists in `georgia_math_guidance_{grade}.json` and whether the description text matches exactly.

#table(
  columns: (auto, auto, auto, auto, auto),
  align: (left, center, center, center, center),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*Grade*], [*Matched*], [*Mismatched*], [*Missing from guidance*], [*Extra in guidance*],
  [K (0)], [26], [5], [8], [0],
  [1], [28], [1], [8], [0],
  [2], [24], [6], [8], [0],
  [3], [31], [7], [8], [0],
  [4], [32], [7], [8], [0],
  [5], [28], [6], [8], [0],
  [*Total*], [*169*], [*32*], [*48*], [*0*],
)

The 48 "missing" are all `{grade}.MP.1`--`{grade}.MP.8` (Mathematical Practices): GaDOE's PDF gives MP one grade-level paragraph with no per-item breakdown, so there is nothing for the guidance file to carry. Most of the 32 "mismatched" are pure typography (en-dash vs. hyphen, double- vs. single-space after period, curly vs. straight quotes, stray OCR spaces). Three are genuine wording differences between Georgia's own two official sources, re-verified against the PDF page in each case:

#table(
  columns: (auto, 1fr, 1fr),
  align: (left, left, left),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*Code*], [*`georgia_math_*.json` (CASE)*], [*GaDOE's own PDF*],
  [`2.GSR.7.4`], ["...may *be* different shapes..."], ["...may different shapes..." (PDF drops "be")],
  [`3.NR.1.1`], ["...up to 10,000 *to the thousands* using..."], ["...up to 10,000 using..." (no such clause)],
  [`4.NR.1`], ["...*and compare decimal numbers to the hundredths place*."], ["...through the hundred-thousands place." (no decimal clause)],
)

None is a substantive disagreement about what is actually required (`2.GSR.7.4` drops a word; `3.NR.1.1`'s clause is redundant; `4.NR.1`'s decimal clause restates content Grade 4 covers separately under `4.NR.5`). Left as-is in both files -- each stays verbatim to its own source.

= Skill mapping: CCSS #sym.arrow.l.r GA

Every Georgia K-5 sub-standard (150) is compared directly against every CCSS K-5 leaf code (175), grade by grade, using the two standards' own description/expectation text -- `georgia_math_guidance_*.json` consulted only to disambiguate an unclear description. *The prerequisite/progression graph (`math_prereq_grounding.json`) is deliberately not consulted*, per the advisor's "skill mapping first, then progression" direction, so this mapping cannot be circular with that later step.

== How the mapping is built

The mapping is produced by `processed/state_ccss_mapping/map_state_to_ccss.py` -- a generalizable, state-agnostic script (usable for any state's K-5 math standards, not just GA's) built around a single source of truth, `taxonomy.py`: the 8-type relationship taxonomy below, the cardinality-first rule, and a set of few-shot examples. One call classifies each GA leaf standard against the complete CCSS K-5 candidate set (~175 codes) at once -- no retrieval/embedding pre-filter, since with a candidate list this small, retrieval only adds a failure mode (a true match filtered out before the model ever sees it) for no benefit. A staged domain #sym.arrow.r cluster #sym.arrow.r leaf alternative was also tested (see "Hierarchical alternative" below) and performs worse; the flat method above is what actually produced this mapping.

Output: `processed/state_ccss_mapping/runs/ga/mapping_final.json` -- every GA code appears exactly once, every referenced CCSS code is real, `verify_mapping.py` checks both automatically plus the cardinality-first rule and a split-integrity check (below). Every entry carries its own GA description and CCSS description(s) inline.

*Human review.* All 150 codes were checked: every code where the script's classification wasn't already trivially settled was independently re-examined against the actual GA and CCSS text, and 7 needed correction. `verify_mapping.py`'s split-integrity check caught one more the manual pass missed (`K.GSR.8.2`, below) -- so *142/150 (95%) of the script's raw output needed no correction at all*. Full review trail, including the script's original (wrong) output for each corrected code: `processed/state_ccss_mapping/runs/ga/human_review.json`.

#table(
  columns: (auto, 1fr),
  align: (left, left),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*GA code*], [*What was wrong, and the fix*],
  [`3.NR.4.1`], [Script gave `exact` to `3.NF.1` alone; GA's text also covers `3.NF.1`'s number-line representation (`3.NF.2a`/`2b`) -- corrected to `merge` with all three.],
  [`3.MDR.5.4`], [Script claimed `split` (a sibling GA code supposedly shares `3.MD.4`), but no such sibling exists -- corrected to `exact`.],
  [`3.GSR.6.2`], [Script gave `exact` to `3.G.1`; GA's text also covers classifying quadrilaterals as faces of 3D figures, which `3.G.1` doesn't -- corrected to `state_superset`.],
  [`3.GSR.7.2`], [Script claimed `split` (citing `3.GSR.7.3` as the sibling), but `3.GSR.7.3` actually cites a different CCSS code entirely -- corrected to `merge` with `3.MD.6`, `3.MD.7a`, `3.MD.7d`.],
  [`3.GSR.7.3`], [Same invalid-split bug, the other direction (claimed `3.GSR.7.2` as its sibling) -- corrected to `merge` with `3.MD.7b`, `3.MD.7c`.],
  [`4.GSR.7.1`], [Script's `merge` was missing two codes (`4.MD.5b`, `4.MD.6`) that GA's text also covers -- corrected to include all four.],
  [`4.GSR.8.2`], [Script gave `state_superset` to `4.G.2` alone; GA's "lines of symmetry" criterion is substantial `4.G.3` content -- corrected to `merge` with both.],
  [`K.GSR.8.2`], [Not caught by manual review -- caught by `verify_mapping.py`'s split-integrity check (below). Script claimed `split` to `K.G.1`, citing `K.GSR.8.1` as the sibling, but `K.GSR.8.1` actually cites `K.G.4`, a different CCSS cluster entirely -- corrected to `state_subset` (GA covers only `K.G.1`'s positional-words half, not its shape-naming half, which is a genuine, separate gap).],
)

Categorized, these 8 corrections cluster into: 3 cases of a `split` claim whose sibling didn't actually exist (`3.GSR.7.2`, `3.GSR.7.3`, `K.GSR.8.2` -- the same underlying bug, one caught by machine), 2 cases of an incomplete `merge` set (`3.NR.4.1`, `4.GSR.7.1`), 1 `merge`/`exact` cardinality miss (`4.GSR.8.2`), 1 scope-judgment miss (`3.GSR.6.2`), and 1 false split with no analogous merge fix (`3.MDR.5.4`). The dominant pattern -- half the corrections -- is the script asserting a `split` relationship without verifying the sibling it names actually exists; `verify_mapping.py` now catches this automatically for any future run (see the split-integrity check description below), so this specific failure mode can't silently recur.

== Relationship types

#table(
  columns: (auto, 1fr),
  align: (left, left),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*Type*], [*Meaning*],
  [`exact`], [Same requirement and scope, reworded at most.],
  [`merge`], [One GA sub-standard covers more than one CCSS leaf code.],
  [`split`], [This GA sub-standard is one of several jointly covering a single CCSS leaf code.],
  [`different_grade`], [Same skill in both documents, but at different K-5 grades -- not a gap.],
  [`state_superset`], [GA requires everything CCSS does, plus more.],
  [`partial`], [Related but genuinely narrower/different; lower confidence.],
  [`state_subset`], [GA requires less than CCSS does (rare).],
  [`none`], [No CCSS K-5 leaf code judged equivalent at any grade -- a genuine gap, flagged for advisor discussion.],
)

The classification rule for `different_grade`/`partial` vs. `none`: an early-grade GA entry is `different_grade` (or `partial`, if scope also differs) only if it is the *same operation* at a narrower scope than its CCSS match -- e.g. `3.GSR.6.1`'s identify-perpendicular-lines is a scope-down of `4.G.1`'s identify-and-draw. If it is a *different operation* that merely shares a topic with a CCSS code some other GA entry already matches, it is `none`. This distinguishes, for example, GA's early identification-only money standards (`K.NR.1.4`, `1.MDR.6.3`, both `partial` -- identification overlaps computation but doesn't equal it) from GA's early pattern-*creation* standards (`K.PAR.6.1` and four others, `none` -- a different skill from CCSS's rule-based pattern-*generation* standard, which GA already matches at the same grade via `4.PAR.3.1`/`3.2`).

Cardinality is decided *before* scope: `state_superset`/`state_subset` are reserved for a true one-GA-to-one-CCSS pair. Any entry citing more than one CCSS code is `merge` (or `split`, the other direction) regardless of whether it also happens to have a superset/subset-flavored scope difference -- that nuance goes in the `note`, not the category. `verify_mapping.py` asserts this automatically: no `state_superset`/`state_subset` entry may cite more than one CCSS code.

A second automated check, added after the human review above surfaced the need for it: *split-integrity*. A `split` relationship means this GA code is one of several jointly covering a single CCSS code, so at least one other GA code in the same mapping must also cite it -- an entry that names a sibling which doesn't actually exist (or doesn't actually cite that code) is internally broken, not just a judgment call. This is exactly the bug behind 3 of the 8 corrections above.

== Results

#table(
  columns: (auto, auto),
  align: (left, right),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*Metric*], [*Count*],
  [GA sub-standards (K--5)], [150],
  [CCSS leaf codes (K--5)], [175],
  [GA mapped to #sym.gt.eq 1 CCSS code (same grade or cross-grade)], [138],
  [*GA genuine gap*], [*12*],
  [CCSS referenced by #sym.gt.eq 1 GA code], [152],
  [*CCSS genuine gap (unreferenced by any GA code)*], [*23*],
  [*Flagged for review, GA side* (`partial` + `state_subset` + `none`)], [*25*],
  [Human-reviewed corrections applied (of 150)], [8],
)

#table(
  columns: (auto, auto),
  align: (left, right),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*Relationship*], [*Count*],
  [exact], [56],
  [merge], [32],
  [split], [18],
  [different_grade], [7],
  [state_superset], [12],
  [partial], [6],
  [state_subset], [7],
  [none], [12],
)

== Review items by grade and category

All 25 GA-side + 23 CCSS-side flagged entries are recomputed directly from `mapping_final.json` -- not a separately curated review file.

GA-side (25), sorted by grade then domain code:

#table(
  columns: (auto, auto, auto, auto, auto, 1fr),
  align: (right, left, left, left, left, left),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*\#*], [*GA code*], [*Grade*], [*Category*], [*Relationship*], [*Why flagged*],
  [1], [`K.GSR.8.2`], [K], [GSR], [`state_subset`], [Low-confidence type; human-reviewed correction],
  [2], [`K.MDR.7.3`], [K], [MDR], [`none`], [Genuine gap],
  [3], [`K.NR.1.4`], [K], [NR], [`none`], [Genuine gap],
  [4], [`K.PAR.6.1`], [K], [PAR], [`none`], [Genuine gap],
  [5], [`K.PAR.6.2`], [K], [PAR], [`none`], [Genuine gap],
  [6], [`1.MDR.6.3`], [1], [MDR], [`none`], [Genuine gap],
  [7], [`1.PAR.3.1`], [1], [PAR], [`none`], [Genuine gap],
  [8], [`1.PAR.3.2`], [1], [PAR], [`none`], [Genuine gap],
  [9], [`2.MDR.5.1`], [2], [MDR], [`none`], [Genuine gap],
  [10], [`2.MDR.5.4`], [2], [MDR], [`partial`], [Low-confidence type],
  [11], [`2.PAR.4.1`], [2], [PAR], [`none`], [Genuine gap],
  [12], [`2.PAR.4.2`], [2], [PAR], [`none`], [Genuine gap],
  [13], [`3.MDR.5.1`], [3], [MDR], [`partial`], [Low-confidence type],
  [14], [`3.MDR.5.5`], [3], [MDR], [`partial`], [Low-confidence type],
  [15], [`3.PAR.3.4`], [3], [PAR], [`none`], [Genuine gap],
  [16], [`4.MDR.6.2`], [4], [MDR], [`partial`], [Low-confidence type],
  [17], [`4.MDR.6.3`], [4], [MDR], [`state_subset`], [Low-confidence type],
  [18], [`5.GSR.8.1`], [5], [GSR], [`state_subset`], [Low-confidence type],
  [19], [`5.MDR.7.1`], [5], [MDR], [`partial`], [Low-confidence type],
  [20], [`5.MDR.7.2`], [5], [MDR], [`none`], [Genuine gap],
  [21], [`5.NR.2.1`], [5], [NR], [`state_subset`], [Low-confidence type],
  [22], [`5.NR.2.2`], [5], [NR], [`state_subset`], [Low-confidence type],
  [23], [`5.NR.3.2`], [5], [NR], [`partial`], [Low-confidence type],
  [24], [`5.NR.4.3`], [5], [NR], [`state_subset`], [Low-confidence type],
  [25], [`5.NR.4.4`], [5], [NR], [`state_subset`], [Low-confidence type],
)

By domain: MDR -- 10, PAR -- 7, NR -- 6, GSR -- 2 -- MDR and PAR together account for 17 of 25, the two domains where GA's phrasing diverges most from CCSS's.

CCSS-side (23), leaf codes with no GA equivalent at any grade:

#table(
  columns: (auto, auto, auto, auto),
  align: (right, left, left, left),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*\#*], [*CCSS code*], [*Grade*], [*Category*],
  [1], [`K.CC.4a`], [K], [CC],
  [2], [`K.CC.7`], [K], [CC],
  [3], [`K.G.2`], [K], [G],
  [4], [`K.G.3`], [K], [G],
  [5], [`1.OA.5`], [1], [OA],
  [6], [`2.G.2`], [2], [G],
  [7], [`2.MD.2`], [2], [MD],
  [8], [`2.MD.5`], [2], [MD],
  [9], [`2.NBT.9`], [2], [NBT],
  [10], [`3.G.2`], [3], [G],
  [11], [`3.MD.5a`], [3], [MD],
  [12], [`3.NF.3a`], [3], [NF],
  [13], [`3.OA.1`], [3], [OA],
  [14], [`3.OA.2`], [3], [OA],
  [15], [`4.MD.7`], [4], [MD],
  [16], [`4.NF.3a`], [4], [NF],
  [17], [`4.NF.4b`], [4], [NF],
  [18], [`4.NF.4c`], [4], [NF],
  [19], [`5.MD.2`], [5], [MD],
  [20], [`5.MD.3a`], [5], [MD],
  [21], [`5.MD.3b`], [5], [MD],
  [22], [`5.MD.5c`], [5], [MD],
  [23], [`5.NF.4b`], [5], [NF],
)

= Generalizability, and the hierarchical alternative

`processed/state_ccss_mapping/` is state-agnostic: `map_state_to_ccss.py` and `taxonomy.py` take any state's K-5 standards in a common schema, not just GA's, and CCSS's own K-5 standards ship bundled in `ccss_standards/` so a new user doesn't need to separately curate them. As a second demonstration beyond GA, the same flat method was run on the 21 VA SOL codes whose text is available via EDUMath's crosswalk (`papers/edumath_data/matched_standards_summarized.csv`; see the EDUMath paper notes for that dataset's provenance) -- *19/21 domain-level agreement* with EDUMath's crosswalk (built by an undergraduate student and verified by an educator, a real independent check unlike GA's own single-reviewer history above).

#keybox("Standard-level, not sub-standard-level -- a real granularity difference from GA")[
  GA's own codes are sub-standard-level by construction: GaDOE assigns a distinct code to each lettered teaching point (`K.NR.5.1`, `K.NR.5.2`, ...), so this project's GA classification always operates on that fine a grain. VA's SOL numbering doesn't do this -- a VA code like `3.NS.4` covers several lettered bullets (a, b, c, d, ...) under one code, and no separate identifier exists for each. This pipeline classifies at the granularity VA's own numbering actually provides: the whole-standard description. EDUMath's crosswalk, by contrast, was built by citing one *specific* bullet per row for its own dataset's purposes -- so when its citation and this pipeline's citation disagree, the disagreement can be a real granularity mismatch (whole standard vs. one bullet of it) rather than either side simply being wrong. This is an accepted, structural limitation of the VA demonstration, not a defect to fix -- doing better would require first breaking VA's SOL text into its own lettered sub-points, which no source used here provides in complete form.
]

This granularity gap is exactly what's behind both disagreements, confirmed by reading EDUMath's underlying row data directly (`processed/standards/ccss_va_skill_map_edumath_raw.json`, `runs/va/unmatched_review.json`):

- `3.NS.4` -- this pipeline classified the whole standard ("counting, comparing, representing, and making change for money up to \$5.00") against `2.MD.8`, CCSS's dedicated money-computation standard, one grade earlier. EDUMath's row is keyed to one specific bullet, `3.NS.4:d` ("solve contextual problems to make change... using counting on or counting back strategies"), which it cites to `4.MD.2` ("use the four operations to solve word problems involving... money"). Read against that specific bullet, `4.MD.2`'s multi-step money-word-problem framing is arguably the better match for "make change using a strategy" than `2.MD.8`'s simpler coin-totaling -- EDUMath's citation is plausible for the bullet it's actually about, even though it isn't the best match for `3.NS.4` as a whole.
- `4.NS.3` -- this pipeline classified the whole standard ("represent, compare, and order fractions") against `4.NF.2`, the grade-appropriate fraction-comparison standard. EDUMath's row is keyed to a different bullet, `4.NS.3:g` ("represent the division of two whole numbers as a fraction," e.g. 3/5 = 3 #sym.div 5), which has nothing to do with comparison at all -- it cites `3.NF.1`. Read against that specific bullet, EDUMath's citation is closer to the right underlying concept than this pipeline's `4.NF.2`, which answers a different bullet's question entirely.

Both are accepted as expected consequences of the standard-vs-sub-standard granularity difference, not scored as pipeline errors or as EDUMath errors.

== Hierarchical alternative: tested, not adopted

A staged domain #sym.arrow.r cluster #sym.arrow.r leaf search was also tested -- `map_state_to_ccss_hierarchical.py`, modeled on the coarse-to-fine tree-traversal tagging approach used in some standards-tagging literature: pick the plausible CCSS domain famil(y/ies) (`CC`, `OA`, `NBT`, `MD`, `G`, `NF`, each spanning every K-5 grade it appears at), then the plausible cluster(s) within those families, then classify against only that narrowed leaf set -- hypothesized to reduce misclassification by shrinking the candidate set the model reasons over at each step.

#table(
  columns: (auto, auto, auto),
  align: (left, center, center),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*Dataset*], [*Hierarchical vs. adopted mapping*], [*CCSS-code-set agreement*],
  [GA, 150 codes], [111/150 (74%)], [124/150 (83%)],
  [VA, 21 codes#footnote[Domain-level only -- EDUMath's crosswalk cites a CCSS domain, not a specific sub-point, and doesn't classify relationship type. Both flat and hierarchical land on 19/21 (90%) agreement with EDUMath here, identical codes -- staging the search made no difference on VA.]], [19/21 (90%)], [--],
)

On GA it did the opposite of the hypothesis: narrowing to one cluster's ~5 leaf codes made small wording differences more salient, tipping calls the adopted mapping treats as `exact`/`none` into `state_superset`, more often than it fixed genuine merge/split-completeness misses. GA's disagreements were almost never domain-selection mistakes to begin with -- the flat method already picked the right domain family nearly every time -- so staged search targets a bottleneck that mostly isn't present in this dataset while introducing a new one. On VA, both methods converged on identical answers for all 21 codes, likely because VA's SOL statements are broad, multi-clause standards where domain selection was never the hard part.

Categorizing all 48 GA disagreements against the adopted mapping (`processed/state_ccss_mapping/runs/ga/error_analysis.json` has the full per-code breakdown; same fixed category set used for the 8 corrections above):

#table(
  columns: (1fr, auto),
  align: (left, center),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*Error type*], [*Count*],
  [Scope/label judgment, same single code (`exact`/`state_superset`/`state_subset`/`partial`/`different_grade`)], [13],
  [Merge boundary incomplete -- both sides say `merge`, disagree on the exact code set], [9],
  [Split not recognized -- adopted mapping says `split`, hierarchical treated it as standalone], [9],
  [Merge under-claimed -- adopted mapping needs 2+ codes, hierarchical gave a single-code relationship], [7],
  [Merge over-claimed -- hierarchical added a code the adopted mapping doesn't need], [5],
  [Genuine content-interpretation miss], [5],
  [*Total*], [*48*],
)

Scope/label judgment is by far the largest bucket (13/48) -- the two methods usually agree on *which* CCSS code is right, then disagree on how to label the relationship, because narrowing the candidate set to one cluster makes small wording differences more salient without making that judgment call any easier. This is the single biggest reason the hierarchical method underperforms. *The flat method is the recommended default and is what actually produced the adopted mapping*; the hierarchical script is kept and documented so a real API-key run can independently confirm or challenge this finding.

= Progression mapping

== Why CCSS's progression graph isn't transferred

CCSS's progression relationships (which standard is a prerequisite for which) are defined between CCSS codes, at CCSS's own granularity. Projecting them onto GA nodes through the skill map above breaks down unevenly by relationship type:

- `exact` + `state_superset` (71 of 150, about half) transfer cleanly -- one-to-one or superset correspondence preserves the prerequisite structure.
- `merge` (32) is a safe mechanical aggregation -- a GA node absorbing several CCSS codes needs everything those codes require.
- `split` (19) is the real problem -- one CCSS code's content is divided across multiple GA nodes, and an edge attached to that code can't be assigned to the correct child without reading the text again.
- `different_grade`, `partial`, `state_subset`, `none` (51 combined) involve a scope mismatch or outright gap, so there is no clean CCSS progression data to carry over.

Only about half the map transfers without judgment calls; the rest would need a manual, per-entry decision -- not worth solving when GA has published its own progression.

== Georgia's own Learning Progressions table

`dat/ga_k8_math_standards.pdf` includes a GaDOE-authored "K-5 Mathematics: Learning Progressions" table (pp. 5-6): 15 "Key Concept" strands (8 Numerical Reasoning, 2 Patterning \& Algebraic Reasoning, 2 Geometric \& Spatial Reasoning, 3 Measurement \& Data Reasoning) by grade, each cell a bullet list of what that strand covers. It is native to GA's own domain and grade structure, so no merge/split translation is needed to use it.

Transcribed verbatim (rendered as page images and read directly, since `pdftotext`'s layout mode garbled the stacked fraction glyphs in the Grade 4 Measurement \& Data cell) into `processed/standards/georgia_math_progressions.json`: 4 domains, 15 strands, 152 bullets.

This table is coarser than CCSS's own progression documents (long-form narrative, with pedagogical rationale and some cross-strand reasoning) -- GA's version has no narrated "why" and states no cross-strand dependencies (it does not say place value underlies multi-digit addition; that link is implicit). But it is complete across all K-5 grades and domains, officially authored by the same body that wrote the standards, and requires no lossy translation to use.

== Mapping the table to GA sub-standard codes

`georgia_math_progressions.json` names no standard codes -- it is prose bullets per strand per grade. `processed/scripts/map_progressions.py` cross-references every one of its 74 non-empty cells against the GA sub-standard text *and* guidance files (`georgia_math_{grade}.json` and `georgia_math_guidance_{grade}.json`) to identify which code(s) each cell corresponds to. Where a cell's own bullet text doesn't name a sub-standard's specific content but the sub-standard shares a parent standard with a sibling already placed in that cell, it is grouped there too (GA's parent-standard titles, e.g. `1.NR.2`: "...addition and subtraction problems within 20," are a much stronger signal than topical guessing). Output: `processed/standards/georgia_progressions_mapped.json`.

#table(
  columns: (auto, auto),
  align: (left, right),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*Metric*], [*Count*],
  [Progression-table cells mapped], [74],
  [GA sub-standards (K--5)], [150],
  [GA codes referenced by the progression table], [150 (all of them)],
  [Cells with a gap (bullet has no matching standard text, bare or guidance)], [5],
  [Cells whose codes cross the row's own domain heading], [10],
)

== Findings

#keybox("GA's progression table crosses its own domain headings")[
  Ten cells assign codes from a different GA domain than the row they sit under. Grade 3's entire "Computational Fluency", "Addition \& Subtraction", and "Multiplication \& Division" content under the *Numerical Reasoning* heading is coded under *Patterning \& Algebraic Reasoning* (`3.PAR.2.1`, `3.PAR.2.2`, `3.PAR.3.2`--`3.PAR.3.7`). Grade 1 and 2's "Numbers" row includes fraction-partitioning bullets coded as geometry (`1.GSR.4.3`, `2.GSR.7.3`/`7.4`). Money crosses domains inconsistently by grade: Kindergarten's is coded NR (`K.NR.1.4`) despite sitting under the MDR heading; Grade 1's is coded MDR (`1.MDR.6.3`, matching its row); Grades 4 and 5's money-as-tool content lives inside NR fraction/decimal standards (`4.NR.5.2`, `5.NR.4.4`).
]

#keybox("The Money row is real through Grade 5 -- just not as its own standard past Grade 2")[
  GA's dedicated money standards stop at `2.MDR.6.2` (Grade 2). But Grades 4 and 5's "money as a tool/manipulative" bullets aren't empty claims: `4.NR.5.2`'s guidance poses a money word problem to teach fraction/decimal equivalence, and `5.NR.4.4`'s guidance states almost verbatim "money may be used as a tool to aid in the student's understanding of adding and subtracting decimal numbers" -- money embedded as instructional context in another standard, not a dedicated standard of its own. This corroborates the skill-mapping finding that CCSS's own money standard (`2.MD.8`) is also fully realized at GA Grade 2. Grade 3's evidence stays thin -- a single scope caveat, no worked example -- so its "Using money to solve problems" bullet remains an open gap.
]

#keybox("The Counting strand thins into an implicit skill after Grade 2")[
  "Counting unit fractions" (Grade 3), "counting non-unit fractions" (Grade 4), and "counting decimal numbers" (Grade 5) have no standard -- bare or guidance -- describing a counting/enumerating skill for fractions or decimals. The nearest relatives (`3.NR.4.1`, `4.NR.4.4`/`4.NR.4.5`, `5.NR.4.1`) are about representing or reading those numbers, not counting through a sequence of them.
]

== Gap cells

5 cells have a bullet with no matching GA standard text (bare or guidance), recorded in `georgia_progressions_mapped.json`'s `gap_cells` array with the cell's full bullet list and whatever codes did match. 4 are partial (most bullets matched, one did not); 1 is total (zero matching standards: `MDR / Money`, Grade 3).

#table(
  columns: (auto, auto, auto, auto, 1fr),
  align: (right, left, left, center, left),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*\#*], [*Cell*], [*Grade*], [*Total gap?*], [*Unmatched bullet*],
  [1], [NR / Counting], [3], [No], [Counting unit fractions],
  [2], [NR / Counting], [4], [No], [Counting non-unit fractions],
  [3], [NR / Counting], [5], [No], [Counting decimal numbers],
  [4], [MDR / Measurement \& Data], [5], [No], [Create and analyze dot plots (line plots) with fraction measurements],
  [5], [*MDR / Money*], [*3*], [*Yes*], [Using money to solve problems],
)

== Codes placed by parent-standard grouping, not direct bullet match

145 of 150 codes matched a cell's bullet text directly; these 5 were placed alongside a sibling under the same parent standard instead:

#table(
  columns: (auto, auto, 1fr),
  align: (right, left, left),
  inset: 5pt,
  stroke: 0.4pt + luma(190),
  [*\#*], [*Code*], [*Placed alongside its siblings in*],
  [1], [`K.NR.1.3`], [Counting/K, with `K.NR.1.1`/`K.NR.1.2` (parent `K.NR.1`). Weakest fit -- a static relational skill, not sequential counting -- but its 1-20 range matches its siblings, unlike Comparisons/K's 10-object cap.],
  [2], [`K.GSR.8.3`], [Shapes and Properties/K, with `K.GSR.8.1`/`8.2` (parent `K.GSR.8` includes "form 2D/3D shapes" -- the composition half the cell's bullets don't mention).],
  [3], [`K.GSR.8.4`], [Same as `K.GSR.8.3` -- the other half of the same composition content.],
  [4], [`K.PAR.6.2`], [Patterns/K, with `K.PAR.6.1` (parent `K.PAR.6` names "patterns involving the passage of time" -- content no Patterns row at any grade otherwise mentions).],
  [5], [`3.PAR.3.4`], [Multiplication \& Division/3, with `3.PAR.3.3`/`3.5`/`3.6`/`3.7` (parent `3.PAR.3`). Its content (equal-sign/equivalence reasoning) is a narrower fit than its siblings', but the parent grouping is the deciding signal.],
)

For `K.GSR.8.3`, `K.GSR.8.4`, and `K.PAR.6.2`, the cell's own bullets are narrower than their governing parent standard's stated title -- `georgia_progressions_mapped.json`'s per-cell `note` field says so explicitly.

= Directory layout

```
dat/
  ccss-math-standards.pdf            raw source, CCSS
  ga_k8_math_standards.pdf           raw source, Georgia (K-8; only K-5 used)
  georgia-math-stardards.txt         raw source, plain-text GA transcription

processed/
  README.md                         full narrative documentation (this file's prose form)
  preprocess.typ                    this file
  math_prereq_grounding.json        prerequisite-edge citations (separate pipeline, see README)
  scripts/
    parse_math_standards.py         builds georgia_math_*.json from the .txt + CASE API
    map_progressions.py             builds georgia_progressions_mapped.json (see above)
  standards/
    ccss_math_0.json ... _5.json    CCSS K-5, verbatim + footnotes inlined
    ccss_glossary.json              CCSS Table 1 / Table 2, natural-language form
    georgia_math_0.json ... _5.json          GA K-5, bare code + description (CASE-derived)
    georgia_math_guidance_0.json ... _5.json GA K-5, Evidence of Student Learning
    georgia_math_progressions.json  GA's own K-5 Learning Progressions table, verbatim
    georgia_progressions_mapped.json  progression table cross-referenced to GA sub-standard codes
    diagrams/
      {STANDARD_CODE}_{short_description}.png   39 files, see table above
  state_ccss_mapping/                generalizable state <-> CCSS pipeline (see above), full
                                      technical documentation in its own README.md
    taxonomy.py, map_state_to_ccss.py, map_state_to_ccss_hierarchical.py, verify_mapping.py
    ccss_standards/                  bundled CCSS copy for standalone use
    runs/ga/mapping_final.json       the adopted GA <-> CCSS mapping (see "Skill mapping" above)
    runs/ga/human_review.json        full human review trail behind the 8 corrections
    runs/ga/error_analysis.json      categorized error counts, corrections + hierarchical run
    runs/va/                         VA demonstration run (flat + hierarchical)
  history/                           superseded files, kept for provenance -- see history/INDEX.md
```

= What this does and doesn't establish

Skill mapping answers which CCSS standard corresponds to which GA sub-standard, how many go unmapped on each side, and why. The progression question -- the advisor's "map skills first, then progression" next step -- is being answered from GA's own Learning Progressions table rather than by projecting CCSS's progression through the skill map's `merge`/`split` structure, for the reasons given above.

`georgia_progressions_mapped.json` closes the gap between the prose progression table and GA's actual codes: every cell is attached to the code(s) it corresponds to, with every gap and cross-domain case recorded. What remains open is turning this into an actual code-to-code *prerequisite* graph: the table states what each strand covers *at* each grade, not which code is a prerequisite *for* which other code, and it states no dependencies *between* strands. Building that edge-level graph -- within-strand edges from the grade sequence already established here, plus the harder cross-strand edges the source table leaves implicit -- is the next task, not yet started.

== Standing issue: `math_prereq_grounding.json` needs review

`processed/math_prereq_grounding.json` (171 GA-internal prerequisite edges, cited against CCSS's official Progressions documents) predates all of the work in this file and was *not* built against the thorough CCSS #sym.arrow.l.r GA skill mapping or the GA Learning Progressions mapping documented above. It should not be treated as authoritative until it is reviewed against both: several of its edges rely on a CCSS #sym.arrow.r GA correspondence that this file's own skill map may now contradict or refine, and none of its citations have been cross-checked against `georgia_progressions_mapped.json`'s grade-by-grade strand data. Its `OA_PROG` source citations are also currently stale in their own right (see `math_prereq_grounding.json`'s own `metadata.notes` -- the standalone OA extract they were paged against, `ccss_oa_k5.pdf`, was replaced by the combined `ccss_progressions_all.pdf`, and page numbers no longer line up). Reviewing and re-grounding this file against the mappings above is the next step.
