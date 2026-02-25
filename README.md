# OpenClaw Skills

A collection of shareable [OpenClaw](https://openclaw.com) skills.

---

## Skills

| Skill | Description | Requirements |
|-------|-------------|--------------|
| [**wiki-journal**](skills/wiki-journal/) | Daily journaling with deep Wikipedia/encyclopedia research. Builds a wikilinked knowledge graph over time. | Web search (optional) |
| [**city-guide**](skills/city-guide/) | Customizable city lifestyle guide. Track places, get weather-smart recommendations for any city. | `goplaces` skill, Google Places API key |
| [**dubai-guide**](skills/dubai-guide/) | Pre-configured Dubai lifestyle database with extreme-heat awareness and local area knowledge. | `goplaces` skill, Google Places API key |

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

```bash
cp -r skills/wiki-journal/ ~/.openclaw/skills/wiki-journal/
bash ~/.openclaw/skills/wiki-journal/scripts/setup.sh
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

```bash
cp -r skills/city-guide/ ~/.openclaw/skills/city-guide/
```

[View SKILL.md →](skills/city-guide/SKILL.md)

---

### Dubai Guide

Pre-configured version of City Guide optimized for Dubai's extreme climate. Ready to use for Dubai residents and visitors.

**Features:**
- Pre-configured for Dubai's climate (Summer Safe, Winter Only)
- Seasonal recommendations based on extreme heat
- Local area knowledge (Jumeirah, DIFC, Marina, etc.)

```bash
cp -r skills/dubai-guide/ ~/.openclaw/skills/dubai-guide/
```

[View SKILL.md →](skills/dubai-guide/SKILL.md)

---

## How to Install

### Quick Install

1. Copy the raw URL to a skill's `SKILL.md`
2. Paste it in a message to your OpenClaw bot
3. Say: *"Install this skill"*

**Raw URLs:**
- **Wiki Journal:** `https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/wiki-journal/SKILL.md`
- **City Guide:** `https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/city-guide/SKILL.md`
- **Dubai Guide:** `https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/dubai-guide/SKILL.md`

### Manual Install

```bash
git clone https://github.com/hashmil/openclaw-skills.git
cp -r openclaw-skills/skills/<skill-name>/ ~/.openclaw/skills/<skill-name>/
```

---

## License

MIT — See [LICENSE](LICENSE) for details.
