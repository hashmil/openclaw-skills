#!/usr/bin/env python3
import json, os, sqlite3, time, urllib.parse, urllib.request

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DB = os.path.join(SKILL_DIR, "data", "tv.sqlite")
DB_PATH = os.environ.get("TV_DB_PATH") or DEFAULT_DB


def tvmaze_search(name, retries=1):
    q = urllib.parse.quote(name)
    url = f"https://api.tvmaze.com/search/shows?q={q}"
    last_err = None
    for _ in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=6) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            last_err = e
            time.sleep(0.5)
    raise last_err


def pick_match(name, results):
    if not results:
        return None
    lname = name.strip().lower()
    for r in results:
        show = r.get("show", {})
        if show.get("name", "").strip().lower() == lname:
            return show
    return results[0].get("show")


def ensure_schema(conn):
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS meta_tvmaze (
          show_id INTEGER UNIQUE,
          tvmaze_id INTEGER,
          official_name TEXT,
          premiered TEXT,
          status TEXT,
          genres TEXT,
          summary TEXT,
          image TEXT,
          url TEXT,
          imdb_id TEXT
        )
        """
    )


def main():
    conn = sqlite3.connect(DB_PATH)
    ensure_schema(conn)
    cur = conn.cursor()

    rows = cur.execute(
        """
        SELECT s.id, s.name
        FROM shows s
        LEFT JOIN meta_tvmaze m ON m.show_id = s.id
        WHERE m.show_id IS NULL
        ORDER BY s.id
        """
    ).fetchall()

    updated = 0
    skipped = 0

    for idx, (show_id, name) in enumerate(rows, start=1):
        try:
            results = tvmaze_search(name)
            show = pick_match(name, results)
            if not show:
                skipped += 1
                continue
            img = show.get("image", {}) or {}
            externals = show.get("externals", {}) or {}

            cur.execute(
                """
                INSERT OR REPLACE INTO meta_tvmaze
                (show_id, tvmaze_id, official_name, premiered, status, genres, summary, image, url, imdb_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    show_id,
                    show.get("id"),
                    show.get("name"),
                    show.get("premiered"),
                    show.get("status"),
                    ",".join(show.get("genres", []) or []),
                    show.get("summary"),
                    img.get("original") or img.get("medium"),
                    show.get("url"),
                    externals.get("imdb"),
                ),
            )
            updated += 1
        except Exception:
            skipped += 1
        finally:
            if idx % 25 == 0:
                print(json.dumps({"progress": idx, "updated": updated, "skipped": skipped}), flush=True)
            time.sleep(0.1)

    conn.commit()
    print(json.dumps({"processed": len(rows), "updated": updated, "skipped": skipped}, indent=2))


if __name__ == "__main__":
    main()
