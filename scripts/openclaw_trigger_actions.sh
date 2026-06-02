#!/usr/bin/env bash
set -euo pipefail

# Trigger the DailyStock GitHub Actions workflow through a disposable tag,
# then print the Feishu-ready summary that matches this exact run.

REPO_DIR="${DAILYSTOCK_REPO_DIR:-$(pwd)}"
REMOTE="${DAILYSTOCK_GIT_REMOTE:-origin}"
RESULTS_BRANCH="${DAILYSTOCK_RESULTS_BRANCH:-dailystock-results}"
POLL_SECONDS="${DAILYSTOCK_POLL_SECONDS:-60}"
TIMEOUT_SECONDS="${DAILYSTOCK_TIMEOUT_SECONDS:-3900}"

if [ -n "${DAILYSTOCK_GIT_SSH_KEY:-}" ]; then
  export GIT_SSH_COMMAND="ssh -i ${DAILYSTOCK_GIT_SSH_KEY} -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
elif [ -f "$HOME/.ssh/dailystock_github_ed25519" ]; then
  export GIT_SSH_COMMAND="ssh -i $HOME/.ssh/dailystock_github_ed25519 -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
fi

cd "$REPO_DIR"

REMOTE_REF="${DAILYSTOCK_GIT_REMOTE_URL:-$REMOTE}"
if [ -z "${DAILYSTOCK_GIT_REMOTE_URL:-}" ]; then
  remote_url="$(git remote get-url "$REMOTE" 2>/dev/null || true)"
  if [ -n "${GIT_SSH_COMMAND:-}" ] && [[ "$remote_url" == https://github.com/* ]]; then
    repo_path="${remote_url#https://github.com/}"
    repo_path="${repo_path%.git}"
    REMOTE_REF="ssh://git@github.com/${repo_path}.git"
  fi
fi

git fetch "$REMOTE_REF" main
git checkout main
git pull --ff-only "$REMOTE_REF" main

SOURCE_SHA="$(git rev-parse HEAD)"
BASE_TAG="dailystock-$(TZ=Asia/Shanghai date +%Y%m%d-%H%M%S)"
TAG="${DAILYSTOCK_TAG:-$BASE_TAG}"
suffix=1
while git rev-parse -q --verify "refs/tags/$TAG" >/dev/null; do
  TAG="${BASE_TAG}-${suffix}"
  suffix=$((suffix + 1))
done

git tag "$TAG" "$SOURCE_SHA"
git push "$REMOTE_REF" "refs/tags/$TAG"

echo "DailyStock tag pushed: $TAG"
echo "Source commit: $SOURCE_SHA"
echo "Waiting for $RESULTS_BRANCH/latest/feishu_summary.md ..."

deadline=$((SECONDS + TIMEOUT_SECONDS))
while [ "$SECONDS" -lt "$deadline" ]; do
  git fetch "$REMOTE_REF" "$RESULTS_BRANCH:refs/remotes/origin/$RESULTS_BRANCH" >/dev/null 2>&1 || true

  metadata_file="$(mktemp)"
  if git show "origin/$RESULTS_BRANCH:latest/run_metadata.json" > "$metadata_file" 2>/dev/null; then
    if python3 - "$metadata_file" "$TAG" "$SOURCE_SHA" <<'PY'
import json
import sys
from pathlib import Path

metadata = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
expected_tag = sys.argv[2]
expected_sha = sys.argv[3]
actual_tag = metadata.get("tag") or ""
actual_sha = metadata.get("source_sha") or ""
if actual_tag == expected_tag or actual_sha == expected_sha:
    raise SystemExit(0)
raise SystemExit(1)
PY
    then
      echo
      git show "origin/$RESULTS_BRANCH:latest/feishu_summary.md"
      rm -f "$metadata_file"
      exit 0
    fi
  fi
  rm -f "$metadata_file"

  echo "Result not ready for $TAG; sleeping ${POLL_SECONDS}s ..."
  sleep "$POLL_SECONDS"
done

echo "Timed out waiting for DailyStock result for tag $TAG" >&2
exit 1
