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
| i-Ready practice worksheets | Numbered problems as text, with their pictures | The teacher packet's answers, highlighted in place |
| MathFish | The publisher's own formatted page (paragraphs, numbered lists, tables) with its images | None: the publishers keep solutions behind a teacher login |

Every card also has **Show original page**, so you can check the extraction against the
source.

Using the page:

- **Filter** by source, grade, Common Core domain, question type, picture type, or search
  text (e.g. `3.NF.2`, `number line`). "Only items with an answer" hides MathFish.
- **Link to a view:** add filters to the address, e.g. `index.html?source=milestones&grade=4`.
- **Correct our labels:** each item has a *my label* menu (pick the right question type, or
  "Label is correct"), a note box, and a **Flag** button.
- **Where your review is kept:** in your browser. **Export my review (CSV)** downloads it,
  so the corrections can be fed back in.
- **Math symbols** render through KaTeX, which loads from the internet. Offline, the formulas
  show as raw LaTeX.

To rebuild the page after re-running the pipeline: `python3 scripts/build_review.py`.

---

## 2. Summary

- **The real tests are mostly multiple choice.**
  - 70% of Milestones sample items are single-answer multiple choice, 5% multi-select, 25%
    written explanation.
  - 7 of the 10 public i-Ready Diagnostic samples are multiple choice.
- **MathFish is almost never multiple choice (under 1%).**
  - It's lesson material: 42% "explain your reasoning", 29% open activities (games,
    discussions), 24% numeric answers.
  - It covers the standards well, but its question *formats* look nothing like the tests.
- **Question format tracks difficulty on Milestones.** Every DOK-1 (easiest) item is
  multiple choice; 71% of DOK-3 (hardest) items are written.
- **Nearly every picture on the tests can be drawn by code.**
  - Milestones: 56% have no picture, 6% just a table, 36% a simple diagram (number line,
    fraction model, shape, grid, graph).
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

- The official format mix: 70% multiple choice, 5% multi-select, 25% written.
- How format relates to difficulty (DOK).
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
  and worksheet, the question format, picture type, and whether it's a word problem.
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
- The practice worksheets are 91% numeric-answer drills, and 59% end with one "explain your
  strategy" question.
- Kindergarten worksheets mix in circling, matching and drawing.
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
   (`scripts/tag_question_types.py`). 4,428 is too many to label by hand, so text rules do
   it: "Explain…" means written response, lettered options mean multiple choice, "Select
   all" means multi-select, and so on. §8 shows how accurate this is.
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

Full definitions: [`CODEBOOK.md`](CODEBOOK.md). Each item is coded on four separate
dimensions, so the categories don't overlap. For example, a word problem with a number line is
coded "word problem" *and* "number line", on different dimensions.

**A. Response format: what the student has to produce**

| Code | Question type | Example | Seen on |
|---|---|---|---|
| `SR` | Multiple choice, one answer | "What is 738 rounded to the nearest hundred? A. 700 B. 730 …" | Milestones, i-Ready |
| `MS` | Multi-select | "Select **TWO** equations that are missing the same number." | Milestones |
| `NUM` | Numeric / short answer | "Type the answer in the box: ___ inches" | i-Ready, worksheets |
| `MATCH` | Match / sort / drag | "Draw lines to match the numbers." | i-Ready, K worksheets |
| `DRAW` | Draw / plot / shade / label | "Click on the number line to show ½." | i-Ready |
| `CR` | Written explanation | "Part B: Explain the strategy you used." | Milestones (2 or 4 points) |
| `ACT` | Open activity, no single answer | Partner games, number talks, "What do you notice?" | MathFish only |

**When an item mixes formats:**

- **Test items** take the type of their *hardest part*, which is how GaDOE labels its own
  items. "Part A: solve, Part B: explain" counts as a written explanation.
- **i-Ready worksheets** have 4-20 separate problems, so they take their *most common*
  format.

**B. Context:** word problem, visual model (a task about a picture), or symbolic (bare numbers).

**C. Picture (the multimodal question):**

| Category | Meaning | Can we generate it? |
|---|---|---|
| Text only | No picture | Yes, the LLM writes it |
| Table only | A data table | Yes, as Markdown/HTML |
| Code-drawable diagram | Number line, fraction model, clock, shape, grid, graph, base-ten blocks … | Yes, render with code (SVG/matplotlib) from parameters |
| Illustration / photo | Real objects (nails, bottle caps, a fish to measure) | Hard: needs image generation or an image library |
| Interactive tool | Student answers by using an on-screen ruler, protractor, counters | Needs a front-end widget, not just an image |

**D. Difficulty (DOK):** Webb's Depth of Knowledge: 1 = recall, 2 = skill/concept,
3 = strategic thinking. Only Milestones prints it.

---

## 5. Findings

Domains below are **Common Core domains**: CC Counting & Cardinality (K only), OA Operations &
Algebraic Thinking, NBT Number & Operations in Base Ten, NF Fractions, MD Measurement & Data,
G Geometry.

### 5.1 Question type by source

| Question type | Milestones (gr 3-5) | i-Ready Diagnostic samples | i-Ready practice worksheets | MathFish (K-5) |
|---|---|---|---|---|
| Multiple choice (one answer) | **70%** | **7 of 10** | 2% | 0.4% |
| Multi-select | 5% | · | · | 0.2% |
| Numeric / short answer | · | 2 of 10 | **91%** | 24% |
| Match / sort | · | · | 2% | 1% |
| Draw / plot / shade | · | 1 of 10 | 4% | 4% |
| Written explanation | 25% | · | 1% | **42%** |
| Open activity | · | · | · | **29%** |
| **Number of items** | 123 | 10 | 129 worksheets | 4,428 |

- **Fair comparison (grades 3-5 only, since Milestones starts at grade 3):** MathFish is 52%
  written explanation and 0.5% multiple choice.
- **Even MathFish's most test-like parts don't match.** Fishtank exit tickets and IM practice
  problems (grades 3-5) are about 1% multiple choice.
- **Multi-part items are common on the tests.** Most Milestones technology-enhanced and
  written items have a Part A and a Part B.

### 5.2 By grade

| | K | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **MathFish:** open activity | 66% | 40% | 31% | 20% | 16% | 15% |
| **MathFish:** written explanation | 12% | 32% | 36% | 47% | 55% | 55% |
| **i-Ready worksheets:** numeric answer | 60% | 88% | 100% | 96% | 96% | 93% |
| **Milestones:** multiple choice | — | — | — | 72% | 68% | 70% |

- **MathFish shifts with grade.** Kindergarten is mostly games and hands-on activities; by
  grade 5 over half ask for an explanation.
- **Milestones is steady across grades 3-5:** about 70% multiple choice, 5% multi-select,
  25% written.

### 5.3 By domain

| Domain | Milestones: multiple choice | Milestones: has a diagram | MathFish: written explanation | MathFish: open activity |
|---|---|---|---|---|
| CC (K only) | — | — | 10% | 73% |
| OA | 60% | 8% | 42% | 27% |
| NBT | 70% | 15% | 44% | 26% |
| NF | 67% | 41% | **57%** | 14% |
| MD | 76% | **59%** | 43% | 23% |
| G | 80% | **67%** | 32% | 44% |

- **Milestones:** written items cluster in OA (32%) and fractions (30%). Measurement and
  geometry items are multiple choice *about a picture*.
- **MathFish:** fractions are the most explanation-heavy; geometry has the most drawing tasks
  (13%).
- **Per-standard breakdown** (e.g. which `3.OA.x` standards lean toward which type):
  `tables/standard_by_type.csv` and §10.

### 5.4 By difficulty (Milestones only)

| Question type | DOK 1 | DOK 2 | DOK 3 |
|---|---|---|---|
| Multiple choice | **100%** | 67% | 24% |
| Multi-select | · | 7% | 6% |
| Written explanation | · | 26% | **71%** |
| **Items** | 33 | 73 | 17 |

Easy items are always multiple choice; hard items are mostly written. This is useful for a
generator that must produce several difficulty levels.

### 5.5 Pictures

| Picture | Milestones | i-Ready Diagnostic | i-Ready worksheets | MathFish |
|---|---|---|---|---|
| Text only | 56% | · | 64% | 53% |
| Table only | 6% | · | 5% | 4% |
| Code-drawable diagram | 36% | 2 of 10 | 26% | 21% |
| Illustration / photo | 2% | · | 5% | not measured* |
| Interactive tool | · | **8 of 10** | · | · |
| Image, kind unknown | · | · | · | 21%* |

\*MathFish images weren't coded one by one. A spot check of 32 found about 4 in 5 were
ordinary diagrams too.

**Most common diagrams on Milestones** (what to build first):

- geometry figures (9), fraction models (7)
- number lines, area grids, coordinate grids, line plots (4 each)
- rulers (3)
- clocks, picture graphs, decimal grids, 3-D solids (2 each)

Diagrams appear in 59-67% of measurement and geometry items, but only 8-15% of OA and NBT
items.

### 5.6 What this means for our question generator

- **Formats to support:**
  - 4-option multiple choice with error-based wrong answers (model: the Milestones
    rationales)
  - multi-select (choose 2-3 of 5-6)
  - two-part items (Part A / Part B)
  - numeric entry
  - written explanation with a rubric
  - for i-Ready alignment: number-line plotting and drop-down
- **Use MathFish for content, not format:** convert its standard-labeled problems into the
  formats above.
- **Pictures:** a code-drawn diagram library covers nearly all grade 3-5 test items; start
  with the list in §5.5.

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
| Apply the categories to everything | `scripts/tag_question_types.py` | `data/all_items.jsonl` (4,690) |
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
  && python3 tag_question_types.py && python3 analyze.py \
  && python3 extract_milestones_images.py && python3 extract_iready_images.py \
  && ../.venv/bin/python extract_milestones_structured.py && ../.venv/bin/python extract_milestones_answers.py \
  && ../.venv/bin/python extract_iready_structured.py && ../.venv/bin/python extract_iready_diagnostic.py \
  && python3 build_review.py
```

**How accurate is the MathFish tagging?** Text rules label MathFish, so they were checked
three ways:

| Check | Result |
|---|---|
| Rules vs GaDOE's own labels, on the 123 Milestones items | 92% agree (κ = 0.83) |
| Rules vs my blind labels, on 30 new MathFish items | 21/30 (70%) |
| Same 30, after fixing one bug that check exposed | 23/30 (77%), no longer blind |

- **Where the rules go wrong:** on fuzzy boundaries: "open activity" vs "explain", answer
  choices without A/B/C letters, "draw" vs "explain".
- **So read MathFish percentages as about ±10 points.**
- **The multiple-choice gap is real.** Only 6% of MathFish problems contain *any*
  answer-choice prompt.
- **You can check it yourself:** the review page shows every label next to its item.

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
3. **Review.** Go through `review/index.html`, fix labels, and export the CSV so corrections
   feed back in.
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
| i-Ready practice sets (K-5) | one worksheet (4-20 problems) | 129 | K-5 | Common Core, assigned by us |
| MathFish (IM + Fishtank, K-5) | one problem / activity | 4428 | K-5 | Common Core, by IM / Fishtank |

#### 10.1 Question type by source

| Question type | Milestones (GaDOE EOG samples, gr 3-5) | i-Ready Diagnostic samples | i-Ready practice sets (K-5) | MathFish (IM + Fishtank, K-5) |
|---|---|---|---|---|
| Selected response (single) | 86 (70%) | 7 (70%) | 3 (2%) | 16 (<1%) |
| Multi-select | 6 (5%) | · | · | 9 (<1%) |
| Numeric / short answer | · | 2 (20%) | 117 (91%) | 1082 (24%) |
| Match / sort | · | · | 3 (2%) | 23 (<1%) |
| Draw / plot / shade | · | 1 (10%) | 5 (4%) | 174 (4%) |
| Constructed response (explain) | 31 (25%) | · | 1 (<1%) | 1851 (42%) |
| Open activity (no scorable answer) | · | · | · | 1273 (29%) |
| **Total** | 123 | 10 | 129 | 4428 |

**Same grades only (3-5)** — Milestones has no K-2 test, so this is the fair comparison:

| Question type | Milestones gr 3-5 | MathFish gr 3-5 (all) | MathFish gr 3-5: FL target tasks (exit tickets) | MathFish gr 3-5: IM practice problems | i-Ready practice gr 3-5 |
|---|---|---|---|---|---|
| Selected response (single) | 86 (70%) | 12 (<1%) | 2 (<1%) | 1 (1%) | · |
| Multi-select | 6 (5%) | 5 (<1%) | · | 3 (4%) | · |
| Numeric / short answer | · | 636 (25%) | 146 (38%) | 26 (36%) | 72 (95%) |
| Match / sort | · | 10 (<1%) | · | · | · |
| Draw / plot / shade | · | 126 (5%) | 32 (8%) | 3 (4%) | 3 (4%) |
| Constructed response (explain) | 31 (25%) | 1345 (52%) | 181 (48%) | 37 (51%) | 1 (1%) |
| Open activity (no scorable answer) | · | 442 (17%) | 20 (5%) | 3 (4%) | · |
| **Total** | 123 | 2576 | 381 | 73 | 76 |

Share of items that **contain** each format anywhere (an item can count in several rows):

| Question type | Milestones (GaDOE EOG samples, gr 3-5) | i-Ready Diagnostic samples | i-Ready practice sets (K-5) | MathFish (IM + Fishtank, K-5) |
|---|---|---|---|---|
| Selected response (single) | 74% | 70% | 13% | 5% |
| Multi-select | 5% | · | <1% | 1% |
| Numeric / short answer | 17% | 20% | 95% | 61% |
| Match / sort | <1% | · | 3% | 3% |
| Draw / plot / shade | <1% | 10% | 12% | 10% |
| Constructed response (explain) | 25% | · | 59% | 47% |

#### 10.2 Question type × Common Core domain

Domains: **CC** Counting & Cardinality, **OA** Operations & Algebraic Thinking, **NBT** Number & Operations in Base Ten, **NF** Number & Operations - Fractions, **MD** Measurement & Data, **G** Geometry.

**Milestones (GaDOE EOG samples, gr 3-5)** (n=123)

| Question type | OA | NBT | NF | MD | G | Total |
|---|---|---|---|---|---|---|
| Selected response (single) | 15 (60%) | 19 (70%) | 18 (67%) | 22 (76%) | 12 (80%) | 86 |
| Multi-select | 2 (8%) | 1 (4%) | 1 (4%) | 2 (7%) | · | 6 |
| Constructed response (explain) | 8 (32%) | 7 (26%) | 8 (30%) | 5 (17%) | 3 (20%) | 31 |
| **Total** | 25 | 27 | 27 | 29 | 15 | 123 |

**i-Ready Diagnostic samples** (n=10)

| Question type | CC | OA | NBT | NF | MD | Total |
|---|---|---|---|---|---|---|
| Selected response (single) | 1 (100%) | 2 (100%) | 1 (100%) | · | 3 (60%) | 7 |
| Numeric / short answer | · | · | · | · | 2 (40%) | 2 |
| Draw / plot / shade | · | · | · | 1 (100%) | · | 1 |
| **Total** | 1 | 2 | 1 | 1 | 5 | 10 |

**i-Ready practice sets (K-5)** (n=129)

| Question type | CC | OA | NBT | NF | MD | Total |
|---|---|---|---|---|---|---|
| Selected response (single) | 2 (33%) | 1 (2%) | · | · | · | 3 |
| Numeric / short answer | 4 (67%) | 51 (89%) | 42 (95%) | 15 (88%) | 5 (100%) | 117 |
| Match / sort | · | 2 (4%) | 1 (2%) | · | · | 3 |
| Draw / plot / shade | · | 3 (5%) | · | 2 (12%) | · | 5 |
| Constructed response (explain) | · | · | 1 (2%) | · | · | 1 |
| **Total** | 6 | 57 | 44 | 17 | 5 | 129 |

**MathFish (IM + Fishtank, K-5)** (n=4428)

| Question type | CC | OA | NBT | NF | MD | G | Total |
|---|---|---|---|---|---|---|---|
| Selected response (single) | · | 1 (<1%) | 3 (<1%) | 5 (<1%) | 5 (<1%) | 2 (<1%) | 16 |
| Multi-select | · | 1 (<1%) | 3 (<1%) | 1 (<1%) | 3 (<1%) | 1 (<1%) | 9 |
| Numeric / short answer | 50 (16%) | 273 (28%) | 333 (28%) | 153 (22%) | 227 (29%) | 46 (10%) | 1082 |
| Match / sort | 2 (<1%) | 5 (<1%) | 6 (<1%) | 4 (<1%) | 2 (<1%) | 4 (<1%) | 23 |
| Draw / plot / shade | 2 (<1%) | 19 (2%) | 24 (2%) | 37 (5%) | 33 (4%) | 59 (13%) | 174 |
| Constructed response (explain) | 32 (10%) | 403 (42%) | 526 (44%) | 399 (57%) | 342 (43%) | 149 (32%) | 1851 |
| Open activity (no scorable answer) | 227 (73%) | 259 (27%) | 309 (26%) | 96 (14%) | 179 (23%) | 203 (44%) | 1273 |
| **Total** | 313 | 961 | 1204 | 695 | 791 | 464 | 4428 |


#### 10.3 Question type × grade

**Milestones (GaDOE EOG samples, gr 3-5)** (n=123)

| Question type | 3 | 4 | 5 | Total |
|---|---|---|---|---|
| Selected response (single) | 31 (72%) | 27 (68%) | 28 (70%) | 86 |
| Multi-select | 2 (5%) | 2 (5%) | 2 (5%) | 6 |
| Constructed response (explain) | 10 (23%) | 11 (28%) | 10 (25%) | 31 |
| **Total** | 43 | 40 | 40 | 123 |

**i-Ready Diagnostic samples** (n=10)

| Question type | K | 2 | 3 | 4 | 5 | Total |
|---|---|---|---|---|---|---|
| Selected response (single) | 2 (100%) | 2 (100%) | 1 (50%) | 2 (67%) | · | 7 |
| Numeric / short answer | · | · | · | 1 (33%) | 1 (100%) | 2 |
| Draw / plot / shade | · | · | 1 (50%) | · | · | 1 |
| **Total** | 2 | 2 | 2 | 3 | 1 | 10 |

**i-Ready practice sets (K-5)** (n=129)

| Question type | K | 1 | 2 | 3 | 4 | 5 | Total |
|---|---|---|---|---|---|---|---|
| Selected response (single) | 2 (13%) | 1 (6%) | · | · | · | · | 3 |
| Numeric / short answer | 9 (60%) | 14 (88%) | 22 (100%) | 25 (96%) | 22 (96%) | 25 (93%) | 117 |
| Match / sort | 2 (13%) | 1 (6%) | · | · | · | · | 3 |
| Draw / plot / shade | 2 (13%) | · | · | 1 (4%) | 1 (4%) | 1 (4%) | 5 |
| Constructed response (explain) | · | · | · | · | · | 1 (4%) | 1 |
| **Total** | 15 | 16 | 22 | 26 | 23 | 27 | 129 |

**MathFish (IM + Fishtank, K-5)** (n=4428)

| Question type | K | 1 | 2 | 3 | 4 | 5 | Total |
|---|---|---|---|---|---|---|---|
| Selected response (single) | · | 1 (<1%) | 3 (<1%) | 4 (<1%) | 3 (<1%) | 5 (<1%) | 16 |
| Multi-select | · | 1 (<1%) | 3 (<1%) | 1 (<1%) | 4 (<1%) | · | 9 |
| Numeric / short answer | 109 (19%) | 167 (25%) | 170 (28%) | 227 (27%) | 197 (23%) | 212 (25%) | 1082 |
| Match / sort | 6 (1%) | 5 (<1%) | 2 (<1%) | 4 (<1%) | 3 (<1%) | 3 (<1%) | 23 |
| Draw / plot / shade | 10 (2%) | 8 (1%) | 30 (5%) | 46 (5%) | 44 (5%) | 36 (4%) | 174 |
| Constructed response (explain) | 69 (12%) | 217 (32%) | 220 (36%) | 399 (47%) | 471 (55%) | 475 (55%) | 1851 |
| Open activity (no scorable answer) | 373 (66%) | 270 (40%) | 188 (31%) | 169 (20%) | 139 (16%) | 134 (15%) | 1273 |
| **Total** | 567 | 669 | 616 | 850 | 861 | 865 | 4428 |


#### 10.4 Which standards each question type concentrates on

Common Core standards (e.g. `3.OA.4`; sub-letters merged) with the most items of each type. *share* = that type's share of the standard's items (standards with ≥ 8 items in the source). Full per-standard counts: `tables/standard_by_type.csv`.

**MathFish** (standards with ≥ 8 items)

| Question type | Top standards: count (share of standard's items) |
|---|---|
| Selected response (single) | `1.MD.1` 1 (12%), `5.G.3` 1 (5%), `5.G.4` 1 (5%), `3.MD.7` 3 (4%), `2.NBT.4` 1 (4%), `5.NF.1` 2 (4%) |
| Multi-select | `2.MD.4` 1 (8%), `3.G.2` 1 (8%), `2.NBT.3` 1 (7%), `4.MD.1` 2 (5%), `1.NBT.5` 1 (5%), `2.OA.4` 1 (4%) |
| Numeric / short answer | `2.NBT.6` 7 (70%), `4.OA.1` 13 (68%), `K.CC.A` 6 (60%), `5.MD.1` 13 (50%), `2.NBT.3` 7 (50%), `4.NBT.B` 5 (50%) |
| Match / sort | `4.NF.7` 2 (14%), `K.MD.3` 1 (9%), `1.NBT.3` 3 (8%), `1.G.2` 1 (7%), `K.G.2` 1 (7%), `K.G.1` 1 (6%) |
| Draw / plot / shade | `2.G.2` 6 (67%), `4.MD.6` 8 (36%), `5.OA.3` 5 (36%), `5.G.2` 7 (33%), `4.G.3` 7 (29%), `5.G.1` 9 (29%) |
| Constructed response (explain) | `5.OA.A` 8 (89%), `4.NF.1` 33 (87%), `5.NF.2` 30 (86%), `5.NF.5` 38 (84%), `4.OA.5` 20 (83%), `5.MD.3` 9 (82%) |
| Open activity (no scorable answer) | `K.G` 19 (100%), `4.G.A` 10 (100%), `5.G.B` 21 (95%), `K.G.5` 17 (94%), `K.CC.6` 42 (89%), `2.G.A` 8 (89%) |

**Milestones** (standards with ≥ 3 items)

| Question type | Top standards: count (share of standard's items) |
|---|---|
| Selected response (single) | `3.NBT.1` 3 (100%), `3.MD.4` 2 (67%), `3.OA.4` 2 (67%), `3.MD.3` 2 (67%), `4.NBT.3` 2 (67%), `5.NF.2` 2 (67%) |
| Multi-select | `3.OA.4` 1 (33%), `4.OA.4` 1 (33%), `5.NBT.4` 1 (33%), `5.MD.5` 1 (33%), `4.NF.3` 1 (17%) |
| Constructed response (explain) | `4.NF.3` 3 (50%), `3.NBT.2` 2 (50%), `3.MD.4` 1 (33%), `3.MD.3` 1 (33%), `4.OA.4` 1 (33%), `4.NBT.3` 1 (33%) |

**i-Ready practice** (standards with ≥ 3 items)

| Question type | Top standards: count (share of standard's items) |
|---|---|
| Numeric / short answer | `3.OA.7` 9 (100%), `1.OA.6` 5 (100%), `2.OA.1` 4 (100%), `2.NBT.5` 4 (100%), `2.NBT.7` 4 (100%), `4.NBT.4` 4 (100%) |
| Draw / plot / shade | `5.NF.4` 1 (33%), `4.NF.3` 1 (25%) |
| Constructed response (explain) | `5.NBT.7` 1 (12%) |


#### 10.5 Visual content (multimodal) by source

| Visual category | Milestones (GaDOE EOG samples, gr 3-5) | i-Ready Diagnostic samples | i-Ready practice sets (K-5) | MathFish (IM + Fishtank, K-5) |
|---|---|---|---|---|
| Text only | 69 (56%) | · | 83 (64%) | 2343 (53%) |
| Table only | 7 (6%) | · | 7 (5%) | 198 (4%) |
| Code-drawable diagram | 44 (36%) | 2 (20%) | 33 (26%) | 952 (21%) |
| Illustration / photo | 3 (2%) | · | 6 (5%) | · |
| Interactive tool | · | 8 (80%) | · | · |
| Image, kind unknown (MathFish) | · | · | · | 935 (21%) |

Visual category × CCSS domain (share of the domain's items):

**Milestones (GaDOE EOG samples, gr 3-5)**

| Visual category | OA | NBT | NF | MD | G | Total |
|---|---|---|---|---|---|---|
| Text only | 20 (80%) | 22 (81%) | 15 (56%) | 7 (24%) | 5 (33%) | 69 |
| Table only | 2 (8%) | 1 (4%) | 1 (4%) | 3 (10%) | · | 7 |
| Code-drawable diagram | 2 (8%) | 4 (15%) | 11 (41%) | 17 (59%) | 10 (67%) | 44 |
| Illustration / photo | 1 (4%) | · | · | 2 (7%) | · | 3 |
| **Total** | 25 | 27 | 27 | 29 | 15 | 123 |

**MathFish (IM + Fishtank, K-5)**

| Visual category | CC | OA | NBT | NF | MD | G | Total |
|---|---|---|---|---|---|---|---|
| Text only | 198 (63%) | 529 (55%) | 739 (61%) | 388 (56%) | 282 (36%) | 207 (45%) | 2343 |
| Table only | 1 (<1%) | 42 (4%) | 57 (5%) | 39 (6%) | 46 (6%) | 13 (3%) | 198 |
| Code-drawable diagram | 42 (13%) | 111 (12%) | 145 (12%) | 168 (24%) | 308 (39%) | 178 (38%) | 952 |
| Image, kind unknown (MathFish) | 72 (23%) | 279 (29%) | 263 (22%) | 100 (14%) | 155 (20%) | 66 (14%) | 935 |
| **Total** | 313 | 961 | 1204 | 695 | 791 | 464 | 4428 |

Code-drawable diagram kinds (count of items showing each kind):

| Source | Diagram kinds |
|---|---|
| Milestones (GaDOE EOG samples, gr 3-5) | geometry_2d 9, fraction_model 7, area_grid 4, number_line 4, coordinate_grid 4, line_plot 4, ruler 3, picture_graph 2, clock 2, decimal_grid 2, geometry_3d 2, equal_groups_array 1, bar_graph 1, protractor 1, measurement_scale 1 |
| i-Ready Diagnostic samples | ruler 2, counters 1, number_line 1, geometry_3d 1, base_ten 1, protractor 1, geometry_2d 1, area_grid 1, ten_frame 1 |
| i-Ready practice sets (K-5) | counters 9, number_line 8, ten_frame 6, cubes 5, number_bond 4, ruler 2, equal_groups_array 2, fraction_model 2, base_ten 1, clock 1, decimal_grid 1, area_grid 1 |
| MathFish (IM + Fishtank, K-5) | geometry_2d 407, number_line 160, area_grid 138, fraction_model 86, geometry_3d 76, base_ten 72, counters 59, protractor 52, equal_groups_array 34, money 32, coordinate_grid 30, clock 29, line_plot 27, ten_frame 25, bar_graph 21, ruler 20, picture_graph 12, tape_diagram 3 |

#### 10.6 Problem context by source

| Context | Milestones (GaDOE EOG samples, gr 3-5) | i-Ready Diagnostic samples | i-Ready practice sets (K-5) | MathFish (IM + Fishtank, K-5) |
|---|---|---|---|---|
| Symbolic (bare numbers) | 45 (37%) | 8 (80%) | 76 (59%) | 856 (19%) |
| Word problem | 49 (40%) | 2 (20%) | 23 (18%) | 2398 (54%) |
| Visual model | 29 (24%) | · | 30 (23%) | 1174 (27%) |

#### 10.7 Milestones: question type × DOK level

| Question type | DOK 1 | DOK 2 | DOK 3 | Total |
|---|---|---|---|---|
| Selected response (single) | 33 (100%) | 49 (67%) | 4 (24%) | 86 |
| Multi-select | · | 5 (7%) | 1 (6%) | 6 |
| Constructed response (explain) | · | 19 (26%) | 12 (71%) | 31 |
| **Total** | 33 | 73 | 17 | 123 |

#### 10.8 How reliable is the MathFish tagger?

| Check | Agreement | Cohen's κ |
|---|---|---|
| Text tagger vs GaDOE's official item type (123 Milestones items) | 113/123 (92%) | 0.83 |
| Tagger vs our hand labels, held-out MathFish sample (blind; one rule fixed afterwards, see below) | 23/30 (77%) | 0.65 |
| Tagger vs our hand labels, tuning MathFish sample (rules were refined on it, optimistic) | 37/40 (92%) | 0.89 |
<!-- TABLES:END -->
