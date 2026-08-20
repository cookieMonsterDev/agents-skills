---
name: git-docs
description: Use when users ask how to use, explain, configure, or troubleshoot core Git version control commands and concepts, including branching, merging, rebasing, resetting, stashing, bisecting, worktrees, submodules, hooks, reflog, and revision syntax, especially when they need the official Git reference manual, exact command flags, or docs-grounded guidance distinct from a specific hosting provider's UI.
---

Git questions are easy to answer from stale memory or from a hosting provider's UI docs instead of Git itself. Use this skill to ground answers in the official Git documentation and return the closest authoritative command reference or book chapter instead of guessing flag behavior.

## When to Use

Use this skill when the request is about:

- Core Git commands and their exact flags: `commit`, `branch`, `checkout`, `switch`, `restore`, `merge`, `rebase`, `reset`, `log`, `diff`, `push`, `pull`, `fetch`, `clone`, `tag`, `stash`, `cherry-pick`, `bisect`, `worktree`, `submodule`, `reflog`, `blame`, `remote`
- Git concepts: the object model (blobs, trees, commits, refs), the index/staging area, and the working tree
- Revision syntax (`HEAD~2`, `main..feature`, `@{upstream}`) and the gitrevisions reference
- Branching and merging strategies, rebase workflows, and conflict resolution
- Git hooks, `.gitignore`, `.gitattributes`, and repository configuration
- Submodules and worktrees for managing multiple checkouts or nested repositories
- History rewriting: interactive rebase, filter-repo-style history surgery, and reflog recovery
- Git internals: plumbing vs porcelain commands, packfiles, and the transfer protocols

Do not use this skill for:

- GitHub-specific features (pull requests, GitHub Actions, GitHub CLI, repository settings UI). Use `github-actions-docs` for Actions, or the GitHub product docs for the rest.
- GitLab-specific features (merge requests, GitLab CI/CD pipelines). Use `gitlab-ci-docs` instead.
- GUI Git clients unless the question is about the underlying Git command each button runs.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and everyday workflow
- Branching, merging, and rebasing
- Undoing changes: reset, revert, restore, checkout, and reflog
- Inspecting history: log, diff, blame, and bisect
- Remote operations: fetch, pull, push, and remotes
- Advanced structures: worktrees and submodules
- Configuration, hooks, ignore/attribute files
- Internals and the object model

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Git docs first

- Treat `git-scm.com` as the source of truth for core Git.
- Prefer the command reference under <https://git-scm.com/docs/> for exact flags and syntax.
- Prefer the Pro Git book under <https://git-scm.com/book/en/v2> for conceptual explanations and workflows.
- Search with the user's exact terms plus focused Git phrases such as `--force-with-lease`, `ORIG_HEAD`, `reflog`, `fast-forward`, `detached HEAD`, or `ancestry path`.
- When multiple pages are plausible, compare the command reference (exact syntax) against the relevant Pro Git chapter (conceptual explanation) and pick whichever matches the question's depth.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Git docs links, not just the docs landing page.
- Only provide command examples when the user asks for them or when the docs page makes an example necessary.
- Warn explicitly before suggesting any history-rewriting or destructive command (`reset --hard`, `push --force`, `rebase` on shared branches, `clean -f`).
- Make any inference explicit. Good phrasing:
  - `According to the Git docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example command, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For beginner questions, prefer gittutorial and the Pro Git book's early chapters before the full command reference.
- For "how do I undo X" questions, distinguish `restore` (working tree/index) from `reset` (branch pointer and index) from `revert` (new commit undoing changes) from `reflog` (recovering lost commits).
- For merge vs rebase questions, prefer the Pro Git branching chapters and be explicit about the shared-history risk of rebasing pushed commits.
- For "what does this command do" questions on plumbing commands (`git cat-file`, `git rev-parse`, `git hash-object`), prefer the Git internals chapters before the terse man-page description.
- For revision syntax questions (`HEAD^`, `A...B`, `:/pattern`), prefer gitrevisions directly rather than inferring syntax from examples.
- For hook questions, confirm client-side vs server-side hooks before giving setup steps.

## Common Mistakes

- Answering from memory without verifying exact flag names and defaults in the command reference
- Linking the Git docs homepage when the specific command page or Pro Git chapter answers the question directly
- Recommending `git push --force` without mentioning `--force-with-lease` as the safer alternative
- Confusing `git checkout` (multi-purpose in older Git) with the newer `git switch`/`git restore` split
- Suggesting `git reset --hard` or `git clean -f` without warning that uncommitted or untracked work is destroyed
- Treating GitHub or GitLab-specific terminology (pull request, merge request, fork) as core Git concepts

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Git docs as the final authority.
