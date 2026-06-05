/*
197. Rising Temperature
https://leetcode.com/problems/rising-temperature/

Problem
  Table Weather(id, recordDate, temperature)
  Return ids where temperature is strictly higher than the previous day's
  temperature. recordDate is unique per row (one row per day).

Example
  id | recordDate | temperature
  1  | 2015-01-01 | 10
  2  | 2015-01-02 | 25
  → Id = 2 (25 > 10 vs previous day)

Pattern — self-join (Basic Joins / SQL 50)
  Join the table to itself: row "today" (w2) vs row "yesterday" (w1).
  Match consecutive calendar days, then filter w2.temperature > w1.temperature.

Your approach (self-join + DATEDIFF)
  - w1 = previous day, w2 = current day
  - DATEDIFF(w1.recordDate, w2.recordDate) = -1  → w2 is exactly 1 day after w1
  - WHERE w1.temperature < w2.temperature
  - SELECT w2.id (the warmer *current* day, not yesterday)

DATEDIFF reminder (MySQL)
  DATEDIFF(a, b) = a - b in days.
  So DATEDIFF(yesterday, today) = -1  ⟺  today is yesterday + 1 day.

Alternatives (same idea, often clearer in interviews)
  1) DATE_ADD / + INTERVAL 1 DAY
     ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL -1 DAY)
     or ON w2.recordDate = DATE_ADD(w1.recordDate, INTERVAL 1 DAY)

  2) Flip DATEDIFF sign
     ON DATEDIFF(w2.recordDate, w1.recordDate) = 1

  3) Window (MySQL 8+) — mention if asked
     LAG(temperature) OVER (ORDER BY recordDate)
     then filter temperature > prev_temp

Common bugs
  - Wrong date join → cartesian product or missed pairs
  - Returning w1.id instead of w2.id (question wants the *rising* day)
  - Using <= instead of < (need strictly higher)
  - Assuming rows are sorted by date without joining on date

Complexity (typical)
  Self-join on date: O(n) rows with index on recordDate; else O(n²) nested match
  Space: O(1) extra besides result set

DE interview line
  "Self-join on consecutive dates — same pattern as comparing today vs yesterday
   metrics in a daily fact table (sessions, revenue, temperature)."

Log: add to sql/week2_sql50_log.md or week3 when you batch Basic Joins.
*/

-- =============================================================================
-- SUBMIT (your solution) — self-join + DATEDIFF(w1, w2) = -1
-- =============================================================================
-- Write your MySQL query statement below
SELECT w2.id AS Id
FROM Weather w1
JOIN Weather w2
  ON DATEDIFF(w1.recordDate, w2.recordDate) = -1
WHERE w1.temperature < w2.temperature;

-- Write your MySQL query statement below
SELECT w2.id AS Id FROM Weather w1
JOIN Weather w2 
ON DATEDIFF(w1.recordDate, w2.recordDate) = -1
AND w1.temperature < w2.temperature

-- =============================================================================
-- ALTERNATIVE 1 — DATE_ADD (often easier to read aloud in interviews)
-- w2 is the day after w1
-- =============================================================================
SELECT w2.id AS Id
FROM Weather w1
JOIN Weather w2
  ON w2.recordDate = DATE_ADD(w1.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature < w2.temperature;

-- Same join, written from w2's perspective (yesterday = today minus 1 day):
SELECT w2.id AS Id
FROM Weather w1
JOIN Weather w2
  ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL -1 DAY)
WHERE w1.temperature < w2.temperature;

-- =============================================================================
-- ALTERNATIVE 2 — flip DATEDIFF sign (equivalent to submit version)
-- DATEDIFF(today, yesterday) = 1
-- =============================================================================
SELECT w2.id AS Id
FROM Weather w1
JOIN Weather w2
  ON DATEDIFF(w2.recordDate, w1.recordDate) = 1
WHERE w1.temperature < w2.temperature;

-- =============================================================================
-- ALTERNATIVE 3 — LAG window (MySQL 8+ / BQ / Snowflake; no self-join)
-- Compare each row to previous day by recordDate order
-- =============================================================================
SELECT id AS Id
FROM (
  SELECT
    id,
    temperature,
    LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp
  FROM Weather
) t
WHERE prev_temp IS NOT NULL
  AND temperature > prev_temp;

-- BigQuery-style (DATE_ADD on prior row via LAG on dates — if dates can have gaps,
-- prefer self-join or DATE_ADD join; LAG assumes consecutive rows = consecutive days
-- only when every calendar day exists in the table):
SELECT id AS Id
FROM (
  SELECT
    id,
    temperature,
    LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
    LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date,
    recordDate
  FROM Weather
) t
WHERE prev_temp IS NOT NULL
  AND DATE_DIFF(recordDate, prev_date, DAY) = 1
  AND temperature > prev_temp;