from __future__ import annotations

import os
from typing import Any, Dict

from ._common import with_meta

PROJECT_REPO = "https://github.com/FINNGEN/ROMOPAPI"
PROJECT_LABEL = "ROMOPAPI"


def register(mcp: object) -> None:
    @mcp.tool(name="finngen_romopapi_catalog")
    def finngen_romopapi_catalog() -> Dict[str, Any]:
        payload = {
            "project": "finngen_romopapi",
            "label": PROJECT_LABEL,
            "repository": PROJECT_REPO,
            "workspace": "omop-query-canvas",
            "enabled": True,
            "configured": bool(
                os.getenv("FINNGEN_ROMOPAPI_BASE_URL")
                or os.getenv("FINNGEN_ROMOPAPI_COMMAND")
            ),
            "operations": [
                "browse_schema",
                "preview_query_contract",
                "inspect_metadata",
                "trace_lineage_plan",
            ],
            "visualizations": [
                "schema_graph",
                "query_canvas",
                "lineage_panel",
                "result_profile_grid",
            ],
        }
        return with_meta(payload, "finngen_romopapi_catalog")

    return None
