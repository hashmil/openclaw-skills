# wiki-journal

Daily journaling with deep Wikipedia/encyclopedia research. Builds a wikilinked knowledge graph over time.

Your agent picks a topic each day, researches it using web search and training knowledge, then writes a structured journal entry with [[wikilinks]] connecting concepts across entries. Over weeks and months, the journal becomes an interconnected knowledge base.

## Install

Copy the skill folder into your OpenClaw skills directory:

```bash
# From this repo
cp -r skills/wiki-journal/ ~/.openclaw/skills/wiki-journal/
```

Or clone the whole repo and copy:

```bash
git clone https://github.com/hashmil/openclaw-skills.git
cp -r openclaw-skills/skills/wiki-journal/ ~/.openclaw/skills/wiki-journal/
```

## Setup

Run the setup script to create the journal directory and register a daily cron job:

```bash
bash ~/.openclaw/skills/wiki-journal/scripts/setup.sh
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `--agent <id>` | Which agent runs the journal | default agent |
| `--hour <0-23>` | Hour to run (local time) | 22 |
| `--minute <0-59>` | Minute to run | 0 |
| `--tz <timezone>` | IANA timezone (e.g. `America/New_York`) | system timezone |
| `--timeout <sec>` | Max seconds per entry | 300 |
| `--thinking <level>` | `off\|minimal\|low\|medium\|high` | medium |

### Examples

```bash
# Default: runs at 10pm system time on default agent
bash ~/.openclaw/skills/wiki-journal/scripts/setup.sh

# Specific agent at 9pm Eastern
bash ~/.openclaw/skills/wiki-journal/scripts/setup.sh --agent main --hour 21 --tz America/New_York

# Quick entries with minimal thinking
bash ~/.openclaw/skills/wiki-journal/scripts/setup.sh --timeout 120 --thinking low
```

No model is hardcoded — the cron job uses whatever model your agent is configured with.

## Customize Topics

Copy the template and edit to taste:

```bash
cp ~/.openclaw/skills/wiki-journal/config.md.template ~/.openclaw/skills/wiki-journal/config.md
```

In `config.md` you can:
- **Add/remove topic domains** — focus on what interests you
- **Queue specific topics** — the agent picks from these first
- **Exclude topics** — skip domains or specific subjects
- **Set entry length** — short (~800w), medium (~2000w), or long (~4000w)
- **Set tone** — academic, conversational, or exploratory
- **Add a sign-off** — optional line at the end of each entry

If no `config.md` exists, the agent uses broad defaults from SKILL.md.

## Where Entries Go

Entries are written to `journal/YYYY/MM/DD.md` inside the agent's workspace:

```
~/.openclaw/workspace-<agent>/journal/
  2026/
    03/
      04.md    # March 4 entry
      05.md    # March 5 entry
```

Entries are local files only — no git commits, no pushes, no channel posting by default.

## How It Works

1. The cron job fires daily and tells the agent to read `SKILL.md`
2. The agent reads your `MEMORY.md`, recent memory files, and previous journal entries
3. It picks a topic — following [[wikilink]] trails from previous entries or choosing based on your interests
4. It researches the topic via web search (or training knowledge if search is unavailable)
5. It writes a structured entry with citations, applied reflections, and links to future topics
6. The entry is saved as a markdown file

Updating `SKILL.md` or `config.md` immediately changes behavior — no need to re-register the cron job.

## Wikilinks

Entries use `[[Concept Name]]` format on first mention. These are compatible with:
- **Obsidian** — shows up as internal links, visible in graph view
- **Logseq** — works natively
- **Plain markdown** — renders as text with brackets, still readable

You don't need any of these tools. The wikilinks work as a lightweight knowledge graph in plain text.

## Uninstall

```bash
# Remove the cron job
openclaw cron remove wiki-journal-daily

# Remove the skill (keeps your journal entries)
rm -rf ~/.openclaw/skills/wiki-journal/

# Optionally remove journal entries
rm -rf ~/.openclaw/workspace-<agent>/journal/
```
