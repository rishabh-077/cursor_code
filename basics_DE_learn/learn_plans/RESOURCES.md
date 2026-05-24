# Learning resources — curated for your prep

**How this fits:** [learn_plan_v2.md](./learn_plan_v2.md) says *what week* to study each topic. This file says *where* and *how good* each source is.

---

## Your suggested sources — verdict

| Resource | Rating | Add to plan? | When |
|----------|--------|--------------|------|
| **LeetCode SQL 50** | ⭐⭐⭐⭐⭐ | ✅ Already primary | Weeks 1–7 (finish all 50) |
| **StrataScratch (SQL, Medium)** | ⭐⭐⭐⭐ | ✅ **Added** | Weeks 5–8, 2 problems/week after SQL 50 basics |
| **DataTalksClub DE Zoomcamp — Spark** | ⭐⭐⭐⭐⭐ | ✅ **Added** | Weeks 2–4 hands-on; revisit Week 16 |
| **Databricks Spark Performance Tuning (YouTube)** | ⭐⭐⭐⭐⭐ | ✅ **Added** | Weeks 16–17 (shuffle, memory, AQE) |

**Bottom line:** Your picks are strong and complementary. Nothing to replace — SQL 50 + Zoomcamp labs + performance playlist is a solid DE stack. Keep NeetCode for DSA (separate skill).

---

## SQL

| Resource | URL | Best for | Weeks |
|----------|-----|----------|-------|
| **LeetCode SQL 50** | https://leetcode.com/studyplan/top-sql-50/ | Structured path: joins → windows → analytics | **1–7** (primary) |
| **StrataScratch** | https://platform.stratascratch.com/ | Company-style questions (Amazon, Netflix, etc.) | **5–8** (2/week, Medium) |
| **DataLemur** | https://datalemur.com/questions | DE interview SQL, explanations | **5+** (optional) |
| **Mode SQL Tutorial** | https://mode.com/sql-tutorial/ | Window functions theory | **4** |
| HackerRank SQL | https://www.hackerrank.com/domains/sql | Extra drills if bored | Optional |

**How to learn SQL here:**  
1. SQL 50 in order — don’t skip window function week.  
2. After problem ~12, add StrataScratch Medium (realistic phrasing).  
3. Write each solution in `basics_DE_learn/sql/` with 1-line “approach” comment.

---

## PySpark & Dataproc

| Resource | URL | Best for | Weeks |
|----------|-----|----------|-------|
| **DE Zoomcamp — Spark module** | https://github.com/DataTalksClub/data-engineering-zoomcamp | Free labs: DataFrames, joins, running Spark | **2–4**, **16** |
| **Databricks Spark Performance Tuning** | https://www.youtube.com/results?search_query=databricks+spark+performance+tuning | Shuffle, skew, memory, AQE visuals | **16–17** |
| Spark by Examples | https://sparkbyexamples.com/ | Copy-paste snippets, quick reference | Any PySpark block |
| Official PySpark API | https://spark.apache.org/docs/latest/api/python/ | Lookup | Reference |
| Databricks Academy (free) | https://www.databricks.com/learn/training/home | Structured courses | **16** (1 module) |
| Spark SQL performance docs | https://spark.apache.org/docs/latest/sql-performance-tuning.html | AQE, broadcast join | **16** |
| *Learning Spark* (O’Reilly) | Book | Deep read if you have time | Phase 2 |

**How to learn PySpark here:**  
1. Week 2–4: follow Zoomcamp Spark homework in `basics_DE_learn/pyspark/`.  
2. Week 16: watch performance playlist + tie to Dataproc jobs you know.  
3. Always say aloud: transformation (lazy) vs action (eager).

---

## DSA & Python

| Resource | URL | Weeks |
|----------|-----|-------|
| NeetCode 150 | https://neetcode.io/practice | **1–20** (follow order) |
| NeetCode YouTube | https://www.youtube.com/@neetcode | Before each new pattern |
| LeetCode Top Interview 150 | https://leetcode.com/studyplan/top-interview-150/ | Phase 2–3 review |
| Corey Schafer OOP | https://www.youtube.com/playlist?list=PL-osiE80TeTsqIkl9taNte_P9D5gAEsOB | **1–2** |
| [big_O_notation.md](../leetcode/big_O_notation.md) | Local | **1** |

---

## GCP / your stack

| Topic | URL |
|-------|-----|
| BigQuery best practices | https://cloud.google.com/bigquery/docs/best-practices-performance |
| BQ partitioning / clustering | https://cloud.google.com/bigquery/docs/partitioned-tables |
| Composer | https://cloud.google.com/composer/docs |
| dbt + BigQuery | https://docs.getdbt.com/docs/core/connect-data-platform/bigquery-setup |
| Cloud Run | https://cloud.google.com/run/docs |
| Vertex AI | https://cloud.google.com/vertex-ai/docs |

---

## Streaming (interview gap)

| Resource | URL | Weeks |
|----------|-----|-------|
| Confluent Kafka fundamentals (free) | https://developer.confluent.io/courses/ | **11** |
| GCP Pub/Sub | https://cloud.google.com/pubsub/docs | **11** |
| Dataflow / Beam model | https://cloud.google.com/dataflow/docs/concepts/beam-programming-model | **12** |
| DDIA Ch 11 | Book | **12** |
| *Streaming Systems* (Akidau) | O’Reilly | **12–14** (optional) |

---

## DDIA

| Option | Notes |
|--------|--------|
| **Physical book** (arriving soon) | Primary — 30–45 min/day |
| O’Reilly Learning | Legal ebook trial |
| Read order | Ch 1–3 (W1–4) → 5–6 (W13) → 11 (W12) |

---

## AI / GenAI for DE

| Resource | Topic | Weeks |
|----------|-------|-------|
| Endeavour Vertex/Gemini (your work) | Production LLM integration | Resume now |
| [rag_side_project.md](../projects/rag_side_project.md) | RAG pipeline | **14**, **19** |
| Chip Huyen — *AI Engineering* | ML systems | **4+** |
| Pinecone learn | Vectors, RAG | **1**, **9** |
| Vertex AI embeddings docs | GCP-native RAG | **14**, **19** |

---

## System design & behavioral

| Resource | Use |
|----------|-----|
| [DataEngineering.wiki](https://dataengineering.wiki/) | DE system design |
| [profile.md](./profile.md) | Company-specific prep |
| [pipeline_whiteboard_template.md](../behavioral/pipeline_whiteboard_template.md) | Lowe’s / Endeavour |
| [endeavour_gemini_story.md](../behavioral/endeavour_gemini_story.md) | STAR — AI project |
| Pramp / Exponent | Mocks **23–24** |

---

## Resource stack by phase (one glance)

| Phase | SQL | PySpark | DSA |
|-------|-----|---------|-----|
| **1 (W1–10)** | SQL 50 → StrataScratch | Zoomcamp Spark labs | NeetCode Easy → Easy-Medium |
| **2 (W11–20)** | DataLemur refresh | Performance tuning videos + Academy | NeetCode Medium |
| **3 (W21–30)** | Review missed SQL 50 | Explain optimizations in mocks | Timed mediums + Pramp |
