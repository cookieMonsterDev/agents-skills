---
name: git-docs
description: Official Git documentation, answered with links to the exact pages. Use for any Git question, including branching, merging and rebasing, undoing changes and reflog, worktrees and submodules, hooks and config, or revision syntax.
---

# Git Docs

Git answers drift with new commands and changing flag defaults, and blur into hosting-provider docs, so ground each answer in the live docs at <https://git-scm.com/docs/>, not memory, and link the exact page behind every claim.

Route GitHub Actions to `github-actions-docs`, and GitLab merge requests or CI/CD pipelines to `gitlab-ci-docs`. Other GitHub features (pull requests, GitHub CLI, repository settings) belong to GitHub's own docs, and GUI clients to their own docs, unless the question turns on the underlying Git command.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `git-scm.com` with the user's exact terms plus Git vocabulary such as `--force-with-lease`, `ORIG_HEAD`, `reflog`, `fast-forward`, `detached HEAD`, or `ancestry path`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and commands only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Exact flags and syntax: the command reference under <https://git-scm.com/docs/>.
- Concepts and workflows: the Pro Git book at <https://git-scm.com/book/en/v2>; pick reference or book by the question's depth.
- Beginner questions: gittutorial and the Pro Git early chapters, before the full command reference.
- Undoing changes: tell `restore` (working tree and index) from `reset` (branch pointer and index), `revert` (a new commit undoing changes) and `reflog` (recovering lost commits).
- Merge vs rebase: the Pro Git branching chapters.
- Plumbing commands (`git cat-file`, `git rev-parse`, `git hash-object`): the Git internals chapters, before the terse man page.
- Revision syntax (`HEAD^`, `A...B`, `:/pattern`): gitrevisions directly.
- Hooks: confirm client-side or server-side hooks before giving setup steps.

## Gotchas

- Warn before any destructive or history-rewriting command: `reset --hard` and `clean -f` destroy uncommitted or untracked work, and rebasing pushed commits rewrites shared history.
- Offer `--force-with-lease` as the safer alternative to `git push --force`.
- Newer Git splits the multi-purpose `git checkout` into `git switch` and `git restore`; match advice to the split.
- Pull requests, merge requests and forks are hosting-provider concepts; keep them apart from core Git.
