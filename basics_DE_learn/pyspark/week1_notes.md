# PySpark — Week 1 notes

**Plan:** [week_01.md](../weekly_plans/week_01.md) · **Tracker:** [portal_week_01.md](../trackers/portal_week_01.md)

---

## Driver vs Executor (done)

| Role | What it does | Interview one-liner |
|------|----------------|---------------------|
| **Driver** | Runs your `main` / SparkContext; builds the DAG; schedules work; collects small results | “The brain — plans the job, does not process big data itself.” |
| **Executor** | JVM processes on worker nodes; run tasks; store partitions in memory/disk | “The muscle — does the actual compute on data shards.” |

**Flow (batch job):**

1. You submit a Spark app → **Driver** starts.
2. Driver asks the **cluster manager** (YARN, K8s, Dataproc…) for executors.
3. Driver sends **tasks** to executors (each task = a partition of work).
4. Executors read/write data (GCS, BQ connector, Parquet, etc.) and shuffle when needed.
5. Driver returns action results (e.g. `collect()` — avoid on large data).

**Relate to your DE work:** Lowe’s / Endeavour batch jobs — Driver on Composer/Dataproc driver node; executors scale with cluster size.

---

## Lazy transformation vs eager action (done — synced from dashboard)

Fill in **your own words** after [Spark cluster overview](https://spark.apache.org/docs/latest/cluster-overview.html):

| Type | Examples | When work runs |
|------|----------|----------------|
| **Transformation (lazy)** | `filter`, `select`, `join`, `groupBy` | Not until an **action** |
| **Action (eager)** | `count`, `collect`, `show`, `write` | Triggers execution of the DAG |

**Why lazy matters:** Spark can optimize the full DAG (predicate pushdown, shuffle planning) before running.

**Your sentence:** _“A transformation is lazy because …”_

---

## Quick links

- [Spark cluster overview](https://spark.apache.org/docs/latest/cluster-overview.html)
- [How Spark works (Databricks)](https://www.youtube.com/watch?v=znBa13W5ocA)
- [8 min architecture](https://www.youtube.com/watch?v=AJ6Uf9bbLpg)
