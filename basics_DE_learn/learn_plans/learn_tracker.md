# Interview prep tracker

**Start date:** 2026-05-24 · **Target apply window:** Week 21+ · **Master plan:** [learn_plan_v2.md](./learn_plan_v2.md)

---

## Profile snapshot

**Full profile:** [profile.md](./profile.md)

| Field | Value |
|-------|--------|
| Total IT experience | 6.1 years |
| DE experience | 3.5 years |
| Current employer | Tiger Analytics |
| Previous | Accenture |
| Tiger clients | **Lowe’s**, **Endeavour Group** |
| Current CTC | ~25 LPA (India) |
| Target CTC (realistic) | 35–42 LPA → stretch 42–50 LPA |
| Notice period | **2 months** |
| Location | Remote preferred · Hyderabad · Bangalore · Pune · Mumbai |
| Target companies | Google, Walmart GTC, Databricks, Snowflake, Fivetran, Razorpay, JPM, Chase |
| Risk appetite | Startups OK if growth is strong |
| Primary cloud | GCP |
| Tools | BigQuery, Composer, Dataproc, dbt, Git, Docker, ADO, Cloud Run |
| AI — prod | Endeavour: Vertex AI / Gemini match validation pipeline |
| AI — side project | RAG pipeline (Week 14) → [rag_side_project.md](../projects/rag_side_project.md) |
| Python / DSA | Can read code; solving from scratch: **beginner** |
| Streaming | Conceptual only — **priority gap** |
| Daily study time | 3–4 hours |
| DDIA book | Ordered; arrives in 3–4 days |

---

## Overall progress

| Phase | Weeks | Status | Target end |
|-------|-------|--------|------------|
| 1 — Foundations | 1–10 | ⬜ Not started / 🟡 In progress / ✅ Done | __________ |
| 2 — Systems + streaming + AI | 11–20 | ⬜ / 🟡 / ✅ | __________ |
| 3 — Interviews & offers | 21–30 | ⬜ / 🟡 / ✅ | __________ |

**Current week:** Week ___ · **Daily plan file:** [plan_week1.md](./plan_week1.md)

---

## Weekly tracker (tick when week exit criteria met)

### Phase 1 — Foundations (Weeks 1–10)

| Wk | Theme | DSA (problems) | SQL | PySpark / GCP | AI / DDIA | Done |
|----|-------|----------------|-----|---------------|-------------|------|
| 1 | Big O, hash maps | 217, 1, 242 | SQL50: 1–4 | Spark arch notes | DDIA Ch3 start, vector DB article | ⬜ |
| 2 | Arrays, two pointers | 88, 121, 125, 167 | SQL50: 5–8 | Zoomcamp Spark lab | Embeddings 101 | ⬜ |
| 3 | Sliding window | 3, 219, 643 | SQL50: 9–12 | Joins + shuffle | DDIA Ch3 done | ⬜ |
| 4 | Strings | 49, 242 review | SQL50: 13–16 | — | RAG overview | ⬜ |
| 5 | Stacks | 20, 155, 739 | SQL50: 17–20 + 2× StrataScratch Medium | groupBy/window | — | ⬜ |
| 6 | Binary search | 704, 35, 74 | SQL50: 21–25 | Catalyst notes | DDIA Ch 1–2 | ⬜ |
| 7 | Linked lists | 206, 21, 141 | **SQL50 complete** | cache/persist | — | ⬜ |
| 8 | Trees intro | 104, 111, 226 | 2× StrataScratch/wk | dbt tests, Cloud Run | Chunking | ⬜ |
| 9 | Consolidation | Re-solve 10 hardest | — | — | Vector indexes | ⬜ |
| 10 | Phase 1 exam | 5 timed Easy | — | Batch pipeline whiteboard | RAG failure modes | ⬜ |

**Phase 1 exit (Week 10):**
- [ ] 35+ LeetCode problems in repo with complexity notes
- [ ] LeetCode SQL 50 **finished**
- [ ] Explain BQ partition vs cluster + dbt incremental (5 min aloud)
- [ ] PySpark: transformation vs action + one join example

---

### Phase 2 — Systems, streaming, AI (Weeks 11–20)

| Wk | Theme | DSA | DE / streaming | AI | Done |
|----|-------|-----|----------------|-----|------|
| 11 | Kafka / Pub/Sub | 238, 153 | Confluent course + diagram | — | ⬜ |
| 12 | Stream processing | 56, 57 | Event time, windows | — | ⬜ |
| 13 | DDIA replication | 102, 98 | DDIA Ch 5–6 | — | ⬜ |
| 14 | Watermarks | 200, 323 | Late data notes | Mini RAG script | ⬜ |
| 15 | Composer scale | 235, 701 | DAG optimization story | — | ⬜ |
| 16 | Spark tuning | 5 timed Medium | Databricks perf playlist + AQE | — | ⬜ |
| 17 | Batch system design | — | E-commerce metrics design doc | Enterprise RAG diagram | ⬜ |
| 18 | Streaming design | — | Fraud / logs design doc | — | ⬜ |
| 19 | CDC / lakehouse | 15 LC review | CDC reading | — | ⬜ |
| 20 | Phase 2 exam | — | 2 designs in `system_design/` | 1 AI pipeline pitch | ⬜ |

**Phase 2 exit (Week 20):**
- [ ] 60+ total LC logged
- [ ] 15-min streaming whiteboard without notes
- [ ] 2 system design markdown files written

---

### Phase 3 — Interview machine (Weeks 21–30)

| Wk | Focus | Key deliverable | Done |
|----|--------|-----------------|------|
| 21 | Resume v2 | PDF with XYZ metrics | ⬜ |
| 22 | Behavioral | 8 STAR stories in `behavioral/` | ⬜ |
| 23 | Coding mocks | 2 mocks completed | ⬜ |
| 24 | DE mocks | 2 system design mocks | ⬜ |
| 25 | Applications | 15 companies applied | ⬜ |
| 26 | Company research | 5 tailored profiles | ⬜ |
| 27–28 | Live interviews | Feedback log updated | ⬜ |
| 29 | Gap drill | Weak-area sprint | ⬜ |
| 30 | Negotiation | Offer comparison sheet | ⬜ |

---

## Daily habit checklist (every study day)

- [ ] Block A — 90 min DSA (NeetCode + LeetCode)
- [ ] Block B — 90 min DE (SQL / PySpark / BQ rotation)
- [ ] Block C — 30–45 min DDIA / streaming / AI
- [ ] Updated this tracker or week plan notes
- [ ] Saved code to repo (`leetcode_*.py`, etc.)

---

## LeetCode log (add rows as you solve)

| # | Problem | Pattern | Solved | Without hints | Complexity written |
|---|---------|---------|--------|---------------|-------------------|
| 217 | Contains Duplicate | Hash set | ⬜ | ⬜ | ⬜ |
| 1 | Two Sum | Hash map | ⬜ | ⬜ | ⬜ |
| 242 | Valid Anagram | Hash / sort | ⬜ | ⬜ | ⬜ |
| | | | | | |

---

## SQL 50 progress

| # | Problem name | Done | Notes |
|---|--------------|------|-------|
| 1 | | ⬜ | |
| 2 | | ⬜ | |
| … | | | |

*Full list: https://leetcode.com/studyplan/top-sql-50/*

---

## PySpark practice log

| Week | Exercise | Done | Link / file |
|------|----------|------|-------------|
| 1 | Driver vs Executor + lazy vs action notes | ⬜ | notes |
| 2 | Read CSV → filter → groupBy | ⬜ | `pyspark/week2.py` |
| 3 | Join two DataFrames | ⬜ | |
| 5 | Window function | ⬜ | |

---

## STAR stories (fill for behavioral)

| # | Story | Company | Metric in result |
|---|--------|---------|------------------|
| 1 | **Vertex AI / Gemini match validation** | Endeavour | See [endeavour_gemini_story.md](../behavioral/endeavour_gemini_story.md) |
| 2 | End-to-end pipeline whiteboard | Endeavour or Lowe’s | [pipeline_whiteboard_template.md](../behavioral/pipeline_whiteboard_template.md) |
| 3 | BQ cost optimization | Tiger | e.g. __% cost reduction |
| 4 | dbt incremental migration | Tiger | |
| 5 | Composer pipeline failure / fix | Tiger | |
| 6 | Large-scale batch pipeline | Lowe’s / Accenture | |
| 7 | Tight deadline delivery | Accenture | |
| 8 | Production incident | | |

---

## Interview pipeline (start Week 21+; 2-month notice)

| Company | Role | Applied | OA | Technical | Offer | CTC | Notes |
|---------|------|---------|-----|-----------|-------|-----|-------|
| Razorpay | DE | ⬜ | ⬜ | ⬜ | ⬜ | | Apply early — strong fit |
| Walmart Global Tech | DE | ⬜ | ⬜ | ⬜ | ⬜ | | Use Lowe’s retail story |
| Fivetran | DE | ⬜ | ⬜ | ⬜ | ⬜ | | EL/CDC angle |
| Databricks | DE | ⬜ | ⬜ | ⬜ | ⬜ | | Spark depth |
| Snowflake | DE | ⬜ | ⬜ | ⬜ | ⬜ | | SQL + warehousing |
| Google | DE / Cloud | ⬜ | ⬜ | ⬜ | ⬜ | | After mocks strong |
| JP Morgan | DE | ⬜ | ⬜ | ⬜ | ⬜ | | SQL + governance |
| Chase | DE | ⬜ | ⬜ | ⬜ | ⬜ | | |

---

## Weekly reflection (copy each Sunday)

**Week #:** ___

- What I finished:
- What blocked me:
- Adjust next week (more DSA / SQL / rest):
- Energy level (1–5):

---

## Milestones & compensation

| Milestone | Target week | Achieved |
|-----------|-------------|----------|
| First LC Easy without hints | Week 2–3 | ⬜ |
| SQL 50 complete | Week 7 | ⬜ |
| First system design doc | Week 17 | ⬜ |
| Resume sent to 15 companies | Week 25 | ⬜ |
| First offer | Week 27+ | ⬜ |
| Target band 35–42 LPA | Negotiation | ⬜ |
| Stretch 42–50 LPA | Negotiation | ⬜ |

---

## How to work with Cursor on this plan

1. **Every week:** Say *“Update plan_week2 from learn_tracker — I finished X, stuck on Y.”*  
2. **Monthly:** Review phase exit criteria; delay interviews if Phase 1 incomplete.  
3. **After real interviews:** Paste questions asked → get a gap sprint for Week 29-style drill.

**You do not need a new master plan each week** — only `plan_weekN.md` + tracker updates.
