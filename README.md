# NeuroSAN Digital War Room Commander

## 5-Agent Autonomous Incident Command Network for Enterprise Production Outage Response

### What Is It?

A multi-agent AI system built on [Neuro SAN Studio](https://github.com/cognizant-ai-lab/neuro-san-studio) that autonomously manages production incidents through five specialized agents working in concert — from alert detection to RCA documentation.

### Key Capabilities

| Capability | Description |
|-----------|-------------|
| **Incident Classification** | Auto-classifies P1/P2/P3 severity from alert context |
| **Blast Radius Analysis** | Maps impacted services, business functions, and SLA exposure |
| **Root Cause Analysis** | Correlates logs, changes, and history to produce ranked hypotheses |
| **Safe Remediation** | Recommends runbook-based fixes with risk assessment and approval gates |
| **War Room Communication** | Generates multi-audience updates: engineering, executive, and RCA docs |

### Architecture

```
User Alert → Incident Commander Agent
                 ├→ Impact & Dependency Agent    → ImpactAnalysisTool
                 ├→ RCA Intelligence Agent       → RCAIntelligenceTool
                 ├→ Resolution & Runbook Agent   → ResolutionRunbookTool
                 └→ War Room Communication Agent → WarRoomCommunicationTool
```

### Quick Start

```powershell
# Set environment
$env:PYTHONPATH = "C:\NSAN\neuro-san-studio"
$env:AGENT_MANIFEST_FILE = "C:\NSAN\neuro-san-studio\registries\manifest.hocon"
$env:AGENT_TOOL_PATH = "C:\NSAN\neuro-san-studio\coded_tools"

# Start server
python -m neuro_san_studio run

# Open nsflow UI
# http://localhost:4173 → select "digital_war_room"
```

### Demo Input

```
Payment API latency above threshold. Service: Payment Gateway.
Symptom: Transaction timeout. Recent change: Firewall rule modified. Severity: High.
```

### Expected Output

- **Severity**: P1 — ~$2.3M/hour at risk, 45,000 users affected
- **Root Cause**: Firewall rule change blocking outbound payment traffic (92% confidence)
- **Remediation**: Rollback firewall rule (RB-NET-042) — approval required
- **Communication**: War-room note, executive update, SME routing, preventive actions

### Technology Stack

| Component | Technology |
|-----------|-----------|
| Framework | Neuro SAN Studio (Python ≥3.10) |
| LLM | gpt-4o-mini (OpenAI-compatible) |
| Config | HOCON agent network definition |
| Tools | Python coded tools with synthetic enterprise data |

### File Structure

```
registries/industry/digital_war_room.hocon          ← Agent network config
coded_tools/industry/digital_war_room/
├── __init__.py
├── impact_analysis_tool.py                         ← Blast-radius data
├── rca_intelligence_tool.py                        ← Root cause hypotheses
├── resolution_runbook_tool.py                      ← Runbook matching
└── war_room_communication_tool.py                  ← Comms generation
docs/examples/industry/digital_war_room.md          ← Documentation
```

### Author

**Umesh Anjanappa** — Cognizant Technology Solutions  
Hackathon: Neuro SAN Multi-Agent Innovation Challenge 2026

### License

Apache License 2.0 — See [LICENSE.txt](../../LICENSE.txt)
