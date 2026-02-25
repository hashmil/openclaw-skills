---
name: book-recommender
description: Spoiler-free book recommendations with reading order, cover images, and a JSON-based reading tracker.
---

# Book Recommender

Recommend books and series (spoiler-free), including clear reading order for series, brief neutral content notes, and small actionable shortlists (3-6 picks) with an obvious next step.

Use for: book recommendations, what-to-read-next, mood-based picks (sci-fi/fantasy/romance/thriller), series reading order questions, and micro reading plans.

## Core rule

Before making recommendations, **read and follow** `references/system-prompt.md` (treat it as the governing system prompt for this task).

Also load the books database and treat it as the **source of truth** for:
- what the user has read / is reading / has parked
- likes/dislikes and notes
- avoiding accidental repeat recommendations

### Database location

The books database (`books.json`) is resolved in this order:
1. `BOOKS_JSON_PATH` environment variable (if set)
2. `books.json` in the agent's workspace directory
3. `data/books.json` relative to this skill directory

## Workflow

1. Load `books.json` and quickly infer: recent reads, current status, and hard avoids.
2. If the user gave a mood/constraint (genre, vibes, length, standalone vs series, content tolerance): proceed.
3. If not, ask **one** clarifying question (use the default one from the prompt).
4. Produce output using the prompt's **Recommendation Algorithm** + **Output Format**.
   - Ensure each title includes a **Cover:** direct image URL line (prefer Open Library ISBN cover URLs).
   - Avoid recommending anything already marked `finished`/`reading`/`parked`/`abandoned` unless the user explicitly asks for a re-read/recap.

## Metadata, covers, and accuracy

When recommending a specific title, prefer to attach **a cover image URL** and validate metadata (title/author/series order) against a public source.

**Primary source (no key): Open Library**
- Search: `https://openlibrary.org/search.json?title=<TITLE>&author=<AUTHOR>`
- Pick the best match using: exact/near title match + author match; prefer hits with ISBN.
- Cover images:
  - Prefer ISBN: `https://covers.openlibrary.org/b/isbn/<ISBN>-L.jpg`
  - Else OLID: `https://covers.openlibrary.org/b/olid/<COVER_OLID>-L.jpg`
  - If the cover 404s or looks wrong, try `-M` or choose the next-best search hit.

**Fallback (if Open Library is missing/ambiguous): Google Books**
- Search: `https://www.googleapis.com/books/v1/volumes?q=intitle:<TITLE>+inauthor:<AUTHOR>`
- Use `volumeInfo.imageLinks.thumbnail`/`smallThumbnail` and cross-check author.

**Accuracy rules**
- Never invent ISBNs, publication years, page counts, or series numbering.
- If uncertain about edition/order: say so briefly and present the safest statement (e.g., "Start with Book 1: ...").

## Safety / quality checks

- No spoilers (including "reveals" or endgame stakes).
- If series: explicitly label **Book 1** and give the reading order.
- Keep it tight: **one top pick** + **2-4 alternatives**.
- Include brief, neutral content notes.
- End with a single next step.
