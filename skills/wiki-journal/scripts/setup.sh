#!/usr/bin/env bash
set -euo pipefail

# wiki-journal setup — creates journal directory and registers cron job
# Usage: bash setup.sh [--agent <id>] [--hour <0-23>] [--minute <0-59>]
#                       [--tz <timezone>] [--timeout <sec>] [--thinking <level>]

# Defaults
AGENT_ID=""
HOUR=22
MINUTE=0
TZ=""
TIMEOUT=300
THINKING="medium"

# Parse flags
while [[ $# -gt 0 ]]; do
  case "$1" in
    --agent)   AGENT_ID="$2"; shift 2 ;;
    --hour)    HOUR="$2"; shift 2 ;;
    --minute)  MINUTE="$2"; shift 2 ;;
    --tz)      TZ="$2"; shift 2 ;;
    --timeout) TIMEOUT="$2"; shift 2 ;;
    --thinking) THINKING="$2"; shift 2 ;;
    -h|--help)
      echo "Usage: bash setup.sh [OPTIONS]"
      echo ""
      echo "Options:"
      echo "  --agent <id>       Agent to run the journal on (default: default agent)"
      echo "  --hour <0-23>      Hour to run daily (default: 22)"
      echo "  --minute <0-59>    Minute to run (default: 0)"
      echo "  --tz <timezone>    IANA timezone, e.g. America/New_York (default: system tz)"
      echo "  --timeout <sec>    Max seconds per entry (default: 300)"
      echo "  --thinking <level> off|minimal|low|medium|high (default: medium)"
      echo "  -h, --help         Show this help"
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      exit 1
      ;;
  esac
done

# Find openclaw binary
OPENCLAW_BIN=""
for candidate in openclaw "$HOME/.npm-global/bin/openclaw" /usr/local/bin/openclaw; do
  if command -v "$candidate" &>/dev/null || [[ -x "$candidate" ]]; then
    OPENCLAW_BIN="$candidate"
    break
  fi
done

if [[ -z "$OPENCLAW_BIN" ]]; then
  echo "Error: openclaw binary not found. Is OpenClaw installed?" >&2
  echo "  Install: npm install -g openclaw" >&2
  exit 1
fi

echo "Found openclaw: $OPENCLAW_BIN"

# Resolve skill directory (where this script lives)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
echo "Skill directory: $SKILL_DIR"

# Resolve the agent's workspace
if [[ -n "$AGENT_ID" ]]; then
  # Try to find agent workspace via openclaw config
  OPENCLAW_DIR="$(dirname "$(dirname "$SKILL_DIR")")"
  WORKSPACE_DIR="$OPENCLAW_DIR/workspace-$AGENT_ID"
  if [[ ! -d "$WORKSPACE_DIR" ]]; then
    echo "Warning: workspace-$AGENT_ID not found at $WORKSPACE_DIR"
    echo "Creating journal directory there anyway..."
  fi
else
  # Default agent — use workspace-main if it exists, otherwise first workspace found
  OPENCLAW_DIR="$(dirname "$(dirname "$SKILL_DIR")")"
  if [[ -d "$OPENCLAW_DIR/workspace-main" ]]; then
    WORKSPACE_DIR="$OPENCLAW_DIR/workspace-main"
    AGENT_ID="main"
  else
    # Look for any workspace-* directory
    WORKSPACE_DIR="$(find "$OPENCLAW_DIR" -maxdepth 1 -type d -name 'workspace-*' | head -1)"
    if [[ -z "$WORKSPACE_DIR" ]]; then
      echo "Error: No agent workspace found in $OPENCLAW_DIR" >&2
      exit 1
    fi
    AGENT_ID="$(basename "$WORKSPACE_DIR" | sed 's/workspace-//')"
  fi
fi

echo "Target agent: $AGENT_ID"
echo "Workspace: $WORKSPACE_DIR"

# Create journal directory
JOURNAL_DIR="$WORKSPACE_DIR/journal"
mkdir -p "$JOURNAL_DIR"
echo "Journal directory: $JOURNAL_DIR (created)"

# Detect system timezone if not specified
if [[ -z "$TZ" ]]; then
  if command -v timedatectl &>/dev/null; then
    TZ="$(timedatectl show -p Timezone --value 2>/dev/null || true)"
  fi
  if [[ -z "$TZ" ]] && [[ -f /etc/timezone ]]; then
    TZ="$(cat /etc/timezone)"
  fi
  if [[ -z "$TZ" ]]; then
    TZ="UTC"
    echo "Warning: Could not detect timezone, using UTC"
  fi
fi

echo "Schedule: daily at $(printf '%02d:%02d' "$HOUR" "$MINUTE") $TZ"
echo "Timeout: ${TIMEOUT}s, Thinking: $THINKING"
echo ""

# Build cron command
CRON_ARGS=(
  cron add
  --name "wiki-journal-daily"
  --cron "$MINUTE $HOUR * * *"
  --tz "$TZ"
  --session isolated
  --message "Daily wiki-journal entry. Read the skill at $SKILL_DIR/SKILL.md and follow its instructions to write today's journal entry."
  --timeout-seconds "$TIMEOUT"
  --thinking "$THINKING"
)

# Add agent flag if specified (omit for default agent)
if [[ -n "$AGENT_ID" ]]; then
  CRON_ARGS+=(--agent "$AGENT_ID")
fi

echo "Registering cron job..."
"$OPENCLAW_BIN" "${CRON_ARGS[@]}"

echo ""
echo "Setup complete!"
echo ""
echo "Verify with:  $OPENCLAW_BIN cron list"
echo "Test run:     $OPENCLAW_BIN cron run <job-id>"
echo "Entries at:   $JOURNAL_DIR/YYYY/MM/DD.md"
