# DE Learn Dashboard

**Repo guide for agents:** [../CONTEXT.md](../CONTEXT.md)

**Primary:** http://127.0.0.1:5050/portal

## `progress.json` (slim)

Only:

```json
{
  "meta": { "today", "currentWeek", "startDate", ... },
  "portal": { "dailyTasks", "dailyLog", "reflectionDraft" }
}
```

Legacy `week1` / `week2` blocks removed → archived in `data/_archive/progress_weeks_legacy.json`.

## Sync to Markdown

| Output | Source |
|--------|--------|
| `trackers/portal_week_01.md`, `portal_week_02.md` | Portal tasks + logs |
| `trackers/lc_log.md` | `lc_log.json` |
| `trackers/phase_checklist.md` | `dsa_mastery.json` |

`/week` redirects to `/portal`.

## Other JSON

- `lc_log.json` — LeetCode done / no-hints
- `dsa_mastery.json` — topic gates
- `dsa_progress.json` — `/dsa` UI
- `week_plans/N.json` — portal schedule (not in progress.json)
