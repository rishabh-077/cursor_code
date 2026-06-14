/*
1661. Average Time of Process per Machine
https://leetcode.com/problems/average-time-of-process-per-machine/

Problem
  Table Activity(machine_id, process_id, activity_type, timestamp)
  activity_type is 'start' or 'end'.
  Each (machine_id, process_id) has exactly one start row and one end row.
  Return machine_id and processing_time = average duration per machine,
  rounded to 3 decimal places.

Example
  machine_id | process_id | activity_type | timestamp
  0          | 0          | start         | 0.712
  0          | 0          | end           | 1.520
  0          | 1          | start         | 3.140
  0          | 1          | end           | 4.120
  → machine_id 0, processing_time = ROUND(AVG(0.808, 0.980), 3) = 0.894

Pattern — self-join / pair events (Basic Joins / SQL 50 #10)
  Match each **start** row to its **end** row on (machine_id, process_id).
  Duration = end.timestamp - start.timestamp.
  Aggregate with AVG(...) GROUP BY machine_id.

Your approach (self-join on start + end)
  - Pair start (a1) with end (a2) on machine_id AND process_id
  - processing_time = AVG(a2.timestamp - a1.timestamp)
  - ROUND(..., 3) and GROUP BY machine_id

Pro tip (start/end pairing)

Whenever you see:
  event logs with 'start' / 'end' (or open / close)
Think:
  - Self-join same table: start alias ⋈ end alias
  - Join keys = entity id + session/process id (here: machine_id + process_id)
  - Duration = end_time - start_time → AVG or SUM per group

Same pattern as session length, job runtime, or request latency in production logs.

Approach comparison
  | Approach                          | Notes                              |
  |-----------------------------------|------------------------------------|
  | Subquery filter start/end + JOIN  | Your first draft — clear separation|
  | Single table self-join + WHERE    | Preferred — submit below           |
  | Conditional aggregation (MAX CASE)| One pass; harder to read           |

Common bugs
  - Joining only on machine_id (misses process_id → wrong pairings)
  - Forgetting ROUND(..., 3) (LeetCode checks precision)
  - GROUP BY wrong column (need machine_id, not process_id)
  - Filtering activity_type in ON instead of WHERE (usually same result here)

Complexity (typical)
  Join on (machine_id, process_id): O(n) with index; one row per process
  Space: O(1) extra besides result set

DE interview line
  "Pair start/end events on a composite key, then AVG duration per machine —
   same idea as measuring average task runtime from Airflow/Spark event logs."

Log: sql/week3_sql50_log.md (#10)
*/

-- =============================================================================
-- SUBMIT (your solution) — self-join with WHERE on activity_type
-- =============================================================================
SELECT
  a1.machine_id,
  ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM Activity a1
INNER JOIN Activity a2
  ON a1.machine_id = a2.machine_id
  AND a1.process_id = a2.process_id
WHERE a1.activity_type = 'start'
  AND a2.activity_type = 'end'
GROUP BY a1.machine_id;

-- =============================================================================
-- ALTERNATIVE 1 — subqueries (your first draft; equivalent logic)
-- =============================================================================
SELECT
  a1.machine_id,
  ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM (
  SELECT * FROM Activity WHERE activity_type = 'start'
) a1
INNER JOIN (
  SELECT * FROM Activity WHERE activity_type = 'end'
) a2
  ON a1.machine_id = a2.machine_id
  AND a1.process_id = a2.process_id
GROUP BY a1.machine_id;

-- =============================================================================
-- ALTERNATIVE 2 — conditional aggregation (one scan; no self-join)
-- Pivot start/end per (machine_id, process_id), then AVG per machine
-- =============================================================================
SELECT
  machine_id,
  ROUND(AVG(end_ts - start_ts), 3) AS processing_time
FROM (
  SELECT
    machine_id,
    process_id,
    MAX(CASE WHEN activity_type = 'start' THEN timestamp END) AS start_ts,
    MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end_ts
  FROM Activity
  GROUP BY machine_id, process_id
) per_process
GROUP BY machine_id;
