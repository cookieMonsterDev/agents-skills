# Scenario: foreign issuer

Use when the company is not a US domestic 10-K filer.

## US-listed foreign private issuer

If it has a CIK, it still files on EDGAR: **20-F** (annual) and **6-K** (current), sometimes **40-F** (Canadian). The `edgar` adapter already keeps those forms. Face-statement tags may be `ifrs-full` rather than `us-gaap`.

Run the same CLI as a US stock (`--tickers` or a portfolio row with ticker/CIK). Then check `form` and `taxonomy` in the CSV.

Home-market annual reports are often richer (equity roll-forward, segments, commentary). After the EDGAR extract, open the topic-map Non-US list and record the home-market URL in analysis notes. This skill does not scrape SEDAR+, EDINET, or Bundesanzeiger yet.

## Not US-listed

No adapter. The pipeline writes `record_kind=error`, `concept=no_adapter`. Next step is to add an adapter or a catalog entry, not to call Yahoo.

Irish UCITS ETFs and iShares ETCs are not this scenario — use [scenario-ucits-etf.md](scenario-ucits-etf.md) or [scenario-precious-metals-etc.md](scenario-precious-metals-etc.md).
