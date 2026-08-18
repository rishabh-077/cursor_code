# How to use your interview prep system

**Maintainers / Cursor:** [CONTEXT.md](../CONTEXT.md) — full repo map and rules for new weeks.

**Start date (original):** 2026-05-25 · **Week math after rebase:** `meta.startDate` **2026-07-06** — each study week is **Mon → Sun**  
**This week:** [week_07.md](../weekly_plans/week_07.md) (**17–23 Aug 2026**)

---

## One sentence (phased plan — rebased Aug 2026)

**Daily:** [http://127.0.0.1:5050/portal](../dashboard/README.md) — today’s PRIMARY/SECONDARY tasks, LC log, DSA mastery → **Sync to Markdown** → git.  
**Rules:** [MASTER_PLAN.md](../MASTER_PLAN.md) · **DE/theory menu:** [DE_CURRICULUM.md](../DE_CURRICULUM.md) · **This week:** [weekly_plans/week_07.md](../weekly_plans/week_07.md).  
**DSA curriculum:** [dsa-study-plan.html](./dsa-study-plan.html) (one topic/week per [DSA_PACING.md](./DSA_PACING.md)).

`/week` redirects to `/portal` (no separate tracker UI).

---

## Which week / which day?

| Question | Where to look |
|----------|----------------|
| **Which calendar week am I in?** | Portal status bar · `progress.json` → `meta.currentWeek` (from `startDate` **2026-07-06**) |
| **What DSA topic this week?** | [DSA_PACING.md](./DSA_PACING.md) — one focus (Week 7 = t07 Prefix sums) |
| **What do I do today?** | **Portal** — PRIMARY + SECONDARY for today · [weekly_plans/week_0N.md](../weekly_plans/) |
| **Chip / Zoomcamp / DDIA (optional)?** | [DE_CURRICULUM.md](../DE_CURRICULUM.md) week menu · [ai_engineering_notes.md](../theory/ai_engineering_notes.md) for Chip `[x]` |
| **DSA patterns / LC list** | [dsa-study-plan.html](./dsa-study-plan.html) or **/dsa** |
| **Did I finish portal tasks?** | Sync → [trackers/portal_week_NN.md](../trackers/) |

**Update “today”:** **Set today (IST)** on portal.

---

## File map

| File | Job |
|------|-----|
| **[dsa-study-plan.html](./dsa-study-plan.html)** | DSA prep — theory, patterns, problems (t01–t23) |
| **[MASTER_PLAN.md](../MASTER_PLAN.md)** | Phased rules (single source of truth) |
| **[DE_CURRICULUM.md](../DE_CURRICULUM.md)** | DE/theory/SD by calendar week (menu, not daily stack) |
| **[trackers/portal_week_NN.md](../trackers/)** | Synced portal tasks + daily logs |
| [weekly_plans/week_NN.md](../weekly_plans/) | Human-readable week plan |
| [trackers/lc_log.md](../trackers/lc_log.md) | All LC progress |
| [learn_tracker.md](./learn_tracker.md) | Phase exit gates, apply date, interviews |
| [TRACKER_GUIDE.md](./TRACKER_GUIDE.md) | Portal sync + where theory is marked |

---

## Daily — Phase 1 weeks 1–8 (DSA primary)

1. Open **portal** → do **PRIMARY** (~2–2.5 h DSA).
2. **Tue/Thu only:** **SECONDARY** = 30 min SQL 50 (if listed).
3. **Sat (optional):** one **SECONDARY** line if present (Chip catch-up, Zoomcamp, or skip if DSA behind).
4. Save LC to `leetcode/week_N/` · tick LC + mastery in portal.
5. **Chip chapters:** mark `[x]` in [ai_engineering_notes.md](../theory/ai_engineering_notes.md) when done (not per-chapter portal boxes).

---

## Sunday (~15 min)

1. Portal **reflection** (finished / blocked / next week).
2. **Sync to Markdown** → `trackers/portal_week_NN.md`.
3. Tick phase items in [learn_tracker.md](./learn_tracker.md) if a gate cleared.
4. Ask Cursor: **`Generate next week plan.`** ([CONTEXT.md](../CONTEXT.md) §11 — agent auto-reads reflection + trackers)

---

## When to apply

| Milestone | Curriculum week | Approx dates (after Aug 2026 rebase) |
|-----------|-----------------|--------------------------------------|
| Phase 1 DSA exit (t01–t16 + SQL 50) | **~16** | **~19–25 Oct 2026** |
| Phase 2 exit (t01–t23 + RAG + designs) | **~24** | **~14–20 Dec 2026** |
| **Applications** | **~28** | **~11–17 Jan 2027** |

See [MASTER_PLAN.md](../MASTER_PLAN.md) and [learn_tracker.md](./learn_tracker.md).
