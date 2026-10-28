# Finance

Workflow skills that research companies and portfolios from official evidence: SEC
filings, issuer documents and broker statements. Each skill bundles offline Python
helpers, synthetic test fixtures and reference playbooks. The skills depend on each
other, so install all three together.

These skills produce research and conditional suggestions, not personalized financial,
tax or legal advice. They never place trades, file taxes or change accounts.

## Skills

| Skill                                                             | Description                                                                                   | Depends on                                           |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| [`financial-reports-scraper`](financial-reports-scraper/SKILL.md) | Collects SEC EDGAR facts and filings and iShares fund literature into a CSV with a manifest   | —                                                    |
| [`fundamental-analysis`](fundamental-analysis/SKILL.md)           | Analyzes a company's filings and writes a cited report on quality, resilience and valuation   | `financial-reports-scraper`                          |
| [`portfolio-analysis`](portfolio-analysis/SKILL.md)               | Reviews a broker statement (IBKR Flex XML) and writes a cited allocation and positions report | `financial-reports-scraper`, `fundamental-analysis` |

## Routing

- **Broker statement or holdings review:** `portfolio-analysis`, which coordinates the other two.
- **Company financial health, valuation or thesis:** `fundamental-analysis`, with evidence from `financial-reports-scraper`.
- **Official filings, company facts or fund documents only:** `financial-reports-scraper`.
- **General saving, budgeting, debt or investing concepts:** answer directly; no skill is needed unless real portfolio or issuer evidence matters.

## Conventions

- Run each skill's scripts by path from the user's working directory. Generated reports, CSVs and filing snapshots go to `reports/` in the user's working directory or a chosen `--out-dir`, never into this repository.
- Broker statements and account identifiers stay local. Tests and examples use synthetic data only.
- Validate a change with the skill's test command, listed in the Maintenance section of its `SKILL.md`.
