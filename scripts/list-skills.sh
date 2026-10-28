#!/usr/bin/env bash
# Print every skill as `<category>/<skill-name>`, sorted.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"

cd "$REPO/skills"
find . -mindepth 3 -maxdepth 3 -name SKILL.md | sed -e 's|^\./||' -e 's|/SKILL\.md$||' | sort
