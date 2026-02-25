---
name: tv-tracker
description: TV show tracking and recommendations backed by a local SQLite database and TVMaze metadata.
---

# TV Tracker

Track TV shows, get recommendations, and manage your watchlist using a local SQLite database enriched with TVMaze metadata.

## Database

The database location is resolved in this order:
1. `TV_DB_PATH` environment variable (if set)
2. `data/tv.sqlite` relative to this skill directory

## Commands

```
python3 scripts/tv_cli.py list watching
python3 scripts/tv_cli.py list paused
python3 scripts/tv_cli.py list not-started
python3 scripts/tv_cli.py recommend
python3 scripts/tv_cli.py start "Show Name"
python3 scripts/tv_cli.py pause "Show Name"
python3 scripts/tv_cli.py finish "Show Name"
python3 scripts/tv_cli.py season "Show Name" "Season 3"
python3 scripts/tv_cli.py episode "Show Name" 3x05
python3 scripts/tv_cli.py recap "Show Name"
python3 scripts/tv_cli.py recap "Show Name" --wiki
python3 scripts/tv_cli.py stats
python3 scripts/tv_cli.py add "Show Name"
python3 scripts/tv_cli.py search "Show Name"
```

## Natural language handling

Interpret common phrases and route via:
```
python3 scripts/tv_router.py "<message>"
```

### Examples
- "what should I watch?" -> recommend
- "show me paused shows" -> list paused
- "start The Sopranos" -> start
- "I finished The Sopranos" -> finish
- "set season 3 for The Bear" -> season
- "add Severance" -> add
- "search for Severance" -> search

## Output style
- Keep replies short (5-10 lines max)
- Avoid markdown tables in chat contexts
- Ask **one** clarifying question only if multiple matches

## Enrichment

After adding shows, enrich metadata from TVMaze:
```
python3 scripts/enrich_tvmaze.py
```

Align show names with TVMaze official names:
```
python3 scripts/cleanup_names.py
```

## Notes
- Uses TVMaze official names when available
- All scripts work with Python 3.9+ and the standard library (no pip dependencies)
- `uv run python` works as an alternative to `python3` if uv is installed
