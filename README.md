# agents-skills

[Agent Skills](https://skills.sh/) for coding agents. Each skill is a folder with a `SKILL.md` file that teaches the agent how to answer questions using official documentation.

## Available skills

| Skill                | Description                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------- |
| `postgresql-16-docs` | Docs-grounded answers for [PostgreSQL 16](https://www.postgresql.org/docs/16/index.html)                |
| `postgresql-17-docs` | Docs-grounded answers for [PostgreSQL 17](https://www.postgresql.org/docs/17/index.html)                |
| `postgresql-18-docs` | Docs-grounded answers for [PostgreSQL 18](https://www.postgresql.org/docs/18/index.html)                |
| `nestjs-docs`        | Docs-grounded answers for [NestJS](https://docs.nestjs.com/)                                            |
| `fastify-docs`       | Docs-grounded answers for [Fastify](https://fastify.dev/docs/latest/)                                   |
| `expressjs-docs`     | Docs-grounded answers for [Express.js](https://expressjs.com/en/)                                       |
| `redis-docs`         | Docs-grounded answers for [Redis](https://redis.io/docs/latest/)                                        |
| `kafka-docs`         | Docs-grounded answers for [Apache Kafka 4.3](https://kafka.apache.org/43/getting-started/introduction/) |
| `aws-cli-docs`       | Docs-grounded answers for the [AWS CLI](https://docs.aws.amazon.com/cli/)                               |
| `aws-s3-docs`        | Docs-grounded answers for [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/)           |
| `aws-eks-docs`       | Docs-grounded answers for [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/)               |
| `aws-ecs-docs`       | Docs-grounded answers for [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/)    |
| `aws-lambda-docs`    | Docs-grounded answers for [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/)                   |
| `aws-iam-docs`       | Docs-grounded answers for [AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/)                  |
| `docker-docs`        | Docs-grounded answers for [Docker](https://docs.docker.com/reference/)                                  |
| `kubernetes-docs`    | Docs-grounded answers for [Kubernetes](https://kubernetes.io/docs/home/)                                |
| `terraform-docs`     | Docs-grounded answers for [Terraform](https://developer.hashicorp.com/terraform/docs)                   |
| `helm-docs`          | Docs-grounded answers for [Helm](https://helm.sh/docs/)                                                 |
| `rabbitmq-docs`      | Docs-grounded answers for [RabbitMQ](https://www.rabbitmq.com/docs)                                     |
| `opentelemetry-docs` | Docs-grounded answers for [OpenTelemetry](https://opentelemetry.io/docs/)                               |
| `bullmq-docs`        | Docs-grounded answers for [BullMQ](https://docs.bullmq.io/)                                             |
| `grafana-docs`       | Docs-grounded answers for [Grafana Labs](https://grafana.com/docs/)                                     |
| `mongodb-docs`       | Docs-grounded answers for [MongoDB](https://www.mongodb.com/docs/)                                      |
| `nginx-docs`         | Docs-grounded answers for [NGINX](https://nginx.org/en/docs/)                                           |

## Install with Skills CLI

The easiest way is the [Skills CLI](https://skills.sh/):

```bash
# Install one skill globally (available in all projects)
npx skills add cookieMonsterDev/agents-skills@postgresql-18-docs -g -y

# Install all skills from this repo
npx skills add cookieMonsterDev/agents-skills --all -g -y

# Install into the current project only
npx skills add cookieMonsterDev/agents-skills@postgresql-17-docs -y

# List skills in this repo without installing
npx skills add cookieMonsterDev/agents-skills -l
```

From a local clone:

```bash
git clone git@github.com:cookieMonsterDev/agents-skills.git
cd agents-skills
npx skills add .@postgresql-16-docs -g -y
```

Other useful commands:

```bash
npx skills list          # show installed skills
npx skills update        # update installed skills
npx skills remove <name> # remove a skill
```

## Manual install

Copy or symlink a skill folder into one of these locations:

| Scope                 | Path                             |
| --------------------- | -------------------------------- |
| Global (all projects) | `~/.cursor/skills/<skill-name>/` |
| Project only          | `.cursor/skills/<skill-name>/`   |
| Project (alternative) | `.agents/<skill-name>/`          |

Example:

```bash
ln -s ~/Projects/personal/agents-skills/postgresql-18-docs ~/.cursor/skills/postgresql-18-docs
```

Each skill needs at least:

```
postgresql-18-docs/
├── SKILL.md
└── references/
    └── topic-map.md
```

## How it works

When a skill is installed, the agent can load it for matching questions. Each docs skill:

1. Routes the question to the right docs section
2. Searches the official documentation for that framework or product
3. Answers with direct links to the authoritative docs pages

Pick the skill that matches your stack. For PostgreSQL, use the skill that matches your major version — check `SELECT version();` or your deployment docs if unsure.
