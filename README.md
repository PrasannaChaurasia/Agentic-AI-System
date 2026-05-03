# Urban Matrix Agentic AI OS

<p align="center">
  <img src="assets/urban-matrix-hero.svg" alt="Urban Matrix Agentic AI OS dashboard concept" width="100%">
</p>

<p align="center">
  <strong>A cloud + local hybrid multi-agent command platform for architecture, BIM, computational design, research, visualisation, automation, and project delivery.</strong>
</p>

<p align="center">
  <a href="#english">English</a> |
  <a href="#हिन्दी">हिन्दी</a> |
  <a href="#español">Español</a> |
  <a href="#français">Français</a> |
  <a href="#العربية">العربية</a>
</p>

<p align="center">
  <img alt="Phase" src="https://img.shields.io/badge/phase-v0.1%20local%20starter-2dd4bf">
  <img alt="Stack" src="https://img.shields.io/badge/stack-Python%20%7C%20FastAPI%20ready%20%7C%20Agents-f59e0b">
  <img alt="Safety" src="https://img.shields.io/badge/safety-human%20approval%20gates-111827">
  <img alt="Mode" src="https://img.shields.io/badge/mode-cloud%20%2B%20local%20hybrid-64748b">
</p>

## English

Urban Matrix Agentic AI OS is the foundation for a professional design operations platform: one command centre, one master orchestrator, and a controlled team of specialist AI agents for architecture, BIM, site analysis, prompt generation, research, rendering, BOQ, portfolio boards, communication, code, deployment, and QA.

The current build proves the first working pattern:

```text
Project brief -> Prompt Generator Agent -> structured JSON -> Markdown prompt package -> local output archive
```

## Command Centre Vision

| Area | Purpose |
| --- | --- |
| Global Command Bar | Type any instruction for the Master Orchestrator |
| Active Projects | Track architecture, BIM, AI design, and delivery work |
| Agent Status | See which specialist agents are online, idle, running, or blocked |
| Approval Queue | Review risky scripts, emails, publishes, file edits, and BIM actions |
| Recent Outputs | Browse prompts, reports, boards, renders, code, and exports |
| System Health | Monitor cloud worker, local worker, API usage, queue, and logs |
| Quick Launch | Start Site Analysis, Prompt Generator, BOQ, Revit Check, Portfolio Board |

## Agentic Architecture

```mermaid
flowchart TB
    User["Founder / Design Lead / Project Team"] --> UI["Urban Matrix Command Centre"]
    UI --> Master["Agent 00: Master Orchestrator"]
    Master --> A1["Agent 01: Prompt Generator"]
    Master --> A2["Agent 02: Site Analysis"]
    Master --> A3["Agent 03: Research & Extraction"]
    Master --> A8["Agent 08: BIM / Revit"]
    Master --> A10["Agent 10: BOQ / Cost"]
    Master --> A11["Agent 11: Portfolio Board"]
    Master --> A17["Agent 17: QA / Reviewer"]
    A17 --> Gate["Human Approval Gate"]
    Gate --> Output["Reports / Prompts / Boards / Logs / Files"]
```

## Specialist Agent Map

| ID | Agent | Primary Value | Risk Level |
| --- | --- | --- | --- |
| 00 | Master Orchestrator | Routes goals, plans workflows, manages approvals | Medium |
| 01 | Prompt Generator | Creates structured architectural prompts | Low |
| 02 | Site Analysis | Extracts urban, climate, planning, and site drivers | Medium |
| 03 | Research & Extraction | Summarises URLs, PDFs, reports, and sources | Medium |
| 04 | Codes & Compliance | Supports standards and compliance research | High |
| 05 | Concept Development | Converts briefs into narratives and spatial strategies | Low |
| 06 | Visual Rendering | Builds shot lists, render prompts, camera and lighting direction | Low |
| 07 | ComfyUI Workflow | Plans workflow JSON and image-generation pipelines | Medium |
| 08 | BIM / Revit | Supports documentation, schedules, model checks, script planning | Critical |
| 09 | Rhino / Grasshopper | Plans parametric geometry and computational workflows | High |
| 10 | BOQ / Cost Planning | Produces early quantity and cost assumption structures | Medium |
| 11 | Portfolio Board | Plans A1/A2 boards, layouts, captions, and visual hierarchy | Low |
| 12 | AI Media | Creates video, storyboard, voiceover, and motion prompts | Medium |
| 13 | Communication | Drafts client updates, emails, Slack, and Telegram messages | High |
| 14 | Daily Operations | Summaries, priorities, reminders, and personal operations | Medium |
| 15 | GitHub / Code / Deployment | Repo, CI, deployment, README, and issue workflows | High |
| 16 | AI Tool Intelligence | Tracks AI tools, APIs, MCP servers, pricing, and relevance | Medium |
| 17 | QA / Reviewer | Checks schema, citations, hallucinations, missing fields, safety | Medium |

## v0.1 Working Build

The first implemented agent is:

```text
Agent 01 — Urban Matrix Prompt Generator Agent
```

It accepts a structured project input and creates:

- JSON output
- Markdown prompt package
- negative prompt
- camera direction
- lighting direction
- consistency lock
- next-step checklist

Run it locally:

```powershell
python agents/prompt_generator_agent.py
```

Expected output:

```text
outputs/flux_pavilion_prompt_package.json
outputs/flux_pavilion_prompt_package.md
```

## Repository Structure

```text
Agentic AI System/
├── agents/
│   └── prompt_generator_agent.py
├── assets/
│   └── urban-matrix-hero.svg
├── docs/
│   ├── citations.md
│   ├── contributing.md
│   ├── recovery.md
│   └── system_architecture.md
├── examples/
│   └── flux_pavilion_input.json
├── outputs/
│   └── .gitkeep
├── skills/
│   └── urban_matrix_prompt_generator.md
├── tools/
│   └── markdown_writer.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Product Roadmap

| Phase | Build | Outcome |
| --- | --- | --- |
| 0 | Learning foundation | Run one local AI script |
| 1 | Prompt Generator Agent | Structured prompt + Markdown export |
| 2 | Local dashboard | Browser UI with form, preview, save, task history |
| 3 | Site + Research agents | Prompt + site + source-backed research workflow |
| 4 | Database + queue | Task status, logs, agent events, running/completed states |
| 5 | Cloud deployment | Dashboard and cloud agents run while laptop is off |
| 6 | Local worker | Revit, Rhino, ComfyUI, and local folder tasks run when PC is on |
| 7 | Advanced agents | BIM, ComfyUI, BOQ, Portfolio, Code, Reviewer system |

## Safety And Governance

| Risk | Example | Rule |
| --- | --- | --- |
| Low | Generate prompt, summarise note | Can run automatically |
| Medium | Write file, update Notion, create issue | Log and review when needed |
| High | Send email, publish, run script | Approval required |
| Critical | Delete files, edit Revit model, payment, production DB edit | Always approval + backup |

Core safety rules:

- Never hard-code keys.
- Never commit `.env`.
- Use read-only tokens first.
- Keep local workers behind outbound polling.
- Require approval for send, delete, publish, payment, and live BIM edits.
- Log every agent action with task ID, risk level, tool call, status, and output path.

## Persistence And Recovery

Persistence is a first-class requirement, not an afterthought.

- GitHub stores code, docs, skills, examples, and version history.
- `outputs/` stores generated packages during local development.
- Future PostgreSQL/Neon stores tasks, logs, approvals, and project records.
- Future Drive/S3/R2 stores large files, PDFs, boards, renders, and exports.
- Future vector memory can be rebuilt from approved source documents and outputs.

More detail: [docs/recovery.md](docs/recovery.md)

## Contributing

Contributions should improve the system without weakening safety. Good contribution areas include agents, skill files, dashboard UX, examples, tests, docs, and deployment workflows.

Read: [docs/contributing.md](docs/contributing.md)

## Citations

This project is based on documented patterns from OpenAI Agents, structured outputs, MCP, LangGraph, CrewAI, Autodesk Platform Services, Revit API, ComfyUI workflow JSON, and related official resources.

Full citation list: [docs/citations.md](docs/citations.md)

## हिन्दी

Urban Matrix Agentic AI OS एक hybrid cloud + local multi-agent command platform है, जो architecture, BIM, research, rendering, prompts, BOQ, portfolio boards और project delivery के लिए बनाया गया है।

## Español

Urban Matrix Agentic AI OS es una plataforma híbrida cloud + local para coordinar agentes especializados de arquitectura, BIM, investigación, visualización, costes, comunicación y entrega de proyectos.

## Français

Urban Matrix Agentic AI OS est une plateforme hybride cloud + locale pour piloter des agents spécialisés en architecture, BIM, recherche, visualisation, estimation, communication et livraison de projet.

## العربية

Urban Matrix Agentic AI OS هو نظام هجين بين السحابة والجهاز المحلي لإدارة وكلاء ذكاء اصطناعي متخصصين في العمارة وBIM والبحث والتصور والتكلفة والتسليم.

