#!/usr/bin/env python3
import os, sqlite3, sys, json, subprocess, re, urllib.parse, urllib.request

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DB = os.path.join(SKILL_DIR, "data", "tv.sqlite")
DB_PATH = os.environ.get("TV_DB_PATH") or DEFAULT_DB
SCRIPTS_DIR = os.path.abspath(os.path.dirname(__file__))

STATUS_MAP = {
    "watching": "👁Watching",
    "paused": "⏸Paused",
    "not-started": "🙈 Not Started",
    "watched": "✅Watched",
}


def db():
    return sqlite3.connect(DB_PATH)


def normalize_name(name):
    return name.strip().lower()


def slugify(s):
    s = (s or "").lower().strip().replace(" ", "-")
    return "".join(ch for ch in s if ch.isalnum() or ch == "-")[:80]


def find_show(cur, name):
    rows = cur.execute(
        """
        SELECT s.id, COALESCE(m.official_name, s.name) AS name
        FROM shows s
        LEFT JOIN meta_tvmaze m ON m.show_id = s.id
        """
    ).fetchall()
    lname = normalize_name(name)
    exact = [r for r in rows if normalize_name(r[1]) == lname]
    if len(exact) == 1:
        return exact[0], []
    contains = [r for r in rows if lname in normalize_name(r[1])]
    if len(contains) == 1:
        return contains[0], []
    return None, contains[:5]


def cmd_list(status_key):
    conn = db()
    cur = conn.cursor()
    status = STATUS_MAP[status_key]
    rows = cur.execute(
        """
        SELECT COALESCE(m.official_name, s.name) AS name, s.season
        FROM shows s
        LEFT JOIN meta_tvmaze m ON m.show_id = s.id
        WHERE s.status = ?
        ORDER BY name
        """,
        (status,),
    ).fetchall()
    print(f"{status} — {len(rows)} shows")
    for name, season in rows[:15]:
        print(f"- {name} ({season})")
    if len(rows) > 15:
        print(f"…and {len(rows) - 15} more")


def cmd_recommend():
    subprocess.run(["python3", os.path.join(SCRIPTS_DIR, "recommend.py")], check=False)


def cmd_add(name):
    conn = db()
    cur = conn.cursor()
    existing, _ = find_show(cur, name)
    if existing:
        print(f"Already exists: {existing[1]}")
        return
    slug = slugify(name)
    cur.execute(
        "INSERT INTO shows (name, status, slug) VALUES (?, ?, ?)",
        (name.strip(), "🙈 Not Started", slug),
    )
    conn.commit()
    print(f"Added: {name.strip()} (Not Started)")


def cmd_search(name):
    q = urllib.parse.quote(name)
    url = f"https://api.tvmaze.com/search/shows?q={q}"
    try:
        with urllib.request.urlopen(url, timeout=8) as resp:
            results = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Search failed: {e}")
        return
    if not results:
        print("No results found.")
        return
    print(f"TVMaze results for \"{name}\":\n")
    for r in results[:5]:
        show = r.get("show", {})
        sname = show.get("name", "?")
        premiered = show.get("premiered", "?")
        year = premiered[:4] if premiered else "?"
        genres = ", ".join(show.get("genres", []) or []) or "—"
        status = show.get("status", "?")
        print(f"- {sname} ({year}) — {genres} [{status}]")


def cmd_episode(name, season, episode):
    conn = db()
    cur = conn.cursor()
    show, suggestions = find_show(cur, name)
    if not show:
        if suggestions:
            print("Multiple matches. Be more specific:")
            for _, n in suggestions:
                print(f"- {n}")
        else:
            print("No match found.")
        return
    cur.execute(
        "UPDATE shows SET current_season = ?, current_episode = ? WHERE id = ?",
        (season, episode, show[0]),
    )
    conn.commit()
    print(f"Updated progress: {show[1]} → S{season}E{episode}")


def _strip_html(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def cmd_recap(name, use_wiki=False):
    conn = db()
    cur = conn.cursor()
    show, suggestions = find_show(cur, name)
    if not show:
        if suggestions:
            print("Multiple matches. Be more specific:")
            for _, n in suggestions:
                print(f"- {n}")
        else:
            print("No match found.")
        return

    row = cur.execute(
        """
        SELECT s.current_season, s.current_episode, m.tvmaze_id, COALESCE(m.official_name, s.name)
        FROM shows s
        LEFT JOIN meta_tvmaze m ON m.show_id = s.id
        WHERE s.id = ?
        """,
        (show[0],),
    ).fetchone()

    current_season, current_episode, tvmaze_id, display_name = row
    if not current_season or not current_episode:
        print("Progress missing. Set with: tv episode <show> <SxE>")
        return
    if not tvmaze_id:
        print("TVMaze ID missing for this show. Run enrich_tvmaze.py first.")
        return

    url = f"https://api.tvmaze.com/shows/{tvmaze_id}/episodes"
    with urllib.request.urlopen(url, timeout=12) as resp:
        episodes = json.loads(resp.read().decode("utf-8"))

    seen = []
    for ep in episodes:
        s = ep.get("season")
        e = ep.get("number")
        if s is None or e is None:
            continue
        if s < current_season or (s == current_season and e <= current_episode):
            seen.append(ep)

    if not seen:
        print("No episode data found up to your current progress.")
        return

    seen.sort(key=lambda x: (x.get("season", 0), x.get("number", 0)))
    print(f"Recap: {display_name} (up to S{current_season}E{current_episode})")
    print(f"Episodes covered: {len(seen)}")
    print("Recent episodes:")
    for ep in seen[-5:]:
        s = ep.get("season")
        e = ep.get("number")
        title = ep.get("name")
        summary = _strip_html(ep.get("summary"))
        if summary:
            summary = summary[:200] + ("…" if len(summary) > 200 else "")
        print(f"- S{s}E{e} {title}: {summary}")

    if use_wiki and len(seen) < 3:
        q = urllib.parse.quote(display_name)
        wurl = f"https://en.wikipedia.org/api/rest_v1/page/summary/{q}"
        try:
            with urllib.request.urlopen(wurl, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            wiki = data.get("extract")
            if wiki:
                print("\nWikipedia summary (may include spoilers):")
                print(wiki)
        except Exception:
            pass


def cmd_update_status(action, name):
    conn = db()
    cur = conn.cursor()
    target_status = STATUS_MAP[action]
    show, suggestions = find_show(cur, name)
    if not show:
        if suggestions:
            print("Multiple matches. Be more specific:")
            for _, n in suggestions:
                print(f"- {n}")
        else:
            print("No match found.")
        return
    cur.execute("UPDATE shows SET status = ? WHERE id = ?", (target_status, show[0]))
    conn.commit()
    print(f"Updated: {show[1]} → {target_status}")


def cmd_season(name, season):
    conn = db()
    cur = conn.cursor()
    show, suggestions = find_show(cur, name)
    if not show:
        if suggestions:
            print("Multiple matches. Be more specific:")
            for _, n in suggestions:
                print(f"- {n}")
        else:
            print("No match found.")
        return
    cur.execute("UPDATE shows SET season = ? WHERE id = ?", (season, show[0]))
    conn.commit()
    print(f"Updated: {show[1]} → {season}")


def cmd_stats():
    conn = db()
    cur = conn.cursor()
    rows = cur.execute("SELECT status, COUNT(*) FROM shows GROUP BY status").fetchall()
    total = cur.execute("SELECT COUNT(*) FROM shows").fetchone()[0]
    print(f"Total shows: {total}")
    for status, count in rows:
        print(f"- {status}: {count}")


def main():
    if len(sys.argv) < 2:
        print("Usage: tv_cli.py <list|recommend|start|pause|finish|season|episode|recap|stats|add|search> ...")
        return
    cmd = sys.argv[1]
    if cmd == "list" and len(sys.argv) >= 3:
        cmd_list(sys.argv[2])
    elif cmd == "recommend":
        cmd_recommend()
    elif cmd == "start" and len(sys.argv) >= 3:
        cmd_update_status("watching", " ".join(sys.argv[2:]))
    elif cmd == "pause" and len(sys.argv) >= 3:
        cmd_update_status("paused", " ".join(sys.argv[2:]))
    elif cmd == "finish" and len(sys.argv) >= 3:
        cmd_update_status("watched", " ".join(sys.argv[2:]))
    elif cmd == "season" and len(sys.argv) >= 4:
        cmd_season(" ".join(sys.argv[2:-1]), sys.argv[-1])
    elif cmd == "episode" and len(sys.argv) >= 4:
        if "x" in sys.argv[-1].lower():
            s, e = sys.argv[-1].lower().split("x", 1)
            cmd_episode(" ".join(sys.argv[2:-1]), int(s), int(e))
        else:
            cmd_episode(" ".join(sys.argv[2:-2]), int(sys.argv[-2]), int(sys.argv[-1]))
    elif cmd == "recap" and len(sys.argv) >= 3:
        use_wiki = "--wiki" in sys.argv or "--wikipedia" in sys.argv
        args = [a for a in sys.argv[2:] if a not in ("--wiki", "--wikipedia")]
        cmd_recap(" ".join(args), use_wiki=use_wiki)
    elif cmd == "stats":
        cmd_stats()
    elif cmd == "add" and len(sys.argv) >= 3:
        cmd_add(" ".join(sys.argv[2:]))
    elif cmd == "search" and len(sys.argv) >= 3:
        cmd_search(" ".join(sys.argv[2:]))
    else:
        print("Invalid command or args.")


if __name__ == "__main__":
    main()
