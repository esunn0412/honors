# processed/

Derived data for the K–5 personalized learning project.
**Nothing in `dat/` was modified** — all files here are new outputs.

---

## Directory structure

```
processed/
  README.md
raw/standards/                              # moved here from processed/standards/ on 2026-09-25
  json_to_csv.py                            # flattens ga/ and ccss/ JSON into the two CSVs
  ga_standards.csv                          # one row per GA leaf standard, guidance merged in
  ccss_standards.csv                        # one row per CCSS leaf standard
  ga/
    georgia_math_0.json ... _5.json         # K–5 GA math standards (raw/scripts/parse_math_standards.py)
    georgia_math_guidance_0.json ... _5.json  # GA "Evidence of Student Learning" guidance
    diagrams/                               # images referenced by the guidance files
  ccss/
    ccss_math_0.json ... _5.json            # K–5 CCSS math standards
    ccss_glossary.json                      # CCSS Glossary Tables 1 and 2
```

ELA data (`ela_precedes.json`, `extract_ela_precedes.py`, `georgia_ela_*_enriched.json`) is currently archived — see "ELA data (currently archived)" below and `history/ela_deprioritized/README.md`.

---

## Data sources & scripts

| Output | Source | Script |
|--------|--------|--------|
| `raw/standards/ga/georgia_math_*.json` | `dat/georgia-math-stardards.txt` (validated: 150/150 codes match live CASE API) | `raw/scripts/parse_math_standards.py` |
| `raw/standards/ccss/ccss_math_*.json` | `dat/ccss-math-standards.pdf` (official CCSSM PDF, corestandards.org), transcribed directly page-by-page, not OCR'd | manually transcribed, no script (no live API for CCSS) |

---

## Math standards schema

Math uses a **3-level hierarchy** — domain → standard → sub_standard — because
the Georgia math standards have no "big ideas" grouping. This differs from ELA
which has 4 levels (domain → big_idea → standard → sub_standard).

```json
{
  "subject": "Mathematics",
  "grade": "0",
  "source": "Georgia K-12 Mathematics Standards (SY2023-2024)",
  "case_document_id": "e9dd7229-3558-4df2-85c6-57b8938f6180",
  "domains": [
    {
      "code": "K.NR",
      "name": "Numerical Reasoning",
      "is_meta": false,
      "standards": [
        {
          "code": "K.NR.1",
          "description": "Demonstrate and explain the relationship...",
          "sub_standards": [
            { "code": "K.NR.1.1", "description": "Count up to 20 objects..." }
          ]
        }
      ]
    },
    {
      "code": "K.MP",
      "name": "Mathematical Practices",
      "is_meta": true,
      "description": "Display perseverance and patience...",
      "standards": [
        { "code": "K.MP.1", "description": "Make sense of problems..." }
      ]
    }
  ]
}
```

### Math domains (consistent across all grades)

Names are GaDOE's own, as printed in `raw/ga_k8_math_standards.pdf` and
`georgia_math_guidance_*.json`. The source `.txt` carries no domain names, so
they are hardcoded in `parse_math_standards.py`'s `DOMAIN_META`; before
2026-09-25 that table had wrong names ("Number Relations", "Measurement,
Data, and Results", ...), which were then corrected in both places.

| Code | Full name | is_meta |
|------|-----------|---------|
| `MP` | Mathematical Practices | true |
| `NR` | Numerical Reasoning | false |
| `PAR` | Patterning and Algebraic Reasoning | false |
| `MDR` | Measurement and Data Reasoning | false |
| `GSR` | Geometric and Spatial Reasoning | false |

### LaTeX patches

Three Grade 5 sub-standards had math notation plain-texted in the source file.
The script fetches their canonical descriptions from the CASE API at runtime:

| Code | Plain text (source file) | LaTeX (CASE API / output) |
|------|--------------------------|---------------------------|
| `5.NR.1.1` | `1/10` | `$\frac{1}{10}$` |
| `5.NR.1.2` | `10^3` | `$10^3$` |
| `5.NR.3.1` | `a / b = a ÷ b` | `$\frac{a}{b}$ = a ÷ b` |

### Sub-standard counts

| Grade | Domains | Standards | Sub-standards |
|-------|---------|-----------|---------------|
| K (0) | 6 | 16 | 22 |
| 1 | 6 | 14 | 22 |
| 2 | 6 | 15 | 22 |
| 3 | 6 | 16 | 29 |
| 4 | 6 | 16 | 30 |
| 5 | 6 | 16 | 25 |

---

## CCSS math standards schema

`raw/standards/ccss/ccss_math_0.json` ... `ccss_math_5.json` hold the full K–5 Common
Core State Standards for Mathematics, transcribed directly from the official
PDF page-by-page (not OCR'd, not reconstructed from memory) so every
description string can be checked against a specific page. Built for the
CCSS<->GA math skill-mapping step directed by the advisor (2026-09-01 meeting):
map skills first, then progression, with zero ambiguity on what counts as a
standard on each side.

### Why this schema has 4 levels, not 3

CCSS's real structure is **domain → cluster → standard → (optional) lettered
sub-standard**, one level deeper than `georgia_math_*.json`'s domain → standard
→ sub-standard. Clusters are unlabeled heading text in the source document (no
code, e.g. "Know number names and the count sequence."); standards are numbered
and coded (`K.CC.1`); some standards further break into lettered parts
(`K.CC.4a/b/c`) that are the genuine finest-grained unit when present. Numbering
is continuous across clusters within a domain, not restarted per cluster.
Collapsing clusters into GA's 3-level shape would misrepresent the source, so
the extra level is kept and documented instead.

```json
{
  "subject": "Mathematics",
  "grade": "0",
  "source": "Common Core State Standards for Mathematics (CCSSM), NGA/CCSSO, 2010",
  "source_document": "dat/ccss-math-standards.pdf",
  "source_pages": "pp. 9-12",
  "notes": { "hierarchy": "...", "footnote_1": "..." },
  "domains": [
    {
      "code": "K.CC",
      "name": "Counting and Cardinality",
      "clusters": [
        {
          "description": "Know number names and the count sequence.",
          "standards": [
            { "code": "K.CC.1", "description": "Count to 100 by ones and by tens." }
          ]
        }
      ]
    }
  ]
}
```

Domain/cluster/standard-scoped footnotes from the source (e.g. "Grade 3
expectations in this domain are limited to fractions with denominators 2, 3,
4, 6, and 8") are concatenated directly into the relevant node's `description`
text in parentheses, at the exact standard the source PDF attaches them to
(verified against the source page for every footnote, not just assumed from
placement in the running text) — not kept as a separate footnote lookup.

### Glossary references (`ccss_glossary.json`)

Six standards' descriptions cite "see Glossary, Table 1" or "Table 2" instead
of restating the content inline — those two tables are full word-problem
taxonomies (addition/subtraction situations; multiplication/division
situations), too long to fold into a description string the way an ordinary
footnote is. Handled differently from ordinary footnotes: the raw "(see
Glossary, Table N)" text is stripped from the standard's `description`, and a
`"glossary_ref"` key is added naming one of `ccss_glossary.json`'s block
`id`s (`addition_subtraction_situations` or
`multiplication_division_situations`), where the table is reproduced as
structured categories with the source's own examples, not a literal grid.
`glossary_ref` is a convention invented for this project, not a CCSS/CASE
field — it matches a block's own `"id"` field, not just the JSON key it
happens to sit under, so the reference still resolves if a block is ever
moved or the file restructured.

Every field inside `ccss_glossary.json` (titles, category names, examples,
footnotes) is a verbatim transcription checked against the source page
images — nothing is summarized or paraphrased. The file is also the single
source of truth for which standards cite which slug: it does **not** keep a
reverse "referenced_by" list back to the citing standards, since that would
be a second hand-maintained copy of what the standards files' own
`glossary_ref` tags already say, and the two could silently drift apart. To
find every standard citing a slug, scan `ccss_math_*.json` for that
`glossary_ref` value directly (currently: `addition_subtraction_situations` →
`1.OA.1`, `2.OA.1`, `2.MD.10`; `multiplication_division_situations` →
`3.OA.3`, `3.MD.2`, `4.OA.2`).

The source Glossary also has Table 3 (properties of operations), Table 4
(properties of equality), and Table 5 (properties of inequality) — not
reproduced here since no K-5 standard actually cites them.

### Standard counts (K–5)

| Grade | Domains | Top-level standards | Leaf units (lettered parts counted separately) |
|-------|---------|----------------------|--------------------------------------------------|
| K (0) | 5 | 22 | 24 |
| 1 | 4 | 21 | 23 |
| 2 | 4 | 26 | 27 |
| 3 | 5 | 25 | 33 |
| 4 | 5 | 28 | 34 |
| 5 | 5 | 26 | 34 |
| **Total** | | **148** | **175** |

"Top-level standards" counts each numbered CCSS standard once regardless of
lettered parts (e.g. `K.CC.4` counts as 1). "Leaf units" counts lettered parts
separately when present (e.g. `K.CC.4a/b/c` count as 3), matching the
finest-grained citable unit — the number to use when comparing against GA's
150 K–5 math sub-standards for the skill-mapping exercise.

---

## Georgia "Evidence of Student Learning" guidance (`raw/standards/ga/georgia_math_guidance_*.json`)

Richer per-sub-standard content GaDOE prints in its own standards PDF but does
**not** expose via the CASE API (confirmed by querying it directly — API
items only carry a bare `fullStatement`). Source:
`dat/ga_k8_math_standards.pdf` (GaDOE, 2021), K-5 section is pp. 7-70 (pp.
71-75 are 6-8 progression overview tables, out of scope). All six grades are
built: `georgia_math_guidance_0.json` (K, pp. 7-15) through `_5.json` (Grade
5, pp. 61-70). Sub-standard counts (22, 22, 22, 29, 30, 25) sum to exactly
150, matching `georgia_math_*.json`'s known K-5 total.

Per sub-standard: `expectation` plus whichever of `fundamentals`,
`strategies_and_methods`, `terminology`, `age_developmentally_appropriate`,
`relevance_and_application`, `examples` the source actually has for it (not
every sub-standard has all six) — every bullet verbatim, checked against the
source page images.

Two categories of source content are deliberately excluded: the decorative
"GELDS" Pre-K logo icon (repeated, no information beyond the text citation
already kept), and photographs of actual student handwork (real, but out of
scope here — their own explanatory "Note" text, when the source provides
one, is kept as ordinary example text regardless).

Clean instructional diagrams (manipulatives, patterns, shape compositions)
**are** kept as real image files — extracted directly from the PDF's
embedded image objects via `pdfimages` (not a rendered screenshot crop), saved
to `raw/standards/ga/diagrams/`, and referenced from the citing sub-standard's
`diagrams` array by relative path with a caption.

## ELA data (currently archived)

ELA's CASE `precedes` data (826 cross-grade links, real and well-cited) and
the enriched standards files built from it are not part of the active dataset
right now — moved to `history/ela_deprioritized/` on 2026-09-01 per an explicit
scope decision, not a data-quality problem. See that directory's `README.md`
for the full format documentation and the return path when ELA work resumes.

---

## Math prerequisite grounding document

`processed/math_prereq_grounding.json` is the authoritative source for authoring
math skill dependency edges. It was built by reading the CCSS Progressions documents
(OA K-5 and NBT K-5) and mapping the explicit grade-by-grade statements to Georgia
sub-standard codes.

### Schema

```json
{
  "metadata": { "version", "description", "sources", "rule_taxonomy", "notes" },
  "dependencies": [
    {
      "from": "K.NR.5.1",       ← prerequisite sub-standard
      "to": "1.NR.2.1",         ← dependent sub-standard (requires 'from' first)
      "rule": "grade_progression",
      "source": "OA_PROG p.16: '...'",
      "ccss_from": "K.OA.3",
      "ccss_to": "1.OA.6",
      "confidence": "high | medium"   ← only present when medium
    }
  ]
}
```

### Rule taxonomy

| Rule | Meaning |
|------|---------|
| `grade_progression` | Same concept, next grade year |
| `scope_expansion` | Same concept, wider number range or added complexity |
| `concept_foundation` | One standard is a named conceptual prerequisite for another |
| `bloom_progression` | Lower cognitive level precedes higher on the same concept |
| `decomposition` | Foundational sub-skill precedes the composite whole |
| `topic_continuity` | Same topic recurs at the next grade with expanding scope, read directly from Georgia's own standard text -- used only where no CCSS Progressions document exists (time, money, a few verbatim-repeated GA standards). Always `confidence: medium`. |

### Coverage

148 dependency edges (`NR`: 79, `PAR`: 20, `MDR`: 23, `GSR`: 26) -- 145/150 K-5 sub-standards (97%) have at least one edge:
- `NR`/`PAR`: full K-5 coverage (place value, computation, fractions, decimals, algebraic patterns) except one `NR` sub-standard. Fraction edges are cited directly against NF_PROG, not secondhand.
- `MDR`: full K-5 coverage except one sub-standard; time and money grounded via `topic_continuity` since no CCSS Progressions document covers either.
- `GSR`: full K-5 coverage of area/perimeter/angle/volume/quadrilateral-hierarchy content, including `3.GSR.6.1`/`3.GSR.6.3` (Georgia introduces this vocabulary a grade earlier than GEOM_PROG's own sequencing; cited by reusing the same passage that grounds their Grade-4 CCSS-placed equivalents, with the placement difference stated explicitly) except two sub-standards.

Remaining 5 gaps, all genuine -- no document addresses any of them (not an unread-source problem): `1.NR.2.5` (equal-sign truth/falsity), `K.PAR.6.2` (time-pattern description), `5.MDR.7.1` (general measurement-units overview), `K.GSR.8.2` (positional words), `2.GSR.7.2` (informal symmetry recognition). Each still gets a well-defined `relative_depth` via the sibling-median fallback (see `proposal.typ`, "Computing prerequisite depth") -- nothing is left undefined, they simply have no citation.

### Source PDFs -- all now read in full

| Key | File |
|-----|------|
| `OA_PROG` | `processed/scripts/ccss_oa_k5.pdf` (39 pages) |
| `NBT_PROG` | K-5, Number and Operations in Base Ten (draft 4/7/2011). https://www.isbe.net/Documents/number-base-ten-k-5.pdf |
| `GEOM_PROG` | Geometry, K-6 (draft 27 Dec 2014), 21 pages. |
| `GEOM_MEAS_PROG` | Geometric Measurement, K-5 (draft 6/23/2012), 28 pages. |
| `DATA_PROG` | "K-3, Categorical Data; Grades 2-5, Measurement Data" (draft 6/20/2011), 13 pages. |
| `NF_PROG` | Number and Operations--Fractions, 3-5 (draft 8/12/2011), 13 pages. |
| Combined | `processed/scripts/ccss_progressions_all.pdf` (11 MB, superseded by the individual PDFs above). |

---

## What these files are NOT

### ELA within-grade skill ordering — archived, not used

The `precedes` data only captures **cross-grade** progressions. A separate,
pre-existing file previously at `dat/skills/skills_ela_*.json` carried a
`prerequisites` field encoding **within-grade** sequential ordering (e.g.
Rhyme Recognition → Word Segmentation → Compound Words). Those links were
constructed separately and are **NOT derived from the CASE API and carry no
citation**. This file has been moved to
`history/ela_skills_ungrounded/` and is not part of the active dataset —
see the README there for what is and isn't still usable from it.

### Math prerequisites

The math CASE package has **no `precedes` associations** — only `isChildOf`
(hierarchy) and `isRelatedTo` (old GSE → new 2023 standard crosswalk).
All math dependencies (both within-grade and cross-grade) must be authored
when building `dat/skills/skills_math_*.json`.

---

## Regenerating outputs

```bash
# From the project root (honors/)
python3 raw/scripts/parse_math_standards.py
python3 raw/scripts/verify_guidance_descriptions.py   # GA standards vs guidance wording check
python3 raw/standards/json_to_csv.py
```

Requires network access to the Georgia CASE API; can run offline if the LaTeX
patches fail, falling back to the plain-text source descriptions.

`ccss_math_*.json` has no regenerating script — there is no live CCSS API, so
it was transcribed by hand directly from `dat/ccss-math-standards.pdf`
(citations to exact page ranges are in each file's `source_pages` field).

`extract_ela_precedes.py` (ELA `precedes` extraction, requires the CASE API)
is currently archived — see `history/ela_deprioritized/README.md`.
