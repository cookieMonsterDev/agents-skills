---
name: aws-s3-docs
description: Official Amazon S3 documentation, answered with links to the exact pages. Use for any Amazon S3 question, including buckets and objects, storage classes and lifecycle, encryption and access control, presigned URLs, versioning and replication, event notifications, static websites, or Glacier restores.
---

# Amazon S3 Docs

S3 answers drift with every release and pre-Block Public Access defaults linger in memory, so ground each answer in the live docs at <https://docs.aws.amazon.com/AmazonS3/latest/userguide/>, not memory, and link the exact page behind every claim.

Route AWS CLI install, profiles and global options to `aws-cli-docs`, and IAM policy language unrelated to S3 resources to `aws-iam-docs`. Container image storage in ECR and S3-compatible tools such as MinIO belong to their own docs unless the question turns on documented S3 behavior.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.aws.amazon.com/AmazonS3/latest` with the user's exact terms plus S3 vocabulary such as `Block Public Access`, `bucket policy`, `storage class`, `presigned URL`, `lifecycle configuration`, or `replication rule`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and policies, lifecycle JSON or commands only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- Operation request and response fields: the API reference at <https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html>.
- Access denied: the IAM, bucket policy, ACL, and Block Public Access pages together, since S3 denies are often multi-layer.
- Encryption: tell SSE-S3, SSE-KMS, SSE-C, DSSE-KMS, and bucket default encryption apart.
- Cost: the storage classes and lifecycle pages, before recommending Glacier transitions.
- Public websites: the static website hosting page and its Block Public Access interaction.
- `aws s3` and `aws s3api` syntax: cross-check `aws-cli-docs`.

## Gotchas

- Check Block Public Access and bucket policy guidance before recommending public ACLs.
- Bucket policies and IAM user policies are separate layers; access denied troubleshooting needs both.
- Check presigned URL expiry and signature version against the S3 docs before treating a failure as IAM.
- S3 Standard, Intelligent-Tiering, and Glacier storage classes behave differently; name which one applies.
- Confirm versioning and replication prerequisites before enabling lifecycle or delete operations.
- Bucket names are global; most configuration is per bucket and per region.
