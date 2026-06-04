# Learning resources (read + video)

**Rule:** Watch video for intuition → read docs/book for depth → practice (LeetCode / labs).

**Plan mapping:** [MASTER_PLAN.md](../MASTER_PLAN.md) · **Week tasks:** [weekly_plans/](../weekly_plans/)

---

## Week 1 quick links

| Topic | Video | Read |
|-------|-------|------|
| Big O | [NeetCode](https://www.youtube.com/watch?v=BgLTDT03QtU) | [big_O_notation.md](../leetcode/big_O_notation.md) |
| LC 217 / 1 / 242 / 88 / 121 | [NeetCode channel](https://www.youtube.com/@neetcode) | LeetCode links in [plan_week1](./weekly_plan/plan_week1.md) |
| SQL joins | [freeCodeCamp SQL](https://www.youtube.com/watch?v=HXV3zeQKqGY) (joins section) | [SQL 50](https://leetcode.com/studyplan/top-sql-50/) |
| Spark architecture | [How Spark works (Databricks)](https://www.youtube.com/watch?v=znBa13W5ocA) | [Cluster overview](https://spark.apache.org/docs/latest/cluster-overview.html) |
| BigQuery | [BQ architecture](https://www.youtube.com/watch?v=NCwbF1xllb4) | [BQ best practices](https://cloud.google.com/bigquery/docs/best-practices-performance) |
| Vector DB | [Explained (5 min)](https://www.youtube.com/watch?v=klTvEwg3oJ4) | [Pinecone guide](https://www.pinecone.io/learn/vector-database/) |
| RAG | [IBM RAG](https://www.youtube.com/watch?v=T-D1OfcDW1M) | [GCP RAG](https://cloud.google.com/use-cases/retrieval-augmented-generation) |
| Theory (until 8 Jun) | — | [Chip Huyen AI Engineering](theory_reading.md) |
| DDIA Ch 3 (from 8 Jun) | [Kleppmann streams talk](https://www.youtube.com/watch?v=AvsaGRE79r4) | DDIA book / O’Reilly |
| DSA full plan | — | [dsa-study-plan.html](./dsa-study-plan.html) |

---

## DSA & Python

| Topic | Video | Read / practice | Weeks |
|-------|-------|-----------------|-------|
| Patterns + LC | [NeetCode YouTube](https://www.youtube.com/@neetcode) | [NeetCode 150](https://neetcode.io/practice) | 1–20 |
| Big O | [NeetCode Big O](https://www.youtube.com/watch?v=BgLTDT03QtU) | [big_O_notation.md](../leetcode/big_O_notation.md) | 1 |
| Interview set | — | [LC Top Interview 150](https://leetcode.com/studyplan/top-interview-150/) | 15+ |
| Python OOP | [Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTsqIkl9taNte_P9D5gAEsOB) | `python/*.py` in repo | 1–2 |

---

## SQL

| Resource | Video | Read / practice | Weeks |
|----------|-------|-----------------|-------|
| **LeetCode SQL 50** | [freeCodeCamp SQL](https://www.youtube.com/watch?v=HXV3zeQKqGY) (reference) | [Study plan](https://leetcode.com/studyplan/top-sql-50/) | **1–7** |
| Window functions | [Mode windows](https://mode.com/sql-tutorial/sql-window-functions/) (interactive) | [Mode SQL](https://mode.com/sql-tutorial/) | 4–5 |
| StrataScratch | — | [platform.stratascratch.com](https://platform.stratascratch.com/) | 5–8 |
| DataLemur | [DataLemur channel](https://www.youtube.com/@DataLemur) | [Questions](https://datalemur.com/questions) | 5+ |

---

## PySpark & Dataproc

| Resource | Video | Read / practice | Weeks |
|----------|-------|-----------------|-------|
| **DE Zoomcamp** | [Zoomcamp playlist](https://www.youtube.com/playlist?list=PLbzoR-pLrL3qZZG5qYX9l04c4Lo4Np8s2) | [GitHub labs](https://github.com/DataTalksClub/data-engineering-zoomcamp) | **2–4**, 16 |
| Spark internals | [Databricks — How Spark works](https://www.youtube.com/watch?v=znBa13W5ocA) | [Cluster overview](https://spark.apache.org/docs/latest/cluster-overview.html) | 1–2 |
| Performance | [Spark performance tuning playlist](https://www.youtube.com/results?search_query=databricks+spark+performance+tuning) | [Spark SQL tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) | **16–17** |
| Snippets | — | [Spark by Examples](https://sparkbyexamples.com/) | Any |
| Courses | [Databricks Academy](https://www.databricks.com/learn/training/home) | — | 16 |

---

## GCP (your stack)

| Topic | Video | Read |
|-------|-------|------|
| BigQuery | [BQ architecture](https://www.youtube.com/watch?v=NCwbF1xllb4) · [Cost optimization](https://www.youtube.com/watch?v=8QUbjAEZ_gQ) | [Best practices](https://cloud.google.com/bigquery/docs/best-practices-performance) |
| Partition / cluster | [BQ partitioning](https://www.youtube.com/watch?v=jpH-zpE5w5g) | [Partitioned tables](https://cloud.google.com/bigquery/docs/partitioned-tables) |
| Composer / Airflow | [Cloud Composer intro](https://www.youtube.com/watch?v=5q2yftSqeBc) | [Composer docs](https://cloud.google.com/composer/docs) |
| dbt | [dbt + BigQuery (official)](https://www.youtube.com/watch?v=lSCXKvMRcTc) | [dbt BQ setup](https://docs.getdbt.com/docs/core/connect-data-platform/bigquery-setup) |
| Cloud Run | [Cloud Run intro](https://www.youtube.com/watch?v=EmxyjHDIEA8) | [Cloud Run docs](https://cloud.google.com/run/docs) |

---

## Streaming

| Topic | Video | Read | Weeks |
|-------|-------|------|-------|
| Kafka | [Confluent Kafka in 6 min](https://www.youtube.com/watch?v=aj9CDLmclko) · [Full course](https://developer.confluent.io/courses/) | Confluent docs | **11** |
| Pub/Sub | [GCP Pub/Sub](https://www.youtube.com/watch?v=cvu53CnZmGI) | [Pub/Sub docs](https://cloud.google.com/pubsub/docs) | 11 |
| Stream processing | [Beam / Dataflow model](https://www.youtube.com/watch?v=TC_C54EY5UI) | [Dataflow concepts](https://cloud.google.com/dataflow/docs/concepts/beam-programming-model) | 12 |
| Windows / watermarks | [Streaming 101 (Google)](https://www.youtube.com/watch?v=HrN2Z7v0HeU) | DDIA Ch 11 · *Streaming Systems* | 12–14 |

---

## DDIA

| Topic | Video | Read |
|-------|-------|------|
| Why distributed systems | [Kleppmann — stream processing](https://www.youtube.com/watch?v=AvsaGRE79r4) | DDIA Ch 1–3 |
| Replication / partition | [DDIA summaries on YouTube](https://www.youtube.com/results?search_query=designing+data+intensive+applications+chapter) | DDIA Ch 5–6 |
| Storage engines | — | DDIA Ch 3 (book primary) |

---

## AI / GenAI for DE

| Topic | Video | Read / build | Weeks |
|-------|-------|--------------|-------|
| **Your Endeavour work** | — | [endeavour_gemini_story.md](../behavioral/endeavour_gemini_story.md) | Now |
| Vector DB | [What is vector DB](https://www.youtube.com/watch?v=klTvEwg3oJ4) | [Pinecone learn](https://www.pinecone.io/learn/) | 1, 9 |
| Embeddings | [Word embeddings](https://www.youtube.com/watch?v=viZrOnJclY0) | [OpenAI embeddings](https://platform.openai.com/docs/guides/embeddings) | 2 |
| RAG | [IBM RAG](https://www.youtube.com/watch?v=T-D1OfcDW1M) · [Google](https://www.youtube.com/watch?v=qaW4l-uBAEE) | [GCP RAG](https://cloud.google.com/use-cases/retrieval-augmented-generation) | 1, 4 |
| LLM systems | [Chip Huyen talk](https://www.youtube.com/watch?v=9Km1-U0u1LQ) | *AI Engineering* (O’Reilly) | 4+ |
| Vertex AI / Gemini | [Vertex AI overview](https://www.youtube.com/watch?v=VvJk3GTeoW0) · [Gemini on Vertex](https://www.youtube.com/watch?v=3-bSc7m0Za0) | [Vertex AI docs](https://cloud.google.com/vertex-ai/docs) | 14, 19 |
| RAG side project | — | [rag_side_project.md](../projects/rag_side_project.md) | **14** |
| Chunking | [LangChain chunking](https://www.youtube.com/watch?v=8OJ7HKzLUX4) | LangChain docs | 8 |

---

## System design & mocks

| Topic | Video | Read |
|-------|-------|------|
| DE system design | [Exponent DE interview](https://www.youtube.com/results?search_query=exponent+data+engineer+system+design) | [dataengineering.wiki](https://dataengineering.wiki/) |
| Batch pipeline design | [DE design interview tips](https://www.youtube.com/watch?v=I1lq9UG-h9c) | Your `system_design/` notes |
| Mocks | — | [Pramp](https://www.pramp.com/) · [Exponent](https://www.tryexponent.com/) |

---

## Suggested sources (your picks) — still in plan

| Resource | Rating | When |
|----------|--------|------|
| LeetCode SQL 50 | ⭐⭐⭐⭐⭐ | Weeks 1–7 |
| StrataScratch Medium | ⭐⭐⭐⭐ | Weeks 5–8 |
| DE Zoomcamp Spark | ⭐⭐⭐⭐⭐ | Weeks 2–4, 16 |
| Databricks perf tuning | ⭐⭐⭐⭐⭐ | Weeks 16–17 |

---

## Stretch path: 50–60+ LPA (extra bar)

Not a different resource list — **higher proof**:

| Area | Minimum bar for 50–60+ |
|------|-------------------------|
| DSA | 80+ LC, **20+ mediums** without hints; timed 25 min |
| SQL | SQL 50 + 15 StrataScratch/DataLemur mediums |
| Spark | Explain shuffle, skew, AQE on whiteboard |
| Design | 4 polished designs (batch, streaming, CDC, RAG) |
| AI | Prod story (Endeavour) + public RAG repo |
| Companies | Google, Databricks, Walmart GTC top band — apply **after** Week 24 mocks |

See [profile.md — stretch section](./profile.md#stretch-50–60-lpa).
