# Print each line of a Markdown file as `<line number>:<text>` with fenced code
# blocks and inline code spans blanked out, so prose checks ignore example code.
# Fenced lines are still printed (empty) to keep line numbers aligned.

/^[[:space:]]*(```|~~~)/ {
  in_fence = !in_fence
  print NR ":"
  next
}

in_fence {
  print NR ":"
  next
}

{
  gsub(/`[^`]*`/, "")
  print NR ":" $0
}
