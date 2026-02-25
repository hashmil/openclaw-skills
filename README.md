# OpenClaw Skills

A collection of shareable [OpenClaw](https://openclaw.com) skills.

---

## Skills

| Skill | Description | Requirements |
|-------|-------------|--------------|
| [**wiki-journal**](skills/wiki-journal/) | Daily journaling with deep Wikipedia/encyclopedia research. Builds a wikilinked knowledge graph over time. | Web search (optional) |
| [**city-guide**](skills/city-guide/) | Customizable city lifestyle guide. Track places, get weather-smart recommendations for any city. | `goplaces` skill, Google Places API key |
| [**dubai-guide**](skills/dubai-guide/) | Pre-configured Dubai lifestyle database with extreme-heat awareness and local area knowledge. | `goplaces` skill, Google Places API key |
| [**tv-tracker**](skills/tv-tracker/) | TV show tracking and recommendations with SQLite database and TVMaze metadata. | Python 3.9+, SQLite |
| [**book-recommender**](skills/book-recommender/) | Spoiler-free book recommendations with reading order and cover images. | None |

---

### Wiki Journal

Daily autonomous journaling — your agent picks a topic, researches it deeply, and writes a structured entry with `[[wikilinks]]` connecting concepts. Over time, the journal becomes an interconnected knowledge base.

**Features:**
- Autonomous topic selection following wikilink trails from previous entries
- Deep research via web search + training knowledge
- Structured entries: core argument, applied reflection, deeper implications, open questions
- `[[Wikilinks]]` compatible with Obsidian, Logseq, or plain markdown
- Configurable topics, length, tone via optional `config.md`
- Daily cron job with one-command setup

**Install:** Copy this URL and paste it to your agent — *"Install this skill"*
```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/wiki-journal/SKILL.md
```

[Full docs →](skills/wiki-journal/README.md)

---

### City Guide

Generic city lifestyle guide — customize for your own city. Tracks restaurants, cafes, activities with weather-adaptive recommendations.

**Features:**
- Set any city worldwide as your base
- Auto-creates database file if missing
- Weather-adaptive recommendations (hot/cold/rain/snow)
- Vibe checks via Reddit, TripAdvisor, blogs
- Google Reviews integration

**Install:** Copy this URL and paste it to your agent — *"Install this skill"*
```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/city-guide/SKILL.md
```

[View SKILL.md →](skills/city-guide/SKILL.md)

---

### Dubai Guide

Pre-configured version of City Guide optimized for Dubai's extreme climate. Ready to use for Dubai residents and visitors.

**Features:**
- Pre-configured for Dubai's climate (Summer Safe, Winter Only)
- Seasonal recommendations based on extreme heat
- Local area knowledge (Jumeirah, DIFC, Marina, etc.)

**Install:** Copy this URL and paste it to your agent — *"Install this skill"*
```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/dubai-guide/SKILL.md
```

[View SKILL.md →](skills/dubai-guide/SKILL.md)

---

### TV Tracker

Track TV shows, get recommendations, and manage your watchlist. Uses a local SQLite database enriched with metadata from TVMaze.

**Features:**
- Track shows by status: Watching, Paused, Not Started, Watched
- Smart recommendations based on interest ratings and metadata
- TVMaze integration for official names, genres, images, and synopses
- Episode progress tracking with spoiler-safe recaps
- Natural language command routing
- Zero dependencies beyond Python 3.9+ standard library

**Install:** Copy this URL and paste it to your agent — *"Install this skill"*
```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/tv-tracker/SKILL.md
```

[Full docs →](skills/tv-tracker/README.md)

---

### Book Recommender

Spoiler-free book recommendations with reading order verification, cover images, and a simple JSON-based reading tracker.

**Features:**
- Spoiler-free recommendations with content notes
- Series reading order always included
- Cover images from Open Library / Google Books
- Mood-based grouping (sci-fi, fantasy, romance, thriller, etc.)
- Micro reading plans (7-day, 20-30 min/day)
- Taste inference from your reading history

**Install:** Copy this URL and paste it to your agent — *"Install this skill"*
```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/book-recommender/SKILL.md
```

[Full docs →](skills/book-recommender/README.md)

---

## Install Methods

### 1. Paste the URL (Easiest)

Copy a skill's raw URL from above and paste it in a message to your OpenClaw agent. Tell it to install the skill. Done.

### 2. Clone and Copy

```bash
git clone https://github.com/hashmil/openclaw-skills.git
cp -r openclaw-skills/skills/<skill-name>/ ~/.openclaw/skills/<skill-name>/
```

Pick the skills you want — no need to install all of them.

---

## License

MIT — See [LICENSE](LICENSE) for details.
