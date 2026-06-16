/*
1934. Confirmation Rate
https://leetcode.com/problems/confirmation-rate/

Problem
  Tables:
    Signups(user_id, signup_date)
    Confirmations(user_id, action, time_stamp)
      action ∈ {'confirmed', 'timeout'}

  Return each user's **confirmation rate**:
    (# confirmed messages) / (# total confirmation messages)
  Round to **2** decimal places.
  Include **every** user from Signups — if no confirmations, rate = 0.00.

Example
  Signups: user 6, 7
  Confirmations: (6, confirmed), (6, confirmed), (6, confirmed),
                  (7, confirmed), (7, timeout)
  → user 6: 3/3 = 1.00
  → user 7: 1/2 = 0.50
  → user with no Confirmations rows: 0.00

Pattern — LEFT JOIN + ratio aggregate (Basic Joins / SQL 50)
  1) **Signups** LEFT JOIN **Confirmations** — keep users with zero emails
  2) Compute rate per user with GROUP BY user_id
  3) ROUND(..., 2) and COALESCE(..., 0) for no-confirmation users

Your approach (AVG of boolean)
  - `action = 'confirmed'` → 1 if confirmed, 0 if timeout (MySQL)
  - AVG(1/0 values) = confirmed_count / total_count
  - No confirmations → action is NULL → AVG is NULL → COALESCE → 0

Pro tip (conversion / confirmation rate)

Whenever you see:
  "rate" / "percentage" / "ratio" / "include users with 0 events"
Think:
  - LEFT JOIN from the **dimension** table (Signups) to **events** (Confirmations)
  - Numerator/denominator OR AVG(boolean) OR SUM/COUNT on nullable columns
  - COALESCE when no events → NULL aggregate → show 0
  - Never COUNT(*) on a LEFT JOIN null row as the denominator (see bugs)

MySQL boolean AVG trick
  `action = 'confirmed'` in SELECT/aggregate:
    confirmed row → 1
    timeout row   → 0
    NULL action   → NULL (excluded from AVG)
  AVG(1,0,1) = 2/3 — same as SUM(confirmed)/COUNT(rows with action).

Relation to other SQL 50 problems
  **#1280** Students & Examinations — LEFT JOIN + COUNT for zeros (counting rows).
  **#1934** — LEFT JOIN + **ratio** (fraction confirmed).
  Same spine: anchor table LEFT JOIN facts, aggregate per user.

Common bugs
  - INNER JOIN Confirmations → drops users who never got an email
  - Missing COALESCE → NULL rate instead of 0.00 for no confirmations
  - `COUNT(*)` as denominator with LEFT JOIN → 1 row with NULLs still counts as 1 → wrong 0/1
  - Using COUNT(*) instead of COUNT(Confirmations.action) in SUM/COUNT variant
  - Forgetting ROUND(..., 2) — LeetCode checks precision
  - GROUP BY wrong table — group by Signups.user_id (all signups)

Approach comparison
  | Approach                         | Notes                              |
  |----------------------------------|------------------------------------|
  | AVG(action = 'confirmed')        | Your solution — submit below       |
  | SUM(confirmed) / COUNT(action)   | Explicit ratio; needs NULLIF/COALESCE |
  | SUM(CASE WHEN...) / COUNT(*)     | Only safe if filtering joined rows correctly |
  | Subquery rates + RIGHT JOIN      | Heavier; LEFT JOIN from Signups is simpler |

Complexity (typical)
  LEFT JOIN + GROUP BY user_id: O(S + C) scan; hash aggregate by user
  Space: O(U) for U distinct users in result

DE interview line
  "LEFT JOIN signups to confirmation events, AVG of a boolean flag for conversion rate —
   same pattern as email open rate, funnel step conversion, or feature adoption % in analytics."

Log: add to sql/week4_sql50_log.md when you batch Basic Joins.
*/

-- =============================================================================
-- SUBMIT (your solution) — LEFT JOIN + AVG(boolean) + COALESCE
-- =============================================================================
-- Write your MySQL query statement below
SELECT
  Signups.user_id,
  COALESCE(ROUND(AVG(action = 'confirmed'), 2), 0) AS confirmation_rate
FROM Signups
LEFT JOIN Confirmations
  ON Signups.user_id = Confirmations.user_id
GROUP BY Signups.user_id;

-- =============================================================================
-- ALTERNATIVE 1 — explicit SUM / COUNT (same logic, more readable in interviews)
-- COUNT(action) ignores NULL → denominator 0 when no confirmations → COALESCE
-- =============================================================================
SELECT
  s.user_id,
  COALESCE(
    ROUND(
      SUM(c.action = 'confirmed') / NULLIF(COUNT(c.action), 0),
      2
    ),
    0
  ) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
  ON s.user_id = c.user_id
GROUP BY s.user_id;

-- =============================================================================
-- ALTERNATIVE 2 — CASE WHEN (portable across SQL dialects)
-- =============================================================================
SELECT
  s.user_id,
  COALESCE(
    ROUND(
      SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END)
        / NULLIF(COUNT(c.action), 0),
      2
    ),
    0
  ) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
  ON s.user_id = c.user_id
GROUP BY s.user_id;

-- =============================================================================
-- WHY NOT COUNT(*) ? — bug demo (do not submit)
-- User with zero confirmations: LEFT JOIN yields 1 row, all Confirmations cols NULL
-- COUNT(*) = 1  →  SUM(...)/1 = 0  (accidentally OK here)
-- But pattern is wrong for other rates; use COUNT(fact_column) or AVG(boolean)
-- =============================================================================

-- =============================================================================
-- TRACE — user 7: one confirmed, one timeout
--   Rows after JOIN: (7, confirmed), (7, timeout)
--   action = 'confirmed' → 1, 0
--   AVG → 0.5 → ROUND → 0.50
--
-- TRACE — user with no Confirmations:
--   One row: action = NULL
--   action = 'confirmed' → NULL
--   AVG(NULL) → NULL → COALESCE → 0
-- =============================================================================
