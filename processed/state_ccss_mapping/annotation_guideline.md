# Annotation guideline: mapping state math standards to CCSS (K–5)

*Version 1.2, Sep 30, 2026.*

This guideline tells an annotator how to map one state's K–5 mathematics standards onto the Common
Core State Standards for Mathematics (CCSS), K–5. It was established by three annotators while
jointly adjudicating a complete mapping of Georgia's K–5 standards, and it is written to apply to any
state. Every rule is meant to be applied the same way by different annotators working alone; where a
judgment could go either way, the guideline states which way to go.

**How to use it.** Read sections 1–8 once before starting. While annotating, work from the
**quick reference** (section 9). Each rule is stated in full in one place; other sections point to
it.

## Contents

1. [The task](#1-the-task)
2. [Units](#2-units): which state and CCSS units to annotate and cite
3. [Reading a standard](#3-reading-a-standard): what one standard requires
4. [Comparing standards: the four tests](#4-comparing-standards-the-four-tests): whether two standards share a requirement, and which is inside which
5. [Relationship types](#5-relationship-types): what the seven labels mean, per row
6. [Decision procedure](#6-decision-procedure): finding the codes and labeling each row; step 5 which is inside which, step 6 split, subset, merge or superset
7. [Worked examples](#7-worked-examples): E1–E20
8. [What to record](#8-what-to-record)
9. [Quick reference](#9-quick-reference)

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
(section 8). Annotate **content standards only**: a state's own practice standards (e.g. Georgia
`K.MP.1`–`K.MP.8` at each grade) are not annotated, because they correspond to the CCSS Standards for
Mathematical Practice, which are not in the K–5 content list.

**CCSS side.** Cite **leaf codes**: a CCSS standard's lettered parts where it has them (e.g. `3.MD.7a`,
`3.MD.7b`), otherwise the standard itself (e.g. `3.MD.6`). Never cite a parent standard that has
lettered parts (e.g. `3.MD.7`).

- The state standard matches the parent's general statement → cite **all** its lettered parts (E11).
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
- **a code two or more grades above the state standard, covered only with narrower bounds** (Test D):
  an early, simpler version of later content.

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
  result, using a model to show it, estimating alongside measuring or telling time. When such an action
  is a standard's whole task (e.g. CCSS 2.MD.3, "Estimate lengths using units of inches, feet,
  centimeters, and meters"), consider it as that standard's main action;
- receptive and productive forms of the same skill on the same content (identifying written numerals
  vs. writing them, when both standards require representing quantities with numerals);
- ordinary components of the task (finding the value of a group of coins as part of solving money
  problems; ordering numbers as part of comparing them);
- a general setting ("in authentic problems", "to solve problems", "in real-world contexts") when
  problems are only the setting for another action (e.g. "fluently add and subtract within 1000 to
  solve problems": the action is fluent computation). When solving problems is the standard's main
  action, "solve problems" corresponds to CCSS "solve word problems".

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
| `merge` | the code is a piece of the state standard | the code is inside the state standard | the CCSS codes that cover parts of the state standard together make up all of the state standard |
| `state_superset` | the state asks for more | the code is inside the state standard | the CCSS codes that cover parts of the state standard do not make up all of the state standard: some part of it (a separate objective or wider bounds) is covered by no CCSS code |
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
| 4 | A code that isn't needed | S = all of B + all of C; A is inside S, but B already covers A's part more fully | S–B `merge`, S–C `merge`; A is **not cited** (step 3): B and C make up S without it |
| 5 | Superset | S = all of A + y | S–A `state_superset`: y is covered by no code |
| 6 | Overlap pieces completing two splits | A = a1 + a2; B = b1 + b2; S = a1 + b1; T = a2; U = b2 | S–A `overlap`, S–B `overlap` (S has something each code lacks, and each code has something S lacks); T–A `split` (T and the overlap piece S make up A); U–B `split` (U and S make up B) |
| 7 | An overlap piece completing a merge | X = x1 + x2; S = all of X; T = all of A + x1 | S–X `exact`; T–X `overlap` (T has A, which X lacks; X has x2, which T lacks); T–A `merge` (A and the overlap piece X make up T). X has different labels on different rows. |
| 8 | Overlap that isn't needed | V = all of A; S = a1 + y | V–A `exact`; S–A `overlap` (S has y, which A lacks; A has a2, which S lacks) |

Section 6 applies these rules to Georgia standards (steps 5–6), and section 7 has worked examples.

---

## 6. Decision procedure

Steps 1–4 find the codes and make one row per code; steps 5–6 label each row. In each row's rationale,
record the step that decided it.

### Step 1. Describe

Describe the state standard's core requirement: action, content, bounds (section 3.2).

### Step 2. Search

Search the whole CCSS list, every domain and grade, starting at the state standard's own grade and
domain (states organize content differently: e.g. Georgia puts area under geometry, CCSS under
Measurement and Data). Search in both directions:

- **Every part of the state standard:** look for a code that requires each part. Don't stop at the
  first match; a state standard often combines several codes, from any domain or grade. A part that no
  code requires stays uncovered.
- **Every part of the code**, for a code the state standard covers only partly: search the state's
  standards, at every grade, for the parts it doesn't cover. These are its possible split partners.

### Step 3. Keep

Keep a candidate code only if the state standard states one of its requirements, whole or a part
(Test A); a shared detail, example or topic is not enough. Drop prerequisites, definitions, same-topic
codes with a different action, and later codes the standard only introduces (Test B).

For each part of the state standard, cite the code that matches it **most closely**. A code is cited
whenever it is the closest match for some part, even if it doesn't help make up a whole (e.g. an
`overlap` or `state_subset` row). A code whose shared part another code matches more closely is not
cited: it relates to other standards, as a prerequisite or an earlier or later pass.

### Step 4. Count

**0 codes** → one row, `none`. **1 or more** → one row per code, labeled by steps 5–6.

### Step 5. Which is inside which?

Compare the state standard with the row's code (Tests C and D; grade never matters):

| Comparison | Label |
|---|---|
| each is inside the other | `exact` |
| neither is inside the other | `overlap` (it can still help make up a whole; fill `split_with` and `merge_with` from step 2, section 8) |
| the state standard is inside the code | step 6A |
| the code is inside the state standard | step 6B |

Section 5's common patterns show how labels combine across rows.

### Step 6. Do the pieces make up the whole?

**A. The state standard is inside the code.** Of all the state standards that cover part of the code
(step 2, including `overlap` rows), which together make up all of it?

| This row's state standard is… | Label |
|---|---|
| needed: with the others, it covers all of the code's parts | `split` |
| not needed: another standard already covers its part more fully (e.g. an earlier, narrower grade), one standard covers the whole code, or no combination covers all of the code | `state_subset` |

If two sets of standards each make up the code (e.g. in grade 3 and again, more fully, in grade 4),
only the set with the fuller scope, usually nearest the code's grade, is `split`. A part covered with
somewhat narrower bounds (e.g. quarter hours rather than minutes) still counts; note it in the
rationale. **When unsure** whether this row's state standard is needed, choose `state_subset` and mark
the row `low` confidence. Examples: E15, E16, E17.

**B. The code is inside the state standard.** Of all the codes that cover part of the state standard
(the rows from steps 2–4, including `overlap` rows), which together make up all of it?

| The cited codes… | Label on each row whose code is inside the state standard |
|---|---|
| together cover all of the state standard's parts | `merge` |
| leave some part uncovered: a separate objective or wider bounds (Tests C, D) that no code requires | `state_superset` |

A `merge` needs at least two pieces. A code missing only an attached demand (e.g. "explain why") still
counts as inside; note it in the rationale. Examples: E5, E10, E12, E13, E14.

---

## 7. Worked examples

From the Georgia mapping. Each gives the texts, the rows to record (section 8), what decided them and
what the example shows. Where the adjudicated Georgia mapping currently differs, the example says so;
those rows are being re-adjudicated.

| Label | Examples |
|---|---|
| `exact` | E1, E2, E3, E4, E14 |
| `state_superset` | E5, E6, E7 |
| `state_subset` | E3, E8, E9, E16 |
| `merge` | E10, E11, E12, E13, E14 |
| `split` | E15, E16, E17 |
| `overlap` | E13, E14, E18 |
| `none` | E19, E20 |

**E1. `exact`: different wording, same requirement.**
- **Georgia K.NR.1.2:** "When counting objects, explain that the last number counted represents the
  total quantity in a set (cardinality), regardless of the arrangement and order."
- **CCSS K.CC.4b:** "Understand that the last number name said tells the number of objects counted.
  The number of objects is the same regardless of their arrangement or the order in which they were
  counted."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| K.NR.1.2 | K.CC.4b | `exact` | | | high |

- **Decided by:** step 5, Test C. "Explain" and "understand" are each their standard's whole task, so
  they are compared as main actions, and they name the same conceptual requirement. Content and bounds
  match.
- **Shows:** the most common `exact`: the wording differs, the learning doesn't.

**E2. `exact`: receptive and productive forms of the same skill.**
- **Georgia K.NR.4.1:** "Identify written numerals 0-20 and represent a number of objects with a
  written numeral 0-20 (with 0 representing a count of no objects)."
- **CCSS K.CC.3:** "Write numbers from 0 to 20. Represent a number of objects with a written numeral
  0-20 (with 0 representing a count of no objects)."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| K.NR.4.1 | K.CC.3 | `exact` | | | medium |

- **Decided by:** step 5, Test C. The second sentence is identical. Identifying vs. writing numerals
  are receptive and productive forms of the same skill (Ignored). Rationale notes "identifies rather
  than writes numerals".
- **Shows:** a difference that looks like an action but is ignored; medium confidence for a judgment
  within a clear rule.

**E3. `exact` across grades, with an earlier `state_subset`.**
- **Georgia 4.NR.4.2 (grade 4):** "Compare two fractions with the same numerator or the same
  denominator by reasoning about their size and recognize that comparisons are valid only when the two
  fractions refer to the same whole."
- **Georgia 3.NR.4.2 (grade 3):** "Compare two unit fractions by flexibly using a variety of tools and
  strategies."
- **CCSS 3.NF.3d (grade 3):** "Compare two fractions with the same numerator or the same denominator by
  reasoning about their size. Recognize that comparisons are valid only when the two fractions refer to
  the same whole. Record the results of comparisons with the symbols >, =, or <, and justify the
  conclusions, e.g., by using a visual fraction model."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 4.NR.4.2 | 3.NF.3d | `exact` | | | high |
| 3.NR.4.2 | 3.NF.3d | `state_subset` | | | high |

- **Decided by:** 4.NR.4.2, step 5, Test C: recording with symbols and justifying are demands attached
  to the same task (Ignored), so each is inside the other, a grade apart. 3.NR.4.2, steps 5 and 6A,
  Test D: unit fractions only, so it is inside 3.NF.3d; 4.NR.4.2 already covers the whole code, so it
  is not needed.
- **Shows:** `exact` at a different grade; attached demands ignored; a narrower standard is not needed
  when another covers the whole code. (The adjudicated mapping labels 4.NR.4.2 `different_grade`, a
  label this guideline no longer uses.)

**E4. `exact` through R4: "solve problems" is "solve word problems".**
- **Georgia 1.NR.2.1:** "Use a variety of strategies to solve addition and subtraction problems within
  20."
- **CCSS 1.OA.1:** "Use addition and subtraction within 20 to solve word problems involving situations
  of adding to, taking from, putting together, taking apart, and comparing, with unknowns in all
  positions, e.g., by using objects, drawings, and equations with a symbol for the unknown number to
  represent the problem."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 1.NR.2.1 | 1.OA.1 | `exact` | | | medium |

- **Decided by:** step 5, Test C. Solving problems is the standard's main action, so it corresponds to
  "solve word problems" (general setting entry). "A variety of strategies" and the CCSS "e.g." methods
  are hows. The situation types and unknown positions come from Georgia's guidance ("a variety of
  problem types within 20"), which interprets "problems" (section 3); hence medium confidence.
- **Shows:** "solve problems" as a main action; guidance interpreting the text without adding a
  requirement. (The adjudicated mapping labels it `split` with 1.NR.2.2; see E17.)

**E5. `state_superset`: an added part no CCSS code requires.**
- **Georgia K.NR.2.1:** "Count forward to 100 by tens and ones and backward from 20 by ones."
- **CCSS K.CC.1:** "Count to 100 by ones and by tens."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| K.NR.2.1 | K.CC.1 | `state_superset` | | | high |

- **Decided by:** step 2 finds no code for counting backward (K.CC.2 counts forward); step 5: K.CC.1 is
  inside, and counting backward is a separate objective (Matters); step 6B: the cited code leaves it
  uncovered.
- **Shows:** the plain superset (pattern 5), and why step 2 searches every part before step 6B.

**E6. `state_superset`: a much later code is not cited.**
- **Georgia 1.MDR.6.2 (grade 1):** "Tell and write time in hours and half-hours using analog and digital
  clocks, and measure elapsed time to the hour on the hour using a predetermined number line."
- **CCSS 1.MD.3 (grade 1):** "Tell and write time in hours and half-hours using analog and digital
  clocks."
- **Not cited, CCSS 3.MD.1 (grade 3):** "Tell and write time to the nearest minute and measure time
  intervals in minutes. Solve word problems involving addition and subtraction of time intervals in
  minutes, e.g., by representing the problem on a number line diagram."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 1.MDR.6.2 | 1.MD.3 | `state_superset` | | | high |

- **Decided by:** step 3, Test B: 3.MD.1 is two grades above and is covered only with narrower bounds
  (to the hour, not minutes), an early, simpler version of later content, so it is not cited. Step 5:
  1.MD.3 is inside; elapsed time is a separate objective (Matters). Step 6B: left uncovered.
- **Shows:** not citing a code (Test B) is different from ignoring a difference (Test C): elapsed time
  still matters.

**E7. `state_superset` across grades: wider content, not grade.**
- **Georgia 3.PAR.3.4 (grade 3):** "Use the meaning of the equal sign to determine whether expressions
  involving addition, subtraction, and multiplication are equivalent."
- **CCSS 1.OA.7 (grade 1):** "Understand the meaning of the equal sign, and determine if equations
  involving addition and subtraction are true or false."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 3.PAR.3.4 | 1.OA.7 | `state_superset` | | | high |

- **Decided by:** steps 5 and 6B, Test D. 1.OA.7 is inside; multiplication widens the content, and no
  code requires it with the equal sign.
- **Shows:** a state standard later and wider than its code; the grade gap plays no part.

**E8. `state_subset`: narrower bounds.**
- **Georgia 5.NR.4.3:** "Use place value understanding to round decimal numbers to the hundredths
  place."
- **CCSS 5.NBT.4:** "Use place value understanding to round decimals to any place."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 5.NR.4.3 | 5.NBT.4 | `state_subset` | | | high |

- **Decided by:** steps 5 and 6A, Test D. Hundredths only, vs. any place; no other Georgia standard
  covers the rest.
- **Shows:** a subset caused by bounds.

**E9. `state_subset`: a missing separate objective.**
- **Georgia 3.MDR.5.4:** "Use rulers to measure lengths in halves and fourths (quarters) of an inch and
  a whole inch."
- **CCSS 3.MD.4:** "Generate measurement data by measuring lengths using rulers marked with halves and
  fourths of an inch. Show the data by making a line plot…"

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 3.MDR.5.4 | 3.MD.4 | `state_subset` | | | high |

- **Decided by:** steps 5 and 6A, Test C. Making a line plot is a separate objective (Matters), and no
  other Georgia grade-3 standard covers it.
- **Shows:** a subset caused by a missing objective, not bounds.

**E10. `merge`: a code missing only an attached demand.**
- **Georgia 3.NR.4.4:** "Recognize and generate simple equivalent fractions."
- **CCSS 3.NF.3a:** "Understand two fractions as equivalent (equal) if they are the same size, or the
  same point on a number line."
- **CCSS 3.NF.3b:** "Recognize and generate simple equivalent fractions, e.g., 1/2 = 2/4, 4/6 = 2/3.
  Explain why the fractions are equivalent, e.g., by using a visual fraction model."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 3.NR.4.4 | 3.NF.3a | `merge` | | 3.NF.3b | high |
| 3.NR.4.4 | 3.NF.3b | `merge` | | 3.NF.3a | high |

- **Decided by:** section 3 and step 6B. The text states 3.NF.3b's core; Georgia's guidance interprets
  "equivalent" as 3.NF.3a does ("two fractions are equal when they are the same size or on the same
  location on a number line"). 3.NF.3b's "explain why" is an attached demand, so both codes are inside,
  and together they make up the standard.
- **Shows:** a plain merge; guidance interpreting a term; an attached demand noted in the rationale.

**E11. `merge`: the parent's general statement.**
- **Georgia 1.NR.1.2:** "Explain that the two digits of a 2-digit number represent the amounts of tens
  and ones."
- **CCSS 1.NBT.2a, 1.NBT.2b, 1.NBT.2c**, whose parent standard reads "Understand that the two digits of a
  two-digit number represent amounts of tens and ones. Understand the following as special cases:".

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 1.NR.1.2 | 1.NBT.2a | `merge` | | 1.NBT.2b, 1.NBT.2c | high |
| 1.NR.1.2 | 1.NBT.2b | `merge` | | 1.NBT.2a, 1.NBT.2c | high |
| 1.NR.1.2 | 1.NBT.2c | `merge` | | 1.NBT.2a, 1.NBT.2b | high |

- **Decided by:** section 2. It matches the parent's general statement, so all three lettered parts are
  cited, never the parent.
- **Shows:** citing lettered parts for a parent-level match.

**E12. `merge`: cite the codes whose content the text states.**
- **Georgia 3.GSR.7.1:** "Investigate area by covering the space of rectangles … using multiple copies
  of the same unit, with no gaps or overlaps, and determine the total area…"
- **CCSS 3.MD.5b:** "A plane figure which can be covered without gaps or overlaps by n unit squares is
  said to have an area of n square units."
- **CCSS 3.MD.6:** "Measure areas by counting unit squares (square cm, square m, square in, square ft, and
  improvised units)."
- **Not cited, CCSS 3.MD.5a:** "A square with side length 1 unit, called 'a unit square,' is said to
  have 'one square unit' of area, and can be used to measure area."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 3.GSR.7.1 | 3.MD.5b | `merge` | | 3.MD.6 | high |
| 3.GSR.7.1 | 3.MD.6 | `merge` | | 3.MD.5b | high |

- **Decided by:** Test A. The state text states 3.MD.5b's content almost word for word (covering with no
  gaps or overlaps; area as the number of units) and 3.MD.6's (counting units). It never states 3.MD.5a's
  content, what a unit square is: it uses "the same unit" without defining it. Both 3.MD.5a and 3.MD.5b
  are worded as definitions; what decides is which content the state text states.
- **Shows:** deciding by content, not by how a code is worded.

**E13. `merge` completed by an `overlap` piece; fluency matters.**
- **Georgia 3.PAR.3.2:** "Represent single digit multiplication and division facts using a variety of
  strategies. Explain the relationship between multiplication and division."
- **CCSS 3.OA.6:** "Understand division as an unknown-factor problem. For example, find 32 / 8 by finding
  the number that makes 32 when multiplied by 8."
- **CCSS 3.OA.7:** "Fluently multiply and divide within 100, using strategies such as the relationship
  between multiplication and division (e.g., knowing that 8 x 5 = 40, one knows 40 / 5 = 8) or
  properties of operations. By the end of Grade 3, know from memory all products of two one-digit
  numbers."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 3.PAR.3.2 | 3.OA.6 | `merge` | | 3.OA.7 | medium |
| 3.PAR.3.2 | 3.OA.7 | `overlap` | | 3.OA.6 | medium |

- **Decided by:** "Explain the relationship…" is the second sentence's whole task, so it is compared as
  a main action, and it matches 3.OA.6's understanding (as in E1). 3.OA.7 is `overlap`: it requires
  fluency and "know from memory" (Matters), and the standard's relationship work is in 3.OA.7 only as a
  strategy example. Step 6B: 3.OA.6 and the overlap piece 3.OA.7 make up the standard. No Georgia
  grade-3 standard requires the fluency, so 3.OA.7's `split_with` is empty.
- **Shows:** fluency as a difference that matters; the whole-task clause; an overlap piece completing a
  merge (pattern 7). (The adjudicated mapping labels 3.PAR.3.2 → 3.OA.7 `exact` and does not cite
  3.OA.6.)

**E14. Two state standards that each cover all of one code: `exact` and `merge`.**
- **Georgia 3.PAR.3.6:** "Solve practical, relevant problems involving multiplication and division
  within 100 using part-whole strategies, visual representations, and/or concrete models."
- **Georgia 3.PAR.3.7:** "Use multiplication and division to solve problems involving whole numbers to
  100. Represent these problems using equations with a letter standing for the unknown quantity.
  Justify solutions."
- **CCSS 3.OA.3:** "Use multiplication and division within 100 to solve word problems in situations
  involving equal groups, arrays, and measurement quantities, e.g., by using drawings and equations with
  a symbol for the unknown number to represent the problem."
- **CCSS 3.OA.8:** "Solve two-step word problems using the four operations. Represent these problems
  using equations with a letter standing for the unknown quantity…"

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 3.PAR.3.6 | 3.OA.3 | `exact` | | | high |
| 3.PAR.3.7 | 3.OA.3 | `merge` | | 3.OA.8 | medium |
| 3.PAR.3.7 | 3.OA.8 | `overlap` | | 3.OA.3 | medium |

- **Decided by:** 3.PAR.3.6: "practical, relevant problems" is its main action ("solve word
  problems"); strategies, representations and models are hows, so it is `exact`. 3.PAR.3.7: it covers
  3.OA.3 too, and requires equations with a letter for the unknown, which 3.OA.3 has only as an "e.g."
  but 3.OA.8 requires. 3.OA.3 is inside it (and can't be a second `exact`); 3.OA.8 is `overlap` (it adds
  two-step, four-operation problems); together they make up 3.PAR.3.7. "Justify solutions" is an
  attached demand.
- **Shows:** why `split` needs different parts (both standards cover the whole code); a CCSS "e.g." is
  not a requirement, but the same thing required in a state standard can match another code. (The
  adjudicated mapping labels both `split`.)

**E15. `split`: two standards, each covering a separate objective of one code.**
- **Georgia 3.MDR.5.2:** "Tell and write time to the nearest minute and estimate time to the nearest
  fifteen minutes (quarter hour) from the analysis of an analog clock."
- **Georgia 3.MDR.5.3:** "Solve meaningful problems involving elapsed time, including intervals of time to
  the hour, half hour, and quarter hour where the times presented are only on the hour, half hour, or
  quarter hour within a.m. or p.m. only."
- **CCSS 3.MD.1:** "Tell and write time to the nearest minute and measure time intervals in minutes.
  Solve word problems involving addition and subtraction of time intervals in minutes, e.g., by
  representing the problem on a number line diagram."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 3.MDR.5.2 | 3.MD.1 | `split` | 3.MDR.5.3 | | high |
| 3.MDR.5.3 | 3.MD.1 | `split` | 3.MDR.5.2 | | high |

- **Decided by:** step 6A. 3.MDR.5.2 covers telling time; its estimating is attached to telling time
  (Ignored). 3.MDR.5.3 covers the elapsed-time problems, with narrower bounds (quarter hours, not
  minutes), which still counts within a split; note it in the rationale. Together they make up 3.MD.1.
- **Shows:** the plain split; an attached estimate; narrower bounds inside a split.

**E16. `split` and `state_subset`: one code, four state standards.**
- **CCSS 4.NBT.2 (grade 4):** "Read and write multi-digit whole numbers using base-ten numerals, number
  names, and expanded form. Compare two multi-digit numbers based on meanings of the digits in each
  place, using >, =, and < symbols to record the results of comparisons." Two parts: read and write,
  and compare.
- **Georgia 4.NR.1.1 (grade 4):** "Read and write multi-digit whole numbers to the hundred-thousands
  place using base-ten numerals and expanded form."
- **Georgia 4.NR.1.3 (grade 4):** "Use place value reasoning to represent, compare, and order
  multi-digit numbers, using >, =, and < symbols to record the results of comparisons."
- **Georgia 3.NR.1.1 (grade 3):** "Read and write multi-digit whole numbers up to 10,000 … using
  base-ten numerals and expanded form."
- **Georgia 3.NR.1.2 (grade 3):** "Use place value reasoning to compare multi-digit numbers up to 10,000,
  using >, =, and < symbols to record the results of comparisons."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 4.NR.1.1 | 4.NBT.2 | `split` | 4.NR.1.3 | | high |
| 4.NR.1.3 | 4.NBT.2 | `split` | 4.NR.1.1 | | high |
| 3.NR.1.1 | 4.NBT.2 | `state_subset` | | | high |
| 3.NR.1.2 | 4.NBT.2 | `state_subset` | | | high |

- **Decided by:** step 6A. All four are inside 4.NBT.2 ("order" is part of comparing; ordinary
  components). The grade-4 pair makes up the code; 4.NR.1.1 lacks "number names" (Georgia's guidance:
  "Students are not expected to write numbers in word form"), narrower bounds within a split, noted in
  the rationale. The grade-3 pair covers the same parts only up to 10,000 (Test D), so the full code is
  made up without it.
- **Shows:** the "two sets of standards" rule; ordering ignored. (The adjudicated mapping labels all
  four `split`.)

**E17. `split` whose pieces are strategies and fluency.**
- **Georgia 1.NR.2.2:** "Use pictures, drawings, and equations to develop strategies for addition and
  subtraction within 20 by exploring strings of related problems."
- **Georgia 1.NR.2.4:** "Fluently add and subtract within 10 using a variety of strategies."
- **CCSS 1.OA.6:** "Add and subtract within 20, demonstrating fluency for addition and subtraction within
  10. Use strategies such as counting on; making ten…" Two parts: adding and subtracting within 20 with
  strategies, and fluency within 10.

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 1.NR.2.2 | 1.OA.6 | `split` | 1.NR.2.4 | | medium |
| 1.NR.2.4 | 1.OA.6 | `split` | 1.NR.2.2 | | high |

- **Decided by:** step 6A, Tests C and D. 1.NR.2.2 covers strategies within 20 (pictures, drawings,
  equations and strings of problems are hows); 1.NR.2.4 covers fluency within 10, a narrower range (Test
  D). Together they make up 1.OA.6. Not cited: 1.NR.2.2 → 1.OA.1 (its action is developing strategies,
  not solving word problems, Test A).
- **Shows:** fluency as a bound; split pieces that differ in kind, not topic. (The adjudicated mapping
  labels 1.NR.2.4 → 1.OA.6 `exact` and 1.NR.2.2 → 1.OA.1 `split`.)

**E18. `overlap` that helps on neither side.**
- **Georgia 3.GSR.6.1 (grade 3):** "Identify perpendicular line segments, parallel line segments, and
  right angles, identify these in polygons, and solve problems involving parallel line segments,
  perpendicular line segments, and right angles."
- **CCSS 4.G.1 (grade 4):** "Draw points, lines, line segments, rays, angles (right, acute, obtuse), and
  perpendicular and parallel lines. Identify these in two-dimensional figures."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 3.GSR.6.1 | 4.G.1 | `overlap` | | | high |

- **Decided by:** step 5, Test C. They share identifying these figures. The state standard adds solving
  problems (a separate objective); 4.G.1 adds drawing and more figures. Both columns stay empty: Georgia
  4.GSR.8.1 alone makes up 4.G.1, and no code covers the state standard's problem solving.
- **Shows:** `overlap` with an extra on each side; an overlap that is still cited because it is the
  closest match for part of the state standard (pattern 8). (The adjudicated mapping labels it
  `state_subset`.)

**E19. `none`: shared topic, different action.**
- **Georgia K.NR.1.4:** "Identify pennies, nickels, and dimes and know their name and value."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| K.NR.1.4 | | `none` | | | high |

- **Decided by:** Test A. The only CCSS money standard, 2.MD.8, asks students to "Solve word problems
  involving dollar bills, quarters, dimes, nickels, and pennies": same topic, different action.
- **Shows:** a shared topic is not a shared requirement.

**E20. `none`: no code except a much later, broader one.**
- **Georgia 1.PAR.3.2 (grade 1):** "Identify, describe, and create growing, shrinking, and repeating
  patterns based on the repeated addition or subtraction of 1s, 2s, 5s, and 10s."

| state_code | ccss_code | relationship | split_with | merge_with | confidence |
|---|---|---|---|---|---|
| 1.PAR.3.2 | | `none` | | | high |

- **Decided by:** Tests A and B. CCSS has no K–2 pattern standards. 3.OA.9 ("Identify arithmetic
  patterns … and explain them using properties of operations") asks for different work. 4.OA.5
  ("Generate a number or shape pattern that follows a given rule") shares creating a pattern from a
  rule, but it is three grades above and the state standard covers it only with narrower bounds
  (adding 1s, 2s, 5s or 10s), an early, simpler version, so it is not cited.
- **Shows:** `none` decided partly by the introductory-pass rule (Test B).

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
  action, or a code 2+ grades above that the standard covers only with narrower bounds.
- **C (separate objective):** a difference matters only if it is a separate learning objective, not
  wording, examples, recording/justifying, receptive vs. productive form, or ordinary components.
- **D (bounds):** different bounds always matter (range, number type, place value, cases, steps).

**Steps** (section 6).
1. **Describe** the requirement: action, content, bounds.
2. **Search** all grades and domains, both ways: a code for every part of the standard, and (for a code
   it covers only partly) the state's standards for every other part of the code.
3. **Keep** codes that share a requirement, whole or a part (A, B).
4. **Count:** 0 → one row, `none`; otherwise one row per code, labeled by steps 5–6.
5. **Which is inside which?** Each inside the other → `exact` (any grade); neither → `overlap`;
   standard inside code → 6A; code inside standard → 6B.
6. **Do the pieces make up the whole?**
   - A (state standard inside the code): the state standards covering parts of the code (incl.
     overlaps) make up all of the code, and this row's state standard is needed → `split`; otherwise
     `state_subset`.
   - B (code inside the state standard): the CCSS codes covering parts of the state standard (incl.
     overlaps) make up all of the state standard → `merge`; otherwise
     `state_superset`.

**Always.**
- One `exact` per CCSS code.
- Grade alone is not scope.
- One label per row; a standard's rows may differ.
- `merge` mirrors `split`; `overlap` rows count as pieces on both sides.
- When unsure whether a difference matters, ignore it; when unsure whether a standard is needed to
  make up a code, choose `state_subset`. Mark such rows `low` confidence.
