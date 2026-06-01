# DSA topic pacing (realistic)

**Rule:** Block A = **90 min/day**. Aim for **one topic at a time**, not four topics in one calendar week.

**Weeks run Monday → Sunday** (program start **25 May 2026 = Monday**).

| Topic | Title | Est. time | Calendar week(s) | Block A goal |
|-------|--------|-----------|------------------|--------------|
| **t01** | Big-O | 3–4 days | **1** | Theory + explain O(1)/O(n)/O(n²) aloud |
| **t02** | Arrays | 7–10 days | **1–2** | Theory + **4–6 Easy** (not every Medium) |
| **t03** | Strings | 7 days | **3** | Theory + **3–5 Easy** (anagram, palindrome, etc.) |
| **t04** | Hash maps | 7–10 days | **4** | Pattern + **4–5 Easy**, 1–2 Medium if strong |
| **t05** | Two pointers | 7 days | **5** | Pattern + **3 Easy**, then 2 Medium |
| **t06** | Sliding window | 7–10 days | **6** | Hardest pattern so far — **2–3 Easy**, then LC 3 |
| **t07** | Prefix sums | 4–5 days | **7** | **2–3 Easy** + 1 Medium (Subarray Sum = K) |
| **t08** | Stacks | 7 days | **8** | Valid Parens + **3–4 Easy** |
| **t09** | Queues | 5–7 days | **9** | BFS intro + **2–3 Easy** |
| **t10** | Linked lists | 10 days | **9–10** | Draw pointers · **4 Easy** minimum |
| **t11** | Recursion | 7 days | **11** | Abdul Bari series · **4 Easy** |
| **t12** | Tree traversals | 7–10 days | **12** | All 4 traversals · **5 Easy** |
| **t13** | BST | 7 days | **13** | Validate BST, Kth smallest |
| **t14** | Graphs BFS | 7 days | **14** | Number of Islands, Rotting Oranges |
| **t15** | Graphs DFS | 7 days | **15** | Course Schedule |
| **t16** | Topo sort | 5–7 days | **16** | Kahn's algorithm |
| **t17** | Union-find | 5–7 days | **17** | |
| **t18** | Binary search | 7 days | **18** | |
| **t19** | Heaps | 7 days | **19** | |
| **t20** | Greedy | 7 days | **20** | |
| **t21** | DP intro | **14 days** | **21–22** | 1D DP only first week |
| **t22** | Backtracking | 7–10 days | **23** | |
| **t23** | Tries | 5–7 days | **24** | |

**Phase 1 DSA exit (t01–t16):** ~**16 calendar weeks** from start (not 4 topics in Week 1).

---

## Two parallel tracks (important)

| Track | What moves weekly | File |
|-------|-------------------|------|
| **DE** | SQL 50, Spark, Zoomcamp, Chip/DDIA | [learn_plan_v2.md](./learn_plan_v2.md) DE columns |
| **DSA** | **One topic focus** from table above | This file + [dsa-study-plan.html](./dsa-study-plan.html) |

SQL can stay on **calendar Week 2 = SQL #5–8** even while DSA is still on **t02/t03**. That is normal — do not rush four DSA topics to “catch up.”

---

## If you already solved LC early (Week 1)

You may have code for 217, 1, 242, 88, 121 before finishing **theory** for t02–t04. That is fine:

1. Still tick the topic in `/dsa` only after **theory + pattern + planned Easy count**.
2. Use extra LC time for **second pass** (no hints) or Medium from that topic’s list.

---

## Where this is reflected

- [learn_plan_v2.md](./learn_plan_v2.md) — DSA column (one topic per week)
- [plan_weekN.md](./weekly_plan/) — daily Block A
- [dsa-study-plan.html](./dsa-study-plan.html) — badge on each topic
- Dashboard `/week?w=N` — `WEEK_PLAN` in `app.js`
