# DE, system design, data modeling & AI theory — curriculum map

**Purpose:** One table for **what to study when**, and **which resource** (free video, book chapter, lab).  
**Does not replace:** [MASTER_PLAN.md](MASTER_PLAN.md) (rules) · [weekly_plans/week_NN.md](weekly_plans/) (daily tasks) · [learn_plans/RESOURCES.md](learn_plans/RESOURCES.md) (all URLs).

**Agents:** update this file when calendar weeks or book mapping changes; bump [CONTEXT.md](CONTEXT.md) §10.

---

## How the three layers fit

| Layer | File | Answers |
|-------|------|---------|
| **Rules** | [MASTER_PLAN.md](MASTER_PLAN.md) | Phases, “DSA only in Phase 1”, mastery gates |
| **This file** | `DE_CURRICULUM.md` | Week ↔ DE topic ↔ DDIA / Chip / video ↔ practice |
| **Links** | [learn_plans/RESOURCES.md](learn_plans/RESOURCES.md) | Exact YouTube & doc URLs |
| **Daily** | Portal + `weekly_plans/` | What you do **today** |

**Study order:** Video (intuition) → book chapter or docs (depth) → practice (SQL / lab / notes in repo).

---

## How to read this (so it does not feel like “6 subjects per day”)

**Your instinct is correct:** if you tried to do every cell in the Phase 1 table on one evening, that would **break** [MASTER_PLAN.md](MASTER_PLAN.md) rules 1–2.

| What the big table is | What it is **not** |
|----------------------|---------------------|
| A **week-level menu** — topics you may touch sometime this week | A **daily** portal plan |
| A **reference** for agents generating `weekly_plans/week_0N.md` | “Do DSA + SQL + Zoomcamp + Chip + 2 videos tonight” |

**MASTER_PLAN always wins for each day.** DE_CURRICULUM only answers: *“If I have extra time this week, what DE/theory bucket am I in?”*

### Phase 1 — what you actually do (weeks 1–8)

| Day | Real daily load (2–3 h total) |
|-----|-------------------------------|
| **Mon, Wed, Fri, Sat** | **DSA only** (~2–2.5 h) — one LC focus from [DSA_PACING](learn_plans/DSA_PACING.md) |
| **Tue, Thu** | DSA (~2 h) **+** SQL 50 (**30 min** secondary) |
| **Sun** | ~15 min reflection (portal) |
| **DE / Chip / DDIA / Zoomcamp** | **Not** a third equal block Mon–Fri. Optional: **Sat afternoon** or **skip until week 9+** if DSA is behind |

Example — **calendar week 2** row lists: t02/t03, SQL #5–8, Zoomcamp, Chip (finish 1–2 then 3–4), Vector DB, RAG intro.

That does **not** mean Tuesday = arrays + SQL + Zoomcamp + Chip + RAG. It means:

- **Tue/Thu:** DSA + one SQL problem (see [weekly_plans/week_02.md](weekly_plans/week_02.md)).
- **Rest of week:** DSA only on portal.
- **Optional (0–1 h total on Sat or a light evening):** e.g. 20 min Chip **or** one short video **or** one Zoomcamp page — pick **one**, not all.

### Phase 1 — weeks 9–16 (slightly more DE)

MASTER_PLAN: **1.5 h DSA *or* 45 min SQL/DE** — still **one** main focus per day, not both full blocks.

### Phase 2+ (week 17+)

Then the table matches daily life: **Mon/Wed/Fri = one DE topic**, **Tue/Thu = DSA**, **Sat = SQL or system design reading**. Two subjects per week, on **different days** — that is intentional.

**Rule of thumb:** Open **portal / `weekly_plans/`** every day. Open **DE_CURRICULUM** when planning the week or choosing one optional Saturday task.

---

## Portal vs DE_CURRICULUM — what you must do vs what can wait

| Source | Meaning | If you skip it |
|--------|---------|----------------|
| **Portal PRIMARY** | Required this week (DSA) | Week plan / mastery slips — fix next week |
| **Portal SECONDARY** | Required on that day only (SQL Tue/Thu, or optional Sat DE) | SQL count lags; add to reflection |
| **DE_CURRICULUM row** | **Menu for the calendar week** — not auto-added to portal | Stays on **parallel backlog** until you do it or explicitly defer |
| **learn_tracker Phase 1 exit** | Real gates (SQL 50, Zoomcamp, Spark lazy, Chip notes…) | Checked by **week 16**, not “must finish in week 2” |

**How you know today:** If it is in **portal** (primary/secondary for that date) → do it. If it is only in **DE_CURRICULUM** → optional unless you put it in portal yourself or Sunday reflection says “carry Chip.”

**Week 2 example:** Portal = LC + SQL #5–7. Sat optional = **Chip Ch 1–2 catch-up** (not Ch 3–4 if 1–2 unread). Zoomcamp is separate optional. Calendar “week 2 = Ch 3–4” in the table below means **target if caught up**, not “skip Ch 1–2”.

### If Chip / Zoomcamp are never done in week 2

Nothing breaks for **daily** prep. They roll forward:

1. **Backlog** — still listed on Phase 1 exit in `learn_tracker.md` (e.g. Zoomcamp, PySpark lazy, Chip Ch 1–4).
2. **Sunday reflection** — write under *Blocked*: “Chip Ch 3–4 not started” or *Next week*: “Sat optional: 30 min Chip OR Zoomcamp module 1.”
3. **Week 3 generation** (you + Cursor) — reads reflection + backlog + DE_CURRICULUM week 3 row; may add **one** optional secondary on Sat or week 9+ DE slot per MASTER_PLAN.
4. **Hard deadline** — Phase 1 **exit ~week 16** (SQL 50, Zoomcamp, theory started). Calendar week 2 is a **suggested** window, not a pass/fail for that week alone.

**DSA vs DE priority:** If t02 mastery is not met, Week 3 portal stays DSA-heavy; Chip/Zoomcamp stay on backlog — **by design**.

---

## Theory books (spine)

| Book | When | Role |
|------|------|------|
| **Chip Huyen — *AI Engineering*** (O’Reilly) | **Weeks 1–2+** (primary until DDIA arrives) | LLM systems, RAG, eval, production — parallel to DSA |
| **Martin Kleppmann — *DDIA*** | **From ~week 3** (`ddiaArrives`: 2026-06-08) | Storage, replication, streaming, distributed framing |
| **Online only** | All phases | Spark, BQ, Kafka, NeetCode — see RESOURCES |

**Notes:** [theory/ai_engineering_notes.md](theory/ai_engineering_notes.md) · Schedule: [learn_plans/theory_reading.md](learn_plans/theory_reading.md)

**Chip reading rule:** Chapters are **sequential**. Optional portal Sat task = **next unchecked chapter** in `ai_engineering_notes.md`, not the calendar-week number alone.

---

## Phase 1 parallel track (weeks 1–16) — while DSA is primary

**Daily (portal):** DSA ~2–2.5 h · SQL **Tue/Thu only** (weeks 1–7).  
**DE / theory below:** parallel or on Sat — **not** a third equal block on the same night unless you have extra time.

### Calendar map — **week menu** (not daily stack)

*Columns = “touch this week if you have time,” except SQL which is only Tue/Thu per MASTER_PLAN.*

| Cal wk | Dates (2026) | DSA focus ([DSA_PACING](learn_plans/DSA_PACING.md)) | SQL 50 (Tue/Thu only) | Optional DE (Sat / spare) | Optional theory (Sat / spare) | Optional video (pick one) |
|--------|----------------|-----------------------------------------------------|------------------|--------------------------|----------------------|----------------------------|
| **1** | 25 May – 31 May | t01 Big-O · start t02 | #1–4 | Spark driver/executor · [pyspark/week1_notes.md](pyspark/week1_notes.md) | **Chip Ch 1–2** | [Spark architecture](learn_plans/RESOURCES.md#pyspark--dataproc) · [BQ intro](learn_plans/RESOURCES.md#gcp-your-stack) |
| **2** | 1 – 7 Jun | t02 Arrays · start t03 | #5–8 | Zoomcamp start · lazy vs action notes | **Chip: finish Ch 1–2, then 3–4** | Vector DB · RAG intro (light) |
| **3** | 8 – 14 Jun | t03 Strings | #9–12 | Zoomcamp cont. · dbt intro (light) | **DDIA Ch 3** (storage) | Kleppmann streams talk |
| **4** | 15 – 21 Jun | t04 Hash | #13–16 | BQ partitioning mindset | DDIA Ch 3 review · RAG read | GCP RAG doc |
| **5** | 22 – 28 Jun | t05 Two pointers | #17–20 | StrataScratch start | Chip / DDIA Ch 5–6 skim | Mode SQL windows |
| **6** | 29 Jun – 5 Jul | t06 Sliding window | #21–25 | — | DDIA replication/partition | — |
| **7** | 6 – 12 Jul | t07 Prefix sums | **Finish SQL 50** | — | — | — |
| **8** | 13 – 19 Jul | t08 Stacks | — | StrataScratch | Chunking (LangChain) | LangChain chunking video |
| **9** | 20 – 26 Jul | t09 Queues · t10 LL start | — | STAR draft | Review Chip notes | — |
| **10** | 27 Jul – 2 Aug | t10 Linked lists | — | [pipeline whiteboard](behavioral/pipeline_whiteboard_template.md) | — | — |
| **11** | 3 – 9 Aug | t11 Recursion | — | Mock LC easy | **DDIA Ch 11** (streams intro) | Streaming 101 (Google) |
| **12** | 10 – 16 Aug | t12 Trees | — | — | DDIA Ch 11 cont. | — |
| **13** | 17 – 23 Aug | t13 BST | — | — | — | — |
| **14** | 24 – 30 Aug | t14 Graphs BFS | — | — | — | — |
| **15** | 31 Aug – 6 Sep | t15 DFS | — | — | — | — |
| **16** | 7 – 13 Sep | t16 Topo · Phase 1 review | — | Zoomcamp finish · Phase 1 DE recap | Phase 1 theory recap | Spark tuning preview |

**SQL logs:** [sql/week1_sql50_log.md](sql/week1_sql50_log.md) · [sql/week2_sql50_log.md](sql/week2_sql50_log.md) (extend per week as needed).

**Phase 1 DE exit (not DSA):** SQL 50 done · Zoomcamp lab · Spark/BQ explained aloud · Chip Ch 1–4 notes · DDIA Ch 3 started.

---

## Data modeling (where it appears)

| When | Resource | Practice |
|------|----------|----------|
| Weeks 1–7 | SQL 50 + [freeCodeCamp SQL](https://www.youtube.com/watch?v=HXV3zeQKqGY) (joins) | Normalization via SQL problems |
| Weeks 4–5 | [Mode SQL tutorial](https://mode.com/sql-tutorial/) | Windows, aggregates |
| Weeks 5–8 | [StrataScratch](https://platform.stratascratch.com/) | Interview-style schemas |
| **Week 19 (Phase 2)** | dbt + dimensional modeling | [dbt + BQ video](learn_plans/RESOURCES.md) · star/snowflake in design docs |
| Ongoing | DDIA Ch 3 (storage models) | Notes in theory folder |
| Interviews | [DataLemur](https://datalemur.com/questions) | Week 5+ in RESOURCES |

**Repo:** No separate `data_modeling/` folder yet — add notes under `theory/` or `system_design/` when you start week 19.

---

## AI / GenAI for DE (Chip + videos + your work)

| Week | Topic | Chip Huyen (*AI Engineering*) | Video / doc | Repo artifact |
|------|--------|----------------------------------|-------------|----------------|
| 1 | Foundations | Ch 1–2 | Vector DB explainer | [ai_engineering_notes.md](theory/ai_engineering_notes.md) |
| 2 | Pipelines / data for ML | **Ch 1–2 if open, else 3–4** | RAG intro (IBM/Google) | Endeavour link in notes |
| 4 | RAG concepts | RAG / embedding chapters | GCP RAG overview | — |
| 8 | Chunking for RAG | Production text ch. | LangChain chunking | — |
| 14 | Vertex / Gemini | Deployment / monitoring ch. | Vertex AI videos | [endeavour_gemini_story.md](behavioral/endeavour_gemini_story.md) |
| 21–22 | **RAG MVP** | Full book tie-in | — | [rag_side_project.md](projects/rag_side_project.md) |

**Rule:** Connect every chapter to **3 bullets** in `ai_engineering_notes.md` (term · Endeavour link · interview line).

---

## Phase 2 — DE depth (calendar weeks 17–24)

**Daily shape ([MASTER_PLAN](MASTER_PLAN.md)):** Mon/Wed/Fri = DE 2–2.5 h · Tue/Thu = DSA t17–t23 · Sat = SQL/DataLemur or **system design reading**.

| Cal wk | DE / systems focus | DSA (maintenance) | Theory & books | System design output |
|--------|-------------------|-------------------|----------------|---------------------|
| **17** | **Spark internals** + shuffle, stages | t17 Union-find | DDIA Ch 5–6 · Kafka | Whiteboard: batch ETL |
| **18** | **Kafka / GCP Pub/Sub** | t18 Binary search | DDIA Ch 11 | Event-time diagram |
| **19** | **Data modeling** + **dbt** on BQ | t19 Heaps | dbt docs | Dimensional model doc |
| **20** | **CDC / reliability** | t20 Greedy | DDIA reliability themes | Idempotent pipeline design |
| **21** | **Batch pipeline design** | t21 DP (wk 1) | — | Doc: batch architecture |
| **22** | **Streaming design** + late data | t21 DP (wk 2) | DDIA Ch 11 | Doc: streaming architecture |
| **23** | **RAG project build** | t22 Backtracking | Chip production chapters | [rag_side_project.md](projects/rag_side_project.md) public |
| **24** | **GCP architecture** + cost | t23 Tries | BQ/Composer/Cloud Run | Batch + streaming design finals |

**Videos/labs:** [RESOURCES.md — PySpark](learn_plans/RESOURCES.md#pyspark--dataproc) · [Streaming](learn_plans/RESOURCES.md#streaming) · [GCP](learn_plans/RESOURCES.md#gcp-your-stack) · [AI/GenAI](learn_plans/RESOURCES.md#ai--genai-for-de).

**Phase 2 exit:** 60+ LC · explain Spark shuffle + BQ partitioning · 2 design docs · public RAG repo.

---

## System design (when & what)

| Phase | Weeks | Activity | Resources |
|-------|-------|----------|-----------|
| **1 (light)** | 10 | Pipeline whiteboard template | [pipeline_whiteboard_template.md](behavioral/pipeline_whiteboard_template.md) |
| **2 (build)** | 17–24 | Write 2–4 design docs (batch, streaming, CDC, RAG) | [dataengineering.wiki](https://dataengineering.wiki/) · [DE design tips video](https://www.youtube.com/watch?v=I1lq9UG-h9c) |
| **3 (mocks)** | 25–30 | Tue/Thu system design mocks | [Pramp](https://www.pramp.com/) · [Exponent](https://www.tryexponent.com/) · Exponent DE SD search in RESOURCES |

**Not in Phase 1 daily portal** until Phase 3 — only light prep above.

---

## Phase 3 — interviews (weeks 25–30)

| Day (MASTER_PLAN) | Focus | Resources |
|-------------------|--------|-----------|
| Mon / Wed | Timed LC Medium | NeetCode · LC Top Interview 150 |
| Tue / Thu | **System design mock** | Exponent · Pramp · your design docs |
| Fri | STAR / behavioral | [endeavour_gemini_story.md](behavioral/endeavour_gemini_story.md) + STAR files |
| Sat | Apply + follow-up | Company list in [profile.md](learn_plans/profile.md) |

---

## DDIA chapter quick reference

| Chapter | Topic | Best calendar weeks |
|---------|--------|---------------------|
| Ch 1–2 | Reliable, scalable, maintainable apps | 17 (skim) |
| **Ch 3** | **Storage & retrieval** | **3–4** (start) |
| Ch 4 | Encoding (skim as needed) | 4 |
| Ch 5–6 | Replication, partitioning | 5–6, 17 |
| Ch 7–10 | Distributed data (skim) | 17–18 |
| **Ch 11** | **Stream processing** | **11–12, 18, 22** |
| Ch 12 | Future of data systems (optional) | 24+ |

---

## What to add to portal weekly plans

When generating `weekly_plans/week_0N.md` + `week_plans/N.json`:

1. Pull **DSA** row from [DSA_PACING.md](learn_plans/DSA_PACING.md).  
2. Pull **DE/theory/SQL** row from **this file** for calendar week N.  
3. Phase 1: only **PRIMARY** = DSA; put SQL on Tue/Thu **SECONDARY**; DE/theory as optional “Sat parallel” line or secondary if 30 min.  
4. Phase 2: DE becomes PRIMARY on Mon/Wed/Fri per table above.

---

## Related files (index)

| Topic | Path |
|-------|------|
| All video URLs | [learn_plans/RESOURCES.md](learn_plans/RESOURCES.md) |
| DSA week map | [learn_plans/DSA_PACING.md](learn_plans/DSA_PACING.md) |
| Theory schedule | [learn_plans/theory_reading.md](learn_plans/theory_reading.md) |
| Chip notes | [theory/ai_engineering_notes.md](theory/ai_engineering_notes.md) |
| PySpark | [pyspark/week1_notes.md](pyspark/week1_notes.md) |
| SQL logs | [sql/](sql/) |
| Archived 30-wk calendar | [learn_plans/_archive/learn_plan_v2.md](learn_plans/_archive/learn_plan_v2.md) |

*Last curriculum update: 2026-06-08*
