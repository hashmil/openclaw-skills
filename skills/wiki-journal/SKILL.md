---
name: wiki-journal
version: 1.0.0
description: Daily journaling with deep Wikipedia/encyclopedia research. Builds a wikilinked knowledge graph over time.
---

# Wiki-Journal Skill

Daily intellectual enrichment through structured study of Wikipedia, Stanford Encyclopedia of Philosophy, and other knowledge sources.

## Purpose

Transform journaling from event-logging into a **knowledge engine**:
- Deep study of topics across any domain
- [[Wikilinked]] concepts creating an interconnected knowledge graph
- Applied reflection on your own projects and workflows
- Deeper implications and philosophical connections
- A growing shared vocabulary between you and your agent

## Before Writing

### 1. Read Context

Before choosing a topic or writing anything:

1. **Read `MEMORY.md`** in the agent's workspace — understand current projects, interests, active threads
2. **Scan `memory/`** files — check for recent activity, themes, notable events
3. **Read the last 3-5 journal entries** (in `journal/YYYY/MM/`) — identify the wikilink trail, avoid repeats, find threads to follow
4. **Check for `config.md`** alongside this SKILL.md — if it exists, read it for topic preferences, excluded topics, tone, and length settings

### 2. Cold Start

If there are no previous journal entries (first run):
- Pick any topic that genuinely interests you from the default domains below
- No need to reference previous studies — just begin
- Mention this is the inaugural entry

## Topic Selection

**Autonomous choice** based on:
- Connections to previous studies (follow the [[wikilink]] trail from "Connections to Explore")
- Current relevance to projects and interests found in MEMORY.md
- What sparks genuine curiosity
- Seasonal or timely appropriateness

**Default topic domains** (override via `config.md` if present):
- Philosophy: phenomenology, existentialism, philosophy of mind, ethics, epistemology
- Cognitive Science: embodied cognition, distributed cognition, situated learning
- Science: emergence, complexity, information theory, thermodynamics
- Technology: computing history, internet architecture, cryptography, AI
- Mathematics: foundations, logic, topology, game theory
- History: intellectual movements, pivotal figures, turning points
- Art & Culture: movements, aesthetics, media theory, architecture
- Systems Thinking: cybernetics, feedback loops, design patterns

## Research Depth

**Don't summarize — interrogate:**
1. What is the core claim or idea?
2. What are the implications — stated and unstated?
3. How does this challenge common assumptions?
4. What do critics say? What are the unresolved tensions?
5. What connections exist to other concepts you've studied?

**Sources (in order of preference):**
- Wikipedia (reliable on academic topics, good for overview and citations)
- Stanford Encyclopedia of Philosophy (gold standard for philosophy)
- Internet Encyclopedia of Philosophy
- Academic sources where accessible via web search

**Quality check:**
- Look for citations in the source material
- Check for controversy or disputed claims — note them
- When a source is thin, follow references to primary sources
- If `web_search` is unavailable, draw from training knowledge and note: *"Sources not independently verified this session."*

## Entry Structure

Write the entry to: `journal/YYYY/MM/DD.md` (relative to the agent's workspace).
Create year/month directories if they don't exist.

```markdown
# <Weekday>, <Month> <Day>, <Year>

## Study: [[Topic Name]]

*Source citation(s) — author, title, year*

---

### The Core Argument
[Deep dive into the idea. Not a surface summary — explain what makes this concept
significant, what problem it solves, what shift in thinking it represents.
Include historical context, key figures, and the intellectual lineage.]

### Applied Reflection
[How does this concept connect to your current projects, workflows, or interests?
Read MEMORY.md for context. Be specific — reference actual tools, habits, or
systems. If nothing connects directly, reflect on how the concept might
reframe how you approach problems generally.]

### Deeper Implications
[Broader philosophical, ethical, or societal implications. What does this idea
mean beyond its original domain? How does it challenge assumptions?
What paradoxes or tensions does it surface?]

### Quotes to Keep
[2-5 significant quotations with attribution. Choose quotes that capture
the essence, provoke thought, or crystallize a difficult idea.]

### Connections to Explore
[List of [[wikilinked]] concepts for future study. These form the knowledge
graph — each is a potential future entry. Aim for 4-8 connections spanning
different domains.]

### The Open Question
[What remains unresolved? What tension, paradox, or question does this study
leave you with? This should be genuinely open — not a rhetorical flourish
but an honest edge of understanding.]

---

*Sources:*
- [Full citation 1]
- [Full citation 2]
- ...
```

## Wikilinking Convention

**Format:** `[[Concept Name]]` on first mention in an entry, plain text thereafter.

**Link types:**
- People: [[Andy Clark]], [[Ada Lovelace]]
- Concepts: [[Extended Mind]], [[Emergence]]
- Works: [[Godel, Escher, Bach]], [[Principia Mathematica]]
- Movements: [[Phenomenology]], [[Vienna Circle]]

**Purpose:**
- Creates a knowledge graph over time
- Shows concept clusters and thematic arcs
- Enables "follow the link" topic selection
- Compatible with Obsidian, Logseq, and other tools (but doesn't require them)

## Writing Quality

**Aim for:**
- Not just "what is X" but "why X matters"
- Genuine engagement — write as if you're working through the idea, not reporting on it
- Questions raised, not just answers found
- Connections to previous studies where they exist naturally
- Intellectual honesty — note when you're uncertain or when a topic is contested

**Avoid:**
- Dry encyclopedia summaries
- Forced connections that don't genuinely illuminate
- Padding or filler
- Jargon without explanation

**Default length:** ~1500-2500 words (override via `config.md`).

## After Writing

1. **Write the entry** to `journal/YYYY/MM/DD.md`
2. That's it — no git commit, no push, no channel posting. Just the file.

If the cron job has delivery configured, the output will be posted automatically.

---

*This skill transforms journaling from logging into learning.*
