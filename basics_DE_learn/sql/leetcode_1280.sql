/*
1280. Students and Examinations
https://leetcode.com/problems/students-and-examinations/

Problem
  Tables:
    Students(student_id, student_name)
    Subjects(subject_name)
    Examinations(student_id, subject_name)

  Return every (student, subject) pair and how many times that student took
  an exam in that subject. Include pairs with **zero** exams.
  Order by student_id, subject_name.

Example
  Students: (1, Alice), (2, Bob)
  Subjects: Math, Physics
  Examinations: (1, Math), (1, Math), (2, Math)
  → All 4 student×subject combos; Alice-Math=2, Alice-Physics=0, Bob-Math=1, Bob-Physics=0

Pattern — cross join + LEFT JOIN + COUNT (Basic Joins / SQL 50 #12)
  1) Build the **full grid**: every student × every subject (CROSS JOIN)
  2) LEFT JOIN actual exam rows on (student_id, subject_name)
  3) COUNT non-null exam columns → 0 when student never took that subject

Your approach
  - FROM Students JOIN Subjects  → implicit CROSS JOIN (no ON clause)
  - LEFT JOIN Examinations ON student_id AND subject_name
  - COUNT(Examinations.subject_name) — NULLs excluded → 0 for missing exams
  - GROUP BY student_id, student_name, subject_name

Pro tip (reporting matrix with zeros)

Whenever you see:
  "all combinations" / "include rows with count 0" / "every X with every Y"
Think:
  - CROSS JOIN (or JOIN without ON) for the full grid
  - LEFT JOIN facts table
  - COUNT(fact_column) not COUNT(*) — COUNT(*) is 1 even when LEFT JOIN is NULL

JOIN precedence (MySQL)
  FROM Students JOIN Subjects LEFT JOIN Examinations ON ...
  is read as: (Students ⋈ Subjects) LEFT JOIN Examinations
  — which is what you want. Use explicit CROSS JOIN if clearer in interviews.

Common bugs
  - INNER JOIN Examinations → drops student-subject pairs with 0 exams
  - COUNT(*) instead of COUNT(Examinations.*) → shows 1 instead of 0
  - Forgetting to join on **both** student_id and subject_name
  - Only listing students who took exams (missing the cross product)

Approach comparison
  | Approach                    | Notes                              |
  |-----------------------------|------------------------------------|
  | JOIN + LEFT JOIN (yours)    | Submit — implicit cross join       |
  | Explicit CROSS JOIN         | Same logic, clearer intent         |
  | Subquery grid + LEFT JOIN   | SELECT * FROM Students, Subjects   |

Complexity (typical)
  Cross join: |Students| × |Subjects| rows; join exams O(exams)
  Space: O(1) extra besides result set

DE interview line
  "Cross join for the full student×subject matrix, LEFT JOIN attendance facts,
   COUNT nullable column — same as a sparse metrics grid filled with zeros in BI."

Log: sql/week3_sql50_log.md (#12)
*/

-- =============================================================================
-- SUBMIT (your solution) — cross join grid + LEFT JOIN + COUNT
-- =============================================================================
SELECT
  Students.student_id,
  Students.student_name,
  Subjects.subject_name,
  COUNT(Examinations.subject_name) AS attended_exams
FROM Students
JOIN Subjects
LEFT JOIN Examinations
  ON Students.student_id = Examinations.student_id
  AND Subjects.subject_name = Examinations.subject_name
GROUP BY 1, 2, 3
ORDER BY 1, 3;

-- =============================================================================
-- ALTERNATIVE — explicit CROSS JOIN (preferred readability in interviews)
-- =============================================================================
SELECT
  s.student_id,
  s.student_name,
  sub.subject_name,
  COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
  ON s.student_id = e.student_id
  AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;

-- =============================================================================
-- ALTERNATIVE — derived grid (comma = cross join in FROM)
-- =============================================================================
SELECT
  grid.student_id,
  grid.student_name,
  grid.subject_name,
  COUNT(e.subject_name) AS attended_exams
FROM (
  SELECT s.student_id, s.student_name, sub.subject_name
  FROM Students s
  CROSS JOIN Subjects sub
) grid
LEFT JOIN Examinations e
  ON grid.student_id = e.student_id
  AND grid.subject_name = e.subject_name
GROUP BY grid.student_id, grid.student_name, grid.subject_name
ORDER BY grid.student_id, grid.subject_name;
