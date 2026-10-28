#!/usr/bin/env bash
# Check that relative links in the repository's Markdown files resolve: the target
# file or directory exists and, for `file.md#anchor` links, the heading exists.
# External links (any `scheme:`) are left to scripts/check_doc_links.py.
#
# Usage:
#   scripts/lint-md-links.sh                # every Markdown file git knows about,
#                                           # except templates/ (placeholder links)
#   scripts/lint-md-links.sh README.md docs # selected files or directories
# Exit status is 1 when any link is broken.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
PROSE_AWK="$REPO/scripts/lib/markdown-prose.awk"

cd "$REPO"

# Prints `<line number>:<link target>` for each inline link or image in prose.
extract_links() {
  awk -f "$PROSE_AWK" "$1" | awk '{
    separator = index($0, ":")
    line_number = substr($0, 1, separator - 1)
    text = substr($0, separator + 1)
    while (match(text, /\]\([^)]+\)/)) {
      print line_number ":" substr(text, RSTART + 2, RLENGTH - 3)
      text = substr(text, RSTART + RLENGTH)
    }
  }'
}

# Prints the GitHub-style anchor of every heading in a Markdown file, adding the
# `-1`, `-2` suffixes GitHub gives repeated headings.
heading_anchors() {
  awk -f "$PROSE_AWK" "$1" | awk '{
    text = substr($0, index($0, ":") + 1)
    if (text !~ /^#+[[:space:]]/) next
    sub(/^#+[[:space:]]+/, "", text)
    sub(/[[:space:]]+#*[[:space:]]*$/, "", text)
    anchor = tolower(text)
    gsub(/[^a-z0-9 _-]/, "", anchor)
    gsub(/ /, "-", anchor)
    if (anchor in seen) {
      seen[anchor]++
      print anchor "-" seen[anchor]
    } else {
      seen[anchor] = 0
      print anchor
    }
  }'
}

list_markdown_files() {
  if [ "$#" -eq 0 ]; then
    git ls-files --cached --others --exclude-standard -- '*.md' ':!:templates/*'
    return
  fi
  local target
  for target in "$@"; do
    if [ -d "$target" ]; then
      find "$target" -name '*.md' -not -path '*/node_modules/*'
    else
      echo "$target"
    fi
  done
}

error_count=0
link_count=0
while IFS= read -r markdown_file; do
  [ -f "$markdown_file" ] || continue
  file_dir="$(dirname "$markdown_file")"
  while IFS= read -r entry; do
    line_number="${entry%%:*}"
    target="${entry#*:}"
    # Drop an optional link title and angle-bracket wrapping: [text](<path> "title").
    target="${target%% \"*}"
    target="${target#<}"
    target="${target%>}"

    if [[ "$target" =~ ^[A-Za-z][A-Za-z0-9+.-]*: ]]; then
      continue
    fi
    link_count=$((link_count + 1))

    path_part="${target%%#*}"
    path_part="${path_part%%\?*}"
    anchor=""
    case "$target" in
      *#*) anchor="${target#*#}" ;;
    esac

    if [ -z "$path_part" ]; then
      resolved="$markdown_file"
    elif [ "${path_part#/}" != "$path_part" ]; then
      resolved="${path_part#/}"
    else
      resolved="$file_dir/$path_part"
    fi

    if [ ! -e "$resolved" ]; then
      echo "error: $markdown_file:$line_number: broken link '$target' ($resolved does not exist)" >&2
      error_count=$((error_count + 1))
      continue
    fi
    case "$resolved" in
      *.md) ;;
      *) continue ;;
    esac
    if [ -n "$anchor" ] && ! heading_anchors "$resolved" | grep -Fxq "$anchor"; then
      echo "error: $markdown_file:$line_number: broken link '$target' (no heading '#$anchor' in $resolved)" >&2
      error_count=$((error_count + 1))
    fi
  done < <(extract_links "$markdown_file")
done < <(list_markdown_files "$@" | sort -u)

if [ "$error_count" -gt 0 ]; then
  echo "lint-md-links: $error_count broken link(s) out of $link_count relative link(s)" >&2
  exit 1
fi
echo "lint-md-links: $link_count relative link(s) OK"
