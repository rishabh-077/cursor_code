# DE Learn Progress Dashboard

Interactive web UI to track Week 1 progress and sync checkboxes back to `tracker_week1.md`.

## Quick start (local)

**Easiest (Windows):** double-click `start_dashboard.bat` or run:

```powershell
cd basics_DE_learn\dashboard
.\start_dashboard.ps1
```

Or manually:

```powershell
cd basics_DE_learn\dashboard
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5050** in your browser.

## What you can do

| Feature | Description |
|---------|-------------|
| **Progress bars** | LeetCode, SQL 50, exit checklist, daily blocks |
| **Tabs** | Daily blocks, LeetCode, SQL, Spark/BQ, exit list, reflection |
| **Auto-save** | Changes saved to `data/progress.json` (~400ms after each click) |
| **Sync to Markdown** | Rewrites `learn_plans/weekly_tracker/tracker_week1.md` from JSON |

## Data flow

```
Browser UI  →  progress.json  →  (Sync button)  →  tracker_week1.md
```

`progress.json` is the source of truth for the dashboard. Use **Sync to Markdown** before committing to git so your `.md` tracker stays aligned.

## Hosting online (optional)

For access from phone/other PC:

1. **Same WiFi:** use `http://<your-pc-ip>:5050` (Windows firewall may prompt to allow Python).
2. **Cloud:** deploy Flask app to [Render](https://render.com) or [Railway](https://railway.app) with this folder as root; persist `progress.json` via mounted disk or replace with a small DB later.

For now, **local is recommended** — simple and private.

## Adding Week 2+

Extend `data/progress.json` and UI tabs when `plan_week2` exists, or duplicate the week1 structure as `week2` in JSON.
