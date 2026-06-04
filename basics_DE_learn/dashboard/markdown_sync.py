"""Generate tracker_weekN.md from progress.json."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
TRACKER_DIR = ROOT / "learn_plans" / "weekly_tracker"

WEEK_META = {
    1: {
        "title": "Week 1 tracker · Mon 25 May – Sun 31 May 2026",
        "plan": "plan_week1.md",
        "sql_log": "sql/week1_sql50_log.md",
        "sql_range": "1–4",
        "reflection_day": "Sun 31 May",
    },
    2: {
        "title": "Week 2 tracker · Mon 1 Jun – Sun 7 Jun 2026",
        "plan": "plan_week2.md",
        "sql_log": "sql/week2_sql50_log.md",
        "sql_range": "5–8",
        "reflection_day": "Sun 7 Jun",
    },
}


def _cb(done: bool) -> str:
    return "x" if done else " "


def _count_done(items: list[dict], key: str = "done") -> int:
    return sum(1 for i in items if i.get(key))


def render_tracker_week(week_num: int, week: dict[str, Any], last_updated: str) -> str:
    meta = WEEK_META[week_num]
    lc = week["leetcode"]
    sql = week["sql50"]
    de = week.get("deTopics", [])
    days = week["days"]
    exit_items = week["exitChecklist"]
    refl = week["reflection"]

    lc_done = _count_done(lc)
    sql_done = _count_done(sql)
    de_done = _count_done(de)
    block_c_done = sum(1 for d in days if d.get("blockC"))
    exit_done = _count_done(exit_items)
    exit_total = len(exit_items)

    if week_num == 1:
        if exit_done == exit_total and block_c_done == 0:
            exit_status = "Complete except **Block C (theory)** — ongoing in parallel"
        elif exit_done == exit_total:
            exit_status = "Complete"
        else:
            exit_status = f"{exit_done}/{exit_total} exit items"
    else:
        exit_status = f"{exit_done}/{exit_total} exit items"

    day_rows = "\n".join(
        f"| {d['date']} | {d['day']} | [{_cb(d['blockA'])}] | [{_cb(d['blockB'])}] | [{_cb(d['blockC'])}] | {d.get('notes', '')} |"
        for d in days
    )

    exit_lines = "\n".join(f"- [{_cb(e['done'])}] {e['label']}" for e in exit_items)

    def _lc_row(p: dict) -> str:
        repo = ""
        if p.get("repoFile"):
            repo = f" → [{p['repoFile']}](../../{p['repoFile']})"
        return (
            f"| {p['id']} | [{p['title']}](https://leetcode.com/problems/{p['slug']}/) | {p['pattern']} | "
            f"[{_cb(p['done'])}] | [{_cb(p.get('noHints', False))}] | [{_cb(p.get('complexityInRepo', False))}]{repo} |"
        )

    lc_rows = "\n".join(_lc_row(p) for p in lc)

    sql_rows = "\n".join(
        f"| {s['num']} | [{s['lc']} · {s['title']}](https://leetcode.com/problems/{s['slug']}/) | [{_cb(s['done'])}] | {s['section']} |"
        for s in sql
    )

    de_rows = "\n".join(
        f"| {t['title']} | [{_cb(t['done'])}] | {t.get('path') or 'Notes TBD'} |" for t in de
    )

    energy = refl.get("energy") or "_"
    if isinstance(energy, int) and energy > 0:
        energy = str(energy)

    de_section = ""
    if de_rows:
        de_section = f"""
## DE / theory log

| Topic | Done | Where |
|-------|:----:|-------|
{de_rows}
"""

    return f"""# {meta['title']}

**Plan:** [{meta['plan']}](../weekly_plan/{meta['plan']}) · **Program:** [learn_tracker.md](../learn_tracker.md) · **Dashboard:** [dashboard/README.md](../../dashboard/README.md)

**Last synced from dashboard:** {last_updated}

---

## Progress snapshot

| Area | Status | Detail |
|------|--------|--------|
| **LeetCode** | {lc_done} / {len(lc)} | See log below |
| **SQL 50** | {sql_done} / {len(sql)} | [{meta['sql_log']}](../../{meta['sql_log']}) |
| **DE / theory topics** | {de_done} / {len(de)} | Block C may still be in progress |
| **Week exit** | {exit_status} | Checklist below |

---

## Day-by-day (Blocks A / B / C)

| Date | Day | Block A | Block B | Block C | Notes |
|------|-----|:-------:|:-------:|:-------:|-------|
{day_rows}

---

## Week {week_num} exit

{exit_lines}

---

## LeetCode log

| # | Problem | Pattern | Done | No hints | Notes in repo |
|---|---------|---------|:----:|:--------:|:-------------:|
{lc_rows}

---

## SQL 50 log (#{meta['sql_range']})

| # | Problem | Done | Section |
|---|---------|:----:|---------|
{sql_rows}

Full log: [{meta['sql_log']}](../../{meta['sql_log']})

{de_section}
---

## Weekly reflection (fill {meta['reflection_day']})

- **Finished:** {refl.get('finished') or '_'}
- **Blocked:** {refl.get('blocked') or '_'}
- **Next week adjust:** {refl.get('nextWeek') or '_'}
- **Energy (1–5):** {energy}
"""


def sync_tracker(progress: dict[str, Any], week_num: int = 1) -> Path:
    week = progress[f"week{week_num}"]
    updated = progress["meta"].get("lastUpdated", datetime.now().isoformat(timespec="seconds"))
    path = TRACKER_DIR / f"tracker_week{week_num}.md"
    path.write_text(render_tracker_week(week_num, week, updated), encoding="utf-8")
    return path


TRACKERS_DIR = ROOT / "trackers"
WEEK_PLANS_DIR = ROOT / "dashboard" / "data" / "week_plans"
LC_LOG_JSON = ROOT / "dashboard" / "data" / "lc_log.json"
DSA_MASTERY_JSON = ROOT / "dashboard" / "data" / "dsa_mastery.json"

TOPIC_LABELS = {
    "t01": "Big-O",
    "t02": "Arrays",
    "t03": "Strings",
    "t04": "Hash",
    "t05": "Two pointers",
    "t06": "Sliding window",
    "t07": "Prefix sums",
}


def _load_json(path: Path) -> dict[str, Any]:
    if path.exists():
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    return {}


def render_lc_log(lc: dict[str, Any]) -> str:
    rows = []
    no_hint_count = 0
    for p in lc.get("problems", []):
        done = _cb(p.get("done"))
        nh = _cb(p.get("noHints"))
        if p.get("noHints"):
            no_hint_count += 1
        pid = p["id"]
        title = p["title"]
        slug = title.lower().replace(" ", "-").replace("'", "")
        rows.append(
            f"| {pid} | [{title}](https://leetcode.com/problems/{slug}/) | "
            f"{p.get('topic', '')} | {p.get('week', '')} | {p.get('difficulty', 'Easy')[0]} | "
            f"[{done}] | [{nh}] | {p.get('repo', '')} |"
        )
    n = len(lc.get("problems", []))
    return f"""# LeetCode log (running)

**Synced from dashboard** · **Phase 1 target:** 35+ problems · **Stretch:** 60+

| # | Problem | Topic | Wk | Diff | Done | No hints | Repo |
|---|---------|-------|:--:|:----:|:----:|:--------:|------|
{chr(10).join(rows)}

**Count:** {n} logged · **No-hints count:** {no_hint_count}
"""


def _sql_done_count(progress: dict[str, Any]) -> int:
    n = 0
    for key in progress:
        if key.startswith("week") and isinstance(progress[key], dict):
            for s in progress[key].get("sql50", []):
                if s.get("done"):
                    n += 1
    return n


def render_phase_checklist(
    mastery: dict[str, Any],
    lc: dict[str, Any],
    sql_done: int = 0,
) -> str:
    topics = mastery.get("topics", {})
    t01_t16_done = sum(1 for k, v in topics.items() if k <= "t16" and v.get("complete"))
    lc_n = len(lc.get("problems", []))

    def row(tid: str, label: str) -> str:
        t = topics.get(tid, {})
        return (
            f"| {label} | [{_cb(t.get('theory'))}] | [{_cb(t.get('easyNoHints'))}] | "
            f"[{_cb(t.get('mediumAttempted'))}] | [{_cb(t.get('complete'))}] |"
        )

    mastery_rows = "\n".join(
        row(f"t{i:02d}", TOPIC_LABELS.get(f"t{i:02d}", f"t{i:02d}"))
        for i in range(1, 8)
    )
    rest = "| t08–t16 | … | … | … | [ ] |"

    return f"""# Phase exit checklists

**Mastery rule (each DSA topic):** Theory done · Easy without hints · ≥1 Medium attempted · then mark complete in portal.

---

## Phase 1 — Weeks 1–16 (DSA foundation)

**Target end:** ~mid Sep 2026 · **Current:** Week 2

| Requirement | Target | Current | Done |
|-------------|--------|---------|:----:|
| DSA topics t01–t16 | 16 topics mastered | {t01_t16_done} | [{'x' if t01_t16_done >= 16 else ' '}] |
| LC problems logged | 35+ | {lc_n} | [{'x' if lc_n >= 35 else ' '}] |
| SQL 50 | 30+ / 50 | {sql_done} / 50 | [{'x' if sql_done >= 30 else ' '}] |
| Explain patterns aloud | array, hash, graph basics | — | [ ] |

### DSA topic mastery (portal syncs here)

| Topic | Theory | Easy no hints | Medium tried | Complete |
|-------|:------:|:-------------:|:------------:|:--------:|
{mastery_rows}
{rest}

---

## Phase 2 — Weeks 17–24 (DE depth)

| Requirement | Done |
|-------------|:----:|
| t01–t23 complete | [ ] |
| 60+ LC | [ ] |
| Batch + streaming whiteboard | [ ] |
| RAG repo public | [ ] |

---

## Phase 3 — Weeks 25–30 (interviews)

| Requirement | Done |
|-------------|:----:|
| 8 STAR stories | [ ] |
| Applications live | [ ] |
| Mock cadence weekly | [ ] |
"""


def sync_lc_log(lc: dict[str, Any] | None = None) -> Path:
    TRACKERS_DIR.mkdir(parents=True, exist_ok=True)
    data = lc if lc is not None else _load_json(LC_LOG_JSON)
    path = TRACKERS_DIR / "lc_log.md"
    path.write_text(render_lc_log(data), encoding="utf-8")
    return path


def sync_phase_checklist(
    mastery: dict[str, Any] | None = None,
    lc: dict[str, Any] | None = None,
    progress: dict[str, Any] | None = None,
) -> Path:
    TRACKERS_DIR.mkdir(parents=True, exist_ok=True)
    m = mastery if mastery is not None else _load_json(DSA_MASTERY_JSON)
    l = lc if lc is not None else _load_json(LC_LOG_JSON)
    sql_done = _sql_done_count(progress) if progress else 0
    path = TRACKERS_DIR / "phase_checklist.md"
    path.write_text(render_phase_checklist(m, l, sql_done), encoding="utf-8")
    return path


def _task_flags(portal: dict[str, Any], date: str) -> tuple[bool, bool]:
    tasks = portal.get("dailyTasks", {}).get(date, [False, False])
    primary = bool(tasks[0]) if len(tasks) > 0 else False
    secondary = bool(tasks[1]) if len(tasks) > 1 else False
    return primary, secondary


def render_portal_week(
    week_num: int,
    progress: dict[str, Any],
    plan: dict[str, Any],
    last_updated: str,
) -> str:
    portal = progress.get("portal", {})
    days = plan.get("days", {})
    dates = sorted(days.keys())
    refl = portal.get("reflectionDraft", {})

    rows = []
    for date in dates:
        d = days[date]
        primary_done, secondary_done = _task_flags(portal, date)
        log = (portal.get("dailyLog", {}).get(date) or "").strip() or "_"
        log = log.replace("|", "\\|").replace("\n", " ")
        sec = d.get("secondary", "none")
        sec_cell = (
            f"[{_cb(secondary_done)}] {sec}"
            if sec and sec != "none"
            else "—"
        )
        rows.append(
            f"| {date} | {d.get('day', '')} | [{_cb(primary_done)}] | {sec_cell} | {log} |"
        )

    energy = refl.get("energy") or "_"
    if isinstance(energy, int) and energy > 0:
        energy = str(energy)

    return f"""# Portal log — Week {week_num} ({plan.get('range', '')})

**Synced from** `dashboard/data/progress.json` → `portal.dailyTasks` + `portal.dailyLog`  
**Plan:** [week_{week_num:02d}.md](../weekly_plans/week_{week_num:02d}.md) · **Last synced:** {last_updated}

---

## Daily tasks + log

| Date | Day | Primary done | Secondary | Daily log |
|------|-----|:------------:|-----------|-----------|
{chr(10).join(rows)}

---

## Reflection draft (portal)

- **Finished:** {refl.get('finished') or '_'}
- **Blocked:** {refl.get('blocked') or '_'}
- **Next week adjust:** {refl.get('nextWeek') or '_'}
- **Energy (1–5):** {energy}

*After sync with "clear daily logs", entries above are archived here; live log keys removed from JSON.*
"""


def sync_portal_week(progress: dict[str, Any], week_num: int) -> Path | None:
    plan_path = WEEK_PLANS_DIR / f"{week_num}.json"
    if not plan_path.is_file():
        return None
    plan = _load_json(plan_path)
    updated = progress.get("meta", {}).get("lastUpdated", datetime.now().isoformat(timespec="seconds"))
    TRACKERS_DIR.mkdir(parents=True, exist_ok=True)
    path = TRACKERS_DIR / f"portal_week_{week_num:02d}.md"
    path.write_text(render_portal_week(week_num, progress, plan, updated), encoding="utf-8")
    return path


def apply_portal_reflection_to_week(progress: dict[str, Any], week_num: int) -> bool:
    """Copy portal.reflectionDraft into weekN.reflection for legacy tracker sync."""
    portal = progress.get("portal", {})
    draft = portal.get("reflectionDraft", {})
    week_key = f"week{week_num}"
    if week_key not in progress:
        return False
    if not any(str(draft.get(k, "")).strip() for k in ("finished", "blocked", "nextWeek")):
        return False
    progress[week_key]["reflection"] = {
        "finished": draft.get("finished", ""),
        "blocked": draft.get("blocked", ""),
        "nextWeek": draft.get("nextWeek", ""),
        "energy": draft.get("energy", 0) or 3,
    }
    return True


def clear_portal_daily_logs(progress: dict[str, Any], week_num: int | None = None) -> list[str]:
    """Remove dailyLog keys for dates in week_plans (one week or all)."""
    portal = progress.setdefault("portal", {})
    logs = portal.setdefault("dailyLog", {})
    dates_to_clear: set[str] = set()
    if not WEEK_PLANS_DIR.is_dir():
        return []
    for plan_file in WEEK_PLANS_DIR.glob("*.json"):
        try:
            n = int(plan_file.stem)
        except ValueError:
            continue
        if week_num is not None and n != week_num:
            continue
        plan = _load_json(plan_file)
        dates_to_clear.update(plan.get("days", {}).keys())
    cleared = []
    for date in sorted(dates_to_clear):
        if date in logs and str(logs[date]).strip():
            cleared.append(date)
            del logs[date]
    return cleared


def sync_all(progress: dict[str, Any]) -> list[Path]:
    """Portal + LC + mastery only (legacy tracker_weekN removed)."""
    paths: list[Path] = []
    if WEEK_PLANS_DIR.is_dir():
        for plan_file in sorted(WEEK_PLANS_DIR.glob("*.json")):
            try:
                week_num = int(plan_file.stem)
            except ValueError:
                continue
            p = sync_portal_week(progress, week_num)
            if p:
                paths.append(p)
    paths.append(sync_lc_log())
    paths.append(sync_phase_checklist(progress=progress))
    return paths
