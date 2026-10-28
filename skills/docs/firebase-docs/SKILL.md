---
name: firebase-docs
description: Use when users ask how to build, configure, secure, or troubleshoot Firebase applications, including Authentication, Firestore, Realtime Database, Cloud Functions, Hosting, Cloud Storage, Cloud Messaging, Remote Config, Crashlytics, App Check, Security Rules, Extensions, or the Admin/client SDKs across Web, iOS, Android, and Flutter, especially when they need official Firebase documentation, exact links, or docs-grounded guidance.
---

Firebase questions are easy to answer from stale memory or by conflating Firestore with the older Realtime Database. Use this skill to ground answers in the official Firebase documentation and return the closest authoritative page instead of generic backend-as-a-service advice.

## When to Use

Use this skill when the request is about:

- Firebase Authentication: sign-in methods, session management, and the Admin SDK
- Cloud Firestore: data model, queries, indexes, and security rules
- Realtime Database: JSON tree structure, queries, and security rules
- Cloud Functions for Firebase: triggers, HTTP functions, and deployment
- Firebase Hosting: deploys, rewrites, and custom domains
- Cloud Storage for Firebase: uploads, downloads, and storage security rules
- Cloud Messaging (FCM), Remote Config, Crashlytics, App Check, and Firebase Extensions
- Client SDK setup for Web, iOS, Android, Flutter, Unity, and C++
- Firebase Security Rules language and testing rules with the emulator suite
- Firebase project setup, pricing tiers, and the Firebase CLI

Do not use this skill for:

- Underlying Google Cloud Platform services (Cloud Run, BigQuery, Compute Engine) unless accessed specifically through a Firebase product. Use general GCP documentation for those.
- MongoDB, DynamoDB, or other NoSQL databases unless the user is explicitly comparing them to Firestore or Realtime Database.
- General mobile or web app architecture questions unless they concern a specific Firebase SDK or service.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Project setup and SDK installation (Web, iOS, Android, Flutter)
- Authentication
- Firestore vs Realtime Database
- Cloud Functions
- Hosting
- Cloud Storage
- Messaging, Remote Config, Crashlytics, App Check
- Security Rules and the emulator suite
- Extensions and pricing

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Firebase docs first

- Treat `firebase.google.com/docs` as the source of truth for Firebase.
- Prefer pages under <https://firebase.google.com/docs/>.
- Confirm the platform (Web, iOS, Android, Flutter, Admin SDK) before answering, since setup and API shape differ per platform.
- Search with the user's exact terms plus focused Firebase phrases such as `onSnapshot`, `security rules`, `Cloud Functions trigger`, `FCM token`, or `Firestore index`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Firebase docs links, not just the docs homepage.
- Only provide SDK code examples when the user asks for them or when the docs page makes an example necessary, and specify which platform the example targets.
- Make any inference explicit. Good phrasing:
  - `According to Firebase docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example SDK code, only if needed (state the platform)
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For database questions, first confirm whether the user means Firestore (document model, richer queries) or Realtime Database (JSON tree, simpler queries) — they have separate docs and security rules languages.
- For beginner questions, prefer the platform-specific quickstart before deep reference pages.
- For security questions, prefer the Security Rules docs for the specific product (Firestore, Realtime Database, or Storage) rather than assuming rules syntax carries over between products.
- For Cloud Functions questions, distinguish HTTP-triggered functions from background triggers (Firestore, Auth, Storage events) before giving deployment steps.
- For messaging questions, distinguish notification messages from data messages and check platform-specific token handling.
- For testing questions, prefer the Firebase Local Emulator Suite docs before recommending tests against production data.

## Common Mistakes

- Answering from memory without verifying the current Firebase docs
- Linking the Firebase docs homepage when a narrower product or platform page exists
- Confusing Firestore security rules syntax with Realtime Database security rules syntax
- Assuming client SDK behavior (subject to security rules) applies to Admin SDK usage (which bypasses security rules)
- Recommending Realtime Database for new projects without noting Firestore is the more capable default for most use cases
- Mixing platform-specific setup steps (for example, Android `google-services.json` vs iOS `GoogleService-Info.plist`) across platforms

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Firebase docs as the final authority.
