# Week 1 · 25 May – 31 May 2026

**Phase 1 — Foundations**  
**Tracker:** [tracker_week1.md](../weekly_tracker/tracker_week1.md) · **Program:** [learn_tracker.md](../learn_tracker.md) · **Resources:** [RESOURCES.md](../RESOURCES.md) · **Hub:** [README.md](../../../README.md)

## Daily split (~3.5 h)

| Block | Time | This week |
|-------|------|-----------|
| A | 90 min | Big O, hash maps, LeetCode |
| B | 90 min | SQL 50 (×2), PySpark arch (×2), BQ (×1) |
| C | 30 min | DDIA Ch 3, vector DB / AI intro |

---

## Day map (start 2026-05-25)

| Date | A — DSA | B — DE | C — Theory |
|------|---------|--------|------------|
| **Sun 25** | Big O video + cheat sheet | SQL50 #1 | DDIA Ch 3 start |
| **Mon 26** | LC **217** | Spark driver/executor | DDIA |
| **Tue 27** | LC **1** | SQL50 #2–3 | Vector DB video |
| **Wed 28** | LC **242** | SQL50 #4 | DDIA |
| **Thu 29** | LC **88** | BQ Capacitor + `SELECT *` | RAG intro video |
| **Fri 30** | LC **121** | Spark lazy vs action notes | DDIA |
| **Sat 31** | Re-solve hardest LC | Review SQL + Spark | Week review |

---

## 1. Python DSA (Block A)

### Day 1 — Big O (Sun 25)

| Type | Resource |
|------|----------|
| **Video** | [NeetCode — Big O](https://www.youtube.com/watch?v=BgLTDT03QtU) |
| **Read** | [big_O_notation.md](../../leetcode/big_O_notation.md) |
| **Practice** | Explain O(1), O(n), O(n²) with one example each (say aloud) |

### Day 2 — LC 217 (Mon 26)

| Type | Resource |
|------|----------|
| **Video** | [NeetCode — Contains Duplicate](https://www.youtube.com/watch?v=3OamzN90kPg) |
| **Practice** | [LeetCode 217](https://leetcode.com/problems/contains-duplicate/) → save in [leetcode_217.py](../../leetcode/leetcode_217.py) + time/space |

### Day 3 — LC 1 (Tue 27)

| Type | Resource |
|------|----------|
| **Video** | [NeetCode — Two Sum](https://www.youtube.com/watch?v=KLlXCFG5TnA) |
| **Practice** | [LeetCode 1](https://leetcode.com/problems/two-sum/) (hash map) |

### Day 4 — LC 242 (Wed 28)

| Type | Resource |
|------|----------|
| **Video** | [NeetCode — Valid Anagram](https://www.youtube.com/watch?v=9UtInBqnCgA) |
| **Practice** | [LeetCode 242](https://leetcode.com/problems/valid-anagram/) |

### Day 5 — LC 88 (Thu 29)

| Type | Resource |
|------|----------|
| **Video** | [NeetCode — Merge Sorted Array](https://www.youtube.com/watch?v=0ui1em1F9oc) |
| **Practice** | [LeetCode 88](https://leetcode.com/problems/merge-sorted-array/) |

### Day 6 — LC 121 (Fri 30)

| Type | Resource |
|------|----------|
| **Video** | [NeetCode — Best Time to Buy and Sell Stock](https://www.youtube.com/watch?v=1pkOgXD63ay) |
| **Practice** | [LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |

### Day 7 — Review (Sat 31)

- Re-solve **hardest** problem this week without notes.
- Tick [tracker_week1.md](../weekly_tracker/tracker_week1.md) exit checklist.

**Optional OOP:** [classes_and_instances.py](../../python/classes_and_instances.py) · [class_variables.py](../../python/class_variables.py) · [Corey Schafer OOP playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqIkl9taNte_P9D5gAEsOB)

---

## 2. SQL & PySpark (Block B)

### SQL — Days Sun 25 & Tue 27 (4 problems)

| Type | Resource |
|------|----------|
| **Path** | [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) → **Select #1–4** (see [week1_sql50_log.md](../../sql/week1_sql50_log.md)) |
| **Video (windows preview)** | [freeCodeCamp SQL 4h](https://www.youtube.com/watch?v=HXV3zeQKqGY) — skim joins section if rusty |

### PySpark — Days Mon 26 & Wed 28

| Type | Resource |
|------|----------|
| **Video** | [Spark architecture in 8 min](https://www.youtube.com/watch?v=AJ6Uf9bbLpg) or [Databricks — How Spark works](https://www.youtube.com/watch?v=znBa13W5ocA) |
| **Read** | [Spark cluster overview](https://spark.apache.org/docs/latest/cluster-overview.html) |
| **Write** | Transformation (lazy) vs action (eager); Driver vs Executor |

### BigQuery — Day Thu 29

| Type | Resource |
|------|----------|
| **Video** | [BigQuery architecture (Google Cloud)](https://www.youtube.com/watch?v=NCwbF1xllb4) |
| **Read** | [BQ performance best practices](https://cloud.google.com/bigquery/docs/best-practices-performance) |
| **Takeaway** | Why `SELECT *` increases bytes scanned |

---

## 3. Cloud & AI (Block C)

### Days Sun–Wed — DDIA Ch 3

| Type | Resource |
|------|----------|
| **Read** | DDIA Ch 3 (*Storage and Retrieval*) — book or [O’Reilly DDIA](https://learning.oreilly.com/library/view/designing-data-intensive/9781491903063/) |
| **Video (supplement)** | [Martin Kleppmann — Kafka/streams talk](https://www.youtube.com/watch?v=AvsaGRE79r4) (storage context) |

3 bullets per section: problem solved · one term · link to your BQ work.

### Day Tue 27 — Vector DBs

| Type | Resource |
|------|----------|
| **Video** | [What are vector databases?](https://www.youtube.com/watch?v=klTvEwg3oJ4) |
| **Read** | [Pinecone — vector database guide](https://www.pinecone.io/learn/vector-database/) |

### Day Thu 29 — RAG intro

| Type | Resource |
|------|----------|
| **Video** | [RAG explained (IBM)](https://www.youtube.com/watch?v=T-D1OfcDW1M) or [Google — What is RAG](https://www.youtube.com/watch?v=qaW4l-uBAEE) |
| **Read** | [Google Cloud — RAG overview](https://cloud.google.com/use-cases/retrieval-augmented-generation) |

One paragraph: how RAG relates to your Endeavour Gemini work.

### Day Sat 31 — Review

- Skim DDIA notes + LC complexity write-ups.
- Update [tracker_week1.md](../weekly_tracker/tracker_week1.md).

---

## Week 1 exit checklist

*Synced 2026-05-25 — detail in [tracker_week1.md](../weekly_tracker/tracker_week1.md)*

- [x] Explain O(1), O(n), O(n²), O(n log n) with examples → [big_O_notation.md](../../leetcode/week_1/big_O_notation.md)
- [ ] 5+ of 6 LeetCode problems in repo with complexity *(4/6: 217, 1, 242, 88 — add **121**)*
- [x] 4 SQL 50 problems done → [sql/week1_sql50_log.md](../../sql/week1_sql50_log.md)
- [x] Spark Driver/Executor in own words → [pyspark/week1_notes.md](../../pyspark/week1_notes.md)
- [ ] Spark lazy vs action in own words *(TODO in same file)*
- [ ] BQ `SELECT *` anti-pattern explained

---

## All Week 1 links

See [RESOURCES.md — Week 1 quick list](../RESOURCES.md#week-1-quick-links).
