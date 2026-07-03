---
name: aws-s3-docs
description: Use when users ask how to create, configure, secure, access, replicate, lifecycle-manage, or troubleshoot Amazon S3 buckets and objects, including storage classes, encryption, bucket policies, ACLs, Block Public Access, presigned URLs, static website hosting, event notifications, replication, S3 Glacier, Mountpoint, or S3 API behavior, especially when they need official Amazon S3 documentation, exact links, or docs-grounded guidance.
---

Amazon S3 questions are easy to answer from stale memory or pre–Block Public Access defaults. Use this skill to ground answers in the official Amazon S3 documentation and return the closest authoritative page instead of generic object-storage advice.

## When to Use

Use this skill when the request is about:

- S3 concepts: buckets, objects, keys, prefixes, and regions
- Creating buckets, uploading objects, and object metadata
- Storage classes, intelligent tiering, and lifecycle rules
- Encryption at rest and in transit (SSE-S3, SSE-KMS, SSE-C, DSSE-KMS)
- Access control: bucket policies, ACLs, IAM policies, and Block Public Access
- Presigned URLs, public access, and cross-account access patterns
- Versioning, MFA delete, and object locking (WORM)
- Replication (same-region and cross-region), batch operations, and inventory
- Event notifications, EventBridge, and S3 Object Lambda
- Static website hosting, CORS, and request routing
- Transfer Acceleration, multipart upload, and performance tuning
- S3 Glacier, Glacier Flexible Retrieval, and restore workflows
- S3 on Outposts, directory buckets, and Mountpoint for Amazon S3
- Troubleshooting access denied, 403, signature errors, and throttling

Do not use this skill for:

- AWS CLI install, profiles, or global CLI options. Use `aws-cli-docs` instead.
- IAM policy language fundamentals unrelated to S3 resources. Use `aws-iam-docs` for general IAM concepts.
- EKS/ECS container image storage in ECR. Use service-specific docs unless the question is about S3 as artifact or log storage.
- Third-party S3-compatible tools (MinIO, etc.) unless the question maps to documented S3 API behavior.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and core concepts
- Buckets and object operations
- Storage classes and lifecycle
- Security, encryption, and access control
- Replication, versioning, and data protection
- Event notifications and integrations
- Performance, transfer, and multipart uploads
- Static websites, CORS, and routing
- Glacier and archival workflows
- Advanced features (Object Lambda, Access Points, Batch Operations)
- Troubleshooting and error codes

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official Amazon S3 docs first

- Treat `docs.aws.amazon.com/AmazonS3/latest/userguide` as the source of truth for Amazon S3.
- Prefer the user guide at <https://docs.aws.amazon.com/AmazonS3/latest/userguide/>.
- Prefer the API reference at <https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html> for operation-level details.
- Search with the user's exact terms plus focused S3 phrases such as `Block Public Access`, `bucket policy`, `storage class`, `presigned URL`, `lifecycle configuration`, or `replication rule`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For access denied errors, check IAM, bucket policy, ACL, and Block Public Access docs before guessing permission fixes.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For API operations, open the specific API reference page when request/response fields matter.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact Amazon S3 docs links, not just the docs homepage.
- Only provide bucket policies, lifecycle JSON, or CLI examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to Amazon S3 docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example policy, configuration, or commands, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer What is Amazon S3? and getting started before API reference pages.
- For access questions, check bucket policies, Block Public Access, and IAM together — S3 denies are often multi-layer.
- For encryption questions, distinguish SSE-S3, SSE-KMS, SSE-C, and bucket default encryption settings.
- For cost questions, prefer storage classes and lifecycle docs before recommending Glacier transitions.
- For public website questions, check static website hosting and Block Public Access interaction docs.
- For CLI syntax-only questions, cross-check `aws-cli-docs` command reference for `aws s3` and `aws s3api`.
- Note regional behavior: bucket names are global; most configuration is per-bucket and per-region.

## Common Mistakes

- Answering from memory without verifying the current Amazon S3 docs
- Linking the S3 landing page when a narrower user guide or API page exists
- Recommending public ACLs without checking Block Public Access and bucket policy guidance
- Confusing bucket policies with IAM user policies when troubleshooting access denied
- Mixing S3 Standard, Intelligent-Tiering, and Glacier storage class behavior
- Treating presigned URL expiry or signature version issues as IAM problems without checking S3 docs
- Ignoring versioning and replication prerequisites when enabling lifecycle or delete operations

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live Amazon S3 docs as the final authority.
