#!/usr/bin/env python3
import re, sys, subprocess, os, shutil

SCRIPTS_DIR = os.path.abspath(os.path.dirname(__file__))


def run(args):
    if shutil.which("uv"):
        subprocess.run(["uv", "run", "python", os.path.join(SCRIPTS_DIR, "tv_cli.py")] + args, check=False)
    else:
        subprocess.run(["python3", os.path.join(SCRIPTS_DIR, "tv_cli.py")] + args, check=False)


def parse(text):
    t = text.strip()
    low = t.lower()

    # explicit commands
    if low.startswith("tv "):
        parts = t.split()[1:]
        return parts

    # recommend
    if any(k in low for k in ["recommend", "what should i watch", "pick a show", "suggest", "any recommendations"]):
        return ["recommend"]

    # list states
    if "paused" in low:
        return ["list", "paused"]
    if "watching" in low or "currently watching" in low:
        return ["list", "watching"]
    if "not started" in low or "to watch" in low or "watchlist" in low:
        return ["list", "not-started"]

    # finish/watched
    m = re.search(r"(?:finished|done with|watched|mark as watched)\s+(.+)$", t, re.I)
    if m:
        return ["finish", m.group(1).strip()]

    # add
    m = re.search(r"(?:add|track)\s+(.+)$", t, re.I)
    if m:
        return ["add", m.group(1).strip()]

    # search
    m = re.search(r"(?:search|find|look up|lookup)\s+(.+)$", t, re.I)
    if m:
        return ["search", m.group(1).strip()]

    # start
    m = re.search(r"(?:start|starting|resume|continue)\s+(.+)$", t, re.I)
    if m:
        return ["start", m.group(1).strip()]

    # pause
    m = re.search(r"(?:pause|paused)\s+(.+)$", t, re.I)
    if m:
        return ["pause", m.group(1).strip()]

    # recap
    if "recap" in low or "summary so far" in low:
        base = re.sub(r".*(?:recap|summary so far)\s+", "", t, flags=re.I).strip() or t
        if "wiki" in low or "wikipedia" in low:
            return ["recap", base, "--wiki"]
        return ["recap", base]

    # episode progress
    m = re.search(r"(?:episode|ep|s)(\d+)[xEe](\d+)\s+for\s+(.+)$", t, re.I)
    if m:
        s, e, show = m.group(1), m.group(2), m.group(3)
        return ["episode", show.strip(), f"{s}x{e}"]
    m = re.search(r"(?:i'm at|im at|up to)\s+s?(\d+)[xEe](\d+)\s+(?:of|in)\s+(.+)$", t, re.I)
    if m:
        s, e, show = m.group(1), m.group(2), m.group(3)
        return ["episode", show.strip(), f"{s}x{e}"]

    # season update
    m = re.search(r"season\s+(\d+|limited series)\s+for\s+(.+)$", t, re.I)
    if m:
        season = m.group(1)
        show = m.group(2).strip()
        season_label = f"Season {season}" if season.isdigit() else season.title()
        return ["season", show, season_label]

    return None


def main():
    if len(sys.argv) < 2:
        print("Usage: tv_router.py <message text>")
        return
    text = " ".join(sys.argv[1:])
    args = parse(text)
    if not args:
        print("No command recognized.")
        return
    run(args)


if __name__ == "__main__":
    main()
