---
name: city-guide
description: Manage your personal City Lifestyle Database. Log places (with Google data), recommend spots based on weather/vibe, and track visits. Works for any city worldwide.
requires: ["goplaces"]
---

# City Guide Skill

> **⚠️ API Key Required:** This skill requires the `goplaces` skill and a Google Places API key. 
> Set up `goplaces` first and configure your API key via `goplaces auth` or environment variable.

Manage your personal city database — log places, get smart recommendations based on weather and vibe, and track your visits. Works for **any city worldwide**.

## Data Source
- **File:** `memory/city-tracker.json`
- **Helper:** `goplaces` CLI (for fetching address, rating, location data)

## First-Time Setup

If `memory/city-tracker.json` doesn't exist, the skill will create it with this structure:

```json
{
  "city": "Your City Name",
  "places": []
}
```

## Actions

### 1. Set Your City
**Trigger:** "Set city to [City Name]", "I'm in [City]", "Change city to [City]"
**Procedure:**
1. Create `memory/city-tracker.json` if it doesn't exist
2. Set the `city` field to the user's city
3. Confirm: "City set to [City]. Ready to log places!"

### 2. Log a New Place
**Trigger:** "Log [Place Name]", "I went to [Place]", "Add [Place]"
**Procedure:**
1. **Check City:** Ensure `memory/city-tracker.json` exists and has a city set. If not, ask the user to set their city first.
2. **Search:** Run `goplaces search "[Place Name] [City Name]" --limit 1 --json`.
3. **Verify:** Check if the result matches the user's intent.
4. **Read DB:** Read `memory/city-tracker.json`.
5. **Append:** Add a new entry to the `places` array using the **Schema** below.
    *   *Auto-fill:* Name, Google Place ID, Details (rating, address), Location.
    *   *Infer:* Area (from address), Type (from `types`), Environment (Indoor/Outdoor based on type/photos if available, or ask user).
    *   *Ask User:* specific notes, "Good for hot weather?" (if unclear), "Vibe".
5. **Save:** Write back to `memory/city-tracker.json`.

### 3. Log a Repeat Visit
**Trigger:** "We went back to [Place]", "Visited [Place] again"
**Procedure:**
1. **Find:** Locate the place in `memory/city-tracker.json`.
2. **Update:** Add a new object to the `visits` array with `date` (YYYY-MM-DD) and `notes`.

### 4. Recommend
**Trigger:** "Where should I go?", "Suggest a place for [activity]", "Dinner spot?"
**Procedure:**
1. **Analyze Context:**
    *   **Weather:** Hot/cold/rainy? User's preference for indoor/outdoor?
    *   **Vibe:** Chill, fancy, work, kids?
2. **Filter DB:** Query `memory/city-tracker.json`.
    *   *If hot weather:* Filter for `environment: "Indoor"` or `seasonality: "All Year"`.
    *   *If nice weather:* Prefer `environment: "Outdoor"`.
3. **Vibe Check (Consensus Search):**
    *   For the top candidate, run multiple targeted searches across different platforms:
        *   **Reddit:** "[Place] [City] reddit review tips"
        *   **Twitter/X:** "[Place] [City] twitter review experience"
        *   **TripAdvisor:** "[Place] [City] tripadvisor review"
        *   **Blogs:** "[Place] [City] blog review 2024"
    *   Look for: Parking chaos, best arrival times, hidden gems, "tourist trap" warnings, crowd levels, and recent experiences.
4. **Output:** Present 3 top options with their status (Visited/Wishlist) and a **"Pro Tip"** derived from the search.

## JSON Schema (Enforced)

```json
{
  "city": "string (City Name)",
  "places": [
    {
      "name": "string (Official Name)",
      "area": "string (e.g. Downtown, Waterfront)",
      "type": "string (Cafe, Beach, Mall, Dinner, Activity)",
      "environment": "Indoor ❄️ | Outdoor ☀️ | Hybrid 🌓",
      "seasonality": "All Year 🗓️ | Hot Weather 🛡️ | Cold Weather ❄️",
      "vibe": "comma-separated tags (e.g. work, date-night, loud, quiet)",
      "status": "Visited ✅ | Wishlist 📌",
      "google_place_id": "string",
      "details": {
        "rating": number,
        "address": "string",
        "location": { "lat": number, "lng": number }
      },
      "visits": [
        {
          "date": "YYYY-MM-DD",
          "notes": "User comments (parking, food, service)",
          "companions": ["names"]
        }
      ]
    }
  ]
}
```

## Nuance Guide
- **Hot Weather Safe:** Malls, heavily AC'd cafes, indoor play areas.
- **Cold Weather Only:** Outdoor terraces, beaches (in cold climates), open-air markets.
- **Parking:** Always note if parking is "Valet only" or "Easy".

## Examples

**Setting up:**
- "Set my city to Dubai"
- "I'm in London now"

**Logging places:**
- "Log Black Tap"
- "Add The Shard to my wishlist"
- "I visited Dubai Mall yesterday"

**Getting recommendations:**
- "Where should I go for dinner?"
- "Suggest a cafe for working"
- "It's raining, where's good indoors?"
