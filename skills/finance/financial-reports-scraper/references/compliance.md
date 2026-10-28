# Compliance

Not legal advice. Identify the client; prefer documented APIs; stay under published rate limits.

## SEC EDGAR

Official access notes: [Accessing EDGAR data](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data), [EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces).

- Use an identifying `User-Agent: {app} {email}`. A 403 may indicate identification or access/rate restrictions; it does not diagnose the cause by itself.
- Fair access: at most 10 requests per second across `sec.gov` / `data.sec.gov` / `efts.sec.gov`. This client waits ≥0.12s between SEC calls.
- The limit applies across processes/machines sharing the user/IP. Keep acquisition serial unless rate limiting is coordinated. Retry transient HTTP/network failures up to three attempts, respecting `Retry-After`; waits above 60 seconds are surfaced for a later retry rather than ignored.
- CIK in URLs is 10 digits with leading zeros.
- Preserve the distinction between SEC-created material and issuer-authored filings. Saving source evidence does not grant redistribution rights or imply SEC endorsement.

## iShares / BlackRock

Product pages and literature PDFs are the issuer's own publications. Fetch them identified, slowly (≥0.5s), without logins or Selenium. Store PDF **URLs** in the CSV; do not copy the files into `reports/`.

The optional `--download-filings` feature applies to SEC primary filings, not these fund-literature PDFs. It preserves local source evidence and hashes; uploading or publishing a bundle is outside acquisition.

## What not to treat as official

Yahoo Finance, FMP, Alpha Vantage, Polygon, and similar aggregators. Spot-check material figures against the filing if some other tool used them.

## Operating rules

Check each site's terms of use before automating access; this skill fetches only public pages and documents. Facts are not copyrightable. Creative works (MD&A prose, branded PDFs) are. `robots.txt` is practical courtesy. Password gates are off limits. Rate limits are architecture, not an afterthought.
