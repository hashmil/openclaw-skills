# Book Recommender

Spoiler-free book recommendations with reading order verification, cover images, and a simple JSON-based reading tracker.

## Features

- Spoiler-free recommendations with content notes
- Series reading order always included
- Cover images from Open Library / Google Books
- Mood-based grouping (sci-fi, fantasy, romance, thriller, etc.)
- Micro reading plans (7-day, 20-30 min/day)
- JSON database for tracking what you've read, liked, and want to read
- Taste inference from your reading history — no manual profile needed

## Install

Copy this URL and paste it to your OpenClaw agent — *"Install this skill"*

```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/book-recommender/SKILL.md
```

Or clone and copy:

```bash
git clone https://github.com/hashmil/openclaw-skills.git
cp -r openclaw-skills/skills/book-recommender/ ~/.openclaw/skills/book-recommender/
```

## Setup

Run the setup script to create a starter database:

```bash
bash scripts/setup.sh
```

This copies `references/books-starter.json` to `data/books.json` with two placeholder entries. Replace them with your own books.

## Usage

Once installed, just talk to your agent:

- "What should I read next?"
- "Recommend something sci-fi"
- "I'm in the mood for fantasy with magic systems"
- "What order do I read Mistborn?"
- "Give me a 7-day reading plan for a standalone thriller"

The agent reads your `books.json` to understand your taste and avoids recommending books you've already read.

## Database Format

`books.json` is a simple JSON file:

```json
{
  "schemaVersion": 1,
  "updatedAt": "2026-01-15T10:00:00Z",
  "books": [
    {
      "title": "The Martian",
      "author": "Andy Weir",
      "status": "finished",
      "liked": true,
      "rating": 5,
      "format": "kindle",
      "series": null,
      "started": "2025-12-01",
      "finished": "2025-12-10",
      "tags": ["sci-fi", "survival"],
      "notes": "Loved the problem-solving."
    }
  ]
}
```

### Status values

| Status | Meaning |
|--------|---------|
| `finished` | Completed reading |
| `reading` | Currently reading |
| `to-read` | Want to read |
| `parked` | Started but set aside |
| `abandoned` | Won't finish |

## Custom Database Path

Set `BOOKS_JSON_PATH` to use a database in a different location:

```bash
export BOOKS_JSON_PATH=/path/to/my/books.json
```

## License

MIT
