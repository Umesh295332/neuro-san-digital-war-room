# Copyright 2025-2026 Cognizant Technology Solutions
"""Impact & Dependency Analysis Tool - Returns blast-radius and business impact data."""

from typing import Any, Dict


class ImpactAnalysisTool:
    """Coded tool that provides synthetic impact and dependency data for incidents."""

    # Synthetic service dependency map
    DEPENDENCY_MAP = {
        "payment gateway": {
            "direct_dependencies": ["Card Processing Engine", "Fraud Detection Service", "Transaction DB"],
            "downstream_services": ["Mobile Banking Payments", "ACH Processing", "Bill Pay", "Notification Service"],
            "business_functions": ["Real-time Payments", "Merchant Settlements", "Customer Refunds"],
            "user_impact": "~45,000 active users, ~$2.3M transactions/hour at risk",
            "sla_breach": "99.95% SLA - breach in 12 minutes if unresolved",
        },
        "authentication service": {
            "direct_dependencies": ["LDAP Directory", "MFA Provider", "Session Store"],
            "downstream_services": ["All Customer-Facing Apps", "Internal Tools", "API Gateway"],
            "business_functions": ["Customer Login", "Employee Access", "API Authentication"],
            "user_impact": "~120,000 active sessions, all logins blocked",
            "sla_breach": "99.99% SLA - already breached",
        },
        "default": {
            "direct_dependencies": ["Core Database", "Message Queue", "Cache Layer"],
            "downstream_services": ["Dependent Service A", "Dependent Service B"],
            "business_functions": ["Primary Business Function", "Secondary Function"],
            "user_impact": "~10,000 users potentially affected",
            "sla_breach": "SLA at risk within 30 minutes",
        },
    }

    def get_function_name(self) -> str:
        return "ImpactAnalysisTool"

    def get_function_description(self) -> str:
        return "Returns blast-radius and business impact data for an incident."

    def invoke(self, args: Dict[str, Any], _sly_data: Any = None) -> str:
        service = args.get("service", "unknown").lower()
        symptom = args.get("symptom", "degradation")

        # Match service to dependency map
        data = None
        for key in self.DEPENDENCY_MAP:
            if key in service:
                data = self.DEPENDENCY_MAP[key]
                break
        if not data:
            data = self.DEPENDENCY_MAP["default"]

        # Compact pipe-delimited output
        deps = ",".join(data["direct_dependencies"])
        downstream = ",".join(data["downstream_services"])
        biz = ",".join(data["business_functions"])

        return (
            f"IMPACT_ANALYSIS|service:{service}|symptom:{symptom}"
            f"|direct_deps:{deps}"
            f"|downstream:{downstream}"
            f"|business_functions:{biz}"
            f"|user_impact:{data['user_impact']}"
            f"|sla_status:{data['sla_breach']}"
            f"|severity_recommendation:P1-Critical"
        )
