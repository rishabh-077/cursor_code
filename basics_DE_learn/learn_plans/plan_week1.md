# Week 1 Plan — Coding, SQL/PySpark, Cloud & AI

**Phase:** 1 (Foundations) · **Tracker:** [learn_tracker.md](./learn_tracker.md) · **Roadmap:** [learn_plan_v2.md](./learn_plan_v2.md) · **Sources:** [RESOURCES.md](./RESOURCES.md) · **Hub:** [README.md](../../README.md)

## Daily time split (~3.5 hours)

| Block | Time | Focus |
|-------|------|--------|
| Python DSA | 90 min | Big O, LeetCode, Python OOP notes |
| SQL & PySpark (rotating) | 90 min | LeetCode SQL 50, Spark internals, BQ |
| Cloud & AI theory | 30 min | DDIA, vector DB concepts |

---

## 1. Python DSA (90 min daily)

- [ ] **Day 1:** Watch [Big O Notation Explained — NeetCode](https://www.youtube.com/results?search_query=neetcode+big+o+notation) (YouTube). Review [big_O_notation.md](../leetcode/big_O_notation.md).
- [ ] **Day 2:** Solve [LeetCode 217 — Contains Duplicate](https://leetcode.com/problems/contains-duplicate/). Write time & space complexity in [leetcode_217.py](../leetcode/leetcode_217.py).
- [ ] **Day 3:** Solve [LeetCode 1 — Two Sum](https://leetcode.com/problems/two-sum/) (dictionary approach).
- [ ] **Day 4:** Solve [LeetCode 242 — Valid Anagram](https://leetcode.com/problems/valid-anagram/).
- [ ] **Day 5:** Solve [LeetCode 88 — Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/).
- [ ] **Day 6:** Solve [LeetCode 121 — Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/).
- [ ] **Day 7:** Re-solve the **hardest** problem from this week from memory (no notes).

**Optional Python OOP (alongside Week 1):**

- [ ] [classes_and_instances.py](../python/classes_and_instances.py) — classes, `self`, `__init__`
- [ ] [class_variables.py](../python/class_variables.py) — class vs instance variables

---

## 2. Rotated DE fronts: SQL & PySpark (90 min daily)

### SQL — Days 1 & 3

- [ ] Go to [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/).
- [ ] Solve the **first 4** problems under **Select** and **Basic Joins**.
- [ ] Note one takeaway per problem (filter vs join, when to use `DISTINCT`, etc.).

### PySpark — Days 2 & 4

- [ ] Read about **Spark Driver vs Executor** architecture.
- [ ] Write down the difference between:
  - **Transformation** — lazy (builds a plan; nothing runs yet)
  - **Action** — eager (triggers execution, e.g. `count()`, `collect()`, `show()`)

### BigQuery internals — Day 5

- [ ] Read BigQuery **Capacitor** columnar storage docs (overview is enough for Week 1).
- [ ] Learn why `SELECT *` is an expensive anti-pattern in BQ (bytes scanned, unused columns).

---

## 3. Cloud & AI theory (30 min daily)

### Days 1–4

- [ ] Start **DDIA — Chapter 3** (*Storage and Retrieval*) to prepare before the physical book arrives.
- [ ] Jot 3 bullets per section: what problem it solves, one term you learned, one link to your GCP/BQ work.

### Days 5–6

- [ ] Read one introductory article on **“What is a Vector Database?”** (conceptual only — embeddings, similarity search, why OLTP schemas don’t fit).
- [ ] One paragraph: how this relates to RAG / GenAI data pipelines (no implementation required in Week 1).

### Day 7

- [ ] Light review: skim DDIA Ch 3 notes + Week 1 LeetCode complexity write-ups.

---

## Week 1 exit checklist

- [ ] Can explain **O(1), O(n), O(n²), O(n log n)** with one example each.
- [ ] Completed at least **5 of 6** Python LeetCode problems above.
- [ ] Completed **4** SQL 50 starter problems.
- [ ] Can explain **lazy transformation vs eager action** in Spark in your own words.
- [ ] Know why **`SELECT *`** hurts in BigQuery.

---

## Local study files

| Topic | File |
|-------|------|
| Big O cheat sheet | [../leetcode/big_O_notation.md](../leetcode/big_O_notation.md) |
| LC 217 | [../leetcode/leetcode_217.py](../leetcode/leetcode_217.py) |
| Classes & instances | [../python/classes_and_instances.py](../python/classes_and_instances.py) |
| Class variables | [../python/class_variables.py](../python/class_variables.py) |
