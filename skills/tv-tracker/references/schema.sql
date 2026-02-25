PRAGMA journal_mode=WAL;

CREATE TABLE IF NOT EXISTS shows (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  status TEXT DEFAULT '🙈 Not Started',
  season TEXT,
  interest TEXT,
  show_status TEXT,
  current_season INTEGER,
  current_episode INTEGER,
  slug TEXT,
  notes TEXT,
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS show_genres (
  show_id INTEGER REFERENCES shows(id),
  genre TEXT,
  UNIQUE(show_id, genre)
);

CREATE TABLE IF NOT EXISTS show_platforms (
  show_id INTEGER REFERENCES shows(id),
  platform TEXT,
  UNIQUE(show_id, platform)
);

CREATE TABLE IF NOT EXISTS meta_tvmaze (
  show_id INTEGER UNIQUE REFERENCES shows(id),
  tvmaze_id INTEGER,
  official_name TEXT,
  premiered TEXT,
  status TEXT,
  genres TEXT,
  summary TEXT,
  image TEXT,
  url TEXT,
  imdb_id TEXT
);
