# OpenClaw Skills by Hash

A collection of custom OpenClaw skills for the community.

## Skills

### 🌴 Dubai Guide (Pre-configured)
My personal Dubai lifestyle database — optimized for Dubai's extreme weather patterns.

**Best for:** Dubai residents/visitors who want ready-to-use recommendations.

**Features:**
- Pre-configured for Dubai's climate (Summer Safe 🛡️, Winter Only ❄️)
- Seasonal recommendations based on Dubai's extreme heat
- Local area knowledge (Jumeirah, DIFC, Marina, etc.)

**Quick Install:**
```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/dubai-guide/SKILL.md
```

[View Skill Docs →](skills/dubai-guide/SKILL.md)

---

### 🌍 City Guide (Customizable)
Generic city guide — customize for your own city! Works for any city worldwide.

**Best for:** Users who want to track places in their own city (London, NYC, Tokyo, etc.)

**Features:**
- Set any city worldwide as your base
- Auto-creates database file if missing
- Weather-adaptive recommendations (hot/cold weather)
- Fully customizable for your local climate

**Quick Install:**
```
https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/city-guide/SKILL.md
```

[View Skill Docs →](skills/city-guide/SKILL.md)

---

## How to Install

### Method 1: Quick Install (Easiest)
1. Copy the raw URL to the skill you want:
   - **Dubai Guide:** `https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/dubai-guide/SKILL.md`
   - **City Guide:** `https://raw.githubusercontent.com/hashmil/openclaw-skills/master/skills/city-guide/SKILL.md`

2. Paste it in a message to your OpenClaw bot

3. Say: *"Install this skill"*

### Method 2: Manual Install

1. Clone this repo:
```bash
git clone https://github.com/hashmil/openclaw-skills.git
```

2. Copy the skill folder to your OpenClaw skills directory:
```bash
# For Dubai Guide
cp -r openclaw-skills/skills/dubai-guide ~/.openclaw/skills/

# For City Guide
cp -r openclaw-skills/skills/city-guide ~/.openclaw/skills/
```

---

## Requirements

Both skills require:
- `goplaces` skill (Google Places integration)
- Google Places API key

Set up `goplaces` first, then configure your API key.

---

## Contributing

Feel free to submit PRs or issues. These skills are provided as-is for the community.

---

## License

MIT License - See [LICENSE](LICENSE) for details.
