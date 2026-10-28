# Code review checklist

Use this checklist for repositories, diffs, API specs, moderation tooling, ad and recommender systems, onboarding flows and interface designs. Code shows what the service does; it rarely shows the terms, staffing or decisions behind it. Pair each technical finding with the organizational question it raises.

For a diff or pull request, review the changed DSA surface and its direct interactions: a new moderation action, ad field, ranking signal or onboarding step. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover DSA surfaces

Search before reading. Adapt the patterns to the codebase's language and naming, and read every hit in context.

```bash
# Notices, moderation actions and appeals
rg -n -i '\b(report|flag|notice|takedown|moderat|remove|demote|shadowban|visibility|suspend|ban|strike|appeal|complaint|reinstat|trusted_?flagger)'

# Statements of reasons and the Transparency Database
rg -n -i '(statement_?of_?reasons|decision_?ground|transparency\.dsa|automated_?detection|automated_?decision|content_?type|territorial_?scope)'

# Ads and recommender systems
rg -n -i '\b(ad_?(id|campaign|targeting|creative)|sponsored|promoted|advertiser|paid_?by|targeting_?param|recommend|ranking|feed_?(algo|score)|personali[sz])'

# Minors, age and traders
rg -n -i '\b(age|birth|dob|minor|under_?1[3-8]|teen|parental|age_?(gate|assurance|verif)|trader|seller|merchant|vat|trade_?register|kyc|business_?id)'
```

Also inspect: moderation queue schemas and decision enums, notice forms, account state machines, ad serving and targeting pipelines, ranking feature lists, user settings defaults, seller onboarding, and the metrics or events that feed transparency reports.

Done when the inventory in SKILL.md step 2 lists each surface, its code location and the articles it triggers at the service's tier.

## 2. Checks

Each check names its main articles. Severity guidance is in [report-template.md](report-template.md#severity).

### Notice and action (Art. 16, 22)

- A notice form or endpoint exists for every content type, reachable without an account, collecting explanation, exact location, notifier name and email (optional for child sexual abuse offences) and a good-faith confirmation.
- Each notice gets an acknowledgement, a decision and a decision notice to the notifier, stating whether automated means were used.
- Notices from trusted flaggers are tagged and routed to a priority queue.

### Statement of reasons (Art. 17, 24(5))

- Every restriction (removal, disabling, demotion, demonetisation, suspension, termination) produces a statement to the affected recipient with the 17(3) fields: restriction and scope, facts, automated detection or decision, legal or contractual ground, redress options.
- Decision records store those fields as structured data, so the statement, the report and the database submission come from one source.
- For online platforms, statements are submitted to the Transparency Database API without undue delay, stripped of personal data; failures are retried and monitored.

### Complaints and misuse (Art. 20, 21, 23)

- Affected recipients and notifiers can file a complaint electronically for at least six months after a decision, free of charge.
- Complaint outcomes are reviewed by a human under qualified supervision, and a successful complaint reverses the action.
- Decision notices link to certified out-of-court dispute settlement bodies.
- Suspension for misuse follows a prior warning, applies for a reasonable period, and is logged with its reason.

### Interface design (Art. 25)

- Cancellation, settings changes and refusals take no more steps than sign-up or acceptance; no pre-selected or visually favoured option steers a choice; no repeated prompts after a choice.

### Advertising (Art. 26, 28(2), 39)

- Each ad render carries a label, the advertiser, the payer if different, and a link to the main targeting parameters and how to change them, generated from the ad's own record.
- Users can declare a post as a commercial communication, and declared posts are labelled.
- Targeting excludes profiling on GDPR Art. 9 special categories, including inferred interests that reveal them (health, religion, sexual orientation, political views).
- Accounts known with reasonable certainty to belong to minors receive no profiling-based ads; check the flag that drives this.
- VLOPs: every served ad is written to a public repository with the Art. 39 fields, retained for one year after last display.

### Recommender systems (Art. 27, 38)

- The main ranking parameters exposed in the terms match the signals in code.
- Where users can choose among options, the control is reachable directly from the feed.
- VLOPs: a non-profiling option (chronological or non-personalised) exists and persists.

### Minors (Art. 28)

- Accounts of minors default to the highest privacy and safety settings: private profile, restricted contact by strangers, no location sharing (Commission Art. 28 guidelines).
- Age assurance is proportionate to the risk, and does not collect more data than needed (28(3)); review the data handling under `gdpr-compliance`.

### Marketplaces (Art. 30-32)

- Trader onboarding blocks listing until the Art. 30(1) fields are collected, and verification against available official sources runs before activation.
- Trader data is retained for six months after the relationship ends and then deleted.
- Product listing forms carry the fields for pre-contractual, labelling and product safety information (Art. 31).
- A job identifies buyers of a product later found illegal in the past six months and notifies them (Art. 32).

### Reporting metrics (Art. 15, 24, 42)

- Events exist for every count in the Implementing Regulation 2024/2835 templates: notices by category and source, actions by type and ground, automated versus human decisions, complaint outcomes, median handling times.
- Average monthly active recipients are computed by a documented method that counts each recipient once per month across devices.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: a new field on the decision record, a queue routing rule, an ad-render template change, a settings default. Note when a fix needs a decision first (tier classification, a moderation policy, an age assurance method).
