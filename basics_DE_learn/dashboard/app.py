"""
DE Learn Progress Dashboard — week tracker + DSA study plan.

Run:  python app.py
Open:  http://127.0.0.1:5050        — hub
       http://127.0.0.1:5050/week   — weekly tracker
       http://127.0.0.1:5050/dsa    — full DSA plan (like dsa-study-plan.html)
"""

from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from flask import Flask, jsonify, request, send_from_directory

from markdown_sync import sync_tracker

APP_DIR = Path(__file__).resolve().parent
ROOT = APP_DIR.parent
DATA_DIR = APP_DIR / "data"
PROGRESS_FILE = DATA_DIR / "progress.json"
DSA_PROGRESS_FILE = DATA_DIR / "dsa_progress.json"
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


def tz_name(data: dict) -> str:
    return data.get("meta", {}).get("timezone", "Asia/Kolkata")


def today_in_tz(data: dict | None = None) -> date:
    zone = tz_name(data or {})
    return datetime.now(ZoneInfo(zone)).date()


def calendar_week_for(data: dict, on: date | None = None) -> int:
    """Week number from meta.startDate (Week 1 = start day through +6 days)."""
    start_s = data.get("meta", {}).get("startDate")
    if not start_s:
        return int(data.get("meta", {}).get("currentWeek", 1))
    start = date.fromisoformat(start_s)
    d = on or today_in_tz(data)
    return max(1, (d - start).days // 7 + 1)


@app.route("/")
def hub():
    return send_from_directory(STATIC_DIR, "hub.html")


@app.route("/week")
def week_tracker():
    return send_from_directory(STATIC_DIR, "index.html")


@app.route("/dsa")
def dsa_plan():
    return send_from_directory(PLANS_DIR, "dsa-study-plan.html")


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
    week = request.args.get("week", "1")
    data = load_progress()
    if week == "1":
        path = sync_tracker(data)
    else:
        path = ROOT / "learn_plans" / "weekly_tracker" / f"tracker_week{week}.md"
        path = path  # week2+ sync: manual or extend markdown_sync later
    return jsonify({"ok": True, "path": str(path.relative_to(ROOT)), "week": week})


@app.get("/api/stats")
def get_stats():
    week = request.args.get("week", "1")
    data = load_progress()
    w = data.get(f"week{week}", {})
    lc = w.get("leetcode", [])
    sql = w.get("sql50", [])
    exit_items = w.get("exitChecklist", [])
    days = w.get("days", [])

    lc_done = sum(1 for x in lc if x.get("done"))
    sql_done = sum(1 for x in sql if x.get("done"))
    exit_done = sum(1 for x in exit_items if x.get("done"))
    blocks_done = sum(
        sum([d.get("blockA"), d.get("blockB"), d.get("blockC")])
        for d in days
    )
    blocks_total = len(days) * 3 if days else 1

    dsa = load_dsa_progress()
    dsa_done = sum(1 for v in dsa.get("topics", {}).values() if v)

    return jsonify({
        "week": week,
        "leetcode": {"done": lc_done, "total": len(lc)},
        "sql50": {"done": sql_done, "total": len(sql)},
        "exit": {"done": exit_done, "total": len(exit_items)},
        "blocks": {"done": blocks_done, "total": blocks_total},
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


if __name__ == "__main__":
    print("DE Learn Hub:      http://127.0.0.1:5050")
    print("Week tracker:      http://127.0.0.1:5050/week")
    print("DSA study plan:    http://127.0.0.1:5050/dsa")
    app.run(host="127.0.0.1", port=5050, debug=True)
