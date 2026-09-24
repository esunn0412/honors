# Question-type codebook (K-5 math)

The category scheme is built **from the assessments first** (Georgia Milestones EOG and the
i-Ready Diagnostic). It is then applied unchanged to MathFish and the i-Ready practice
packets, so every source is counted with the same codes.

Each question is coded on **three separate dimensions**:

1. **Answer mode:** what the student has to do to answer.
2. **Structure:** one question, or several parts.
3. **Stimulus:** what the student looks at.

Keeping them separate avoids overlapping categories. For example, "Part A: pick one; Part B:
explain, with a number line" is *multi-part* on structure. Its parts are *select one* and
*write*, and its stimulus is a *diagram*.

Difficulty (DOK) and context (word problem vs. bare numbers) are **not** used to categorize
questions. DOK is printed only for Milestones, so it can't be compared across sources. It is
kept as a GaDOE label (`dok`) for reference. Context coding was dropped.

**Unit of analysis = one question.**

| Source | One question is… |
|---|---|
| Milestones | one sample item (duplicates across guides counted once) |
| i-Ready Diagnostic | one sample item |
| i-Ready practice | one numbered problem on a worksheet. Worksheet pages with no numbered problems (all of Kindergarten and 8 pages in grades 1-4) count as one question per page |
| MathFish | one problem / activity as the dataset gives it |

## 1. Answer mode: *what the student does to answer*

| Code | Name | What counts | Where the category comes from |
|---|---|---|---|
| `select_one` | Select one | Choose one answer from given options; circle one; true/false; yes/no; pick from a word bank | Milestones *Selected-Response* (4 options); i-Ready *Multiple-Choice* |
| `select_many` | Select many | Choose 2+ options ("Select TWO", "Select all", "Circle all") | Milestones *Technology-Enhanced: multi-select* (pick 2-3 of 5-6) |
| `enter` | Enter | Type or write a number, equation, expression, fraction, time or word form; fill a blank or a table cell | i-Ready *Short-Answer*; the answer blanks inside Milestones CR parts |
| `write` | Write | A written explanation or justification ("Explain", "How do you know?", "Write a word problem for…") | Milestones *Constructed-Response* (2 pt) and *Extended CR* (4 pt) |
| `construct` | Construct | Draw a model or array, shade a fraction, plot or label points on a number line or grid, draw clock hands | i-Ready *Number Line Item* (click to plot) |
| `match` | Match / order / sort | Connect, drag, sort into groups, put in order | i-Ready *Drag and Drop*; K practice "draw a line to match" |
| `dropdown` | Drop-down | Pick from a menu inside a sentence | i-Ready *Drop-Down Item* (the only public sample is grade 8, so there are no K-5 instances) |

**`open`: outside the scheme.** It is used only for MathFish, which is curriculum material.
It marks an activity with no single scorable answer: games and centers, teacher-led
routines, "notice and wonder", hands-on building. It is reported separately and is not an
answer mode.

**One part, several cues.** A single prompt such as "How many are left? Explain how you
know." is coded `write`. The explanation contains the number, which matches GaDOE's
labeling: any written part makes an item Constructed-Response. When one part has several
cues, the more demanding one wins: `write > construct > match > select_many > select_one > enter`.

## 2. Structure: *one question or several parts*

| Code | Meaning |
|---|---|
| `single` | One question with one answer mode |
| `multi_part` | Two or more parts, each answered separately. This covers explicit parts (Part A / Part B; a. / b.; "Problem 1 / Problem 2") and **item sets** (several questions about one shared situation, table or picture) |

- `part_modes` lists each part's answer mode **in order**, e.g. `["select_many", "select_one"]`
  for a Milestones TE item.
- A list of exercises under **one** prompt is a single question, not multi-part. For example:
  "Find the value of each expression: a. 3 × 10 b. 3 × 20". A question is multi-part only
  when at least two of its parts have a prompt of their own.

**`question_type`** combines the two dimensions for the main tables. It is the answer mode
for a single question, or `multi_part`.

How the official Milestones item types fall into this scheme:

| GaDOE item type | question_type |
|---|---|
| Selected-Response | `select_one` |
| Technology-Enhanced, multi-select | `select_many` |
| Technology-Enhanced, multi-part | `multi_part` (parts are `select_one` / `select_many` / `enter`) |
| Constructed-Response / Extended CR | `write`, or `multi_part` when the item has Part A / Part B (parts are usually `enter` + `write`) |

## 3. Stimulus: *what the student looks at*

`stimulus` is one category. `visuals` lists the specific kinds that are present.

| Code | Meaning | Kinds in `visuals` |
|---|---|---|
| `none` | Text only (numbers and symbols count as text) | — |
| `table` | A table of text or numbers | `table` |
| `diagram` | A structured math picture that a program could draw exactly from parameters | `number_line`, `ruler`, `clock`, `area_grid`, `fraction_model`, `decimal_grid`, `base_ten`, `ten_frame`, `counters`, `cubes`, `number_bond`, `equal_groups_array`, `tape_diagram`, `bar_graph`, `picture_graph`, `line_plot`, `coordinate_grid`, `geometry_2d`, `geometry_3d`, `protractor`, `measurement_scale`, `money` |
| `illustration` | A drawing or photo of real objects or scenes (nails, bottle caps, a fish to measure) | `illustration` |
| `interactive` | The student answers *by manipulating* an on-screen tool (i-Ready ruler, protractor, counters, click-to-plot) | `interactive` |
| `image_unknown` | A picture is present, but its kind isn't known from the text | — |

- **Pictures inside a table count as pictures.** A table whose cells hold shapes or models
  is coded by the picture (`diagram`, or `image_unknown` if the kind isn't named), and
  `visuals` also gets `table_with_pictures`. `table` is used only when the cells are text
  or numbers.
- **Several visuals:** the most demanding one wins, in the order
  `interactive > illustration > image_unknown > diagram > table > none`.

**How stimulus was coded:**

- **Milestones and i-Ready:** by hand from rendered page images, per item (Milestones and
  Diagnostic) or per worksheet (practice). A practice problem gets a picture only if its
  own region has a figure. The figure's kind comes from the problem or page text, or else
  from the worksheet's hand-coded kinds.
- **MathFish:** image placeholders come from the dataset's `elements` field. The kind comes
  only from what the text names ("number line", "tape diagram", "shaded", ...). The file
  type is **not** used as a proxy: a spot check found that most `.png` *and* `.jpeg` files
  are simple diagrams.

## How labels are assigned, and how they are checked

- **Milestones:** GaDOE's printed type settles single-choice items. For every other item,
  the extracted text blocks are split at "Part A / Part B". Each part's mode comes from its
  answer options, "Select TWO / THREE", explain / draw cues, or answer boxes.
- **i-Ready Diagnostic:** coded by hand from the sample screenshots.
- **i-Ready practice:** each problem's mode comes from its own prompt. A bare exercise such
  as "62,554 − 31,618" takes the page instruction ("Subtract.", "Draw a model…"). A page
  with no numbered problems takes the worksheet's hand-coded mode.
- **MathFish:** parts come from the numbered list items in the publisher's HTML, or from
  explicit part markers. Each part's mode comes from cue words. Centers, teacher-led
  activities and game-like activities are `open`.

All of these labels except the i-Ready Diagnostic ones are a **rule-based first pass**.
**They are checked by a person in the review page** (`review/index.html`): for every
question, the reviewer can correct the answer mode, structure, part modes and stimulus,
add a note, and export the corrections as CSV. The reported numbers should be treated as
provisional until that review is done.

## Other fields

- `official_type`, `points`, `dok` (Milestones only): as printed by GaDOE.
- `ccss_codes`: Common Core codes, normalized (`4.NBT.B.5` → `4.NBT.5`; old Georgia `MGSE3.OA.1` → `3.OA.1`).
  MathFish and i-Ready are left in Common Core; there is no Georgia translation.
- `ccss_standards`: the same codes at standard level, with sub-letters merged (`3.NF.3a` → `3.NF.3`).
- `ccss_domain`: the most common domain among the item's codes (CC, OA, NBT, NF, MD, G).
- `ga_codes` (Milestones only, extra information): the current Georgia K-12 (2023) code, from
  `processed/state_ccss_mapping/states/ga/mapping_final.json`.
- `standard_source`: `publisher` (MathFish, Milestones) or `assigned` (i-Ready; we chose the
  codes from the content because the source doesn't print them).
