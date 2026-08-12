# CONTEXT.md — Agent & maintainer guide for this repo

**Read this file first** before scanning the whole tree. Update this file when the system changes (see §9).

**Human:** [MASTER_PLAN.md](MASTER_PLAN.md) · [DE_CURRICULUM.md](DE_CURRICULUM.md) (DE / theory / SD week map) · [HOW_TO_USE.md](learn_plans/HOW_TO_USE.md) · Portal: http://127.0.0.1:5050/portal

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
├── DE_CURRICULUM.md           ← DE / SQL / theory / SD by calendar week (detail map)
├── weekly_plans/
│   ├── week_01.md             ← Human-readable week plan
│   ├── week_02.md
│   ├── week_03.md
│   ├── week_04.md
│   ├── week_05.md
│   └── week_06.md
├── trackers/                  ← Git-facing sync output
│   ├── portal_week_01.md      ← Portal tasks + daily logs + reflection
│   ├── portal_week_02.md
│   ├── portal_week_03.md
│   ├── portal_week_04.md      ← (after sync)
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
│   │   │   ├── 2.json
│   │   │   ├── 3.json
│   │   │   ├── 4.json
│   │   │   ├── 5.json
│   │   │   └── 6.json
│   │   └── _archive/
│   │       └── progress_weeks_legacy.json  ← old week1/week2 blocks
│   └── static/
│       ├── portal.html / portal.js / portal.css
│       └── hub.html
├── learn_plans/
│   ├── dsa-study-plan.html    ← /dsa — full LC curriculum
│   ├── lc-numbers.js          ← LC id ↔ name for HTML plan
│   ├── DSA_PACING.md          ← One DSA topic per calendar week
│   ├── RESOURCES.md           ← All video & doc URLs
│   ├── theory_reading.md      ← Chip → DDIA schedule (points to DE_CURRICULUM)
│   ├── profile.md
│   ├── learn_tracker.md       ← Phase exit gates + parallel backlog (Block C)
│   ├── HOW_TO_USE.md
│   ├── TRACKER_GUIDE.md       ← Portal sync + theory marking (not legacy archive)
│   ├── weekly_plan/README.md  ← Deprecated → use weekly_plans/
│   └── _archive/              ← Old learn_plan_v2, tracker_weekN, plan_week3–6
├── leetcode/week_N/leetcode_*.py
├── python/dsa_theory/         ← arrays.md, strings.md, …
├── sql/week1_sql50_log.md, week2_sql50_log.md, …
├── pyspark/, theory/ai_engineering_notes.md, behavioral/, projects/
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

## 3b. Planning layers — what to do today (human + agent)

**Do not treat [DE_CURRICULUM.md](DE_CURRICULUM.md) as the daily schedule.** Full prose: DE_CURRICULUM §“How to read this” + §“Portal vs DE_CURRICULUM”.

| Layer | File | Role |
|-------|------|------|
| **Rules** | [MASTER_PLAN.md](MASTER_PLAN.md) | Phase 1: one primary/day; SQL Tue/Thu 30 min only (wk 1–8); no 3 subjects same evening |
| **Daily** | Portal + `week_plans/N.json` + `weekly_plans/week_0N.md` | **Source of truth for today** — checkboxes |
| **Week menu** | [DE_CURRICULUM.md](DE_CURRICULUM.md) | Calendar-week **bucket** (Chip, Zoomcamp, DDIA…) — optional unless copied into portal |
| **Long gates** | [learn_plans/learn_tracker.md](learn_plans/learn_tracker.md) | Phase 1 **exit** (~wk 16): SQL 50, Zoomcamp, Spark lazy, Chip notes — not “must finish in week 2” |

### If it is in portal vs only in DE_CURRICULUM

| Portal field | You must |
|--------------|----------|
| **PRIMARY** | Do it (DSA in Phase 1 wk 1–8) |
| **SECONDARY** | Do it that day (SQL Tue/Thu, or **optional** Sat DE/theory — pick one or skip if DSA behind) |
| **Only in DE_CURRICULUM row** | **Parallel backlog** — not forgotten; defer OK while DSA weak |

**Phase 1 daily (wk 1–8):** Mon/Wed/Fri/Sat = DSA primary · Tue/Thu = DSA + SQL secondary · Sun = reflection ~15 min · DE/theory = **Sat optional secondary** in `N.json` when generating the week (max one of Chip / Zoomcamp / video). **Chip:** next unchecked ch in `theory/ai_engineering_notes.md` — never assign Ch 3–4 if Ch 1–2 are still open.

### Skipped Chip / Zoomcamp / theory

1. Does **not** fail the calendar week if portal DSA/SQL done.  
2. Stays on **learn_tracker** Phase 1 exit checklist + user `reflectionDraft.blocked` / `nextWeek`.  
3. **Week N+1:** agent reads reflection + backlog + DE_CURRICULUM row → add **one** optional Sat secondary **or** defer to week 9+ (MASTER_PLAN late Phase 1).  
4. **DSA mastery** overrides DE backlog (carry t02 before advancing t03).

**Week 2 example:** Portal = LC + SQL; Sat optional = **Chip Ch 1–2 catch-up** (not Ch 3–4 until notes show Ch 1–2 done) or Zoomcamp — see `ai_engineering_notes.md` chapter log.

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
      "YYYY-MM-DD": "free text (live; cleared after sync if checkbox on)"
    },
    "archivedDailyLog": {
      "YYYY-MM-DD": "persisted log text for markdown after clear"
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

**Trigger:** User says **`Generate Week N plan.`** or **`Generate next week plan.`** — see §11. Agent **auto-reads** all inputs from repo files; do **not** ask the user to paste dates, SQL count, hint audit, or backlog unless a file is missing or reflection is empty.

### Auto-read before writing (agent — no user paste)

| Source | Gets |
|--------|------|
| `CONTEXT.md` §3b, §10 | Planning rules + current snapshot |
| `MASTER_PLAN.md` | Phase / daily shape |
| `DSA_PACING.md` | DSA topic for calendar week **N** |
| `DE_CURRICULUM.md` | Row for calendar week **N** (DE menu) |
| `dashboard/data/progress.json` | `meta` · `portal.reflectionDraft` · `dailyTasks` for week **N−1** |
| `trackers/portal_week_{N-1}.md` | Prior week logs + synced reflection |
| `lc_log.json` or `trackers/lc_log.md` | Hint audit → re-solve queue (`noHints: false`) |
| `dsa_mastery.json` or `trackers/phase_checklist.md` | Prior topic mastered? carry-forward? |
| `learn_plans/learn_tracker.md` | Phase 1 exit backlog (Chip, Zoomcamp, Spark lazy, …) |
| `theory/ai_engineering_notes.md` | Next unchecked Chip chapter (Sat optional) |
| `sql/week*_sql50_log.md` | SQL count |
| `weekly_plans/week_{N-1}.md` | Prior plan format + carry-forward LC queue |

**Infer N:** `N = meta.currentWeek + 1` unless user names **Week N**. **Dates:** Mon–Sun from `meta.startDate` + week number (`weekStartsOn: Monday`).

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

**Planning rules:** Follow [MASTER_PLAN.md](MASTER_PLAN.md) + [DSA_PACING.md](learn_plans/DSA_PACING.md) + [DE_CURRICULUM.md](DE_CURRICULUM.md) (row for calendar week N: SQL, DE parallel, Chip/DDIA, videos). Phase 1 wk 1–8: DSA primary; SQL **Tue/Thu only** (30 min). DE/theory from DE_CURRICULUM = **parallel/Sat optional secondary** in `week_plans/N.json` (pick one), not a third equal weeknight block. **Carry-forward:** if user skipped Chip/Zoomcamp, read `learn_tracker.md` Phase 1 exit + portal `reflectionDraft.blocked` / `nextWeek` and attach **one** optional secondary on Sat or defer to week 9+. One DSA topic focus per week; carry prior topic if not mastered.

---

## 7. Sync to Markdown (Flask)

**Endpoint:** `POST /api/sync-markdown?week=N&clear_logs=1`

| Output | Source |
|--------|--------|
| `trackers/portal_week_01.md`, `…_02.md`, … | Every `week_plans/*.json` + `portal.*` |
| `trackers/lc_log.md` | `lc_log.json` |
| `trackers/phase_checklist.md` | `dsa_mastery.json` + SQL count from legacy if any |

**Clear daily logs (checkbox, default on):** Before sync, non-empty logs copy to `portal.archivedDailyLog`. Sync **reads existing** `portal_week_NN.md` into archive if JSON is empty (manual edits kept). After sync, clears **only `meta.today`** live log in portal — not the whole week. Markdown = live + archived. **Do not edit tracker md for long-term storage without syncing once** — or edits are imported on next sync. `dailyTasks` stay in JSON.

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
- Change DE/theory/SD week mapping → update [DE_CURRICULUM.md](DE_CURRICULUM.md) + [learn_plans/theory_reading.md](learn_plans/theory_reading.md) if book schedule shifts

**Do not** duplicate full week plans here — link to `weekly_plans/week_0N.md` and `DE_CURRICULUM.md` for DE/theory rows.

**§10 snapshot** — bump `lastContextUpdate` date and 3–5 bullets on progress.

---

## 10. Current state (update when things change)

| Field | Value |
|-------|--------|
| **lastContextUpdate** | 2026-06-29 (Week 6 plan generated — auto-read from wk 5 reflection) |
| **Calendar week** | 6 (Mon 29 Jun – Sun 5 Jul 2026) |
| **meta.today** | 2026-06-27 (set in portal when you open wk 6) |
| **DSA focus** | **t06 Sliding window** (primary) · do not start t07 until pattern automatic |
| **Portal weeks in UI** | 1–6 (`week_plans/1.json` … `6.json`) |
| **LC logged** | 28 in `lc_log.json` · 19 no-hints · **#11** no-hints (wk 5) |
| **t04–t05 mastery** | ✅ Complete in portal · light optional re-solve: #977, #167, #15 (used hints) |
| **t06 mastery** | Not started — theory + #643, #1456 + Medium **#3** |
| **SQL 50** | ~20/50 (#1–20) · wk 6 target #21–24 Tue/Thu → **24–25/50** |
| **Hint re-solve queue** | #977, #167, #15 (optional) · #49, #205, #347 · 88, 118 optional |
| **Theory spine** | **Still nothing checked off** — Chip Ch 1 first · Zoomcamp mod 1 · DDIA Ch 5–6 (wk 6 menu) |
| **Parallel backlog** | Chip Ch 1 · Zoomcamp mod 1 · PySpark lazy · StrataScratch — Sat optional ONE |
| **Week 6 plan** | [weekly_plans/week_06.md](weekly_plans/week_06.md) · DE menu: DDIA replication/partition · Chip catch-up |

---

## 11. User prompt (new week) — minimal

### Default (copy-paste)

```text
Generate next week plan.
```

Or name the week explicitly:

```text
Generate Week 6 plan.
```

**That is enough.** Agent follows §6 auto-read + deliverables. Behavior matches the old long “hybrid” prompt — reflection, hint audit, mastery, backlog, and DE menu all come from repo files.

### Before you prompt (~2 min on Sunday)

1. Fill portal **reflection** (`finished` / `blocked` / `nextWeek` / `energy`).
2. **Sync to Markdown** for the week you just finished.
3. Paste **`Generate next week plan.`** in Cursor.

If reflection is empty, agent uses `portal_week_{N-1}.md` logs + §10 — or asks **one** question: *“Anything blocked for next week?”*

### Optional overrides (only when needed)

Add **one short line** after the default prompt — do not repeat the old bullet list.

```text
Generate Week 6 plan. Blocked: DDIA book not arrived.
```

```text
Generate next week plan. Hold t05 — #15 still needs no-hint re-solve.
```

```text
Generate Week 6 plan. Skip Sat optional — DSA catch-up only.
```

### Agent must still deliver (§6)

`weekly_plans/week_0N.md` · `dashboard/data/week_plans/N.json` · `portal.html` week dropdown · `sql/weekN_sql50_log.md` (if SQL that week) · bump `CONTEXT.md` §10

### Deprecated — do not use

Long prompts with manual dates, SQL count, hint audit, and backlog bullets are **redundant** — agent reads §6 auto-read table instead.

---

## 12. Flask quick reference

```powershell
cd basics_DE_learn\dashboard
python app.py
```

| URL | Role |
|-----|------|
| `/` | Hub (links to portal + /dsa) |
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
