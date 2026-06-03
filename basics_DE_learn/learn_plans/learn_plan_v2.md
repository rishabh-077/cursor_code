# Master roadmap — 30 weeks

> **Active plan:** [MASTER_PLAN.md](../MASTER_PLAN.md) + [weekly_plans/](../weekly_plans/) + portal `/portal`.  
> This file is the **historical 30-week calendar** — keep for reference; do not stack 3 subjects/day in Phase 1.

**Start:** 2026-05-25 (**Monday**) · **Weeks:** Mon → Sun · **Profile:** [profile.md](./profile.md) · **Daily:** 2–3 h

---

## One study system (read this once)

You have **one DSA curriculum** and **one calendar** that wraps it with SQL, Spark, and theory.

| What | File | Your job |
|------|------|----------|
| **DSA (Block A) — THE main prep** | [dsa-study-plan.html](./dsa-study-plan.html) | **One topic at a time** — see [DSA_PACING.md](./DSA_PACING.md) |
| **This week’s tasks** | [plan_weekN.md](./weekly_plan/plan_week1.md) | Block A topic + SQL/Spark/theory |
| **Mark progress** | [Dashboard](../dashboard/README.md) → `/dsa` + `/week?w=N` | Tick topics + weekly items |
| **30-week calendar** | This file (below) | DE/SQL/theory by calendar week · DSA by pacing table |

**Pacing change:** t01–t04 in one week or t05–t07 in one week is **not** realistic at 90 min/day. Use **[DSA_PACING.md](./DSA_PACING.md)** — roughly **one DSA topic per calendar week** (t02 and t10 span two weeks).

### Block A flow (every study day, 90 min)

1. Open [dsa-study-plan.html](./dsa-study-plan.html) (or http://127.0.0.1:5050/dsa).
2. Check **this week’s ONE topic** in the table below (e.g. calendar Week 2 = finish **t02**, not t05).
3. For that topic: **Theory** → **Watch** → **Pattern** → **Easy problems** (counts in pacing doc).
4. Save code in `leetcode/week_N/` · tick topic in `/dsa` when truly done.
5. **DE track (SQL/Spark) continues on calendar week** even if DSA is slower — see “Two parallel tracks” in [DSA_PACING.md](./DSA_PACING.md).

---

## Daily split

| Block | Time | Focus |
|-------|------|--------|
| **A** | 90 min | **[dsa-study-plan.html](./dsa-study-plan.html)** — **one topic** from pacing table |
| **B** | 90 min | SQL 50 · PySpark · BQ/dbt (per calendar week) |
| **C** | 30–45 min | Chip Huyen *AI Engineering* (until **8 Jun 2026**) → then DDIA |
| Buffer | 15 min | [learn_tracker.md](./learn_tracker.md) |

---

## DSA curriculum phases (from your study plan)

Same order as [dsa-study-plan.html](./dsa-study-plan.html):

| DSA phase | Topics | Realistic span |
|-----------|--------|----------------|
| **1 — Absolute basics** | t01–t04 | Weeks **1–4** |
| **1 — Core patterns** | t05–t07 | Weeks **5–7** |
| **2 — Linear structures** | t08–t10 | Weeks **8–10** |
| **2 — Trees** | t11–t13 | Weeks **11–13** |
| **3 — Graphs** | t14–t17 | Weeks **14–17** |
| **3 — Heaps / intervals** | t18–t20 | Weeks **18–20** |
| **4 — Advanced** | t21–t23 | Weeks **21–24** |

Full problem lists and videos live **only** in the HTML file.

---

## PHASE 1 — Calendar (DE + DSA)

**DSA column = one primary topic.** SQL/Spark columns follow **calendar week** (may run ahead of DSA — OK).

| Cal wk | Dates | **DSA (Block A)** | Block B (DE) | Block C (theory) |
|--------|-------|-------------------|--------------|------------------|
| **1** | Mon 25 – Sun 31 May | **t01** Big-O · start **t02** Arrays | SQL50 #1–4 · Spark driver | Chip Ch1–2 |
| **2** | Mon 1 – Sun 7 Jun | **t02** Arrays finish · start **t03** Strings | SQL50 #5–8 · Zoomcamp | Chip Ch3–4 |
| **3** | 8–14 Jun | **t03** Strings finish | SQL50 #9–12 · dbt | **DDIA Ch3** (book arrives) |
| **4** | 15–21 Jun | **t04** Hash maps | SQL50 #13–16 · BQ | RAG overview |
| **5** | 22–28 Jun | **t05** Two pointers | SQL50 #17–20 | Chip / DDIA |
| **6** | 29 Jun – 5 Jul | **t06** Sliding window | SQL50 #21–25 | DDIA |
| **7** | 6–12 Jul | **t07** Prefix sums | Finish SQL 50 | — |
| **8** | 13–19 Jul | **t08** Stacks | StrataScratch | Chunking |
| **9** | 20–26 Jul | **t09** Queues · **t10** LL start | STAR stories | Review |
| **10** | 27 Jul – 2 Aug | **t10** Linked lists finish | Pipeline whiteboard | — |
| **11** | 3–9 Aug | **t11** Recursion | Mock LC easy | DDIA |
| **12** | 10–16 Aug | **t12** Tree traversals | — | — |
| **13** | 17–23 Aug | **t13** BST | — | — |
| **14** | 24–30 Aug | **t14** Graphs BFS | — | — |
| **15** | 31 Aug – 6 Sep | **t15** DFS | — | — |
| **16** | 7–13 Sep | **t16** Topo sort · review t01–t16 | Phase 1 DSA exam | Phase 1 exit |

**Week plans:** [plan_week1](./weekly_plan/plan_week1.md) · [plan_week2](./weekly_plan/plan_week2.md) · [plan_week3](./weekly_plan/plan_week3.md) · …

**Phase 1 exit (revised):** **t01–t16** in DSA plan · SQL 50 done · Zoomcamp · 35+ LC saved · PySpark story · STAR ready (~**mid Sep 2026** for DSA portion)

---

## PHASE 2 — Weeks 17–26 (DSA t17–t23 + systems)

| Cal wk | DSA topics (HTML) | DE / streaming | AI |
|--------|-------------------|----------------|-----|
| **17** | **t17** Union-find | Kafka / Pub/Sub | — |
| **18** | **t18** Binary search | Event time · DDIA Ch 11 | — |
| **19** | **t19** Heaps | Late data | — |
| **20** | **t20** Greedy | — | — |
| **21–22** | **t21** DP (2 weeks) | **RAG MVP** | [rag_side_project](../projects/rag_side_project.md) |
| **23** | **t22** Backtracking | Spark tuning | — |
| **24** | **t23** Tries | Batch system design doc | Enterprise RAG |
| **25** | Review weak DSA topics | Streaming design doc | — |
| **26** | Phase 2 DSA exam | 2 design docs | AI pitch |

**Phase 2 exit:** **t01–t23** complete · 60+ LC · streaming whiteboard · public RAG repo

---

## PHASE 3 — Applications (shift ~6 weeks later if you follow realistic DSA)

| Wk | Focus |
|----|--------|
| **27** | Resume polish |
| **28** | **Start applications** (was week 21 on old aggressive timeline) |
| **29–30** | Mocks · interviews · negotiate |

*Original “apply week 21” (~Oct 2026) assumed faster DSA. With realistic pacing, target **apply ~late Nov 2026** unless you add extra daily time. Update [learn_tracker.md](./learn_tracker.md) when you commit.*

---

## Goals

| When | Target |
|------|--------|
| Month 0–6 | DSA t01–t16 + SQL 50 + pipeline stories |
| Month 7–9 | t17–t23 + RAG |
| **Apply** | **~Week 28** (realistic DSA) or earlier if you study 5+ h/day |
| Month 5–7 pay | **35–42 LPA** |

---

## Other files

| File | Role |
|------|------|
| [DSA_PACING.md](./DSA_PACING.md) | Days per topic · two-track model |
| [RESOURCES.md](./RESOURCES.md) | Verified video links |
| [theory_reading.md](./theory_reading.md) | Chip Huyen until 8 Jun, then DDIA |
| [HOW_TO_USE.md](./HOW_TO_USE.md) | Daily / Sunday routine |
| [learn_tracker.md](./learn_tracker.md) | Phases · milestones |
| [VERIFIED_VIDEOS.md](./VERIFIED_VIDEOS.md) | Link checks |

**Old note:** [dsa_week_map.md](./dsa_week_map.md) is retired — use **DSA_PACING.md** + this file.
