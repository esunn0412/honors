#!/usr/bin/env python3
"""Maps every cell of Georgia's own K-5 "Learning Progressions" table
(georgia_math_progressions.json) to the actual GA sub-standard code(s) that
cell's bullets correspond to.

Each entry below is one (domain, concept, grade) cell -- one row of the
progression table at one grade -- built by direct comparison of that cell's
bullet text against every GA sub-standard's description at that grade
(read from georgia_math_{grade}.json). This is NOT the CCSS<->GA skill
mapping (build_skill_mapping.py) -- it stays entirely inside GA's own
documents, cross-referencing GA's own scope-and-sequence chart against GA's
own standard codes.

Fields per entry:
  domain, concept, grade  -- identify the cell (matches georgia_math_progressions.json)
  codes    -- list of GA sub-standard codes judged to correspond to this cell's
              bullets. May span more than one domain code prefix (see
              cross_domain below) or be empty (see gap below).
  gap      -- True if at least one of this cell's bullets has no matching
              GA standard text. The progression table asserts the content
              exists at this grade; the standards codes don't contain
              matching text. Not treated as an error in either document --
              recorded and left for the advisor to weigh in on.
  unmatched_bullets -- for gap cells only: the exact bullet string(s) (verbatim
              from georgia_math_progressions.json) that have no matching code,
              so the gap can be checked against the specific claim, not just
              the cell as a whole. Empty for non-gap cells.
  note     -- reasoning, especially for anything non-obvious: bound
              mismatches, wording differences, or why a gap was called a
              gap rather than a loose match.

cross_domain is computed automatically (not hand-set) by comparing each
code's own domain prefix against the cell's stated `domain` -- so it can't
be silently mismarked the way relationship types were in the skill map.
"""
import json
import re
from pathlib import Path

STANDARDS_DIR = Path(__file__).resolve().parent.parent / "standards"

GRADE_INDEX = {"K": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}

# =====================================================================
# Hand-built cell -> GA code mapping. One entry per non-empty cell in
# georgia_math_progressions.json (72 cells total).
# =====================================================================
MAPPINGS = [
    # ---------------- NR: Numbers ----------------
    dict(domain="NR", concept="Numbers (whole numbers, fractions, and decimal numbers)", grade="K",
         codes=["K.NR.2.1", "K.NR.4.1"], gap=False,
         note="Strand-level summary of K's overall number range, not one single standard: K.NR.2.1 supplies the 'to 100' bound (counting), K.NR.4.1 supplies numeral identification (to 20 only -- the bare description never reaches 100 for numeral writing specifically)."),
    dict(domain="NR", concept="Numbers (whole numbers, fractions, and decimal numbers)", grade="1",
         codes=["1.NR.1.1", "1.GSR.4.3"], gap=False,
         note="'Whole numbers to 120' -> 1.NR.1.1. 'Partition shapes into halves and quarters with no shading' -> 1.GSR.4.3, which is a GSR-domain standard, not NR -- fraction partitioning is coded under geometry in GA even though this progression row sits under the Numerical Reasoning header. See the cross-domain callout below."),
    dict(domain="NR", concept="Numbers (whole numbers, fractions, and decimal numbers)", grade="2",
         codes=["2.NR.1.1", "2.NR.1.2", "2.GSR.7.3", "2.GSR.7.4"], gap=False,
         note="'Whole numbers to 1000' -> 2.NR.1.1/2.NR.1.2. 'Partition shapes...' -> 2.GSR.7.3, again GSR-domain, not NR; 2.GSR.7.4 (equal shares of a whole may be different shapes) is the same parent standard's (2.GSR.7) next sub-item extending the same partitioning concept, added alongside it."),
    dict(domain="NR", concept="Numbers (whole numbers, fractions, and decimal numbers)", grade="3",
         codes=["3.NR.1.1", "3.NR.4.1", "3.NR.4.2", "3.NR.4.3", "3.NR.4.4"], gap=False,
         note="Clean match: whole numbers to 10,000 -> 3.NR.1.1; the four fraction bullets (unit fractions, represent fractions, equivalence, shading) -> 3.NR.4.1-3.NR.4.4 respectively."),
    dict(domain="NR", concept="Numbers (whole numbers, fractions, and decimal numbers)", grade="4",
         codes=["4.NR.1.1", "4.NR.4.1", "4.NR.4.2", "4.NR.4.3", "4.NR.4.4", "4.NR.4.5", "4.NR.4.6", "4.NR.5.1", "4.NR.5.2"], gap=False,
         note="'Whole numbers to 100,000' -> 4.NR.1.1. 'Non-unit fractions with denominators of 2,3,4,5,6,8,10,12,and 100' is a summary of grade 4's whole fraction-representation cluster (4.NR.4.1-4.NR.4.5), not one standard's exact wording. 'Fractions with like denominators' -> 4.NR.4.6. 'Decimal fractions (tenths and hundredths)' -> 4.NR.5.1/4.NR.5.2."),
    dict(domain="NR", concept="Numbers (whole numbers, fractions, and decimal numbers)", grade="5",
         codes=["5.NR.1.1", "5.NR.3.2", "5.NR.3.3", "5.NR.4.1"], gap=False,
         note="'Multi-digit whole numbers' loosely attributed to 5.NR.1.1 (place value magnitude), no Grade 5 standard restates multi-digit whole-number reading/writing as its own item. 'Fractions with unlike denominators' -> 5.NR.3.2/5.NR.3.3. 'Fractions greater than 1' has no distinct Grade 5 standard -- that language belongs to 3.NR.4.3/4.NR.4.1 (reinforcement, not new Grade 5 content); left unattributed rather than forced onto an unrelated code. 'Decimal fractions to thousandths' -> 5.NR.4.1."),

    # ---------------- NR: Counting ----------------
    dict(domain="NR", concept="Counting", grade="K",
         codes=["K.NR.2.1", "K.NR.2.2", "K.NR.1.1", "K.NR.1.2", "K.NR.1.3"], gap=False,
         note="'Counting forward to 100' and 'counting backward from 20' -> K.NR.2.1 (starting from 0) and K.NR.2.2 (starting from any number within the range). 'Counting objects to 20' -> K.NR.1.1, plus K.NR.1.2 (cardinality) and K.NR.1.3 (one more/one less), the rest of the same parent standard (K.NR.1). K.NR.1.3 is the weakest fit of the three -- it's a static relational skill (given a number, name its neighbor), not the sequential-counting action the bullet names -- but it shares K.NR.1.3's own 1-20 range with K.NR.1.1/1.2 exactly, whereas Comparisons/K's bullets cap at 10 objects, so Counting is the better-matching bound even though the skill itself is a weaker fit than a true counting action. Placed here as the best available cell rather than left unreferenced."),
    dict(domain="NR", concept="Counting", grade="1",
         codes=["1.NR.1.1", "1.PAR.3.2"], gap=False,
         note="'Counting forward and backward within 120' and 'counting objects to 120' -> 1.NR.1.1. 'Skip counting by 2s, 5s, and 10s' has no matching NR standard, but 1.PAR.3.2's own text -- 'growing, shrinking, and repeating patterns based on the repeated addition or subtraction of 1s, 2s, 5s, and 10s' -- is functionally the same skill (repeatedly adding 2 from 0 produces the skip-count-by-2s sequence), just framed as a pattern rather than a counting action. Cross-domain, not a gap: PAR, not NR, the same pattern already seen at Grade 3 for Computational Fluency/Addition & Subtraction/Multiplication & Division."),
    dict(domain="NR", concept="Counting", grade="2",
         codes=["2.NR.1.2"], gap=False,
         note="All three bullets (forward/backward within 1000, skip counting by 2s/5s/10s/25s/100s, counting objects to 1000) map cleanly onto 2.NR.1.2's own wording, which lists all of them explicitly."),
    dict(domain="NR", concept="Counting", grade="3",
         codes=["3.NR.4.1"], gap=True,
         unmatched_bullets=["Counting unit fractions"],
         note="'Counting unit fractions' has no standard whose text describes a counting/enumerating skill for fractions (3.NR.4.1 describes unit fractions but as composition, not counting in sequence). Nearest relative given, but recorded as a gap."),
    dict(domain="NR", concept="Counting", grade="4",
         codes=["4.NR.4.4", "4.NR.4.5"], gap=True,
         unmatched_bullets=["Counting non-unit fractions"],
         note="'Counting non-unit fractions' has no standard literally describing counting; nearest relative is representing fractions as sums of unit fractions (4.NR.4.4/4.NR.4.5), which is counting-adjacent but not the same stated skill. Recorded as a gap."),
    dict(domain="NR", concept="Counting", grade="5",
         codes=["5.NR.4.1"], gap=True,
         unmatched_bullets=["Counting decimal numbers"],
         note="'Counting decimal numbers' has no standard literally describing counting; nearest relative is read/write decimals (5.NR.4.1). Recorded as a gap. Pattern across grades 3-5: the 'Counting' strand's own concept (counting unit fractions/non-unit fractions/decimals) is never restated as an explicit standalone skill in the standards text past Grade 2 -- it becomes purely conceptual/implicit."),

    # ---------------- NR: Place Value ----------------
    dict(domain="NR", concept="Place Value", grade="K",
         codes=["K.NR.3.1", "K.NR.5.1", "K.NR.4.1"], gap=False,
         note="'Compose and decompose numbers within 20' is split across two GA codes by number range: K.NR.3.1 covers 11-19, K.NR.5.1 covers up to 10. 'Identify and write numerals to 20' -> K.NR.4.1."),
    dict(domain="NR", concept="Place Value", grade="1",
         codes=["1.NR.1.2"], gap=False, note=""),
    dict(domain="NR", concept="Place Value", grade="2",
         codes=["2.NR.1.1"], gap=False, note=""),
    dict(domain="NR", concept="Place Value", grade="3",
         codes=["3.NR.1.3", "3.NR.1.1"], gap=False, note=""),
    dict(domain="NR", concept="Place Value", grade="4",
         codes=["4.NR.1.2", "4.NR.1.1", "4.NR.1.4", "4.NR.5.1"], gap=False, note=""),
    dict(domain="NR", concept="Place Value", grade="5",
         codes=["5.NR.1.1", "5.NR.1.2", "5.NR.4.1", "5.NR.4.3"], gap=False, note=""),

    # ---------------- NR: Comparisons ----------------
    dict(domain="NR", concept="Comparisons", grade="K",
         codes=["K.NR.4.2"], gap=False, note=""),
    dict(domain="NR", concept="Comparisons", grade="1",
         codes=["1.NR.1.3"], gap=False, note=""),
    dict(domain="NR", concept="Comparisons", grade="2",
         codes=["2.NR.1.3"], gap=False, note=""),
    dict(domain="NR", concept="Comparisons", grade="3",
         codes=["3.NR.1.2", "3.NR.4.2"], gap=False, note=""),
    dict(domain="NR", concept="Comparisons", grade="4",
         codes=["4.NR.1.3", "4.NR.4.2", "4.NR.4.3", "4.NR.5.3"], gap=False, note=""),
    dict(domain="NR", concept="Comparisons", grade="5",
         codes=["5.NR.4.2", "5.NR.3.2"], gap=False,
         note="'Fractions greater than 1' has no dedicated Grade 5 comparison standard; loosely attributed to 5.NR.3.2 (compare up to three fractions), which does not itself use 'greater than 1' language."),

    # ---------------- NR: Computational Fluency ----------------
    dict(domain="NR", concept="Computational Fluency", grade="K",
         codes=["K.NR.5.4"], gap=False, note=""),
    dict(domain="NR", concept="Computational Fluency", grade="1",
         codes=["1.NR.2.4"], gap=False, note=""),
    dict(domain="NR", concept="Computational Fluency", grade="2",
         codes=["2.NR.2.1", "2.NR.2.4"], gap=False, note=""),
    dict(domain="NR", concept="Computational Fluency", grade="3",
         codes=["3.PAR.3.2", "3.PAR.2.1"], gap=False,
         note="Both bullets are PAR-domain standards, not NR: Grade 3 files multiplication/division fluency AND addition/subtraction fluency under Patterns & Algebraic Reasoning (3.PAR.2.1, 3.PAR.3.2), not Number Relations. See the cross-domain callout -- this is the largest single instance of it."),
    dict(domain="NR", concept="Computational Fluency", grade="4",
         codes=["4.NR.2.1"], gap=False, note=""),
    dict(domain="NR", concept="Computational Fluency", grade="5",
         codes=["5.NR.2.1", "5.NR.2.2"], gap=False, note=""),

    # ---------------- NR: Addition & Subtraction ----------------
    dict(domain="NR", concept="Addition & Subtraction", grade="K",
         codes=["K.NR.5.2", "K.NR.5.3"], gap=False, note=""),
    dict(domain="NR", concept="Addition & Subtraction", grade="1",
         codes=["1.NR.2.1", "1.NR.2.2", "1.NR.2.3", "1.NR.2.5", "1.NR.2.6", "1.NR.2.7", "1.NR.5.1", "1.NR.5.2", "1.NR.5.3"], gap=False,
         note="Confirmed by GA's own parent-standard titles, not just topical similarity: 1.NR.2's own title is 'Explain the relationship between addition and subtraction and apply the properties of operations to solve real-life addition and subtraction problems within 20' -- i.e. all seven of 1.NR.2.1-1.NR.2.7 belong to 'Within 20', not just the ones whose own bare text happens to say 'properties of operations' (1.NR.2.5's equal-sign true/false and 1.NR.2.6's unknown-addend both fall under this same umbrella; 1.NR.2.4 is excluded because it narrows to 'within 10' and is already used for the Computational Fluency cell instead). Likewise 1.NR.5's own title is 'Use concrete models, the base ten structure, and properties of operations to add and subtract within 100' -- covering 1.NR.5.1 (general strategies), 1.NR.5.2 (mentally find 10 more/less, i.e. add/subtract 10 -- moved here from an earlier, wrong placement under Place Value), and 1.NR.5.3 (add/subtract multiples of 10)."),
    dict(domain="NR", concept="Addition & Subtraction", grade="2",
         codes=["2.NR.2.3", "2.NR.2.2"], gap=False,
         note="No 2.NR standard states addition/subtraction 'within 1,000' as a word-problem-solving bound explicitly; attributed to the two nearest strategy-based standards. Loose."),
    dict(domain="NR", concept="Addition & Subtraction", grade="3",
         codes=["3.PAR.2.2"], gap=False,
         note="PAR-domain, not NR: Grade 3's addition/subtraction-within-10,000 standard is coded 3.PAR.2.2."),
    dict(domain="NR", concept="Addition & Subtraction", grade="4",
         codes=["4.NR.2.1", "4.NR.2.5", "4.NR.4.6"], gap=False,
         note="'Within 100,000' attributed to 4.NR.2.1, whose own text says 'multi-digit numbers' without stating the bound explicitly (Grade 4's number range tops out at 100,000 per 4.NR.1.1). 'Fractions with like denominators' -> 4.NR.4.6. UNCERTAIN PLACEMENT: 4.NR.2.5 ('solve multi-step problems using addition, subtraction, multiplication, and division... mental computation and estimation') is placed here as its most natural home, but it explicitly spans all four operations, not just addition/subtraction -- it could equally be argued to belong under Multiplication & Division/4 instead. Both cells' shared parent standard is 4.NR.2, whose own title covers addition, subtraction, multiplication, and division together, so the parent standard itself doesn't resolve which single cell is the better fit."),
    dict(domain="NR", concept="Addition & Subtraction", grade="5",
         codes=["5.NR.3.3", "5.NR.4.4"], gap=False, note=""),

    # ---------------- NR: Multiplication & Division ----------------
    dict(domain="NR", concept="Multiplication & Division", grade="2",
         codes=["2.NR.3.1", "2.NR.3.2"], gap=False,
         note="2.NR.3.1 (odd/even numbers, sum of two equal addends) and 2.NR.3.2 (arrays) share the same parent standard, 2.NR.3: 'Work with equal groups to gain foundations for multiplication.' 'Building arrays' names only 2.NR.3.2's own content literally, but 2.NR.3.1 is the other half of the same foundations-for-multiplication parent, added alongside it."),
    dict(domain="NR", concept="Multiplication & Division", grade="3",
         codes=["3.PAR.3.3", "3.PAR.3.4", "3.PAR.3.5", "3.PAR.3.6", "3.PAR.3.7"], gap=False,
         note="All PAR-domain: Grade 3 files multiplication/division content under Patterns & Algebraic Reasoning, not Number Relations. All five sub-standards share the parent standard 3.PAR.3 ('multiplication and division with whole numbers within 100') and every other 3.PAR.3.x sibling is placed here, so 3.PAR.3.4 (equal sign / equivalence of expressions involving multiplication) joins them by the same parent-standard grouping, even though its own content (equivalence reasoning) is a narrower fit for the 'Within 100' bullet's computation focus than its siblings are."),
    dict(domain="NR", concept="Multiplication & Division", grade="4",
         codes=["4.PAR.3.3", "4.PAR.3.4", "4.NR.2.2", "4.NR.2.3", "4.NR.2.4"], gap=False,
         note="'Factors and multiples' and 'prime and composite numbers' are PAR-domain (4.PAR.3.3, 4.PAR.3.4); 'multiply by multi-digit whole numbers' and 'divide by 1-digit divisors' are back in NR (4.NR.2.3, 4.NR.2.4). Grade 4 splits this strand across two domains. 4.NR.2.2 (multiplicative comparison) added alongside 4.NR.2.3/2.4 -- same parent standard (4.NR.2), and multiplicative comparison is foundational to the multiply/divide skills the bullets name."),
    dict(domain="NR", concept="Multiplication & Division", grade="5",
         codes=["5.NR.2.1", "5.NR.3.4", "5.NR.3.6", "5.NR.3.5"], gap=False, note=""),

    # ---------------- NR: Expressions ----------------
    dict(domain="NR", concept="Expressions", grade="5",
         codes=["5.NR.5.1", "5.NR.3.1"], gap=False,
         note="'Express fractions as division problems' -> 5.NR.3.1 (fraction as division of numerator by denominator), filed under the fractions standard group, not a separate expressions standard."),

    # ---------------- PAR: Patterns ----------------
    dict(domain="PAR", concept="Patterns", grade="K",
         codes=["K.PAR.6.1", "K.PAR.6.2"], gap=False,
         note="K.PAR.6.1 is a near-verbatim match to the cell's bullets. K.PAR.6.2 (patterns involving the passage of time) shares the same parent standard, K.PAR.6, whose own title explicitly names 'patterns involving the passage of time' -- joins its sibling here by that grouping, even though the cell's own bullet text (repeating patterns with numbers/shapes) doesn't itself mention time, and no other K-5 grade's Patterns row mentions time either."),
    dict(domain="PAR", concept="Patterns", grade="1",
         codes=["1.PAR.3.1", "1.PAR.3.2"], gap=False, note=""),
    dict(domain="PAR", concept="Patterns", grade="2",
         codes=["2.PAR.4.1", "2.PAR.4.2"], gap=False, note=""),
    dict(domain="PAR", concept="Patterns", grade="3",
         codes=["3.PAR.3.1"], gap=False, note=""),
    dict(domain="PAR", concept="Patterns", grade="4",
         codes=["4.PAR.3.1", "4.PAR.3.2"], gap=False, note=""),
    dict(domain="PAR", concept="Patterns", grade="5",
         codes=["5.PAR.6.1"], gap=False, note=""),

    # ---------------- PAR: Graphing ----------------
    dict(domain="PAR", concept="Graphing", grade="5",
         codes=["5.PAR.6.2"], gap=False,
         note="The progression table's own bullet reads 'Plot order pairs in first quadrant' -- 'order pairs' rather than 'ordered pairs' (5.PAR.6.2's own wording). A wording slip in GA's progression table itself, not in the standard; kept verbatim in georgia_math_progressions.json per this project's verbatim policy, noted here rather than silently corrected."),

    # ---------------- GSR: Shapes and Properties ----------------
    dict(domain="GSR", concept="Shapes and Properties", grade="K",
         codes=["K.GSR.8.1", "K.GSR.8.2", "K.GSR.8.3", "K.GSR.8.4"], gap=False,
         note="K.GSR.8.1/8.2 match the cell's identification/positional-words bullets directly. K.GSR.8.3/8.4 (compose shapes into other shapes) share the same parent standard, K.GSR.8, whose own title includes 'form two-dimensional shapes and three-dimensional figures' -- joined here by that grouping, even though the cell's own bullet text doesn't itself mention composition (that content is restated as its own explicit bullet one grade later, 'Compose 2D shapes & 3D shapes', Grade 1, mapped to 1.GSR.4.2)."),
    dict(domain="GSR", concept="Shapes and Properties", grade="1",
         codes=["1.GSR.4.1", "1.GSR.4.2"], gap=False, note=""),
    dict(domain="GSR", concept="Shapes and Properties", grade="2",
         codes=["2.GSR.7.1", "2.GSR.7.2"], gap=False, note=""),
    dict(domain="GSR", concept="Shapes and Properties", grade="3",
         codes=["3.GSR.6.2", "3.GSR.6.1", "3.GSR.6.3"], gap=False,
         note="'Lines of symmetry with quadrilaterals' attributed to 3.GSR.6.3, whose own text says 'polygons' generically, not 'quadrilaterals' specifically -- minor scope-wording difference between the progression table and the standard."),
    dict(domain="GSR", concept="Shapes and Properties", grade="4",
         codes=["4.GSR.8.1", "4.GSR.8.2"], gap=False, note=""),
    dict(domain="GSR", concept="Shapes and Properties", grade="5",
         codes=["5.GSR.8.1", "5.GSR.8.2"], gap=False, note=""),

    # ---------------- GSR: Geometric Measurement ----------------
    dict(domain="GSR", concept="Geometric Measurement", grade="3",
         codes=["3.GSR.7.1", "3.GSR.7.2", "3.GSR.7.3", "3.GSR.8.1", "3.GSR.8.2"], gap=False, note=""),
    dict(domain="GSR", concept="Geometric Measurement", grade="4",
         codes=["4.GSR.8.3", "4.GSR.7.1", "4.GSR.7.2"], gap=False, note=""),
    dict(domain="GSR", concept="Geometric Measurement", grade="5",
         codes=["5.GSR.8.3", "5.GSR.8.4"], gap=False, note=""),

    # ---------------- MDR: Measurement & Data ----------------
    dict(domain="MDR", concept="Measurement & Data", grade="K",
         codes=["K.MDR.7.1", "K.MDR.7.2", "K.MDR.7.3"], gap=False, note=""),
    dict(domain="MDR", concept="Measurement & Data", grade="1",
         codes=["1.MDR.6.1", "1.MDR.6.4"], gap=False,
         note="'Display and interpret categorical data (with up to 3 categories)' attributed to 1.MDR.6.4, whose own text says 'compare and order whole numbers' via graphical displays -- the 'up to 3 categories' bound is not stated in 1.MDR.6.4 itself (may come from georgia_math_guidance_1.json instead of the bare standard)."),
    dict(domain="MDR", concept="Measurement & Data", grade="2",
         codes=["2.MDR.5.2", "2.MDR.5.1", "2.MDR.5.4", "2.MDR.5.3", "2.MDR.5.5"], gap=False,
         note="2.MDR.5.3 (measure the length difference between two objects) and 2.MDR.5.5 (represent sums/differences of lengths on a number line) both share the parent standard 2.MDR.5 with 2.MDR.5.1/5.2/5.4, and are both length-measurement content matching this cell's 'measure length' bullets, added alongside the other three."),
    dict(domain="MDR", concept="Measurement & Data", grade="3",
         codes=["3.MDR.5.5", "3.MDR.5.4", "3.MDR.5.1"], gap=False, note=""),
    dict(domain="MDR", concept="Measurement & Data", grade="4",
         codes=["4.MDR.6.1", "4.MDR.6.3", "4.MDR.6.2"], gap=False,
         note="'Measure liquid volume, distance, and mass using the metric system' -> 4.MDR.6.1. 'Analyze data using dot plots' -> 4.MDR.6.3, plus 4.MDR.6.2 (the recurring 'ask questions and answer them...graphical displays' standard every other grade's data-analysis bullet is also attributed to). 'Use rulers to measure lengths to nearest 1/2, 1/4 and 1/8 of an inch' has no matching text in 4.MDR.6.3's bare description, but its own georgia_math_guidance_4.json entry states this exactly: age_developmentally_appropriate says 'Students should only use rulers marked to the nearest 1/8 of an inch,' and strategies_and_methods says 'Use rulers to measure lengths and record numerical measurement data to the nearest 1/2, 1/4 and 1/8 of an inch.' Not a gap -- the content lives in the guidance file, not the bare standard text. (This is exactly why every earlier 'gap' cell was re-checked against the guidance files too, not just the bare standards, before being finalized.)"),
    dict(domain="MDR", concept="Measurement & Data", grade="5",
         codes=["5.MDR.7.1", "5.MDR.7.3", "5.MDR.7.4", "5.MDR.7.2"], gap=True,
         unmatched_bullets=["Create and analyze dot plots (line plots) with fraction measurements"],
         note="'Measure length and weight in metric units' and 'convert between units' map cleanly to 5.MDR.7.1/7.3/7.4. But 'create and analyze dot plots (line plots) with fraction measurements' has no matching text in any 5.MDR standard -- none mentions dot/line plots or fractions. 5.MDR.7.2 (ask/answer questions from graphical displays) is the nearest relative, but does not state fractions. Recorded as a gap."),

    # ---------------- MDR: Money ----------------
    dict(domain="MDR", concept="Money", grade="K",
         codes=["K.NR.1.4"], gap=False,
         note="NR-domain, not MDR: Kindergarten's money standard is coded under Number Relations even though this progression row sits under Measurement & Data Reasoning."),
    dict(domain="MDR", concept="Money", grade="1",
         codes=["1.MDR.6.3"], gap=False,
         note="MDR-domain this time -- inconsistent with Kindergarten's own money standard being NR-domain one grade earlier, within GA's own coding, not across documents."),
    dict(domain="MDR", concept="Money", grade="2",
         codes=["2.MDR.6.2"], gap=False, note="Exact, near-verbatim match."),
    dict(domain="MDR", concept="Money", grade="3",
         codes=[], gap=True,
         unmatched_bullets=["Using money to solve problems"],
         note="No Grade 3 GA standard names money as its subject, checked against every bare standard (3.NR, 3.PAR, 3.MDR, 3.GSR) AND every guidance file entry (georgia_math_guidance_3.json). The only hit anywhere in Grade 3's guidance is a scope caveat on 3.PAR.3.7 -- 'situations involving money should not include decimal numbers' -- which implies money-themed word problems are used as one possible context for that standard's multiplication/division content, but no actual worked example anywhere in Grade 3's guidance uses money (checked every examples field). Thin evidence, not enough to call this resolved -- recorded as a gap, with the caveat noted for completeness."),
    dict(domain="MDR", concept="Money", grade="4",
         codes=["4.NR.5.2"], gap=False,
         note="No Grade 4 GA standard names money as its subject, but 4.NR.5.2's guidance directly evidences money being used 'as a tool or manipulative to solve problems' (the bullet's own wording): its examples field poses a $0.62 refund-check word problem specifically to teach fraction/decimal equivalence (62 cents as 62/100 of a dollar). Cross-domain (NR, not MDR) and not the standard's stated topic, but the bullet's own framing -- money as a *tool* for other content, not a dedicated skill -- is exactly what this shows."),
    dict(domain="MDR", concept="Money", grade="5",
         codes=["5.NR.4.4"], gap=False,
         note="5.NR.4.4's guidance states, nearly verbatim: 'Money may be used as a tool to aid in the student's understanding of adding and subtracting decimal numbers to the hundredths place' -- matching the bullet ('Using money as a tool to solve problems involving decimals') almost exactly. Cross-domain (NR, not MDR) and not the standard's stated topic (5.NR.4.4 is about decimal addition/subtraction generally), but this is the strongest guidance-level evidence found for any Money cell past Grade 2."),

    # ---------------- MDR: Time ----------------
    dict(domain="MDR", concept="Time", grade="1",
         codes=["1.MDR.6.2"], gap=False, note=""),
    dict(domain="MDR", concept="Time", grade="2",
         codes=["2.MDR.6.1"], gap=False,
         note="'Distinguish between a.m. & p.m.' is not stated in 2.MDR.6.1's own bare text (which covers telling time to five minutes and elapsed time to hour/half hour); likely drawn from georgia_math_guidance_2.json's elaboration rather than the bare standard."),
    dict(domain="MDR", concept="Time", grade="3",
         codes=["3.MDR.5.2", "3.MDR.5.3"], gap=False, note=""),
    dict(domain="MDR", concept="Time", grade="4",
         codes=["4.MDR.6.1"], gap=False, note=""),
    dict(domain="MDR", concept="Time", grade="5",
         codes=["5.MDR.7.1"], gap=False, note=""),
]

def ga_desc_lookup():
    """code -> (description, domain_code) across all six GA standards files."""
    out = {}
    for g in range(6):
        d = json.load(open(STANDARDS_DIR / f"georgia_math_{g}.json"))
        for dom in d["domains"]:
            if dom.get("is_meta"):
                continue
            dcode = dom["code"].split(".", 1)[1]  # "K.NR" -> "NR"
            for st in dom["standards"]:
                subs = st.get("sub_standards")
                items = subs if subs else [st]
                for item in items:
                    out[item["code"]] = (item["description"], dcode)
    return out


def code_domain(code):
    # e.g. "1.GSR.4.3" -> "GSR"; "K.NR.1.4" -> "NR"
    m = re.match(r"^[K0-5]\.([A-Z]+)\.", code)
    return m.group(1)


def main():
    prog = json.load(open(STANDARDS_DIR / "georgia_math_progressions.json"))
    ga_desc = ga_desc_lookup()
    all_ga_codes = set(ga_desc.keys())

    # Sanity: every cell in MAPPINGS corresponds to a real, non-empty cell
    # in georgia_math_progressions.json, and every non-empty cell in that
    # file has exactly one entry in MAPPINGS.
    prog_cells = set()
    for dom in prog["domains"]:
        for c in dom["key_concepts"]:
            for g in ["K", "1", "2", "3", "4", "5"]:
                if c["by_grade"][g]:
                    prog_cells.add((dom["domain_code"], c["concept"], g))

    mapping_cells = set((m["domain"], m["concept"], m["grade"]) for m in MAPPINGS)
    assert mapping_cells == prog_cells, (
        f"Cell mismatch.\nIn progressions but not mapped: {prog_cells - mapping_cells}\n"
        f"In mapping but not a real progressions cell: {mapping_cells - prog_cells}"
    )
    assert len(MAPPINGS) == len(set((m["domain"], m["concept"], m["grade"]) for m in MAPPINGS)), \
        "Duplicate cell entry in MAPPINGS"

    # Every referenced code must be real.
    referenced = set()
    for m in MAPPINGS:
        for code in m["codes"]:
            assert code in all_ga_codes, f"Unknown GA code {code} referenced in cell {m['domain']}/{m['concept']}/{m['grade']}"
            referenced.add(code)

    unreferenced = sorted(all_ga_codes - referenced)
    assert not unreferenced, (
        f"Every GA code is expected to be referenced by some cell (grouped by parent "
        f"standard where a bullet-level match doesn't exist) -- these are not: {unreferenced}"
    )

    # gap cells must name which bullet(s) are unmatched; non-gap cells must not.
    for m in MAPPINGS:
        ub = m.get("unmatched_bullets", [])
        if m["gap"]:
            assert ub, f"gap=True but no unmatched_bullets given for {m['domain']}/{m['concept']}/{m['grade']}"
            cell_bullets = prog["domains"][
                [d["domain_code"] for d in prog["domains"]].index(m["domain"])
            ]["key_concepts"][
                [c["concept"] for c in prog["domains"][
                    [d["domain_code"] for d in prog["domains"]].index(m["domain"])
                ]["key_concepts"]].index(m["concept"])
            ]["by_grade"][m["grade"]]
            for b in ub:
                assert b in cell_bullets, f"unmatched_bullets entry {b!r} is not a real bullet in {m['domain']}/{m['concept']}/{m['grade']}"
        else:
            assert not ub, f"gap=False but unmatched_bullets given for {m['domain']}/{m['concept']}/{m['grade']}"

    # Cross-domain detection: does any code's own domain prefix differ from
    # the cell's stated domain?
    def cross_domain_codes(m):
        return [c for c in m["codes"] if code_domain(c) != m["domain"]]

    gaps = [m for m in MAPPINGS if m["gap"]]
    cross_domain_cells = [m for m in MAPPINGS if cross_domain_codes(m)]
    fully_empty_gaps = [m for m in gaps if not m["codes"]]

    def cell_bullets_of(m):
        return prog["domains"][
            [d["domain_code"] for d in prog["domains"]].index(m["domain"])
        ]["key_concepts"][
            [c["concept"] for c in prog["domains"][
                [d["domain_code"] for d in prog["domains"]].index(m["domain"])
            ]["key_concepts"]].index(m["concept"])
        ]["by_grade"][m["grade"]]

    def cell_json(m):
        return {
            "domain": m["domain"],
            "concept": m["concept"],
            "grade": m["grade"],
            "bullets": cell_bullets_of(m),
            "mapped_codes": [
                {"code": c, "description": ga_desc[c][0], "domain": ga_desc[c][1]}
                for c in m["codes"]
            ],
            "gap": m["gap"],
            "unmatched_bullets": m.get("unmatched_bullets", []),
            "cross_domain": bool(cross_domain_codes(m)),
            "note": m["note"],
        }

    output = {
        "description": "Maps every cell of georgia_math_progressions.json (GA's own K-5 Learning Progressions table) to the actual GA sub-standard code(s) whose text corresponds to that cell's bullets. Built entirely from GA's own documents (georgia_math_progressions.json cross-referenced against georgia_math_0.json..._5.json) -- no CCSS text or the CCSS<->GA skill map was consulted.",
        "totals": {
            "cells_mapped": len(MAPPINGS),
            "ga_codes_total": len(all_ga_codes),
            "ga_codes_referenced_by_progression_table": len(referenced),
            "ga_codes_not_in_progression_table": len(unreferenced),
            "cells_with_a_gap": len(gaps),
            "cells_with_a_gap_and_zero_mapped_codes": len(fully_empty_gaps),
            "cells_with_cross_domain_codes": len(cross_domain_cells),
        },
        "gap_cells": [cell_json(m) for m in gaps],
        "cells": [cell_json(m) for m in MAPPINGS],
    }

    out_path = STANDARDS_DIR / "georgia_progressions_mapped.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Wrote {out_path}")
    print(json.dumps(output["totals"], indent=2))
    print()
    print("GA codes never referenced by the progression table "
          f"({len(unreferenced)}):", ", ".join(unreferenced))
    print()
    print(f"Cells with a gap ({len(gaps)}):")
    for m in gaps:
        print(f"  {m['domain']}/{m['concept']}/{m['grade']}: {m.get('unmatched_bullets')}")
    print()
    print(f"Cells with cross-domain codes ({len(cross_domain_cells)}):")
    for m in cross_domain_cells:
        print(f"  {m['domain']}/{m['concept']}/{m['grade']} -> {cross_domain_codes(m)}")


if __name__ == "__main__":
    main()
