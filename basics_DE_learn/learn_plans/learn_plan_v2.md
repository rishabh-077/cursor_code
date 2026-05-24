# Master roadmap — 30 weeks (compact)

**You:** 3.5 YOE DE · GCP · Tiger (Lowe’s, Endeavour) · 25 LPA → **35–42 LPA** · 2-month notice · [profile.md](./profile.md)  
**Daily:** 3–4 h · **Sources:** [RESOURCES.md](./RESOURCES.md) · **How to run:** [HOW_TO_USE.md](./HOW_TO_USE.md) · **Progress:** [learn_tracker.md](./learn_tracker.md)

> Week-by-day tasks live in `plan_weekN.md` (Week 1 ready). Don’t pre-build all 30 weeks — update tracker weekly.

---

## Goals

| When | Target |
|------|--------|
| Month 0–4 | Prep only — Easy/Medium LC, SQL 50, pipeline stories |
| Month 5–7 | **35–42 LPA** — 40+ LC, system design, STAR ready |
| Month 7–9 | **42–50 LPA** stretch — streaming + mocks clean |
| Apply | **Week 21+** (2-month notice) |

**Interview bar:** Many targets (Google, Databricks, Razorpay) include coding — DSA from zero needs Phase 1 complete before Tier A.

---

## Daily split

| Block | Time | Focus |
|-------|------|--------|
| A | 90 min | DSA — NeetCode + LeetCode → `leetcode/` |
| B | 90 min | SQL · PySpark · BQ/dbt (rotate) |
| C | 30–45 min | DDIA · streaming · AI |
| Buffer | 15 min | [learn_tracker.md](./learn_tracker.md) |

**DSA rules:** pattern video → 20 min try → hints OK → re-solve next day → log time/space complexity.

---

## Phase overview

| Phase | Weeks | Outcome |
|-------|-------|---------|
| **1 Foundations** | 1–10 | SQL 50 + StrataScratch · Zoomcamp Spark · Easy/Medium LC · BQ/dbt stories |
| **2 Systems + AI** | 11–20 | Kafka/Pub/Sub · DDIA · RAG project · Medium LC · 2 system designs |
| **3 Interviews** | 21–30 | Resume · mocks · apply · negotiate |

---

## PHASE 1 — Weeks 1–10

| Wk | Theme | LeetCode (Python) | SQL / DE | AI / reading |
|----|--------|-------------------|----------|--------------|
| **1** | Big O, hash maps | 217, 1, 242 | SQL50: 1–4 · Spark arch notes | DDIA Ch3 start · vector DB article |
| **2** | Arrays, two pointers | 88, 121, 125, 167 | SQL50: 5–8 · **Zoomcamp Spark** lab | Embeddings 101 |
| **3** | Sliding window | 3, 219, 643 | SQL50: 9–12 · joins/shuffle · dbt incremental | DDIA Ch3 done |
| **4** | Strings | 49, 242, (347 optional) | SQL50: 13–16 · BQ slots/cost | RAG overview |
| **5** | Stacks | 20, 155, 739 | SQL50: 17–20 · **+2 StrataScratch Medium** | — |
| **6** | Binary search | 704, 35, 74 | SQL50: 21–25 · Catalyst (high level) | DDIA Ch 1–2 |
| **7** | Linked lists | 206, 21, 141 | **Finish SQL 50** · BQ ARRAY | cache/persist |
| **8** | Trees intro | 104, 111, 226 | **StrataScratch** 2/wk · dbt tests · Cloud Run | Chunking |
| **9** | Consolidation | Re-solve 10 hardest | 3 STAR stories | Vector indexes |
| **10** | Phase 1 exam | 5 timed Easy | Pipeline whiteboard (Endeavour) | RAG failure modes |

**Week 1 daily tasks:** [plan_week1.md](./plan_week1.md)

**Phase 1 exit:** 35+ LC logged · SQL 50 done · StrataScratch ≥8 · explain BQ partition/cluster + dbt incremental · PySpark lazy vs action · Zoomcamp Spark module done

---

## PHASE 2 — Weeks 11–20

| Wk | Theme | LeetCode | DE / streaming | AI |
|----|--------|----------|----------------|-----|
| **11** | Kafka / Pub/Sub | 238, 153 | Confluent course + diagram | — |
| **12** | Stream processing | 56, 57 | Event time, windows · DDIA Ch 11 | — |
| **13** | DDIA replication | 102, 98 | DDIA Ch 5–6 | — |
| **14** | Watermarks | 200, 323 | Late data notes | **RAG MVP** → [rag_side_project.md](../projects/rag_side_project.md) |
| **15** | Composer scale | 235, 701 | DAG optimization story | — |
| **16** | Spark tuning | 5× Medium timed | **Databricks perf playlist** + AQE · Zoomcamp revisit | — |
| **17** | Batch system design | — | E-commerce metrics lake doc | Enterprise RAG diagram |
| **18** | Streaming design | — | Fraud / logs design doc | — |
| **19** | CDC / lakehouse | 15 LC review | CDC reading · RAG polish | GCP prod story |
| **20** | Phase 2 exam | — | 2 designs in `system_design/` | 1 AI pipeline pitch |

**Phase 2 exit:** 60+ LC · 15-min streaming whiteboard · 2 design markdown files · public RAG repo

---

## PHASE 3 — Weeks 21–30

| Wk | Focus |
|----|--------|
| **21** | Resume v2 (XYZ) · light networking · **start applications** (Razorpay, Walmart GTC first) |
| **22** | 8 STAR stories · [endeavour_gemini_story.md](../behavioral/endeavour_gemini_story.md) |
| **23** | 2 coding mocks (Pramp) |
| **24** | 2 DE system design mocks |
| **25** | 15 tailored applications |
| **26** | Research [profile.md](./profile.md) companies (3 bullets each) |
| **27–28** | Live interviews (first 2 = practice) |
| **29** | Gap sprint from feedback |
| **30** | Negotiate (levels.fyi India) — don’t wait if offer early |

---

## Personalized assets

| Asset | File |
|-------|------|
| Companies, notice, location | [profile.md](./profile.md) |
| Endeavour Gemini STAR | [endeavour_gemini_story.md](../behavioral/endeavour_gemini_story.md) |
| Pipeline whiteboard | [pipeline_whiteboard_template.md](../behavioral/pipeline_whiteboard_template.md) |
| RAG side project | [rag_side_project.md](../projects/rag_side_project.md) |

**Fill Endeavour/Lowe’s pipeline bullets** → unlock Walmart, Google, Fivetran interviews.

---

## Where details live (file split)

| Topic | File |
|-------|------|
| Repo hub, quick links | [README.md](../../README.md) |
| All URLs, source ratings, SQL/Spark how-to | [RESOURCES.md](./RESOURCES.md) |
| Weekly rhythm, when to apply | [HOW_TO_USE.md](./HOW_TO_USE.md) |
| Checkboxes, interview pipeline | [learn_tracker.md](./learn_tracker.md) |
| This file | Week themes + LC IDs only |
