#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DATA_DIR="$SKILL_DIR/data"

mkdir -p "$DATA_DIR"

if [ -f "$DATA_DIR/tv.sqlite" ]; then
  echo "Database already exists at $DATA_DIR/tv.sqlite"
else
  sqlite3 "$DATA_DIR/tv.sqlite" < "$SKILL_DIR/references/schema.sql"
  echo "Database created at $DATA_DIR/tv.sqlite"
fi

echo ""
echo "Next steps:"
echo "  Add a show:        python3 $SCRIPT_DIR/tv_cli.py add \"Breaking Bad\""
echo "  Search TVMaze:     python3 $SCRIPT_DIR/tv_cli.py search \"Breaking Bad\""
echo "  Enrich metadata:   python3 $SCRIPT_DIR/enrich_tvmaze.py"
echo "  View stats:        python3 $SCRIPT_DIR/tv_cli.py stats"
