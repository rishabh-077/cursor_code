# DE Learn Progress Dashboard

Interactive hub: **weekly tracker** (like checkboxes in markdown) + **full DSA study plan** (like [dsa-study-plan.html](../learn_plans/dsa-study-plan.html)).

## Quick start

```powershell
cd basics_DE_learn\dashboard
.\start_dashboard.bat
```

| URL | What |
|-----|------|
| http://127.0.0.1:5050 | **Hub** — pick Week 1, Week 2, or DSA plan |
| http://127.0.0.1:5050/week?w=1 | Week 1 tracker |
| http://127.0.0.1:5050/week?w=2 | **Week 2 tracker (start here)** — Today box + t05/t06 |
| http://127.0.0.1:5050/dsa | **DSA mastery plan** (theory + patterns + LC list) |

## Data files

| File | Purpose |
|------|---------|
| `data/progress.json` | Week 1 & 2 blocks, LC, SQL, exit checklist |
| `data/dsa_progress.json` | DSA topic IDs (t01, t02, …) synced with `/dsa` UI |

**Set today (IST):** Header button on `/week` — sets `meta.today` and recalculates `currentWeek` from `startDate` (25 May 2026). If the calendar week changed, you are redirected to the right `?w=N`.

**Sync to Markdown:** Week 1 → `tracker_week1.md` via button on `/week?w=1`.

## Verify videos before adding to plans

```powershell
python scripts/verify_videos.py
```

See [VERIFIED_VIDEOS.md](../learn_plans/VERIFIED_VIDEOS.md).

## Theory schedule

- **Until 8 Jun 2026:** Chip Huyen *AI Engineering* ([theory_reading.md](../learn_plans/theory_reading.md))
- **From 8 Jun:** DDIA Ch 3+
