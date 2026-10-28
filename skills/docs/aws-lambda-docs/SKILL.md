---
name: aws-lambda-docs
description: Official AWS Lambda documentation, answered with links to the exact pages. Use for any Lambda question, including runtimes, handlers and layers, zip or container image deployment, triggers and event source mappings, function URLs, VPC access, permissions, concurrency and cold starts, or monitoring.
---

# AWS Lambda Docs

Lambda answers drift with every release and generic serverless advice skips its runtime limits and event source semantics, so ground each answer in the live docs at <https://docs.aws.amazon.com/lambda/latest/dg/>, not memory, and link the exact page behind every claim.

Route AWS CLI install and global options to `aws-cli-docs`, IAM policy language unrelated to Lambda resources to `aws-iam-docs`, and long-running container services to `aws-ecs-docs`. API Gateway configuration and Step Functions workflow design belong to their own docs unless the question turns on Lambda as the integration or task target.

## Workflow

1. **Locate** the question in [`references/topic-map.md`](references/topic-map.md), a selective index of docs entry points. Done when each part of the question maps to a section of the map, or you have noted that none fits.
2. **Search** `docs.aws.amazon.com/lambda/latest` with the user's exact terms plus Lambda vocabulary such as `event source mapping`, `execution role`, `provisioned concurrency`, `function URL`, `deployment package`, or `container image`, starting from the map's pages and the Routing rules below. Done when you hold the one page that most directly answers each part.
3. **Read** each page down to the relevant section. Done when you have read the passage behind every claim you will make. When a page has moved, been renamed, or stops short, say so and link the nearest authoritative pages.
4. **Answer** with the direct answer first, each docs link beside the claim it supports, and handler code, policies or commands only when the user asks or the page needs them. Mark any conclusion that joins several pages as `Inference:`. Done when every claim cites a specific page, not the docs home.

## Routing

- API parameters: the API reference at <https://docs.aws.amazon.com/lambda/latest/api/Welcome.html>.
- Deployment: tell zip deployment packages from container images on ECR.
- Triggers: the page for the specific event source, and the event source mapping pages for polling versus push models, before generic webhook patterns.
- VPC: the VPC networking and ENI pages, before recommending security group changes alone.
- Permission errors: the execution role and resource-based policy pages together.
- Performance: tell cold starts, init duration, and provisioned concurrency apart.
- `aws lambda` syntax: cross-check `aws-cli-docs`.

## Gotchas

- The execution role grants the function's permissions; the function's resource-based policy is separate.
- Follow the runtime-specific handler signature and check the runtime's deprecation timeline.
- SQS event source mappings deliver batches; handle them with the documented batching semantics, not as HTTP requests.
- Attach a function to a VPC only with the documented cold start and ENI impacts in view.
- Container images for Lambda follow Lambda's documented image limits, not general Docker assumptions.
