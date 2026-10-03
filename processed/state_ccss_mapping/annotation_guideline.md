# Annotation guideline: mapping state math standards to CCSS (K–5)

*Version 1.2, Sep 30, 2026.*

This guideline tells an annotator how to map one state's K–5 mathematics standards onto the Common
Core State Standards for Mathematics (CCSS), K–5. It was established by three annotators while
jointly adjudicating a complete mapping of Georgia's K–5 standards, and it is written to apply to any
state. Every rule is meant to be applied the same way by different annotators working alone; where a
judgment could go either way, the guideline states which way to go.

**How to use it.** Read sections 1–8 once before starting. While annotating, work from the
**quick reference** (section 9) and look up cases in **Find your case** below. Each rule is stated in
full in one place; other sections point to it.

## Contents

1. [The task](#1-the-task)
2. [Units](#2-units): which state and CCSS units to annotate and cite
3. [Reading a standard](#3-reading-a-standard): what one standard requires
4. [Comparing standards: the four tests](#4-comparing-standards-the-four-tests): whether two standards share a requirement, and which is inside which
5. [Relationship types](#5-relationship-types): what the seven labels mean, per row
6. [Decision procedure](#6-decision-procedure): finding the codes and labeling each row; step 5 which is inside which, step 6 split, subset, merge or superset
7. [Worked examples](#7-worked-examples): E1–E15
8. [What to record](#8-what-to-record)
9. [Quick reference](#9-quick-reference)

## Find your case

| If… | Rule | Example |
|---|---|---|
| the two standards share a topic but ask for different work | Test A (requirement) → `none` or drop the code | E13 |
| no CCSS code at any grade shares the requirement | `none` | E14 |
| the state standard is a general practice repeated at every grade | `none` unless it states a code's requirement | E15 |
| the wording differs but the requirement is the same | Test C (separate objective) → `exact` | E1 |
| one standard identifies and the other writes the same thing | Test C: receptive vs. productive form | E2 |
| one standard adds "explain", "justify" or "record with symbols" | Test C: an attached demand, not an objective | E7 |
| a method or tool is given with "e.g." or "such as" | Test C: an example, not a requirement | — |
| the number range, number type or place value differs | Test D (bounds): always matters | E5 |
| the only matching CCSS code is at another grade | grade alone never matters: `exact` if otherwise the same | E7, E8 |
| a CCSS code is a prerequisite or only a definition (e.g. 3.MD.5a) | Test B (not a match): don't cite it | E11 |
| the state standard matches a CCSS parent's general statement | Section 2: cite all its lettered parts | E10 |
| the state's guidance adds something the text doesn't say | Section 3.1: guidance interprets, never adds | — |
| the state standard matches one code and has an extra part | Step 3: look for a code that requires the extra part; none → `state_superset` (step 6B) | E3, E4 |
| several codes each cover part of the state standard | Step 6B: together they make up all of it → `merge`; something left over → `state_superset` | E9, E10, E11 |
| the state standard covers only part of a code, and no other standard covers the rest | Step 6A → `state_subset` | E6 |
| the two share some requirements, and each also has one the other lacks | Step 5 → `overlap`; it still counts as a piece | patterns 6–8 in section 5 |
| two or more state standards each cover a different part of one code | Step 6A → `split` | E12 |
| an earlier or narrower state standard covers part of a code another standard covers more fully | Step 6A → `state_subset` | 4.NBT.2 table in step 6 |
| you already marked a CCSS code `exact` and find a second state standard like it | Section 5, `exact` row: re-examine both | — |
| the state standard both adds and lacks something | Step 5 → `overlap` | 3.GSR.6.1 in step 6 |
| you are still unsure | Use the "when unsure" default in section 4.2 or step 6A; mark `low` confidence | — |

---

## 1. The task

For each state standard, record:

1. **which CCSS codes it corresponds to** (zero, one or more), and
2. **how it relates to each**: one of seven relationship types per (state standard, CCSS code) pair
   (section 5).

A "correspondence" means the two standards require the same learning of students. It does not mean
they are on the same topic.

---

## 2. Units

**State side.** Annotate each state standard at its **lowest level**: the smallest unit the state
itself numbers or letters (e.g. Georgia `K.NR.1.1`; a lettered part of a Virginia standard, `3.MG.2 a)`).
Sub-points under that unit (e.g. Roman numerals i, ii under a lettered part) belong to it and are not
annotated separately. Each unit gets one row per CCSS code it corresponds to, or one row with no code
(section 8).

**CCSS side.** Cite **leaf codes**: a CCSS standard's lettered parts where it has them (e.g. `3.MD.7a`,
`3.MD.7b`), otherwise the standard itself (e.g. `3.MD.6`). Never cite a parent standard that has
lettered parts (e.g. `3.MD.7`).

- The state standard matches the parent's general statement → cite **all** its lettered parts (E10).
- It matches only some parts → cite **those**.

---

## 3. Reading a standard

This section is about one standard at a time: what it requires. Section 4 compares two.

### 3.1 The standard's own text sets the requirement

What a standard requires is what its own text says. The surrounding context (domain, cluster, parent
standard) and the state's guidance (examples, strategies, limits) are used only to **interpret** that
text: what a term means, which numbers or representations are intended, what is out of scope at that
grade. Context and guidance never **add** a requirement the text doesn't state.

> Example: Georgia's guidance for 3.NR.1.2 ("compare multi-digit numbers up to 10,000…") mentions dot
> plots and bar graphs as one setting for comparing numbers. The standard's text asks only to compare
> numbers, so graphing is not part of its requirement.

*Why:* states' guidance differs greatly in length and detail, from standard to standard and from state
to state. Reading the requirement from the text keeps annotators consistent and makes mappings of
different states comparable. It is not a judgment that the guidance matters less for teaching.

### 3.2 Describe the core requirement

Describe each standard (the state standard and each candidate CCSS code) by:

- **Action:** what students must do (count, identify, compare, represent, compute, solve problems,
  explain, draw, create, measure…).
- **Content:** the mathematics the action applies to (e.g. fractions with the same numerator or
  denominator; area of rectangles).
- **Bounds:** limits on that content (number ranges, place values, number types, denominators, number
  of steps, which cases).

A standard can have more than one requirement (e.g. "measure lengths … **and** show the data on a
line plot"). List each separately.

---

## 4. Comparing standards: the four tests

Comparing a state standard with a CCSS code comes down to two questions. The four tests answer them;
the decision procedure (section 6) applies them, and they are referred to by letter throughout.

| Question | Tests | What the answer decides |
|---|---|---|
| 1. Do the two standards share a requirement? | A (requirement), B (not a match) | yes → the pair gets a row; no → no row (step 3) |
| 2. Which is inside which? | C (separate objective), D (bounds) | which differences matter; a difference that matters means the standard that has it is not inside the other (the one without it may still be inside). That gives the label's first column in section 5: each inside the other, one inside the other, or neither (step 5) |

### 4.1 Do the two standards share a requirement? (Tests A and B)

#### Test A (requirement): shared requirement, not shared topic

Two standards correspond only if they share a requirement: the same action on the same content (one
whole requirement, or one part of it). Being about the same topic is not enough. Differences in bounds
don't prevent a match; they decide which standard is inside which (Test D).

> Identifying coins and their values (Georgia K.NR.1.4) and solving word problems with coins (CCSS
> 2.MD.8) share a topic, not a requirement.

#### Test B (not a match): not every related code is a match

Do not cite a CCSS code that is:

- **a prerequisite** the state standard builds on but doesn't itself state;
- **a base definition** the state standard assumes but doesn't state (e.g. CCSS 3.MD.5a, "A square with
  side length 1 unit, called 'a unit square,' is said to have 'one square unit' of area…"). A state
  standard that uses the concept matches the CCSS code that uses it (e.g. 3.MD.5b, 3.MD.6), not the
  definition;
- **a same-topic code that asks for a different action** (Test A);
- **a code from a distant grade that only shares the topic.** A match can be at any K–5 grade (states
  teach some content earlier or later than CCSS), but a code two or more grades away must require the
  same action on the same content at a comparable level.

### 4.2 Which is inside which? (Tests C and D)

When one standard has something the other doesn't, the difference either **matters** (the standard
that has it is not inside the other) or is **ignored**. For example, if a code has a part the state
standard lacks, the code is not inside the state standard, but the state standard can still be inside
the code (`split` or `state_subset`, with other standards covering the rest). Test C decides for differences in what students
do; Test D for differences in bounds. Grade never matters: the same requirement at another grade is
`exact` (section 5). **When unsure** whether a difference matters, treat it as ignored, and mark the
row `low` confidence (section 8).

#### Test C (separate objective): does a difference in what students do matter?

A difference matters only if it is **a separate learning objective**: something a teacher would plan,
teach and assess as its own goal.

**Matters** (the standard that has it is not inside the other):

- a different product or skill: making a line plot, drawing figures, solving word problems, a second
  operation, counting backward as well as forward, measuring elapsed time;
- fluency ("fluently", "demonstrating fluency"): performing a task fluently and performing the same
  task without a fluency requirement are treated as different. Both documents define fluency as its own
  expectation (CCSS: "fast and accurate"; Georgia: able to "choose flexibly among methods and strategies
  to solve mathematical problems accurately and efficiently"). When both standards ask for fluency,
  treat it as the same, even though the definitions differ. CCSS's "know from memory" counts as
  fluency;
- a different or wider number range, number type, place value or set of cases (Test D).

**Ignored:**

- wording, phrasing, emphasis (but not "fluently", above);
- other words about how the action is done, such as "mentally" or a specific procedure ("using the
  standard algorithm"): unlike fluency, neither document defines these as a separate expectation;
- methods, tools or representations given as examples ("e.g.", "such as", "for example", "using
  objects or drawings");
- a demand attached to the same task: recording the result with symbols, justifying or explaining the
  result, using a model to show it;
- receptive and productive forms of the same skill on the same content (identifying written numerals
  vs. writing them, when both standards require representing quantities with numerals);
- ordinary components of the task (finding the value of a group of coins as part of solving money
  problems);
- a general setting ("in authentic problems", "in real-world contexts"), unless the other standard's
  requirement is specifically problem solving.

*Why explaining and justifying are ignored:* the question is whether two standards target the same
learning, not how that learning is shown. Explaining and justifying are expected across all standards
(e.g. CCSS Mathematical Practice 3), so counting them would make most pairs differ on wording alone.
They are still worth recording: note a missing "explain" or "justify" in the rationale.

#### Test D (bounds): a difference in bounds always matters

A different number range (to 20 vs. to 100), number type (whole numbers vs. fractions vs. decimals),
place value (to hundredths vs. to any place), denominators, number of digits, number of steps, or set
of cases. The standard with the narrower bounds is inside the other (e.g. rounding to hundredths is
inside rounding to any place); if each is wider in a different way, neither is inside the other. The
range of a fluency expectation is a bound too: fluently within 10 is inside fluently within 20.

---

## 5. Relationship types

Each row of the annotation is one **(state standard, CCSS code) pair**, and each row gets one of seven
labels describing **that pair** (section 8). A state standard with several codes has several rows,
and they may carry different labels. This section says what each label means; section 6 says how to
choose one.

The labels rest on one question: **which standard is inside which?** One standard is inside another
when everything it requires (every separate objective and bound) is also required by the other.
Differences that are not separate objectives (Test C), such as a missing "explain why", don't matter;
neither does grade.

| Label | In short | Which is inside which? | And |
|---|---|---|---|
| `exact` | same standard, at any grade | each inside the other | a state standard has at most one `exact` row, and a CCSS code is `exact` with at most one state standard. If a second state standard seems `exact` with the same code, re-examine both: usually each covers a separate part of it (`split`), or one of them differs in scope |
| `split` | the state standard is a piece of the code | the state standard is inside the code | the state standards that cover parts of the code together make up all of the code, and this row's state standard is needed for that |
| `state_subset` | the state asks for less | the state standard is inside the code | the state standards that cover parts of the code do not make up all of the code; or they do, but this row's state standard is not needed for that |
| `merge` | the code is a piece of the state standard | the code is inside the state standard | the CCSS codes that cover parts of the state standard together make up all of the state standard, and this row's code is needed for that |
| `state_superset` | the state asks for more | the code is inside the state standard | the CCSS codes that cover parts of the state standard do not make up all of the state standard (some part of the state standard is covered by no CCSS code); or they do, but this row's code is not needed for that |
| `overlap` | they share some requirements, and each also has a requirement the other lacks | neither | the row still counts as a piece on both sides: it helps the state standards that cover parts of the code make up the code, and the CCSS codes that cover parts of the state standard make up the state standard |
| `none` | no CCSS counterpart | — | no CCSS K–5 code shares any of the state standard's requirements; one row, with no code |

**Pieces.** A code's pieces are the state standards that cover part of it: its `split`, `state_subset`
and `overlap` rows. A state standard's pieces are the codes that cover part of it: its `merge`,
`state_superset` and `overlap` rows. An `overlap` row keeps its own label but counts as a piece on both
sides at once, like a split piece for the code and a merge piece for the state standard: it can help
the other rows make up a whole (`split` or `merge`).

**`merge` mirrors `split`.** Both ask whether the pieces make up a whole, from opposite sides:

| | One CCSS code, several state standards | One state standard, several CCSS codes |
|---|---|---|
| The pieces make up the **whole** | `split` on each state standard inside the code | `merge` on each code inside the state standard |
| The pieces do not make up the whole | `state_subset` | `state_superset` |
| A piece that is neither inside nor contains | `overlap` (and it still counts toward making up the whole) | `overlap` (likewise) |

**Common patterns.** In these cases, A, B, C and X are CCSS codes; R, S, T, U and V are state standards;
lowercase letters are parts of a standard (a1 and a2 are the two parts of A). "y" is a part that no
CCSS code requires.

| # | Pattern | Standards | Rows |
|---|---|---|---|
| 1 | Split | A = a1 + a2; S = a1; T = a2 | S–A `split`, T–A `split`: S and T together make up A |
| 2 | Split plus an earlier, narrower pass | as in 1, plus R = a smaller-number version of a1 | S–A `split`, T–A `split`, R–A `state_subset`: A is made up without R |
| 3 | Merge | S = all of A + all of B | S–A `merge`, S–B `merge`: A and B together make up S |
| 4 | Merge plus a code that isn't needed | S = all of B + all of C; A is inside S, but B already covers A's part more fully | S–B `merge`, S–C `merge`, S–A `state_superset`: S is made up without A |
| 5 | Superset | S = all of A + y | S–A `state_superset`: y is covered by no code |
| 6 | Overlap pieces completing two splits | A = a1 + a2; B = b1 + b2; S = a1 + b1; T = a2; U = b2 | S–A `overlap`, S–B `overlap` (S has something each code lacks, and each code has something S lacks); T–A `split` (T and the overlap piece S make up A); U–B `split` (U and S make up B) |
| 7 | An overlap piece completing a merge | X = x1 + x2; S = all of X; T = all of A + x1 | S–X `exact`; T–X `overlap` (T has A, which X lacks; X has x2, which T lacks); T–A `merge` (A and the overlap piece X make up T). X has different labels on different rows. |
| 8 | Overlap that isn't needed | V = all of A; S = a1 + y | V–A `exact`; S–A `overlap` (S has y, which A lacks; A has a2, which S lacks) |

Section 6 applies these rules to Georgia standards (steps 5–6), and section 7 has worked examples.

---

## 6. Decision procedure

Steps 1–4 find the codes, one row each; steps 5–6 label each row. Record the step at which you decided
in the row's rationale.

### Step 1. Describe

Describe the state standard's core requirement: action, content, bounds (section 3.2).

### Step 2. Search

Search the whole CCSS list for candidate codes: every domain and every grade. Start at the state
standard's own grade and domain, then widen. States organize content differently (e.g. a state may
place area, perimeter, volume and angle measure under geometry, where CCSS places them under
Measurement and Data).

### Step 3. Keep the codes that share a requirement

Keep a code if the state standard states one of its requirements, all of it or one of its parts:
the action on the content (Test A). Sharing a detail, an example or the topic is not enough.

- **Drop** prerequisites, assumed definitions, same-topic codes with a different action, and
  distant-grade topic matches (Test B).
- **Check the neighbours.** Once you find one match, check its lettered siblings and the other codes in
  its cluster: state standards often combine several CCSS codes.
- **Look up every part of the state standard.** For each part not yet covered by a kept code, search all
  grades and domains for a code that requires it, and keep it if there is one. A part that no code
  requires stays uncovered (it can make the standard a `state_superset`, step 6).

### Step 4. Count the codes kept

- **0** → one row, `none`. Stop.
- **1 or more** → one row per code. Label each row with steps 5–6.

### Step 5. Which is inside which?

For each row, compare the state standard with the code (Tests C and D; grade doesn't matter):

- **Each is inside the other** (essentially the same requirement) → `exact`. Stop.
- **Neither is inside the other** (they share some requirements, and each also has a separate
  objective or bound the other lacks) → `overlap`. Stop.
- **The state standard is inside the code** (the code has more) → step 6, part A.
- **The code is inside the state standard** (the state standard has more) → step 6, part B.

For how these labels combine across rows (e.g. an `overlap` piece completing a `split`), see the
common patterns in section 5.

### Step 6. Do the pieces make up the whole?

**Part A: the state standard is inside the code.** Look at **all** the code's pieces (every state
standard that covers part of it, including `overlap` rows), and ask:

> **Which standards, together, make up the full CCSS code: all of its parts?**

| Situation | Label on this row |
|---|---|
| This row's state standard is one of the state standards that together cover all of the code's parts | `split` |
| This row's state standard covers a part that another state standard already covers more fully (typically an earlier, narrower pass: smaller numbers, fewer cases, an earlier grade) | `state_subset`: this row's state standard contributes to learning the code, but the full code is made up without it |
| The same parts are covered by more than one set of standards (e.g. in grade 3 and again, more fully, in grade 4) | `split` for the set with the fuller scope, usually at or nearest the code's grade; `state_subset` for the others |
| No combination of the state's standards covers all of the code's parts | `state_subset` |
| Another state standard covers the full code by itself | `state_subset` |

Within a split, a part may be covered with somewhat narrower bounds than the code (e.g. time intervals
in quarter hours rather than minutes); note it in the rationale. What decides `split` is that the
standard is needed to cover one of the code's parts. **When unsure** whether this row's state
standard is needed to make up the code, choose `state_subset`, and mark the row `low` confidence.

**Example: CCSS 4.NBT.2** (grade 4, whole numbers up to 1,000,000): "Read and write multi-digit whole
numbers using base-ten numerals, number names, and expanded form. Compare two multi-digit numbers based
on meanings of the digits in each place, using >, =, and < symbols to record the results of
comparisons." It has two parts: read and write numbers, and compare numbers.

| Georgia standard | Covers | Needed to make up 4.NBT.2? | Label |
|---|---|---|---|
| 4.NR.1.1 (grade 4): "Read and write multi-digit whole numbers to the hundred-thousands place using base-ten numerals and expanded form." | read and write, grade-4 numbers | Yes | `split` |
| 4.NR.1.3 (grade 4): "Use place value reasoning to represent, compare, and order multi-digit numbers, using >, =, and < symbols to record the results of comparisons." | compare, grade-4 numbers | Yes | `split` |
| 3.NR.1.1 (grade 3): "Read and write multi-digit whole numbers up to 10,000 to the thousands using base-ten numerals and expanded form." | read and write, only up to 10,000 | No: 4.NR.1.1 already covers this part more fully | `state_subset` |
| 3.NR.1.2 (grade 3): "Use place value reasoning to compare multi-digit numbers up to 10,000, using >, =, and < symbols to record the results of comparisons." | compare, only up to 10,000 | No: 4.NR.1.3 already covers this part more fully | `state_subset` |

The two grade-4 standards together make up 4.NBT.2, so they are `split`. The grade-3 standards teach
the same parts earlier, with smaller numbers; the full code is made up without them, so each is a
`state_subset` of 4.NBT.2, not a split partner. (Note: the adjudicated Georgia mapping currently labels
all four `split`; it is to be re-adjudicated under this rule.)

**Contrast: CCSS 4.G.1** (grade 4): "Draw points, lines, line segments, rays, angles (right, acute,
obtuse), and perpendicular and parallel lines. Identify these in two-dimensional figures." A single
Georgia standard, 4.GSR.8.1, covers all of it, so it is `exact`. Georgia 3.GSR.6.1 (grade 3: "Identify
perpendicular line segments, parallel line segments, and right angles, identify these in polygons, and
solve problems involving…" them) covers only identifying, for fewer figures, and adds solving problems,
a separate objective (Test C): neither is inside the other, so it is `overlap`.

See also E12 (a two-standard split).

**Part B: the code is inside the state standard.** Look at **all** the CCSS codes that cover parts of
the state standard (including `overlap` rows), and ask:

> **Which CCSS codes, together, make up the full state standard: all of its parts?**

| Situation | Label on this row |
|---|---|
| This row's code is one of the CCSS codes that together cover all of the state standard's parts | `merge` |
| This row's code covers a part of the state standard that another CCSS code already covers more fully (e.g. an earlier-grade, narrower code) | `state_superset`: the full state standard is made up without this row's code |
| No combination of CCSS codes covers all of the state standard's parts: some part is covered by no CCSS code, and it is a separate objective or wider bounds (Tests C and D) | `state_superset` |

A `merge` needs at least two pieces. A code covered a bit narrowly (e.g. without a demand attached to
its task) still counts as inside: note it in the rationale.

| Georgia standard | Pieces | Left over | Rows |
|---|---|---|---|
| K.NR.2.1: "Count forward to 100 by tens and ones and backward from 20 by ones." | K.CC.1 (count to 100 by ones and tens) | Counting backward: a separate objective no CCSS code requires | K.CC.1 `state_superset` |
| 3.GSR.7.1: "Investigate area by covering the space of rectangles … using multiple copies of the same unit, with no gaps or overlaps, and determine the total area…" | 3.MD.5b (a figure covered without gaps or overlaps by n unit squares has area n), 3.MD.6 (measure areas by counting unit squares) | None; 3.MD.5a is only a definition (Test B) | both `merge` |
| 3.NR.4.4: "Recognize and generate simple equivalent fractions." | 3.NF.3a (fractions as equivalent when the same size or the same point on a number line, as Georgia's guidance interprets "equivalent"), 3.NF.3b (recognize and generate simple equivalent fractions) | None; 3.NF.3b's "Explain why the fractions are equivalent" is an attached demand (Test C): noted in the rationale | both `merge` |

---

## 7. Worked examples

All from the adjudicated Georgia mapping. Each gives the state text, the CCSS text, the label and
what decided it.

| Label | Examples |
|---|---|
| `exact` | E1, E2, E7 |
| `state_superset` | E3, E4, E8 |
| `state_subset` | E5, E6 |
| `overlap` | 3.GSR.6.1 (step 6), patterns 6–8 in section 5 |
| `merge` | E9, E10, E11 |
| `split` | E12 |
| `none` | E13, E14, E15 |

**E1. `exact`: wording differs, requirement is the same.**
- **Georgia K.NR.1.2:** "When counting objects, explain that the last number counted represents the
  total quantity in a set (cardinality), regardless of the arrangement and order."
- **CCSS K.CC.4b:** "Understand that the last number name said tells the number of objects counted.
  The number of objects is the same regardless of their arrangement or the order in which they were
  counted."
- **Decided by:** Test C. "Explain" and "understand" name the same conceptual requirement; content and
  bounds match.

**E2. `exact`: receptive vs. productive form of the same skill.**
- **Georgia K.NR.4.1:** "Identify written numerals 0-20 and represent a number of objects with a
  written numeral 0-20 (with 0 representing a count of no objects)."
- **CCSS K.CC.3:** "Write numbers from 0 to 20. Represent a number of objects with a written numeral
  0-20 (with 0 representing a count of no objects)."
- **Decided by:** Test C. Identifying vs. writing the same numerals is not a separate objective here;
  the core requirement, representing quantities 0–20 with numerals, is identical.

**E3. `state_superset`: an added separate objective no CCSS code requires.**
- **Georgia K.NR.2.1:** "Count forward to 100 by tens and ones and backward from 20 by ones."
- **CCSS K.CC.1:** "Count to 100 by ones and by tens."
- **Decided by:** Test C and step 6B. K.CC.1 is inside it; counting backward is a separate
  objective that no CCSS code requires, so it is left over.

**E4. `state_superset`: an added separate objective.**
- **Georgia 1.MDR.6.2:** "Tell and write time in hours and half-hours using analog and digital clocks,
  and measure elapsed time to the hour on the hour using a predetermined number line."
- **CCSS 1.MD.3:** "Tell and write time in hours and half-hours using analog and digital clocks."
- **Decided by:** Test C. Elapsed time is a separate objective.

**E5. `state_subset`: narrower bounds.**
- **Georgia 5.NR.4.3:** "Use place value understanding to round decimal numbers to the hundredths
  place."
- **CCSS 5.NBT.4:** "Use place value understanding to round decimals to any place."
- **Decided by:** Test D. Hundredths only, vs. any place.

**E6. `state_subset`: a missing separate objective no other standard covers.**
- **Georgia 3.MDR.5.4:** "Use rulers to measure lengths in halves and fourths (quarters) of an inch
  and a whole inch."
- **CCSS 3.MD.4:** "Generate measurement data by measuring lengths using rulers marked with halves and
  fourths of an inch. Show the data by making a line plot…"
- **Decided by:** Test C and step 6A. Making a line plot is a separate objective, and no other Georgia
  grade-3 standard covers it.

**E7. `exact` across grades: same requirement; attached demands are ignored.**
- **Georgia 4.NR.4.2 (grade 4):** "Compare two fractions with the same numerator or the same
  denominator by reasoning about their size and recognize that comparisons are valid only when the two
  fractions refer to the same whole."
- **CCSS 3.NF.3d (grade 3):** essentially the same text, plus "Record the results of comparisons with
  the symbols >, =, or <, and justify the conclusions, e.g., by using a visual fraction model."
- **Decided by:** Test C and step 5. Recording with symbols and justifying are demands attached to the
  same task, so each is inside the other: `exact`, although the grades differ.

**E8. `state_superset` across grades: scope wins over grade.**
- **Georgia 3.PAR.3.4 (grade 3):** "Use the meaning of the equal sign to determine whether expressions
  involving addition, subtraction, and multiplication are equivalent."
- **CCSS 1.OA.7 (grade 1):** "Understand the meaning of the equal sign, and determine if equations
  involving addition and subtraction are true or false."
- **Decided by:** Test D and step 6B. 1.OA.7 is inside the state standard; multiplication widens the
  content, so it is `state_superset`. The grade difference plays no part.

**E9. `merge`: two codes, one missing only an attached demand.**
- **Georgia 3.NR.4.4:** "Recognize and generate simple equivalent fractions."
- **CCSS 3.NF.3a and 3.NF.3b.**
- **Decided by:** section 3.1 and step 6B. The text states 3.NF.3b's core ("recognize and generate
  simple equivalent fractions"), and Georgia's guidance interprets "equivalent" as 3.NF.3a does: "two
  fractions are equal when they are the same size or on the same location on a number line". It does
  not state 3.NF.3b's "explain why", but that is an attached demand (Test C), so both codes are inside
  it, and together they make up all of it: both rows are `merge`, with the missing part noted in
  the rationale.

**E10. `merge`: the parent's general statement.**
- **Georgia 1.NR.1.2:** "Explain that the two digits of a 2-digit number represent the amounts of tens
  and ones."
- **CCSS 1.NBT.2a, 1.NBT.2b, 1.NBT.2c.**
- **Decided by:** section 2. It matches the general statement of 1.NBT.2 (a parent), so all three
  lettered parts are cited.

**E11. `merge` with an excluded definition.**
- **Georgia 3.GSR.7.1:** "Investigate area by covering the space of rectangles … using multiple copies
  of the same unit, with no gaps or overlaps, and determine the total area…"
- **CCSS 3.MD.5b and 3.MD.6, not 3.MD.5a.**
- **Decided by:** Test B. 3.MD.5a only defines a unit square; the state standard uses the concept
  without stating the definition.

**E12. `split`: two standards, each covering a separate objective of one code.**
- **Georgia 3.MDR.5.2:** "Tell and write time to the nearest minute and estimate time to the nearest
  fifteen minutes…"
- **Georgia 3.MDR.5.3:** "Solve meaningful problems involving elapsed time…"
- **CCSS 3.MD.1 (both):** "Tell and write time to the nearest minute and measure time intervals in
  minutes. Solve word problems involving addition and subtraction of time intervals in minutes…"
- **Decided by:** step 6A. Telling time and solving elapsed-time problems are separate objectives of
  3.MD.1; each Georgia standard covers one, and together they make up the code. Each is `split`,
  naming the other. (For an earlier, narrower standard that is `state_subset` rather than a split
  partner, see the 4.NBT.2 table in step 6.)

**E13. `none`: shared topic, different action.**
- **Georgia K.NR.1.4:** "Identify pennies, nickels, and dimes and know their name and value."
- **Decided by:** Test A. The only CCSS money standard, 2.MD.8, asks students to solve word problems
  with money: same topic, different action.

**E14. `none`: no CCSS standard with the requirement at any grade.**
- **Georgia 1.PAR.3.2:** "Identify, describe, and create growing, shrinking, and repeating patterns
  based on the repeated addition or subtraction of 1s, 2s, 5s, and 10s."
- **Decided by:** Test A. CCSS pattern standards begin in grade 3 and ask for different work (e.g.
  identifying arithmetic patterns and explaining them with properties of operations), so none shares
  this requirement.

**E15. `none`: a recurring general practice.**
- **Georgia (every grade K–5):** "Ask questions and answer them based on gathered information,
  observations, and appropriate graphical displays to solve problems relevant to everyday life."
- **Decided by:** Test A. A state standard that repeats in nearly the same words across grades as a
  general way of doing mathematics, rather than grade-specific content, corresponds to a CCSS code only
  if it states that code's specific requirement. This Georgia standard resembles the Standards for Mathematical
  Practice more than any grade's content standard.

---

## 8. What to record

**One row per (state standard, CCSS code) pair**, the same layout as the adjudicated Georgia mapping
(`states/ga/gold.csv`). A state standard with several codes gets one row per code; a CCSS code shared
by several state standards appears on each of their rows; a `none` standard gets one row with no code.

| Field | What to enter |
|---|---|
| `state_code` | The state standard's code |
| `ccss_code` | One CCSS leaf code; empty for `none` |
| `relationship` | One of the seven types, for this pair (section 5) |
| `split_with` | On a `split` row, and on an `overlap` row that helps make up this row's code: the other state standards that, together with this row's state standard, make up this row's code. Otherwise empty. |
| `merge_with` | On a `merge` row, and on an `overlap` row that helps make up this row's state standard: the other CCSS codes that, together with this row's code, make up this row's state standard. Otherwise empty. |
| `confidence` | `high`: the guideline decides it clearly; `medium`: a judgment within a clear rule; `low`: you used a "when unsure" default (section 4.2 or step 6A) |
| `rationale` | One or two sentences: the requirement matched, the decisive difference (if any), and the test or step that decided it (e.g. "Step 6, Test D: rounds to hundredths only, CCSS to any place"). |

A standard's rows may carry different labels, because each describes one pair. `split_with` and
`merge_with` record which rows belong together, including the `overlap` rows that help make up a whole.
An `overlap` row that helps on neither side (pattern 8 in section 5) leaves both empty; one that helps
on both sides fills both.

| Example | `state_code` | `ccss_code` | `relationship` | `split_with` | `merge_with` |
|---|---|---|---|---|---|
| Georgia merge | 3.NR.4.4 | 3.NF.3a | `merge` | | 3.NF.3b |
| | 3.NR.4.4 | 3.NF.3b | `merge` | | 3.NF.3a |
| Georgia split | 3.MDR.5.2 | 3.MD.1 | `split` | 3.MDR.5.3 | |
| | 3.MDR.5.3 | 3.MD.1 | `split` | 3.MDR.5.2 | |
| Georgia superset | K.NR.2.1 | K.CC.1 | `state_superset` | | |
| Georgia none | K.NR.1.4 | | `none` | | |
| Pattern 6 (section 5): S is part of two splits, one per row | S | A | `overlap` | T | B |
| | S | B | `overlap` | U | A |
| | T | A | `split` | S | |
| | U | B | `split` | S | |
| Pattern 7 (section 5): an overlap piece completing a merge | S | X | `exact` | | |
| | T | X | `overlap` | | A |
| | T | A | `merge` | | X |

**Before moving on, check:**
- every `split` row has `split_with` filled, and every `merge` row has `merge_with` filled;
- the partners agree: if row T–A lists S in `split_with`, the row S–A lists T (likewise for
  `merge_with`);
- each `split_with` group, with this row's state standard, makes up all of the code (step 6A); each
  `merge_with` group, with this row's code, makes up all of the state standard (step 6B);
- a `none` standard has exactly one row, with no code;
- no parent code with lettered parts is cited.

---

## 9. Quick reference

*A one-page summary; the full rules are in the sections named.*

**Units** (section 2). State standard at its lowest level. CCSS leaf codes only; if the state standard
matches a parent's general statement, cite all its lettered parts.

**Tests** (section 4). Question 1, a shared requirement: A, B. Question 2, which is inside which: C, D.
- **A (requirement):** the same action on the same content, not a shared topic; bounds may differ.
- **B (not a match):** don't cite prerequisites, assumed definitions, same-topic codes with a different
  action, or distant-grade topic matches.
- **C (separate objective):** a difference matters only if it is a separate learning objective, not
  wording, examples, recording/justifying, receptive vs. productive form, or ordinary components.
- **D (bounds):** different bounds always matter (range, number type, place value, cases, steps).

**Steps** (section 6).
1. **Describe** the requirement: action, content, bounds.
2. **Search** all grades and domains.
3. **Keep** codes that share a requirement, whole or a part (A, B); check siblings; look for a code for
   every part of the standard.
4. **Count:** 0 → one row, `none`; otherwise one row per code, labeled by steps 5–6.
5. **Which is inside which?** Each inside the other → `exact` (any grade); neither → `overlap`;
   standard inside code → 6A; code inside standard → 6B.
6. **Do the pieces make up the whole?**
   - A (state standard inside the code): the state standards covering parts of the code (incl.
     overlaps) make up all of the code, and this row's state standard is needed → `split`; otherwise
     `state_subset`.
   - B (code inside the state standard): the CCSS codes covering parts of the state standard (incl.
     overlaps) make up all of the state standard, and this row's code is needed → `merge`; otherwise
     `state_superset`.

**Always.**
- One `exact` per CCSS code.
- Grade alone is not scope.
- One label per row; a standard's rows may differ.
- `merge` mirrors `split`; `overlap` rows count as pieces on both sides.
- When unsure whether a difference matters, ignore it; when unsure whether a standard is needed to
  make up a code, choose `state_subset`. Mark such rows `low` confidence.
