# Agents Skills

[Agent Skills](https://skills.sh/) for coding agents. Each skill is a folder with a `SKILL.md` file that teaches the agent how to perform a specific task.

## Repository layout

```
agents-skills/
├── skills/
│   ├── docs/              # docs-grounded skills, one per product or framework
│   │   ├── README.md      # category index
│   │   └── <skill>/
│   ├── architecture/      # catalog skills: patterns, principles, practices
│   │   ├── README.md
│   │   └── <skill>/
│   ├── finance/           # workflow skills: filings, company and portfolio analysis
│   │   ├── README.md
│   │   └── <skill>/
│   └── compliance/        # workflow skills: reviews against regulations such as GDPR
│       ├── README.md
│       └── <skill>/
├── templates/             # starting points for new skills (not installable)
└── scripts/               # lint, list, link and link-check tooling
```

Skills are grouped as `skills/<category>/<skill-name>/`. Skill names are unique across categories, so a skill installs under its own name regardless of its category.

## Categories

| Category                                        | Skills                                                                                                                  |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [`docs`](skills/docs/README.md)                 | Route a question to the official docs of a product or framework and answer with direct links to the authoritative pages |
| [`architecture`](skills/architecture/README.md) | Teach a catalog of design items with a reference explanation per item and runnable examples where useful                |
| [`finance`](skills/finance/README.md)           | Research companies and portfolios from official filings and broker statements, with cited Markdown reports              |
| [`compliance`](skills/compliance/README.md)     | Review code, data flows and documents against regulations such as the GDPR, with cited findings reports                 |

## Install with Skills CLI

The easiest way is the [Skills CLI](https://skills.sh/):

```bash
# Install one skill globally (available in all projects)
npx skills add cookieMonsterDev/agents-skills@postgresql-18-docs -g -y

# Install all skills from this repo
npx skills add cookieMonsterDev/agents-skills --all -g -y

# Install into the current project only
npx skills add cookieMonsterDev/agents-skills@postgresql-17-docs -y

# List skills in this repo without installing
npx skills add cookieMonsterDev/agents-skills -l
```

From a local clone:

```bash
git clone git@github.com:cookieMonsterDev/agents-skills.git
cd agents-skills
npx skills add . --skill postgresql-16-docs -g -y
```

Other useful commands:

```bash
npx skills list          # show installed skills
npx skills update        # update installed skills
npx skills remove <name> # remove a skill
```

## Manual install

Copy or symlink a skill folder into one of these locations:

| Scope                 | Path                             |
| --------------------- | -------------------------------- |
| Global (all projects) | `~/.cursor/skills/<skill-name>/` |
| Project only          | `.cursor/skills/<skill-name>/`   |
| Project (alternative) | `.agents/<skill-name>/`          |

Example:

```bash
ln -s ~/Projects/personal/agents-skills/skills/docs/postgresql-18-docs ~/.cursor/skills/postgresql-18-docs
```

To symlink every skill at once into `~/.claude/skills` and `~/.agents/skills`, run `scripts/link-skills.sh`. Each entry points back into the clone, so a `git pull` keeps the installed skills current.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for authoring new skills, the lint and link-check scripts, and commit conventions. [SKILLS.md](SKILLS.md) lists every skill in the repository.

## How it works

When a skill is installed, the agent can load it for matching questions. Each docs skill:

1. Routes the question to the right docs section
2. Searches the official documentation for that framework or product
3. Answers with direct links to the authoritative docs pages

Pick the skill that matches your stack. For PostgreSQL, use the skill that matches your major version — check `SELECT version();` or your deployment docs if unsure.
