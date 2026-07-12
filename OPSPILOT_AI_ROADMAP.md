# OpsPilot AI — Build Roadmap

## Goal

Build a portfolio project that demonstrates AI and automation engineering skills without using company data or systems.

OpsPilot AI will be a model-independent infrastructure operations agent. It will investigate simulated incidents, use narrowly scoped tools to gather evidence, recommend remediation, request approval for controlled actions, execute approved changes, validate recovery, and create an auditable incident report.

## First complete workflow

We will build and polish one scenario before adding more integrations:

1. User reports that a demo website is unavailable.
2. Agent checks the HTTP endpoint.
3. Agent checks the Docker container.
4. Agent reads the container logs.
5. Agent identifies the likely cause.
6. Agent requests approval to restart the container.
7. User approves or rejects the action.
8. Agent restarts the demo container if approved.
9. Agent validates the endpoint.
10. Agent creates a resolution report and audit trail.

## Technology direction

- TypeScript and Node.js, managed with pnpm
- LangChain.js and Zod tool schemas
- LM Studio first; Docker Model Runner as a second provider
- Next.js dashboard later
- Docker Compose for a local infrastructure lab
- SQLite first, with PostgreSQL as an optional later upgrade
- Markdown runbooks and retrieval-augmented generation later
- Dockerized deployment and GitHub Actions later

## Phases

### Phase 0 — Project decisions and prerequisites

- [ ] Confirm Node.js, pnpm, Docker Desktop, and Git are available.
- [ ] Enable pnpm's lockfile and prefer frozen-lockfile installs in CI.
- [ ] Review dependencies with `pnpm audit` before adding packages or upgrading versions.
- [ ] Choose the first local model in LM Studio.
- [ ] Confirm the model supports reliable structured tool calling.
- [ ] Decide whether the initial project is CLI-only or includes the dashboard immediately. Recommended: CLI first.
- [ ] Create only synthetic lab data and local demo infrastructure.

### Phase 1 — Basic local agent

- [ ] Create the TypeScript project.
- [ ] Configure ES modules, environment variables, formatting, and linting.
- [ ] Connect LangChain.js to LM Studio's OpenAI-compatible API.
- [ ] Add a health-check tool.
- [ ] Add a Docker-container-status tool.
- [ ] Add a container-logs tool.
- [ ] Run the agent from the command line.
- [ ] Add timeouts, error handling, and structured tool results.

Target command:

```text
pnpm agent "Why is the demo application unavailable?"
```

### Phase 2 — Local infrastructure lab

- [ ] Create a Docker Compose environment.
- [ ] Add a healthy demo web application.
- [ ] Add a deliberately broken web application scenario.
- [ ] Add a database and log generator if useful for the demo.
- [ ] Add scripts to reproduce and reset failures.
- [ ] Keep all container names and actions on explicit allowlists.

### Phase 3 — Human approval and safety

- [ ] Classify tools as read-only, controlled, or restricted.
- [ ] Run read-only tools automatically.
- [ ] Require approval before restarting the demo container.
- [ ] Disable destructive tools initially.
- [ ] Validate all tool arguments with Zod.
- [ ] Add audit records for requests, evidence, approvals, actions, and results.

### Phase 4 — Web dashboard

- [ ] Add a Next.js and TypeScript frontend.
- [ ] Add an agent console with live progress.
- [ ] Display tool calls, arguments, results, approval requests, and conclusions.
- [ ] Add an infrastructure-lab health view.
- [ ] Add an agent-runs history page.

### Phase 5 — Runbooks and RAG

- [ ] Create fictional Markdown runbooks.
- [ ] Retrieve the relevant runbook for each incident.
- [ ] Display runbook citations in the agent response.
- [ ] Add retrieval and response evaluation cases.

### Phase 6 — Engineering quality and deployment

- [ ] Add unit tests for every tool.
- [ ] Add agent workflow tests with deterministic fixtures.
- [ ] Add retries, idempotency, and failure recovery.
- [ ] Add structured JSON logging and latency tracking.
- [ ] Add GitHub Actions, Docker image builds, and security scanning.
- [ ] Document deployment options such as Azure Container Apps.

## Initial tool catalogue

Start with these narrowly scoped tools:

- `check_http_endpoint`
- `get_container_status`
- `get_container_logs`
- `restart_demo_container`
- `create_incident_report`

Do not expose an unrestricted terminal or arbitrary command execution to the model. Prefer purpose-built tools with validated inputs and allowlists.

## Suggested repository structure

```text
opspilot-ai/
├── apps/
│   ├── web/
│   └── agent-api/
├── packages/
│   ├── agent/
│   ├── tools/
│   ├── database/
│   └── shared/
├── infrastructure/
│   └── docker/
├── knowledge/
│   └── runbooks/
├── tests/
├── docs/
├── docker-compose.yml
└── README.md
```

## Portfolio requirements

The final README should include:

- Architecture diagram
- Screenshots and a short demonstration video
- Example incident workflow
- Safety and approval model
- Tool definitions
- Evaluation results
- Local setup and deployment instructions
- Known limitations

## Working agreement for this project

We will work one phase and one small milestone at a time. After each milestone, we will run the relevant checks before continuing. No company credentials, proprietary data, internal infrastructure, or organization systems will be connected.

## Package-management policy

- Use pnpm for initialization, installation, scripts, and lockfile management.
- Commit `pnpm-lock.yaml`.
- Use `pnpm install --frozen-lockfile` for reproducible installs.
- Run `pnpm audit` and review transitive dependencies before accepting upgrades.
- Avoid installing packages that are not required for the current milestone.
- Do not use npm commands or commit `package-lock.json`.

## Current milestone

**Next step:** inspect the local development prerequisites, then create the minimal TypeScript project for Phase 1.
