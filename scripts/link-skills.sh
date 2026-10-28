#!/usr/bin/env bash
# Symlink every skill into local agent skill directories, so a `git pull` in this
# clone is all it takes to keep them current. Installing through the Skills CLI
# (see README.md) is the supported route for everyone else.
#
# Usage:
#   scripts/link-skills.sh                  # ~/.claude/skills and ~/.agents/skills
#   scripts/link-skills.sh ~/.cursor/skills # selected destination directories
#
# Existing symlinks are repointed; a real file or directory with a skill's name is
# left alone and reported, so locally installed copies are never deleted.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"

if [ "$#" -gt 0 ]; then
  destinations=("$@")
else
  destinations=("$HOME/.claude/skills" "$HOME/.agents/skills")
fi

skipped_count=0
for destination in "${destinations[@]}"; do
  # Writing through a destination that resolves into this repo would drop the
  # per-skill symlinks into the repo's own skills/ tree.
  if [ -L "$destination" ]; then
    resolved="$(readlink -f "$destination")"
    case "$resolved" in
      "$REPO" | "$REPO"/*)
        echo "error: $destination is a symlink into this repo ($resolved); remove it and re-run" >&2
        exit 1
        ;;
    esac
  fi
  mkdir -p "$destination"

  while IFS= read -r skill; do
    name="$(basename "$skill")"
    source_dir="$REPO/skills/$skill"
    link="$destination/$name"
    if [ -e "$link" ] && [ ! -L "$link" ]; then
      echo "skipped $link: exists and is not a symlink" >&2
      skipped_count=$((skipped_count + 1))
      continue
    fi
    ln -sfn "$source_dir" "$link"
    echo "linked $link -> $source_dir"
  done < <("$REPO/scripts/list-skills.sh")
done

if [ "$skipped_count" -gt 0 ]; then
  echo "link-skills: skipped $skipped_count existing non-symlink path(s); remove them to link this repo's version" >&2
fi
