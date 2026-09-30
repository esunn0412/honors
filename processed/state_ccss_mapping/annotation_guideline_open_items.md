# Open items: conflicts for re-adjudication and pending edits

*Companion to [`annotation_guideline.md`](annotation_guideline.md), version 1.2 (Sep 30, 2026). For the adjudication meeting only: it discusses specific answers in the adjudicated Georgia mapping, so don't give it to annotators or use it in calibration (guideline section 10). "Section" numbers below refer to the guideline.*

A check of the guideline against the adjudicated Georgia mapping (`states/ga/gold.json`) found the
cases below, where applying the guideline gives a different answer from the gold. The gold has **not**
been changed; each case is to be re-adjudicated, and either the gold or the guideline updated.

## 1. Split or subset (section 5.1)

| # | Georgia standard(s) | Gold | Guideline implies | Why |
|---|---|---|---|---|
| 1 | 3.NR.1.1, 3.NR.1.2 → 4.NBT.2 | `split` (with 4.NR.1.1, 4.NR.1.3) | `state_subset` | 4.NR.1.1 and 4.NR.1.3 together make up 4.NBT.2; the grade-3 standards cover the same parts with smaller numbers (the worked example in section 5.1). |
| 2 | 1.NR.2.1, 1.NR.2.2 → 1.OA.1 | `split` | 1.NR.2.1 `exact`; 1.NR.2.2 not a split partner | 1.OA.1 has one part, solving word problems within 20; its drawings and equations are an "e.g." (Test B). 1.NR.2.1 covers the whole code (its guidance lists all problem types). 1.NR.2.2's action, developing strategies, is 1.OA.6's. |
| 3 | 3.PAR.3.6, 3.PAR.3.7 → 3.OA.3 | `split` | no clear answer | Both solve multiplication and division problems within 100 and differ only in representations, which 3.OA.3 gives as an "e.g.". Each covers the whole code, so neither `split` (different parts) nor two `exact` fits. **Needs a ruling.** |

## 2. Merge or superset (section 5.2)

| # | Georgia standard | Gold | Guideline implies | Why |
|---|---|---|---|---|
| 4 | 4.GSR.8.1 → 4.G.1 | `exact` | `merge`: 4.G.1 + 4.G.3 | Its extra part, "draw … lines of symmetry", is 4.G.3's core requirement. Also the contrast example in section 5.1. |
| 5 | 3.NR.4.1 → 3.NF.1 | `state_superset` | `merge`: 3.NF.1 + 3.NF.2a + 3.NF.2b | Its extra part, "points on a number line, distances on a number line", is 3.NF.2a and 3.NF.2b's core requirement; it is a required "Use", not an "e.g.". |
| 6 | 2.NR.2.3 → 2.NBT.6 + 2.NBT.7 | `merge` | `merge`, citing 2.OA.1 | The text's core, solving addition and subtraction problems with two-digit numbers, is 2.OA.1's (cited nowhere in the gold; the Georgia guidance paraphrases it). 2.NBT.6 (up to four addends) and 2.NBT.7 (within 1000) rest on bounds from the guidance only (section 4.1). |
| 7 | 3.GSR.7.3 → 3.MD.7b + 3.MD.7c | `merge` | drop 3.MD.7c: 3.MD.7b `exact`, or `merge` with 3.MD.7a | The distributive property (3.MD.7c) appears only in a guidance example (section 4.1, Test A). "Discover … how area can be found by multiplying" matches 3.MD.7a's "show that the area is the same as would be found by multiplying". |
| 8 | 4.NR.4.6 → 4.NF.3c + 4.NF.3d | `merge` | drop 4.NF.3d; possibly 4.NF.3a + 4.NF.3c | Solving word problems (4.NF.3d's core) comes only from the guidance, which itself uses 4.NF.3a's wording ("joining and separating parts referring to the same whole"). |
| 9 | 4.GSR.7.1 → 4.MD.5b + 4.G.1 | `merge` | `state_subset` of 4.G.1 | 4.MD.5b ("an angle that turns through n one-degree angles…") is not stated and is close to a definition (Test D). The text restates only the first half of 4.MD.5's general statement, so "cite all lettered parts" does not apply. |
| 10 | K.NR.5.1 → K.OA.3 + K.OA.4 | `merge` | possibly `state_superset` of K.OA.3 | K.OA.4's core, finding the number that makes 10, is not stated; "compose numbers up to 10" is general. Borderline. |
| 11 | K.MDR.7.1 → K.MD.1 + K.MD.2 | `merge` | `merge`, adding 1.MD.1 | Its extra part, ordering objects, is 1.MD.1's first requirement (one grade away). Label unchanged. |
| 12 | 2.MDR.6.1 → 2.MD.7 | `state_superset` | possibly `merge`: 2.MD.7 + 3.MD.1 | Its extra part, measuring elapsed time, is 3.MD.1's "measure time intervals", with narrower bounds; the gold accepts the same narrowing for 3.MDR.5.3 in the 3.MD.1 split. **Needs a ruling** on how narrow an extra part may be. |
| 13 | 3.NR.4.3 → 3.NF.2a + 3.NF.2b + 3.NF.3c | `merge` | drop 3.NF.3c | The number line is supported by the guidance (an interpretation, section 4.1); "fractions greater than one" is not 3.NF.3c's "express whole numbers as fractions". |
| 14 | 2.GSR.7.1 → 2.G.1 | `state_superset` | unclear | It lacks 2.G.1's "draw" (a separate objective), so it does not fully match the code; it both adds and lacks, and step 6 decides by the more substantial difference. |
| 15 | 5.NR.3.4 → 4.NF.4b + 4.NF.4c | `merge` | consider 5.NF.4a, 5.NF.6 | Section 7 tie-break: prefer a same-grade code with the same requirement. 5.NF.4a and 5.NF.6 are cited nowhere in the gold. |

Items 4–7 are the clearest; items 10–15 are judgment calls.

## 3. From the educator review

A review of the guideline as a K–5 math educator would read it (checked against the CCSS text, the
CCSS Progressions and Georgia's guidance) found the cases below. Items 17–19 depend on the proposed
rules in part 4.

| # | Georgia standard(s) | Gold | Educator reading implies | Why |
|---|---|---|---|---|
| 16 | K.MDR.7.3, 1.MDR.6.4, 2.MDR.5.4, 3.MDR.5.1, 4.MDR.6.2, 5.MDR.7.2 ("Ask questions and answer them based on gathered information, observations, and appropriate graphical displays…") | `none` (also worked example E15) | at least grades 1–3: `state_subset` of the grade's data code (1.MD.4, 2.MD.10, 3.MD.3); K, 4 and 5 to be checked | These are Georgia's data standards (domain MDR), not general practices; Georgia has separate practice standards (K.MP.1–8 etc.). The Progressions describe 1.MD.4 in nearly Georgia's words: students "ask and answer questions about categorical data based on a representation of the data". 1.MDR.6.4's "compare and order whole numbers" matches 1.MD.4's "how many more or less". 1.MD.4, 2.MD.10 and 3.MD.3 are cited nowhere in the gold, so the mapping implies Georgia has no data standards in grades 1–3. **Strongest item from this review.** |
| 17 | 4.NR.2.1 → 4.NBT.4 | `exact` | `state_subset` (under R1) | 4.NBT.4 requires "using the standard algorithm"; 4.NR.2.1 instead says "using place value understanding, properties of operations, and relationships between operations". The standard algorithm is a required method, not an "e.g."; teachers treat it as its own objective, and Georgia's omission of it is deliberate. |
| 18 | 5.NR.2.1 → 5.NBT.5 | `state_subset` | label unchanged; add the reason | Its text also lacks "using the standard algorithm"; Georgia's guidance makes it optional ("Students may also use a standard algorithm…"). This adds to the narrower bounds already noted. |
| 19 | 1.NR.2.4 → 1.OA.6 | `exact` | `state_subset`, or `split` with 1.NR.2.2 (under R2) | 1.OA.6 requires adding and subtracting within 20 with strategies, and fluency within 10. 1.NR.2.4 covers fluency within 10 only (Test C); 1.NR.2.2 (strategies within 20) may cover the rest. Related to item 2. |
| 20 | K.NR.4.1 → K.CC.3 (worked example E2) | `exact` | contested: possibly `state_subset` | Kindergarten teachers treat writing numerals as its own skill (a fine-motor demand; often reported separately), and "Write numbers from 0 to 20" is its own sentence in K.CC.3. The current rule (receptive vs. productive form, Test B) is clear; the question is whether educators accept it. Classroom judgment, not a source finding. |
| 21 | 3.GSR.7.1 → 3.MD.5b + 3.MD.6 (worked example E11) | `merge` | contested: possibly add 3.MD.5a | 3.MD.5a and 3.MD.5b are both phrased as definitions ("is said to have"), and 3.GSR.7.1's "multiple copies of the same unit" arguably states 5a's unit. Either add 5a or explain in Test D why 5a is a definition and 5b is not. |

## 4. Proposed rules (drafts for the annotators to approve)

Not in the guideline yet. Each gives the draft wording, where it goes, and the gold items it affects.

**R1. Required methods.** *Test B table, left column (counts as a separate objective):*
> A specific procedure the standard requires, not as an example (e.g. "using the standard algorithm"
> in 4.NBT.4 and 5.NBT.5).

*And to the right-column row on methods, add:* "Broad families of methods ('strategies based on place
value, properties of operations, and/or the relationship between addition and subtraction') are not a
specific procedure." Without that limit, R1 would also affect standards such as 3.PAR.2.1 → 3.NBT.2,
whose CCSS text lists broad methods. Affects items 17 and 18.

**R2. Fluency.** *Test B table, left column:*
> Fluency ("fluently", "demonstrating fluency") as well as, or instead of, computing with strategies.

*And to Test C:* "The range of a fluency expectation is a bound (fluently within 10 vs. within 20)."
Affects item 19; the other fluency standards in the gold (K.NR.5.4, 2.NR.2.1, 2.NR.2.4, 3.PAR.2.1,
4.NR.2.1, 5.NR.2.1, 5.NR.2.2) should be re-checked against it.

**R3. Practice standards.** *Section 3, state side, new paragraph:*
> Annotate content standards only. A state's own practice standards (e.g. Georgia K.MP.1–8 at each
> grade) are not annotated: they correspond to the CCSS Standards for Mathematical Practice, which are
> not in the K–5 content list.

The gold already does this (150 content standards, no MP standards); the guideline doesn't say so.

**R4. "Solve problems" vs. "solve word problems".** *Test B table, right column, replace the "general
setting" row with:*
> A general setting ("in authentic problems", "to solve problems", "in real-world contexts") when
> problems are only the setting for another action (e.g. "fluently add and subtract within 1000 to
> solve problems": the action is fluent computation). When solving problems is the standard's main
> action, "solve problems" corresponds to CCSS "solve word problems".

Affects items 2 and 6 (1.OA.1, 2.OA.1).

## 5. Pending edits to the guideline

- **Section 5.1, contrast example (4.G.1):** depends on item 4. If 4.GSR.8.1 becomes a `merge`, replace
  the example or reword it.
- **Section 5.1, contrast example:** 3.GSR.6.1 is described as covering "only identifying"; its text also
  asks students to "solve problems involving" those figures. Reword; the label is unaffected.
- **Section 5.1, 4.NBT.2 example:** remove the note on the Georgia mapping once item 1 is re-adjudicated.
- ~~**Section 5.2 and section 8, 3.NR.4.4:** say why the standard states 3.NF.3a's requirement.~~
  Done in version 1.2: E9 and the section 5.2 table now cite Georgia's guidance ("the same size or on
  the same location on a number line").
- **Section 8, E15 ("Ask questions…"):** depends on item 16. If those standards are remapped, replace
  E15 (the "general practice" rationale no longer holds) and remove its row from "Find your case". If
  they stay `none`, fix the wording: grade 1 (1.MDR.6.4) ends "…to compare and order whole numbers", so
  "at every grade K–5" needs "(grade 1 with a different ending)".
- **Section 8, E2 and E11:** depend on items 20 and 21.
- **Test B "Why" note on explaining and justifying:** acknowledge that CCSS weights justification
  heavily ("One hallmark of mathematical understanding is the ability to justify… why a particular
  mathematical statement is true", CCSS Introduction, "Understanding mathematics"), and
  say the rule is kept for agreement, with the difference recorded in the rationale.
- **Section 9, `rationale`:** for `different_grade`, and for any match at another grade, say whether the
  state teaches the content earlier or later than CCSS. Teachers care about the direction.
- **Test D, "comparable level":** vague. A pointer to the CCSS Progressions would help, but section 2
  limits annotators to the provided materials; either add the Progressions to those materials or
  define "comparable level" in the guideline.
- **Section 5.1, 4.NBT.2 example:** say that 4.NR.1.1 lacks 4.NBT.2's "number names" on purpose
  (Georgia's guidance: "Students are not expected to write numbers in word form"), and that this is
  allowed within a split.
- **Section 9 vs. the gold:** the gold has no `split_with` field; add it, or derive it from shared codes.

## 6. Source-text errors (in our Georgia files, not in the guideline)

- **3.NR.1.1:** our files (`raw/standards/ga/georgia_math_3.json`, `states/ga/ga_input.json`, the gold)
  read "up to 10,000 **to the thousands** using base-ten numerals…"; the official standards PDF (p. 36)
  has no "to the thousands". The quote in section 5.1 inherits it. Fix the source files, then the quote.
- **3.NR.1.3:** our files read "round whole numbers **within** up to 1000"; the PDF reads "up to 1000".
- Known transcription artifacts, already noted: K.NR.4.1 "0- 20" (official "0-20"); 5.MDR.7.2 missing its
  final period.
