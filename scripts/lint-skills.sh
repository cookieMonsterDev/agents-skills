#!/usr/bin/env bash
# Validate every skill under skills/<category>/<skill-name>/:
#   - the folder holds SKILL.md and LICENSE; docs skills also hold references/topic-map.md
#   - SKILL.md frontmatter has a valid `name` matching the folder and a `description`
#     within the Agent Skills limits (https://agentskills.io/specification)
#   - no template `{placeholder}` is left in the skill's Markdown prose
#   - skill names are unique across categories
#   - each skill is listed in its category README and the SKILLS.md skills map, and
#     each category is listed in the root README
#
# Usage: scripts/lint-skills.sh
# Exit status is 1 when any check fails.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
PROSE_AWK="$REPO/scripts/lib/markdown-prose.awk"
MAX_NAME_LENGTH=64
MAX_DESCRIPTION_LENGTH=1024
# Matches template placeholders such as `{skill-name}` or `{Product Name}`.
PLACEHOLDER_RE='[{][A-Za-z][A-Za-z0-9 _-]*[}]'

cd "$REPO"

error_count=0
report() {
  echo "error: $1" >&2
  error_count=$((error_count + 1))
}

# Prints the value of a top-level `key:` in the frontmatter of the given file.
frontmatter_value() {
  awk -v key="$1" '
    NR == 1 { if ($0 != "---") exit; next }
    $0 == "---" { exit }
    index($0, key ": ") == 1 { print substr($0, length(key) + 3); exit }
  ' "$2"
}

has_frontmatter() {
  [ "$(head -n 1 "$1")" = "---" ] && [ "$(awk 'NR > 1 && $0 == "---" { print "closed"; exit }' "$1")" = "closed" ]
}

lint_frontmatter() {
  local skill_md="$1" folder_name="$2" name description

  if ! has_frontmatter "$skill_md"; then
    report "$skill_md: missing YAML frontmatter delimited by '---' lines"
    return
  fi

  name="$(frontmatter_value name "$skill_md")"
  description="$(frontmatter_value description "$skill_md")"

  if [ -z "$name" ]; then
    report "$skill_md: frontmatter has no 'name'"
  elif [ "$name" != "$folder_name" ]; then
    report "$skill_md: name '$name' does not match folder '$folder_name'"
  fi
  if ! echo "$folder_name" | grep -Eq '^[a-z0-9]+(-[a-z0-9]+)*$'; then
    report "$skill_md: folder name '$folder_name' must be lowercase letters, digits and single hyphens"
  fi
  if [ "${#folder_name}" -gt "$MAX_NAME_LENGTH" ]; then
    report "$skill_md: name is longer than $MAX_NAME_LENGTH characters"
  fi

  if [ -z "$description" ]; then
    report "$skill_md: frontmatter has no 'description'"
  elif [ "${#description}" -gt "$MAX_DESCRIPTION_LENGTH" ]; then
    report "$skill_md: description is ${#description} characters (max $MAX_DESCRIPTION_LENGTH)"
  fi
}

lint_placeholders() {
  local skill_dir="$1" markdown_file match
  while IFS= read -r markdown_file; do
    while IFS= read -r match; do
      report "$markdown_file:${match%%:*}: leftover template placeholder '${match#*:}'"
    done < <(awk -f "$PROSE_AWK" "$markdown_file" | awk -v re="$PLACEHOLDER_RE" '{
      separator = index($0, ":")
      line_number = substr($0, 1, separator - 1)
      text = substr($0, separator + 1)
      while (match(text, re)) {
        print line_number ":" substr(text, RSTART, RLENGTH)
        text = substr(text, RSTART + RLENGTH)
      }
    }')
  done < <(find "$skill_dir" -name '*.md' | sort)
}

lint_registries() {
  local category="$1" name="$2"
  if ! grep -Fq "]($name/SKILL.md)" "skills/$category/README.md" 2>/dev/null; then
    report "skills/$category/README.md: does not link $name/SKILL.md"
  fi
  if ! grep -Fq "](skills/$category/$name/SKILL.md)" SKILLS.md; then
    report "SKILLS.md: skills map does not link skills/$category/$name/SKILL.md"
  fi
}

lint_skill() {
  local skill_dir="$1" category name
  category="$(basename "$(dirname "$skill_dir")")"
  name="$(basename "$skill_dir")"

  if [ ! -f "$skill_dir/SKILL.md" ]; then
    report "$skill_dir: missing SKILL.md"
    return
  fi
  if [ ! -f "$skill_dir/LICENSE" ]; then
    report "$skill_dir: missing LICENSE"
  fi
  if [ "$category" = "docs" ] && [ ! -f "$skill_dir/references/topic-map.md" ]; then
    report "$skill_dir: docs skills need references/topic-map.md"
  fi

  lint_frontmatter "$skill_dir/SKILL.md" "$name"
  lint_placeholders "$skill_dir"
  lint_registries "$category" "$name"
}

# A SKILL.md at any other depth would be installed by the Skills CLI but skipped here.
while IFS= read -r misplaced; do
  report "$misplaced: skills must live at skills/<category>/<skill-name>/SKILL.md"
done < <(find skills -name SKILL.md | grep -Ev '^skills/[^/]+/[^/]+/SKILL\.md$' | sort)

if ! grep -Fxq "@SKILLS.md" AGENTS.md; then
  report "AGENTS.md: does not import the skills map with an '@SKILLS.md' line"
fi

skill_count=0
for category_dir in skills/*/; do
  category_dir="${category_dir%/}"
  category="$(basename "$category_dir")"
  if [ ! -f "$category_dir/README.md" ]; then
    report "$category_dir: missing README.md category index"
  fi
  if ! grep -Fq "](skills/$category/README.md)" README.md; then
    report "README.md: categories table does not link skills/$category/README.md"
  fi
  for skill_dir in "$category_dir"/*/; do
    [ -d "$skill_dir" ] || continue
    lint_skill "${skill_dir%/}"
    skill_count=$((skill_count + 1))
  done
done

while IFS= read -r duplicate; do
  report "skill name '$duplicate' is used in more than one category"
done < <(find skills -mindepth 2 -maxdepth 2 -type d -exec basename {} \; | sort | uniq -d)

if [ "$error_count" -gt 0 ]; then
  echo "lint-skills: $error_count error(s) across $skill_count skill(s)" >&2
  exit 1
fi
echo "lint-skills: $skill_count skill(s) OK"
