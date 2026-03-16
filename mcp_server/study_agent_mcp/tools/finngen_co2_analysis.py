from __future__ import annotations

import os
from typing import Any, Dict

from ._common import with_meta

PROJECT_REPO = "https://github.com/FINNGEN/CO2AnalysisModules"
PROJECT_LABEL = "CO2AnalysisModules"


def register(mcp: object) -> None:
    @mcp.tool(name="finngen_co2_analysis_catalog")
    def finngen_co2_analysis_catalog() -> Dict[str, Any]:
        payload = {
            "project": "finngen_co2_analysis",
            "label": PROJECT_LABEL,
            "repository": PROJECT_REPO,
            "workspace": "analysis-gallery",
            "enabled": True,
            "configured": bool(
                os.getenv("FINNGEN_CO2_ANALYSIS_BASE_URL")
                or os.getenv("FINNGEN_CO2_ANALYSIS_COMMAND")
            ),
            "operations": [
                "list_analysis_modules",
                "preview_module_inputs",
                "run_analysis_job",
                "inspect_result_package",
            ],
            "visualizations": [
                "forest_plot",
                "heatmap_matrix",
                "execution_timeline",
                "covariate_balance_panel",
            ],
        }
        return with_meta(payload, "finngen_co2_analysis_catalog")

    return None
