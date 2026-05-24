# Pipeline whiteboard template (fill one per client)

**Purpose:** In DE interviews you get *“Walk me through a pipeline you built end-to-end.”*  
You need **facts**, not a perfect diagram. **15–20 bullets** is enough.

Copy this file to `lowes_pipeline.md` and `endeavour_pipeline.md` and fill in.

---

## Client: _____________ (Lowe’s / Endeavour Group)

### 1. Business context (30 seconds)

| Question | Your answer |
|----------|-------------|
| What business problem did this solve? | |
| Who consumed the data? (analysts, ML team, ops, finance) | |
| How often did they need fresh data? (hourly / daily / weekly) | |

---

### 2. Sources → landing (ingestion)

| Question | Your answer |
|----------|-------------|
| **Source systems** (SAP, APIs, SFTP, GCS files, Pub/Sub, etc.) | |
| **Format** (CSV, JSON, Parquet, DB CDC) | |
| **Volume** (GB/day, rows/day — rough order of magnitude) | |
| **Ingestion tool** (Composer/Airflow, Fivetran, custom Python, Dataflow) | |
| **Landing zone** (GCS bucket path pattern?) | |
| **Idempotency** — what if the same file runs twice? | |

---

### 3. Transform (dbt / Spark / SQL)

| Question | Your answer |
|----------|-------------|
| **dbt** — staging → intermediate → mart layer names (2–3 examples) | |
| **Materialization** (view / table / incremental — which facts were incremental?) | |
| **Incremental key** (date, `updated_at`, merge key) | |
| **Dataproc** — used or not? If yes, what job (join, aggregate, ML feature prep) | |
| **Data quality** (dbt tests, Great Expectations, custom checks) | |
| **One hard bug you fixed** (schema drift, late data, duplicate keys) | |

---

### 4. Warehouse (BigQuery)

| Question | Your answer |
|----------|-------------|
| **Dataset structure** (raw / staging / analytics) | |
| **Partition column** | |
| **Cluster columns** (if any) | |
| **Approx table size** or query pattern (daily aggregate vs row-level) | |
| **Cost optimization** you did (partition pruning, avoid `SELECT *`, slot reservation?) | |

---

### 5. Orchestration & CI/CD

| Question | Your answer |
|----------|-------------|
| **Composer** — DAG name pattern, schedule, dependencies | |
| **ADO** — what triggers deploy (PR merge → dbt run / Cloud Run?) | |
| **Failure alerting** (email, PagerDuty, Slack) | |
| **SLA** — what happens if DAG misses SLA? | |

---

### 6. Consumption & impact

| Question | Your answer |
|----------|-------------|
| **Downstream** (Looker, Power BI, reverse ETL, ML feature store) | |
| **Metric you improved** (% faster reports, cost saved, error rate down) | |
| **Your specific ownership** vs team (you designed / you built / you maintained) | |

---

### 7. Endeavour only — Vertex AI / Gemini branch

| Question | Your answer |
|----------|-------------|
| **Input to Gemini** (fields sent: product names, competitor name, match score?) | |
| **Trigger** (batch after match job / API / Composer task) | |
| **Output** (label: valid match / mismatch / confidence) | |
| **Where output lands** (BQ table, feedback queue for analysts) | |
| **Volume** (records/day) | |
| **Evaluation** — how did you know the LLM was “good enough”? | |
| **Guardrails** (rate limits, cost cap, PII filtering) | |

---

### 8. Whiteboard draw order (practice this aloud)

Draw left → right in **under 5 minutes**:

```
[Sources] → [Ingest/Landing GCS] → [dbt/Spark transform] → [BigQuery marts] → [BI / ML / Gemini]
                ↑
         [Composer/Airflow schedule]
```

Say at each box: **technology + one sentence why**.

---

### 9. 60-second opener (script — fill blanks)

> “At Tiger for **[client]**, I worked on **[business problem]**. Data flowed from **[sources]** into **[landing]**, we transformed with **[dbt/Spark]** into **[BQ datasets]**, orchestrated by **[Composer]**, and consumed by **[downstream]**. I personally owned **[X]**. One optimization I’m proud of is **[metric/cost/latency]**.  
> *(Endeavour add-on)* We also integrated **Vertex AI Gemini** to **[classify matches / reduce false positives]**.”

---

## Minimum details needed from you (reply in chat or edit this file)

To make your whiteboard **interview-ready**, send **bullet answers** for **one** client first (recommend **Endeavour** — unique AI angle):

1. Source type + format  
2. Ingestion tool (Composer task name pattern is enough)  
3. 2–3 dbt model layers you touched  
4. BQ partition/cluster (if any)  
5. Schedule (daily/hourly)  
6. One metric (volume or business impact)  
7. For Endeavour Gemini: input fields, output table, rough volume/day  

Lowe’s can be second — good for Walmart / retail interviews.
