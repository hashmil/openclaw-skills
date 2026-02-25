# TV Tracker

Track TV shows, get recommendations, and manage your watchlist. Uses a local SQLite database enriched with metadata from [TVMaze](https://www.tvmaze.com/api).

## Features

- Track shows by status: Watching, Paused, Not Started, Watched
- Smart recommendations based on interest ratings and show metadata
- TVMaze integration for official names, genres, images, and synopses
- Episode progress tracking with spoiler-safe recaps
- Natural language command routing
- Zero dependencies beyond Python 3.9+ standard library

## Install

Copy this URL and paste it to your OpenClaw agent — *"Install this skill"*

```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/tv-tracker/SKILL.md
```

Or clone and copy:

```bash
git clone https://github.com/hashmil/openclaw-skills.git
cp -r openclaw-skills/skills/tv-tracker/ ~/.openclaw/skills/tv-tracker/
```

## Setup

Run the setup script to create an empty database:

```bash
bash scripts/setup.sh
```

This creates `data/tv.sqlite` with the schema ready to go.

## Usage

### Add shows

```bash
python3 scripts/tv_cli.py add "Breaking Bad"
python3 scripts/tv_cli.py add "The Bear"
python3 scripts/tv_cli.py search "Severance"   # search TVMaze first
```

### Enrich with TVMaze metadata

```bash
python3 scripts/enrich_tvmaze.py    # fetches metadata for all unenriched shows
python3 scripts/cleanup_names.py    # aligns names with TVMaze official names
```

### Track progress

```bash
python3 scripts/tv_cli.py start "Breaking Bad"
python3 scripts/tv_cli.py episode "Breaking Bad" 2x05
python3 scripts/tv_cli.py season "Breaking Bad" "Season 3"
python3 scripts/tv_cli.py pause "Breaking Bad"
python3 scripts/tv_cli.py finish "Breaking Bad"
```

### Get recommendations and recaps

```bash
python3 scripts/tv_cli.py recommend
python3 scripts/tv_cli.py recap "Breaking Bad"
python3 scripts/tv_cli.py recap "Breaking Bad" --wiki
python3 scripts/tv_cli.py stats
```

### Natural language routing

```bash
python3 scripts/tv_router.py "what should I watch?"
python3 scripts/tv_router.py "I finished The Sopranos"
python3 scripts/tv_router.py "add Severance"
```

## Database Schema

See [`references/schema.sql`](references/schema.sql) for the full schema. Key tables:

- **shows** — name, status, season, interest rating, episode progress
- **show_genres** / **show_platforms** — many-to-many tags
- **meta_tvmaze** — cached TVMaze metadata (official name, premiered, genres, summary, image, IMDb ID)

## Custom Database Path

Set `TV_DB_PATH` to use a database in a different location:

```bash
export TV_DB_PATH=/path/to/my/tv.sqlite
```

## License

MIT
