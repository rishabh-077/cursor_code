# CONTEXT.md — Agent & maintainer guide for this repo

**Read this file first** before scanning the whole tree. Update this file when the system changes (see §9).

**Human:** [MASTER_PLAN.md](MASTER_PLAN.md) · [HOW_TO_USE.md](learn_plans/HOW_TO_USE.md) · Portal: http://127.0.0.1:5050/portal

---

## 1. What this repo is

DE interview prep for **~3.5 YOE**, target **35–50+ LPA**, apply ~**calendar week 28** (from start **2026-05-25 Monday**).

| Phase | Calendar weeks | Focus |
|-------|----------------|--------|
| **1** | 1–16 | DSA primary · SQL Tue/Thu only (wk 1–8) |
| **2** | 17–24 | DE depth · DSA Tue/Thu maintenance |
| **3** | 25–30 | Mocks · apply |

**Program ID:** `phased-v1` (see `progress.json` → `meta.program`).

---

## 2. Repo map (canonical paths only)

```
basics_DE_learn/
├── CONTEXT.md                 ← THIS FILE (agent bootstrap)
├── MASTER_PLAN.md             ← Rules & phases (rarely changes)
├── weekly_plans/
│   ├── week_01.md             ← Human-readable week plan
│   └── week_02.md
├── trackers/                  ← Git-facing sync output
│   ├── portal_week_01.md      ← Portal tasks + daily logs + reflection
│   ├── portal_week_02.md
│   ├── lc_log.md              ← All LC problems
│   └── phase_checklist.md     ← DSA mastery t01–t16+
├── dashboard/
│   ├── app.py                 ← Flask
│   ├── markdown_sync.py       ← Sync to Markdown
│   ├── README.md
│   ├── data/
│   │   ├── progress.json      ← ONLY meta + portal (slim)
│   │   ├── lc_log.json
│   │   ├── dsa_mastery.json
│   │   ├── dsa_progress.json  ← /dsa UI topic ticks
│   │   ├── week_plans/
│   │   │   ├── 1.json         ← Portal schedule (machine)
│   │   │   └── 2.json
│   │   └── _archive/
│   │       └── progress_weeks_legacy.json  ← old week1/week2 blocks
│   └── static/
│       ├── portal.html / portal.js / portal.css
│       └── hub.html
├── learn_plans/
│   ├── dsa-study-plan.html    ← /dsa — full LC curriculum
│   ├── lc-numbers.js          ← LC id ↔ name for HTML plan
│   ├── DSA_PACING.md          ← One DSA topic per calendar week
│   ├── profile.md
│   ├── HOW_TO_USE.md
│   └── _archive/              ← Old learn_plan_v2, tracker_weekN, plan_week3–6
├── leetcode/week_N/leetcode_*.py
├── python/dsa_theory/         ← arrays.md, strings.md, …
├── sql/weekN_sql50_log.md
├── pyspark/, theory/, behavioral/, projects/
```

**Do not use as daily driver:** `learn_plans/_archive/`, `/week` (redirects to portal), `dashboard/static/_archive/`.

---

## 3. Data flow (portal-first)

```
┌─────────────────────────────────────────────────────────────┐
│  Browser: /portal  +  /dsa                                   │
└────────────┬───────────────────────────────┬────────────────┘
             │ PUT                            │ PUT
             ▼                                ▼
   progress.json                    lc_log.json, dsa_mastery.json
   (meta + portal only)             dsa_progress.json (from mastery)
             │
             │  POST /api/sync-markdown
             ▼
   trackers/portal_week_NN.md
   trackers/lc_log.md
   trackers/phase_checklist.md
             │
             ▼
        git commit
```

**Not automatic:** Markdown does **not** reload into JSON on startup. **New weeks** are **not** auto-created — see §6.

**`week_plans/N.json`:** Read by portal for daily PRIMARY/SECONDARY text. **Not** stored inside `progress.json`.

---

## 4. `progress.json` schema (slim)

```json
{
  "meta": {
    "startDate": "2026-05-25",
    "today": "YYYY-MM-DD",
    "currentWeek": 2,
    "timezone": "Asia/Kolkata",
    "phase": 1,
    "program": "phased-v1",
    "weekStartsOn": "Monday",
    "ddiaArrives": "2026-06-08",
    "lastUpdated": "ISO datetime"
  },
  "portal": {
    "dailyTasks": {
      "YYYY-MM-DD": [primaryDone, secondaryDone]
    },
    "dailyLog": {
      "YYYY-MM-DD": "free text"
    },
    "reflectionDraft": {
      "finished": "",
      "blocked": "",
      "nextWeek": "",
      "energy": 3
    }
  }
}
```

**Removed (archived):** top-level `week1`, `week2`, … legacy Block A/B/C blocks.

---

## 5. Other JSON files

| File | Purpose | Synced to |
|------|---------|-----------|
| `lc_log.json` | LC done, noHints, repo path, week | `trackers/lc_log.md` |
| `dsa_mastery.json` | per topic: theory, easyNoHints, mediumAttempted, complete | `trackers/phase_checklist.md` |
| `dsa_progress.json` | boolean per t01–t23 for `/dsa` | (internal; driven by mastery `complete`) |
| `week_plans/N.json` | 7 days: primary, secondary, sql flag | drives portal UI only |

---

## 6. Adding a new calendar week (e.g. Week 3)

**Trigger:** User asks (hybrid): *"Generate Week N plan"* with reflection + hint audit + mastery status.

**Agent checklist — create/update ALL of:**

| # | Action | Path |
|---|--------|------|
| 1 | Human week plan | `weekly_plans/week_0N.md` |
| 2 | Portal machine plan | `dashboard/data/week_plans/N.json` |
| 3 | Portal dropdown | `dashboard/static/portal.html` → `<option value="N">` |
| 4 | Optional SQL log section | `sql/weekN_sql50_log.md` if SQL that week |
| 5 | Update §10 below | Current week, DSA topic, dates |
| 6 | Update `MASTER_PLAN.md` snapshot | Only if milestone changed |
| 7 | Do **not** add `weekN` to `progress.json` | Legacy pattern removed |

**After user studies:** Sync creates `trackers/portal_week_0N.md` automatically (any `week_plans/*.json`).

**`N.json` day shape:**

```json
{
  "week": 3,
  "phase": 1,
  "range": "Mon 8 Jun – Sun 14 Jun 2026",
  "dsaTopic": "t03",
  "dsaTitle": "Strings",
  "masteryGoal": "…",
  "days": {
    "2026-06-08": {
      "day": "Mon",
      "primary": "…",
      "secondary": "… or none",
      "sql": false
    }
  }
}
```

**Planning rules:** Follow [MASTER_PLAN.md](MASTER_PLAN.md) + [DSA_PACING.md](learn_plans/DSA_PACING.md). Phase 1 wk 1–8: DSA primary; SQL **Tue/Thu only** (30 min). One DSA topic focus per week; carry prior topic if not mastered.

---

## 7. Sync to Markdown (Flask)

**Endpoint:** `POST /api/sync-markdown?week=N&clear_logs=1`

| Output | Source |
|--------|--------|
| `trackers/portal_week_01.md`, `…_02.md`, … | Every `week_plans/*.json` + `portal.*` |
| `trackers/lc_log.md` | `lc_log.json` |
| `trackers/phase_checklist.md` | `dsa_mastery.json` + SQL count from legacy if any |

**Clear daily logs (checkbox, default on):** After sync, deletes `portal.dailyLog` keys for dates in **that week's** `week_plans/N.json` only. **Markdown keeps the text.** `dailyTasks` stay in JSON.

**Does NOT sync:** `progress.json` → nothing imports back from markdown.

---

## 8. LeetCode notes convention

Path: `leetcode/week_N/leetcode_<id>.py`

- Top docstring: problem, pattern, complexity, approaches
- **Keep user's solution code** — do not replace with refactored version unless asked
- Submit class: `Solution` only on LeetCode
- Portal + `/dsa` checkboxes → `lc_log.json`

**Mastery gate (per topic):** theory + Easy **no hints** + ≥1 **Medium attempted** → `dsa_mastery.json`.

---

## 9. Rules for updating THIS file (`CONTEXT.md`)

Update **in the same PR/session** when you:

- Add/remove dashboard routes or JSON files
- Change `progress.json` shape
- Change sync outputs or clear-log behavior
- Add week 3+ (update §10 snapshot)
- Archive or move major folders
- Change phased rules in `MASTER_PLAN.md`

**Do not** duplicate full week plans here — link to `weekly_plans/week_0N.md`.

**§10 snapshot** — bump `lastContextUpdate` date and 3–5 bullets on progress.

---

## 10. Current state (update when things change)

| Field | Value |
|-------|--------|
| **lastContextUpdate** | 2026-06-04 |
| **Calendar week** | 2 (Mon 1 Jun – Sun 7 Jun 2026) |
| **meta.today** | 2026-06-04 |
| **DSA focus** | t02 finish · t03 start |
| **Portal weeks in UI** | 1, 2 (`week_plans/1.json`, `2.json`) |
| **LC logged** | 11 in `lc_log.json` |
| **t02 mastery** | Not complete (need no-hint Easy + medium) |
| **SQL 50** | 8/50 |
| **Known weak spot** | 485, 26, 66, 118, 125 used hints; 283 clean |

---

## 11. User prompt template (new week)

```text
Generate Week N plan (hybrid). Read CONTEXT.md + MASTER_PLAN.md first.

- Calendar week N dates: …
- Reflection from portal: …
- LC hint audit: …
- t02 mastered? Y/N · SQL count: …
- Blocked days: …

Deliver: weekly_plans/week_0N.md, dashboard/data/week_plans/N.json,
portal.html week dropdown, update CONTEXT.md §10.
```

---

## 12. Flask quick reference

```powershell
cd basics_DE_learn\dashboard
python app.py
```

| URL | Role |
|-----|------|
| `/portal` | Daily hub |
| `/portal?w=N` | View week N plan |
| `/dsa` | DSA study plan |
| `/week` | Redirect → `/portal` |

---

## 13. Git commit checklist (weekly)

```text
dashboard/data/progress.json
dashboard/data/lc_log.json
dashboard/data/dsa_mastery.json
dashboard/data/week_plans/N.json
trackers/portal_week_0N.md
trackers/lc_log.md
trackers/phase_checklist.md
weekly_plans/week_0N.md
leetcode/week_N/*.py
```

---

*End of CONTEXT.md — prefer editing this over re-scanning 100+ files.*
