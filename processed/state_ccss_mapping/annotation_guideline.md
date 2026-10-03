# Annotation guideline: mapping state math standards to CCSS (K–5)

*Version 1.2, Sep 30, 2026.*

This guideline tells an annotator how to map one state's K–5 mathematics standards onto the Common
Core State Standards for Mathematics (CCSS), K–5. It was established by three annotators while
jointly adjudicating a complete mapping of Georgia's K–5 standards, and it is written to apply to any
state. Every rule is meant to be applied the same way by different annotators working alone; where a
judgment could go either way, the guideline states which way to go.

**How to use it.** Read sections 1–10 once before starting. While annotating, work from the
**quick reference** (section 12) and look up cases in **Find your case** below. Each rule is stated in
full in one place; other sections point to it.

## Contents

1. [The task](#1-the-task)
2. [Independence](#2-independence)
3. [Units](#3-units): which state and CCSS units to annotate and cite
4. [Reading a standard](#4-reading-a-standard): what one standard requires
5. [Comparing standards: the four tests](#5-comparing-standards-the-four-tests): when two requirements match
6. [Relationship types](#6-relationship-types): what the seven labels mean
7. [Decision procedure](#7-decision-procedure): how to choose a label; step 3 merge or superset, step 5 split or subset
8. [Tie-break defaults](#8-tie-break-defaults): what to choose when unsure
9. [Worked examples](#9-worked-examples): E1–E15
10. [What to record](#10-what-to-record)
11. [Process](#11-process)
12. [Quick reference](#12-quick-reference)

## Find your case

| If… | Rule | Example |
|---|---|---|
| the two standards share a topic but ask for different work | Test A (requirement) → `none` or drop the code | E13 |
| no CCSS code at any grade shares the requirement | `none` | E14 |
| the state standard is a general practice repeated at every grade | `none` unless it states a code's requirement | E15 |
| the wording differs but the requirement is the same | Test B (separate objective) → `exact` | E1 |
| one standard identifies and the other writes the same thing | Test B: receptive vs. productive form | E2 |
| one standard adds "explain", "justify" or "record with symbols" | Test B: an attached demand, not an objective | E7 |
| a method or tool is given with "e.g." or "such as" | Test B: an example, not a requirement | — |
| the number range, number type or place value differs | Test C (bounds): always counts | E5 |
| the only matching CCSS code is at another grade | `different_grade` if otherwise the same; grade alone is never scope | E7, E8 |
| a CCSS code is a prerequisite or only a definition (e.g. 3.MD.5a) | Test D (not a match): don't cite it | E11 |
| the state standard matches a CCSS parent's general statement | Section 3: cite all its lettered parts | E10 |
| the state's guidance adds something the text doesn't say | Section 4.1: guidance interprets, never adds | — |
| the state standard matches one code and has an extra part | Step 3: extra is another code's core → `merge`; otherwise `state_superset` | E3, E4 |
| the state standard states two or more codes' core requirements | Step 4 → `merge`; leftovers in the rationale | E9, E10, E11 |
| the state standard covers only part of a code, and no other standard covers the rest | Step 5 → `state_subset` | E6 |
| two or more state standards each cover a different part of one code | Step 5 → `split` | E12 |
| an earlier or narrower state standard covers part of a code another standard covers more fully | Step 5 → `state_subset` | 4.NBT.2 table in step 5 |
| you already marked a CCSS code `exact` and find a second state standard like it | Exact rule (section 6): re-examine both | — |
| the state standard both adds and lacks something | Step 6: decide by the more substantial difference, note both | — |
| you are still unsure | Section 8 tie-breaks; mark `low` confidence | — |

---

## 1. The task

For each state standard, record:

1. **which CCSS codes it corresponds to** (zero, one or more), and
2. **how it relates to them**: one of seven relationship types (section 6).

A "correspondence" means the two standards require the same learning of students. It does not mean
they are on the same topic.

---

## 2. Independence

The annotations are used to measure agreement between annotators, so they must be independent.

- **Work alone.** Do not discuss standards, decisions or difficult cases with the other annotators
  until the annotation is finished.
- **Use only the provided materials:** the state standards (with the state's own context and guidance
  where provided), the CCSS K–5 list (with domains, clusters and parent standards), and this guideline.
- **Do not consult other mappings or crosswalks** of this state to CCSS (published, commercial or
  automatic), or any model's output.
- **Questions go to the question log** (section 11), not to other annotators. Answers are sent to all
  annotators in writing, so everyone works from the same guideline.

---

## 3. Units

**State side.** Annotate each state standard at its **lowest level**: the smallest unit the state
itself numbers or letters (e.g. Georgia `K.NR.1.1`; a lettered part of a Virginia standard, `3.MG.2 a)`).
Sub-points under that unit (e.g. Roman numerals i, ii under a lettered part) belong to it and are not
annotated separately. Each unit gets exactly one annotation.

**CCSS side.** Cite **leaf codes**: a CCSS standard's lettered parts where it has them (e.g. `3.MD.7a`,
`3.MD.7b`), otherwise the standard itself (e.g. `3.MD.6`). Never cite a parent standard that has
lettered parts (e.g. `3.MD.7`).

- The state standard matches the parent's general statement → cite **all** its lettered parts (E10).
- It matches only some parts → cite **those**.

---

## 4. Reading a standard

This section is about one standard at a time: what it requires. Section 5 compares two.

### 4.1 The standard's own text sets the requirement

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

### 4.2 Describe the core requirement

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

## 5. Comparing standards: the four tests

These tests decide whether a state standard's requirement and a CCSS code's requirement match. The
decision procedure (section 7) applies them; they are referred to by letter throughout.

### Test A (requirement): shared requirement, not shared topic

Two requirements correspond only if the action, content and bounds are essentially the same. Being
about the same topic is not enough.

> Identifying coins and their values (Georgia K.NR.1.4) and solving word problems with coins (CCSS
> 2.MD.8) share a topic, not a requirement.

### Test B (separate objective): does a difference change the relationship?

When one standard has something the other doesn't, decide whether that difference is **a separate
learning objective**: something a teacher would plan, teach and assess as its own goal. Only then does
it change the relationship.

| Counts as a separate objective (changes the relationship) | Does not (the relationship stays the same) |
|---|---|
| A different product or skill: making a line plot, drawing figures, solving word problems, a second operation, counting backward as well as forward, measuring elapsed time | Wording, phrasing, emphasis |
| A different or wider number range, number type, place value or set of cases (Test C) | Methods, tools or representations given as examples ("e.g.", "such as", "for example", "using objects or drawings") |
| | A demand attached to the same task: recording the result with symbols, justifying or explaining the result, using a model to show it |
| | Receptive and productive forms of the same skill on the same content (identifying written numerals vs. writing them, when both standards require representing quantities with numerals) |
| | Ordinary components of the task (finding the value of a group of coins as part of solving money problems) |
| | A general setting ("in authentic problems", "in real-world contexts") unless the other standard's requirement is specifically problem solving |

*Why explaining and justifying don't count:* the question is whether two standards target the same
learning, not how that learning is shown. Explaining and justifying are expected across all standards
(e.g. CCSS Mathematical Practice 3), so counting them would make most pairs differ on wording alone.
They still matter: note a missing "explain" or "justify" in the rationale.

### Test C (bounds): a difference in bounds always counts

A different number range (to 20 vs. to 100), number type (whole numbers vs. fractions vs. decimals),
place value (to hundredths vs. to any place), denominators, number of digits, number of steps, or set
of cases.

### Test D (not a match): not every related code is a match

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

A **grade difference alone is never a difference in scope** (`different_grade`, section 6).

---

## 6. Relationship types

Exactly one per state standard. This section says what each label **means**; section 7 says how to
choose one.

| Type | In short | CCSS codes cited | Definition |
|---|---|---|---|
| `exact` | same standard | exactly 1 | Essentially the same requirement: same action, content and bounds, at the same grade. Differences that are not separate objectives (Test B) are still `exact`. Not word for word. |
| `state_superset` | the state asks for more | exactly 1 | Everything the CCSS code requires **plus** a separate objective or wider bounds that is not itself the core requirement of another CCSS code. |
| `state_subset` | the state asks for less | exactly 1 | **Less** than the CCSS code requires (a missing separate objective or narrower bounds), and **not** one of the standards that together make up the full code. |
| `different_grade` | same standard, another grade | exactly 1 | Essentially the same requirement (as for `exact`), but the CCSS code is at a different K–5 grade. |
| `merge` | one state standard, several CCSS codes | 2 or more | The state standard states the core requirement of two or more CCSS codes, whether it covers each fully or partly. |
| `split` | one CCSS code, spread over several state standards | exactly 1 | One of two or more state standards that **together make up the full CCSS code**, each covering a different part of it. Name the others in `split_with`. |
| `none` | no CCSS counterpart | 0 | No CCSS K–5 code shares the state standard's requirement at any grade. |

Two rules always hold:

- **Exact rule.** A state standard is `exact` with at most one CCSS code, and a CCSS code is `exact` with
  at most one state standard. If a second state standard is also essentially the same as a CCSS code
  you already marked `exact`, re-examine both: usually each covers a separate part of it (`split`), or
  one of them differs in scope.
- **Count the codes first.** How many CCSS codes a standard corresponds to is decided before scope: a
  standard that corresponds to two or more codes is `merge`, even if it is broader or narrower than
  them.

---

## 7. Decision procedure

Work through the steps in order for each state standard. Record the step at which you decided in your
rationale. Steps 3–4 decide `merge` or `state_superset`; step 5 decides `split` or `state_subset`.

### Step 1. Describe

Describe the state standard's core requirement: action, content, bounds (section 4.2).

### Step 2. Search

Search the whole CCSS list for candidate codes: every domain and every grade. Start at the state
standard's own grade and domain, then widen. States organize content differently (e.g. a state may
place area, perimeter, volume and angle measure under geometry, where CCSS places them under
Measurement and Data).

### Step 3. Keep the codes whose core requirement the standard states

For each candidate code, ask:

> **Does the state standard's text state this code's core requirement?**

- **Keep a code only if the state standard states its core requirement** (Test A): its action on its
  content. Sharing a detail, an example or the topic with the code is not enough.
- **Drop** prerequisites, assumed definitions, same-topic codes with a different action, and
  distant-grade topic matches (Test D).
- **Check the neighbours.** Once you find one match, check its lettered siblings and the other codes in
  its cluster: state standards often combine several CCSS codes.
- **Look up any extra part.** If the state standard fully matches one code and has an extra part:
  - the extra part is itself the core requirement of another CCSS code (search all grades and domains)
    → keep that code too (it will be a `merge`);
  - no CCSS code requires it → keep only the one code (it will be a `state_superset`, step 6).

### Step 4. Count the codes kept

- **0** → `none`. Stop.
- **2 or more** → `merge`. Stop. Leftover differences go in the rationale, not the label: a small extra
  part that no CCSS code requires, or one code covered a bit narrowly (e.g. without a demand attached to
  the task, or with somewhat narrower bounds), does not turn a `merge` into `state_superset` or
  `state_subset`.
- **1** → step 5.

**Examples for steps 3–4:**

| Georgia standard | Codes whose core requirement it states | Extra or leftover | Label |
|---|---|---|---|
| K.NR.2.1: "Count forward to 100 by tens and ones and backward from 20 by ones." | K.CC.1 (count to 100 by ones and tens) | Counting backward: a separate objective, but no CCSS code requires it | `state_superset` of K.CC.1 |
| 3.GSR.7.1: "Investigate area by covering the space of rectangles … using multiple copies of the same unit, with no gaps or overlaps, and determine the total area…" | 3.MD.5b (a figure covered without gaps or overlaps by n unit squares has area n) and 3.MD.6 (measure areas by counting unit squares) | None; 3.MD.5a is only a definition (Test D) | `merge` |
| 3.NR.4.4: "Recognize and generate simple equivalent fractions." | 3.NF.3a (fractions as equivalent when the same size or the same point on a number line, as Georgia's guidance interprets "equivalent") and 3.NF.3b (recognize and generate simple equivalent fractions) | 3.NF.3b's "Explain why the fractions are equivalent" is not stated: noted in the rationale | `merge` |

K.NR.2.1 is not a merge: counting backward is a separate objective (Test B), but because no CCSS code
has it as its core requirement, there is no second code to cite. 3.NR.4.4 stays a merge even though it
covers 3.NF.3b a little narrowly: once two codes' core requirements are stated, what is missing from
one of them is recorded in the rationale, not in the label.

### Step 5. Coverage: split or subset

Does the state standard cover the full code (all of its parts)? **Yes** → step 6. **No, only part of
it** → look at **all** the state's standards that cover any part of that code, and ask:

> **Which standards, together, make up the full CCSS code: all of its parts?**

| Situation | Label |
|---|---|
| The standards that together cover all of the code's parts, each a different part, none the whole code alone | `split` (each names the others in `split_with`) |
| A standard covering a part that another standard already covers more fully (typically an earlier, narrower pass: smaller numbers, fewer cases, an earlier grade) | `state_subset`: it contributes to learning the code, but the full code is made up without it |
| The same parts covered by more than one set of standards (e.g. in grade 3 and again, more fully, in grade 4) | the set with the fuller scope, usually at or nearest the code's grade, is `split`; the others are `state_subset` |
| No combination of the state's standards covers all of the code's parts | every standard covering part of it is `state_subset` |
| A single standard covers the full code | that standard goes to step 6 (`exact`, `state_superset` or `different_grade`); any other standard covering part of the code is `state_subset` |

Within a split, a part may be covered with somewhat narrower bounds than the code (e.g. time intervals
in quarter hours rather than minutes); note it in the rationale. What decides `split` is that the
standard is needed to cover one of the code's parts.

**Example: CCSS 4.NBT.2** (grade 4, whole numbers up to 1,000,000): "Read and write multi-digit whole
numbers using base-ten numerals, number names, and expanded form. Compare two multi-digit numbers based
on meanings of the digits in each place, using >, =, and < symbols to record the results of
comparisons." It has two parts: read and write numbers, and compare numbers.

| Georgia standard | Covers | Needed to make up 4.NBT.2? | Label |
|---|---|---|---|
| 4.NR.1.1 (grade 4): "Read and write multi-digit whole numbers to the hundred-thousands place using base-ten numerals and expanded form." | read and write, grade-4 numbers | Yes | `split`, with 4.NR.1.3 |
| 4.NR.1.3 (grade 4): "Use place value reasoning to represent, compare, and order multi-digit numbers, using >, =, and < symbols to record the results of comparisons." | compare, grade-4 numbers | Yes | `split`, with 4.NR.1.1 |
| 3.NR.1.1 (grade 3): "Read and write multi-digit whole numbers up to 10,000 to the thousands using base-ten numerals and expanded form." | read and write, only up to 10,000 | No: 4.NR.1.1 already covers this part more fully | `state_subset` |
| 3.NR.1.2 (grade 3): "Use place value reasoning to compare multi-digit numbers up to 10,000, using >, =, and < symbols to record the results of comparisons." | compare, only up to 10,000 | No: 4.NR.1.3 already covers this part more fully | `state_subset` |

The two grade-4 standards together make up 4.NBT.2, so they are `split`. The grade-3 standards teach
the same parts earlier, with smaller numbers; the full code is made up without them, so each is a
`state_subset` of 4.NBT.2, not a split partner. (Note: the adjudicated Georgia mapping currently labels
all four `split`; it is to be re-adjudicated under this rule.)

**Contrast: CCSS 4.G.1** (grade 4): "Draw points, lines, line segments, rays, angles (right, acute,
obtuse), and perpendicular and parallel lines. Identify these in two-dimensional figures." A single
Georgia standard, 4.GSR.8.1, covers all of it, so it is `exact`. Georgia 3.GSR.6.1 (grade 3: "Identify
perpendicular line segments, parallel line segments, and right angles, identify these in polygons…")
covers only identifying, for fewer figures; the full code is made up without it, so it is
`state_subset`.

See also E12 (a two-standard split).

### Step 6. Scope

Compare the state standard with its one code (Tests B and C):

- essentially the same → `exact` (same grade) or `different_grade` (other grade);
- adds a separate objective or has wider bounds → `state_superset` (if the added part is another code's
  core requirement, go back to step 3: it is a `merge`);
- has narrower bounds → `state_subset`;
- both adds and lacks something → decide by the more substantial difference and note both.

---

## 8. Tie-break defaults

When a case could reasonably go either way, use these defaults, so that annotators who are uncertain
in the same way still agree. Mark such cases **`low` confidence** (section 10).

| Unsure between | Choose | Unless |
|---|---|---|
| `exact` and `state_superset` / `state_subset` | `exact` | the difference passes Test B or Test C |
| `different_grade` and `state_superset` / `state_subset` | `different_grade` | the difference passes Test B or Test C (a grade difference alone never does) |
| citing a code or not (step 3), e.g. `state_superset` vs. `merge` | don't cite it | the state standard's text states the code's action on its content (Test A) |
| `split` and `state_subset` (step 5) | `state_subset` | you can name the other standard(s) that, together with this one, make up the full code |
| `state_subset` and `none` | `state_subset` | the shared part is only the topic, not a requirement (Test A) |
| a same-grade code vs. another-grade code with the same requirement | the same-grade code | only the other-grade code shares the requirement |

---

## 9. Worked examples

All from the adjudicated Georgia mapping. Each gives the state text, the CCSS text, the label and
what decided it.

| Label | Examples |
|---|---|
| `exact` | E1, E2 |
| `state_superset` | E3, E4, E8 |
| `state_subset` | E5, E6 |
| `different_grade` | E7 |
| `merge` | E9, E10, E11 |
| `split` | E12 |
| `none` | E13, E14, E15 |

**E1. `exact`: wording differs, requirement is the same.**
- **Georgia K.NR.1.2:** "When counting objects, explain that the last number counted represents the
  total quantity in a set (cardinality), regardless of the arrangement and order."
- **CCSS K.CC.4b:** "Understand that the last number name said tells the number of objects counted.
  The number of objects is the same regardless of their arrangement or the order in which they were
  counted."
- **Decided by:** Test B. "Explain" and "understand" name the same conceptual requirement; content and
  bounds match.

**E2. `exact`: receptive vs. productive form of the same skill.**
- **Georgia K.NR.4.1:** "Identify written numerals 0-20 and represent a number of objects with a
  written numeral 0-20 (with 0 representing a count of no objects)."
- **CCSS K.CC.3:** "Write numbers from 0 to 20. Represent a number of objects with a written numeral
  0-20 (with 0 representing a count of no objects)."
- **Decided by:** Test B. Identifying vs. writing the same numerals is not a separate objective here;
  the core requirement, representing quantities 0–20 with numerals, is identical.

**E3. `state_superset`: an added separate objective no CCSS code requires.**
- **Georgia K.NR.2.1:** "Count forward to 100 by tens and ones and backward from 20 by ones."
- **CCSS K.CC.1:** "Count to 100 by ones and by tens."
- **Decided by:** Test B and step 3. Counting backward is a separate objective, and no CCSS code
  requires it, so there is no second code to cite.

**E4. `state_superset`: an added separate objective.**
- **Georgia 1.MDR.6.2:** "Tell and write time in hours and half-hours using analog and digital clocks,
  and measure elapsed time to the hour on the hour using a predetermined number line."
- **CCSS 1.MD.3:** "Tell and write time in hours and half-hours using analog and digital clocks."
- **Decided by:** Test B. Elapsed time is a separate objective.

**E5. `state_subset`: narrower bounds.**
- **Georgia 5.NR.4.3:** "Use place value understanding to round decimal numbers to the hundredths
  place."
- **CCSS 5.NBT.4:** "Use place value understanding to round decimals to any place."
- **Decided by:** Test C. Hundredths only, vs. any place.

**E6. `state_subset`: a missing separate objective no other standard covers.**
- **Georgia 3.MDR.5.4:** "Use rulers to measure lengths in halves and fourths (quarters) of an inch
  and a whole inch."
- **CCSS 3.MD.4:** "Generate measurement data by measuring lengths using rulers marked with halves and
  fourths of an inch. Show the data by making a line plot…"
- **Decided by:** Test B and step 5. Making a line plot is a separate objective, and no other Georgia
  grade-3 standard covers it.

**E7. `different_grade`: same requirement; attached demands don't count.**
- **Georgia 4.NR.4.2 (grade 4):** "Compare two fractions with the same numerator or the same
  denominator by reasoning about their size and recognize that comparisons are valid only when the two
  fractions refer to the same whole."
- **CCSS 3.NF.3d (grade 3):** essentially the same text, plus "Record the results of comparisons with
  the symbols >, =, or <, and justify the conclusions, e.g., by using a visual fraction model."
- **Decided by:** Test B. Recording with symbols and justifying are demands attached to the same task,
  so the requirement is essentially the same; only the grade differs.

**E8. `state_superset` across grades: scope wins over grade.**
- **Georgia 3.PAR.3.4 (grade 3):** "Use the meaning of the equal sign to determine whether expressions
  involving addition, subtraction, and multiplication are equivalent."
- **CCSS 1.OA.7 (grade 1):** "Understand the meaning of the equal sign, and determine if equations
  involving addition and subtraction are true or false."
- **Decided by:** Test C. Multiplication widens the content, so it is `state_superset`, not
  `different_grade`.

**E9. `merge`: two codes, one covered a little narrowly.**
- **Georgia 3.NR.4.4:** "Recognize and generate simple equivalent fractions."
- **CCSS 3.NF.3a and 3.NF.3b.**
- **Decided by:** section 4.1 and steps 3–4. The text states 3.NF.3b's core ("recognize and generate
  simple equivalent fractions"), and Georgia's guidance interprets "equivalent" as 3.NF.3a does: "two
  fractions are equal when they are the same size or on the same location on a number line". It does
  not state 3.NF.3b's "explain why"; two codes means `merge`, and the missing part goes in the
  rationale.

**E10. `merge`: the parent's general statement.**
- **Georgia 1.NR.1.2:** "Explain that the two digits of a 2-digit number represent the amounts of tens
  and ones."
- **CCSS 1.NBT.2a, 1.NBT.2b, 1.NBT.2c.**
- **Decided by:** section 3. It matches the general statement of 1.NBT.2 (a parent), so all three
  lettered parts are cited.

**E11. `merge` with an excluded definition.**
- **Georgia 3.GSR.7.1:** "Investigate area by covering the space of rectangles … using multiple copies
  of the same unit, with no gaps or overlaps, and determine the total area…"
- **CCSS 3.MD.5b and 3.MD.6, not 3.MD.5a.**
- **Decided by:** Test D. 3.MD.5a only defines a unit square; the state standard uses the concept
  without stating the definition.

**E12. `split`: two standards, each covering a separate objective of one code.**
- **Georgia 3.MDR.5.2:** "Tell and write time to the nearest minute and estimate time to the nearest
  fifteen minutes…"
- **Georgia 3.MDR.5.3:** "Solve meaningful problems involving elapsed time…"
- **CCSS 3.MD.1 (both):** "Tell and write time to the nearest minute and measure time intervals in
  minutes. Solve word problems involving addition and subtraction of time intervals in minutes…"
- **Decided by:** step 5. Telling time and solving elapsed-time problems are separate objectives of
  3.MD.1; each Georgia standard covers one, and together they make up the code. Each is `split`,
  naming the other. (For an earlier, narrower standard that is `state_subset` rather than a split
  partner, see the 4.NBT.2 table in step 5.)

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
  if it states that code's specific requirement. This one resembles the Standards for Mathematical
  Practice more than any grade's content standard.

---

## 10. What to record

One row per state standard:

| Field | What to enter |
|---|---|
| `state_code` | The state standard's code |
| `ccss_codes` | The CCSS leaf codes, separated by commas; empty for `none` |
| `relationship` | One of the seven types |
| `split_with` | For `split` only: the other state standard(s) covering the rest of the code |
| `confidence` | `high`: the guideline decides it clearly; `medium`: a judgment within a clear rule; `low`: a tie-break default was needed (section 8) |
| `rationale` | One or two sentences: the core requirement matched, the decisive difference (if any), and the test or step that decided it (e.g. "Step 6, Test C: rounds to hundredths only, CCSS to any place") |

**Before moving on, check:**
- the number of codes fits the type (section 6);
- no parent code with lettered parts is cited;
- `split` names its partners.

---

## 11. Process

1. **Calibration.** Before annotating, each annotator maps a short practice set of standards from the
   adjudicated Georgia mapping (not from the state being annotated) and compares their answers with the
   adjudicated answers. Differences are discussed only in terms of this guideline. Practice items are not
   part of the agreement measurement.
2. **Independent annotation.** Each annotator annotates their assigned standards alone (section 2), in
   any order, without revising the guideline.
3. **Question log.** Questions about the guideline go to a shared log. They are answered in writing by
   the guideline owner, without reference to specific annotators' answers, and every answer is sent to
   all annotators. Clarifications are added to the guideline's next version.
4. **Agreement.** Each standard is annotated by two annotators; agreement is measured per annotator pair
   with Cohen's kappa (0.60 acceptable, 0.70 usable, 0.80 or above strong).
5. **Adjudication.** After agreement is measured, all annotators meet to resolve disagreements by the
   guideline; the result is the gold mapping. Any guideline change made during adjudication is recorded
   with its reason.

---

## 12. Quick reference

*A one-page summary; the full rules are in the sections named.*

**Units** (section 3). State standard at its lowest level. CCSS leaf codes only; if the state standard
matches a parent's general statement, cite all its lettered parts.

**Tests** (section 5).
- **A (requirement):** shared action + content + bounds, not a shared topic.
- **B (separate objective):** a difference matters only if it is a separate learning objective, not
  wording, examples, recording/justifying, receptive vs. productive form, or ordinary components.
- **C (bounds):** different bounds always matter (range, number type, place value, cases, steps).
- **D (not a match):** don't cite prerequisites, assumed definitions, same-topic codes with a different
  action, or distant-grade topic matches.

**Steps** (section 7).
1. **Describe** the requirement: action, content, bounds.
2. **Search** all grades and domains.
3. **Keep** codes whose core requirement the standard states (A, D); check siblings; look for a code
   that requires any extra part.
4. **Count:** 0 → `none`; 2+ → `merge` (leftovers in the rationale); 1 → step 5.
5. **Coverage:** covers only part of the code? Helps make up the full code with other standards →
   `split`; otherwise `state_subset`.
6. **Scope:** same → `exact` (same grade) / `different_grade` (other grade); more, and no code requires
   the extra → `state_superset`; less → `state_subset`.

**Always.**
- One `exact` per CCSS code.
- Grade alone is not scope.
- When unsure, use the tie-break defaults (section 8) and mark `low` confidence.
