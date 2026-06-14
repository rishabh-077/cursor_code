# PySpark — Week 1 notes

**Plan:** [week_01.md](../weekly_plans/week_01.md) · **Tracker:** [portal_week_01.md](../trackers/portal_week_01.md)  
**Deep dive:** [spark_architecture_intro.md](./spark_architecture_intro.md) (Emil Kaminsky — Spark architecture course)

---

## What Spark is

- **Compute engine**, not storage — read → transform → write elsewhere.
- Built for **clusters**; overkill if data fits on one machine (use pandas/SQL locally).
- Main API for DE: **Spark SQL / DataFrame** (Python).

---

## Driver vs Executor (done)

| Role | What it does | Interview one-liner |
|------|----------------|---------------------|
| **Driver** | `SparkSession`; builds DAG; schedules tasks; **rarely touches data** | “The brain — plans the job, does not process big data itself.” |
| **Executor** | JVM on worker; runs tasks; holds partitions; 1 executor ≈ 1 worker (typical) | “The muscle — does compute on data shards.” |
| **Cluster manager** | YARN / K8s / Standalone — allocates driver + executors | “Resource broker.” |

**Flow (batch job):**

1. You submit app → **Driver** starts via `SparkSession`.
2. Driver asks **cluster manager** for executors.
3. Driver splits work into **tasks** (one task ≈ one partition).
4. Executors run tasks in parallel (**slots = CPU cores**).
5. Wide ops (groupBy, join, sort) → **shuffle** (Exchange in UI).
6. Action results may return to driver (`show`, `count`) — avoid `collect()` on large data.

**Relate to DE work:** Dataproc/Composer — driver on driver node; executors scale with cluster.

---

## Jobs → Stages → Tasks

| Level | Trigger / boundary |
|-------|-------------------|
| **Job** | Usually one **action** (or metadata discovery) |
| **Stage** | Split at **shuffle** (Exchange in DAG) |
| **Task** | One per partition; parallelized up to core count |

**Spark UI (port 4040):** Jobs → Stages → task timeline + shuffle metrics. SQL/DataFrame tab for DataFrame/SQL only (not RDD).

---

## Lazy transformation vs eager action (done)

| Type | Examples | When work runs |
|------|----------|----------------|
| **Transformation (lazy)** | `filter`, `select`, `join`, `groupBy` | Not until an **action** |
| **Action (eager)** | `count`, `collect`, `show`, `write` | Triggers execution of the DAG |

| Transform kind | Shuffle? | Examples |
|----------------|----------|----------|
| **Narrow** | No | `filter`, `select`, `withColumn` |
| **Wide** | Yes | `groupBy`, `join`, `sort`, `orderBy` |

**Why lazy matters:** Spark optimizes the full DAG before running — predicate pushdown, stage fusion, join strategy, AQE at runtime.

**Your sentence:** A transformation is lazy because Spark waits for an action so Catalyst can merge filters, minimize data read, and plan shuffle stages once instead of executing step-by-step.

**Debug without running:** `df.explain(True)` — read plan bottom → top; look for **Exchange** (= shuffle).

---

## RDD vs DataFrame (high level)

| | DataFrame (use this) | RDD (legacy) |
|---|---------------------|--------------|
| API | SQL-like | `map` / `filter` / `reduceByKey` |
| Optimizer | **Catalyst** | None |
| Spark UI SQL tab | Yes | No |
| Entry | `SparkSession` | `SparkContext` |

---

## Shuffle — when to worry

- **Exchange** in plan = redistribute across executors (memory → disk → network → disk).
- Cost depends on **transformation AND data** — `groupBy` on high-cardinality column shuffles far more than low-cardinality.
- Default post-shuffle partitions: **200**; **AQE** can coalesce at runtime.
- Avoid global **`orderBy`** on huge datasets unless required.

---

## Deployment modes (exam)

| Mode | Production? |
|------|-------------|
| Local | No — dev only |
| Client (driver local, executors remote) | No — interactive dev |
| **Cluster** | **Yes** — driver + executors on cluster |

---

## Quick links

- [spark_architecture_intro.md](./spark_architecture_intro.md) — full course notes
- [Spark cluster overview](https://spark.apache.org/docs/latest/cluster-overview.html)
- [How Spark works (Databricks)](https://www.youtube.com/watch?v=znBa13W5ocA)
- [Spark SQL tuning / AQE](https://spark.apache.org/docs/latest/sql-performance-tuning.html)
