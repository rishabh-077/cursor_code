# How to update trackers (checkboxes are not clickable in Preview)

Markdown checkboxes only work when you **edit the file**. Preview mode is read-only.

---

## Interactive dashboard (optional)

Run the web UI to tick progress and sync to markdown:

```powershell
cd basics_DE_learn\dashboard
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5050** · Details: [dashboard/README.md](../dashboard/README.md)

---

## Three tracker levels

| Level | File | Update how often |
|-------|------|------------------|
| **Daily** | [weekly_tracker/tracker_weekN.md](./weekly_tracker/tracker_weekN.md) | Every study day (5 min) — or use dashboard |
| **Weekly** | Same file — Sunday reflection + week exit | Every Sunday (15 min) |
| **Program** | [learn_tracker.md](./learn_tracker.md) | Sunday + when a week/phase completes |

**Plans (what to do):** [weekly_plan/plan_weekN.md](./weekly_plan/plan_week1.md) — do not duplicate tasks in the tracker; tracker = done/not done.

---

## How to check a box

1. Open the `.md` file in the **editor** (not Preview).
2. Find `- [ ]` and change to `- [x]` (lowercase x).

```markdown
- [ ] Block A — DSA          →  not done
- [x] Block A — DSA          →  done
```

3. Save the file (`Ctrl + S`).

---

## Daily routine (end of study session)

Open [tracker_week1.md](./weekly_tracker/tracker_week1.md):

1. Tick **today’s row** in the day table (Blocks A, B, C).
2. If you solved a LeetCode problem → update the LeetCode table (`Solved` → ✅ or `[x]` in notes).
3. Optional: one line under **Today’s note**.

---

## Sunday routine (week close)

1. Fill **Weekly reflection** in `tracker_week1.md`.
2. Tick **Week exit checklist** in [plan_week1.md](./weekly_plan/plan_week1.md).
3. In [learn_tracker.md](./learn_tracker.md) — set Week 1 **Done** column to ✅.
4. Ask Cursor: *“Create plan_week2 and tracker_week2 from learn_plan_v2; my Week 1 reflection: …”*

---

## Can Cursor update trackers for you?

**Yes.** After a study session, paste:

> Update tracker_week1 for 2026-05-26: finished Block A (LC 217), Block B SQL problem 1, Block C DDIA 30 min.

Cursor will edit `- [ ]` → `- [x]` and tables for you. You review and save.

---

## Start date: **2026-05-25**

| Week | Dates (Mon–Sun) | Plan | Tracker |
|------|-----------------|------|---------|
| 1 | 25 May – 31 May 2026 | [plan_week1](./weekly_plan/plan_week1.md) | [tracker_week1](./weekly_tracker/tracker_week1.md) |
| 2 | 1 Jun – 7 Jun 2026 | *create when Week 1 ~70% done* | *tracker_week2* |
| 21 (apply) | ~12 Oct 2026 | Phase 3 | [learn_tracker](./learn_tracker.md) pipeline |
| 30 (end) | ~23 Dec 2026 | Negotiation | |

*Calendar assumes 7-day weeks from start; slip a week = shift dates — update this table on Sunday.*
