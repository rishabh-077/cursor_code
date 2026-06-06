# Introduction to Apache Spark Architecture

**Source:** Emil Kaminsky — *Introduction to Apache Spark Architecture* (Databricks notebooks + Spark UI demos)  
**Companion:** [week1_notes.md](./week1_notes.md) · [Spark cluster overview](https://spark.apache.org/docs/latest/cluster-overview.html)

---

## 1. What Spark is (and is not)

| Point | Detail |
|-------|--------|
| **Definition** | Unified compute engine + libraries for **parallel data processing on a cluster** |
| **Not storage** | Spark reads data from one place, transforms it, writes/sends results elsewhere |
| **Sweet spot** | Data too big for one machine — needs multiple nodes |
| **Overkill when** | Data fits on your laptop → pandas/SQL on single node is simpler |

**Interview one-liner:** “Spark is a distributed *compute* layer, not a database. Use it when data and work need a cluster.”

---

## 2. Spark ecosystem & languages

| Module | Purpose |
|--------|---------|
| **Spark SQL** | SQL + DataFrames — main API for DE (what you use daily) |
| **Structured Streaming** | Stream processing |
| **MLlib** | Distributed ML |
| **GraphX** | Graph analytics (less mature) |
| **SparkR** | R API |

| Language | Notes |
|----------|-------|
| **Python** | Most common for DE |
| **SQL** | Runs through Spark SQL |
| **Scala / Java** | Spark written in Scala; JVM-based |
| **R** | SparkR module |

Scala ≈ “Java on the JVM.” You do **not** need Scala for 99.9% of DE work.

**Where Spark runs:** Databricks, GCP Dataproc, AWS EMR, Azure Synapse, on-prem YARN/K8s.

---

## 3. Core architecture

```
You (Python/SQL) → SparkSession → Driver → Cluster Manager → Executors
                                      ↓
                              plans DAG, schedules tasks
                                      ↓
                              Executors read/write data, shuffle, report back
```

### Components

| Component | Role | Interview one-liner |
|-----------|------|---------------------|
| **Driver** | JVM process; entry via `SparkSession`; builds execution plan; splits work into tasks; **almost never touches data** | “The brain — plans jobs, avoids becoming a bottleneck.” |
| **Executor** | JVM worker; runs tasks; holds partitions in memory/disk; reports status to driver | “The muscle — one executor per worker node (typical).” |
| **Cluster manager** | YARN, Mesos, Kubernetes, or Spark Standalone — **allocates** driver + executors | “Resource broker — gives Spark machines to run on.” |
| **SparkSession** | **Only entry point** to Spark (replaces old `SparkContext` for DataFrames) | “Your handle to the cluster.” |

### Slots, tasks, partitions

| Term | Meaning |
|------|---------|
| **Slot** | One CPU core on an executor → one parallel task slot |
| **Task** | Smallest unit of work (exam favorite) — **one task ≈ one partition** |
| **Partition** | Chunk of data; driver decides how to split input; reassigned on shuffle |

**Example cluster (course demo):** 2 workers × 4 cores = **8 slots** → up to **8 tasks in parallel**.

**Key rules:**
- Driver plans; if a task fails, driver **reassigns** it to another executor.
- Executor slots = CPU cores; tasks run in parallel up to slot count.
- Driver + executors run on **JVM**.

---

## 4. Deployment modes (Databricks exam / interviews)

| Mode | Driver | Executors | Use case |
|------|--------|-----------|----------|
| **Local** | Your machine | Your machine | Dev, debug, learning |
| **Client** | Your machine | Cluster (cloud/DC) | Interactive dev; needs good network |
| **Cluster** | Cluster | Cluster | **Production only** |

---

## 5. Jobs → Stages → Tasks (hierarchy)

Every Spark application breaks down as:

```
Application
  └── Job(s)        — triggered by an action (or metadata job)
        └── Stage(s) — separated by shuffle boundaries
              └── Task(s) — one per partition; run on executor slots
```

| Level | Rule of thumb |
|-------|---------------|
| **Job** | One or more per action; jobs usually run **sequentially** |
| **Stage** | Stage N+1 starts after stage N finishes (shuffle boundary) |
| **Task** | As many in parallel as executor **CPU cores** |

**Why stages exist:** Spark **pipelines narrow transformations** (filter, select, map) into one stage. A **wide** transformation (groupBy, join, sort) forces **shuffle** → **new stage**.

**DAG (Directed Acyclic Graph):** Visual plan in Spark UI. **Exchange** in the DAG = **shuffle**.

---

## 6. Walkthrough: `count()` on NYC taxi CSV (~5 GB)

**Query:** `spark.read.csv(...).count()`

**What happens:**

1. **Job 0** — fast metadata job (~1 task): figure out files, partitioning (not full compute).
2. **Job 1** — main work (~12 tasks for 2009 data):
   - Scan CSV per partition
   - **Local partial count** per task (hash aggregate)
   - **Exchange** (shuffle) — gather partial counts
   - **Final count**
3. **Job 2** — tiny (~1 task): return result to driver for display.

**Scaling data:**
- 2009 only → **12 tasks**
- 2009 + 2010 → **24 tasks** (more data → more partitions)
- Single small file (Dec 2019) → **1 task** (Spark: “not worth splitting”)

**Spark UI tabs (most useful):**
- **Jobs** — duration, stage count, task count
- **Stages** — input size, task timeline, shuffle metrics
- **SQL / DataFrame** — higher-level plan (DataFrame/SQL only — **not RDD**)

**Port:** Spark UI default **4040**.

**Reading task timeline:** 2 workers × 4 cores → max **4 tasks per worker** at once; extra tasks queue until a slot frees.

**Partition skew:** Min partition ~457 MB, max ~540 MB on one run — uneven partitions → some tasks finish early (stragglers).

---

## 7. RDD vs DataFrame vs Dataset

| API | Level | Optimized? | SQL tab in UI? | Language |
|-----|-------|------------|----------------|----------|
| **RDD** | Low | No (manual) | No | Scala, Java, Python |
| **DataFrame** | High (Spark SQL) | **Catalyst** | Yes | Python, Scala, Java, R |
| **Dataset** | High + **typed** | **Catalyst** | Yes | **Scala only** (typed) |

### RDD (legacy)

- **Resilient Distributed Dataset** — immutable, distributed collection.
- Fault tolerance via **lineage** (recompute lost partitions).
- API: `filter`, `map`, `reduceByKey` — functional style, not SQL-like.
- Read via **`SparkContext.textFile()`** (not `SparkSession.read`).
- Example: 1 job, **2 stages**, 5 tasks — shuffle between stages; **no SQL/DataFrame tab**.

### DataFrame (default for DE)

- Named columns — table/spreadsheet mental model (pandas-like).
- `spark.read.option(...).csv(...)` + `groupBy().count()` — intuitive SQL style.
- **Catalyst Optimizer** rewrites plan before execution.
- Example: **3 jobs**, each often **1 stage** (optimizer splits work differently than RDD).

### Dataset (Scala)

- Same as DataFrame + **compile-time type safety** via `case class`.
- `spark.read.csv(...).as[TaxiTrip]` — schema enforced at compile time.

**Takeaway:** Prefer **DataFrame/SQL**. RDD = escape hatch for low-level control, not default.

---

## 8. Transformations vs actions

| Type | Runs when? | Examples |
|------|------------|----------|
| **Transformation** | **Lazy** — builds DAG only | `filter`, `select`, `withColumn`, `groupBy`, `join` |
| **Action** | **Triggers execution** | `count`, `collect`, `show`, `take`, `write` |

**Immutability:** Every transformation returns a **new** DataFrame/RDD; originals unchanged.

### Narrow vs wide transformations

| | Narrow | Wide |
|---|--------|------|
| **Shuffle?** | No | Yes — data exchanged between executors |
| **Examples** | `filter`, `select`, `map`, `cast` | `groupBy`, `join`, `sort`, `orderBy`, `distinct` |
| **Per executor** | Process only local partition | Needs data from other partitions |

**Narrow:** Each executor filters/maps **its own** partition — no cross-node talk.

**Wide:** e.g. `sort` — partial sort per executor is not global sort → **shuffle** required.

### Lazy demo (course notebook)

```python
df = spark.read.csv(...)
df = df.filter(...).select(...).groupBy(...).agg(...)  # NO compute yet

df.show()   # NOW Spark runs everything
# df.count()
# df.write.format("noop").save()  # fake write for testing — still an action
```

Before `show()`: only a **fast metadata job** (~1 s) to discover files/partitions — **not** reading 5 GB.

After `show()`: full pipeline (~57 s in demo) — read + transform + aggregate.

---

## 9. `explain()` — see the plan without running

```python
df.filter(...).select(...).groupBy(...).agg(...).explain()       # physical plan
df.filter(...).select(...).groupBy(...).agg(...).explain(True)   # logical + optimized + physical
```

- Read plan **bottom → top** (scan → transforms → shuffle → final agg).
- **Exchange** = shuffle.
- **HashAggregate** = partial group-by per partition.
- Works **without an action** — Catalyst plans ahead.

### Predicate pushdown (lazy optimization)

If you write:

```python
df.filter(passenger_count == 1).select(...).groupBy(...).agg(...)
df.filter(payment_type == "cash")  # added later
```

Catalyst **pushes** `payment_type == "cash"` **next to** `passenger_count == 1` at the scan — filters combined early to **read less data**.

`explain(True)` shows:
- **Parsed logical plan** — what you wrote
- **Optimized logical plan** — after Catalyst (filters merged, constants folded)
- **Physical plan** — what actually runs

**CSV caveat:** Row-based format — Spark must read **whole rows** even if only one column needed. **Parquet/Delta** (columnar) enable true **column pruning**.

---

## 10. Data shuffling (Exchange)

**Shuffle** = redistribute data across partitions between executors.

**Physical steps (slow):**
1. Write partition data from memory → **disk** (shuffle write)
2. Send over **network**
3. Write to disk on target executor → read back to **memory** (shuffle read)

In-memory processing is Spark’s speed advantage; shuffle breaks that.

### How to spot shuffle in Spark UI

| Signal | Meaning |
|--------|---------|
| **Exchange** in DAG / SQL plan | Shuffle happening |
| **Shuffle Write** / **Shuffle Read** metrics | Bytes spilled for shuffle |
| **Yellow bars** on task timeline | Time spent on shuffle write |

### Cardinality matters (same query, different column)

| Group by column | Cardinality | Shuffle size (demo) |
|-----------------|-------------|---------------------|
| `payment_type` | Low (CREDIT/CASH) | ~125 KB |
| `fare_amount` | Medium | ~1.4 MB |
| `pickup_datetime` | **High** (almost unique) | **~673 MB** |
| `orderBy(trip_distance)` | Full sort | **~37 GB** shuffle write, **40 min** job |

**Lesson:** Same `groupBy`/`orderBy` code — shuffle cost depends on **how many distinct keys** you redistribute.

**Default shuffle partitions:** `spark.sql.shuffle.partitions` = **200** (post-shuffle). AQE can collapse this dynamically.

---

## 11. Optimization stack (built-in)

You can tune a lot (format, partitioning, bucketing, cluster size) — but Spark also optimizes automatically:

### Catalyst Optimizer (query planning)

Applies to **SQL, DataFrame, Dataset** (not RDD).

```
Unresolved logical plan
  → validate tables/columns in catalog
  → logical plan
  → optimize (constant folding, predicate pushdown, projection pruning)
  → optimized logical plan
  → generate physical plans (join strategies, etc.)
  → cost model (data read, network, CPU)
  → chosen physical plan
```

### Tungsten (execution / “bare metal”)

- Generates **whole-stage codegen** — fused, optimized JVM bytecode per stage.
- Memory/CPU layout improvements.
- In UI: **WholeStageCodegen** nodes (vs generic `HashAggregate` when Tungsten codegen is off).

### Adaptive Query Execution (AQE)

**Runtime** re-optimization while the job runs.

| AQE can… | Example |
|----------|---------|
| Coalesce shuffle partitions | 200 → 4 (or 1) when data is small |
| Convert sort-merge join → broadcast join | If one side is tiny |
| Handle skew | Split heavy partitions |
| Re-run Catalyst | Between jobs on long queries |

**Demo:** `spark.sql.adaptive.enabled = false` → stage with **200 tasks** after shuffle.  
**AQE on** → extra job; partitions **collapsed** to 1–4; no 200-task stage.

**Why multiple 1-stage jobs?** AQE finishes a stage → re-plans → **new job**.

---

## 12. Partitioning (two moments)

| When | Who decides | What |
|------|-------------|------|
| **Read** | Driver inspects files/size | Input partitions (e.g. 12 for 5 GB, 1 for small file) |
| **Shuffle** | Spark (default 200; AQE may change) | Repartition for wide transforms |

---

## 13. Exam / interview cheat sheet

| Question | Answer |
|----------|--------|
| Smallest unit of work? | **Task** |
| Entry point to Spark? | **SparkSession** (DataFrame); **SparkContext** (RDD) |
| Driver touches data? | **Almost never** — bottleneck risk |
| Slots per executor? | **= CPU cores** |
| Exchange in DAG? | **Shuffle** |
| Lazy vs eager? | Transformations lazy; **actions** trigger execution |
| Narrow vs wide? | Wide = needs **shuffle** |
| RDD vs DataFrame? | DataFrame + **Catalyst**; RDD low-level, no SQL UI tab |
| Default shuffle partitions? | **200** (AQE can reduce) |
| Production deploy mode? | **Cluster mode** |
| CSV vs Parquet for pruning? | CSV reads full rows; **Parquet/Delta** read only needed columns |
| Sort in DE pipelines? | **Avoid** global `orderBy` on huge data unless necessary |

---

## 14. Your one-liners (fill after re-watching)

**Transformation is lazy because:** Spark waits until an action so it can optimize the full DAG (merge filters, push predicates, pick join strategy) before touching data.

**Shuffle is expensive because:** Data leaves memory → disk → network → disk → memory; orders of magnitude slower than in-memory ops.

**Why DataFrame over RDD:** SQL-like API + Catalyst + Spark UI SQL tab + better defaults for production.

---

## 15. Practice habit (from the course)

Every query you run:

1. Open **Spark UI** (Jobs → slowest job → Stages → task timeline).
2. Check **SQL / DataFrame** tab for Exchange and shuffle bytes.
3. Run `.explain(True)` **before** heavy actions.
4. Ask: *Is this shuffle necessary? Can I filter earlier? Is my group-by key high cardinality?*

---

## Quick links

- [Spark cluster overview](https://spark.apache.org/docs/latest/cluster-overview.html)
- [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html)
- [Adaptive Query Execution](https://spark.apache.org/docs/latest/sql-performance-tuning.html#adaptive-query-execution)
- [How Spark works (Databricks)](https://www.youtube.com/watch?v=znBa13W5ocA)
