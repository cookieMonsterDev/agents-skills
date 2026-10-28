# Contributing

## Rules

- Put each skill in `skills/<category>/<skill-name>/`, starting from a [template](templates/). Skill names stay unique across categories.
- List a new skill in its category README (`skills/<category>/README.md`) and in [`SKILLS.md`](SKILLS.md).
- Run `scripts/lint.sh` before committing. It checks skill layout, frontmatter, placeholders, registry listings and relative links.
- Run `scripts/check_doc_links.py` before committing link changes in docs or compliance skills. It reports broken links and lists bot-blocked hosts (`dev.mysql.com`, `docs.gitlab.com`) separately as inconclusive.

## Authoring new skills

Skill templates live under [`templates/`](templates/):

| Template                | Use for                                                                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `docs-template`         | Documentation-grounded skills that route to official product docs                                                                              |
| `architecture-template` | Catalog-style skills that teach a set of design items (patterns, principles, practices) with reference explanations and optional code examples |

To create a new docs skill:

```bash
cp -R templates/docs-template skills/docs/my-product-docs
```

Then replace the `{placeholder}` values in `SKILL.md` and `references/topic-map.md`, and add the skill to [`skills/docs/README.md`](skills/docs/README.md) and the skills map in [`SKILLS.md`](SKILLS.md).

To create a new architecture skill:

```bash
cp -R templates/architecture-template skills/architecture/my-catalog-skill
```

Then replace the `{placeholder}` values in `SKILL.md`, duplicate `references/example-item.md` (and its matching `examples/example-item/` folder, if used) per catalog item, and add the skill to [`skills/architecture/README.md`](skills/architecture/README.md) and the skills map in [`SKILLS.md`](SKILLS.md).

Finance skills have no template: they are workflow skills with Python helpers, `scripts/`, `tests/` and synthetic fixtures. When changing one, run its test command (in the Maintenance section of its `SKILL.md`) in addition to `scripts/lint.sh`. Keep fixtures synthetic, and never commit broker statements, generated reports or copyrighted third-party material such as books.

Compliance skills have no template either: they are review workflows with reference checklists that cite the official text of the regulation (article, recital or clause) and link its authoritative source. Examples use synthetic data only.

To add a category, create `skills/<category>/README.md` with a skills table, add the category to the categories table in [`README.md`](README.md), and give it a section in [`SKILLS.md`](SKILLS.md).

Run `scripts/lint.sh` before committing; it fails when a placeholder is left over or a skill is missing from a registry.

**Language examples:** add a file only for languages that support the skill's concepts. OOP skills need first-class classes (Python, C++, Java, C#, JavaScript, PHP, Swift — not C, Go, or Rust). Design-pattern skills may also include C, Go, and Rust where patterns are idiomatically emulated. Omit a language per catalog item when the concept is built into the language or has no honest mapping. See the [Choosing languages](templates/architecture-template/SKILL.md#choosing-languages) section in the architecture template.

## Scripts

| Script                       | Purpose                                                                                                  |
| ---------------------------- | -------------------------------------------------------------------------------------------------------- |
| `scripts/lint.sh`            | Run every offline check below; the CI gate                                                               |
| `scripts/lint-skills.sh`     | Validate skill layout, `SKILL.md` frontmatter, unique names, leftover placeholders and registry listings |
| `scripts/lint-md-links.sh`   | Check that relative Markdown links point at files that exist                                             |
| `scripts/list-skills.sh`     | Print every skill as `<category>/<skill-name>`                                                           |
| `scripts/link-skills.sh`     | Symlink every skill into local agent skill directories                                                   |
| `scripts/check_doc_links.py` | Request every external docs link and report the broken ones (network, slow)                              |

`scripts/lint.sh` also runs [ShellCheck](https://www.shellcheck.net/) on the scripts when it is installed (`brew install shellcheck`).

## Keeping docs links fresh

Docs sites reorganize, so every skill's links are machine-checkable:

```bash
# Check every skill under skills/
scripts/check_doc_links.py

# Check one skill while editing it
scripts/check_doc_links.py skills/docs/redis-docs

# Slow down a host that answers 429, and keep a machine-readable report
scripts/check_doc_links.py --host-delay 2 --json /tmp/links.json
```

The script exits non-zero when a link is broken, so it works as a CI gate. Links that
answer 401/403/429 are listed separately as inconclusive rather than broken: those
statuses mean the host refused a scripted request. `dev.mysql.com` and `docs.gitlab.com`
block the checker this way, so their links need a browser to confirm. Pass `--strict`
to count them as failures anyway.

When a link is genuinely gone, fix the entry in the skill's `references/topic-map.md`
and, if the docs site moved a whole section, update the "Search official docs first"
guidance in its `SKILL.md` too.

## Commit messages (Conventional Commits)

Use [Conventional Commits](https://www.conventionalcommits.org/) when the user asks for a commit message:

```
<type>(<optional scope>): <short imperative summary>

[optional body - what and why, wrapped at ~72 chars]
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `chore`, `ci`

**Scope:** skill(s) type (e.g. `doc`, `tool`, `architecture`). Omit if unclear.

**Examples:**

```
fix(doc): links update for latest fastAPI docs version
feat(tool): add pnpm tool skill with references to to official docs
refactor(architecture): add OOP guidelines skill with code examples
```
