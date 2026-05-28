"""Generate tracker_week1.md from progress.json."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
TRACKER_PATH = ROOT / "learn_plans" / "weekly_tracker" / "tracker_week1.md"


def _cb(done: bool) -> str:
    return "x" if done else " "


def _count_done(items: list[dict], key: str = "done") -> int:
    return sum(1 for i in items if i.get(key))


def render_tracker(week: dict[str, Any], last_updated: str) -> str:
    lc = week["leetcode"]
    sql = week["sql50"]
    de = week["deTopics"]
    days = week["days"]
    exit_items = week["exitChecklist"]
    refl = week["reflection"]

    lc_done = _count_done(lc)
    sql_done = _count_done(sql)
    spark_done = sum(1 for t in de if t["id"].startswith("spark") and t["done"])
    spark_total = sum(1 for t in de if t["id"].startswith("spark"))

    day_rows = "\n".join(
        f"| {d['date']} | {d['day']} | [{_cb(d['blockA'])}] | [{_cb(d['blockB'])}] | [{_cb(d['blockC'])}] | {d.get('notes', '')} |"
        for d in days
    )

    exit_lines = "\n".join(
        f"- [{_cb(e['done'])}] {e['label']}" for e in exit_items
    )

    def _lc_row(p: dict) -> str:
        repo = f" → [{p['repoFile']}](../../{p['repoFile']})" if p.get("repoFile") else ""
        return (
            f"| {p['id']} | [{p['title']}](https://leetcode.com/problems/{p['slug']}/) | {p['pattern']} | "
            f"[{_cb(p['done'])}] | [{_cb(p['noHints'])}] | [{_cb(p['complexityInRepo'])}]{repo} |"
        )

    lc_rows = "\n".join(_lc_row(p) for p in lc)

    sql_rows = "\n".join(
        f"| {s['num']} | [{s['lc']} · {s['title']}](https://leetcode.com/problems/{s['slug']}/) | [{_cb(s['done'])}] | {s['section']} |"
        for s in sql
    )

    de_rows = "\n".join(
        f"| {t['title']} | [{_cb(t['done'])}] | {t['path'] or 'Notes TBD'} |"
        for t in de
    )

    energy = refl.get("energy") or "_fill Sunday_"
    if isinstance(energy, int) and energy > 0:
        energy = str(energy)

    return f"""# Week 1 tracker · 25 May – 31 May 2026

**Plan:** [plan_week1.md](../weekly_plan/plan_week1.md) · **Program tracker:** [learn_tracker.md](../learn_tracker.md) · **Dashboard:** [dashboard/README.md](../../dashboard/README.md)

**Last synced from dashboard:** {last_updated}

---

## Progress snapshot

| Area | Status | Detail |
|------|--------|--------|
| **LeetCode (Python)** | {lc_done} / {len(lc)} | See LeetCode log below |
| **SQL 50** | {sql_done} / {len(sql)} | [sql/week1_sql50_log.md](../../sql/week1_sql50_log.md) |
| **PySpark** | {spark_done} / {spark_total} topics | [pyspark/week1_notes.md](../../pyspark/week1_notes.md) |
| **Week exit** | In progress | See checklist below |

---

## Day-by-day (tick Blocks A / B / C)

| Date | Day | Block A (DSA) | Block B (DE) | Block C (theory) | Notes |
|------|-----|:-------------:|:------------:|:----------------:|-------|
{day_rows}

---

## Week 1 exit (mirror plan)

{exit_lines}

---

## LeetCode log (Week 1)

| # | Problem | Pattern | Done | No hints | Complexity in repo |
|---|---------|---------|:----:|:--------:|:------------------:|
{lc_rows}

---

## SQL 50 log (Week 1 — problems 1–4)

| # | Problem (study plan order) | Done | Notes |
|---|---------------------------|:----:|-------|
{sql_rows}

Study plan: https://leetcode.com/studyplan/top-sql-50/

---

## PySpark / BQ log (Week 1)

| Topic | Done | Where |
|-------|:----:|-------|
{de_rows}

---

## Weekly reflection (fill Sunday 2026-05-31)

- **Finished:** {refl.get('finished') or '_'}
- **Blocked:** {refl.get('blocked') or '_'}
- **Next week adjust:** {refl.get('nextWeek') or '_'}
- **Energy (1–5):** {energy}
"""


def sync_tracker(progress: dict[str, Any]) -> Path:
    week = progress["week1"]
    updated = progress["meta"].get("lastUpdated", datetime.now().isoformat(timespec="seconds"))
    TRACKER_PATH.write_text(render_tracker(week, updated), encoding="utf-8")
    return TRACKER_PATH
