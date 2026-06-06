#!/usr/bin/env bash
set -euo pipefail

RESULTS_BRANCH="${DAILYSTOCK_RESULTS_BRANCH:-dailystock-results}"
POLL_SECONDS="${DAILYSTOCK_POLL_SECONDS:-60}"
TIMEOUT_SECONDS="${DAILYSTOCK_TIMEOUT_SECONDS:-5400}"
EXPECTED_AS_OF="${DAILYSTOCK_EXPECTED_AS_OF:-}"

if [ -z "$EXPECTED_AS_OF" ]; then
  EXPECTED_AS_OF="$(
    python3 - <<'PY'
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

today = datetime.now(ZoneInfo("Asia/Shanghai")).date()
print((today - timedelta(days=(today.weekday() - 4) % 7)).isoformat())
PY
  )"
fi

deadline=$((SECONDS + TIMEOUT_SECONDS))
echo "Waiting for the scheduled DailyStock result for $EXPECTED_AS_OF ..."

while [ "$SECONDS" -lt "$deadline" ]; do
  if ! git fetch --quiet origin "$RESULTS_BRANCH"; then
    echo "Git fetch failed; retrying in ${POLL_SECONDS}s." >&2
    sleep "$POLL_SECONDS"
    continue
  fi
  metadata="$(git show "origin/$RESULTS_BRANCH:latest/run_metadata.json" 2>/dev/null || true)"

  if [ -n "$metadata" ] && METADATA="$metadata" EXPECTED_AS_OF="$EXPECTED_AS_OF" python3 - <<'PY'
import json
import os
from datetime import datetime, time
from zoneinfo import ZoneInfo

metadata = json.loads(os.environ["METADATA"])
expected = os.environ["EXPECTED_AS_OF"]
generated_at = datetime.fromisoformat(metadata["generated_at"])
if generated_at.tzinfo is None:
    generated_at = generated_at.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
generated_at = generated_at.astimezone(ZoneInfo("Asia/Shanghai"))
cutoff = datetime.combine(
    datetime.fromisoformat(expected).date(),
    time(16, 30),
    tzinfo=ZoneInfo("Asia/Shanghai"),
)
raise SystemExit(0 if metadata.get("as_of") == expected and generated_at >= cutoff else 1)
PY
  then
    git show "origin/$RESULTS_BRANCH:latest/feishu_summary.md"
    exit 0
  fi

  sleep "$POLL_SECONDS"
done

echo "Timed out waiting for the scheduled DailyStock result for $EXPECTED_AS_OF." >&2
exit 1
