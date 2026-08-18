# Master plan — DE interview prep (single source of truth)

**Profile:** [learn_plans/profile.md](learn_plans/profile.md) · **Original start:** 2026-05-25 · **Rebased week math:** `meta.startDate` **2026-07-06** (Week 6 = **10–16 Aug 2026**) · **Apply target:** ~curriculum Week 28 (~**Jan 2027** after slip) · **Daily time:** 2–3 h  
**Agents:** read [CONTEXT.md](CONTEXT.md) first (repo map, sync rules, how to add new weeks).

This file does **not** change every week. Weekly tasks live in `weekly_plans/week_NN.md`. **DE / theory / system design / data modeling by calendar week:** [DE_CURRICULUM.md](DE_CURRICULUM.md) · **Video URLs:** [learn_plans/RESOURCES.md](learn_plans/RESOURCES.md). Daily UI: Flask portal → http://127.0.0.1:5050/portal

---

## Rules (non-negotiable)

1. **Early Phase 1 (weeks 1–8):** One primary subject per day — **DSA only** (~2–2.5 h). Optional **30 min SQL** on **Tuesday + Thursday only** (LeetCode SQL 50).
2. **Never 3 subjects in one day** in Phase 1. No Spark + theory + SQL + DSA on the same evening.
3. **Late Phase 1 (weeks 9–16):** DSA 1.5 h **or** SQL/DE 45 min — not both as equal priorities same day.
4. **Topic mastery before advancing:** Easy LC **without hints** for that topic + **≥1 Medium attempted** → see [trackers/phase_checklist.md](trackers/phase_checklist.md).
5. **DSA order:** [learn_plans/DSA_PACING.md](learn_plans/DSA_PACING.md) — t01 → t23, one focus per calendar week.
6. **Weekly plans:** Generated **one week at a time** (Sunday reflection → draft in portal → refine in Cursor).

---

## Phase 1 — Weeks 1–16: DSA foundation (PRIMARY)

**Goal:** Solve Easy LC without hints; attempt ≥1 Medium per topic.  
**Exit (all required):** t01–t16 complete · 35+ LC logged · SQL 50 ≥30/50 · explain array/hash/graph patterns aloud.

| Weeks | Daily shape |
|-------|-------------|
| **1–8** | 2–2.5 h DSA · Tue/Thu +30 min SQL 50 only |
| **9–16** | 1.5 h DSA · 45 min SQL **or** one DE concept (alternate days) |

**DSA topics (one per week):** t01 → t02 → t03 → t04 → t05 → t06 → t07 → t08 → t09 → t10 → t11 → t12 → t13 → t14 → t15 → t16

**Curriculum detail:** [learn_plans/dsa-study-plan.html](learn_plans/dsa-study-plan.html)

---

## Phase 2 — Weeks 17–24: DE depth (SHIFT FOCUS)

**Goal:** System design + streaming + GCP depth; DSA maintenance.

| Day | Focus |
|-----|--------|
| Mon / Wed / Fri | DE topic (2–2.5 h) — one per week |
| Tue / Thu | DSA t17–t23 (1.5 h), same mastery rule |
| Sat | SQL / DataLemur or system design reading (2 h) |

**DE topics (order):** Spark internals → Kafka/streaming → data modelling → dbt → CDC/reliability → batch/streaming design → RAG project → GCP architecture

**Exit:** t01–t23 · 60+ LC · batch + streaming whiteboard · public RAG repo · Spark shuffle + BQ partitioning explained without notes

---

## Phase 3 — Weeks 25–30: Interview simulation

| Day | Focus |
|-----|--------|
| Mon / Wed | Timed LC Medium (25 min) |
| Tue / Thu | System design mock |
| Fri | STAR / behavioral |
| Sat | Apply + follow-up |

**Apply order:** Razorpay → Walmart GTC → Fivetran → Databricks/Snowflake → JPMorgan → Google

---

## What stays in the repo (reference only)

| Keep | Do not use as daily driver |
|------|---------------------------|
| [trackers/portal_week_NN.md](trackers/) | Portal daily tasks + logs (synced from JSON) |
| [trackers/lc_log.md](trackers/lc_log.md) | All LC progress |
| [trackers/phase_checklist.md](trackers/phase_checklist.md) | DSA mastery gates |
| [dashboard/data/progress.json](dashboard/data/progress.json) | **Only** `meta` + `portal` (no per-week legacy blocks) |
| [learn_plans/_archive/](learn_plans/_archive/) | Old plans, tracker_weekN, Block A/B/C UI |
| [learn_plans/DSA_PACING.md](learn_plans/DSA_PACING.md) | `learn_plan_v2.md` parallel DE columns (historical) |
| [DE_CURRICULUM.md](DE_CURRICULUM.md) | Week-by-week DE / theory / SD map (use with RESOURCES) |
| [learn_plans/RESOURCES.md](learn_plans/RESOURCES.md) | StrataScratch / Zoomcamp in Phase 1 daily |
| [trackers/lc_log.md](trackers/lc_log.md) | — |
| Flask dashboard + **Sync to Markdown** | — |

---

## Your progress snapshot (2026-08-17)

| Item | Status |
|------|--------|
| **Phase** | 1 · Curriculum **Week 7** (**17–23 Aug 2026**) |
| **DSA** | t01–t06 ✅ · **t07 Prefix sums** (wk 7 primary) |
| **Calendar** | Week **8** starts **Mon 24 Aug** (t08 Stacks) |
| **SQL 50** | ~24/50 · this week **#25–28** (target ~28/50) |
| **Theory** | Chip Ch 1 · Zoomcamp still backlog — Sat optional only |
| **Apply** | ~curriculum week 28 ≈ **Jan 2027** (6-week slip) |

*Detail:* [CONTEXT.md](CONTEXT.md) §10 · [weekly_plans/week_07.md](weekly_plans/week_07.md) · [learn_tracker.md](learn_plans/learn_tracker.md)
