# Copyright 2025-2026 Cognizant Technology Solutions
"""RCA Intelligence Tool - Correlates data to generate root cause hypotheses."""

from typing import Any, Dict


class RCAIntelligenceTool:
    """Coded tool that provides synthetic root cause analysis data."""

    # Synthetic RCA knowledge base
    RCA_PATTERNS = {
        "firewall": {
            "hypothesis_1": "Firewall rule change blocking outbound payment traffic on port 443",
            "confidence_1": 92,
            "evidence_1": "Timing correlation: rule change at 14:32, first timeout at 14:34|Connection resets on egress to payment processor|No application code deployments in 48h",
            "hypothesis_2": "Network ACL misconfiguration on payment VLAN",
            "confidence_2": 45,
            "evidence_2": "Similar pattern in INC-2024-0891|Network team had maintenance window",
        },
        "timeout": {
            "hypothesis_1": "Database connection pool exhaustion causing cascading timeouts",
            "confidence_1": 78,
            "evidence_1": "Connection pool at 98% capacity|Slow query spike at 14:30|GC pause detected",
            "hypothesis_2": "Upstream dependency latency propagation",
            "confidence_2": 55,
            "evidence_2": "Latency spike in dependent service|Circuit breaker not triggered",
        },
        "default": {
            "hypothesis_1": "Recent configuration change impacting service connectivity",
            "confidence_1": 75,
            "evidence_1": "Change detected in deployment window|Error rate spike correlated with change|No prior incidents on this path",
            "hypothesis_2": "Infrastructure capacity issue under peak load",
            "confidence_2": 40,
            "evidence_2": "CPU at 85%|Memory pressure detected",
        },
    }

    def get_function_name(self) -> str:
        return "RCAIntelligenceTool"

    def get_function_description(self) -> str:
        return "Returns root cause analysis data including hypotheses, confidence, and evidence."

    def invoke(self, args: Dict[str, Any], _sly_data: Any = None) -> str:
        service = args.get("service", "unknown")
        symptom = args.get("symptom", "")
        recent_change = args.get("recent_change", "")

        # Match pattern
        context = f"{symptom} {recent_change}".lower()
        data = None
        for key in self.RCA_PATTERNS:
            if key in context:
                data = self.RCA_PATTERNS[key]
                break
        if not data:
            data = self.RCA_PATTERNS["default"]

        return (
            f"RCA_ANALYSIS|service:{service}"
            f"|hypothesis_1:{data['hypothesis_1']}"
            f"|confidence_1:{data['confidence_1']}%"
            f"|evidence_1:{data['evidence_1']}"
            f"|hypothesis_2:{data['hypothesis_2']}"
            f"|confidence_2:{data['confidence_2']}%"
            f"|evidence_2:{data['evidence_2']}"
            f"|log_correlation:14:32-14:35 error spike 340%"
            f"|change_window:Last change {recent_change or 'unknown'} at 14:32 UTC"
        )
