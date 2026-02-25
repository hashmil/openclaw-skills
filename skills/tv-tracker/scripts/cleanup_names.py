#!/usr/bin/env python3
import os, sqlite3

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DB = os.path.join(SKILL_DIR, "data", "tv.sqlite")
DB_PATH = os.environ.get("TV_DB_PATH") or DEFAULT_DB


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    rows = cur.execute(
        """
        SELECT s.id, s.name, m.official_name
        FROM shows s
        JOIN meta_tvmaze m ON m.show_id = s.id
        WHERE m.official_name IS NOT NULL AND m.official_name != s.name
        """
    ).fetchall()

    for sid, old, new in rows:
        cur.execute("UPDATE shows SET name = ? WHERE id = ?", (new, sid))

    conn.commit()
    print({"updated": len(rows)})


if __name__ == "__main__":
    main()
