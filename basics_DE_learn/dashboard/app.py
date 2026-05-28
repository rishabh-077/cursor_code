"""
DE Learn Progress Dashboard — local web UI.

Run:  python app.py
Open:  http://127.0.0.1:5050
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

from markdown_sync import sync_tracker

APP_DIR = Path(__file__).resolve().parent
DATA_DIR = APP_DIR / "data"
PROGRESS_FILE = DATA_DIR / "progress.json"
STATIC_DIR = APP_DIR / "static"

app = Flask(__name__, static_folder=str(STATIC_DIR))


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        with PROGRESS_FILE.open(encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_progress(data: dict) -> None:
    data["meta"]["lastUpdated"] = datetime.now().isoformat(timespec="seconds")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with PROGRESS_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


@app.route("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(STATIC_DIR, path)


@app.get("/api/progress")
def get_progress():
    return jsonify(load_progress())


@app.put("/api/progress")
def put_progress():
    data = request.get_json(force=True)
    save_progress(data)
    return jsonify({"ok": True, "lastUpdated": data["meta"]["lastUpdated"]})


@app.post("/api/sync-markdown")
def post_sync_markdown():
    data = load_progress()
    path = sync_tracker(data)
    return jsonify({"ok": True, "path": str(path.relative_to(APP_DIR.parent))})


@app.get("/api/stats")
def get_stats():
    data = load_progress()
    w = data.get("week1", {})
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
    blocks_total = len(days) * 3

    return jsonify({
        "leetcode": {"done": lc_done, "total": len(lc)},
        "sql50": {"done": sql_done, "total": len(sql)},
        "exit": {"done": exit_done, "total": len(exit_items)},
        "blocks": {"done": blocks_done, "total": blocks_total},
        "lastUpdated": data.get("meta", {}).get("lastUpdated"),
    })


if __name__ == "__main__":
    print("DE Learn Dashboard: http://127.0.0.1:5050")
    print("Press Ctrl+C to stop")
    app.run(host="127.0.0.1", port=5050, debug=True)
