# OpenClaw Skills by Hash

A collection of custom OpenClaw skills for the community.

## Skills

### City Guide
Manage your personal City Lifestyle Database — log places, get recommendations based on weather/vibe, and track visits. **Works for any city worldwide!**

**Quick Install:**
1. Copy this URL: `https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/city-guide/SKILL.md`
2. Paste it in a message to your OpenClaw bot and say "Install this skill"

**Or Manual Install:**
```bash
git clone https://github.com/hashmil/openclaw-skills.git
cp -r openclaw-skills/skills/city-guide ~/.openclaw/skills/
```

**Requirements:**
- `goplaces` skill (Google Places integration)
- Google Places API key

**Features:**
- Set any city worldwide as your base
- Auto-creates database file if missing
- Log new places with auto-fetched Google data
- Track repeat visits with notes
- Smart recommendations based on weather and vibe
- JSON-based local database

[View Full Skill Docs →](skills/city-guide/SKILL.md)

---

## Installation

### Method 1: Quick Install (Recommended)
Copy the raw URL to any skill's `SKILL.md` file and paste it in a message to your OpenClaw bot:

```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/city-guide/SKILL.md
```

Then say: *"Install this skill for me"*

### Method 2: Manual Install

1. Clone this repo:
```bash
git clone https://github.com/hashmil/openclaw-skills.git
```

2. Copy the skill folder to your OpenClaw skills directory:
```bash
cp -r openclaw-skills/skills/city-guide ~/.openclaw/skills/
```

3. Install any required dependencies (see individual skill READMEs)

---

## Contributing

Feel free to submit PRs or issues. These skills are provided as-is for the community.

---

## License

MIT License - See [LICENSE](LICENSE) for details.
