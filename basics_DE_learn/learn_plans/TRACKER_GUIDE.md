# Tracker guide (portal only)

**Daily:** http://127.0.0.1:5050/portal → tick tasks, log, LC, mastery → **Sync to Markdown**.

| Synced file | Source |
|-------------|--------|
| `trackers/portal_week_NN.md` | `progress.json` → `portal.dailyTasks`, `portal.dailyLog`, reflection |
| `trackers/lc_log.md` | `lc_log.json` |
| `trackers/phase_checklist.md` | `dsa_mastery.json` |

**Commit:** `dashboard/data/progress.json`, `lc_log.json`, `dsa_mastery.json`, + synced `trackers/`.

Old Block A/B/C UI archived: `learn_plans/_archive/weekly_tracker/` · data: `dashboard/data/_archive/progress_weeks_legacy.json`
