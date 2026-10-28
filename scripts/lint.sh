#!/usr/bin/env bash
# Run every offline repository check and report which ones failed. External docs
# links need the network and minutes per run, so scripts/check_doc_links.py stays
# a separate step.
#
# Usage: scripts/lint.sh
# Exit status is 1 when any check fails.
set -uo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO" || exit 1

failed_checks=()

run_check() {
  local check_name="$1"
  shift
  echo "==> $check_name"
  if ! "$@"; then
    failed_checks+=("$check_name")
  fi
}

run_check "skills" scripts/lint-skills.sh
run_check "markdown links" scripts/lint-md-links.sh

if command -v shellcheck >/dev/null 2>&1; then
  run_check "shellcheck" shellcheck scripts/*.sh
else
  echo "==> shellcheck (skipped: not installed)"
fi

if [ "${#failed_checks[@]}" -gt 0 ]; then
  echo "lint: failed: ${failed_checks[*]}" >&2
  exit 1
fi
echo "lint: all checks passed"
