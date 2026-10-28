---
name: firebase-docs
description: Official Firebase documentation, answered with links to the exact pages. Use for any Firebase question, including Authentication, Firestore and Realtime Database, Cloud Functions, Hosting and Cloud Storage, Cloud Messaging, or Security Rules.
---

# Firebase Docs

Firebase answers drift between platform SDKs and between Firestore and the older Realtime Database, so ground each answer in the live docs at <https://firebase.google.com/docs/>, not memory, and link the exact page behind every claim.

Route MongoDB questions to `mongodb-docs`, and DynamoDB questions to `aws-dynamodb-docs`, unless the user is comparing them to Firestore or Realtime Database. Underlying Google Cloud services (Cloud Run, BigQuery, Compute Engine) belong to Google Cloud's own docs, and general app architecture is out of scope, unless the question turns on a specific Firebase product or SDK.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `firebase.google.com/docs` with the user's exact terms plus Firebase vocabulary such as `onSnapshot`, `security rules`, `Cloud Functions trigger`, `FCM token`, or `Firestore index`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and SDK code, naming its platform, only when the user asks or the page needs it. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Setup and API shape: confirm the platform (Web, iOS, Android, Flutter, Admin SDK) first, then use that platform's pages.
- Database questions: confirm Firestore (document model, richer queries) or Realtime Database (JSON tree, simpler queries) first; they have separate docs.
- Security: the Security Rules docs for the specific product (Firestore, Realtime Database or Storage).
- Cloud Functions: tell HTTP-triggered functions from background triggers (Firestore, Auth, Storage events) before giving deployment steps.
- Messaging: tell notification messages from data messages, then check the platform's token handling.
- Testing: the Firebase Local Emulator Suite docs, before any test against production data.

## Gotchas

- Firestore and Realtime Database use different security rules syntax; write rules against the product's own reference.
- The Admin SDK bypasses security rules; client SDK behavior under rules does not carry over to it.
- For new projects, present Firestore as the more capable default for most use cases over Realtime Database.
- Keep platform setup files apart: Android uses `google-services.json`, iOS uses `GoogleService-Info.plist`.
