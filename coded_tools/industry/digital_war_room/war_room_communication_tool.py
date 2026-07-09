# Copyright 2025-2026 Cognizant Technology Solutions
"""War Room Communication & RCA Tool - Generates stakeholder communication and RCA artifacts."""

from typing import Any, Dict
from datetime import datetime


class WarRoomCommunicationTool:
    """Coded tool that generates synthetic war-room communications and RCA documentation."""

    def get_function_name(self) -> str:
        return "WarRoomCommunicationTool"

    def get_function_description(self) -> str:
        return "Returns war-room communication artifacts, executive updates, and RCA documentation."

    def invoke(self, args: Dict[str, Any], _sly_data: Any = None) -> str:
        service = args.get("service", "Unknown Service")
        severity = args.get("severity", "P1")
        root_cause = args.get("root_cause", "Under investigation")
        resolution = args.get("resolution", "Remediation in progress")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M UTC")

        war_room_note = (
            f"{severity} War Room Active|Service: {service}|"
            f"Status: Remediation in progress|"
            f"Root Cause: {root_cause}|"
            f"Next Update: 15 minutes"
        )

        exec_summary = (
            f"Production impact to {service} identified at {timestamp}. "
            f"Root cause isolated to {root_cause}. "
            f"Remediation underway with expected resolution in 15-25 minutes. "
            f"Customer impact being monitored."
        )

        sme_roles = "Network Engineer (firewall rollback)|Payment SME (transaction validation)|SRE Lead (monitoring)|Incident Manager (coordination)"

        timeline = (
            "14:32-Alert triggered|14:34-War room opened|"
            "14:38-Impact assessed|14:42-Root cause identified|"
            "14:45-Remediation initiated|14:50-Pending approval"
        )

        preventive_actions = (
            "1.Implement pre-change validation for firewall rules affecting payment paths|"
            "2.Add automated canary test post-network-change|"
            "3.Enhance monitoring with payment-flow-specific latency alerts|"
            "4.Update change management process with blast-radius assessment"
        )

        return (
            f"WAR_ROOM_COMMS|timestamp:{timestamp}"
            f"|war_room_note:{war_room_note}"
            f"|executive_summary:{exec_summary}"
            f"|sme_roles_needed:{sme_roles}"
            f"|incident_timeline:{timeline}"
            f"|preventive_actions:{preventive_actions}"
            f"|rca_status:Draft RCA generated - pending final review"
        )
