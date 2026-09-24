# Question-type codebook (K-5 math)

Step 1 of the question-type work: a category scheme built **from the assessments first**
(Georgia Milestones EOG + i-Ready Diagnostic), then applied unchanged to MathFish and the
i-Ready practice packets so every source is counted with the same codes.

Each item is coded on four independent dimensions. Keeping them separate avoids categories
that overlap ("is a word problem with a number line a *word problem* or a *number line
item*?" — it is both, on different axes).

## A. Response format — *what the student has to produce*

| Code | Name | What counts | Where the category comes from |
|---|---|---|---|
| `SR` | Selected response (single) | Choose one answer from given options; circle one; true/false; yes/no | Milestones *Selected-Response* (4 options); i-Ready *Multiple-Choice* |
| `MS` | Multi-select | Choose 2+ correct options ("Select TWO", "Select all", "Circle all") | Milestones *Technology-Enhanced: Multi-Select* (pick 2-3 of 5-6) |
| `NUM` | Numeric / short answer | Type or write a number, equation, expression, fraction, time, word form; fill a blank or a table | i-Ready *Short-Answer*; Milestones answer blanks inside CR parts |
| `MATCH` | Match / sort / order | Connect, drag, sort into groups, put in order | i-Ready *Drag and Drop*; K practice "draw lines to match" |
| `DRAW` | Draw / plot / shade / label | Draw a model or array, shade a fraction, plot or label points on a number line or grid, draw clock hands | i-Ready *Number Line Item* (click to plot) |
| `DD` | Drop-down (inline choice) | Pick from a menu embedded in a sentence | i-Ready *Drop-Down Item* (only public sample is grade 8, so no K-5 instances) |
| `CR` | Constructed response | Written explanation or justification ("Explain", "How do you know?", "Write a word problem for…") | Milestones *Constructed-Response* (2 pt) and *Extended CR* (4 pt) |
| `ACT` | Open activity | No single scorable answer: games/centers, teacher-led number talks, "notice and wonder", hands-on building | Not an assessment format; needed only for MathFish (curriculum) |

**Primary format.** An item can contain several formats (e.g. Part A multiple choice +
Part B explain). `primary_format` = the **most demanding** format present, in the order
`CR > DRAW > NUM > MATCH > MS > SR`. This follows GaDOE's own labeling: any written part makes
the whole item Constructed-Response. It matched GaDOE's labels better (92%) than "most frequent
format" (78%).

- **Exception:** an i-Ready practice worksheet has 4-20 separate problems, so it takes its most
  common format. The other label is kept as `gadoe_rule_format`.
- `formats` lists every format present. Multi-part structure is a separate flag, `multi_part`.

## B. Context — *how the problem is framed*

| Code | Meaning |
|---|---|
| `word_problem` | A story or real-world situation (people, objects, quantities with units) |
| `visual_model` | No story; the task is about a picture or model (shaded shape, array, number line, cubes) |
| `symbolic` | Bare numbers or expressions (`724 + 152 = ?`, "Round 5.816") |

## C. Visual content — *what would have to be rendered* (the multimodal question)

`visuals` lists the kinds present. `visual_category` summarizes what that means for generation:

| Category | Meaning | Kinds |
|---|---|---|
| `none` | Text only; an LLM can generate it directly | — |
| `table` | Needs a table only (Markdown/HTML is enough) | `table` |
| `code_generatable` | Structured diagram that a program can draw exactly (SVG, matplotlib, TikZ) from parameters | `number_line`, `ruler`, `clock`, `area_grid`, `fraction_model`, `decimal_grid`, `base_ten`, `ten_frame`, `counters`, `cubes`, `number_bond`, `equal_groups_array`, `tape_diagram`, `bar_graph`, `picture_graph`, `line_plot`, `coordinate_grid`, `geometry_2d`, `geometry_3d`, `protractor`, `measurement_scale`, `money` |
| `illustration` | A drawing or photo of real objects or scenes (nails, bottle caps, a fish to measure). Needs image generation or an asset library, and its measurements must be exact | `illustration` |
| `interactive` | The response is given *by manipulating* an on-screen tool (i-Ready ruler/protractor/counters, click-to-plot) | `interactive` |
| `image_unknown` | MathFish only: an image is present but its kind couldn't be determined from the text (see note below) | — |

When an item has several visuals, `visual_category` takes the most demanding one:
`interactive > illustration > image_unknown > code_generatable > table > none`.

*How visuals were coded.* Milestones and i-Ready: by hand, from rendered page images (their
figures are vector graphics that text extraction can't see). MathFish: image placeholders
come from the dataset's `elements` field, and the kind comes only from what the item text
names ("number line", "tape diagram", "shaded", ...). If the text doesn't name it, the item
is `image_unknown`. The file type is **not** used as a proxy: a spot check of 32 real
images found that most `.png` *and* `.jpeg` files are simple diagrams (see the README).

## D. Cognitive demand (Milestones only)

`dok` = Webb's Depth of Knowledge level (1 recall, 2 skill/concept, 3 strategic thinking),
as printed by GaDOE for every sample item. The other sources don't label DOK, and we don't
infer it.

## Standards fields (all sources)

- `ccss_codes`: Common Core codes, normalized (`4.NBT.B.5` → `4.NBT.5`; old Georgia `MGSE3.OA.1` → `3.OA.1`).
  MathFish and i-Ready are left in Common Core; there is no Georgia translation.
- `ccss_standards`: the same codes at standard level, with sub-letters merged (`3.NF.3a` → `3.NF.3`).
- `ccss_domain`: the most common domain among the item's codes (CC, OA, NBT, NF, MD, G).
- `ga_codes` (Milestones only, extra information): the current Georgia K-12 (2023) code, from
  `processed/state_ccss_mapping/states/ga/mapping_final.json`.
- `standard_source`: `publisher` (MathFish, Milestones) or `assigned` (i-Ready; we chose the
  codes from the content because the source doesn't print them).
