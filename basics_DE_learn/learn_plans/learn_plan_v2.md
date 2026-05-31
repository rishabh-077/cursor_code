# Master roadmap — 30 weeks

**Start:** 2026-05-25 · **Profile:** [profile.md](./profile.md) · **Daily:** 3–4 h

---

## One study system (read this once)

You have **one DSA curriculum** and **one calendar** that wraps it with SQL, Spark, and theory.

| What | File | Your job |
|------|------|----------|
| **DSA (Block A) — THE main prep** | [dsa-study-plan.html](./dsa-study-plan.html) | Study **topic by topic in order** (t01 → t23): theory → video → pattern → practice |
| **This week’s tasks** | [plan_week1.md](./weekly_plan/plan_week1.md), [plan_week2.md](./weekly_plan/plan_week2.md), … | Which **topics** + which **SQL/Spark/theory** this calendar week |
| **Mark progress** | [Dashboard](../dashboard/README.md) → `/dsa` + `/week?w=N` | Tick topics + weekly items |
| **30-week calendar** | This file (below) | Which DSA topics fit in each **calendar week** alongside DE |

**You do not follow two DSA plans.** The old roadmap listed random LeetCode IDs per week. That is replaced by the **comprehensive DSA plan** you added. Block A = only that plan.

### Block A flow (every study day, 90 min)

1. Open [dsa-study-plan.html](./dsa-study-plan.html) (or http://127.0.0.1:5050/dsa).
2. Find **this week’s topics** in the table below (e.g. Week 2 = **t05**, **t06**).
3. For each topic: read **Theory** → watch **Resources** → learn **Pattern** → solve **Easy problems first** (then Medium if time).
4. Save code in `leetcode/week_N/` · tick topic when done.
5. Ignore other problems in that topic until a later week unless marked optional.

---

## Daily split

| Block | Time | Focus |
|-------|------|--------|
| **A** | 90 min | **[dsa-study-plan.html](./dsa-study-plan.html)** — topics scheduled below |
| **B** | 90 min | SQL 50 · PySpark · BQ/dbt (per week) |
| **C** | 30–45 min | Chip Huyen *AI Engineering* (until **8 Jun 2026**) → then DDIA |
| Buffer | 15 min | [learn_tracker.md](./learn_tracker.md) |

---

## DSA curriculum phases (from your study plan)

Same order as [dsa-study-plan.html](./dsa-study-plan.html):

| DSA phase | Topics | Content |
|-----------|--------|---------|
| **1 — Absolute basics** | t01–t04 | Big-O, arrays, strings, hash maps |
| **1 — Core patterns** | t05–t07 | Two pointers, sliding window, prefix sums |
| **2 — Linear structures** | t08–t10 | Stacks, queues, linked lists |
| **2 — Trees** | t11–t13 | Recursion, traversals, BST |
| **3 — Graphs** | t14–t17 | BFS, DFS, topo sort, union-find |
| **3 — Heaps / intervals** | t18–t20 | Heaps, intervals, greedy |
| **4 — Advanced** | t21–t23 | DP, backtracking, tries |

Full problem lists and videos live **only** in the HTML file — not duplicated here.

---

## PHASE 1 — Calendar weeks 1–10 (DSA + DE together)

**Block A = topics column.** Do those topics in the HTML plan. **Block B/C** = same as before.

| Cal wk | Dates | DSA topics (do in HTML) | Block B (DE) | Block C (theory) |
|--------|-------|-------------------------|--------------|------------------|
| **1** | 25–31 May | **t01** Big-O · **t02** Arrays · **t03** Strings · **t04** Hash | SQL50 #1–4 · Spark driver | Chip Huyen Ch1–2 |
| **2** | 1–7 Jun | **t05** Two pointers · **t06** Sliding window · **t07** Prefix (if time) | SQL50 #5–8 · Zoomcamp | Chip Huyen Ch3–4 |
| **3** | 8–14 Jun | **t07** finish · **t08** Stacks | SQL50 #9–12 · dbt | **DDIA Ch3** (book arrives) |
| **4** | 15–21 Jun | **t09** Queues · **t10** Linked lists (start) | SQL50 #13–16 · BQ | RAG overview |
| **5** | 22–28 Jun | **t10** finish · **t11** Recursion | SQL50 #17–20 | — |
| **6** | 29 Jun – 5 Jul | **t12** Tree traversals | SQL50 #21–25 | DDIA |
| **7** | 6–12 Jul | **t13** BST | Finish SQL 50 | — |
| **8** | 13–19 Jul | **t14** Graphs BFS | StrataScratch | Chunking |
| **9** | 20–26 Jul | **t15–t16** DFS · Topo sort | STAR stories | Review |
| **10** | 27 Jul – 2 Aug | Review **t01–t16** · timed LC | Pipeline whiteboard | Phase 1 exam |

**Week 1 plan:** [plan_week1](./weekly_plan/plan_week1.md) · **Week 2:** [plan_week2](./weekly_plan/plan_week2.md) · **Trackers:** [weekly_tracker/](./weekly_tracker/)

**Phase 1 exit:** All topics **t01–t16** ticked in DSA plan · SQL 50 done · Zoomcamp · 35+ LC saved · PySpark story · STAR ready

---

## PHASE 2 — Weeks 11–20 (DSA continues t17–t23 + systems)

| Cal wk | DSA topics (HTML) | DE / streaming | AI |
|--------|-------------------|----------------|-----|
| **11** | **t17** Union-find · **t18** Heaps start | Kafka / Pub/Sub | — |
| **12** | **t18** finish · **t19** Intervals | Event time · DDIA Ch 11 | — |
| **13** | **t20** Greedy | DDIA Ch 5–6 | — |
| **14** | **t21** DP intro | Late data · **RAG MVP** | [rag_side_project](../projects/rag_side_project.md) |
| **15** | **t21** DP | Composer / DAG story | — |
| **16** | **t22** Backtracking | Spark tuning | — |
| **17** | **t23** Tries | Batch system design doc | Enterprise RAG |
| **18** | Review weak DSA topics | Streaming design doc | — |
| **19** | Mixed Medium timed | CDC / lakehouse | RAG polish |
| **20** | Phase 2 DSA exam | 2 design docs | AI pitch |

**Phase 2 exit:** **t01–t23** complete · 60+ LC · streaming whiteboard · public RAG repo

---

## PHASE 3 — Weeks 21–30 (interviews)

| Wk | Focus |
|----|--------|
| **21** | Resume · **start applications** |
| **22** | 8 STAR stories |
| **23–24** | Coding + DE design mocks |
| **25–28** | Applications + live interviews |
| **29–30** | Gap sprint · negotiate |

---

## Goals & apply date

| When | Target |
|------|--------|
| Month 0–4 | Follow DSA plan + SQL 50 + pipeline stories |
| Month 5–7 | **35–42 LPA** |
| **Apply** | **Week 21+** (~12 Oct 2026) |

---

## Other files

| File | Role |
|------|------|
| [RESOURCES.md](./RESOURCES.md) | Verified video links |
| [theory_reading.md](./theory_reading.md) | Chip Huyen until 8 Jun, then DDIA |
| [HOW_TO_USE.md](./HOW_TO_USE.md) | Daily / Sunday routine |
| [learn_tracker.md](./learn_tracker.md) | Phases · milestones · interviews |
| [VERIFIED_VIDEOS.md](./VERIFIED_VIDEOS.md) | Link checks |

**Old note:** [dsa_week_map.md](./dsa_week_map.md) is retired — schedule lives in **this file** + [dsa-study-plan.html](./dsa-study-plan.html).
