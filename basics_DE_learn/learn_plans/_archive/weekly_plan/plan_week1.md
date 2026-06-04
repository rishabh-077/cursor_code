# Week 1 · Mon 25 May – Sun 31 May 2026

**Calendar:** [MASTER_PLAN.md](../../MASTER_PLAN.md) · Week 1 archive

---

## Block A (90 min) — [dsa-study-plan.html](../dsa-study-plan.html)

**Realistic pace:** [DSA_PACING.md](../DSA_PACING.md) — **not** four topics in one week.

**This week:** **t01** Big-O (finish) · **start t02** Arrays only.

| Topic | Target this week | Notes |
|-------|------------------|-------|
| **t01** | 3–4 days theory + drills | [big_O_notation.md](../../leetcode/week_1/big_O_notation.md) |
| **t02** | Start only — theory + 1–2 Easy | You may have 217/88/121 code early; still do t02 theory in HTML |

**Do not** tick t03/t04 in `/dsa` this week — those are Weeks 3–4.

LC you already wrote (217, 1, 242, 88, 121) counts toward **later** topics when you reach them officially.

## Blocks B + C (~2 h)

| Block | This week |
|-------|-----------|
| B | SQL50 #1–4 · Spark driver/executor · BQ (carry if open) |
| C | Chip Huyen Ch1–2 · vector DB video |

**Tracker:** [tracker_week1.md](../weekly_tracker/tracker_week1.md)

---

## Day map (start 2026-05-25 = **Monday**)

| Date | A — DSA | B — DE | C — Theory |
|------|---------|--------|------------|
| **Mon 25** | Big O video + cheat sheet | SQL50 #1 | Chip Huyen Ch 1–2 |
| **Tue 26** | LC **217** | Spark driver/executor | Chip Huyen |
| **Wed 27** | LC **1** | SQL50 #2–3 | Vector DB video |
| **Thu 28** | LC **242** | SQL50 #4 | Chip Huyen |
| **Fri 29** | LC **88** | BQ Capacitor + `SELECT *` | RAG intro video |
| **Sat 30** | LC **121** | Spark lazy vs action notes | Chip Huyen |
| **Sun 31** | Re-solve hardest LC | Review SQL + Spark | Week review |

---

## Block A — day detail (same topics as HTML plan)

### Day 1 — topic **t01** Big-O (Mon 25)

| Type | Resource |
|------|----------|
| **Video** | [NeetCode — Big O](https://www.youtube.com/watch?v=BgLTDT03QtU) |
| **Read** | [big_O_notation.md](../../leetcode/big_O_notation.md) |
| **Practice** | Explain O(1), O(n), O(n²) with one example each (say aloud) |

### Day 2 — topic **t02** Arrays + LC 217 (Tue 26)

| Type | Resource |
|------|----------|
| **Video** | [NeetCode — Contains Duplicate](https://www.youtube.com/watch?v=3OamzN90kPg) |
| **Practice** | [LeetCode 217](https://leetcode.com/problems/contains-duplicate/) → save in [leetcode_217.py](../../leetcode/leetcode_217.py) + time/space |

### Day 3 — topic **t04** Hash + LC 1 (Wed 27)

| Type | Resource |
|------|----------|
| **Video** | [NeetCode — Two Sum](https://www.youtube.com/watch?v=KLlXCFG5TnA) |
| **Practice** | [LeetCode 1](https://leetcode.com/problems/two-sum/) (hash map) |

### Day 4 — topic **t03** Strings + LC 242 (Thu 28)

| Type | Resource |
|------|----------|
| **Video** | [NeetCode — Valid Anagram](https://www.youtube.com/watch?v=9UtInBqnCgA) |
| **Practice** | [LeetCode 242](https://leetcode.com/problems/valid-anagram/) |

### Day 5 — topic **t02** + LC 88 (Fri 29)

| Type | Resource |
|------|----------|
| **Video** | [NeetCode — Merge Sorted Array](https://www.youtube.com/watch?v=0ui1em1F9oc) |
| **Practice** | [LeetCode 88](https://leetcode.com/problems/merge-sorted-array/) |

### Day 6 — topic **t02** + LC 121 (Sat 30)

| Type | Resource |
|------|----------|
| **Video** | [NeetCode — Best Time to Buy and Sell Stock](https://www.youtube.com/watch?v=1pkOgXD63ay) |
| **Practice** | [LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |

### Day 7 — Review (Sun 31)

- Re-solve **hardest** problem this week without notes.
- Tick [tracker_week1.md](../weekly_tracker/tracker_week1.md) exit checklist.

**Optional OOP:** [classes_and_instances.py](../../python/classes_and_instances.py) · [class_variables.py](../../python/class_variables.py) · [Corey Schafer OOP playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqIkl9taNte_P9D5gAEsOB)

---

## 2. SQL & PySpark (Block B)

### SQL — Days Mon 25 & Wed 27 (4 problems)

| Type | Resource |
|------|----------|
| **Path** | [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) → **Select #1–4** (see [week1_sql50_log.md](../../sql/week1_sql50_log.md)) |
| **Video (windows preview)** | [freeCodeCamp SQL 4h](https://www.youtube.com/watch?v=HXV3zeQKqGY) — skim joins section if rusty |

### PySpark — Days Tue 26 & Thu 28

| Type | Resource |
|------|----------|
| **Video** | [Spark architecture in 8 min](https://www.youtube.com/watch?v=AJ6Uf9bbLpg) or [Databricks — How Spark works](https://www.youtube.com/watch?v=znBa13W5ocA) |
| **Read** | [Spark cluster overview](https://spark.apache.org/docs/latest/cluster-overview.html) |
| **Write** | Transformation (lazy) vs action (eager); Driver vs Executor |

### BigQuery — Day Fri 29

| Type | Resource |
|------|----------|
| **Video** | [BigQuery architecture (Google Cloud)](https://www.youtube.com/watch?v=NCwbF1xllb4) |
| **Read** | [BQ performance best practices](https://cloud.google.com/bigquery/docs/best-practices-performance) |
| **Takeaway** | Why `SELECT *` increases bytes scanned |

---

## 3. Theory (Block C) — Chip Huyen until DDIA arrives **8 Jun 2026**

| Type | Resource |
|------|----------|
| **Read** | *AI Engineering* (Chip Huyen) Ch 1–2 — see [theory_reading.md](../theory_reading.md) |
| **Notes** | [theory/ai_engineering_notes.md](../../theory/ai_engineering_notes.md) |

3 bullets per chapter: one term · Endeavour/Gemini link · one interview sentence.

*DDIA Ch 3 starts **Monday 8 Jun** — see [plan_week2.md](./plan_week2.md) / Week 3.*

### Day Tue 27 — Vector DBs

| Type | Resource |
|------|----------|
| **Video** | [What are vector databases?](https://www.youtube.com/watch?v=klTvEwg3oJ4) |
| **Read** | [Pinecone — vector database guide](https://www.pinecone.io/learn/vector-database/) |

### Day Fri 29 — RAG intro

| Type | Resource |
|------|----------|
| **Video** | [RAG explained (IBM)](https://www.youtube.com/watch?v=T-D1OfcDW1M) or [Google — What is RAG](https://www.youtube.com/watch?v=qaW4l-uBAEE) |
| **Read** | [Google Cloud — RAG overview](https://cloud.google.com/use-cases/retrieval-augmented-generation) |

One paragraph: how RAG relates to your Endeavour Gemini work.

### Day Sun 31 — Review

- Skim DDIA notes + LC complexity write-ups.
- Update [tracker_week1.md](../weekly_tracker/tracker_week1.md).

---

## Week 1 exit checklist

*Synced 2026-05-25 — detail in [tracker_week1.md](../weekly_tracker/tracker_week1.md)*

- [x] Explain O(1), O(n), O(n²), O(n log n) with examples → [big_O_notation.md](../../leetcode/week_1/big_O_notation.md)
- [x] 5+ of 6 LeetCode problems in repo with complexity → [leetcode_121.py](../../leetcode/week_1/leetcode_121.py) added
- [x] 4 SQL 50 problems done → [sql/week1_sql50_log.md](../../sql/week1_sql50_log.md)
- [x] Spark Driver/Executor in own words → [pyspark/week1_notes.md](../../pyspark/week1_notes.md)
- [ ] Spark lazy vs action in own words *(TODO in same file)*
- [ ] BQ `SELECT *` anti-pattern explained

---

## All Week 1 links

See [RESOURCES.md — Week 1 quick list](../RESOURCES.md#week-1-quick-links).
