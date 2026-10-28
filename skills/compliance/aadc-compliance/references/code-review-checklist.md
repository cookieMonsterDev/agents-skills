# Code review checklist

Use this checklist for repositories, diffs, feature flags and remote configuration, settings schemas, recommender and notification services, age-assurance integrations, and data-flow descriptions. Code shows the defaults and mechanics a child meets; it rarely shows audience data or the reasoning in a DPIA. Pair each technical finding with the design or organizational question it raises.

For a diff or pull request, review the changed feature and its direct interactions: a new default, notification, recommendation signal, sharing option or contact surface. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover child-facing features and data

Search before reading. Adapt the patterns to the codebase's language and naming, and read every hit in context.

```bash
# Age signals and age assurance
rg -n -i '(birth_?(date|year)|dob|\bage\b|age_?(gate|band|range|check|verif|estimat|assur)|is_?(minor|child|teen|under_?(13|16|18))|yoti|k-?id|privo|persona|onfido)'

# Defaults and settings
rg -n -i '(default|defaults|DEFAULT_)\W.*(visib|public|private|discover|search|contact|dm|message|share|location|personaliz|recommend|ads?_)'

# Geolocation
rg -n -i '(geoloc|CLLocation|LocationManager|FusedLocation|navigator\.geolocation|lat(itude)?|lng|lon(gitude)?|precise_?location|location_?sharing|live_?location)'

# Profiling, recommenders and ads
rg -n -i '(recommend|for_?you|feed_?rank|personaliz|embedding|interest|segment|audience|lookalike|targeting|ad_?personal|ATT|tracking_?auth)'

# Engagement and persuasive design
rg -n -i '(streak|autoplay|infinite_?scroll|push|notification|badge|reward|loot|gacha|coins|gems|daily_?bonus|reminder|quiet_?hours|read_?receipt|typing_?indicator)'

# Contact, visibility and parental features
rg -n -i '(friend_?(request|suggest)|follow|direct_?message|dm_?|chat|stranger|parent(al)?_?(control|monitor|dashboard)|family_?link|guardian|supervis)'
```

Also inspect: onboarding and sign-up flows, settings screens and their initial values, remote-config and A/B test defaults, notification schedules, recommender feature inputs, ad SDK configuration, connected-device firmware and companion apps, and every place an age result is read.

Done when the inventory in SKILL.md step 2 lists each child-reachable feature with its default, data and engagement mechanics.

## 2. Checks

Each check names the ICO standard, the California section and the DSA guidelines topic. Grade only against codes in scope and in force. Severity guidance is in [report-template.md](report-template.md#severity).

### Age assurance (ICO 3; Cal. (a)(5), (b)(8); DSA 28 guidelines)

- The method's certainty matches the risk of the riskiest feature; a bare self-declared birth date guards only low-risk features.
- When age is unknown, users receive the child protections by default.
- Age data is used only for age assurance and kept no longer than needed; vendor results are stored as an age band or a pass flag, not the documents or images.
- Every feature that branches on age reads the same age result, and re-entry after a failed check is throttled.

### Defaults (ICO 7, 8; Cal. (a)(6))

- Child accounts start private: profile not public, not searchable or suggested to strangers, contact from unknown adults off, content visible to approved contacts only.
- Optional data collection and personalisation start off; each element the child uses can be switched on separately.
- Defaults are the same in code, remote config and experiment variants; an A/B test that weakens a child default is a finding.
- Settings changed by a child to a lower privacy level carry a clear explanation, and remain changeable back.

### Geolocation (ICO 10; Cal. (b)(5)-(b)(6))

- Location collection and sharing are off by default for child users, at the coarsest precision the feature needs.
- An obvious sign shows while location is collected or shared.
- Options making location visible to others revert to off at the end of each session.

### Profiling and recommenders (ICO 12; Cal. (b)(2); DSA 28(2), Art. 38 for very large platforms)

- Profiling for recommendations and ads is off by default for child users, or justified with protections recorded in the DPIA.
- No personalised ads based on profiling for users known with reasonable certainty to be minors (DSA 28(2)); ad SDKs receive the minor signal.
- Recommender inputs exclude signals that infer vulnerability, and feeds have a non-profiled option.

### Nudges and persuasive design (ICO 5, 13; Cal. (b)(7); DSA 28 guidelines)

- Privacy choices present the high-privacy option with at least equal prominence; no confirmshaming, pre-ticked options or repeated prompts to lower settings.
- Engagement mechanics are off or bounded for children: autoplay, infinite scroll, streaks, variable rewards, and notifications during school and night hours.
- Virtual currency and paid items show real-money cost and avoid pressure tactics.

### Data sharing and minimisation (ICO 8, 9; Cal. (b)(3)-(b)(4))

- Children's data reaches third parties only where a compelling best-interests reason is documented; analytics and ad SDKs receive the minimum.
- Data collected for one feature is not reused for another without a new choice.

### Parental controls (ICO 11; Cal. (a)(8))

- When a parent can monitor activity or location, the child sees an obvious, persistent signal and age-appropriate information about it.

### Rights and reporting tools (ICO 15; Cal. (a)(10); DSA 28 guidelines)

- In-product tools let a child or parent access, delete and correct data, and report content or contacts, reachable within a few taps from the main screens.

### Connected toys and devices (ICO 14)

- Recording and transmission are visible on the device; listening starts only on clear activation; data stays local where the feature allows.
- Companion app set-up explains the data flows before pairing, and shared family devices do not mix profiles.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: the settings schema default, the remote-config key, the existing age service, the recommender's feature switch. Note when a fix needs a design or organizational decision first (the risk level that sets the age-assurance method, a best-interests justification).
