#!/usr/bin/env python3
import os, sqlite3, re

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DB = os.path.join(SKILL_DIR, "data", "tv.sqlite")
DB_PATH = os.environ.get("TV_DB_PATH") or DEFAULT_DB

INTEREST_SCORE = {
    "★★★★★": 5,
    "★★★★": 4,
    "★★★": 3,
    "★★": 2,
    "★": 1,
}


def strip_html(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def main(limit=10):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    watching = cur.execute(
        "SELECT COUNT(*) FROM shows WHERE status = '👁Watching'"
    ).fetchone()[0]

    rows = cur.execute(
        """
        SELECT s.id, COALESCE(m.official_name, s.name) as name, s.status, s.season, s.interest, s.show_status,
               m.genres, m.premiered, m.status as m_status, m.image, m.summary
        FROM shows s
        LEFT JOIN meta_tvmaze m ON m.show_id = s.id
        WHERE s.status IN ('🙈 Not Started', '⏸Paused')
        ORDER BY s.id
        """
    ).fetchall()

    recs = []
    for r in rows:
        (sid, name, status, season, interest, show_status, genres, premiered, m_status, image, summary) = r
        score = 0
        score += INTEREST_SCORE.get(interest, 0) * 10
        if season == "Limited Series":
            score += 8
        if m_status == "Ended":
            score += 2
        if watching == 0:
            score += 5
        synopsis = strip_html(summary)
        if synopsis and len(synopsis) > 150:
            synopsis = synopsis[:150] + "…"
        recs.append({
            "id": sid,
            "name": name,
            "status": status,
            "season": season,
            "interest": interest,
            "show_status": show_status,
            "genres": genres.split(",") if genres else [],
            "premiered": premiered,
            "score": score,
            "image": image,
            "synopsis": synopsis,
        })

    recs.sort(key=lambda x: x["score"], reverse=True)
    out = recs[:limit]
    print(f"Watching now: {watching}")
    print("Top picks:\n")
    for r in out:
        season = r.get("season") or ""
        interest = r.get("interest") or ""
        synopsis = r.get("synopsis") or ""
        image = r.get("image") or ""
        print(f"**{r['name']}** {season} {interest}")
        if synopsis:
            print(f"> {synopsis}")
        if image:
            print(f"{image}")
        print()


if __name__ == "__main__":
    main()
