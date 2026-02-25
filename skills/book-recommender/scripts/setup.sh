#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DATA_DIR="$SKILL_DIR/data"
STARTER="$SKILL_DIR/references/books-starter.json"
TARGET="$DATA_DIR/books.json"

mkdir -p "$DATA_DIR"

if [ -f "$TARGET" ]; then
  echo "books.json already exists at $TARGET"
else
  cp "$STARTER" "$TARGET"
  echo "Created $TARGET from starter template."
fi

echo ""
echo "Next steps:"
echo "  1. Edit $TARGET and replace the placeholder entries with your own books."
echo "  2. Ask your agent: \"What should I read next?\""
echo ""
echo "Schema fields per book:"
echo "  title, author, status (finished|reading|to-read|parked|abandoned),"
echo "  liked (true|false|null), rating (1-5|null), format, series, tags, notes"
