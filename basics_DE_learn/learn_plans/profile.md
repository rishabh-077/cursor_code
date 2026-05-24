# Your interview profile (personalized)

**Last updated:** from your answers · **Master plan:** [learn_plan_v2.md](./learn_plan_v2.md) · **Resources:** [RESOURCES.md](./RESOURCES.md) · **Hub:** [README.md](../../README.md)

---

## Logistics

| Item | Your answer | Plan impact |
|------|-------------|-------------|
| **Notice period** | 2 months | Start applications **Week 21**; offer timeline = interview length + 2 months |
| **Location** | Remote preferred → Hyderabad, Bangalore, Pune, Mumbai | Filter roles; highlight remote delivery at Tiger |
| **Risk** | Startups OK if growth exists | Tier B startups + unicorns in apply list, not only Big Tech |
| **Current CTC** | ~25 LPA | Negotiate on **fixed + variable + ESOP** separately |

---

## Target companies (tailored prep)

| Company | Why you fit | Interview emphasis | Prep focus |
|---------|-------------|-------------------|------------|
| **Google** | GCP, BQ, scale | LC Medium+, system design, GCP depth | NeetCode 150, GCP cert topics, BQ cost stories |
| **Walmart Global Tech** | Retail data, batch pipelines | SQL, Spark/BQ, behavioral scale | Lowe’s retail story, supply chain metrics |
| **Databricks** | Spark, lakehouse | PySpark internals, Delta awareness | Weeks 6–7, 16; Spark shuffle, AQE |
| **Snowflake** | SQL, warehousing | SQL windows, modeling, migration angles | SQL 50 + DataLemur; compare BQ vs Snowflake |
| **Fivetran** | Ingestion, EL | CDC concepts, connector mindset, dbt | Week 19 CDC; pipeline reliability |
| **Razorpay** | India product, GCP common | DE + SQL + light LC | Medium LC + payment data sensitivity (PII) |
| **JP Morgan / Chase** | Enterprise batch, compliance | SQL heavy, process, reliability | STAR on governance, idempotent pipelines, audit |

**Apply order (suggested):** Razorpay → Walmart GTC → Fivetran → Databricks/Snowflake → Chase/JPM → Google (after mocks strong).

---

## Tiger clients — pipeline whiteboard assets

You have **two** strong stories. Pick **one primary** for 5-min “walk me through your pipeline” and keep the second as backup.

| Client | Use for interviews targeting |
|--------|------------------------------|
| **Lowe’s** | Retail, Walmart GTC, large-scale batch |
| **Endeavour Group** | GCP, Vertex AI / GenAI, product matching, Australia retail |

**Fill in:** [pipeline_whiteboard_template.md](../behavioral/pipeline_whiteboard_template.md) (one file per client).

---

## AI / GenAI on resume (two bullets)

### 1. Production — Endeavour (already built) ✅

**One-liner for resume (XYZ style):**  
*Improved competitor product-match quality for Endeavour Group by building a Vertex AI (Gemini) classification pipeline that validated customer-matching outputs and flagged false mismatches caused by cross-portal naming differences.*

**Interview story (2 min):**  
- **Problem:** Competitor product matches arrived from portals with inconsistent naming vs Endeavour SKUs.  
- **Solution:** Passed match records to **Gemini via Vertex AI**; LLM judged true match vs false mismatch using product names/context.  
- **Your role:** Pipeline integration, prompting/eval design, monitoring bad matches (fill metrics below).  
- **Tech:** GCP, Vertex AI, Gemini, (BQ/Composer/dbt — *fill what you used*).

### 2. Side project — RAG pipeline (to build, Week 14)

**Goal:** Small but **real** repo: ingest docs → chunk → embed → vector store → query → answer with citations.

| Week | Deliverable |
|------|-------------|
| 14 | MVP script + README architecture diagram |
| 19 | 1-page “how I’d run this in prod on GCP” (Cloud Run + Vertex embeddings + optional Vector Search) |

**Outline:** [rag_side_project.md](../projects/rag_side_project.md)

---

## Apply timeline (start **2026-05-25**, 2-month notice)

| Week | Date (approx) | Action |
|------|---------------|--------|
| 1 | 25 May 2026 | Prep starts — [plan_week1](./weekly_plan/plan_week1.md) |
| 19 | 28 Sep 2026 | Resume + LinkedIn |
| 20 | 5 Oct 2026 | Phase 2 exit; RAG repo public |
| **21** | **12 Oct 2026** | **Applications** |
| 27–30 | Nov–Dec 2026 | Offers · negotiate |
| Join | Offer + **2 months** | |

---

## Stretch: 50–60+ LPA

**Honest:** 50–60+ in India for ~3.5 YOE DE is **top band** (Google L4/L5 band, Databricks senior IC, Walmart principal-track). Achievable but not the default outcome of the base plan.

| Lever | What you need |
|-------|----------------|
| **DSA** | 80+ LC, 20+ mediums timed; don’t apply Google until mocks are clean |
| **DE depth** | 4 whiteboard-ready designs + Endeavour AI prod + RAG repo |
| **Negotiation** | Multiple offers; RSU/ESOP literate |
| **Timeline** | May need **Week 30+** extension (9–10 months total) if DSA starts from zero |
| **Tier** | Prioritize Databricks, Google, Walmart GTC high band — not only service companies |

**Realistic ladder:** 35–42 (base plan) → 42–50 (Phase 2 solid) → 50–60+ (stretch + right company + interview peak).

---

## Open items (fill when you can)

- [ ] Lowe’s pipeline template completed  
- [ ] Endeavour pipeline template completed  
- [ ] Metrics for Gemini project (% mismatch reduction, volume/day)  
- [ ] RAG repo URL on resume  
- [x] Start date **2026-05-25** in [learn_tracker.md](./learn_tracker.md)
