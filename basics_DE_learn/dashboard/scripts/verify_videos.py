"""Verify YouTube URLs in VERIFIED_VIDEOS.md plans. Run: python scripts/verify_videos.py"""

import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PLAN = ROOT / "learn_plans" / "VERIFIED_VIDEOS.md"

URL_RE = re.compile(r"https://www\.youtube\.com/[^\s|)]+")


def check(url: str) -> bool:
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status < 400
    except Exception:
        return False


def main() -> None:
    text = PLAN.read_text(encoding="utf-8")
    urls = sorted(set(URL_RE.findall(text)))
    ok = fail = 0
    for url in urls:
        if check(url):
            print(f"OK  {url}")
            ok += 1
        else:
            print(f"FAIL {url}")
            fail += 1
    print(f"\n{ok} ok, {fail} fail")


if __name__ == "__main__":
    main()
