# Copyright 2025-2026 Cognizant Technology Solutions
"""Resolution & Runbook Tool - Finds matching runbooks and recommends remediation."""

from typing import Any, Dict


class ResolutionRunbookTool:
    """Coded tool that provides synthetic runbook and remediation data."""

    # Synthetic runbook database
    RUNBOOKS = {
        "firewall": {
            "runbook_id": "RB-NET-042",
            "runbook_name": "Firewall Rule Rollback Procedure",
            "steps": "1.Identify changed rule via change log|2.Validate rollback won't break other flows|3.Execute rollback in staging first|4.Apply to production with approval|5.Validate with synthetic transactions|6.Monitor for 15min stability",
            "risk_level": "Medium",
            "approval_required": "Yes - Change Advisory Board or Incident Commander",
            "estimated_time": "15-25 minutes",
            "validation": "Run synthetic payment transaction end-to-end|Check latency returns below 200ms|Confirm zero connection resets for 10min",
            "rollback_plan": "Re-apply original firewall rule if rollback causes issues",
        },
        "database": {
            "runbook_id": "RB-DB-019",
            "runbook_name": "Database Connection Pool Recovery",
            "steps": "1.Kill long-running queries|2.Restart connection pool|3.Scale up pool size|4.Clear application connection cache|5.Validate response times",
            "risk_level": "Low",
            "approval_required": "No - standard recovery procedure",
            "estimated_time": "5-10 minutes",
            "validation": "Connection pool utilization below 70%|Query response time normal|No new timeouts",
            "rollback_plan": "Restart application pods if pool restart fails",
        },
        "default": {
            "runbook_id": "RB-GEN-001",
            "runbook_name": "Generic Service Recovery Procedure",
            "steps": "1.Identify and revert recent change|2.Restart affected service|3.Clear caches|4.Validate service health|5.Monitor",
            "risk_level": "Medium",
            "approval_required": "Yes - for production changes",
            "estimated_time": "20-30 minutes",
            "validation": "Service health check passes|Error rate returns to baseline|SLA metrics recovering",
            "rollback_plan": "Escalate to platform team if standard recovery fails",
        },
    }

    def get_function_name(self) -> str:
        return "ResolutionRunbookTool"

    def get_function_description(self) -> str:
        return "Returns matching runbook, remediation steps, risk level, and approval requirements."

    def invoke(self, args: Dict[str, Any], _sly_data: Any = None) -> str:
        service = args.get("service", "unknown")
        root_cause = args.get("root_cause", "").lower()

        # Match runbook
        data = None
        for key in self.RUNBOOKS:
            if key in root_cause:
                data = self.RUNBOOKS[key]
                break
        if not data:
            data = self.RUNBOOKS["default"]

        return (
            f"RESOLUTION|service:{service}"
            f"|runbook:{data['runbook_id']} - {data['runbook_name']}"
            f"|steps:{data['steps']}"
            f"|risk_level:{data['risk_level']}"
            f"|approval_required:{data['approval_required']}"
            f"|estimated_time:{data['estimated_time']}"
            f"|validation:{data['validation']}"
            f"|rollback:{data['rollback_plan']}"
        )
