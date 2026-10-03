# Open items: conflicts for re-adjudication and pending edits

*Companion to [`annotation_guideline.md`](annotation_guideline.md), version 1.2 (Sep 30, 2026). For the adjudication meeting only: it discusses specific answers in the adjudicated Georgia mapping, so don't give it to annotators or use it in calibration (guideline section 10). "Section" numbers below refer to the guideline.*

A check of the guideline against the adjudicated Georgia mapping (`states/ga/gold.json`) found the
cases below, where applying the guideline gives a different answer from the gold. The gold has **not**
been changed; each case is to be re-adjudicated, and either the gold or the guideline updated.

## 1. Split or subset (section 7, step 6A)

| # | Georgia standard(s) | Gold | Guideline implies | Why |
|---|---|---|---|---|
| 1 | 3.NR.1.1, 3.NR.1.2 → 4.NBT.2 | `split` (with 4.NR.1.1, 4.NR.1.3) | `state_subset` | 4.NR.1.1 and 4.NR.1.3 together make up 4.NBT.2; the grade-3 standards cover the same parts with smaller numbers (the worked example in step 5). |
| 2 | 1.NR.2.1, 1.NR.2.2 → 1.OA.1 | `split` | 1.NR.2.1 `exact`; 1.NR.2.2 not a split partner | 1.OA.1 has one part, solving word problems within 20; its drawings and equations are an "e.g." (Test C). 1.NR.2.1 covers the whole code (its guidance lists all problem types). 1.NR.2.2's action, developing strategies, is 1.OA.6's. |
| 3 | 3.PAR.3.6, 3.PAR.3.7 → 3.OA.3 | `split` | no clear answer | Both solve multiplication and division problems within 100 and differ only in representations, which 3.OA.3 gives as an "e.g.". Each covers the whole code, so neither `split` (different parts) nor two `exact` fits. **Needs a ruling.** |

## 2. Merge or superset (section 7, step 6B)

| # | Georgia standard | Gold | Guideline implies | Why |
|---|---|---|---|---|
| 4 | 4.GSR.8.1 → 4.G.1 | `exact` | `merge`: 4.G.1 + 4.G.3 | Its extra part, "draw … lines of symmetry", is 4.G.3's core requirement. Also the contrast example in step 5. |
| 5 | 3.NR.4.1 → 3.NF.1 | `state_superset` | `merge`: 3.NF.1 + 3.NF.2a + 3.NF.2b | Its extra part, "points on a number line, distances on a number line", is 3.NF.2a and 3.NF.2b's core requirement; it is a required "Use", not an "e.g.". |
| 6 | 2.NR.2.3 → 2.NBT.6 + 2.NBT.7 | `merge` | `merge`, citing 2.OA.1 | The text's core, solving addition and subtraction problems with two-digit numbers, is 2.OA.1's (cited nowhere in the gold; the Georgia guidance paraphrases it). 2.NBT.6 (up to four addends) and 2.NBT.7 (within 1000) rest on bounds from the guidance only (section 4.1). |
| 7 | 3.GSR.7.3 → 3.MD.7b + 3.MD.7c | `merge` | drop 3.MD.7c: 3.MD.7b `exact`, or `merge` with 3.MD.7a | The distributive property (3.MD.7c) appears only in a guidance example (section 4.1, Test A). "Discover … how area can be found by multiplying" matches 3.MD.7a's "show that the area is the same as would be found by multiplying". |
| 8 | 4.NR.4.6 → 4.NF.3c + 4.NF.3d | `merge` | drop 4.NF.3d; possibly 4.NF.3a + 4.NF.3c | Solving word problems (4.NF.3d's core) comes only from the guidance, which itself uses 4.NF.3a's wording ("joining and separating parts referring to the same whole"). |
| 9 | 4.GSR.7.1 → 4.MD.5b + 4.G.1 | `merge` | `state_subset` of 4.G.1 | 4.MD.5b ("an angle that turns through n one-degree angles…") is not stated and is close to a definition (Test B). The text restates only the first half of 4.MD.5's general statement, so "cite all lettered parts" does not apply. |
| 10 | K.NR.5.1 → K.OA.3 + K.OA.4 | `merge` | possibly `state_superset` of K.OA.3 | K.OA.4's core, finding the number that makes 10, is not stated; "compose numbers up to 10" is general. Borderline. |
| 11 | K.MDR.7.1 → K.MD.1 + K.MD.2 | `merge` | `merge`, adding 1.MD.1 | Its extra part, ordering objects, is 1.MD.1's first requirement (one grade away). Label unchanged. |
| 12 | 2.MDR.6.1 → 2.MD.7 | `state_superset` | possibly `merge`: 2.MD.7 + 3.MD.1 | Its extra part, measuring elapsed time, is 3.MD.1's "measure time intervals", with narrower bounds; the gold accepts the same narrowing for 3.MDR.5.3 in the 3.MD.1 split. **Needs a ruling** on how narrow an extra part may be. |
| 13 | 3.NR.4.3 → 3.NF.2a + 3.NF.2b + 3.NF.3c | `merge` | drop 3.NF.3c | The number line is supported by the guidance (an interpretation, section 4.1); "fractions greater than one" is not 3.NF.3c's "express whole numbers as fractions". |
| 14 | 2.GSR.7.1 → 2.G.1 | `state_superset` | `overlap` (item 32) | It lacks 2.G.1's "draw" (a separate objective), so it does not fully match the code; it both adds and lacks, and step 6 decides by the more substantial difference. |
| 15 | 5.NR.3.4 → 4.NF.4b + 4.NF.4c | `merge` | consider adding rows for 5.NF.4a, 5.NF.6 | The "prefer a same-grade code" tie-break was removed (Oct 3): with per-row labels, codes at different grades that share the requirement each get a row. Same-grade 5.NF.4a and 5.NF.6 are cited nowhere in the gold; check whether they share a requirement with 5.NR.3.4 and add rows if so. |

Items 4–7 are the clearest; items 10–15 are judgment calls.

## 3. From the educator review

A review of the guideline as a K–5 math educator would read it (checked against the CCSS text, the
CCSS Progressions and Georgia's guidance) found the cases below. Items 17–19 depend on the proposed
rules in part 5.

| # | Georgia standard(s) | Gold | Educator reading implies | Why |
|---|---|---|---|---|
| 16 | K.MDR.7.3, 1.MDR.6.4, 2.MDR.5.4, 3.MDR.5.1, 4.MDR.6.2, 5.MDR.7.2 ("Ask questions and answer them based on gathered information, observations, and appropriate graphical displays…") | `none` (also worked example E15) | at least grades 1–3: `state_subset` of the grade's data code (1.MD.4, 2.MD.10, 3.MD.3); K, 4 and 5 to be checked | These are Georgia's data standards (domain MDR), not general practices; Georgia has separate practice standards (K.MP.1–8 etc.). The Progressions describe 1.MD.4 in nearly Georgia's words: students "ask and answer questions about categorical data based on a representation of the data". 1.MDR.6.4's "compare and order whole numbers" matches 1.MD.4's "how many more or less". 1.MD.4, 2.MD.10 and 3.MD.3 are cited nowhere in the gold, so the mapping implies Georgia has no data standards in grades 1–3. **Strongest item from this review.** |
| 17 | 4.NR.2.1 → 4.NBT.4 | `exact` | ~~`state_subset` (under R1)~~ settled: stays `exact` (R1 declined) | 4.NBT.4 requires "using the standard algorithm"; 4.NR.2.1 instead says "using place value understanding, properties of operations, and relationships between operations". The standard algorithm is a required method, not an "e.g."; teachers treat it as its own objective, and Georgia's omission of it is deliberate. |
| 18 | 5.NR.2.1 → 5.NBT.5 | `state_subset` | settled: unchanged (R1 declined) | Its text also lacks "using the standard algorithm"; Georgia's guidance makes it optional ("Students may also use a standard algorithm…"). This adds to the narrower bounds already noted. |
| 19 | 1.NR.2.4 → 1.OA.6 | `exact` | `state_subset`, or `split` with 1.NR.2.2 (under R2) | 1.OA.6 requires adding and subtracting within 20 with strategies, and fluency within 10. 1.NR.2.4 covers fluency within 10 only (Test D); 1.NR.2.2 (strategies within 20) may cover the rest. Related to item 2. |
| 20 | K.NR.4.1 → K.CC.3 (worked example E2) | `exact` | contested: possibly `state_subset` | Kindergarten teachers treat writing numerals as its own skill (a fine-motor demand; often reported separately), and "Write numbers from 0 to 20" is its own sentence in K.CC.3. The current rule (receptive vs. productive form, Test C) is clear; the question is whether educators accept it. Classroom judgment, not a source finding. |
| 21 | 3.GSR.7.1 → 3.MD.5b + 3.MD.6 (worked example E11) | `merge` | contested: possibly add 3.MD.5a | 3.MD.5a and 3.MD.5b are both phrased as definitions ("is said to have"), and 3.GSR.7.1's "multiple copies of the same unit" arguably states 5a's unit. Either add 5a or explain in Test B why 5a is a definition and 5b is not. |

## 4. From the per-row and `overlap` rules (Oct 3, 2026)

The guideline now labels each (state standard, CCSS code) row on its own by **which standard is inside
which** (sections 6–7): each inside the other → `exact` (at any grade; `different_grade` was removed);
the state standard inside the code → `split` / `state_subset`; the code inside the state standard →
`merge` / `state_superset`; neither → `overlap`, which still counts as a piece toward making up either
side. A row-by-row pass over the gold's 23 merges and all split, subset and superset rows (the 61
`exact` rows were not re-checked):

- **Unchanged:** the merges K.NR.5.1, K.GSR.8.1, 1.NR.1.2, 2.NR.1.1, 2.MDR.5.2, 3.NR.4.4, 3.GSR.7.1,
  4.NR.2.2, 5.NR.3.3, 5.NR.3.4, 5.NR.3.6, 5.NR.5.1, and most split, subset and superset rows.
- **Would change** (judged from the texts and Georgia's guidance; for the annotators to confirm):

| # | Georgia standard | Gold | Rows under the new rules | Why |
|---|---|---|---|---|
| 22 | 1.MDR.6.1 | `merge` | 1.MD.1 `overlap`; 1.MD.2 `state_superset` | 1.MD.1's indirect comparison ("compare the lengths of two objects indirectly by using a third object") is not in the standard, and the standard has "estimate", which 1.MD.1 lacks. "Estimate" lengths is left over: no code covers it in non-standard units. |
| 23 | K.MDR.7.1 | `merge` | K.MD.1, K.MD.2 `merge`, plus 1.MD.1 `overlap`; without 1.MD.1, `state_superset` | "Order" objects is left over unless 1.MD.1 ("Order three objects by length") is cited; as an `overlap` piece it covers ordering, so the pieces make up the standard. Settles item 11. Depends on item 26 only if ordering objects is ruled not a separate objective. |
| 24 | 2.NR.1.3 | `merge` | `merge`, or `state_superset` on both rows | Depends on item 26 ("order" whole numbers to 1000). |
| 25 | 4.GSR.8.2 | `merge` | 4.G.2 `overlap`; 4.G.3 `overlap` | Each code has something the standard lacks (4.G.2: right triangles; 4.G.3: "draw lines of symmetry") and the standard has more (side lengths, comparing and contrasting). |
| 26 | **Ruling needed:** is ordering numbers a separate objective from comparing them? | — | apply one answer to 1.NR.1.3, 2.NR.1.3, 4.NR.1.3, 5.NR.3.2, 5.NR.4.2 | The gold disagrees with itself: 1.NR.1.3 ("Compare and order whole numbers up to 100") is `exact` with 1.NBT.3, so ordering did not count; 5.NR.3.2 and 5.NR.4.2 ("compare and order") are `state_superset`, so it did. No CCSS code requires ordering numbers. If ordering counts, 4.NR.1.3 → 4.NBT.2 becomes `overlap`, which changes the 4.NBT.2 worked example. Add the answer to the Test C lists. |
| 27 | 4.GSR.7.1 | `merge` | 4.G.1 `overlap`; 4.MD.5b `merge` (if kept, item 9) | The standard covers only drawing angles from 4.G.1, and adds recognizing angles as shapes. 4.MD.5b and the overlap piece 4.G.1 together make up the standard. |
| 28 | 2.NR.2.3 | `merge` | 2.NBT.6 `merge` or `state_superset`; 2.NBT.7 `overlap` | 2.NBT.7 is within 1000 with three-digit place value, which the standard lacks; the standard's problem solving is not in 2.NBT.7. Whether the pieces make up the standard depends on item 6 (2.OA.1). |
| 29 | 4.NR.4.6 | `merge` | 4.NF.3c `merge`; 4.NF.3d `overlap` | 4.NF.3d's word problems are only in the guidance (item 8), and the standard has mixed numbers, which 4.NF.3d lacks. 4.NF.3c and the overlap piece make up the standard. |
| 30 | 4.MDR.6.1 | `merge` | 4.MD.1 `merge`; 4.MD.2 `overlap` | 4.MD.2 includes "money" and "simple fractions or decimals", which the standard lacks (Test D); the standard adds converting a smaller unit to a larger one. The pieces make up the standard. |
| 31 | 5.GSR.8.3 | `merge` | 5.MD.3b `merge`; 5.MD.5a `overlap` | 5.MD.5a also asks to "show that the volume is the same as would be found by multiplying the edge lengths" (covered by 5.GSR.8.4), and the standard adds solving problems. If 5.GSR.8.4 gets a 5.MD.5a row, the two together make up 5.MD.5a. |
| 32 | 2.GSR.7.1 | `state_superset` | 2.G.1 `overlap` | 2.G.1's "draw shapes" is not in the standard; the standard adds 3-D shapes and sorting. Settles item 14. |
| 33 | 3.NR.4.3 | `merge` | 3.NF.2a, 3.NF.2b `merge` or `state_superset`; 3.NF.3c `overlap` or dropped (item 13) | Whether the pieces make up "represent fractions … in multiple ways" depends on whether area and set models (named in the guidance) count as a separate objective (Test C: representations). |
| 34 | 3.GSR.7.3 | `merge` | depends on item 7 | If 3.MD.7c stays cited, the standard lacks its distributive property and it is `overlap` at most. |
| 35 | 1.GSR.4.1 → 1.G.1 | `state_subset` | `overlap` | The standard adds identifying, sorting and classifying 2-D and 3-D shapes; 1.G.1 adds distinguishing defining from non-defining attributes. |
| 36 | 3.MDR.5.5 → 3.MD.2 | `state_subset` | `overlap` | The standard uses customary units and includes lengths; 3.MD.2 uses metric units (g, kg, l) for masses and volumes (Test D both ways). |
| 37 | 3.GSR.6.1 → 4.G.1 | `state_subset` | `overlap` | The standard adds "solve problems involving" the figures (a separate objective, Test C); 4.G.1 adds drawing. Now the guideline's `overlap` contrast example. |
| 38 | 3.GSR.6.2 → 4.G.2 | `state_subset` | `overlap` | The standard adds analyzing 3-D figures for quadrilateral faces; 4.G.2 adds right triangles. |
| 39 | 4.GSR.8.3 → 4.MD.3 | `state_subset` | `overlap`; consider also citing 3.MD.7d | The standard adds composite rectangles, which is CCSS 3.MD.7d ("Find areas of rectilinear figures by decomposing them into non-overlapping rectangles…"), cited nowhere in the gold. |
| 40 | 5.NR.2.2 → 5.NBT.6 | `state_subset` | `overlap` (R2 adopted) | The standard says "fluently divide"; 5.NBT.6 does not ask for fluency. |
| 41 | 1.NR.2.2 → 1.OA.1 | `split` | `overlap` | "Develop strategies … by exploring strings of related problems" is not in 1.OA.1. See item 2. |
| 42 | 3.MDR.5.2 → 3.MD.1 | `split` | `split`, or `overlap` if estimating to the quarter hour is a separate objective | Also changes worked example E12 if `overlap`. |
| 43 | 4.NR.4.2 → 3.NF.3d | `different_grade` | `exact` | `different_grade` was removed; worked example E7 already updated. |
| 44 | 3.PAR.3.2 → 3.OA.7 | `exact` | `state_subset` | 3.OA.7 asks students to "Fluently multiply and divide within 100" and to "know from memory all products of two one-digit numbers"; 3.PAR.3.2 asks them to represent the facts with strategies and explain the relationship between multiplication and division, not fluency (R2). No other grade-3 Georgia standard covers the fluency. |

## 5. Proposed rules (drafts for the annotators to approve)

Not in the guideline yet. Each gives the draft wording, where it goes, and the gold items it affects.

**R1. Required methods.** **Declined Oct 3, 2026:** a specific procedure such as "using the standard
algorithm" is in Test C's "Ignored" list, as in the gold (neither document defines it as a separate
expectation the way both define fluency). Items 17 and 18 stand as in the gold: 4.NR.2.1 → 4.NBT.4
stays `exact`, and 5.NR.2.1 → 5.NBT.5 stays `state_subset` for its bounds alone.

**R2. Fluency.** ~~Draft.~~ **Adopted Oct 3, 2026:** fluency is in Test C's "Matters" list, and the range of
a fluency expectation is a bound (Test D). Basis: both documents define fluency as its own expectation
(CCSS: "fast and accurate"; Georgia: choosing "flexibly among methods and strategies … accurately and
efficiently", "not … timed tests or speed"); "fluently" on both sides counts as the same expectation.
Other how-to qualifiers ("mentally", "using the standard algorithm") are explicitly ignored. The gold did not treat fluency as mattering (3.PAR.3.2 →
3.OA.7 is `exact` although only the CCSS code asks for fluency). Re-check of every gold row that
mentions fluency:

- **Unchanged:** K.NR.5.4, 2.NR.2.1, 2.NR.2.4, 3.PAR.2.1, 5.NR.2.1 (fluency on both sides; 5.NR.2.1 is
  already `state_subset` for its bounds). 4.NR.2.1 is unchanged by R2 (see item 17 for the standard
  algorithm).
- **1.NR.2.4 → 1.OA.6:** item 19 (`state_subset`, or `split` with 1.NR.2.2).
- **5.NR.2.2 → 5.NBT.6:** item 40 becomes `overlap` (Georgia adds fluency; 5.NBT.6 has divisors above 25).
- **3.PAR.3.2 → 3.OA.7:** item 44.

**R3. Practice standards.** *Section 3, state side, new paragraph:*
> Annotate content standards only. A state's own practice standards (e.g. Georgia K.MP.1–8 at each
> grade) are not annotated: they correspond to the CCSS Standards for Mathematical Practice, which are
> not in the K–5 content list.

The gold already does this (150 content standards, no MP standards); the guideline doesn't say so.

**R4. "Solve problems" vs. "solve word problems".** *Test C, replace the "general setting" item in the "Ignored" list
with:*
> A general setting ("in authentic problems", "to solve problems", "in real-world contexts") when
> problems are only the setting for another action (e.g. "fluently add and subtract within 1000 to
> solve problems": the action is fluent computation). When solving problems is the standard's main
> action, "solve problems" corresponds to CCSS "solve word problems".

Affects items 2 and 6 (1.OA.1, 2.OA.1).

## 6. Pending edits to the guideline

- **Step 6A, contrast example (4.G.1):** depends on item 4. If 4.GSR.8.1 becomes a `merge`, replace
  the example or reword it.
- ~~**Contrast example (3.GSR.6.1):** described as covering "only identifying".~~ Done: under the
  `overlap` rule the example now says it also adds solving problems and is `overlap` (item 37).
- **Step 6A, 4.NBT.2 example:** remove the note on the Georgia mapping once item 1 is re-adjudicated.
- ~~**Step 6B examples table and section 8, 3.NR.4.4:** say why the standard states 3.NF.3a's requirement.~~
  Done in version 1.2: E9 and the step 6B examples table now cite Georgia's guidance ("the same size or on
  the same location on a number line").
- **Section 8, E15 ("Ask questions…"):** depends on item 16. If those standards are remapped, replace
  E15 (the "general practice" rationale no longer holds) and remove its row from "Find your case". If
  they stay `none`, fix the wording: grade 1 (1.MDR.6.4) ends "…to compare and order whole numbers", so
  "at every grade K–5" needs "(grade 1 with a different ending)".
- **Section 8, E2 and E11:** depend on items 20 and 21.
- **Test C "Why" note on explaining and justifying:** acknowledge that CCSS weights justification
  heavily ("One hallmark of mathematical understanding is the ability to justify… why a particular
  mathematical statement is true", CCSS Introduction, "Understanding mathematics"), and
  say the rule is kept for agreement, with the difference recorded in the rationale.
- **Section 9, `rationale`:** for any match at another grade (`exact` now covers these, since
  `different_grade` was removed), say whether the state teaches the content earlier or later than CCSS. Teachers care about the direction.
- **Test B, "comparable level":** vague. A pointer to the CCSS Progressions would help, but section 2
  limits annotators to the provided materials; either add the Progressions to those materials or
  define "comparable level" in the guideline.
- **Step 6A, 4.NBT.2 example:** say that 4.NR.1.1 lacks 4.NBT.2's "number names" on purpose
  (Georgia's guidance: "Students are not expected to write numbers in word form"), and that this is
  allowed within a split.
- **Section 9 vs. the gold:** the guideline now has `split_with` and `merge_with` columns (needed
  because an `overlap` row may or may not help make up a split or merge); `gold.csv` has neither. Add
  them when the gold is re-adjudicated.
- **3.NR.1.1:** our files (`raw/standards/ga/georgia_math_3.json`, `states/ga/ga_input.json`, the gold)
  read "up to 10,000 **to the thousands** using base-ten numerals…"; the official standards PDF (p. 36)
  has no "to the thousands". The quote in step 6A (the 4.NBT.2 table) inherits it. Fix the source files, then the quote.
- **3.NR.1.3:** our files read "round whole numbers **within** up to 1000"; the PDF reads "up to 1000".
- Known transcription artifacts, already noted: K.NR.4.1 "0- 20" (official "0-20"); 5.MDR.7.2 missing its
  final period.
