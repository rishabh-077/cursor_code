# STAR story — Endeavour Group · Vertex AI / Gemini match validation

**Use for:** Google, Razorpay, Databricks, AI-adjacent DE roles, behavioral “tell me about a challenging project”

---

## S — Situation

At Tiger Analytics for **Endeavour Group** (retail/beverages), we received **competitor product matching** data: whether products found on external portals matched Endeavour’s catalog. Portal naming conventions differed, so **rule-based matching produced false positives and false negatives**.

## T — Task

Design a pipeline step to **validate match quality** using an LLM that could interpret **product names and context**, and flag records analysts should review.

## A — Action *(fill specifics — placeholders below)*

- Integrated **Vertex AI Gemini** API into existing batch pipeline after match generation  
- Defined prompt / input schema: *[e.g. endeavour_product_name, competitor_product_name, match_score, portal_id]*  
- Wrote outputs to *[BQ table name]* with labels: *[match_valid / mismatch / needs_review]*  
- Orchestrated via *[Composer DAG / Cloud Run / other]* with *[retry / rate limit]*  
- Collaborated with *[business users]* to tune prompts on *[N]* sample records  
- *(Add)* Monitoring: *[daily volume, % flagged, cost per 1k calls]*

## R — Result *(fill numbers — even estimates help)*

- Reduced *[X]%* manual review effort OR improved precision on *[Y]* sample audit  
- Processed *[N]* records per *[day/week]*  
- Enabled analysts to focus on *[high-value exceptions]*

---

## 2-minute technical follow-ups (prepare answers)

| Question | Your prepared answer |
|----------|---------------------|
| Why Gemini vs custom ML? | |
| How did you handle API cost? | |
| Hallucination / wrong label risk? | |
| Idempotency if batch re-runs? | |
| PII in product names? | |

---

## Resume bullet (copy when metrics filled)

> Built a **Vertex AI (Gemini)** validation layer for Endeavour Group competitor product-matching data, classifying cross-portal name matches and surfacing false mismatches for analyst review — processing **[N]/day** and **[metric]**.
