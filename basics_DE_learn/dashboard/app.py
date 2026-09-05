"""
DE Learn Progress Dashboard — portal + DSA study plan.

Run:  python app.py
Open:  http://127.0.0.1:5050/portal  — daily portal (primary)
       http://127.0.0.1:5050          — hub
       http://127.0.0.1:5050/dsa      — full DSA plan
"""

from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from flask import Flask, jsonify, redirect, request, send_from_directory

from markdown_sync import (
    clear_portal_daily_logs,
    ensure_portal_reflections,
    merge_portal_daily_logs_to_archive,
    sync_all,
)

APP_DIR = Path(__file__).resolve().parent
ROOT = APP_DIR.parent
DATA_DIR = APP_DIR / "data"
PROGRESS_FILE = DATA_DIR / "progress.json"
DSA_PROGRESS_FILE = DATA_DIR / "dsa_progress.json"
LC_LOG_FILE = DATA_DIR / "lc_log.json"
DSA_MASTERY_FILE = DATA_DIR / "dsa_mastery.json"
WEEK_PLANS_DIR = DATA_DIR / "week_plans"
STATIC_DIR = APP_DIR / "static"
PLANS_DIR = ROOT / "learn_plans"

app = Flask(__name__, static_folder=str(STATIC_DIR))


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        with PROGRESS_FILE.open(encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_progress(data: dict) -> None:
    if "meta" not in data:
        data["meta"] = {}
    data["meta"]["lastUpdated"] = datetime.now().isoformat(timespec="seconds")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with PROGRESS_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_dsa_progress() -> dict:
    if DSA_PROGRESS_FILE.exists():
        with DSA_PROGRESS_FILE.open(encoding="utf-8") as f:
            return json.load(f)
    return {"topics": {}}


def save_dsa_progress(data: dict) -> None:
    data["lastUpdated"] = datetime.now().isoformat(timespec="seconds")
    with DSA_PROGRESS_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_json_file(path: Path, default: dict | None = None) -> dict:
    if path.exists():
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    return default or {}


def save_json_file(path: Path, data: dict) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def sync_dsa_progress_from_mastery(mastery: dict) -> None:
    """Keep dsa_progress.json topic booleans aligned with mastery complete flags."""
    dsa = load_dsa_progress()
    topics = dsa.setdefault("topics", {})
    for tid, t in mastery.get("topics", {}).items():
        topics[tid] = bool(t.get("complete"))
    save_dsa_progress(dsa)


def tz_name(data: dict) -> str:
    return data.get("meta", {}).get("timezone", "Asia/Kolkata")


def today_in_tz(data: dict | None = None) -> date:
    zone = tz_name(data or {})
    return datetime.now(ZoneInfo(zone)).date()


def calendar_week_for(data: dict, on: date | None = None) -> int:
    """Week number from meta.startDate (Week 1 = Mon start day through +6 days, Sun).

    Optional meta.week8SlipFrom (ISO date): from that Monday onward, subtract one
    calendar week so Week 8 can start later (e.g. slip gap Aug 24–30, Week 8 Mon 31 Aug).
    """
    meta = data.get("meta", {})
    start_s = meta.get("startDate")
    if not start_s:
        return int(meta.get("currentWeek", 1))
    start = date.fromisoformat(start_s)
    d = on or today_in_tz(data)
    raw = max(1, (d - start).days // 7 + 1)
    slip_from = meta.get("week8SlipFrom")
    if slip_from and d >= date.fromisoformat(slip_from):
        raw = max(1, raw - 1)
    return raw


@app.route("/")
def hub():
    return send_from_directory(STATIC_DIR, "hub.html")


@app.route("/portal")
def portal():
    return send_from_directory(STATIC_DIR, "portal.html")


@app.route("/week")
@app.route("/week/")
def week_tracker_redirect():
    w = request.args.get("w", "")
    return redirect(f"/portal?w={w}" if w else "/portal")


@app.route("/dsa")
def dsa_plan():
    return send_from_directory(PLANS_DIR, "dsa-study-plan.html")


@app.route("/lc-numbers.js")
def dsa_lc_numbers():
    return send_from_directory(PLANS_DIR, "lc-numbers.js")


@app.route("/<path:path>")
def static_assets(path):
    """CSS/JS for week tracker and hub."""
    file = STATIC_DIR / path
    if file.is_file():
        return send_from_directory(STATIC_DIR, path)
    from flask import abort
    abort(404)


@app.get("/api/progress")
def get_progress():
    return jsonify(load_progress())


@app.put("/api/progress")
def put_progress():
    data = request.get_json(force=True)
    save_progress(data)
    return jsonify({"ok": True, "lastUpdated": data["meta"]["lastUpdated"]})


@app.get("/api/today")
def get_today():
    """IST (or meta.timezone) date vs stored meta.today."""
    data = load_progress()
    actual = today_in_tz(data).isoformat()
    stored = data.get("meta", {}).get("today")
    suggested_week = calendar_week_for(data)
    return jsonify({
        "timezone": tz_name(data),
        "actualToday": actual,
        "storedToday": stored,
        "inSync": stored == actual,
        "currentWeek": data.get("meta", {}).get("currentWeek"),
        "suggestedWeek": suggested_week,
    })


@app.post("/api/set-today")
def post_set_today():
    """Set meta.today to current date in meta.timezone; refresh currentWeek from startDate."""
    data = load_progress()
    meta = data.setdefault("meta", {})
    actual = today_in_tz(data)
    previous = meta.get("today")
    meta["today"] = actual.isoformat()
    meta["currentWeek"] = calendar_week_for(data, actual)
    save_progress(data)
    return jsonify({
        "ok": True,
        "today": meta["today"],
        "previous": previous,
        "currentWeek": meta["currentWeek"],
        "timezone": tz_name(data),
    })


@app.post("/api/sync-markdown")
def post_sync_markdown():
    data = load_progress()
    week_num = int(
        request.args.get("week", data.get("meta", {}).get("currentWeek", 1))
    )
    clear_logs = request.args.get("clear_logs", "1") != "0"

    portal = data.setdefault("portal", {})
    merge_portal_daily_logs_to_archive(portal)
    ensure_portal_reflections(data)
    paths = sync_all(data)
    cleared_dates: list[str] = []
    if clear_logs:
        today = data.get("meta", {}).get("today")
        cleared_dates = clear_portal_daily_logs(
            data, week_num=week_num, only_date=today
        )
    save_progress(data)

    rel = [str(p.relative_to(ROOT)) for p in paths]
    return jsonify({
        "ok": True,
        "paths": rel,
        "week": week_num,
        "clearedLogDates": cleared_dates,
    })


@app.get("/api/stats")
def get_stats():
    data = load_progress()
    lc = load_json_file(LC_LOG_FILE, {"problems": []})
    lc_done = sum(1 for x in lc.get("problems", []) if x.get("done"))
    portal = data.get("portal", {})
    task_days = len(portal.get("dailyTasks", {}))

    dsa = load_dsa_progress()
    dsa_done = sum(1 for v in dsa.get("topics", {}).values() if v)

    return jsonify({
        "leetcode": {"done": lc_done, "total": len(lc.get("problems", []))},
        "portalTaskDays": task_days,
        "dsaTopics": {"done": dsa_done, "total": 23},
        "lastUpdated": data.get("meta", {}).get("lastUpdated"),
    })


@app.get("/api/dsa-progress")
def get_dsa_progress():
    return jsonify(load_dsa_progress())


@app.put("/api/dsa-progress")
def put_dsa_progress():
    data = request.get_json(force=True)
    save_dsa_progress(data)
    return jsonify({"ok": True})


@app.get("/api/lc-log")
def get_lc_log():
    return jsonify(load_json_file(LC_LOG_FILE, {"problems": []}))


@app.put("/api/lc-log")
def put_lc_log():
    data = request.get_json(force=True)
    save_json_file(LC_LOG_FILE, data)
    return jsonify({"ok": True})


@app.get("/api/dsa-mastery")
def get_dsa_mastery():
    return jsonify(load_json_file(DSA_MASTERY_FILE, {"topics": {}}))


@app.put("/api/dsa-mastery")
def put_dsa_mastery():
    data = request.get_json(force=True)
    data["lastUpdated"] = datetime.now().isoformat(timespec="seconds")
    save_json_file(DSA_MASTERY_FILE, data)
    sync_dsa_progress_from_mastery(data)
    return jsonify({"ok": True})


@app.get("/api/week-plan/<int:week>")
def get_week_plan(week: int):
    path = WEEK_PLANS_DIR / f"{week}.json"
    if not path.is_file():
        return jsonify({"error": "not found", "week": week}), 404
    return jsonify(load_json_file(path))


if __name__ == "__main__":
    print("Daily portal:      http://127.0.0.1:5050/portal")
    print("DE Learn Hub:      http://127.0.0.1:5050")
    print("DSA study plan:    http://127.0.0.1:5050/dsa")
    app.run(host="127.0.0.1", port=5050, debug=True)
