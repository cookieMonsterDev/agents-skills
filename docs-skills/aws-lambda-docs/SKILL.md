---
name: aws-lambda-docs
description: Use when users ask how to create, configure, deploy, invoke, scale, secure, monitor, or troubleshoot AWS Lambda functions, including runtimes, layers, deployment packages, container images, triggers, event sources, VPC configuration, concurrency, provisioned concurrency, Lambda URLs, permissions, environment variables, or Lambda extensions, especially when they need official AWS Lambda documentation, exact links, or docs-grounded guidance.
---

AWS Lambda questions are easy to answer from stale memory or generic serverless patterns that ignore runtime limits, cold starts, and event source mappings. Use this skill to ground answers in the official AWS Lambda documentation and return the closest authoritative page instead of improvising deployment advice.

## When to Use

Use this skill when the request is about:

- Lambda concepts: functions, handlers, runtimes, and execution environment
- Creating functions, deployment packages (zip), and container images
- Runtimes, layers, and custom runtimes
- Function configuration: memory, timeout, ephemeral storage, and architecture (x86_64/arm64)
- Environment variables, parameters, and secrets integration
- Triggers and event source mappings (SQS, SNS, Kinesis, DynamoDB Streams, EventBridge, etc.)
- Lambda URLs, function URLs, and API Gateway integration patterns documented for Lambda
- VPC configuration, ENI behavior, and networking constraints
- IAM execution roles, resource-based policies, and permission boundaries
- Concurrency, reserved concurrency, and provisioned concurrency
- SnapStart, response streaming, and runtime-specific features
- Monitoring: CloudWatch Logs, metrics, X-Ray, and Lambda Insights
- Troubleshooting timeouts, throttling, permission errors, and cold starts

Do not use this skill for:

- AWS CLI install or global CLI options. Use `aws-cli-docs` instead.
- General IAM policy language unrelated to Lambda resources. Use `aws-iam-docs` for IAM fundamentals.
- ECS/Fargate long-running services. Use `aws-ecs-docs` instead.
- API Gateway service configuration when the question is only about API Gateway, not Lambda integration.
- Step Functions workflow design unless the question is about Lambda as a task target in Lambda docs.

## Workflow

### 1. Classify the request

Decide which bucket the question belongs to before searching:

- Getting started and core concepts
- Creating and deploying functions (zip and container image)
- Runtimes, layers, and handler models
- Configuration: memory, timeout, environment, and architecture
- Triggers, event sources, and asynchronous invocation
- Networking and VPC
- Security, IAM roles, and resource policies
- Concurrency, scaling, and performance
- Monitoring, logging, and tracing
- Advanced features (URLs, SnapStart, extensions)
- Troubleshooting and quotas

If you need a quick starting point, load `references/topic-map.md` and jump to the closest section.

### 2. Search official AWS Lambda docs first

- Treat `docs.aws.amazon.com/lambda/latest/dg` as the source of truth for AWS Lambda.
- Prefer the developer guide at <https://docs.aws.amazon.com/lambda/latest/dg/>.
- Prefer the API reference at <https://docs.aws.amazon.com/lambda/latest/api/Welcome.html> for operation-level details.
- Search with the user's exact terms plus focused Lambda phrases such as `event source mapping`, `execution role`, `provisioned concurrency`, `function URL`, `deployment package`, or `Lambda container image`.
- When multiple pages are plausible, compare 2-3 candidate pages and pick the one that most directly answers the user's question.
- For trigger behavior, open the specific event source documentation before answering from generic webhook patterns.

### 3. Open the best page before answering

- Read the most relevant page, and the exact section when practical.
- Use the topic map only to narrow the search space or surface likely starting pages.
- For API fields, open the specific Lambda API reference page when parameters matter.
- If a page appears renamed, moved, or incomplete, say that explicitly and return the nearest authoritative pages instead of guessing.

### 4. Answer with docs-grounded guidance

- Start with a direct answer in plain language.
- Include exact AWS Lambda docs links, not just the docs homepage.
- Only provide handler code, IAM policies, or CLI examples when the user asks for them or when the docs page makes an example necessary.
- Make any inference explicit. Good phrasing:
  - `According to AWS Lambda docs, ...`
  - `Inference: this likely means ...`

## Answer Shape

Use a compact structure unless the user asks for depth:

1. Direct answer
2. Relevant docs
3. Example handler, configuration, or commands, only if needed
4. Explicit inference callout, only if you had to connect multiple docs pages

Keep citations close to the claim they support.

## Search and Routing Tips

- For concept questions, prefer What is AWS Lambda? and getting started before API reference pages.
- For deployment questions, distinguish zip deployment packages from container images on ECR.
- For trigger questions, check event source mapping docs for polling vs push models.
- For VPC questions, check VPC networking and ENI documentation before recommending security group changes alone.
- For permission errors, check execution role and resource-based policy docs together.
- For performance questions, distinguish cold start, init duration, and provisioned concurrency.
- For CLI syntax-only questions, cross-check `aws-cli-docs` for `aws lambda` commands.

## Common Mistakes

- Answering from memory without verifying the current AWS Lambda docs
- Linking the Lambda landing page when a narrower developer guide or API page exists
- Confusing execution role permissions with resource-based policies on the function
- Ignoring runtime-specific handler signatures and deprecation timelines
- Treating SQS event source mapping batching semantics as standard HTTP request handling
- Recommending always-on VPC attachment without noting cold start and ENI impacts documented by AWS
- Mixing Lambda container image limits with arbitrary Docker image assumptions

## Bundled Reference

Read `references/topic-map.md` only as a compact index of likely doc entry points. It is intentionally incomplete and should never replace the live AWS Lambda docs as the final authority.
