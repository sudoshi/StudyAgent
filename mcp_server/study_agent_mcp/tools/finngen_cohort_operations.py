from __future__ import annotations

import os
from typing import Any, Dict

from ._common import with_meta

PROJECT_REPO = "https://github.com/FINNGEN/CohortOperations2"
PROJECT_LABEL = "CohortOperations2"


def register(mcp: object) -> None:
    @mcp.tool(name="finngen_cohort_operations_catalog")
    def finngen_cohort_operations_catalog() -> Dict[str, Any]:
        payload = {
            "project": "finngen_cohort_operations",
            "label": PROJECT_LABEL,
            "repository": PROJECT_REPO,
            "workspace": "cohort-workbench",
            "enabled": True,
            "configured": bool(
                os.getenv("FINNGEN_COHORT_OPERATIONS_BASE_URL")
                or os.getenv("FINNGEN_COHORT_OPERATIONS_COMMAND")
            ),
            "operations": [
                "compile_cohort",
                "inspect_inclusion_flow",
                "summarize_attrition",
                "preview_export_bundle",
            ],
            "visualizations": [
                "attrition_funnel",
                "criteria_timeline",
                "cohort_overlap_map",
                "sql_artifact_panel",
            ],
        }
        return with_meta(payload, "finngen_cohort_operations_catalog")

    return None
