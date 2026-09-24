# What kinds of questions do K-5 math tests ask?

**Georgia Milestones and i-Ready, compared with the MathFish dataset**

This folder answers the meeting to-do:

> The question output is not aligned with i-Ready. Compile a comprehensive list of the
> different types of question for each grade (i-Ready, Milestones), categorize them, with
> separate categories for multimodal. Find legitimate free sample tests.

**Contents**

1. [Review the questions yourself](#1-review-the-questions-yourself)
2. [Summary](#2-summary)
3. [What we collected and what we did, source by source](#3-what-we-collected-and-what-we-did-source-by-source)
4. [The question-type categories](#4-the-question-type-categories)
5. [Findings](#5-findings)
6. [How the questions, pictures and answers were extracted](#6-how-the-questions-pictures-and-answers-were-extracted)
7. [Sources: links to every file](#7-sources-links-to-every-file)
8. [How it was built, reliability, limitations](#8-how-it-was-built-reliability-limitations)
9. [Next steps / questions for Dr. Choi](#9-next-steps--questions-for-dr-choi)
10. [Full tables](#10-full-tables)

---

## 1. Review the questions yourself

Open **`review/index.html`** in a browser: double-click it, or run `open review/index.html`.
Every item from all three sources is on one page, **extracted as text** (question, answer
choices, parts), with its **figures as separate images** and its **answer**:

| Source | What you see for each item | Answer shown |
|---|---|---|
| Milestones | Question text, lettered choices (text or picture), figures, "[answer space]" markers | GaDOE's key + explanation of every choice; full-credit exemplar for written items |
| i-Ready Diagnostic samples | Hand transcription of the question and choices, the diagram cut out of the screenshot, how the student answers (click, type, tool) | Worked out by us (i-Ready publishes no key), labeled as such |
| i-Ready practice problems | One card per numbered problem: the worksheet title and page instruction, then the problem as text with its pictures | The teacher packet's answer, highlighted in place |
| MathFish | The publisher's own formatted page (paragraphs, numbered lists, tables) with its images | None: the publishers keep solutions behind a teacher login |

Every card also has **Show original page**, so you can check the extraction against the
source.

Using the page:

- **Filter** by source, grade, Common Core domain, question type, answer mode used in any
  part, stimulus, or search text (e.g. `3.NF.2`, `number line`). "Only items with an answer"
  hides MathFish.
- **Link to a view:** add filters to the address, e.g.
  `index.html?source=milestones&grade=4&type=multi_part`.
- **Check and correct the labels.** All labels except the i-Ready Diagnostic ones come from
  rules, and **this page is where a person validates them.** Each card has:
  - a **Question type** menu and a **Stimulus** menu. The first entry is the rule's label;
    pick another entry to correct it.
  - a **Part modes** box for multi-part questions, e.g. `enter, write`.
  - **Labels are correct**, to mark a card as checked with no change.
  - a note box and a **Flag** button.
- **Corrections take effect immediately** in the filters and chips, so you can re-count by
  filtering.
- **Where your review is kept:** in your browser. **Export my review (CSV)** downloads it,
  so the corrections can be fed back in.
- **Math symbols** render through KaTeX, which loads from the internet. Offline, the formulas
  show as raw LaTeX.

To rebuild the page after re-running the pipeline: `python3 scripts/build_review.py`.

---

## 2. Summary

Every question is coded on three dimensions: **answer mode** (select one, select many,
enter, write, construct, match, drop-down), **structure** (single or multi-part), and
**stimulus** (none, table, diagram, illustration, interactive). See §4.

These labels are a rule-based first pass, to be checked by hand in the review page (§1).
Treat the percentages as provisional until then.

- **The real tests are mostly "select one".**
  - Milestones: 67% select one, 2% select many, 9% write, **21% multi-part**.
  - i-Ready Diagnostic samples: 7 of 10 select one.
- **Multi-part is the tests' second format.** Milestones multi-part items are all
  technology-enhanced or constructed-response. Their parts are usually *enter → write*
  (solve, then explain) or two *select one* parts.
- **MathFish is almost never "select" (6% of problems have any select part).**
  - It's lesson material: 37% multi-part (mostly chains of *enter* and *write* prompts), 27%
    open activities, 15% write, 14% enter.
  - It covers the standards well, but its question *formats* look nothing like the tests.
- **i-Ready practice worksheets are drills:** 91% of their 1,213 problems are *enter*.
- **Nearly every picture on the tests is a diagram a program could draw.**
  - Milestones: 56% no picture, 6% a table, 36% a diagram (number line, fraction model,
    shape, grid, graph).
  - Only 3 of 123 items need a real illustration.
- **i-Ready's distinctive feature is interaction.** 8 of its 10 samples are answered with an
  on-screen tool: ruler, protractor, counters, click-to-plot.

---

## 3. What we collected and what we did, source by source

### 3.1 Georgia Milestones

**The files:** six official GaDOE PDFs for grades 3-5, one of each per grade:

- **Study/Resource Guide for Students and Parents:** sample items grouped by unit.
- **Assessment Guide:** example items for each DOK level, plus a set of practice items.

They are the 2016-2017 editions. Newer ones aren't available as files: GaDOE's portal only
works in a browser, and the current practice tests are an interactive test player.

**What's in them:** 132 math sample items. 9 appear in both guides of the same grade,
leaving **123 unique items**. For every item GaDOE prints:

| Label | Values | Example |
|---|---|---|
| Item type | Selected-Response (4 options), Technology-Enhanced (multi-select "Select TWO/THREE" and/or two-part Part A/Part B), Constructed-Response (2 points), Extended Constructed-Response (4 points) | "Technology-Enhanced: 2 points" |
| DOK level | 1, 2 or 3 | "DOK Level 2" |
| Standard | Old Georgia code, which uses Common Core numbering | `MGSE3.OA.4` = Common Core `3.OA.4` |
| Answer + rationale | Correct answer, and why each wrong answer is wrong | "Choice (B) is incorrect because it shows rounding to the nearest ten" |

**Milestones item types (GaDOE's labels), 123 unique items:**

| GaDOE item type | Points | What the student does | Items | Example |
|---|---|---|---|---|
| Selected-Response | 1 | Choose one of 4 answer choices | 83 | "What is 738 rounded to the nearest hundred? A. 700 B. 730 C. 740 D. 800" |
| Technology-Enhanced, multi-select | 2 | Choose 2-3 correct answers out of 5-6 | 3 | "Select THREE colors of paper that each have an area of 36 square inches." |
| Technology-Enhanced, multi-part with a multi-select part | 2 | Part A multi-select, Part B one choice | 3 | "Part A: Select TWO equations that are missing the same number… Part B: How many friends shared this bag?" |
| Technology-Enhanced, multi-part (single choices) | 2 | Part A and Part B, one choice each | 3 | "Part A: What will be the length of the new park? Part B: What is the perimeter of the old park?" |
| Constructed-Response | 2 | Write an answer and/or explanation, scored with a rubric | 19 | "Part A: Solve. 571 − 324 = ☐  Part B: Explain the strategy you used." |
| Extended Constructed-Response | 4 | Longer multi-part written response, scored with a rubric | 12 | "Part A: Write a story problem for 32 ÷ ☐ = 8. Part B: Solve it. Part C: Circle groups of dots…" |
| **Total** | | | **123** | |

- **Where the label comes from:** it's printed on the line under each item's heading
  ("Item 9 / Technology-Enhanced"; "Selected-Response: 1 point"). Point values are printed
  in the assessment guides.
- **Technology-enhanced subtypes:** GaDOE defines math technology-enhanced items as exactly
  two kinds, "a multiple-select item and a multiple-part item" (assessment guides, "Item
  Types" section).
  - The study guides print only "Technology-Enhanced", so I split the 9 items by reading
    them: 3 multi-select, 6 multi-part (3 of which include a multi-select part).
  - The grade 5 assessment guide does print the subtypes. Its three technology-enhanced items
    are duplicates of grade 5 study-guide items, and its labels (Multi-Select; Multi-Part
    Multi-Select; Multi-Part) match my split.
- **Despite the name,** the 2016-2017 technology-enhanced math items are still choose-from-a-list
  items, just multi-select or two-part. No drag-and-drop or graphing appears in these guides.

**What we did:**

1. **Parsed the PDFs** (`scripts/build_milestones.py`). For each item it pulls the text,
   GaDOE's item type, DOK, standard and answer key. Example items print these next to the
   item; the other items get them from the answer-key table at the end of the section.
2. **Kept the standard as Common Core** (`MGSE3.OA.4` → `3.OA.4`). As extra information
   only, each item also carries its current Georgia code (`ga_codes`) from
   `mapping_final.json`, since this is Georgia's own test.
3. **Coded the pictures by hand.** I looked at every item page and recorded its picture type:
   number line, fraction model, clock, shape, table, … Saved in `data/milestones_visuals.json`.
4. **Extracted every item as structured content** (`scripts/extract_milestones_structured.py`,
   see §6): question text, lettered answer choices, figures cropped on their own, inline
   answer boxes (☐), fractions (`3/4`) and answer spaces. Output:
   `data/milestones_structured.json`.
5. **Extracted GaDOE's answers** (`scripts/extract_milestones_answers.py`): the key and
   explanation for every item, and the full-credit exemplar for written items. Output:
   `data/milestones_answers.json`.

**What we got:**

- The official format mix: 83 select one, 3 select many, 11 write, 26 multi-part (§10.2 lists
  what the parts are).
- Error-based wrong answers with a stated reason for each: a model for generating
  distractors.
- A frequency list of the diagrams the test uses, i.e. what a drawing library must cover.
- **Answers for all 132 items:**
  - multiple-choice keys with GaDOE's explanation of why each wrong choice is wrong;
  - two-part keys (e.g. "Part A: C/F, Part B: B");
  - the scored exemplar responses (4/3/2/1/0 points) for written items.
- **Extraction check:** 131 of 132 items extract cleanly. The one that doesn't (grade 5
  assessment guide item 1, whose answer choices are drawn tables) is flagged in the review
  page with the original shown.

### 3.2 i-Ready

i-Ready's Diagnostic is a closed, adaptive test. Only two kinds of material are public.

**(a) Diagnostic sample items.** Two PDFs from Curriculum Associates, each page a screenshot
of one item.

- **13 math items**, 3 of them grade-8 content (dropped), leaving **10 for K-5**.
- **What they show:** the formats and tools the Diagnostic uses:

| Format / tool | Example in the samples |
|---|---|
| Multiple choice (sometimes picture answers) | "Matt has 8 balloons. He gives 4 to a friend. Which number sentence…?" |
| Short answer (type in a box) | "How many more inches of ribbon does she need?" |
| Click on a number line | "Click on the number line to show ½." |
| Drop-down menu | shown only in a grade-8 sample |
| Drag and drop | shown only in a reading sample |
| On-screen tools | ruler, protractor, base-ten blocks, hundred chart, unit squares, counters/ten-frame, calculator |

**(b) At-Home Activity Packets (2020), K-5.** Free printable packets of **129 worksheets**
("Fluency and Skills Practice") from i-Ready's classroom lessons. They are practice material,
not the Diagnostic test.

**What we did:**

- **Coded by hand from the page images** (`scripts/build_iready.py`): for each sample item
  and worksheet, the answer mode and the picture kinds.
- **Transcribed the 10 Diagnostic samples** (`scripts/extract_iready_diagnostic.py`). These
  PDFs are screenshots with no text in them, so the questions were typed in by hand and only
  the diagram was cut out.
  - **Answers are ours**, since i-Ready publishes none. 8 are worked out or measured from the
    picture. 2 are left blank because the screenshot doesn't show enough (the paintbrush
    ruler and a partly covered area figure).
- **Extracted the 129 worksheets as problems** (`scripts/extract_iready_structured.py`).
  These PDFs do contain text.
  - **1,176 numbered problems**, with their pictures cropped from the student packet.
  - **Answers** come from Curriculum Associates' free teacher packets, which are the same
    pages with answers printed in blue. Student and teacher packets for every grade are
    linked from the [At-Home Resources: Mathematics](https://www.curriculumassociates.com/summer-learning-support/at-home-resources-mathematics)
    page. 1,098 problems have a written answer; the rest are
    worked examples or have answers that are drawn (circling, shading).
- **Assigned Common Core standards.** i-Ready prints none, so I chose them from the content
  (i-Ready is built on Common Core). They're marked `standard_source: "assigned"`; you can
  check them in the review page.
- **Saved every page as an image** (`scripts/extract_iready_images.py`), 184 pages, for the
  review page's "Show original". Kindergarten pages are printed sideways and were rotated
  upright.

**What we got:**

- The list of **interactive formats and tools** that Milestones doesn't show.
- **Counted per problem:** each numbered problem is one question (1,176 problems), and a page
  with no numbered problems counts as one question (29 Kindergarten pages and 8 others),
  giving **1,213**.
- 91% are *enter* (numeric drills); 6% are *write*, usually the "explain your strategy"
  question that ends a worksheet.
- Kindergarten pages mix in circling, matching and drawing.
- **Limit:** 10 samples show *which* formats exist, not how often each is used.

### 3.3 MathFish

**The data:** a research dataset (Li et al., EMNLP 2024) of 21,776 K-12 problems from two
free curricula, **Illustrative Mathematics (IM)** and **Fishtank Learning (FL)**. Each problem
is labeled by the publisher with Common Core standards.

**What we did:**

1. **Kept K-5** (`scripts/build_mathfish.py`): problems whose main standards are all K-5.
   That's **4,428** problems.

   | Kind | Count |
   |---|---|
   | IM lesson activities | 2,448 |
   | IM centers (games) | 667 |
   | IM tasks | 402 |
   | IM practice problems | 147 |
   | Fishtank anchor tasks | 383 |
   | Fishtank target tasks (exit tickets) | 381 |

   By grade: K 567, 1st 669, 2nd 616, 3rd 850, 4th 861, 5th 865.

2. **Kept the standards as Common Core**, exactly as the publishers labeled them. No
   conversion to Georgia codes.
3. **Kept only what students see.** IM lessons include long teacher notes; only the "Student
   Facing" part is used. Lessons with no student part (teacher-led number talks) are marked
   as open activities.
4. **Tagged every problem with the same categories as the tests**
   (`scripts/tag_question_types.py`). 4,428 is too many to label by hand, so text rules give
   a first pass: numbered list items or "Problem 1 / Problem 2" make it multi-part, "Explain…"
   means *write*, lettered options mean *select one*, "Select all" means *select many*, and
   so on. The labels are checked by hand in the review page (§8).
5. **Downloaded MathFish's images** (4,869 files for the K-5 problems) so the review page can
   show them.
6. **Used the publisher's own HTML for display** (`scripts/mathfish_html.py`). MathFish's
   `text` field is flattened: every fraction and list item lands on its own line. Each record
   also keeps the original page HTML, which has real paragraphs, numbered lists and tables.
   - The cleaner keeps only the student-facing part and removes icons and buttons.
   - It swaps the expired image links for the local image files.
   - It works for 4,400 of the 4,428 problems; the other 28 fall back to the plain text.

**What we got:**

- A large pool of **standard-labeled K-5 content** (contexts, numbers, representations)
  covering every grade.
- Its formats are curriculum formats, not test formats, so it would need converting before
  it could serve as test-style items.
- **No answers.** Only 6 of the 4,428 K-5 problems include a visible solution. Illustrative
  Mathematics and Fishtank publish their student responses only to logged-in teachers
  ("Create a free account or sign in to view Student Response"), and the dataset didn't
  include them.

---

## 4. The question-type categories

Full definitions and rules: [`CODEBOOK.md`](CODEBOOK.md). Each question is coded on **three
separate dimensions**, so the categories don't overlap.

**1. Answer mode: what the student does to answer**

| Code | Answer mode | Example | Seen on |
|---|---|---|---|
| `select_one` | Select one | "What is 738 rounded to the nearest hundred? A. 700 B. 730 …" | Milestones, i-Ready |
| `select_many` | Select many | "Select **TWO** equations that are missing the same number." | Milestones |
| `enter` | Enter a number / expression | "Type the answer in the box: ___ inches" | i-Ready, worksheets, Milestones parts |
| `write` | Write an explanation | "Explain the strategy you used." | Milestones (2 or 4 points) |
| `construct` | Construct: plot, shade, draw | "Click on the number line to show ½." | i-Ready |
| `match` | Match / order / sort | "Draw lines to match the numbers." | i-Ready, K worksheets |
| `dropdown` | Drop-down | a menu inside a sentence | i-Ready (grade-8 sample only) |

`open` (MathFish only) marks games, centers and teacher-led routines. These have no
scorable answer, so they fall **outside** the scheme and are reported separately.

**2. Structure: one question or several parts**

- `single`: one question.
- `multi_part`: two or more parts answered separately. This includes explicit parts (Part A /
  Part B, a. / b.) and **item sets** (several questions on one shared situation).
- Each part keeps its own answer mode, in order (`part_modes`), e.g. Milestones *enter →
  write* = "Part A: solve. Part B: explain."
- A list of exercises under one prompt ("Find each value: a. 3 × 10 b. 3 × 20") is a
  single question.

The main tables use **question type** = the answer mode of a single question, or
"multi-part".

**3. Stimulus: what the student looks at (the multimodal question)**

| Stimulus | Meaning | Can we generate it? |
|---|---|---|
| None | Text only | Yes, the LLM writes it |
| Table | Text or numbers in cells | Yes, as Markdown/HTML |
| Diagram | Number line, fraction model, clock, shape, grid, graph, base-ten blocks … | Yes, render with code (SVG/matplotlib) from parameters |
| Illustration / photo | Real objects (nails, bottle caps, a fish to measure) | Hard: needs image generation or an image library |
| Interactive tool | Student answers by using an on-screen ruler, protractor, counters | Needs a front-end widget, not just an image |

A table whose cells contain pictures (e.g. shapes to classify) counts as the picture, not
as a table.

**Not used to categorize:**

- **Difficulty (DOK).** Only Milestones prints it, so it can't be compared across sources.
  It is kept as GaDOE's label for reference.
- **Context** (word problem vs. bare numbers). This coding was dropped.

---

## 5. Findings

Domains below are **Common Core domains**: CC Counting & Cardinality (K only), OA Operations &
Algebraic Thinking, NBT Number & Operations in Base Ten, NF Fractions, MD Measurement & Data,
G Geometry.

All numbers come from the rule-based first-pass labels (see §8) and will change as the
labels are checked in the review page.

### 5.1 Question type by source

| Question type | Milestones (gr 3-5) | i-Ready Diagnostic samples | i-Ready practice problems | MathFish (K-5) |
|---|---|---|---|---|
| Select one | **67%** | **7 of 10** | <1% | 4% |
| Select many | 2% | · | <1% | <1% |
| Enter | · | 2 of 10 | **91%** | 14% |
| Write | 9% | · | 6% | 15% |
| Construct | · | 1 of 10 | 2% | 1% |
| Match / order / sort | · | · | <1% | <1% |
| **Multi-part** | **21%** | · | · | **37%** |
| Open activity (outside the scheme) | · | · | · | 27% |
| **Number of questions** | 123 | 10 | 1,213 | 4,428 |

- **Fair comparison (grades 3-5 only, since Milestones starts at grade 3):** MathFish is 2%
  select one, and only 4% of its problems have a select part anywhere. 48% ask for a written
  explanation somewhere.
- **Even MathFish's most test-like parts don't match.** Fishtank exit tickets and IM practice
  problems (grades 3-5) have a select part in only 4-5% of problems.
- **Milestones multi-part items** (26) are all technology-enhanced (6) or constructed-response
  (20). Counting their parts, 23% of Milestones items ask for writing somewhere and 16% ask
  the student to enter a number.

### 5.2 What the multi-part questions are made of

| | Milestones | MathFish |
|---|---|---|
| Multi-part questions | 26 of 123 | 1,660 of 4,428 |
| Parts per question | mostly 2 (15) or 3 (8) | 2-5 usually; 424 have 6+ (long IM activities) |
| Most common part sequences | enter → write (4); enter → enter (3); select one → select one (3); enter → enter → write (3) | enter → enter (143); enter → enter → enter (117); write → write (95) |

The test's multi-part items are short and structured (2-3 parts, often ending in an
explanation). MathFish's are longer chains of prompts.

### 5.3 By grade

| | K | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **MathFish:** open activity | 61% | 36% | 29% | 19% | 16% | 15% |
| **MathFish:** multi-part | 5% | 18% | 36% | 42% | 55% | 53% |
| **MathFish:** asks for writing in any part | 10% | 29% | 31% | 42% | 51% | 51% |
| **i-Ready practice:** enter | 62% | 94% | 95% | 89% | 89% | 92% |
| **Milestones:** select one | — | — | — | 70% | 65% | 68% |
| **Milestones:** multi-part | — | — | — | 19% | 18% | 28% |

- **MathFish shifts with grade.** Kindergarten is mostly games and hands-on activities; by
  grade 4-5 over half the problems are multi-part and ask for an explanation.
- **Milestones is steady across grades 3-5:** about two-thirds select one and a fifth
  multi-part; grade 5 has the most multi-part items.

### 5.4 By domain

| Domain | Milestones: select one | Milestones: multi-part | Milestones: diagram | MathFish: writing in any part | MathFish: construct in any part | MathFish: open activity |
|---|---|---|---|---|---|---|
| CC (K only) | — | — | — | 10% | 1% | 68% |
| OA | 56% | **40%** | 8% | 38% | 4% | 25% |
| NBT | 70% | 19% | 15% | 40% | 4% | 24% |
| NF | 67% | 19% | 41% | **54%** | 13% | 13% |
| MD | 69% | 14% | **59%** | 38% | 8% | 21% |
| G | 80% | 13% | **67%** | 28% | **19%** | 42% |

- **Milestones:** multi-part items cluster in OA (10 of 25 OA items). Measurement and
  geometry items are mostly *select one about a picture*.
- **MathFish:** fractions are the most explanation-heavy; geometry has the most drawing tasks.
- **Per-standard breakdown** (e.g. which `3.OA.x` standards lean toward which type):
  `tables/standard_by_type.csv` and §10.5.

### 5.5 Stimulus (pictures)

| Stimulus | Milestones | i-Ready Diagnostic | i-Ready practice problems | MathFish |
|---|---|---|---|---|
| None | 56% | · | 65% | 53% |
| Table | 6% | · | <1% | 4% |
| Diagram | 36% | 2 of 10 | 14% | 22% |
| Illustration / photo | 2% | · | <1% | not measured* |
| Interactive tool | · | **8 of 10** | · | · |
| Image, kind unknown | · | · | 19%* | 21%* |

\*"Kind unknown" = a picture is present, but the text doesn't say what it is. For i-Ready
practice, the worksheet's hand-coded kinds didn't include a diagram and the problem text names
none. MathFish images weren't coded one by one; a spot check of 32 found about 4 in 5 were
ordinary diagrams. The review page's Stimulus menu is where these get fixed.

**Most common diagrams on Milestones** (what to build first):

- geometry figures (9), fraction models (7)
- number lines, area grids, coordinate grids, line plots (4 each)
- rulers (3)
- clocks, picture graphs, decimal grids, 3-D solids (2 each)

Diagrams appear in 59-67% of measurement and geometry items, but only 8-15% of OA and NBT
items.

### 5.6 What this means for our question generator

- **Formats to support:**
  - select one (4 options) with error-based wrong answers (model: the Milestones
    rationales)
  - select many (choose 2-3 of 5-6)
  - multi-part items, mostly two or three parts (enter → write; select → select)
  - enter a number
  - write an explanation, with a rubric
  - for i-Ready alignment: construct (number-line plotting) and drop-down
- **Use MathFish for content, not format:** convert its standard-labeled problems into the
  formats above.
- **Pictures:** a library of code-drawn diagrams covers nearly all grade 3-5 test items;
  start with the list in §5.5.

---

## 6. How the questions, pictures and answers were extracted

### Why not the same tool as the Georgia guidance diagrams?

- The Georgia guidance documents **embed** their diagrams as image objects. `pdfimages`
  pulls those out directly, and that's how `processed/standards/diagrams/` was made.
- The Milestones guides **draw** their figures as vector graphics: lines, rectangles and
  curves, with no image objects. `pdfimages -list` finds nothing in them.
- Plain text extraction only picks up the stray labels inside a drawing. A number-line
  question comes out as `0 R 1`, with no line, no tick marks, and no position for R.

### Milestones: text + separate figures (`extract_milestones_structured.py`)

[PyMuPDF](https://pymupdf.readthedocs.io/) reads the PDF's drawing commands
(`page.get_drawings()`), which give the exact position of every line and shape. For each item:

1. **Collect the words and drawings** in the item's region, from its "Item N" heading to the
   next heading. Items that continue onto a second page are followed.
2. **Rebuild fractions.** A fraction is drawn as a short line with a number above and below
   it; these become text such as `2/3`.
3. **Group the remaining drawings and classify each group:**

   | Group | Becomes |
   |---|---|
   | Small box inside a sentence | `☐` in the text (e.g. `54 ÷ ☐ = 9`) |
   | Ruled lines or a lined box | `[answer space]` |
   | Invisible white backgrounds, page rules | ignored |
   | Anything else | a **figure**: cropped from the page, with the labels printed inside it, and saved as its own PNG |

4. **Assemble the question.**
   - Words outside figures become the question text, in reading order.
   - Lines starting "A." … "F." become answer choices.
   - A choice letter with a picture beside it becomes a picture choice.
   - Exponents (`10^5`) and decimals are rejoined.
5. **Quality check.** An item is flagged if its choice letters are out of order or a choice
   came out empty. 1 of 132 is flagged; the review page shows it with a warning and the
   original.

### Milestones answers (`extract_milestones_answers.py`)

- **Example items:** "Correct Answer" and "Explanation of Correct Answer", printed right
  after the item.
- **Sample items:** the "Additional Sample Item Keys" table. Its rows are vertically centred
  and explanations wrap, so it's read by word position (column x-ranges), and each
  explanation is split at its opening phrase ("The correct answer is…").
- **Written items:** the "Exemplar Response" table (score points 4/3/2/1/0 and the sample
  answer for each).

### i-Ready worksheets (`extract_iready_structured.py`)

- **Text** is real text in these PDFs. Math symbols use a symbol font where `1 2 3 4 5 , .`
  stand for `+ − × ÷ = < >`; these are mapped back.
- **Problems:** problem numbers are white digits in black boxes, and every word and picture
  is assigned to the nearest problem number above-left of it.
- **Answers** are the blue text in the teacher packet (same pages). An answer printed on an
  answer line is placed on that line, and stacked answer boxes become one fraction.
- **Figures** are cropped from the student packet, so no answers are drawn into them.

### i-Ready Diagnostic samples (`extract_iready_diagnostic.py`)

The PDFs are screenshots of the online test, so there is no text to extract. The 10 items
were transcribed by hand, and each diagram was cropped from the screenshot at recorded
coordinates.

### MathFish (`mathfish_html.py`)

The images are separate files in the dataset, and the publisher's HTML supplies the layout
(see §3.3).

## 7. Sources: links to every file

Every source is **free and public**: no login or payment. Click to get the exact file used;
local copies are in `raw/`.

### Georgia Milestones (grades 3-5)

**Why these files, and why they're from 2016-2017.**

- **GaDOE's current guides aren't downloadable.** The Milestones page
  ([gadoe.org › Georgia Milestones](https://gadoe.org/assessment-accountability/georgia-milestones/))
  sends you to GaDOE's "Inspire" portal. That portal is a JavaScript app that works only in a
  browser, and its file server (`lor2.gadoe.org`) returned a web page instead of the PDF when
  I tried to download one directly.
- **The current practice tests are interactive only.** They run in the DRC test player
  ([gaexperienceonline.com](https://www.gaexperienceonline.com/)), with no PDF to download.
- **The downloadable copies are older.** The copies schools post publicly are the 2016-2017
  GaDOE editions. They were written for the old Georgia standards, before the 2023 math
  standards.
- **Newer copies may exist on some school's site;** I didn't find any.

**Where each file came from:**

- **Study guides:** posted by **Fair Oaks Elementary (Cobb County)** on its
  [Parent Resources page](https://www.cobbk12.org/fairoaks/parent-resources). The page links
  to `media.cobbk12.org/…/fgg/2411/Grade N Milestone Study Guide-1.pdf`; I downloaded the
  same files from the Cobb storage mirror (`sbcobbstor.blob.core.windows.net`, same path).
- **Assessment guides:** other Cobb and DeKalb school file servers, found by web search.

| Document | Grade | Year | Link | Local file |
|---|---|---|---|---|
| EOG Study/Resource Guide | 3 | 2017 | [PDF (Fair Oaks ES, Cobb)](https://sbcobbstor.blob.core.windows.net/media/WWWCobb/fgg/2411/Grade%203%20Milestone%20Study%20Guide-1.pdf) | `raw/milestones/cobb_g3_study_guide.pdf` |
| EOG Study/Resource Guide | 4 | 2017 | [PDF (Fair Oaks ES, Cobb)](https://sbcobbstor.blob.core.windows.net/media/WWWCobb/fgg/2411/Grade%204%20Milestone%20Study%20Guide-1.pdf) | `raw/milestones/cobb_g4_study_guide.pdf` |
| EOG Study/Resource Guide | 5 | 2017 | [PDF (Fair Oaks ES, Cobb)](https://sbcobbstor.blob.core.windows.net/media/WWWCobb/fgg/2411/Grade%205%20Milestone%20Study%20Guide-1.pdf) | `raw/milestones/cobb_g5_study_guide.pdf` |
| EOG Assessment Guide | 3 | 2016 | [PDF (DeKalb County, Cedar Grove ES)](https://cedargrovees.dekalb.k12.ga.us/Downloads/Grade%203%20Assessment%20Guide.pdf) | `raw/milestones/dekalb_g3_assessment_guide.pdf` |
| EOG Assessment Guide | 4 | 2017 | [PDF (Cobb County school file server)](https://media.cobbk12.org/media/WWWCobb/frf/3552/Grade-4_Assessment%20Guide.pdf) | `raw/milestones/cobb_g4_assessment_guide.pdf` |
| EOG Assessment Guide | 5 | 2017 | [PDF (Cobb County school file server)](https://media.cobbk12.org/media/WWWCobb/frf/3552/Grade-5%20Assessment%20Guide.pdf) | `raw/milestones/cobb_g5_assessment_guide.pdf` |
| Experience Online user guide (how to open the *current* practice tests) | 3-8 | 2023-24 | [PDF (DRC)](http://assets.drcedirect.com/States/GA/Experience/UserGuide.pdf) | `raw/milestones/experience_online_user_guide_2023-24.pdf` |

Current online practice tests: [gaexperienceonline.com](https://www.gaexperienceonline.com/)
(Chrome, no login; interactive only).

### i-Ready (Curriculum Associates)

| Document | Link | Local file |
|---|---|---|
| Diagnostic sample items page (starting point) | [curriculumassociates.com › Diagnostic sample items](https://www.curriculumassociates.com/reviews/assessment/diagnostic-sample-items) | — |
| "Sample Items: Item Types" | [PDF](https://cdn.bfldr.com/LS6J0F7/at/2r35hjbf2vjnn4xbvbtwmvw/Sample_Items_Item_Types_1.pdf) | `raw/iready/iready_item_types.pdf` |
| "Sample Items: Math Tools" | [PDF](https://cdn.bfldr.com/LS6J0F7/at/g5ppsbkw934jqt3wtqsgb/Sample_Items_Math_Tools.pdf) | `raw/iready/iready_math_tools.pdf` |
| **At-Home Activity Packets, all grades: student and teacher (answer-key) versions** | [curriculumassociates.com › At-Home Resources: Mathematics](https://www.curriculumassociates.com/summer-learning-support/at-home-resources-mathematics) (the source page; every packet link below is on it) | — |
| Student packet, Kindergarten (2020) | [PDF](https://capubstore.blob.core.windows.net/athomepdfs/iready-at-home-activity-packets-student-math-grade-k-2020.pdf) | `raw/iready/iready_athome_practice_grade_k.pdf` |
| Student packet, Grade 1 | [PDF](https://capubstore.blob.core.windows.net/athomepdfs/iready-at-home-activity-packets-student-math-grade-1-2020.pdf) | `raw/iready/iready_athome_practice_grade_1.pdf` |
| Student packet, Grade 2 | [PDF](https://capubstore.blob.core.windows.net/athomepdfs/iready-at-home-activity-packets-student-math-grade-2-2020.pdf) | `raw/iready/iready_athome_practice_grade_2.pdf` |
| Student packet, Grade 3 | [PDF](https://capubstore.blob.core.windows.net/athomepdfs/iready-at-home-activity-packets-student-math-grade-3-2020.pdf) | `raw/iready/iready_athome_practice_grade_3.pdf` |
| Student packet, Grade 4 | [PDF](https://capubstore.blob.core.windows.net/athomepdfs/iready-at-home-activity-packets-student-math-grade-4-2020.pdf) | `raw/iready/iready_athome_practice_grade_4.pdf` |
| Student packet, Grade 5 | [PDF](https://capubstore.blob.core.windows.net/athomepdfs/iready-at-home-activity-packets-student-math-grade-5-2020.pdf) | `raw/iready/iready_athome_practice_grade_5.pdf` |
| Teacher packet (answers in blue), Kindergarten | [PDF](https://capubstore.blob.core.windows.net/athomepdfs/iready-at-home-activity-packets-teacher-math-grade-k-2020.pdf) | `raw/iready/iready_athome_teacher_grade_k.pdf` |
| Teacher packet (answers in blue), Grade 1 | [PDF](https://capubstore.blob.core.windows.net/athomepdfs/iready-at-home-activity-packets-teacher-math-grade-1-2020.pdf) | `raw/iready/iready_athome_teacher_grade_1.pdf` |
| Teacher packet (answers in blue), Grade 2 | [PDF](https://capubstore.blob.core.windows.net/athomepdfs/iready-at-home-activity-packets-teacher-math-grade-2-2020.pdf) | `raw/iready/iready_athome_teacher_grade_2.pdf` |
| Teacher packet (answers in blue), Grade 3 | [PDF](https://capubstore.blob.core.windows.net/athomepdfs/iready-at-home-activity-packets-teacher-math-grade-3-2020.pdf) | `raw/iready/iready_athome_teacher_grade_3.pdf` |
| Teacher packet (answers in blue), Grade 4 | [PDF](https://capubstore.blob.core.windows.net/athomepdfs/iready-at-home-activity-packets-teacher-math-grade-4-2020.pdf) | `raw/iready/iready_athome_teacher_grade_4.pdf` |
| Teacher packet (answers in blue), Grade 5 | [PDF](https://capubstore.blob.core.windows.net/athomepdfs/iready-at-home-activity-packets-teacher-math-grade-5-2020.pdf) | `raw/iready/iready_athome_teacher_grade_5.pdf` |

### MathFish

| What | Link |
|---|---|
| Dataset | [huggingface.co/datasets/allenai/mathfish](https://huggingface.co/datasets/allenai/mathfish) |
| Paper: Li et al., *Evaluating Language Model Math Reasoning via Grounding in Educational Curricula*, EMNLP 2024 | [arxiv.org/abs/2408.04226](https://arxiv.org/abs/2408.04226) (local: `papers/copies/mathfish-emnlp-2024.pdf`) |
| Code | [github.com/allenai/mathfish](https://github.com/allenai/mathfish) |

- **Problem files:** [`train.jsonl`](https://huggingface.co/datasets/allenai/mathfish/resolve/main/train.jsonl),
  [`dev.jsonl`](https://huggingface.co/datasets/allenai/mathfish/resolve/main/dev.jsonl),
  [`test.jsonl`](https://huggingface.co/datasets/allenai/mathfish/resolve/main/test.jsonl),
  saved in `raw/mathfish/`.
- **Image archives:**
  [`im_lesson`](https://huggingface.co/datasets/allenai/mathfish/resolve/main/images/im_lesson.tar.gz),
  [`im_practice`](https://huggingface.co/datasets/allenai/mathfish/resolve/main/images/im_practice.tar.gz),
  [`im_task`](https://huggingface.co/datasets/allenai/mathfish/resolve/main/images/im_task.tar.gz),
  [`fl_problem`](https://huggingface.co/datasets/allenai/mathfish/resolve/main/images/fl_problem.tar.gz).
  Only the 4,869 images used by K-5 problems are kept, in `raw/mathfish/images/images/`.
- **License:** dataset ODC-By 1.0; Illustrative Mathematics content CC BY 4.0; Fishtank CC
  BY-NC-SA 4.0 (non-commercial).

### Considered but not used

| Source | Why not |
|---|---|
| [IXL: Georgia math standards](https://www.ixl.com/standards/georgia/math/kindergarten) | Practice drills generated on the fly; 10 free questions a day; its [terms of service](https://www.ixl.com/termsofservice) forbid automated collection |
| i-Ready Classroom Mathematics sample lessons | Download requires a sales-contact form |
| Third-party "GMAS practice tests" (Lumos, Effortless Math, Teachers Pay Teachers, …) | Not official; many paid |
| Other states' released tests (MCAS, New York, STAAR, …) | Surveyed in [`SOURCE_CANDIDATES.md`](SOURCE_CANDIDATES.md); not pursued |

---

## 8. How it was built, reliability, limitations

**Pipeline**

| Step | Script | Output |
|---|---|---|
| Code normalization helpers | `scripts/common.py` | — |
| Filter MathFish to K-5, student-facing text | `scripts/build_mathfish.py` | `data/mathfish_k5.jsonl` (4,428) |
| Parse Milestones PDFs (type, DOK, standard, answer) | `scripts/build_milestones.py` | `data/milestones_items.jsonl` (132, 9 duplicates flagged) |
| Milestones pictures, coded by hand | — | `data/milestones_visuals.json` |
| i-Ready items, coded by hand | `scripts/build_iready.py` | `data/iready_items.jsonl` (139) |
| Apply the categories to everything (first-pass labels) | `scripts/tag_question_types.py` (reads the structured extractions, so run it after them) | `data/all_items.jsonl` (5,774 questions) |
| Tables | `scripts/analyze.py` | `tables/*.csv`, §10 |
| Milestones questions as text + figures | `scripts/extract_milestones_structured.py` | `data/milestones_structured.json`, `review/img/milestones_fig/` |
| Milestones answers, explanations, exemplars | `scripts/extract_milestones_answers.py` | `data/milestones_answers.json` |
| i-Ready worksheets as problems + answers | `scripts/extract_iready_structured.py` | `data/iready_structured.json`, `review/img/iready_fig/` |
| i-Ready Diagnostic transcription + figures | `scripts/extract_iready_diagnostic.py` | `data/iready_diagnostic.json`, `review/img/iready_dx_fig/` |
| Original page images (for "Show original") | `scripts/extract_milestones_images.py`, `scripts/extract_iready_images.py` | `review/img/milestones/`, `review/img/iready/` |
| MathFish display HTML | `scripts/mathfish_html.py` (used by `build_review.py`) | — |
| Review page | `scripts/build_review.py` | `review/index.html` + `review/items.js` |

Rerun everything:

The PDF extraction scripts need PyMuPDF, installed in a local virtual environment
(`processed/question_types/.venv`; create it with
`python3 -m venv .venv && .venv/bin/pip install pymupdf`).

```bash
cd processed/question_types/scripts
python3 build_mathfish.py && python3 build_milestones.py && python3 build_iready.py \
  && python3 extract_milestones_images.py && python3 extract_iready_images.py \
  && ../.venv/bin/python extract_milestones_structured.py && ../.venv/bin/python extract_milestones_answers.py \
  && ../.venv/bin/python extract_iready_structured.py && ../.venv/bin/python extract_iready_diagnostic.py \
  && python3 tag_question_types.py && python3 analyze.py && python3 build_review.py
```

**How the labels are checked.** Apart from the hand-coded i-Ready Diagnostic samples, the
labels come from rules applied to the extracted text (`tag_question_types.py`; the rules are
in `CODEBOOK.md`). They are a **first pass for a person to check**, not a result:

- **Milestones:** GaDOE's printed item type is a built-in check. The rule labels agree with
  it on all 123 items: every Selected-Response item is *select one*, the 3 multi-select items
  are *select many*, and the 6 multi-part technology-enhanced items are *multi-part*. The
  part breakdown inside CR items is still the rules' reading.
- **i-Ready practice and MathFish:** no official labels exist, so they need **human review in
  the review page** (§1). There, a reviewer corrects the question type, part modes and
  stimulus, and exports the corrections as CSV.
- **Known weak spots to look at first:**
  - MathFish *open* vs *write* (discussion prompts);
  - MathFish long activities split into many parts;
  - i-Ready pages where the instruction applies to every problem ("Circle all the problems
    with…, then find…");
  - pictures of unknown kind.
- **The multiple-choice gap is robust** to these errors: only 6% of MathFish problems contain
  *any* answer-choice prompt.

**Limitations**

- **Old Milestones items.** The samples are 2016-2017. Since 2023 the tests follow the new
  Georgia standards; GaDOE says they add on-screen protractor/ruler tools and sets of three
  short questions built around one problem situation.
- **No Milestones below grade 3.** For K-2 the only test-format evidence is 4 i-Ready
  samples.
- **i-Ready frequencies unknown.** The 10 samples show which formats exist, not how often.
- **i-Ready standards are my assignment.** Please check them in the review page.
- **Domain counts reflect curriculum emphasis.** 49% of MathFish is NBT + OA, so compare
  percentages *within* a domain.

---

## 9. Next steps / questions for Dr. Choi

1. **Current Milestones formats.** Hand-transcribe the grades 3-5 online practice tests, or
   can a district login to GaDOE's portal (or GOFAR, its formative item bank) give us current
   items?
2. **i-Ready.** Is there a legitimate way to see more Diagnostic items (e.g. a partner
   teacher's account)?
3. **Human validation of the labels.** Go through `review/index.html` (starting with a
   sample per source), correct the labels, and export the CSV. Who should the second reviewer
   be, and how big a sample?
4. **Generator.** Lock in the target formats (§5.6) and start the diagram library (§5.5).

---

## 10. Full tables

Generated by `scripts/analyze.py`; don't edit by hand. Cells are **count (column %)**; column
% is the share of that domain's or grade's items, so read **down a column**.

<!-- TABLES:START -->
#### Corpus

| Source | Unit | Items | Grades | Standards labels |
|---|---|---|---|---|
| Milestones (GaDOE EOG samples, gr 3-5) | one test item | 123 | 3-5 | GaDOE (old GA codes, Common Core numbering) |
| i-Ready Diagnostic samples | one test item | 10 | K-5 | Common Core, assigned by us |
| i-Ready practice problems (K-5) | one numbered problem (K: one page) | 1213 | K-5 | Common Core, assigned by us |
| MathFish (IM + Fishtank, K-5) | one problem / activity | 4428 | K-5 | Common Core, by IM / Fishtank |

#### 10.1 Question type by source

| Question type | Milestones (GaDOE EOG samples, gr 3-5) | i-Ready Diagnostic samples | i-Ready practice problems (K-5) | MathFish (IM + Fishtank, K-5) |
|---|---|---|---|---|
| Select one | 83 (67%) | 7 (70%) | 4 (<1%) | 197 (4%) |
| Select many | 3 (2%) | · | 3 (<1%) | 11 (<1%) |
| Enter (number / expression) | · | 2 (20%) | 1101 (91%) | 608 (14%) |
| Write (explanation) | 11 (9%) | · | 76 (6%) | 686 (15%) |
| Construct (plot / shade / draw) | · | 1 (10%) | 22 (2%) | 52 (1%) |
| Match / order / sort | · | · | 7 (<1%) | 24 (<1%) |
| Drop-down | · | · | · | · |
| Multi-part | 26 (21%) | · | · | 1660 (37%) |
| Open activity (outside the scheme) | · | · | · | 1190 (27%) |
| **Total** | 123 | 10 | 1213 | 4428 |

**Same grades only (3-5)** — Milestones has no K-2 test, so this is the fair comparison:

| Question type | Milestones gr 3-5 | MathFish gr 3-5 (all) | MathFish gr 3-5: FL target tasks (exit tickets) | MathFish gr 3-5: IM practice problems | i-Ready practice gr 3-5 |
|---|---|---|---|---|---|
| Select one | 83 (67%) | 52 (2%) | 2 (<1%) | 1 (1%) | 1 (<1%) |
| Select many | 3 (2%) | 3 (<1%) | · | 3 (4%) | 3 (<1%) |
| Enter (number / expression) | · | 338 (13%) | 59 (15%) | 18 (25%) | 735 (90%) |
| Write (explanation) | 11 (9%) | 424 (16%) | 63 (17%) | 29 (40%) | 59 (7%) |
| Construct (plot / shade / draw) | · | 38 (1%) | 14 (4%) | 2 (3%) | 18 (2%) |
| Match / order / sort | · | 8 (<1%) | · | · | 1 (<1%) |
| Drop-down | · | · | · | · | · |
| Multi-part | 26 (21%) | 1288 (50%) | 230 (60%) | 18 (25%) | · |
| Open activity (outside the scheme) | · | 425 (16%) | 13 (3%) | 2 (3%) | · |
| **Total** | 123 | 2576 | 381 | 73 | 817 |

Share of questions that **use** each answer mode in any part (a multi-part question counts in every row its parts use):

| Question type | Milestones (GaDOE EOG samples, gr 3-5) | i-Ready Diagnostic samples | i-Ready practice problems (K-5) | MathFish (IM + Fishtank, K-5) |
|---|---|---|---|---|
| Select one | 72% | 70% | <1% | 6% |
| Select many | 5% | · | <1% | <1% |
| Enter (number / expression) | 16% | 20% | 91% | 43% |
| Write (explanation) | 23% | · | 6% | 38% |
| Construct (plot / shade / draw) | <1% | 10% | 2% | 7% |
| Match / order / sort | · | · | <1% | 1% |
| Drop-down | · | · | · | · |

#### 10.2 What multi-part questions are made of

Each part keeps its own answer mode; the combination lists the parts in order.

| Source | Multi-part | Parts per question | Most common combinations |
|---|---|---|---|
| Milestones (GaDOE EOG samples, gr 3-5) | 26 | 2: 15, 3: 8, 4: 2, 5: 1 | enter → write (4); enter → enter (3); select_one → select_one (3); enter → enter → write (3) |
| i-Ready Diagnostic samples | 0 | · | · |
| i-Ready practice problems (K-5) | 0 | · | · |
| MathFish (IM + Fishtank, K-5) | 1660 | 2: 433, 3: 341, 4: 281, 5: 181, 6+: 424 | enter → enter (143); enter → enter → enter (117); write → write (95); enter → enter → enter → enter (85) |

#### 10.3 Question type × Common Core domain

Domains: **CC** Counting & Cardinality, **OA** Operations & Algebraic Thinking, **NBT** Number & Operations in Base Ten, **NF** Number & Operations - Fractions, **MD** Measurement & Data, **G** Geometry.

**Milestones (GaDOE EOG samples, gr 3-5)** (n=123)

| Question type | OA | NBT | NF | MD | G | Total |
|---|---|---|---|---|---|---|
| Select one | 14 (56%) | 19 (70%) | 18 (67%) | 20 (69%) | 12 (80%) | 83 |
| Select many | · | · | 1 (4%) | 2 (7%) | · | 3 |
| Write (explanation) | 1 (4%) | 3 (11%) | 3 (11%) | 3 (10%) | 1 (7%) | 11 |
| Multi-part | 10 (40%) | 5 (19%) | 5 (19%) | 4 (14%) | 2 (13%) | 26 |
| **Total** | 25 | 27 | 27 | 29 | 15 | 123 |

**i-Ready Diagnostic samples** (n=10)

| Question type | CC | OA | NBT | NF | MD | Total |
|---|---|---|---|---|---|---|
| Select one | 1 (100%) | 2 (100%) | 1 (100%) | · | 3 (60%) | 7 |
| Enter (number / expression) | · | · | · | · | 2 (40%) | 2 |
| Construct (plot / shade / draw) | · | · | · | 1 (100%) | · | 1 |
| **Total** | 1 | 2 | 1 | 1 | 5 | 10 |

**i-Ready practice problems (K-5)** (n=1213)

| Question type | CC | OA | NBT | NF | MD | Total |
|---|---|---|---|---|---|---|
| Select one | 3 (27%) | 1 (<1%) | · | · | · | 4 |
| Select many | · | · | 3 (<1%) | · | · | 3 |
| Enter (number / expression) | 8 (73%) | 405 (91%) | 510 (92%) | 148 (89%) | 30 (88%) | 1101 |
| Write (explanation) | · | 22 (5%) | 40 (7%) | 10 (6%) | 4 (12%) | 76 |
| Construct (plot / shade / draw) | · | 13 (3%) | 1 (<1%) | 8 (5%) | · | 22 |
| Match / order / sort | · | 5 (1%) | 2 (<1%) | · | · | 7 |
| **Total** | 11 | 446 | 556 | 166 | 34 | 1213 |

**MathFish (IM + Fishtank, K-5)** (n=4428)

| Question type | CC | OA | NBT | NF | MD | G | Total |
|---|---|---|---|---|---|---|---|
| Select one | 23 (7%) | 56 (6%) | 48 (4%) | 13 (2%) | 28 (4%) | 29 (6%) | 197 |
| Select many | · | 2 (<1%) | 2 (<1%) | 1 (<1%) | 5 (<1%) | 1 (<1%) | 11 |
| Enter (number / expression) | 34 (11%) | 157 (16%) | 203 (17%) | 101 (15%) | 95 (12%) | 18 (4%) | 608 |
| Write (explanation) | 26 (8%) | 188 (20%) | 182 (15%) | 134 (19%) | 106 (13%) | 50 (11%) | 686 |
| Construct (plot / shade / draw) | · | 7 (<1%) | 5 (<1%) | 9 (1%) | 12 (2%) | 19 (4%) | 52 |
| Match / order / sort | 2 (<1%) | 6 (<1%) | 4 (<1%) | 4 (<1%) | 5 (<1%) | 3 (<1%) | 24 |
| Multi-part | 16 (5%) | 306 (32%) | 474 (39%) | 345 (50%) | 372 (47%) | 147 (32%) | 1660 |
| Open activity (outside the scheme) | 212 (68%) | 239 (25%) | 286 (24%) | 88 (13%) | 168 (21%) | 197 (42%) | 1190 |
| **Total** | 313 | 961 | 1204 | 695 | 791 | 464 | 4428 |


#### 10.4 Question type × grade

**Milestones (GaDOE EOG samples, gr 3-5)** (n=123)

| Question type | 3 | 4 | 5 | Total |
|---|---|---|---|---|
| Select one | 30 (70%) | 26 (65%) | 27 (68%) | 83 |
| Select many | 1 (2%) | 1 (2%) | 1 (2%) | 3 |
| Write (explanation) | 4 (9%) | 6 (15%) | 1 (2%) | 11 |
| Multi-part | 8 (19%) | 7 (18%) | 11 (28%) | 26 |
| **Total** | 43 | 40 | 40 | 123 |

**i-Ready Diagnostic samples** (n=10)

| Question type | K | 2 | 3 | 4 | 5 | Total |
|---|---|---|---|---|---|---|
| Select one | 2 (100%) | 2 (100%) | 1 (50%) | 2 (67%) | · | 7 |
| Enter (number / expression) | · | · | · | 1 (33%) | 1 (100%) | 2 |
| Construct (plot / shade / draw) | · | · | 1 (50%) | · | · | 1 |
| **Total** | 2 | 2 | 2 | 3 | 1 | 10 |

**i-Ready practice problems (K-5)** (n=1213)

| Question type | K | 1 | 2 | 3 | 4 | 5 | Total |
|---|---|---|---|---|---|---|---|
| Select one | 3 (10%) | · | · | 1 (<1%) | · | · | 4 |
| Select many | · | · | · | · | 3 (1%) | · | 3 |
| Enter (number / expression) | 18 (62%) | 99 (94%) | 249 (95%) | 238 (89%) | 190 (89%) | 307 (92%) | 1101 |
| Write (explanation) | · | 4 (4%) | 13 (5%) | 15 (6%) | 19 (9%) | 25 (7%) | 76 |
| Construct (plot / shade / draw) | 4 (14%) | · | · | 13 (5%) | 2 (<1%) | 3 (<1%) | 22 |
| Match / order / sort | 4 (14%) | 2 (2%) | · | 1 (<1%) | · | · | 7 |
| **Total** | 29 | 105 | 262 | 268 | 214 | 335 | 1213 |

**MathFish (IM + Fishtank, K-5)** (n=4428)

| Question type | K | 1 | 2 | 3 | 4 | 5 | Total |
|---|---|---|---|---|---|---|---|
| Select one | 49 (9%) | 61 (9%) | 35 (6%) | 28 (3%) | 9 (1%) | 15 (2%) | 197 |
| Select many | 5 (<1%) | 1 (<1%) | 2 (<1%) | 1 (<1%) | 2 (<1%) | · | 11 |
| Enter (number / expression) | 74 (13%) | 109 (16%) | 87 (14%) | 122 (14%) | 99 (11%) | 117 (14%) | 608 |
| Write (explanation) | 50 (9%) | 128 (19%) | 84 (14%) | 150 (18%) | 135 (16%) | 139 (16%) | 686 |
| Construct (plot / shade / draw) | 6 (1%) | 4 (<1%) | 4 (<1%) | 21 (2%) | 8 (<1%) | 9 (1%) | 52 |
| Match / order / sort | 8 (1%) | 5 (<1%) | 3 (<1%) | 4 (<1%) | 2 (<1%) | 2 (<1%) | 24 |
| Multi-part | 31 (5%) | 118 (18%) | 223 (36%) | 361 (42%) | 472 (55%) | 455 (53%) | 1660 |
| Open activity (outside the scheme) | 344 (61%) | 243 (36%) | 178 (29%) | 163 (19%) | 134 (16%) | 128 (15%) | 1190 |
| **Total** | 567 | 669 | 616 | 850 | 861 | 865 | 4428 |


#### 10.5 Which standards each question type concentrates on

Common Core standards (e.g. `3.OA.4`; sub-letters merged) with the most items of each type. *share* = that type's share of the standard's items (standards with ≥ 8 items in the source). Full per-standard counts: `tables/standard_by_type.csv`.

**MathFish** (standards with ≥ 8 items)

| Question type | Top standards: count (share of standard's items) |
|---|---|
| Select one | `1.NBT.5` 8 (38%), `1.NBT.6` 4 (31%), `1.OA.5` 22 (29%), `5.MD.3` 3 (27%), `1.OA.8` 13 (27%), `2.G.A` 2 (22%) |
| Select many | `K.MD.2` 4 (29%), `3.G.2` 1 (8%), `2.NBT.3` 1 (7%), `1.NBT.5` 1 (5%), `2.OA.4` 1 (4%), `4.MD.1` 1 (3%) |
| Enter (number / expression) | `2.NBT.6` 7 (70%), `K.CC.A` 6 (60%), `K.CC.C` 4 (44%), `1.NBT.B` 5 (33%), `1.OA.7` 8 (32%), `4.NBT.B` 3 (30%) |
| Write (explanation) | `1.OA.7` 14 (56%), `5.OA.A` 5 (56%), `1.MD.1` 4 (50%), `3.OA.A` 4 (50%), `3.NBT.3` 6 (40%), `1.OA.3` 7 (37%) |
| Construct (plot / shade / draw) | `K.G.2` 3 (20%), `3.G.2` 2 (17%), `K.MD.2` 2 (14%), `4.G.3` 3 (12%), `3.NF.1` 4 (11%), `2.G.2` 1 (11%) |
| Match / order / sort | `K.MD.3` 3 (27%), `1.G.2` 2 (14%), `4.NF.7` 2 (14%), `1.MD.4` 2 (7%), `K.G.2` 1 (7%), `1.G.A` 2 (6%) |
| Multi-part | `5.OA.3` 13 (93%), `2.MD.5` 10 (91%), `5.NBT.2` 26 (87%), `3.NBT.1` 30 (81%), `5.G.2` 17 (81%), `5.MD.1` 21 (81%) |
| Open activity (outside the scheme) | `K.G` 19 (100%), `4.G.A` 10 (100%), `5.G.B` 21 (95%), `K.CC.1` 26 (87%), `K.CC.6` 40 (85%), `K.G.5` 15 (83%) |

**Milestones** (standards with ≥ 3 items)

| Question type | Top standards: count (share of standard's items) |
|---|---|
| Select one | `3.NBT.1` 3 (100%), `3.MD.4` 2 (67%), `3.OA.4` 2 (67%), `3.MD.3` 2 (67%), `4.NBT.3` 2 (67%), `5.NF.2` 2 (67%) |
| Select many | `5.MD.5` 1 (33%), `4.NF.3` 1 (17%) |
| Write (explanation) | `3.MD.3` 1 (33%), `4.NBT.3` 1 (33%), `3.NBT.2` 1 (25%), `4.NF.3` 1 (17%) |
| Multi-part | `4.OA.4` 2 (67%), `4.NF.3` 2 (33%), `3.MD.4` 1 (33%), `3.OA.4` 1 (33%), `5.NF.2` 1 (33%), `5.NBT.7` 1 (33%) |

**i-Ready practice** (standards with ≥ 3 items)

| Question type | Top standards: count (share of standard's items) |
|---|---|
| Select one | `K.CC.6` 2 (50%), `K.CC.4` 1 (33%), `3.OA.8` 1 (7%) |
| Select many | `4.NBT.2` 3 (18%) |
| Enter (number / expression) | `4.NBT.3` 19 (100%), `4.OA.2` 18 (100%), `4.NF.2` 16 (100%), `1.OA.1` 15 (100%), `2.MD.3` 10 (100%), `1.OA.7` 9 (100%) |
| Write (explanation) | `5.NBT.1` 2 (67%), `3.OA.9` 1 (33%), `3.MD.7` 2 (25%), `3.OA.1` 1 (25%), `4.OA.3` 2 (18%), `4.NBT.6` 5 (16%) |
| Construct (plot / shade / draw) | `3.OA.2` 4 (80%), `K.OA.3` 2 (50%), `3.NF.1` 4 (33%), `5.NBT.1` 1 (33%), `5.NF.4` 2 (9%), `3.OA.5` 2 (7%) |
| Match / order / sort | `K.OA.1` 4 (100%), `3.OA.5` 1 (3%) |


#### 10.6 Stimulus (what the student looks at) by source

| Stimulus | Milestones (GaDOE EOG samples, gr 3-5) | i-Ready Diagnostic samples | i-Ready practice problems (K-5) | MathFish (IM + Fishtank, K-5) |
|---|---|---|---|---|
| None (text only) | 69 (56%) | · | 794 (65%) | 2343 (53%) |
| Table (text / numbers in cells) | 7 (6%) | · | 3 (<1%) | 171 (4%) |
| Diagram | 44 (36%) | 2 (20%) | 174 (14%) | 962 (22%) |
| Illustration / photo | 3 (2%) | · | 9 (<1%) | · |
| Interactive tool | · | 8 (80%) | · | · |
| Image, kind unknown | · | · | 233 (19%) | 952 (21%) |

Stimulus × question type (share of each type's questions):

**Milestones (GaDOE EOG samples, gr 3-5)**

| Stimulus | Select one | Select many | Write | Multi-part | Total |
|---|---|---|---|---|---|
| None (text only) | 46 (55%) | 2 (67%) | 6 (55%) | 15 (58%) | 69 |
| Table (text / numbers in cells) | 4 (5%) | 1 (33%) | 1 (9%) | 1 (4%) | 7 |
| Diagram | 30 (36%) | · | 4 (36%) | 10 (38%) | 44 |
| Illustration / photo | 3 (4%) | · | · | · | 3 |
| **Total** | 83 | 3 | 11 | 26 | 123 |

**i-Ready Diagnostic samples**

| Stimulus | Select one | Enter | Construct | Total |
|---|---|---|---|---|
| Diagram | 1 (14%) | 1 (50%) | · | 2 |
| Interactive tool | 6 (86%) | 1 (50%) | 1 (100%) | 8 |
| **Total** | 7 | 2 | 1 | 10 |

**i-Ready practice problems (K-5)**

| Stimulus | Select one | Select many | Enter | Write | Construct | Match / order / sort | Total |
|---|---|---|---|---|---|---|---|
| None (text only) | 1 (25%) | 3 (100%) | 717 (65%) | 58 (76%) | 14 (64%) | 1 (14%) | 794 |
| Table (text / numbers in cells) | · | · | 3 (<1%) | · | · | · | 3 |
| Diagram | · | · | 153 (14%) | 7 (9%) | 8 (36%) | 6 (86%) | 174 |
| Illustration / photo | 3 (75%) | · | 6 (<1%) | · | · | · | 9 |
| Image, kind unknown | · | · | 222 (20%) | 11 (14%) | · | · | 233 |
| **Total** | 4 | 3 | 1101 | 76 | 22 | 7 | 1213 |

**MathFish (IM + Fishtank, K-5)**

| Stimulus | Select one | Select many | Enter | Write | Construct | Match / order / sort | Multi-part | Open activity | Total |
|---|---|---|---|---|---|---|---|---|---|
| None (text only) | 14 (7%) | 4 (36%) | 367 (60%) | 309 (45%) | 11 (21%) | 7 (29%) | 616 (37%) | 1015 (85%) | 2343 |
| Table (text / numbers in cells) | 3 (2%) | · | 35 (6%) | 13 (2%) | · | · | 110 (7%) | 10 (<1%) | 171 |
| Diagram | 45 (23%) | 5 (45%) | 114 (19%) | 111 (16%) | 36 (69%) | 6 (25%) | 579 (35%) | 66 (6%) | 962 |
| Image, kind unknown | 135 (69%) | 2 (18%) | 92 (15%) | 253 (37%) | 5 (10%) | 11 (46%) | 355 (21%) | 99 (8%) | 952 |
| **Total** | 197 | 11 | 608 | 686 | 52 | 24 | 1660 | 1190 | 4428 |

Stimulus × CCSS domain (share of the domain's questions):

**Milestones (GaDOE EOG samples, gr 3-5)**

| Stimulus | OA | NBT | NF | MD | G | Total |
|---|---|---|---|---|---|---|
| None (text only) | 20 (80%) | 22 (81%) | 15 (56%) | 7 (24%) | 5 (33%) | 69 |
| Table (text / numbers in cells) | 2 (8%) | 1 (4%) | 1 (4%) | 3 (10%) | · | 7 |
| Diagram | 2 (8%) | 4 (15%) | 11 (41%) | 17 (59%) | 10 (67%) | 44 |
| Illustration / photo | 1 (4%) | · | · | 2 (7%) | · | 3 |
| **Total** | 25 | 27 | 27 | 29 | 15 | 123 |

**i-Ready practice problems (K-5)**

| Stimulus | CC | OA | NBT | NF | MD | Total |
|---|---|---|---|---|---|---|
| None (text only) | · | 258 (58%) | 381 (69%) | 140 (84%) | 15 (44%) | 794 |
| Table (text / numbers in cells) | · | · | 3 (<1%) | · | · | 3 |
| Diagram | 6 (55%) | 97 (22%) | 45 (8%) | 11 (7%) | 15 (44%) | 174 |
| Illustration / photo | 5 (45%) | · | · | · | 4 (12%) | 9 |
| Image, kind unknown | · | 91 (20%) | 127 (23%) | 15 (9%) | · | 233 |
| **Total** | 11 | 446 | 556 | 166 | 34 | 1213 |

**MathFish (IM + Fishtank, K-5)**

| Stimulus | CC | OA | NBT | NF | MD | G | Total |
|---|---|---|---|---|---|---|---|
| None (text only) | 198 (63%) | 529 (55%) | 739 (61%) | 388 (56%) | 282 (36%) | 207 (45%) | 2343 |
| Table (text / numbers in cells) | 1 (<1%) | 38 (4%) | 50 (4%) | 32 (5%) | 41 (5%) | 9 (2%) | 171 |
| Diagram | 42 (13%) | 112 (12%) | 147 (12%) | 168 (24%) | 311 (39%) | 182 (39%) | 962 |
| Image, kind unknown | 72 (23%) | 282 (29%) | 268 (22%) | 107 (15%) | 157 (20%) | 66 (14%) | 952 |
| **Total** | 313 | 961 | 1204 | 695 | 791 | 464 | 4428 |

Diagram kinds (count of questions showing each kind):

| Source | Diagram kinds |
|---|---|
| Milestones (GaDOE EOG samples, gr 3-5) | geometry_2d 9, fraction_model 7, area_grid 4, number_line 4, coordinate_grid 4, line_plot 4, ruler 3, picture_graph 2, clock 2, decimal_grid 2, geometry_3d 2, equal_groups_array 1, bar_graph 1, protractor 1, measurement_scale 1 |
| i-Ready Diagnostic samples | ruler 2, counters 1, number_line 1, geometry_3d 1, base_ten 1, protractor 1, geometry_2d 1, area_grid 1, ten_frame 1 |
| i-Ready practice problems (K-5) | geometry_2d 52, number_bond 30, ten_frame 25, number_line 24, counters 17, cubes 13, ruler 10, base_ten 8, fraction_model 8, clock 6, equal_groups_array 3, area_grid 2, decimal_grid 1 |
| MathFish (IM + Fishtank, K-5) | geometry_2d 412, number_line 160, area_grid 138, fraction_model 86, geometry_3d 78, base_ten 75, counters 59, protractor 55, table_with_pictures 55, equal_groups_array 34, money 32, coordinate_grid 30, clock 29, line_plot 27, ten_frame 25, bar_graph 21, ruler 20, picture_graph 12, tape_diagram 3 |
<!-- TABLES:END -->
