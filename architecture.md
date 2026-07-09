# Architecture: NeuroSAN Digital War Room Commander

## System Context

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXTERNAL SYSTEMS (Simulated)                   │
│  Splunk/ELK │ ServiceNow CMDB │ Dynatrace APM │ Confluence     │
└──────────────────────────────────┬──────────────────────────────┘
                                   │ (Synthetic data in coded tools)
                                   ▼
┌─────────────────────────────────────────────────────────────────┐
│                     NEURO SAN RUNTIME                            │
│                                                                  │
│   LLM: gpt-4o-mini │ OpenAI-compatible API                     │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │            DIGITAL WAR ROOM AGENT NETWORK                 │  │
│   │                                                           │  │
│   │   ┌─────────────────────────────────────────────────┐    │  │
│   │   │     1. INCIDENT COMMANDER (Orchestrator)         │    │  │
│   │   └──────┬──────────┬─────────────┬────────────┬────┘    │  │
│   │          │          │             │            │          │  │
│   │          ▼          ▼             ▼            ▼          │  │
│   │   ┌──────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐   │  │
│   │   │2. IMPACT │ │ 3. RCA  │ │4. RESOL. │ │ 5. COMMS │   │  │
│   │   │  AGENT   │ │  AGENT  │ │  AGENT   │ │  AGENT   │   │  │
│   │   └────┬─────┘ └────┬────┘ └────┬─────┘ └────┬─────┘   │  │
│   │        │             │           │            │          │  │
│   │        ▼             ▼           ▼            ▼          │  │
│   │   ┌──────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐   │  │
│   │   │ Impact   │ │  RCA    │ │ Runbook  │ │ WarRoom  │   │  │
│   │   │  Tool    │ │  Tool   │ │  Tool    │ │  Tool    │   │  │
│   │   └──────────┘ └─────────┘ └──────────┘ └──────────┘   │  │
│   │                                                           │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Agent Responsibilities

| # | Agent | Input | Output | Tool |
|---|-------|-------|--------|------|
| 1 | IncidentCommanderAgent | Alert payload | Severity classification + consolidated summary | None (orchestrator) |
| 2 | ImpactDependencyAgent | service, symptom | Blast radius, business impact, SLA status | ImpactAnalysisTool |
| 3 | RCAIntelligenceAgent | service, symptom, recent_change | Root cause hypotheses with confidence | RCAIntelligenceTool |
| 4 | ResolutionRunbookAgent | service, root_cause | Runbook, steps, risk, approval gate | ResolutionRunbookTool |
| 5 | WarRoomCommunicationAgent | service, severity, root_cause, resolution | Comms, exec update, SME roles, RCA | WarRoomCommunicationTool |

## Execution Flow

```
Phase 0: User submits incident alert
    │
Phase 1: Commander classifies severity (P1/P2/P3)
    │
Phase 2: Impact Agent → ImpactAnalysisTool
    │     Returns: dependencies, downstream, SLA breach countdown
    │
Phase 3: RCA Agent → RCAIntelligenceTool
    │     Returns: ranked hypotheses, confidence %, evidence
    │
Phase 4: Resolution Agent → ResolutionRunbookTool
    │     Returns: runbook match, steps, risk level, approval gate
    │
Phase 5: Communication Agent → WarRoomCommunicationTool
    │     Returns: war-room note, exec summary, SME roles, preventive actions
    │
Phase 6: Commander consolidates → Final Incident Command Summary
```

## Data Architecture

### Tool Output Format
Pipe-delimited compact strings for structured data exchange:
```
SECTION|key1:value1|key2:value2|key3:val_a,val_b,val_c
```

### Synthetic Data Coverage

| Tool | Scenarios |
|------|-----------|
| ImpactAnalysisTool | Payment Gateway, Authentication Service, Default |
| RCAIntelligenceTool | Firewall change, Timeout/DB, Default |
| ResolutionRunbookTool | Firewall rollback, DB recovery, Generic |
| WarRoomCommunicationTool | Dynamic (builds from inputs) |

## Technology Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Architecture | Commander Pattern (not AAOSA) | Deterministic flow, predictable execution, demo-clear |
| LLM | gpt-4o-mini | Fast, cost-effective, capable of tool-calling |
| Data | Synthetic (hardcoded) | No external dependencies, instant response |
| Output format | Pipe-delimited | Compact structured data exchange between agents |

## Security

- API key: Managed via environment variables or HOCON config
- Data: 100% synthetic — no real customer/incident data
- SSL: `truststore` package handles corporate proxy cert verification
