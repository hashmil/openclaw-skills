# 🧩 OpenClaw Skills

A collection of shareable skills for [OpenClaw](https://openclaw.com) agents.

> **One-line install** — copy a skill URL, paste it to your agent, say *"Install this skill"*. Done.

---

## Skills at a Glance

| | Skill | What it does | Requires |
|---|-------|-------------|----------|
| 📓 | [**wiki-journal**](skills/wiki-journal/) | Daily deep-research journaling with `[[wikilinks]]` | Web search (optional) |
| 🏙️ | [**city-guide**](skills/city-guide/) | Weather-smart city lifestyle guide for any city | `goplaces`, Google Places API |
| 🏜️ | [**dubai-guide**](skills/dubai-guide/) | Pre-configured Dubai guide with extreme-heat awareness | `goplaces`, Google Places API |
| 📺 | [**tv-tracker**](skills/tv-tracker/) | TV show tracking + recommendations via SQLite & TVMaze | Python 3.9+ |
| 📚 | [**book-recommender**](skills/book-recommender/) | Spoiler-free book recs with reading order & covers | — |

---

## 📓 Wiki Journal

Daily autonomous journaling — your agent picks a topic, researches it deeply, and writes a structured entry with `[[wikilinks]]` connecting concepts. Over time, the journal becomes an interconnected knowledge base.

- 🔗 Autonomous topic selection following wikilink trails from previous entries
- 🔍 Deep research via web search + training knowledge
- 🧱 Structured entries: core argument, reflection, implications, open questions
- 🗂️ Compatible with Obsidian, Logseq, or plain markdown
- ⚙️ Configurable topics, length, tone via optional `config.md`
- ⏰ Daily cron job with one-command setup

<details>
<summary><strong>Install</strong></summary>

```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/wiki-journal/SKILL.md
```
</details>

[Full docs →](skills/wiki-journal/README.md)

---

## 🏙️ City Guide

Generic city lifestyle guide — customize for your own city. Tracks restaurants, cafes, activities with weather-adaptive recommendations.

- 🌍 Set any city worldwide as your base
- 🌦️ Weather-adaptive recommendations (hot/cold/rain/snow)
- 💬 Vibe checks via Reddit, TripAdvisor, blogs
- ⭐ Google Reviews integration
- 📄 Auto-creates database file if missing

<details>
<summary><strong>Install</strong></summary>

```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/city-guide/SKILL.md
```
</details>

[View SKILL.md →](skills/city-guide/SKILL.md)

---

## 🏜️ Dubai Guide

Pre-configured version of City Guide optimized for Dubai's extreme climate. Ready to use for Dubai residents and visitors.

- ☀️ Pre-configured for Dubai's climate (Summer Safe, Winter Only)
- 🌡️ Seasonal recommendations based on extreme heat
- 📍 Local area knowledge (Jumeirah, DIFC, Marina, etc.)

<details>
<summary><strong>Install</strong></summary>

```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/dubai-guide/SKILL.md
```
</details>

[View SKILL.md →](skills/dubai-guide/SKILL.md)

---

## 📺 TV Tracker

Track TV shows, get recommendations, and manage your watchlist. Uses a local SQLite database enriched with metadata from [TVMaze](https://www.tvmaze.com/api).

- 🎬 Track shows by status: Watching, Paused, Not Started, Watched
- 🎯 Smart recommendations based on interest ratings and metadata
- 🔄 TVMaze integration for official names, genres, images, and synopses
- 📍 Episode progress tracking with spoiler-safe recaps
- 💬 Natural language command routing
- 📦 Zero dependencies beyond Python 3.9+ standard library

<details>
<summary><strong>Install</strong></summary>

```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/tv-tracker/SKILL.md
```
</details>

[Full docs →](skills/tv-tracker/README.md)

---

## 📚 Book Recommender

Spoiler-free book recommendations with reading order verification, cover images, and a simple JSON-based reading tracker.

- 🚫 Zero spoilers — ever
- 📖 Series reading order always included
- 🖼️ Cover images from Open Library / Google Books
- 🎭 Mood-based grouping (sci-fi, fantasy, romance, thriller…)
- 📅 Micro reading plans (7-day, 20–30 min/day)
- 🧠 Taste inference from your reading history — no manual profile needed

<details>
<summary><strong>Install</strong></summary>

```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/book-recommender/SKILL.md
```
</details>

[Full docs →](skills/book-recommender/README.md)

---

## 🛠️ Install Methods

### 1. Paste the URL (easiest)

Copy a skill's install URL from above and paste it in a message to your OpenClaw agent. Tell it to install the skill. Done.

### 2. Clone and copy

```bash
git clone https://github.com/hashmil/openclaw-skills.git
cp -r openclaw-skills/skills/<skill-name>/ ~/.openclaw/skills/<skill-name>/
```

Pick the skills you want — no need to install all of them.

---

## 📄 License

MIT — See [LICENSE](LICENSE) for details.
